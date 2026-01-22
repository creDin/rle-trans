# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.


##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False, CountWords = 0): #CountWords is just a counter used with the gag

    # Decide if we want to use the one-window or two-window variant.

    if who == "N":
            $ who = Ch_Focus.Name

    if not two_window:
        # The one window variant. Used for caption boxes
        window:
#            xpos 0.0
#            xanchor 0.0

            pos (0.0,0.1) #(0.3,0.1)
            anchor (0.0,0.0)

            style "textbox"

            id "textbox"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what" color "#000000" font "CRIMFBRG.ttf"
            #text what id "what"
    else:
        # The two window variant. Used for character dialog
        # start gag code
        if who == "Rogue" and RogueX.Gag:
            $ CountWords = 1
        elif who == "Kitty" and KittyX.Gag:
            $ CountWords = 1
        if CountWords == 1:
            $ CountWords = what.count(" ") if what.count(" ") <= 10 else 10
            $ CountWords = CountWords - what.count(".")
            $ what = ""
            python:
                while CountWords >= 0:
                    CountWords -= 1
                    what = what + renpy.random.choice(["Мпф",
                                                    "Хграф",
                                                    "Ргн",
                                                    "Ффф",
                                                    "Гефс",
                                                    "Фаха",
                                                    "Грр",
                                                    "Фраф",
                                                    "Уфф"])
                    if CountWords:
                        what = what + " "
                    else:
                        what = what + "."
        # End gag code

        vbox:
            #Main chat text window
#            pos (0.0,0.1) #(0.7,0.1)
#            anchor (0.0,0.0)#(1.0,0.0)
            pos (0.45,0.1) #(0.7,0.1)
            anchor (1.0,0.0)#(1.0,0.0)

            style "say_two_window_vbox"

            window:    #rkeljsvg
                    if who == GwenX.Name: #new code. . .
                        style "say_balloon" background Frame("images/WordballoonG.png", 50, 50)
                    else:
                        style "say_balloon"

#                    has vbox:
#                            style "say_balloon"

                    text what id "what" color "#000000" font "CRIMFBRG.ttf" text_align 0.5

            if who == RogueX.Name: #"Rogue":              #rkeljsvg
                    if RogueX.Loc != bg_current or RogueX.SpriteLoc == StageFarLeft:
                        add "arrow" xalign 0.1 #xzoom -1
                    elif RogueX.SpriteLoc == StageRight or RogueX.SpriteLoc == StageFarRight:
                        add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                    else: #RogueX.SpriteLoc == StageCenter, Left, etc.:
                        add "arrow" xalign 0.8
            elif who == KittyX.Name:
                    if KittyX.Loc != bg_current or KittyX.SpriteLoc == StageFarLeft:
                        add "arrow" xalign 0.1 #xzoom -1
                    elif KittyX.SpriteLoc == StageRight or KittyX.SpriteLoc == StageFarRight:
                        add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                    else: #KittyX.SpriteLoc == StageCenter, Left, etc.:
                        add "arrow" xalign 0.8
            elif who == EmmaX.Name:
                    if EmmaX.Loc != bg_current or EmmaX.SpriteLoc == StageFarLeft:
                        add "arrow" xalign 0.1 #xzoom -1
                    elif EmmaX.SpriteLoc == StageRight or EmmaX.SpriteLoc == StageFarRight:
                        add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                    else: #EmmaX.SpriteLoc == StageCenter, Left, etc.:
                        add "arrow" xalign 0.8
            elif who == LauraX.Name:
                    if LauraX.Loc != bg_current or LauraX.SpriteLoc == StageFarLeft:
                        add "arrow" xalign 0.1 #xzoom -1
                    elif LauraX.SpriteLoc == StageRight or LauraX.SpriteLoc == StageFarRight:
                        add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                    else: #LauraX.SpriteLoc == StageCenter, Left, etc.:
                        add "arrow" xalign 0.8
            elif who == JeanX.Name:
                    if JeanX.Loc != bg_current or JeanX.SpriteLoc == StageFarLeft:
                        add "arrow" xalign 0.1 #xzoom -1
                    elif JeanX.SpriteLoc == StageRight or JeanX.SpriteLoc == StageFarRight:
                        add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                    else: #JeanX.SpriteLoc == StageCenter, Left, etc.:
                        add "arrow" xalign 0.8
            elif who == StormX.Name:
                    if StormX.Loc != bg_current or StormX.SpriteLoc == StageFarLeft:
                        add "arrow" xalign 0.1 #xzoom -1
                    elif StormX.SpriteLoc == StageRight or StormX.SpriteLoc == StageFarRight:
                        add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                    else: #StormX.SpriteLoc == StageCenter, Left, etc.:
                        add "arrow" xalign 0.8
            elif who == JubesX.Name:
                    if JubesX.Loc != bg_current or JubesX.SpriteLoc == StageFarLeft:
                        add "arrow" xalign 0.1 #xzoom -1
                    elif JubesX.SpriteLoc == StageRight or JubesX.SpriteLoc == StageFarRight:
                        add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                    else: #JubesX.SpriteLoc == StageCenter, Left, etc.:
                        add "arrow" xalign 0.8
            elif who == GwenX.Name:
                    if GwenX.Loc != bg_current or GwenX.SpriteLoc == StageFarLeft:
                        add "arrowG" xalign 0.1 #xzoom -1
                    elif GwenX.SpriteLoc == StageRight or GwenX.SpriteLoc == StageFarRight:
                        add "arrowG" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                    else: #GwenX.SpriteLoc == StageCenter, Left, etc.:
                        add "arrowG" xalign 0.8
            elif who == BetsyX.Name:
                    if BetsyX.Loc != bg_current or BetsyX.SpriteLoc == StageFarLeft:
                        add "arrow" xalign 0.1 #xzoom -1
                    elif BetsyX.SpriteLoc == StageRight or BetsyX.SpriteLoc == StageFarRight:
                        add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                    else: #BetsyX.SpriteLoc == StageCenter, Left, etc.:
                        add "arrow" xalign 0.8
            elif who == DoreenX.Name:
                    if DoreenX.Loc != bg_current or DoreenX.SpriteLoc == StageFarLeft:
                        add "arrow" xalign 0.1 #xzoom -1
                    elif DoreenX.SpriteLoc == StageRight or DoreenX.SpriteLoc == StageFarRight:
                        add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                    else: #DoreenX.SpriteLoc == StageCenter, Left, etc.:
                        add "arrow" xalign 0.8
            elif who == WandaX.Name:
                    if WandaX.Loc != bg_current or WandaX.SpriteLoc == StageFarLeft:
                        add "arrow" xalign 0.1 #xzoom -1
                    elif WandaX.SpriteLoc == StageRight or WandaX.SpriteLoc == StageFarRight:
                        add "arrow" rotate -90 xzoom -1 xpos 1.03 ypos -0.85
                    else: #WandaX.SpriteLoc == StageCenter, Left, etc.:
                        add "arrow" xalign 0.8
            elif who == Player.Name or who == "Комната Опасности": #elif who == Playername or who == "Danger Room":
                    pass
            elif who == "Профессор Икс":
                    add "arrow" xalign 0.4
            elif who:
                    add "arrow" xalign 0.8

        if who:
            # this block is the name tag
            window:
                    pos (0.4,0.07) #(0.65,0.07)
                    anchor (0.5,0)#(0.5,0.5)
                    style "say_who_window"
