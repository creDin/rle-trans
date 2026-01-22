
# Stat-ups popups / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
init python:
    def CallHolder(Value, Color, XPOS):
            global HolderCount
            HolderCount += 1 if HolderCount < 10 else -9                             #Resets holder screens when it maxes out.
#            if HolderCount == 1:
#                    #Shows the "+3" style feedback screen
#                    renpy.show_screen("StatHolder1", Value, Color, XPOS)
#            elif HolderCount == 2:
#                    renpy.show_screen("StatHolder2", Value, Color, XPOS)
#            elif HolderCount == 3:
#                    renpy.show_screen("StatHolder3", Value, Color, XPOS)
#            elif HolderCount == 4:
#                    renpy.show_screen("StatHolder4", Value, Color, XPOS)
#            elif HolderCount == 5:
#                    renpy.show_screen("StatHolder5", Value, Color, XPOS)
#            else:           #== 6:
#                    renpy.show_screen("StatHolder6", Value, Color, XPOS)
            renpy.show_screen("StatHolder"+str(HolderCount), Value, Color, XPOS)
#            HolderCount += 1 if HolderCount < 6 else -5                             #Resets holder screens when it maxes out.
            return

transform StatAnimation(Timer, XPOS):
        #this is the animation for the Stat ticker
        alpha 0
        pause Timer
        xpos XPOS ypos 0.15 alpha 1
        parallel:
            linear 1 ypos 0.0
        parallel:
            pause .3
            linear .3 alpha 0

screen StatGraphic(Value, Color, Timer, XPOS):
        #this displays the stat ticker when called
        showif Value > 0:
            text "+[Value]" size 30 color Color at StatAnimation(Timer, XPOS)
        else:
            text "[Value]" size 30 color Color at StatAnimation(Timer, XPOS)

screen StatHolder1(Value, Color, XPOS):
        #This cycles through the possible stat ticker frameworks
        use StatGraphic(Value, Color, 0.0, XPOS-30)
        timer 0.6 action Hide("StatHolder1")
screen StatHolder2(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.1, XPOS)
        timer 0.7 action Hide("StatHolder2")
screen StatHolder3(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.2, XPOS+30)
        timer 0.8 action Hide("StatHolder3")
screen StatHolder4(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.3, XPOS-30)
        timer 0.9 action Hide("StatHolder4")
screen StatHolder5(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.4, XPOS)
        timer 1.0 action Hide("StatHolder5")
screen StatHolder6(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.5, XPOS+30)
        timer 1.1 action Hide("StatHolder6")
screen StatHolder7(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.6, XPOS-30)
        timer 1.2 action Hide("StatHolder7")
screen StatHolder8(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.7, XPOS)
        timer 1.3 action Hide("StatHolder8")
screen StatHolder9(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.8, XPOS+30)
        timer 1.4 action Hide("StatHolder9")
screen StatHolder10(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.9, XPOS-30)
        timer 1.5 action Hide("StatHolder10")

# End Stat-ups popups / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

init python:
# Start Approval Check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    def ApprovalCheck(Chr = 0, T = 1000, Type = "LOI", Spread = 150, TmpM = 1, TabM = 0, C = 1, Bonus = 0, Loc = 0, Check=0, Alt=[[],0], Bias=0):
            # $ Count = ApprovalCheck(Rogue,125,"L")
            # T is the value being checked against, Type is the LOI condition in play, Spread is the difference between basic approval and high approval
            # TmpM is Tempmod multiplier, TabM is the taboo modifier, C is cologne modifiers, Bonus is a random bonus applied, and Loc is the girl's location
            #figure out a way to send a matrix variable for altering the results based on character Alt=[[RogueX,KittyX],800]

            if Chr not in TotalGirls: #should remove "character don't exist" errors
                return 0

            for x in Alt[0]:
                    #if there is an alternate character option. . .
                    if Chr in Alt[0]:
                            T = Alt[1] if Alt[1] else T

            L = Chr.Love
            O = Chr.Obed
            I = Chr.Inbt
            LocalTaboo = Chr.Taboo
            Loc = Chr.Loc if not Loc else Loc

            if Bias and not Player.Male:
                    if "girltalk" not in Chr.History and "nogirls" not in Chr.History:
                            #if you haven't talked to her about sex stuff, she is more open to some things
                            Bonus += Bias

            if Chr.Tag == "Jean" and (O <= 800 or JeanX.Taboo):
                    # Reduces effective value of Inhibition by 500 to a minimum of 0.
                    I = (I - JeanX.IX) #IX is a value of up to 500
            elif Chr.Tag == "Betsy" and Chr.Taboo:
                    #Betsy in public, higher penalty
                    LocalTaboo += 10
            elif Chr.Tag == "Wanda" and Player.Male != 1:
                    #Wanda if you're a girl
                    Bonus += 200

            if Loc == bg_current and C:
                    #Bumps stats based on colognes
                    if Chr == LauraX:
                            if "mandrill" in Player.Traits:
                                    if L <= 400:
                                        L += 600
                                    else:
                                        L = 1200
                                    if "drugged" not in Chr.Traits:
                                            Chr.Traits.append("drugged")
                            elif "purple" in Player.Traits:
                                    if O <= 400:
                                        O += 600
                                    else:
                                        O = 1200
                                    if "drugged" not in Chr.Traits:
                                            Chr.Traits.append("drugged")
                            elif "corruption" in Player.Traits:
                                    if I <= 400:
                                        I += 600
                                    else:
                                        I = 1200
                                    if "drugged" not in Chr.Traits:
                                            Chr.Traits.append("drugged")
                    else:
                            if "mandrill" in Player.Traits:
                                    if L <= 500:
                                        L += 500
                                    else:
                                        L = 1000
                            elif "purple" in Player.Traits:
                                    if O <= 500:
                                        O += 500
                                    else:
                                        O = 1000
                            elif "corruption" in Player.Traits:
                                    if I <= 500:
                                        I += 500
                                    else:
                                        I = 1000

            if Type == "LOI":
                    LocalTaboo = LocalTaboo * 10
                    LocalTempmod = Tempmod * 10

            elif Type == "LO":                      #40 -> 240
                    #culls unwanted parameters.
                    #These bits multiply everything from the 0-300 range to the 0-3000 range
                    I = 0
                    LocalTaboo = LocalTaboo * 6
                    LocalTempmod = Tempmod * 6
            elif Type == "OI":
                    L = 0
                    LocalTaboo = LocalTaboo * 6
                    LocalTempmod = Tempmod * 6
            elif Type == "LI":
                    O = 0
                    LocalTaboo = LocalTaboo * 6
                    LocalTempmod = Tempmod * 6

            elif Type == "L":                       #40 -> 120
                    O = 0
                    I = 0
                    LocalTaboo = LocalTaboo * 3
                    LocalTempmod = Tempmod * 3
            elif Type == "O":
                    L = 0
                    I = 0
                    LocalTaboo = LocalTaboo * 3
                    LocalTempmod = Tempmod * 3
            elif Type == "I":
                    O = 0
                    L = 0
                    LocalTaboo = LocalTaboo * 3
                    LocalTempmod = Tempmod * 3

            else:
                    LocalTaboo = LocalTaboo * 10         #40 -> 400
                    LocalTempmod = Tempmod * 10

            TabM = 0 if TabM <= 0 else TabM #test this, makes sure TabM is positive

#            renpy.say(None,str(L + O + I)+"B", interact=True) #fix remove

            if Check:
                    #this returns the actual value of the tested stat.
                    Check = (L + O + I + Bonus + (TmpM * LocalTempmod) - (TabM * LocalTaboo))
                    return Check

#            renpy.say(None,"A"+str(L + O + I), interact=True) #fix remove
            if (L + O + I + Bonus + (TmpM * LocalTempmod) - (TabM * LocalTaboo)) >= (T + (2 * Spread)):
                    #She passes and loves it
                    return 3
            elif (L + O + I + Bonus + (TmpM * LocalTempmod) - (TabM * LocalTaboo)) >= (T + Spread):
                    #She passes
                    return 2
            elif (L + O + I + Bonus + (TmpM * LocalTempmod) - (TabM * LocalTaboo)) >= T:
                    #She doesn't really want to, but can be convinced
                    return 1
            else:
                    return 0
# End Approval Check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Room Full / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    def Room_Full(Here = [],BO=[]):
            # Culls parties down to 2 max
            # if Room_Full(): do something to empty it.
            global Party
            Here = []
            while len(Party) > 2:
                    # If two or more members in the party
                    #Culls down party size to two
                    Party.remove(Party[2])

            # checks to see which girls are present at a given location
            # adds members who are not currently in the party

            BO = TotalGirls[:]
            for BX in BO:
                    if BX.Loc == bg_current and BX not in Party:
                                Here.append(BX)
            if len(Party) + len(Here) >= 2:
                return 1
            else:
                return 0
#end RoomFull  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# AloneCheck / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    def AloneCheck(Girl=0,BO=[]):
            # returns a positive value if alone
            # if Girl, it checks if she's the only one in the room
            BO = TotalGirls[:]
            if Girl and Girl in TotalGirls:
                    BO.remove(Girl)
            for BX in BO:
                    if BX.Loc == bg_current:
                            return 0
            return 1



# GirlCheck / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    def GirlCheck(Check=0,Local=0,BO=[]):
            #checks whether the indicated girl is available for this activity
            # $ Girl = GirlCheck(Girl,1)
            global Ch_Focus
            if Check in TotalGirls and (not Local or bg_current == Check.Loc):
                        #if the sent girl is valid and the game does not care about location
                        #or if the sent girl is valid and the girl is nearby
                        return Check
            elif bg_current == Ch_Focus.Loc:
                        #if this sent girl is in the room and focal, make her the choice.
                        return Ch_Focus
            else:
                #If the sent girl is invalid, and the focal girl is not local,
                #search all girls for one that is local, and make her the focal girl
                BO = TotalGirls[:]
                for BX in BO:
                        if bg_current == BX.Loc:
                                #if this current girl is in the room, make her the choice.
                                #renpy.call("Shift_Focus",BO[0],from_current=True)
                                Ch_Focus = BX
                                return BX
            narrator("Tell Oni, no appropriate character was found.", interact=True)
            return Ch_Focus
# End Python Init stuff/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / // / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Time and Space Stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Start Round 10 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Round10(BO=[],Occupant=0): #rkeljsvgb
        #Called when it's time to auto-wait/sleep
        if Time_Count >= 3: #night
                    call Sleepover
                    return
                    #End night time

        #if it's not night time, just wait
        if bg_current not in PersonalRooms:# and bg_current != "bg player":
                    #if you are in a public space
                    call Wait
                    return
        #else. . .

        $ BO = TotalGirls[:]
        python:
            for BX in BO:
                #sets Occupant if this is in one of the girls' rooms
                if BX.Home == bg_current:
                        Occupant = BX
                        break #$ BO = [1]

        if not Occupant:
                #if nobody was found, do this
                call Wait
                return
        #else
        if Occupant.Loc == bg_current:
                #If they are home
                if Occupant == RogueX:
                        ch_r "Конечно, ты можешь немного подождать."
                elif Occupant == KittyX:
                        ch_k "Конечно, ты можешь немного посидеть тут."
                elif Occupant == EmmaX:
                        ch_e "Ты можешь остаться нанадолго, если хочешь."
                elif Occupant == LauraX:
                        ch_l "Ты можешь остаться."
                elif Occupant == JeanX:
                        pass
                elif Occupant == StormX:
                        ch_s "Я не возражаю против твоего присутствия."
                elif Occupant == JubesX:
                        ch_v "Ага, ты можешь немного посидеть здесь."
                elif Occupant == GwenX:
                        ch_g "Хорошо, конечно."
                elif Occupant == BetsyX:
                        ch_b "Ты здесь желанный гость. . ."
                elif Occupant == DoreenX:
                        ch_d "Конечно, я тебе всегда рада. . ."
                elif Occupant == WandaX:
                        ch_w "Заходи. . ."
        else:
                #if nobody is home
                "Вы ждете, когда [Occupant.Name] вернется."

        call Wait

        call Girls_Location #new here

        if Time_Count < 3 or Occupant.Loc != bg_current:
                #if it's not nightime or the girl is not home. . .
                return

        if Occupant == JubesX or Line == "stay":
                #Jubilee doesn't sleep, so doesn't kick you out, if you argued and won in the Girls_arrive dialgoues, it skips this check
                pass
        elif Occupant.Sleep or Occupant.SEXP >= 30:
                #It's late but she really likes you
                if Occupant == RogueX:
                        ch_r "Уже довольно поздно, [RogueX.Petname], но ты можешь остаться. . ."
                elif Occupant == KittyX:
                        ch_k "Уже довольно поздно, [KittyX.Petname], но ты можешь остаться, если хочешь. . ."
                elif Occupant == EmmaX:
                        if not Player.Male:
                            ch_e "Уже довольно поздно, [EmmaX.Petname], но я бы хотела, чтобы ты осталась. . ."
                        else:
                            ch_e "Уже довольно поздно, [EmmaX.Petname], но я бы хотела, чтобы ты остался. . ."
                elif Occupant == LauraX:
                        ch_l "Я скоро пойду спать, но ты можешь остаться."
                elif Occupant == JeanX:
                        ch_j "Я собираюсь немного поспать, не хочешь присоединиться ко мне?"
                elif Occupant == StormX:
                        ch_s "Я скоро ложусь спать, не хочешь присоединиться ко мне?"
                elif Occupant == GwenX:
                        ch_g "Слушай, я скоро собираюсь в кровать."
                        ch_g "Ты со мной?"
                elif Occupant == BetsyX:
                        ch_b "Я собираюсь пойти спать, хорошо, что ты можешь составить мне компанию."
                elif Occupant == DoreenX:
                        ch_d "Уже двольно поздно, ты что-то еще хочешь?"
                elif Occupant == WandaX:
                        ch_w "Уже довольно поздно, чего ты хочешь?"

        elif ApprovalCheck(Occupant, 1000, "LI") or ApprovalCheck(Occupant, 600, "OI"):
                #It's late but she really likes you
                if Occupant == RogueX:
                        ch_r "Уже довольно поздно, [Occupant.Petname], но ты можешь ненадолго остаться."
                elif Occupant == KittyX:
                        ch_k "Уже довольно поздно, [KittyX.Petname], но ты можешь остаться ненадолго."
                elif Occupant == EmmaX:
                        ch_e "Уже довольно поздно, [EmmaX.Petname], но ты можешь остаться."
                elif Occupant == LauraX:
                        ch_l "Уже поздно, но ты можешь остаться."
                elif Occupant == JeanX:
                        ch_j "Уже поздно."
                elif Occupant == StormX:
                        ch_s "Уже довольно поздно, [StormX.Petname]."
                elif Occupant == GwenX:
                        ch_g "Уже довольно поздно. . ."
                elif Occupant == BetsyX:
                        ch_b "Я собираюсь пойти спать, но перед этим у нас есть немного времени."
                elif Occupant == DoreenX:
                        ch_d "Уже двольно поздно, ты что-то еще хочешь?"
                elif Occupant == WandaX:
                        ch_w "Уже довольно поздно, чего ты хочешь?"
        else:
                #she likes you well enough but it's late so you should go
                if Occupant == RogueX:
                        ch_r "Уже довольно поздно [Occupant.Petname]. Тебе лучше уйти."
                elif Occupant == KittyX:
                        ch_k "Уже поздно, [KittyX.Petname]. Тебе нужно идти спать."
                elif Occupant == EmmaX:
                        ch_e "Уже поздно, [EmmaX.Petname]. Мне пора спать."
                elif Occupant == LauraX:
                        if not Player.Male:
                            ch_l "Я собираюсь идти спать. Ты должна уйти."
                        else:
                            ch_l "Я собираюсь идти спать. Ты должен уйти."
                elif Occupant == JeanX:
                        ch_j "Я спать. Тебе нужно уйти."
                elif Occupant == StormX:
                        ch_s "Я скоро ложусь спать. Тебе пора идти."
                elif Occupant == GwenX:
                        ch_g "Слушай, я скоро спать, ты можешь. . . уйти?"
                elif Occupant == BetsyX:
                        ch_b "Я собираюсь пойти спать, тебе лучше уйти."
                elif Occupant == DoreenX:
                        ch_d "Уже двольно поздно, может, зайдешь утром?"
                elif Occupant == WandaX:
                        ch_w "Уже довольно поздно, увидимся завтра?"
                $ bg_current == "bg campus"
                jump Misplaced
        return
# End Round 10 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Checkout  Overrun checking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Checkout(Total = 0,BO=[]):
#        call VersionNumber

        $ BO = TotalGirls[:]
        python:
            for BX in BO:
                BX.Love = 1000 if BX.Love > 1000 else BX.Love
                BX.Obed = 1000 if BX.Obed > 1000 else BX.Obed
                BX.Inbt = 1000 if BX.Inbt > 1000 else BX.Inbt
                BX.Lust = 99 if BX.Lust > 99 else BX.Lust

                BX.Love = 0 if BX.Love < 0 else BX.Love
                BX.Obed = 0 if BX.Obed < 0 else BX.Obed
                BX.Inbt = 0 if BX.Inbt < 0 else BX.Inbt
                BX.Lust = 0 if BX.Lust < 0 else BX.Lust

                BX.Action = BX.MaxAction if BX.Action > BX.MaxAction else BX.Action
                BX.Action = 0 if BX.Action < 0 else BX.Action

                BX.Addict = 100 if BX.Addict > 100 else BX.Addict
                BX.Addict = 0 if BX.Addict < 0 else BX.Addict
                BX.Addictionrate = 10 if BX.Addictionrate > 10 else BX.Addictionrate
                BX.Addictionrate = 0 if BX.Addictionrate < 0 else BX.Addictionrate
                BX.Thirst = 100 if BX.Thirst > 100 else BX.Thirst
                BX.Thirst = 0 if BX.Thirst < 0 else BX.Thirst

                if BX.Forced and BX.ForcedCount < 10:
                            BX.ForcedCount += 1
                if BX is LauraX:
                            LauraX.ScentTimer = 0
                if Total:
                            BX.Offhand = 0
                #BX.Pose = 0        #resets pose to default
                #$ BO.remove(BO[0])

        #Player
        $ Player.Focus = 99 if Player.Focus > 99 else Player.Focus
        $ Player.Focus = 0 if Player.Focus < 0 else Player.Focus
        $ Player.Semen = Player.Semen_Max if Player.Semen > Player.Semen_Max else Player.Semen
        $ Player.Semen = 0 if Player.Semen < 0 else Player.Semen
        $ Player.Cock = "out"
        $ Speed = 0

        if Total:
                $ MultiAction = 1
                $ Player.DrainWord("cockout")
                $ Player.DrainWord("nude")
                $ Player.DrainWord("interruption")
                $ Trigger = 0
                $ Trigger2 = 0
#                $ Trigger3 = 0
#                $ Trigger4 = 0
#                $ Trigger5 = 0
                $ ThreeCount = 100
                $ Partner = 0
                $ Player.FocusX = 0
        return
#End Checkout  Overrun checking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Wait/Sleep Cycle //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #Wait
label Wait (Outfit = 1, Lights = 1, BO=[]):
    # If Outfit is 1, it changes her clothes to the scheduled default, otherwise it does not.
    # If Lights is 1, it removes the blackout screen, otherwise it does not.
    show blackscreen onlayer black

    call Checkout(1)
#    $ Player.XP = 3330 if Player.XP > 3330 else Player.XP

    if Time_Count < 3:  #not sleep time
                $ Time_Count += 1
    else:
        # Things that happen when you sleep
                $ del Party[:]

                #Setting the time/date
                $ Time_Count = 0
                $ Day += 1
                # Modification mode
                if JubesX.Delay > 0:
                    $ JubesX.Delay -= 1
                if GwenX.Delay > 0:
                    $ GwenX.Delay -= 1
                # -----------------
                if Weekday < 6:
                    $ Weekday += 1
                else:
                    $ Weekday = 0
                $ DayofWeek = Week[Weekday]

                if PunishmentX: #Event[3]:
                        #If you're under punishment
                        $ Player.Cash += int(Player.Income / 2)
                        if PunishmentX == 1:
                            "Ваше наказание от Ксавье подошло к концу."
                        $ PunishmentX -= 1
                else:
                        #otherwise, you make money
                        $ Player.Cash += Player.Income


        # Things about you when you sleep:
                $ Player.Semen = Player.Semen_Max
                $ Player.Spunk = 0
                $ Player.Rep = 0 if Player.Rep < 0 else Player.Rep
                $ Player.Rep += 10 if Player.Rep < 800 else 0
                $ Player.Rep = 1000 if Player.Rep > 1000 else Player.Rep

                $ TotalSEXP = 0 #zeros out so that next bit and add to it

                #Clearing colognes
                if "mandrill" in Player.Traits:
                        $ Player.Traits.remove("mandrill")
                if "purple" in Player.Traits:
                        $ Player.Traits.remove("purple")
                if "corruption" in Player.Traits:
                        $ Player.Traits.remove("corruption")
                call Favorite_Actions # Sets the girl's favorite activities once per day

        # Things about the girls when you sleep:

                if "halloween" in Player.DailyActions:
                        if RogueX.Hair == "cosplay":
                            if "evo" in RogueX.DailyActions:
                                $ RogueX.Hair = "evo"
                            elif "wet" in RogueX.DailyActions:
                                $ RogueX.Hair = "wet"
                        if JeanX.Hair == "pony":
                            if "short" in JeanX.DailyActions:
                                $ JeanX.Hair = "short"
                            elif "wet" in JeanX.DailyActions:
                                $ JeanX.Hair = "wet"
                        if StormX.Hair == "short":
                            if "long" in StormX.DailyActions:
                                $ StormX.Hair = "long"
                            elif "mohawk" in StormX.DailyActions:
                                $ StormX.Hair = "mohawk"
                            elif "wet" in StormX.DailyActions:
                                $ StormX.Hair = "wet"
                            elif "wethawk" in StormX.DailyActions:
                                $ StormX.Hair = "wethawk"
                        if GwenX.Hair == "pony":
                            if "short" in GwenX.DailyActions:
                                $ GwenX.Hair = "short"
                            elif "wet" in GwenX.DailyActions:
                                $ GwenX.Hair = "wet"
                        if BetsyX.Hair == "blonde":
                            if "long" in BetsyX.DailyActions:
                                $ BetsyX.Hair = "long"
                            elif "short" in BetsyX.DailyActions:
                                $ BetsyX.Hair = "short"
                            elif "wet" in BetsyX.DailyActions:
                                $ BetsyX.Hair = "wet"
                            elif "wetlong" in BetsyX.DailyActions:
                                $ BetsyX.Hair = "wetlong"
                        if WandaX.Hair == "long":
                            if "short" in WandaX.DailyActions:
                                $ WandaX.Hair = "short"
                            elif "wet" in WandaX.DailyActions:
                                $ WandaX.Hair = "wet"
                            elif "wetlong" in WandaX.DailyActions:
                                $ WandaX.Hair = "wetlong"

                $ BO = TotalGirls[:]
                python:
                    for BX in BO:
                        #loops through and makes choices.
                        if BX in ActiveGirls and BX.Loc != bg_current:
                                BX.Loc = BX.Home
                        BX.Outfit = "sleep"
                        BX.OutfitChange("sleep")
                        BX.Red = 0 #de-reds her butt

                        #Addiction
                        BX.Addict += BX.Addictionrate   #(0-10)
                        BX.Addict -= (3*BX.Resistance)  #(0,3,6, or 9)
                        if "nonaddictive" in Player.Traits:
                                    BX.Addictionrate -= 2
                                    BX.Addict -= 5
                        if "addictive" not in Player.Traits:
                                    BX.Addictionrate -= BX.Resistance
                                    if BX is not RogueX and BX.Addictionrate >= 3:
                                            # further bonus for anyone other than Rogue
                                            BX.Addictionrate -= BX.Resistance

                        BX.ForcedCount -= 1 if BX.ForcedCount > 0 else 0
                        if BX.ForcedCount > 0:
                                BX.ForcedCount -= 1 if ApprovalCheck(BX, 1000, "LO") else 0
                        BX.Action = BX.MaxAction

                        BX.Rep = 0 if BX.Rep < 0 else BX.Rep
                        BX.Rep += 10 if BX.Rep < 800 else 0
                        BX.Rep = 1000 if BX.Rep > 1000 else BX.Rep

                        BX.Lust -= 5 if BX.Lust >= 50 else 0
                        TotalSEXP += BX.SEXP #tabulates total based on combined score
                        if BX.Plug:
                                BX.Plug = 0
                                BX.Statup("Obed", 95, 2)
                                BX.Plugged += 1

                        if BX.SEXP >= 15:
                                #raises thirst if you've had sex before
                                if BX.SEXP >= 50:
                                    BX.Thirst += 8 if BX.Thirst <= 70 else 4
                                elif BX.SEXP >= 25:
                                    BX.Thirst += 5 if BX.Thirst <= 60 else 2
                                else:
                                    BX.Thirst += 3 if BX.Thirst <= 50 else 1

                                BX.Thirst -= 5 if BX.Break[0] else 0
                                BX.Thirst += 1 if BX.Lust >= 50 else 0

                        if "gonnafap" in BX.DailyActions and BX.Loc != bg_current:
                                #if it's morning and she wanted to fap yesterday, so she did. . .
                                BX.Lust = 25
                                BX.Thirst -= int(BX.Thirst/2) if BX.Thirst >= 50 else int(BX.Thirst/4)
                        elif "wannafap" in BX.DailyActions:
                                #if it's morning and she didn't get to fap yesterday. . .
                                BX.Thirst += 10 if BX.Thirst <= 50 else 5
                        if "backsy" in BX.DailyActions:
                                BX.AddWord(1,0,0,0,"backsy") #you backed out on her, add to history

                        BX.Break[0] -= 1 if BX.Break[0] > 0 else 0

                        del BX.Spunk[:]

                        if "lover" in BX.Petnames and BX.Love > 800:
                                BX.Love += 10
                        if "master" in BX.Petnames and BX.Obed > 600:
                                BX.Obed += 10
                        if "fuck buddy" in BX.Petnames:
                                BX.Inbt += 10

                        BX.SluttyClothes()   #checks to see if they want to change their default look

                        if BX.Tag == "Jean":
                                if BX.Love < 1000 and BX.StatStore > 0:
                                        #for Jean, after her obedience raises above 500, it starts filling her Love stat from her Stored stat
                                        if BX.Obed >= 900:
                                                BX.Love += 10
                                                BX.StatStore -= 10
                                        elif BX.Obed >= 700:
                                                BX.Love += 5
                                                BX.StatStore -= 5
                                        elif BX.Obed >= 500:
                                                BX.Love += 1
                                                BX.StatStore -= 1
                                if BX.Rep <= 800 and "nowhammy" not in JeanX.Traits:
                                        #she mindwipes students to reset her reputation
                                        BX.Rep = 800

                        if "Jeaned" in BX.Traits:
                                # fixes if the girl's like-stats have been whammied
                                BX.Traits.remove("Jeaned") #got whammied tag
                                BX.LikeJean = getattr(JeanX,"LikeS"+BX.Tag) #To restore to original values. . .

                        # TodoList content
                        if BX == LauraX:
                                if "pubes" in BX.Todo:
                                        BX.Pubes = 1
                                        BX.Todo.remove("pubes")

                                if "mission" in BX.Todo: #puts her on ice until a week after the first meeting
                                        BX.PubeC -= 1
                                        if BX.PubeC >= 1:
                                                BX.Loc = "hold"
                                        else:
                                                BX.History.append("dress0") #starts dress event where you'll meet again
                                                BX.Todo.remove("mission")
                                if "cleanhouse" in BX.Todo:
                                        #if you promised to break up with other girls, this counts it down
                                        if LauraX in Player.Harem or not Player.Harem:
                                                # mission complete
                                                BX.Event[5] = 2
                                                BX.Todo.remove("cleanhouse")
                                        LauraX.Event[5] -= 1 if LauraX.Event[5] > 1 else 0
                        else:
                                if "pubes" in BX.Todo:
                                        BX.PubeC -= 1
                                        if BX.PubeC >= 1:
                                                pass
                                        else:
                                                BX.Pubes = 1
                                                BX.Todo.remove("pubes")
                                if BX == BetsyX and BetsyX.Event[2]:
                                        BetsyX.Event[2] -= 1
                                if BX == DoreenX and "SGattic" in Player.History:
                                        DoreenX.Event[2] -= 1 if DoreenX.Event[2] > 0 else 0
                                elif BX == GwenX:
                                    if "Gwentro" in BX.Todo: #puts her on ice until a week after the first meeting
                                            BX.PubeC -= 1
                                            if BX.PubeC >= 1:
                                                    BX.Loc = "hold"
                                            else:
                                                    BX.Todo.remove("Gwentro")
                                    GwenX.Event[7] -= 1 if GwenX.Event[7] > 0 else 0          #ticks the "gwengone" event down one week

                        #causes her to wax her pubes
                        if "shave" in BX.Todo:
                                BX.Pubes = 0
                                BX.Todo.remove("shave")

                        if "hair" in BX.Todo:
                                if StormX.Hair == "long":
                                        StormX.Hair = "mohawk"
                                elif StormX.Hair == "wethawk":
                                        StormX.Hair = "wet"
                                elif StormX.Hair == "wet":
                                        StormX.Hair = "wethawk"
                                else:
                                        StormX.Hair = "long"
                                BX.Todo.remove("hair")

                        #causes her to put in piercings
                        if "ring" in BX.Todo:
                                BX.Pierce = "ring"
                                BX.Todo.remove("ring")
                        if "barbell" in BX.Todo:
                                BX.Pierce = "barbell"
                                BX.Todo.remove("barbell")

                if "SGattic" in Player.History:
                        #doreen gets caught, feeding her greatly reduces odds, odds go up over time
                        $ D20 = renpy.random.randint(1, 20)
                        if (D20 + (10*DoreenX.Event[2]) - DoreenX.Event[4]) < 18:
                                $ Player.AddWord(1,0,0,0,"doreenafter") #adds tag to History
    #End of things when you sleep

    # Things that happen every time you wait
    #Things that are about you:
    $ Player.Semen += 1
    $ MultiAction = 1
    $ Player.Focus -= 5 if Player.Focus >= 10 else 0
    $ Situation = 0
    $ Current_Time = Time_Options[(Time_Count)]
    $ Round = 100
    # Clears out recent and daily actions
    $ del Player.RecentActions[:]
    if Time_Count == 0:
            $ del Player.DailyActions[:]
    call Taboo_Level(0)
    call GirlWaitUp #checks girls attraction based on who's in the room

    #Things that are about the girls:      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if Time_Count == 3:
            #if it was just Evening, check to see if they studied
            call Study_Time
    $ BO = TotalGirls[:]
    python:
        for BX in BO:
            #cycles through each girl possible

            BX.Action += 1 if Time_Count != 0 else 0  #not morning

            BX.OCount = 0
            if BX.Lust >= 70 or BX.Thirst >= 30 or (renpy.random.randint(1, 40) + BX.Lust)>= 70:
                        # checks if she wants to fap
                        if "nofap" in BX.Traits:
                                BX.AddWord(1,0,"wannafap",0,0) #adds "wannafap" tag to daily
                        else:
                                BX.AddWord(1,0,"gonnafap",0,0) #adds "wannafap" tag to daily

            if "les" in BX.RecentActions: #if she had a lesbian encounter without you. . .
                        BX.Thirst -= int(BX.Thirst/2) if BX.Thirst >= 50 else BX.Thirst #sets to 0 if under 50, otherwise half it
                        BX.Lust = 20

            #Resets her flirt  options
            BX.Chat[5] = 0
            #Resets her addiction fix attempts            :
            BX.Event[3] -= 1 if BX.Event[3] > 0 else 0 #resets her addiction fix, takes at least five turns before she hassles you again

            BX.Forced = 0
            if BX.Loc == "bg classroom" or BX.Loc == "bg dangerroom" or BX.Loc == "bg teacher":
                    BX.XP += 10
            elif (bg_current == "bg classroom" or bg_current == "bg dangerroom") and BX.Loc == "nearby":
                    BX.XP += 10

            if BX in ActiveGirls and "met" not in BX.History:
                    ActiveGirls.remove(BX)

            #Appearance clean-up
            BX.Blush = 0
            BX.Water = 0
            BX.Held = 0
            if BX.Lust >= 90:
                    BX.Wet = 2
            elif BX.Lust >= 60:
                    BX.Wet = 1
            else:
                    BX.Wet = 0

            #Reduced addiction
            BX.Addict += BX.Addictionrate # +0-10
            BX.Addictionrate -= BX.Resistance if BX.Addictionrate > 3 else 0         #if rate is above 3, drop it by an extra Resistance

            #Adjusts shame rate
            if BX.Taboo and BX.Shame and BX in ActiveGirls:
                        if BX.Loc == "bg dangerroom":
                                BX.Shame -= 10 if BX.Shame >=10 else BX.Shame
                        Count = int((BX.Taboo * BX.Shame) / 200)
                        BX.Statup("Obed", 90, Count)
                        BX.Statup("Inbt", 90, Count)
                        BX.Rep -= Count

            if BX.Plug:
                    BX.Statup("Obed", 95, 1)
                    BX.Statup("Lust", 95, 3)
            if "vibein" in BX.DailyActions:
                    BX.Statup("Obed", 95, 1)
                    BX.Statup("Lust", 95, 3)

            #subtracts BX.Love by 5* the number of recent unsatisfieds
            BX.Love -= 5 * BX.RecentActions.count("unsatisfied")

            # Clears out recent and daily actions
            del BX.RecentActions[:]
            if "angry" in BX.DailyActions:
                        BX.RecentActions.append("angry")
            if Time_Count == 0:
                        del BX.DailyActions[:]
                        if "dailyvibe" in BX.Traits:
                                BX.DailyActions.append("vibein")
                        if "dailyplug" in BX.Traits:
                                BX.Plug = 1
            elif Time_Count == 3 and "yesdate" in BX.DailyActions and "stoodup" not in BX.Traits:
                        #if you stood her up for a date. . .
                        Player.DrainWord("yesdate",0,1)
                        BX.Traits.append("stoodup")

            if BX.Loose < 2:  #checks how tight the girl's asshole is
                        if (BX.Anal + BX.DildoA + BX.Plugged) >= 15:
                                BX.Loose = 2
                        elif (BX.Anal + BX.DildoA + BX.Plugged) >= 3:
                                BX.Loose = 1

#            $ BO[0].XP = 3330 if BO[0].XP > 3330 else BO[0].XP #caps XP
            if BX.XP >= BX.XPgoal and BX.Lvl < 10:
                        BX.XPgoal = int((1.15 * BX.XPgoal) + 100)
                        BX.Lvl += 1
                        BX.StatPoints += 1
#                        "[BO[0].Name]'s leveled up! I bet she has some new tricks to learn."  #change this so that it is something that works #change this so that it is something that works #change this so that it is something that works
#                        if BO[0].Lvl == 10:
#                                "[BO[0].Name]'s reached max level!"
            elif BX.XP > BX.XPgoal:               #caps XP
                        BX.XP = BX.XPgoal
            if BX is LauraX:
                        BX.Addictionrate -= (2 * BX.Resistance) if BX.Addictionrate > 5 else 0
            elif BX is JubesX and "met" in JubesX.History:
                        BX.Addictionrate = 2 if BX.Addictionrate < 2 else BX.Addictionrate
                        if "sunshine" not in JubesX.History:
                                #keeps her getting too hungry before Sunshine event
                                BX.Addict = 40 if BX.Addict > 40 else BX.Addict

            BX.DefaultFaces()      #sets a default face based on conditions
            BX.FaceChange(5)       #resets face
    #end loop

    call Girls_Schedule #schedules all the girls. . .

    if Outfit:
            $ BO = TotalGirls[:]
            python:
                for BX in BO:
                    #loops through and makes choices.
                    BX.OutfitChange(BX.OutfitDay)

    #Player leveling check
    if Player.Lvl < 12 and Player.XP >= Player.XPgoal:
            $ Player.XPgoal = int((1.15 * Player.XPgoal) + 100)
            $ Player.Lvl += 1
            $ Player.StatPoints += 1
            if Player.Lvl <5:
                $ Count = 1
            elif Player.Lvl <9:
                $ Count = 2
            else:
                $ Count = 3
            $ Player.Income += Count
            "Вы подняли свой уровень!"
            "Ксавье заметил ваши достижения и повысил вашу стипендию на [Count]$ в день. Теперь она составляет [Player.Income]$."
            if Player.Lvl == 12:
                "Вы достигли максимального уровня!"
    elif Player.XP > Player.XPgoal:               #caps XP
                $ Player.XP = Player.XPgoal

    #End Hourly actions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

    call LesCheck               #checks to see if the girls hook up with each other. . .
    call JumperCheck            #checks to see if any girls want to jump you
    call AddictCheck            #checks to see if any girls need a fix
#    if _return:                 #acts if a girl messages you that she needs to meet you
#            $ TempLine = _return
#            if "asked meet" in TempLine.DailyActions and TempLine.Addict >= 80:
#                    "[TempLine.Name] texts you. . ."
#                    call AnyLine(TempLine,"I know I asked to meet you in your room earlier, but I'm serious, this is important.")
#                    $ Player.AddWord(1,"asked fix",0,0,0)
#                    $ TempLine.AddWord(1,"asked meet","asked meet",0,0)
#                    $ TempLine = 0
#                    call ReturnToRoom
#            else:
#                    "[TempLine.Name] texts and asks if you could meet her in your room later."
#                    $ TempLine.AddWord(1,"asked meet","asked meet",0,0)
#                    $ TempLine = 0
#                    call ReturnToRoom
    call Relationship_Select    #determines if any of them will have a relationship drama this turn
    #end wait items:

    call Checkout
    if Time_Count < 3:
            hide NightMask onlayer nightmask
    if Lights:
            hide blackscreen onlayer black
    return

# End Wait/Sleep Cycle / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Girl's clothes/location scheduler / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Girl's clothes/location scheduler / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girls_Schedule(Girls = [], Clothes = 1, Location = 1, LocTemp = 0):
        # Set the girl's natural movements
        # If not Clothes, don't bother with her outfit in the schedule
        # Clothes 2 is ordered to change regardless of time of day
        # If not Location, don't bother with the location portion of the schedule
        if not Girls:
                #fills list unless a specific girl is sent
                $ Girls = TotalGirls[:] # neh ActiveGirls[:]
        elif Girls[0] not in TotalGirls:
                return
        python:
            for BX in Girls:
                if BX in Party and Clothes != 2 or not Location:
                        #if she's in a party, never mind
                        pass
                elif Clothes != 2 and "sleepover" in BX.Traits and Time_Count == 0:
                        #she slept over, so just forget this for now
                        pass
                elif BX not in ActiveGirls:
                        LocTemp = "hold"
                        BX.Loc = "hold"
                else:
                        if (Time_Count == 0 and Clothes and Round >= 90) or Clothes == 2:
                                #In the morning, or if ordered to reschedule, pick an outfit for the day.
                                BX.OutfitDay = 0
                                if BX.Break[0]:
                                        pass #she won't pick clothes if she's mad at you
                                elif BX.Clothing[Weekday] == 1:
                                        BX.OutfitDay = "casual1"
                                elif BX.Clothing[Weekday] == 2:
                                        BX.OutfitDay = "casual2"
                                elif BX.Clothing[Weekday] == 3 and BX.Custom1[0]:
                                        BX.OutfitDay = "custom1"
                                elif BX.Clothing[Weekday] == 4:
                                        BX.OutfitDay = "gym"
                                elif BX.Clothing[Weekday] == 5 and BX.Custom2[0]:
                                        BX.OutfitDay = "custom2"
                                elif BX.Clothing[Weekday] == 6 and BX.Custom3[0]:
                                        BX.OutfitDay = "custom3"

                                if not BX.OutfitDay:
                                        #if no custome outfit is set, pick a random one
                                        if BX is GwenX:
                                                Options = ["casual1","casual2","casual2","casual2"]
                                        else:
                                                Options = ["casual1","casual2"]
                                        if not BX.Break[0]:
                                                Options.append("custom1") if BX.Custom1[0] == 2 else Options
                                                Options.append("custom2") if BX.Custom2[0] == 2 else Options
                                                Options.append("custom3") if BX.Custom3[0] == 2 else Options
                                        renpy.random.shuffle(Options)
                                        BX.OutfitDay = Options[0]
                                        del Options[:]
                                BX.Outfit = BX.OutfitDay
                        #End clothing portion

                        #Location portion
                        LocTemp = BX.Loc
                        if BX not in ActiveGirls:
                                LocTemp = "hold"
                                BX.Loc = "hold"
                        elif BX in Party or BX.Loc == "hold":
                                pass
                        else:
                                BX.Loc = BX.Schedule[Weekday][Time_Count]
                                if BX is JubesX and JubesX.Addict > 60:
                                                #Jubilee will not leave her room voluntarily if it's higher than 60
                                                JubesX.Loc = JubesX.Home

                        if BX.Loc != LocTemp and BX not in Party:
                                #if she moved
                                if LocTemp == bg_current:
                                        if ApprovalCheck(BX, 1200) and BX.Loc not in ("bg classroom","bg teacher","bg dangerroom"):
                                                # if she's contented, then she just sticks around
                                                BX.Loc = LocTemp
                                        else:
                                                #If she was where you were, but left
                                                BX.RecentActions.append("leaving")
                                elif BX.Loc == bg_current:
                                                #If she's showed up
                                                BX.RecentActions.append("arriving")
                        if BX in Nearby:
                                                Nearby.remove(BX)
        #end while looping
        if EmmaX.Loc == "bg teacher":
                call AltClothes(EmmaX,8) #Sets teaching outfit
                $ EmmaX.OutfitChange()
        if StormX.Loc == "bg teacher":
                call AltClothes(StormX,8) #Sets teaching outfit
                $ StormX.OutfitChange()
        return
#End Schedule / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Study Time / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Study_Time(BO=[],Studiers=[]):
    #this finds girls that are alone in their rooms and has them study together in the evenings.
    $ BO = TotalGirls[:]
    python:
        for BX in BO:
            if BX.Loc != bg_current and BX.Loc in PersonalRooms:
                    #if they aren't with you, and are in a character room, they study
                    Studiers.append(BX)
    if len(Studiers) < 2:
            #returns if there aren't enough available girls
            return

    $ renpy.random.shuffle(Studiers)
    $ Studiers[0].GLG(Studiers[1],800,5,1)
    $ Studiers[1].GLG(Studiers[0],800,5,1)

    $ Studiers[0].XP += 5
    $ Studiers[1].XP += 5
    return
# End Study Time / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Todo list / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Todo(Chr=0): #rkeljsvgb
        #Actions checked each night
        #causes her to grow her pubes out
        if Chr not in TotalGirls:
            return

        if Chr == LauraX:
                if "pubes" in Chr.Todo:
                        $ Chr.Pubes = 1
                        $ Chr.Todo.remove("pubes")

                if "mission" in Chr.Todo: #puts her on ice until a week after the first meeting
                        $ Chr.PubeC -= 1
                        if Chr.PubeC >= 1:
                                $ Chr.Loc = "hold"
                        else:
                                $ Chr.History.append("dress0") #starts dress event where you'll meet again
                                $ Chr.Todo.remove("mission")
                if "cleanhouse" in Chr.Todo:
                        #if you promised to break up with other girls, this counts it down
                        if LauraX in Player.Harem or not Player.Harem:
                                # mission complete
                                $ LauraX.Event[5] = 2
                                $ Chr.Todo.remove("cleanhouse")
                        $ LauraX.Event[5] -= 1 if LauraX.Event[5] > 1 else 0
        else:
                if "pubes" in Chr.Todo:
                        $ Chr.PubeC -= 1
                        if Chr.PubeC >= 1:
                                pass
                        else:
                                $ Chr.Pubes = 1
                                $ Chr.Todo.remove("pubes")
                if Chr == BetsyX and BetsyX.Event[2]:
                        $ BetsyX.Event[2] -= 1
                if Chr == DoreenX and "SGattic" in Player.History:
                        $ DoreenX.Event[2] -= 1 if DoreenX.Event[2] > 0 else 0
                elif Chr == GwenX:
                    if "Gwentro" in Chr.Todo: #puts her on ice until a week after the first meeting
                            $ Chr.PubeC -= 1
                            if Chr.PubeC >= 1:
                                    $ Chr.Loc = "hold"
                            else:
                                    $ Chr.Todo.remove("Gwentro")
                    $ GwenX.Event[7] -= 1 if GwenX.Event[7] > 0 else 0          #ticks the "gwengone" event down one week

        #causes her to wax her pubes
        if "shave" in Chr.Todo:
                $ Chr.Pubes = 0
                $ Chr.Todo.remove("shave")

        if "hair" in Chr.Todo:
                if StormX.Hair == "long":
                        $ StormX.Hair = "mohawk"
                elif StormX.Hair == "wethawk":
                        $ StormX.Hair = "wet"
                elif StormX.Hair == "wet":
                        $ StormX.Hair = "wethawk"
                else:
                        $ StormX.Hair = "long"
                $ Chr.Todo.remove("hair")

        #causes her to put in piercings
        if "ring" in Chr.Todo:
                $ Chr.Pierce = "ring"
                $ Chr.Todo.remove("ring")
        if "barbell" in Chr.Todo:
                $ Chr.Pierce = "barbell"
                $ Chr.Todo.remove("barbell")
        return

# End Todo list / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Event Calls / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label EventCalls(EGirls=[]): #rkeljsvg
        call Present_Check
        $ D20 = renpy.random.randint(1, 20)
        call Get_Dressed

#        return # fix, for testing only
        if Time_Count == 2 and "yesdate" in Player.DailyActions:
            if bg_current == "bg campus":
                    call DateNight
                    $ Player.DrainWord("yesdate",0,1)
                    return
            else:
                    menu:
                        "У вас назначено свидание, пойдете на площадь?"
                        "Да":
                            $ renpy.pop_call()
                            jump Campus_Entry
                        "Нет":
                            "Вы сделали свой выбор. . ."

        if Day < 2 or Round <= 10: #was day 3
                    #Disables events when it's too early in the game or the turn is about to end
                    return

        #Activates Jubes meet
        if JubesX in ActiveGirls:
                    #you've met Jubes
                    if "switchcheck" in JubesX.Traits:
                            pass
                    elif Time_Count < 3 and "sunshine" not in JubesX.History and "traveling" in Player.RecentActions and bg_current in ("bg classroom","bg dangerroom","bg campus","bg pool"):
                            jump Jubes_Sunshine
                            return
                    elif "mall" not in Player.History and "sunshine" in JubesX.History and Time_Count < 3 and JubesX.Addict < 50:
                            call Jubes_Mall
                            jump Misplaced
                    elif not JubesX.Event[1] and JubesX.Addict < 50:
                            #if she hasn't had her addiction event yet. . .
                            $ JubesX.Addict += 5
        elif "mall" not in Player.History and Day >= 20 and ("met" in JubesX.History or Day >= 30):
                            #if you somehow have met Jubilee but gotten rid of her before unlocking the mall, it unlocks anyway.
                            "Вы находите листовку с рекламой торгового центра."
                            "Хм. Похоже, тут есть торговый центр."
                            $ Player.AddWord(1,0,0,0,"mall") #history
        #End Jubes meet

        #Activates Kitty meet
        if KittyX in ActiveGirls:
                if "switchcheck" in KittyX.Traits:
                        pass
                elif "Kate" not in KittyX.Names and KittyX.Inbt >= 500 and KittyX.Loc == bg_current:
                        #She calls herself Kate now.
                        call Kitty_Kate
                        return

        #Activates Laura meet
        if LauraX in ActiveGirls:
                    pass
        elif "met" not in LauraX.History and "traveling" in Player.RecentActions:
                    #Calls Kitty starting dressup event
                    if Time_Count < 3 and "met" in KittyX.History and "switchcheck" not in KittyX.Traits and "dress0" in LauraX.History:
                                    call Laura_Dressup
                                    return

        #Activates Storm meet
        if StormX in ActiveGirls:
                    if "switchcheck" in StormX.Traits:
                            pass
                    elif Time_Count == 3 and bg_current == "bg pool" and "poolnight" in Player.History and not Party:
                            if "sex friend" not in StormX.Petnames or (D20 < 5 and "poolnight" not in Player.RecentActions):
                                    #call's Storm's skinny dipping thing at night if it's the first time or a 25% chance.
                                    call Storm_Poolnight
                                    return
                    elif Time_Count == 2 and "EmmaStormQueue" in EmmaX.Traits and bg_current != "bg classroom" and "EmmaStorm" not in EmmaX.DailyActions:
                            #Storm and Emma discipline scene and redo
                            if "EmmaStorm" in EmmaX.History:
                                    call Emma_and_Storm_Redux
                            else:
                                    call Emma_and_Storm
                            return
        elif PlotBreak:
                    pass
        elif "met" not in StormX.History and "met" in JeanX.History:
                    if bg_current == "bg player" and "attic" not in Player.History and "noise" not in Player.History and "Intro" not in Player.DailyActions:
                            #You hadn't asked Emma yet
                            call StormMeetPrelude
                            return
                    elif bg_current == "bg classroom" and "noise" in Player.History and "traveling" in Player.RecentActions and Time_Count < 3:
                            #You hadn't asked Emma yet
                            call StormMeetAsk
                            return
                    elif bg_current == "bg player" and Time_Count < 2 and 0 < StormX.Break[0] <= 101 and "traveling" in Player.RecentActions:
                            #Break is being used as a 3-day countdown to when you are forced to meet Storm.
                            call StormMeetWater
                            jump Misplaced
        #End Storm meet

        #Activates Gwen meet
        if GwenX in ActiveGirls:
                if "switchcheck" in GwenX.Traits:
                            pass
                elif "gwengone" in Player.Traits or "promised" in GwenX.Traits:
                            #if you've brought her back into service. . .
                            call Gwenback
                else:
                            #checks ot se if she's yet to meet any of the girls in this room
                            call Gwen_Meet_Check
        else:
                if "gwengone" in Player.Traits and GwenX.Event[7] <= 0:
                        call Gwen_Second_Chance
                elif "met" in GwenX.History:
                        pass
                elif "Gwentro" in GwenX.Todo or "met" not in JeanX.History:
                        pass #if she's recovering from the Laura intro
                elif PlotBreak:
                        pass

                # Modification mode
                elif "traveling" in Player.RecentActions and Time_Count < 3 and "closet" not in Player.RecentActions and GwenX.Delay == 0: #and bg_current == "bg classroom":
                        #happens when going to class if haven't met Gwen or done this today.
                        menu:
                            "Advance towards Gween first meeting?"
                            "Ask again tomorrow":
                                $ GwenX.Delay = 1
                                pass
                            "Ask again in a week":
                                $ GwenX.Delay = 7
                                pass
                            "Ask again in a month":
                                $ GwenX.Delay = 30
                                pass
                            "Sure":
                # -----------------
                                call GwenMeet #returns here if you ignore Gwen
        #End Gwen content

        #Activates Betsy meet
        if BetsyX in ActiveGirls:
                    if "switchcheck" in BetsyX.Traits:
                            pass
                    elif "knife" not in BetsyX.History and ApprovalCheck(BetsyX, 1200) and BetsyX.Loc == bg_current and bg_current in PersonalRooms:
                            #if she hasn't shown off the knife and you are together in a room,
                            call Betsy_Psyknife_Intro
                            return
        elif PlotBreak:
                    pass
        elif "met" not in BetsyX.History and "met" in JubesX.History:
                    if "luggage" in BetsyX.History and BetsyX.Event[2] < 1 and bg_current == "bg classroom":
                            #if you skipped the main intro and she's in the same room as you
                            call BetsyMeet2
                            return
                    elif "luggage" in BetsyX.History:
                            pass
                    elif bg_current != "bg classroom" and Time_Count == 1 and "Intro" not in Player.DailyActions:
                            #You hadn't asked Betsy yet
                            call BetsyMeet
                            jump Misplaced
        #End Betsy conent

        #Activates Doreen meet
        if DoreenX in ActiveGirls:
                    pass
        # Modification mode
        elif "met" not in DoreenX.History and "met" in BetsyX.History and "permanentlyfixed" not in DoreenX.History and "met" in StormX.History:
            if "nightlight" not in Player.History and Time_Count == 1 and "Intro" not in Player.DailyActions:
                            #You hadn't been told to check her yet
                            call DoreenMeetPrelude
                            return
            else:
                # Modification mode
                if "stormreport" in Player.History and (bg_current == StormX.Loc or (StormX.Loc == "bg teacher" and bg_current == "bg classroom")) and "permanentlyfixed" not in DoreenX.History:
                                #if you see Storm without having reported to her, it happens
                                call DoreenStormReport
                # Modification mode
                elif "doreenafter" in Player.History and "doreenafter" not in Player.DailyActions and "traveling" in Player.RecentActions and "permanentlyfixed" not in DoreenX.History:
                                #if you reported her to Storm yesterday
                                call DoreenAftermath
        elif PlotBreak:
                    pass
        elif "met" in BetsyX.History:
            if "nightlight" not in Player.History and Time_Count == 1 and "Intro" not in Player.DailyActions:
                            #You hadn't been told to check her yet
                            call DoreenMeetPrelude
                            return
        #End Doreen content

        #Activates Wanda meet
        if WandaX in ActiveGirls:
                    if "switchcheck" in WandaX.Traits:
                            pass
                    elif "witch" not in WandaX.History and ApprovalCheck(WandaX, 1200) and WandaX.Loc == bg_current:
                            #Shows off MCU costume
                            call Wanda_Witch
                            return
        elif PlotBreak:
                    pass

        # Modification mode
        elif "met" not in WandaX.History and "met" in KittyX.History:
        # -----------------
                    if bg_current != "bg classroom" and "traveling" in Player.RecentActions and Time_Count == 1 and "Intro" not in Player.DailyActions:
                            #You hadn't asked Wanda yet
                            if bg_current not in PersonalRooms:
                                    call WandaMeet
                                    jump Misplaced
        #End Wanda content
        #End character events / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

        #skips events if you were just now following someone
        if "goto" in Player.RecentActions:
                $ Player.RecentActions.remove("goto")
                return

        #locked door check
        if "locked" in Player.Traits:
                #exits if the door is locked, but maybe open this up a bit later.
                return

        if "micro" not in Player.History and Day > 10:
                #this is to offer players microtransactions
                call Microtransactions_Intro
                return
        if "switcher" not in Player.History and Day > 15 and bg_current == "bg player":
                call Rule63_Intro
                return

        #Start relationship checks

        #activates if you haven't done an addiction event today

        if Addict_Queue and Round >= 30 and "fix" not in Player.DailyActions:
            #Addict_Queue will be one girl selected to do it
            if "exhibitionist" in Addict_Queue.Traits or bg_current == "bg player" or bg_current == Addict_Queue.Home:
                call First_Addicted(Addict_Queue)
                return

        if ShareQueue:
                # This has the girl telling you whether another girl is willing to date you
                call Share(ShareQueue[0],ShareQueue[1])

        #this activates a relationship scene to play out this time block if it's in Event_Queue as [RogueX,"_Love"]
        #This is then called in Events by "call expression Event_Queue[0].Tag + Event_Queue[1] #calls an event, ala "Rogue_Love""
        if Event_Queue[1] == "poly":
                call Poly_Start(Event_Queue[0])
                return
        elif Event_Queue[1] == "Stoodup":
                call Date_Stood_Up(Event_Queue[0])
                return
        elif Event_Queue[1]:
                call expression Event_Queue[0].Tag + Event_Queue[1] #calls an event, ala "Rogue_Love"
                return

        #Activates if any girl caught you cheating
        #checks to see if any of the girls noticed you cheating on them
        #returns if not
        call CheatCheck

        #if they might be into you joining their lesbian adventure. . .
        if LesQueue and "no les" not in Player.RecentActions:
            if LesQueue[0].Loc != bg_current and LesQueue[1].Loc != bg_current:
                    #only calls if they are not in the room with you.
                    call Call_For_Les(LesQueue[0],LesQueue[1])
                    if "no les" not in Player.RecentActions:
                            return

        #checks to see if a girl wants to jump you. . .
        call Jumped #will return if nobody in JumpQueue

        #Checks to see if any girls want to fap.
        #If they have "wannafap" in their daily, and "nofap" in their traits, and are not in the room, they will ask you
        #otherwise, they will automatically fap. If you meet them after this, they will be fapping,
        #if you keep them busy, they will do it overnight
        if Time_Count >= 2 and "fapcall" not in Player.DailyActions:
                #if it's evening or later and nobody has yet called you about fapping. . .
                call CalltoFap #checks to see if she's allowed
        #end fap call check

        $ EGirls = ActiveGirls[:]
        $ renpy.random.shuffle(EGirls)
#        while EGirls:
#                if EGirls[0].Loc == bg_current and "switchcheck" in EGirls[0].Traits:
#                        call expression EGirls[0].Tag + "_Switch" #call Rogue_Switch
#                $ EGirls.remove(EGirls[0])
        $ Situation = 0
        python:
            for EGX in EGirls:
                if EGX.Loc == bg_current and "switchcheck" in EGX.Traits:
                        Situation = EGX
                        break
        if Situation:
                call expression Situation.Tag + "_Switch" #call Rogue_Switch

        #activates if you have done an addiction event today
        if Addict_Queue and Round >= 30 and (bg_current == "bg player" or bg_current == Addict_Queue.Home):
                call First_Addicted(Addict_Queue)
                return

        # EndPrimary Event Calls / / / / / / / / / / / / / / / / / Drops down to. . .

label QuickEvents(EGirls=[]):
        #These events get checked every screen refresh
        $ Options = []
        call Present_Check
        $ Player.DrainWord("sexit")

        $ Situation = 0
        $ EGirls = TotalGirls[:]
        $ renpy.random.shuffle(EGirls)
        python:
            for EGX in EGirls:
                if EGX.Loc != bg_current:
                        #if Girl is not around
                        if EGX.Loc == "bg showerroom" and "showered" in EGX.DailyActions:
                                #if she's recently showered and still in the shower, send her elsewhere
                                EGX.Loc = EGX.Schedule[Weekday][Time_Count]
                                if EGX is JubesX and JubesX.Addict > 60:
                                        #Jubilee will not leave her room voluntarily if it's higher than 60
                                        JubesX.Loc = JubesX.Home
                                EGX.Spunk = []
                                EGX.OutfitChange()
                else:
                        if EGX.Lust >= 90:
                                EGX.Blush = 1
                                EGX.Wet = 2
                        elif EGX.Lust >= 60:
                                EGX.Blush = 1
                                EGX.Wet = 1
                        else:
                                EGX.FaceChange(EGX.Emote)
                                EGX.Wet = 0
            for EGX in EGirls:
                if EGX.Loc == bg_current:
                        #Girl reacts to getting horny
                        if Taboo and EGX.Lust >= 75:
                                if EGX.Inbt > 800 or "exhibitionist" in EGX.Traits:
                                        EGX.FaceChange("sly", 2)
                                        if "squirms" not in EGX.RecentActions:
                                                #"[EGX.Name] gets a sly smile on her face and squirms a bit."
                                                narrator(EGX.Name+" лукаво улыбается и начинает слегка ерзать.", interact=True)
                                                EGX.AddWord(1,"squirms",0,0,0) #adds "wannafap" tag to recent
                                elif EGX.Inbt > 500 and EGX.Lust < 90:
                                        EGX.FaceChange("perplexed", 2)
                                        if "flushed" not in EGX.RecentActions:
                                                #"[EGX.Name] looks a bit flushed and uncomfortable."
                                                narrator(EGX.Name+" немного ркраснеет и смущается.", interact=True)
                                                EGX.AddWord(1,"flushed",0,0,0) #adds "wannafap" tag to recent
                                elif bg_current != "bg showerroom":
                                                EGX.FaceChange("perplexed", 2)
                                                #"[EGX.Name] gets an embarrassed look on her face and suddenly leaves the room."
                                                narrator(EGX.Name+" сильно смущается и внезапно выходит из комнаты.", interact=True)
                                                #"gonnafap" in Chr.DailyActions
                                                Situation = EGX
                                                break
            #end orgasm/horny loop
        if Situation:
                #if the girl cums and broke out of loop
                call Remove_Girl(Situation)
                call Set_The_Scene
                $ Situation.Loc = Situation.Home if bg_current != Situation.Home else "bg campus"
                if "nofap" in Situation.Traits:
                        $ Situation.AddWord(1,0,"wannafap",0,0) #adds "wannafap" tag to daily
                        call CalltoFap(Situation) #checks to see if she's allowed
                else:
                        $ Situation.AddWord(1,0,"gonnafap",0,0) #adds "wannafap" tag to daily

        return
#End Quick Events

label Events_Classroom:
        if KittyX not in ActiveGirls and "traveling" in Player.RecentActions and "met" not in KittyX.History and "Intro" not in Player.DailyActions and not PlotBreak:
                        jump KittyMeet
                        return
        #end Kitty content

        if EmmaX in ActiveGirls:
                if "switchcheck" in EmmaX.Traits:
                        pass
                elif Time_Count == 2 and Weekday in (0,2,4):
                        #If you've met Emma, it's evening on a school night, mon/tue/fri
                        if "traveling" in Player.RecentActions and not Party:
                                #if you are in motion,
                                if "classcaught" not in EmmaX.History:
                                        #if first time you catch her, 100% chance
                                        jump Emma_Caught_Classroom
                                        return
                                elif D20 <= 10 and "gonnafap" in EmmaX.DailyActions:
                                        #50/50 chance of catching Emma in class
                                        jump Emma_Caught_Classroom
                                        return

                        if "detention" in Player.Traits and not Party:
                                        jump Emma_Detention

                        if Round >= 70:
                                #if you are in class and not traveling. . .
                                $ EmmaX.Loc = "bg classroom"
        elif "Intro" not in Player.DailyActions and not PlotBreak:
                #Emma is not in ActiveGirls
                if Day >= 4 and "met" not in EmmaX.History and "traveling" in Player.RecentActions and Weekday < 5 and Time_Count < 2:   #was day 6
                        jump EmmaMeet
                        return
        #end Emma content

        if StormX in ActiveGirls:
                    if "switchcheck" in StormX.Traits:
                            pass
                    elif StormX.Loc == "bg teacher" and "Peter" in StormX.History and "traveling" in Player.RecentActions:
                            #if you told her your name was Peter Parker
                            call Storm_Peter
                            return
                    elif Time_Count == 2 and Weekday in (1,3):
                            if "mohawk" not in StormX.History and "traveling" not in Player.RecentActions and ApprovalCheck(StormX, 200, "I"):
                                    jump Storm_Hairtalk
                                    return
                            if Round >= 70:
                                    #if you are in class and not traveling. . .
                                    $ StormX.Loc = "bg classroom"
        #end Storm content

        return
#end  Events_Classroom / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Events_DangerRoom:
        if LauraX not in ActiveGirls and  "met" not in LauraX.History and "traveling" in Player.RecentActions and "Intro" not in Player.DailyActions and not PlotBreak:
            if Day >= 7 and "dress0" not in LauraX.History and "mission" not in LauraX.Todo:
                    call LauraMeet
                    return
        return
#end  Events_DangerRoom / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# End Event Calls / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label AskedMeet(Girl = 0, Emotion = "bemused",Why=0): # Use AskedMeet(RogueX,"angry")
    #This asks the player to meet the chosen character later

    if "switchcheck" in Girl.Traits:
                if Girl.Loc == bg_current or Girl in Party:
                    call expression Girl.Tag + "_Switch" #call Rogue_Switch
                else:
                    if "asked meet" in Girl.DailyActions:
                                $ Girl.DrainWord("asked meet")
                    return
    elif "nogirls" in Girl.History and not Player.Male:
                    if "asked meet" in Girl.DailyActions:
                                $ Girl.DrainWord("asked meet")
                    return

    if "asked meet" not in Girl.DailyActions and Girl.Loc != bg_current and "meet girl" not in Player.DailyActions:
                    $ Girl.FaceChange(Emotion)
                    "[Girl.Name] спрашивает, можете ли вы встретиться с ней позже в своей комнате."
                    "Она [Why]"
                    $ Girl.AddWord(1,"asked meet","asked meet",0,0) # adds "asked meet" to recent and daily
                    $ Player.AddWord(1,0,"meet girl",0,0)
                    if RTR_Toggle:
                            call ReturnToRoom
    return

# End Asked Meet / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label ReturnToRoom:
    #used when asked to meet up with a girl
    menu:
        "Хотите вернуться в свою комнату и разбраться с этим?"
        "Да":
#            $ renpy.pop_call() #removes call to this label
#            $ renpy.pop_call() #removes call to Events
            jump Player_Room_Entry
        "Нет":
            pass
    return

# start Tutorial //////////////////////////////////////////////////////////
menu Tutorial:
    "О чем бы вы хотели узнать?"
    "ПОЛЬЗОВАТЕЛЬСКИЙ ИНТЕРФЕЙС":
        while True:
            menu:
                "О каком элементе ПИ вы бы потели узнать?"
                "Панель отношений":
                        "Панель в верхней левой части экрана отображает характеристики основной девушки. Эти характеристики описаны в другом месте данного обучения."
                        "Если панель темно зеленая - она отображает характеристики Роуг. Если темно-синяя - характеристики Китти."
                "Кнопка фокуса":
                        "Вы можете переключаться между доступными девушками, нажав на маленькую иконку с изображением девушки справа от панели отношений."
                        "Таким образом произойдет смена девушки, на которой вы в данный момент сконцентрированы. Вы можете нажимать на нее так часто, как захотите."
                "Инвентарь":
                        "Маленький рюкзак слева от кнопки фокуса - ваш инвентарь."
                "Время":
                        "На следующей панели отображается день с момента начала игры, день недели и время суток."
                        "Всего четыре времени суток, Утро, Полдень, Вечер, Ночь, все в среднем по 4 часа (не включая время сна)"
                "Меню":
                        "Большая часть вариантов выбора в игре производится через меню в левой части экрана."
                        "Не беспокойтесь о том, что вы сделали 'плохие' выборы, это лишь временные неудачи."
                        "Абсолютных неудач не существует, даже выбор, который расстраивает девушку, может иметь свои плюсы."
                        "Играйте так, как вы хотите играть и получайте удовольствие."
                "Назад":
                    jump Tutorial
    "Характеристики":
        menu Tutorial_Stats:
            "О каких характеристиках вы хотели бы узнать?"
            "Характеристики Взаимоотношений":
                "Характеристики используется для отслеживания вашего прогресса с различными девушками в особняке."
                while True:
                    menu:
                        "Какая именно характеристика вас интересует?"
                        "Любовь":
                                "Если вы посмотрите в верхний левый угол экрана, там находится красная панель."
                                "Она представляет собой \"уровень любви девушки.\""
                                "Вы можете поднять эту характеристику, выполняя взаимодействия, которые делают девушку счастливой. Это приводит к появлению красного +Х, где Х - это количество набранных очков."
                                $ RogueX.Statup("Love", 200, 1)
                                "Вы также можете снизить это число, если делаете то, что заставляет девушку расстраиваться. Это приводит к появлению красного -X."
                                $ RogueX.Statup("Love", 200, -1)
                                "Если она заполнена примерно на 50\%, это означает, что девушка относится к вам плюс-минус \"нейтрально\". Если ниже, то вы ей не очень нравитесь."
                        "Повиновение":
                                "Синяя панель справа от Любви - это \"уровень Повиновения\""
                                "Он представляет желание девушки делать то, что Вы хотите, и поднимается, когда Вы убеждаете ее что-то делать."
                                $ RogueX.Statup("Obed", 200, 1)
                                "Он опускается, когда Вы слишком сильно нажимаете на нее, и она отказывается."
                                $ RogueX.Statup("Obed", 200, -1)
                        "Раскрепощенность":
                                "Желтая полоса - это \"уровень Раскрепощенности\"."
                                "Он показывает, насколько сексуальной считает себя девушка, и он поднимается, когда она решает что-то сделать сама по себе или что-то пошлое в первый раз."
                                $ RogueX.Statup("Inbt", 200, 1)
                                "Он опускается, когда ей становится слишком стыдно, например, когда ее поймали за чем-то, что выходит за рамки ее понимания понятия сексуальности."
                                $ RogueX.Statup("Inbt", 200, -1)
                                "Это три основные характеристики отношений, и большинство действий в игре определяется тем, насколько высока каждая из них, либо самостоятельно, либо в комбинациях."
                                "Если вы сможете достичь 1000 во всех трех характеристиках, она будет готова практически на все, хотя некоторые виды деятельности потребуют особых условий."
                        "Назад":
                                jump Tutorial_Stats
            "Эро Характеристики":
                "Есть несколько характеристик, которые используются в сексуальных контактах."
                while True:
                    menu:
                        "Какая именно характеристика вас интересует?"
                        "Похоть":
                                "Панель под \"панелью Любви\" представляет собой \"Похоть девушки\""
                                "Этот стат поднимается, когда она возбуждается, и падает, когда ее обламывают или после ее оргазма (при 100%%)."
                                $ RogueX.Statup("Lust", 200, 1)
                                $ RogueX.Lust -= 1
                        "Возбуждение Игрока":
                                "Довольно \"внушительная\" панель справа от панели Раскрепощенности представляет ваше собственное возбуждение."
                                $ Player.Statup("Focus", 200, 1)
                                $ Player.Focus -= 1
                                "При достижении 100%% наступит оргазм. Чтобы замедлить наступление оргазма надо научиться \"концентрации\"."
                                "Чем лучше Вы в сексе, тем быстрее будут расти показатели."
                                if Player.Male:
                                        "Нажатие на эту панель в определенных позах сделает пенис полупрозрачным."
                                        "Ниже есть еще одна панель, которая отображает, сколько раз Вы сможете кончит перед тем, как вам будет нужна передышка. Эту характеристику можно будет увеличить при повышении уровня."
                                else:
                                        "Ниже есть еще одна панель, которая отображает, сколько раз Вы сможете поднять Вашего храброго воина до того, как будет нужна передышка. Эту характеристику можно будет увеличить при повышении уровня."
                                "Также следует учитывать, что девушки будут готовы только к определенному количеству сексуальных актов за определенный период времени."
                        "Назад":
                                jump Tutorial_Stats
            "Характеристики Игрока":
                    "Кроме Похоти, упомянутой выше, у игрока есть еще несколько характеристик, о которых следует упомянуть."
                    "Одна из них - ОП или очки опыта. Они повышаюся, когда Игрок учится, посещает занятия или тренируется."
                    "Опыт отображает прогресс Игрока в качестве мутанта и студента Института. При повышении уровней Вы получаете очки характеристик."
                    "Их можно использовать для открытия новых черт, как улучшающих Ваши собственные силы, так и сексуальные навыки."
                    "Девушки также могут получать черты, которые открывают новые способности."
                    "У вас также есть уровень дохода, основанный на стипендии, которую предоставляет Ксавье. Он повышается по мере роста вашего уровня, но может быть уменьшен за плохое поведение."
            "Зависимость":
                    "Под Послушанием отображена панель Зависимости. Она повышается каждый раз, когда девушке не хватает Ваших прикосновений."
                    "Она опускается, когда девушка вступает в физический контакт с Вами, и чем интенсивнее контакт, тем слабее становится желание."
                    "На высоких уровнях зависимости она очень восприимчива к Вашим предложениям, но не будет счастлива, если Вы будете слишком сильно на чем-то настаивать."
                    "Сила Зависимости представлена справа от панели Зависимости. Эта характеристика показывает, как быстро тяга девушки к Вам растет и как со временем падает."
                    "Существуют различные способы, которыми Вы можете увеличить или уменьшить ее зависимость от ваших прикосновений. Используйте эту возможность на свой страх и риск."
                    "Если этот аспект Вас не интересует, Вы можете просто выбирать более мягкие варианты, чтобы удовлетворить ее тягу до тех пор, пока ее зависимость не исчезнет."
            "Назад":
                    jump Tutorial
        jump Tutorial_Stats
    "Деятельность":
        while True:
            menu:
                "Хотите узнать как вы можете проводить свое время?"
                "Ждать / Спать":
                        "Вы всегда можете просто \"Ждать.\" Это приведет к тому, что вы просто-напросто потеряете свое время, но кто знает, может, произойдет что-то интересное."
                        "Конечно, ночью можно только \"Спать.\" Поначалу вы сможете спать только в своей комнате, но, возможно, кто-нибудь еще позволит вам спать в ее комнате."
                "Магазин":
                        "Вы также можете получить доступ к магазину-поставщику института, где можно заказать различные предметы, которые будут доставлены в вашу комнату."
                "Аудитория":
                        "Вы всегда можете посещать занятия. Как правило, это не особо интересно, но зато дает очки опыта, да и в аудитории могут возникнуть различные события."
                        "Занятия доступны в будние дни утром и в полдень. Там вы также можете столкнуться с другими девушками."
                        "Вы можете пойти на занятия через \"Выйти [[Идти на площадь кампуса].\""
                "Комната Опасности":
                        "Вы также можете пойти на тренировки в Комнату Опасности, что даст вам дополнительные очки опыта."
                        "Комната Опасности открыта в любое время, кроме поздней ночи (студенты все таки нуждаются во сне)."
                        "Вы можете попасть в Комнату Опасности через \"Выйти [[Идти на площадь кампуса].\""
                "Душ":
                        "Вы можете также принимать душ. Не волнуйтесь, это не обязательное действие, никто не заставляет вас ходить туда каждый день."
                        "Вы можете попасть в душевые через \"Выйти [[Идти на площадь кампуса].\""
                "Заниматься":
                        "Вы можете учиться с каким-нибудь другим студентом. Это принесет вам дополнительный опыт, и, кто знает, может еще что произойдет?"
                "Свидания":
                        "Вечером вы можете пойти с кем-нибудь на свидание. Она, скорее всего, будет ожидать, что вы за все заплатите, так что будьте к этому готовы."
                "Общение":
                        "И конечно вы можете просто поболтать с кем-нибудь, или же поговорить с ними по телефону, если у вас есть их номер."
                "Хэллоуин":
                        "Вы можете устроить вечеринку в честь Хэллоуина, находясь в своей комнате, через меню \"спец. возможности\"."
                        "На этой вечеринке можно разблокировать хэллоуинские костюмы для каждой девушки."
                        "Вы можете устраивать данную вечеринку так часто, как вам захочется."
                "Назад":
                        jump Tutorial

    "Неважно.":
        return
jump Tutorial

label SpecialMenu: #rkeljsvgb
    while True:
        menu:
            "Обучение":
                    jump Tutorial
            "Проверка характеристики" if False:
                    "Этот элемент проверит все характеристики и удостоверится, что они работает корректно на вашем текущем сохранение."
                    "Пригодится при ошибке типа 'variable not found', на русском скорее всего будет работать не корректно, в будущем, возможно, будет поправлено[[Напомните пожалуйста CreDz-у об этом]."
                    menu:
                        "Вы хотите выполнить это действие?"
                        "Да":
                                $ renpy.pop_call()
                                call Failsafe
                                jump Player_Room
                        "Неважно.":
                                pass
            "Вечеринка в честь Хэллоуина [[Только вечером] (locked)" if Time_Count != 2:
                    pass
            "Вечеринка в честь Хэллоуина" if Time_Count == 2:
                    if "halloween" in Player.History:
                            "Хотите повторить вечеринку в честь Хэллоуина?"
                            "Прошедшее событие не окажет влияния ни на одну девушку,"
                            "но флирт и подобные действия смогут повлиять на их статы."
                    else:
                            "Институт Ксавье заполняется всякими жуткими штучками."
                            "Вы же получаете приглашение посетить вечеринку в честь Хэллоуина, которая пройдет на площади кампуса."
                            "Вы можете пойти сейчас или когда-нибудь потом. Вы всегда сможете повторить это событие."
                    menu:
                        "Пойти на вечеринку?"
                        "Да":
                                "Вы переодеваетесь в свой костюм и отправляетесь на вечеринку."
                                call Halloween_Party_Entry
                        "Нет":
                                return


            "Выполнить несколько Микротранзакций [[Заблокировано] (locked)" if "micro" not in Player.History:
                    call Microtransactions
            "Выполнить несколько Микротранзакций" if "micro" in Player.History:
                    call Microtransactions
            "Посетить лабораторию МакКоя, чтобы изменить информацию о себе.":
                    call Hanks_Lab
            "Меню уровней":
                while True:
                    menu:
                        "Меню повышения уровня"
                        "Повысить свой уровень" if Player.StatPoints > 0 or "addict control" in Player.Traits:
                                call Level_Up(Player)
                        "Повысить свой уровень [[нет свободных очков] (locked)" if Player.StatPoints <= 0 and "addict control" not in Player.Traits:
                                pass
                        "Повысить уровень: [RogueX.Name]" if RogueX.StatPoints > 0:
                                call Level_Up(RogueX)
                        "Повысить уровень: [KittyX.Name]" if KittyX.StatPoints > 0 and "met" in KittyX.History:
                                call Level_Up(KittyX)
                        "Повысить уровень: [EmmaX.Name]" if EmmaX.StatPoints > 0 and "met" in EmmaX.History:
                                call Level_Up(EmmaX)
                        "Повысить уровень: [LauraX.Name]" if LauraX.StatPoints > 0 and "met" in LauraX.History:
                                call Level_Up(LauraX)
                        "Повысить уровень: [JeanX.Name]" if JeanX.StatPoints > 0 and "met" in JeanX.History:
                                call Level_Up(JeanX)
                        "Повысить уровень: [StormX.Name]" if StormX.StatPoints > 0 and "met" in StormX.History:
                                call Level_Up(StormX)
                        "Повысить уровень: [JubesX.Name]" if JubesX.StatPoints > 0 and "met" in JubesX.History:
                                call Level_Up(JubesX)
                        "Повысить уровень: [GwenX.Name]" if GwenX.StatPoints > 0 and "met" in GwenX.History:
                                call Level_Up(GwenX)
                        "Повысить уровень: [BetsyX.Name]" if BetsyX.StatPoints > 0 and "met" in BetsyX.History:
                                call Level_Up(BetsyX)
                        "Повысить уровень: [DoreenX.Name]" if DoreenX.StatPoints > 0 and "met" in DoreenX.History:
                                call Level_Up(DoreenX)
                        "Повысить уровень: [WandaX.Name]" if WandaX.StatPoints > 0 and "met" in WandaX.History:
                                call Level_Up(WandaX)
                        "Назад":
                                jump SpecialMenu
                "Сначала вам нужно набраться опыта, тренируясь или посещая занятия."

            "Возвращаться в свою комнату по просьбе?":
                        "Если девушка говорит, что хочет вас видеть, по умолчанию вас спрашивают, \"Хотите ли вы вернуться\"."
                        menu:
                            "Хотите ли вы, чтобы игра сначала спрашивала вас об этом?"
                            "Да [[уже выбрано]" if RTR_Toggle:
                                    pass
                            "Да" if not RTR_Toggle:
                                    $ RTR_Toggle = 1
                            "Нет [[уже выбрано]" if not RTR_Toggle:
                                    pass
                            "Нет" if RTR_Toggle:
                                    $ RTR_Toggle = 0
            "Вкл особый Режим Перемещения" if not TravelMode:
                    "Этот режим позволяет вам перемещаться только непосредственно в соседние области, а не сразу в более отдаленные."
                    "Если вы предпочитаете использовать стандартный вид, типа \"карта мира\" вид перемещения, вы можете отключить этот режим."
                    "Используйте \"Выйти\" чтобы открыть список локаций."
                    $ TravelMode = 1
            "Чит-меню":
                    call cheats
            "Выкл особый Режим Перемещения" if TravelMode:
                    $ TravelMode = 0

            "Нажать большую красную кнопку" if False:
                "Хм, интересно, что бы это могло значить. . ."

            "Неважно.":
                return
    return
# end Tutorial//////////////////////////////////////////////////////////

# start Hank's Lab//////////////////////////////////////////////////////////
label Hanks_Lab(Line=0, BO=[]):
        "Это лаборатория профессора МакКоя. Здесь вы можете изменять себя."
        "Изменения будут настолько безобидными, что никто даже не заметит!"
        while True:
            $ Line = 0
            menu:
                "Что бы вы хотели сделать?"
                "Измененить цвет кожи":
                        menu:
                            "Какой цвет кожи вы бы хотели?"
                            "Зеленый":
                                    $ Player.Color = "green"
                            "Белый":
                                    $ Player.Color = "pink"
                            "Черный":
                                    $ Player.Color = "brown"
                            "Неважно":
                                    $ Line = 1
                        if not Line:
                                "Вы возитесь с аппаратом МакКоя и в итоге светящаяся голубая жидкость наливается в колбу."
                                "Вы проглатываете ее одним глотком и вскоре тон вашей кожи меняется на угодный вам."

                "Изменить свое имя.":
                            "Вы входите в систему на высокопроизводительном компьютере МакКоя, это должно позволить вам изменить свое имя во всех официальных базах данных."
                            $ Player.XName = Player.Name
                            $ Player.XName_rod = Player.Name_rod
                            $ Player.XName_dat = Player.Name_dat
                            $ Player.XName_vin = Player.Name_vin
                            $ Player.XName_tvo = Player.Name_tvo
                            $ Player.XName_pre = Player.Name_pre
                            $ Player.Name = renpy.input("Какое имя вы бы хотели?", default="Зеро", length = 10)
                            $ Player.Name = Player.Name.strip()
                            if not Player.Name :
                                    $ Player.Name  = "Зеро"
                                    $ Player.Name_rod  = "Зеро"
                                    $ Player.Name_dat  = "Зеро"
                                    $ Player.Name_vin  = "Зеро"
                                    $ Player.Name_tvo  = "Зеро"
                                    $ Player.Name_pre  = "Зеро"
                            if Player.Name in ("хозяин", "господин", "любимый", "парень", "любовник", "ебарь", "хозяйка", "госпожа", "любимая", "девушка", "любовница", "ебунша"):
                                    "Хорошая попытка, умник."
                                    $ Player.Name  = "Зеро"
                                    $ Player.Name_rod  = "Зеро"
                                    $ Player.Name_dat  = "Зеро"
                                    $ Player.Name_vin  = "Зеро"
                                    $ Player.Name_tvo  = "Зеро"
                                    $ Player.Name_pre  = "Зеро"
                            if Player.Name != "Зеро":
                                    $ Player.Name_rod  = renpy.input("Имя в Р.п (у кого?)?", default=Player.Name, length = 10)
                                    $ Player.Name_rod  = Player.Name_rod.strip()
                                    $ Player.Name_dat  = renpy.input("Имя в Д.п (кому?)?", default=Player.Name, length = 10)
                                    $ Player.Name_dat  = Player.Name_dat.strip()
                                    $ Player.Name_vin  = renpy.input("Имя в В.п (кого?)?", default=Player.Name, length = 10)
                                    $ Player.Name_vin  = Player.Name_vin.strip()
                                    $ Player.Name_tvo  = renpy.input("Имя в Т.п (кем?)?", default=Player.Name, length = 10)
                                    $ Player.Name_tvo  = Player.Name_tvo.strip()
                                    $ Player.Name_pre  = renpy.input("Имя в П.п (о ком?)?", default=Player.Name, length = 10)
                                    $ Player.Name_pre  = Player.Name_pre.strip()
                            if Player.Name == "Зеро":
                                    $ Player.Name_rod  = "Зеро"
                                    $ Player.Name_dat  = "Зеро"
                                    $ Player.Name_vin  = "Зеро"
                                    $ Player.Name_tvo  = "Зеро"
                                    $ Player.Name_pre  = "Зеро"
                            if "met" in KittyX.History:
                                    $ KittyX.Petnames.append(Player.Name[:1])
                            if "met" in EmmaX.History:
                                    call LastNamer
                                    $ EmmaX.Petnames.append(_return)
                            if Player.XName in JeanX.Petnames and Player.Name not in JeanX.Petnames:
                                    $ JeanX.Petnames.append(Player.Name)  #adds new name if old one was in there.
                            "Это должно помочь, ваше имя было обновлено и всем в кампусе было отправлено электронное письмо об его изменении."


                "Сменить пол." if "switcher" in Player.History:
                            if Player.Male:
                                    "Устройство МакКоя позволит вам сменить свой биологический пол, став женщиной."
                            else:
                                    "Устройство МакКоя позволит вам сменить свой биологический пол, став мужчиной."
                            "Вы желаете это сделать?"
                            menu:
                                extend ""
                                "Да.":
                                        "Вы настраиваете устройство и входите в него."
                                        "Устройство мигает, кряхтит, когда все прекращается, вы выходите."
                                        if Player.Male:
                                                "Теперь вы женщина, поздравляю."
                                                $ Player.Male = 0
                                                $ Loadout = Loadout0
                                                if "switched" not in Player.History:
                                                        "Когда вы выходите, вы слышите \"лязг\" из лотка, вмонтированного в устройство."
                                                        "Заглянув внутрь, вы видите что-то похожее на большой фиолетовый член, выглядящий до жути знакомым. . ."
                                                        "Он может вам пригодиться."
                                        else:
                                                "Теперь вы мужчина, поздравляю."
                                                $ Player.Male = 1
                                                $ Loadout = Loadout1

                                        "Вы хотите также сменить свое имя?"
                                        menu:
                                            extend ""
                                            "Да.":
                                                    $ Player.XName = Player.Name
                                                    $ Player.XName_rod = Player.Name_rod
                                                    $ Player.XName_dat = Player.Name_dat
                                                    $ Player.XName_vin = Player.Name_vin
                                                    $ Player.XName_tvo = Player.Name_tvo
                                                    $ Player.XName_pre = Player.Name_pre
                                                    $ Player.Name = renpy.input("Какое имя вы бы хотели?", default="Зеро", length = 10)
                                                    $ Player.Name = Player.Name.strip()
                                                    if not Player.Name :
                                                            $ Player.Name  = "Зеро"
                                                            $ Player.Name_rod  = "Зеро"
                                                            $ Player.Name_dat  = "Зеро"
                                                            $ Player.Name_vin  = "Зеро"
                                                            $ Player.Name_tvo  = "Зеро"
                                                            $ Player.Name_pre  = "Зеро"
                                                    if Player.Name in ("хозяин", "господин", "любимый", "парень", "любовник", "ебарь", "хозяйка", "госпожа", "любимая", "девушка", "любовница", "ебунша"):
                                                            "Хорошая попытка, умник."
                                                            $ Player.Name  = "Зеро"
                                                            $ Player.Name_rod  = "Зеро"
                                                            $ Player.Name_dat  = "Зеро"
                                                            $ Player.Name_vin  = "Зеро"
                                                            $ Player.Name_tvo  = "Зеро"
                                                            $ Player.Name_pre  = "Зеро"
                                                    if Player.Name != "Зеро":
                                                            $ Player.Name_rod  = renpy.input("Имя в Р.п (у кого?)?", default=Player.Name, length = 10)
                                                            $ Player.Name_rod  = Player.Name_rod.strip()
                                                            $ Player.Name_dat  = renpy.input("Имя в Д.п (кому?)?", default=Player.Name, length = 10)
                                                            $ Player.Name_dat  = Player.Name_dat.strip()
                                                            $ Player.Name_vin  = renpy.input("Имя в В.п (кого?)?", default=Player.Name, length = 10)
                                                            $ Player.Name_vin  = Player.Name_vin.strip()
                                                            $ Player.Name_tvo  = renpy.input("Имя в Т.п (кем?)?", default=Player.Name, length = 10)
                                                            $ Player.Name_tvo  = Player.Name_tvo.strip()
                                                            $ Player.Name_pre  = renpy.input("Имя в П.п (о ком?)?", default=Player.Name, length = 10)
                                                            $ Player.Name_pre  = Player.Name_pre.strip()
                                                    if Player.Name == "Зеро":
                                                            $ Player.Name_rod  = "Зеро"
                                                            $ Player.Name_dat  = "Зеро"
                                                            $ Player.Name_vin  = "Зеро"
                                                            $ Player.Name_tvo  = "Зеро"
                                                            $ Player.Name_pre  = "Зеро"
                                                    if Player.XName in JeanX.Petnames and Player.Name not in JeanX.Petnames:
                                                            $ JeanX.Petnames.append(Player.Name)  #adds new name if old one was in there.
                                            "Нет.":
                                                    #no name change
                                                    $ Player.XName = Player.Name
                                                    $ Player.XName_rod = Player.Name_rod
                                                    $ Player.XName_dat = Player.Name_dat
                                                    $ Player.XName_vin = Player.Name_vin
                                                    $ Player.XName_tvo = Player.Name_tvo
                                                    $ Player.XName_pre = Player.Name_pre

                                        $ BO = TotalGirls[:]
                                        python:
                                            for BX in BO:
                                                if "met" in BX.History and "switched2" not in BX.History:
                                                        #adds a check if you haven't switched bodies at least twice yet
                                                        BX.Spunk = []                      #clears out spunk, since it would change anyway
                                                        BX.AddWord(1,0,0,"switchcheck")    #traits
                                        $ Player.AddWord(1,0,0,0,"switched") #adds to history
                                        $ Player.AddWord(1,0,0,"switchxavier") #adds to traits

                                        if "switched2" not in JeanX.History:
                                                call JeanName


                                "Нет.":
                                        #no sex change
                                        pass
                            #end sex change
                "Красная кнопка" if False:
                            if not Player.Harem:
                                "Нет гарема"
                            elif len(Player.Harem) == 4:
                                "[Player.Harem[0].Tag],[Player.Harem[1].Tag],[Player.Harem[2].Tag],[Player.Harem[3].Tag]"
                            elif len(Player.Harem) == 3:
                                "[Player.Harem[0].Tag],[Player.Harem[1].Tag],[Player.Harem[2].Tag]"
                            elif len(Player.Harem) == 2:
                                "[Player.Harem[0].Tag],[Player.Harem[1].Tag]"
                            else:
                                "[Player.Harem[0].Tag]"
                "Синяя кнопка" if False:
                            $ Count = len(ActiveGirls)
                            "[Count]"
                            if len(ActiveGirls) == 8:
                                "A-[ActiveGirls[0].Tag],[ActiveGirls[1].Tag],[ActiveGirls[2].Tag],[ActiveGirls[3].Tag]"
                                "B-[ActiveGirls[4].Tag],[ActiveGirls[5].Tag],[ActiveGirls[6].Tag],[ActiveGirls[7].Tag]"
                            elif len(ActiveGirls) == 7:
                                "A-[ActiveGirls[0].Tag],[ActiveGirls[1].Tag],[ActiveGirls[2].Tag],[ActiveGirls[3].Tag]"
                                "B-[ActiveGirls[4].Tag],[ActiveGirls[5].Tag],[ActiveGirls[6].Tag]"
                            elif len(ActiveGirls) == 6:
                                "A-[ActiveGirls[0].Tag],[ActiveGirls[1].Tag],[ActiveGirls[2].Tag],[ActiveGirls[3].Tag]"
                                "B-[ActiveGirls[4].Tag],[ActiveGirls[5].Tag]"
                            elif len(ActiveGirls) == 5:
                                "A-[ActiveGirls[0].Tag],[ActiveGirls[1].Tag],[ActiveGirls[2].Tag],[ActiveGirls[3].Tag]"
                                "B-[ActiveGirls[4].Tag]"
                            elif len(ActiveGirls) == 4:
                                "[ActiveGirls[0].Tag],[ActiveGirls[1].Tag],[ActiveGirls[2].Tag],[ActiveGirls[3].Tag]"
                            elif len(ActiveGirls) == 3:
                                "[ActiveGirls[0].Tag],[ActiveGirls[1].Tag],[ActiveGirls[2].Tag]"
                            elif len(ActiveGirls) == 2:
                                "[ActiveGirls[0].Tag],[ActiveGirls[1].Tag]"
                            else:
                                "[ActiveGirls[0].Tag]"
                            $ Count = 0
                "Желтая кнопка" if False:
                            $ Count = len(TotalGirls)
                            "[Count]"
                            if len(TotalGirls) > 11:
                                "more"
                            elif len(TotalGirls) == 11:
                                "A-[TotalGirls[0].Tag],[TotalGirls[1].Tag],[TotalGirls[2].Tag],[TotalGirls[3].Tag]"
                                "B-[TotalGirls[4].Tag],[TotalGirls[5].Tag],[TotalGirls[6].Tag],[TotalGirls[7].Tag]"
                                "C-[TotalGirls[8].Tag],[TotalGirls[9].Tag],[TotalGirls[10].Tag]"
                            elif len(TotalGirls) == 10:
                                "A-[TotalGirls[0].Tag],[TotalGirls[1].Tag],[TotalGirls[2].Tag],[TotalGirls[3].Tag]"
                                "B-[TotalGirls[4].Tag],[TotalGirls[5].Tag],[TotalGirls[6].Tag],[TotalGirls[7].Tag]"
                                "C-[TotalGirls[8].Tag],[TotalGirls[9].Tag]"
#                                "C-[TotalGirls[8].Tag],[TotalGirls[9].Tag],[TotalGirls[10].Tag],[TotalGirls[11].Tag]"
                            elif len(TotalGirls) == 9:
                                "A-[TotalGirls[0].Tag],[TotalGirls[1].Tag],[TotalGirls[2].Tag],[TotalGirls[3].Tag]"
                                "B-[TotalGirls[4].Tag],[TotalGirls[5].Tag],[TotalGirls[6].Tag],[TotalGirls[7].Tag]"
                                "C-[TotalGirls84].Tag]"
                            elif len(TotalGirls) == 8:
                                "A-[TotalGirls[0].Tag],[TotalGirls[1].Tag],[TotalGirls[2].Tag],[TotalGirls[3].Tag]"
                                "B-[TotalGirls[4].Tag],[TotalGirls[5].Tag],[TotalGirls[6].Tag],[TotalGirls[7].Tag]"
                            elif len(TotalGirls) == 7:
                                "A-[TotalGirls[0].Tag],[TotalGirls[1].Tag],[TotalGirls[2].Tag],[TotalGirls[3].Tag]"
                                "B-[TotalGirls[4].Tag],[TotalGirls[5].Tag],[TotalGirls[6].Tag]"
                            elif len(TotalGirls) == 6:
                                "A-[TotalGirls[0].Tag],[TotalGirls[1].Tag],[TotalGirls[2].Tag],[TotalGirls[3].Tag]"
                                "B-[TotalGirls[4].Tag],[TotalGirls[5].Tag]"
                            elif len(TotalGirls) == 5:
                                "A-[TotalGirls[0].Tag],[TotalGirls[1].Tag],[TotalGirls[2].Tag],[TotalGirls[3].Tag]"
                                "B-[TotalGirls[4].Tag]"
                            elif len(TotalGirls) == 4:
                                "[TotalGirls[0].Tag],[TotalGirls[1].Tag],[TotalGirls[2].Tag],[TotalGirls[3].Tag]"
                            elif len(TotalGirls) == 3:
                                "[TotalGirls[0].Tag],[TotalGirls[1].Tag],[TotalGirls[2].Tag]"
                            elif len(TotalGirls) == 2:
                                "[TotalGirls[0].Tag],[TotalGirls[1].Tag]"
                            else:
                                "[TotalGirls[0].Tag]"
                            $ Count = 0
                "Оранжевая кнопка" if False:
                            $ Line = "This is Halloween." if "halloween" in RogueX.History else "no"
                            "Rogue: [Line]"
                            $ Line = "This is Halloween." if "halloween" in KittyX.History else "no"
                            "Kitty: [Line]"
                            $ Line = "This is Halloween." if "halloween" in EmmaX.History else "no"
                            "Emma: [Line]"
                            $ Line = "This is Halloween." if "halloween" in LauraX.History else "no"
                            "Laura: [Line]"
                            $ Line = "This is Halloween." if "halloween" in JeanX.History else "no"
                            "Jean: [Line]"
                            $ Line = "This is Halloween." if "halloween" in StormX.History else "no"
                            "Storm: [Line]"
                            $ Line = 0
                "Бирюзовая кнопка":
                            if "EmmaStorm" in EmmaX.History:
                                if ApprovalCheck(EmmaX, 1200) and ApprovalCheck(StormX, 1200): #and "EmmaStormQueue" not in EmmaX.Traits:
                                        $ EmmaX.AddWord(1,0,0,"EmmaStormQueue") #adds to Traits, queuing up a redo of event
                                        "Ready, should work in the evenings, when outside of the classroom."
                                else:
                                        "Not elligible for repeast, get better scores with Emma and Storm."
                            elif "classcaught" in EmmaX.History and "met" in StormX.History and (EmmaX.SEXP >= 15 or StormX.SEXP >= 15):
                                        $ EmmaX.AddWord(1,0,0,"EmmaStormQueue") #adds to Traits, queuing up a redo of event
                                        "Ready, should work in the evenings, when outside of the classroom."
                            else:
                                        "Not elligible, get a little action with either Emma or Storm."
                "Зеленая кнопка":
                            $ bg_current = "bg campus"
                            call Remove_Girl("All")
                            call Set_The_Scene
                            $ Count = len(Nearby)
                            while True:
                                menu:
                                    "There are currently [Count] girls nearby."
                                    "Add a girl":
                                        if Count < len(TotalGirls):
                                                $ Nearby.append(TotalGirls[Count])
                                                $ Count += 1
                                        else:
                                                "There are no girls left to add"
                                    "Remove a girl":
                                        if Count > 0 and Nearby:
                                                $ Count -= 1
                                                $ Nearby.remove(TotalGirls[Count])
                                                call Girl_Hide(TotalGirls[Count],1)  #call expression TotalGirls[Count].Tag + "_Hide" pass (1)
                                        else:
                                                "There are no girls left to remove"
                                    "Show Nearby":
                                        call Campus_Nearby
                                    "Do some dialogue":
                                            ch_r "What's up?"
                                            "Not much."
                                            ch_r "That was a waste of time."
                                    "Exit":
                                            $ bg_current = "bg player"
                                            $ Nearby = []
                                            $ Count = 0
                                            jump Misplaced
                "Выйти.":
                            "Вы возвращаетесь в свою комнату."
                            return

        return

label Petname_Update(BO=[]):
    # This is called when you change terms, updating everyone's Petnames
    $ BO = TotalGirls[:]
    python:
        for BX in BO:
            if BX.Petname in ("boyfriend","girlfriend","dearfriend","мой парень","моя девушка"):
                    if not Player.Male:
                        BX.Petname = "моя девушка"
                    else:
                        BX.Petname = "мой парень"
            elif BX.Petname in ("sir","ma'am","господин","госпожа"):
                    if not Player.Male:
                        BX.Petname = "госпожа"
                    else:
                        BX.Petname = "господин"
            elif BX.Petname in ("master","mistress","хозяин","хозяйка"):
                    if not Player.Male:
                        BX.Petname = "хозяйка"
                    else:
                        BX.Petname = "хозяин"
            elif BX.Petname in ("daddy","momma","мамочка","папочка"):
                    if not Player.Male:
                        BX.Petname = "мамочка"
                    else:
                        BX.Petname = "папочка"
            elif BX.Petname in ("bro","sis","бро","сис"):
                    if not Player.Male:
                        BX.Petname = "сис"
                    else:
                        BX.Petname = "бро"
    return
## end Petname_Update//////////////////////////////////////////////////////////

# end Hank's Lab//////////////////////////////////////////////////////////

# Start player/girl leveling / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Level_Up(Chr=Player):
        if Chr != Player and Chr not in TotalGirls:
            return
        if Chr == Player:
            while Player.StatPoints > 0 or "addict control" in Player.Traits:
                menu:
                    "Ваше количество очков: [Player.StatPoints]. На что вы хотели бы их потратить?"
                    "Повышение сексуальной выносливости. [[Приобретено] (locked)" if "focus" in Player.Traits:
                        pass
                    "Повышение сексуальной выносливости. [[Одно очко]" if "focus" not in Player.Traits:
                        menu:
                            "Эта черта разблокирует вариант \"Сфокусироваться\" во время секса, давая вам больше времени, прежде чем вы кончите."
                            "Открыть фокусировку.":
                                if Player.StatPoints > 0:
                                        $ Player.StatPoints -= 1
                                        $ Player.Traits.append("focus")
                                else:
                                        "Для этого у вас недостаточно очков."
                            "Отмена.":
                                        pass

                    "Повысить эффект зависимости. [[Одно очко]" if "addict control" not in Player.Traits and "nonaddictive" not in Player.Traits and "addictive" not in Player.Traits:
                        menu:
                            "Эта черта повысит эффект привыкания от ваших прикосновений, из-за чего девушкам станет сложнее отказаться от них."
                            "Повысить эффект зависимости.":
                                if Player.StatPoints > 0:
                                        $ Player.StatPoints -= 1
                                        $ Player.Traits.append("addictive")
                                else:
                                        "Для этого у вас недостаточно очков."
                            "Отмена.":
                                        pass

                    "Понизить эффект зависимости. [[Одно очко]" if "addict control" not in Player.Traits and "nonaddictive" not in Player.Traits and "addictive" not in Player.Traits:
                        menu:
                            "Эта черта понизит эффект зависимости от ваших прикосновений, из-за чего девушкам станет проще противостоять им."
                            "Понизить эффект зависимости.":
                                if Player.StatPoints > 0:
                                        $ Player.StatPoints -= 1
                                        $ Player.Traits.append("nonaddictive")
                                else:
                                        "Для этого у вас недостаточно очков."
                            "Отмена.":
                                        pass

                    "Контроль уровня зависимости. [[Два очка]" if "addict control" not in Player.Traits and ("nonaddictive" in Player.Traits or "addictive" in Player.Traits):
                        menu:
                            "Эта черта позволит вам свободно контролировать, какой эффект зависимости будет от ваших прикосновений."
                            "Приобрести контроль уровня зависимости.":
                                if Player.StatPoints >= 2:
                                        $ Player.StatPoints -= 2
                                        $ Player.Traits.append("addict control")
                                else:
                                        "Для этого у вас недостаточно очков."
                            "Отмена.":
                                        pass

                    "Повысить эффект зависимости. [[бесплатно]" if "addict control" in Player.Traits: #If you have Addict-control
                        menu:
                            "Эта черта повысит эффект привыкания от ваших прикосновений, из-за чего девушкам станет сложнее отказаться от них."
                            "Повысить эффект зависимости, бесплатно.":
                                if "nonaddictive" in Player.Traits:
                                        $ Player.Traits.remove("nonaddictive")
                                        "Сейчас у вас стандартный уровень вызывания зависимости."
                                elif "addictive" not in Player.Traits:
                                        $ Player.Traits.append("addictive")
                                        "Сейчас у вас повышенный уровень вызывания зависимости."
                                else:
                                        "Сейчас у вас максимальный уровень вызывания зависимости."
                            "Отмена.":
                                        pass
                    "Понизить эффект зависимости. [[бесплатно]" if "addict control" in Player.Traits:
                        menu:
                            "Эта черта понизит эффект зависимости от ваших прикосновений, из-за чего девушкам станет проще противостоять им."
                            "Понизить эффект зависимости.":
                                if "addictive" in Player.Traits:
                                        $ Player.Traits.remove("addictive")
                                        "Сейчас у вас стандартный уровень вызывания зависимости."
                                elif "nonaddictive" not in Player.Traits:
                                        $ Player.Traits.append("nonaddictive")
                                        "Сейчас у вас пониженный уровень вызывания зависимости."
                                else:
                                        "Сейчас у вас минимальный уровень вызывания зависимости."

                                if "addictive" in Player.Traits:
                                        $ Player.Traits.remove("addictive")
                                        $ Player.Traits.append("nonaddictive")
                                        $ Player.Traits.append("addict control")
                                else:
                                        $ Player.Traits.append("nonaddictive")
                            "Отмена.":
                                        pass

                    "Повысить объем производства спермы. [[Максимум] (locked)" if Player.Semen_Max >= 5 and Player.Male:
                        pass
                    "Повысить объем производства спермы. [[Одно очко]" if Player.Semen_Max < 5 and Player.Male:
                        menu:
                            "Эта черта повысит на единицу количество раз, сколько вы сможете кончить до того, как вам потребуется передышка."
                            "Увеличить количество спермы.":
                                if Player.StatPoints > 0:
                                        $ Player.StatPoints -= 1
                                        $ Player.Semen_Max += 1
                                else:
                                        "Для этого у вас недостаточно очков."
                                if Player.Semen_Max >= 5:
                                        "У вас уже максимальный уровень."
                            "Отмена.":
                                        pass
                    "Повышение сексуального желания. [[Максимум] (locked)" if Player.Semen_Max >= 5 and not Player.Male:
                        pass
                    "Повышение сексуального желания. [[Одно очко]" if Player.Semen_Max < 5 and not Player.Male:
                        menu:
                            "Эта черта повысит на единицу количество раз, сколько вы сможете кончить до того, как вам потребуется передышка."
                            "Повысить сексуальное желание.":
                                if Player.StatPoints > 0:
                                        $ Player.StatPoints -= 1
                                        $ Player.Semen_Max += 1
                                else:
                                        "Для этого у вас недостаточно очков."
                                if Player.Semen_Max >= 5:
                                        "У вас уже максимальный уровень."
                            "Отмена.":
                                        pass

                    "Удвоенный максимум спермы. [[Максимум] (locked)" if "double" in Player.Traits and Player.Male:
                        pass
                    "Удвоенный максимум спермы. [[Два очка]" if Player.Semen_Max == 5 and "double" not in Player.Traits and Player.Male:
                        menu:
                            "Этот признак позволит вам восстанавливать уровень спермы до максимума один раз в день."
                            "Удвоить максимальный запас спермы.":
                                if Player.StatPoints > 1:
                                        $ Player.StatPoints -= 2
                                        $ Player.Traits.append("double")
                                        "Нажмите на иконку \"заряды спермы\" сверху экрана, чтобы восстановить их."
                                else:
                                        "Для этого у вас недостаточно очков."
                            "Отмена.":
                                        pass
                    "Удвоенный максимум сексуального желания [[Максимум] (locked)" if "double" in Player.Traits and not Player.Male:
                        pass
                    "Удвоенный максимум сексуального желания. [[Два очка]" if Player.Semen_Max == 5 and "double" not in Player.Traits and not Player.Male:
                        menu:
                            "Этот признак позволит вам восстанавливать сексуальное желание до максимума один раз в день."
                            "Удвоить максимум желания.":
                                if Player.StatPoints > 1:
                                        $ Player.StatPoints -= 2
                                        $ Player.Traits.append("double")
                                        "Нажмите на иконку \"уровень желания\" сверху экрана, чтобы восстановить его."
                                else:
                                        "Для этого у вас недостаточно очков."
                            "Отмена.":
                                        pass


                    "Неважно, я вернусь позже.":
                                        return
        else:
            #Girls leveling system
            while Chr.StatPoints > 0:
                menu:
                    "[Chr.Name]: уровень [Chr.Lvl] и [Chr.StatPoints] очков. Как бы вы хотели их потратить?"
                    "Повышение сексуальной выносливости. [[Приобретено] (locked)" if "focus" in Chr.Traits:
                        pass
                    "Повышение сексуальной выносливости. [[Одно очко]" if "focus" not in Chr.Traits:
                        menu:
                            "Эта черта разблокирует \"Сфокусироваться\" во время секса, давая [Chr.Name_dat] больше времени до оргазма."
                            "Открыть фокусировку.":
                                if Chr.StatPoints:
                                        $ Chr.StatPoints -= 1
                                        $ Chr.Traits.append("focus")
                                else:
                                        "Для этого у вас недостаточно очков."
                            "Отмена.":
                                pass

                    "[Chr.Name]: повысить сопротивление. [[Максимум] (locked)" if Chr.Resistance >= 3:
                        pass
                    "[Chr.Name]: повысить сопротивление. [[Одно очко]" if 0 < Chr.Resistance < 3:
                        menu:
                            "Эта черта будет увеличит устойчивость [Chr.Name_rod] к вашим прикосновениям."
                            "Увеличить Сопротивление.":
                                if Chr.StatPoints:
                                        $ Chr.StatPoints -= 1
                                        $ Chr.Resistance += 1
                                else:
                                        "Для этого у вас недостаточно очков."
                            "Отмена.":
                                        pass


                    "Увеличение выносливости. [[Максимум] (locked)" if Chr.MaxAction >= 10:
                        pass
                    "Увеличение выносливости. [[Одно очко]" if Chr.MaxAction < 10:
                        "Эта черта увеличит на 2 количество сексуальных действий с ней до того, как ей потребуется передышка."
                        menu:
                            "На текущий момент этот показатель у нее равен [Chr.MaxAction]."
                            "Повысить выносливость.":
                                if Chr.StatPoints:
                                    $ Chr.StatPoints -= 1
                                    $ Chr.MaxAction += 2
                                    if Chr.MaxAction > 10:
                                        $ Chr.MaxAction = 10
                                        "Выносливость [Chr.Name_rod] достигла максимума."
                                else:
                                        "Для этого у вас недостаточно очков."
                            "Отмена.":
                                        pass

                    "[Chr.Name]: свободное прикосновение к другим. [[Приобретено] (locked)" if Chr == RogueX and "touch" in Chr.Traits:
                        pass
                    "[Chr.Name]: свободное прикосновение к другим. [[Одно очко]" if Chr == RogueX and "touch" not in Chr.Traits and Chr.Lvl >= 5:
                        "Эта черта позволит [Chr.Name_dat] прикасаться к другим людям, а не только к вам, не причиняя им вреда."
                        menu:
                            "Она все еще может позаимствовать их способности, если они у них есть."
                            "Разблокировать возможность прикасаться.":
                                if Chr.StatPoints:
                                        $ Chr.StatPoints -= 1
                                        $ Chr.Traits.append("touch")
                                else:
                                        "Для этого у вас недостаточно очков."
                            "Отмена.":
                                        pass

#                    "Allow [Chr.Name] to permanently Steal. [[Two points]" if Chr == RogueX and "touch" in Chr.Traits and "steal" not in Chr.Traits:
#                        "This trait will allow [Chr.Name] to permanently copy one other mutant ability at a time."
#                        menu:
#                            "This does not harm the person she borrows from and can switch abilities with a touch."
#                            "Unlock steal ability.":
#                                if Chr.StatPoints >= 2:
#                                        $ Chr.StatPoints -= 2
#                                        $ Chr.Traits.append("steal")
#                                else:
#                                        "You don't have enough points for that."
#                            "Cancel.":
#                                        pass
                    "Неважно, я вернусь позже.":
                                        return

        return

label Reset_Semen:
        #Resets max semen level once per day
        if "double" in Player.Traits and "double" not in Player.DailyActions:
                $ Player.Semen = 5
                $ Player.DailyActions.append("double")
                $ renpy.restart_interaction()
        return

# End leveling menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Remove Girl / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Remove_Girl(Girl = 0, HideGirl = 1, Hold=0,BO=[]):
        # Girl is the girl being removed, this is for putting girls in a safe location if they run.
        # "Hold" is sent by Present_Check/Girls_Arrive, if active, and you are in public, it sets the girl nearby

        if Girl == "All":
                $ Party = []
                $ Nearby = []
                $ Partner = 0
                $ BO = TotalGirls[:]
        else:
                while Girl in Party:
                        $ Party.remove(Girl)
                while Girl in Present:
                        $ Present.remove(Girl)
                while Girl in Nearby:
                        $ Nearby.remove(Girl)
                if Partner == Girl:
                        $ Partner = 0
                $ BO = [Girl]

        python:
            for BX in BO:
                BX.DrainWord("leaving",1,0,0)
                BX.DrainWord("arriving",1,0,0)

                if BX.Loc == bg_current or (bg_current == "bg classroom" and BX.Loc == "bg teacher") or BX.Loc == "nearby":
                    if Hold and bg_current in ("bg campus","bg classroom","bg dangerroom","bg pool","bg mall"):
                            # "Hold" is sent by Present_Check/Girls_Arrive, if active, and you are in public, it sets the girl nearby
                            if BX not in Nearby:
                                    Nearby.append(BX)
                            BX.Loc = "nearby"
                    elif bg_current == BX.Home:
                            #if you are in the girl's room, send her to the campus
                            if BX is JubesX and JubesX.Addict >= 60:
                                        BX.Loc = "bg showerroom"
                            BX.Loc = "bg campus"
                            Player.DrainWord("locked",0,0,1)
                    else:
                            #if you are not in the girl's room, send her home
                            BX.Loc = BX.Home
                            Player.DrainWord("locked",0,0,1)

                #below portion visually removes girls.
                if HideGirl:
                            renpy.hide(BX.Tag+"_SexSprite")
                            renpy.hide(BX.Tag+"_Doggy_Animation")
                            renpy.hide(BX.Tag+"_HJ_Animation")
                            renpy.hide(BX.Tag+"_BJ_Animation")
                            renpy.hide(BX.Tag+"_TJ_Animation")
                            renpy.hide(BX.Tag+"_Finger_Animation")
                            renpy.hide(BX.Tag+"_CUN_Animation")
                            renpy.hide(BX.Tag+"_69_Animation")
                            renpy.hide(BX.Tag+"_69_CUN")
                            renpy.hide(BX.Tag+"_SC_Sprite")
                            renpy.hide(BX.Tag+"_PJ_Animation") #Jean, mainly
                            renpy.hide(BX.Tag+"_FJ_Animation") #Emma, mainly
                            renpy.hide(BX.Tag+"_Seated")
                            renpy.hide(BX.Tag+"_Sprite")
        return
# End Remove Girl / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Clear the Room / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label CleartheRoom(Character = 0, Passive = 0, Silent = 0, Girls=[],BO=[]): #rkeljsvgb
        #This is intended to clear the room of non-essential characters
        #the named character is the one who stays, everyone else is kicked out.
        #Character is the one asking to clear the room.
        #Passive is when the second person leaves on their own.
        #Silent removes dialog
        # call CleartheRoom(RogueX,1,1)

        #this populates a list of other girls at the current location
#        if not Silent and bg_current not in PersonalRooms and Time_Count <= 1:
#                    #if it's not a player room and it's not evening+, give up on whatever this is supposed to be
#                    #Fix this mess, It's breaking Kitty's intro scene anyway. . .
#                    jump Misplaced

        $ BO = TotalGirls[:]
        $ BO.remove(Character) if Character in TotalGirls else BO
        python:
            for BX in BO:
                if BX.Loc == bg_current or BX in Party:
                        #if she is at current location, or in your Party
                        Girls.append(BX)
                elif BX.Loc == "bg teacher" and bg_current == "bg classroom":
                        #or is not the character asking people to leave, but is in a teacher role in class. . .
                        Girls.append(BX)
                BX.DrainWord("leaving",1,0,0)
                BX.DrainWord("arriving",1,0,0)

        $ Nearby = [] #empties the nearby list
        $ Present = []

        if not Silent and not Passive:
                #this section asks a question that a later phase will answer
                if Character.Loc != bg_current:
                        "[Character.Name] входит в комнату."
                        $ Character.Loc = bg_current
                if not Girls:
                        #if there is no other girl. . .
                        if Character in TotalGirls:
                                call Display_Girl(Character)
                        return
                if Character is RogueX:
                        # if the clearing character is Rogue
                        if len(Girls) > 1:
                            #if there is at least two other girls. . .
                            ch_r "Дамы, могу я поговорить с [Player.Name_tvo] наедине?"
                        elif Girls:
                            ch_r "[Girls[0].Name], могу я поговорить с [Player.Name_tvo] наедине?"
                elif Character == KittyX:
                        if len(Girls) > 1:
                            ch_k "Девочки, могу я немного поговорить с [Player.Name_tvo] наедине?"
                        elif Girls:
                            ch_k "[Girls[0].Name], могу я немного поговорить с [Player.Name_tvo] наедине?"
                elif Character == EmmaX:
                        if len(Girls) > 1:
                            ch_e "Девочки, вы позволите мне поговорить с [Player.Name_tvo] наедине?"
                        elif Girls:
                            ch_e "[Girls[0].Name], ты позволишь мне поговорить с [Player.Name_tvo] наедине?"
                elif Character == LauraX:
                        if len(Girls) > 1:
                            ch_l "Эй, убирайтесь, мне нужно поговорить с [Player.Name_tvo]."
                        elif Girls:
                            ch_l "[Girls[0].Name], убирайся, мне нужно поговорить с [Player.Name_tvo]."
                elif Character == JeanX:
                        if len(Girls) > 1:
                            ch_j "Дамы, освободите комнату."
                        elif Girls:
                            ch_j "Эй ты, выйди."
                elif Character == StormX:
                        if len(Girls) > 1:
                            ch_s "Не могли бы вы освободить комнату, дамы?"
                        elif Girls:
                            ch_s "[Girls[0].Name], не могла бы ты освободить комнату? Мне нужно поговорить с [Player.Name_tvo]."
                elif Character == JubesX:
                        if len(Girls) > 1:
                            ch_v "Эй, не могли бы вы, девочки, выйти? Мне нужно поговорить с [Player.Name_tvo]."
                        elif Girls:
                            ch_v "Эй, [Girls[0].Name], не могла бы ты выйти? Мне нужно поговорить с [Player.Name_tvo]."
                elif Character == GwenX:
                        if len(Girls) > 1:
                            ch_g "Ладно, дамы, освободите комнату, мне нужно поговорить с [Player.Name_tvo]."
                        elif Girls:
                            ch_g "Слушай, [Girls[0].Name], освободишь комнату на пару секунд? Мне нужно поговорить с [Player.Name_tvo]."
                elif Character is BetsyX:
                        if len(Girls) > 1:
                            ch_b "Дамы, можете выйти? Мне нужно поговорить с [Player.Name_tvo] наедине."
                        elif Girls:
                            ch_b "Пардон, [Girls[0].Name], но не могла бы ты выйти? Мне нужно поговорить с [Player.Name_tvo]."
                elif Character is DoreenX:
                        if len(Girls) > 1:
                            ch_d "Эм, девочки, не могли бы вы ненадолго выйти? Мне нужно поговорить с [Player.Name_tvo]."
                        elif Girls:
                            ch_d "Эм, [Girls[0].Name], не могла бы ты ненадолго выйти? Мне нужно поговорить с [Player.Name_tvo]."
                elif Character is WandaX:
                        if len(Girls) > 1:
                            ch_w "Дамы, внимание, не могли бы вы выйти на минутку? Мне нужно поговорить с [Player.Name_tvo]."
                        elif Girls:
                            ch_w "Слушай, [Girls[0].Name], не могла бы ты выйти на минутку? Мне нужно поговорить с [Player.Name_tvo]."
        #end portion asking about each girl

        $ renpy.random.shuffle(Girls)
        while Girls:
                while Girls[0] in Party:
                        $ Party.remove(Girls[0])
                $ Girls[0].DrainWord("leaving",1,0,0)
                $ Girls[0].DrainWord("arriving",1,0,0)

                if Silent:
                        pass
                elif not Passive and Character != "All":
                        #if there are other girls. . .
                        if Girls[0] is RogueX:
                                ch_r "Без проблем, увидимся позже."
                        elif Girls[0] is KittyX:
                                ch_k "[KittyX.Like]конечно, увидимся позже."
                        elif Girls[0] is EmmaX:
                                ch_e "Ладно, увидимся позже."
                        elif Girls[0] is LauraX:
                                ch_l "Хорошо. Я ухожу."
                        elif Girls[0] is JeanX:
                                ch_j "Я притворюсь, что ты мне не нагрубила. . ."
                        elif Girls[0] is StormX:
                                ch_s "Увидимся позже. . ."
                        elif Girls[0] is JubesX:
                                ch_v "Удаляюсь. . ."
                        elif Girls[0] is GwenX:
                                ch_g "Тогда я пошла. . ."
                        elif Girls[0] is BetsyX:
                                ch_b "Конечно. . ."
                        elif Girls[0] is DoreenX:
                                ch_d "Хорошо. . ."
                        elif Girls[0] is WandaX:
                                ch_w "Конечно."
                else:
                        if Girls[0] is RogueX:
                                ch_r "Мне пора идти, увидимся позже, [RogueX.Petname]."
                        elif Girls[0] is KittyX:
                                ch_k "Думаю, мне пора, увидимся позже."
                        elif Girls[0] is EmmaX:
                                ch_e "Пожалуй, мне пора идти."
                        elif Girls[0] is LauraX:
                                ch_l "Я ухожу."
                        elif Girls[0] is JeanX:
                                "[JeanX.Name] уходит."
                        elif Girls[0] is StormX:
                                ch_s "Я должна идти. . ."
                        elif Girls[0] is JubesX:
                                ch_v "Удаляюсь. . ."
                        elif Girls[0] is GwenX:
                                ch_g "Мне нужно идти. . ."
                        elif Girls[0] is BetsyX:
                                ch_b "Я пойду. . ."
                        elif Girls[0] is DoreenX:
                                ch_d "Мне нужно идти. . ."
                        elif Girls[0] is WandaX:
                                ch_w "Увидимся позже."

                if bg_current == Girls[0].Home:
                                $ Girls[0].Loc = "bg campus"
                else:
                                $ Girls[0].Loc = Girls[0].Home

                call Girl_Hide(Girls[0],1) # call expression Girls[0].Tag + "_Hide" pass (1) #hides the sex sprites
                $ Girls.remove(Girls[0])
        if Character in TotalGirls:
                call Display_Girl(Character)
        call Taboo_Level
        return

# End Clear the Room / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Girls Location / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girls_Location(GirlsNum = 0, Change=0, BOptions=[]):
        #this figures out where girls are and where to put spares.
        #it's called most often by Locations, after Waits
        #Girlsnum sets the number of girls that have already talked
        #"arriving" is set by the "Schedule" code, and will not be applied unless
        # the girl in questions was someplace else, and just showed up here on their own.

        $ BOptions = TotalGirls[:]
        $ renpy.random.shuffle(BOptions)
        while BOptions:
                #cycles through each girl possible, adds them to the local area if possible
                if "leaving" in BOptions[0].RecentActions and BOptions[0].Loc != bg_current:
                        if "sleepover" in BOptions[0].Traits:
                                $ BOptions[0].DrainWord("sleepover",0,0,1)  #remove from Traits
                        call expression BOptions[0].Tag + "_Leave" #call Rogue_Leave
                        if BOptions[0].Loc != bg_current:
                                if BOptions[0] in Present:
                                        $ Present.remove(BOptions[0])
                                $ Change = 1
                        $ GirlsNum += 1
                #if Girl was in Nearby, but was moved to a new location
                if BOptions[0] in Nearby and BOptions[0].Loc != "nearby": #and BOptions[0].Loc != bg_current
                                $ Nearby.remove(BOptions[0])
                $ BOptions.remove(BOptions[0])

#        if "Storm" in ActiveGirls and StormX.Loc == "bg teacher" and EmmaX.Loc == "bg teacher":
#                    # Swaps Storm in for Emma if she's available
#                    $ EmmaX.Loc = "bg emma"

        if Change:
            #if there are any fewer girls than there were, Set the Scene
            call Set_The_Scene(Dress=0)

        $ BOptions = TotalGirls[:]
        while BOptions:
                        if "arriving" in BOptions[0].RecentActions:
                                call Girls_Arrive
                                return
                        $ BOptions.remove(BOptions[0])
        return

# End Girls Location / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Girls Arrive / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girls_Arrive(Primary = 0, Secondary = 0, GirlsNum = 0,BO=[]): #rkeljsvgb
        # Called by Girls_Location after a Wait period
        #"arriving" is set by the "Schedule" code, and will not be applied unless
        # the girl in questions was someplace else, and just showed up here on their own.
        # Present contains all girls already local

        $ Options = []

        call Present_Check
        $ BO = Present[:]
        while BO:
                #Each girl trying to arrive is added to the Options, I'll leave this while because it's small
                if "arriving" in BO[0].RecentActions and BO[0] not in Party:
                        $ GirlsNum += 1
                        $ Options.append(BO[0])
                $ BO[0].DrainWord("arriving")
                $ BO.remove(BO[0])

        if not Options:
                #If there are no incoming girl options, then no point to the rest
                return


#        if len(Options) <= 0 or (len(Party)+len(Present)) >= 2:    ##should be unnecesary as Present_Check should cull extra characters
#                    #If nobody's here, or if the space is full, return
#                    return
#        elif (len(Party)+len(Present)) <= 1:
#                    #if the party is one or less and people are in the room

        $ renpy.random.shuffle(Options)
        $ Primary = Options[0]
        if len(Options) >= 2:
                #if 2+ people are arriving
                if bg_current == Options[1].Home:       #if you're in Options[0]'s room,
                        $ Primary = Options[1]
                        $ Secondary = Options[0]
                else:
                        $ Secondary = Options[1]

        if Secondary not in TotalGirls:
                $ Secondary = 0
        $ Options = []

        if "locked" in Player.Traits:
                if Primary == KittyX:
                        call Locked_Door(KittyX)
                        if KittyX.Loc != bg_current:
                            $ Primary = 0
                        elif Secondary:
                            #since Kitty can just barge right in, if she does so,
                            "Вы слышите \"удар\", как будто кто-то пытался проследовать за Китти."
                            call Locked_Door(Secondary)
                            if Secondary.Loc != bg_current:
                                    $ Secondary = 0
                elif Primary.Home == bg_current:
                        #if it's the girl's room. . .
                        "Вы слышите, как ключ поворачивается в замке"
                else:
                        call Locked_Door(Primary)
                        if Primary.Loc != bg_current:
                            $ Primary = 0
        #End "if the door was locked."

        if not Primary:
                return

        #This sequence sets the pecking order, more important once there are more girls
        #girls left out of this are put into "Nearby" for the current space

        call Shift_Focus(Primary)
        if bg_current == "bg dangerroom":
                    #call Gym_Clothes("auto")
                    #puts incoming girls into gym clothes
                    $ Primary.Outfit = "gym"
                    $ Primary.OutfitChange()
                    if Secondary:
                            $ Secondary.Outfit = "gym"
                            $ Secondary.OutfitChange()

        call Set_The_Scene #causes the girls to display
        if bg_current == "bg player":
                    if Secondary:
                            #if there's a second girl
                            "[Primary.Name] с [Secondary.Name_tvo] входят в вашу комнату."
                    else:
                            #if there's no second girl,
                            "[Primary.Name] входит в вашу комнату."

                    if Primary is RogueX:
                                if Secondary:
                                    ch_r "Привет, [Primary.Petname], мы можем войти?"
                                else:
                                    ch_r "Привет, [Primary.Petname], я могу войти?"
                    elif Primary is KittyX:
                                if Secondary:
                                    ch_k "Привет[KittyX.like]мы можем войти?"
                                else:
                                    ch_k "Привет[KittyX.like]можно мне войти?"
                    elif Primary is EmmaX:
                                if Secondary:
                                    ch_e "Ах, хорошо, что ты здесь. Можно нам войти?"
                                else:
                                    ch_e "Ах, хорошо, что ты здесь. Можно мне войти?"
                    elif Primary is LauraX:
                                    ch_l "Привет."
                                    ch_p ". . . [[Похоже, она хочет остаться]."
                    elif Primary is JeanX:
                                    ch_j "Привет, [Primary.Petname]."
                                    ch_p ". . . [[Ладно, она никуда не собирается уходить]."
                    elif Primary is StormX:
                                if Secondary:
                                    ch_s "Замечательно, ты здесь. Можно нам войти?"
                                else:
                                    ch_s "Замечательно, ты здесь. Можно мне войти?"
                    elif Primary is JubesX:
                                if Secondary:
                                    ch_v "О, привет, не возражаешь, если мы войдем?"
                                else:
                                    ch_v "О, привет, не возражаешь, если я войду?"
                    elif Primary is GwenX:
                                if Secondary:
                                    ch_g "Привет, ты не занят? Мы можем составить тебе компанию?"
                                else:
                                    ch_g "Привет, ты не занят? Я могу составить тебе компанию?"
                    elif Primary is BetsyX:
                                if Secondary:
                                    ch_b "Здравствуй, [Primary.Petname]! Ты не возражаешь, если мы зайдем на минутку?"
                                else:
                                    ch_b "Здравствуй, [Primary.Petname]! Ты не возражаешь, если я зайду на минутку?"
                    elif Primary is DoreenX:
                                if Secondary:
                                    ch_d "Привет, [Primary.Petname]! Можно мы войдем?"
                                else:
                                    ch_d "Привет, [Primary.Petname]! Можно я войду?"
                    elif Primary is WandaX:
#                                if Secondary:
#                                    ch_w "Hey, [Primary.Petname]! Can we come in?"
#                                else:
                                    ch_w "Привет, [Primary.Petname]."
                    menu:
                        extend ""
                        "Конечно.":
                            $ Line = "sure"
                        "Не сейчас. Возможно, позже.":
                            $ Line = "later"
                        "Я против.":
                            $ Line = "no"

                    if Line == "sure":
                            $ Primary.Statup("Love", 80, 1)
                            $ Primary.Statup("Obed", 50, 2)
                            $ Primary.Statup("Inbt", 50, 2)
                            if Primary is RogueX:
                                    ch_r "Спасибо."
                            elif Primary is KittyX:
                                    $ KittyX.Statup("Inbt", 50, 1)
                                    ch_k "Круто."
                            elif Primary is EmmaX:
                                    ch_e "Хорошо."
                            elif Primary is LauraX:
                                    $ LauraX.Statup("Love", 50, 1)
                                    $ LauraX.Statup("Obed", 60, 1)
                                    "Она не уходит."
                            elif Primary is JeanX:
                                    "Она не уходит."
                            elif Primary is StormX:
                                    ch_s "Хорошо."
                            elif Primary is JubesX:
                                    ch_v "Отлично."
                            elif Primary is GwenX:
                                    ch_g "Круто."
                            elif Primary is BetsyX:
                                    ch_b "Замечательно."
                            elif Primary is DoreenX:
                                    ch_d "Здорово!"
                            elif Primary is WandaX:
                                    ch_w "Клево."
                            if Secondary:
                                    $ Secondary.Statup("Love", 80, 1)
                                    $ Secondary.Statup("Obed", 50, 2)
                                    $ Secondary.Statup("Inbt", 50, 2)
                            #end "sure"
                    if Line == "later":
                            $ Primary.Statup("Love", 60, -1, 1)
                            $ Primary.Statup("Obed", 70, 5)
                            $ Primary.FaceChange("confused")
                            if Primary is EmmaX or Secondary is EmmaX:
                                    $ EmmaX.Statup("Love", 90, -2)
                                    $ EmmaX.Statup("Obed", 30, -7)
                                    ch_e "Если ты так этого хочешь. . ."
                            if Primary is LauraX or Secondary is LauraX:
                                    $ LauraX.Statup("Love", 90, -2)
                                    $ LauraX.Statup("Obed", 30, -7)
                                    ch_l "Ладно, тогда в другой раз."
                            if Primary is StormX or Secondary is StormX:
                                    if not Player.Male:
                                        ch_s "Ах, тогда мы оставим тебя."
                                    else:
                                        ch_s "Ах, тогда мы оставим тебя одного."
                            if Primary is JubesX or Secondary is JubesX:
                                    ch_v "Ох. Ладно. . ."
                            if Primary is GwenX or Secondary is GwenX:
                                    ch_g "Ох. . . без проблем. . ."
                            if Primary is BetsyX or Secondary is BetsyX:
                                    ch_b "Ох, ну хорошо."
                            if Primary is DoreenX or Secondary is DoreenX:
                                    ch_d "Ох. . . ладно."
                            if Primary is WandaX or Secondary is WandaX:
                                        ch_w "Ох. Как скажешь."

                            if Secondary and Secondary is not JeanX:
                                    $ Secondary.Statup("Love", 60, -1, 1)
                                    $ Secondary.Statup("Obed", 70, 5)
                                    $ Secondary.FaceChange("confused")
                                    if Primary is RogueX:
                                            ch_r "Эм, ладно, тогда мы пойдем."
                                    elif Primary is KittyX:
                                            $ KittyX.Statup("Love", 60, -1, 1)
                                            $ KittyX.Statup("Obed", 70, 2)
                                            ch_k "Ох[KittyX.like]тогда мы пойдем."
                                    call Remove_Girl(Secondary)
                            else:
                                    if Primary is RogueX:
                                            ch_r "Эм, ладно."
                                    elif Primary is KittyX:
                                            $ KittyX.Statup("Love", 60, -1, 1)
                                            $ KittyX.Statup("Obed", 70, 2)
                                            ch_k "Ох[KittyX.like]тогда я пойду."

                            if Primary is JeanX or Secondary is JeanX:
                                    ch_j "Угу-м."
                                    "Она не уходит."
                            if Primary is not JeanX:
                                    call Remove_Girl(Primary)
                            #end "later"
                    if Line == "no":
                            $ Primary.Statup("Obed", 50, 5)
                            if ApprovalCheck(Primary, 1800) or ApprovalCheck(Primary, 500, "O"):
                                # She accepts it
                                $ Primary.Statup("Obed", 80, 2)
                                if Primary is RogueX:
                                        ch_r "Думаю, это нормально. Тогда увидимся позже."
                                elif Primary is KittyX:
                                        ch_k "Ну, если ты хочешь побыть в одиночестве. . ."
                                elif Primary is EmmaX:
                                        $ EmmaX.Statup("Obed", 50, 2)
                                        ch_e "Полагаю, ты имеешь право на личное пространство. . ."
                                elif Primary is LauraX:
                                        ch_l "Без проблем."
                                elif Primary is StormX:
                                        ch_s ". . .  хорошо. . ."
                                elif Primary is JubesX:
                                        ch_v "Ох. Ладно. . ."
                                elif Primary is GwenX:
                                        ch_g "Ох. . . без проблем. . ."
                                elif Primary is BetsyX:
                                        ch_b "Ох, ну хорошо."
                                elif Primary is DoreenX:
                                        ch_d "Ох. . . ладно."
                                elif Primary is WandaX:
                                        ch_w "Ох, как скажешь."
                            else:
                                $ Primary.FaceChange("angry")
                                $ Primary.Statup("Love", 60, -5, 1)
                                $ Primary.Statup("Love", 80, -2)
                                $ Primary.Statup("Obed", 80, 3)
                                $ Primary.Statup("Inbt", 50, 1)
                                if Primary is RogueX:
                                        ch_r "Ну и ладно!"
                                elif Primary is KittyX:
                                        $ KittyX.Statup("Love", 80, -2)
                                        $ KittyX.Statup("Obed", 80, 2)
                                        if not Player.Male:
                                            ch_k "Ну и дура!"
                                        else:
                                            ch_k "Придурок!"
                                elif Primary is EmmaX:
                                        $ EmmaX.Statup("Love", 90, -2)
                                        $ EmmaX.Statup("Obed", 80, 3)
                                        ch_e "Посмотрим, как долго я смогу тебя терпеть, при таком отношение. . ."
                                elif Primary is LauraX:
                                        $ LauraX.Statup("Love", 90, -2)
                                        "Она выглядит расстроенной."
                                elif Primary is StormX:
                                        ch_s ". . . Я поняла. . ."
                                elif Primary is JubesX:
                                        if not Player.Male:
                                            ch_v "Ох, значит ты будешь вот -такой-. . .?"
                                        else:
                                            ch_v "Ох, значит ты будешь вот -таким-. . .?"
                                elif Primary is GwenX:
                                        ch_g "Наверное, у тебя другие планы. . ."
                                elif Primary is BetsyX:
                                        ch_b "Ну раз у тебя -другие- планы. . ."
                                elif Primary is DoreenX:
                                        ch_d "Ну. . . ладно."
                                elif Primary is WandaX:
                                        ch_w "Ох. Все понятно. . ."
                            if Primary is JeanX or Secondary is JeanX:
                                    ch_j "Угу-м."
                                    "Она не уходит."
                            if Primary is not JeanX:
                                    call Remove_Girl(Primary)
                            if Secondary and Secondary is not JeanX:
                                    $ Secondary.Statup("Obed", 50, 5)
                                    if ApprovalCheck(Secondary, 1800) or ApprovalCheck(Secondary, 500, "O"):
                                        $ Secondary.Statup("Obed", 80, 2)
                                        if Secondary is RogueX:
                                                ch_r "Думаю, это нормально. Тогда увидимся позже."
                                        elif Secondary is KittyX:
                                                ch_k "Ну, если ты хочешь побыть в одиночестве. . ."
                                        elif Secondary is EmmaX:
                                                $ EmmaX.Statup("Obed", 50, 2)
                                                ch_e "Полагаю, ты имеешь право на личное пространство. . ."
                                        elif Secondary is LauraX:
                                                ch_l "Без проблем."
                                        elif Primary is StormX:
                                                ch_s ". . . хорошо. . ."
                                        elif Primary is JubesX:
                                                ch_v "Ох. Ладно. . ."
                                        elif Primary is GwenX:
                                                ch_g "Ох. . . без проблем. . ."
                                        elif Secondary is BetsyX:
                                                ch_b "Ох, ну хорошо."
                                        elif Secondary is DoreenX:
                                                ch_d "Ох. . . ладно."
                                        elif Secondary is WandaX:
                                                ch_w "Ох, как скажешь."
                                    else:
                                        $ Secondary.FaceChange("angry")
                                        $ Secondary.Statup("Love", 60, -5, 1)
                                        $ Secondary.Statup("Love", 80, -2)
                                        $ Secondary.Statup("Obed", 80, 3)
                                        $ Secondary.Statup("Inbt", 50, 1)
                                        if Secondary is RogueX:
                                                ch_r "Ну и ладно!"
                                        elif Secondary is KittyX:
                                                $ KittyX.Statup("Love", 80, -2)
                                                $ KittyX.Statup("Obed", 80, 2)
                                                if not Player.Male:
                                                    ch_k "Ну и дура!"
                                                else:
                                                    ch_k "Придурок!"
                                        elif Secondary is EmmaX:
                                                $ EmmaX.Statup("Love", 90, -2)
                                                $ EmmaX.Statup("Obed", 80, 3)
                                                ch_e "Посмотрим, как долго я смогу тебя терпеть, при таком отношение. . ."
                                        elif Secondary is LauraX:
                                                $ LauraX.Statup("Love", 90, -2)
                                                "Она выглядит расстроенной."
                                        elif Secondary is StormX:
                                                ch_s ". . . Я поняла. . ."
                                        elif Secondary is JubesX:
                                                if not Player.Male:
                                                    ch_v "Ох, значит ты будешь вот -такой-. . .?"
                                                else:
                                                    ch_v "Ох, значит ты будешь вот -таким-. . .?"
                                        elif Secondary is GwenX:
                                                $ Primary.Statup("Inbt", 50, 1)
                                                ch_g "Наверное, у тебя другие планы. . ."
                                        elif Secondary is BetsyX:
                                                ch_b "Ну раз у тебя -другие- планы. . ."
                                        elif Secondary is DoreenX:
                                                ch_d "Ну. . . ладно."
                                        elif Secondary is WandaX:
                                                ch_w "Ох, ну понятно. . ."
                                    call Remove_Girl(Secondary)
                                    if Primary is JeanX:
                                            "[Secondary.Name] убегает."
                                    else:
                                            "Девчонки убегают."
                        #end "nope"
                    #end girls showed up to player's room.

        elif bg_current in PersonalRooms:
                    #if you show up at one of the girls' rooms
                    if Secondary:
                            #if there's a second girl
                            "[Primary.Name] с [Secondary.Name_tvo] входят в комнату."
                    else:
                            #if there's no second girl,
                            "[Primary.Name] входит в комнату."
                    if bg_current == Primary.Home:
                                    if "angry" in Primary.DailyActions:
                                            #She's angry
                                            $ Primary.FaceChange("bemused", 1,Brows="angry")
                                            if Primary is RogueX:
                                                            ch_r "Я зла на тебя, убирайся."
                                            elif Primary is KittyX:
                                                            ch_k "Тебе не должно здесь быть, уходи."
                                            elif Primary is EmmaX:
                                                            if not Player.Male:
                                                                ch_e "Я не думаю, что ты должна быть здесь, уходи."
                                                            else:
                                                                ch_e "Я не думаю, что ты должен быть здесь, уходи."
                                            elif Primary is LauraX:
                                                            if not Player.Male:
                                                                ch_l "Ты должна уйти, пока можешь."
                                                            else:
                                                                ch_l "Ты должен уйти, пока можешь."
                                            elif Primary is JeanX:
                                                            ch_j "Я не в настроении."
                                            elif Primary is StormX:
                                                            ch_s "Для тебя сейчас здесь не безопасно. . ."
                                            elif Primary is JubesX:
                                                            ch_v "\"Не ступай в мое логово\". . ."
                                            elif Primary is GwenX:
                                                            ch_g "Мне надоели твои глупости! Вон!"
                                            elif Primary is BetsyX:
                                                            ch_b "В данный момент у меня совсем нет на тебя времени. Уходи."
                                            elif Primary is DoreenX:
                                                            ch_d "Я хочу отдохнуть от тебя."
                                            elif Primary is WandaX:
                                                            ch_w "Тебя сейчас никто не приглашал."

                                    elif Time_Count >= 3 and ApprovalCheck(Primary, 1000, "LI") and ApprovalCheck(Primary, 600, "OI"):
                                            #it's night and she likes you
                                            pass #this argument is had over in the Round10 label
                                            call AnyLine(Primary,"О, привет, "+Primary.Petname+".")
#                                            if Primary is RogueX:
#                                                            ch_r "Oh, hey, [RogueX.Petname], it's pretty late, but I guess you can stick around for a bit."
#                                            elif Primary is KittyX:
#                                                            ch_k "Oh, hey, it's kinds late, but you can stay for a bit."
#                                            elif Primary is EmmaX:
#                                                            ch_e "Oh, it's a bit late, but you're welcome."
#                                            elif Primary is LauraX:
#                                                            ch_l "It's late."
#                                            elif Primary is JeanX:
#                                                            ch_j "Oh, you know what time it is, right?"
#                                            elif Primary is StormX:
#                                                            ch_s "Delightful to see you, but the hour is late. . ."
#                                            elif Primary is JubesX:
#                                                            ch_v "Kinda late, [JubesX.Petname], s'up?"
#                                            elif Primary is GwenX:
#                                                            ch_g "Oh! What are you doing here in the middle of the night?"
#                                            elif Primary is BetsyX:
#                                                            ch_b "It's rather late, was there something you needed?"
#                                            elif Primary is DoreenX:
#                                                            ch_d "It's pretty late, but could I help you with something?"
#                                            elif Primary is WandaX:
#                                                            ch_w "It's kinda late, but what'd you want?"
                                            $ Line = "stay"
                                    elif ApprovalCheck(Primary, 1300) or ApprovalCheck(Primary, 500, "O") or Primary == JubesX:
                                            #it's not night and she likes you
                                            if Primary is RogueX:
                                                            ch_r "О, привет, [RogueX.Petname], рада видеть тебя здесь."
                                            elif Primary is KittyX:
                                                            ch_k "О, привет, рада тебя видеть."
                                            elif Primary is EmmaX:
                                                            ch_e "Ох, рада тебя видеть."
                                            elif Primary is LauraX:
                                                            ch_l "О, привет."
                                            elif Primary is JeanX:
                                                            ch_j "О, привет?"
                                            elif Primary is StormX:
                                                            ch_s "Рада тебя видеть."
                                            elif Primary is JubesX:
                                                            ch_v "Привет, [JubesX.Petname], в чем дело?"
                                            elif Primary is GwenX:
                                                            if not Player.Male:
                                                                ch_g "Ох, решила зайти в гости?"
                                                            else:
                                                                ch_g "Ох, решил зайти в гости?"
                                            elif Primary is BetsyX:
                                                            ch_b "Ох, здравствуй. Ты что-то хочешь?"
                                            elif Primary is DoreenX:
                                                            ch_d "О, привет, тебе что-то нужно?"
                                            elif Primary is WandaX:
                                                            if not Player.Male:
                                                                ch_w "Привет, ты чего-то хотела?"
                                                            else:
                                                                ch_w "Привет, ты чего-то хотел?"
                                            $ Line = "stay"
                                    elif Time_Count >= 3:
                                            #it's night and she wants you gone
                                            call AnyLine(Primary,"О, привет, "+Primary.Petname+".")
                                            pass #this argument is had over in the Round10 label
#                                            if Primary is RogueX:
#                                                            ch_r "Oh, hey, [RogueX.Petname], it's kind late, could you head out of here?"
#                                            elif Primary is KittyX:
#                                                            ch_k "Oh, hey, [KittyX.Petname]. It's kind of late, could you come back tomorrow?"
#                                            elif Primary is EmmaX:
#                                                            ch_e "Oh, hello, [EmmaX.Petname]. It's a bit late, could you come back tomorrow?"
#                                            elif Primary is LauraX:
#                                                            ch_l "Oh, hey, it's late."
#                                            elif Primary is JeanX:
#                                                            ch_j "You -can- tell time, right?"
#                                            elif Primary is StormX:
#                                                            ch_s "I'm afraid that the hour is a bit late for visits. . ."
#                                            #elif Primary is JubesX:
#                                                            #not a factor since she does not sleep
#                                            elif Primary is GwenX:
#                                                            ch_g "It's kinda late to be hanging out, [GwenX.Petname]."
#                                            elif Primary is BetsyX:
#                                                            ch_b "It's rather late, I was hoping to retire early."
#                                            elif Primary is DoreenX:
#                                                            ch_d "It's pretty late, maybe tomorrow?"
#                                            elif Primary is WandaX:
#                                                            ch_w "It's kinda late, see you tomorrow?"
                                    elif ApprovalCheck(Primary, 600, "LI") or ApprovalCheck(Primary, 300, "OI"):
                                            #it's not night and she's neutral
                                            if Primary is RogueX:
                                                            ch_r "О, привет, [Primary.Petname]. Думаю, ты можешь остаться."
                                            elif Primary is KittyX:
                                                            ch_k "О, привет, [Primary.Petname], что случилось?"
                                            elif Primary is EmmaX:
                                                            ch_e "Ох, здравствуй, [Primary.Petname], чем я могу тебе помочь?"
                                            elif Primary is LauraX:
                                                            ch_l "О, привет, [Primary.Petname]."
                                            elif Primary is JeanX:
                                                            ch_j "Эм, привет?"
                                            elif Primary is StormX:
                                                            ch_s "Да? Тебе что-то нужно?"
                                            elif Primary is JubesX:
                                                            ch_v "Привет, [Primary.Petname], в чем дело?"
                                            elif Primary is GwenX:
                                                            ch_g "О, привет, ты в моей комнате. . ."
                                            elif Primary is BetsyX:
                                                            ch_b "О, здравствуй. Я не ожидала застать тебя в своей комнате."
                                            elif Primary is DoreenX:
                                                            ch_d "Эм, привет?"
                                            elif Primary is WandaX:
                                                            ch_w "О, привет, [Primary.Petname]."
                                            $ Line = "stay"
                                    else:
                                            #she wants you gone
                                            if Primary is RogueX:
                                                            if not Player.Male:
                                                                ch_r "Привет, [RogueX.Petname], я не знаю, зачем ты здесь, но я бы предпочла, чтобы ты ушла."
                                                            else:
                                                                ch_r "Привет, [RogueX.Petname], я не знаю, зачем ты здесь, но я бы предпочла, чтобы ты ушел."
                                            elif Primary is KittyX:
                                                            ch_k "Привет, [KittyX.Petname], что ты вообще здесь делаешь?"
                                                            if not Player.Male:
                                                                ch_k "Не могла бы ты[KittyX.like]уйти?"
                                                            else:
                                                                ch_k "Не мог бы ты[KittyX.like]уйти?"
                                            elif Primary is EmmaX:
                                                            ch_e "О, здравствуй, [EmmaX.Petname]?"
                                                            if not Player.Male:
                                                                ch_e "Ну и зачем ты зашла?"
                                                            else:
                                                                ch_e "Ну и зачем ты зашел?"
                                            elif Primary is LauraX:
                                                            $ Primary.FaceChange("confused")
                                                            ch_l "Привет, [LauraX.Petname], зачем ты здесь?"
                                            elif Primary is JeanX:
                                                            $ Primary.FaceChange("confused")
                                                            ch_j "Я не приглашала тебя сюда."
                                            elif Primary is StormX:
                                                            ch_s "Боюсь, что сейчас не самое подходящее время."
                                            elif Primary is JubesX:
                                                            ch_v "Привет, [JubesX.Petname]? Сейчас не самое удачное время."
                                            elif Primary is GwenX:
                                                            if not Player.Male:
                                                                ch_g "Эм? Не могла бы ты выйти из моей комнаты?"
                                                            else:
                                                                ch_g "Эм? Не мог бы ты выйти из моей комнаты?"
                                            elif Primary is BetsyX:
                                                            ch_b "Я не ожидала, что застану. . . незванных гостей."
                                            elif Primary is DoreenX:
                                                            if not Player.Male:
                                                                ch_d "Не ожидала тебя здесь увидеть. Не могла бы ты уйти?"
                                                            else:
                                                                ch_d "Не ожидала тебя здесь увидеть. Не мог бы ты уйти?"
                                            elif Primary is WandaX:
                                                            ch_w "Нам лучше увидеться попозже."
                                    if Line != "stay":
                                        #if she asked you to leave. . .
                                        menu:
                                            extend ""
                                            "Конечно. [[вы уходите]":
                                                        $ Primary.Statup("Love", 80, 1)
                                                        $ Primary.Statup("Obed", 50, 2)
                                                        $ Primary.Statup("Inbt", 50, 2)
                                                        call AnyLine(Primary,"Спасибо.")
                                                        "Вы возвращаетесь в свою комнату."
                                            "Извини, я уже ухожу.":
                                                        $ Primary.Statup("Love", 90, 2)
                                                        $ Primary.Statup("Obed", 50, 3)
                                                        $ Primary.FaceChange("smile")
                                                        call AnyLine(Primary,"Спасибо.")
                                                        "Вы возвращаетесь в свою комнату."
                                            "Ты уверена, что я не могу остаться?":
                                                        if "angry" in Primary.DailyActions:
                                                                $ Primary.FaceChange("angry")
                                                                if Primary is RogueX:
                                                                                if not Player.Male:
                                                                                    ch_r "Какую часть слова \"нет\" ты не поняла?"
                                                                                else:
                                                                                    ch_r "Какую часть слова \"нет\" ты не понял?"
                                                                elif Primary is KittyX:
                                                                                ch_k "Кажется, я сказала тебе {i}НЕТ!{/i}"
                                                                elif Primary is EmmaX:
                                                                                ch_e "Уверена, я сказала {i}нет.{/i}"
                                                                elif Primary is LauraX:
                                                                                ch_l "[[рычит] . . . уверена."
                                                                elif Primary is JeanX:
                                                                                if not Player.Male:
                                                                                    ch_j "Ох, ты дурочка, [Primary.Petname]?"
                                                                                else:
                                                                                    ch_j "Ох, ты дурачок, [Primary.Petname]?"
                                                                elif Primary is StormX:
                                                                                ch_s "Абсолютно."
                                                                elif Primary is JubesX:
                                                                                ch_v "Ох, сейчас уточню. . ."
                                                                                $ Primary.FaceChange("angry",Eyes="side")
                                                                                ch_v ". . ."
                                                                                $ Primary.FaceChange("angry",Mouth="open")
                                                                                ch_v "-ДА.-"
                                                                                $ Primary.FaceChange("angry")
                                                                elif Primary is GwenX:
                                                                                ch_g "Очень."
                                                                elif Primary is BetsyX:
                                                                                ch_b "Абсолютно."
                                                                elif Primary is DoreenX:
                                                                                ch_d "Ага."
                                                                elif Primary is WandaX:
                                                                                ch_w "Ага."
                                                        elif Time_Count >= 3 and ApprovalCheck(Primary, 800, "LI") and ApprovalCheck(Primary, 400, "OI"):
                                                                $ Primary.FaceChange("sadside")
                                                                if Primary is RogueX:
                                                                                ch_r "Наверное, на этот раз я могу сделать исключение."
                                                                elif Primary is KittyX:
                                                                                ch_k "Ладно, но только в этот раз. . ."
                                                                elif Primary is EmmaX:
                                                                                ch_e "Хорошо, но только в этот раз. . ."
                                                                elif Primary is LauraX:
                                                                                ch_l "Думаю, можешь остаться. . ."
                                                                elif Primary is JeanX:
                                                                                ch_j "Ладно, но давай побыстрее."
                                                                elif Primary is StormX:
                                                                                ch_s "Если это действительно так важно. . ."
                                                                elif Primary is JubesX:
                                                                                ch_v "Конечно."
                                                                elif Primary is GwenX:
                                                                                ch_g "Думаю, ты можешь остаться. . ."
                                                                elif Primary is BetsyX:
                                                                                ch_b "Пожалуй, ненадолго можешь остаться. . ."
                                                                elif Primary is DoreenX:
                                                                                ch_d "Эм, наверное можешь. . . ненадолго."
                                                                elif Primary is WandaX:
                                                                                ch_w "Ладно, у тебя есть минута."
                                                                $ Line = "stay"
                                                        elif Time_Count >= 3 and Primary is not JubesX:
                                                                if Primary is RogueX:
                                                                                ch_r "Ни за что, [RogueX.Petname]. Можешь попытаться зайти завтра."
                                                                elif Primary is KittyX:
                                                                                ch_k "Нееет. Можешь попытаться зайти завтра."
                                                                elif Primary is EmmaX:
                                                                                ch_e "Боюсь, что нет. Можешь попробовать зайти завтра."
                                                                elif Primary is LauraX:
                                                                                ch_l "Нет. Может быть завтра."
                                                                elif Primary is JeanX:
                                                                                ch_j "Эм, нет? Уходи."
                                                                elif Primary is StormX:
                                                                                ch_s "Не сегодня, возможно, увидимся завтра во время занятий."
                                                                elif Primary is GwenX:
                                                                                ch_g "Эм, нет, ты не можешь остаться."
                                                                elif Primary is BetsyX:
                                                                                ch_b "Я абсолютно в этом уверена. Можешь попробовать зайти завтра."
                                                                elif Primary is DoreenX:
                                                                                ch_d "Эм, ты точно не можешь остаться. . . может, зайдешь завтра?"
                                                                elif Primary is WandaX:
                                                                                ch_w "Хех, нет, увидимся завтра."
                                                        elif ApprovalCheck(Primary, 750):
                                                                if Primary == RogueX:
                                                                                ch_r "Ох, ладно. Но только не надолго."
                                                                elif Primary is KittyX:
                                                                                ch_k "Ох, лааадно."
                                                                                ch_k "Но ненадолго."
                                                                elif Primary is EmmaX:
                                                                                ch_e "Ох, ну хорошо. . ."
                                                                                ch_e "Но не надолго."
                                                                elif Primary is LauraX:
                                                                                ch_l "Ладно."
                                                                                ch_l "Но только на минутку."
                                                                elif Primary is JeanX:
                                                                                ch_j "Думаю, можно? Да пофиг."
                                                                elif Primary is StormX:
                                                                                ch_s "Если это действительно так важно. . ."
                                                                elif Primary is JubesX:
                                                                                ch_v "Конечно."
                                                                elif Primary is GwenX:
                                                                                ch_g "Наверное?"
                                                                elif Primary is BetsyX:
                                                                                ch_b "Пожалуй, можешь остаться ненадолго. . ."
                                                                elif Primary is DoreenX:
                                                                                ch_d "Эм, наверное. . .  но ненадолго."
                                                                elif Primary is WandaX:
                                                                                ch_w "Ладно, у тебя есть минута."
                                                                $ Line = "stay"
                                                        else:
                                                                $ Primary.FaceChange("angry")
                                                                if Primary is RogueX:
                                                                                ch_r "Да, я серьезно, уходи."
                                                                elif Primary == KittyX:
                                                                                ch_k "Ага."
                                                                elif Primary == EmmaX:
                                                                                ch_e "Определённо."
                                                                elif Primary == LauraX:
                                                                                ch_l "Да."
                                                                elif Primary == JeanX:
                                                                                ch_j "Эм, да?"
                                                                elif Primary == StormX:
                                                                                ch_s "Ты точно не можешь остаться."
                                                                elif Primary == JubesX:
                                                                                ch_v "Ага, уходи."
                                                                elif Primary == GwenX:
                                                                                ch_g "Да, уходи."
                                                                elif Primary is BetsyX:
                                                                                ch_b "Абсолютно."
                                                                elif Primary is DoreenX:
                                                                                ch_d "Эм, да."
                                                                elif Primary is WandaX:
                                                                                ch_w "Хех, да."
                                                        if Line != "stay":
                                                                $ Primary.Statup("Love", 80, -1)
                                                                $ Primary.Statup("Inbt", 50, 3)
                                                                "[Primary.Name] выгоняет вас из комнаты."

                                            "Я остаюсь, спасибо.":
                                                        if "angry" in Primary.DailyActions or (not ApprovalCheck(Primary, 1800) and not ApprovalCheck(Primary, 500, "O")):
                                                                $ Primary.FaceChange("angry")
                                                                if Primary is RogueX:
                                                                                ch_r "Ни за что! На выход!"
                                                                elif Primary is KittyX:
                                                                                ch_k "Неееет, на выход!"
                                                                elif Primary is EmmaX:
                                                                                ch_e "Ты должно быть шутишь."
                                                                elif Primary is LauraX:
                                                                                ch_l "Не стоит."
                                                                elif Primary is JeanX:
                                                                                ch_j "Эм, нет, я не согласна."
                                                                elif Primary is StormX:
                                                                                ch_s "Я не позволю тебе этого."
                                                                elif Primary is JubesX:
                                                                                ch_v "Нуу, похоже, еда сама пришла ко мне. . ."
                                                                elif Primary is GwenX:
                                                                                ch_g "Не-а! Уходи!"
                                                                elif Primary is BetsyX:
                                                                                if not Player.Male:
                                                                                    ch_b "И речи быть не может! Пошла вон!"
                                                                                else:
                                                                                    ch_b "И речи быть не может! Пошел вон!"
                                                                elif Primary is DoreenX:
                                                                                ch_d "Тебе нельзя!"
                                                                elif Primary is WandaX:
                                                                                ch_w "Нет, [Player.Name]."
                                                        else:
                                                                $ Primary.Statup("Obed", 80, 5)
                                                                $ Primary.FaceChange("sad")
                                                                if Primary is RogueX:
                                                                                ch_r ". . ."
                                                                                ch_r "Ладно, все нормально."
                                                                elif Primary is KittyX:
                                                                                ch_k ". . ."
                                                                                ch_k "Ладно."
                                                                elif Primary is EmmaX:
                                                                                ch_e ". . ."
                                                                                ch_e "Хорошо."
                                                                elif Primary is LauraX:
                                                                                ch_l ". . ."
                                                                elif Primary is JeanX:
                                                                                ch_j "Ладно, как хочешь."
                                                                elif Primary is StormX:
                                                                                ch_s "Позже нам придется обсудить границы дозволенного."
                                                                elif Primary is JubesX:
                                                                                ch_v "Угум. . ."
                                                                elif Primary is GwenX:
                                                                                $ Primary.Statup("Obed", 90, 2)
                                                                                ch_g "Думаю, нет смысла спорить. . ."
                                                                elif Primary is BetsyX:
                                                                                ch_b ". . ."
                                                                                ch_b "Ну хорошо. . . но чая от меня не жди."
                                                                elif Primary is DoreenX:
                                                                                ch_d "Эм, ну, наверное, ты можешь остаться. . .  ненадолго."
                                                                elif Primary is WandaX:
                                                                                ch_w "Ладно, как хочешь."
                                                                $ Line = "stay"
                                                        if Line != "stay":
                                                                $ Primary.Statup("Love", 60, -5, 1)
                                                                $ Primary.Statup("Love", 80, -5)
                                                                $ Primary.Statup("Obed", 50, 2)
                                                                $ Primary.Statup("Inbt", 60, 5)
                                                                "[Primary.Name] выгоняет вас из комнаты."

                                    if Line != "stay":
                                            $ bg_current = "bg player"
                                            jump Misplaced
                                    #End the girl tells you to leave.
                    elif Primary is RogueX:
                                    ch_r "Извини, я не ожидала, что встречу тебя здесь."
                    elif Primary is KittyX:
                                    ch_k "Привет[KittyX.like]странно видеть тебя здесь."
                    elif Primary is EmmaX:
                                    ch_e "Я не ожидала встретить тебя здесь."
                    elif Primary is LauraX:
                                    ch_l "Ох. . . привет."
                    elif Primary is JeanX:
                                    ch_j "О, это ты. . ."
                    elif Primary is StormX:
                                    ch_s "Ах, [StormX.Petname]."
                    elif Primary is JubesX:
                                    ch_v "Ох, привет. . ."
                    elif Primary is GwenX:
                                    ch_g "Ох. . . здравствуй."
                    elif Primary is BetsyX:
                                    ch_b "Ох. . . здравствуй?"
                    elif Primary is DoreenX:
                                    ch_d "Эм, привет?"
                    elif Primary is WandaX:
                                    ch_w "О. Привет."
        #end girls showed up to Primary's room.

        elif bg_current == "bg classroom" and Weekday < 5 and Time_Count < 2:
                #if this is triggered, Adjacent should never be higher than 1.
                #adjacent characters who are neither Primary nor secondary should have been removed from adjacency

                if Secondary:
                        #if there's a second girl
                        "[Primary.Name] с [Secondary.Name_tvo] входят в комнату."
                else:
                        #if there's no second girl,
                        "[Primary.Name] входит в комнату."

                if Primary is RogueX or Secondary is RogueX:
                                ch_r "Привет, [RogueX.Petname]."
                if Primary is KittyX or Secondary == KittyX:
                                ch_k "Ох, привет."
                if Primary is EmmaX or Secondary == EmmaX:
                                ch_e "Ох, здравствуй, [EmmaX.Petname]."
                if Primary is LauraX or Secondary == LauraX:
                                ch_l "Привет."
                if Primary is StormX or Secondary == StormX:
                                ch_s "Здравствуй, [StormX.Petname]."
                if Primary is JubesX or Secondary == JubesX:
                                ch_v "Привет!"
                if Primary is GwenX or Secondary == GwenX:
                                ch_g "Йо."
                if Primary is BetsyX or Secondary is BetsyX:
                                ch_b "Здравствуй, [BetsyX.Petname]."
                if Primary is DoreenX or Secondary is DoreenX:
                                ch_d "Привет, [DoreenX.Petname]."
                if Primary is WandaX or Secondary is WandaX:
                                ch_w "Привет, [WandaX.Petname]."

                $ Line = 0
                $ D20 = renpy.random.randint(1, 20)

                if Primary is EmmaX or Primary is StormX:
                        #if the Primary is one of the teachers, swap the Secondary in
                        if Secondary:
                                $ Primary = Secondary
                                $ Secondary = 0
                        else:
                                $ Primary = 0
                if Primary and Primary not in Present:
                        #Determines who sits next to you
                        if ApprovalCheck(Primary, 1000):
                                if len(Present) < 2 and D20 >= 10:
                                        $ Line = Primary.Name + " садится рядом с вами"
                                        $ Present.append(Primary)
                                else:
                                        $ Line = Primary.Name + " садится подальше от вас"
                                        $ Nearby.append(Primary)
                        else:
                                        $ Line = Primary.Name + " садится подальше от вас"
                                        $ Nearby.append(Primary)

                if Secondary and Primary not in Present:
                        if ApprovalCheck(Secondary, 1000):
                            if len(Present) < 2 and D20 >= 10:
                                        #changes dialog based on whether she does the same or differently than the last person
                                        if Primary in Present:
                                                $ Line = Primary.Name + " и " + Secondary.Name + " садятся рядом с вами"
                                        else:
                                                $ Line = Line + ", пока " + Secondary.Name + " садится рядом с вами"
                                        $ Present.append(Secondary)
                            else:
                                        if Primary in Nearby:
                                                $ Line = Primary.Name + " и " + Secondary.Name + " садятся подальше от вас"
                                        else:
                                                $ Line = Line + ", пока " + Secondary.Name + " садится подальше от вас"
                                        $ Nearby.append(Secondary)
                        else:
                                        if Primary in Nearby:
                                                $ Line = Primary.Name + " и " + Secondary.Name + " садятся подальше от вас"
                                        else:
                                                $ Line = Line + ", пока " + Secondary.Name + " садится подальше от вас"
                                        $ Nearby.append(Secondary)
                if Line:
                    "[Line]."

                if EmmaX.Loc == "bg teacher":
                        "[EmmaX.Name] занимает свое место за подиумом."
                elif StormX.Loc == "bg teacher":
                        "[StormX.Name] занимает свое место за подиумом."
                #end girls showed up to class
        elif bg_current == "bg classroom" and Weekday < 5 and Time_Count == 2:
                #if it's after class,
                if EmmaX.Loc == bg_current:
                        "[EmmaX.Name] подходит к вам."
                elif StormX.Loc == bg_current:
                        "[StormX.Name] подходит к вам."
        elif bg_current == "bg dangerroom":
                if Secondary:
                        #if there's a second girl
                        "[Primary.Name] с [Secondary.Name_tvo] входят в комнату."
                else:
                        #if there's no second girl,
                        "[Primary.Name] входит в комнату."
                #end girls showed up to the Danger Room
        elif bg_current == "bg campus":
                if Secondary:
                        #if there's a second girl
                        "[Primary.Name] с [Secondary.Name_tvo] приходят на площадь."
                else:
                        #if there's no second girl,
                        "[Primary.Name] приходит на площадь."
                #end girls showed up to the campus
        elif bg_current == "bg pool":
                if Secondary:
                        #if there's a second girl
                        "[Primary.Name] с [Secondary.Name_tvo] входят на территорию бассейна."
                else:
                        #if there's no second girl,
                        "[Primary.Name] входит на территорию бассейна."
                #end girls showed up to the campus
        else: #if it's anywhere else,
                if Secondary:
                        #if there's a second girl
                        "[Primary.Name] с [Secondary.Name_tvo] входят в комнату."
                else:
                        #if there's no second girl,
                        "[Primary.Name] входит в комнату."
                #end girls showed up someplace

        if bg_current in ("bg campus","bg dangerroom","bg pool"):
                if Primary == RogueX or Secondary is RogueX:
                            ch_r "Привет, [RogueX.Petname]."
                if Primary is KittyX or Secondary is KittyX:
                            ch_k "Ох, привет."
                if Primary is EmmaX or Secondary is EmmaX:
                            ch_e "Ох, здравствуй, [EmmaX.Petname]."
                if Primary is LauraX or Secondary is LauraX:
                            ch_l "Привет."
                if Primary is StormX or Secondary is StormX:
                            ch_s "Здравствуй, [StormX.Petname]."
                if Primary is JubesX or Secondary is JubesX:
                            ch_v "Привет!"
                if Primary is GwenX or Secondary is GwenX:
                            ch_g "Йо."
                if Primary is BetsyX or Secondary is BetsyX:
                            ch_b "Здравствуй, [BetsyX.Petname]."
                if Primary is DoreenX or Secondary is DoreenX:
                            ch_d "Привет, [DoreenX.Petname]."
                if Primary is WandaX or Secondary is WandaX:
                                ch_w "Привет, [WandaX.Petname]."
        #end "girls showed up"

        $ BO = TotalGirls[:]
        python:
            for BX in BO:
                if BX in Nearby:
                        BX.Loc = "nearby"
                elif BX.Loc == bg_current and BX not in Present:
                        Present.append(BX)
        if Nearby:
                "Здесь были и другие люди, но они держались на расстоянии."
        return
# End Girls Arrive / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Gym Clothes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Gym Entry / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Gym_Entry(BO=[],GirlsNum = 0):  #rkeljsvgb
        if Taboo == 0 and bg_current == "bg dangerroom":
            menu:
                "Вы зашли тренироваться или развлекаться"
                "Тренироваться [[подготовиться, переодеться]":
                        pass
                "Развлекаться [[не переодеваться]":
                        return
        $ BO = TotalGirls[:]
        python:
            for BX in BO:
                #while there are still girls to do or the Mode is exit. . .
                if BX.Loc != "bg dangerroom" and BX not in Nearby and BX.Outfit == "gym":
                                #If she isn't in the dangerroom, switch to her day clothes
                                BX.Outfit = BX.OutfitDay
                elif BX.Outfit == "gym":
                                #If she's already in gym clothes, skip this
                                pass
                elif (BX.Loc == "bg dangerroom" or BX in Nearby) and BX not in Party:
                                #If she was already here
                                BX.Outfit = "gym"
        call Set_The_Scene
        $ BO = Present[:]
        while BO:
                if BO[0].Outfit != "gym":
                        #If girl is in the gym, see if she'll change clothes
                        if ApprovalCheck(BO[0], 1300, "LO") or "passive" in BO[0].Traits:
                            pass
                        elif ApprovalCheck(BO[0], 800, "LO") and BO[0].Custom1[0]:
                            pass
                        elif ApprovalCheck(BO[0], 600, "LO") and BO[0].Gym[0] != 1:
                            pass
                        else:
                            $ Line = "no"

                        if Line == "no" or "asked gym" in BO[0].DailyActions or "no ask gym" in BO[0].Traits:
                                #If she decides not to ask you
                                show blackscreen onlayer black
                                if BO[0] in (EmmaX,StormX,BetsyX):
                                        call AnyLine(BO[0],"Я тоже должна переодеться. . .")
                                else:
                                    if GirlsNum:
                                            call AnyLine(BO[0],"Я тоже скоро вернусь.")
                                    else:
                                            call AnyLine(BO[0],"Я скоро вернусь, мне нужно переодеться.")
                                $ BO[0].Outfit = "gym"
                        else:
                                # She asks to change outfits
                                $ BO[0].DailyActions.append("asked gym")
                                if GirlsNum:
                                    #if the second girl to ask. . .
                                    if BO[0] is EmmaX:
                                            $ Line = "Как думаешь, может, мне тоже переодеться?"
                                    elif BO[0] in (StormX,BetsyX):
                                            $ Line = "Как ты думаешь, мне стоит тоже переодеться?"
                                    else:
                                            $ Line = "Должна ли я тоже переодеться?"
                                else:
                                    if BO[0] is EmmaX:
                                            $ Line = "Ты хочешь, чтобы я переоделась?"
                                    elif BO[0] in (StormX,BetsyX):
                                            $ Line = "Как ты думаешь, мне стоит переодеться в спортивную одежду?"
                                    else:
                                            $ Line = "Хочешь, я переоденусь в спортивную одежду?"
                                call AnyLine(BO[0],Line)
                                menu:
                                        extend ""
                                        "Да, было бы неплохо.":
                                                    $ BO[0].FaceChange("smile")
                                                    $ BO[0].Statup("Love", 80, 2)
                                                    $ BO[0].Statup("Obed", 40, 1)
                                                    $ BO[0].Statup("Inbt", 30, 1)
                                                    $ Line = 1
                                        "Нет, не стоит.":
                                                    $ BO[0].FaceChange("confused")
                                                    $ BO[0].Statup("Obed", 50, 5)
                                                    $ Line = 0
                                        "Как тебе самой больше нравится.":
                                                    $ BO[0].FaceChange("confused")
                                                    $ BO[0].Statup("Inbt", 50, 1)
                                                    $ Line = renpy.random.randint(0, 3)
                                        "Мне все равно.":
                                                    $ BO[0].FaceChange("angry")
                                                    $ BO[0].Statup("Love", 50, -3, 1)
                                                    $ BO[0].Statup("Obed", 50, 4)
                                                    $ BO[0].Statup("Inbt", 50, 2)
                                                    $ Line = renpy.random.randint(0, 1)
                                if Line:
                                        #If she decided to change
                                        if BO[0] is RogueX:
                                                ch_r "Хорошо, я скоро вернусь."
                                        elif BO[0] is KittyX:
                                                ch_k "Ладно, я отойду ненадолго."
                                        elif BO[0] is EmmaX:
                                                ch_e "Хорошо, я сейчас вернусь."
                                        elif BO[0] is LauraX:
                                                ch_l "Я сейчас вернусь."
                                        elif BO[0] is StormX:
                                                ch_s "Тогда я скоро вернусь."
                                        elif BO[0] is JubesX:
                                                ch_v "Лады, сейчас вернусь."
                                        elif BO[0] is GwenX:
                                                ch_g "Хорошо, вернусь через секунду."
                                        elif BO[0] is BetsyX:
                                                ch_b "Тогда я скоро вернусь."
                                        elif BO[0] is DoreenX:
                                                ch_d "Тогда я отойду ненадолго."
                                        elif BO[0] is WandaX:
                                                ch_w "Сейчас вернусь."
                                        $ BO[0].Outfit = "gym"
                                # End She asks to change outfits
                        if BO[0].Outfit == "gym":
                                $ GirlsNum += 1
                        $ Line = 0
                        # End She isn't already in gym clothes
                $ BO.remove(BO[0])
                # End if BO[0].Outfit != "gym":

        $ BO = TotalGirls[:]
        while BO:
                #loops through and makes choices.
                $ BO[0].OutfitChange()
                $ BO.remove(BO[0])
        hide blackscreen onlayer black
        return
# End Gym Entry / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Gym_Exit / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Gym_Exit(BO=[]):  #rkeljsvgbdw
        #Called when you leave the gym, puts girls in their day clothes
        # call with "call Gym_Exit([RogueX]) " for a specific girl only
        if BO and BO[0] in TotalGirls:
                pass
        else:
                $ BO = Party[:]
        $ PassLine = 0
        while BO:
                if BO[0].Outfit == "gym":
                        #if they are in gym clothes, they tell you they'll change
                        if len(Party) > 1:
                                $ PassLine = "Раз уж мы уходим, нам нужно переодеться. . ."
                        else:
                                $ PassLine = "Раз уж мы уходим, мне нужно переодеться. . ."
                        $ BO[0].Outfit = BO[0].OutfitDay
                $ BO.remove(BO[0])
        if PassLine:
            if Party:
                    call AnyLine(Party[0],PassLine)
                    show blackscreen onlayer black with dissolve
                    $ BO = Party[:]
                    while BO:
                            #then they will change
                            $ BO[0].OutfitChange()
                            $ BO.remove(BO[0])
            $ PassLine = 0
            hide blackscreen onlayer black
        return
# End Gym_Exit / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Gym_Clothes_Off / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Gym_Clothes_Off(BO=[]):  #rkeljsvgb
        #Called when time changes and girls leave the Gym, puts girls in their day clothes
        if BO and BO[0] in TotalGirls:
                pass
        else:
                $ BO = TotalGirls[:]
        while BO: #or Mode == "exit"?
                #while there are still girls to do or the Mode is exit. . .
                if BO[0] not in Party:
                    if BO[0].Outfit == "gym" and BO[0].Loc != "bg dangerroom":
                            $ BO[0].Outfit = BO[0].OutfitDay
                    elif BO[0].Loc == "bg dangerroom":
                            $ BO[0].Outfit = "gym"
                $ BO.remove(BO[0])
        return
# End Gym_Clothes_Off / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# End Gym clothes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Present Check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Present_Check(Hold=1,BO=[],TempList=[]):
        # Culls parties down to 2 max
        # call Present Check will cull inhabitants of the room down to zero
        # moves them to Nearby if Hold, otherwise kicks them loose

        while len(Party) > 2:
                # If two or more members in the party
                #Culls down party size to two
                $ Party.remove(Party[2])

        #if in class and Present is already full, skip this.
        if bg_current == "bg classroom" and Present:
                pass            #if Party:   $ Present.append(Party[:])
        else:
                #If there is a party, fill the Present list with the party first
                $ Present = Party[:] if Party else []

        # checks to see which girls are present at a given location
        # If they are in the party, makes sure they are in the room
        # adds members who are not currently in the party

        $ BO = TotalGirls[:]
        $ renpy.random.shuffle(BO) #Randomizes pool
        python:
            for BX in BO:
                #cycles through each girl possible, adds them to the local area if possible
                if BX not in Present and BX.Loc == bg_current:
                        Present.append(BX)

        while len(Present) > 2:
                #culls the Temporary Present list down to two items (or less if the party is full)
                #Removes the rest
                #Moves girls to Nearby if that's an option.
                call Remove_Girl(Present[2],Hold=Hold)
#                $ Present.reverse() #flips the first to last

        if Present:
            if Ch_Focus in Present and Ch_Focus is not Present[0] and not renpy.showing(Ch_Focus.Tag+"_Seated"):
                    $ Present.reverse() #makes sure the room's owner is first
            call Shift_Focus(Present[0])

        $ BO = Present[:]
        python:
            for BX in BO:
                #cycles through each girl possible, removes them from NEarby if they were there.
                if BX in Nearby:
                        Nearby.remove(BX)
                BX.Loc = bg_current
        return

# End Present Check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Nearby clear / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label ReturnToSender:
        #Set's girl's location back to where she's meant to be if she was "nearby"
        #Set's girl's location back to where she's meant to be if she stuck around in an area you've since left
        $ BO = ActiveGirls[:]
        while BO:
            #if BO[0].Loc != bg_current and BO[0].Loc == "nearby":
            #if BO[0].Loc != bg_current and BO[0] not in Party:

            if BO[0] not in Party and BO[0].Schedule[Weekday][Time_Count] != bg_current:
                    # so long as she is not scheduled to be in the current location,
                    $ BO[0].Loc = BO[0].Schedule[Weekday][Time_Count]
                    if BO[0] is JubesX and JubesX.Addict > 60:
                                    #Jubilee will not leave her room voluntarily if it's higher than 60
                                    $ JubesX.Loc = JubesX.Home
            $ BO.remove(BO[0])
        return
# End Nearby clears / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Swap Nearby Girls / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Swap_Nearby(Girl=0, Other=0): #rkeljsvgb
        #allows you to bring nearby girls in.
        # girl is the girl in question, here is a counter for locals
        if Girl == "menu":
            menu:
                "К кому вы хотели бы приблизиться?"
                "[RogueX.Name]" if RogueX in Nearby:
                        $ Girl = RogueX
                "[KittyX.Name]" if KittyX in Nearby:
                        $ Girl = KittyX
                "[EmmaX.Name]" if EmmaX in Nearby:
                        $ Girl = EmmaX
                "[LauraX.Name]" if LauraX in Nearby:
                        $ Girl = LauraX
                "[JeanX.Name]" if JeanX in Nearby:
                        $ Girl = JeanX
                "[StormX.Name]" if StormX in Nearby:
                        $ Girl = StormX
                "[JubesX.Name]" if JubesX in Nearby:
                        $ Girl = JubesX
                "[GwenX.Name]" if GwenX in Nearby:
                        $ Girl = GwenX
                "[BetsyX.Name]" if BetsyX in Nearby:
                        $ Girl = BetsyX
                "[DoreenX.Name]" if DoreenX in Nearby:
                        $ Girl = DoreenX
                "[WandaX.Name]" if WandaX in Nearby:
                        $ Girl = WandaX
                "Ни к кому.":
                        return
        if Girl not in Nearby:
                        return
#        if bg_current not in ("bg campus","bg classroom","bg dangerroom","bg pool"):
#                #if you aren't in a space that supports this. . .
#                "There's no room for that here."
#                return

        if len(Present) >= 2:
                #if two or more girls are adjacent so there is no room. . .
                call AnyLine(Girl,"Там слегка тесновато.")
                menu:
                    "От кого-то вы хотели бы отойти подальше?"
                    "[RogueX.Name]" if RogueX.Loc == bg_current:
                            $ Other = RogueX
                    "[KittyX.Name]" if KittyX.Loc == bg_current:
                            $ Other = KittyX
                    "[EmmaX.Name]" if EmmaX.Loc == bg_current:
                            $ Other = EmmaX
                    "[LauraX.Name]" if LauraX.Loc == bg_current:
                            $ Other = LauraX
                    "[JeanX.Name]" if JeanX.Loc == bg_current:
                            $ Other = JeanX
                    "[StormX.Name]" if StormX.Loc == bg_current:
                            $ Other = StormX
                    "[JubesX.Name]" if JubesX.Loc == bg_current:
                            $ Other = JubesX
                    "[GwenX.Name]" if GwenX.Loc == bg_current:
                            $ Other = GwenX
                    "[BetsyX.Name]" if BetsyX.Loc == bg_current:
                            $ Other = BetsyX
                    "[DoreenX.Name]" if DoreenX.Loc == bg_current:
                            $ Other = DoreenX
                    "[WandaX.Name]" if WandaX.Loc == bg_current:
                            $ Other = WandaX
                    "Ни от кого.":
                            return
                if Other not in TotalGirls:
                            return
                "Вы отходите от [Other.Name_rod]."
                call Remove_Girl(Other,1,1)    #Hide+moveto nearby
        "Вы подходите к [Girl.Name_dat]."
        $ Nearby.remove(Girl)
        $ Present.append(Girl)
        call Shift_Focus(Girl)
        $ Girl.Loc = bg_current
        call Set_The_Scene(1,0,0,0)
        return

label Drain_Nearby(BO=[]):
        #finds all girls with loc = "nearby" and moves them to where you just left
        $ BO = TotalGirls[:]
        python:
            for BX in BO:
                    BX.Loc = bg_current if BX.Loc == "nearby" else BX.Loc
        $ Nearby = []
        return

label Clear_Nearby:
        #empties out Nearby, sends girls home
        while Nearby:
                $ Nearby[0].Loc = Nearby[0].Home #if bg_current != Nearby[0].Home else "bg campus"
                $ Nearby.remove(Nearby[0])
        return
#end Swap_Nearby / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Dismiss girl / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Dismissed:  #rkeljsvgb
        # this is called to dismiss any girl in the local area.
        menu:
            "Хотите попросить кого-нибудь уйти?"
            "[RogueX.Name]" if RogueX.Loc == bg_current or RogueX in Party:
                call Girl_Dismissed(RogueX)
            "[KittyX.Name]" if KittyX.Loc == bg_current or KittyX in Party:
                call Girl_Dismissed(KittyX)
            "[EmmaX.Name]" if EmmaX.Loc == bg_current or EmmaX in Party:
                call Girl_Dismissed(EmmaX)
            "[LauraX.Name]" if LauraX.Loc == bg_current or LauraX in Party:
                call Girl_Dismissed(LauraX)
            "[JeanX.Name]" if JeanX.Loc == bg_current or JeanX in Party:
                call Girl_Dismissed(JeanX)
            "[StormX.Name]" if StormX.Loc == bg_current or StormX in Party:
                call Girl_Dismissed(StormX)
            "[JubesX.Name]" if JubesX.Loc == bg_current or JubesX in Party:
                call Girl_Dismissed(JubesX)
            "[GwenX.Name]" if GwenX.Loc == bg_current or GwenX in Party:
                call Girl_Dismissed(GwenX)
            "[BetsyX.Name]" if BetsyX.Loc == bg_current or BetsyX in Party:
                call Girl_Dismissed(BetsyX)
            "[DoreenX.Name]" if DoreenX.Loc == bg_current or DoreenX in Party:
                call Girl_Dismissed(DoreenX)
            "[WandaX.Name]" if WandaX.Loc == bg_current or WandaX in Party:
                call Girl_Dismissed(WandaX)
            "Нет.":
                pass
        return

# End Dismiss Girl / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Locked_Door(Girl=0,Entry=1,Current=0): #rkeljsvgb
        # called when a girl tries to enter a locked room, mainly from the summon function
        # Girl is the indicated girl, Entry is True if you want to always have her enter with dialog
        # Current is a girl you are currently with
        if Girl not in TotalGirls or "phonesex" in Player.RecentActions or "interruption" in Player.RecentActions:
                return
        if Current not in TotalGirls:
                $ Current = 0
        $ Player.AddWord(1,"interruption") #adds to Recent
        if "switchcheck" in Girl.Traits:
                return 1
        if not Trigger:
                #resets the scene if not during a sex act
                call Set_The_Scene
        if Girl is KittyX:
                if bg_current == "bg campus" or bg_current == "bg pool":
                        "Неожиданно [Girl.Name] выглядывает из-за угла."
                else:
                        "Вы видите, как [KittyX.Name] заходит в комнату сквозь дверь."
                $ KittyX.Loc = bg_current
                call Taboo_Level
                $ KittyX.OutfitChange()
                call Display_Girl(KittyX,TrigReset=0)
                ch_k "Hi, [KittyX.Petname]!"
                return 1
        if "locked" not in Player.Traits:
                $ Girl.Loc = bg_current
                call Display_Girl(Girl,TrigReset=0)
                if bg_current == "bg campus" or bg_current == "bg pool":
                        "Неожиданно [Girl.Name] выглядывает из-за угла."
                else:
                        "Неожиданно [Girl.Name] входит в комнату без стука."
                if Entry:
                        if Girl is RogueX:
                                ch_r "[Girl.Petname], есть минутка?"
                        elif Girl is EmmaX:
                                ch_e "[Girl.Petname], мне нужно кое-что с тобой обсудить. . ."
                        elif Girl is LauraX:
                                ch_l "Привет, [Girl.Petname]."
                        elif Girl is JeanX:
                                ch_j "Привет, [Girl.Petname]."
                        elif Girl is StormX:
                                ch_s "[Girl.Petname], я могу войти?"
                        elif Girl is JubesX:
                                ch_v "Привет, [Girl.Petname]."
                        elif Girl is GwenX:
                                ch_g "Ох, [Girl.Petname]."
                        elif Girl is BetsyX:
                                ch_b "Пардон, [Girl.Petname]?"
                        elif Girl is DoreenX:
                                ch_d "Ох, эм, привет, [Girl.Petname]?"
                        elif Girl is WandaX:
                                ch_w "Привет, [Girl.Petname]. . ."
                call Taboo_Level
                #return 1
        elif Girl.Loc == Girl.Home:
                "Вы слышите, как в замке поворачивается ключ, затем [Girl.Name] входит в комнату."
        elif Girl is JeanX:
                "Вы слышите стук в дверь."
                "Затем слышите несколько щелчков и дверь открывается."
                "После этого [JeanX.Name] входит в комнату."
                $ JeanX.Loc = bg_current
                call Taboo_Level
                $ JeanX.OutfitChange()
                call Display_Girl(JeanX,TrigReset=0)
                ch_j "Привет, [JeanX.Petname]!"
                return 1
        else:
            "Дверная ручка начинает дергаться и через мгновение вы слышите стук."
            if Girl is RogueX:
                    ch_r "[Girl.Petname], можно мне войти?"
            elif Girl is EmmaX:
                    ch_e "[Girl.Petname], я жду."
            elif Girl is LauraX:
                    ch_l "Это я."
            elif Girl is StormX:
                    ch_s "[Girl.Petname], я могу войти?"
            elif Girl is JubesX:
                    ch_v "Привет, это [Girl.Name]."
            elif Girl is GwenX:
                    ch_g "Это [Girl.Name], я могу войти?"
            elif Girl is BetsyX:
                    ch_b "Пардон, это [Girl.Name], могу я войти?"
            elif Girl is DoreenX:
                    ch_d "Привет, это [Girl.Name], можно мне войти?"
            elif Girl is WandaX:
                    ch_w "Привет, [Girl.Petname], открывай."
            menu:
                extend ""
                "Открыть дверь":
                        ch_p "Подожди секунду, [Girl.Name]!"
                        "Вы открываете дверь и впускаете ее."
                        $ Girl.Loc = bg_current
                        $ Girl.OutfitChange()
                "Open door [[but stop fucking first]" if Trigger:
                        ch_p "Подожди секунду, [Girl.Name]!"
                        call Sex_Over(1,Primary) #Cleans up after the sex stuff
                        "Вы открываете дверь и впускаете ее."
                        $ Girl.Loc = bg_current
                        call Taboo_Level
                        $ Girl.OutfitChange()
                        call Display_Girl(Girl,TrigReset=0)
                        if Girl is RogueX:
                                ch_r "Есть минутка, [Girl.Petname]?"
                        elif Girl is EmmaX:
                                ch_e "[Girl.Petname], мне нужно кое-что с тобой обсудить. . ."
                        elif Girl is LauraX:
                                ch_l "Привет, [Girl.Petname]."
                        elif Girl is StormX:
                                ch_s "Здравствуй, я хотела поговорить с тобой. . ."
                        elif Girl is JubesX:
                                ch_v "Привет, [Girl.Petname]."
                        elif Girl is GwenX:
                                ch_g "Привет."
                        elif Girl is BetsyX:
                                ch_b "Ох, здравствуй, Я хотела кое-что обсудить с тобой."
                        elif Girl is DoreenX:
                                ch_d "Ох, эм, слушай, мне нужно кое о чем. . . поговорить с тобой. . ."
                        elif Girl is WandaX:
                                ch_w "Привет. . ."
                        jump Misplaced
                "Прогнать её":
                        ch_p "Эм, извини, не могла бы ты зайти попозже?"
                        $ Girl.Statup("Love", 80, -2)
                        if Girl is RogueX:
                                ch_r "Да ладно, [Girl.Petname], не пренебрегай мной!"
                                if Girl.Loc == bg_current:
                                    call Remove_Girl(Girl)
                                return 0
                        elif Girl is EmmaX:
                                $ Girl.Statup("Obed", 80, -2)
                                ch_e "Должна отметить, [EmmaX.Petname], я понимаю, что тебе приятно, когда тебя все слушаются. . ."
                                ch_e "но я не люблю, когда со мной так разговаривают!"
                                if Girl.Loc == bg_current:
                                    call Remove_Girl(Girl)
                                return 0
                        elif Girl in (LauraX,JubesX,WandaX):
                            "[Girl.Name] затихает."
                            if ApprovalCheck(Girl, 500,"I") and not ApprovalCheck(Girl, 500,"O"):
                                    $ Girl.Loc = bg_current
                                    $ Girl.OutfitChange()
                                    if Girl is LauraX:
                                            $ LauraX.ArmPose = 2
                                            $ LauraX.Claws = 1
                                            "*чик*"
                                            call Display_Girl(Girl,TrigReset=0)
                                            "Дверь неожиданно распахивается."
                                            $ LauraX.Claws = 0
                                            ch_l "Я не люблю, когда мной пренебрегают, так что не делай так больше, ладно?"
                                    elif Girl is WandaX:
                                            call Display_Girl(Girl,TrigReset=0)
                                            "Вы видите синее свечение из-под двери, и дверь распахивается."
                                            ch_w "Привет."
                                    else:
                                            "Призрачный туман проходит под дверью и принимает форму человека."
                                            call Display_Girl(Girl,TrigReset=0) #fix, make a misty animation?
                                            ch_v "Так вот, я хотела бы поговорить."
                                    $ Girl.Statup("Obed", 80, -4)
                            else:
                                    $ Girl.Statup("Love", 80, -1)
                                    $ Girl.Statup("Obed", 80, 3)
                                    call AnyLine(Girl,"Ладно.")
                                    "Вы слышите, как она уходит."
                                    if Girl.Loc == bg_current:
                                        call Remove_Girl(Girl)
                                    return 0
                        elif Girl is StormX:
                            if ApprovalCheck(Girl, 800,"LI") and not ApprovalCheck(Girl, 500,"O"):
                                    $ Girl.Loc = bg_current
                                    $ Girl.OutfitChange()
                                    call Display_Girl(Girl,TrigReset=0)
                                    "Вы слышите какой-то щелчок."
                                    "Дверь неожиданно распахивается."
                                    $ Girl.Statup("Obed", 80, -4)
                                    ch_s "У тебя некачественный замок."
                            else:
                                    $ Girl.Statup("Love", 80, -1)
                                    $ Girl.Statup("Obed", 80, 3)
                                    ch_s ". . ."
                                    ch_s "Хорошо, я уважаю твое мнение."
                                    if Girl.Loc == bg_current:
                                        call Remove_Girl(Girl)
                                    return 0
                        elif Girl is GwenX:
                                if not Player.Male:
                                    ch_g "Хорошо, должно быть ты. . . занята. . ."
                                else:
                                    ch_g "Хорошо, должно быть ты. . . занят. . ."
                                if Girl.Loc == bg_current:
                                    call Remove_Girl(Girl)
                                return 0
                        elif Girl is BetsyX:
                                $ Girl.Statup("Obed", 80, -2)
                                if not Player.Male:
                                    ch_b "Я понимаю твою потребность в уединении, хотя я бы и хотела, чтобы ты впустила меня."
                                else:
                                    ch_b "Я понимаю твою потребность в уединении, хотя я бы и хотела, чтобы ты впустил меня."
                                if Girl.Loc == bg_current:
                                    call Remove_Girl(Girl)
                                return 0
                        elif Girl is DoreenX:
                                $ Girl.Statup("Love", 60, -1)
                                $ Girl.Statup("Love", 80, -1)
                                $ Girl.Statup("Obed", 80, 1)
                                ch_d "Хорошо, но не зови меня больше, если не хочешь впускать, ладно?"
                                if Girl.Loc == bg_current:
                                    call Remove_Girl(Girl)
                                return 0
        if Girl.Loc == bg_current:
                call Display_Girl(Girl)
        if Trigger and Ch_Focus.Loc == bg_current:
            $ Current = Ch_Focus
        if Current:
            if Current is EmmaX and ("three" not in EmmaX.History or "classcaught" not in EmmaX.History):
                    #Emma-specific code
                    $ Girl.AddWord(1,0,0,"saw with " + Current.Tag) #adds to Traits.
                    if bg_current == EmmaX.Home:
                            #if you're in her room. . .
                            ch_e "Я. . . Это не то, чем кажется. . ."
                            "Она выгоняет вас обоих в коридор и захлопывает дверь."
                            $ Girl.Loc = "bg player"
                            call Remove_Girl(EmmaX)
                    else:
                            ch_e "Я. . . Это не то, чем кажется. . ."
                            call Remove_Girl(EmmaX)
                            "Кажется, ей стало неуютно от подобной ситуации, она выходит из комнаты."
                            "Возможно, вам стоит поговорить с ней об этом позже."
                    jump Misplaced

            if "poly " + Current.Tag in Girl.Traits or (Current in Player.Harem and Girl in Player.Harem):
                    #if they already have a relationship. . .
                    pass
            else:
                    #if they don't have a relationship. . .
                    if ApprovalCheck(Current, 1500, TabM=2, Bonus = (Girl.GirlLikeCheck(Current) - 500),Alt=[[WandaX],1000]):
                            #if the current girl approves of starting something. . .
                            $ Current.FaceChange("sexy", 1)
                            $ Current.Statup("Obed", 90, 5)
                            $ Current.Statup("Inbt", 90, 5)
                            $ Current.Statup("Lust", 90, 3)
                    else:
                            #the current girl isn't on board with this
                            $ Current.FaceChange("angry", 1)
                            if Current is RogueX:
                                    ch_r "Послушай, [Girl.Tag], ты не видишь, что мы тут немного заняты?"
                            elif Current is KittyX:
                                    ch_k "Эм, [Girl.Tag]? Ты понимаешь, что сейчас происходит?"
                            elif Current is EmmaX:
                                    ch_e "[Girl.Tag], не могла бы ты, пожалуйста, уйти?"
                            elif Current is LauraX:
                                    ch_l "Проваливай, [Girl.Tag]."
                            elif Current is JeanX:
                                    ch_j "Уходи, [Girl.Tag]."
                            elif Current is StormX:
                                    ch_s "Не могла бы ты дать нам немного уединения?"
                            elif Current is JubesX:
                                    ch_v "Ага, мы тут, как бы. . . заняты."
                            elif Current is GwenX:
                                    ch_g "Эм. . . Тебе скинуть потом фотки?"
                            elif Current is BetsyX:
                                    ch_b "Мне ужасно жаль, [Girl.Tag], потом я заглажу свою вину."
                            elif Current is DoreenX:
                                    ch_d "Извини, [Girl.Tag]! Мы, эм, потом об этом поговорим."
                            elif Current is WandaX:
                                    ch_w "И? Не могла бы ты уже уйти?"
                            $ Girl.AddWord(1,0,0,"saw with " + Current.Tag)
                            if Girl is RogueX:
                                    $ Girl.FaceChange("perplexed", 2)
                                    ch_r "Ох, извините! Я сейчас же уйду."
                            elif Girl is KittyX:
                                    $ Girl.FaceChange("perplexed", 2)
                                    ch_k "Ох! Мнежальизвинитепожалуйста!"
                            elif Girl is EmmaX:
                                    $ Girl.FaceChange("bemused", 2)
                                    ch_e "Я не хотела вас прерывать. . ."
                            elif Girl is LauraX:
                                    ch_l "Ох, конечно. Как скажешь."
                            elif Girl is JeanX:
                                    $ Girl.FaceChange("bemused", 1)
                                    ch_j "Хорошо."
                            elif Girl is StormX:
                                    $ Girl.FaceChange("bemused", 1)
                                    ch_s "Да. . ."
                            elif Girl is JubesX:
                                    $ Girl.FaceChange("perplexed", 2)
                                    ch_v "Ах, да! Извините!"
                            elif Girl is GwenX:
                                    $ Girl.FaceChange("perplexed", 2)
                                    ch_g "Извините! Я не хотела вам мешать. . ."
                                    ch_g "Я. . . пойду. . ."
                                    ch_g "Или нет?"
                                    call AnyLine(Current,"Проваливай.")
                                    ch_g "Да, мне лучше уйти. . ."
                            elif Girl is BetsyX:
                                    $ Girl.FaceChange("bemused", 1)
                                    ch_b "Конечно, конечно, я не хочу навязываться."
                            elif Girl is DoreenX:
                                    $ Girl.FaceChange("perplexed", 2)
                                    ch_d "Эм, ага! Конечно! Я, эм, пошла. . ."
                            elif Girl is WandaX:
                                    ch_w "О! Ага, хорошо . ."
                            $ Girl.FaceChange("sad", 1)
                            $ Current.FaceChange("sexy", 1)
                            if Girl.Loc == bg_current:
                                    call Remove_Girl(Girl)
                            call Taboo_Level
                            return 0
            if Current is RogueX:
                    ch_r "Ох, [Girl.Tag], не хочешь присоединиться к нам?"
            elif Current == KittyX:
                    ch_k "Эм, [Girl.Tag]? Ты чего - то хотела?"
            elif Current == EmmaX:
                    ch_e "Ох, [Girl.Tag]. . . не хочешь составить нам компанию?"
            elif Current == LauraX:
                    ch_l "О, привет, [Girl.Tag]."
            elif Current == JeanX:
                    ch_j "Привет."
            elif Current == StormX:
                    ch_s "Ох, здравствуй, [Girl.Tag], не хочешь присоединиться к нам?"
            elif Current == JubesX:
                    ch_v "Привет, [Girl.Tag], тебе что-то нужно?"
            elif Girl is GwenX:
                    ch_g "Нуууу. . . не хочешь поучавствовать?"
            elif Current is BetsyX:
                    ch_b "Ох, здравствуй, [Girl.Tag], не желаешь присоединиться к нам?"
            elif Current is DoreenX:
                    ch_d "Ох, [Girl.Tag], привет. . . не хочешь присоединиться к нам?"
            elif Current is WandaX:
                    ch_w "Не хочешь присоединиться к нам?"
        #end current stuff
        $ Girl.Loc = bg_current
        call Taboo_Level
        $ Girl.OutfitChange(5)
        $ Player.DrainWord("locked",0,0,1)
#        call Set_The_Scene(1,0,0,0)#characters, no entry, no clothes changes, no triggers

#        if Partner == Girl:
#                #if this is already a Partner, skip this dialog
#                $ Silent = 1
        if Current:
            $ Partner = Girl
            if Partner:
                    call Display_Girl(Partner,0,0)
                    call Sex_Basic_Dialog(Partner,"enjoyyes")
        else:
            call Shift_Focus(Girl)

        $ Line = 0
        return 1
#End Locked door responses / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Taboo stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Taboo_Level(Taboo_Loc=1,Teach=0,BO=[],BO2=[],Taboo_Check=bg_current): #rkeljsvgb
        #cycles through each girl, setting their taboo level.
        # if Taboo_Loc, will only work on local characters.
        #Set your taboo level
        $ Taboo = 0 #resets it each time

        if EmmaX.Loc == "bg teacher":
                $ EmmaX.Loc = "bg classroom" #Sets Emma to being in class if she's teaching
                $ Teach = 1
        elif StormX.Loc == "bg teacher":
                $ StormX.Loc = "bg classroom" #Sets Storm to being in class if she's teaching
                $ Teach = 2

        #Player Check

        if bg_current in PersonalRooms or "locked" in Player.Traits:
                            $ Player.Taboo = 0
        elif Time_Count >= 3 or Taboo_Check == "bg showerroom":
                            $ Player.Taboo = 20
        else:
                            $ Player.Taboo = 40
        $ Taboo = Player.Taboo

        $ BO = TotalGirls[:]
        if JeanX in BO and "nowhammy" not in JeanX.Traits:
                # So long as Jean is allowed to whammy students, she does not care about location.
                $ JeanX.Taboo = 0
                $ BO.remove(JeanX)
        python:
            for BX in BO:
                #cycles through each girl possible, setting them to local if they are in the party
                #Then it checks their taboo level
                if BX in Party:
                        BX.Loc = bg_current
                if BX.Loc == "nearby" or BX in Nearby:
                        Taboo_Check = bg_current
                else:
                        Taboo_Check = BX.Loc
                if not Taboo_Loc or Taboo_Check == bg_current:
                        #only checks if they are local if it's not a general check
                        if Taboo_Check in PersonalRooms or Taboo_Check == "hold":
                                            BX.Taboo = 0
                        elif Taboo_Check == "bg player":
                                            BX.Taboo = 0
                        elif "locked" in Player.Traits and Taboo_Check == bg_current:
                                            BX.Taboo = 0
                        elif Time_Count >= 3 or Taboo_Check == "bg showerroom":
                                            BX.Taboo = 20
                        else:
                                            BX.Taboo = 40
                        if BX.Taboo >= 20:
                                # if it's already 20+, or if we're testing the player stat, there's no point to this
                                pass
                        else:
                                BO2 = TotalGirls[:]
                                for BY in BO2:
                                        #compares the first girl to each of the others.
                                        if BY != BX:
                                                #loops through the girls in an inner loop if they are not the same
                                                if BX.Loc == BY.Loc and BX.GirlLikeCheck(BY) <= 700 and not (BX in Player.Harem and BY in Player.Harem):
                                                        #if either she likes the second girl, or both are in the harem, skip
                                                        BX.Taboo = 20
                        Taboo = BX.Taboo if (BX.Taboo > Taboo and bg_current == BX.Loc) else Taboo
        #end loop

        if Teach == 2:
                $ StormX.Loc = "bg teacher" #Sets Storm to being a teacher again
        elif Teach:
                $ EmmaX.Loc = "bg teacher" #Sets Emma to being a teacher again
        return
        #end taboo level

#End Taboo stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# End Time and Space Stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Speed_Shift(S=0):
        #adjusts the speed of animations to S, uses fade to hide glitches
        # call Speed_Shift(2)
        $ Speed = S
        show blackscreen onlayer black
        pause 0.01
        hide blackscreen onlayer black
        return



# Start shop interface / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Shop: #rkeljsvg
    menu:
        "Вы заходите в онлайн магазин. У вас [Player.Cash] долларов."
        "Купить фаллоимитатор за $20.":
                if Player.Inventory.count("dildo") >= 10:
                    "У вас уже большой набор фаллоимитаторов. 2, 4, 6. . . да, очень много."
                elif Player.Cash >= 20:
                    "Вы покупаете один фаллоимитатор."
                    $ Player.Inventory.append("dildo")
                    $ Player.Cash -= 20
                else:
                    "У вас недостаточно средств."
        "Купить вибратор за $25.":
                if Player.Inventory.count("vibrator") >= 10:
                    "Если вы купите еще один, то разверзнется земля."
                elif Player.Cash >= 25:
                    "Вы покупаете один вибратор."
                    $ Player.Inventory.append("vibrator")
                    $ Player.Cash -= 25
                else:
                    "У вас недостаточно средств."
        "Подарки для: [RogueX.Name]":
            menu:
                "Купить зеленую кружевную ночнушку за $75 $75." if "nighty" not in RogueX.Inventory and "Rogue nighty" not in Player.Inventory:
                    if Player.Cash >= 75:
                        "Вы покупаете ночнушку, она хорошо подойдет [RogueX.Name_dat]."
                        $ Player.Inventory.append("Rogue nighty")
                        $ Player.Cash -= 75
                    else:
                        "У вас недостаточно средств."
                "Купить черный кружевной лифчик за $90." if "lace bra" not in RogueX.Inventory and "Rogue lace bra" not in Player.Inventory:
                    if Player.Cash >= 90:
                        "Вы покупаете кружевной лифчик, он хорошо подойдет [RogueX.Name_dat]."
                        $ Player.Inventory.append("Rogue lace bra")
                        $ Player.Cash -= 90
                    else:
                        "У вас недостаточно средств."
                "Купить черные кружевные трусики за $110." if "lace panties" not in RogueX.Inventory and "Rogue lace panties" not in Player.Inventory:
                    if Player.Cash >= 110:
                        "Вы покупаете кружевные трусики, они хорошо подойдут [RogueX.Name_dat]."
                        $ Player.Inventory.append("Rogue lace panties")
                        $ Player.Cash -= 110
                    else:
                        "У вас недостаточно средств."
#                "Buy stockings and garterbelt for $100." if "stockings and garterbelt" not in RogueX.Inventory and "stockings and garterbelt" not in Player.Inventory and ApprovalCheck(RogueX, 1500):
#                    if Player.Cash >= 100:
#                        "You purchase the stockings, these will look nice on [RogueX.Name]."
#                        $ Player.Inventory.append("stockings and garterbelt")
#                        $ Player.Cash -= 100
#                    else:
#                        "У вас недостаточно средств."
                "Купить желтый лифчик бикини за $50." if "bikini top" not in RogueX.Inventory and "Rogue bikini top" not in Player.Inventory:
                        if Player.Cash >= 50:
                            "Вы покупаете лифчик бикини, он хорошо подойдет [RogueX.Name_dat]."
                            $ Player.Inventory.append("Rogue bikini top")
                            $ Player.Cash -= 50
                        else:
                            "У вас недостаточно средств."
                "Купить зеленые трусики бикини за $50." if "bikini bottoms" not in RogueX.Inventory and "Rogue bikini bottoms" not in Player.Inventory:
                        if Player.Cash >= 50:
                            "Вы покупаете трусики бикини, они хорошо подойдут [RogueX.Name_dat]."
                            $ Player.Inventory.append("Rogue bikini bottoms")
                            $ Player.Cash -= 50
                        else:
                            "У вас недостаточно средств."
                "Неважно.":
                    pass
        "Подарки для: [KittyX.Name]" if "met" in KittyX.History:
            menu:
                "Купить белый кружевной лифчик за $90." if "lace bra" not in KittyX.Inventory and "Kitty lace bra" not in Player.Inventory:
                    if Player.Cash >= 90:
                        "Вы покупаете кружевной лифчик, он хорошо подойдет [KittyX.Name_dat]."
                        $ Player.Inventory.append("Kitty lace bra")
                        $ Player.Cash -= 90
                    else:
                        "У вас недостаточно средств."
                "Купить белые кружевные трусики за $110." if "lace panties" not in KittyX.Inventory and "Kitty lace panties" not in Player.Inventory:
                    if Player.Cash >= 110:
                        "Вы покупаете кружевные трусики, они хорошо подойдут [KittyX.Name_dat]."
                        $ Player.Inventory.append("Kitty lace panties")
                        $ Player.Cash -= 110
                    else:
                        "У вас недостаточно средств."

                "Купить колготки за $50." if "pantyhose" not in KittyX.Inventory and "Kitty pantyhose" not in Player.Inventory:
                    if Player.Cash >= 50:
                        "Вы покупаете колготки, они хорошо подойдут [KittyX.Name_dat]."
                        $ Player.Inventory.append("Kitty pantyhose")
                        $ Player.Cash -= 50
                    else:
                        "У вас недостаточно средств."
#                "Buy stockings and garterbelt for $100." if "stockings and garterbelt" not in KittyX.Inventory and "stockings and garterbelt" not in Player.Inventory:
#                    if Player.Cash >= 100:
#                        "You purchase the stockings, these will look nice on [KittyX.Name]."
#                        $ Player.Inventory.append("stockings and garterbelt")
#                        $ Player.Cash -= 100
#                    else:
#                        "У вас недостаточно средств."
                "Купить гольфы за $50." if "knee" not in KittyX.Inventory and "knee" not in Player.Inventory:
                    if Player.Cash >= 50:
                        "Вы покупаете гольфы, они хорошо подойдут [KittyX.Name_dat]."
                        $ Player.Inventory.append("knee")
                        $ Player.Cash -= 50
                    else:
                        "У вас недостаточно средств."

                "Купить синий лифчик бикини за $60." if "bikini top" not in KittyX.Inventory and "Kitty bikini top" not in Player.Inventory:
                        if Player.Cash >= 60:
                            "Вы покупаете лифчик бикини, он хорошо подойдет [KittyX.Name_dat]."
                            $ Player.Inventory.append("Kitty bikini top")
                            $ Player.Cash -= 60
                        else:
                            "У вас недостаточно средств."
                "Купить синие трусики бикини за $60." if "bikini bottoms" not in KittyX.Inventory and "Kitty bikini bottoms" not in Player.Inventory:
                        if Player.Cash >= 60:
                            "Вы покупаете трусики бикини, они хорошо подойдут [KittyX.Name_dat]."
                            $ Player.Inventory.append("Kitty bikini bottoms")
                            $ Player.Cash -= 60
                        else:
                            "У вас недостаточно средств."
                "Купить синюю мини-юбку за $50." if "blue skirt" not in KittyX.Inventory and "Kitty blue skirt" not in Player.Inventory:
                        if Player.Cash >= 50:
                            "Вы покупаете синюю юбку, она хорошо подойдет [KittyX.Name_dat]."
                            $ Player.Inventory.append("Kitty blue skirt")
                            $ Player.Cash -= 50
                        else:
                            "У вас недостаточно средств."
                "Неважно.":
                    pass
        "Подарки для: [EmmaX.Name]" if "met" in EmmaX.History:
            menu:
                "Купить белый кружевной лифчик за $90." if "lace bra" not in EmmaX.Inventory and "Emma lace bra" not in Player.Inventory:
                        if Player.Cash >= 90:
                            "Вы покупаете кружевной лифчик, он хорошо подойдет [EmmaX.Name_dat]."
                            $ Player.Inventory.append("Emma lace bra")
                            $ Player.Cash -= 90
                        else:
                            "У вас недостаточно средств."
                "Купить белые кружевные трусики за $110." if "lace panties" not in EmmaX.Inventory and "Emma lace panties" not in Player.Inventory:
                        if Player.Cash >= 110:
                            "Вы покупаете кружевные трусики, они хорошо подойдут [EmmaX.Name_dat]."
                            $ Player.Inventory.append("Emma lace panties")
                            $ Player.Cash -= 110
                        else:
                            "У вас недостаточно средств."
                "Купить колготки за $50." if "pantyhose" not in EmmaX.Inventory and "Emma pantyhose" not in Player.Inventory:
                    if Player.Cash >= 50:
                        "Вы покупаете колготки, они хорошо подойдут [EmmaX.Name_dat]."
                        $ Player.Inventory.append("Emma pantyhose")
                        $ Player.Cash -= 50
                    else:
                        "У вас недостаточно средств."
#                "Buy stockings and garterbelt for $100." if "stockings and garterbelt" not in EmmaX.Inventory and "stockings and garterbelt" not in Player.Inventory and ApprovalCheck(EmmaX, 1500):
#                    if Player.Cash >= 100:
#                        "You purchase the stockings, these will look nice on [EmmaX.Name]."
#                        $ Player.Inventory.append("stockings and garterbelt")
#                        $ Player.Cash -= 100
#                    else:
#                        "У вас недостаточно средств."
                "Купить белый лифчик бикини за $60." if "bikini top" not in EmmaX.Inventory and "Emma bikini top" not in Player.Inventory:
                        if Player.Cash >= 60:
                            "Вы покупаете лифчик бикини, он хорошо подойдет [EmmaX.Name_dat]."
                            $ Player.Inventory.append("Emma bikini top")
                            $ Player.Cash -= 60
                        else:
                            "У вас недостаточно средств."
                "Купить белые трусики бикини за $60." if "bikini bottoms" not in EmmaX.Inventory and "Emma bikini bottoms" not in Player.Inventory:
                        if Player.Cash >= 60:
                            "Вы покупаете трусики бикини, они хорошо подойдут [EmmaX.Name_dat]."
                            $ Player.Inventory.append("Emma bikini bottoms")
                            $ Player.Cash -= 60
                        else:
                            "У вас недостаточно средств."
                "Неважно.":
                    pass
        "Подарки для: [LauraX.Name]" if "met" in LauraX.History:
            menu:
                "Купить красный корсет за $70." if "corset" not in LauraX.Inventory and "Laura corset" not in Player.Inventory:
                    if Player.Cash >= 70:
                        "Вы покупаете корсет, он хорошо подойдет [LauraX.Name_dat]."
                        $ Player.Inventory.append("Laura corset")
                        $ Player.Cash -= 70
                    else:
                        "У вас недостаточно средств."
                "Купить красный кружевной корсет за $90." if "lace corset" not in LauraX.Inventory and "Laura lace corset" not in Player.Inventory:
                    if Player.Cash >= 90:
                        "Вы покупаете кружевной корсет, он хорошо подойдет [LauraX.Name_dat]."
                        $ Player.Inventory.append("Laura lace corset")
                        $ Player.Cash -= 90
                    else:
                        "У вас недостаточно средств."
                "Купить красные кружевные трусики за $110." if "lace panties" not in LauraX.Inventory and "Laura lace panties" not in Player.Inventory:
                    if Player.Cash >= 110:
                        "Вы покупаете кружевные трусики, они хорошо подойдут [LauraX.Name_dat]."
                        $ Player.Inventory.append("Laura lace panties")
                        $ Player.Cash -= 110
                    else:
                        "У вас недостаточно средств."
                "Купить черный лифчик бикини за $50." if "bikini top" not in LauraX.Inventory and "Laura bikini top" not in Player.Inventory:
                        if Player.Cash >= 50:
                            "Вы покупаете лифчик бикини, он хорошо подойдет [LauraX.Name_dat]."
                            $ Player.Inventory.append("Laura bikini top")
                            $ Player.Cash -= 50
                        else:
                            "У вас недостаточно средств."
                "Купить черные трусики бикини за $50." if "bikini bottoms" not in LauraX.Inventory and "Laura bikini bottoms" not in Player.Inventory:
                        if Player.Cash >= 50:
                            "Вы покупаете трусики бикини, они хорошо подойдут [LauraX.Name_dat]."
                            $ Player.Inventory.append("Laura bikini bottoms")
                            $ Player.Cash -= 50
                        else:
                            "У вас недостаточно средств."
                "Неважно.":
                    pass

        "Подарки для: [JeanX.Name]" if "met" in JeanX.History:
            menu:
                "Купить черный корсет за $70." if "corset" not in JeanX.Inventory and "Jean corset" not in Player.Inventory:
                    if Player.Cash >= 70:
                        "Вы покупаете корсет, он хорошо подойдет [JeanX.Name_dat]."
                        $ Player.Inventory.append("Jean corset")
                        $ Player.Cash -= 70
                    else:
                        "У вас недостаточно средств."
#                "Buy black lace corset for $90." if "lace corset" not in JeanX.Inventory and "Jean lace corset" not in Player.Inventory:
#                    if Player.Cash >= 90:
#                        "Вы покупаете кружевной корсет, он хорошо подойдет [JeanX.Name]."
#                        $ Player.Inventory.append("Jean lace corset")
#                        $ Player.Cash -= 90
#                    else:
#                        "У вас недостаточно средств."
                "Купить зеленый кружевной лифчик за $90." if "lace bra" not in JeanX.Inventory and "Jean lace bra" not in Player.Inventory:
                    if Player.Cash >= 90:
                        "Вы покупаете кружевной лифчик, он хорошо подойдет [JeanX.Name_dat]."
                        $ Player.Inventory.append("Jean lace bra")
                        $ Player.Cash -= 90
                    else:
                        "У вас недостаточно средств."
                "Купить зеленые кружевные трусики за $110." if "lace panties" not in JeanX.Inventory and "Jean lace panties" not in Player.Inventory:
                    if Player.Cash >= 110:
                        "Вы покупаете кружевные трусики, они хорошо подойдут [JeanX.Name_dat]."
                        $ Player.Inventory.append("Jean lace panties")
                        $ Player.Cash -= 110
                    else:
                        "У вас недостаточно средств."
                "Купить \"X\" образный лифчик бикини за $50." if "bikini top" not in JeanX.Inventory and "Jean bikini top" not in Player.Inventory:
                        if Player.Cash >= 50:
                            "Вы покупаете лифчик бикини, он хорошо подойдет [JeanX.Name_dat]."
                            $ Player.Inventory.append("Jean bikini top")
                            $ Player.Cash -= 50
                        else:
                            "У вас недостаточно средств."
                "Купить черные трусики бикини за $50." if "bikini bottoms" not in JeanX.Inventory and "Jean bikini bottoms" not in Player.Inventory:
                        if Player.Cash >= 50:
                            "Вы покупаете трусики бикини, они хорошо подойдут [JeanX.Name_dat]."
                            $ Player.Inventory.append("Jean bikini bottoms")
                            $ Player.Cash -= 50
                        else:
                            "У вас недостаточно средств."
                "Купить колготки за $50." if "pantyhose" not in JeanX.Inventory and "Jean pantyhose" not in Player.Inventory:
                    if Player.Cash >= 50:
                        "Вы покупаете колготки, они хорошо подойдут [JeanX.Name_dat]."
                        $ Player.Inventory.append("Jean pantyhose")
                        $ Player.Cash -= 50
                    else:
                        "У вас недостаточно средств."
#                "Buy stockings and garterbelt for $100." if "stockings and garterbelt" not in JeanX.Inventory and "stockings and garterbelt" not in Player.Inventory and ApprovalCheck(JeanX, 800):
#                    if Player.Cash >= 100:
#                        "You purchase the stockings, these will look nice on [JeanX.Name]."
#                        $ Player.Inventory.append("stockings and garterbelt")
#                        $ Player.Cash -= 100
#                    else:
#                        "У вас недостаточно средств."
                "Неважно.":
                    pass
        "Подарки для: [StormX.Name]" if "met" in StormX.History:
            menu:
                "Купить черный кружевной лифчик за $90." if "lace bra" not in StormX.Inventory and "Storm lace bra" not in Player.Inventory:
                        if Player.Cash >= 90:
                            "Вы покупаете кружевной лифчик, он хорошо подойдет [StormX.Name_dat]."
                            $ Player.Inventory.append("Storm lace bra")
                            $ Player.Cash -= 90
                        else:
                            "У вас недостаточно средств."
                "Купить черные кружевные трусики за $110." if "lace panties" not in StormX.Inventory and "Storm lace panties" not in Player.Inventory:
                        if Player.Cash >= 110:
                            "Вы покупаете кружевные трусики, они хорошо подойдут [StormX.Name_dat]."
                            $ Player.Inventory.append("Storm lace panties")
                            $ Player.Cash -= 110
                        else:
                            "У вас недостаточно средств."
                "Купить колготки за $50." if "pantyhose" not in StormX.Inventory and "Storm pantyhose" not in Player.Inventory:
                    if Player.Cash >= 50:
                        "Вы покупаете колготки, они хорошо подойдут [StormX.Name_dat]."
                        $ Player.Inventory.append("Storm pantyhose")
                        $ Player.Cash -= 50
                    else:
                        "У вас недостаточно средств."
#                "Buy stockings and garterbelt for $100." if "stockings and garterbelt" not in StormX.Inventory and "stockings and garterbelt" not in Player.Inventory and ApprovalCheck(StormX, 1500):
#                    if Player.Cash >= 100:
#                        "You purchase the stockings, these will look nice on [StormX.Name]."
#                        $ Player.Inventory.append("stockings and garterbelt")
#                        $ Player.Cash -= 100
#                    else:
#                        "У вас недостаточно средств."
                "Купить черный лифчик бикини за $60." if "bikini top" not in StormX.Inventory and "Storm bikini top" not in Player.Inventory:
                        if Player.Cash >= 60:
                            "Вы покупаете лифчик бикини, он хорошо подойдет [StormX.Name_dat]."
                            $ Player.Inventory.append("Storm bikini top")
                            $ Player.Cash -= 60
                        else:
                            "У вас недостаточно средств."
                "Купить черные трусики бикини за $60." if "bikini bottoms" not in StormX.Inventory and "Storm bikini bottoms" not in Player.Inventory:
                        if Player.Cash >= 60:
                            "Вы покупаете трусики бикини, они хорошо подойдут [StormX.Name_dat]."
                            $ Player.Inventory.append("Storm bikini bottoms")
                            $ Player.Cash -= 60
                        else:
                            "У вас недостаточно средств."
                "Неважно.":
                    pass

        "Подарки для: [GwenX.Name]" if "met" in GwenX.History:
            menu:
                "Купить белый кружевной лифчик за $90." if "lace bra" not in GwenX.Inventory and "Gwen lace bra" not in Player.Inventory:
                        if Player.Cash >= 90:
                            "Вы покупаете кружевной лифчик, он хорошо подойдет [GwenX.Name_dat]."
                            $ Player.Inventory.append("Gwen lace bra")
                            $ Player.Cash -= 90
                        else:
                            "У вас недостаточно средств."
                "Купить белые кружевные трусики за $110." if "lace panties" not in GwenX.Inventory and "Gwen lace panties" not in Player.Inventory:
                        if Player.Cash >= 110:
                            "Вы покупаете кружевные трусики, они хорошо подойдут [GwenX.Name_dat]."
                            $ Player.Inventory.append("Gwen lace panties")
                            $ Player.Cash -= 110
                        else:
                            "У вас недостаточно средств."
                "Купить колготки за $50." if "pantyhose" not in GwenX.Inventory and "Gwen pantyhose" not in Player.Inventory:
                    if Player.Cash >= 50:
                        "Вы покупаете колготки, они хорошо подойдут [GwenX.Name_dat]."
                        $ Player.Inventory.append("Gwen pantyhose")
                        $ Player.Cash -= 50
                    else:
                        "У вас недостаточно средств."
#                "Buy stockings and garterbelt for $100." if "stockings and garterbelt" not in StormX.Inventory and "stockings and garterbelt" not in Player.Inventory and ApprovalCheck(StormX, 1500):
#                    if Player.Cash >= 100:
#                        "You purchase the stockings, these will look nice on [StormX.Name]."
#                        $ Player.Inventory.append("stockings and garterbelt")
#                        $ Player.Cash -= 100
#                    else:
#                        "У вас недостаточно средств."
                "Купить розовый лифчик бикини за $60." if "bikini top" not in GwenX.Inventory and "Gwen bikini top" not in Player.Inventory:
                        if Player.Cash >= 60:
                            "Вы покупаете лифчик бикини, он хорошо подойдет [GwenX.Name_dat]."
                            $ Player.Inventory.append("Gwen bikini top")
                            $ Player.Cash -= 60
                        else:
                            "У вас недостаточно средств."
                "Купить розовые трусики бикини за $60." if "bikini bottoms" not in GwenX.Inventory and "Gwen bikini bottoms" not in Player.Inventory:
                        if Player.Cash >= 60:
                            "Вы покупаете трусики бикини, они хорошо подойдут [GwenX.Name_dat]."
                            $ Player.Inventory.append("Gwen bikini bottoms")
                            $ Player.Cash -= 60
                        else:
                            "У вас недостаточно средств."
                "Неважно.":
                    pass

        "Купить книги":
            menu Shop_Books:
                "Купить \"Ослепительная и Счастливчик\" за $20.":
                    "Счастливая романтическая история о двух влюбленных, благословленных звездами."
                    if "DL" not in Shop_Inventory: #if Inventory_Check("Dazzler and Longshot") >= 4:
                        "В данный момент, похоже, ее нет в наличие."
                    elif Player.Cash >= 20:
                        "Вы покупаете книгу."
                        $ Shop_Inventory.remove("DL")
                        $ Player.Inventory.append("Dazzler and Longshot")
                        $ Player.Cash -= 20
                    else:
                        "У вас недостаточно средств."
                "Купить \"256 Оттенков Серого\" за $20.":
                    "Захватывающий сексуальный триллер о суровой рыжеволосой \"королеве гоблинов\" и ее похождениях."
                    if "G" not in Shop_Inventory: #if "256 Shades of Grey" in Player.Inventory:
                        "В данный момент, похоже, ее нет в наличие."
                    elif Player.Cash >= 20:
                        "Вы покупаете книгу."
                        $ Shop_Inventory.remove("G")
                        $ Player.Inventory.append("256 Shades of Grey")
                        $ Player.Cash -= 20
                    else:
                        "У вас недостаточно средств."
                "Купить \"Пентхаус Башни Мстителей\" за $20.":
                    "Книга, наполненная фотографиями сексуальных, обнаженных Мстителей."
                    if "A" not in Shop_Inventory:
                        "В данный момент, похоже, ее нет в наличие."
                    elif Player.Cash >= 20:
                        "Вы покупаете книгу."
                        $ Shop_Inventory.remove("A")
                        $ Player.Inventory.append("Avengers Tower Penthouse")
                        $ Player.Cash -= 20
                    else:
                        "У вас недостаточно средств."
                "Назад":
                    jump Shop
            jump Shop_Books
        "Купить Одеколон":
            if Day < 50:
                "В настоящее время этого товара нет на складе, загляните позже."
                jump Shop
            menu:
                "Посмотреть на Одеколон с Феромонами Обезьян (\"Ничто так не расскажет о вашей любви, как красная сияющая задница\").":
                    menu:
                        "Одеколон гарантирует, что женщины Вас полюбят [[+Любовь]."
                        "Купить Одеколон с  Феромонами Обезьян за $150":
                            pass
                        "Неважно.":
                            jump Shop
                    if "Mandrill Cologne" in Player.Inventory:
                        "К сожалению, этого товара сейчас нет на складе, загляните позже."
                    elif Player.Cash >= 150:
                        "Вы покупаете один флакон одеколона с Феромонами Обезьян."
                        $ Player.Inventory.append("Mandrill Cologne")
                        $ Player.Inventory.append("Mandrill Cologne")
                        $ Player.Inventory.append("Mandrill Cologne")
                        $ Player.Inventory.append("Mandrill Cologne")
                        $ Player.Inventory.append("Mandrill Cologne")
                        $ Player.Cash -= 150
                    else:
                        "У вас недостаточно средств."
                "Посмотреть на 'Пурпурный дождь' (\"Они не смогут устоять против ваших чар\").":
                    menu:
                        "Этот одеколон гаранирует, что женщины станут более сговорчивыми вплоть до завтрашнего утра [[+Послушание]."
                        "Купить одеколон 'Пурпурный дождь' за $200":
                            pass
                        "Неважно.":
                            jump Shop
                    if "Purple Rain Cologne" in Player.Inventory:
                        "К сожалению, этого товара сейчас нет на складе, загляните позже."
                    elif Player.Cash >= 200:
                        "Вы покупаете один флакон одеколона 'Пурпурный дождь'."
                        $ Player.Inventory.append("Purple Rain Cologne")
                        $ Player.Inventory.append("Purple Rain Cologne")
                        $ Player.Inventory.append("Purple Rain Cologne")
                        $ Player.Inventory.append("Purple Rain Cologne")
                        $ Player.Inventory.append("Purple Rain Cologne")
                        $ Player.Inventory.append("Purple Rain Cologne")
                        $ Player.Cash -= 200
                    else:
                        "У вас недостаточно средств."
                "Посмотреть на Одеколон 'Раскрепощение' (\"Выпусти своего зверя наружу\").":
                    menu:
                        "Этот одеколон гарантирует, что женщина станет более развязной [[+Раскрепощенность]."
                        "Купить Одеколон 'Раскрепощение' за $250":
                            pass
                        "Неважно.":
                            jump Shop
                    if "Corruption Cologne" in Player.Inventory:
                        "К сожалению, этого товара сейчас нет на складе, загляните позже."
                    elif Player.Cash >= 250:
                        "Вы покупаете один флакон одеколона 'Раскрепощение'."
                        $ Player.Inventory.append("Corruption Cologne")
                        $ Player.Inventory.append("Corruption Cologne")
                        $ Player.Inventory.append("Corruption Cologne")
                        $ Player.Inventory.append("Corruption Cologne")
                        $ Player.Inventory.append("Corruption Cologne")
                        $ Player.Cash -= 250
                    else:
                        "У вас недостаточно средств."
                "Назад":
                    pass
        "Выйти из магазина":
            return
    jump Shop
return

# end Shop Interface / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start LikeUpdater / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#label LikeUpdater(Primary = 0, Value = 1, Noticed = 1,BO=[]):
#    # call LikeUpdater(RogueX,1)
#    # Primary is the primary girl in action, Value is the amount added/subtracted
#    # Noticed is whether it matters if she notices or not.
#    $ BO = TotalGirls[:]
#    if Primary
#    while BO:
#            if BO[0]Loc == bg_current:
#                    if not Noticed or "noticed " + Primary.Tag in BO[0].RecentActions: # if "noticed Rogue"
#                                #If girl was participating in Primary's activity
#                                $ Primary.GirlLikeUp(BO[0],Value)
#                                $ BO[0].GirlLikeUp(Primary,Value)
#            $ BO.remove(BO[0])
#    return

# End LikeUpdater / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Display/Animation Stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Start Set the Scene  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Set_The_Scene(Chara = 1, Entry = 0, Dress = 1, TrigReset = 1, Quiet=0, Class=0, DLoc = 0, YLoc=50, BO=[],DO=[]): #rkeljsvgb
        # If Chara, then display the characters in the room
        # If Entry, then show the "entry" version of a room, such as a closed door, does not display characters
        # If Dress, then check whether the character is underdressed when displaying her, DO is characters getting dressed
        # Trigreset resets triggers
        # if Quiet, no fade to black

        if not Quiet:
                show blackscreen onlayer black

        if Entry == 1:
                $ Chara = 0
#                call AllHide
                scene onlayer master #new, good idea?
                $ renpy.free_memory()

        call Display_Background(Entry)

        if Time_Count >= 3:
                show NightMask onlayer nightmask
        else:
                hide NightMask onlayer nightmask

        if TrigReset:
                # resets triggers
                $ Trigger = 0
                $ Trigger2 = 0 if Trigger2 not in ("jackin","jilling") else Trigger2
#                $ TrigReset = 0 #why was this here?

        if Chara:
                #sets location to bg_current, removes extra girls, sets Focus to a girl in the room

                call Present_Check  #culls out Party to 2,

                #Start Display_Girl replcement
                $ BO = TotalGirls[:]
                python:
                    for BX in BO:
                        #Start Hide stuff, removes all sex poses
                        renpy.hide(BX.Tag+"_SexSprite")
                        renpy.hide(BX.Tag+"_Doggy_Animation")
                        renpy.hide(BX.Tag+"_HJ_Animation")
                        renpy.hide(BX.Tag+"_BJ_Animation")
                        renpy.hide(BX.Tag+"_TJ_Animation")
                        renpy.hide(BX.Tag+"_Finger_Animation")
                        renpy.hide(BX.Tag+"_CUN_Animation")
                        renpy.hide(BX.Tag+"_69_CUN")
                        renpy.hide(BX.Tag+"_69_Animation")
                        renpy.hide(BX.Tag+"_SC_Sprite")
                        renpy.hide(BX.Tag+"_Seated")
                        renpy.hide(BX.Tag+"_PJ_Animation") #Jean, mainly
                        renpy.hide(BX.Tag+"_FJ_Animation") #Emma, mainly
                        #End Hide stuff, removes all sex poses, sprite only removed if girl not there
                        if BX not in Party and BX.Loc != bg_current:
                                # If girl isn't there, put her away  (does this interact well with Nearby stuff?)
                                renpy.hide(BX.Tag+"_Sprite")
                                BX.OutfitChange(Changed=1)
                                continue #skips to next girl

                        if Dress:
                                #if the dress tag, dress her appropriately to specific areas
                                if BX.Outfit == "swimwear":
                                    if BX.Loc == "bg pool":
                                        BX.OutfitChange(Changed=1)
                                    elif BX.OutfitDay != "swimwear":
                                        BX.Outfit = BX.OutfitDay
                                        BX.OutfitChange(Changed=1)
                                elif Taboo: #If not in the showers, get dressed and dry off
                                        BX.OutfitChange(Changed=1)
                                elif BX.Loc != "bg dangerroom":
                                        #if she's not in the gym and is wearing gym clothes. . .
                                        BX.Outfit = BX.OutfitDay
                                        BX.OutfitChange(Changed=1)
                                DO.append(BX) #adds girl for later queue

                        if BX.Loc != "bg showerroom" and BX.Loc != "bg pool":
                                        BX.Water = 0

                        BX.Offhand = 0 if TrigReset else BX.Offhand

#                        if DLoc: #if sent a pre-location, use that, otherwise, accept the existing one.
#                                        BX.SpriteLoc = DLoc
#                        elif Partner is BX:
#                                        DLoc = StageRight #Moves Girl over if she's secondary
#                        else:
#                                        DLoc = BX.SpriteLoc
#                        #Start Hide stuff, removes all sex poses
#                        renpy.hide(BX.Tag+"_SexSprite")
#                        renpy.hide(BX.Tag+"_Doggy_Animation")
#                        renpy.hide(BX.Tag+"_HJ_Animation")
#                        renpy.hide(BX.Tag+"_BJ_Animation")
#                        renpy.hide(BX.Tag+"_TJ_Animation")
#                        renpy.hide(BX.Tag+"_Finger_Animation")
#                        renpy.hide(BX.Tag+"_CUN_Animation")
#                        renpy.hide(BX.Tag+"_69_Animation")
#                        renpy.hide(BX.Tag+"_69_CUN")
#                        renpy.hide(BX.Tag+"_Seated")
#                        #end Hide stuff

                        #displays girl if present, Sets her as local if in a party
                        BX.Loc = bg_current

                        if BX is Ch_Focus:
                                BX.SpriteLoc = StageCenter
                                BX.Layer = 100
                        else:
                                #moves all other girls to Stage Right, 75 layer
                                BX.SpriteLoc = StageRight
                                BX.Layer = 75
                        if bg_current == "bg movies" or bg_current == "bg restaurant":
                                #shifts them downward if on a date
                                YLoc = 250
                                BX.SpriteLoc = StageRight if BX is Ch_Focus else StageLeft
                        else:
                                YLoc = 50

#                        #Display Girl

                        if BX is LauraX:
                                BX.Claws = 0 # Resets her claws
                        elif BX is BetsyX:
                                BX.Knife = 0 # Resets her psy knife
                        elif BX is DoreenX:
                                BX.Layer = 74 #sets her behind other girls in order
#                        DO.append(BX) #adds girl for later queue

                        renpy.show(BX.Tag+"_Sprite",at_list=[Sprite_Set(BX.SpriteLoc,YLoc)],zorder=BX.Layer)
        #                show Rogue_Sprite at SpriteLoc(DLoc,YLoc) zorder RogueX.Layer:
        #                        zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.6, 0.0)
                        #End show BX
                #End python loop

                if Dress:
                        #If in public, check to see if clothes are too sexy, and change them if necessary
                        while DO:
                            call OutfitShame(DO[0])
                            $ DO.remove(DO[0])
                #End Display_Girl replcement

#                if bg_current == "bg study" and Time_Count < 3:
#                        show Professor at SpriteLoc(StageLeft) zorder 25
#                else:
#                        hide Professor
        else:
#                        call AllHide(1) #removes all girls that aren't there.
                        scene onlayer master #new, good idea?
        show Chibi_UI
        hide Cellphone

        if bg_current == "bg classroom":
            if EmmaX.Loc == "bg teacher":
                    #if Emma is teaching, sets teaching outfit
                    call AltClothes(EmmaX,8)
                    $ EmmaX.OutfitChange()
            elif StormX.Loc == "bg teacher":
                    #if Storm is teaching, sets teaching outfit
                    call AltClothes(StormX,8)
                    $ StormX.OutfitChange()
#            if Class and Time_Count < 2:
#                    #only gets checked if by the classroom location
#                    #only applies during class periods
#                    call Class_Nearby
#                    call Class_Adjacent
#            else:
#                    call Clear_Seated
        if bg_current == "bg showerroom":
                show Shower_Steam zorder 151:
                    pos (500,800)
        else:
                hide Shower_Steam
        if bg_current == "bg restaurant":
                show dinnertable onlayer nightmask
        else:
                hide dinnertable onlayer nightmask
        if bg_current == "bg pool":
                call Pool_Nearby
        else:
                #hides pool overlay if not in the pool area
                hide FullPool

        if TrigReset and Dress:
                #resets your clothing if nude
                call Get_Dressed

#        if Entry == 2:
#                show bg_opendoor zorder 151
        hide bg_opendoor
        hide DressScreen
        if "Historia" in Player.Traits: #Simulation haze
                show BlueScreen onlayer black
        else:
                hide BlueScreen onlayer black
        hide blackscreen onlayer black
        return

label Class_Setting:
        if bg_current == "bg classroom":
            if Weekday < 5 and Time_Count < 2:
                    #only gets checked if by the classroom location
                    #only applies during class periods
                    call Class_Nearby
                    call Class_Adjacent
            else:
                    call Clear_Seated
        return
# End primary Display function / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start shift Focus / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Shift_Focus(Chr = RogueX, Second = 0,BO=[],Return=0):
        #When used like Shift_Focus(KittyX), changes the focus character and relative default positions
        if Chr not in TotalGirls:
                "Tell Oni [Chr]"
                "Then Tell Oni [Chr.Tag]"
        if Chr == Ch_Focus == Partner:
                #if somehow the partner and chosen girl are the same. . .
                $ BO = TotalGirls[:]
                if Partner in TotalGirls:
                        $ BO.remove(Partner)
                else:
                        "Tell Oni, in Shift Focus, P:[Partner]"
                $ Partner = 0
                python:
                    for BX in BO:
                        #loops through and makes choices.
                        if BX.Loc == bg_current:
                                Partner = BX
                                break
                #if anyone else is in the room, make her the partner. Do I want this?
        if Chr.Loc == bg_current:
                #If she is where you're at. . .
                $ BO = TotalGirls[:]
#                if Chr in TotalGirls:
#                        $ BO.remove(Chr)
#                else:
#                        "Tell Oni, in Shift Focus, C:[Chr]"
                python:
                    for BX in BO:
                        #loops through and makes choices.
                        if BX != Chr and BX.Loc == bg_current:
                                #if other girl is in the room, shift her to second position
                                BX.SpriteLoc = StageRight
                                BX.Layer = 75
                                #break
#                while BO:
#                        #loops through and makes choices.
#                        if BO[0].Loc == bg_current:
#                                #if other girl is in the room, shift her to second position
#                                $ BO[0].SpriteLoc = StageRight
#                                $ BO[0].Layer = 75
#                                $ BO = [1]
#                        $ BO.remove(BO[0])
                #and move Girl to first position
                $ Chr.SpriteLoc = StageCenter
                $ Chr.Layer = 100
        if Ch_Focus == Chr:
                #If Girl was already the focal character, return
                pass
        elif Second and Second != Chr:
                #if a deliberate partner was offered to the call, use it
                $ Partner = Second
        elif Partner is Chr:
                #If Chr was the Partner in a scene, make the existing focal character the Partner
                $ Partner = Ch_Focus
        $ Ch_Focus = Chr
        $ UI_Focus = Chr
        if Partner is Chr:
                $ Partner = 0

        $ renpy.restart_interaction()
#        if Return:
#            "[Chr.Tag]"
#            return Chr
        return

label Shift_UI(Chr = RogueX, Second = 0,BO=[],Return=0):
        #When used like This swaps who the UI is focused on.
        if Chr not in TotalGirls:
                "Tell Oni [Chr]"
                "Then Tell Oni [Chr.Tag]"
        $ UI_Focus = Chr
        $ renpy.restart_interaction()
        return
# End shift Focus / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Display Girls / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
transform SpriteLoc(Loc = StageRight, LocY = 50):
        #This puts the sprite at a location relative to the sent variable
        pos (Loc,LocY)

transform Sprite_Set(LocX = StageRight, LocY = 50,Alp=1,ZM=1,XOff=0,YOff=0,XAn=0.5,YAn=0,XZM=1,YZM=1):
        #This puts the sprite at a location relative to the sent variable
        pos (LocX,LocY) alpha Alp zoom ZM offset (XOff,YOff) anchor (XAn,YAn) xzoom XZM yzoom YZM

label Display_Girl(Chr=0,Dress = 1, TrigReset = 1, DLoc = 0, YLoc=50): #rkeljsvgb
                # If Dress, then check whether the character is underdressed when displaying her
                # call Display_Girl(RogueX,0,0)
                if Chr not in TotalGirls:
                        "Tell Oni that in Display_Girl, Chr is [Chr]"
                        return

                if Chr not in Party and Chr.Loc != bg_current:
                        # If girl isn't there, put her away
                        call Girl_Hide(Chr,1)
                        $ Chr.OutfitChange(Changed=1)
                        return

                if Dress:
                        if Chr.Outfit == "swimwear":
                            if Chr.Loc == "bg pool":
                                $ Chr.OutfitChange(Changed=1)
                            elif Chr.OutfitDay != "swimwear":
                                $ Chr.Outfit = Chr.OutfitDay
                                $ Chr.OutfitChange(Changed=1)
                        elif Taboo: #If not in the showers, get dressed and dry off
                                $ Chr.OutfitChange(Changed=1)
                        elif Chr.Loc != "bg dangerroom":
                                #if she's not in the gym and is wearing gym clothes. . .
                                $ Chr.Outfit = Chr.OutfitDay
                                $ Chr.OutfitChange(Changed=1)

                elif Chr.Loc != "bg showerroom" and Chr.Loc != "bg pool":
                        $ Chr.Water = 0

                if TrigReset:
                        # resets triggers
                        $ Trigger = 0
                        $ Trigger2 = 0 if Trigger2 not in ("jackin","jilling") else Trigger2
                        $ Chr.Offhand = 0               #  $ Trigger3 = 0# $ Trigger4 = 0# $ Trigger5 = 0


#                if DLoc: #if sent a pre-location, use that, otherwise, accept the existing one.
#                        $ Chr.SpriteLoc = DLoc
#                elif Partner is Chr:
#                        $ DLoc = StageRight #Moves Girl over if she's secondary
#                else:
#                        $ DLoc = StageCenter

                call Girl_Hide(Chr)

                #displays girl if present, Sets her as local if in a party
                $ Chr.Loc = bg_current

                if Dress:
                        #If in public, check to see if clothes are too sexy, and change them if necessary
                        call OutfitShame(Chr)

                if Chr is Ch_Focus:
                        $ Chr.SpriteLoc = StageCenter
                        $ DLoc = StageCenter
                        $ Chr.Layer = 100
                else:
                        #moves all other girls to Stage Right, 75 layer
                        $ Chr.SpriteLoc = StageRight
                        $ DLoc = StageRight
                        $ Chr.Layer = 75

                if bg_current == "bg movies" or bg_current == "bg restaurant":
                        #shifts them downward if on a date
                        $ YLoc = 250
                        $ DLoc = StageRight if Chr == Ch_Focus else StageLeft
                else:
                        $ YLoc = 50

                #Display Girl

                if Chr is LauraX:
                        $ Chr.Claws = 0 # Resets her claws
                elif Chr is BetsyX:
                        $ Chr.Knife = 0 # Resets her psy knife
                elif Chr is DoreenX:
                        $ Chr.Layer = 74 #sets her behind other girls in order

                $ renpy.show(Chr.Tag+"_Sprite",at_list=[Sprite_Set(DLoc,YLoc)],zorder=Chr.Layer)
#                show Rogue_Sprite at SpriteLoc(DLoc,YLoc) zorder RogueX.Layer:
#                        zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.6, 0.0)
                #End show Chr
                return


#Start QuickDisplay / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label QuickDisplay(Girl=0,XLoc=0,YLoc=0):
        #Displayed girl sprite at chosen position
        # call QuickDisplay(Girl,StageRight,50)
        if Girl not in TotalGirls:
                return
        $ XLoc = StageRight if not XLoc else XLoc
        $ YLoc = 50 if not YLoc else YLoc
        $ renpy.show(Girl.Tag+"_Sprite",at_list=[SpriteLoc(XLoc,YLoc)],zorder=Girl.Layer)
        return
# End Display Girls / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label ViewShift(Girl=0,View=0,ShouldHide=1,ViewTrig=Trigger):
    # Allows you to shift the viewpoint of a girl in fondling modes
    # call ViewShift(RogueX,"breasts")
    if Girl not in TotalGirls:
            return
    if View == "menu":
            if renpy.showing("PhoneSex"):
                menu:
                    "Все тело":
                            $ Girl.Pose = 0
                    "Вид сзади": #if Girl not in (DoreenX,1):
                            $ Girl.Pose = "doggy"
                            call View_Facing(Girl)
                    "Лицом вперед" if Girl in (EmmaX,JeanX,StormX):
                            $ Girl.Pose = "sex"
                    "Лежа" if Girl in (RogueX,KittyX,LauraX,JubesX,GwenX,BetsyX,DoreenX,WandaX):
                            $ Girl.Pose = "sex"
                    "Неважно":
                            pass
                return
#            elif not renpy.showing(Girl.Tag+"_Sprite") and not renpy.showing(Girl.Tag+"_Doggy_Animation") and not renpy.showing(Girl.Tag+"_SexSprite"):
#                    #if she's not already visible, this should not work
#                    return
            menu:
                    "Все тело":
                            call Girl_Pos_Reset(Girl,ViewTrig,1) # call expression Girl.Tag + "_Pos_Reset" pass (ViewTrig,1)
                    "Верхняя часть тела":
                            call Girl_Breasts_Launch(Girl,ViewTrig)  #call expression Girl.Tag + "_Breasts_Launch" pass (ViewTrig)
                    "Посередине":
                            call Girl_Middle_Launch(Girl,ViewTrig)  #call expression Girl.Tag + "_Middle_Launch" pass (ViewTrig)
                    "Нижняя часть тела":
                            call Girl_Pussy_Launch(Girl,ViewTrig)  #call expression Girl.Tag + "_Pussy_Launch" pass (ViewTrig)
                    "Вид сзади": # if Girl not in (DoreenX,1):
                            $ Girl.Pose = "doggy"
                            call View_Facing(Girl)
                            call expression Girl.Tag + "_Sex_Launch" pass (ViewTrig)
                    "На вас сверху" if Girl in (EmmaX,JeanX,StormX):
                            $ Girl.Pose = "sex"
                            call expression Girl.Tag + "_Sex_Launch" pass (ViewTrig)
                    "Лежа" if Girl in (RogueX,KittyX,LauraX,JubesX,GwenX,BetsyX,DoreenX,WandaX):
                            $ Girl.Pose = "sex"
                            call expression Girl.Tag + "_Sex_Launch" pass (ViewTrig)
                    " 69 [[locked] (locked)" if "69" not in Girl.History:
                            pass
                    " 69 " if "69" in Girl.History:
                            $ Girl.Pose = "69"
                            call expression Girl.Tag + "_BJ_Launch" pass (ViewTrig)
                    "Неважно":
                            pass
    else:
                    if renpy.showing("PhoneSex"):
                            $ Player.Sprite = 0
                            $ Player.Cock == 'out'
                            $ Speed = 0
                            if View == "doggy":
                                    $ Girl.Pose = "doggy"
                            elif View == "sex":
                                    $ Girl.Pose = "sex"
                            else:
                                    $ Girl.Pose = 0
                            return
                    if ShouldHide:
                            call Girl_Hide(Girl)
                    if View == "full":
                            call Girl_Pos_Reset(Girl,ViewTrig,1) #call expression Girl.Tag + "_Pos_Reset" pass (ViewTrig,1)
                    elif View == "breasts":
                            call Girl_Breasts_Launch(Girl,ViewTrig)  #call expression Girl.Tag + "_Breasts_Launch" pass (ViewTrig)
                    elif View == "mid":
                            call Girl_Middle_Launch(Girl,ViewTrig)  #call expression Girl.Tag + "_Middle_Launch" pass (ViewTrig)
                    elif View == "pussy":
                            call Girl_Pussy_Launch(Girl,ViewTrig)  #call expression Girl.Tag + "_Pussy_Launch" pass (ViewTrig)
                    elif View == "doggy" or View == "sex":
                            call expression Girl.Tag + "_Sex_Launch" pass (ViewTrig)
                    elif View == "69":
                            call expression Girl.Tag + "_BJ_Launch" pass (ViewTrig)
                    elif View == "kiss":
                            call Girl_Kissing_Launch(Girl,ViewTrig)  #call expression Girl.Tag + "_Kissing_Launch" pass (ViewTrig)
    return

label View_Facing(Girl=0,Auto=0):
        #called from ViewShift and sex acts, checks whether she is facing forward or not during doggy style
        if Girl not in TotalGirls or Girl.Pose != "doggy":
                return
        if Auto:
            $ Girl.Facing = 0 if Girl.Facing else 1
        else:
            menu:
                "Лицом к вам":
                    $ Girl.Facing = 0
                "Лицом вперед":
                    $ Girl.Facing = 1

        if not Girl.Facing:
                "Вы поворачиваете ее голову лицом к себе."
        else:
                if Girl.Inbt > (1.5*Girl.Obed):
                    $ Girl.FaceChange("angry",2)
                    pause 0.3
                    $ Girl.Facing = 0
                    "Вы пытаетесь повернуть ее голову вперед, но она отказывается."
                    if ApprovalCheck(Girl, 700, "L"):
                            $ Girl.FaceChange("smile",1)
                    else:
                            $ Girl.FaceChange("normal",1)
                elif "facing" in Girl.DailyActions:
                    pass
                else:
                    $ Girl.AddWord(1,0,"facing")
                    if not ApprovalCheck(Girl, 500, "O"):
                            $ Girl.Statup("Love", 90, -2)
                            $ Girl.Statup("Obed", 80, 2)
                            $ Girl.FaceChange("sadside")
                    $ Girl.Statup("Obed", 80, 1)
                    "Вы поворачиваете ее голову лицом вперед."
        return

label WardrobeView(Girl=0,View=0,ViewTrig=Trigger):
        # Allows you to shift the viewpoint of a girl in fondling modes
        # call WardrobeView(RogueX)
        if Girl not in TotalGirls or Girl.Loc != bg_current:
                return
        menu:
            "Все тело":
                    call Girl_Pos_Reset(Girl,ViewTrig,1) #call expression Girl.Tag + "_Pos_Reset" pass (ViewTrig,1)
            "Верхняя часть тела":
                    call Girl_Breasts_Launch(Girl,ViewTrig)     #call expression Girl.Tag + "_Breasts_Launch" pass (ViewTrig)
            "Посередине":
                    call Girl_Middle_Launch(Girl,ViewTrig)     #call expression Girl.Tag + "_Middle_Launch" pass (ViewTrig)
            "Нижняя часть тела":
                    call Girl_Pussy_Launch(Girl,ViewTrig)       #call expression Girl.Tag + "_Pussy_Launch" pass (ViewTrig)
            "Ноги":
                    call Girl_Feet_Launch(Girl)
            "Вид сзади": # if Girl not in (DoreenX,1):
                    $ Girl.Pose = "doggy"
                    call View_Facing(Girl)
                    call expression Girl.Tag + "_Sex_Launch" pass (ViewTrig)
            "Неважно":
                    pass
        return

image Punchout:
    Null(0,0)

label Punch:
    #causes the screen to shake a bit
    show Punchout with vpunch
    hide Punchout
    return

# All Reset / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label AllReset(Chr = 0,BO=[]): #rkeljsvg
        #resets all the sex animation poses
        #call AllReset("all")
        if Chr in TotalGirls:
                $ BO = [Chr]
        else:
                $ BO = TotalGirls[:]

        while BO:
                call expression BO[0].Tag + "_BJ_Reset"
                call expression BO[0].Tag + "_TJ_Reset"
                call expression BO[0].Tag + "_HJ_Reset"
                call expression BO[0].Tag + "_CUN_Reset"
                call expression BO[0].Tag + "_Finger_Reset"
                call expression BO[0].Tag + "_Sex_Reset"
                call expression BO[0].Tag + "_Doggy_Reset"
                call Girl_Hide(BO[0]) #call expression BO[0].Tag + "_Hide"
                if BO[0].Loc == bg_current:
                        $ renpy.show(BO[0].Tag+"_Sprite",at_list=[Sprite_Set(BO[0].SpriteLoc,50)],zorder=BO[0].Layer)
                else:
                        $ renpy.hide(BO[0].Tag+"_Sprite")
    #                show Rogue_Sprite at SpriteLoc(DLoc,YLoc) zorder RogueX.Layer:
    #                        zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.6, 0.0)
                $ BO.remove(BO[0])
        return
# End All Reset / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Girl_Pos_Reset(Girl=0,T = 0,Set=0):
        if Girl.Loc != bg_current:
                return
        call Girl_Hide(Girl,0)
        $ Girl.Pose = "full" if Set else 0
        $ Trigger = T
        $ renpy.show(Girl.Tag+"_Sprite",at_list=[Sprite_Set(Girl.SpriteLoc,50)],zorder=Girl.Layer)
        return

label Girl_Hide(Girl=0,Sprite=0):
        #call Girl_Hide(Girl,0)
        #hides all sprites for the selected girl
        $ renpy.hide(Girl.Tag+"_SexSprite")
        $ renpy.hide(Girl.Tag+"_Doggy_Animation")
        $ renpy.hide(Girl.Tag+"_HJ_Animation")
        $ renpy.hide(Girl.Tag+"_BJ_Animation")
        $ renpy.hide(Girl.Tag+"_TJ_Animation")
        $ renpy.hide(Girl.Tag+"_Finger_Animation")
        $ renpy.hide(Girl.Tag+"_CUN_Animation")
        $ renpy.hide(Girl.Tag+"_69_CUN")
        $ renpy.hide(Girl.Tag+"_69_Animation")
        $ renpy.hide(Girl.Tag+"_SC_Sprite")
        $ renpy.hide(Girl.Tag+"_Seated")
        $ renpy.hide(Girl.Tag+"_PJ_Animation") #Jean, mainly
        $ renpy.hide(Girl.Tag+"_FJ_Animation") #Emma, mainly
        if Sprite:
                $ renpy.hide(Girl.Tag+"_Sprite")
        return

label AllHide(Cull=0,BO=[]): #rkeljsvgb
        #cycles through all girls and removes them if they are not around
        $ BO = ActiveGirls[:]
        while BO:
                if Cull or BO[0].Loc != bg_current:
                        call Girl_Hide(BO[0],1)
                $ BO.remove(BO[0])
        if Cull or "bg study" != bg_current:
                hide Professor
        return
# End Display/Animation Stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Threesome/Lesbian stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Sex_Menu_Threesome(Girl=0): #rkeljsvgb
        if not Girl or Girl not in TotalGirls:
            return

        menu:
            "Хочешь присоединиться к нам, [RogueX.Name]?" if RogueX.Loc == bg_current and Girl is not RogueX:
                    if Partner is RogueX:
                        #if she's already involved
                        ch_r "Я что-то делаю не так. . .?"
                    else:
                        if Girl is JeanX:
                                #this raises a girl's like-Jean stat if Jean wants to sleep with her
                                call Girl_Whammy(RogueX)
                        call Girls_Noticed(Girl,RogueX,1)
                        if Girl.Loc != bg_current:
                            # if the lead ran away
                            ch_r "Ох, ну. . . по крайне мере, у тебя осталась я. . ."
                            call SexAct("switch") # call Rogue_SexAct("switch")
                        elif RogueX.Loc == bg_current:
                            ch_r "Думаю, я могла бы оказать тебе помощь. . ."
                        else:
                            "Похоже, ее смутила эта ситуация, она выходит из комнаты."

            "Хочешь присоединиться к нам, [KittyX.Name]?" if KittyX.Loc == bg_current and Girl is not KittyX:
                    if Partner is KittyX:
                        #if she's already involved
                        ch_k "Лол, о чем ты вообще?"
                    else:
                        if Girl is JeanX:
                                #this raises a girl's like-Jean stat if Jean wants to sleep with her
                                call Girl_Whammy(KittyX)
                        call Girls_Noticed(Girl,KittyX,1)
                        if Girl.Loc != bg_current:
                            # if the lead ran away
                            ch_k "Ууу, как драматично. . ."
                            call SexAct("switch") # call Kitty_SexAct("switch")
                        elif KittyX.Loc == bg_current:
                            ch_k "Я могу[KittyX.like]попробовать. . ."
                        else:
                            "Похоже, ее смутила эта ситуация, она выходит из комнаты."

            "Хочешь присоединиться к нам, [EmmaX.Name]?" if EmmaX.Loc == bg_current and Girl is not EmmaX:
                    if Partner is EmmaX:
                        #if she's already involved
                        ch_e "Разве я не поспеваю?"
                    else:
                        if Girl is JeanX:
                                #this raises a girl's like-Jean stat if Jean wants to sleep with her
                                call Girl_Whammy(EmmaX)
                        call Girls_Noticed(Girl,EmmaX,1)
                        if Girl.Loc != bg_current:
                            # if the lead ran away
                            ch_e "Какая жалость. . ."
                            call SexAct("switch") # call Emma_SexAct("switch")
                        elif EmmaX.Loc == bg_current:
                            if not Player.Male:
                                ch_e "Интересно, что же ты для нас задумала. . ."
                            else:
                                ch_e "Интересно, что же ты для нас задумал. . ."
                        else:
                            "Похоже, ее смутила эта ситуация, она выходит из комнаты."

            "Хочешь присоединиться к нам, [LauraX.Name]?" if LauraX.Loc == bg_current and Girl is not LauraX:
                    if Partner is LauraX:
                        #if she's already involved
                        ch_l "Я уже с вами."
                    else:
                        if Girl is JeanX:
                                #this raises a girl's like-Jean stat if Jean wants to sleep with her
                                call Girl_Whammy(LauraX)
                        call Girls_Noticed(Girl,LauraX,1)
                        if Girl.Loc != bg_current:
                            # if the lead ran away
                            ch_l "Ну, ей же хуже. . ."
                            call SexAct("switch") # call Laura_SexAct("switch")
                        elif LauraX.Loc == bg_current:
                            ch_l "Хм, ладно. . ."
                        else:
                            "Похоже, ее смутила эта ситуация, она выходит из комнаты."

            "Хочешь присоединиться к нам, [JeanX.Name]?" if JeanX.Loc == bg_current and Girl is not JeanX:
                    if Partner is JeanX:
                        #if she's already involved
                        ch_j "Я здесь, с тобой, все это время. . ."
                    else:
                        call Girls_Noticed(Girl,JeanX,1)
                        if Girl.Loc != bg_current:
                            # if the lead ran away
                            ch_j "Ха, ей же хуже. . ."
                            call SexAct("switch") # call Jean_SexAct("switch")
                        elif JeanX.Loc == bg_current:
                            ch_j "Конечно."
                        else:
                            "She seems annoyed with this whole situation and leaves the room."

            "Хочешь присоединиться к нам, [StormX.Name]?" if StormX.Loc == bg_current and Girl is not StormX:
                    if Partner is StormX:
                        #if she's already involved
                        ch_s "Разве ты не заметил, что я уже с тобой?"
                    else:
                        if Girl is JeanX:
                                #this raises a girl's like-Jean stat if Jean wants to sleep with her
                                call Girl_Whammy(StormX)
                        call Girls_Noticed(Girl,StormX,1)
                        if Girl.Loc != bg_current:
                            # if the lead ran away
                            ch_s "Ох, как жаль. . ."
                            call SexAct("switch") # call Storm_SexAct("switch")
                        elif StormX.Loc == bg_current:
                            ch_s "С радостью. . ."
                        else:
                            "Похоже, ее смутила эта ситуация, она выходит из комнаты."

            "Хочешь присоединиться к нам, [JubesX.Name]?" if JubesX.Loc == bg_current and Girl is not JubesX:
                    if Partner is JubesX:
                        #if she's already involved
                        ch_v "Я думала, что уже с тобой!"
                    else:
                        if Girl is JeanX:
                                #this raises a girl's like-Jean stat if Jean wants to sleep with her
                                call Girl_Whammy(JubesX)
                        call Girls_Noticed(Girl,JubesX,1)
                        if Girl.Loc != bg_current:
                            # if the lead ran away
                            ch_v "Ох, что ж. . ."
                            call SexAct("switch") # call Jubes_SexAct("switch")
                        elif JubesX.Loc == bg_current:
                            ch_v "Конечно!"
                        else:
                            "Похоже, ее смутила эта ситуация, она выходит из комнаты."

            "Хочешь присоединиться к нам, [GwenX.Name]?" if GwenX.Loc == bg_current and Girl is not GwenX:
                    if Partner is GwenX:
                        #if she's already involved
                        ch_g "Я разве не с вами?"
                    else:
                        if Girl is JeanX:
                                #this raises a girl's like-Jean stat if Jean wants to sleep with her
                                call Girl_Whammy(GwenX)
                        call Girls_Noticed(Girl,GwenX,1)
                        if Girl.Loc != bg_current:
                            # if the lead ran away
                            ch_g "Ну ладно. . ."
                            call SexAct("switch") # call Gwen_SexAct("switch")
                        elif GwenX.Loc == bg_current:
                            ch_g "Ага!"
                        else:
                            "Похоже, ее смутила эта ситуация, она выходит из комнаты."

            "Хочешь присоединиться к нам, [BetsyX.Name]?" if BetsyX.Loc == bg_current and Girl is not BetsyX:
                    if Partner is BetsyX:
                        #if she's already involved
                        ch_b "Я уже с тобой."
                    else:
                        if Girl is JeanX:
                                #this raises a girl's like-Jean stat if Jean wants to sleep with her
                                call Girl_Whammy(BetsyX)
                        call Girls_Noticed(Girl,BetsyX,1)
                        if Girl.Loc != bg_current:
                            # if the lead ran away
                            ch_b "С этим разобрались. . ."
                            call SexAct("switch") # call Betsy_SexAct("switch")
                        elif BetsyX.Loc == bg_current:
                            ch_b "Конечно."
                        else:
                            "Похоже, ее смутила эта ситуация, она выходит из комнаты."

            "Хочешь присоединиться к нам, [DoreenX.Name]?" if DoreenX.Loc == bg_current and Girl is not DoreenX:
                    if Partner is DoreenX:
                        #if she's already involved
                        ch_d "Ох. Разве я не с вами?"
                    else:
                        if Girl is JeanX:
                                #this raises a girl's like-Jean stat if Jean wants to sleep with her
                                call Girl_Whammy(DoreenX)
                        call Girls_Noticed(Girl,DoreenX,1)
                        if Girl.Loc != bg_current:
                            # if the lead ran away
                            ch_d "Ну вот, она ушла. . ."
                            call SexAct("switch") # call Doreen_SexAct("switch")
                        elif DoreenX.Loc == bg_current:
                            ch_d "Конечно!"
                        else:
                            "Похоже, ее смутила эта ситуация, она выходит из комнаты."

            "Хочешь присоединиться к нам, [WandaX.Name]?" if WandaX.Loc == bg_current and Girl is not WandaX:
                    if Partner is WandaX:
                        #if she's already involved
                        ch_w "Думала, я уже с вами."
                    else:
                        if Girl is JeanX:
                                #this raises a girl's like-Jean stat if Jean wants to sleep with her
                                call Girl_Whammy(WandaX)
                        call Girls_Noticed(Girl,WandaX,1)
                        if Girl.Loc != bg_current:
                            # if the lead ran away
                            ch_w "Что ж, если ей это не нравится. . ."
                            call SexAct("switch") # call Wanda_SexAct("switch")
                        elif WandaX.Loc == bg_current:
                            ch_w "Конечно!"
                        else:
                            "Похоже, ее смутила эта ситуация, она выходит из комнаты."

            "Неважно [[заняться чем-нибудь другим]":
                    pass
        if AloneCheck(Girl) and Girl.Taboo == 20:
                $ Girl.Taboo = 0
                $ Taboo = 0
        return

label Partner_Like(Girl=0,Value=1,AltValue=1,Measure=800,Partner=Partner):
        # This raises a partner's "like" stat by an amount
        # call Partner_Like(RogueX,2)
        # Girl is the lead, Partner is the second girl
        # Value is the amount it changes if Measure is met, otherwise AltValue
        if Girl not in TotalGirls or Partner not in TotalGirls or Partner == Girl: #should remove "character don't exist" errors
                return


        if Partner.Offhand:
                # if the Partner is doing a secondary action. . .
                if Partner.Offhand == "watch":
                        pass
                elif Partner.Offhand in ("hand","blow","cun","finger","nips"):
                        $ Value += 1
                elif Partner.Offhand in ("lick girl pussy","lick girl ass"):
                        $ Value += 3
                else:
                        $ Value += 2
        #End Trigger4 bonuses

        $ Partner.GLG(Girl,Measure,Value,1)
        $ Girl.GLG(Partner,Measure,Value,1)
        return
#End Partner_Like


# Start Room Stat Booster / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label RoomStatboost(Type=0,Check=0,Amount=0,BO=[]):
        # raises/lowers stats of all girls in the room by a fixed amount
        # ie call RoomStatboost("Love",80,2)
        $ BO = TotalGirls[:]
        python:
            for BX in BO:
                if BX.Loc == bg_current or BX in Nearby:
                        BX.Statup(Type, Check, Amount)
        return
# end Room Stat Booster / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start GirlWaitUp / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label GirlWaitUp(Local=0,Check=70,D20=0,Teach=0,BOA=[],BOB=[]):  #rkeljsvgb
        #This adjusts girl's liking each other based on shared activities
        #Local =1 only checks if they are in the room with you.
        #it goes R+K, R+E, R+L, K+E, K+L, E+L, etc.
        # was call GirlWaitAttract()
        # now call GirlWaitUp

        $ D20 = renpy.random.randint(0,1) if not D20 else D20

        if EmmaX.Loc == "bg teacher":
                $ EmmaX.Loc = "bg classroom" #Sets Emma to being in class if she's teaching
                $ Teach = 1
        elif StormX.Loc == "bg teacher":
                $ StormX.Loc = "bg classroom" #Sets Storm to being in class if she's teaching
                $ Teach = 2
        $ BOA = TotalGirls[:]
        #$ BOA.extend(TotalGirls)

        python:
            for BX in BOA:
                #loops through the girls in an outer loop
                BOB = TotalGirls[:]
                for BY in BOB:
                        #loops through the girls in an inner loop
                        if BX != BY and BX.Loc == BY.Loc:
                                #if the two girls are not identical, and are in the same location. . .
                                if BX.Loc == "bg classroom":
                                                BX.GLG(BY,700,1,1)
                                                #R_LikeKitty += 1
                                elif BX.Loc == "bg dangerroom":
                                                BX.GLG(BY,700,(1+D20),1)
                                                #R_LikeKitty += 1+D20
                                elif BX.Loc == "bg showerroom":
                                        if BX is EmmaX:
                                                #if it's EmmaX. . .
                                                BX.GLG(BY,900,3,1)
                                                #EmmaX.LikeKitty += 3
                                        elif BY in (EmmaX,StormX) and BX is not LauraX:
                                                #If it's anyone other than Laura seeing Emma's body. . .
                                                BX.GLG(BY,900,3,1)
                                                #RogueX.LikeEmma += 3
                                        else:
                                                BX.GLG(BY,900,2,1)
                                                #RogueX.LikeKitty += 2
                                else:
                                                BX.GLG(BY,Check, D20,1)
                                                #RogueX.LikeKitty += D20

                                #RogueX.LikeKitty += (int(KittyX.Shame/5)) #Rogue likes Kitty based on how slutty Kitty looks
                                if BX is EmmaX:
                                        #if it's Emma. . .
                                        #raise Emma's like by 1/4 other girl's shame
                                        BX.GLG(BY,1000,(int(BY.Shame/4)),1)
                                elif BY in (EmmaX,StormX) and BX is not LauraX:
                                        #If it's anyone other than Laura seeing Emma's body. . .
                                        #raise girl's like by 1/4 other girl's shame
                                        BX.GLG(BY,1000, (int(BY.Shame/4)),1)
                                else:
                                        #raise girl's like by 1/5 other girl's shame
                                        BX.GLG(BY,1000, (int(BY.Shame/5)),1)


        if Teach == 2:
                $ StormX.Loc = "bg teacher" #Sets Storm to being a teacher again
        elif Teach:
                $ EmmaX.Loc = "bg teacher" #Sets Emma to being a teacher again
        return
# End GirlWaitUp / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Lesbian Jumping check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label LesCheck(Girls=[],BO=[]): #rkeljsvgb
        #Called by Wait, Checks if any girls will jump each other behind the scenes. . .
        # They will if they have over 500 Inbt and are thirsty

        $ LesQueue = []

        if "three" not in EmmaX.History:
                #this addes threecheck if she's really slutty
                if EmmaX.Thirst >= 30 and ApprovalCheck(EmmaX, 800, "I"):
                        $ EmmaX.History.append("three")

        $ BO = ActiveGirls[:]
        python:
            for BX in BO:
                #loops through and makes choices.
                if BX is RogueX and "touch" not in RogueX.Traits:
                        #skip if Rogue and she doesn't have touch upgrade
                        pass
                elif BX is EmmaX and "three" not in EmmaX.History:
                        #skip if it's Emma and she doesn't do threesomes
                        pass
                elif BX.Thirst < 30:
                        pass
                elif ApprovalCheck(BX, 500, "I",Alt=[[EmmaX,JeanX,GwenX,WandaX],300]): #and "refused" not in R_DailyActions?
                        if ("mono" not in BX.Traits or BX.Break[0]) and BX not in Party:
                            Girls.append(BX)
                            if BX.Thirst >= 60:
                                    Girls.append(BX)
                        if BX.Thirst >= 90:
                                    Girls.append(BX)
                elif Day > 20 and BX.SEXP <= 50: #If you basically ignore a girl
                        if ("mono" not in BX.Traits or BX.Break[0]) and BX not in Party:
                            Girls.append(BX)
        if len(Girls) < 2: #if not enough girls are in, leave
                return

        if Girls[0] is not JeanX: #keeps Jean as lead if she's in the mix
                $ renpy.random.shuffle(Girls)

        $ Partner = 0
        while len(Girls) >= 2:
                # So long as the list has two people in it, check to see if the second girl is viable
                # if not, remove her and try again
                if Partner:
                        # if a partner's been picked, cull out the 3+ girls
                        $ Girls.remove(Girls[1]) #$ Girls.remove(Girls[2])
                elif Girls[1] == Girls[0] or Girls[1].Loc == bg_current or Girls[1] in Party:
                        # if the second girl in the list is the same as the first, remove her
                        # if the second girl is at your location, remove her too
                        $ Girls.remove(Girls[1])
                elif Girls[0] in (JeanX,WandaX) and Girls[1].GirlLikeCheck(Girls[0]) >= 500:
                        # Jean tends to get her way, and Wanda just has riz. . .
                        $ Partner = Girls[1]
                elif (Girls[1] in Player.Harem and Girls[0] in Player.Harem) and Girls[0].GirlLikeCheck(Girls[1]) >= 600:
                        $ Partner = Girls[1]
                elif Girls[1].GirlLikeCheck(Girls[0]) >= 800 and Girls[0].GirlLikeCheck(Girls[1]) >= 800:
                        $ Partner = Girls[1]
                elif Girls[1].Thirst >= 90 and Girls[0].GirlLikeCheck(Girls[1]) >= 600:
                        $ Partner = Girls[1]
                else:
                        #if not picked, remove this girl from the list
                        $ Girls.remove(Girls[1])

        if not Partner:
                # if nobody is picked, then return, otherwise you should have at least two girls picked
                return

        $ Girls.append(Partner)
        $ Partner = 0
        #move both girls into the same room

        if bg_current != Girls[0].Home:
                #if you aren't in first girl's room, move both there.
                $ Girls[0].Loc = Girls[0].Home
                $ Girls[1].Loc = Girls[0].Home
        elif bg_current != Girls[1].Home:
                #if you are in the first girl's room, move both to the seconds'.
                $ Girls[0].Loc = Girls[1].Home
                $ Girls[1].Loc = Girls[1].Home

        $ Girls[0].AddWord(1,"les",0,0,0) #adds "les" to recent actions for both girls
        $ Girls[1].AddWord(1,"les",0,0,0) #adds "les" to recent actions for both girls

        $ Girls[0].GLG(Girls[1],700,15,1)         #Like +15 if under 700
        $ Girls[1].GLG(Girls[0],700,15,1)         #Like +15 if under 700

        $ Girls[0].GLG(Girls[1],900,10,1)         #Like +10 if under 900
        $ Girls[1].GLG(Girls[0],900,10,1)         #Like +10 if under 900

        $ Girls[0].GLG(Girls[1],1000,5,1)         #Like +5 if under 1000
        $ Girls[1].GLG(Girls[0],1000,5,1)         #Like +5 if under 1000

        $ Girls[0].DrainWord("arriving",1,0) #removes "arriving" from recent
        $ Girls[1].DrainWord("arriving",1,0) #removes "arriving" from recent

        $ Girls[0].Statup("Lust", 60, 20)
        $ Girls[1].Statup("Lust", 60, 20)

        $ Girls[0].Thirst -= 5
        $ Girls[1].Thirst -= 5

        if ApprovalCheck(Girls[0], 1600, TabM=0) and ApprovalCheck(Girls[1], 1600, TabM=0):
                #if both are into it, queue up a call later
                $ LesQueue = [Girls[0],Girls[1]]
        return
# end Les_Check, checking to see if the girls jump each other / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Harem stat boost  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label HaremStatup(Girl=0,Check=1000,Value=0,Greater=0,BOA=[],BOB=[]): #rkeljsvgb
        # This cycles through every Harem member and applies a like-up to each one.
        # if Girl == "All", it cycles all of them.
        # call HaremStatup(LauraX,700,-5)
        if "Historia" in Player.Traits:
                return
        if Girl == "All" or Girl == 0:
                $ BOA = Player.Harem[:]
        elif Girl in TotalGirls:
                $ BOA = [Girl]
        else:
                return
        python:
            for BX in BOA:
                #loops entire harem is "all," else just loops the one girl through.
                BOB = Player.Harem[:]
                if BX in BOB:
                    # remove the girl being checked from the potential matches
                    BOB.remove(BX)
                for BY in BOB:
                    # If Girl likes the Harem Member below the Check value, apply Value to it.
                    BX.GLG(BY,Check,Value,1)
        return
#End Harem stat boost  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# End Lesbian stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Jumping check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label JumperCheck(BO=[]): #rkeljsvgbdw
        #decides whether a girl wants to jump you unexpectedly
        #Called during Wait, fills queue of potential girls, triggers Jumper later.
        $ JumpQueue = []
        $ BO = ActiveGirls[:]
        python:
            for BX in BO:
                if "switchcheck" in BX.Traits:
                        pass
                elif BX.Action and BX.Thirst >= 30 and ApprovalCheck(BX, 500, "I") and "refused" not in BX.DailyActions and "met" in BX.History:
                        if "chill" not in BX.Traits and BX.Tag not in Player.DailyActions and "jumped" not in BX.DailyActions and BX.Loc != "bg teacher":
                            # I rule out if she is teaching, she won't jump you. . .
                            if renpy.random.randint(0,3) > 1:
                                    JumpQueue.append(BX)
                            if BX.Thirst >= 60:
                                    JumpQueue.append(BX)
                        if BX.Thirst >= 90:
                                    JumpQueue.append(BX)
        return
#End Jumper_Check, checking to see if a girl wants to jump you


label Jumped(Act=0): #rkeljsvgbdw
        # called by EventCalls if someone is in JumpQueue
        # JumpQueue[0] is the girl
        # make sure that this puts people in the right rooms after they do stuff. . .

        if Time_Count == 0 and Round > 80 and bg_current in PersonalRooms:
                #it's too early for this shit
                return

        if not JumpQueue or Party:
                return

        $ D20 = renpy.random.randint(1, 20)
        if D20-(Round/10) < 5: #(20-10 to 1-10 at start of turn, 20-1 to 1-1 toward end)
                return

        $ renpy.random.shuffle(JumpQueue)
        $ Partner = 0

        if JumpQueue[0] is EmmaX and "three" not in EmmaX.History:
                #if lead is Emma, there is a partner, but she doesn't share. . .
                $ JumpQueue = [EmmaX]
        elif EmmaX in JumpQueue and ((Taboo and "taboo" not in EmmaX.History) or "three" not in EmmaX.History):
                #if partner is Emma and she doesn't share. . .
                while EmmaX in JumpQueue:
                        $ JumpQueue.remove(EmmaX)

        if not JumpQueue:
                return

        call Shift_Focus(JumpQueue[0])
        if JumpQueue[0].Loc != bg_current and "locked" in Player.Traits:
                #if the girl is not in the room with you, and your door is locked. . .
                call Locked_Door(Ch_Focus)
                if not JumpQueue or JumpQueue[0].Loc != bg_current:
                        #if you refused her entry. . .
                        while Ch_Focus in JumpQueue:
                                #removes all copies of first girl
                                $ JumpQueue.remove(Ch_Focus)
                        $ Player.RecentActions.append("nope")
                        return
        if not JumpQueue:
                return

        call Shift_Focus(JumpQueue[0])

        #if there are two+ girls, it adds the second as a potential partner
        python:
            for BX in JumpQueue:
                if BX == JumpQueue[0]:
                        #if this girl is a dupe, drop her
                        pass #$ JumpQueue.remove(JumpQueue[1])
                elif BX.Loc != bg_current and BX not in Nearby:
                        #if this girl is not nearby, drop her
                        pass #$ JumpQueue.remove(JumpQueue[1])
                elif JumpQueue[0] in Player.Harem and BX in Player.Harem:
                        #if both are in the harem, they will join in.
                        Partner = BX
                        break
                elif JumpQueue[0].GirlLikeCheck(BX) >= 800 and BX.GirlLikeCheck(JumpQueue[0]) >= 800:
                        #if the girls really like each other, one will follow.
                        Partner = BX
                        break
                #else:
                        #otherwise, cut the girl
        while Ch_Focus in JumpQueue:
                #removes all copies of first girl
                $ JumpQueue.remove(Ch_Focus)
        while Partner in JumpQueue:
                #removes all copies of second girl
                $ JumpQueue.remove(Partner)

        #sets their location
        $ Ch_Focus.Loc = bg_current
        if Partner:
                $ Partner.Loc = bg_current
        $ Present = []
        $ Nearby = []

        call Taboo_Level #makes sure Taboo level is accurate

        if Taboo and (not ApprovalCheck(Ch_Focus, 1500, TabM=3) or (Ch_Focus is EmmaX and "taboo" not in EmmaX.History)):
                #causes you to leave if the girl is not ready for public stuff
                $ Act = "leave"

        if bg_current in PersonalRooms:
                #Causes the girl to pull you out if she doesn't live in the room you're in
                if bg_current == "bg player":
                                pass
                elif Ch_Focus.Home != bg_current and not (Partner and Partner.Home == bg_current):
                                #if it's not the first girl's room, and also not the second's
                                $ Act = "leave"

        if Room_Full(): #if the room is full. . .
                $ Act = "leave"

        call Shift_Focus(Ch_Focus) #this is not working, sometimes?
        call Set_The_Scene

        $ Player.RecentActions.append("jumped")
        $ Ch_Focus.FaceChange("sly",1)
        if Act == "leave":
                #if she's not supercool with public stuff. . .
                if bg_current == "bg player":
                        "Вдруг [Ch_Focus.Name] хватает вас за руку и с озорной улыбкой ведет обратно в свою комнату."
                else:
                        "Вдруг [Ch_Focus.Name] хватает вас за руку и с озорной улыбкой ведет обратно в вашу комнату."
                menu:
                    "Идти вместе с ней":
                        $ Ch_Focus.Statup("Inbt", 95, 3)
                        "Вы следуете за ней."
                    "Отказаться.":
                        $ Ch_Focus.Statup("Love", 90, -10)
                        $ Ch_Focus.Statup("Obed", 50, 10)
                        $ Ch_Focus.Statup("Obed", 95, 5)
                        $ Ch_Focus.Statup("Inbt", 95, -5)
                        $ Ch_Focus.FaceChange("sad",1)
                        "Вы просите ее остановиться."
                        $ Player.RecentActions.append("nope")
                        $ Ch_Focus.AddWord(1,"refused","refused")
                        if not ApprovalCheck(Ch_Focus, 500, "O"):
                                $ Ch_Focus.AddWord(1,"angry","angry")
                        $ Partner = 0
                        return

                if bg_current == "bg player":
                            $ bg_current = Ch_Focus.Home
                else:
                            $ bg_current = "bg player"
                call CleartheRoom(Ch_Focus,1,1)
                if Partner:
                            "[Partner.Name] также следует за вами."

                #call Taboo_Level #makes sure Taboo level is accurate, moved lower in chain
        else:
            if Partner in TotalGirls:
                    $ Partner.FaceChange("sly",1)
                    "Вдруг [Ch_Focus.Name] отводит вас в сторону, [Partner.Name] следует за вами."
            else:
                    "Вдруг [Ch_Focus.Name] отводит вас в сторону."
            menu:
                    "Посмотреть, к чему это приведет":
                        $ Ch_Focus.Statup("Inbt", 95, 2)
                    "Не здесь [[отправиться в вашу комнату]" if bg_current != "bg player":
                        $ Ch_Focus.Statup("Inbt", 95, 1)
                        "Сначала вы отправляетесь в свою комнату."
                        $ bg_current = "bg player"
                        call CleartheRoom(Ch_Focus,1,1)
                    "Отказаться.":
                        $ Ch_Focus.Statup("Love", 90, -10)
                        $ Ch_Focus.Statup("Obed", 50, 10)
                        $ Ch_Focus.Statup("Obed", 95, 5)
                        $ Ch_Focus.Statup("Inbt", 95, -5)
                        $ Ch_Focus.FaceChange("sad",1)
                        "Вы просите ее остановиться."
                        $ Player.RecentActions.append("nope")
                        $ Ch_Focus.AddWord(1,"refused","refused")
                        if not ApprovalCheck(Ch_Focus, 500, "O"):
                                $ Ch_Focus.AddWord(1,"angry","angry")
                        $ Partner = 0
                        return

        $ Ch_Focus.Loc = bg_current
        if Partner:
                $ Partner.Loc = bg_current

        call Taboo_Level #makes sure Taboo level is accurate
        call Set_The_Scene(Dress=0)

        $ Ch_Focus.AddWord(1,"jumped","jumped",0,"jumped") #adds jumped to recent, daily, and history

        if Ch_Focus is RogueX:
                ch_r "В последнее время ты меня избегаешь."
                ch_r "Я подумала, что пора что-то с этим делать."
        elif Ch_Focus is KittyX:
                ch_k "Почему ты не заходишь ко мне?"
                ch_k "Разве тебе не нравится проводить время с \"Китти\"?"
        elif Ch_Focus is EmmaX:
                ch_e "В последнее время ты не приходишь ко мне в гости."
                ch_e "Как я могу это исправить?"
        elif Ch_Focus is LauraX:
                ch_l "Я дико возбуждена, давай трахаться."
        elif Ch_Focus is JeanX:
                ch_j "Слушай, я очень возбуждена, давай трахаться."
        elif Ch_Focus is StormX:
                ch_s "Ты не справляешься со своими обязанностями. . ."
        elif Ch_Focus is JubesX:
                ch_v "Я бы не отказалась от внимания. . ."
        elif Ch_Focus is GwenX:
                ch_g "Слушай, в последнее время ты слишком много времени проводишь с другими девушками. . ."
        elif Ch_Focus is BetsyX:
                ch_b "В последнее время я чувствую, что ты мной пренебрегаешь. . ."
        elif Ch_Focus is DoreenX:
                ch_d "Мне -очень- нужно немного внимания. . ."
        elif Ch_Focus is WandaX:
                ch_w "Мне сейчас очень тяжело. . ."
        else:
                $ Partner = 0
                return
        call Favorite_Actions(Ch_Focus,1) #returns a string of the action
        $ Act = _return
        $ Situation = Ch_Focus
        if not Player.Male and "girltalk" not in Ch_Focus.History:
                $ Ch_Focus.DrainWord("nogirls",0,0,0,1) #history
                $ Ch_Focus.AddWord(1,0,0,0,"girltalk") #history

        if not Player.Male and Act in ("anal","sex","blow","tit","hand","hotdog"):
                # if cock needs to be out but you don't have one. . .
                "[Ch_Focus.Name] наклоняется и прикрепляет вам резиновый член. . ."
        elif not Player.Male and Act in ("cun","finger"):
                # if pussy needs to be out. . .
                "[Ch_Focus.Name] наклоняется и расстегивает вашу ширинку. . ."
                if not Player.Semen:
                    "Вы жалеете, что так устали. . . вы останавливаете ее руки."
                    ch_p "Мне бы сейчас не помешало отдохнуть. . "
                    $ Act = "fondle breasts"
                else:
                    call Seen_First_Peen(Ch_Focus,Partner,1)
        elif Act in ("anal","sex","blow","tit","hand","hotdog"):
                # if cock needs to be out. . .
                "[Ch_Focus.Name] наклоняется и расстегивает вашу ширинку. . ."
                if not Player.Semen:
                    "Вам бы хотелось, чтобы вы не были так истощены. . . вы останавливаете ее руки."
                    ch_p "Мне бы сейчас не помешало отдохнуть. . ."
                    $ Act = "fondle breasts"
                else:
                    call Seen_First_Peen(Ch_Focus,Partner,1)

        if Partner:
                call Girls_Noticed(Ch_Focus,1) #calls the "noticed check" for this girl.

        # launches the appropriate scene based on the sex act in question.
        call Sex_Directory(Ch_Focus,Act)
        if Situation:
                #called if "exiting out to sex menu"
                $ Situation = 0
                call SexMenu #call expression Girl.Tag + "_SexMenu" #call Gwen_SexMenu
        elif "sexit" not in Player.RecentActions:
                call Trig_Reset
                call Sex_Over

        if "nope" in Player.RecentActions:
                #if you refused sex. . .
#                call Remove_Girl(Ch_Focus)
#                if Partner:
#                        call Remove_Girl(Partner)
                jump Misplaced
#        elif JumpQueue:
#                #if you had some sort of sexual encounter, it will hop you to the appropriate sex menu
#                if Ch_Focus.Loc == bg_current:
#                        call expression Ch_Focus.Tag + "_SexMenu" #call Rogue_SexMenu

        $ Partner = 0
#        if bg_current == "bg player":
#                #if it jumped to your room. . .
        jump Misplaced
        return


#End Jumped, when a girl does try to jump you/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start quick sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Quick_Sex(Girl=Ch_Focus,Act=0): #rkeljsvgbdw
        # called by Chitchat if a girl is horny
        call Shift_Focus(Girl)
        $ Girl.FaceChange("sly",1)
        $ Girl.AddWord(1,"quicksex","quicksex")
        menu:
            extend ""
            "Конечно":
                    $ Girl.Statup("Love", 95, 4)
                    $ Girl.Statup("Obed", 50, 1)
                    $ Girl.Statup("Inbt", 70, 2)
                    $ Girl.Statup("Inbt", 90, 3)
            "Нет, спасибо":
                    $ Line = 0
                    $ Girl.Statup("Love", 80, -2)
                    if (2*Girl.Obed) >= (Girl.Love + Girl.Inbt + (5*Girl.Thirst)):
                            #she's more obedient than horny
                            $ Girl.FaceChange("sadside",1)
                            $ Girl.Statup("Obed", 90, 7)
                            if Girl is RogueX:
                                    ch_r "Ну ладно. . ."
                            elif Girl is KittyX:
                                    ch_k "Ладно, как хочешь. . ."
                            elif Girl is EmmaX:
                                    ch_e "Ладно, я поняла. . ."
                            elif Girl is LauraX:
                                    ch_l "Ладно. . ."
                            elif Girl is JeanX:
                                    ch_j ". . . Ладно. . ."
                            elif Girl is StormX:
                                    ch_s "Хорошо. . ."
                            elif Girl is JubesX:
                                    ch_v "Как скажешь. . ."
                            elif Girl is GwenX:
                                    ch_g "Ох. . . я понимаю. . ."
                            elif Girl is BetsyX:
                                    ch_b "Жаль. . ."
                            elif Girl is DoreenX:
                                    ch_d "Оу. . ."
                            elif Girl is WandaX:
                                    ch_w "Отстой."
                            menu:
                                "Подожди, я тут хорошенько подумала и. . ." if not Player.Male:
                                        $ Girl.Statup("Love", 80, -2)
                                        $ Girl.Statup("Obed", 80, -8)
                                        $ Line = "ask"
                                "Подожди, я тут хорошенько подумал и. . ." if Player.Male:
                                        $ Girl.Statup("Love", 80, -2)
                                        $ Girl.Statup("Obed", 80, -8)
                                        $ Line = "ask"
                                ". . . [[молчать, ничего не изменилось].":
                                        pass
                    elif (ApprovalCheck(Girl, 600, "I") and Girl.Thirst >= 30) or Girl.Thirst >= 50:
                                        #she's pretty horny
                                        $ Girl.FaceChange("confused",1,Eyes="surprised")
                                        $ Girl.Statup("Love", 80, -1)
                                        $ Girl.Statup("Obed", 70, 4)
                                        $ Girl.Statup("Inbt", 60, 5)
                                        $ Girl.Statup("Inbt", 90, 3)
                                        if Girl is RogueX:
                                                if not Player.Male:
                                                    ch_r "Ты в этом уверена?"
                                                else:
                                                    ch_r "Ты в этом уверен?"
                                        elif Girl is KittyX:
                                                ch_k "Ты серьезно?"
                                        elif Girl is EmmaX:
                                                if not Player.Male:
                                                    ch_e "Ты хорошо подумала?"
                                                else:
                                                    ch_e "Ты хорошо подумал?"
                                        elif Girl is LauraX:
                                                ch_l "Ты серьезно? Тебе предлагают легкий секс."
                                        elif Girl is JeanX:
                                                ch_j "Ты серьезно? . ."
                                        elif Girl is StormX:
                                                if not Player.Male:
                                                    ch_s "Ты абсолютно уверена? . ."
                                                else:
                                                    ch_s "Ты абсолютно уверен? . ."
                                        elif Girl is JubesX:
                                                ch_v "Я могу сделать так, чтобы это стоило твоего времени. . ."
                                        elif Girl is GwenX:
                                                ch_g "Даже немного не хочешь? . ."
                                        elif Girl is BetsyX:
                                                if not Player.Male:
                                                    ch_b "Уверена, я бы смогла сделать приятно нам обеим. . ."
                                                else:
                                                    ch_b "Уверена, я бы смогла сделать приятно нам обоим. . ."
                                        elif Girl is DoreenX:
                                                ch_d "Я могла бы сделать тебе приятно. . ."
                                        elif Girl is WandaX:
                                                ch_w "Я позволю тебе вести, если захочешь. . ."
                                        $ Line = "ask"
                    #above stack falls through to here.
                    if Line == "ask":
                            $ Line = 0
                            $ Count = 2
                            $ Cnt = 0
                            while Count > 0:
                                    #loops at least twice, more if she starts begging
                                    $ Count -= 1
                                    menu:
                                        extend ""
                                        "Ну ладно.":
                                                $ Act = 1
                                                $ Count = 0
                                                $ Line = 0
                                                $ Girl.FaceChange("sly",1)
                                                $ Girl.Statup("Love", 80, 2)
                                                $ Girl.Statup("Love", 95, 3)
                                                $ Girl.Statup("Obed", 70, 2)
                                                $ Girl.Statup("Inbt", 90, 3)

                                        "Умоляй меня." if Cnt < 100:
                                                $ Girl.Statup("Obed", 80, 2)
                                                $ Line = "beg"
                                        "Снова умоляй меня." if Cnt >= 100:
                                                $ Girl.Statup("Obed", 90, 2)
                                                $ Line = "beg"

                                        "Только если выбор за мной.":
                                                $ Girl.FaceChange("smile",1,Brows="confused")
                                                $ Girl.Statup("Love", 90, 2)
                                                $ Girl.Statup("Obed", 80, 3)
                                                $ Girl.Statup("Obed", 95, 3)
                                                $ Girl.Statup("Inbt", 85, 2)
                                                if Girl is RogueX:
                                                        ch_r "Ну ладно."
                                                elif Girl is KittyX:
                                                        ch_k "Ага, как скажешь."
                                                elif Girl is EmmaX:
                                                        ch_e "Наверное, я согласна."
                                                elif Girl is LauraX:
                                                        ch_l "Справедливо."
                                                elif Girl is JeanX:
                                                        ch_j "Ладно, как скажешь. . ."
                                                elif Girl is StormX:
                                                        ch_s "Это можно устроить. . ."
                                                elif Girl is JubesX:
                                                        ch_v "Хмммм, ладно. . ."
                                                elif Girl is GwenX:
                                                        ch_g "Конечно, почему нет?"
                                                elif Girl is BetsyX:
                                                        ch_b "Это не проблема. . ."
                                                elif Girl is DoreenX:
                                                        ch_d "Конечно, почему нет?"
                                                elif Girl is WandaX:
                                                        ch_w "Конечно, конечно."
                                                $ Line = 0
                                                call SexMenu #call expression Girl.Tag + "_SexMenu"
                                                return

                                        "И все равно мой ответ \"нет\".":
                                                $ Girl.Statup("Love", 85, -2)
                                                $ Girl.Statup("Obed", 90, 3)
                                                if ApprovalCheck(Girl, 1500+(5*Cnt)-(10*Girl.Thirst), "LI"):
                                                            #if she's obedient, or her horniness is higher than her Inhibition
                                                            $ Line = "beg"
                                                elif not Cnt and Count:
                                                            #if you've never refused before
                                                            $ Girl.Uptop = 1 #Uptop up
                                                            pause 1
                                                            call Girl_First_Topless(Girl,1)
                                                            $ Girl.Uptop = 0 #Uptop up
                                                            $ Girl.FaceChange("confused",1,Mouth="smile")
                                                            $ Girl.Statup("Inbt", 70, 3)
                                                            $ Girl.Statup("Inbt", 95, 3)
                                                            if Girl is RogueX:
                                                                    if not Player.Male:
                                                                        ch_r "Ты -абсолютно- в этом уверена?"
                                                                    else:
                                                                        ch_r "Ты -абсолютно- в этом уверен?"
                                                            elif Girl is KittyX:
                                                                    ch_k "Тоооочно?"
                                                            elif Girl is EmmaX:
                                                                    ch_e "Точно не передумаешь, [Girl.Petname]?"
                                                            elif Girl is LauraX:
                                                                    ch_l "Да ладно!"
                                                            elif Girl is JeanX:
                                                                    ch_j "Я же знаю, ты этого хочешь. . ."
                                                            elif Girl is StormX:
                                                                    if not Player.Male:
                                                                        ch_s "Ты -настолько- уверена?"
                                                                    else:
                                                                        ch_s "Ты -настолько- уверен?"
                                                            elif Girl is JubesX:
                                                                    ch_v "Облом. . ."
                                                            elif Girl is GwenX:
                                                                    ch_g "Ай, меня отвергли. . ."
                                                            elif Girl is BetsyX:
                                                                    ch_b "Жаль. . ."
                                                            elif Girl is DoreenX:
                                                                    ch_d "Облом. . ."
                                                            elif Girl is WandaX:
                                                                    ch_w "Супер отстой."
                                                            $ Cnt += 25
                                    if Line == "beg":
                                            if ApprovalCheck(Girl, 600+Cnt, "O") or ApprovalCheck(Girl, 1500+(5*Cnt)-(10*Girl.Thirst)):
                                                    #if she's obedient, or her horniness is higher than her Inhibition
                                                    if Cnt < 50:
                                                            #first time
                                                            $ Girl.FaceChange("sad",2)
                                                            $ Girl.Statup("Love", 90, -2)
                                                            $ Girl.Statup("Obed", 50, 5)
                                                            $ Girl.Statup("Obed", 95, 3)
                                                            $ Girl.Statup("Inbt", 90, 3)
                                                            if Girl is RogueX:
                                                                    ch_r "Ну пожалуйста?"
                                                            elif Girl is KittyX:
                                                                    ch_k "Пожалуйста-пожалуйста?"
                                                            elif Girl is EmmaX:
                                                                    ch_e ". . ."
                                                                    $ Girl.Statup("Love", 90, -2)
                                                                    $ Girl.Statup("Obed", 200, 3)
                                                                    ch_e ". . .Пожалуйста?"
                                                            elif Girl is LauraX:
                                                                    ch_l "Эм. . . Пожалуйста?"
                                                            elif Girl is JeanX:
                                                                    ch_j "Хм. . ."
                                                                    $ Girl.Statup("Obed", 90, 3)
                                                                    ch_j "Ладно. . . Пожалуйста? . ."
                                                            elif Girl is StormX:
                                                                    if not Player.Male:
                                                                        ch_s "Нет? Ты в этом уверена?"
                                                                    else:
                                                                        ch_s "Нет? Ты в этом уверен?"
                                                            elif Girl is JubesX:
                                                                    if not Player.Male:
                                                                        ch_v "Уверена?"
                                                                    else:
                                                                        ch_v "Уверен?"
                                                            elif Girl is GwenX:
                                                                    ch_g "Оу. . . Пожалуйста? . ."
                                                            elif Girl is BetsyX:
                                                                    ch_b "Неужели у меня нет никакого способа убедить тебя?"
                                                            elif Girl is DoreenX:
                                                                    ch_d "Даже если я скажу \"пожалуйста?\""
                                                            elif Girl is WandaX:
                                                                    ch_w "Что, если я буду умолять тебя?"
                                                    else:
                                                            #second time
                                                            $ Girl.FaceChange("sad",2,Eyes="surprised")
                                                            $ Girl.Statup("Love", 90, -4)
                                                            $ Girl.Statup("Obed", 70, 6)
                                                            $ Girl.Statup("Obed", 200, 3)
                                                            $ Girl.Statup("Inbt", 90, 5)
                                                            if Girl is RogueX:
                                                                    ch_r "Давай, мне это очень нужно. . ."
                                                            elif Girl is KittyX:
                                                                    ch_k "Я хочу тебя, [Girl.Petname]!"
                                                            elif Girl is EmmaX:
                                                                    $ Girl.Statup("Love", 90, -2)
                                                                    $ Girl.Statup("Obed", 200, 1)
                                                                    ch_e "Я. . . очень хочу тебя, здесь и сейчас, [Girl.Petname]. . ."
                                                            elif Girl is LauraX:
                                                                    $ Girl.Statup("Obed", 80, 1)
                                                                    if not Player.Male:
                                                                        ch_l "У меня лихорадка, а единственное лекарство - это твоя киска. . ."
                                                                    else:
                                                                        ch_l "У меня лихорадка, а единственное лекарство - это твой член. . ."
                                                            elif Girl is JeanX:
                                                                    ch_j "Я. . ."
                                                                    ch_j "Да ладно, блин. . ."
                                                                    $ Girl.Statup("Obed", 90, 5)
                                                                    ch_j "Пожалуйста?"
                                                            elif Girl is StormX:
                                                                    ch_s ". . ."
                                                            elif Girl is JubesX:
                                                                    ch_v "Пожалуйста-пожалуйста?"
                                                            elif Girl is GwenX:
                                                                    ch_g "Пожалуйстапожалуйстапожалуйста? . ."
                                                            elif Girl is BetsyX:
                                                                    ch_b "Я никогда никого не умоляла. . ."
                                                                    ch_b ". . .  однако, сейчас мне очень плохо. . ."
                                                                    ch_b ". . . пожалуйста?"
                                                            elif Girl is DoreenX:
                                                                    ch_d "Давай. . ."
                                                                    if not Player.Male:
                                                                        ch_d "Мне -очень- нужно, чтобы ты вошла в меня."
                                                                    else:
                                                                        ch_d "Мне -очень- нужно, чтобы ты вошел в меня."
                                                            elif Girl is WandaX:
                                                                    if not Player.Male:
                                                                        ch_w "А если я скажу, что-то типа: \"пожалуйста, пожалуйста, пожалуйста, я хочу ее\". . ."
                                                                    else:
                                                                        ch_w "А если я скажу, что-то типа: \"пожалуйста, пожалуйста, пожалуйста, я хочу его\". . ."
                                                                    ch_w "Ты изменишь свое решение?"
                                                    $ Count = 1 if Count <= 0 else Count #allows it to cycle one more time
                                                    $ Cnt += 100
                                            elif Cnt > 50:
                                                            #she refuses on second time
                                                            $ Girl.FaceChange("angry",1)
                                                            $ Girl.Statup("Love", 70, -3)
                                                            $ Girl.Statup("Love", 85, -5)
                                                            $ Girl.Statup("Obed", 80, -2)
                                                            $ Girl.Statup("Inbt", 90, 4)
                                                            if Girl is RogueX:
                                                                    ch_r "Я больше не буду умолять."
                                                            elif Girl is KittyX:
                                                                    ch_k "Больше даже не проси!"
                                                            elif Girl is EmmaX:
                                                                    $ Girl.Statup("Love", 90, -3)
                                                                    $ Girl.Statup("Obed", 70, -3)
                                                                    $ Girl.Statup("Obed", 200, 2)
                                                                    ch_e "Я. . . Даже одного раза уже слишком много!"
                                                            elif Girl is LauraX:
                                                                    ch_l "Ооох, не дави на меня, [Player.Name]."
                                                            elif Girl is JeanX:
                                                                    $ Girl.Statup("Obed", 90, 4)
                                                                    ch_j "Ну как хочешь. . ."
                                                            elif Girl is StormX:
                                                                    ch_s "Да будет так."
                                                            elif Girl is JubesX:
                                                                    ch_v "Бууу."
                                                            elif Girl is GwenX:
                                                                    ch_g "Пфф, ну и ладно. . ."
                                                            elif Girl is BetsyX:
                                                                    ch_b "Не хочешь как хочешь. . ."
                                                            elif Girl is DoreenX:
                                                                    ch_d "Не заставляй меня умолять. . ."
                                                            elif Girl is WandaX:
                                                                    ch_w "Этого было мало?"
                                            else:
                                                            #she refuses
                                                            $ Girl.FaceChange("sad",2,Brows="confused")
                                                            $ Girl.Statup("Love", 95, -2)
                                                            $ Girl.Statup("Obed", 50, -2)
                                                            $ Girl.Statup("Obed", 90, -2)
                                                            $ Girl.Statup("Inbt", 90, 5)
                                                            if Girl is RogueX:
                                                                    ch_r "Я не собираюсь умолять."
                                                            elif Girl is KittyX:
                                                                    ch_k "Это. . . оскорбительно."
                                                            elif Girl is EmmaX:
                                                                    $ Girl.Statup("Obed", 70, -2)
                                                                    ch_e "Это ниже моего достоинства."
                                                            elif Girl is LauraX:
                                                                    ch_l "Не дождешься. . ."
                                                            elif Girl is JeanX:
                                                                    $ Girl.Statup("Obed", 90, 4)
                                                                    ch_j "Ага, не дождешься. . ."
                                                            elif Girl is StormX:
                                                                    ch_s "Так тому и быть."
                                                            elif Girl is JubesX:
                                                                    ch_v "Буууу."
                                                            elif Girl is GwenX:
                                                                    ch_g "Пфф, ну и ладно. . ."
                                                            elif Girl is BetsyX:
                                                                    ch_b "Не хочешь как хочешь. . ."
                                                            elif Girl is DoreenX:
                                                                    ch_d "Ну и. . . ладно. . ."
                                                            elif Girl is WandaX:
                                                                    ch_w "Ну и хорошо. . ."
                                    #end of "beg" chain
                            #end of loop, if not Act, return disappointed
                    $ Line = 0
                    if not Act:
                            #she accepts your refusal
                            $ Girl.Statup("Love", 80, -2)
                            if Girl is RogueX:
                                    ch_r "Ладно, тебе же хуже. . ."
                            elif Girl is KittyX:
                                    ch_k "Тебе же хуже . ."
                            elif Girl is EmmaX:
                                    ch_e "Хорошо. . . Я и без тебя справлюсь. . ."
                            elif Girl is LauraX:
                                    ch_l "Тебе же хуже. . ."
                            elif Girl is JeanX:
                                    ch_j "Тебе же хуже. . ."
                            elif Girl is StormX:
                                    ch_s "Хорошо, тебе же хуже. . ."
                            elif Girl is JubesX:
                                    ch_v "Отстой."
                            elif Girl is GwenX:
                                    ch_g "Разве не в этом весь смысл?!"
                            elif Girl is BetsyX:
                                    ch_b "Я постараюсь найти себе какое-нибудь другое занятие. . ."
                            elif Girl is DoreenX:
                                    ch_d "Я справлюсь. . ."
                            elif Girl is WandaX:
                                    ch_w "Ладно, как хочешь."
                            return

        $ Line = 0
        call Favorite_Actions(Girl,1) #returns a string of the action
        $ Act = _return

        if not Player.Male and Act in ("anal","sex","blow","tit","hand","hotdog"):
                # if cock needs to be out but you don't have one. . .
                "[Girl.Name] наклоняется и пристегивает вам резиновый член. . ."
        elif not Player.Male and Act in ("cun","finger"):
                # if pussy needs to be out. . .
                "[Girl.Name] наклоняется и расстегивает вашу ширинку. . ."
                if not Player.Semen:
                    "Вы жалеете, что так устали. . . вы останавливаете ее руки."
                    ch_p "Мне бы сейчас не помешало отдохнуть. . "
                    $ Act = "fondle breasts"
                else:
                    call Seen_First_Peen(Girl,Partner,1)
        elif Act in ("anal","sex","blow","tit","hand","hotdog"):
                # if cock needs to be out. . .
                "[Girl.Name] наклоняется и расстегивает вашу ширинку. . ."
                if not Player.Semen:
                    "Вам бы хотелось, чтобы вы не были так истощены. . . вы останавливаете ее руки."
                    ch_p "Мне бы сейчас не помешало отдохнуть. . "
                    $ Act = "fondle breasts"
                else:
                    call Seen_First_Peen(Girl,Partner,1)

        $ Situation = Girl

        # launches the appropriate scene based on the sex act in question.
        call Sex_Directory(Girl,Act)
        if Situation:
                #called if "exiting out to sex menu"
                $ Situation = 0
                call SexMenu #call expression Girl.Tag + "_SexMenu" #call Gwen_SexMenu
        return

label Sex_Directory(Girl=0,Act=0):
        #called by Jumped and Quick_Sex, via call Sex_Directory(Girl,Act)
        if not Act:
                return
        # launches the appropriate scene based on the sex act in question.
        if Partner:
                call Threeway_Set(Partner,Girl,"watch")
        if Act == "anal":
                call Girl_AnalPrep # call expression Girl.Tag + "_AnalPrep" #call R_AnalPrep
        elif Act == "sex":
                call Girl_SexPrep #call expression Girl.Tag + "_SexPrep" #call R_SexPrep
        elif Act ==  "lick pussy":
                call Girl_LP_Prep #call expression Girl.Tag + "_LP_Prep" #call R_LPlayer.Prep
        elif Act == "fondle pussy":
                call Girl_FP_Prep #call expression Girl.Tag + "_FP_Prep" #call R_FPlayer.Prep
        elif Act == "blow":
                call Girl_BJ_Prep #call expression Girl.Tag + "_BJ_Prep" #call R_BJ_Prep
        elif Act == "cun":
                call Girl_CUN_Prep
        elif Act == "tit":
                call Girl_TJ_Prep #call expression Girl.Tag + "_TJ_Prep" #call R_TJ_Prep
        elif Act == "foot":
                call Girl_FJ_Prep #call expression Girl.Tag + "_FJ_Prep" #call R_FJ_Prep
        elif Act == "hand":
                call Girl_HJ_Prep #call expression Girl.Tag + "_HJ_Prep" #call R_HJ_Prep
        elif Act == "finger":
                call Girl_Finger_Prep
        elif Act == "hotdog":
                call Girl_HotdogPrep #call expression Girl.Tag + "_HotdogPrep" #call R_HotdogPrep
        elif Act == "suck breasts":
                call Girl_SB_Prep #call expression Girl.Tag + "_SB_Prep" #call R_SB_Prep
        elif Act == "fondle breasts":
                call Girl_FB_Prep #call expression Girl.Tag + "_FB_Prep" #call R_FB_Prep
        elif Act == "insert ass" or Act == "lick ass":
                call Girl_IA_Prep #call expression Girl.Tag + "_IA_Prep" #call R_IA_Prep
        else: #Act == "kiss you"
                call KissPrep #call R_KissPrep
#        if Situation:
#                #called if "exiting out to sex menu"
#                $ Situation = 0
#                call SexMenu #call expression Girl.Tag + "_SexMenu" #call Gwen_SexMenu
#        jump Misplaced
        return
#end quick sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start sex act escalation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Escalation(Girl=0): #rkeljsvgb
        #call Escalation("Rogue","R")
        # raises the level of the sexual activity if the girl would like that.
        if Cnt < 5 or ThreeCount <= Round or Girl.Forced:
                #if things just started, or you recently made a change, return
                return

        $ Situation = Girl

        if Trigger == "fondle breast" and ApprovalCheck(Girl,1050,TabM=4,Alt=[[JeanX],800]) and Girl.Lust >= 30 and Girl.SuckB:
                    #if you're fondling her breasts, she has over 30 Lust, and she's had her breasts sucked before. . .
                    if Trigger2 == "suck breasts":
                            $ Trigger2 = 0
                    $ Girl.Statup("Inbt", 80, 2)
                    call Girl_SB_Prep #call expression Girl.Tag + "_SB_Prep" #call Rogue_SB_Prep
                    if "suck breasts" in Girl.RecentActions:
                            # If you went through with it, drop one phase back when returning to this point
                            $ renpy.pop_call()
        elif Trigger == "fondle thighs" and ApprovalCheck(Girl,1050,TabM=4,Alt=[[JeanX],800]) and Girl.Lust >= 30 and Girl.FondleP:
                    #if you're fondling her thighs, she has over 30 Lust, and she's had her pussy fondled before. . .
                    if Trigger2 == "fondle thighs":
                            $ Trigger2 = 0
                    $ Girl.Statup("Inbt", 80, 4)
                    call Girl_FP_Prep #call expression Girl.Tag + "_FP_Prep" #call Rogue_FPlayer.Prep
                    if "fondle pussy" in Girl.RecentActions:
                            # If you went through with it, drop one phase back when returning to this point
                            $ renpy.pop_call()
        elif not Player.Semen:
                    #can't do the rest if you're tapped out
                    pass
        elif Trigger == "hand" and ApprovalCheck(Girl,1200,TabM=4) and Girl.Lust >= 30 and Girl.Blow:
                    #if she's giving a handy, she has over 30 Lust, and she's sucked cock before. . .
                    $ Girl.Statup("Inbt", 80, 3)
                    call Girl_BJ_Prep #call expression Girl.Tag + "_BJ_Prep" #call Rogue_BJ_Prep
                    if "blow" in Girl.RecentActions:
                            # If you went through with it, drop one phase back when returning to this point
                            $ renpy.pop_call()
        elif Trigger == "finger" and ApprovalCheck(Girl,1200,TabM=4) and Girl.Lust >= 30 and Girl.CUN:
                    #if she's giving a fingering, she has over 30 Lust, and she's sucked pussy before. . .
                    $ Girl.Statup("Inbt", 80, 3)
                    call Girl_CUN_Prep
                    if "cun" in Girl.RecentActions:
                            # If you went through with it, drop one phase back when returning to this point
                            $ renpy.pop_call()

        elif Trigger == "blow" and Girl.Lust >= 10:
                    call expression Girl.Tag + "_69_Intro"
        elif Trigger == "cun" and Girl.Lust >= 10:
                    call expression Girl.Tag + "_69_Intro"
        elif Trigger == "lick pussy" and Girl.Lust >= 30:
                    call expression Girl.Tag + "_69_Intro"

        elif Trigger not in ("sex","anal") and ApprovalCheck(Girl,1400,TabM=5,Alt=[[JeanX],1200]) and Girl.Lust >= 60 and Girl.Sex >= 3:
                    #if you're not having sex, she has over 60 Lust, and she's had sex before. . .
                    $ Girl.Statup("Inbt", 80, 4)
                    call Girl_SexPrep #call expression Girl.Tag + "_SexPrep" #call Rogue_SexPrep
                    if "sex" in Girl.RecentActions:# and not Situation:
                            # If you went through with it, drop one phase back when returning to this point
                            $ renpy.pop_call()
        elif Trigger != "anal" and ApprovalCheck(Girl,1400,TabM=5,Alt=[[JeanX],1200]) and Girl.Lust >= 70 and Girl.Anal >= 5:
                    #if you're not having anal, she has over 70 Lust, and she's had anal before. . .
                    $ Girl.Statup("Inbt", 80, 5)
                    call Girl_AnalPrep #call expression Girl.Tag + "_AnalPrep" #call Rogue_AnalPrep
                    if "anal" in Girl.RecentActions:# and not Situation:
                            # If you went through with it, drop one phase back when returning to this point
                            $ renpy.pop_call()

        #if it falls through the options
        $ ThreeCount = 0
        $ Situation = 0
        return
#end Escalation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start General sex stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Primary Sex Dialog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Sex_Dialog(Primary=Ch_Focus,Secondary=0,TempFocus=0,PrimaryLust=0,SecondaryLust=0,Line1=0,Line2=0,Line3=0,Line4=0,D20S=0):  #rkeljsvgb
        # call Sex_Dialog(RogueX,Partner)
        # Primary is main female, secondary is supporting female, action is what they are doing.

        # If the seed is 0-5, only offhands will play. If it's 15-20, only trigger3's will play. If it's 5-10, offhand and Secondaries will play.
        # If it's 10-15 all things will play.

        $ D20S = renpy.random.randint(1, 20) if not D20S else D20S
        $ Line = 0

        # Checks for Taboo, and if it passes through, calls the first sex dialog
#        if Taboo and Primary.Loc == bg_current: #removed this block because it was skipping the locked door check
#            if (D20S + (int(Taboo/10)) - Stealth) >= 10:
#                    #If there is a Taboo level, and your modified roll is over 10
#                    call Girls_Taboo(Primary)
#        else:
        call Girls_Taboo(Primary)
        if not Trigger:
                return

        $ Secondary = Partner

        call Primary_SexDialog
        $ Line1 = Line #Set Line1 to the current state of the Line variable
        #End Primary Dialog

        #Trigger 2
        if Trigger2:
                    # If there is a player offhand Trigger set
                    $ Line = ""
                    call Offhand_Dialog
                    if D20S <= 15: #if the random value is 1-15, add an Offhand dialog
                            $ Line1 = Line1 + Line
        #End Offhand


        #Trigger 3
        if Trigger not in ("masturbation", "lesbian"):
                    # If there is a Primary offhand Trigger set and the random value is 1-10, add a self-directed dialog
                    $ Line = 0
                    if Primary.Offhand:
                            call Girl_Self_Lines(Primary,Primary.Offhand,D20X=D20S)
                            if Line and D20S >= 7:
                                    $ Line3 = Line + "."
                    elif D20S >= 7:
                            call Girl_Self_Lines(Primary,Primary.Offhand,D20X=D20S)
                            $ Line3 = Line + "." if Line else Line3
        #End Primary girl offhand

        #Trigger 4
        if Secondary and (not Secondary.Offhand or 7 <= D20S <= 17 or Secondary.Offhand == "watch"):
                    # If there is a Secondary character and the random value is 5-15, add a threeway dialog
                    $ Line = 0
                    if Secondary.Offhand:
                            #If there is a Secondary action picked, check threeway, and maybe say the line
                            call SexDialog_Threeway(Secondary,Primary)
                            if Line and 7 <= D20S <= 17:
                                    $ Line4 = Line + "."
                    elif 7 <= D20S <= 17:
                            call SexDialog_Threeway(Secondary,Primary)
                            $ Line4 = Line + "." if Line else Line4
        #End Secondary Dialog

        #Applying player's satisfaction
        $ Player.Statup("Focus", 200, TempFocus)

        #Applying primary girl's satisfaction
        $ PrimaryLust += 2 if "vibein" in Primary.DailyActions else 0
        $ Primary.Statup("Lust", 200, PrimaryLust)
        $ Primary.LustFace()

        #Applying secondary girl's satisfaction
        if Secondary:
                $ SecondaryLust += (int(PrimaryLust/10)) if Secondary.GirlLikeCheck(Primary) >= 700 else 0
                $ SecondaryLust += 2 if "vibein" in Secondary.DailyActions else 0
                $ Secondary.Statup("Lust", 200, SecondaryLust)
                $ Secondary.LustFace()

        # Dialog begins to play out. . .
        "[Line1]"
        if Line3:
                #If there's a secondary line, play it
                call Seen_First_Peen(Primary,Secondary,Passive=3)
                "[Line3]"
        if Line4:
                #add call to First Les here."
                #If there's a third person line, play it
                call Seen_First_Peen(Primary,Secondary,Passive=4)
                "[Line4]"
                if Secondary.Offhand == "suck girl breasts" or Secondary.Offhand == "fondle girl breasts":
                    #if breastplay is involved. . .
                    if ApprovalCheck(Primary,500,"I",TabM=2) and Primary.Lust >= 50 and (Primary.ChestNum() > 1 or Primary.OverNum() > 1):
                            # if the girl is horny and her top is on. . .
                            $ Primary.Uptop = 1
                            "[Primary.Name] похоже расстроилась, но все равно она обнажает свою грудь."

        call Activity_Check(Primary,Secondary,0)
        if not _return:
                #sees if girl is cool with what's happening, if not, removes her.
                if Primary.Forced:
                        #if you're coercing her, it just reverts to the previous tier
                        #$ renpy.pop_call() #negates call to Sex Dialog
                        return
                if Secondary and Secondary.Loc == bg_current:
                        #if the first girl leaves, but there is another,
                        $ Trigger = Secondary
                        $ Secondary.Offhand = 0
                        $ Partner = 0
                        #$ renpy.pop_call() #negates call to Sex Dialog
                        #$ renpy.pop_call() #negates call to sexaction in progress
                        #$ renpy.pop_call() #negates call to sex menu
                else:
                        call Trig_Reset
                jump Misplaced   #moved out of previous column

        call Dirty_Talk

        return
# End Primary Sex Dialog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Trig_Reset(Visual=0):
        # Resets all triggers, and sprites if Visual
        $ Trigger = 0
        $ Trigger2 = 0
#        $ Trigger3 = 0
#        $ Trigger4 = 0
#        $ Trigger5 = 0
        $ Situation = 0
        $ Player.Cock = 0
        call Clear_Offhands
        if Visual:
                call AllReset
        return

# Start Trigger swap  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Trigger_Swap(Active = 0, TriggerX1 = Trigger, TriggerX3 = 0, Primary = Partner): #rkeljsvgb
    #this would switch primary character triggers over to secondary characters.
    # call Trigger_Swap("Rogue")
    # TriggerX1 and TriggerX3 store the primary girl's actions
    # Active is the old lead girl
    # Primary is the new lead girl

    $ TriggerX3 = Active.Offhand
    $ Trigger2 = 0 if Trigger2 not in ("jackin","jilling") else Trigger2
    $ Tempmod = 0

    if Partner.Offhand:
            #if the second girl is already doing something
            if Partner.Offhand in ("fondle pussy","fondle breasts","fondle ass","suck breasts","dildo pussy","dildo anal","vibrator pussy"):
                    $ Trigger = "masturbation"
                    #"hand","fondle breasts","suck breasts","fondle pussy","dildo pussy",
                    #"vibrator pussy","fondle ass","dildo anal"
            elif TriggerX1 == "lesbian":
                    $ Trigger = "lesbian"
            elif Partner.Offhand in ("hand","blow","finger","cun","kiss you"):
                    $ Trigger = Partner.Offhand
#                    $ Active.Offhand = 0
                    $ Partner.Offhand = 0
            else:
                    $ Trigger = 0
                    $ Active.Offhand = 0
                    $ Partner.Offhand = 0
                    #"fondle breasts","suck breasts","fondle pussy","lick pussy",
                    #"fondle ass","lick ass",
    else:
                    #if the second girl is not already doing anything
                    $ Trigger = 0
                    $ Active.Offhand = 0

    call Shift_Focus(Primary)
    if not Active:
            #if no girl is sent to this system, cycle active girls and place any locals into the Partner role
            $ BO = ActiveGirls[:]
            $ BO.remove(Primary) if Primary in BO else BO
            python:
                for BX in BO:
                    if BX.Loc == bg_current:
                            Partner = BX
                            break
    else:
                    $ Partner = Active

    #if the primary girl was doing something
    if TriggerX1 == "masturbation" or TriggerX1 == "lesbian":
            pass
    else:
            if TriggerX1 in ("hand","blow","finger","cun","kiss you"):
                $ Partner.Offhand = TriggerX1
            else:
                if TriggerX1 in ("fondle thighs","fondle ass","insert ass","lick ass"):
                        $ Partner.Offhand = "fondle ass"
                        "Вы отстраняетесь от [Partner.Name_rod]."
                elif TriggerX1 in ("dildo pussy","dildo anal"):
                        #call Cock_Occupied(Partner,"pussy") #Maybe?
                        $ Partner.Offhand = TriggerX1
                        "Вы отстраняетесь от [Partner.Name_rod]."
                elif TriggerX1 in ("titjob","hotdog","fondle breasts","suck breasts"):
                        $ Partner.Offhand = "fondle breasts"
                        "Вы отстраняетесь от [Partner.Name_rod]."
                elif TriggerX1 in ("fondle pussy","lick pussy"):
                        $ Partner.Offhand = "fondle pussy"
                        "Вы отстраняетесь от [Partner.Name_rod]."
                elif TriggerX1 == "sex":
                        $ Partner.Offhand = "fondle pussy"
                        "Вы отстраняетесь от [Partner.Name_rod] и переключаете свое внимание на [Primary.Name_vin]."
                elif TriggerX1 == "anal":
                        $ Partner.Offhand = "fondle ass"
                        "Вы отстраняетесь от [Partner.Name] и переключаете свое внимание на [Primary.Name_vin]."
                else:
                        $ Partner.Offhand = 0
    call AllReset(Partner)

    if not Trigger:
#            call Set_The_Scene(Dress = 0, TrigReset = 0, Quiet=1)
#            "What would you like her to do?"

            $ renpy.pop_call() #causes it to skip past the cycle you were in before
            $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
            jump SMenu

#            if Primary == RogueX:
#                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
#                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
#                    jump Rogue_SMenu
#            if Primary == KittyX:
#                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
#                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
#                    jump Kitty_SMenu
#            if Primary == EmmaX:
#                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
#                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
#                    jump Emma_SMenu
#            if Primary == LauraX:
#                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
#                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
#                    jump Laura_SMenu
#            if Primary == JeanX:
#                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
#                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
#                    jump Jean_SMenu
#            if Primary == StormX:
#                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
#                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
#                    jump Storm_SMenu
#            if Primary == JubesX:
#                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
#                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
#                    jump Jubes_SMenu
#            if Primary == GwenX:
#                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
#                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
#                    jump Gwen_SMenu
#            if Primary == BetsyX:
#                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
#                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
#                    jump Betsy_SMenu
#            if Primary == DoreenX:
#                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
#                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
#                    jump Doreen_SMenu
#            if Primary == WandaX:
#                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
#                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
#                    jump Wanda_SMenu
    else:
                    call Set_The_Scene(Dress = 0, TrigReset = 0, Quiet=1)
                    if Primary in TotalGirls:
                        call SexAct("SkipTo") #call expression Primary.Tag + "_SexAct" pass ("SkipTo") #call Kitty_SexAct("SkipTo")
    return
# End Trigger swap  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Activity Checker  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Activity_Check(Girl=0,Girl2=0,Silent=0,Removal=1,ClothesCheck=1,Mod=0,Approval=3,Tempshame=0,TabooM=1): #rkeljsvgb
        # This checks whether a girl is up for watching a given activity
        # Silent is whether it plays dialog or not, Removal is whether it auto-removes the girl on a fail,
        # ClothesCheck is whether it bothers checking clothing, 2 if skip first girl
        # Mod gets set to her Like stat -600, so 600 Like, you break even, otherwise it's a penalty
        # call Activity_Check("Rogue",0,1,0)

        if Girl == Girl2:
            "Tell oni that the activity check failed after [Trigger]."
            $ Girl.NotAStat = 5

        #if they don't know you're there, they don't run
        if "unseen" in Girl.RecentActions or "classcaught" in Girl.RecentActions:
                    return 2

        $ Mod += 200 if Girl.Forced else 0                              #bonus if in the Forced state
        $ Mod += (Girl.Lust*5) if Girl.Lust >= 50 else 0                #bonus if high lust (50 = +250, 75= +375, 90 = +450)

        if Girl2 and ClothesCheck != 2:
                #if there is a second girl and it's not told to skip it
                $ Mod = int(Mod/2) if Mod > 0 else Mod
                #halves the benefits from the above mechanisms
                $ Mod += (Girl.GirlLikeCheck(Girl2)-600)
                # if 500 = -100, if 700 = +100 if 900 = +300
                if Girl in Player.Harem and Girl2 in Player.Harem: #bonus for if both in harem
                        $ Mod += 500

        $ Mod += 200 if "activity" in Girl.RecentActions else 0         #If you've already bargained with her, you get a bonus on further tests

        if ClothesCheck and Girl2:
                #sets her shame level to be accurate to current look
                #call expression Girl2.Tag + "_OutfitShame" pass (20)
                call OutfitShame(Girl2,20)
                $ Tempshame = Girl2.Shame

                if Girl is StormX:
                        #Storm doesn't care
                                $ Approval = 2
                elif Tempshame <= 15 and (ApprovalCheck(Girl, 600,Bonus=Mod) or ApprovalCheck(Girl, 350, "I")):
                        #If the outfit is hot but she's ok
                        if ApprovalCheck(Girl, 900,Bonus=Mod) or ApprovalCheck(Girl, 450, "I"):
                                $ Approval = 2
                elif Tempshame <= 20 and (ApprovalCheck(Girl, 900,Bonus=Mod) or ApprovalCheck(Girl, 450, "I")):
                        #If the outfit is sexy but she's cool with that
                        if ApprovalCheck(Girl, 1100,Bonus=Mod) or ApprovalCheck(Girl, 550, "I"):
                                $ Approval = 2
                elif Tempshame <= 25 and (ApprovalCheck(Girl, 1100,Bonus=Mod) or ApprovalCheck(Girl, 550, "I")):
                        #If the outfit is sexy but she's cool with that
                        if ApprovalCheck(Girl, 1400,Bonus=Mod) or ApprovalCheck(Girl, 650, "I"):
                                $ Approval = 2
                elif (ApprovalCheck(Girl, 1400,Bonus=Mod) or ApprovalCheck(Girl, 650, "I")):
                        #If the outfit is very scandalous but she's ok with that
                        if ApprovalCheck(Girl, 1600,Bonus=Mod) or ApprovalCheck(Girl, 850, "I"):
                                $ Approval = 2
                else:
                                $ Approval = 0
#        else:
#                $ Approval = 3

        if "exhibitionist" in Girl.Traits or ApprovalCheck(Girl,900,"I"):
                    #this negates or reduces the taboo modifier if they are slutty
                    $ TabooM = 0
        elif ApprovalCheck(Girl,50,"X") or ApprovalCheck(Girl,800,"I"):
                    $ TabooM = .5

        if not Approval:
                    # If it fails the clothing check, skip the next part
                    pass
        elif Trigger == "strip" and Trigger2 not in ("jackin","jilling"):
                    pass #covered by the above check
        elif not Trigger and not Trigger2:
                    pass
        elif Trigger == "lick ass":
                    $ Approval = ApprovalCheck(Girl,1550,Bonus=Mod, TabM = (TabooM* 3 )) #1550
        elif Trigger == "anal":
                    $ Approval = ApprovalCheck(Girl,1550,Bonus=Mod, TabM = (TabooM* 3 )) #1550
        elif Trigger == "sex":
                    $ Approval = ApprovalCheck(Girl,1400,Bonus=Mod, TabM = (TabooM* 3 )) #1400
        elif Trigger == "lick pussy" or Trigger == "cun":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = (TabooM* 2 )) #1250
        elif Trigger2 == "jackin" or Trigger2 == "jilling":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = (TabooM* 2 )) #1250
        elif Trigger == "blow":
                    $ Approval = ApprovalCheck(Girl,1300,Bonus=Mod, TabM = (TabooM* 2 )) #1300
        elif Trigger == "titjob":
                    $ Approval = ApprovalCheck(Girl,1200,Bonus=Mod, TabM = (TabooM* 3 )) #1200
        elif Trigger == "hotdog":
                    $ Approval = ApprovalCheck(Girl,1000,Bonus=Mod, TabM = (TabooM* 3 )) #1000
        elif Trigger == "hand" or Girl.Offhand  == "hand" or Trigger == "finger" or Girl.Offhand  == "finger":
                    $ Approval = ApprovalCheck(Girl,1100,Bonus=Mod, TabM = (TabooM* 2 )) #1100
        elif Trigger == "foot":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = (TabooM* 2 )) #1250
        elif Trigger == "dildo anal":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = (TabooM* 2 )) #1250
        elif Trigger == "dildo pussy":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = (TabooM* 2 )) #1250
        elif Trigger == "insert ass":
                    $ Approval = ApprovalCheck(Girl,1300,Bonus=Mod, TabM = (TabooM* 2 )) #1300
        elif Trigger == "fondle pussy" or Trigger == "insert pussy":
                    $ Approval = ApprovalCheck(Girl,1050,Bonus=Mod, TabM = (TabooM* 2 )) #1050
        elif Trigger == "suck breasts":
                    $ Approval = ApprovalCheck(Girl,1050,Bonus=Mod, TabM = (TabooM* 3 )) #1050
        elif Trigger == "fondle breasts":
                    $ Approval = ApprovalCheck(Girl,950,Bonus=Mod, TabM = (TabooM* 2 )) #950
        elif Trigger == "fondle ass":
                    $ Approval = ApprovalCheck(Girl,850,Bonus=Mod, TabM = (TabooM* 1 )) #850

        elif Trigger == "masturbation":
                    $ Approval = ApprovalCheck(Girl,1200,Bonus=Mod, TabM = (TabooM* 2 ))#1200

        elif Trigger == "kiss you":
                    $ Approval = ApprovalCheck(Girl,500,Bonus=Mod, TabM = 0)            #500
        elif Trigger == "fondle thighs":
                    $ Approval = ApprovalCheck(Girl,750,Bonus=Mod, TabM = 0)            #750

        elif Trigger == "lesbian":
                    $ Approval = ApprovalCheck(Girl,1350,Bonus=Mod, TabM = (TabooM* 2 )) #1350


        #Threesomecheck
        if not Approval:
                    # If it fails the primary trigger check, skip the next part
                    pass
        elif not Girl2:
                    pass
        elif Girl is WandaX and ApprovalCheck(Girl,1200,Bonus=(Mod+200)):
                    $ Approval = 2 #Wanda is less bothered by others girls doing stuff
        elif Girl2.Offhand == "lick ass" or Girl2.Offhand == "lick girl ass":
                    $ Approval = ApprovalCheck(Girl,1750,Bonus=(Mod+200), TabM = (TabooM* 3 )) #1750
        elif Girl2.Offhand == "lick pussy" or Girl2.Offhand == "cun" or Girl2.Offhand == "lick girl pussy":
                    $ Approval = ApprovalCheck(Girl,1450,Bonus=(Mod+200), TabM = (TabooM* 2 )) #1450
        elif Girl2.Offhand == "blow":
                    $ Approval = ApprovalCheck(Girl,1300,Bonus=(Mod+200), TabM = (TabooM* 2 )) #1300
        elif Girl2.Offhand == "hand" or Girl2.Offhand == "finger":
                    $ Approval = ApprovalCheck(Girl,1200,Bonus=(Mod+200), TabM = (TabooM* 2 )) #1200
        elif Girl2.Offhand == "insert ass" or Girl2.Offhand == "insert girl ass":
                    $ Approval = ApprovalCheck(Girl,1500,Bonus=(Mod+200), TabM = (TabooM* 2 )) #1500
        elif Girl2.Offhand == "fondle pussy" or Girl2.Offhand == "fondle girl pussy":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=(Mod+200), TabM = (TabooM* 2 )) #1250
        elif Girl2.Offhand == "suck breasts" or Girl2.Offhand == "suck girl breasts":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=(Mod+200), TabM = (TabooM* 3 )) #1250
        elif Girl2.Offhand == "fondle breasts" or Girl2.Offhand == "fondle girl breasts":
                    $ Approval = ApprovalCheck(Girl,1150,Bonus=(Mod+200), TabM = (TabooM* 2 )) #1150
        elif Girl2.Offhand == "kiss girl":
                    $ Approval = ApprovalCheck(Girl,1050,Bonus=(Mod+200), TabM = 0)             #1050
        elif Girl2.Offhand == "kiss both":
                    $ Approval = ApprovalCheck(Girl,1050,Bonus=(Mod+200), TabM = 0)             #1050
        elif Girl2.Offhand == "fondle ass" or Girl2.Offhand == "fondle girl ass":
                    $ Approval = ApprovalCheck(Girl,1050,Bonus=(Mod+200), TabM = (TabooM* 1 ))  #1050
        elif Girl2.Offhand == "masturbation":
                    $ Approval = ApprovalCheck(Girl,1400,Bonus=(Mod+200), TabM = (TabooM* 2 ))  #1400
        elif Girl2.Offhand == "watch":
                    $ Approval = ApprovalCheck(Girl,1000,Bonus=(Mod+200), TabM = 0)             #1000
        elif Girl2.Offhand == "kiss you":
                    $ Approval = ApprovalCheck(Girl,600,Bonus=Mod, TabM = 0)                    #600

        if Girl.Forced:
                return Approval


        if not Silent and Approval < 2:
            if "activity" not in Girl.RecentActions:
                #if approval is 2 (150 above the threshold) then it autopasses, otherwise it questions
                $ Girl.FaceChange("sadside",1)
                if Girl is RogueX:
                        if Girl2:
                            ch_r "Я не уверена, как-никак [Girl2.Name] здесь."
                        ch_r "Мне это не нравится, [Girl.Petname]."
                elif Girl is KittyX:
                        if Girl2:
                            ch_k "Я не уверена, все таки [Girl2.Name] здесь."
                        ch_k "Мне[KittyX.like]это не очень нравится."
                elif Girl is EmmaX:
                        if Girl2:
                            ch_e "Я не уверена, мне не комфортно, когда [Girl2.Name] рядом."
                        ch_e "Ситуация становится. . . как по мне, возмутительной."
                elif Girl is LauraX:
                        if Girl2:
                            ch_l "[Girl2.Name] меня бесит."
                        else:
                            ch_l "Ситуация становится странной."
                        ch_l "Увидимся позже."
                elif Girl is JeanX:
                        if Girl2:
                            ch_j "Я не хочу находится рядом с [Girl2.Name]."
                        ch_j "Я ухожу."
                elif Girl is StormX:
                        if Girl2:
                            ch_s "Я не не хочу заниматься подобный, когда [Girl2.Name] рядом."
                        ch_s "Для меня это слишком, прости."
                elif Girl is JubesX:
                        if Girl2:
                            ch_v "Не когда [Girl2.Name] рядом, [Girl.Petname]."
                        ch_v "Это совсем не круто. Извини."
                elif Girl is GwenX:
                        if Girl2:
                            ch_g "Я, эм, не когда рядом [Girl2.Name], [Girl.Petname]."
                        ch_g "Думаю, я пас. . ."
                elif Girl is BetsyX:
                        if Girl2:
                            ch_b "Пардон, [Girl2.Name], это уже чересчур."
                        else:
                            ch_b "Пардон, это уже чересчур. . ."
                elif Girl is DoreenX:
                        if Girl2:
                            ch_d "Ох, ого, [Girl2.Name], я, эм. . . для меня это слишком. . ."
                        else:
                            ch_d "Ох, я, эм. . . для меня это слишком. . ."
                elif Girl is WandaX:
                        if Girl2:
                            ch_w "Воу, [Girl2.Name], это слишком. . ."
                        else:
                            ch_w "Воу, это слишком. . ."
                menu:
                    extend ""
                    "[[ничего не говорить]":
                            pass
                    "Хорошо, давай остановимся.":
                                $ Girl.FaceChange("smile")
                                $ Girl.Statup("Love", 70, 2)
                                $ Girl.Statup("Love", 90, 2)
                                $ Girl.Statup("Inbt", 50, 2)
                                $ Girl.Statup("Inbt", 70, 1)
                                call AnyLine(Girl,"Спасибо. . .")
                                call Sex_Over
                                jump Misplaced

                    "Пожалуйста?":
                        if Approval and (ApprovalCheck(Girl, 850, "L") or ApprovalCheck(Girl, 1500)):
                                $ Girl.Statup("Love", 80, 1)
                                $ Girl.Statup("Obed", 80, 2)
                                $ Girl.Statup("Inbt", 60, 1)
                                call AnyLine(Girl,"Хорошо, ради тебя. . .")
                                "Она остается, пока."
                                $ Approval = 2
                        else:
                                $ Girl.FaceChange("sad")
                                call AnyLine(Girl,"Извини. . .")

                    "Мы продолжим.":
                        $ Girl.Statup("Love", 80, -1)
                        if Approval and (ApprovalCheck(Girl, 550, "O") or ApprovalCheck(Girl, 1500)):
                                $ Girl.Statup("Obed", 70, 2)
                                $ Girl.Statup("Obed", 90, 2)
                                $ Girl.Statup("Inbt", 60, 1)
                                $ Girl.FaceChange("sad")
                                call AnyLine(Girl,"Если ты настаиваешь. . .")
                                "Она остается, пока."
                                $ Approval = 2
                        else:
                                $ Girl.FaceChange("angry",1)
                                call AnyLine(Girl,"Я так не думаю.")

                    "Ой, да ладно, мы же развлекаемся.":
                        if Approval and (ApprovalCheck(Girl, 550, "I") or ApprovalCheck(Girl, 1500)):
                                $ Girl.Statup("Obed", 70, 2)
                                $ Girl.Statup("Inbt", 70, 2)
                                $ Girl.Statup("Inbt", 90, 1)
                                call AnyLine(Girl,"Хорошо, ради тебя. . .")
                                "Она остается, пока."
                                $ Approval = 2
                        else:
                            $ Girl.FaceChange("angry")
                            if Girl in (StormX,EmmaX):
                                call AnyLine(Girl,"Я так не думаю. . .")
                            else:
                                call AnyLine(Girl,"Ага, я от этого не в восторге. . .")

                $ Girl.AddWord(1,"activity") #adds word to Recent
            else: #if "activity" in Girl.RecentActions:
                    call AnyLine(Girl,"Нет, для меня это слишком. . .")


        if Removal and Approval < 2:
                call Remove_Girl(Girl,2)
                "[Girl.Name] уходит."
                $ Approval = 0

        return Approval
#end Activity Checker  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start First Seen Peen / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Seen_First_Peen(Primary=0, Secondary=0, Silent=0, Undress=0, Passive=0, GirlsNum=0, React=0, BOptions=[]):
    # call Seen_First_Peen(Primary,Secondary,Silent,Undress)
    # Primary is the first girl, Secondary the second, if there is one
    # _return will be 0 if other girl didn't comment,
    # 1 = if the other girl commented, 2 = didn't like it
    # Girlsnum will pass Second to the next girl, and keep track of whether anyone acted
    # Passive will be 3 or 4 if linked to Sex dialog acts 3 or 4
    if not Primary:
            #if this is not during a sex act
            $ BOptions = Present[:]  #loads up all local girls
            $ renpy.random.shuffle(BOptions)
            while BOptions:
                    #cycles through each girl possible,
                    #If girl is around, check to see if she noticed your cock yet
                    if (Ch_Focus == BOptions[0] or D20 >= 10) and "peen" not in BOptions[0].RecentActions:
                            #If BOptions[0] is the primary or secondary character, and hasn't seen your cock yet, call the thing
                            #call expression BOptions[0].Tag + "_First_Peen" pass (Silent,Undress)
                            call Girl_First_Peen(BOptions[0],Silent,Undress)
                            $ GirlsNum = _return
                    $ BOptions.remove(BOptions[0])

            if not GirlsNum:
                #if no girls are present
                if "naked" not in Player.RecentActions and Undress:
                        "Вы полностью раздеваетесь."
                        $ Player.AddWord(1,"naked",0,0,0)
                elif "cockout" in Player.RecentActions:
                        return
                elif not Player.Male:
                        "Вы оголяете свою киску."
                else:
                        "Вы достаете свой член."
                $ Player.AddWord(1,"cockout",0,0,0)
    #end if not during a sex act
    else:
            #It's during a sex act
            if Passive:
                    #if in Passive mode, during sex dialog, it only activates if cock is already out.
                    if Approval == Passive and "cockout" not in Player.RecentActions:
                        #if both are 3 or both are 4, meaning the activities matched up,
                        call CockOut
                    if "cockout" not in Player.RecentActions:
                        return

            #call expression Primary.Tag + "_First_Peen" pass (Silent,Undress,React=React)
            call Girl_First_Peen(Primary,Silent,Undress,React=React)

            if Secondary:
                    #call expression Secondary.Tag + "_First_Peen" pass (Silent,Undress,Second = _return)
                    call Girl_First_Peen(Secondary,Silent,Undress,Second = _return)
    return

label CockOut:
        # Passive and therefore Approval will be 3 or 4 if linked to Sex dialog acts 3 or 4
        if Approval == 3:
                    #if attached to line 3, use the Primary girl
                    #call expression Primary.Tag + "_First_Peen" pass (React=1)
                    call Girl_First_Peen(Primary,React=1)
        elif Approval == 4:
                    #if attached to line 4, use the Secondary girl
                    #call expression Secondary.Tag + "_First_Peen" pass (React=1)
                    call Girl_First_Peen(Secondary,React=1)
        $ Approval = 0
        return

label Get_Dressed: #checked each time she sees your cock
        #if no girls are present
        if "naked" in Player.RecentActions:
                "Вы одеваетесь."
                $ Player.DrainWord("naked")
                $ Player.DrainWord("cockout")
        elif "cockout" in Player.RecentActions:
                if Player.Male:
                        "Вы прячете свой член."
                else:
                        "Вы застегиваете свои штаны."
                $ Player.DrainWord("cockout")
        return

label Girl_Dressed(BO=[],Girls=0):
        #if asked to put their clothes back on.
        $ BO = TotalGirls[:]
        $ PassLine = 0
        python:
            for BX in BO:
                if BX.Loc == bg_current:
                    if BX.OutfitChange(6,Changed=1) == 2:
                        #if BX in Party:
                        if PassLine:
                            PassLine = PassLine + " с " + BX.Name_tvo
                        else:
                            PassLine = BX.Name
                        Girls += 1
                        BX.Set_Temp_Outfit() #sets current outfit as temporary
        if Girls > 1:
            "[PassLine] одеваются."
        elif Girls:
            "[PassLine] одевается."
        $ PassLine = 0
        return

# End First Seen Peen / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Seen Peen / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_First_Peen(Girl = 0, Silent = 0, Undress = 0, Second = 0, React = 0):  #rkeljsvgb
        #checked each time she sees your cock  ## call Girl_First_Peen(RogueX,0,1)
        #if Silent it doesn't say anything
        #if Undress then you get nude
        #if Secondary then this is the second girl to see it.
        # React 0 if other girl didn't comment,
        # 1 = if the other girl commented, 2 = didn't like it
        if not Player.Male:
                #if lacks a penis, use the "seen pussy" version instead.
                call Girl_First_Puss(Girl,Silent,Undress,Second,React)
                return

        if Girl.Loc != bg_current:
                    if Partner == Girl:
                            $ Partner = 0
                    return
        if "cockout" in Player.RecentActions and "peen" in Girl.RecentActions:
                    #If the cock is already out and she's seen it, return
                    return

        if "unseen" in Girl.RecentActions:
                    #if she hasn't noticed you, she won't notice this, yet.
                    return

        $ Girl.RecentActions.append("peen")
        $ Girl.DailyActions.append("peen")
        $ Girl.SeenPeen += 1
        $ Girl.Statup("Inbt", 30, 2)
        $ Girl.Statup("Inbt", 80, 1)

        if Second:
                #If another girl commented on it first. . .
                if Girl.SeenPeen == 1:
                                $ Girl.FaceChange("surprised", 2)
                                if Girl is RogueX:
                                        if not Player.Male:
                                            ch_r "Воу, а она очень милая. . ."
                                        else:
                                            ch_r "Воу, а он очень милый. . ."
                                elif Girl is KittyX:
                                        ch_k "Ох, ничего себе, похоже, ты не шутишь. . ."
                                elif Girl is EmmaX:
                                        $ Girl.FaceChange("sly", 2, Eyes = "down")
                                        ch_e "Боже, какой впечатляющий образец. . ."
                                elif Girl is LauraX:
                                        $ Girl.FaceChange("sly", 2, Eyes = "down")
                                        if not Player.Male:
                                            ch_l "Хм, а он неплоха. . ."
                                        else:
                                            ch_l "Хм, а он неплох. . ."
                                elif Girl is JeanX:
                                        $ Girl.FaceChange("sly", 2, Eyes = "down")
                                        if not Player.Male:
                                            ch_j "Да, а она хорошо выглядит. . ."
                                        else:
                                            ch_j "Да, а он хорошо выглядит. . ."
                                elif Girl is StormX:
                                        $ Girl.FaceChange("sly", 2, Eyes = "down")
                                        ch_s "Да, впечатляет. . ."
                                elif Girl is JubesX:
                                        $ Girl.FaceChange("sly", 2, Eyes = "down")
                                        ch_v "Ну ничего себе, дааа. . ."
                                elif Girl is GwenX:
                                        $ Girl.FaceChange("sly", 2, Eyes = "down")
                                        if not Player.Male:
                                            ch_g "Красивая. . ."
                                        else:
                                            ch_g "Большой. . ."
                                elif Girl is BetsyX:
                                        $ Girl.FaceChange("sly", 2, Eyes = "down")
                                        if not Player.Male:
                                            ch_b "Ох, ну и ну! Очень милая. . ."
                                        else:
                                            ch_b "Ох, ну и ну! Очень милый. . ."
                                elif Girl is DoreenX:
                                        $ Girl.FaceChange("smile", 2, Eyes = "down")
                                        if not Player.Male:
                                            ch_d "Ого, а она милая. . ."
                                        else:
                                            ch_d "Ого, а он милый. . ."
                                elif Girl is WandaX:
                                        $ Girl.FaceChange("sly", 1, Eyes = "down")
                                        if not Player.Male:
                                            ch_w "-О-, а она милая!"
                                        else:
                                            ch_w "-О-, а он милый!"
                                $ Girl.FaceChange("bemused", 1)
                elif Second == 1:
                        # The other girl liked it
                        if not ApprovalCheck(Girl, 800) and not ApprovalCheck(Girl, 500, "I"):
                                $ Girl.FaceChange("sad", 1)
                                if Girl is RogueX:
                                        ch_r "Что-то в этом есть. . ."
                                elif Girl is KittyX:
                                        ch_k "Наверное, я с ней согласна. . ."
                                elif Girl is EmmaX:
                                        ch_e "Полагаю, у тебя не так уж много опыта. . ."
                                elif Girl is LauraX:
                                        ch_l "Наверное, так. . ."
                                elif Girl is JeanX:
                                        if not Player.Male:
                                            ch_j "Да, она неплоха. . ."
                                        else:
                                            ch_j "Да, он неплох. . ."
                                elif Girl is StormX:
                                        ch_s "Полагаю, возможно так и есть. . ."
                                elif Girl is JubesX:
                                        ch_v "Наверное. . ."
                                elif Girl is GwenX:
                                        ch_g "Конечно. . ."
                                elif Girl is BetsyX:
                                        ch_b "Пожалуй. . ."
                                elif Girl is DoreenX:
                                        ch_d "Наверное. . ."
                                elif Girl is WandaX:
                                        ch_w "Думаешь?"
                        else:
                                $ Girl.FaceChange("bemused", 1)
                                if Girl is RogueX:
                                        if not Player.Male:
                                            ch_r "Да, она действительно красива. . ."
                                        else:
                                            ch_r "Да, он действительно красив. . ."
                                elif Girl is KittyX:
                                        ch_k "Я знаю, верно?!"
                                elif Girl is EmmaX:
                                        if not Player.Male:
                                            ch_e "Да, меня она тоже застала врасплох. . ."
                                        else:
                                            ch_e "Да, меня он тоже застал врасплох. . ."
                                elif Girl is LauraX:
                                        if not Player.Male:
                                            ch_l "Да, она и вправду милая. . ."
                                        else:
                                            ch_l "Да, он и вправду милый. . ."
                                elif Girl is JeanX:
                                        ch_j "Верно?"
                                elif Girl is StormX:
                                        ch_s "Я тоже так подумала."
                                elif Girl is JubesX:
                                        ch_v "Верно?"
                                elif Girl is GwenX:
                                        if not Player.Male:
                                            ch_g "Красивая. . ."
                                        else:
                                            ch_g "Большой. . ."
                                elif Girl is BetsyX:
                                        if not Player.Male:
                                            ch_b "О да, очень милая. . ."
                                        else:
                                            ch_b "О да, очень милый. . ."
                                elif Girl is DoreenX:
                                        ch_d "Ага, это точно. . ."
                                elif Girl is WandaX:
                                        ch_w "-Ага-, именно так!"
                elif Second == 2:
                        # The other girl didn't like it
                        if not ApprovalCheck(Girl, 800) and not ApprovalCheck(Girl, 500, "I"):
                                $ Girl.FaceChange("sad", 1)
                                if Girl is RogueX:
                                        ch_r "Ладно, как скажешь. . ."
                                elif Girl is KittyX:
                                        ch_k "Ну значит мы определились. . ."
                                elif Girl is EmmaX:
                                        ch_e "Ты прямо знаток. . ."
                                elif Girl is LauraX:
                                        ch_l "Наверное. . ."
                                elif Girl is JeanX:
                                        ch_j "Ага. . ."
                                elif Girl is StormX:
                                        ch_s "Верно. . ."
                                elif Girl is JubesX:
                                        ch_v "Наверное. . ."
                                elif Girl is GwenX:
                                        ch_g "Конечно. . ."
                                elif Girl is BetsyX:
                                        ch_b "Пожалуй. . ."
                                elif Girl is DoreenX:
                                        ch_d "Наверное. . ."
                                elif Girl is WandaX:
                                        ch_w "Серьезно?"
                        else:
                                $ Girl.FaceChange("confused", 1)
                                if Girl is RogueX:
                                        if not Player.Male:
                                            ch_r "Ну, а мне понравилась. . ."
                                        else:
                                            ch_r "Ну, а мне понравился. . ."
                                        $ Girl.FaceChange("sexy", 1)
                                elif Girl is KittyX:
                                        if not Player.Male:
                                            ch_k "Да ладно тебе, она милая!"
                                        else:
                                            ch_k "Да ладно тебе, он милый!"
                                        $ Girl.FaceChange("smile", 1)
                                elif Girl is EmmaX:
                                        ch_e "Ты просто ничего не понимаешь. . ."
                                        $ Girl.FaceChange("sly",0)
                                elif Girl is LauraX:
                                        ch_l "Ах, да ладно тебе, все не так уж плохо. . ."
                                        $ Girl.FaceChange("sly",0)
                                elif Girl is JeanX:
                                        ch_j "Ну, я видела и похуже. . ."
                                        $ Girl.FaceChange("sly",0)
                                elif Girl is StormX:
                                        ch_s "Это далеко не самый худший образец, что я видела. . ."
                                        $ Girl.FaceChange("sly",0)
                                elif Girl is JubesX:
                                        ch_v "Мне же больше достанется. . ."
                                        $ Girl.FaceChange("sly",0)
                                elif Girl is GwenX:
                                        ch_g "Ты не знаешь, что упускаешь. . ."
                                        $ Girl.FaceChange("sly",0)
                                elif Girl is BetsyX:
                                        ch_b "Я могу понять, если для тебя это слишком. . ."
                                        $ Girl.FaceChange("sly",0)
                                elif Girl is DoreenX:
                                        $ Girl.FaceChange("smile", 1, Eyes = "down")
                                        if not Player.Male:
                                            ch_d "Ну, а я думаю, что она очень милая. . ."
                                        else:
                                            ch_d "Ну, а я думаю, что он очень милый. . ."
                                elif Girl is WandaX:
                                        $ Girl.FaceChange("sly", 1, Eyes = "down")
                                        if not Player.Male:
                                            ch_w "Ну а -мне- она нравится. . ."
                                        else:
                                            ch_w "Ну а -мне- он нравится. . ."
                                        $ Girl.FaceChange("sly", 1)
                $ Silent = 1

        if Undress:
                    $ Player.AddWord(1,"naked")
        if not Silent:
            if "cockout" in Player.RecentActions:
                    $ Girl.FaceChange("down", 2)
                    "[Girl.Name] смотрит вниз на ваш торчащий член."
                    $ Girl.FaceChange("smile", 1)
            elif React:
                    #If called by a sex dialog
                    "[Girl.Name] тянется к вашим штанам и вытаскивает ваш член."
            elif Undress:
                    "Вы полностью раздеваетесь."
            else:
                    "Вы достаете свой член."
            $ Player.AddWord(1,"cockout")
            if not Girl.Forced and not React and Taboo > 20 and (not ApprovalCheck(Girl, 1500) or Girl.SEXP < 10) and bg_current != "bg showerroom" and Girl not in (JeanX,StormX):
                #if it's a semi-public space that isn't the showers, and she is not down with this. . .
                if not ApprovalCheck(Girl, 800) and not ApprovalCheck(Girl, 500, "I"):
                        #If the girl is very not into it. . .
                        if Girl is EmmaX and ("detention" in Girl.RecentActions or "classcaught" in Girl.RecentActions):
                            #special exceptions for detention and classcaught events
                            $ Girl.FaceChange("confused", Eyes="down")
                            ch_e "Ммм?"
                            $ Girl.FaceChange("surprised", Eyes="squint")
                            if Girl.SeenPeen == 1:
                                    $ Girl.Statup("Love", 30, 10)
                                    $ Girl.Statup("Love", 90, 5)
                                    $ Girl.Statup("Obed", 50, 20)
                                    $ Girl.Statup("Inbt", 60, 30)
                            else:
                                    $ Girl.Statup("Love", 90, 2)
                                    $ Girl.Statup("Obed", 50, 3)
                                    $ Girl.Statup("Inbt", 60, 5)
                            ch_e "Что ж, полагаю, в этом случае я могу сделать исключение."
                            $ React = 1
                        else:
                            #If the girl is very not into it. . .
                            $ Girl.FaceChange("surprised", 2)
                            if Girl is RogueX:
                                    ch_r "Какого черта?"
                            elif Girl is KittyX:
                                    ch_k "А?!"
                            elif Girl is EmmaX:
                                    $ Girl.Eyes = "down"
                                    ch_e "Ммм?"
                            elif Girl is LauraX:
                                    $ Girl.Eyes = "down"
                                    ch_l "Ммм?"
                            elif Girl is JubesX:
                                    $ Girl.Eyes = "down"
                                    ch_v "Эй. . ."
                                    $ Girl.Eyes = "squint"
                                    ch_v "Что за дела?"
                            elif Girl is GwenX:
                                    $ Girl.Eyes = "down"
                                    ch_g "Ох. . . значит теперь мы достаем члены. . ."
                            elif Girl is BetsyX:
                                    $ Girl.Eyes = "down"
                                    ch_b "Я считаю, что это слишком даже для Америки. . ."
                            elif Girl is DoreenX:
                                    $ Girl.Eyes = "down"
                                    ch_d "Воу, спрячь его!"
                            elif Girl is WandaX:
                                    $ Girl.Eyes = "down"
                                    ch_w "Эй, держи его в штанах!"
                            $ Girl.FaceChange("angry", 1)
                            $ Girl.RecentActions.append("angry")
                            $ Girl.DailyActions.append("angry")
                            $ React = 2
                            if Girl.SeenPeen == 1:
                                        $ Girl.Statup("Love", 90, -20)
                                        $ Girl.Statup("Obed", 50, 30)
                                        $ Girl.Statup("Inbt", 60, 20)
                            else:
                                #if this is the second time you've done this today. . .
                                if Girl is RogueX:
                                        ch_r "Что с тобой -не так-?"
                                elif Girl is KittyX:
                                        ch_k "Чувак, серьезно, ты больной!"
                                elif Girl is EmmaX:
                                        ch_e "[Girl.Petname]! Нам придется разобраться с этой. . . твоей проблемой."
                                elif Girl is LauraX:
                                        ch_l "Это совсем не клево."
                                elif Girl is JubesX:
                                        ch_v "Держи его в штанах. . ."
                                elif Girl is GwenX:
                                        ch_g "Значит для тебя это довольно обычное дело. . ."
                                elif Girl is BetsyX:
                                        ch_b "Похоже ты. . . всегда так делаешь. . ?"
                                elif Girl is DoreenX:
                                        ch_d "Ты не можешь держать его в штанах?"
                                elif Girl is WandaX:
                                        ch_w "Ну ты чего?!"
                                if Girl.DailyActions.count("peen") >= 2:
                                        #if she's seen more than one peen today
                                        $ Girl.Statup("Love", 90, -1)
                                        $ Girl.Statup("Obed", 50, 1)
                                        $ Girl.Statup("Inbt", 60, 2)
                                else:
                                        $ Girl.Statup("Love", 90, -5)
                                        $ Girl.Statup("Obed", 50, 10)
                                        $ Girl.Statup("Inbt", 60, 10)
                #end if bg_current != "bg showerroom" and not ApprovalCheck(Girl, 800) and not ApprovalCheck(Girl, 500, "I"):
                else:
                            #if ApprovalCheck is 800-1500 and not ApprovalCheck(Girl, 500, "I"):
                            $ Girl.FaceChange("surprised", 2)
                            if Girl is RogueX:
                                    ch_r "Ты должен убрать эту штуку!"
                            elif Girl is KittyX:
                                    ch_k "Эм, ты не должен[Girl.like]доставать его на людях."
                            elif Girl is EmmaX:
                                    ch_e "Осторожней, не доставай его где попало."
                            elif Girl is LauraX:
                                    ch_l "Не думаю, что сейчас подходящее место и время."
                            elif Girl is JubesX:
                                    ch_v "Эм. . . может быть, тебе стоит убрать его подальше?"
                            elif Girl is GwenX:
                                    ch_g "Неужели больше никто этого не замечает?"
                            elif Girl is BetsyX:
                                    ch_b "Я искренне желаю, чтобы ты убрал его. . ."
                            elif Girl is DoreenX:
                                    ch_d "Воу, спрячь его!"
                            elif Girl is WandaX:
                                    ch_w "Эй, держи его в штанах!"
                            if Girl.SeenPeen == 1:
                                    $ Girl.FaceChange("bemused", 1,Eyes="down")
                                    if Girl is RogueX:
                                            ch_r "То есть. . . Нет, убери его!"
                                    elif Girl is KittyX:
                                            ch_k "Или[Girl.like]может быть. . . хотя, нет. . ."
                                    elif Girl is EmmaX:
                                            $ Girl.Eyes = "down"
                                            ch_e ". . . однако, впечатляет. . ."
                                    elif Girl is LauraX:
                                            ch_l ". . .не то чтобы я особо возражала, но. . ."
                                    elif Girl is JubesX:
                                            ch_v "Или. . . нет. . ."
                                    elif Girl is DoreenX:
                                            ch_d "Хмммм. . ."
                                    elif Girl is WandaX:
                                            ch_w ". . . знаешь, иногда. . ."
                                    $ Girl.Statup("Love", 90, 20)
                                    $ Girl.Statup("Obed", 50, 20)
                                    $ Girl.Statup("Inbt", 60, 30)
                            $ Girl.FaceChange("bemused", 1)
                            $ React = 2

                #end if not Girl.Forced and not React and Taboo > 20 and (not ApprovalCheck(Girl, 1500) or Girl.SEXP < 10) and bg_current != "bg showerroom" and Girl is not JeanX:
            elif Girl.SeenPeen > 10:
                        #if it's been more than 10 times, return
                        return 0
            elif ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "L"):
                    #She basically likes it
                    $ Girl.FaceChange("sly",1)
                    if Girl.SeenPeen == 1:
                            $ Girl.FaceChange("surprised",2)
                            if Girl is RogueX:
                                    if not Player.Male:
                                        ch_r "Ого, я и представить не могла, что вблизи она окажется такой красивой."
                                    else:
                                        ch_r "Ого, я и представить не могла, что вблизи он окажется таким большим."
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Love", 90, 5)
                            elif Girl is KittyX:
                                    $ Girl.FaceChange("surprised",2)
                                    ch_k "Эм. . . впечатляет."
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Love", 90, 3)
                            elif Girl is EmmaX:
                                    $ Girl.FaceChange("surprised",1, Eyes="down")
                                    ch_e "Что ж, это безусловно интересный экземпляр."
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Love", 50, 5)
                                    $ Girl.Statup("Love", 90, 10)
                            elif Girl is LauraX:
                                    $ Girl.FaceChange("surprised",1, Eyes="down")
                                    ch_l "Хм, а у тебя там очень хорошая штука. . ."
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Love", 50, 5)
                                    $ Girl.Statup("Love", 90, 10)
                            elif Girl is JeanX:
                                    $ Girl.FaceChange("confused",1, Eyes="down",Mouth="smile")
                                    ch_j "Так, что тут у нас. . ."
                                    $ Girl.FaceChange("bemused",1)
                                    ch_j "Очень мило, [Girl.Petname]."
                                    $ Girl.Statup("Love", 50, 5)
                                    $ Girl.Statup("Love", 90, 10)
                                    $ Girl.Statup("Obed", 80, 3)
                            elif Girl is StormX:
                                    $ Girl.FaceChange("confused",1, Eyes="down")
                                    if not Player.Male:
                                        ch_s "Хмм. . . она прекрасна."
                                    else:
                                        ch_s "Хмм. . . он прекрасен."
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Love", 50, 5)
                                    $ Girl.Statup("Love", 90, 5)
                                    $ Girl.Statup("Inbt", 60, 2)
                            elif Girl is JubesX:
                                    $ Girl.FaceChange("surprised",2, Eyes="down")
                                    if not Player.Male:
                                        ch_v "Ох. . . миленькая."
                                    else:
                                        ch_v "Ох. . . миленький."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Love", 80, 3)
                                    $ Girl.Statup("Obed", 80, 1)
                                    $ Girl.Statup("Inbt", 60, 4)
                            elif Girl is GwenX:
                                    $ Girl.FaceChange("surprised",2, Eyes="down")
                                    if not Player.Male:
                                        ch_g "Изящная."
                                    else:
                                        ch_g "Изящный."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Love", 80, 3)
                                    $ Girl.Statup("Obed", 80, 1)
                                    $ Girl.Statup("Inbt", 60, 4)
                            elif Girl is BetsyX:
                                    $ Girl.FaceChange("surprised",2, Eyes="down")
                                    if not Player.Male:
                                        ch_b "Ох, она очень милая. . ."
                                    else:
                                        ch_b "Ох, он очень милый. . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Love", 80, 3)
                                    $ Girl.Statup("Obed", 80, 1)
                                    $ Girl.Statup("Inbt", 60, 4)
                            elif Girl is DoreenX:
                                    $ Girl.FaceChange("surprised",2, Eyes="down")
                                    ch_d "Ooo."
                                    $ Girl.FaceChange("smile",1)
                                    $ Girl.Statup("Love", 80, 3)
                                    $ Girl.Statup("Obed", 80, 1)
                                    $ Girl.Statup("Inbt", 60, 4)
                            elif Girl is WandaX:
                                    $ Girl.FaceChange("surprised",2, Eyes="down")
                                    ch_w "Ну привет. . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Love", 80, 3)
                                    $ Girl.Statup("Obed", 80, 1)
                                    $ Girl.Statup("Inbt", 60, 4)
                    elif Girl.SeenPeen == 2:
                            if Girl is RogueX:
                                    if not Player.Male:
                                        ch_r "Она и правда впечатляет."
                                    else:
                                        ch_r "Он и правда впечатляет."
                                    $ Girl.Statup("Obed", 50, 5)
                            elif Girl is KittyX:
                                    if not Player.Male:
                                        ch_k "Никак не могу забыть о ней."
                                    else:
                                        ch_k "Никак не могу забыть о нем."
                                    $ Girl.Statup("Obed", 50, 7)
                            elif Girl is EmmaX:
                                    $ Girl.Eyes = "down"
                                    ch_e "Ох, и снова здравствуй."
                                    $ Girl.Statup("Inbt", 50, 5)
                            elif Girl is LauraX:
                                    $ Girl.Eyes = "down"
                                    if not Player.Male:
                                        ch_l "Ох, вот и она."
                                    else:
                                        ch_l "Ох, вот и он."
                                    $ Girl.Statup("Obed", 50, 2)
                                    $ Girl.Statup("Inbt", 50, 3)
                            elif Girl is JeanX:
                                    $ Girl.Eyes = "down"
                                    ch_j "Все еще довольно впечатляюще. . ."
                                    $ Girl.Statup("Love", 90, 3)
                                    $ Girl.Statup("Obed", 80, 3)
                            elif Girl is StormX:
                                    $ Girl.Eyes = "down"
                                    ch_s "Хмм. . ."
                                    $ Girl.Statup("Inbt", 50, 2)
                            elif Girl is JubesX:
                                    $ Girl.FaceChange("sly",1, Eyes="down")
                                    ch_v "Привет тебе снова."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Obed", 80, 1)
                                    $ Girl.Statup("Inbt", 60, 1)
                            elif Girl is GwenX:
                                    $ Girl.FaceChange("smile",1, Eyes="down")
                                    ch_g ". . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Obed", 80, 1)
                                    $ Girl.Statup("Inbt", 60, 1)
                            elif Girl is BetsyX:
                                    $ Girl.FaceChange("smile",1, Eyes="down")
                                    ch_b ". . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Obed", 80, 1)
                                    $ Girl.Statup("Inbt", 60, 1)
                            elif Girl is DoreenX:
                                    $ Girl.FaceChange("smile",1, Eyes="down")
                                    ch_d "Хмммм. . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Obed", 80, 1)
                                    $ Girl.Statup("Inbt", 60, 1)
                            elif Girl is WandaX:
                                    $ Girl.FaceChange("sly",1, Eyes="down")
                                    ch_w "Ага. . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Obed", 80, 1)
                                    $ Girl.Statup("Inbt", 80, 2)
                    elif Girl.SeenPeen == 5:
                            if Girl is RogueX:
                                    ch_r "Мне нравится этот парень."
                                    $ Girl.Statup("Inbt", 60, 5)
                            elif Girl is KittyX:
                                    ch_k "А вот и он."
                                    $ Girl.Statup("Inbt", 60, 5)
                            elif Girl is EmmaX:
                                    ch_e "Да, мы уже виделись раньше."
                                    $ Girl.Statup("Obed", 60, 7)
                            elif Girl is LauraX:
                                    ch_l "Да, я уже его видела."
                                    $ Girl.Statup("Obed", 60, 4)
                                    $ Girl.Statup("Inbt", 60, 3)
                            elif Girl is JeanX:
                                    $ Girl.Eyes = "down"
                                    ch_j "Мило. . ."
                                    $ Girl.Statup("Love", 90, 3)
                                    $ Girl.Statup("Obed", 80, 2)
                            elif Girl is StormX:
                                    ch_s ". . ."
                                    $ Girl.Statup("Inbt", 60, 5)
                            elif Girl is JubesX:
                                    $ Girl.FaceChange("sly",1, Eyes="down")
                                    ch_v "Приветик. . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Love", 80, 1)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 2)
                            elif Girl is GwenX:
                                    $ Girl.FaceChange("sly",1, Eyes="down")
                                    ch_g "Думаю, я могу привыкнуть к нему."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 1)
                            elif Girl is BetsyX:
                                    $ Girl.FaceChange("sly",1, Eyes="down")
                                    ch_b "Он никогда не перестает впечатлять. . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 1)
                            elif Girl is DoreenX:
                                    $ Girl.FaceChange("sly",1, Eyes="down")
                                    ch_d "Я думаю, он начинает мне нравиться."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 1)
                            elif Girl is WandaX:
                                    $ Girl.FaceChange("sly",1, Eyes="down")
                                    ch_w "Мммм. . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Inbt", 80, 4)
                    elif Girl.SeenPeen == 10:
                            if Girl is RogueX:
                                    ch_r "Он мне никогда не надоест."
                                    $ Girl.Statup("Love", 90, 10)
                            elif Girl is KittyX:
                                    ch_k "Такой красивый."
                                    $ Girl.Statup("Obed", 80, 10)
                                    $ Girl.Statup("Inbt", 60, 3)
                            elif Girl is EmmaX:
                                    $ Girl.Eyes = "down"
                                    ch_e "Я ценю некоторые твои \"особенности\"."
                                    $ Girl.Statup("Obed", 80, 5)
                                    $ Girl.Statup("Inbt", 60, 10)
                            elif Girl is LauraX:
                                    $ Girl.Eyes = "down"
                                    ch_l "Я никогда не устану от его вида."
                                    $ Girl.Statup("Obed", 80, 8)
                                    $ Girl.Statup("Inbt", 60, 7)
                            elif Girl is JeanX:
                                    $ Girl.Eyes = "down"
                                    ch_j "Спасибо. . ."
                                    $ Girl.Statup("Love", 90, 10)
                                    $ Girl.Statup("Obed", 80, 8)
                            elif Girl is StormX:
                                    $ Girl.Eyes = "down"
                                    ch_s "Что ж, мне он очень нравится."
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Love", 90, 5)
                                    $ Girl.Statup("Inbt", 60, 2)
                            elif Girl is JubesX:
                                    $ Girl.FaceChange("confused",1, Eyes="down")
                                    ch_v "Так. . . завораживает. . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Love", 80, 1)
                                    $ Girl.Statup("Obed", 80, 3)
                                    $ Girl.Statup("Inbt", 60, 2)
                            elif Girl is GwenX:
                                    $ Girl.FaceChange("smile",1)
                                    ch_g ". . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 1)
                            elif Girl is BetsyX:
                                    $ Girl.FaceChange("smile",1)
                                    ch_b ". . . просто великолепно."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 1)
                            elif Girl is DoreenX:
                                    $ Girl.FaceChange("smile",1)
                                    ch_d "Хорошо, я в деле. . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 1)
                            elif Girl is WandaX:
                                    $ Girl.FaceChange("sly",1, Eyes="down")
                                    ch_w "С удовольсвием полюбуюсь видами. . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Love", 90, 5)
                                    $ Girl.Statup("Inbt", 60, 5)
                    $ Girl.Eyes = "sexy"
                    $ React = 1
            elif bg_current == "bg showerroom":
                    #you're in the shower so she should not react seriously.
                    $ Girl.Eyes = "down"
                    call AnyLine(Girl,". . .")
                    $ Girl.Eyes = "normal"
                    $ Silent = 1
            else:
                    #she doesn't like it much
                    $ Girl.FaceChange("sad",1)
                    if Girl.SeenPeen == 1:
                            $ Girl.FaceChange("perplexed",1 )
                            $ Girl.Eyes = "down"
                            if Girl is RogueX:
                                    ch_r "Ох, впечатляет. И что ты планируешь с ним делать?"
                                    $ Girl.Statup("Obed", 50, 5)
                                    $ Girl.Statup("Inbt", 60, 5)
                            elif Girl is KittyX:
                                    ch_k "Ну вот это и произошло. . ."
                            elif Girl is EmmaX:
                                    ch_e "Ты в курсе, что у тебя член торчит?"
                                    $ Girl.Statup("Obed", 50, 2)
                            elif Girl is LauraX:
                                    ch_l "У тебя член торчит."
                                    $ Girl.Statup("Inbt", 60, 2)
                            elif Girl is JeanX:
                                    ch_j "Эй, у тебя член торчит."
                                    $ Girl.Statup("Obed", 80, 4)
                                    $ Girl.Statup("Inbt", 70, 4)
                            elif Girl is StormX:
                                    ch_s "Видимо, тебе тоже нравится приятный ветерок. . ."
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Inbt", 60, 5)
                            elif Girl is JubesX:
                                    ch_v "Хмм, ладно. . ."
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 2)
                            elif Girl is GwenX:
                                    ch_g "Серьезно, неужели никто больше этого не видит?!"
                                    $ Girl.Statup("Obed", 80, 3)
                                    $ Girl.Statup("Inbt", 60, 2)
                            elif Girl is BetsyX:
                                    ch_b "Это совсем неуместно."
                                    $ Girl.Statup("Obed", 80, 3)
                                    $ Girl.Statup("Inbt", 60, 2)
                            elif Girl is DoreenX:
                                    ch_d "Существуют правила, запрещающие такое!"
                                    $ Girl.Statup("Obed", 80, 3)
                                    $ Girl.Statup("Inbt", 60, 2)
                            elif Girl is WandaX:
                                    ch_w "Старайся, чтобы его не было видно. . ."
                                    $ Girl.Statup("Obed", 80, 3)
                                    $ Girl.Statup("Inbt", 60, 2)
                            $ Girl.Statup("Obed", 50, 5)
                            $ Girl.Statup("Inbt", 60, 5)
                    elif Girl.SeenPeen < 5:
                            $ Girl.FaceChange("sad",0)
                            if Girl is RogueX:
                                    ch_r "Да, я уже его видела."
                            elif Girl is KittyX:
                                    ch_k "Хм."
                            elif Girl is EmmaX:
                                    ch_e "Полагаю, тебе не стоит им размахивать, [Girl.Petname]."
                            elif Girl is LauraX:
                                    ch_l "Эй. . ."
                                    ch_l "Пожалуй, тебе не стоит им размахивать, [Girl.Petname]."
                            elif Girl is JeanX:
                                    ch_j "Я уже его видела."
                            elif Girl is StormX:
                                    ch_s ". . ."
                            elif Girl is JubesX:
                                    ch_v "Он здесь. . . не к месту. . ."
                                    $ Girl.Statup("Obed", 80, 2)
                            elif Girl is GwenX:
                                    ch_g "Угум. . ."
                                    $ Girl.Statup("Obed", 80, 2)
                            elif Girl is BetsyX:
                                    ch_b "Я -уже- видела его."
                            elif Girl is DoreenX:
                                    ch_d "Я уже его видела!"
                            elif Girl is WandaX:
                                    ch_w "Ага, ага. . ."
                            $ Girl.Statup("Inbt", 60, 2)
                    elif Girl.SeenPeen == 10:
                            if Girl is RogueX:
                                    ch_r "Мне уже надоело на него смотреть."
                                    $ Girl.Statup("Obed", 50, 5)
                                    $ Girl.Statup("Inbt", 60, 5)
                            elif Girl is KittyX:
                                    ch_k "[Girl.Like]убери его."
                                    $ Girl.Statup("Obed", 50, 7)
                                    $ Girl.Statup("Inbt", 60, 3)
                            elif Girl is EmmaX:
                                    ch_e "Да, мы уже все на него насмотрелись."
                                    $ Girl.Statup("Obed", 50, 7)
                                    $ Girl.Statup("Inbt", 60, 5)
                            elif Girl is LauraX:
                                    ch_l "Да - да, снова размахиваешь своим членом."
                                    $ Girl.Statup("Obed", 50, 8)
                                    $ Girl.Statup("Inbt", 60, 4)
                            elif Girl is JeanX:
                                    ch_j "О, Пенис. Как оригинально."
                                    $ Girl.Statup("Obed", 50, 8)
                                    $ Girl.Statup("Inbt", 60, 4)
                            elif Girl is StormX:
                                    ch_s ". . ."
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Obed", 50, 2)
                                    $ Girl.Statup("Inbt", 60, 4)
                            elif Girl is JubesX:
                                    ch_v ". . ."
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 2)
                            elif Girl is GwenX:
                                    ch_g ". . ."
                                    $ Girl.Statup("Obed", 80, 4)
                                    $ Girl.Statup("Inbt", 60, 2)
                            elif Girl is BetsyX:
                                    ch_b ". . ."
                                    $ Girl.Statup("Obed", 80, 4)
                                    $ Girl.Statup("Inbt", 60, 2)
                            elif Girl is DoreenX:
                                    ch_d "Хмм, ну. . ."
                                    $ Girl.Statup("Obed", 80, 4)
                                    $ Girl.Statup("Inbt", 60, 2)
                            elif Girl is WandaX:
                                    ch_w "А вот и ты. . . снова. . ."
                                    $ Girl.Statup("Obed", 80, 5)
                                    $ Girl.Statup("Inbt", 60, 3)
                    $ Girl.Eyes = "sexy"
                    $ React = 2
        if Silent:
                    #Silent mode
                    $ Player.RecentActions.append("cockout")
                    if Girl.SeenPeen > 10:
                        return
                    elif ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "L"):
                            if Girl.SeenPeen == 1:
                                $ Girl.Statup("Love", 90, 5)
                            elif Girl.SeenPeen == 2:
                                $ Girl.Statup("Obed", 50, 5)
                            elif Girl.SeenPeen == 5:
                                $ Girl.Statup("Inbt", 60, 5)
                            elif Girl.SeenPeen == 10:
                                $ Girl.Statup("Love", 90, 10)
                    else:
                            if Girl.SeenPeen == 1:
                                $ Girl.Statup("Obed", 50, 5)
                                $ Girl.Statup("Inbt", 60, 5)
                                $ Girl.AddWord(1,0,0,0,"seenpeen") #$ Girl.History.append("seenpeen")
                            elif Girl.SeenPeen < 5:
                                $ Girl.Statup("Inbt", 60, 2)
                            elif Girl.SeenPeen == 10:
                                $ Girl.Statup("Obed", 50, 5)
                                $ Girl.Statup("Inbt", 60, 5)
                    if Girl is JubesX:
                            $ Girl.Statup("Obed", 80, 1)
        if Girl.SeenPeen == 1:
                if Girl is JeanX:
                        $ Girl.Statup("Love", 90, 10)
                        $ Girl.Statup("Obed", 30, 20)
                        $ Girl.Statup("Obed", 50, 10)
                        $ Girl.Statup("Obed", 80, 5)
                elif Girl is JubesX:
                        $ Girl.Statup("Obed", 80, 3)
                $ Girl.Statup("Love", 90, 15)
                $ Girl.Statup("Obed", 90, 20,Alt=[[StormX],90,0])
                $ Girl.Statup("Inbt", 60, 20)
                $ Girl.Statup("Lust", 200, 5)
        $ Girl.FaceChange("sly",1)
        return React

# End Seen Peen / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Girl_First_Puss(Girl = 0, Silent = 0, Undress = 0, Second = 0, React = 0):  #rkeljsvgb
        #checked each time she sees your pussy  ## call Girl_First_Puss(RogueX,0,1)
        #if Silent it doesn't say anything
        #if Undress then you get nude
        #if Secondary then this is the second girl to see it.
        # React 0 if other girl didn't comment,
        # 1 = if the other girl commented, 2 = didn't like it
        # Strapped is a passed variable that causes you to put your strapon on, mainly from sex actions

        if Girl.Loc != bg_current:
                    if Partner == Girl:
                            $ Partner = 0
                    return
        if "cockout" in Player.RecentActions and "peen" in Girl.RecentActions:
                    #If the cock is already out and she's seen it, return
#                    if Strapped and "strapon" not in Player.RecentActions:
#                            "You whip out your rubber strap-on."
#                            $ Player.AddWord(1,"strapon",0,0,0) #Recent
                    return

        if "unseen" in Girl.RecentActions:
                    #if she hasn't noticed you, she won't notice this, yet.
                    return

        $ Girl.RecentActions.append("peen")
        $ Girl.DailyActions.append("peen")
        $ Girl.SeenPuss += 1
        $ Girl.Statup("Inbt", 30, 2)
        $ Girl.Statup("Inbt", 80, 1)

        if Second:
                #If another girl commented on it first. . .
                if Girl.SeenPuss == 1:
                                $ Girl.FaceChange("surprised", 2)
                                if Girl is RogueX:
                                        ch_r "Ага, она очень милая. . ."
                                elif Girl is KittyX:
                                        ch_k "О, ты не шутишь. . ."
                                elif Girl is EmmaX:
                                        $ Girl.FaceChange("sly", 2, Eyes = "down")
                                        ch_e "Боже, какая привлекательная маленькая киска. . ."
                                elif Girl is LauraX:
                                        $ Girl.FaceChange("sly", 2, Eyes = "down")
                                        ch_l "Хм, а у тебя там все впорядке. . ."
                                elif Girl is JeanX:
                                        $ Girl.FaceChange("sly", 2, Eyes = "down")
                                        ch_j "Ага, хорошо выглядит. . ."
                                elif Girl is StormX:
                                        $ Girl.FaceChange("sly", 2, Eyes = "down")
                                        ch_s "Да, она прекрасна. . ."
                                elif Girl is JubesX:
                                        $ Girl.FaceChange("sly", 2, Eyes = "down")
                                        ch_v "Ох, ого, ага. . ."
                                elif Girl is GwenX:
                                        $ Girl.FaceChange("sly",1, Eyes="down")
                                        ch_g "Она такая красивая. . ."
                                elif Girl is BetsyX:
                                        $ Girl.FaceChange("sly",1, Eyes="down")
                                        ch_b "Да, она очень милая. . ."
                                elif Girl is DoreenX:
                                        $ Girl.FaceChange("sly",1, Eyes="down")
                                        ch_d "Ладно, ага. . ."
                                elif Girl is WandaX:
                                        $ Girl.FaceChange("sly",1, Eyes="down")
                                        ch_w "Она очень милая. . ."
                                $ Girl.FaceChange("bemused", 1)
                elif Second == 1:
                        # The other girl liked it
                        if not ApprovalCheck(Girl, 800) and not ApprovalCheck(Girl, 500, "I"):
                                $ Girl.FaceChange("sad", 1)
                                if Girl is RogueX:
                                        ch_r "Если ты увлекаешься подобными. . ."
                                elif Girl is KittyX:
                                        ch_k "Эм. . ."
                                elif Girl is EmmaX:
                                        ch_e "Полагаю, у тебя не так уж много опыта. . ."
                                elif Girl is LauraX:
                                        ch_l "Хм . ."
                                elif Girl is JeanX:
                                        ch_j "Ага, все нормально. . ."
                                elif Girl is StormX:
                                        ch_s "Интересно. . ."
                                elif Girl is JubesX:
                                        ch_v "Хм. . ."
                                elif Girl is GwenX:
                                        ch_g "Может быть. . ."
                                elif Girl is BetsyX:
                                        ch_b "Хммм. . ."
                                elif Girl is DoreenX:
                                        ch_d "Эм. . ."
                                elif Girl is WandaX:
                                        ch_w "Серьезно?"
                        else:
                                $ Girl.FaceChange("bemused", 1)
                                if Girl is RogueX:
                                        ch_r "Да, она настоящее сокровище. . ."
                                elif Girl is KittyX:
                                        ch_k "Я знаю?!"
                                elif Girl is EmmaX:
                                        ch_e "Да, меня она тоже совершенно обезоружила. . ."
                                elif Girl is LauraX:
                                        ch_l "Да, она милая. . ."
                                elif Girl is JeanX:
                                        ch_j "Почти так же хороша, как и моя. . ."
                                elif Girl is StormX:
                                        ch_s "Я тоже так подумала."
                                elif Girl is JubesX:
                                        ch_v "Ага?"
                                elif Girl is GwenX:
                                        ch_g "Ага, впечатляет."
                                elif Girl is BetsyX:
                                        ch_b "Я абсолютно согласна. . ."
                                elif Girl is DoreenX:
                                        ch_d "Наверное. . ."
                                elif Girl is WandaX:
                                        ch_w "Она определенно милая. . ."
                elif Second == 2:
                        # The other girl didn't like it
                        if not ApprovalCheck(Girl, 800) and not ApprovalCheck(Girl, 500, "I"):
                                $ Girl.FaceChange("sad", 1)
                                if Girl is RogueX:
                                        ch_r "Ага, как скажешь. . ."
                                elif Girl is KittyX:
                                        ch_k "Эм. . ."
                                elif Girl is EmmaX:
                                        ch_e "Ты неплохо разбираешься в этом. . ."
                                elif Girl is LauraX:
                                        ch_l "Наверное. . ."
                                elif Girl is JeanX:
                                        ch_j "Ага. . ."
                                elif Girl is StormX:
                                        ch_s "Верно. . ."
                                elif Girl is JubesX:
                                        ch_v "Наверное. . ."
                                elif Girl is GwenX:
                                        ch_g "Может быть. . ."
                                elif Girl is BetsyX:
                                        ch_b "Пожалуй. . ."
                                elif Girl is DoreenX:
                                        ch_d "Наверное. . ."
                                elif Girl is WandaX:
                                        ch_w "Ну. . ."
                        else:
                                $ Girl.FaceChange("confused", 1)
                                if Girl is RogueX:
                                        ch_r "Ну а мне она нравится. . ."
                                        $ Girl.FaceChange("sexy", 1)
                                elif Girl is KittyX:
                                        ch_k "Да ладно тебе, она очень милая!"
                                        $ Girl.FaceChange("smile", 1)
                                elif Girl is EmmaX:
                                        ch_e "Ты просто не можешь оценить прекрасное. . ."
                                        $ Girl.FaceChange("sly",0)
                                elif Girl is LauraX:
                                        ch_l "Оу, да ладно тебе, она не так уж и плоха. . ."
                                        $ Girl.FaceChange("sly",0)
                                elif Girl is JeanX:
                                        ch_j "Конечно, она не так хороша, как моя, но все же. . ."
                                        $ Girl.FaceChange("sly",0)
                                elif Girl is StormX:
                                        ch_s "Это далеко не худшее, что я видела. . ."
                                        $ Girl.FaceChange("sly",0)
                                elif Girl is JubesX:
                                        ch_v "А мне понравилась. . ."
                                        $ Girl.FaceChange("sly",0)
                                elif Girl is GwenX:
                                        ch_g "Ну, если у тебя нет вкуса. . ."
                                        $ Girl.FaceChange("sly",0)
                                elif Girl is BetsyX:
                                        ch_b "Я не могу сказать, что согласна с тобой. . ."
                                        $ Girl.FaceChange("sly",0)
                                elif Girl is DoreenX:
                                        ch_d "Я думаю, она выглядит мило. . ."
                                        $ Girl.FaceChange("sly",1)
                                elif Girl is WandaX:
                                        ch_w "Ты так думаешь?"
                                        $ Girl.FaceChange("sly",1)
                $ Silent = 1

        if Undress:
                    $ Player.AddWord(1,"naked")
        if not Silent:
            if "cockout" in Player.RecentActions:
                    $ Girl.FaceChange("down", 2)
                    "[Girl.Name] бросает взгляд на вашу обнаженную киску."
                    $ Girl.FaceChange("sly",1)
            elif React:
                    #If called by a sex dialog
                    "[Girl.Name] тянется к вашим штанам и обнажает вашу киску."
            elif Undress:
                    "Вы полностью раздеваетесь."
            else:
                    "Вы обнажаете свою киску."
            $ Player.AddWord(1,"cockout")
            if "girltalk" not in Girl.History and bg_current == "bg showerroom":
                $ Silent = 1
            elif not Girl.Forced and not React and Taboo > 20 and (not ApprovalCheck(Girl, 1500) or Girl.SEXP < 10) and bg_current != "bg showerroom" and Girl not in (JeanX,StormX):
                #if it's a semi-public space that isn't the showers, and she is not down with this. . .
                if not ApprovalCheck(Girl, 800) and not ApprovalCheck(Girl, 500, "I"):
                        #If the girl is very not into it. . .
                        if Girl is EmmaX and ("detention" in Girl.RecentActions or "classcaught" in Girl.RecentActions):
                            #special exceptions for detention and classcaught events
                            $ Girl.FaceChange("confused", Eyes="down")
                            ch_e "Ммм?"
                            $ Girl.FaceChange("surprised", Eyes="squint")
                            if Girl.SeenPuss == 1:
                                    $ Girl.Statup("Love", 30, 5)
                                    $ Girl.Statup("Love", 90, 5)
                                    $ Girl.Statup("Obed", 50, 20)
                                    $ Girl.Statup("Inbt", 60, 30)
                            else:
                                    $ Girl.Statup("Love", 90, 2)
                                    $ Girl.Statup("Obed", 50, 3)
                                    $ Girl.Statup("Inbt", 60, 5)
                            ch_e "Что ж, полагаю, в таком случае я могу сделать исключение."
                            $ React = 1
                        else:
                            #If the girl is very not into it. . .
                            $ Girl.FaceChange("surprised", 2)
                            if Girl is RogueX:
                                    ch_r "А?"
                            elif Girl is KittyX:
                                    ch_k "А?!"
                            elif Girl is EmmaX:
                                    $ Girl.Eyes = "down"
                                    ch_e "Ммм?"
                            elif Girl is LauraX:
                                    $ Girl.Eyes = "down"
                                    ch_l "Ммм?"
                            elif Girl is JubesX:
                                    $ Girl.Eyes = "down"
                                    ch_v "Эй. . ."
                                    $ Girl.Eyes = "squint"
                                    ch_v "Что это значит?"
                            elif Girl is GwenX:
                                    $ Girl.Eyes = "down"
                                    ch_g "Значит. . . хвастаешься?"
                            elif Girl is BetsyX:
                                    ch_b ". . . Что ты делаешь, [BetsyX.Petname]?"
                            elif Girl is DoreenX:
                                    ch_d "Воу, что ты делаешь?"
                            elif Girl is WandaX:
                                    ch_w "Что ты делаешь? . ."
                            if "nogirls" in Girl.History:
                                    $ Girl.FaceChange("angry", 1)
                                    $ Girl.RecentActions.append("angry")
                                    $ Girl.DailyActions.append("angry")
                            $ React = 2
                            if Girl.SeenPuss == 1:
                                        $ Girl.Statup("Love", 90, -20)
                                        $ Girl.Statup("Obed", 50, 30)
                                        $ Girl.Statup("Inbt", 60, 20)
                            else:
                                #if this is the second time you've done this today. . .
                                if Girl is RogueX:
                                        ch_r "Что с тобой -не так- ?"
                                elif Girl is KittyX:
                                        ch_k "Подруга, да у тебя проблемы, серьезно!"
                                elif Girl is EmmaX:
                                        ch_e "[Girl.Petname]! Нам придется поработать. . . над твоей проблемой."
                                elif Girl is LauraX:
                                        ch_l "Подруга, это не клево."
                                elif Girl is JubesX:
                                        ch_v "Держи ее в штанах. . ."
                                elif Girl is GwenX:
                                        ch_g "Ты. . . постоянно так делаешь?"
                                elif Girl is BetsyX:
                                        ch_b "Это. . . нормально поведение в штатах? . ."
                                elif Girl is DoreenX:
                                        ch_d "Не стягивай штаны!"
                                elif Girl is WandaX:
                                        ch_w "Эй, эй, эй, не выставляй ее напоказ. . ."
                                if Girl.DailyActions.count("puss") >= 2:
                                        #if she's seen more than one peen today
                                        $ Girl.Statup("Love", 90, -1)
                                        $ Girl.Statup("Obed", 50, 1)
                                        $ Girl.Statup("Inbt", 60, 2)
                                else:
                                        $ Girl.Statup("Love", 90, -5)
                                        $ Girl.Statup("Obed", 50, 10)
                                        $ Girl.Statup("Inbt", 60, 10)
                            $ Girl.Eyes = "sexy"
                #end if bg_current != "bg showerroom" and not ApprovalCheck(Girl, 800) and not ApprovalCheck(Girl, 500, "I"):
                else:
                            #if ApprovalCheck is 800-1500 and not ApprovalCheck(Girl, 500, "I"):
                            $ Girl.FaceChange("surprised", 2)
                            if Girl is RogueX:
                                    ch_r "Тебе не следует обнажать ее!"
                            elif Girl is KittyX:
                                    ch_k "Эм, тебе не следует[Girl.like]обнажать ее на людях."
                            elif Girl is EmmaX:
                                    ch_e "Аккуратнее с этим."
                            elif Girl is LauraX:
                                    ch_l "Я думаю, что для подобных вещей должно быть свое время и место."
                            elif Girl is JubesX:
                                    ch_v "Эм, тебе не кажется, что не стоит показывать ее всем?"
                            elif Girl is GwenX:
                                    ch_g "Боже, не снимай свои штаны!"
                            elif Girl is BetsyX:
                                    ch_b "Сохраняй хоть немного достоинства!"
                            elif Girl is DoreenX:
                                    ch_d "Не снимай свои штаны!"
                            elif Girl is WandaX:
                                    ch_w "Эй, эй, эй, не выставляй ее напоказ. . ."
                            $ Girl.FaceChange("bemused", 1)
                            if Girl.SeenPuss == 1:
                                    if Girl is RogueX:
                                            ch_r "То есть. . . нет, спрячь ее!"
                                    elif Girl is KittyX:
                                            ch_k "Или[Girl.like]может быть. . ."
                                    elif Girl is EmmaX:
                                            $ Girl.Eyes = "down"
                                            ch_e ". . . какой бы очаровательной она ни была. . ."
                                    elif Girl is LauraX:
                                            ch_l ". . . не то чтобы я сама была против. . ."
                                    elif Girl is JubesX:
                                            ch_v "Или. . . нет. . ."
                                    elif Girl is GwenX:
                                            ch_g "Знаешь. . . если ты хочешь. . ."
                                    elif Girl is BetsyX:
                                            ch_b ". . . хотя. . ."
                                    elif Girl is DoreenX:
                                            ch_d "Хммм. . ."
                                    elif Girl is WandaX:
                                            ch_w "Но, знаешь, неплохо. . ."
                                    $ Girl.Statup("Love", 90, 20)
                                    $ Girl.Statup("Obed", 50, 20)
                                    $ Girl.Statup("Inbt", 60, 30)
                            $ Girl.Eyes = "sexy"
                            $ React = 2

                #end if not Girl.Forced and not React and Taboo > 20 and (not ApprovalCheck(Girl, 1500) or Girl.SEXP < 10) and bg_current != "bg showerroom" and Girl != JeanX:
            elif Girl.SeenPuss > 10:
                        #if it's been more than 10 times, return
                        return 0
            elif ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "L"):
                    #She basically likes it
                    $ Girl.FaceChange("sly",1)
                    if Girl.SeenPuss == 1:
                            $ Girl.FaceChange("surprised",2)
                            if Girl is RogueX:
                                    ch_r "У тебя, эм, она тоже симпатичная. . ."
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Love", 90, 5)
                            elif Girl is KittyX:
                                    $ Girl.FaceChange("surprised",2)
                                    ch_k "Она. . . милая."
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Love", 90, 3)
                            elif Girl is EmmaX:
                                    $ Girl.FaceChange("surprised",1, Eyes="down")
                                    ch_e "Весьма неплохо. . ."
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Love", 50, 5)
                                    $ Girl.Statup("Love", 90, 5)
                            elif Girl is LauraX:
                                    $ Girl.FaceChange("surprised",1, Eyes="down")
                                    ch_l "Хм, она очень милая. . ."
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Love", 50, 5)
                                    $ Girl.Statup("Love", 90, 5)
                            elif Girl is JeanX:
                                    $ Girl.FaceChange("confused",1, Eyes="down",Mouth="smile")
                                    ch_j "Ну и что у нас тут. . ."
                                    $ Girl.FaceChange("bemused",1)
                                    ch_j "У нас тут все очень хорошо, [Girl.Petname]."
                                    $ Girl.Statup("Love", 50, 5)
                                    $ Girl.Statup("Love", 90, 5)
                                    $ Girl.Statup("Obed", 80, 3)
                            elif Girl is StormX:
                                    $ Girl.FaceChange("confused",1, Eyes="down")
                                    ch_s "Хмм. . . очень милая."
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Love", 50, 2)
                                    $ Girl.Statup("Love", 90, 3)
                                    $ Girl.Statup("Inbt", 60, 2)
                            elif Girl is JubesX:
                                    $ Girl.FaceChange("surprised",2, Eyes="down")
                                    ch_v "Ох. . . милая."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Love", 80, 3)
                                    $ Girl.Statup("Obed", 80, 1)
                                    $ Girl.Statup("Inbt", 60, 4)
                            elif Girl is GwenX:
                                    $ Girl.FaceChange("surprised",2, Eyes="down")
                                    ch_g "Ладно, сейчас посмотрим, что там у тебя. . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Love", 80, 3)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 4)
                            elif Girl is BetsyX:
                                    $ Girl.FaceChange("surprised",2, Eyes="down")
                                    ch_b "Она прекрасна, да. . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Love", 80, 3)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 4)
                            elif Girl is DoreenX:
                                    $ Girl.FaceChange("surprised",2, Eyes="down")
                                    ch_d "Ох, милая. . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Love", 80, 3)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 4)
                            elif Girl is WandaX:
                                    $ Girl.FaceChange("surprised",2, Eyes="down")
                                    ch_w "Вау. . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Love", 80, 3)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 4)
                    elif Girl.SeenPuss == 5:
                            if Girl is RogueX:
                                    ch_r "Она начинает мне нравиться."
                                    $ Girl.Statup("Inbt", 60, 5)
                            elif Girl is KittyX:
                                    ch_k "А вот и она."
                                    $ Girl.Statup("Inbt", 60, 5)
                            elif Girl is EmmaX:
                                    ch_e "Да, мы раньше и виделись с ней."
                                    $ Girl.Statup("Obed", 60, 7)
                            elif Girl is LauraX:
                                    ch_l "Да, я видела ее."
                                    $ Girl.Statup("Obed", 60, 4)
                                    $ Girl.Statup("Inbt", 60, 3)
                            elif Girl is JeanX:
                                    $ Girl.Eyes = "down"
                                    ch_j "Милая. . ."
                                    $ Girl.Statup("Love", 90, 3)
                                    $ Girl.Statup("Obed", 80, 2)
                            elif Girl is StormX:
                                    ch_s ". . ."
                                    $ Girl.Statup("Inbt", 60, 5)
                            elif Girl is JubesX:
                                    $ Girl.FaceChange("sly",1, Eyes="down")
                                    ch_v "Ну привет. . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Love", 80, 1)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 2)
                            elif Girl is GwenX:
                                    $ Girl.FaceChange("surprised",2, Eyes="down")
                                    ch_g "Думаю, я смогу к этому привыкнуть. . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Love", 80, 3)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 4)
                            elif Girl is BetsyX:
                                    $ Girl.FaceChange("surprised",2, Eyes="down")
                                    ch_b "Здравствуй. . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Love", 80, 3)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 4)
                            elif Girl is DoreenX:
                                    $ Girl.FaceChange("surprised",2, Eyes="down")
                                    ch_d "Ох. . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Love", 80, 3)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 4)
                            elif Girl is WandaX:
                                    $ Girl.FaceChange("surprised",1, Eyes="down")
                                    ch_w "Ну привет. . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Love", 80, 3)
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 4)
                    $ Girl.Eyes = "sexy"
                    $ React = 1
            elif bg_current == "bg showerroom":
                    #you're in the shower so she should not react seriously.
                    $ Girl.Eyes = "down"
                    call AnyLine(Girl,". . .")
                    $ Girl.Eyes = "normal"
                    $ Silent = 1
            else:
                    #she doesn't like it much
                    $ Girl.FaceChange("sad",1)
                    if Girl.SeenPuss == 1:
                            $ Girl.FaceChange("perplexed",1 )
                            $ Girl.Eyes = "down"
                            if Girl is RogueX:
                                    ch_r "Зачем ты показываешь ее мне?"
                                    $ Girl.Statup("Obed", 50, 5)
                                    $ Girl.Statup("Inbt", 60, 5)
                            elif Girl is KittyX:
                                    ch_k "Ну, это произошло. . ."
                            elif Girl is EmmaX:
                                    ch_e "Ты знаешь, что у тебя есть своя киска?"
                                    $ Girl.Statup("Obed", 50, 2)
                            elif Girl is LauraX:
                                    ch_l "Почему ты обнажила свою киску?"
                                    $ Girl.Statup("Inbt", 60, 2)
                            elif Girl is JeanX:
                                    ch_j "Эй, мне кажется, ты что-то забыла."
                                    $ Girl.Statup("Obed", 80, 4)
                                    $ Girl.Statup("Inbt", 70, 4)
                            elif Girl is StormX:
                                    ch_s "Судя по всему, тебе тоже нравится приятный ветерок там. . ."
                                    $ Girl.FaceChange("bemused",1)
                                    $ Girl.Statup("Inbt", 60, 5)
                            elif Girl is JubesX:
                                    ch_v "Хмм, ладно. . ."
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 2)
                            elif Girl is GwenX:
                                    ch_g "Ну ладно. . ."
                                    $ Girl.Statup("Obed", 80, 1)
                                    $ Girl.Statup("Inbt", 60, 4)
                            elif Girl is BetsyX:
                                    ch_b "Пожалуйста, держи себя в руках. . ."
                                    $ Girl.Statup("Obed", 80, 1)
                                    $ Girl.Statup("Inbt", 60, 4)
                            elif Girl is DoreenX:
                                    ch_d "Спрячь ее. . ."
                                    $ Girl.FaceChange("sly",1)
                                    $ Girl.Statup("Obed", 80, 1)
                                    $ Girl.Statup("Inbt", 60, 4)
                            elif Girl is WandaX:
                                    ch_w "Да ладно тебе. . ."
                                    $ Girl.Statup("Obed", 80, 2)
                                    $ Girl.Statup("Inbt", 60, 5)
                            $ Girl.Statup("Obed", 50, 5)
                            $ Girl.Statup("Inbt", 60, 5)
                    elif Girl.SeenPuss < 5:
                            $ Girl.FaceChange("sad",0)
                            if Girl is RogueX:
                                    ch_r "Да, я видела ее."
                            elif Girl is KittyX:
                                    ch_k "Хм."
                            elif Girl is EmmaX:
                                    ch_e "Мне кажется, [Girl.Petname], тебе лучше спрятать ее."
                            elif Girl is LauraX:
                                    ch_l "Эй. . ."
                                    ch_l "[Girl.Petname], тебе лучше ее спрятать."
                            elif Girl is JeanX:
                                    ch_j "Я уже видела ее."
                            elif Girl is StormX:
                                    ch_s ". . ."
                            elif Girl is JubesX:
                                    ch_v "Это. . . неуместно. . ."
                                    $ Girl.Statup("Obed", 80, 2)
                            elif Girl is GwenX:
                                    ch_g "Не переходи границы. . ."
                                    $ Girl.Statup("Obed", 80, 1)
                            elif Girl is BetsyX:
                                    ch_b "Я прошу сохранять достоинство, это не так уж и сложно. . ."
                            elif Girl is DoreenX:
                                    ch_d "Да ладно тебе. . ."
                            elif Girl is WandaX:
                                    $ Girl.Statup("Obed", 80, 1)
                                    $ Girl.Statup("Inbt", 70, 1)
                                    ch_w "Ладно, ладно, мы поняли. . ."
                            $ Girl.Statup("Inbt", 60, 2)
                    $ Girl.Eyes = "sexy"
                    $ React = 2
        if Silent:
                    #Silent mode
                    $ Player.RecentActions.append("cockout")
                    if Girl.SeenPuss > 10:
                        return
                    elif ApprovalCheck(Girl, 1200) or ApprovalCheck(Girl, 500, "L"):
                            if Girl.SeenPuss == 1:
                                $ Girl.Statup("Love", 90, 5)
                            elif Girl.SeenPuss == 2:
                                $ Girl.Statup("Obed", 50, 5)
                            elif Girl.SeenPuss == 5:
                                $ Girl.Statup("Inbt", 60, 5)
                            elif Girl.SeenPuss == 10:
                                $ Girl.Statup("Love", 90, 5)
                    else:
                            if Girl.SeenPuss == 1:
                                $ Girl.Statup("Obed", 50, 5)
                                $ Girl.Statup("Inbt", 60, 5)
                                $ Girl.AddWord(1,0,0,0,"seenpuss") #$ Girl.History.append("seenpeen")
                            elif Girl.SeenPuss < 5:
                                $ Girl.Statup("Inbt", 60, 2)
                            elif Girl.SeenPuss == 10:
                                $ Girl.Statup("Obed", 50, 5)
                                $ Girl.Statup("Inbt", 60, 5)
#                    if Girl is JubesX:
#                                $ Girl.Statup("Obed", 80, 1)
        if Girl.SeenPuss == 1:
                if Girl is JeanX:
                        $ Girl.Statup("Love", 90, 10)
                        $ Girl.Statup("Obed", 30, 10)
                        $ Girl.Statup("Obed", 80, 5)
                elif Girl is JubesX:
                        $ Girl.Statup("Obed", 80, 3)
                $ Girl.Statup("Love", 90, 10)
                $ Girl.Statup("Obed", 90, 10,Alt=[[StormX],90,0])
                $ Girl.Statup("Inbt", 60, 10)
                $ Girl.Statup("Lust", 200, 5)
        $ Girl.FaceChange("sly",1)
#        if Strapped and "strapon" not in Player.RecentActions:
#                "You whip out your rubber strap-on."
#                $ Player.AddWord(1,"strapon",0,0,0) #Recent
        return React

# End Seen Puss / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Zero_Strapped(Girl=0): #rkeljsvgb
        #adds strap-on if needed
        if not Player.Male and "strapon" not in Player.RecentActions:
                if Situation == Girl:
                        "[Girl.Name] достает свой резиновый член из сумки и надевает его на вас."
                else:
                        "Вы достаете свой резиновый член."
                $ Player.AddWord(1,"strapon",0,0,0) #Recent
                if "strapped" not in Girl.History:
                        $ Girl.Statup("Inbt", 80, 3)
                        $ Girl.Statup("Lust", 80, 3)
                        if Girl is RogueX:
                                ch_r "Ох! . . . Пожалуй ты уже со всем разобралась."
                        elif Girl is KittyX:
                                ch_k "Ну, я думаю, он пригодится."
                        elif Girl is EmmaX:
                                ch_e "Я не должна была сомневаться в тебе. . ."
                        elif Girl is LauraX:
                                ch_l "Ох, он пригодится. . ."
                        elif Girl is JeanX:
                                ch_j "Ну, наверное, он пригодится."
                        elif Girl is StormX:
                                ch_s "Ты, безусловно, находчива. . ."
                        elif Girl is JubesX:
                                ch_v "Ох! . . . я поняла."
                        elif Girl is GwenX:
                                ch_g "Похоже, инструмент у тебя всегда под рукой. . ."
                        elif Girl is BetsyX:
                                ch_b "Я вижу, ты хорошо подготовилась. . ."
                        elif Girl is DoreenX:
                                ch_d "Ох, -теперь- я все поняла. . ."
                        elif Girl is WandaX:
                                ch_w "Оооох. . ."
                                ch_w "Я должна была догадаться."
                        $ Girl.AddWord(1,0,0,0,"strapped") #Recent
        return

# End Seen Peen set / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start public sex check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girls_Taboo(Girl=0,Cnt= 1,Choice=0,D20=0):  #nee  Rogue_Taboo(Cnt= 1,Choice=0) #rkeljsvgb
        #Called by Sex_Dialog
        #Girl is the Primary actor, Cnt is a count of how many times you've been spotted,
        #Choice is how the girl is reacting, D20 is a randomizer
        #With Jean, Taboo should not be a factor if she can whammy people
        if Girl not in TotalGirls:
                $ Girl = Ch_Focus
        $ Player.AddWord(1,0,Girl.Tag) #$ Player.DailyActions.append(Girl.Tag)
        $ Player.AddWord(1,0,"scent") #$ Player.DailyActions.append("scent") Allows Laura to track you.

        if "uninterrupted" in Girl.RecentActions:
                return
        elif "MindFuck" in Player.RecentActions:
                return
        $ Cnt = Girl.RecentActions.count("spotted") if "spotted" in Girl.RecentActions else 1
        $ Cnt = 4 if Cnt > 4 else Cnt

        $ D20 = renpy.random.randint(1, 20)

        if bg_current == "bg dressing":
                call Girls_Noticed(Girl)
                if D20 > 18:
                        "Вы слышите стук в дверь примерочной."
                        $ Girl.FaceChange("surprised", 2)
                        ch_u "Эм, вы слишком. . . шумите?"
                        ch_u "Не могли бы вы. . . прекратить, пожалуйста?"
                        ch_u "Спасибо."
                        $ Girl.FaceChange("smile", 1,Brows="sad")
                        call AllReset(Girl)
                        if Partner:
                                call AllReset(Partner)
                        call Checkout
                        call Trig_Reset
                        "Вы с [Girl.Name_tvo] прекращаете то, чем занимались."
                        $ renpy.pop_call() #removes call to sex scene
                        $ renpy.pop_call() #fix, test for necessity.
                return

        if "screen" in Girl.Traits or (Partner and "screen" in Partner.Traits):
                #You've told Jean/Emma to screen Xavier's perceptions
                $ D20 += 8

        if D20 < 10:
                #if you're at the point where the girls would notice you. . .
                if Taboo > 20:
                        if (Trigger == "kiss you" and not Trigger2 and not Girl.Offhand):
                                #if it's very innocent, skip this part
                                pass
                        elif bg_current == "bg mall":
                                #Xavier ignores stuff at the mall
                                pass
                        elif Girl not in Rules:
                                #if Xavier is looking. . .
                                $ Girl.FaceChange("surprised", 1)
                                if Trigger == "blow" or Trigger == "hand" or Trigger == "titjob":
                                        "[Girl.Name] останавливается с испуганным видом."
                                else:
                                        "Вы начинаете ощущать легкий гул в голове и решаете остановиться."
                                ch_x "Немедленно прекратите! Живо ко мне в кабинет!"
                                call AllReset(Girl)
                                call Girls_Caught(Girl) #Rogue_Caught
                                return
                        else:
                                #if you've disabled Xavier's looking
                                ch_x "Хммм. . ."
                                $ Girl.Statup("Inbt", 90, 2)
                                $ Girl.Statup("Lust", 200, 3)
                if bg_current == "bg classroom" and EmmaX.Loc == "bg teacher" and Girl is not EmmaX:
                                #If you're in class and Emma's there as a teacher. . .
                                call Emma_Teacher_Caught(Girl)
                elif bg_current == "bg classroom" and StormX.Loc == "bg teacher" and Girl is not StormX:
                                #If you're in class and Storm's there as a teacher. . .
                                call Storm_Teacher_Caught(Girl)
                elif "interruption" in Player.RecentActions:
                                #skips locked door event if it's already happened lately.
                                pass
                elif D20 == 1 and AloneCheck(Girl) and Time_Count < 3:
                                #bad luck, a girl showed up out of nowhere. . .
                                $ Choice = ActiveGirls[:]
                                if Choice in ActiveGirls:
                                        $ Choice.remove(Girl)
                                $ renpy.random.shuffle(Choice)
                                $ Approval = 0
                                python:
                                    for BX in Choice:
                                        if BX.Loc != bg_current and "lockedout" not in Girl.Traits:
                                                Approval = BX
                                                break
                                if Approval:
                                        call Locked_Door(Approval,1,Girl)
                                # either this new girl will be allowed in and stay, or she will run away
                                $ Choice = 0
                                $ Approval = 0


                #now the girls get their turn to notice. . .
                call Girls_Noticed(Girl)
                if Nearby:
                        call Girls_Noticed_Nearby(Girl)

        if Taboo <= 20:
                #This is a private space with others around.
                call Girls_Noticed(Girl)
                return
        elif (Trigger == "kiss you" and not Trigger2 and not Girl.Offhand):
                #if it's very innocent, skip this part
                pass
        elif Cnt < 4:
                #if this has happened less than 4 times within the current cycle of events

                if Girl in (EmmaX,StormX) and "public" not in Girl.History:
                        $ Girl.History.append("public")

                if "spotted" not in Girl.RecentActions:
                        if bg_current == "bg mall":
                                "Несколько покупателей замечают вас с [Girl.Name_tvo]."
                        elif bg_current == "bg classroom":
                            if Nearby:
                                    $ BO = Nearby[:]
                                    while BO:
                                            $ BO[0].Facing = 0 #turns to look at you
                                            $ BO.remove(BO[0])
                            "Несколько студентов замечают вас с [Girl.Name_tvo]."
                        else:
                                "Несколько студентов замечают вас с [Girl.Name_tvo]."
                        $ Girl.Statup("Inbt", 200, 2)
                        $ Girl.Rep -= 2
                        $ Player.Rep -= 2
                elif Cnt < 3:
                        if bg_current == "bg mall":
                                "Еще несколько покупателей обращают свое внимание на вас с [Girl.Name_tvo]."
                        else:
                                "Еще несколько студентов обращают свое внимание на вас с [Girl.Name_tvo]."
                        $ Girl.Statup("Inbt", 200, 2)
                        $ Girl.Rep -= 1
                        $ Player.Rep -= 1
                elif Cnt == 3:
                        "У вас довольно много зрителей."
                        $ Girl.Statup("Inbt", 200, 3)
                        $ Girl.Rep -= 1
                        $ Player.Rep -= 1
                if Partner:
                        $ Partner.Rep -= 1


                if "exhibitionist" in Girl.Traits:
                        $ Girl.FaceChange("sexy", 0)
                        if "spotted" not in Girl.RecentActions:
                                if Girl is RogueX:
                                        ch_r "Пусть смотрят, [Girl.Petname]."
                                elif Girl is KittyX:
                                        ch_k "Думаю, можно устроить им достойное представление, [Girl.Petname]."
                                elif Girl is EmmaX:
                                        ch_e "Хм, возможно, они хоть чему-нибудь научатся, [Girl.Petname]."
                                elif Girl is LauraX:
                                        ch_l "Ну, давай дадим им то, чего они хотят."
                                elif Girl is JeanX:
                                        ch_j "Ну конечно они хотят поглазеть."
                                elif Girl is StormX:
                                        ch_s "Пусть они боготворят нас. . ."
                                elif Girl is JubesX:
                                        ch_v "Я не против, если ты тоже. . ."
                                elif Girl is GwenX:
                                        ch_g "Какое мне дело до кучки НИПов?"
                                elif Girl is BetsyX:
                                        ch_b "Как я могу отказать им в подобном опыте?"
                                elif Girl is DoreenX:
                                        ch_d "Давай устроим им безумное представление. . ."
                                elif Girl is WandaX:
                                        ch_w "О, я знаю парочку кое-каких трюков, которые я хотела бы им показать. . ."
                        $ Girl.Statup("Lust", 200, 4)
                        $ Choice = "A"
                elif ApprovalCheck(Girl, 650, "I", TabM=Cnt):
                        #not an exhibitionist but very uninhibited
                        $ Girl.FaceChange("sexy", 1, Brows="sad")
                        if "spotted" not in Girl.RecentActions:
                                if Girl is RogueX:
                                        ch_r "Хм, что нам с этим делать, [Girl.Petname]?"
                                elif Girl is KittyX:
                                        ch_k "Что же нам делать?"
                                elif Girl is EmmaX:
                                        ch_e "Что ж, мы попали в неудобное положение."
                                elif Girl is LauraX:
                                        ch_l "Как поступим?"
                                elif Girl is JeanX:
                                        $ Girl.Statup("Obed", 80, 3)
                                        $ Girl.Statup("Inbt", 80, 3)
                                        ch_j "Похоже, у нас появились зрители. . ."
                                elif Girl is StormX:
                                        ch_s "Кажется, мы привлекли к себе немного внимания. . ."
                                elif Girl is JubesX:
                                        ch_v "Ох, эм, они смотрят. . ."
                                elif Girl is GwenX:
                                        ch_g "Ох. . . эм. . . у нас тут зрители. . ."
                                elif Girl is BetsyX:
                                        ch_b "Мы словно. . . на сцене?"
                                elif Girl is DoreenX:
                                        ch_d "Ох, на нас. . . смотрят. . ."
                                elif Girl is WandaX:
                                        ch_w "Тут довольно много зрителей. . ."
                        $ Girl.Statup("Lust", 200, 3)
                        $ Choice = "B"
                elif ApprovalCheck(Girl, 1000, "OI", TabM=Cnt):
                        #not an exhibitionist but obedient/uninhibited
                        $ Girl.FaceChange("surprised", 2)
                        if Girl in (EmmaX,StormX):
                                "[Girl.Name] выглядит немного обеспокоенной."
                        elif Girl is LauraX:
                                "[Girl.Name] выглядит немного смущенной."
                        else:
                                "[Girl.Name] выглядит немного испуганной."
                        $ Girl.Statup("Lust", 200, 3)
                        $ Choice = "C"
                else:
                        # She fails her inhibition checks
                        $ Girl.FaceChange("surprised", 2)
                        if "spotted" not in Girl.RecentActions:
                                if Girl is KittyX:
                                        "[Girl.Name] вся красная от стыда вскакивает. Быстро хватает свою одежду и убегает через ближайшую стену."
                                elif Girl in (EmmaX,StormX):
                                        "[Girl.Name] со смущенным видом вскакивает. Быстро хватает свою одежду и убегает."
                                else:
                                        "[Girl.Name] со смущенным видом вскакивает. И убегает, находу надевая свою одежду."
                                $ Girl.Rep -= 3 if Girl.Rep >= 30 else Girl.Rep
                        else:
                                if Girl is KittyX:
                                        $ Girl.Statup("Love", 90, -15)
                                        "[Girl.Name] паникует от такого развития событий. Она ныряет в ближайшую стену."
                                elif Girl in (EmmaX,StormX):
                                        $ Girl.Statup("Love", 90, -15)
                                        "От такого развития событий [Girl.Name] останавливается. Хватает всю свою одежду и убегает."
                                else:
                                        "[Girl.Name] паникует от такого развития событий. Она быстро надевает всю свою одежду."
                        "Вы возвращаетесь в свою комнату."
                        $ Choice = "stop"

                if Choice != "stop":
                    menu:
                        "Что будете делать?"
                        "Да пусть смотрят. . ." if "spotted" not in Girl.RecentActions:
                            if Choice == "A":
                                    $ Girl.FaceChange("sexy", 0)
                                    if Girl is RogueX:
                                            ch_r "И я того же мнения."
                                    elif Girl is KittyX:
                                            ch_k "Продолжим нашу игру."
                                    elif Girl is EmmaX:
                                            ch_e "Поддерживаю твое решение."
                                    elif Girl is LauraX:
                                            ch_l "С этим я справлюсь."
                                    elif Girl is JeanX:
                                            ch_j "Дааа."
                                    elif Girl is StormX:
                                            ch_s "Да. . ."
                                    elif Girl is JubesX:
                                            ch_v "Давай зажжем!"
                                    elif Girl is GwenX:
                                            ch_g "Поехали!"
                                    elif Girl is BetsyX:
                                            ch_b "Давай!"
                                    elif Girl is DoreenX:
                                            ch_d "Согласна!"
                                    elif Girl is WandaX:
                                            ch_w "Ооо да. . ."
                            elif Choice == "B":
                                    #not an exhibitionist but very uninhibited
                                    $ Girl.FaceChange("sexy", 1,Brows="sad")
                                    if Girl is RogueX:
                                            ch_r "Эм, ладно."
                                    elif Girl is KittyX:
                                            ch_k "Хихи, эм, ага."
                                    elif Girl is EmmaX:
                                            ch_e "Полагаю, мы можем показать им, как это делается."
                                    elif Girl is LauraX:
                                            ch_l "Ладно."
                                    elif Girl is JeanX:
                                            ch_j "Конечно, как скажешь."
                                    elif Girl is StormX:
                                            ch_s "Полагаю, пусть будет так. . ."
                                    elif Girl is JubesX:
                                            ch_v "Эм, ага. . ."
                                    elif Girl is GwenX:
                                            ch_g "Ох. . . ладно."
                                    elif Girl is BetsyX:
                                            ch_b "Я постараюсь справиться. . ."
                                    elif Girl is DoreenX:
                                            ch_d "Ох, эм. . . ладно. . ."
                                    elif Girl is WandaX:
                                            ch_w "Ладно. . ."
                            elif Choice == "C":
                                    $ Girl.FaceChange("sexy",2)
                                    if Girl.Obed > Girl.Inbt:
                                        $ Girl.Eyes = "side"
                                        if Girl is RogueX:
                                                ch_r "Ну, если ты этого хочешь, [Girl.Petname]."
                                        elif Girl is KittyX:
                                                ch_k "Если ты настаиваешь, [KittyX.Petname]."
                                        elif Girl is EmmaX:
                                                ch_e "Я не отступлю, пока ты со мной, [EmmaX.Petname]."
                                        elif Girl is LauraX:
                                                if not Player.Male:
                                                    ch_l "Наверное, ты права."
                                                else:
                                                    ch_l "Наверное, ты прав."
                                        elif Girl is JeanX:
                                                ch_j "Полагаю, мы можем продолжить. . ."
                                        elif Girl is StormX:
                                                ch_s "Конечно. . ."
                                        elif Girl is JubesX:
                                                ch_v ". . . Ага."
                                        elif Girl is GwenX:
                                                ch_g ". . . круто. . . круто."
                                        elif Girl is BetsyX:
                                                ch_b "Если это необходимо. . ."
                                        elif Girl is DoreenX:
                                                ch_d "Ох, эм, ладно. . ."
                                        elif Girl is WandaX:
                                                ch_w "Ох. . . конечно. . ."
                                    else:
                                        $ Girl.Mouth = "smile"
                                        $ Girl.Brows = "sad"
                                        if Girl is RogueX:
                                                if not Player.Male:
                                                    ch_r "Эм, наверное, ты права. . ."
                                                else:
                                                    ch_r "Эм, наверное, ты прав. . ."
                                        elif Girl is KittyX:
                                                ch_k "Ага[KittyX.like]конечно. . ."
                                        elif Girl is EmmaX:
                                                ch_e "Ладно, я не возражаю."
                                        elif Girl is LauraX:
                                                ch_l "Как хочешь. . ."
                                        elif Girl is JeanX:
                                                $ Girl.Statup("Obed", 80, 3)
                                                $ Girl.Statup("Inbt", 80, 3)
                                                ch_j "Ага. . ."
                                        elif Girl is StormX:
                                                ch_s "Хорошо. . ."
                                        elif Girl is JubesX:
                                                ch_v "Наверное."
                                        elif Girl is GwenX:
                                                ch_g "Эхехей. . ."
                                        elif Girl is BetsyX:
                                                ch_b "Ну хорошо. . ."
                                        elif Girl is DoreenX:
                                                ch_d "Ох, эм, ладно. . ."
                                        elif Girl is WandaX:
                                                ch_w "Эмм. . . ладно."
                                    $ Girl.Statup("Obed", 200, 5)
                            "Вы возвращаетесь к своим забавам."
                            $ Girl.Blush = 1
                        "Продолжим" if "spotted" in Girl.RecentActions:
                            if Choice == "C":
                                    $ Girl.Statup("Obed", 200, 4)
                        "Ладно, давай остановимся.":
                            if Choice == "A":
                                    $ Girl.FaceChange("sad")
                                    if Girl is KittyX:
                                            ch_k "Буууу."
                                    elif Girl is LauraX:
                                            ch_l "Неженка."
                                    elif Girl is StormX:
                                            ch_s "Ох, если ты настаиваешь. . ."
                                    elif Girl is DoreenX:
                                            ch_d "Оууу. . . а мне это даже. . ."
                                            ch_d "Нравилось."
                                    else:
                                            if not Player.Male:
                                                call AnyLine(Girl,"Обломщица.")
                                            else:
                                                call AnyLine(Girl,"Обломщик.")
                            elif Choice == "B":
                                    $ Girl.FaceChange("sad")
                                    if Girl is RogueX:
                                            if not Player.Male:
                                                ch_r "Ага, наверное, ты права."
                                            else:
                                                ch_r "Ага, наверное, ты прав."
                                    elif Girl is KittyX:
                                            ch_k "Эм, ага."
                                    elif Girl is EmmaX:
                                            if not Player.Male:
                                                ch_e "Пожалуй, ты права."
                                            else:
                                                ch_e "Пожалуй, ты прав."
                                    elif Girl is LauraX:
                                            ch_l "Наверное, это правильное решение."
                                    elif Girl is JeanX:
                                            $ Girl.Statup("Love", 80, 3)
                                            $ Girl.Statup("Obed", 80, 3)
                                            ch_j "Да. . . не будем нарушать порядок."
                                    elif Girl is StormX:
                                            ch_s "Я полагаю, это к лучшему. . ."
                                    elif Girl is JubesX:
                                            if not Player.Male:
                                                ch_v "Ага, наверное, ты права. . ."
                                            else:
                                                ch_v "Ага, наверное, ты прав. . ."
                                    elif Girl is GwenX:
                                            ch_g "Ох. . . хорошо."
                                    elif Girl is BetsyX:
                                            ch_b "Прелестно. . ."
                                    elif Girl is DoreenX:
                                            ch_d "Ох, эм хорошо. . ."
                                    elif Girl is WandaX:
                                            ch_w ". . . ладно."
                            elif Choice == "C":
                                    $ Girl.Statup("Love", 90, 5)
                                    $ Girl.FaceChange("smile")
                                    if Girl is RogueX:
                                            ch_r "Хех, спасибо, [Girl.Petname]"
                                    elif Girl is KittyX:
                                            ch_k "Хихи, спасибо, [Girl.Petname]."
                                            $ Girl.Statup("Love", 90, 5)
                                    elif Girl is EmmaX:
                                            ch_e "Это, наверное, к лучшему. . ."
                                    elif Girl is LauraX:
                                            ch_l "Ага, спасибо."
                                            $ Girl.Statup("Love", 90, 5)
                                    elif Girl is JeanX:
                                            $ Girl.Statup("Love", 80, 3)
                                            $ Girl.Statup("Obed", 80, 3)
                                            ch_j "Ага. . ."
                                    elif Girl is StormX:
                                            ch_s "Да, в этом есть смысл. . ."
                                    elif Girl is JubesX:
                                            ch_v "Хех, спасибо."
                                    elif Girl is GwenX:
                                            ch_g "Божеспасибобольшое!"
                                    elif Girl is BetsyX:
                                            ch_b "Ах, замечательно."
                                    elif Girl is DoreenX:
                                            ch_d "Фух. . ."
                                    elif Girl is WandaX:
                                            ch_w "Эм, ага."
                            if bg_current == "bg mall":
                                    "Вы вдвоем убегаете обратно в институт."
                            else:
                                    "Вы разбегаетесь по своим комнатам."
                            $ Choice = "stop"

                if Choice == "stop":
                            $ Girl.RecentActions.append("caught")
                            $ Girl.DailyActions.append("caught")
                            show blackscreen onlayer black
                            call AllReset(Girl)
                            call Remove_Girl(Girl)
                            $ Girl.OutfitChange(Changed=0)
                            hide blackscreen onlayer black
                            $ bg_current = "bg player"
                            jump Misplaced
        elif "exhibitionist" not in Girl.Traits:
                            $ Girl.FaceChange("sly")
                            if Girl is JeanX and "nowhammy" not in JeanX.Traits:
                                    #if it's Jean, this doesn't count unless she's got "nowhammy" status
                                    pass
                            else:
                                    $ Girl.Traits.append("exhibitionist")
                                    "[Girl.Name], похоже, стала кем-то вроде эксгибиционистки."
        elif D20 > 15:
                            $ Girl.FaceChange("sexy")
                            "Толпа аплодирует вам."

        $ Girl.RecentActions.append("spotted") if Cnt < 4 else Girl.RecentActions
        $ Girl.DailyActions.append("spotted")  if "spotted" not in Girl.DailyActions else Girl.DailyActions
        return

# end public sex check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start girls noticed / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girls_Noticed(Girl=Primary,Other=0,Silent=0,B=0,BO=[]): #rkeljsvgb
        # Called by Sex_Dialog or Girls_Taboo
        # Girl is lead girl, Other is a girl who notices you
        # if Silent, no dialog plays, B is a carried bonus value.
        if not Girl or Girl not in TotalGirls:
                        "Tell Oni that in noticed, no primary is set."
                        return
        $ BO = TotalGirls[:]
        $ BO.remove(Girl)
        python:
            for BX in BO:
                if BX.Loc == bg_current and BX is not Girl:
                        # if there is a girl who is not primary, but is in the location
                        # set her as the one being noticed by the primary girl
                        Other = BX
                        break
        if Other not in TotalGirls or Other == Girl:
                return
        if "threesome" in Other.RecentActions:
                return
        if Partner == Other and "noticed " + Girl.Tag in Other.RecentActions:
                return

        if not Silent:
            if Partner != Other:
                    #if there has been no connection yet. . .
                    $ Other.FaceChange("surprised", 1)
                    "[Other.Name] замечает, чем вы [Girl.Name_tvo] занимаетесь."
            else:
                    #if there has been some noticing already. . .
                    $ Other.FaceChange("sly", 1)
                    if Other == KittyX:
                            "[Other.Name] внимательно смотрит на вас с [Girl.Name_tvo]. . ."
                    elif Other == EmmaX:
                            "[Other.Name] внимательно наблюдает за вами с [Girl.Name_tvo]. . ."
                    else:
                            "[Other.Name] смотрит на вас с [Girl.Name_tvo]. . ."

        if "cockout" in Player.RecentActions:
                    #call Girl_First_Peen(Other)
                    call Seen_First_Peen(Other,Girl)

        $ Girl.RecentActions.append("noticed " + Other.Tag)
        $ Other.RecentActions.append("noticed " + Girl.Tag)
        if Other == EmmaX and ("three" not in EmmaX.History or "classcaught" not in EmmaX.History):
                    #Emma-specific code
                    $ Other.AddWord(1,0,0,"saw with " + Girl.Tag) #adds to Traits.
                    if bg_current == EmmaX.Home:
                            #if you're in her room. . .
                            ch_e "Если, вы двое, не в состояние держаться подальше друг от друга, пожалуйста, занимайтесь подобным в другом месте. . ."
                            if not Player.Male:
                                "Она выгоняет вас обеих в коридор и захлопывает дверь."
                            else:
                                "Она выгоняет вас обоих в коридор и захлопывает дверь."
                            $ Girl.Loc = "bg player"
                            jump Misplaced
                    call Remove_Girl(EmmaX)
                    if not Silent:
                            "Кажется, ей стало неуютно от подобной ситуации, она выходит из комнаты."
                            "Возможно, вам стоит поговорить с ней об этом позже."
                    return

        if "poly " + Girl.Tag in Other.Traits or (Girl in Player.Harem and Other in Player.Harem) or Other is WandaX:
                #if they already have a relationship. . .
                $ B = (1000-(20*Taboo))
        else:
                #if they don't have a relationship. . .
                $ B = (Other.GirlLikeCheck(Girl) - 500) #RogueX.LikeLaura - 500
                if Other in Player.Harem:
                        #if you and the other girl have a relationship. . .
                        $ B -= 200

        $ Other.SpriteLoc = StageFarRight
        call Display_Girl(Other,0,0)
        if Partner == Other:
                #if this is already a Partner, skip this dialog
                $ Silent = 1
        $ Partner = Other
        $ Line = 0
        if not Player.Male and "girltalk" not in Other.History and "nogirls" not in Other.History:
                    #if you're a girl and she hasn't clocked you yet
                    $ Other.AddWord(1,0,0,"intome") #trait

        if ApprovalCheck(Other, 2000, TabM=2, Bonus = B) or ApprovalCheck(Other, 950, "L", TabM=2, Bonus = (B/3)):
                    #if she's very loose or really likes you
                    $ Other.FaceChange("sexy", 1)
                    if not Silent:
                            "Она решает присоединиться к вам."
                    $ Other.Statup("Obed", 90, 5)
                    $ Other.Statup("Inbt", 90, 5)
                    $ Other.Statup("Lust", 90, 3)
                    $ Other.AddWord(1,0,0,"poly " + Girl.Tag)
                    call Threeway_Set(Other,Girl)
        elif (ApprovalCheck(Other, 650, "O", TabM=2) and ApprovalCheck(Other, 450, "L", TabM=1)) or ApprovalCheck(Other, 800, "O", TabM=2, Bonus = (B/3)):
                    #if she likes you, but is very obedient
                    $ Other.FaceChange("sexy")
                    if not Silent:
                            "Она терпеливо сидит в сторонке и наблюдает."
                    $ Other.Statup("Love", 90, 5)
                    $ Other.Statup("Inbt", 90, 5)
                    $ Other.Statup("Lust", 90, 2)
                    $ Other.AddWord(1,0,0,"poly " + Girl.Tag)
                    call Threeway_Set(Other,Girl,"watch")
        elif (ApprovalCheck(Other, 650, "I", TabM=2) and ApprovalCheck(Other, 450, "L", TabM=1)) or ApprovalCheck(Other, 800, "I",Alt=[[GwenX],300], TabM=2, Bonus = (B/3)):
                    #if she likes you, but is very uninhibited
                    $ Other.FaceChange("sexy")
                    if not Silent:
                            "Она садится и смотрит на вас голодным взглядом."
                    $ Other.Statup("Love", 90, 5)
                    $ Other.Statup("Obed", 90, 2)
                    $ Other.Statup("Inbt", 90, 2)
                    $ Other.Statup("Lust", 90, 5)
                    $ Other.AddWord(1,0,0,"poly " + Girl.Tag)
                    call Threeway_Set(Other,Girl,"watch")
        elif ApprovalCheck(Other, 1500, TabM=2, Bonus = B):
                    $ Other.FaceChange("perplexed", 1)
                    if not Silent:
                            "Она выглядит немного смущенной ситуацией, но, тем не менее, остается на месте и наблюдает."
                    if Other.Love >= Other.Obed and Other.Love >= Other.Inbt:
                        $ Other.Statup("Obed", 90, 2)
                        $ Other.Statup("Inbt", 90, 2)
                    elif Other.Obed >= Other.Inbt:
                        $ Other.Statup("Love", 90, 2)
                        $ Other.Statup("Inbt", 90, 2)
                    else:
                        $ Other.Statup("Love", 90, 2)
                        $ Other.Statup("Obed", 90, 1)
                        $ Other.Statup("Inbt", 90, 1)
                    $ Other.Statup("Lust", 90, 5)
                    call Threeway_Set(Other,Girl,"watch")
        elif ApprovalCheck(Other, 650, "L", TabM=1) or ApprovalCheck(Other, 400, "O", TabM=2):
                    #if she likes you or is obedient, but not enough
                    $ Other.FaceChange("angry", 2)
                    if bg_current == Other.Home:
                            if Other in (LauraX,JeanX):
                                if not Player.Male:
                                    "Она с раздражением выгоняет вас обеих из комнаты."
                                else:
                                    "Она с раздражением выгоняет вас обоих из комнаты."
                            else:
                                if not Player.Male:
                                    "Она выгоняет вас обеих из комнаты. Она выглядела обманутой."
                                else:
                                    "Она выгоняет вас обоих из комнаты. Она выглядела обманутой."
                    else:
                            if Other in (LauraX,JeanX):
                                "Она выбегает из комнаты. Она выглядела раздраженной."
                            else:
                                "Она выбегает из комнаты. Она выглядела обманутой."
                    $ Other.Statup("Love", 200, -5)
                    $ Other.Statup("Love", 80, -5)
                    $ Other.Statup("Love", 70, -5)
                    $ Other.Statup("Obed", 90, -5)
                    $ Other.Statup("Lust", 89, 10)
                    menu:
                        "[[Отпустить ее.]":
                                $ Partner = 0
                                if Other.SEXP > 10:
                                        $ Other.AddWord(1,0,0,"saw with " + Girl.Tag)
                        "Подожди, вернись!":
                                $ Other.Statup("Obed", 80, 1)

                                if "intome" in Other.Traits:
                                        #if she thinks you might be into her as a girl
                                        $ Other.DrainWord("intome",0,0,1)
                                        call expression Other.Tag + "_Girltalk" pass (1) # "Hey, are you inta me?"

                                if ApprovalCheck(Other, 1200, TabM=2, Bonus = B):
                                    #she agrees to stick around
                                    call Noticed_Dialogue(2)
                                elif ApprovalCheck(Other, 900, TabM=2, Bonus = B):
                                    #she leaves, but is calmer
                                    call Noticed_Dialogue(1)
                                    $ Partner = 0
                                else:
                                    #she refuses to stick around
                                    call Noticed_Dialogue(0)
                                    $ Partner = 0

                    if not Partner:
                            if bg_current == Other.Home: #Kicks you out if in Rogue's room
                                    $ Other.RecentActions.append("angry")
                                    call GirlsAngry
                            call Remove_Girl(Other)
                    call Taboo_Level(1)
        else:
                    #if she doesn't like you much
                    $ Other.FaceChange("surprised", 2)
                    $ Other.Statup("Inbt", 90, 2)
                    $ Other.Statup("Lust", 40, 20)
                    if Trigger != "kiss you":
                            $ Other.Statup("Love", 90, -10)
                            $ Other.Statup("Obed", 90, -5)
                            $ Other.Statup("Lust", 80, 10)
                    if bg_current == Other.Home:
                            $ Other.Statup("Love", 90, -5)
                            $ Other.Statup("Obed", 90, -5)
                            if Other in (LauraX,JeanX):
                                    if not Player.Male:
                                        "Похоже ей стало неуютно от происходящего и она решает выгнать вас обеих из комнаты."
                                    else:
                                        "Похоже ей стало неуютно от происходящего и она решает выгнать вас обоих из комнаты."
                            else:
                                    if not Player.Male:
                                        "Похоже ее смутило происходящее и она решает выгнать вас обеих из комнаты."
                                    else:
                                        "Похоже ее смутило происходящее и она решает выгнать вас обоих из комнаты."
                    elif Trigger != "kiss you":
                            if Other in (LauraX,JeanX):
                                    "Похоже ей стало неуютно от происходящего и она решает выйти из комнаты."
                            else:
                                    "Похоже ее смутило происходящее и она решает выйти из комнаты."
                    else:
                                "Похоже ее разочаровало происходящее и она решает выйти из комнаты."
                    $ Partner = 0
                    if bg_current == Other.Home: #Kicks you out if in Rogue's room
                            $ Other.RecentActions.append("angry")
                            call GirlsAngry
                    call Remove_Girl(Other)
                    call Taboo_Level(1)

        if AloneCheck(Girl) and Girl.Taboo == 20:
                    #if the second girl ran away, it removes the taboo factor she added.
                    $ Girl.Taboo = 0
                    $ Taboo = 0
        if Line:
                    # This plays a line from a threesome action, if there is one.
                    "[Line]."
                    $ Line = 0
        return

label Noticed_Dialogue(Agree=0): #rkeljsvgb
        #if Agree=2, then she agrees, if 1 she is sympathetic, if 0, she doesn't
        if Agree > 1:
                $ Other.FaceChange("angry", 1)
                $ Other.Statup("Love", 90, 2)
                $ Other.Statup("Obed", 50, 2)
                $ Other.Statup("Obed", 90, 1)
                $ Other.Statup("Inbt", 90, 1)
                if Other is RogueX:
                        ch_r "Я могу остаться ненадолго, [Other.Petname]. . ."
                elif Other is KittyX:
                        ch_k "Эм. . ."
                        "Она присаживается. . ."
                elif Other is EmmaX:
                        ch_e "Полагаю, я могла бы понаблюдать, [Other.Petname]."
                elif Other is LauraX:
                        ch_l "Ок, конечно."
                elif Other is JeanX:
                        ch_j "Да пофиг."
                elif Other is StormX:
                        ch_s "Пожалуй, я могу остаться. . ."
                elif Other is JubesX:
                        ch_v "О, если ты хочешь, можно. . ."
                elif Other is GwenX:
                        ch_g "Я, эм. . . наверное, могу понаблюдать. . ."
                elif Other is BetsyX:
                        ch_b "Если подумать, мне. . . возможно, немного любопытно. . ."
                elif Other is DoreenX:
                        ch_d "Я могу остаться. . . ради научного интереса. . ."
                elif Other is WandaX:
                        ch_w "Ну, раз вам нужны зрители. . ."
        elif Agree:
                $ Other.FaceChange("angry", 1,Eyes="side")
                $ Other.Statup("Love", 90, 2)
                $ Other.Statup("Obed", 90, 1)
                $ Other.Statup("Inbt", 90, 1)
                if Other is RogueX:
                        ch_r "Мне нужно подумать, [Other.Petname]."
                elif Other is KittyX:
                        ch_k "Эм, нет. . ."
                elif Other is EmmaX:
                        ch_e "Что ж, не прямо сейчас, [Other.Petname]."
                elif Other is LauraX:
                        ch_l "Может быть, в другой раз. . ."
                elif Other is JeanX:
                        ch_j "Неа."
                elif Other is StormX:
                        ch_s "Останься я здесь, я бы чувстовала себя некомфортно. . ."
                elif Other is JubesX:
                        ch_v "Эм, я бы не хотела мешать. . ."
                elif Other is GwenX:
                        ch_g "Это, эм. . . слишком реально. . ."
                elif Other is BetsyX:
                        ch_b "Возможно. . . как-нибудь в другой раз. . ."
                elif Other is DoreenX:
                        ch_d "Я могла бы остаться. . . но лучше уйду. . ."
                elif Other is WandaX:
                        ch_w "Хех, я бы не хотела стеснять вас. . ."
        else:
                $ Other.Statup("Love", 90, -1)
                if Other is RogueX:
                        ch_r "Отвали, [Other.Petname]!"
                elif Other is KittyX:
                        ch_k "Я так не думаю, [Other.Petname]!"
                elif Other is EmmaX:
                        ch_e "Мне это не интересно, [Other.Petname]."
                elif Other is LauraX:
                        ch_l "Ты -совсем- не хочешь этого, [Other.Petname]."
                elif Other is JeanX:
                        "Она просто разворачивается."
                elif Other is StormX:
                        ch_s "Я не заинтересована."
                elif Other is JubesX:
                        ch_v "Нет, ребята, веселитесь сами."
                elif Other is GwenX:
                        ch_g "Ох, эм. . . мне не интересно."
                elif Other is BetsyX:
                        ch_b "Я не думаю, что это было бы правильно. . ."
                elif Other is DoreenX:
                        ch_d "Я. . . не могу. . ."
                elif Other is WandaX:
                        ch_w "Хех, нет, веселитесь. . ."
                if Other.SEXP > 10:
                        $ Other.AddWord(1,0,0,"saw with " + Girl.Tag)
        return

# End girls noticed / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start CloseOut  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label CloseOut(Chr = Ch_Focus): #rkeljsvgbdw
        # This exits out of the current sex act, whichever it might be, then returns
        if Chr and Chr != Ch_Focus:
                call Shift_Focus(Chr)
#        $ Chr = GirlCheck(Chr)
        if Trigger == "blow":
            call Girl_BJ_After # call expression Chr.Tag + "_BJ_After"
        elif Trigger == "hand":
            call Girl_HJ_After # call expression Chr.Tag + "_HJ_After"
        elif Trigger == "cun":
            call Girl_CUN_After # call expression Chr.Tag + "_CUN_After"
        elif Trigger == "finger":
            call Girl_Finger_After # call expression Chr.Tag + "_Finger_After"
        elif Trigger == "titjob":
            call Girl_TJ_After # call expression Chr.Tag + "_TJ_After"
        elif Trigger == "kiss you":
            call Kiss_After
        elif Trigger == "fondle breasts":
            call Girl_FB_After # call expression Chr.Tag + "_FB_After"
        elif Trigger == "suck breasts":
            call Girl_SB_After # call expression Chr.Tag + "_SB_After"
        elif Trigger == "fondle thighs":
            call Girl_FT_After # call expression Chr.Tag + "_FT_After"
        elif Trigger == "fondle pussy":
            call Girl_FP_After # call expression Chr.Tag + "_FP_After"
        elif Trigger == "lick pussy":
            call Girl_LP_After # call expression Chr.Tag + "_LP_After"
        elif Trigger == "fondle ass":
            call Girl_FA_After # call expression Chr.Tag + "_FA_After"
        elif Trigger == "insert ass":
            call Girl_IA_After # call expression Chr.Tag + "_IA_After"
        elif Trigger == "lick ass":
            call Girl_LA_After # call expression Chr.Tag + "_LA_After"
        elif Trigger == "sex":
            call Girl_SexAfter # call expression Chr.Tag + "_SexAfter"
        elif Trigger == "hotdog":
            call Girl_HotdogAfter # call expression Chr.Tag + "_HotdogAfter"
        elif Trigger == "anal":
            call Girl_AnalAfter # call expression Chr.Tag + "_AnalAfter"
        elif Trigger == "dildo pussy":
            call Girl_Dildo_After # call expression Chr.Tag + "_DP_After"
        elif Trigger == "dildo anal":
            call Girl_Dildo_After # call expression Chr.Tag + "_DA_After"
        elif Trigger == "strip":
            call Group_Strip_End
        elif Trigger == "masturbation":
            $ Chr.Action -= 1
            $ Chr.Mast += 1
        elif Trigger == "lesbian":
            call Les_After
        else:
            "That's odd, tell Oni how you got here, Close [Chr.Name] [Trigger]."
        return
# End CloseOut  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Sex_Over  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Sex_Over(Clothes=1,Girls=0,BO=[],Cleaned=[],OverLines={}): #rkeljsvgb
        #this routine plays out at the end of any sex menu session
        #it cleans them up and puts their clothes on, only returning a line of dialog if they were undressed
        # call Sex_Over(1,Girl)
        $ Line = 0
        call Trig_Reset
        if Girls in TotalGirls:
                # in this case, "Girls" would be a single girl, ie RogueX
                $ BO = [Girls]
        else:
                $ BO = TotalGirls[:]
                $ renpy.random.shuffle(BO)
        python:
            for BX in BO:
                if BX.Loc == bg_current:
                        # if this girl is present
                        BX.OCount = 0
                        if not Player.Male:
                                BX.Les += 1
                        Cleaned.append(BX) #call Girl_Cleanup(BX,"after")
                        if Player.Spunk and not Girls:
                                Girls = BX
                        if BX in JumpQueue:
                                JumpQueue.remove(BX)

                if "nowhammy" not in JeanX.Traits and "saw with Jean" in BX.Traits:
                                #if a girl saw you with Jean and got pissed, she forgets. . .
                                BX.Traits.remove("saw with Jean")
                                BX.Traits.append("sawJeanW") #got whammied tag
                BX.Loose = 2 if BX.Loose > 2 else BX.Loose
                BX.Offhand = 0
                BX.Pose = 0

        while Cleaned:
                #if a girl needs to clean up
                call Girl_Cleanup(Cleaned[0],"after")
                $ Cleaned.remove(Cleaned[0])

        if Player.Spunk and Girls:
                #if a girl got picked to clean you
                $ OverLines = {
                            RogueX:     "Позволь мне позаботиться об этом за тебя. . .",
                            KittyX:     "На тебе кое-что есть. . .\n позволь мне все уладить.",
                            EmmaX:      EmmaX.Petname+", давай приведем тебя в презентабельный вид. . .",
                            LauraX:     LauraX.Petname+", на тебе кое-что есть. . .",
                            JeanX:      JeanX.Petname+", возможно, ты захочешь, чтобы тебя привели в порядок. . .",
                            StormX:     "Позволь мне позаботиться об этом, "+StormX.Petname+". . .",
                            JubesX:     "О, я могу помочь тебе, "+JubesX.Petname+". . .",
                            GwenX:      "Мне кажется, ты не против, чтобы я тебе помогла?",
                            BetsyX:     "Хочешь, чтобы я позаботилась обо всем?",
                            DoreenX:    "Я могу навести порядок. . .",
                            WandaX:     "Дай-ка я приведу тебя в порядок. . ."}
                call AnyLine(Girls,OverLines[Girls])
                call Girl_CleanCock(Girls)

        $ LauraX.Red = 0 #she heals fast
        if Girls == Partner and Girls in TotalGirls:
                #swaps lead back to original
                call Shift_Focus(Girls)
        $ Girls = 0
        call AllReset("all") #resets all sex positions.

        if Clothes and Taboo:
                #if asked to put their clothes back on, and in a public place.
                $ BO = TotalGirls[:]
                python:
                    for BX in BO:
                        if BX.Loc == bg_current:
                                if BX.OutfitChange(Changed=1) == 2:
                                        if Line:
                                            Line = Line + " с " + BX.Name_tvo
                                        else:
                                            Line = BX.Name
                                        Girls += 1
                                if BX.Lust >= 90:
                                        BX.Wet = 2
                                elif BX.Lust >= 60:
                                        BX.Wet = 1
                                else:
                                        BX.Wet = 0
                if Girls > 1:
                    "[Line] одеваются."
                elif Girls:
                    "[Line] одевается."
        call Get_Dressed
        $ Player.AddWord(1,"sexit") #adds to recent
        call Checkout(1)
        return


# End Sex_Over  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start SkipTo  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label SkipTo(Chr = Ch_Focus): #rkeljsvgb
        # This jumps to the chosen sex act, called from the sex menu
        if Chr and Chr != Ch_Focus:
                call Shift_Focus(Chr)
#        $ Chr = GirlCheck(Chr)
        if Trigger == "blow":
            call Girl_BJ_Cycle # call expression Chr.Tag + "_BJ_Cycle"
        elif Trigger == "hand":
            call Girl_HJ_Cycle # call expression Chr.Tag + "_HJ_Cycle"
        elif Trigger == "cun":
            call Girl_CUN_Cycle
        elif Trigger == "finger":
            call Girl_Finger_Cycle
        elif Trigger == "titjob":
            call Girl_TJ_Cycle # call expression Chr.Tag + "_TJ_Cycle"
        elif Trigger == "kiss you":
            call KissCycle
        elif Trigger == "fondle breasts":
            call Girl_FB_Cycle # call expression Chr.Tag + "_FB_Cycle"
        elif Trigger == "suck breasts":
            call Girl_SB_Cycle # call expression Chr.Tag + "_SB_Cycle"
        elif Trigger == "fondle thighs":
            call Girl_FT_Cycle # call expression Chr.Tag + "_FT_Cycle"
        elif Trigger == "fondle pussy":
            call Girl_FP_Cycle # call expression Chr.Tag + "_FP_Cycle"
        elif Trigger == "lick pussy":
            call Girl_LP_Cycle # call expression Chr.Tag + "_LP_Cycle"
        elif Trigger == "fondle ass":
            call Girl_FA_Cycle # call expression Chr.Tag + "_FA_Cycle"
        elif Trigger == "insert ass":
            call Girl_IA_Cycle # call expression Chr.Tag + "_IA_Cycle"
        elif Trigger == "lick ass":
            call Girl_LA_Cycle # call expression Chr.Tag + "_LA_Cycle"
        elif Trigger == "sex":
            call Girl_Sex_Cycle # call expression Chr.Tag + "_SexCycle"
        elif Trigger == "hotdog":
            call Girl_Hotdog_Cycle # call expression Chr.Tag + "_HotdogCycle"
        elif Trigger == "anal":
            call Girl_Anal_Cycle # call expression Chr.Tag + "_AnalCycle"
        elif Trigger == "dildo pussy":
            call Girl_Dildo_Cycle # call expression Chr.Tag + "_DP_Cycle"
        elif Trigger == "dildo anal":
            call Girl_Dildo_Cycle # call expression Chr.Tag + "_DA_Cycle"
        elif Trigger == "strip":
            call Group_Strip_End
        elif Trigger == "masturbation":
            $ Chr.Action -= 1
            $ Chr.Mast += 1
        elif Trigger == "lesbian":
            call Les_Cycle
        else:
            "That's odd, tell Oni how you got here, Close [Chr.Name] [Trigger]."
        return
# End SkipTo/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Clear_Stack:
    #this empties the call stack of stray items, and is called when the player goes to his room
    $ StackDepth = renpy.call_stack_depth() #Count = number of items in the call stack
    while StackDepth > 0:
        $ StackDepth -= 1
        $ renpy.pop_call()
    jump Player_Room


#Character Specific stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#Start Microtransactions content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Microtransactions_Intro:
        "Вы чувствуете присутствие Ксавье у себя в голове."
        if not Player.Male:
            ch_x "Не могла бы ты зайти ко мне в кабинет, пожалуйста?"
        else:
            ch_x "Не мог бы ты зайти ко мне в кабинет, пожалуйста?"
        menu:
            extend ""
            "Ладно." if not Party and not Present:
                    $ Party = []
                    "Вы направляетесь в кабнет Ксавье."
            "У меня дела." if Party or Present:
                    $ Party = []
                    "Вы извиняетесь и уходите по своим делам."

            "Нет.":
                ch_x "-Сейчас же,- [Player.Name]!"
                if Party or Present:
                        $ Party = []
                        "Вы извиняетесь и уходите по своим делам."
                else:
                        "Вы направляетесь в кабнет Ксавье."
        show blackscreen onlayer black
        pause 0.1
        $ Round -= 5
        $ bg_current = "bg study"
        call XavierFace("happy")
        call Set_The_Scene
        show Professor at SpriteLoc(StageLeft) zorder 25
        hide blackscreen onlayer black
        if not Player.Male:
            ch_x "[Player.Name], я рад, что ты решила заглянуть ко мне."
        else:
            ch_x "[Player.Name], я рад, что ты решил заглянуть ко мне."
        if "switchxavier" in Player.History:
                call Xavier_Switch
        if not Player.Male:
            ch_x "У меня есть одно дело, с которым, как мне кажется, ты могла бы мне помочь."
        else:
            ch_x "У меня есть одно дело, с которым, как мне кажется, ты мог бы мне помочь."
        ch_x "Я слышал, что у тебя некие. . . финансовые проблемы."
        ch_x "Возможно, я мог бы избавить тебя от них."
        ch_x "Я придумал новый фантастический способ получения денег."
        ch_x "Я называю его \"микротранзакции!\""
        menu:
            extend ""
            "То есть, -мне- типа нужно дать -вам- наличку?":
                    call XavierFace("shocked")
                    ch_x "Что? Какой в этом смысл? Ты даешь мне наличные, а я потом возвращаю тебе их с процентом?"
            "Какой-то лохотрон!":
                    call XavierFace("shocked")
                    ch_x "Я еще даже не объяснил всю схему!"
            "Как-то подозрительно!":
                    call XavierFace("shocked")
                    ch_x "О чем ты вообще говоришь?"
        ch_x "Я не понимаю, в чем проблема, это просто способ доставки сюрпризов!"
        call XavierFace ("happy")
        ch_x "Открываешь небольшую коробочку и получаешь предмет!"
        ch_x "Это невероятная механика!"
        ch_x "Она включает в себя использование одного изобретения, разработанного моим другом."
        ch_x "Оно носит название \"частицы Пима.\""
        menu:
            extend ""
            "Что?!":
                pass
            "О. Понятно, к чему все идет. . .":
                pass
        ch_x "Да, так вот, с его помощью я могу взять большие. . ."
        ch_x ". . . громоздкие. . . "
        ch_x ". . . объекты и уменьшить их до более удобного размера."
        ch_x "Так эти предметы можно легко доставлять по всему городу."
        if not Player.Male:
            ch_x "Все, что мне от тебя нужно, так это то, чтобы ты брала эти посылки и доставляла их по назначению."
            ch_x "Совершала микротранзакции!"
        else:
            ch_x "Все, что мне от тебя нужно, так это то, чтобы ты брал эти посылки и доставлял их по назначению."
            ch_x "Совершал микротранзакции!"
        menu:
            "Все ясно.":
                pass
            "А?":
                call XavierFace("shocked")
                ch_x ". . . Не думаю, что смогу объяснить еще подробнее."
        call XavierFace("happy")
        ch_x "Держи, твоя первая доставка, просто отнеси посылку Генри в лабораторию."
        menu:
            extend ""
            "Хорошо.":
                    pass
            "Нет, спасибо.":
                    ch_x "Если ты не хочешь этим заниматься, я пойму."
                    ch_x "Но это очень срочная доставка, поэтому боюсь, что в этот раз. . ."
                    ch_x "Я буду настаивать."
        show blackscreen onlayer black
        scene
        pause 0.1
        scene empty_class onlayer backdrop
        hide blackscreen onlayer black
        $ Round -= 5
        "Вы берете у профессора маленькую металлическую коробочку и направляетесь в лабораторию профессора Маккоя."
        "Вы кладете ее в угол, и она быстро увеличивается до большого устройства с надписью \"Пим\""
        ch_mc "О, мой уменьшающий луч!"
        $ bg_current = "bg study"
        show blackscreen onlayer black
        pause 0.1
        call Set_The_Scene
        show Professor at SpriteLoc(StageLeft) zorder 25
        hide blackscreen onlayer black
        $ Round -= 5
        "Вы возвращаетесь в кабинет Ксавье."
        $ Player.Cash += 10
        ch_x "Видишь? Все очень просто!"
        $ Player.History.append("micro")
        ch_x "Если захочешь вернуться к микротранзакциям, просто загляни в лабораторию МакКоя."
        ch_x "Уверен, там найдется много работы."
        "Вы возвращаетесь в свою комнату."
        $ bg_current = "bg player"
        show blackscreen onlayer black
        pause 0.1
        call Set_The_Scene
        hide Professor
        hide blackscreen onlayer black
        return

label Microtransactions:
        #You can do up to three of these per day.
        #short ones take 15 minutes and return 1
        #long ones take 30 minutes and return 3
        if Round < 20:
                "Сейчас у вас нет на это времени, может быть, позже."
                return
        if Player.DailyActions.count("micro") >= 3:
                "На сегодня больше нет микротранзакций."
                return
        menu:
            "Что вы хотите сделать?"
            "Взять ближнюю МТ":
                    $ Line = renpy.random.choice(["в комнату Опасности",
                        "в аудиторию",
                        "к бассейну",
                        "в комнату Скотта",
                        "в комнату Курта",
                        "в комнату Бобби",
                        "в конференц зал",
                        "в комнату Логана",
                        "в комнату без опознавательных знаков с единственной мерцающей лампочкой и странными пятнами",
                        "в библиотеку",
                        "в кабинет Ксавье",
                        "в кафетерий"])
                    $ Round -= 10
                    show blackscreen onlayer black
                    pause 0.1
                    hide blackscreen onlayer black
                    "Вы забираете посылку у Маккоя и доставляете ее [Line]."
                    $ Line = renpy.random.choice(["холодильник.",
                        "микроволновку.",
                        "секс куклу. Какая неловкая ситуация.",
                        "секс куклу. Это все объясняет.",
                        "машину. Может, вам следовало открыть ее снаружи?",
                        "стол.",
                        "большую кровать.",
                        "ящик, полный пакетиков белого порошка. Мука, наверное.",
                        "огромную кучу упакованной одежды.",
                        "огромный ящик с выпивкой."])
                    "Она быстро вырастает в [Line]"
                    $ Round -= 5
                    $ Player.Cash += 3
                    show blackscreen onlayer black
                    pause 0.1
                    hide blackscreen onlayer black
                    "Вы возвращаетесь к себе."
            "Взять дальнюю МТ [[Заблокировано] (locked)" if Round < 50:
                    pass
            "Взять дальнюю МТ" if Round >= 50:
                    $ Line = renpy.random.choice(["в ресторан",
                        "в театр",
                        "в местный бутик",
                        "в дом мэра",
                        "в торговый центр",
                        "в пожарную станцию",
                        "в ресторан ресторан, который вы не посещаете",
                        "в танцевальный клуб",
                        "в разрушенную хижину",
                        "в местную среднюю школу"])
                    $ Round -= 20
                    show blackscreen onlayer black
                    pause 0.1
                    hide blackscreen onlayer black
                    "Вы забираете посылку у МакКоя и доставляете ее [Line]."
                    $ Line = renpy.random.choice(["холодильник.",
                        "микроволновку.",
                        "секс куклу. Какая неловкая ситуация.",
                        "секс куклу. Это все объясняет.",
                        "машину. Может, вам следовало открыть ее снаружи?",
                        "диван.",
                        "большую кравать.",
                        "ящик, полный пакетиков белого порошка. Это мука, наверное.",
                        "огромную кучу упакованной одежды.",
                        "огромный ящик попкорна."])
                    "Она быстро вырастает в [Line]"
                    $ Round -= 10
                    $ Player.Cash += 6
                    show blackscreen onlayer black
                    pause 0.1
                    hide blackscreen onlayer black
                    "Вы возвращаетесь к себе."
            "Выйти":
                    return
        $ Line = 0
        $ Player.DailyActions.append("micro")
        return
#End Microtransactions content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start ripped tights / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Girl_TightsRipped(Girl=0,Count=0,BO=[]): #rkeljsvgbdw
        #Called by Training to see if a girl's cloths gets ripped
        $ D20 = 0
        python:
            BO = ActiveGirls[:]
            for BX in BO:
                #Runs through all active girls, if they are in the room, checks to see if their hose were ripped.
                if BX.Loc != bg_current:
                        pass
                elif BX.Hose != "pantyhose" and BX.Hose != "tights":
                        pass
                elif (BX.Hose == "tights" and "ripped tights" in BX.Inventory) or (BX.Hose == "pantyhose" and "ripped pantyhose" in BX.Inventory):
                        #if she already has some, chance ot skip
                        D20 = renpy.random.randint(1, 20)
                        if D20 >= 10:
                            Girl = BX
                            break
                else:  #If she doesn't have any
                            Girl = BX
                            break
        if Girl not in TotalGirls:
                return

        if Girl.Hose == "tights":
                $ Count = 1
                $ Girl.Hose = "ripped tights"
                $ Girl.FaceChange("angry")
        elif Girl.Hose == "pantyhose":
                $ Count = 1
                $ Girl.Hose = "ripped pantyhose"
                $ Girl.FaceChange("angry")

        if D20 > 15:
            pass     #if it's a second time through then it's only a 25% chance of dialogue
        elif "ripped tights" in Girl.Inventory or "ripped pantyhose" in Girl.Inventory:
            #if she'd already torn a pair
            if Girl is RogueX:
                    ch_r "Проклятье, еще одна пара испорчена!"
            elif Girl is KittyX:
                    ch_k "Черт! Только не снова!"
            elif Girl is EmmaX:
                    ch_e "Что ж, нужно будет купить еще одну пару. . ."
            elif Girl is LauraX:
                    ch_l "Мне нужно найти более прочные."
            elif Girl is JeanX:
                    ch_j "Ну, надо бы найти у кого можно взять еще парочку. . ."
            elif Girl is StormX:
                    ch_s "Мне нужно прикупить их побольше."
            elif Girl is JubesX:
                    ch_v "Ну, теперь пора бежать. . ."
            elif Girl is GwenX:
                    ch_g "Серьезно? . ."
            elif Girl is BetsyX:
                    ch_b "Я так разорюсь на них."
            elif Girl is DoreenX:
                    ch_d "У меня они уже заканчиваются. . ."
            elif Girl is WandaX:
                    ch_w "У меня уже есть точно такие же. . ."
        else:
            $ Count = 2
            if Girl is RogueX:
                    ch_r "Ненавижу заниматься в подобных вещах."
            elif Girl is KittyX:
                    ch_k "Ай, похоже, я не смогла увернуться. . ."
            elif Girl is EmmaX:
                    ch_e "Что ж, не повезло. . ."
            elif Girl is LauraX:
                    ch_l "Что?"
                    ch_l ". . ."
                    $ Girl.Eyes = "down"
                    ch_l "Ох, они порвались."
                    $ Girl.Eyes = "normal"
            elif Girl is JeanX:
                    ch_j "Пфф, придется искать новую пару."
            elif Girl is StormX:
                    ch_s "Похоже, они не пригодны для боя."
            elif Girl is JubesX:
                    ch_v "Теперь я вампир и гот. . ."
            elif Girl is GwenX:
                    ch_g "И как так получилось. . ."
            elif Girl is BetsyX:
                    ch_b "Какой ужас!"
            elif Girl is DoreenX:
                    ch_d "Ох, какое безумие!"
            elif Girl is WandaX:
                    ch_w "Они уже были изрядно потрепаны!"
            $ Girl.Inventory.append(Girl.Hose)

        if Count:
                #If they ripped
                if not Girl.Legs and Girl.Panties != "shorts":
                        if Girl is StormX and StormX in Rules:
                            #Storm don't care
                            pass
                        elif Girl.Panties:
                            if Girl.SeenPanties:
                                $ Count = 3 if not ApprovalCheck(Girl, 600) else Count
                            else:
                                $ Girl.SeenPanties = 1
                                $ Count = 3 if not ApprovalCheck(Girl, 900) else Count
                            $ Girl.Statup("Lust", 60, 2)
                        else:
                            if Girl.SeenPussy:
                                $ Count = 3 if not ApprovalCheck(Girl, 900) else Count
                            else:
                                call Girl_First_Bottomless(RogueX)
                                $ Count = 3 if not ApprovalCheck(Girl, 1400) else Count

                if Count != 3:
                        $ Girl.AddWord(1,"ripped","ripped")

                if Count == 2:
                        #first time
                        menu:
                            extend ""
                            "Я думаю, они тебе очень идут.":
                                $ Girl.FaceChange("smile", 1)
                                if Girl is RogueX:
                                        ch_r "Правда? Это так мило, может быть, я приберегу их на потом."
                                elif Girl is KittyX:
                                        ch_k "Ох, ты правда так думаешь? Думаю, я могу оставить их себе."
                                elif Girl is EmmaX:
                                        ch_e "Ох, нравится, когда я выгляжу потрепанной?"
                                elif Girl is LauraX:
                                        ch_l "Наверное так."
                                elif Girl is JeanX:
                                        ch_j "Ох, тебе нравится, когда я потрепанная?"
                                elif Girl is StormX:
                                        ch_s "Полагаю, что так. . ."
                                elif Girl is JubesX:
                                        ch_v "Наверное. . ."
                                elif Girl is GwenX:
                                        ch_g "Правда? . ."
                                elif Girl is BetsyX:
                                        ch_b "Скорее, похожа на \"панка.\""
                                elif Girl is DoreenX:
                                        ch_d "Но они такие \"рваные.\" . ."
                                elif Girl is WandaX:
                                        ch_w "Да? Нравятся вещи на выброс?"

                            "Ага, очень плохо.":
                                $ Girl.FaceChange("bemused")
                                if Girl is RogueX:
                                        ch_r ". . ."
                                elif Girl is KittyX:
                                        if not Player.Male:
                                            ch_k ". . . могла бы и пожалеть. . ."
                                        else:
                                            ch_k ". . . мог бы и пожалеть. . ."
                                elif Girl is EmmaX:
                                        ch_e ". . . да. . ."
                                elif Girl is LauraX:
                                        pass
                                elif Girl is JeanX:
                                        ch_j "Верно?"
                                elif Girl is StormX:
                                        ch_s "Ясно."
                                elif Girl is JubesX:
                                        ch_v "Пожалуй. . ."
                                elif Girl is GwenX:
                                        if not Player.Male:
                                            ch_g "Могла бы и пожалеть меня."
                                        else:
                                            ch_g "Мог бы и пожалеть меня."
                                elif Girl is BetsyX:
                                        ch_b "А ты знаешь, сколько они стоят?"
                                elif Girl is DoreenX:
                                        ch_d "Но я -только недавно- их купила. . ."
                                elif Girl is WandaX:
                                        ch_w "Одной дырой меньше-одной больше, какая разница?"

                            "Ха! Да они же теперь ничего не прикрывают!":
                                if Girl is RogueX:
                                        ch_r "Спасибо. . ."
                                elif Girl is KittyX:
                                        ch_k "А ты, похоже, не шутишь."
                                elif Girl is EmmaX:
                                        ch_e "Уверена, тебе это нравится. . ."
                                elif Girl is LauraX:
                                        ch_l "Думаю, так и есть."
                                elif Girl is JeanX:
                                        ch_j "Ох, наверное."
                                elif Girl is StormX:
                                        if not Player.Male:
                                            ch_s "Возможно, ты права насчет этого. . ."
                                        else:
                                            ch_s "Возможно, ты прав насчет этого. . ."
                                elif Girl is JubesX:
                                        ch_v ". . . ага. . ."
                                elif Girl is GwenX:
                                        ch_g "Ты говоришь очевидные вещи."
                                elif Girl is BetsyX:
                                        ch_b "Безусловно!"
                                elif Girl is DoreenX:
                                        ch_d "Ох, ага. . ."
                                elif Girl is WandaX:
                                        ch_w "Ага, я тебя поняла. . ."


                elif Count == 3: #She is embarrassed and takes off
                    $ Girl.FaceChange("startled", 2)
                    if D20 > 15:
                            call AnyLine(Girl,"!!!")
                    elif Girl is RogueX:
                            ch_r "Я. . . эм. . . Мне нужно уйти."
                    elif Girl is KittyX:
                            ch_k "Я. . . к такому была не готова. . ."
                    elif Girl is EmmaX:
                            $ Girl.FaceChange("sexy", 1)
                            ch_e "Меня могут неправильно понять, пожалуй, мне стоит переодеться. . ."
                    elif Girl is LauraX:
                            $ Girl.FaceChange("perplexed", 0)
                            ch_l "Думаю, мне стоит переодеться во что-нибудь другое."
                    elif Girl is JeanX:
                            ch_j "Пойду переоденусь. . ."
                    elif Girl is StormX:
                            $ Girl.FaceChange("bemused", 0)
                            ch_s "Пожалуй, мне стоит переодеться."
                    elif Girl is JubesX:
                            ch_v "Мне срочно нужно переодеться. . ."
                    elif Girl is GwenX:
                            ch_g "Эм, пока-пока."
                    elif Girl is BetsyX:
                            ch_b "Мне срочно нужно переодеться во что-то другое."
                    elif Girl is DoreenX:
                            ch_d "Иу!"
                    elif Girl is WandaX:
                            ch_w "Я, эм, сейчас вернусь. . ."
                    $ Girl.Blush = 1
                    call Remove_Girl(Girl)
                    $ Girl.OutfitChange()
                #end "if they ripped"
        return

# End ripped tights / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Clear_Offhands(BO=[]):
        # Clears out offhand actions for every girl
        $ BO = ActiveGirls[:]
        python:
            for BX in BO:
                BX.Offhand = 0
        return

label Girls_Noticed_Nearby(Girl=Primary,GirlCount=0,B=0,BO=[]): #rkeljsvgb
        # Called by Sex_Dialog or Girls_Taboo
        # Girl is lead girl, Other is a girl who notices you
        # if Silent, no dialog plays, B is a carried bonus value.
        if not Girl or Girl not in TotalGirls:
                        "Tell Oni that in noticed, no primary is set."
                        return
        $ BO = Nearby[:]
        if Girl in BO:
                $ BO.remove(Girl)
        python:
            for BX in BO:
                if "noticed " + Girl.Tag in BX.RecentActions:
                        pass
                else:
                        BX.RecentActions.append("noticed " + Girl.Tag)

                        if "poly " + Girl.Tag in BX.Traits or (Girl in Player.Harem and BX in Player.Harem):
                                #if they already have a relationship. . .
                                B = (1000-(20*Taboo))
                        else:
                                #if they don't have a relationship. . .
                                B = (BX.GirlLikeCheck(Girl) - 500) #RogueX.LikeLaura - 500
                                if BX in Player.Harem:
                                        #if you and the other girl have a relationship. . .
                                        B -= 200

                        if not Player.Male and "girltalk" not in BX.History and "nogirls" not in BX.History:
                                    #if you're a girl and she hasn't clocked you yet
                                    BX.AddWord(1,0,0,"intome") #trait

                        GirlCount += 1
                        BX.Facing = 0 #turns to look at you

        if GirlCount:
                if bg_current == "bg classroom":
                        "Несколько других девочек в аудитории замечают, чем вы занимаетесь."
                else:
                        "Несколько других девочек вокруг замечают, чем вы занимаетесь."
                $ GirlCount = 0

        #reactions
        $ BO = Nearby[:]
        if Girl in BO:
                $ BO.remove(Girl)
        python:
            for BX in BO:
                if ApprovalCheck(BX, 2000, TabM=2, Bonus = B) or ApprovalCheck(BX, 950, "LI", TabM=2):
                            #if she's very loose or really likes you
                            BX.FaceChange("sexy", 1)
                            GirlCount += 1
                            BX.Statup("Obed", 90, 5)
                            BX.Statup("Inbt", 90, 5)
                            BX.Statup("Lust", 90, 3)
                elif (ApprovalCheck(BX, 650, "I", TabM=2) and ApprovalCheck(BX, 450, "L", TabM=1)) or ApprovalCheck(BX, 800, "I",Alt=[[GwenX],300], TabM=2, Bonus = (B/3)):
                            #if she likes you, but is very uninhibited
                            BX.FaceChange("sexy")
                            GirlCount += 1
                            BX.Statup("Love", 90, 5)
                            BX.Statup("Obed", 90, 2)
                            BX.Statup("Inbt", 90, 2)
                            BX.Statup("Lust", 90, 5)
                elif ApprovalCheck(BX, 1500, TabM=2, Bonus = B):
                            BX.FaceChange("perplexed", 1)
                            GirlCount += 1
                            if BX.Love >= BX.Obed and BX.Love >= BX.Inbt:
                                BX.Statup("Obed", 90, 2)
                                BX.Statup("Inbt", 90, 2)
                            elif BX.Obed >= BX.Inbt:
                                BX.Statup("Love", 90, 2)
                                BX.Statup("Inbt", 90, 2)
                            else:
                                BX.Statup("Love", 90, 2)
                                BX.Statup("Obed", 90, 1)
                                BX.Statup("Inbt", 90, 1)
                            BX.Statup("Lust", 90, 5)
                elif ApprovalCheck(BX, 650, "L", TabM=1) or ApprovalCheck(BX, 400, "O", TabM=2):
                            #if she likes you or is obedient, but not enough
                            BX.FaceChange("angry", 2)
                            BX.Statup("Love", 200, -5)
                            BX.Statup("Love", 80, -5)
                            BX.Statup("Love", 70, -5)
                            BX.Statup("Obed", 90, -5)
                            BX.Statup("Lust", 89, 10)
                            BX.AddWord(1,0,0,"saw with " + Girl.Tag)
                            BX.Facing = 1 #turns to look at you
                else:
                            #if she doesn't like you much
                            BX.FaceChange("surprised", 2)
                            BX.Statup("Inbt", 90, 2)
                            BX.Statup("Lust", 40, 20)
                            if Trigger != "kiss you":
                                    BX.Statup("Love", 90, -10)
                                    BX.Statup("Obed", 90, -5)
                                    BX.Statup("Lust", 80, 10)
                            BX.Facing = 1 #turns to look at you
        if GirlCount:
                if bg_current == "bg classroom":
                        "Кое-кто, похоже, ерзает на своих местах."
                else:
                        "Кое-кто, похоже, наслаждается."
        return

label Girl_Select(Intro_Line="Кто эта девушка?"):
        #"Girl" must be defined by prior function, Intro line is what is asked of the player.
        menu:
            "[Intro_Line]"
            "Роуг":
                    $ Girl = RogueX
            "Китти":
                    $ Girl = KittyX
            "Эмма":
                    $ Girl = EmmaX
            "Лора":
                    $ Girl = LauraX
            "Джин":
                    $ Girl = JeanX
            "Шторм":
                    $ Girl = StormX
            "Джубс":
                    $ Girl = JubesX
            "Гвен":
                    $ Girl = GwenX
            "Бетси":
                    $ Girl = BetsyX
            "Дорин":
                    $ Girl = DoreenX
            "Ванда":
                    $ Girl = WandaX
        return

label cheats:
        "И вот вы здесь. Добро пожаловать в чит-меню."
        "Здесь можно добавить очки опыта, деньги и изменить отношение девушек к себе."
        "Наслаждайтесь."
        while True:
            menu:
                "+100$":
                    "Получите и распишитесь, грязный читер."
                    $ Player.Cash += 100
                "+500$":
                    "Получите и распишитесь, грязный читер."
                    $ Player.Cash += 500
                "+1000$":
                    "Получите и распишитесь, грязный читер."
                    $ Player.Cash += 1000
                "Не мгновенные +100 ОО":
                    "Придет время и вы получите свой опыт, мой маленький читер."
                    $ Player.XP += 100
                "Не мгновенные +500 ОО":
                    "Придет время и вы получите свой опыт, мой маленький читер."
                    $ Player.XP += 500
                "Сброс сохраненых нарядов девушек":
                        call Emergency_Clothing_Reset
                "Выставление прозвищ гг на значение \"по-умолчанию\".":
                    menu:
                        "Роуг":
                            if Player.Male:
                                $ RogueX.Petname = "сладенький"
                                $ RogueX.Petname_rod = "сладенького"
                                $ RogueX.Petname_dat = "сладенькому"
                                $ RogueX.Petname_vin = "сладенького"
                                $ RogueX.Petname_tvo = "сладеньким"
                                $ RogueX.Petname_pre = "сладеньком"
                            else:
                                $ RogueX.Petname = "сладенькая"
                                $ RogueX.Petname_rod = "сладенькой"
                                $ RogueX.Petname_dat = "сладенькой"
                                $ RogueX.Petname_vin = "сладенькую"
                                $ RogueX.Petname_tvo = "сладенькой"
                                $ RogueX.Petname_pre = "сладенькой"
                        "Китти" if "met" in KittyX.History:
                            $ KittyX.Petname = Player.Name[:1]
                            $ KittyX.Petname_rod = Player.Name[:1]
                            $ KittyX.Petname_dat = Player.Name[:1]
                            $ KittyX.Petname_vin = Player.Name[:1]
                            $ KittyX.Petname_tvo = Player.Name[:1]
                            $ KittyX.Petname_pre = Player.Name[:1]
                        "Лора" if "met" in LauraX.History:
                            $ LauraX.Petname = Player.Name
                            $ LauraX.Petname_rod = Player.Name_rod
                            $ LauraX.Petname_dat = Player.Name_dat
                            $ LauraX.Petname_vin = Player.Name_vin
                            $ LauraX.Petname_tvo = Player.Name_tvo
                            $ LauraX.Petname_pre = Player.Name_pre
                        "Эмма" if "met" in EmmaX.History:
                            $ EmmaX.Petname = Player.Name
                            $ EmmaX.Petname_rod = Player.Name_rod
                            $ EmmaX.Petname_dat = Player.Name_dat
                            $ EmmaX.Petname_vin = Player.Name_vin
                            $ EmmaX.Petname_tvo = Player.Name_tvo
                            $ EmmaX.Petname_pre = Player.Name_pre
                        "Шторм" if "met" in StormX.History:
                            $ StormX.Petname = Player.Name
                            $ StormX.Petname_rod = Player.Name_rod
                            $ StormX.Petname_dat = Player.Name_dat
                            $ StormX.Petname_vin = Player.Name_vin
                            $ StormX.Petname_tvo = Player.Name_tvo
                            $ StormX.Petname_pre = Player.Name_pre
                        "Джубили" if "met" in JubesX.History:
                            if Player.Male:
                                $ JubesX.Petname = "бро"
                                $ JubesX.Petname_rod = "бро"
                                $ JubesX.Petname_dat = "бро"
                                $ JubesX.Petname_vin = "бро"
                                $ JubesX.Petname_tvo = "бро"
                                $ JubesX.Petname_pre = "бро"
                            else:
                                $ JubesX.Petname = "сис"
                                $ JubesX.Petname_rod = "сис"
                                $ JubesX.Petname_dat = "сис"
                                $ JubesX.Petname_vin = "сис"
                                $ JubesX.Petname_tvo = "сис"
                                $ JubesX.Petname_pre = "сис"
                        "Гвен" if "met" in GwenX.History:
                            if Player.Male:
                                $ GwenX.Petname = "чувак"
                                $ GwenX.Petname_rod = "чувака"
                                $ GwenX.Petname_dat = "чуваку"
                                $ GwenX.Petname_vin = "чувака"
                                $ GwenX.Petname_tvo = "чуваком"
                                $ GwenX.Petname_pre = "чуваке"
                            else:
                                $ GwenX.Petname = "чувиха"
                                $ GwenX.Petname_rod = "чувихи"
                                $ GwenX.Petname_dat = "чувихе"
                                $ GwenX.Petname_vin = "чувиху"
                                $ GwenX.Petname_tvo = "чувихой"
                                $ GwenX.Petname_pre = "чувихе"
                        "Бетси" if "met" in BetsyX.History:
                            $ BetsyX.Petname = Player.Name
                            $ BetsyX.Petname_rod = Player.Name_rod
                            $ BetsyX.Petname_dat = Player.Name_dat
                            $ BetsyX.Petname_vin = Player.Name_vin
                            $ BetsyX.Petname_tvo = Player.Name_tvo
                            $ BetsyX.Petname_pre = Player.Name_pre
                        "Дорин" if "met" in DoreenX.History:
                            if Player.Male:
                                $ DoreenX.Petname = "чувак"
                                $ DoreenX.Petname_rod = "чувака"
                                $ DoreenX.Petname_dat = "чуваку"
                                $ DoreenX.Petname_vin = "чувака"
                                $ DoreenX.Petname_tvo = "чуваком"
                                $ DoreenX.Petname_pre = "чуваке"
                            else:
                                $ DoreenX.Petname = "чувиха"
                                $ DoreenX.Petname_rod = "чувихи"
                                $ DoreenX.Petname_dat = "чувихе"
                                $ DoreenX.Petname_vin = "чувиху"
                                $ DoreenX.Petname_tvo = "чувихой"
                                $ DoreenX.Petname_pre = "чувихе"
                        "Ванда" if "met" in WandaX.History:
                            if Player.Male:
                                $ WandaX.Petname = "бро"
                                $ WandaX.Petname_rod = "бро"
                                $ WandaX.Petname_dat = "бро"
                                $ WandaX.Petname_vin = "бро"
                                $ WandaX.Petname_tvo = "бро"
                                $ WandaX.Petname_pre = "бро"
                            else:
                                $ WandaX.Petname = "сис"
                                $ WandaX.Petname_rod = "сис"
                                $ WandaX.Petname_dat = "сис"
                                $ WandaX.Petname_vin = "сис"
                                $ WandaX.Petname_tvo = "сис"
                                $ WandaX.Petname_pre = "сис"
                "Изменить отношение девушек к себе":
                    menu:
                        "Выберите девушку. . . Одно нажатие на стат изменяет его значение на 100."
                        "Роуг":
                            label rogue_menu:
                            menu:
                                "Повысить любовь":
                                    $ RogueX.Love += 100
                                    jump rogue_menu
                                "Понизить любовь":
                                    $ RogueX.Love -= 100
                                    jump rogue_menu
                                "Повысить повиновение":
                                    $ RogueX.Obed += 100
                                    jump rogue_menu
                                "Понизить повиновение":
                                    $ RogueX.Obed -= 100
                                    jump rogue_menu
                                "Повысить раскрепощенность":
                                    $ RogueX.Inbt += 100
                                    jump rogue_menu
                                "Понизить раскрепощенность":
                                    $ RogueX.Inbt -= 100
                                    jump rogue_menu
                                "Повысить зависимость":
                                    $ RogueX.Addict += 10
                                    jump rogue_menu
                                "Понизить зависимость":
                                    $ RogueX.Addict -= 10
                                    jump rogue_menu
                                "Назад":
                                    pass
                        "Китти" if "met" in KittyX.History:
                            label kitty_menu:
                            menu:
                                "Повысить любовь":
                                    $ KittyX.Love += 100
                                    jump kitty_menu
                                "Понизить любовь":
                                    $ KittyX.Love -= 100
                                    jump kitty_menu
                                "Повысить повиновение":
                                    $ KittyX.Obed += 100
                                    jump kitty_menu
                                "Понизить повиновение":
                                    $ KittyX.Obed -= 100
                                    jump kitty_menu
                                "Повысить раскрепощенность":
                                    $ KittyX.Inbt += 100
                                    jump kitty_menu
                                "Понизить раскрепощенность":
                                    $ KittyX.Inbt -= 100
                                    jump kitty_menu
                                "Повысить зависимость":
                                    $ KittyX.Addict += 10
                                    jump kitty_menu
                                "Понизить зависимость":
                                    $ KittyX.Addict -= 10
                                    jump kitty_menu
                                "Назад":
                                    pass
                        "Лора" if "met" in LauraX.History:
                            label laura_menu:
                            menu:
                                "Повысить любовь":
                                    $ LauraX.Love += 100
                                    jump laura_menu
                                "Понизить любовь":
                                    $ LauraX.Love -= 100
                                    jump laura_menu
                                "Повысить повиновение":
                                    $ LauraX.Obed += 100
                                    jump laura_menu
                                "Понизить повиновение":
                                    $ LauraX.Obed -= 100
                                    jump laura_menu
                                "Повысить раскрепощенность":
                                    $ LauraX.Inbt += 100
                                    jump laura_menu
                                "Понизить раскрепощенность":
                                    $ LauraX.Inbt -= 100
                                    jump laura_menu
                                "Повысить зависимость":
                                    $ LauraX.Addict += 10
                                    jump laura_menu
                                "Понизить зависимость":
                                    $ LauraX.Addict -= 10
                                    jump laura_menu
                                "Назад":
                                    pass
                        "Эмма" if "met" in EmmaX.History:
                            label emma_menu:
                            menu:
                                "Повысить любовь":
                                    $ EmmaX.Love += 100
                                    jump emma_menu
                                "Понизить любовь":
                                    $ EmmaX.Love -= 100
                                    jump emma_menu
                                "Повысить повиновение":
                                    $ EmmaX.Obed += 100
                                    jump emma_menu
                                "Понизить повиновение":
                                    $ EmmaX.Obed -= 100
                                    jump emma_menu
                                "Повысить раскрепощенность":
                                    $ EmmaX.Inbt += 100
                                    jump emma_menu
                                "Понизить раскрепощенность":
                                    $ EmmaX.Inbt -= 100
                                    jump emma_menu
                                "Повысить зависимость":
                                    $ EmmaX.Addict += 10
                                    jump emma_menu
                                "Понизить зависимость":
                                    $ EmmaX.Addict -= 10
                                    jump emma_menu
                                "Назад":
                                    pass
                        "Джин" if "met" in JeanX.History:
                            label jean_menu:
                            menu:
                                "Повысить любовь":
                                    $ JeanX.Love += 100
                                    jump jean_menu
                                "Понизить любовь":
                                    $ JeanX.Love -= 100
                                    jump jean_menu
                                "Повысить повиновение":
                                    $ JeanX.Obed += 100
                                    jump jean_menu
                                "Понизить повиновение":
                                    $ JeanX.Obed -= 100
                                    jump jean_menu
                                "Повысить раскрепощенность":
                                    $ JeanX.Inbt += 100
                                    jump jean_menu
                                "Понизить раскрепощенность":
                                    $ JeanX.Inbt -= 100
                                    jump jean_menu
                                "Повысить зависимость":
                                    $ JeanX.Addict += 10
                                    jump jean_menu
                                "Понизить зависимость":
                                    $ JeanX.Addict -= 10
                                    jump jean_menu
                                "Назад":
                                    pass
                        "Шторм" if "met" in StormX.History:
                            label storm_menu:
                            menu:
                                "Повысить любовь":
                                    $ StormX.Love += 100
                                    jump storm_menu
                                "Понизить любовь":
                                    $ StormX.Love -= 100
                                    jump storm_menu
                                "Повысить повиновение":
                                    $ StormX.Obed += 100
                                    jump storm_menu
                                "Понизить повиновение":
                                    $ StormX.Obed -= 100
                                    jump storm_menu
                                "Повысить раскрепощенность":
                                    $ StormX.Inbt += 100
                                    jump storm_menu
                                "Понизить раскрепощенность":
                                    $ StormX.Inbt -= 100
                                    jump storm_menu
                                "Повысить зависимость":
                                    $ StormX.Addict += 10
                                    jump storm_menu
                                "Понизить зависимость":
                                    $ StormX.Addict -= 10
                                    jump storm_menu
                                "Назад":
                                    pass
                        "Джубили" if "met" in JubesX.History:
                            label jubes_menu:
                            menu:
                                "Повысить любовь":
                                    $ JubesX.Love += 100
                                    jump jubes_menu
                                "Понизить любовь":
                                    $ JubesX.Love -= 100
                                    jump jubes_menu
                                "Повысить повиновение":
                                    $ JubesX.Obed += 100
                                    jump jubes_menu
                                "Понизить повиновение":
                                    $ JubesX.Obed -= 100
                                    jump jubes_menu
                                "Повысить раскрепощенность":
                                    $ JubesX.Inbt += 100
                                    jump jubes_menu
                                "Понизить раскрепощенность":
                                    $ JubesX.Inbt -= 100
                                    jump jubes_menu
                                "Повысить зависимость":
                                    $ JubesX.Addict += 10
                                    jump jubes_menu
                                "Понизить зависимость":
                                    $ JubesX.Addict -= 10
                                    jump jubes_menu
                                "Назад":
                                    pass
                        "Гвен" if "met" in GwenX.History:
                            label gwen_menu:
                            menu:
                                "Повысить любовь":
                                    $ GwenX.Love += 100
                                    jump gwen_menu
                                "Понизить любовь":
                                    $ GwenX.Love -= 100
                                    jump gwen_menu
                                "Повысить повиновение":
                                    $ GwenX.Obed += 100
                                    jump gwen_menu
                                "Понизить повиновение":
                                    $ GwenX.Obed -= 100
                                    jump gwen_menu
                                "Повысить раскрепощенность":
                                    $ GwenX.Inbt += 100
                                    jump gwen_menu
                                "Понизить раскрепощенность":
                                    $ GwenX.Inbt -= 100
                                    jump gwen_menu
                                "Повысить зависимость":
                                    $ GwenX.Addict += 10
                                    jump gwen_menu
                                "Понизить зависимость":
                                    $ GwenX.Addict -= 10
                                    jump gwen_menu
                                "Назад":
                                    pass
                        "Бетси" if "met" in BetsyX.History:
                            label betsy_menu:
                            menu:
                                "Повысить любовь":
                                    $ BetsyX.Love += 100
                                    jump betsy_menu
                                "Понизить любовь":
                                    $ BetsyX.Love -= 100
                                    jump betsy_menu
                                "Повысить повиновение":
                                    $ BetsyX.Obed += 100
                                    jump betsy_menu
                                "Понизить повиновение":
                                    $ BetsyX.Obed -= 100
                                    jump betsy_menu
                                "Повысить раскрепощенность":
                                    $ BetsyX.Inbt += 100
                                    jump betsy_menu
                                "Понизить раскрепощенность":
                                    $ BetsyX.Inbt -= 100
                                    jump betsy_menu
                                "Повысить зависимость":
                                    $ BetsyX.Addict += 10
                                    jump betsy_menu
                                "Понизить зависимость":
                                    $ BetsyX.Addict -= 10
                                    jump betsy_menu
                                "Назад":
                                    pass
                        "Дорин" if "met" in DoreenX.History:
                            label doreen_menu:
                            menu:
                                "Повысить любовь":
                                    $ DoreenX.Love += 100
                                    jump doreen_menu
                                "Понизить любовь":
                                    $ DoreenX.Love -= 100
                                    jump doreen_menu
                                "Повысить повиновение":
                                    $ DoreenX.Obed += 100
                                    jump doreen_menu
                                "Понизить повиновение":
                                    $ DoreenX.Obed -= 100
                                    jump doreen_menu
                                "Повысить раскрепощенность":
                                    $ DoreenX.Inbt += 100
                                    jump doreen_menu
                                "Понизить раскрепощенность":
                                    $ DoreenX.Inbt -= 100
                                    jump doreen_menu
                                "Повысить зависимость":
                                    $ DoreenX.Addict += 10
                                    jump doreen_menu
                                "Понизить зависимость":
                                    $ DoreenX.Addict -= 10
                                    jump doreen_menu
                                "Назад":
                                    pass
                        "Ванда" if "met" in WandaX.History:
                            label wanda_menu:
                            menu:
                                "Повысить любовь":
                                    $ WandaX.Love += 100
                                    jump wanda_menu
                                "Понизить любовь":
                                    $ WandaX.Love -= 100
                                    jump wanda_menu
                                "Повысить повиновение":
                                    $ WandaX.Obed += 100
                                    jump wanda_menu
                                "Понизить повиновение":
                                    $ WandaX.Obed -= 100
                                    jump wanda_menu
                                "Повысить раскрепощенность":
                                    $ WandaX.Inbt += 100
                                    jump wanda_menu
                                "Понизить раскрепощенность":
                                    $ WandaX.Inbt -= 100
                                    jump wanda_menu
                                "Повысить зависимость":
                                    $ WandaX.Addict += 10
                                    jump wanda_menu
                                "Понизить зависимость":
                                    $ WandaX.Addict -= 10
                                    jump wanda_menu
                                "Назад":
                                    pass
                        "Назад":
                                pass
                "Назад":
                            return