#                    background Frame("images/WordballoonG.png", 50, 50)

                    text who:
                        size 15
                        id "who"
                        font "CRIMFBRG.ttf"

    # Use the quick menu.
    use quick_menu


image side arrow = "arrow"

image arrow:
    "images/Arrow.png"
    ypos -17
    xalign 0.5 #0.9
    zoom 1
    rotate 0

image arrowG:
    "images/ArrowG.png"
    ypos -17
    xalign 0.5 #0.9
    zoom 1
    rotate 0

##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xpos 20
        ypos 0.3
        yanchor 0.0
        xysize (310,530)
        viewport:
            yinitial 0


            if renpy.mobile:
                scrollbars "vertical"
            arrowkeys True
            mousewheel True
            draggable True

            side_yfill True
            vbox:
                style "menu"
                spacing 2

                for caption, action, chosen in items:

                    if action:
                        if " (locked)" in caption:
                            $ caption = caption.replace(" (locked)", "")
                            button:
                                action None
                                style "menu_choice_button"
                                background "#424242"
                                text caption style "menu_choice" color "#6E6E6E"



                        else:               #to fix, just make this the default of "if action"
                            button:
                                action action
                                style "menu_choice_button"

                                text caption style "menu_choice"

                    else:
                        text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True
    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.30) #* 0.45)
        xmaximum int(config.screen_width * 0.30)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt" color "#000000" size 20
        input id "input" style "input_text" color "#6E6E6E" size 25

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"
    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Начать игру") action Start()
        textbutton _("Загрузить игру") action ShowMenu("load")
        textbutton _("Настройки") action ShowMenu("preferences")
        textbutton _("Помощь") action Help()
        textbutton _("Дисклеймер") action Show("Disclaimer_screen")
        textbutton _("Patreon") action OpenURL("http://www.patreon.com/OniArtist")
        textbutton _("Выйти") action Quit(confirm=False)

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Назад") action Return()
        textbutton _("Настройки") action ShowMenu("preferences")
        textbutton _("Сохранить игру") action ShowMenu("save")
        textbutton _("Загрузить игру") action ShowMenu("load")
        textbutton _("Главное меню") action MainMenu()
        textbutton _("Помощь") action Help()
        textbutton _("Выйти") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Пред"):
                action FilePagePrevious()

            textbutton _("Авто"):
                action FilePage("auto")

            textbutton _("Быстр"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("След"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Пустой слот."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Экран")
                textbutton _("В окне") action Preference("display", "window")
                textbutton _("Во весь экран") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Переходы")
                textbutton _("Все") action Preference("transitions", "all")
                textbutton _("Нет") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Скорость текста")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Геймпад...") action Preference("joystick")

            frame: #cock transparency
                style_group "pref"
                has vbox

                label _("Прозрачность элементов")
                if AlphaCock:
                    textbutton _("Полупрозрачные") action SetVariable("AlphaCock", 0)
                else:
                    textbutton _("Непрозрачные") action SetVariable("AlphaCock", 1)

            frame: #Autoclean-up
                style_group "pref"
                has vbox

                label _("Очистка Игрока")
                if CleanUp:
                        textbutton _("Сперва спрашивать") action SetVariable("CleanUp", 0)
                else:
                        textbutton _("Всегда очищать") action SetVariable("CleanUp", 1) #hovered tt.Action("Girls will clean you up without asking. Only applies if they have high obedience.")

            frame: #Autoclean-up
                style_group "pref"
                has vbox

                label _("Очистка Девушки")
                textbutton _("Случайно") action SetVariable("CleanUpDefault", 0)
                textbutton _("Всегда сперва спрашивать") action SetVariable("CleanUpDefault","ask")
                textbutton _("Всегда очищать") action SetVariable("CleanUpDefault","clean")
                textbutton _("Всегда оставлять \"грязь\"") action SetVariable("CleanUpDefault","leave")
                textbutton _("Партнерша должна очищать ее") action SetVariable("CleanUpDefault","partner wipe")
                textbutton _("Партнерша должна вылизывать ее") action SetVariable("CleanUpDefault","partner lick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Пропуск")
                textbutton _("Прочитанный текст") action Preference("skip", "seen")
                textbutton _("Весь текст") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Начать пропуск") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("После выборов")
                textbutton _("Остановить пропуск") action Preference("after choices", "stop")
                textbutton _("Продолжить пропуск") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Скорость авто перемотки текста")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

            frame: #Plot break
                style_group "pref"
                has vbox

                label _("Представлять новых девушек?")
                if PlotBreak:
                        textbutton _("Продолжить") action SetVariable("PlotBreak", 0)
                else:
                        textbutton _("Приостановить") action SetVariable("PlotBreak", 1)
#                textbutton _("Continue") action SetVariable("PlotBreak", 0)

        vbox:
            frame:
                style_group "pref"
                has vbox
                # label _("There is no Audio")

                label _("Громкость музыки")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Громкость звуков")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Тест"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Громкость голоса")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Тест"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Да") action yes_action
            textbutton _("Нет") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"

##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Назад") action Rollback()
        textbutton _("Сохр") action ShowMenu('save')
        textbutton _("Б.Сохр") action QuickSave()
        textbutton _("Б.Загр") action QuickLoad()
        textbutton _("Пропуск") action Skip()
        textbutton _("Б.Пропуск") action Skip(fast=True, confirm=True)
        textbutton _("Авто") action Preference("auto-forward", "toggle")
        textbutton _("Настр") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"


##############################################################################
# My Bullshit
#
# This is the random crap I've added
#

#begin Roguebutton
screen roguebutton:
    imagebutton:
        auto "images/Button_Rogue_%s.png"
        action ui.callsinnewcontext("RogueWardrobe")
        xpos 690
        ypos 5
        focus_mask True

#end roguebutton

#begin Statbutton
screen statbutton:
#    if True: #"Rogue" in Party or R_Loc == bg_current:
    imagebutton:
        auto "images/Button_Rogue_%s.png"
        action ui.calls("RogueStats") #works action ui.callsinnewcontext("RogueStats") #works
        xpos 730
        ypos 5
        focus_mask True

#end statbutton

#begin Inventory Button
screen Inventorybutton:
    imagebutton:
        auto "images/UI_Backpack_%s.png"
        action Show("Inventory_screen")
        xpos 780
        ypos 5
        focus_mask True

#end Inventory Button

#Begin Status screen:

image Alt_Screen_Mask:
    # giant green mask for the second girl's menu
    contains:
        Solid("#159457", xysize=(800,150))
        alpha .5
        pos (0,-20)

screen Status_Screen:

    default tt = Tooltip(" ")


    if Weekday == 0:
        $ DayofWeekRus = "Пн"
    elif Weekday == 6:
        $ DayofWeekRus = "Вс"
    elif Weekday == 1:
        $ DayofWeekRus = "Вт"
    elif Weekday == 2:
        $ DayofWeekRus = "Ср"
    elif Weekday == 3:
        $ DayofWeekRus = "Чт"
    elif Weekday == 4:
        $ DayofWeekRus = "Пт"
    else:
        $ DayofWeekRus = "Сб"


    if Time_Count == 0:
        $ Current_Time_Rus = "Утро"
    elif Time_Count == 1:
        $ Current_Time_Rus = "Полдень"
    elif Time_Count == 2:
        $ Current_Time_Rus = "Вечер"
    else:
        $ Current_Time_Rus = "Ночь"

    #Under bar
    if Partner in TotalGirls:
        frame:
            background None
            pos (-100,30)
#            add "Alt_Screen_Mask"
            add  AlphaMask("images/BarBackdrop_"+Partner.Tag+".png", "Alt_Screen_Mask")
            frame:
                style_group "stat_bar"
                pos (100,25)
                background None
                has vbox
                hbox:
                    imagebutton idle "images/iconlust.png" hover "images/iconlust.png" action NullAction() hovered tt.Action("Похоть: [Partner.Lust]")
                    bar range 100 value FieldValue(Partner, "Lust", 100) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0

                    imagebutton idle "images/iconlove.png" hover "images/iconlove.png" action NullAction() hovered tt.Action("Любовь: [Partner.Love]")
                    bar range 100 value FieldValue(Partner, "Love", 1000) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0

                    imagebutton idle "images/iconobed.png" hover "images/iconobed.png" action NullAction() hovered tt.Action("Повиновение: [Partner.Obed]") #action NullAction("none")?
                    bar range 100 value FieldValue(Partner, "Obed", 1000) xmaximum 100 left_bar "images/barfullO.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0

                    imagebutton idle "images/iconinbt.png" hover "images/iconinbt.png" action NullAction() hovered tt.Action("Раскрепощенность: [Partner.Inbt]")
                    bar range 100 value FieldValue(Partner, "Inbt", 1000) xmaximum 100 left_bar "images/barfulli.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0

    #end Under bar

    #Primary bar
    #Kitty's stats

    if UI_Focus in TotalGirls:
        add "images/BarBackdrop_"+UI_Focus.Tag+".png"
        frame:
            style_group "stat_bar"
            xminimum 130
            background None
            has vbox
            hbox:
                imagebutton idle "images/iconlove.png" hover "images/iconlove.png" action NullAction() hovered tt.Action("Любовь: [UI_Focus.Love]")
                bar range 100 value (UI_Focus.Love/10) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
            hbox:
                imagebutton idle "images/iconlust.png" hover "images/iconlust.png" action NullAction() hovered tt.Action("Похоть: [UI_Focus.Lust]")
                bar range 100 value UI_Focus.Lust xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
        frame:
            xminimum 130
            xpos 130
            background None
            has vbox
            hbox:
                imagebutton idle "images/iconobed.png" hover "images/iconobed.png" action NullAction() hovered tt.Action("Повиновение: [UI_Focus.Obed]")
                bar range 100 value (UI_Focus.Obed/10) xmaximum 100 left_bar "images/barfullO.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
            hbox:
                imagebutton idle "images/iconaddict.png" hover "images/iconaddict.png" action NullAction() hovered tt.Action("Зависимость: [UI_Focus.Addict]")
                bar range 100 value UI_Focus.Addict xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 6 thumb None thumb_offset 0
        frame:
            xminimum 130
            xpos 260
            background None
            has vbox
            hbox:
                imagebutton idle "images/iconinbt.png" hover "images/iconinbt.png" action NullAction() hovered tt.Action("Раскрепощенность: [UI_Focus.Inbt]")
                bar range 100 value (UI_Focus.Inbt/10) xmaximum 100 left_bar "images/barfulli.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
            hbox:
                imagebutton idle "images/iconaddictrate.png" hover "images/iconaddictrate.png" action NullAction() hovered tt.Action("Сила Зависимости: [UI_Focus.Addictionrate]")
                bar range 100 value (UI_Focus.Addictionrate*10) xmaximum 100 left_bar "images/barfull.png" right_bar "images/barempty.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
        showif not Trigger:
    #            imagebutton auto "images/Button_Emma_%s.png" action ui.callsinnewcontext("Shift_Focus", "Emma") xpos 690 ypos 5 focus_mask True
            imagebutton auto "images/Button_"+UI_Focus.Tag+"_%s.png" action ShowTransient("Focus_Map") xpos 690 ypos 5 focus_mask True #xpos 690 ypos 5
        showif Trigger:
            imagebutton idle "images/Button_"+UI_Focus.Tag+"_idle.png" hover "images/Button_"+UI_Focus.Tag+"_idle.png" action NullAction() xpos 690 ypos 5 focus_mask True #xpos 690 ypos 5
        showif UI_Focus is DoreenX:
            imagebutton auto "images/UI_Tail_Button_%s.png" action ToggleVariable("GhostTail") hovered tt.Action("Сделать хвост полупрозрачным") xpos 700 ypos 35 focus_mask True #xpos 690 ypos 5
        showif config.developer:
            imagebutton auto "images/Button_"+UI_Focus.Tag+"_%s.png" action ui.callsinnewcontext("StatHacks",UI_Focus) xpos 730 ypos 5 focus_mask True



    frame:
        #Focus meter (dick)
        xminimum 130
        xpos 390
        background None
        has vbox
        hbox:
#            showif Player.Male != 1:
#                bar range 100 value FieldValue(Player, "Focus", 100) xmaximum 100 left_bar "images/barfullC.png" right_bar "images/baremptyC.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
            showif Player.Male:
                bar range 100 value FieldValue(Player, "Focus", 100) xmaximum 100 left_bar "images/barfullP.png" right_bar "images/baremptyP.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
            else:
                bar range 100 value FieldValue(Player, "Focus", 100) xmaximum 100 left_bar "images/barfullC.png" right_bar "images/baremptyC.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0

        hbox:
            bar range 100 value (Player.Semen*20) xmaximum 100 left_bar "images/barfullS.png" right_bar "images/baremptyS.png" left_gutter 3 right_gutter 5 thumb None thumb_offset 0
        button:
                #button to control whether cock is visible or not
                action ToggleVariable("AlphaCock",1,0)
                area(0,-60,100,30) #xpos,ypos,width,height
                background None #change to "True" to see borders
        button:
                #button to reset semen
                action ui.callsinnewcontext("Reset_Semen")
                area(0,-55,100,30)
                background None

#        imagebutton auto "images/Button_Emma_%s.png" action ui.callsinnewcontext("StatHacks",EmmaX) xpos 730 ypos 5 focus

    frame:
        # Money and level
        xminimum 75
        xpos 500
        background None
        has vbox
        hbox:
            text "Деньги: $[Player.Cash]" size 12
        hbox:
            text "Лвл: [Player.Lvl]" size 12
        hbox:
            text "[UI_Focus.Tag] Лвл: [UI_Focus.Lvl]" size 12
        # this block is the name tag
        window:
            pos (90,-40)#(-15,-8)
            anchor (0,0)
            style "say_who_window"
            text "[UI_Focus.Name]" size 12 font "CRIMFBRG.ttf" color "#000000" #id "UI_Focus"

    frame:
        #Clock
        xpos 880 #900
        ypos 20
        background None

        add "images/Clockbase.png":
            anchor (0.5,0.5)
            yzoom -1
            subpixel True

        if Round < 50:
            add "images/Clockred.png" at rotate_red(Round):
                anchor (0.5,0.5)
                subpixel True
        else:
            add "images/Clockwhite.png" at rotate_white(Round):
                anchor (0.5,0.5)
                subpixel True

#        add "images/Clockface.png":
#            anchor (0.5,0.5)
        imagebutton idle "images/Clockface.png" hover "images/Clockface.png" action SetVariable("Round", 100) hovered tt.Action("Ост. время: [Round]%") anchor (0.5,0.5)

        showif Trigger:
                imagebutton auto "images/UI_Showfeet_%s.png" action ToggleVariable("ShowFeet") hovered tt.Action("Вкл/выкл видимость ног") xpos 80 ypos 35 #focus_mask True #xpos 690 ypos 5
    frame:
        # Date and time
        xminimum 130
        xpos 900#920
        background None
        has vbox
        hbox:
            text "День: [Day] [DayofWeekRus]" size 12
        hbox:
            text "Время: [Current_Time_Rus]" size 12
    frame:
        #displays small icons for nearby characters
        xpos 920
        ypos 30
        background None
        vbox:
            hbox: #rkeljsv
                if RogueX in Nearby:
                        imagebutton auto "images/Button_Rogue_%s.png" action NullAction() hovered tt.Action(RogueX.Name) at TinyButtons
                if KittyX in Nearby:
                        imagebutton auto "images/Button_Kitty_%s.png" action NullAction() hovered tt.Action(KittyX.Name) at TinyButtons
                if EmmaX in Nearby:
                        imagebutton auto "images/Button_Emma_%s.png" action NullAction() hovered tt.Action(EmmaX.Name) at TinyButtons
                if LauraX in Nearby:
                        imagebutton auto "images/Button_Laura_%s.png" action NullAction() hovered tt.Action(LauraX.Name) at TinyButtons
                if JeanX in Nearby:
                        imagebutton auto "images/Button_Jean_%s.png" action NullAction() hovered tt.Action(JeanX.Name) at TinyButtons
                if StormX in Nearby:
                        imagebutton auto "images/Button_Storm_%s.png" action NullAction() hovered tt.Action(StormX.Name) at TinyButtons
                if JubesX in Nearby:
                        imagebutton auto "images/Button_Jubes_%s.png" action NullAction() hovered tt.Action(JubesX.Name) at TinyButtons
                if GwenX in Nearby:
                        imagebutton auto "images/Button_Gwen_%s.png" action NullAction() hovered tt.Action(GwenX.Name) at TinyButtons
                if BetsyX in Nearby:
                        imagebutton auto "images/Button_Betsy_%s.png" action NullAction() hovered tt.Action(BetsyX.Name) at TinyButtons
                if DoreenX in Nearby:
                        imagebutton auto "images/Button_Doreen_%s.png" action NullAction() hovered tt.Action(DoreenX.Name) at TinyButtons
                if WandaX in Nearby:
                        imagebutton auto "images/Button_Wanda_%s.png" action NullAction() hovered tt.Action(WandaX.Name) at TinyButtons


    if tt.value != " ":
        # Pop-up mouse-over labels
        frame :
            xpos 500 ypos 60
            has vbox:
                text tt.value

transform TinyButtons:
    zoom .5

screen Focus_Map: #rkeljsv
    #changes focal character with dropdown box
    imagebutton auto "images/Button_X_%s.png" action Hide("Focus_Map") xpos 690 ypos 5 focus_mask True
    frame:
        xpos 684
        ypos 44
        hbox:
            vbox:
                imagebutton auto "images/Button_Rogue_%s.png" action ui.callsinnewcontext("Shift_UI", RogueX) focus_mask True
                if "met" in KittyX.History:
                        imagebutton auto "images/Button_Kitty_%s.png" action ui.callsinnewcontext("Shift_UI", KittyX) focus_mask True
                        # old way. . . imagebutton auto "images/Button_Kitty_%s.png" action ui.callsinnewcontext("Shift_Focus", "Kitty") focus_mask True
            vbox:
                if "met" in EmmaX.History:
                        imagebutton auto "images/Button_Emma_%s.png" action ui.callsinnewcontext("Shift_UI", EmmaX) focus_mask True
                if "met" in LauraX.History:
                        imagebutton auto "images/Button_Laura_%s.png" action ui.callsinnewcontext("Shift_UI", LauraX) focus_mask True
            vbox:
                if "met" in JeanX.History:
                        imagebutton auto "images/Button_Jean_%s.png" action ui.callsinnewcontext("Shift_UI", JeanX) focus_mask True
                if "met" in StormX.History:
                        imagebutton auto "images/Button_Storm_%s.png" action ui.callsinnewcontext("Shift_UI", StormX) focus_mask True
            vbox:
                if "met" in JubesX.History:
                        imagebutton auto "images/Button_Jubes_%s.png" action ui.callsinnewcontext("Shift_UI", JubesX) focus_mask True
                if "met" in GwenX.History:
                        imagebutton auto "images/Button_Gwen_%s.png" action ui.callsinnewcontext("Shift_UI", GwenX) focus_mask True
            vbox:
                if "met" in BetsyX.History:
                        imagebutton auto "images/Button_Betsy_%s.png" action ui.callsinnewcontext("Shift_UI", BetsyX) focus_mask True
                if "met" in DoreenX.History:
                        imagebutton auto "images/Button_Doreen_%s.png" action ui.callsinnewcontext("Shift_UI", DoreenX) focus_mask True
            vbox:
                if "met" in WandaX.History:
                        imagebutton auto "images/Button_Wanda_%s.png" action ui.callsinnewcontext("Shift_UI", WandaX) focus_mask True

transform rotate_white(x):
    rotate -(int(x *3.6))

transform rotate_red(x):
    rotate -(int(x *3.6-180))

#end wardrobe



screen Inventory_screen: #rkeljsvg
    frame:
        xminimum 200
        xpos 700
        ypos 75
        has vbox

#        hbox:
        text "Инвентарь:" size 20
        showif "dildo" in Player.Inventory:
                $ Inventory_Count = Player.Inventory.count("dildo")
                text "Фаллоимитаторы: [Inventory_Count]" size 15
        showif "vibrator" in Player.Inventory:
                $ Inventory_Count = Player.Inventory.count("vibrator")
                text "Вибраторы: [Inventory_Count]" size 15
        showif "plug" in Player.Inventory:
                $ Inventory_Count = Player.Inventory.count("plug")
                text "Анальные пробки: [Inventory_Count]" size 15
        showif "Dazzler and Longshot" in Player.Inventory:
                $ Inventory_Count = Player.Inventory.count("Dazzler and Longshot")
                text "Ослепительная и Счастливчик: [Inventory_Count]" size 15
        showif "256 Shades of Grey" in Player.Inventory:
                $ Inventory_Count = Player.Inventory.count("256 Shades of Grey")
                text "256 Оттенков Серого: [Inventory_Count]" size 15
        showif "Avengers Tower Penthouse" in Player.Inventory:
                $ Inventory_Count = Player.Inventory.count("Avengers Tower Penthouse")
                text "Пентхаус Башни Мстителей: [Inventory_Count]" size 15
        showif "Xavier's photo" in Player.Inventory:
                text "Фото Ксавье" size 15
        showif "Xavier's files" in Player.Inventory:
                text "Файлы Ксавье" size 15
        #Rogue
        showif "Rogue nighty" in Player.Inventory:
                text "Зеленая ночнушка для Роуг" size 15
        showif "Rogue lace bra" in Player.Inventory:
                text "Кружевной лифчик для Роуг" size 15
        showif "Rogue lace panties" in Player.Inventory:
                text "Кружевные трусики для Роуг" size 15
        showif "Rogue bikini top" in Player.Inventory:
                text "Лифчик бикини для Роуг" size 15
        showif "Rogue bikini bottoms" in Player.Inventory:
                text "Трусики бикини для Роуг" size 15
        #Kitty
        showif "Kitty lace bra" in Player.Inventory:
                text "Кружевной лифчик для Китти" size 15
        showif "Kitty lace panties" in Player.Inventory:
                text "Кружевные трусики для Китти" size 15
        showif "Kitty knee stockings" in Player.Inventory:
                text "Гольфы для Китти" size 15
        showif "Kitty pantyhose" in Player.Inventory:
                text "Колготки для Китти" size 15
        showif "Kitty bikini top" in Player.Inventory:
                text "Лифчик бикини для Китти" size 15
        showif "Kitty bikini bottoms" in Player.Inventory:
                text "Трусики бикини для Китти" size 15
        showif "Kitty blue skirt" in Player.Inventory:
                text "Синяя юбка для Китти" size 15
        #Emma
        showif "Emma lace bra" in Player.Inventory:
                text "Кружевной лифчик для Эммы" size 15
        showif "Emma lace panties" in Player.Inventory:
                text "Кружевные трусики для Эммы" size 15
        showif "Emma pantyhose" in Player.Inventory:
                text "Колготки для Эммы" size 15
        showif "Emma bikini top" in Player.Inventory:
                text "Лифчик бикини для Эммы" size 15
        showif "Emma bikini bottoms" in Player.Inventory:
                text "Трусики бикини для Эммы" size 15
        #Laura
        showif "Laura corset" in Player.Inventory:
                text "Красный корсет для Лоры" size 15
        showif "Laura lace corset" in Player.Inventory:
                text "Кружевной корсет для Лоры" size 15
        showif "Laura lace panties" in Player.Inventory:
                text "LКружевные трусики для Лоры" size 15
        showif "Laura bikini top" in Player.Inventory:
                text "Лифчик бикини для Лоры" size 15
        showif "Laura bikini bottoms" in Player.Inventory:
                text "Трусики бикини для Лоры" size 15
        #Jean
        showif "Jean corset" in Player.Inventory:
                text "Черный корсет для Джин" size 15
        showif "Jean lace corset" in Player.Inventory:
                text "Кружевной корсет для Джин" size 15
        showif "Jean lace bra" in Player.Inventory:
                text "Кружевной лифчик для Джин" size 15
        showif "Jean lace panties" in Player.Inventory:
                text "Кружевные трусики для Джин" size 15
        showif "Jean bikini top" in Player.Inventory:
                text "Лифчик бикини для Джин" size 15
        showif "Jean bikini bottoms" in Player.Inventory:
                text "Трусики бикини для Джин" size 15
        #Storm
        showif "Storm lace bra" in Player.Inventory:
                text "Кружевной лифчик для Шторм" size 15
        showif "Storm lace panties" in Player.Inventory:
                text "Кружевные трусики для Шторм" size 15
        showif "Storm pantyhose" in Player.Inventory:
                text "Колготки для Шторм" size 15
        showif "Storm bikini top" in Player.Inventory:
                text "Лифчик бикини для Шторм" size 15
        showif "Storm bikini bottoms" in Player.Inventory:
                text "Трусики бикини для Шторм" size 15
        #Jubes
        showif "Jubes lace bra" in Player.Inventory:
                text "Кружевной лифчик для Джубили" size 15
        showif "Jubes lace panties" in Player.Inventory:
                text "Кружевные трусики для Джубили" size 15
        showif "Jubes bikini top" in Player.Inventory:
                text "Лифчик бикини для Джубили" size 15
        showif "Jubes bikini bottoms" in Player.Inventory:
                text "Трусики бикини для Джубили" size 15
        showif "socks" in Player.Inventory:
                text "Высокие носки для Джубили" size 15
        #Gwen
        showif "Gwen lace bra" in Player.Inventory:
                text "Кружевной лифчик для Гвен" size 15
        showif "Gwen lace panties" in Player.Inventory:
                text "Кружевные трусики для Гвен" size 15
        showif "Gwen bikini top" in Player.Inventory:
                text "Лифчик бикини для Гвен" size 15
        showif "Gwen bikini bottoms" in Player.Inventory:
                text "Трусики бикини для Гвен" size 15
        #Betsy
        showif "Betsy swimsuit" in Player.Inventory:
                text "Купальник для Бетси" size 15
        showif "stockings and garterbelt" in Player.Inventory:
                text "чулки и пояс с подвязками" size 15
        #Doreen
        showif "Doreen lace bra" in Player.Inventory:
                text "Кружевной лифчик для Дорин" size 15
        showif "Doreen lace panties" in Player.Inventory:
                text "Кружевные трусики для Дорин" size 15
        showif "Doreen bikini top" in Player.Inventory:
                text "Лифчик бикини для Дорин" size 15
        showif "Doreen bikini bottoms" in Player.Inventory:
                text "Трусики бикини для Дорин" size 15
        #Wanda
        showif "Wanda lace bra" in Player.Inventory:
                text "Кружевной лифчик для Ванды" size 15
        showif "Wanda lace panties" in Player.Inventory:
                text "Кружевные трусики для Ванды" size 15
        showif "Wanda bikini top" in Player.Inventory:
                text "Лифчик бикини для Ванды" size 15
        showif "Wanda bikini bottoms" in Player.Inventory:
                text "Трусики бикини для Ванды" size 15

        #rkeljsvg
        #colognes
        showif "Mandrill Cologne" in Player.Inventory:
                $ Inventory_Count = Player.Inventory.count("Mandrill Cologne")
                textbutton "Одеколон с феромонами обезьян: Кол-во порций - [Inventory_Count]" action ui.callsinnewcontext("MandrillScreen") text_size 15
        showif "Purple Rain Cologne" in Player.Inventory:
                $ Inventory_Count = Player.Inventory.count("Purple Rain Cologne")
                textbutton "Одеколон \"Фиолетовый Дождь\": Кол-во порций - [Inventory_Count]" action ui.callsinnewcontext("PurpleRainScreen") text_size 15
        showif "Corruption Cologne" in Player.Inventory:
                $ Inventory_Count = Player.Inventory.count("Corruption Cologne")
                textbutton "Одеколон \"Разрат\": Кол-во порций - [Inventory_Count]" action ui.callsinnewcontext("CorruptionScreen") text_size 15
        showif "Xavier" in Keys:
                text "Ключ Ксавье" size 15
        showif RogueX in Keys:
                text "Ключ Роуг" size 15
        showif KittyX in Keys:
                text "Ключ Китти" size 15
        showif EmmaX in Keys:
                text "Ключ Эммы" size 15
        showif LauraX in Keys:
                text "Ключ Лоры" size 15
        showif JeanX in Keys:
                text "Ключ Джин" size 15
        showif StormX in Keys:
                text "Ключ Шторм" size 15
        showif JubesX in Keys:
                text "Ключ Джубс" size 15
        showif GwenX in Keys:
                text "Ключ Гвен" size 15
        showif BetsyX in Keys:
                text "Ключ Бетси" size 15
        showif DoreenX in Keys:
                text "Ключ Дорин" size 15
        showif WandaX in Keys:
                text "Ключ Ванды" size 15
        #rkeljsvgb


    imagebutton:
        auto "images/UI_Backpack_%s.png"
        action Hide("Inventory_screen")
        xpos 780
        ypos 5
        focus_mask True


label MandrillScreen:
    if "mandrill" in Player.Traits:
            "Вы уже применили на себя этот аромат."
            return
    if "purple" in Player.Traits or "corruption" in Player.Traits:
            "Вы испортите аромат, который уже применили на себя."
            return
#    $ Inventory_Count = Inventory_Check("Mandrill Cologne")
    $ Inventory_Count = Player.Inventory.count("Mandrill Cologne")
    "Этот одеколон обязательно заставит женщин полюбить вас больше [[+Любовь]. У вас есть [Inventory_Count] порций."
    "Предупреждение о продукте: любая любовь, полученная во время воздействия, может быть потеряна, когда действие одеколона закончится, если будут достигнуты пределы."
    menu:
        "Использовать?"
        "Да":
            $ Player.Traits.append("mandrill")
            $ Player.Inventory.remove("Mandrill Cologne")
        "Нет":
            pass

    return

label PurpleRainScreen:
    if "purple" in Player.Traits:
        "Вы уже применили на себя этот аромат."
        return
    if "mandrill" in Player.Traits or "corruption" in Player.Traits:
        "Вы испортите аромат, который уже применили на себя."
        return
#    $ Inventory_Count = Inventory_Check("Purple Rain Cologne")
    $ Inventory_Count = Player.Inventory.count("Purple Rain Cologne")
    "Этот одеколон гарантированно сделает женщин более склонными к вашим указаниям до завтрашнего дня [[+Послушание]. У вас есть [Inventory_Count] порций."
    "Предупреждение о продукте: любое послушание, полученное во время действия, может быть потеряно, когда действие одеколона закончится, если будут достигнуты пределы."
    menu:
        "Использовать?"
        "Да":
            $ Player.Traits.append("purple")
            $ Player.Inventory.remove("Purple Rain Cologne")
        "Нет":
            pass
    return

label CorruptionScreen:
    if "corruption" in Player.Traits:
        "Вы уже применили на себя этот аромат."
        return
    if "purple" in Player.Traits or "mandrill" in Player.Traits:
        "Вы испортите аромат, который уже применили на себя."
        return
#    $ Inventory_Count = Inventory_Check("Corruption Cologne")
    $ Inventory_Count = Player.Inventory.count("Corruption Cologne")
    "Этот одеколон гарантированно заставит женщин раскрыть свою дикую сторону [[+Раскрепощенность]. У вас есть [Inventory_Count] порций."
    "Предупреждение о продукте: любая раскрепощенность, полученная во время воздействия, может быть потеряна, когда действие одеколона закончится, если будут достигнуты пределы."
    menu:
        "Использовать?"
        "Да":
            $ Player.Traits.append("corruption")
            $ Player.Inventory.remove("Corruption Cologne")
        "Нет":
            pass
    return
#Begin Disclaimer screen:

screen Disclaimer_screen:
    window:
        style "gm_root"
    frame:
        xalign .5
        ypos 100
        xmaximum 800
        has vbox
        text "This is a work of parody fiction. It is intended to be distributed through Oniartist's Patreon page, please do not redistribute through other sources."
        text " "
        text "As is noted in the game, this story takes place several years after the last episode of the TV series it is based on, and all characters involved are over the age of 18.The game references events of the TV series, but is not beholden to the canon of the series, and characters will behave differently or have different backstories."
        text " "
        text "I would like to thank Akabur for his help getting started with all this (definitely check out his games too), and the various documentation on the Renpy site for pointing me in the right directions. I've had a lot of fun coding this game, and look forward to continually improving on it. If you'd like to support my efforts, please sign up under my name at Hentai United, or join on to my Patreon page. I have some huge ambitions for where this project will end up."
        text " "
        text "{a=http://www.patreon.com/OniArtist}http://www.patreon.com/OniArtist{/a}"

    frame:
        xalign 0.5
        yalign 0.95
        has hbox
        #textbutton "Return" action Return()
        textbutton "Назад" action Hide("Disclaimer_screen")

#label Disclaimer_screen_label:
#    call screen Disclaimer_screen
#    return
#end Disclaimer
