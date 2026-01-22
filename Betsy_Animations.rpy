# Basic character Sprites

image Betsy_Sprite:
    LiveComposite(
        (600,1250),       #550,950
        (0,0), "images/BetsySprite/Betsy_Sprite_Shadow.png",
        (15,-80), "Betsy_Sprite_HairBack", #(75,-10)
        (0,0), ConditionSwitch(
            #skirt back
#            "BetsyX.Upskirt", Null(),
#            "BetsyX.Legs == 'pants'", "images/BetsySprite/Betsy_Sprite_Legs_Pants_Back.png",
            "BetsyX.Legs == 'skirt'", Recolor("Betsy", "Legs", "images/BetsySprite/Betsy_Sprite_Legs_Skirt_Back.png"),
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #panties down back
#            "not BetsyX.Panties or not BetsyX.PantiesDown", Null(),
#            #if the panties are down
#            "BetsyX.Legs and not BetsyX.Upskirt and BetsyX.Legs != 'skirt'", Null(),
#            #if she's wearing a skirt or nothing else
#            "BetsyX.Panties == 'lace panties'", "images/BetsySprite/Betsy_Sprite_Panties_Lace_Back.png",
#            "BetsyX.Panties == 'swimsuit'", "images/BetsySprite/Betsy_Sprite_Panties_Lace_Back.png",
#            "True", "images/BetsySprite/Betsy_Sprite_Panties_White_Back.png",
#            ),

        (225,505), ConditionSwitch(    #165,560
            #Personal Wetness
            "not BetsyX.Wet", Null(),
            "BetsyX.Wet == 1 or (BetsyX.Legs and BetsyX.Legs != 'skirt' and not BetsyX.Upskirt)", "Wet_Drip", #ConditionSwitch( #Wet = 1
#                    "(BetsyX.Legs == 'pants' or BetsyX.Legs == 'shorts') and not BetsyX.Upskirt", Null(),
#                    "BetsyX.Panties and not BetsyX.PantiesDown", Null(),
#                    "(BetsyX.Legs == 'pants' or BetsyX.Legs == 'shorts')", AlphaMask("Wet_Drip","Betsy_Drip_MaskP"),
#                    "BetsyX.Panties and BetsyX.PantiesDown", AlphaMask("Wet_Drip","Betsy_Drip_MaskP"),
#                    "True", AlphaMask("Wet_Drip","Betsy_Drip_Mask"), #only plays if nothing is in the way
#                    ),
            "True", "Wet_Drip2", #ConditionSwitch( #Wet = 2+
#                    "(BetsyX.Legs == 'pants' or BetsyX.Legs == 'shorts') and BetsyX.Upskirt", AlphaMask("Wet_Drip2","Betsy_Drip_MaskP"),
#                    "BetsyX.Panties and BetsyX.PantiesDown", AlphaMask("Wet_Drip2","Betsy_Drip_MaskP"),
#                    "True", AlphaMask("Wet_Drip2","Betsy_Drip_Mask"), #only plays if nothing is in the way
#                    ),
            ),
        (225,505), ConditionSwitch(    #165,560
            #Spunk
            "('in' not in BetsyX.Spunk and 'anal' not in BetsyX.Spunk) or not Player.Male", Null(),
            "BetsyX.Panties and not BetsyX.PantiesDown", "Spunk_Drip", #ConditionSwitch( #Wet = 1
            "BetsyX.Legs and BetsyX.Legs != 'skirt' and not BetsyX.Upskirt", "Spunk_Drip", #ConditionSwitch( #Wet = 1
#                    "BetsyX.Panties and BetsyX.PantiesDown", AlphaMask("Spunk_Drip","Betsy_Drip_MaskP"),
#                    "(BetsyX.Legs == 'pants' or BetsyX.Legs == 'shorts') and BetsyX.Upskirt", AlphaMask("Spunk_Drip","Betsy_Drip_MaskP"),
#                    "True", AlphaMask("Spunk_Drip","Betsy_Drip_Mask"), #only plays if nothing is in the way
#                    ),
            "True", "Spunk_Drip2", #ConditionSwitch( #Wet = 2+
#                    "(BetsyX.Legs == 'pants' or BetsyX.Legs == 'shorts') and BetsyX.Upskirt", AlphaMask("Spunk_Drip2","Betsy_Drip_MaskP"),
#                    "BetsyX.Panties and BetsyX.PantiesDown", AlphaMask("Spunk_Drip2","Betsy_Drip_MaskP"),
#                    "True", AlphaMask("Spunk_Drip2","Betsy_Drip_Mask"), #only plays if nothing is in the way
#                    ),
            ),

        (0,0), ConditionSwitch(
            #arms back
            # Modification mode
            "BetsyX.ArmPose != 1 and BetsyX.Arms == 'cammy gloves'", "images/BetsySprite/modification/[BetsyX.skin_image.skin_path]Betsy_Sprite_Arm_Back2Cammy.png",         # right hand up/left down
            # -----------------
            "BetsyX.ArmPose != 1 and BetsyX.Arms", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Arm_Back2G.png",         # right hand up/left down
            "BetsyX.ArmPose != 1", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Arm_Back2.png",         # right hand up/left down
            # Modification mode
            "BetsyX.Arms == 'cammy gloves'", "images/BetsySprite/modification/[BetsyX.skin_image.skin_path]Betsy_Sprite_Arm_Back1Cammy.png",         # right hand up/left down
            # -----------------
            "BetsyX.Arms", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Arm_Back1G.png",         # right hand up/left down
            "True", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Arm_Back1.png", #if BetsyX.Arms == 1   # right Hand on hip/left raised
            ),
        (0,0), ConditionSwitch(
            #arms shirt back
            "BetsyX.ArmPose != 1 and BetsyX.Over == 'pink top'", Recolor("Betsy", "Over", "images/BetsySprite/Betsy_Sprite_Over_Shirt2_Back.png"),         # right hand up/left down
            "BetsyX.Over == 'jacket' and BetsyX.ArmPose == 1", Recolor("Betsy", "Over", "images/BetsySprite/Betsy_Sprite_Over_Jacket1_Back.png"),
            "BetsyX.Over == 'jacket'", Recolor("Betsy", "Over", "images/BetsySprite/Betsy_Sprite_Over_Jacket2_Back.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #body
            "BetsyX.Pubes", Recolor("Betsy", "Pubes", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Body_Pubes.png"),         # right hand up/left down
            "True", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Body.png", #if BetsyX.Arms == 1   # right Hand on hip/left raised
            ),
        # Modification mode
        (0,0), ConditionSwitch(
            "BetsyX.Acc and 'cammy print' in BetsyX.Acc", "images/BetsySprite/modification/Betsy_Sprite_Legs_Cammy_Print.png",         # right hand up/left down
            "True", Null(),
            ),
        # -----------------

        (0,0), ConditionSwitch(
            #Water effect
            "BetsyX.Water and BetsyX.ArmPose == 1", "images/BetsySprite/Betsy_Sprite_Water1.png",
            "BetsyX.Water", "images/BetsySprite/Betsy_Sprite_Water2.png",
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #Arms2 behind the body
#            "BetsyX.ArmPose != 1 and BetsyX.Over == 'suit' and BetsyX.Arms", "images/BetsySprite/Betsy_Sprite_Over_Suit_2G_Back.png",                #gloved 2
#            "BetsyX.ArmPose != 1 and (BetsyX.Over == 'suit' or BetsyX.Over == 'open suit')", "images/BetsySprite/Betsy_Sprite_Over_Suit_2_Back.png", #no gloved 2
#            "True", Null(),  #if BetsyX.Arms ==2
#            ),

        (0,0), ConditionSwitch(
            #Personal Wetness  over
            "not BetsyX.Wet", Null(),
            "BetsyX.Panties and not BetsyX.PantiesDown", Null(),
            "BetsyX.Legs and BetsyX.Legs != 'skirt' and not BetsyX.Upskirt", Null(),
            "True", "images/BetsySprite/Betsy_Sprite_Wet_Pussy.png", #ConditionSwitch( #Wet = 2+
            ),
        (0,0), ConditionSwitch(
            #Spunk over
            "('in' not in BetsyX.Spunk and 'anal' not in BetsyX.Spunk) or not Player.Male", Null(),
            "BetsyX.Legs and BetsyX.Legs != 'skirt' and not BetsyX.Upskirt", Null(),
            "BetsyX.Panties and not BetsyX.PantiesDown", Null(),
            "True", "images/BetsySprite/Betsy_Sprite_Spunk_Pussy.png",
            ),

#        (0,0), ConditionSwitch(
#            #pubes
#            "BetsyX.Pubes", "images/BetsySprite/Betsy_Sprite_Pubes.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #Necklaces
#            "BetsyX.Neck == 'choker'", "images/BetsySprite/Betsy_Sprite_Neck_Choker.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #stockings
            "BetsyX.Hose == 'stockings'", Recolor("Betsy", "Hose", "images/BetsySprite/Betsy_Sprite_Hose_Stockings.png"),
            "BetsyX.Hose == 'socks'", Recolor("Betsy", "Hose", "images/BetsySprite/Betsy_Sprite_Hose_Socks.png"),
            "BetsyX.Hose == 'stockings and garterbelt'", Recolor("Betsy", "Hose", "images/BetsySprite/Betsy_Sprite_Hose_StockingsGarter.png"),
            "BetsyX.Hose == 'garterbelt'", Recolor("Betsy", "Hose", "images/BetsySprite/Betsy_Sprite_Hose_Garter.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #panties
#            "not BetsyX.Panties", Null(),
            "BetsyX.PantiesDown", ConditionSwitch(
                    #if the panties are down
                    "not BetsyX.Legs or BetsyX.Upskirt or BetsyX.Legs == 'skirt'", ConditionSwitch(
                            #if she's wearing a skirt or nothing else
                            "BetsyX.Panties == 'swimsuit' or BetsyX.Chest == 'swimsuit'", Recolor("Betsy", "Panties", "images/BetsySprite/Betsy_Sprite_Panties_Bikini_Down.png"),
                            "BetsyX.Panties == 'lace panties'", Recolor("Betsy", "Panties", "images/BetsySprite/Betsy_Sprite_Panties_Lace_Down.png"),
#                            "BetsyX.Panties == 'swimsuit' and BetsyX.Wet", "images/BetsySprite/Betsy_Sprite_Panties_Bikini_Down_Wet.png",
                            # Modification mode
                            "BetsyX.Panties == 'cammy leotard' or BetsyX.Chest == 'cammy leotard'", "images/BetsySprite/modification/Betsy_Sprite_Panties_Cammy_Down.png",
                            # -----------------
                            "BetsyX.Panties", Recolor("Betsy", "Panties", "images/BetsySprite/Betsy_Sprite_Panties_Blue_Down.png"),
                            "True", Null(),
                            ),
                    "True", Null(),
                    ),
            #if she's not wet
            # Modification mode
            "BetsyX.Panties == 'cammy leotard'", "images/BetsySprite/modification/Betsy_Sprite_Panties_Cammy.png",
            "BetsyX.Chest == 'cammy leotard'", "images/BetsySprite/modification/Betsy_Sprite_Panties_Cammy_Down.png", #shows swimsuit as down if bottoms off but top on
            # -----------------
            "BetsyX.Panties == 'swimsuit'", Recolor("Betsy", "Panties", "images/BetsySprite/Betsy_Sprite_Panties_Bikini.png"),
            "BetsyX.Chest == 'swimsuit'", Recolor("Betsy", "Panties", "images/BetsySprite/Betsy_Sprite_Panties_Bikini_Down.png"), #shows swimsuit as down if bottoms off but top on
            "BetsyX.Panties == 'lace panties'", Recolor("Betsy", "Panties", "images/BetsySprite/Betsy_Sprite_Panties_Lace.png"),
            "BetsyX.Panties and BetsyX.Wet", Recolor("Betsy", "Panties", "images/BetsySprite/Betsy_Sprite_Panties_Blue_Wet.png"),
            "BetsyX.Panties", Recolor("Betsy", "Panties", "images/BetsySprite/Betsy_Sprite_Panties_Blue.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pantyhose
            "BetsyX.Hose == 'pantyhose' and (not BetsyX.PantiesDown or not BetsyX.Panties)", Recolor("Betsy", "Hose", "images/BetsySprite/Betsy_Sprite_Hose_Pantyhose.png"),
#            "BetsyX.Hose == 'tights' and BetsyX.Wet and (not BetsyX.PantiesDown or not BetsyX.Panties)", "images/BetsySprite/Betsy_Sprite_Hose_Tights.png",
#            "BetsyX.Hose == 'tights' and (not BetsyX.PantiesDown or not BetsyX.Panties)", "images/BetsySprite/Betsy_Sprite_Hose_Tights.png",
            "BetsyX.Hose == 'ripped pantyhose' and (not BetsyX.PantiesDown or not BetsyX.Panties)", Recolor("Betsy", "Hose", "images/BetsySprite/Betsy_Sprite_Hose_Pantyhose_Holed.png"),
#            "BetsyX.Hose == 'ripped tights' and (not BetsyX.PantiesDown or not BetsyX.Panties)", "images/BetsySprite/Betsy_Sprite_Hose_Tights_Holed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pants
            "not BetsyX.Legs", Null(),
            "BetsyX.Upskirt", ConditionSwitch(
                        #if the skirt's up or pants down
                        "BetsyX.Legs == 'skirt'", Recolor("Betsy", "Legs", "images/BetsySprite/Betsy_Sprite_Legs_Skirt_Up.png"),
                        "BetsyX.Legs == 'shorts'", Recolor("Betsy", "Legs", "images/BetsySprite/Betsy_Sprite_Legs_Shorts_Down.png"),
                        "BetsyX.Legs == 'yoga pants'", Recolor("Betsy", "Legs", "images/BetsySprite/Betsy_Sprite_Legs_Yoga_Down.png"),
                        "True", Null(),
                        ),
            "BetsyX.Legs == 'skirt'", Recolor("Betsy", "Legs", "images/BetsySprite/Betsy_Sprite_Legs_Skirt.png"),
            "BetsyX.Wet > 1", ConditionSwitch(
                #if she's wet
                "BetsyX.Legs == 'yoga pants'", Recolor("Betsy", "Legs", "images/BetsySprite/Betsy_Sprite_Legs_Yoga_Wet.png"),
                "BetsyX.Legs == 'shorts'", Recolor("Betsy", "Legs", "images/BetsySprite/Betsy_Sprite_Legs_Shorts_Wet.png"),
                "True", Null(),
                ),
            #if she's not wet
            "BetsyX.Legs == 'yoga pants'", Recolor("Betsy", "Legs", "images/BetsySprite/Betsy_Sprite_Legs_Yoga.png"),
            "BetsyX.Legs == 'shorts'", Recolor("Betsy", "Legs", "images/BetsySprite/Betsy_Sprite_Legs_Shorts.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #nude lower piercings
            "not BetsyX.Pierce", Null(),
            "BetsyX.Legs == 'skirt' and not BetsyX.Upskirt", Null(),
            "BetsyX.Pierce == 'ring'", ConditionSwitch(
                    # if top is up. . .
                    "BetsyX.Legs == 'shorts' and not BetsyX.Upskirt", "images/BetsySprite/Betsy_Sprite_Pierce_Pussy_Ring_BlueL.png",
                    "BetsyX.Legs == 'yoga pants' and not BetsyX.Upskirt", "images/BetsySprite/Betsy_Sprite_Pierce_Pussy_Ring_Black.png",

                    "BetsyX.Hose == 'pantyhose' and not BetsyX.PantiesDown", "images/BetsySprite/Betsy_Sprite_Pierce_Pussy_Ring_Lace.png",

                    "BetsyX.Panties != 'swimsuit' and BetsyX.Chest == 'swimsuit'", "images/BetsySprite/Betsy_Sprite_Pierce_Pussy_Ring.png",
                    "BetsyX.Panties == 'lace panties' and not BetsyX.PantiesDown", "images/BetsySprite/Betsy_Sprite_Pierce_Pussy_Ring_Lace.png",
                    # Modification mode
                    "BetsyX.Chest == 'cammy leotard' and not BetsyX.PantiesDown", "images/BetsySprite/modification/Betsy_Sprite_Pierce_Pussy_Ring_Cammy.png",
                    # ----------------
                    "BetsyX.Panties and not BetsyX.PantiesDown", "images/BetsySprite/Betsy_Sprite_Pierce_Pussy_Ring_Blue.png",
                    "BetsyX.Chest == 'swimsuit' and not BetsyX.PantiesDown", "images/BetsySprite/Betsy_Sprite_Pierce_Pussy_Ring_Blue.png",

                    "True", "images/BetsySprite/Betsy_Sprite_Pierce_Pussy_Ring.png",
                    ),

            "BetsyX.Legs == 'shorts' and not BetsyX.Upskirt", "images/BetsySprite/Betsy_Sprite_Pierce_Pussy_Barbell_BlueL.png",
            "BetsyX.Legs == 'yoga pants' and not BetsyX.Upskirt", "images/BetsySprite/Betsy_Sprite_Pierce_Pussy_Barbell_Black.png",

            "BetsyX.Hose == 'pantyhose'", "images/BetsySprite/Betsy_Sprite_Pierce_Pussy_Barbell_Lace.png",

            "BetsyX.Panties != 'swimsuit' and BetsyX.Chest == 'swimsuit'", "images/BetsySprite/Betsy_Sprite_Pierce_Pussy_Barbell.png",
            "BetsyX.Panties == 'lace panties' and not BetsyX.PantiesDown", "images/BetsySprite/Betsy_Sprite_Pierce_Pussy_Barbell_Lace.png",
            # Modification mode
            "BetsyX.Chest == 'cammy leotard' and not BetsyX.PantiesDown", "images/BetsySprite/modification/Betsy_Sprite_Pierce_Pussy_Barbell_Cammy.png",
            # -----------------
            "BetsyX.Panties and not BetsyX.PantiesDown", "images/BetsySprite/Betsy_Sprite_Pierce_Pussy_Barbell_Blue.png",
            "BetsyX.Chest == 'swimsuit' and not BetsyX.PantiesDown", "images/BetsySprite/Betsy_Sprite_Pierce_Pussy_Barbell_Blue.png",

            "BetsyX.Pierce == 'barbell'", "images/BetsySprite/Betsy_Sprite_Pierce_Pussy_Barbell.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Chest layer
            "BetsyX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "BetsyX.Chest == 'swimsuit' or BetsyX.Panties == 'swimsuit'", Recolor("Betsy", "Chest", "images/BetsySprite/Betsy_Sprite_Chest_Bikini_Up.png"),
                    "BetsyX.Chest == 'lace bra'", Recolor("Betsy", "Chest", "images/BetsySprite/Betsy_Sprite_Chest_Lace_Up.png"),
                    "BetsyX.Chest == 'sports bra'", Recolor("Betsy", "Chest", "images/BetsySprite/Betsy_Sprite_Chest_Sports_Up.png"),
                    "BetsyX.Chest == 'bra'", Recolor("Betsy", "Chest", "images/BetsySprite/Betsy_Sprite_Chest_Blue_Up.png"),
                    # Modification mode
                    "BetsyX.Chest == 'cammy leotard' or BetsyX.Panties == 'cammy leotard'", "images/BetsySprite/modification/Betsy_Sprite_Chest_Cammy_Up.png",
                    # -----------------
                    "True", Null(),
                    ),
            # Modification mode
            "BetsyX.Chest == 'cammy leotard'", "images/BetsySprite/modification/Betsy_Sprite_Chest_Cammy.png",
            "BetsyX.Panties == 'cammy leotard'", "images/BetsySprite/modification/Betsy_Sprite_Chest_Cammy_Up.png", #shows swimsuit as down if top off but bottoms on
            # ----------------
            "BetsyX.Chest == 'swimsuit'", Recolor("Betsy", "Chest", "images/BetsySprite/Betsy_Sprite_Chest_Bikini.png"),
            "BetsyX.Panties == 'swimsuit'", Recolor("Betsy", "Chest", "images/BetsySprite/Betsy_Sprite_Chest_Bikini_Up.png"), #shows swimsuit as down if top off but bottoms on
            "BetsyX.Chest == 'lace bra'", Recolor("Betsy", "Chest", "images/BetsySprite/Betsy_Sprite_Chest_Lace.png"),
            "BetsyX.Chest == 'sports bra'", Recolor("Betsy", "Chest", "images/BetsySprite/Betsy_Sprite_Chest_Sports.png"),
            "BetsyX.Chest == 'bra'", Recolor("Betsy", "Chest", "images/BetsySprite/Betsy_Sprite_Chest_Blue.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over
            "BetsyX.Over == 'jacket' and BetsyX.ArmPose == 1", Recolor("Betsy", "Over", "images/BetsySprite/Betsy_Sprite_Over_Jacket1.png"),
            "BetsyX.Over == 'jacket'", Recolor("Betsy", "Over", "images/BetsySprite/Betsy_Sprite_Over_Jacket2.png"),
            "BetsyX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "BetsyX.Over == 'tank'", Recolor("Betsy", "Over", "images/BetsySprite/Betsy_Sprite_Over_Tank_Up.png"),
                    "BetsyX.Over == 'pink top' and BetsyX.ArmPose == 1", Recolor("Betsy", "Over", "images/BetsySprite/Betsy_Sprite_Over_Shirt1_Up.png"),
                    "BetsyX.Over == 'pink top'", Recolor("Betsy", "Over", "images/BetsySprite/Betsy_Sprite_Over_Shirt2_Up.png"),
                    "True", Null(),
                    ),
            #If she's using arm pose 1, left arm pointing
            #If she's using arm pose 2, Left arm on hip
            "BetsyX.Over == 'towel'", Recolor("Betsy", "Over", "images/BetsySprite/Betsy_Sprite_Over_Towel.png"),
            "BetsyX.Over == 'tank'", Recolor("Betsy", "Over", "images/BetsySprite/Betsy_Sprite_Over_Tank.png"),
            "BetsyX.Over == 'pink top' and BetsyX.ArmPose == 1", Recolor("Betsy", "Over", "images/BetsySprite/Betsy_Sprite_Over_Shirt1.png"),
            "BetsyX.Over == 'pink top'", Recolor("Betsy", "Over", "images/BetsySprite/Betsy_Sprite_Over_Shirt2.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #naked tit piercings
            "not BetsyX.Pierce", Null(),
#            "not BetsyX.Pierce or ((BetsyX.Over or BetsyX.Chest) and not BetsyX.Uptop)", Null(),
#            "BetsyX.Uptop", Null(),
            #Only does this if she has piercings, has no tops, or has her top up
            "BetsyX.Pierce == 'ring'", ConditionSwitch(
                    # if top is up. . .
                    "BetsyX.Uptop", "images/BetsySprite/Betsy_Sprite_Pierce_Tits_Ring.png",

                    "BetsyX.Over == 'tank'", "images/BetsySprite/Betsy_Sprite_Pierce_Tits_Ring_Blue.png",
                    "BetsyX.Over == 'pink top'", "images/BetsySprite/Betsy_Sprite_Pierce_Tits_Ring_Pink.png", #change if new tops added in other colors
                    "BetsyX.Over == 'towel'", "images/BetsySprite/Betsy_Sprite_Pierce_Tits_Ring_Pink.png", #change if new tops added in other colors

                    "BetsyX.Panties == 'swimsuit' and BetsyX.Chest != 'swimsuit'", "images/BetsySprite/Betsy_Sprite_Pierce_Tits_Ring.png",
                    "BetsyX.Chest == 'lace bra'", "images/BetsySprite/Betsy_Sprite_Pierce_Tits_Ring_Lace.png",
#                    "BetsyX.Chest == 'swimsuit' or BetsyX.Chest == 'bra'", "images/BetsySprite/Betsy_Sprite_Pierce_Tits_Ring_Blue.png",
                    # Modification mode
                    "BetsyX.Chest == 'cammy leotard'", "images/BetsySprite/modification/Betsy_Sprite_Pierce_Tits_Ring_Cammy.png",
                    # -----------------
                    "BetsyX.Chest", "images/BetsySprite/Betsy_Sprite_Pierce_Tits_Ring_Blue.png",
                    "True", "images/BetsySprite/Betsy_Sprite_Pierce_Tits_Ring.png",
                    ),
            # Pierce is "barbell"
            "BetsyX.Uptop", "images/BetsySprite/Betsy_Sprite_Pierce_Tits_Barbell.png",

            "BetsyX.Over == 'tank'", "images/BetsySprite/Betsy_Sprite_Pierce_Tits_Barbell_Blue.png",
            "BetsyX.Over == 'pink top'", "images/BetsySprite/Betsy_Sprite_Pierce_Tits_Barbell_Pink.png", #change if new tops added in other colors
            "BetsyX.Over == 'towel'", "images/BetsySprite/Betsy_Sprite_Pierce_Tits_Barbell_Pink.png", #change if new tops added in other colors

            "BetsyX.Panties == 'swimsuit' and BetsyX.Chest != 'swimsuit'", "images/BetsySprite/Betsy_Sprite_Pierce_Tits_Barbell.png",
            "BetsyX.Chest == 'lace bra'", "images/BetsySprite/Betsy_Sprite_Pierce_Tits_Barbell_Lace.png",
#            "BetsyX.Chest == 'swimsuit' or BetsyX.Chest == 'bra'", "images/BetsySprite/Betsy_Sprite_Pierce_Tits_Barbell_Blue.png",
            # Modification mode
            "BetsyX.Chest == 'cammy leotard'", "images/BetsySprite/modification/Betsy_Sprite_Pierce_Tits_Barbell_Cammy.png",
            # ----------------
            "BetsyX.Chest", "images/BetsySprite/Betsy_Sprite_Pierce_Tits_Barbell_Blue.png",

            "True", "images/BetsySprite/Betsy_Sprite_Pierce_Tits_Barbell.png",
            ),

        (0,0), ConditionSwitch(
            #Boots/Shoes
            "BetsyX.Boots == 'sneaks'", "images/BetsySprite/Betsy_Sprite_Sneaks.png",
            "BetsyX.Boots == 'shoes'", "images/BetsySprite/Betsy_Sprite_Shoes.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Scarf
            # Modification mode
            "BetsyX.Acc and 'scarf' in BetsyX.Acc", "images/BetsySprite/Betsy_Sprite_Scarf.png",
            # -----------------
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #arms top
            # Modification mode
            "BetsyX.ArmPose != 1 and BetsyX.Arms == 'cammy gloves'", "images/BetsySprite/modification/[BetsyX.skin_image.skin_path]Betsy_Sprite_Arm_Top2Cammy.png",
            # -----------------
            "BetsyX.ArmPose != 1 and BetsyX.Arms", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Arm_Top2G.png",         # right hand up/left down
            "BetsyX.ArmPose != 1", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Arm_Top2.png",         # right hand up/left down
            # Modification mode
            "BetsyX.Arms == 'cammy gloves'", "images/BetsySprite/modification/[BetsyX.skin_image.skin_path]Betsy_Sprite_Arm_Top1Cammy.png",         # right hand up/left down
            # -----------------
            "BetsyX.Arms", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Arm_Top1G.png",         # right hand up/left down
            "True", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Arm_Top1.png", #if BetsyX.Arms == 1   # right Hand on hip/left raised
            ),
        (0,0), ConditionSwitch(
            #arms shirt over
            "BetsyX.ArmPose != 1 and BetsyX.Over == 'pink top'", Recolor("Betsy", "Over", "images/BetsySprite/Betsy_Sprite_Over_Shirt2_Arm.png"),         # right hand up/left down
            "BetsyX.ArmPose != 1 and BetsyX.Over == 'jacket'", Recolor("Betsy", "Over", "images/BetsySprite/Betsy_Sprite_Over_Jacket2_Arm.png"),         # right hand up/left down
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #Arms 1 upper layer

#            "BetsyX.Over == 'open suit' and BetsyX.ArmPose == 1", "images/BetsySprite/Betsy_Sprite_Arm1_Top_Suit_Up.png",                                  #no gloved 1
#            "BetsyX.Over == 'open suit'", "images/BetsySprite/Betsy_Sprite_Arm2_Top_Suit_Up.png",

#            "BetsyX.Uptop and BetsyX.Over == 'suit' and BetsyX.ArmPose == 1 and BetsyX.Arms", "images/BetsySprite/Betsy_Sprite_Arm1_Top_SuitG_Up.png", #gloved 1
#            "BetsyX.Uptop and BetsyX.Over == 'suit' and BetsyX.ArmPose == 1", "images/BetsySprite/Betsy_Sprite_Arm1_Top_Suit_Up.png",                 #no gloved 1
#            "BetsyX.Uptop and BetsyX.Over == 'suit' and BetsyX.Arms", "images/BetsySprite/Betsy_Sprite_Arms2_Top_SuitG_Up.png",                        #gloved 2
#            "BetsyX.Uptop and BetsyX.Over == 'suit'", "images/BetsySprite/Betsy_Sprite_Arms2_Top_Suit_Up.png",

#            "BetsyX.Over == 'suit' and BetsyX.ArmPose == 1 and BetsyX.Arms", "images/BetsySprite/Betsy_Sprite_Arms1_Top_SuitG.png",                   #gloved 1
#            "BetsyX.Over == 'suit' and BetsyX.ArmPose == 1", "images/BetsySprite/Betsy_Sprite_Arms1_Top_Suit.png",                                  #no gloved 1
#            "BetsyX.Over == 'suit' and BetsyX.Arms", "images/BetsySprite/Betsy_Sprite_Arms2_Top_SuitG.png",                                          #gloved 2
#            "BetsyX.Over == 'suit'", "images/BetsySprite/Betsy_Sprite_Arms2_Top_Suit.png",                                                         #no gloved 2

#            "BetsyX.ArmPose == 1", "images/BetsySprite/Betsy_Sprite_Arms1_Top.png",        #If she's using arm pose 1, right arm high
#            "True", "images/BetsySprite/Betsy_Sprite_Arms2_Top.png",  #if BetsyX.Arms ==2                                        #If she's using arm pose 2, Left arm high
#            ),
#        (0,0), ConditionSwitch(
#            #Water effect
#            "BetsyX.Water and BetsyX.ArmPose == 1", "images/BetsySprite/Betsy_Sprite_Water1_Arm.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #belly spunk
            "'belly' in BetsyX.Spunk and Player.Male", "images/BetsySprite/Betsy_Sprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast spunk
            "'tits' in BetsyX.Spunk and Player.Male", "images/BetsySprite/Betsy_Sprite_Spunk_Tits.png",
            "True", Null(),
            ),

        (15,-80), "Betsy_Sprite_Head", #(-10,-90)


#        (0,0), "images/BetsySprite/Betsy_Sprite_Headref.png", #53,-45


#        (0,0), ConditionSwitch(
#            #hand spunk
#            "BetsyX.ArmPose == 2 or 'hand' not in BetsyX.Spunk", Null(),
#            "True", "images/BetsySprite/Betsy_Sprite_Spunk_Hand.png",
#            ),
#        (0,0), ConditionSwitch(                                                                         #Props
#            "not BetsyX.Held or BetsyX.ArmPose != 2", Null(),
#            "BetsyX.ArmPose == 2 and BetsyX.Held == 'phone'", "images/BetsySprite/Betsy_held_phone.png",
#            "BetsyX.ArmPose == 2 and BetsyX.Held == 'dildo'", "images/BetsySprite/Betsy_held_dildo.png",
#            "BetsyX.ArmPose == 2 and BetsyX.Held == 'vibrator'", "images/BetsySprite/Betsy_held_vibrator.png",
#            "BetsyX.ArmPose == 2 and BetsyX.Held == 'panties'", "images/BetsySprite/Betsy_held_panties.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #psy knife
            "BetsyX.ArmPose != 1 and BetsyX.Knife", "Betsy_Knife", #"images/BetsySprite/Betsy_Sprite_Knife.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #UI tool for When Rogue is masturbating using RogueX.Offhand actions while lead
            "Trigger == 'lesbian' or not BetsyX.Offhand",Null(),# or Ch_Focus is not BetsyX", Null(),
            "BetsyX.Offhand == 'fondle pussy' and Trigger != 'sex' and BetsyX.Lust >= 70", "GirlFingerPussy_Betsy",
            "BetsyX.Offhand == 'fondle pussy'", "GirlGropePussy_Betsy",
            "BetsyX.Offhand == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeLeftBreast_Betsy",    #When zero is working the right breast, fondle left
            "BetsyX.Offhand == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeRightBreast_Betsy", #When zero is working the left breast, fondle right
            "BetsyX.Offhand == 'fondle breasts'", "GirlGropeRightBreast_Betsy",
            "BetsyX.Offhand == 'vibrator breasts'", "VibratorRightBreast_Betsy",
            "BetsyX.Offhand == 'vibrator pussy'", "VibratorPussy_Betsy",
            "BetsyX.Offhand == 'vibrator pussy insert'", "VibratorPussy_Betsy",
            "BetsyX.Offhand == 'vibrator anal'", "VibratorAnal_Betsy",
            "BetsyX.Offhand == 'vibrator anal insert'", "VibratorPussy_Betsy",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #UI tool for RogueX.Offhand(lesbian) actions (ie Kitty's hand on her when Rogue is secondary)
            "not Partner or Partner is BetsyX or BetsyX in Nearby", Null(),
            "Partner.Offhand == 'fondle girl pussy' and Trigger != 'sex' and BetsyX.Lust >= 70", "GirlFingerPussy_Betsy",
            "Partner.Offhand == 'fondle girl pussy'", "GirlGropePussy_Betsy",
            "Partner.Offhand == 'lick girl pussy'", "Lickpussy_Betsy",
            "Partner.Offhand == 'suck girl breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Betsy",
            "Partner.Offhand == 'suck girl breasts'", "LickRightBreast_Betsy",
            "Partner.Offhand == 'fondle girl breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Betsy",    #When zero is working the right breast, fondle left
            "Partner.Offhand == 'fondle girl breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Betsy", #When zero is working the left breast, fondle right
            "Partner.Offhand == 'fondle girl breasts'", "GirlGropeRightBreast_Betsy",
            "Partner.Offhand == 'vibrator girl breasts'", "VibratorRightBreast_Betsy",
            "Partner.Offhand == 'vibrator girl pussy'", "VibratorPussy_Betsy",
            "Partner.Offhand == 'vibrator girl pussy insert'", "VibratorPussy_Betsy",
            "Partner.Offhand == 'vibrator girl anal'", "VibratorAnal_Betsy",
            "Partner.Offhand == 'vibrator girl anal insert'", "VibratorPussy_Betsy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for when RogueX is the partner in the scene, and the lead is working on her
            "not Partner or Partner is not BetsyX", Null(),
            "Ch_Focus.Offhand == 'fondle girl pussy' and Trigger != 'sex' and BetsyX.Lust >= 70", "GirlFingerPussy_Betsy",
            "Ch_Focus.Offhand == 'fondle girl pussy'", "GirlGropePussy_Betsy",
            "Ch_Focus.Offhand == 'lick girl pussy'", "Lickpussy_Betsy",
            "Ch_Focus.Offhand == 'suck girl breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Betsy",
            "Ch_Focus.Offhand == 'suck girl breasts'", "LickRightBreast",
            "Ch_Focus.Offhand == 'fondle girl breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Betsy",    #When zero is working the right breast, fondle left
            "Ch_Focus.Offhand == 'fondle girl breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Betsy", #When zero is working the left breast, fondle right
            "Ch_Focus.Offhand == 'fondle girl breasts'", "GirlGropeRightBreast_Betsy",
            "Ch_Focus.Offhand == 'vibrator girl breasts'", "VibratorRightBreast_Betsy",
            "Ch_Focus.Offhand == 'vibrator girl pussy'", "VibratorPussy_Betsy",
            "Ch_Focus.Offhand == 'vibrator girl pussy insert'", "VibratorPussy_Betsy",
            "Ch_Focus.Offhand == 'vibrator girl anal'", "VibratorAnal_Betsy",
            "Ch_Focus.Offhand == 'vibrator girl anal insert'", "VibratorPussy_Betsy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger1(primary) actions
            "not Trigger or Ch_Focus is not BetsyX", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast_Betsy",
            "Trigger == 'fondle thighs'", "GropeThigh_Betsy",
            "Trigger == 'fondle breasts'", "GropeLeftBreast_Betsy",
            "Trigger == 'suck breasts'", "LickRightBreast_Betsy",
            "Trigger == 'vibrator pussy'", "VibratorPussy_Betsy",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy_Betsy",
            "Trigger == 'vibrator anal'", "VibratorAnal_Betsy",
            "Trigger == 'vibrator anal insert'", "VibratorPussy_Betsy",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_Betsy",
            "Trigger == 'fondle pussy'", "GropePussy_Betsy",
            "Trigger == 'lick pussy'", "Lickpussy_Betsy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus is not BetsyX", Null(),
#            "Trigger == 'fondle breasts' and not BetsyX.Offhand", "GropeRightBreast_Betsy",  #"Trigger == 'fondle breasts' and not RogueX.Offhand",
            #When doing nothing offhand, use both hands on breasts.
            "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast_Betsy",
            #When sucking right breast, fondle left
            "Trigger2 == 'fondle breasts'", "GropeLeftBreast_Betsy",
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast_Betsy",
            #When sucking right breast, vibrator left
            "Trigger2 == Trigger", Null(),
            #When both triggers are the same, do nothing
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast_Betsy",
            "Trigger2 == 'suck breasts'", "LickLeftBreast_Betsy",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy_Betsy",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy_Betsy",
            "Trigger2 == 'vibrator anal'", "VibratorAnal_Betsy",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy_Betsy",
            "Trigger2 == 'fondle pussy'", "GropePussy_Betsy",
            "Trigger2 == 'lick pussy'", "Lickpussy_Betsy",
            "Trigger2 == 'fondle thighs'", "GropeThigh_Betsy",
            "True", Null(),
            ),

        )
    anchor (0.5, 0.0)
    offset (60,30)#(60,10)
    zoom .83 #.86  #.81


image Betsy_Sprite_HairBack:
    LiveComposite(
        (900,900),
        (0,0), ConditionSwitch(
                #hair back
    #            "renpy.showing('Betsy_BJ_Animation')", Null(),
    #            "renpy.showing('Betsy_SexSprite')", "images/BetsySex/Betsy_Sprite_Hair_Long_UnderSex.png",
                "BetsyX.Hair == 'blonde'", Recolor("Betsy", "Hair", "images/BetsySprite/Betsy_Sprite_Hair_Blonde_Back.png"),
                "BetsyX.Hair == 'wetlong'", Recolor("Betsy", "Hair", "images/BetsySprite/Betsy_Sprite_Hair_Long_Back.png"),
                "BetsyX.Hair == 'long'", Recolor("Betsy", "Hair", "images/BetsySprite/Betsy_Sprite_Hair_Long_Back.png"),
                "BetsyX.Hair == 'wet' or BetsyX.Water", Recolor("Betsy", "Hair", "images/BetsySprite/Betsy_Sprite_Hair_Wet_Back.png"),
                "not Player.Male and 'facial' in BetsyX.Spunk",Recolor("Betsy", "Hair", "images/BetsySprite/Betsy_Sprite_Hair_Wet_Back.png"),
                "True", Recolor("Betsy", "Hair", "images/BetsySprite/Betsy_Sprite_Hair_Short_Back.png"),
                ),
        )
    anchor (0.5, 0.5)
    zoom .45#.47
    transform_anchor True
    rotate -10


image Betsy_Sprite_Head:
    LiveComposite(
        (900,900),
        (0,0), ConditionSwitch(
                # Face background plate
#                "renpy.showing('Betsy_SexSprite') and BetsyX.Blush >= 2", "images/BetsySprite/Betsy_Sprite_Head_Sex_Blush2.png",
#                "renpy.showing('Betsy_SexSprite') and BetsyX.Blush", "images/BetsySprite/Betsy_Sprite_Head_Sex_Blush1.png",
#                "renpy.showing('Betsy_SexSprite')", "images/BetsySprite/Betsy_Sprite_Head_Sex.png",
                "BetsyX.Blush >= 2", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Head_Blush2.png",
                "BetsyX.Blush", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Head_Blush1.png",
                "True", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Head.png",
                ),
        (0,0), ConditionSwitch(
            #chin spunk
            "'chin' in BetsyX.Spunk and Player.Male", "images/BetsySprite/Betsy_Sprite_Spunk_Chin.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Mouths
            "BetsyX.Mouth == 'lipbite'", Recolor("Betsy", "Lips", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Mouth_Lipbite.png"),
            "BetsyX.Mouth == 'sucking'", Recolor("Betsy", "Lips", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Mouth_Open.png"),
            "BetsyX.Mouth == 'kiss'", Recolor("Betsy", "Lips", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Mouth_Kiss.png"),
            "BetsyX.Mouth == 'sad'", Recolor("Betsy", "Lips", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Mouth_Sad.png"),
            "BetsyX.Mouth == 'smile'", Recolor("Betsy", "Lips", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Mouth_Smile.png"),
            "BetsyX.Mouth == 'surprised'", Recolor("Betsy", "Lips", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Mouth_Open.png"),
#            "not Player.Male and 'mouth' in BetsyX.Spunk and BetsyX.Mouth == 'tongue'", Recolor("Betsy", "Lips", "images/BetsySprite/Betsy_Sprite_Mouth_Tongue_Wet.png"),
            "BetsyX.Mouth == 'tongue'", Recolor("Betsy", "Lips", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Mouth_Tongue.png"),
            "BetsyX.Mouth == 'grimace'", Recolor("Betsy", "Lips", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Mouth_Smile.png"),
            "BetsyX.Mouth == 'smirk'", Recolor("Betsy", "Lips", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Mouth_Smirk.png"),
            "BetsyX.Mouth == 'open'", Recolor("Betsy", "Lips", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Mouth_Open.png"),
            "True", Recolor("Betsy", "Lips", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Mouth_Normal.png"),
            ),
        (0,0), ConditionSwitch(
            #Mouths spunk
            "'mouth' not in BetsyX.Spunk or not Player.Male", Null(),
            "BetsyX.Mouth == 'sucking'", "images/BetsySprite/Betsy_Sprite_Spunk_Tongue.png",
            "BetsyX.Mouth == 'kiss'", "images/BetsySprite/Betsy_Sprite_Spunk_Sad.png",
            "BetsyX.Mouth == 'sad'", "images/BetsySprite/Betsy_Sprite_Spunk_Sad.png",
            "BetsyX.Mouth == 'smile'", "images/BetsySprite/Betsy_Sprite_Spunk_Smile.png",
            "BetsyX.Mouth == 'surprised'", "images/BetsySprite/Betsy_Sprite_Spunk_Open.png",
            "BetsyX.Mouth == 'tongue'", "images/BetsySprite/Betsy_Sprite_Spunk_Tongue.png",
            "BetsyX.Mouth == 'grimace'", "images/BetsySprite/Betsy_Sprite_Spunk_Smile.png",
            "True", "images/BetsySprite/Betsy_Sprite_Spunk_Normal.png",
            ),
        (0,0), ConditionSwitch(
            #wet face
            "Player.Male", Null(),
            "'mouth' not in BetsyX.Spunk and 'chin' not in BetsyX.Spunk", Null(),
#            "'chin' not in BetsyX.Spunk and BetsyX.Mouth == 'tongue'", "images/BetsySprite/Betsy_Sprite_Wet_Tongue.png",
#            "BetsyX.Mouth == 'tongue'", "images/BetsySprite/Betsy_Sprite_Wet_Tongue2.png",
            "'chin' in BetsyX.Spunk", "images/BetsySprite/Betsy_Sprite_Wet_Mouth.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(     #    (0,5)
            #brows
            "BetsyX.Brows == 'angry'", "images/BetsySprite/Betsy_Sprite_Brows_Angry.png",
            "BetsyX.Brows == 'sad'", "images/BetsySprite/Betsy_Sprite_Brows_Sad.png",
            "BetsyX.Brows == 'surprised'", "images/BetsySprite/Betsy_Sprite_Brows_Surprised.png",
            "BetsyX.Brows == 'confused'", "images/BetsySprite/Betsy_Sprite_Brows_Confused.png",
            "True", "images/BetsySprite/Betsy_Sprite_Brows_Normal.png",
            ),
        (0,0), "Betsy Blink",     #Eyes  (0,5)
        (0,0), ConditionSwitch(
            #Hair over
#            "renpy.showing('Betsy_TJ_Animation')", Null(),
            "BetsyX.Hair == 'blonde'", Recolor("Betsy", "Hair", "images/BetsySprite/Betsy_Sprite_Hair_Blonde.png"),
            "BetsyX.Hair == 'wet' or BetsyX.Hair == 'wetlong' or BetsyX.Water", Recolor("Betsy", "Hair", "images/BetsySprite/Betsy_Sprite_Hair_Wet.png"),
            "not Player.Male and 'facial' in BetsyX.Spunk",Recolor("Betsy", "Hair", "images/BetsySprite/Betsy_Sprite_Hair_Wet.png"),
#                "BetsyX.Hair == 'pony'", "images/BetsySprite/Betsy_Sprite_Hair_Pony.png",
            "True", Recolor("Betsy", "Hair", "images/BetsySprite/Betsy_Sprite_Hair_Short.png"),
            ),
        (0,0), "images/BetsySprite/Betsy_Sprite_Earring.png",     #Eyes  (0,5)
        # Modification mode
        (0,0), ConditionSwitch(
            "BetsyX.Hat == 'red beret'", "images/BetsySprite/modification/Betsy_Sprite_Hat_Beret.png",
            "True",Null(),
            ),
        # -----------------
        (0,0), ConditionSwitch(
            #Hair Water
            "BetsyX.Water", "images/BetsySprite/Betsy_Sprite_Water_Head.png",
            "not Player.Male and 'facial' in BetsyX.Spunk", "images/BetsySprite/Betsy_Sprite_Water_Head.png",
            "True",Null(),
            ),
        (0,0), ConditionSwitch(
            #facial spunk
            "'hair' in BetsyX.Spunk and Player.Male", "images/BetsySprite/Betsy_Sprite_Spunk_Facial2.png",
            "'facial' in BetsyX.Spunk and Player.Male", "images/BetsySprite/Betsy_Sprite_Spunk_Facial1.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(     #    (0,5)
            #brows
            "BetsyX.Eyes == 'psychic'", "Betsy_Psy",#"images/BetsySprite/Betsy_Sprite_Psychic.png",
            "True", Null(),
            ),
        )
    anchor (0.5, 0.5)
    zoom .45#.38
    transform_anchor True
    rotate -10
#    alpha 0.9

image Betsy Blink:
    ConditionSwitch(
    "BetsyX.Eyes == 'closed'", "images/BetsySprite/Betsy_Sprite_Eyes_Closed.png",
    "BetsyX.Eyes == 'sexy'", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Eyes_Sexy.png",
    "BetsyX.Eyes == 'side'", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Eyes_Side.png",
    "BetsyX.Eyes == 'surprised'", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Eyes_Surprised.png",
    "BetsyX.Eyes == 'normal'", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Eyes_Normal.png",
    "BetsyX.Eyes == 'stunned'", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Eyes_Stunned.png",
    "BetsyX.Eyes == 'down'", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Eyes_Down.png",
    "BetsyX.Eyes == 'leftside'", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Eyes_Leftside.png",
    "BetsyX.Eyes == 'manic'", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Eyes_Sexy.png",#"images/BetsySprite/Betsy_Sprite_Eyes_Squint.png",
    "BetsyX.Eyes == 'squint'", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Eyes_Sexy.png",#"Betsy_Squint",
    "True", "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Eyes_Normal.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/BetsySprite/Betsy_Sprite_Eyes_Closed.png"
    .25
    repeat

image Betsy_Psy:
    "images/BetsySprite/Betsy_Sprite_Psychic.png"
    alpha 1
    choice:
        ease 1 alpha .9
        ease 1 alpha 1
    choice:
        ease .5 alpha .9
        ease .5 alpha 1
#    .25
    repeat

image Betsy_Knife:
    "images/BetsySprite/Betsy_Sprite_Knife.png"
    alpha 1
    choice:
        ease 1 alpha .8
        ease 1 alpha 1
    choice:
        ease .5 alpha .8
        ease .5 alpha 1
#    .25
    repeat
#image Betsy_Squint:
#    "images/BetsySprite/[BetsyX.skin_image.skin_path]Betsy_Sprite_Eyes_Sexy.png"
#    choice:
#        3.5
#    choice:
#        3.25
#    choice:
#        3
#    "images/BetsySprite/Betsy_Sprite_Eyes_Squint.png"
#    .25
#    repeat


#image Betsy_Drip_Mask:
#    #This is the mask for her drip pattern
#    contains:
#        "images/BetsySprite/Betsy_Sprite_WetMask.png"
#        offset (-275,-560)#(-145,-560)#(-225,-560)

#image Betsy_Drip_MaskPanties:
#    #This is the mask for her drip pattern in panties down mode
#    contains:
#        "images/BetsySprite/Betsy_Sprite_DripMaskPanties.png"
#        offset (-145,-560)#(-225,-560)

#image Betsy_Drip_MaskP:
#    #This is the mask for her drip pattern in panties down mode
#    contains:
#        "images/BetsySprite/Betsy_Sprite_WetMask_Pants.png"
#        offset (-275,-560)#(-145,-560)

# End Betsy Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Betsy Doggy Compositing ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#image Betsy_Doggy_Base = LiveComposite(
image Betsy_Doggy_Animation: #nee Betsy_Doggy
    LiveComposite(
        #Base body
        (420,750),
        (0,0), ConditionSwitch(
            #Shows different upper body motion depending on events
            "not Player.Sprite", "Betsy_Doggy_Body",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Betsy_Doggy_Fuck2_Top",
                    "Speed > 1", "Betsy_Doggy_Fuck_Top",
                    "Speed", "Betsy_Doggy_Anal_Head_Top",
                    "True", "Betsy_Doggy_Body",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Betsy_Doggy_Fuck2_Top",
                    "Speed > 1", "Betsy_Doggy_Fuck_Top",
                    "True", "Betsy_Doggy_Body",
                    ),
            "Player.Cock == 'foot'", ConditionSwitch(
                    "Speed > 1", "Betsy_Doggy_Foot2_Top",
                    "Speed", "Betsy_Doggy_Foot1_Top",
                    "True", "Betsy_Doggy_Foot0_Top",
                    ),
            "True", "Betsy_Doggy_Body",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events
            "not Player.Sprite", "Betsy_Doggy_Ass",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Betsy_Doggy_Fuck2_Ass",
                    "Speed > 1", "Betsy_Doggy_Fuck_Ass",
                    "Speed", "Betsy_Doggy_Anal_Head_Ass",
                    "True", "Betsy_Doggy_Ass",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Betsy_Doggy_Fuck2_Ass",
                    "Speed > 1", "Betsy_Doggy_Fuck_Ass",
                    "True", "Betsy_Doggy_Ass",
                    ),
            "Player.Cock == 'foot'", ConditionSwitch(
                    "Speed > 1", "Betsy_Doggy_Foot2_Ass",
                    "Speed", "Betsy_Doggy_Foot1_Ass",
                    "True", "Betsy_Doggy_Foot0_Ass",
                    ),
            "True", "Betsy_Doggy_Ass",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
#            "not Player.Sprite", "Betsy_Doggy_Shins0",
            "Player.Sprite and Player.Cock == 'foot'", ConditionSwitch(
                    "Speed > 1", "Betsy_Doggy_Feet2",
                    "Speed", "Betsy_Doggy_Feet1",
                    "True", "Betsy_Doggy_Feet0",
                    ),
            "ShowFeet", "Betsy_Doggy_Shins0",# "not Player.Sprite and ShowFeet", "Betsy_Doggy_Shins",
            "True", Null(),
            ),
        )
    align (0.6,0.0)
    #yoffset 50
# End Base / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Betsy_Doggy_Body:
    LiveComposite(
        #Upper body
        (610,750),
        #(165,0),"Betsy_Doggy_Hair_Under", #back of the hair
#        (0,60), "Betsy_Doggy_Head",               #Head

        (0,0), ConditionSwitch(
            #head
            "BetsyX.Facing", "Betsy_Doggy_Head_Fore",
            "True", "Betsy_Doggy_Head",
            ),
        #(0,0), "images/BetsyDoggy/Betsy_Doggy_HeadRef.png",               #Head

        (0,0), "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Body.png", #Body base
        (0,0), ConditionSwitch(
            #Legs Layer
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
            "BetsyX.Legs == 'shorts' and not BetsyX.Upskirt and not BetsyX.PantiesDown", Recolor("Betsy", "Legs", "images/BetsyDoggy/Betsy_Doggy_Legs_Shorts_Body.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #gloves
            # Modification mode
            "BetsyX.Arms == 'cammy gloves'", "images/BetsyDoggy/modification/Betsy_Doggy_Gloves_Cammy.png",
            # -----------------
            "BetsyX.Arms", "images/BetsyDoggy/Betsy_Doggy_Gloves.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #chest layer
            "not BetsyX.Chest and BetsyX.Panties != 'swimsuit'", Null(),
            "BetsyX.Uptop", ConditionSwitch(
                    "BetsyX.Chest == 'swimsuit' or BetsyX.Panties == 'swimsuit'", Recolor("Betsy", "Chest", "images/BetsyDoggy/Betsy_Doggy_Chest_Bikini_Up.png"),
                    "BetsyX.Chest == 'sports bra'", Recolor("Betsy", "Chest", "images/BetsyDoggy/Betsy_Doggy_Chest_Sports_Up.png"),
                    "BetsyX.Chest == 'lace bra'", Recolor("Betsy", "Chest", "images/BetsyDoggy/Betsy_Doggy_Chest_Lace_Up.png"),
                    # Modification mode
                    "BetsyX.Chest == 'cammy leotard' or BetsyX.Panties == 'cammy leotard'", "images/BetsyDoggy/modification/Betsy_Doggy_Chest_Cammy_Up.png",
                    # ----------------
                    "True", Recolor("Betsy", "Chest", "images/BetsyDoggy/Betsy_Doggy_Chest_Bra_Up.png"),
                    ),
            # Modification mode
            "BetsyX.Chest == 'cammy leotard' or BetsyX.Panties == 'cammy leotard'", "images/BetsyDoggy/modification/Betsy_Doggy_Chest_Cammy.png",
            # -----------------
            "BetsyX.Chest == 'swimsuit' or BetsyX.Panties == 'swimsuit'", Recolor("Betsy", "Chest", "images/BetsyDoggy/Betsy_Doggy_Chest_Bikini.png"),
            "BetsyX.Chest == 'sports bra'", Recolor("Betsy", "Chest", "images/BetsyDoggy/Betsy_Doggy_Chest_Sports.png"),
            "BetsyX.Chest == 'lace bra'", Recolor("Betsy", "Chest", "images/BetsyDoggy/Betsy_Doggy_Chest_Lace.png"),
            "True", Recolor("Betsy", "Chest", "images/BetsyDoggy/Betsy_Doggy_Chest_Bra.png"),
            ),
#        (0,0), ConditionSwitch(
#            #Wet look
#            "BetsyX.Water", "images/RogueDoggy/Rogue_Doggy_WetTop.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Overshirt
            "not BetsyX.Over", Null(),
            "BetsyX.Over == 'jacket'", Recolor("Betsy", "Over", "images/BetsyDoggy/Betsy_Doggy_Over_Jacket.png"),
            "BetsyX.Over == 'pink top' and BetsyX.Uptop", Recolor("Betsy", "Over", "images/BetsyDoggy/Betsy_Doggy_Over_Pink_Up.png"),
            "BetsyX.Over == 'pink top'", Recolor("Betsy", "Over", "images/BetsyDoggy/Betsy_Doggy_Over_Pink.png"),
            "BetsyX.Over == 'tank' and BetsyX.Uptop", Recolor("Betsy", "Over", "images/BetsyDoggy/Betsy_Doggy_Over_Tank_Up.png"),
            "BetsyX.Over == 'tank'", Recolor("Betsy", "Over", "images/BetsyDoggy/Betsy_Doggy_Over_Tank.png"),
            "BetsyX.Over == 'towel' and BetsyX.Uptop", Null(), #"images/BetsyDoggy/Betsy_Doggy_Over_Towel_Up.png",
            "BetsyX.Over == 'towel'", Recolor("Betsy", "Over", "images/BetsyDoggy/Betsy_Doggy_Over_Towel.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #spunk back Layer
            "'back' in BetsyX.Spunk and Player.Male", "images/BetsyDoggy/Betsy_Doggy_Spunk_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast fondling animation
            "Trigger == 'fondle breasts' or Trigger2 == 'fondle breasts'", "Betsy_Doggy_GropeBreast",
            "True", Null()
            ),
        (0,0), ConditionSwitch(
            #Hair Fore
            "not BetsyX.Facing", Null(),
            "BetsyX.Hair == 'blonde'", Recolor("Betsy", "Hair", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Hair_Fore_Blonde.png"),
            "BetsyX.Hair == 'long'", Recolor("Betsy", "Hair", "images/BetsyDoggy/Betsy_Doggy_Hair_Fore_Long.png"),
#            "(BetsyX.Water and BetsyX.Hair == 'long') or BetsyX.Hair == 'wetlong'", Recolor("Betsy", "Hair", "images/BetsyDoggy/Betsy_Doggy_Hair_Fore_Long.png"),
            "BetsyX.Water or BetsyX.Hair == 'wet'", Recolor("Betsy", "Hair", "images/BetsyDoggy/Betsy_Doggy_Hair_Fore_Wet.png"),
            "not Player.Male and 'facial' in BetsyX.Spunk",Recolor("Betsy", "Hair", "images/BetsyDoggy/Betsy_Doggy_Hair_Fore_Wet.png"),
#            "BetsyX.Hair == 'long'", Recolor("Betsy", "Hair", "images/BetsyDoggy/Betsy_Doggy_Hair_Fore_Long.png"),
            "True", Recolor("Betsy", "Hair", "images/BetsyDoggy/Betsy_Doggy_Hair_Fore_Short.png"),
            ),
        # Modification mode
        (0,0), ConditionSwitch(
            "not BetsyX.Facing", Null(),
            "BetsyX.Hat == 'red beret'", "images/BetsyDoggy/modification/Betsy_Doggy_Hat_Cammy_Fore.png",
            "True", Null()
            ),
        # -----------------
        #(161,-1), "Betsy_Doggy_Head",               #Head
        #(165,0),"Betsy_Doggy_Hair_Over", #front of the hair
        )
    zoom 1.1
    offset (-20,-40)
#    transform_anchor True
#    anchor (225,1400)
#    offset (-175,25)#(-200,0)
#    offset (0,25)#(-200,0)
#    zoom .95
#    offset (-350,-180)#(-190,-40)
#    rotate 20
# End Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Betsy_Doggy_Head:
    LiveComposite(
        #Head
        (420,525),
        #(0,0), "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Head.png", #Body base
        #(0,0), "images/BetsyDoggy/Betsy_Doggy_TestArm.png",#Eyes
        (0,0), ConditionSwitch(
            #Hair back
            "BetsyX.Hair == 'blonde'", Recolor("Betsy", "Hair", "images/BetsyDoggy/Betsy_Doggy_Hair_Blonde_Under.png"),
            "BetsyX.Water or BetsyX.Hair == 'wet' or BetsyX.Hair == 'wetlong'", Recolor("Betsy", "Hair", "images/BetsyDoggy/Betsy_Doggy_Hair_Wet_Under.png"),
            "not Player.Male and 'facial' in BetsyX.Spunk",Recolor("Betsy", "Hair", "images/BetsyDoggy/Betsy_Doggy_Hair_Wet_Under.png"),
            "True", Recolor("Betsy", "Hair", "images/BetsyDoggy/Betsy_Doggy_Hair_Short_Under.png"),
            ),
        (0,0), ConditionSwitch(
            #Head
            #"BetsyX.Blush > 1", "images/BetsyDoggy/Betsy_Doggy_Head_Blush2.png",
            "BetsyX.Blush", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Head_Blush.png",
            "True", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Head.png",
            ),
        (0,0), ConditionSwitch(
            #Mouth
#            "BetsyX.Mouth == 'lipbite'", Recolor("Betsy", "Lips", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Mouth_Normal.png"),
            "BetsyX.Mouth == 'sucking'", Recolor("Betsy", "Lips", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Mouth_Open.png"),
            "BetsyX.Mouth == 'kiss'", Recolor("Betsy", "Lips", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Mouth_Kiss.png"),
            "BetsyX.Mouth == 'sad'", Recolor("Betsy", "Lips", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Mouth_Sad.png"),
#            "BetsyX.Mouth == 'smile'", Recolor("Betsy", "Lips", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Mouth_Normal.png"),
#            "BetsyX.Mouth == 'grimace'", Recolor("Betsy", "Lips", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Mouth_Normal.png"),
            "BetsyX.Mouth == 'surprised'", Recolor("Betsy", "Lips", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Mouth_Open.png"),
            "BetsyX.Mouth == 'open'", Recolor("Betsy", "Lips", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Mouth_Open.png"),
            "BetsyX.Mouth == 'tongue'", Recolor("Betsy", "Lips", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Mouth_Tongue.png"),
            "True", Recolor("Betsy", "Lips", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Mouth_Normal.png"),
            ),
        (0,0), ConditionSwitch(
            #chin spunk
            "'chin' in BetsyX.Spunk", "images/BetsyDoggy/Betsy_Doggy_Spunk_Chin.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Mouth spunk
            "'mouth' not in BetsyX.Spunk", Null(),
            #"BetsyX.Mouth == 'normal'", "images/BetsyDoggy/Betsy_Doggy_Spunk_Normal.png",
            #"BetsyX.Mouth == 'sad'", "images/BetsyDoggy/Betsy_Doggy_Spunk_Normal.png",
            "BetsyX.Mouth == 'lipbite'", "images/BetsyDoggy/Betsy_Doggy_Spunk_Kiss.png",
#            "BetsyX.Mouth == 'smile'", "images/BetsyDoggy/Betsy_Doggy_Spunk_Smile.png",
#            "BetsyX.Mouth == 'grimace'", "images/BetsyDoggy/Betsy_Doggy_Spunk_Smile.png",
            "BetsyX.Mouth == 'sucking'", "images/BetsyDoggy/Betsy_Doggy_Spunk_Open.png",
            #"BetsyX.Mouth == 'kiss'", "images/BetsyDoggy/Betsy_Doggy_Spunk_Open.png",
            "BetsyX.Mouth == 'surprised'", "images/BetsyDoggy/Betsy_Doggy_Spunk_Open.png",
            "BetsyX.Mouth == 'tongue'", "images/BetsyDoggy/Betsy_Doggy_Spunk_tongue.png",
            "True", "images/BetsyDoggy/Betsy_Doggy_Spunk_Kiss.png",
            ),
        (0,0), ConditionSwitch(
            #Brows
            #"BetsyX.Brows == 'normal'", "images/BetsyDoggy/Betsy_Doggy_Brows_Normal.png",
            "BetsyX.Brows == 'angry'", "images/BetsyDoggy/Betsy_Doggy_Brows_Angry.png",
            "BetsyX.Brows == 'sad'", "images/BetsyDoggy/Betsy_Doggy_Brows_Sad.png",
#            "BetsyX.Brows == 'surprised'", "images/BetsyDoggy/Betsy_Doggy_Brows_Surprised.png",
            "BetsyX.Brows == 'confused'", "images/BetsyDoggy/Betsy_Doggy_Brows_Confused.png",
            "True", "images/BetsyDoggy/Betsy_Doggy_Brows_Normal.png",
            ),
        (0,0), "Betsy Doggy Blink",#Eyes
#        (0,0), ConditionSwitch(
#            #Wet look
#            "BetsyX.Water", "images/RogueDoggy/Rogue_Doggy_WetTop.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Hair
            "BetsyX.Hair == 'blonde'", Recolor("Betsy", "Hair", "images/BetsyDoggy/Betsy_Doggy_Hair_Blonde_Over.png"),
            "BetsyX.Hair == 'long' and BetsyX.Water or BetsyX.Hair == 'wet'", Recolor("Betsy", "Hair", "images/BetsyDoggy/Betsy_Doggy_Hair_Wet_Long_Over.png"),
            "BetsyX.Hair == 'long' and not Player.Male and 'facial' in BetsyX.Spunk",Recolor("Betsy", "Hair", "images/BetsyDoggy/Betsy_Doggy_Hair_Wet_Long_Over.png"),
            "BetsyX.Water or BetsyX.Hair == 'wet'", Recolor("Betsy", "Hair", "images/BetsyDoggy/Betsy_Doggy_Hair_Wet_Short_Over.png"),
            "not Player.Male and 'facial' in BetsyX.Spunk",Recolor("Betsy", "Hair", "images/BetsyDoggy/Betsy_Doggy_Hair_Wet_Short_Over.png"),
            "BetsyX.Hair == 'long'", Recolor("Betsy", "Hair", "images/BetsyDoggy/Betsy_Doggy_Hair_Long_Over.png"),
            "True", Recolor("Betsy", "Hair", "images/BetsyDoggy/Betsy_Doggy_Hair_Short_Over.png"),
            ),
        # Modification mode
        (0,0), ConditionSwitch(
            "BetsyX.Facing", Null(),
            "BetsyX.Hat == 'red beret'", "images/BetsyDoggy/modification/Betsy_Doggy_Hat_Cammy_Side.png",
            "True", Null(),
            ),
        # -----------------
        (0,0), ConditionSwitch(
            #face spunk
            "'hair' in BetsyX.Spunk and Player.Male", "images/BetsyDoggy/Betsy_Doggy_Spunk_Hair.png",
            "'facial' in BetsyX.Spunk and Player.Male", "images/BetsyDoggy/Betsy_Doggy_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #face spunk
            "BetsyX.Water or BetsyX.Hair == 'wet'", "images/BetsyDoggy/Betsy_Doggy_Head_Wet.png",
            "not Player.Male and 'facial' in BetsyX.Spunk","images/BetsyDoggy/Betsy_Doggy_Head_Wet.png",
            "True", Null(),
            ),
        (0,0), "images/BetsyDoggy/Betsy_Doggy_Earring.png",
        )
    #zoom 0.95
    #alpha 0.5
# End Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy Doggy Blink:
        #Eyes
        ConditionSwitch(
        "BetsyX.Eyes == 'sexy'", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Eyes_Normal.png",
        "BetsyX.Eyes == 'side'", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Eyes_Side.png",
#        "BetsyX.Eyes == 'normal'", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Eyes_Normal.png",
        "BetsyX.Eyes == 'closed'", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Eyes_Closed.png",
        "BetsyX.Eyes == 'manic'", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Eyes_Stunned.png",
        "BetsyX.Eyes == 'down'", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Eyes_Down.png",
        "BetsyX.Eyes == 'stunned'", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Eyes_Stunned.png",
        "BetsyX.Eyes == 'surprised'", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Eyes_Surprised.png",
        "BetsyX.Eyes == 'squint'", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Eyes_Normal.png",
        "True", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Eyes_Normal.png",
        ),
        choice:
            3.5
        choice:
            3.25
        choice:
            3
        # This randomizes the time between blinking.
        "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Eyes_Closed.png"
        .25
        repeat

image Betsy_Doggy_Head_Fore:
    LiveComposite(
        #Head
        (420,525),
        (0,0), ConditionSwitch(
            #Hair
            "BetsyX.Hair == 'blonde'", Recolor("Betsy", "Hair", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Hair_Fore_Blonde.png"),
            "BetsyX.Water or BetsyX.Hair == 'wet'", Recolor("Betsy", "Hair", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Head_Fore_Wet.png"),
            "not Player.Male and 'facial' in BetsyX.Spunk",Recolor("Betsy", "Hair", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Head_Fore_Wet.png"),
            "BetsyX.Hair == 'long'", Recolor("Betsy", "Hair", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Head_Fore_Long.png"),
            "True", Recolor("Betsy", "Hair", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Head_Fore_Short.png"),
            ),
        )
    #zoom 0.95
    #alpha 0.5

# End Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_Doggy_Ass:
    LiveComposite(
        #Lower body
        (420,750),
#        (0,0), ConditionSwitch(
#            #Legs backside
#            "BetsyX.Legs == 'skirt'","images/BetsyDoggy/Betsy_Doggy_Legs_Skirt_Back.png",
#            "not BetsyX.Upskirt", Null(),
#            "BetsyX.Legs == 'pants'", "images/BetsyDoggy/Betsy_Doggy_Legs_Pants_Back.png",
#            "BetsyX.Legs == 'yoga pants'", "images/BetsyDoggy/Betsy_Doggy_Legs_Yoga_Back.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #Panties back
#            "not BetsyX.PantiesDown or (BetsyX.Legs == 'pants' and not BetsyX.Upskirt)", Null(),
#            "BetsyX.Panties == 'wolvie panties'", "images/BetsyDoggy/Betsy_Doggy_Panties_Wolvie_Back.png",
#            "BetsyX.Panties == 'lace panties'", "images/BetsyDoggy/Betsy_Doggy_Panties_Lace_Back.png",
#            "BetsyX.Panties", "images/BetsyDoggy/Betsy_Doggy_Panties_Back.png",
#            "True", Null(),
#            ),
#        (0,0), "images/BetsyDoggy/Betsy_Doggy_Ass.png", #Ass Base


        (0,0), ConditionSwitch(
            #Pussy base
            "BetsyX.Legs and not BetsyX.Upskirt", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Ass_Closed.png",
            "BetsyX.Panties and not BetsyX.PantiesDown", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Ass_Closed.png",
            "Player.Sprite and Player.Cock == 'in'", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Ass_Fucking.png",
            "Trigger == 'lick pussy'", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Ass_Open.png",
            "'dildo pussy' in (Trigger,Trigger2,BetsyX.Offhand)", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Ass_Fucking.png",#Null(),
            "'fondle pussy' in (Trigger,Trigger2,BetsyX.Offhand)", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Ass_Fucking.png",#Null(),
            "Trigger == 'insert pussy'", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Ass_Fucking.png",#Null(),
            "True", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Ass_Closed.png",
            ),
        (0,0), ConditionSwitch(
            #ass red
            "BetsyX.Red", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Red.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Anus base
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    "Speed", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Anal_FullBase.png",      #Speed 1
                    "True", Null(),               #Speed 0
                    ),
            "'insert ass' in (Trigger,Trigger2,BetsyX.Offhand)", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Anal_FullBase.png",
            "'dildo anal' in (Trigger,Trigger2,BetsyX.Offhand)", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Anal_FullBase.png",
            "BetsyX.Loose > 2", "Betsy_Gape_Anal",    #intentional
            "BetsyX.Loose", "images/BetsyDoggy/Betsy_Doggy_Asshole_Loose.png",
            "True", "images/BetsyDoggy/Betsy_Doggy_Asshole_Tight.png",
            ),

#        (0,0), ConditionSwitch(
#            #Wet look
#            "BetsyX.Water", "images/RogueDoggy/Rogue_Doggy_WetAss.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #Hose
            "BetsyX.Hose == 'stockings'", Recolor("Betsy", "Hose", "images/BetsyDoggy/Betsy_Doggy_Hose_Stockings.png"),
            "BetsyX.Hose == 'socks'", Recolor("Betsy", "Hose", "images/BetsyDoggy/Betsy_Doggy_Hose_Socks.png"),
#            "Player.Sprite and Player.Cock == 'in'", Null(),
#            "Player.Sprite and Player.Cock == 'anal'", Null(),
            "BetsyX.Hose == 'stockings and garterbelt'", Recolor("Betsy", "Hose", "images/BetsyDoggy/Betsy_Doggy_Hose_StockingsGarter.png"),
            "BetsyX.Hose == 'garterbelt'", Recolor("Betsy", "Hose", "images/BetsyDoggy/Betsy_Doggy_Hose_Garter.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Panties if Down
            "BetsyX.Panties == 'swimsuit' or BetsyX.Chest == 'swimsuit'", Null(),
            "not BetsyX.PantiesDown or (BetsyX.Legs == 'pants' and not BetsyX.Upskirt)", Null(),
            "BetsyX.Panties == 'lace panties'", Recolor("Betsy", "Panties", "images/BetsyDoggy/Betsy_Doggy_Panties_Lace_Down.png"),
            "BetsyX.Panties", Recolor("Betsy", "Panties", "images/BetsyDoggy/Betsy_Doggy_Panties_Blue_Down.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #swimsuit bottoms
            "BetsyX.Panties != 'swimsuit' and BetsyX.Chest != 'swimsuit'", Null(),
            "BetsyX.PantiesDown or (not BetsyX.Panties and BetsyX.Chest == 'swimsuit')", Recolor("Betsy", "Panties", "images/BetsyDoggy/Betsy_Doggy_Panties_Bikini_Fucking.png"),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Recolor("Betsy", "Panties", "images/BetsyDoggy/Betsy_Doggy_Panties_Bikini_Fucking.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #spunkpussy Layer
            "'in' in BetsyX.Spunk and Player.Cock == 'in' and Player.Male",Null(),# "images/BetsyDoggy/Betsy_Doggy_SpunkPussyOpen.png",  #fix for BetsyX.Spunk is used later
            "'in' in BetsyX.Spunk and Player.Male", "images/JeanDoggy/Jean_Doggy_SpunkPussyClosed.png",
            "BetsyX.Wet and Player.Cock == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "BetsyX.Wet", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pubes
            "not BetsyX.Pubes", Null(),
            "Player.Sprite and Player.Cock == 'in'", Null(), # "images/BetsyDoggy/Betsy_Doggy_Pubes_Fuckingucked.png",
            "'dildo pussy' in (Trigger,Trigger2,BetsyX.Offhand)", Null(),
            "'fondle pussy' in (Trigger,Trigger2,BetsyX.Offhand)",Null(),
            "Trigger == 'insert pussy'", Null(),
            "BetsyX.Legs == 'shorts' and not BetsyX.Upskirt", Recolor("Betsy", "Pubes", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Pubes_Clothed.png"),
            "BetsyX.Legs == 'yoga pants' and not BetsyX.Upskirt", Recolor("Betsy", "Pubes", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Pubes_Clothed.png"),
            "BetsyX.PantiesDown and Trigger == 'lick pussy'", Recolor("Betsy", "Pubes", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Pubes_Open.png"),
            "BetsyX.PantiesDown", Recolor("Betsy", "Pubes", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Pubes_Closed.png"),
            "BetsyX.Panties", Recolor("Betsy", "Pubes", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Pubes_Clothed.png"),
            "BetsyX.Hose and BetsyX.Hose == 'pantyhose'", Recolor("Betsy", "Pubes", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Pubes_Clothed.png"),
            "Trigger == 'lick pussy'", Recolor("Betsy", "Pubes", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Pubes_Open.png"),
            "True", Recolor("Betsy", "Pubes", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Pubes_Closed.png"),
            ),
        (1,5), ConditionSwitch(
            #Pussy Piercings
            "Player.Sprite and Player.Cock == 'in'", Null(),
            "BetsyX.Panties and not BetsyX.PantiesDown", Null(),
            "BetsyX.Legs and not BetsyX.Upskirt", Null(),
            "BetsyX.Pierce == 'ring'", "images/LauraDoggy/Laura_Doggy_Pierce_Ring.png",
            "BetsyX.Pierce == 'barbell'", "images/LauraDoggy/Laura_Doggy_Pierce_Barbell.png",
            "True", Null(),
            ),


        (2,-8), ConditionSwitch(
            #spunkanal Layer
            "'anal' not in BetsyX.Spunk or (Player.Sprite and Player.Cock == 'anal' and Speed >= 1) or not Player.Male", Null(),
#            "Player.Cock == 'anal'", "images/BetsyDoggy/Betsy_Doggy_SpunkAnalOpen.png",
            "BetsyX.Loose", "images/JeanDoggy/Jean_Doggy_SpunkAnalLoose.png",
            "True", "images/JeanDoggy/Jean_Doggy_SpunkAnalLoose.png",
            ),
        (0,0), ConditionSwitch(
            #Panties if up
            "BetsyX.PantiesDown or not BetsyX.Panties", Null(),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),
            "BetsyX.Panties == 'swimsuit' or BetsyX.Chest == 'swimsuit'", Recolor("Betsy", "Panties", "images/BetsyDoggy/Betsy_Doggy_Panties_Blue.png"),
            "BetsyX.Panties == 'lace panties'", Recolor("Betsy", "Panties", "images/BetsyDoggy/Betsy_Doggy_Panties_Lace.png"),
            "BetsyX.Panties == 'swimsuit'", Recolor("Betsy", "Panties", "images/BetsyDoggy/Betsy_Doggy_Panties_Blue.png"),
            # Modification mode
            "BetsyX.Panties == 'cammy leotard' or BetsyX.Chest == 'cammy leotard'", "images/BetsyDoggy/modification/Betsy_Doggy_Panties_Cammy.png",
            "BetsyX.Panties == 'cammy leotard'", "images/BetsyDoggy/modification/Betsy_Doggy_Panties_Cammy.png",
            # ----------------
            "BetsyX.Wet", Recolor("Betsy", "Panties", "images/BetsyDoggy/Betsy_Doggy_Panties_Blue_Wet.png"),
            "True", Recolor("Betsy", "Panties", "images/BetsyDoggy/Betsy_Doggy_Panties_Blue.png"),
            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #full hose/tights
            "BetsyX.Panties and BetsyX.Panties != 'swimsuit' and BetsyX.PantiesDown", Null(),
            "BetsyX.Hose == 'ripped pantyhose'", Recolor("Betsy", "Hose", "images/BetsyDoggy/Betsy_Doggy_Hose_Pantyhose_Holed.png"),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
            "BetsyX.Hose == 'pantyhose'", Recolor("Betsy", "Hose", "images/BetsyDoggy/Betsy_Doggy_Hose_Pantyhose.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Legs Layer
            "BetsyX.Legs == 'skirt' and Player.Sprite and Player.Cock == 'anal' and Speed" , Recolor("Betsy", "Legs", "images/BetsyDoggy/Betsy_Doggy_Legs_Skirt_Up.png"),   #Rogue_Doggy_Legs_Skirt_UpAnal.png",
            "BetsyX.Legs == 'skirt' and BetsyX.Upskirt", Recolor("Betsy", "Legs", "images/BetsyDoggy/Betsy_Doggy_Legs_Skirt_Up.png"),
            "BetsyX.Legs == 'skirt'", Recolor("Betsy", "Legs", "images/BetsyDoggy/Betsy_Doggy_Legs_Skirt.png"),
            "BetsyX.Legs == 'shorts'", ConditionSwitch(
                    "BetsyX.Upskirt or BetsyX.PantiesDown", Recolor("Betsy", "Legs", "images/BetsyDoggy/Betsy_Doggy_Legs_Shorts_Down.png"),
                    "BetsyX.Wet > 1", Recolor("Betsy", "Legs", "images/BetsyDoggy/Betsy_Doggy_Legs_Shorts_Wet.png"),
                    "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
                    "True", Recolor("Betsy", "Legs", "images/BetsyDoggy/Betsy_Doggy_Legs_Shorts.png"),
                    ),
            "BetsyX.Legs == 'yoga pants'", ConditionSwitch(
                    "BetsyX.Upskirt", Null(), #"images/BetsyDoggy/Betsy_Doggy_Legs_Yoga_Down.png",
                    "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
                    "BetsyX.Wet > 1", Recolor("Betsy", "Legs", "images/BetsyDoggy/Betsy_Doggy_Legs_Yoga_Wet.png"),
                    "True", Recolor("Betsy", "Legs", "images/BetsyDoggy/Betsy_Doggy_Legs_Yoga.png"),
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #Over Layer
            "BetsyX.Over == 'towel' and BetsyX.Legs == 'skirt'", Null(),
            "BetsyX.Over == 'towel' and BetsyX.Upskirt", Null(), #"images/BetsyDoggy/Betsy_Doggy_Legs_Towel_Up.png",
            "BetsyX.Over == 'towel'", Recolor("Betsy", "Over", "images/BetsyDoggy/Betsy_Doggy_Legs_Towel.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #Over Layer
            "BetsyX.Legs == 'skirt' and BetsyX.Upskirt", Null(),
            # Modification mode
            "BetsyX.Acc and 'scarf' in BetsyX.Acc", "images/BetsyDoggy/Betsy_Doggy_Scarf.png",
            # -----------------
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Pussy Piercings clothed
#            "Player.Sprite", Null(),
#            "BetsyX.PantiesDown or (not BetsyX.Panties and BetsyX.Legs != 'leather pants')", Null(), #if not panties or legs, skip this
#            "BetsyX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_RingC.png",
#            "BetsyX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_BarbellC.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Pussy Composite
            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Betsy_Pussy_Fucking3",#Speed 3
                    "Speed > 1", "Betsy_Pussy_Fucking2",#Speed 2
                    "Speed", "Betsy_Pussy_Heading",      #Speed 1
                    "True", "Betsy_Pussy_Static",              #Speed 0
                    ),
            "BetsyX.Legs and not BetsyX.Upskirt",Null(),
            "BetsyX.Panties and not BetsyX.PantiesDown", Null(),
            "'dildo pussy' in (Trigger,Trigger2,BetsyX.Offhand)", "Betsy_Pussy_Fucking2",
            "'fondle pussy' in (Trigger,Trigger2,BetsyX.Offhand)", "Betsy_Pussy_Fingering",
            "Trigger == 'insert pussy'", "Betsy_Pussy_Fingering",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Anus Composite
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Betsy_Anal_Fucking2", #Speed 3
                    "Speed > 1", "Betsy_Anal_Fucking",  #Speed 2
                    "Speed", "Betsy_Anal_Heading",      #Speed 1
                    "True", "Betsy_Anal",               #Speed 0
                    ),
            "BetsyX.Legs and not BetsyX.Upskirt",Null(),
            "BetsyX.Panties and not BetsyX.PantiesDown", Null(),
            "'insert ass' in (Trigger,Trigger2,BetsyX.Offhand)", "Betsy_Anal_Fingering",
            "'dildo anal' in (Trigger,Trigger2,BetsyX.Offhand)", "Betsy_Anal_Fucking",
            "BetsyX.Plug", "images/PlugIn.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk back Layer
            "'back' in BetsyX.Spunk and Player.Male", "images/BetsyDoggy/Betsy_Doggy_Spunk_Ass.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy'", "Rogue_Doggy_Lick_Pussy",
            "Trigger == 'lick ass'", "Rogue_Doggy_Lick_Ass",
            "True", Null()
            ),
#        (0,0), ConditionSwitch(
#            #Hotdogging underlayer
#            "not Player.Sprite or Player.Cock != 'out'", Null(),
#            "BetsyX.Over == 'towel'", Null(),
#            "(BetsyX.Legs == 'skirt' or BetsyX.Legs == 'other skirt') and BetsyX.Upskirt", "images/BetsyDoggy/Betsy_Doggy_Hotdog_Upskirt.png",
#            "True", "images/BetsyDoggy/Betsy_Doggy_HotdogBack.png",
#            ),
        (0,0), ConditionSwitch(
            #Hotdogging Cock w/ alpha
            "not Player.Sprite or Player.Cock != 'out'", Null(),
            "(BetsyX.Legs == 'skirt' or BetsyX.Legs == 'other skirt') and BetsyX.Upskirt and Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "(BetsyX.Legs == 'skirt' or BetsyX.Legs == 'other skirt') and BetsyX.Upskirt", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            "True", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            ),
#        (0,0), ConditionSwitch(
#            #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
        )
# End Ass / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Betsy_Doggy_Feet:         #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
    contains:
            AlphaMask("Betsy_Doggy_Shins", "images/BetsyDoggy/Betsy_Doggy_Feet_Mask2.png")

image Betsy_Doggy_Shins:             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
    #Betsy's footjob shins
#    contains:
#        "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Feet.png"
    contains:
            #hose legs
        ConditionSwitch(
            "BetsyX.Hose == 'garterbelt'", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Feet.png",
            "BetsyX.Hose == 'ripped pantyhose'", Recolor("Betsy", "Hose", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Feet_Hose_Holed.png"),
            "BetsyX.Hose == 'socks'", Recolor("Betsy", "Hose", "images/BetsyDoggy/Betsy_Doggy_Feet_Socks.png"),
            "BetsyX.Hose", Recolor("Betsy", "Hose", "images/BetsyDoggy/Betsy_Doggy_Feet_Hose.png"),
            "True", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Feet.png",
            )
    contains:
        #boots
        ConditionSwitch(
            "BetsyX.Legs == 'yoga pants'", Recolor("Betsy", "Legs", "images/BetsyDoggy/Betsy_Doggy_Feet_Yoga.png"),
            "True", Null(),
            )
    contains:
        #spunk
        ConditionSwitch(
            "'feet' in BetsyX.Spunk and Player.Male", "images/BetsyDoggy/Betsy_Doggy_Spunk_Feet.png",
            "True", Null(),
            )
#    pos (0,0)

image Betsy_Doggy_Shins0:
        #static animation
        "Betsy_Doggy_Shins"
        offset (0, 0) #(0,150) top


image Betsy_Doggy_GropeBreast:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        xzoom -.55
        yzoom .55
        offset (140,340)#(270,410)
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
        block:
            ease 1 rotate 10#60
            ease 1 rotate 0#90
            repeat

image Betsy_Gape_Anal:
        #animation for her asshole growing and shrinking a bit when over 2 Looseness
        contains:
            subpixel True
            "images/JubesDoggy/Jubes_Doggy_Anal_GapeBase.png"
            anchor (0.52,0.69)
            offset (218,513)#(218,513)
            zoom .35 # loose
            block:
                ease 3 zoom .20 #in
                ease 3.2 zoom .30 #out
                repeat
        contains:
            subpixel True
            "images/JubesDoggy/Jubes_Doggy_Anal_GapeHole.png"
            anchor (0.52,0.69)
            offset (218,513)#(218,513)
            zoom .35 # loose
            block:
                ease 3 zoom .15 #in
                ease 3.2 zoom .30 #out
                repeat

#Hotdogging animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Zero_Betsy_Hotdog_Static:
    # The unmoving version of the hotdog cock
    # called in Doggy Ass LC
    contains:
        "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Betsy_Hotdog_Moving:
    # The moving version of the hotdog cock
    # called in Doggy Ass LC
    contains:
        "Zero_Doggy_Up"
        pos (175, 370)
        block:
            ease 1 ypos 330
            ease 1 ypos 420
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


image Betsy_Pussy_Mask:
    #AlphaMask used to prevent the cock from moving past the pussy
    #Called in "Betsy_Pussy_Moving"
    contains:
        #Base
        "images/RogueDoggy/Rogue_Doggy_SexMask.png"
        anchor (0.52,0.69)
        pos (219,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat

image Betsy_Pussy_Mask_Static:
    #AlphaMask used to prevent the cock from moving past the pussy in static pose
    #Called in "Betsy_Pussy_Moving"
    contains:
        #Base
        "images/RogueDoggy/Rogue_Doggy_SexMask.png"
        anchor (0.52,0.69)
        pos (219,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat

image Betsy_Pussy_Mask_Finger:
    #AlphaMask used to prevent the cock from moving past the pussy
    #Called in "Betsy_Pussy_Moving"
    contains:
        #Base
        "images/RogueDoggy/Rogue_Doggy_SexMask.png"
        anchor (0.52,0.69)
        pos (219,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat

image Betsy_Pussy_Mask_Fucking:
    #AlphaMask used to prevent the cock from moving past the pussy
    #Called in "Betsy_Pussy_Moving"
    contains:
        #Base
        "images/RogueDoggy/Rogue_Doggy_SexMask.png"
        anchor (0.52,0.69)
        pos (221,518)
        xzoom 1
#        block:
#            ease 1 xzoom 1
#            pause 1
#            ease 3 xzoom .6
#            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Pussy fucking animations


image Betsy_Pussy_Static:
    #Full Animation for speed 0
    subpixel True
    contains:
        #moving hole
        "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat
    contains:
        #pubes
        ConditionSwitch(
            "BetsyX.Pubes", Recolor("Betsy", "Pubes", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Pubes_Open.png"),
            "True", Null(),
            )
        subpixel True
        transform_anchor True
        anchor (0.515,0.69)#(0.52,0.69)
        pos (217,518) #(219,518)
        xzoom 1.1
        block:
            ease .9 xzoom 1.2 #1
            pause 1.6
            ease 2.5 xzoom 1.1#.9
            repeat
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "BetsyX.Pierce == 'ring'", "images/LauraDoggy/Laura_Doggy_Pierce_Ring.png",
            "BetsyX.Pierce == 'barbell'", "images/LauraDoggy/Laura_Doggy_Pierce_Barbell.png",
            "True", Null(),
            )
        offset (1,5)#(-3,8)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in BetsyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.52,0.69)
        pos (218,516) #(221,516)
        xzoom .9
        block:
            ease 1 xzoom 1.1
            pause 1
            ease 3 xzoom .9
            repeat

    contains:
        #Cock
        AlphaMask("Zero_Betsy_Doggy_Static", "Betsy_Pussy_Mask_Static")

#    contains:
#        # expanding pussy flap
#        AlphaMask("Betsy_PussyHole_Static", "Betsy_Pussy_Hole_Mask_Static")

image Betsy_Pussy_Hole_Mask_Static:
    # This is the alpha used for the little flap in the heading animation "Betsy_Pussy_Moving"
    contains:
        #Base
        AlphaMask("images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat

#image Betsy_PussyHole_Static:
#    #This is the image impacted by the mask for the pussy flap in "Betsy_Pussy_Moving"
#    contains:
#        #Mask
#        "images/BetsyDoggy/Betsy_Doggy_Pussy_FHeading.png"
#        anchor (0.52,0.69)
#        pos (217,515)
#        zoom 1
#        alpha .9
#        block:
#            ease 1 ypos 512
#            pause 1
#            ease 3 ypos 515
#            repeat


image Zero_Betsy_Doggy_Static:
    # Sex Speed 0 motions
    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (169,545)
        block:
            ease 1 ypos 540 #in stroke
            pause 1
            ease 3 ypos 545 #out stroke
            repeat

image Betsy_Pussy_Heading:
    #Full Animation for speed 1
    subpixel True
    contains:
        #moving hole
        "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.51,0.69)#(0.52,0.69)
#        anchor (0.52,0.69)
        pos (215,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat
    contains:
        #pubes
        ConditionSwitch(
            "BetsyX.Pubes", Recolor("Betsy", "Pubes", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Pubes_Fucking.png"),
            "True", Null(),
            )
        subpixel True
        anchor (0.51,0.69)
        pos (215,518) #(213,518)
        xzoom .75
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .77
            repeat
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "BetsyX.Pierce == 'ring'", "images/LauraDoggy/Laura_Doggy_Pierce_Ring.png",
            "BetsyX.Pierce == 'barbell'", "images/LauraDoggy/Laura_Doggy_Pierce_Barbell.png",
            "True", Null(),
            )
        offset (1,5)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in BetsyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.52,0.75) #(0.52,0.69)
        pos (215,560) #(221,518)
        xzoom .6
        block:
            ease .9 xzoom 1
            pause 1.6
            ease 2.5 xzoom .6
            repeat
    contains:
        #Cock
        AlphaMask("Zero_Betsy_Doggy_Heading", "Betsy_Pussy_Mask")

#    contains:
#        # expanding pussy flap
#        AlphaMask("Betsy_Pussy_Heading_Flap", "Betsy_Pussy_Hole_Mask")
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in BetsyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.515,0.75)#(0.52,0.69)
        pos (215,560) #(221,518)
        xzoom .8
        yzoom .6
        parallel:
            ease .9 xzoom 1
            pause 1.6
            ease 2.5 xzoom .7#.6
            repeat
        parallel:
            ease .9 yzoom 1
            pause 1.6
            ease 2.5 yzoom .5#.4
            repeat


image Betsy_Pussy_Hole_Mask:
    # This is the alpha used for the little flap in the heading animation "Betsy_Pussy_Heading"
    contains:
        #Base
        AlphaMask("images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat

#image Betsy_Pussy_Heading_Flap:
#    #This is the image impacted by the mask for the pussy flap in "Betsy_Pussy_Heading"
#    contains:
#        #Mask
#        "images/BetsyDoggy/Betsy_Doggy_Pussy_FHeading.png"
#        anchor (0.52,0.69)
#        pos (217,515)
#        zoom 1
#        alpha .9
#        block:
#            ease 1 ypos 505
#            pause 1
#            ease 3 ypos 515
#            repeat

image Betsy_Pussy_Fingering:
    #Full Animation for speed 1
    subpixel True
    contains:
        #moving hole
        "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (219,518)
        xzoom .6
        block:
            ease 1 xzoom .9#1
            pause 1
            ease 3 xzoom .6
            repeat
    contains:
        #pubes
        ConditionSwitch(
            "BetsyX.Pubes", Recolor("Betsy", "Pubes", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Pubes_Open.png"),
            "True", Null(),
            )
        subpixel True
        anchor (0.51,0.69)
        pos (215,518) #(213,518)
        xzoom .75
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .77
            repeat
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "BetsyX.Pierce == 'ring'", "images/LauraDoggy/Laura_Doggy_Pierce_Ring.png",
            "BetsyX.Pierce == 'barbell'", "images/LauraDoggy/Laura_Doggy_Pierce_Barbell.png",
            "True", Null(),
            )
        offset (1,5)

    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in BetsyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.52,0.69)
        pos (215,516)
        xzoom .9
        block:
            ease 1 xzoom 1.1
            pause 1
            ease 3 xzoom .9
            repeat
    contains:
        #Cock
        AlphaMask("Zero_Betsy_Pussy_Finger", "Betsy_Pussy_Mask_Finger")
#    contains:
#        # expanding pussy flap
#        AlphaMask("Betsy_Pussy_Heading_Flap", "Betsy_Pussy_Hole_Mask")

    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in BetsyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.515,0.75)#(0.52,0.69)
        pos (215,560) #(221,518)
        xzoom .8
        yzoom .6
        parallel:
            ease .9 xzoom 1
            pause 1.6
            ease 2.5 xzoom .7#.6
            repeat
        parallel:
            ease .9 yzoom 1
            pause 1.6
            ease 2.5 yzoom .5#.4
            repeat


image Zero_Betsy_Doggy_Heading:
    # Sex Speed 1 motions
    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (173,545)
        block:
            ease 1 xpos 170 ypos 500 #in stroke
            pause 1
            ease 3 xpos 173 ypos 545 #out stroke
            repeat

image Zero_Betsy_Pussy_Finger:
    # Sex Speed 1 motions
    contains:
        subpixel True
        "images/UI_Fingering.png"
        pos (173,545)
        alpha 0.8
        block:
            ease 1 xpos 170 ypos 500 #in stroke
            pause 1
            ease 3 xpos 173 ypos 545 #out stroke
            repeat

# > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

image Betsy_Pussy_Fucking2:
    #Full Animation for speed 2
    contains:
        #Base
        "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Pussy_FHole.png"
        offset (2,0)
    contains:
        #pubes
        ConditionSwitch(
            "BetsyX.Pubes", Recolor("Betsy", "Pubes", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Pubes_Fucking.png"),
            "True", Null(),
            )
        offset (2,0)
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "BetsyX.Pierce == 'ring'", "images/LauraDoggy/Laura_Doggy_Pierce_Ring.png",
            "BetsyX.Pierce == 'barbell'", "images/LauraDoggy/Laura_Doggy_Pierce_Barbell.png",
            "True", Null(),
            )
        offset (1,5)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in BetsyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            "'dildo pussy' in (Trigger,Trigger2,BetsyX.Offhand)", AlphaMask("Doggy_Fucking_Dildo", "Betsy_Pussy_Mask_Fucking"),
            "True",AlphaMask("Zero_Betsy_Doggy_Fucking2", "Betsy_Pussy_Mask_Fucking"),
            ),
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in BetsyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )


image Zero_Betsy_Doggy_Fucking2:
    # Sex Speed 2 motions
    contains:
        "Zero_Doggy_Insert"
        pos (171,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat


image Betsy_Pussy_Fucking3:
    #Full Animation for speed 3
    contains:
        #Base
        "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Pussy_FHole.png"
        offset (2,0)
    contains:
        #pubes
        ConditionSwitch(
            "BetsyX.Pubes", Recolor("Betsy", "Pubes", "images/BetsyDoggy/[BetsyX.skin_image.skin_path]Betsy_Doggy_Pubes_Fucking.png"),
            "True", Null(),
            )
        offset (2,0)
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "BetsyX.Pierce == 'ring'", "images/LauraDoggy/Laura_Doggy_Pierce_Ring.png",
            "BetsyX.Pierce == 'barbell'", "images/LauraDoggy/Laura_Doggy_Pierce_Barbell.png",
            "True", Null(),
            )
        offset (1,5)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in BetsyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Betsy_Doggy_Fucking3", "Betsy_Pussy_Mask_Fucking")
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in BetsyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )


image Zero_Betsy_Doggy_Fucking3:
    # Sex Speed 3 motions
    contains:
        "Zero_Doggy_Insert"
        pos (171,500)
        block:
            ease .2 ypos 440
            pause .1
            ease .6 ypos 500
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

image Betsy_Anal:
    #Anal static Loose
    contains:
        #Base
        "images/BetsyDoggy/Betsy_Doggy_Asshole_Loose.png"
        anchor (0.50,0.69)
        pos (208,510)
        zoom 1.25
    contains:
        #Cock
        "Zero_Doggy_Insert"
        pos (172,500)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Betsy_Anal_Fingering:
    #Animation for speed 1
    contains:
        #Hole
        "images/GwenDoggy/Gwen_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .6
        block:
            ease .5 zoom .75#1
            pause .5
            ease 1.5 zoom .6
            repeat
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in BetsyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
        anchor (0.52,0.71) #(0.52,0.69)
        pos (218,530)#(218,518)
        zoom .5
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .5
            repeat
    contains:
        #Cock with mask
        AlphaMask("Zero_Betsy_Doggy_Anal_Finger", "Betsy_Doggy_Anal_Fingering_Mask")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in BetsyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )
        anchor (0.52,0.71) #(0.52,0.69)
        pos (218,530)#(218,518)
        zoom .7
        block:
            ease .5 zoom .8
            pause .5
            ease 1.5 zoom .7 #.5
            repeat

image Zero_Betsy_Doggy_Anal_Finger:
        #the cock anal heading animation
    contains:
        "images/UI_Fingering.png"
        pos (172,480)#500
        alpha 0.8
        block:
            ease .5 ypos 460#450
            pause .25
            ease 1.75 ypos 480#500
            repeat
image Betsy_Doggy_Anal_Fingering_Mask:
    #the masking animation for the anal heading
    contains:
        "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"
#        yoffset 10
        anchor (0.52,0.69)
        pos (218,518)
        zoom .6
        block:
            ease .5 zoom .75
            pause .5
            ease 1.5 zoom .6
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Betsy_Anal_Heading:
    #Animation for speed 1
    contains:
        #Hole
        "images/GwenDoggy/Gwen_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .5
            repeat
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in BetsyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
        anchor (0.52,0.71) #(0.52,0.69)
        pos (218,530)#(218,518)
        zoom .5
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .5
            repeat
    contains:
        #Cock with mask
        AlphaMask("Zero_Betsy_Doggy_Anal_Heading", "Betsy_Doggy_Anal_Heading_Mask")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in BetsyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )
        anchor (0.52,0.71) #(0.52,0.69)
        pos (218,530)#(218,518)
        zoom .6
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .6 #.5
            repeat

image Zero_Betsy_Doggy_Anal_Heading:
        #the cock anal heading animation
    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500#505
            repeat

image Zero_Betsy_Doggy_Anal_HeadingJunk:
    #this is a mask to correct an annoying glitch in the core mask
    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease .5 ypos 550
            pause .25
            ease 1.75 ypos 600#505
            repeat

image Betsy_Doggy_Anal_Heading_Mask:
    #the masking animation for the anal heading
    contains:
        "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"
        anchor (0.52,0.69)
        pos (218,534)
        block:
            ease .5 ypos 518
            pause .25
            ease 1.75 ypos 534#518
            repeat

image Betsy_Doggy_Anal_Head_Top:
#animation for anal fucking top half
    contains:
        subpixel True
        "Betsy_Doggy_Body"
        ypos 0
        block:
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat

image Betsy_Doggy_Anal_Head_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Betsy_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -10
            easeout .1 ypos -7
            easein .9 ypos 0
            pause .9
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Betsy_Doggy_Anal1:
    #Animation for speed 2 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat

image Betsy_Anal_Fucking:
    #Animation for speed 2 Ass
    contains:
        #Hole
        "images/GwenDoggy/Gwen_Doggy_Anal_FullHole.png"
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in BetsyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            #full hose/tights
            "'dildo anal' in (Trigger,Trigger2,BetsyX.Offhand)", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", AlphaMask("Zero_Betsy_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            )
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in BetsyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )


image Betsy_Doggy_Fuck_Top:
    #animation for anal fucking top half
    contains:
        subpixel True
        "Betsy_Doggy_Body"
        ypos 15#28
        pause .4
        block:
            ease .2 ypos 5#10
            pause .3
            ease 2 ypos 15#28
            repeat

image Betsy_Doggy_Fuck_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Betsy_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15#-25
            ease .1 ypos -5#-15
            pause .2
            ease 1.6 ypos 0
            repeat


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Betsy_Doggy_Anal2:
    #Animation for speed 3 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat

image Betsy_Anal_Fucking2:
    #Animation for speed 3 Ass
    contains:
        #Hole
        "images/GwenDoggy/Gwen_Doggy_Anal_FullHole.png"
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in BetsyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Betsy_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in BetsyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )

image Betsy_Doggy_Fuck2_Top:
    #animation for anal fucking2 top half
    contains:
        subpixel True
        "Betsy_Doggy_Body"
        ypos 20
        block:
            pause .15
            ease .1 ypos 0
            pause .1
            easein .5 ypos 20
            pause .05
            repeat

image Betsy_Doggy_Fuck2_Ass:
    #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Betsy_Doggy_Ass"
        ypos 5
        block:
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .4 ypos 5
            pause .05
            repeat


# Footjob animations > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

image Betsy_Doggy_Feet0:
    #static animation
    contains:
        "Betsy_Doggy_Shins"
        pos (0, 0) #(0,0) top
        block:
            subpixel True
            pause .5
            ease 2 ypos 20
            pause .5
            ease 2 ypos 0
            repeat
    contains:
        ConditionSwitch(
                "Player.Sprite", "Zero_Doggy_Up",
                "True", Null(),
                )
        zoom 1.2
        pos (160,480)  #(145,480)
    contains:
        "Betsy_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            subpixel True
            pause .5
            ease 2 ypos 20
            pause .5
            ease 2 ypos 0
            repeat

image Betsy_Doggy_Foot0_Top:
    #animation for footjob top half
    contains:
        subpixel True
        "Betsy_Doggy_Body"
        ypos 10#28
        #pause .4
        block:
            pause .5
            ease 2 ypos 14
            pause .5
            ease 2 ypos 10
            repeat

image Betsy_Doggy_Foot0_Ass:
    #animation for footjob ass half
    contains:
        subpixel True
        "Betsy_Doggy_Ass"
        ypos 0
        block:     #total 3
            pause .1 #.5
            ease 2 ypos 10
            pause .5
            ease 2.4 ypos 0
            repeat


image Betsy_Doggy_Feet1:
    #slow animation
    contains:
        "Betsy_Doggy_Shins"
        pos (0, 0) #(0,0) top
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat
    contains:
        "Zero_Doggy_Up"
        zoom 1.2
        pos (160,480)
        block:
            pause .4
            ease 1.7 ypos 500
            ease .9 ypos 480
            repeat
    contains:
        "Betsy_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat

image Betsy_Doggy_Foot1_Top:
    #animation for footjob top half
    contains:
        subpixel True
        "Betsy_Doggy_Body"
        ypos 30#28
        block:
            pause .3
            ease 1.7 ypos 80
            ease 1 ypos 30
            repeat

image Betsy_Doggy_Foot1_Ass:
    #animation for footjob ass half
    contains:
        subpixel True
        "Betsy_Doggy_Ass"
        ypos 0
        block: #total 3
            pause .3
            ease 2 ypos 80
            ease .7 ypos 0
            repeat


image Betsy_Doggy_Feet2:
    #fast animation
    contains:
        "Betsy_Doggy_Shins"
        pos (0, 0) #(0,0) top
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat
    contains:
        "Zero_Doggy_Up"
        zoom 1.2
        pos (160,480)
        block:
            pause .07
            ease .6 ypos 500
            ease .28 ypos 480
            repeat
    contains:
        "Betsy_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat

image Betsy_Doggy_Foot2_Top:
    #animation for footjob top half
    contains:
        subpixel True
        "Betsy_Doggy_Body"
        ypos 70#28
        block:
            pause .05
            ease .6 ypos 90#90#110
            ease .3 ypos 70#70
            repeat

image Betsy_Doggy_Foot2_Ass:
    #animation for footjob ass half
    contains:
        subpixel True
        "Betsy_Doggy_Ass"
        ypos 70
        block: #total .95
            pause .15#.05
            ease .6 ypos 90#110
            ease .2 ypos 70
            repeat

# Footjob animations end > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Doggy Launch/Reset
label Betsy_Doggy_Launch(Line = Trigger):
#    #temporary, remove / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
#    return
#    #temporary, remove / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

    if renpy.showing("Betsy_Doggy_Animation"):
        return
    $ Speed = 0
    call Girl_Hide(BetsyX,1) #call Rogue_Hide(1)
    show Betsy_Doggy_Animation at SpriteLoc(StageCenter+48) zorder 150
    with dissolve
    return

#    if not renpy.showing("Betsy_Doggy_Animation"):
#        $ Speed = 0
#        call Betsy_Hide(1)
#    if Trigger == "lick pussy" or Trigger == "lick ass":
#            show Betsy_Doggy_Animation at SpriteLoc(StageCenter+48) zorder 150:
#                ypos -500
#                zoom 2
#    else:
#            show Betsy_Doggy_Animation at SpriteLoc(StageCenter+48) zorder 150:
#                ypos 50
#                zoom 1
    return

label Betsy_Doggy_Reset:
    if not renpy.showing("Betsy_Doggy_Animation"):
        return
#    $ Trigger = 0               #fix, not sure this is a good idea
    $ BetsyX.ArmPose = 2
    $ BetsyX.SpriteVer = 0
    hide Betsy_Doggy_Animation
    call Girl_Hide(BetsyX)
    show Betsy_Sprite at SpriteLoc(BetsyX.SpriteLoc) zorder BetsyX.Layer:
            alpha 1 zoom 1 offset (0,0) anchor (0.6, 0.0)
    with dissolve
    $ Speed = 0
    return

# End Betsy Doggy Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



## Start Betsy Sex Pose Content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Betsy Sex Pose core / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_SexSprite:
    LiveComposite(
        (1120,840),

#        (0,0), ConditionSwitch(
#                #Shows different upper body motion depending on events
#                "True", "Betsy_Sex_Speed2",
#                ),
        (0,0), ConditionSwitch(
                #Shows different motion depending on events
#                "not Player.Sprite", "Betsy_Sex_Body_Static",
                "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Betsy_Sex_Fucking_Speed3",
                        "Speed >= 2", "Betsy_Sex_Fucking_Speed2",
                        "Speed", "Betsy_Sex_Fucking_Speed1",
                        "True", "Betsy_Sex_Fucking_Speed0",
                        ),
                "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Betsy_Sex_Anal_Speed3",
                        "Speed >= 2", "Betsy_Sex_Anal_Speed2",
                        "Speed", "Betsy_Sex_Anal_Speed1",
                        "True", "Betsy_Sex_Anal_Speed0",
                        ),
                "Player.Sprite and Player.Cock == 'out' and Speed >= 2","Betsy_Sex_Hotdog_Speed2",
                "Player.Sprite and Player.Cock == 'out' and Speed >= 1","Betsy_Sex_Hotdog_Speed1",
                "Player.Cock == 'foot'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 2", "Betsy_Sex_FJ_Speed2",
                        "Speed", "Betsy_Sex_FJ_Speed1",
                        "True", "Betsy_Sex_FJ_Speed0",
                        ),
#                "Player.Cock == 'out' and Speed >= 2","Betsy_Hotdog_Body_Anim2",
                "True", "Betsy_Sex_Static",
                ),
        )
    align (0.6,0.0)
    pos (650,303)#(650,393)
    zoom 0.85#0.7

# End Betsy Sex Pose core / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Betsy Sex Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Betsy_Sex_Body:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Betsy_SexSprite
        (1120,840),
        (217,-165), "Betsy_HairBack_Sex", #(175,-165)
#        (0,0), ConditionSwitch(
#            #shirt under layer
#            "BetsyX.Over == 'red shirt' and BetsyX.Uptop", "images/BetsySex/Betsy_Sex_Over_Red_Back.png",
#            "BetsyX.Over == 'black shirt' and BetsyX.Uptop", "images/BetsySex/Betsy_Sex_Over_Black_Back.png",
#            "True", Null(),
#            ),
        (0,0), "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Neck.png",
#        (0,0), "images/BetsySex/Betsy_Sex_Headref.png",

        (175,-165), "Betsy_Head_Sex",  #(50,-325)
        (0,0), "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Body.png",

        (0,0), ConditionSwitch(
            #rear sleeve
            "BetsyX.Over == 'pink top'", Recolor("Betsy", "Over", "images/BetsySex/Betsy_Sex_Over_Pink_Back.png"),
            "BetsyX.Over == 'jacket'", Recolor("Betsy", "Over", "images/BetsySex/Betsy_Sex_Over_Jacket_Back.png"),
            # Modification mode
            "BetsyX.Arms == 'cammy gloves'", "images/BetsySex/modification/Betsy_Sex_Glove_Cammy_Back.png",
            # ----------------
            "BetsyX.Arms", "images/BetsySex/Betsy_Sex_Glove_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #bra layer
            "not BetsyX.Chest", Null(),
            "BetsyX.Uptop", ConditionSwitch(
                    #if top's up
                    "BetsyX.Chest == 'swimsuit' or BetsyX.Panties == 'swimsuit'", Recolor("Betsy", "Chest", "images/BetsySex/Betsy_Sex_Chest_Bikini_Up.png"),
                    "BetsyX.Chest == 'sports bra'", Recolor("Betsy", "Chest", "images/BetsySex/Betsy_Sex_Chest_Sports_Up.png"),
                    "BetsyX.Chest == 'bra'", Recolor("Betsy", "Chest", "images/BetsySex/Betsy_Sex_Chest_Bra_Up.png"),
                    "BetsyX.Chest == 'lace bra'", Recolor("Betsy", "Chest", "images/BetsySex/Betsy_Sex_Chest_Lace_Up.png"),
                    # Modification mode
                    "BetsyX.Chest == 'cammy leotard' or BetsyX.Panties == 'cammy leotard'", "images/BetsySex/modification/Betsy_Sex_Chest_Cammy_Up.png",
                    # ----------------
                    "True", Null(),
                    ),
            #if the top's down. . .
            "BetsyX.Chest == 'swimsuit' or BetsyX.Panties == 'swimsuit'", Recolor("Betsy", "Chest", "images/BetsySex/Betsy_Sex_Chest_Bikini.png"),
            "BetsyX.Chest == 'sports bra'", Recolor("Betsy", "Chest", "images/BetsySex/Betsy_Sex_Chest_Sports.png"),
            "BetsyX.Chest == 'bra'", Recolor("Betsy", "Chest", "images/BetsySex/Betsy_Sex_Chest_Bra.png"),
            "BetsyX.Chest == 'lace bra'", Recolor("Betsy", "Chest", "images/BetsySex/Betsy_Sex_Chest_Lace.png"),
            # Modification mode
            "BetsyX.Chest == 'cammy leotard' or BetsyX.Panties == 'cammy leotard'", "images/BetsySex/modification/Betsy_Sex_Chest_Cammy.png",
            # -----------------
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "BetsyX.Water", "images/BetsySex/Betsy_Sex_Water_Body.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #shorts X layer
            "BetsyX.Legs == 'shorts' and not BetsyX.Upskirt", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_Sex_Over_Shorts.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #shirt layer
            "BetsyX.Over == 'jacket'", Recolor("Betsy", "Over", "images/BetsySex/Betsy_Sex_Over_Jacket.png"),
            "BetsyX.Over == 'pink top' and BetsyX.Uptop", Recolor("Betsy", "Over", "images/BetsySex/Betsy_Sex_Over_Pink_Up.png"),
            "BetsyX.Over == 'tank' and BetsyX.Uptop", Recolor("Betsy", "Over", "images/BetsySex/Betsy_Sex_Over_Tank_Up.png"),
            "BetsyX.Uptop", Null(),
            "BetsyX.Over == 'towel'", Recolor("Betsy", "Over", "images/BetsySex/Betsy_Sex_Over_Towel.png"),
            "BetsyX.Over == 'pink top'", Recolor("Betsy", "Over", "images/BetsySex/Betsy_Sex_Over_Pink.png"),
            "BetsyX.Over == 'tank'", Recolor("Betsy", "Over", "images/BetsySex/Betsy_Sex_Over_Tank.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #piercings
            "not BetsyX.Pierce", Null(),
            "BetsyX.Pierce == 'ring'", ConditionSwitch(
                    # ring pierce
                    "BetsyX.Uptop", "images/BetsySex/Betsy_Sex_Pierce_Tits_R.png",

                    "BetsyX.Over == 'tank'", "images/BetsySex/Betsy_Sex_Pierce_Tits_R_Blue.png",
                    "BetsyX.Over == 'pink top' or BetsyX.Over == 'towel'", "images/BetsySex/Betsy_Sex_Pierce_Tits_R_Pink.png",                  #pink top or towel

                    "BetsyX.Panties == 'swimsuit'", "images/BetsySex/Betsy_Sex_Pierce_Tits_R_Blue.png",
                    "BetsyX.Chest == 'lace bra'", "images/BetsySex/Betsy_Sex_Pierce_Tits_R_Lace.png",
                    "BetsyX.Chest", "images/BetsySex/Betsy_Sex_Pierce_Tits_R_Blue.png",

                    "True", "images/BetsySex/Betsy_Sex_Pierce_Tits_R.png",
                    ),
            "BetsyX.Uptop", "images/BetsySex/Betsy_Sex_Pierce_Tits_B.png",

            "BetsyX.Over == 'tank'", "images/BetsySex/Betsy_Sex_Pierce_Tits_B_Blue.png",
            "BetsyX.Over == 'pink top' or BetsyX.Over == 'towel'", "images/BetsySex/Betsy_Sex_Pierce_Tits_B_Pink.png",                  #pink top or towel

            "BetsyX.Panties == 'swimsuit'", "images/BetsySex/Betsy_Sex_Pierce_Tits_B_Blue.png",
            "BetsyX.Chest == 'lace bra'", "images/BetsySex/Betsy_Sex_Pierce_Tits_B_Lace.png",
            "BetsyX.Chest", "images/BetsySex/Betsy_Sex_Pierce_Tits_B_Blue.png",

            "True", "images/BetsySex/Betsy_Sex_Pierce_Tits_B.png",
            ),

        (0,0),ConditionSwitch(
            #Outside Spunk
            "'belly' in BetsyX.Spunk and Player.Male", "images/BetsySex/Betsy_Sex_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'tits' in BetsyX.Spunk and Player.Male", "images/BetsySex/Betsy_Sex_Spunk_Tits.png",
            "True", Null(),
            ),
#        (0,0), "images/BetsySex/Betsy_Sex_HeadRef.png",
        )
#    yoffset -163
# End Betsy Sex Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Betsy_Sex_Hand:
    LiveComposite(
        #the lower legs used in the sex pose, referenced by Betsy_Sex_Legs
        (1120,840),
        (0,0), ConditionSwitch(
            #base arms
            "BetsyX.Arms", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Hand_Glove.png",
            "True", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Hand.png",
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "BetsyX.Water", "images/BetsySex/Betsy_Sex_Water_Hand.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #shirt layer
            "BetsyX.Over == 'jacket'", Recolor("Betsy", "Over", "images/BetsySex/Betsy_Sex_Over_Jacket_Up.png"),
            "BetsyX.Over == 'pink top'", Recolor("Betsy", "Over", "images/BetsySex/Betsy_Sex_Over_Pink_Arm.png"),
            "True", Null(),
            ),
        )

image Betsy_Head_Sex:
    # The head used for the sex pose, referenced by Betsy_Sex_Body
    "Betsy_Sprite_Head"
    zoom 1.15#1.24
    anchor (0.5,0.5)
    rotate 28#17
#    alpha 0.5

image Betsy_HairBack_Sex:
    # The hair behind the head for the sex pose, referenced by Betsy_Sex_Body
    "Betsy_Sprite_HairBack"
    zoom 1.15#1.36
    anchor (0.5,0.5)
    rotate 10#28


image Betsy_Sex_Lick_Breasts:
        "Lick_Anim"
        zoom 0.7
        offset (400,350)#(390,620)

image Betsy_Sex_Fondle_Breasts:
        "GropeLeftBreast"
        zoom 1.5
        offset (190,-200)#(160,-40)

# Start Betsy Sex Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Betsy_Sex_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Betsy_SexSprite
        (1120,880),
        (0,0), ConditionSwitch(
            #back of skirt Layer
            "BetsyX.Legs == 'skirt'", "images/BetsySex/Betsy_Sex_Legs_Skirt_Back.png",
            "True", Null(),
            ),
        (545,540), ConditionSwitch(    #165,560
            #Personal Wetness
            "not BetsyX.Wet", Null(),
            "(BetsyX.Legs == 'pants' or BetsyX.Legs == 'shorts') and not BetsyX.Upskirt", Null(),
            "BetsyX.Panties and not BetsyX.PantiesDown", Null(),
            "BetsyX.Wet == 1", "Wet_Drip",
            "True", "Wet_Drip2",
            ),

        (545,540), ConditionSwitch(    #205,530
            #Spunk
            "'anal' not in BetsyX.Spunk or not Player.Male", Null(),
            "(BetsyX.Legs == 'pants' or BetsyX.Legs == 'shorts') and not BetsyX.Upskirt", Null(),
            "BetsyX.Wet == 1", "Spunk_Drip",
            "True", "Spunk_Drip2",
            ),

        (0,0), ConditionSwitch(
            #Legs
#            "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_FBase.png",
            "Player.Sprite and Player.Cock == 'in' and Speed", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_FBase.png",
#            "Player.Sprite and Player.Cock == 'in' and Speed", "Betsy_Sex_Heading_Pussy",
#            "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Ass.png",
#            "Trigger == 'lick pussy'", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Ass.png",
            "True", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Ass.png",
            ),

#        (0,0), ConditionSwitch(
#            "Player.Sprite and Player.Cock == 'anal'", "images/BetsySex/Betsy_Sex_Anus_Cover.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #Wet look
            "not BetsyX.Water", Null(),
            "True", "images/BetsySex/Betsy_Sex_Water_Legs.png",
            ),

        (0,0), "Betsy_Sex_Anus",
            #Anus Composite  (0,-10)

        (0,0), "Betsy_Sex_Pussy",
            #Pussy Composite


        (0,0), ConditionSwitch(
            #hose layer
            "BetsyX.Hose == 'socks'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_Sex_Hose_Socks.png"),
            "BetsyX.Hose == 'stockings and garterbelt'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_Sex_Hose_StockingsGarter.png"),
            "BetsyX.Hose == 'garterbelt'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_Sex_Hose_Garter.png"),
            "BetsyX.Hose == 'stockings'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_Sex_Hose_Stockings.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Panties if up
            "(BetsyX.Panties == 'swimsuit' or BetsyX.Chest == 'swimsuit') and BetsyX.PantiesDown", Recolor("Betsy", "Panties", "images/BetsySex/Betsy_Sex_Panties_Bikini_Down.png"),
            # Modification mode
            "(BetsyX.Panties == 'cammy leotard' or BetsyX.Chest == 'cammy leotard') and BetsyX.PantiesDown", "images/BetsySex/modification/Betsy_Sex_Panties_Cammy_Down.png",
            # -----------------
            "BetsyX.PantiesDown", Null(),
            "BetsyX.Panties == 'lace panties'", Recolor("Betsy", "Panties", "images/BetsySex/Betsy_Sex_Panties_Lace.png"),
            "BetsyX.Panties == 'swimsuit' or BetsyX.Chest == 'swimsuit'", Recolor("Betsy", "Panties", "images/BetsySex/Betsy_Sex_Panties_Bikini.png"),
            # Modification mode
            "BetsyX.Panties == 'cammy leotard' or BetsyX.Chest == 'cammy leotard'", "images/BetsySex/modification/Betsy_Sex_Panties_Cammy.png",
            # ----------------
            "BetsyX.Panties and BetsyX.Wet", Recolor("Betsy", "Panties", "images/BetsySex/Betsy_Sex_Panties_Blue_Wet.png"),
            "BetsyX.Panties", Recolor("Betsy", "Panties", "images/BetsySex/Betsy_Sex_Panties_Blue.png"),
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #Piercings under hose
#            "not BetsyX.Pierce", Null(),
#            "BetsyX.Pierce == 'ring'",ConditionSwitch(
#                    #If she has panties down. . .
#                    "Player.Sprite and Player.Cock == 'in'", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R_Fucking.png",
#                    "not BetsyX.Panties or BetsyX.PantiesDown", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R.png",
#                    "BetsyX.Panties == 'lace panties' and not BetsyX.PantiesDown", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R_Lace.png",
##                    "BetsyX.Panties == 'swimsuit' and not BetsyX.PantiesDown", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R_White.png",
#                    "True", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R_White.png",
#                    ),
#            #else, it's barbell
#            "not BetsyX.Panties or BetsyX.PantiesDown", "images/BetsySex/Betsy_Sex_Pierce_Pussy_B.png",
#            "BetsyX.Panties == 'lace panties' and not BetsyX.PantiesDown", "images/BetsySex/Betsy_Sex_Pierce_Pussy_B_Lace.png",
##            "BetsyX.Panties == 'swimsuit' and not BetsyX.PantiesDown", "images/BetsySex/Betsy_Sex_Pierce_Pussy_B_White.png",
#            "True", "images/BetsySex/Betsy_Sex_Pierce_Pussy_B_White.png",
#            ),
        (0,0), ConditionSwitch(
            #pantyhose layer
            "BetsyX.Panties and BetsyX.PantiesDown", Null(),
#            "BetsyX.Hose == 'tights'", "images/BetsySex/Betsy_Sex_Hose_Tights.png",
#            "BetsyX.Hose == 'ripped tights'", "images/BetsySex/Betsy_Sex_Hose_Tights_Holed.png",
            "BetsyX.Hose == 'pantyhose'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_Sex_Hose_Pantyhose.png"),
            "BetsyX.Hose == 'ripped pantyhose'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_Sex_Hose_Pantyhose_Holed.png"),
            "True", Null(),
            ),


        (0,0), ConditionSwitch(
            #Legs Layer
#            "BetsyX.Legs == 'skirt' and BetsyX.Upskirt", "images/BetsySex/Betsy_Sex_Legs_Skirt_Up.png",
            "BetsyX.Legs == 'skirt'", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_Sex_Legs_Skirt.png"),
            "BetsyX.Upskirt", Null(),
#            "BetsyX.Legs == 'skirt'", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_Sex_Legs_Skirt.png"),
            "BetsyX.Legs == 'shorts' and BetsyX.Wet > 1", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_Sex_Legs_Shorts_Wet.png"),
            "BetsyX.Legs == 'shorts'", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_Sex_Legs_Shorts.png"),
            "BetsyX.Legs == 'yoga pants' and BetsyX.Wet > 1", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_Sex_Legs_Yoga_Wet.png"),
            "BetsyX.Legs == 'yoga pants'", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_Sex_Legs_Yoga.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #scarf
            # Modification mode
            "BetsyX.Acc and 'scarf' in BetsyX.Acc", "images/BetsySex/Betsy_Sex_Scarf.png",
            # -----------------
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #towel
            "BetsyX.Over == 'towel'", Recolor("Betsy", "Over", "images/BetsySex/Betsy_Sex_Legs_Towel.png"),
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #pussy fondling animation
##            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Betsy_Sex_Fondle_Pussy",
#            "True", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Hand.png",
#            ),

        (0,0), ConditionSwitch(
            #Piercings over pants and pantyhose
            "not BetsyX.Pierce", Null(),
            "BetsyX.Pierce == 'ring'",ConditionSwitch(
                    #If she has panties down. . .
                    "Player.Sprite and Player.Cock == 'in'", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R_Fucking.png",

                    "BetsyX.Legs == 'shorts' and not BetsyX.Upskirt", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R_Blue.png",
                    "BetsyX.Legs == 'yoga pants' and not BetsyX.Upskirt", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R_Black.png",
                    "BetsyX.Hose == 'pantyhose' and not (BetsyX.Panties and BetsyX.PantiesDown)", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R_Lace.png",

                    "BetsyX.PantiesDown", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R.png",
                    "BetsyX.Chest == 'swimsuit'", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R_Blue.png",
                    "BetsyX.Panties == 'lace panties'", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R_Lace.png",
                    # Modification mode
                    "BetsyX.Chest == 'cammy leotard'", "images/BetsySex/modification/Betsy_Sex_Pierce_Pussy_R_Cammy.png",
                    # -----------------
                    "BetsyX.Panties", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R_Blue.png",
                    "True", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R.png",

                    "True", Null(),
                    ),
            #else, it's barbell
            "BetsyX.Legs == 'shorts' and not BetsyX.Upskirt", "images/BetsySex/Betsy_Sex_Pierce_Pussy_B_Blue.png",
            "BetsyX.Legs == 'yoga pants' and not BetsyX.Upskirt", "images/BetsySex/Betsy_Sex_Pierce_Pussy_B_Black.png",
            "BetsyX.Hose == 'pantyhose' and not (BetsyX.Panties and BetsyX.PantiesDown)", "images/BetsySex/Betsy_Sex_Pierce_Pussy_B_Lace.png",

            "BetsyX.PantiesDown", "images/BetsySex/Betsy_Sex_Pierce_Pussy_B.png",
            "BetsyX.Chest == 'swimsuit'", "images/BetsySex/Betsy_Sex_Pierce_Pussy_B_Blue.png",
            "BetsyX.Panties == 'lace panties'", "images/BetsySex/Betsy_Sex_Pierce_Pussy_B_Lace.png",
            # Modification moed
            "BetsyX.Chest == 'cammy leotard'", "images/BetsySex/modification/Betsy_Sex_Pierce_Pussy_B_Cammy.png",
            # ----------------
            "BetsyX.Panties", "images/BetsySex/Betsy_Sex_Pierce_Pussy_B_Blue.png",
            "True", "images/BetsySex/Betsy_Sex_Pierce_Pussy_B.png",
            ),
#        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer
#            "not Player.Sprite or Player.Cock != 'out'", Null(),
#            "Speed >= 2", "Betsy_Hotdog_Zero_Anim2",
#            "Speed", "Betsy_Hotdog_Zero_Anim1",
#            "True", "Betsy_Hotdog_Zero_Anim0",
#            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy'", "Betsy_Sex_Lick_Pussy",
            "Trigger == 'lick ass'", "Betsy_Sex_Lick_Ass",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy fondling animation
            "BetsyX.Offhand == 'fondle pussy' and BetsyX.Lust > 60 and not (Player.Sprite)",  At("BetsyFingerHand", GirlFingerPussyX()), #"Betsy_Sex_Mast2",
            "BetsyX.Offhand == 'fondle pussy'", At("BetsyMastHand", GirlGropePussyX()), #"Betsy_Sex_Mast",
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Betsy_Sex_Fondle_Pussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Footjob overlay
            "Player.Cock == 'foot'", Null(),
            "Player.Sprite and Player.Cock == 'anal'",AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_Feet_Mask.png"),
            "renpy.showing('Anal_Plug_In_Sex') or renpy.showing('Anal_Plug_Out_Sex')",AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_Feet_Mask.png"),
            "ShowFeet", "Betsy_Sex_Feet",
#            "Player.Sprite", AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_Feet_Mask.png"),
#            "Trigger == 'lick pussy'", AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_Feet_Mask.png"),
#            "Trigger == 'lick ass'", AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_Feet_Mask.png"),
            "True", AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_Feet_Mask.png"),
            ),

#        (0,0), ConditionSwitch(                                                                                 #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
#            "not Speed", "Betsy_Sex_Feet",
#            "Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_FeetMask.png"),
#            "True", "Betsy_Sex_Feet",
#            ),
        )
# End Betsy Sex Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_Sex_Feet:
    LiveComposite(
        #the lower legs used in the sex pose, referenced by Betsy_Sex_Legs
        (1120,840),
#        (0,0), "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Feet.png",                                                         #Legs Base

        (0,0), ConditionSwitch(
            #hose layer
            "(BetsyX.Hose == 'pantyhose' or BetsyX.Hose == 'ripped pantyhose') and BetsyX.Panties and BetsyX.PantiesDown", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Feet.png",
            "(BetsyX.Hose == 'tights' or BetsyX.Hose == 'ripped tights') and BetsyX.Panties and BetsyX.PantiesDown", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Feet.png",
            "BetsyX.Hose == 'socks'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_Sex_Feet_Socks.png"),
            "BetsyX.Hose == 'ripped pantyhose'", Recolor("Betsy", "Hose", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Feet_Hose_Holed.png"),
#            "BetsyX.Hose == 'ripped tights'", "images/BetsySex/Betsy_Sex_Feet_Tights_Holed.png",
#            "BetsyX.Hose == 'tights'", "images/BetsySex/Betsy_Sex_Feet_Tights.png",
#            "BetsyX.Hose == 'ripped pantyhose' and BetsyX.Panties and BetsyX.PantiesDown", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Feet.png",
            "BetsyX.Hose and BetsyX.Hose != 'garterbelt'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_Sex_Feet_Hose.png"),
#            "BetsyX.Hose == 'pantyhose'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_Sex_Feet_Hose.png"),
            "True", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Feet.png",   #Null(),
            ),

        (0,0), ConditionSwitch(
            #Wet look
            "not BetsyX.Water", Null(),
            "True", "images/BetsySex/Betsy_Sex_Water_Feet.png",
            ),
        (0,0), ConditionSwitch(
            #panties if down
            "not BetsyX.PantiesDown", Null(),
            "BetsyX.Panties == 'lace panties'", Recolor("Betsy", "Panties", "images/BetsySex/Betsy_Sex_Panties_Lace_Down.png"),
            "BetsyX.Panties == 'swimsuit' or BetsyX.Chest == 'swimsuit'", Null(),
            "BetsyX.Panties", Recolor("Betsy", "Panties", "images/BetsySex/Betsy_Sex_Panties_Blue_Down.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Legs Layer
            "BetsyX.Legs == 'yoga pants' and not BetsyX.Upskirt", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_Sex_Feet_Yoga.png"),
            "BetsyX.Legs == 'shorts' and BetsyX.Upskirt", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_Sex_Legs_Shorts_Down.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk
            "'feet' in BetsyX.Spunk", "images/BetsySex/Betsy_Sex_Spunk_Feet.png",
            "True", Null(),
            ),
        )

# Start Betsy Sex Pose Pussy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Betsy_Sex_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).

    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pussy_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and Speed", "Betsy_Sex_Heading_Pussy",
                "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pussy_Open.png",
                "BetsyX.Offhand == 'fondle pussy' and BetsyX.Lust > 60", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pussy_Open.png",
                "True", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pussy_Closed.png",
                )
#    contains:
#            # The background plate of her pussy
#            ConditionSwitch(
#                "not BetsyX.Wet", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/JubesSex/Jubes_Sex_WetPussy_F.png",
#                "True", "images/JubesSex/Jubes_Sex_WetPussy_C.png",
#                )
    contains:
            # pubes
            ConditionSwitch(
                "not BetsyX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/BetsySex/Betsy_Sex_Pubes_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and Speed >= 1", "images/BetsySex/Betsy_Sex_Pubes_Fucking.png",
                "Player.Sprite and Player.Cock == 'in'", Recolor("Betsy", "Pubes", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pubes_Open.png"),
                "Player.Sprite and Player.Cock == 'out'", Recolor("Betsy", "Pubes", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pubes_Open.png"),
                "Trigger == 'lick pussy'", Recolor("Betsy", "Pubes", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pubes_Open.png"),
                "BetsyX.Offhand == 'fondle pussy' and BetsyX.Lust > 60", Recolor("Betsy", "Pubes", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pubes_Open.png"),
                "True", Recolor("Betsy", "Pubes", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pubes_Closed.png"),
                )
    contains:
            #Spunk
            ConditionSwitch(
                "'in' not in BetsyX.Spunk or not Player.Male", Null(),
                "(BetsyX.Legs == 'pants' or BetsyX.Legs == 'shorts') and not BetsyX.Upskirt", Null(),
                "BetsyX.Panties and not BetsyX.PantiesDown", Null(),
                "True", AlphaMask("Spunk_Drip2","Betsy_Sex_Drip_Mask"),
                )
            offset (545,540)

    contains:
            ConditionSwitch(
                #Outside Spunk
                "'in' in BetsyX.Spunk and Player.Sprite and Player.Cock == 'in' and Speed and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_PussyF.png",
                "'in' in BetsyX.Spunk and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Pussy.png",
                "True", Null(),
                )
#            offset (0,-15)
#    contains:
#            #Spunk under penis
#            ConditionSwitch(
#                "'in' in BetsyX.Spunk", "images/BetsySex/Betsy_Sex_Spunk_Puss_Under.png",
#                "True", Null(),
#                )
#    contains:
#            #hose layer
#            ConditionSwitch(
#                "BetsyX.Panties and BetsyX.PantiesDown", Null(),
#                "BetsyX.Hose == 'ripped pantyhose' and ShowFeet", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_Sex_Hose_Pantyhose_Holed.png"),
#                "BetsyX.Hose == 'ripped pantyhose'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_Sex_Hose_Pantyhose_Holed.png"),
#                "True", Null(),
#                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            ConditionSwitch(
#                "not Player.Sprite", Null(),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 3", AlphaMask("Betsy_Sex_Fucking_Zero_Anim3", "Betsy_Sex_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", AlphaMask("Betsy_Sex_Fucking_Zero_Anim2", "Betsy_Sex_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and Speed == 1", AlphaMask("Betsy_Sex_Fucking_Zero_Anim1", "Betsy_Sex_Heading_Mask"),
                "Player.Sprite and Player.Cock == 'in'", "Betsy_Sex_Fucking_Zero_Anim0",
                "True", Null(),
                )
#    contains:
#            #Piercings
#            ConditionSwitch(
#                "BetsyX.Pierce == 'barbell' and Player.Sprite and Player.Cock == 'in' and Speed", "images/BetsySex/Betsy_Sex_Pierce_Pussy_BarbellF.png",
#                "BetsyX.Pierce == 'ring' and Player.Sprite and Player.Cock == 'in' and Speed", "images/BetsySex/Betsy_Sex_Pierce_Pussy_RingF.png",
#                "BetsyX.Pierce == 'barbell'", "images/BetsySex/Betsy_Sex_Pierce_Pussy_Barbell.png",
#                "BetsyX.Pierce == 'ring'", "images/BetsySex/Betsy_Sex_Pierce_Pussy_Ring.png",
#                "True", Null(),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed == 1", "Betsy_Pussy_Spunk_Heading",
#                "True", Null(),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "Speed == 1", Null(),
#                "'in' not in BetsyX.Spunk or not Player.Sprite or Player.Cock != 'in' or not Speed or not Player.Male", Null(),
##                "Speed <= 1", Null(), #"Betsy_Pussy_Spunk_Heading",
#                "True", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
#                )

    #End Betsy Pussy composite

image Betsy_Sex_Drip_Mask:
    #This is the mask for her drip pattern
    contains:
        "images/JubesSex/Jubes_Sex_Mask_Anal.png"
        offset (-545,-450)#(-275,-560)#(-145,-560)#(-225,-560)

image Betsy_Sex_Lick_Pussy:
        "Lick_Anim"
        zoom 0.7
        offset (535,500)#(505,680)

image Betsy_Sex_Lick_Ass:
        "Lick_Anim"
        zoom 0.7
        offset (535,580)#(535,550)

image Betsy_Sex_Fondle_Pussy:
        "GropePussy_Betsy"
        xzoom -1.5
        yzoom 1.5
        offset(-710,-300) #(-890,-300)
#        block:
#            ease 1 offset(-1000,0) #(535,500)
#            ease 1 offset(-1000,-1000) #(535,500)
#            ease 1 offset(0,-1000) #(535,500)
#            ease 1 offset(0,0) #(535,500)
#            repeat

#End Animations for Betsy's Pussy during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_Sex_Zero_Cock:
        #this is the cock generally used by Betsy's sex pose
        contains:
            subpixel True
            ConditionSwitch(
                "Player.Sprite", "Zero_Doggy_Insert",
                "True", Null(),
                )
            subpixel True
            anchor (0.5,1.0)
            transform_anchor True
            offset (1230,1620) #(546,1170)
            zoom 1.3

image Betsy_Sex_Fucking_Mask:
        #This is the mask image for Kitty's wide open pussy
        # Used in "Betsy_Sex_Speed2" and "Betsy_Sex_Speed3"
        contains:
            "images/JubesSex/Jubes_Sex_Mask_Fucking.png"
            yoffset 0#3

# Start Betsy Sex Pose Static / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_Sex_Static:
    # Pose for Betsy's Sex Pose in which she is static
    contains:
            #Betsy's underlying body
            subpixel True
            "Betsy_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
#                pause 0.3
                ease 1.5 ypos -185 #-120
                pause .3
                ease 1.45 ypos -180 #-130
                pause 0.25
                repeat
    contains:
            #Betsy's Legs
            subpixel True
            "Betsy_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
#            block:
#                pause 0.3
#                ease 1.4 ypos -185 #-120
#                pause .3
#                ease 1.25 ypos -180 #-130
#                ease 0.15 ypos -177 #-130
#                ease 0.1 ypos -180 #-130
#                repeat
    contains:
            subpixel True
            "Betsy_Sex_Zero_Cock"
            subpixel True
            transform_anchor True
            anchor (0.5,0.9)
            pos (530,540)#(-800,-800)   #(0,-180)
            rotate 0
            block: #3.5 total
#                pause 0.3
                easein 1.5 rotate 0 #-120
                pause .3
                ease 1.4 rotate -5 #-130
                ease 0.2 rotate 15 #-130
                easeout 0.1 rotate 10 #-130
#                pause 0.3
                repeat
    contains:
            #Betsy's Hand
            subpixel True
            "Betsy_Sex_Hand"
            pos (0,-180) #X less is left, Y less is up
            block:
#                pause 0.3
                ease 1.5 ypos -185 #-120
                pause .3
                ease 1.45 ypos -180 #-130
                pause 0.25
                repeat

    contains:
            #Betsy's Feet
            subpixel True
#            "Betsy_Sex_Feet"
            ConditionSwitch(
                #Footjob overlay
                "ShowFeet", AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_Feet_Mask.png"),
                "True", Null(),
                )
            pos (0,-180) #X less is left, Y less is up
#            block:
#                pause 0.3
#                ease 1.4 ypos -185 #-120
#                pause .3
#                ease 1.25 ypos -180 #-130
#                ease 0.15 ypos -177 #-130
#                ease 0.1 ypos -180 #-130
#                repeat

# End Betsy Sex Pose Speed Static / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Betsy Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Betsy Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_Sex_Fucking_Speed0:
    # Pose for Betsy's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Betsy's underlying body
            subpixel True
            "Betsy_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                ease 2 ypos -160 #0
                pause 0.8
                ease 2 ypos -180 #-130
                pause 0.2
                repeat
    contains:
            #Betsy's Legs
            subpixel True
            "Betsy_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -160 #0
                pause 0.8
                ease 2 ypos -180 #-130
                repeat
    contains:
            #Betsy's Hand
            subpixel True
            "Betsy_Sex_Hand"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                ease 2 ypos -160 #0
                pause 0.8
                ease 2 ypos -180 #-130
                pause 0.2
                repeat
# End main animation for Sex Pose Fucking Speed 1


image Betsy_Sex_Fucking_Zero_Anim0:
        #this is Betsy's sex animation, Speed 1 Fucking
        contains:
            subpixel True
            "Betsy_Sex_Zero_Cock"
#            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            subpixel True
            pos (0,60)#(498,530)
            block:
                pause 0.2
                easeout 1 ypos 50 #-140
                easein .8 ypos 45 #-140
                pause 1.4
                easeout 0.6 ypos 60 #-140
                easein 1 ypos 60 #-10
                repeat


#            pos (0,40)#(498,530)
#            block:
#                pause 0.2
#                easeout 1 ypos 20 #-140
#                easein .8 ypos 10 #-140
#                pause 1.4
#                easeout 0.6 ypos 10 #-140
#                easein 1 ypos 40 #-10
#                repeat

# End Betsy Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Betsy Sex Pose Speed 1 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_Sex_Fucking_Speed1:
    # Pose for Betsy's Sex Pose in which she is fucking at speed 1 (heading)
    contains:
            #Betsy's underlying body
            subpixel True
            "Betsy_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause .8
                ease 1.5 ypos -200 #0
                pause 1.6
                ease 1.1 ypos -180 #-130
                repeat
    contains:
            #Betsy's Legs
            subpixel True
            "Betsy_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause 0.7
                ease 1.5 ypos -200 #0
                pause 1.6
                ease 1.2 ypos -180 #-130
                repeat
    contains:
            #cum over cock
            ConditionSwitch(
                "'in' in BetsyX.Spunk and Player.Sprite and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
                "True", Null(),
                )
            anchor (0.5,0.5)
            transform_anchor True
            xoffset 560
            yoffset 480
            ypos -170 #-130
            xzoom .7
            parallel: #adds to 5
                pause 0.7
                ease 1.5 ypos -200 #0
                pause 1.4
                ease 1.4 ypos -170 #-130
                repeat
            parallel:
                pause 0.2
                ease 1.2 xzoom .9
                ease .4 xzoom .9
                pause 1.2
                ease .2 xzoom .9
                ease 1.8 xzoom .7
                repeat
    contains:
            #Betsy's Hand
            subpixel True
            "Betsy_Sex_Hand"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause .8
                ease 1.5 ypos -200 #0
                pause 1.6
                ease 1.1 ypos -180 #-130
                repeat
# End main animation for Sex Pose Fucking Speed 1


image Betsy_Sex_Fucking_Zero_Anim1:
        #this is Betsy's sex animation, Speed 1 Fucking
        contains:
            subpixel True
            "Betsy_Sex_Zero_Cock"
            subpixel True
            pos (0,40)#(498,530)
            block:
                pause 0.2
#                ease 0.95 ypos -145
                ease 2 ypos -10#-10 #-140
                pause .8
                ease 2 ypos 40 #-10
                repeat

image Betsy_Sex_Heading_Mask:
        #This is the mask image for Betsy's heading pussy
        contains:
            "images/JubesSex/Jubes_Sex_Mask_Fucking.png"
            yoffset 10
            block:
                pause 0.2
                ease 2 yoffset 0#3
                pause 0.9#0.8
                ease 1.9 yoffset 10 #2.0
                repeat


image Betsy_Sex_Heading_Pussy:
        #This is the image for Betsy's heading pussy growing
#        contains:
#            "images/BetsySex/Betsy_Sex_Pussy_Fucking_Base.png"
        contains:
            "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pussy_Fucking.png"
            anchor (0.5,0)
            subpixel True
            transform_anchor True
            xoffset 560
            xzoom .7
            block:
                pause 0.2
                ease 1.2 xzoom 1
                ease .4 xzoom .9
                pause 1.2
                ease .2 xzoom 1
                ease 1.8 xzoom .7
                repeat
        contains:
            "images/JubesDoggy/Jubes_Doggy_Pussy_HHole.png"
            anchor (0.5,0.75)
            subpixel True
            transform_anchor True
            xoffset 560
            yoffset 560
            xzoom .7
            alpha 0.3
            parallel:
                pause 0.2
                ease 1.2 xzoom 1
                ease .4 xzoom .9
                pause 1.2
                ease .2 xzoom 1
                ease 1.8 xzoom .7
                repeat
            parallel:
                pause 0.2
                ease 1.2 yzoom 1
                ease .4 yzoom .9
                pause 1.2
                ease .2 yzoom 1
                ease 1.8 yzoom .7
                repeat

image Betsy_Pussy_Spunk_Heading:
        #This is the image for Betsy's heading pussy cum
        contains:
            ConditionSwitch(
                "'in' in BetsyX.Spunk and Player.Sprite and Player.Cock == 'in' and Speed == 1 and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
                "True", Null(),
                )
            anchor (0.5,0)
            transform_anchor True
            xoffset 560
            yoffset 5
            xzoom .7
            block:
                pause 0.2
                ease 1.2 xzoom 1
                ease .4 xzoom .9
                pause 1.2
                ease .2 xzoom 1
                ease 1.8 xzoom .7
                repeat

# End Betsy Sex Pose Speed 1 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Betsy Sex Pose Speed 2 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_Sex_Fucking_Speed2:
    # Pose for Betsy's Sex Pose in which she is fucking at speed 2
    contains:
            #Betsy's underlying body
            subpixel True
            "Betsy_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 4.2
                pause 0.45
                ease 0.95 ypos -205 # 5
                ease 0.45 ypos -200 # 0
                pause 0.6
                ease 1.75 ypos -180 # -130
                repeat
    contains:
            #Betsy's Legs
            subpixel True
            "Betsy_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 4.2
                pause 0.4
                ease 0.95 ypos -205 # 5
                ease 0.45 ypos -200 # 0
                pause 0.6
                ease 1.8 ypos -180 # -130
                repeat
    contains:
            #cum over cock
            ConditionSwitch(
                "'in' in BetsyX.Spunk and Player.Sprite and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
                "True", Null(),
                )
            anchor (0.5,0.5)
            transform_anchor True
            xoffset 560
            yoffset 480
            ypos -180 #-130
            xzoom .8
            parallel: #adds to 4.2
                pause 0.4
                ease 0.95 ypos -205 # 5
                ease 0.45 ypos -200 # 0
                pause 0.6
                ease 1.8 ypos -180 # -130
                repeat
            parallel:
                pause 0.15
                ease 0.9 xzoom .9 # -145
                pause 1.35
                ease 1.80 xzoom .75 #-10
                repeat
    contains:
            #Betsy's Hand
            subpixel True
            "Betsy_Sex_Hand"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 4.2
                pause 0.45
                ease 0.95 ypos -205 # 5
                ease 0.45 ypos -200 # 0
                pause 0.6
                ease 1.75 ypos -180 # -130
                repeat
# End main animation for Sex Pose Fucking Speed 2


image Betsy_Sex_Fucking_Zero_Anim2:
        #this is Betsy's sex animation, Speed 2 Fucking
        contains:
            subpixel True
            "Betsy_Sex_Zero_Cock"
            subpixel True
            pos (0,20)#(498,530)
            block:
                pause 0.2
                ease 0.95 ypos -100 # -145
                ease 0.25 ypos -90 # -140
                pause .8
                ease 2 ypos 20 #-10
                repeat

# End Betsy Sex Pose Speed 2 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Betsy Sex Pose Speed 3 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_Sex_Fucking_Speed3:
    # Pose for Betsy's Sex Pose in which she is fucking at speed 3
    contains:
            #Betsy's underlying body
            subpixel True
            "Betsy_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.45
                ease 0.45 ypos -220
                ease 0.15 ypos -210
#                pause 0.35
                ease 0.75 ypos -180
                repeat
    contains:
            #Betsy's Legs
            subpixel True
            "Betsy_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.4
                ease 0.45 ypos -220
                ease 0.15 ypos -210
#                pause 0.35
                ease 0.8 ypos -180
                repeat
    contains:
            #cum over cock
            ConditionSwitch(
                "'in' in BetsyX.Spunk and Player.Sprite and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
                "True", Null(),
                )
            anchor (0.5,0.5)
            transform_anchor True
            xoffset 560
            yoffset 480
            ypos -180 #-130
            xzoom .7
            parallel: #adds to 4.2
                pause 0.4
                ease 0.45 ypos -220
                ease 0.15 ypos -210
#                pause 0.35
                ease 0.8 ypos -180
                repeat
            parallel:
                pause 0.1
                ease 0.65 xzoom .9
                pause 0.5
                ease 0.55 xzoom .75
                repeat
    contains:
            #Betsy's Hand
            subpixel True
            "Betsy_Sex_Hand"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.45
                ease 0.45 ypos -220
                ease 0.15 ypos -210
#                pause 0.35
                ease 0.75 ypos -180
                repeat


# End main animation for Sex Pose Fucking Speed 3


image Betsy_Sex_Fucking_Zero_Anim3:
        #this is Betsy's sex animation, Speed3 Fucking
        contains:
            subpixel True
            "Betsy_Sex_Zero_Cock"
            subpixel True
            pos (0,10)
            block:
                pause 0.1
                ease 0.55 ypos -100
                ease 0.15 ypos -90
                pause 0.25
                ease 0.75 ypos 10
                repeat

# End Betsy Sex Pose Speed 3 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Animations for Betsy's Ass during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Betsy's Ass during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_Sex_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/JubesSex/Jubes_Sex_Anal.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/JubesSex/Jubes_Sex_Anal.png",
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Anus.png",
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Anus.png",
            "Player.Sprite and Player.Cock == 'anal' and Speed", "Betsy_Sex_Anal_Heading",
            "Player.Sprite and Player.Cock == 'anal'", "Betsy_Sex_Anal_Tip",
            "BetsyX.Plug", "images/PlugBase_Sex.png",
            "BetsyX.Loose > 2", "Betsy_Gape_Anal_Sex",
            "BetsyX.Loose", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Anus_Loose.png",
            "True", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Anus_Tight.png",
            "True", Null(),
            )
    contains:
            #Spunk under penis
            ConditionSwitch(
                "'anal' not in BetsyX.Spunk or not Player.Male", Null(),
#                "Player.Sprite and Player.Cock != 'anal' and Speed >= 1", "images/BetsySex/Betsy_Sex_Spunk_Anal_Under.png",
                "Player.Sprite and Player.Cock == 'anal' and Speed == 1", "Betsy_Sex_Anal_Spunk_Heading_Under",
                "True", "images/JubesSex/Jubes_Sex_Spunk_Anal.png",
                )
            offset (5,0)
    contains:
            # The animation of Zero's moving penis, masked by her anus shape
            ConditionSwitch(
                "not Player.Sprite or Player.Cock != 'anal'", Null(),
                "Speed >= 3",  AlphaMask("Betsy_Sex_Anal_Zero_Anim3", "Betsy_Sex_Anal_MaskF"),
                "Speed >= 2", AlphaMask("Betsy_Sex_Anal_Zero_Anim2", "Betsy_Sex_Anal_MaskF"),
                "Speed", AlphaMask("Betsy_Sex_Anal_Zero_Anim1", "Betsy_Sex_Anal_Mask"),
                "True", AlphaMask("Betsy_Sex_Anal_Zero_Anim0", "Betsy_Sex_Anal_Mask"),
                )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "'anal' not in BetsyX.Spunk or not Player.Sprite or Player.Cock != 'anal' or not Speed or not Player.Male", Null(),
                "Speed == 1", "Betsy_Sex_Anal_Spunk_Heading_Over",
                "True", "Betsy_Sex_Anal_Spunk",
                )


image Betsy_Gape_Anal_Sex:
        #removing an anal plug
        contains:
            #Hole
            "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Anus_Loose.png"
            transform_anchor True
            subpixel True
            anchor (560,615)#(560,620)
            offset (560,617)#(560,617)
            zoom .40 # tight
            block:
                ease 3 zoom 1 #in.87
                ease 3 zoom .80 #out
                repeat

image Betsy_Sex_Anal_Spunk:
    ConditionSwitch(
                "'anal' in BetsyX.Spunk and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Anal_Over.png",
                "True", Null(),
                )
    anchor (0.5,0.5)
    pos (0.5,0.5)
#    xoffset 20
    yoffset -23#68
    xzoom .9#1.2

image Betsy_Sex_Anal_Mask:
        #This is the mask image for small stuff
        # Used in "Betsy_Sex_Speed2" and "Betsy_Sex_Speed3"
        contains:
            "images/JubesSex/Jubes_Sex_Mask_Anal.png"
            yoffset 98 #-9
            xoffset 3 #3
#            xoffset -5

image Betsy_Sex_Anal_MaskF:
        #This is the mask image for deep stuff
        # Used in "Betsy_Sex_Speed2" and "Betsy_Sex_Speed3"
        contains:
            "images/JubesSex/Jubes_Sex_Mask_AnalB.png"
            yoffset 98 #-9
            xoffset 3



# Start Betsy Sex Pose Speed 0 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_Sex_Anal_Speed0:
    # Pose for Betsy's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Betsy's underlying body
            subpixel True
            "Betsy_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.5
                ease 1 ypos -185 #40
                pause 1.0
                ease 1.5 ypos -180 #90
                repeat
    contains:
            #Betsy's Legs
            subpixel True
            "Betsy_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.2
                ease 1 ypos -190 #40
                pause 1.3
                ease 1.5 ypos -180 #90
                repeat
    contains:
            #Betsy's underlying body
            subpixel True
            "Betsy_Sex_Hand"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.5
                ease 1 ypos -185 #40
                pause 1.0
                ease 1.5 ypos -180 #90
                repeat

# End main animation for Sex Pose Anal Speed 1


image Betsy_Sex_Anal_Zero_Anim0:
        #this is Betsy's sex animation, Speed 0 Anal
        contains:
            subpixel True
            "Betsy_Sex_Zero_Cock"
#            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            subpixel True
            pos (3,135)#(498,530)
            block:
                pause 0.2
                ease 2 ypos 130 #90
                pause .8
                ease 2 ypos  135 #130
                repeat

image Betsy_Sex_Anal_Tip:
#    "images/JubesSex/Jubes_Sex_Anal.png"
    "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Anus.png"
    anchor (560,620)
    pos (560,620)
    transform_anchor True
#    yoffset -20
    zoom 0.4
    block:
        #total 5 second
        pause 0.5   #
        ease 1.50 zoom 0.55   #.75 (1.0)
        pause 0.5   #
        ease .25 zoom 0.55  #(1.0)
        ease 2.25 zoom 0.4   #(0.6)
        repeat

# End Betsy Sex Pose Speed 0 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Betsy Sex Pose Speed 1 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_Sex_Anal_Heading:
#    "images/JubesSex/Jubes_Sex_Anal.png"
    "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Anus.png"
    anchor (560,620)
    pos (560,620)
    transform_anchor True
#    yoffset -20
    zoom 0.6
    block:
        #total 5 second
        pause 0.5   #
        ease 1.50 zoom 1   #.85 (1.0)
        pause 0.5   #
        ease .25 zoom 1  #(1.0)
        ease 2.25 zoom 0.6   #(0.6)
        repeat

image Betsy_Sex_Anal_Spunk_Heading_Over:
    ConditionSwitch(
                "'anal' in BetsyX.Spunk and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Anal_Over.png",
                "True", Null(),
                )
    anchor (0.5,0.5)
    pos (0.5,0.5)
#    xoffset 20
    yoffset -23
    xzoom 0.6
    block:
        #total 5 second
        pause 0.5   #
        ease 1.50 xzoom 0.9   #.75 (1.0)
        pause 0.5   #
        ease .25 xzoom 0.9 #(1.0)
        ease 2.25 xzoom 0.6   #(0.6)
        repeat


#    yoffset -23#68
#    xzoom .9#1.2

image Betsy_Sex_Anal_Spunk_Heading_Under:
    "images/JubesSex/Jubes_Sex_Spunk_Anal.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
    block:
        #total 5 second
        ease .75 xzoom 1.0
        ease .25 xzoom 0.95
        pause 1.50
        ease .25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

image Betsy_Sex_Anal_Speed1:
    # Pose for Betsy's Sex Pose in which she is fucking at speed 1 (heading)
    contains:
            #Betsy's underlying body
            subpixel True
            "Betsy_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.5
                ease 1 ypos -185 #40
                pause 1.0
                ease 1.5 ypos -180 #90
                repeat
    contains:
            #Betsy's Legs
            subpixel True
            "Betsy_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.2
                ease 1 ypos -190 #40
                pause 1.3
                ease 1.5 ypos -180 #90
                repeat
    contains:
            #Betsy's underlying body
            subpixel True
            "Betsy_Sex_Hand"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.5
                ease 1 ypos -185 #40
                pause 1.0
                ease 1.5 ypos -180 #90
                repeat

# End main animation for Sex Pose Anal Speed 1


image Betsy_Sex_Anal_Zero_Anim1:
        #this is Betsy's sex animation, Speed 1 Anal
        contains:
            subpixel True
            "Betsy_Sex_Zero_Cock"
#            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            subpixel True
            pos (3,130)#(498,530)
            block:
                pause 0.2
                ease 2 ypos 90 #40
                pause .8
                ease 2 ypos  130 #90
                repeat

# End Betsy Sex Pose Speed 1 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Betsy Sex Pose Speed 2 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_Sex_Anal_Speed2:
    # Pose for Betsy's Sex Pose in which she is doing anal at speed 2
    contains:
            #Betsy's underlying body
            subpixel True
            "Betsy_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.5
                ease 1.0 ypos -212
                pause .9
                ease 1.8 ypos -180
                repeat
    contains:
            #Betsy's Legs
            subpixel True
            "Betsy_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.4
                ease 0.95 ypos -215
                ease 0.25 ypos -210
                pause .8
                ease 1.8 ypos -180
                repeat
    contains:
            #Betsy's underlying body
            subpixel True
            "Betsy_Sex_Hand"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.5
                ease 1.0 ypos -212
                pause .9
                ease 1.8 ypos -180
                repeat
#    contains:
#            #Zero's cock in the sex pose
#            AlphaMask("Betsy_Sex_Fucking_Zero_Anim2", "Betsy_Sex_Fucking_Mask")
# End main animation for Sex Pose Fucking Speed 2


image Betsy_Sex_Anal_Zero_Anim2:
        #this is Betsy's sex animation, Speed 2 Fucking
        contains:
            subpixel True
            "Betsy_Sex_Zero_Cock"
#            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            subpixel True
            pos (3,-10)#(498,530)
            block:
                pause 0.2
                ease 0.95 ypos -25
                ease 0.25 ypos -20
                pause .8
                ease 2 ypos 90
                repeat

# End Betsy Sex Pose Speed 2 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Betsy Sex Pose Speed 3 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_Sex_Anal_Speed3:
    # Pose for Betsy's Sex Pose in which she is Anal at speed 3
    contains:
            #Betsy's underlying body
            subpixel True
            "Betsy_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 1.8
#                pause 0.5
                easein .4 ypos -180
                ease .35 ypos -210
                pause .4
                ease .65 ypos -185
                repeat

    contains:
            #Betsy's Legs
            subpixel True
            "Betsy_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 1.8
#                pause 0.4
                easein 0.4 ypos -180
                ease 0.3 ypos -215
                ease 0.1 ypos -210
                pause 0.4
                easeout 0.6 ypos -185
                repeat
    contains:
            #Betsy's underlying body
            subpixel True
            "Betsy_Sex_Hand"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 1.8
#                pause 0.5
                easein .4 ypos -180
                ease .35 ypos -210
                pause .4
                ease .65 ypos -185
                repeat

# End main animation for Sex Pose Fucking Speed 3


image Betsy_Sex_Anal_Zero_Anim3:
        #this is Betsy's sex animation, Speed3 Anal
        contains:
            subpixel True
            "Betsy_Sex_Zero_Cock"
            subpixel True
            pos (3,-40)
            block:
                pause 0.1
                ease 0.55 ypos -25
                ease 0.15 ypos -20
                pause 0.25
                ease 0.75 ypos 90
                repeat

# End Betsy Sex Pose Speed 3 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Betsy Sex Pose Speed 1 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_Sex_Hotdog_Speed1:
    # Pose for Betsy's Sex Pose in which she is hotdogging at speed 1 (slow)
    contains:
            #Betsy's underlying body
            subpixel True
            "Betsy_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
#            block:
#                pause 0.8
#                ease 0.8 ypos -190 #-120
#                pause .5
#                ease 1.0 ypos -180 #-130
#                pause 0.4
#                repeat
            block:
                pause 0.65
                ease 0.7 ypos -200 #-120
                ease 0.2 ypos -195 #-130
                pause .5
                ease 1.0 ypos -180 #-130
                pause 0.45
                repeat
    contains:
            #Betsy's Legs
            subpixel True
            "Betsy_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.6
                ease 0.7 ypos -200 #-120
                ease 0.2 ypos -195 #-130
                pause .5
                ease 1.0 ypos -180 #-130
                pause 0.5
                repeat
    contains:
            subpixel True
            "Betsy_Sex_Zero_Cock"
            subpixel True
            pos (0,-180)
            block:
                pause 0.3
                ease 1.0 ypos -330 #-120
                pause .5
                ease 1.5 ypos -175 #-130
                ease 0.2 ypos -180 #-130
#                pause 0.3
                repeat
    contains:
            #Betsy's underlying body
            subpixel True
            "Betsy_Sex_Hand"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.65
                ease 0.7 ypos -200 #-120
                ease 0.2 ypos -195 #-130
                pause .5
                ease 1.0 ypos -180 #-130
                pause 0.45
                repeat
#    contains:
#            #Betsy's Feet
#            subpixel True
#            "Betsy_Sex_Feet"
##            ConditionSwitch(
##                #Footjob overlay
##                "ShowFeet", AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_FeetMask.png"),
##                "True", Null(),
##                )
#            pos (0,-180) #X less is left, Y less is up
#            block:
#                pause 0.6
#                ease 0.7 ypos -200 #-120
#                ease 0.2 ypos -195 #-130
#                pause .5
#                ease 1.0 ypos -180 #-130
#                pause 0.5
#                repeat

# End main animation for Sex Pose Hotdog Speed 1

# End Betsy Sex Pose Speed 1 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Betsy Sex Pose Speed 2 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_Sex_Hotdog_Speed2:
    # Pose for Betsy's Sex Pose in which she is hotdogging at speed 2 (fast)
    contains:
            #Betsy's underlying body
            subpixel True
            "Betsy_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.12
                ease 0.4 ypos -215 #-120
                ease 0.1 ypos -205 #-130
                pause 0.25
                ease 0.73 ypos -180 #-130
#                pause 0.25
                repeat
    contains:
            #Betsy's Legs
            subpixel True
            "Betsy_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.1
                ease 0.4 ypos -215 #-120
                ease 0.1 ypos -205 #-130
                pause 0.25
                ease 0.75 ypos -180 #-130
#                pause 0.25
                repeat
    contains:
            subpixel True
            "Betsy_Sex_Zero_Cock"
            subpixel True
            pos (0,-180)
            block:
#                pause 1.2
                ease 0.5 ypos -330 #-120
                pause 0.25
                ease 0.75 ypos -205 #-130
                ease 0.1 ypos -210 #-130
                #pause 0.3
                repeat
    contains:
            #Betsy's Hand
            subpixel True
            "Betsy_Sex_Hand"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.12
                ease 0.4 ypos -215 #-120
                ease 0.1 ypos -205 #-130
                pause 0.25
                ease 0.73 ypos -180 #-130
#                pause 0.25
                repeat
#    contains:
#            #Betsy's Feet
#            subpixel True
#            "Betsy_Sex_Feet"
##            ConditionSwitch(
##                #Footjob overlay
##                "ShowFeet", AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_FeetMask.png"),
##                "True", Null(),
##                )
#            pos (0,-180) #X less is left, Y less is up
#            block:
#                pause 0.1
#                ease 0.4 ypos -215 #-120
#                ease 0.1 ypos -205 #-130
#                pause 0.25
#                ease 0.75 ypos -180 #-130
##                pause 0.25
#                repeat

# End main animation for Sex Pose Hotdog Speed 2

# End Betsy Sex Pose Speed 2 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Betsy Sex Pose Speed 0 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_Sex_FJ_Speed0:
    # Pose for Betsy's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Betsy's underlying body
            subpixel True
            "Betsy_Sex_Body"
            pos (50,-270) #X less is left, Y less is up (80,0)
            block: #adds to 5
#                pause 0.2
                ease 2.2 ypos -280 #10
                pause 0.8
                ease 2 ypos -270 #0
#                pause 0.2
                repeat
    contains:
            #Betsy's Legs
            subpixel True
            "Betsy_Sex_Legs"
            pos (50,-270) #X less is left, Y less is up (80,0)
            block: #adds to 5
#                pause 0.2
                ease 2 ypos -290 #10
                pause 0.8
                ease 2 ypos -270 #0
                pause 0.2
                repeat
    contains:
            #Betsy's Hand
            subpixel True
            "Betsy_Sex_Hand"
            pos (50,-270) #X less is left, Y less is up (80,0)
            block: #adds to 5
#                pause 0.2
                ease 2.2 ypos -280 #10
                pause 0.8
                ease 2 ypos -270 #0
#                pause 0.2
                repeat
    contains:
            subpixel True
#            "Betsy_Sex_Zero_Cock"
            "Zero_Blowcock"
            zoom .5
            subpixel True
            pos (610,520) #(630,520)
    contains:
            #Betsy's Legs
            subpixel True
            "Betsy_Sex_Feet"
#            alpha 0.5
#            AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_Feet_Mask.png")
            pos (50,-270) #X less is left, Y less is up (80,0)
            block: #adds to 5
#                pause 0.2
                ease 2 ypos -290 #10
                pause 0.8
                ease 2 ypos -270 #0
                pause 0.2
                repeat

# End main animation for Sex Pose Footjob Speed 0

# End Betsy Sex Pose Speed 0 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Betsy Sex Pose Speed 1 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_Sex_FJ_Speed1:
    # Pose for Betsy's Sex Pose in which she is fucking at speed 1 (slow)
    contains:
            #Betsy's underlying body
            subpixel True
            "Betsy_Sex_Body"
            pos (50,-320) #X less is left, Y less is up
            block: #adds to 5
#                pause 0.2
                ease 2 ypos -240 #-140
                pause 1
                ease 2 ypos -320 #-280
#                pause 0.4
                repeat
    contains:
            #Betsy's Legs
            subpixel True
            "Betsy_Sex_Legs"
            pos (50,-320) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -240 #-140
                pause 0.8
                ease 2 ypos -320 #-280
                repeat
    contains:
            #Betsy's Hand
            subpixel True
            "Betsy_Sex_Hand"
            pos (50,-320) #X less is left, Y less is up
            block: #adds to 5
#                pause 0.2
                ease 2 ypos -240 #-140
                pause 1
                ease 2 ypos -320 #-280
#                pause 0.4
                repeat
    contains:
            subpixel True
#            "Betsy_Sex_Zero_Cock"
            "Zero_Blowcock"
            zoom .5
            subpixel True
            pos (610,520) #(0,-380)
            block: #adds to 5
                pause 0.8
                ease 1.5 ypos 550 #40
                pause 0.7
                ease 1 ypos 520 #-100
                pause 1
                repeat
    contains:
            #Betsy's Legs
            subpixel True
            "Betsy_Sex_Feet"
#            alpha 0.5
#            AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_Toes.png")
#            ConditionSwitch(
#                #Footjob overlay
#                "ShowFeet", AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_Toes.png"),
#                "True", Null(),
#                )
            pos (50,-320) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -240 #-140
                pause 0.8
                ease 2 ypos -320 #-280
                repeat

# End main animation for Sex Pose Footjob Speed 1

# End Betsy Sex Pose Speed 1 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Betsy Sex Pose Speed 2 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_Sex_FJ_Speed2:
    # Pose for Betsy's Sex Pose in which she is fucking at speed 2 (fast)
    contains:
            #Betsy's underlying body
            subpixel True
            "Betsy_Sex_Body"
            pos (50,-260) #X less is left, Y less is up
            block: #adds to 1.9
#                pause 0.1
                ease 0.8 ypos -160 #0
                pause 0.2 #0.4
                ease 0.9 ypos -260 #-130
                repeat
    contains:
            #Betsy's Legs
            subpixel True
            "Betsy_Sex_Legs"
            pos (50,-260) #X less is left, Y less is up
            block: #adds to 1.9
                pause 0.1
                ease 0.8 ypos -160 #0
                pause 0.1 #0.4
                ease 0.9 ypos -260 #-130
                repeat
    contains:
            #Betsy's Hand
            subpixel True
            "Betsy_Sex_Hand"
            pos (50,-260) #X less is left, Y less is up
            block: #adds to 1.9
#                pause 0.1
                ease 0.8 ypos -160 #0
                pause 0.2 #0.4
                ease 0.9 ypos -260 #-130
                repeat
    contains:
            subpixel True
            "Zero_Blowcock"
            zoom .5
            subpixel True
            pos (610,520) #(0,-380)
            block: #adds to 5
                pause 0.5
                ease 0.4 ypos 540 #40
                pause 0.1
                ease .4 ypos 520 #-100
                pause .5
                repeat
    contains:
            #Betsy's Legs
            subpixel True
            "Betsy_Sex_Feet"
#            AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_Toes.png")
#            ConditionSwitch(
#                #Footjob overlay
#                "ShowFeet", AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_Toes.png"),
#                "True", Null(),
#                )
            pos (50,-260) #X less is left, Y less is up
            block: #adds to 1.9
                pause 0.1
                ease 0.8 ypos -160 #0
                pause 0.1 #0.4
                ease 0.9 ypos -260 #-130
                repeat

# End main animation for Sex Pose Footjob Speed 2

# End Betsy Sex Pose Speed 2 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     Sex Launch/Reset
label Betsy_Sex_Launch(Line = Trigger):
    $ BetsyX.Offhand = 0 if BetsyX.Offhand == "hand" else BetsyX.Offhand

#    #temporary, remove / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
#    return
#    #temporary, remove / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    $ BetsyX.Pose = "doggy"
##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary

    $ Line = "solo" if not Line else Line
    if Line == "sex":
        $ Player.Sprite = 1
        $ Player.Cock = "in"
        call Cock_Occupied(BetsyX,"pussy")
        if Trigger2 in ("fondle pussy","dildo pussy","lick pussy"):
                $ Trigger2 = 0
    elif Line == "anal":
        $ Player.Sprite = 1
        $ Player.Cock = "anal"
        call Cock_Occupied(BetsyX,"anal")
        if Trigger2 in ("insert ass","dildo anal","lick ass"):
                $ Trigger2 = 0
    elif Line == "hotdog":
        $ Player.Sprite = 1
        if BetsyX.PantsNum() == 5: #upskirts her if she's in a skirt
                $ BetsyX.Upskirt = 1
        $ Player.Cock = "out"
    elif Line == "foot":
        $ Player.Sprite = 1
        $ ShowFeet = 1
        $ Player.Cock = "foot"
    elif Line == "massage":
        $ Player.Sprite = 0
        $ Player.Cock = 0
    elif Line == "dildo pussy":
        $ Player.Cock = 0 if Player.Cock == "in" else Player.Cock
    elif Line == "dildo anal":
        $ Player.Cock = 0 if Player.Cock == "anal" else Player.Cock
    else: #elif Line == "solo":
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        if Trigger != "fondle pussy":
                $ Speed = 0

    if Player.Sprite:
        call Zero_Strapped(BetsyX) #puts strap-on on.
    $ Trigger = Line

    if BetsyX.Pose == "doggy":
            call Betsy_Doggy_Launch(Line)
            return
    if renpy.showing("Betsy_SexSprite"):
        return
    $ Speed = 0
    call Girl_Hide(BetsyX,1)
    show Betsy_SexSprite zorder 150
    with dissolve
    return

label Betsy_Sex_Reset:
    if renpy.showing("Betsy_Doggy_Animation"):
        call Betsy_Doggy_Reset
        return
    if not renpy.showing("Betsy_SexSprite"):
        return
    $ BetsyX.ArmPose = 2
    hide Betsy_SexSprite
    call Girl_Hide(BetsyX)
#    call Set_The_Scene(Dress = 0)
    show Betsy_Sprite at SpriteLoc(BetsyX.SpriteLoc) zorder BetsyX.Layer:
        alpha 1 zoom 1 offset (0,0) anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return


# End Betsy Sex Pose Content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


## End Betsy Sex Pose Content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Betsy's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





## Betsy's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Betsy_BJ_Animation:#BJ_NewTest:                                                                #core BJ animation
    LiveComposite(
        (800,950),
        (0,0), ConditionSwitch( #-270,-160
            # Betsy's hair backside
            "Speed == 0", "Betsy_BJ_Anim0",               #Static
            "Speed == 1", "Betsy_BJ_Anim1",               #Licking

#            "True", "Betsy_BJ_Anim2",               #Heading

            "Speed == 2", "Betsy_BJ_Anim2",               #Heading
            "Speed == 3", "Betsy_BJ_Anim3",               #Sucking
            "Speed == 4", "Betsy_BJ_Anim4",               #Deepthroat
            "Speed == 5", "Betsy_BJ_Anim5",               #Cumming High
            "Speed == 6", "Betsy_BJ_Anim6",               #Cumming Deep
            "True", Null(),
            ),
        )
#    zoom 1
#    anchor (.5,.5)
    zoom .8 #.7
    transform_anchor True
    anchor (.5,.5)
    offset (-95,85) #(-90,100)


#image Betsy_BJ_Backdropb:
#    LiveComposite(
#        (800,950),       #550,950
##        (-10,-90), "Betsy_BJ_HairBack", #(75,-10)
#        (0,0), "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Body.png",
##        (0,0), "Betsy_TJ_Tits_Under",
##        (0,0), "Betsy_TJ_Tits_Over",

##        (0,0), "images/BetsyBJFace/Betsy_TJ_RefLine.png",
##        (-10,-90), "Betsy_Sprite_Head", #(75,-10)
#        )
#    transform_anchor True
#    anchor (0.45, 0.35)#(0.6, 1.0)
##    alpha 0.2
#    xoffset 50#30
#    yoffset -530#-530
##    zoom .75  #.76
#    rotate 0

image Betsy_BJ_Backdrop:
    LiveComposite(
        (800,950),       #550,950
#        (-10,-90), "Betsy_BJ_HairBack", #(75,-10)
        (0,0), ConditionSwitch(
            # Body
            # Modification mode
            "BetsyX.Arms == 'cammy gloves'", "images/BetsyBJFace/modification/[BetsyX.skin_image.skin_path]Betsy_BJ_Body_Cammy.png",
            # -----------------
            "BetsyX.Arms", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Body_G.png",
            "True", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Body.png",
            ),
#        (0,0), ConditionSwitch(
#            #Water effect
#            "BetsyX.Water and BetsyX.ArmPose == 1", "images/BetsySprite/Betsy_Sprite_Water1.png",
#            "BetsyX.Water", "images/BetsySprite/Betsy_Sprite_Water2.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Chest layer under tits
            "BetsyX.Over == 'tshirt'", Null(),
            "BetsyX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "BetsyX.Chest == 'lace bra'", Recolor("Betsy", "Chest", "images/BetsyBJFace/Betsy_BJ_Chest_Lace_Up.png"),
                    "BetsyX.Chest == 'bra'", Recolor("Betsy", "Chest", "images/BetsyBJFace/Betsy_BJ_Chest_Bra_Up.png"),
                    "BetsyX.Chest == 'sports bra'", Recolor("Betsy", "Chest", "images/BetsyBJFace/Betsy_BJ_Chest_Sports_Up.png"),
                    "BetsyX.Chest == 'swimsuit'", Recolor("Betsy", "Chest", "images/BetsyBJFace/Betsy_BJ_Chest_Bikini_Up.png"),
                    # Modification mode
                    "BetsyX.Chest == 'cammy leotard'", "images/BetsyBJFace/modification/Betsy_BJ_Chest_Cammy_Up.png",
                    # ----------------
                    "True", Null(),
                    ),
            "BetsyX.Chest == 'lace bra'", Recolor("Betsy", "Chest", "images/BetsyBJFace/Betsy_BJ_Chest_Lace.png"),
            "BetsyX.Chest == 'sports bra'", Recolor("Betsy", "Chest", "images/BetsyBJFace/Betsy_BJ_Chest_Sports.png"),
            "BetsyX.Chest == 'bra'", Recolor("Betsy", "Chest", "images/BetsyBJFace/Betsy_BJ_Chest_Bra.png"),
            "BetsyX.Chest == 'swimsuit'", Recolor("Betsy", "Chest", "images/BetsyBJFace/Betsy_BJ_Chest_Bikini.png"),
            # Modification mode
            "BetsyX.Chest == 'cammy leotard'", "images/BetsyBJFace/modification/Betsy_BJ_Chest_Cammy.png",
            # ----------------
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over body layer
            "BetsyX.Over == 'jacket'", Recolor("Betsy", "Over", "images/BetsyBJFace/Betsy_BJ_Over_Jacket.png"),
            "BetsyX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "BetsyX.Over == 'tank'", Recolor("Betsy", "Over", "images/BetsyBJFace/Betsy_BJ_Over_Tank_Up.png"),
                    "BetsyX.Over == 'pink top'", Recolor("Betsy", "Over", "images/BetsyBJFace/Betsy_BJ_Over_Pink_Up.png"),
                    "True", Null(),
                    ),
            "BetsyX.Over == 'tank'", Recolor("Betsy", "Over", "images/BetsyBJFace/Betsy_BJ_Over_Tank.png"),
            "BetsyX.Over == 'pink top'", Recolor("Betsy", "Over", "images/BetsyBJFace/Betsy_BJ_Over_Pink.png"),
            "BetsyX.Over == 'towel'", Recolor("Betsy", "Over", "images/BetsyBJFace/Betsy_BJ_Over_Towel.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Piercings layer
            "not BetsyX.Pierce", Null(),
            "BetsyX.Pierce == 'ring'", ConditionSwitch(
                    #if it's the ring pericings
                    "BetsyX.Uptop", "images/BetsyBJFace/Betsy_BJ_Pierce_R.png",
                    "BetsyX.Over == 'tank'", "images/BetsyBJFace/Betsy_BJ_Pierce_R_Blue.png",
                    "BetsyX.Over == 'pink top' or BetsyX.Over == 'towel'", "images/BetsyBJFace/Betsy_BJ_Pierce_R_Pink.png",
                    "BetsyX.Chest == 'lace bra'", "images/BetsyBJFace/Betsy_BJ_Pierce_R_Lace.png",
                    # Modification mode
                    "BetsyX.Chest == 'cammy leotard'", "images/BetsyBJFace/modification/Betsy_BJ_Pierce_R_Cammy.png",
                    # -----------------
                    "BetsyX.Chest", "images/BetsyBJFace/Betsy_BJ_Pierce_R_Blue.png",
#                    "BetsyX.Chest == 'swimsuit'/'bra'/'sportsbra'", "images/BetsyBJFace/Betsy_BJ_Pierce_R_Blue.png",
                    "True", "images/BetsyBJFace/Betsy_BJ_Pierce_R.png",
                    ),
            "BetsyX.Uptop", "images/BetsyBJFace/Betsy_BJ_Pierce_B.png",
            "BetsyX.Over == 'tank'", "images/BetsyBJFace/Betsy_BJ_Pierce_B_Blue.png",
            "BetsyX.Over == 'pink top' or BetsyX.Over == 'towel'", "images/BetsyBJFace/Betsy_BJ_Pierce_B_Pink.png",
            "BetsyX.Chest == 'lace bra'", "images/BetsyBJFace/Betsy_BJ_Pierce_B_Lace.png",
            # Modification mode
            "BetsyX.Chest == 'cammy leotard'", "images/BetsyBJFace/modification/Betsy_BJ_Pierce_B_Cammy.png",
            # ----------------
            "BetsyX.Chest", "images/BetsyBJFace/Betsy_BJ_Pierce_B_Blue.png",
#            "BetsyX.Chest == 'swimsuit'", "images/BetsyBJFace/Betsy_BJ_Pierce_B_Blue.png",
            "True", "images/BetsyBJFace/Betsy_BJ_Pierce_B.png",
            ),
#        (0,0), ConditionSwitch(
#            # spunk over tits
#            "'tits' not in BetsyX.Spunk", Null(),
#            "BetsyX.Over == 'tshirt'", "images/BetsyBJFace/Betsy_TJ_Spunk_Clothed.png",
#            "not BetsyX.Uptop and BetsyX.Over", "images/BetsyBJFace/Betsy_TJ_Spunk_Clothed.png",
#            "True", "images/BetsyBJFace/Betsy_TJ_Spunk_Over.png",
#            ),
#        (0,0), "images/BetsyBJFace/Betsy_TJ_RefLine.png",
#        (-10,-90), "Betsy_Sprite_Head", #(75,-10)
        )
    transform_anchor True
    anchor (0.45, 0.35)#(0.6, 1.0)
    xoffset 50#30
    yoffset -530#-530
#    zoom .75  #.76
    rotate 0
# image Betsy_BJ_Backdrop # image Betsy_BJ_Backdrop # image Betsy_BJ_Backdrop End # image Betsy_BJ_Backdrop # image Betsy_BJ_Backdrop End

# image Betsy_BJ_Backdrop # image Betsy_BJ_Backdrop # image Betsy_BJ_Backdrop End # image Betsy_BJ_Backdrop # image Betsy_BJ_Backdrop End



image Betsy_BJ_Head:                                                                            #These are all the details of the face
    LiveComposite(
        (695,695),
        (-70,480), ConditionSwitch(
            "renpy.showing('Betsy_BJ_Animation') and Speed > 1",Null(),
#            "renpy.showing('Betsy_BJ_Animation') and (Speed == 3 or Speed == 4 or Speed == 6)",Null(),
            "True", "Betsy_BJ_Head_Under"
            ),

        (0,0), ConditionSwitch(
            # Basic Face layer
#            "BetsyX.Blush == 2 and renpy.showing('Betsy_BJ_Animation') and (Speed == 3 or Speed == 4 or Speed == 6)","images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Head_Over_Blush2.png",
#            "BetsyX.Blush and renpy.showing('Betsy_BJ_Animation') and (Speed == 3 or Speed == 4 or Speed == 6)","images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Head_Over_Blush1.png",
#            "renpy.showing('Betsy_BJ_Animation') and (Speed == 3 or Speed == 4 or Speed == 6)","images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Head_Over.png",
##            "True","images/BetsyBJFace/Betsy_BJ_Head_Sucking_Overlay.png",

            "BetsyX.Blush == 2", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Head_Over_Blush2.png",
            "BetsyX.Blush", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Head_Over_Blush1.png",
            "True", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Head_Over.png"

#            "BetsyX.Blush == 2", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Head_Blush2.png",
#            "BetsyX.Blush", "images/BetsyBJFace/Betsy_BJ_Head_Blush.png",
#            "True", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Head.png"
            ),

        (0,0), ConditionSwitch(
            #Mouth
            "Speed and renpy.showing('Betsy_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
                    "Speed == 1", Recolor("Betsy", "Lips", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Mouth_Tongue.png"),  #licking  Betsy_BJ_Mouth_TongueW
#                    "True", Null(),                          #heading
#                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
#                    "Speed == 3", Recolor("Betsy", "Lips", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Mouth_Sucking_Over.png"), #sucking
#                    "Speed == 4", Recolor("Betsy", "Lips", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Mouth_Sucking_Over.png"), #deepthroat
                    "True", Recolor("Betsy", "Lips", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Mouth_Sucking_Over.png"), #cumming
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #wet face
            "Player.Male", Null(),
            "'mouth' not in BetsyX.Spunk and 'chin' not in BetsyX.Spunk", Null(),
#            "'chin' not in BetsyX.Spunk and (BetsyX.Mouth == 'tongue' or Speed)", "images/BetsyBJFace/Betsy_BJ_Wet_Tongue.png",
#            "BetsyX.Mouth == 'tongue' or Speed", "images/BetsyBJFace/Betsy_BJ_Wet_Tongue2.png",
            "'mouth' in BetsyX.Spunk or 'chin' in BetsyX.Spunk", "images/BetsyBJFace/Betsy_BJ_Wet_Mouth.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Spunk layer
            "'mouth' not in BetsyX.Spunk or not Player.Male", Null(),
            "Speed and renpy.showing('Betsy_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
                    "Speed == 1", "images/BetsyBJFace/Betsy_BJ_Spunk_Open.png",  #licking
#                    "True", Null(),                          #heading
                    "(Speed == 2 or Speed == 5)", "images/BetsyBJFace/Betsy_BJ_Spunk_Heading.png",                          #heading
#                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", "images/BetsyBJFace/Betsy_BJ_Spunk_SuckingOver.png", #sucking
                    "Speed == 4", "images/BetsyBJFace/Betsy_BJ_Spunk_SuckingOver.png", #deepthroat
                    "Speed == 6", "images/BetsyBJFace/Betsy_BJ_Spunk_SuckingOver.png", #cumming
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Brows
            "BetsyX.Brows == 'angry'", "images/BetsyBJFace/Betsy_BJ_Brows_Angry.png",
            "BetsyX.Brows == 'sad'", "images/BetsyBJFace/Betsy_BJ_Brows_Sad.png",
            "BetsyX.Brows == 'surprised'", "images/BetsyBJFace/Betsy_BJ_Brows_Surprised.png",
            "BetsyX.Brows == 'confused'", "images/BetsyBJFace/Betsy_BJ_Brows_Surprised.png",
            "True", "images/BetsyBJFace/Betsy_BJ_Brows_Normal.png",
            ),
        (0,0),  "Betsy BJ Blink",
            #Eyes
        (0,0), ConditionSwitch(
            #Hair overlay
#            "BetsyX.Hair == 'wetlong' or (BetsyX.Hair == 'long' and BetsyX.Water)", "images/BetsyBJFace/Betsy_BJ_Hair_Long_Wet.png",
#            "BetsyX.Hair == 'long' and not Player.Male and 'facial' in BetsyX.Spunk","images/BetsyBJFace/Betsy_BJ_Hair_Long_Wet.png",
#            "BetsyX.Hair == 'long'", "images/BetsyBJFace/Betsy_BJ_Hair_Long.png",
            "BetsyX.Hair == 'blonde'", Recolor("Betsy", "Hair", "images/BetsyBJFace/Betsy_BJ_Hair_Blonde.png"),
            "BetsyX.Hair == 'wet' or BetsyX.Water", Recolor("Betsy", "Hair", "images/BetsyBJFace/Betsy_BJ_Hair_Short_Wet.png"),
            "not Player.Male and 'facial' in BetsyX.Spunk",Recolor("Betsy", "Hair", "images/BetsyBJFace/Betsy_BJ_Hair_Short_Wet.png"),
            "True", Recolor("Betsy", "Hair", "images/BetsyBJFace/Betsy_BJ_Hair_Short.png"),
            ),
        (0,0),  "images/BetsyBJFace/Betsy_BJ_Earring.png",
        # Modification mode
        (0,0), ConditionSwitch(
            "BetsyX.Hat == 'red beret'", "images/BetsyBJFace/modification/Betsy_BJ_Hat_Beret.png",
            "True",Null(),
            ),
        # ----------------
        (0,0), ConditionSwitch(
            # water overlay
            "BetsyX.Water", "images/BetsyBJFace/Betsy_BJ_Wet_Face.png",
            "not Player.Male and 'facial' in BetsyX.Spunk", "images/BetsyBJFace/Betsy_BJ_Wet_Face.png",
            "True",Null(),
            ),

#        (0,0), "Betsy_Tester",
        (0,0), ConditionSwitch(
            #cum on the face
            "'hair' in BetsyX.Spunk and Player.Male", "images/BetsyBJFace/Betsy_BJ_Spunk_Hair.png",
            "'facial' in BetsyX.Spunk and Player.Male", "images/BetsyBJFace/Betsy_BJ_Spunk_Facial.png",
            "True", Null(),
            ),
        (250,400), ConditionSwitch( #(250,400)(-500,-400)
            #steam
            "True", "Big_Steam",
            "BetsyX.Lust > 70", "Big_Steam",
            "True", Null(),
            ),
        )
    zoom 1
    anchor (0.5, 0.5)
    offset (70,-480)#(90,-480)

# image Betsy_BJ_Head End        # image Betsy_BJ_Head End        # image Betsy_BJ_Head End        # image Betsy_BJ_Head End

#image Betsy_Tester:
#            "images/BetsyBJFace/Betsy_BJ_tester.jpg"
#            alpha 0.5
image Betsy BJ Blink:
        #eyeblinks
        ConditionSwitch(
            "BetsyX.Eyes == 'normal'", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Eyes_Normal.png",
            "BetsyX.Eyes == 'sexy'", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Eyes_Sexy.png",
            "BetsyX.Eyes == 'closed'", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Eyes_Closed.png",
            "BetsyX.Eyes == 'surprised'", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Eyes_Surprised.png",
            "BetsyX.Eyes == 'side'", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Eyes_Side.png",
            "BetsyX.Eyes == 'leftside'", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Eyes_Side.png",
            "BetsyX.Eyes == 'stunned'", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Eyes_Stunned.png",
            "BetsyX.Eyes == 'down'", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Eyes_Down.png",
            "BetsyX.Eyes == 'manic'", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Eyes_Surprised.png",
            "BetsyX.Eyes == 'squint'", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Eyes_Sexy.png",
            "True", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Eyes_Normal.png",
            ),
        choice:
            3.5
        choice:
            3.25
        choice:
            3
        "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Eyes_Closed.png"
        .25
        repeat

image Betsy_BJ_HairBack:
    LiveComposite(
        (695,695),
        (0,0), ConditionSwitch(
            #Hair backside
            "BetsyX.Hair == 'blonde'", Recolor("Betsy", "Hair", "images/BetsyBJFace/Betsy_BJ_Hair_Blonde_Back.png"),
            "BetsyX.Hair == 'wetlong' or (BetsyX.Hair == 'long' and BetsyX.Water)", Recolor("Betsy", "Hair", "images/BetsyBJFace/Betsy_BJ_Hair_Long_Wet_Back.png"),
            "BetsyX.Hair == 'long' and not Player.Male and 'facial' in BetsyX.Spunk",Recolor("Betsy", "Hair", "images/BetsyBJFace/Betsy_BJ_Hair_Long_Wet_Back.png"),
            "BetsyX.Hair == 'long'", Recolor("Betsy", "Hair", "images/BetsyBJFace/Betsy_BJ_Hair_Long_Back.png"),
            "BetsyX.Hair == 'wet' or BetsyX.Water", Recolor("Betsy", "Hair", "images/BetsyBJFace/Betsy_BJ_Hair_Short_Wet_Back.png"),
            "not Player.Male and 'facial' in BetsyX.Spunk",Recolor("Betsy", "Hair", "images/BetsyBJFace/Betsy_BJ_Hair_Short_Wet_Back.png"),
            "True", Recolor("Betsy", "Hair", "images/BetsyBJFace/Betsy_BJ_Hair_Short_Back.png"),
            ),
        )
    zoom 1
    anchor (0.5, 0.5)
    offset (70,-480)

image Betsy_BJ_Head_Under:
    LiveComposite(
        (695,695),
#        (0,0), "images/BetsyBJFace/Betsy_BJ_Head_Sucking_Under.png",
        (0,0), ConditionSwitch(
            # Basic Face layer
            "BetsyX.Blush == 2", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Head_Blush2.png",
            "BetsyX.Blush", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Head_Blush1.png",
            "True", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Head.png"
            ),
#         (0,0), ConditionSwitch(
#            # Basic Face layer
#            "Speed and renpy.showing('Betsy_BJ_Animation') and Speed != 1 and Speed != 2 and Speed != 5","images/BetsyBJFace/Betsy_BJ_Head_Sucking_Overlay.png",
##            "True","images/BetsyBJFace/Betsy_BJ_Head_Sucking_Overlay.png",
#            "BetsyX.Blush == 2", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Head_Blush2.png",
#            "BetsyX.Blush", "images/BetsyBJFace/Betsy_BJ_Head_Blush.png",
#            "True", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Head.png"
#            ),

         (0,0), ConditionSwitch(
            #cum on the chin
            "'chin' in BetsyX.Spunk and Player.Male", "images/BetsyBJFace/Betsy_BJ_Spunk_Chin.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Mouth
#            "True", Null(), #cumming
            "Speed and renpy.showing('Betsy_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
                    "Speed == 1", Recolor("Betsy", "Lips", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Mouth_Tongue.png"),  #licking  Betsy_BJ_Mouth_TongueW
#                    "True", Null(),                          #heading
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", Recolor("Betsy", "Lips", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Mouth_Sucking.png"), #sucking
                    "Speed == 4", Recolor("Betsy", "Lips", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Mouth_Sucking.png"), #deepthroat
                    "Speed == 6", Recolor("Betsy", "Lips", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Mouth_Sucking.png"), #cumming
                    ),
            "renpy.showing('Betsy_CUN_Animation') and Speed", Recolor("Betsy", "Lips", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Mouth_Tongue.png"), #Betsy_BJ_Mouth_TongueW
            "Speed >= 3 and renpy.showing('Betsy_TJ_Animation')", Recolor("Betsy", "Lips", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Mouth_Tongue.png"), #Betsy_BJ_Mouth_TongueW
            "BetsyX.Mouth == 'normal'", Recolor("Betsy", "Lips", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Mouth_Normal.png"),
            "BetsyX.Mouth == 'lipbite'", Recolor("Betsy", "Lips", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Mouth_Normal.png"),
            "BetsyX.Mouth == 'sucking'", Recolor("Betsy", "Lips", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Mouth_Open.png"),
            "BetsyX.Mouth == 'kiss'", Recolor("Betsy", "Lips", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Mouth_Kiss.png"),
            "BetsyX.Mouth == 'sad'", Recolor("Betsy", "Lips", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Mouth_Sad.png"),
            "BetsyX.Mouth == 'smile'", Recolor("Betsy", "Lips", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Mouth_Smile.png"),
            "BetsyX.Mouth == 'smirk'", Recolor("Betsy", "Lips", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Mouth_Normal.png"),
            "BetsyX.Mouth == 'grimace'", Recolor("Betsy", "Lips", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Mouth_Smile.png"),
            "BetsyX.Mouth == 'surprised'", Recolor("Betsy", "Lips", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Mouth_Open.png"),
            "BetsyX.Mouth == 'tongue'", Recolor("Betsy", "Lips", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Mouth_Tongue.png"),
            "True", Recolor("Betsy", "Lips", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Mouth_Smile.png"),
            ),
        (0,0), ConditionSwitch(
            #Spunk layer
            "'mouth' not in BetsyX.Spunk or not Player.Male", Null(),
            "Speed and renpy.showing('Betsy_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
                    "Speed == 1", "images/BetsyBJFace/Betsy_BJ_Spunk_Open.png",  #licking
#                    "True", Null(),                          #heading
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", "images/BetsyBJFace/Betsy_BJ_Spunk_SuckingUnder.png", #sucking
                    "Speed == 4", "images/BetsyBJFace/Betsy_BJ_Spunk_SuckingUnder.png", #deepthroat
                    "Speed == 6", "images/BetsyBJFace/Betsy_BJ_Spunk_SuckingUnder.png", #cumming
                    ),
#            "BetsyX.Mouth == 'normal'", "images/BetsyBJFace/Betsy_BJ_Spunk_Smile.png",
#            "BetsyX.Mouth == 'lipbite'", "images/BetsyBJFace/Betsy_BJ_Spunk_Smile.png",
            "BetsyX.Mouth == 'kiss'", "images/BetsyBJFace/Betsy_BJ_Spunk_Sad.png",
            "BetsyX.Mouth == 'sad'", "images/BetsyBJFace/Betsy_BJ_Spunk_Sad.png",
#            "BetsyX.Mouth == 'smile'", "images/BetsyBJFace/Betsy_BJ_Spunk_Smile.png",
#            "BetsyX.Mouth == 'smirk'", "images/BetsyBJFace/Betsy_BJ_Spunk_Kiss.png",
            "BetsyX.Mouth == 'surprised'", "images/BetsyBJFace/Betsy_BJ_Spunk_Open.png",
            "BetsyX.Mouth == 'open'", "images/BetsyBJFace/Betsy_BJ_Spunk_Open.png",
            "BetsyX.Mouth == 'tongue'", "images/BetsyBJFace/Betsy_BJ_Spunk_Open.png",
            "BetsyX.Mouth == 'sucking'", "images/BetsyBJFace/Betsy_BJ_Spunk_Open.png",
            "True", "images/BetsyBJFace/Betsy_BJ_Spunk_Smirk.png",
            ),

#        (0,0), ConditionSwitch(
#            #cum on the chin
#            "'chin' in BetsyX.Spunk and Player.Male", "images/BetsyBJFace/Betsy_BJ_Spunk_Chin.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #Spunk layer
#            "'mouth' not in BetsyX.Spunk or not Player.Male", Null(),
#            "True", "images/BetsyBJFace/Betsy_BJ_Spunk_SuckingUnder.png",
#            ),
#        (0,0), Recolor("Betsy", "Lips", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Mouth_Open.png"),
        )
    zoom 1
    anchor (0.5, 0.5)
    offset (70,-480)#(90,-480)

image Betsy_BJ_Heading_Mouth:
    LiveComposite(
        (695,695),
        (0,0), Recolor("Betsy", "Lips", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_BJ_Mouth_Open.png"),
        (0,0), ConditionSwitch(
            #cum in mouth
            "'mouth' in BetsyX.Spunk and Player.Male", "images/BetsyBJFace/Betsy_BJ_Spunk_Open.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Hair overlay
#            "True", Recolor("Betsy", "Hair", "images/BetsyBJFace/Betsy_BJ_Hair_Short_Back.png"),
#            ),
        )
    zoom 1
    anchor (0.5, 0.5)
    offset (70,-480)


image Betsy_BJ_Anim0:
        #Static animation
        contains:
                # Betsy's hair back
                "Betsy_BJ_HairBack"
                subpixel True
                offset (10,90)     #top (350,190), - is up
                rotate 10
                parallel:
                    ease 1 offset (10,110)           #bottom
                    pause .2
                    ease 1.5 offset (10,90)     #top
                    repeat
                parallel:
                    ease 3 rotate -10          #bottom
                    pause 1
                    ease 3 rotate 10    #top
                    pause 1
                    repeat
        contains:
                #  Betsy's body, everything below the chin
                "Betsy_BJ_Backdrop"
                subpixel True
                offset (0,160)     #top
                alpha 1
                transform_anchor True
                rotate 0
                parallel:
                    ease 1 offset (0,170)           #bottom
                    pause .2
                    ease 1.5 offset (0,160)     #top
                    repeat
#                parallel:
#                    ease 1 rotate -10
#                    pause .2
#                    ease 1.5 rotate -5#-20
#                    repeat
        contains:
                # head overlay
                "Betsy_BJ_Head"
#                AlphaMask("Betsy_BJ_Head", "Betsy_BJ_MaskHeadingComposite") #"Betsy_BJ_MouthHeadingComposite")
                subpixel True
#                alpha .9
                offset (10,90)     #top (350,190), - is up
                rotate 10
                parallel:
                    ease 1 offset (10,110)           #bottom
                    pause .2
                    ease 1.5 offset (10,90)     #top
                    repeat
                parallel:
                    ease 3 rotate -10          #bottom
                    pause 1
                    ease 3 rotate 10    #top
                    pause 1
                    repeat
        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Betsy_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                rotate 0
                parallel:
                    pause 1
                    ease .2 rotate -.5
#                    pause .2
                    ease .3 rotate .5
                    ease .3 rotate 0
                    pause .9
                    repeat
#end Betsy_BJ_Anim0 Static

image Betsy_BJ_Anim1:
        #Licking animation
        contains:
                # Betsy's hair back
                "Betsy_BJ_HairBack"
                subpixel True
                offset (-25,65)     #top (350,190), - is up
                rotate -15
                parallel: #2.4 down, 1.8 up
                    ease 1 xoffset -30           #bottom
                    pause 1.4
                    ease .5 xoffset -10     #top    -40
#                    pause .2
                    ease 1.3 xoffset -25     #top
                    repeat
                parallel:
                    ease 1 yoffset 250           #bottom
                    ease .4 yoffset 240     #top     105
                    ease 1.0 yoffset 85     #top     105
                    ease .5 yoffset 65     #top     105
                    pause 1.3
                    repeat
                parallel:
                    easein .8 rotate -20          #bottom
                    pause .3
                    easein 0.8 rotate -15          #bottom
                    ease .5 rotate 20#0          #bottom
                    ease .8 rotate 0          #bottom
#                    pause .5
                    easeout 1 rotate -15    #top
                    repeat
        contains:
                #  Betsy's body, everything below the chin
                "Betsy_BJ_Backdrop"
                subpixel True
                offset (-45,120)     #top
                alpha 1
                transform_anchor True
                rotate -20
#                parallel: #2.4 down, 1.8 up
#                    ease 1 xoffset -60           #bottom
#                    pause 1.4
##                    ease 1 xoffset -40     #top
#                    ease .3 xoffset 20     #top
#                    pause .3
#                    ease 1.2 xoffset -45     #top
#                    repeat
                parallel:
                    ease .9 yoffset 280           #bottom
                    pause .6
                    ease 1.2 yoffset 110     #top
                    ease .9 yoffset 120     #top
                    ease .6 yoffset 105           #bottom
                    repeat
#                parallel:
#                    ease .9 rotate -30           #bottom
#                    pause .5
#                    ease 1.6 rotate -10     #top
#                    ease 1.2 rotate -15           #bottom
#                    repeat
        contains:
                # head overlay
                "Betsy_BJ_Head"
#                AlphaMask("Betsy_BJ_Head", "Betsy_BJ_MaskHeadingComposite") #"Betsy_BJ_MouthHeadingComposite")
                subpixel True
#                alpha .9
                offset (-25,65)     #top (350,190), - is up
                rotate -15
                parallel: #2.4 down, 1.8 up
                    ease 1 xoffset -30           #bottom
                    pause 1.4
                    ease .5 xoffset -10     #top    -40
#                    pause .2
                    ease 1.3 xoffset -25     #top
                    repeat
                parallel:
                    ease 1 yoffset 250           #bottom
                    ease .4 yoffset 240     #top     105
                    ease 1.0 yoffset 85     #top     105
                    ease .5 yoffset 65     #top     105
                    pause 1.3
                    repeat
                parallel:
                    easein .8 rotate -20          #bottom
                    pause .3
                    easein 0.8 rotate -15          #bottom
                    ease .5 rotate 20#0          #bottom
                    ease .8 rotate 0          #bottom
#                    pause .5
                    easeout 1 rotate -15    #top
                    repeat
        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Betsy_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                rotate 0
                parallel:
#                    pause 2.5
                    pause .3
                    ease .7 rotate -3
                    pause .5
                    ease .6 rotate 1           #bottom
                    pause .1
                    ease .2 rotate -2
                    ease .3 rotate 1
                    ease .2 rotate 0
                    pause 1.3
                    repeat
#end Betsy_BJ_Anim1 Licking


image Betsy_BJ_Anim2:
        #Heading animation
        contains:
                # Betsy's head hair back
                "Betsy_BJ_HairBack"
                subpixel True
                offset (-20,130)     #top (350,190), - is up
                rotate 0
                parallel:
                    ease 1 yoffset 180#400    #bottom
                    pause .4
                    ease 1 yoffset 130         #top
                    repeat
        contains:
                #  Betsy's body, everything below the chin
                "Betsy_BJ_Backdrop"
                subpixel True
                offset (-20,130)     #top
                alpha 1
                transform_anchor True
                rotate 0
#                parallel:
#                    ease .4 rotate -30
#                    pause .05
#                    ease .55 rotate -20#-20
#                    repeat
                parallel:
                    ease 1 yoffset 160#400    #bottom
                    pause .4
                    ease 1 yoffset 130         #top
                    repeat
        contains:
                # Betsy's head Underlay
                "Betsy_BJ_Head_Under"
                subpixel True
                offset (-20,130)     #top (350,190), - is up
                rotate 0
                parallel:
                    ease 1 yoffset 180#400    #bottom
                    pause .4
                    ease 1 yoffset 130         #top
                    repeat
#                parallel:
#                    ease .4 rotate 5          #bottom
#                    pause .1
#                    ease .5 rotate 0    #top
#                    repeat
        contains:
                # Betsy's open mouth
                "Betsy_BJ_Heading_Mouth"
                subpixel True
                transform_anchor True
                anchor (310,380)#(285,365)
                pos (-64,15) #(-64,13)
                offset (-10,130)     #top (-20,130), - is up
                rotate 0
                xzoom 1
                yzoom 1
                parallel:
                    ease 1 xzoom 1.8    #bottom
                    pause .4
                    ease 1 xzoom 1      #top
                    repeat
                parallel:
                    ease 1 yzoom 1.2    #bottom
                    pause .4
                    ease 1 yzoom 1      #top
                    repeat
                parallel:
                    ease 1 yoffset 190#400    #bottom
                    pause .4
                    ease 1 yoffset 140         #top
                    repeat
        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Betsy_TJ_ZeroCock"
                offset(0,0)
                transform_anchor True
                rotate -1
#                alpha .9
                parallel:
                    easeout .4 rotate 0    #bottom
                    pause 1.6
                    easein .4 rotate -1      #top
                    repeat
#                parallel:
#                    pause .1
#                    ease .3 yoffset 20
#                    ease .5 yoffset 0
#                    pause .1
#                    repeat
#        contains:
#                # mouth area overlay
#                "Betsy_BJ_Heading_Overlay"
##                AlphaMask("Betsy_BJ_Head", "Betsy_BJ_MaskHeadingComposite") #"Betsy_BJ_MouthHeadingComposite")
#                subpixel True
#                transform_anchor True
#                anchor (295,363)
#                pos (-50,15)
#                offset (-20,130)     #top (350,190), - is up
#                rotate 0
#                xzoom 1
#                yzoom 1
#                parallel:
#                    ease 1 xzoom 1.8    #bottom
#                    pause .1
#                    ease 1 xzoom 1      #top
#                    repeat
#                parallel:
#                    ease 1 yzoom 1.2    #bottom
#                    pause .1
#                    ease 1 yzoom 1      #top
#                    repeat
#                parallel:
#                    ease 1 yoffset 180#400    #bottom
#                    pause .1
#                    ease 1 yoffset 130         #top
#                    repeat
        contains:
                # head overlay
                "Betsy_BJ_Head"
#                AlphaMask("Betsy_BJ_Head", "Betsy_BJ_MaskHeadingComposite") #"Betsy_BJ_MouthHeadingComposite")
                subpixel True
                alpha 1
                offset (-20,130)     #top (350,190), - is up
                rotate 0
                parallel:
                    ease 1 yoffset 180#400    #bottom
                    pause .4
                    ease 1 yoffset 130         #top
                    repeat
#                parallel:
#                    ease .4 rotate 5          #bottom
#                    pause .1
#                    ease .5 rotate 0    #top
#                    repeat
#end Betsy_BJ_Anim2 Heading


image Betsy_BJ_Anim3:
        #sucking fast animation
        contains:
                # Betsy's head hair back
                "Betsy_BJ_HairBack"
                subpixel True
                offset (-20,180)     #top (350,190), - is up
                rotate 0
                parallel: #2.7 -> 1.0
                    ease .4 offset (-10,300)           #bottom
                    pause .05
                    ease .55 offset (-20,180)     #top
                    repeat #(-20,270)
                parallel:
                    ease .4 rotate 5          #bottom
                    pause .1
                    ease .5 rotate 0    #top
                    repeat
        contains:
                #  Betsy's body, everything below the chin
                "Betsy_BJ_Backdrop"
                subpixel True
                offset (-50,180)     #top (-20,180)
                alpha 1
                transform_anchor True
                rotate -20
#                parallel:
#                    ease .4 rotate -20
#                    pause .05
#                    ease .55 rotate -10#-20
#                    repeat
                parallel:
                    ease .35 yoffset 360#300           #bottom
                    pause .05
                    ease .6 yoffset 280     #top
                    repeat
        contains:
                # Betsy's head Underlay
                "Betsy_BJ_Head_Under"
                subpixel True
                offset (-20,180)     #top (350,190), - is up
                rotate 0
                parallel: #2.7 -> 1.0
                    ease .4 offset (-10,300)           #bottom
                    pause .05
                    ease .55 offset (-20,180)     #top
                    repeat #(-20,270)
                parallel:
                    ease .4 rotate 5          #bottom
                    pause .1
                    ease .5 rotate 0    #top
                    repeat
        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Betsy_TJ_ZeroCock"
                offset(0,0)
                transform_anchor True
                rotate 0
#                alpha 0.5
                parallel:
                    pause .1
                    ease .3 rotate 2
                    ease .4 rotate 0
                    pause .2
                    repeat
                parallel:
                    pause .1
                    ease .3 yoffset 20
                    ease .5 yoffset 0
                    pause .1
                    repeat
        contains:
                # head overlay
                "Betsy_BJ_Head"
#                AlphaMask("Betsy_BJ_Head", "Betsy_BJ_MaskHeadingComposite") #"Betsy_BJ_MouthHeadingComposite")
                subpixel True
#                alpha .9
                offset (-20,180)     #top (350,190), - is up
                rotate 0
                parallel: #2.7 -> 1.0
                    ease .4 offset (-10,300)           #bottom
                    pause .05
                    ease .55 offset (-20,180)     #top
                    repeat #(-20,270)
                parallel:
                    ease .4 rotate 5          #bottom
                    pause .1
                    ease .5 rotate 0    #top
                    repeat
##end Betsy_BJ_Anim3 Sucking

image Betsy_BJ_Anim4:
        #Deep animation
        contains:
                # Betsy's hair back
                "Betsy_BJ_HairBack"
                subpixel True
                offset (-20,180)     #top (350,190), - is up
                rotate 0
                parallel:
                    ease 1 offset (15,450)           #bottom
                    pause .2
                    ease 1.5 offset (-20,180)     #top
                    repeat #(-20,270)
                parallel:
                    ease 1 rotate 20          #bottom
                    pause .2
                    ease 1.5 rotate 0    #top
                    repeat
        contains:
                #  Betsy's body, everything below the chin
                "Betsy_BJ_Backdrop"
                subpixel True
                offset (-40,180)     #top  (-20,180)
                alpha 1
                transform_anchor True
                rotate -10
                parallel:
                    ease 1 rotate -20#-20
                    pause .2
                    ease 1.5 rotate -10#-10
                    repeat
                parallel:
                    ease 1 yoffset 500#550           #bottom
                    pause .2
                    ease 1.5 yoffset 180     #top  180
                    repeat
        contains:
                # Betsy's head Underlay
                "Betsy_BJ_Head_Under"
                subpixel True
                offset (-20,180)     #top (350,190), - is up
                rotate 0
                parallel:
                    ease 1 offset (15,450)           #bottom
                    pause .2
                    ease 1.5 offset (-20,180)     #top
                    repeat
                parallel:
                    ease 1 rotate 20          #bottom
                    pause .2
                    ease 1.5 rotate 0    #top
                    repeat
        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Betsy_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                rotate 0
                parallel:
                    pause .2
                    ease .8 rotate 15
                    pause .2
                    ease 1.2 rotate 0
                    pause .3
                    repeat
        contains:
                # head overlay
                "Betsy_BJ_Head"
#                AlphaMask("Betsy_BJ_Head", "Betsy_BJ_MaskHeadingComposite") #"Betsy_BJ_MouthHeadingComposite")
                subpixel True
#                alpha .9
                offset (-20,180)     #top (350,190), - is up
                rotate 0
                parallel: #2.7s
                    ease 1 offset (15,450)           #bottom
                    pause .2
                    ease 1.5 offset (-20,180)     #top
                    repeat #(-20,270)
                parallel:
                    ease 1 rotate 20          #bottom
                    pause .2
                    ease 1.5 rotate 0    #top
                    repeat
#end Betsy_BJ_Anim4 Deep


image Betsy_BJ_Anim5:
        #Cum high animation
        contains:
                # Betsy's hair back
                "Betsy_BJ_HairBack"
                subpixel True
                offset (10,140)     #top (-10,160)- is up
                rotate 30
                parallel:
                    ease 1 offset (-10,160)           #bottom
                    pause .2
                    ease .5 offset (10,140)     #top
                    repeat
                parallel:
                    ease 1 rotate 25          #bottom
                    pause .2
                    ease .5 rotate 30    #top
                    repeat
        contains:
                #  Betsy's body, everything below the chin
                "Betsy_BJ_Backdrop"
                subpixel True
                offset (-10,180)     #top
                alpha 1
                transform_anchor True
                rotate 0
                parallel:
                    ease 1 offset (-20,190)           #bottom
                    pause .2
                    ease .5 offset (-10,180)     #top
                    repeat
#                parallel:
#                    ease 1 rotate -5
#                    pause .2
#                    ease .5 rotate 0#-20
#                    repeat
        contains:
                # Betsy's head Underlay
                "Betsy_BJ_Head_Under"
                subpixel True
                offset (10,140)     #top (-10,160)- is up
                rotate 30
                parallel:
                    ease 1 offset (-10,160)           #bottom
                    pause .2
                    ease .5 offset (10,140)     #top
                    repeat
                parallel:
                    ease 1 rotate 25          #bottom
                    pause .2
                    ease .5 rotate 30    #top
                    repeat
        contains:
                # Betsy's open mouth
                "Betsy_BJ_Heading_Mouth"
                subpixel True
                transform_anchor True
                anchor (310,380)#(285,365)
                pos (-64,-15) #(-64,15)
                offset (25,160)     #top (350,190), - is up
                rotate 30
                xzoom 1
                yzoom 1
                parallel:
                    ease 1 xzoom 1.6    #bottom
                    pause .2
                    ease .5 xzoom 1      #top
                    repeat
                parallel:
                    ease 1 yzoom 1.2    #bottom
                    pause .2
                    ease .5 yzoom 1      #top
                    repeat
                parallel:
                    ease 1 offset (5,180)#(-30,180)           #bottom
                    pause .2
                    ease .5 offset (25,160)#(-10,160)     #top
                    repeat
                parallel:
                    ease 1 rotate 25          #bottom
                    pause .2
                    ease .5 rotate 30    #top
                    repeat
        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Betsy_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
#                alpha .9
                rotate 0
                parallel:
                    pause .2
                    ease .8 rotate -3
                    pause .2
                    ease .5 rotate 0
#                    pause .2
                    repeat
        contains:
                # head overlay
                "Betsy_BJ_Head"
#                AlphaMask("Betsy_BJ_Head", "Betsy_BJ_MaskHeadingComposite") #"Betsy_BJ_MouthHeadingComposite")
                subpixel True
                offset (10,140)     #top (350,190), - is up
                rotate 30
                parallel:
                    ease 1 offset (-10,160)           #bottom
                    pause .2
                    ease .5 offset (10,140)     #top
                    repeat
                parallel:
                    ease 1 rotate 25          #bottom
                    pause .2
                    ease .5 rotate 30    #top
                    repeat
#end Betsy_BJ_Anim5 Cum high


image Betsy_BJ_Anim6:
        #Cum Deep animation
        contains:
                # Betsy's hair back
                "Betsy_BJ_HairBack"
                subpixel True
                offset (15,430)     #top (350,190), - is up
                rotate 28
                parallel: #2s
                    ease 1.5 offset (10,450)           #bottom
                    pause .2
                    ease .3 offset (15,430)     #top
                    repeat #(-20,270)
                parallel:
                    ease 1.5 rotate 23          #bottom
                    pause .2
                    ease .3 rotate 28    #top
                    repeat
        contains:
                #  Betsy's body, everything below the chin
                "Betsy_BJ_Backdrop"
                subpixel True
                offset (-20,550)     #top
                alpha 1
                transform_anchor True
                rotate -10
                parallel:
                    ease 1.8 yoffset 530#410           #bottom
                    pause .2
                    ease 1.8 yoffset 550#430     #top
                    pause .2
                    repeat
        contains:
                # Betsy's head Underlay
                "Betsy_BJ_Head_Under"
                subpixel True
                offset (15,430)     #top (350,190), - is up
                rotate 28
                parallel: #2s
                    ease 1.5 offset (10,450)           #bottom
                    pause .2
                    ease .3 offset (15,430)     #top
                    repeat #(-20,270)
                parallel:
                    ease 1.5 rotate 23          #bottom
                    pause .2
                    ease .3 rotate 28    #top
                    repeat
        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Betsy_TJ_ZeroCock"
                offset (0,20) #top (0,30)
                transform_anchor True
                rotate 10
                parallel:
                    ease 1.5 rotate 12          #bottom
                    pause .2
                    ease .3 rotate 10    #top
                    repeat
                parallel:
                    ease 1.5 yoffset 0#400           #bottom
                    pause .2
                    ease .3  yoffset 10#180     #top
                    repeat
        contains:
                # head overlay
                "Betsy_BJ_Head"
#                AlphaMask("Betsy_BJ_Head", "Betsy_BJ_MaskHeadingComposite") #"Betsy_BJ_MouthHeadingComposite")
                subpixel True
#                alpha .9
                offset (15,430)     #top (350,190), - is up
                rotate 28
                parallel: #2s
                    ease 1.5 offset (10,450)           #bottom
                    pause .2
                    ease .3 offset (15,430)     #top
                    repeat #(-20,270)
                parallel:
                    ease 1.5 rotate 23          #bottom
                    pause .2
                    ease .3 rotate 28    #top
                    repeat
#end Betsy_BJ_Anim6 Cum Deep

##Head and Body Animations for Betsy's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
#                                                               #BJ Launchers
##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Betsy_BJ_Launch(Line = Trigger):    # The sequence to launch the Betsy BJ animations

##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    return
##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary

    if renpy.showing("Betsy_BJ_Animation") and BetsyX.Pose != "69":
        return
    elif renpy.showing("Betsy_69_Animation") and BetsyX.Pose == "69":
        return

    if not Player.Male:
        call Betsy_CUN_Launch
        return

    #". . ."
    $ Speed = 0
    $ Player.Sprite = 1

    if Line == "none":
        $ Player.Sprite = 0
    elif Line != "cum":
        $ Trigger = "blow"

#    show Betsy_BJ_Animation zorder 150:
#        pos (630,650) #(645,510)

    if renpy.showing("Betsy_TJ_Animation"):
            hide Betsy_TJ_Animation
    else:
            call Girl_Hide(BetsyX)
            if Line == "L" or Line == "cum":
                show Betsy_Sprite at SpriteLoc(StageCenter) zorder 150:
                    alpha 1
                    ease 1 zoom 2.5 offset (150,80)
                with dissolve
            else:
                show Betsy_Sprite at SpriteLoc(StageCenter) zorder 150:
                    alpha 1 zoom 2.5 offset (150,80)
                with dissolve
            hide Betsy_Sprite

    $ Player.Cock = 0
    if BetsyX.Pose == "69":
            show Betsy_69_Animation zorder 150
    else:
            show Betsy_BJ_Animation zorder 150:
                pos (1000,1050)#(1000,1000)#(700,520)


    if Taboo and Line == "L": # Betsy gets started. . .
            if len(Present) >= 2:
                if Present[0] != BetsyX:
                        "[BetsyX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                elif Present[1] != BetsyX:
                        "[BetsyX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
            else:
                        "[BetsyX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
            "Затем она наклоняется и берет ваш член в свой рот."
    elif Line == "L":
            "[BetsyX.Name] плавно наклоняется и прислоняет ваш член к своей щеке."

    return

label Betsy_BJ_Reset: # The sequence to the Betsy animations from BJ to default
    if Player.Male != 1:
            call Betsy_CUN_Reset
    if not renpy.showing("Betsy_BJ_Animation") and not renpy.showing("Betsy_69_Animation"):
        return
#    hide Betsy_BJ_Animation
    call Girl_Hide(BetsyX)
    $ Speed = 0

    show Betsy_Sprite at SpriteLoc(StageCenter) zorder 150:
        alpha 1 zoom 2.5 offset (150,80)
    with dissolve

    show Betsy_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .2
        ease .3 zoom 1 offset (0,0)
    pause 1.5
    show Betsy_Sprite at SpriteLoc(BetsyX.SpriteLoc) zorder BetsyX.Layer:
        alpha 1 zoom 1 offset (0,0)
    return

# End Betsy Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Betsy's TJ animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Animation components / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# start base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Betsy_TJ_Animation:
            #core TJ animation
            contains:
                ConditionSwitch(
                    # Betsy's upper body
                    "not Player.Sprite","Betsy_TJ_0",#Static
                    "Speed == 1", "Betsy_TJ_1",#slow
                    "Speed == 3", "Betsy_TJ_3",#licking
                    "Speed == 4", "Betsy_TJ_0",#cumming high
                    "Speed == 5", "Betsy_TJ_5",#cumming low
                    "Speed >= 2", "Betsy_TJ_2",#fast
                    "True",       "Betsy_TJ_0",#Static
                    )
            zoom .8 #.7
            transform_anchor True
            anchor (.5,.5)
# end base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#image Betsy_TJ_Head:
#            #Hair underlay
#            "Betsy_BJ_Head"
#            transform_anchor True
#            zoom .7
#            anchor (0.5, 0.5)
#            offset (30,-450)
#            rotate 0


image Betsy_TJ_ZeroCock:
            #cock used in Betsy's sex pose
            "Zero_Blowcock"
            transform_anchor True
            zoom .6
            anchor (0.5, 0.6)
            offset (0,50)#(5,50)
            rotate 0


image Betsy_TJ_Body:
    LiveComposite(
        (800,950),       #550,950
#        (-10,-90), "Betsy_BJ_HairBack", #(75,-10)

        (0,0), ConditionSwitch(
            #Body
            # Modification mode
            "BetsyX.Arms == 'cammy gloves'", "images/BetsyBJFace/modification/[BetsyX.skin_image.skin_path]Betsy_TJ_Body_Cammy.png",
            # -----------------
            "BetsyX.Arms", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_TJ_Body_G.png",
            "True", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_TJ_Body.png",
            ),
#        (0,0), ConditionSwitch(
#            #Water effect
#            "BetsyX.Water and BetsyX.ArmPose == 1", "images/BetsyBJFace/Betsy_Sprite_Water1.png",
#            "BetsyX.Water", "images/BetsyBJFace/Betsy_Sprite_Water2.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            # under tit
##            "BetsyX.Water", "images/BetsyBJFace/Betsy_Sprite_Water2.png",
#            "True", "images/BetsyBJFace/Betsy_TJ_Tit_Under.png",
#            ),
#        (0,0), "images/BetsyBJFace/Betsy_TJ_RefCock.png",

#        (0,0), ConditionSwitch(
#            # under tit smoosh
#            "BetsyX.Water", Null(),
#            "True", "images/BetsyBJFace/Betsy_TJ_Tit_Under_Smoosh.png",
#            ),
#        (0,0), ConditionSwitch(
#            # over tit
##            "BetsyX.Water", "images/BetsySprite/Betsy_Sprite_Water2.png",
#            "True", "images/BetsyBJFace/Betsy_TJ_Tit_Over.png",
#            ),

        (0,0), ConditionSwitch(
            #Chest layer under tits
#            "BetsyX.Over == 'tshirt'", Null(),
            "BetsyX.Chest == 'lace bra'", Recolor("Betsy", "Chest", "images/BetsyBJFace/Betsy_TJ_Chest_Lace_Under.png"),
            "BetsyX.Chest == 'sports bra'", Recolor("Betsy", "Chest", "images/BetsyBJFace/Betsy_TJ_Chest_Sports_Under.png"),
            "BetsyX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "BetsyX.Chest == 'swimsuit'", Recolor("Betsy", "Chest", "images/BetsyBJFace/Betsy_TJ_Chest_Bikini_Up_Under.png"),
                    # Modification mode
                    "BetsyX.Chest == 'cammy leotard'", "images/BetsyBJFace/modification/Betsy_TJ_Chest_Cammy_Up_Under.png",
                    # -----------------
                    "True", Null(),
                    ),
            "BetsyX.Chest == 'swimsuit' and Player.Sprite", Recolor("Betsy", "Chest", "images/BetsyBJFace/Betsy_TJ_Chest_Bikini_Up_Under.png"),
            "BetsyX.Chest == 'swimsuit'", Recolor("Betsy", "Chest", "images/BetsyBJFace/Betsy_TJ_Chest_Bikini_Under.png"),
            # Modification mode
            "BetsyX.Chest == 'cammy leotard' and Player.Sprite", "images/BetsyBJFace/modification/Betsy_TJ_Chest_Cammy_Up_Under.png",
            "BetsyX.Chest == 'cammy leotard'", "images/BetsyBJFace/modification/Betsy_TJ_Chest_Cammy_Under.png",
            # ----------------
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over body layer
            "BetsyX.Over == 'jacket'", Recolor("Betsy", "Over", "images/BetsyBJFace/Betsy_TJ_Over_Jacket_Under.png"),
            "BetsyX.Over == 'tank'", Recolor("Betsy", "Over", "images/BetsyBJFace/Betsy_TJ_Over_Tank_Under.png"),
            "BetsyX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "BetsyX.Over == 'pink top'", Recolor("Betsy", "Over", "images/BetsyBJFace/Betsy_TJ_Over_Pink_Up_Under.png"),
                    "True", Null(),
                    ),
            "BetsyX.Over == 'pink top'", Recolor("Betsy", "Over", "images/BetsyBJFace/Betsy_TJ_Over_Pink_Under.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # spunk under tits
            "'tits' not in BetsyX.Spunk", Null(),
            "True", "images/BetsyBJFace/Betsy_TJ_Spunk_Under.png",
            ),


#        (0,0), ConditionSwitch(
#            #hands layer
#            "BetsyX.Arms and (BetsyX.Over == 'suit' or BetsyX.Over == 'open suit')", "images/BetsyBJFace/Betsy_TJ_Hands_Gloved.png",
#            "True", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_TJ_Hands.png",
#            ),

#        (0,0), ConditionSwitch(
#            #breast spunk
#            "'tits' in BetsyX.Spunk and Player.Male", "images/BetsySprite/Betsy_Sprite_Spunk_Tits.png",
#            "True", Null(),
#            ),

#        (-10,-90), "Betsy_Sprite_Head", #(75,-10)



        )
    transform_anchor True
    anchor (0.6, 1.0)#(0.6, 0.0)
    xoffset 105#155
    yoffset 125#125
#    alpha .5
#    zoom .75  #.76
    rotate 0

#    transform_anchor True
#    zoom 1
#    anchor (0.4, 1.0)
#    #offset (410,770) # (300,275)
#    rotate 0


image Betsy_TJ_Tits_Under:
    LiveComposite(
        (800,950),       #550,950
        (0,0), ConditionSwitch(
            # under tit
#            "BetsyX.Water", "images/BetsySprite/Betsy_Sprite_Water2.png",
            "True", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_TJ_Tits_Under.png",
            ),
#        (0,0), ConditionSwitch(
#            #Chest tits layer
#            "BetsyX.Uptop", Null(),
#            "BetsyX.Over == 'tshirt'", Null(),
#            "BetsyX.Chest == 'tank'", "images/BetsyBJFace/Betsy_TJ_Chest_Tank_Body_Fucking.png",
##            "BetsyX.Chest == 'swimsuit'", Recolor("Betsy", "Chest", "images/BetsyBJFace/Betsy_TJ_Chest_Bikini_Tits.png"),
#            "True", Null(),
#            ),
        )
    transform_anchor True
#    anchor (0.6, 1.0)#(0.6, 0.0)
#    xoffset 155#300
#    yoffset 125#-600
##    zoom .75  #.76
    rotate 0


image Betsy_TJ_Tits_Over:
    LiveComposite(
        (800,950),    #800,950
#        (0,0), ConditionSwitch(
#            # under tit smoosh
#            "BetsyX.Water", Null(),
#            "True", "images/BetsyBJFace/Betsy_TJ_Tit_Under_Smoosh.png",
#            ),
#        (0,0), ConditionSwitch(
#            # over tit
#            "Player.Sprite and renpy.showing('Betsy_TJ_Animation')", "images/BetsyBJFace/Betsy_TJ_Tit_Over_Smoosh.png",
#            "True", "images/BetsyBJFace/Betsy_TJ_Tit_Over.png",
#            ),

#        (0,0),  "images/BetsyBJFace/Betsy_TJ_Tit_Right_Mask.png",
        (0,0),  "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_TJ_Tits_Over.png",
        (0,0), ConditionSwitch(
            # spunk under tits
            "'tits' not in BetsyX.Spunk", Null(),
            "True", "images/BetsyBJFace/Betsy_TJ_Spunk_Over_Nude.png",
            ),
        (0,0), ConditionSwitch(
            #Chest tits layer
            "BetsyX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "BetsyX.Chest == 'lace bra'", Recolor("Betsy", "Chest", "images/BetsyBJFace/Betsy_TJ_Chest_Lace_Up_Tits.png"),
                    "BetsyX.Chest == 'bra'", Recolor("Betsy", "Chest", "images/BetsyBJFace/Betsy_TJ_Chest_Blue_Up_Tits.png"),
                    "BetsyX.Chest == 'sports bra'", Recolor("Betsy", "Chest", "images/BetsyBJFace/Betsy_TJ_Chest_Sports_Up_Tits.png"),
                    "True", Null(),
                    ),
            "BetsyX.Chest == 'lace bra'", Recolor("Betsy", "Chest", "images/BetsyBJFace/Betsy_TJ_Chest_Lace_Tits.png"),
            "BetsyX.Chest == 'bra'", Recolor("Betsy", "Chest", "images/BetsyBJFace/Betsy_TJ_Chest_Blue_Tits.png"),
            "BetsyX.Chest == 'sports bra'", Recolor("Betsy", "Chest", "images/BetsyBJFace/Betsy_TJ_Chest_Sports_Tits.png"),
            "BetsyX.Chest == 'swimsuit' and Player.Sprite and renpy.showing('Betsy_TJ_Animation')", Null(),
            "BetsyX.Chest == 'swimsuit'", Recolor("Betsy", "Chest", "images/BetsyBJFace/Betsy_TJ_Chest_Bikini_Tits.png"),
            # Modification mode
            "BetsyX.Chest == 'cammy leotard'", "images/BetsyBJFace/modification/Betsy_TJ_Chest_Cammy_Tits.png",
            # ----------------
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Over tits layer
            "BetsyX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "BetsyX.Over == 'tank'", Recolor("Betsy", "Over", "images/BetsyBJFace/Betsy_TJ_Over_Tank_Up_Tits.png"),
                    "BetsyX.Over == 'pink top'", Recolor("Betsy", "Over", "images/BetsyBJFace/Betsy_TJ_Over_Pink_Up_Tits.png"),
                    "True", Null(),
                    ),
            "BetsyX.Over == 'tank'", Recolor("Betsy", "Over", "images/BetsyBJFace/Betsy_TJ_Over_Tank_Tits.png"),
            "BetsyX.Over == 'pink top'", Recolor("Betsy", "Over", "images/BetsyBJFace/Betsy_TJ_Over_Pink_Tits.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Piercings layer
            "not BetsyX.Pierce", Null(),
            "BetsyX.Pierce == 'ring'", ConditionSwitch(
                    #if it's the ring pericings
                    "BetsyX.Uptop", "images/BetsyBJFace/Betsy_TJ_Pierce_R_Left.png",

                    "BetsyX.Over == 'tank'", "images/BetsyBJFace/Betsy_TJ_Pierce_R_Left_Blue.png",
                    "BetsyX.Over == 'pink top'", "images/BetsyBJFace/Betsy_TJ_Pierce_R_Left_Pink.png",

                    "BetsyX.Chest == 'lace bra'", "images/BetsyBJFace/Betsy_TJ_Pierce_R_Left_Lace.png",
                    "BetsyX.Chest == 'swimsuit' and Player.Sprite", "images/BetsyBJFace/Betsy_TJ_Pierce_R_Left.png",
                    # Modification mode
                    "BetsyX.Chest == 'cammy leotard'", "images/BetsyBJFace/modification/Betsy_TJ_Pierce_R_Left_Cammy.png",
                    # ----------------
                    "BetsyX.Chest", "images/BetsyBJFace/Betsy_TJ_Pierce_R_Left_Blue.png",
#                    "BetsyX.Chest == 'swimsuit'", "images/BetsyBJFace/Betsy_TJ_Pierce_R_Left_Blue.png",

                    "True", "images/BetsyBJFace/Betsy_TJ_Pierce_R_Left.png",
                    ),
            "BetsyX.Uptop", "images/BetsyBJFace/Betsy_TJ_Pierce_B_Left.png",

            "BetsyX.Over == 'tank'", "images/BetsyBJFace/Betsy_TJ_Pierce_B_Left_Blue.png",
            "BetsyX.Over == 'pink top'", "images/BetsyBJFace/Betsy_TJ_Pierce_B_Left_Pink.png",

            "BetsyX.Chest == 'lace bra'", "images/BetsyBJFace/Betsy_TJ_Pierce_B_Left_Lace.png",
            "BetsyX.Chest == 'swimsuit' and Player.Sprite", "images/BetsyBJFace/Betsy_TJ_Pierce_B_Left.png",
            # Modification mode
            "BetsyX.Chest == 'cammy leotard'", "images/BetsyBJFace/modification/Betsy_TJ_Pierce_B_Left_Cammy.png",
            # ----------------
            "BetsyX.Chest", "images/BetsyBJFace/Betsy_TJ_Pierce_B_Left_Blue.png",
#            "BetsyX.Chest == 'swimsuit'", "images/BetsyBJFace/Betsy_TJ_Pierce_B_Left_Blue.png",

            "True", "images/BetsyBJFace/Betsy_TJ_Pierce_B_Left.png",
            ),
        (0,0), ConditionSwitch(
            # spunk under tits
            "'tits' not in BetsyX.Spunk", Null(),
            "BetsyX.Over in ('tank','pink top')", "images/BetsyBJFace/Betsy_TJ_Spunk_Over_Clothed.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            # spunk over tits
#            "'tits' not in BetsyX.Spunk", Null(),
##            "BetsyX.Over == 'tshirt'", "images/BetsyBJFace/Betsy_TJ_Spunk_Clothed.png",
#            "not BetsyX.Uptop and BetsyX.Over", "images/BetsyBJFace/Betsy_TJ_Spunk_Clothed.png",
#            "True", "images/BetsyBJFace/Betsy_TJ_Spunk_Over.png",
#            ),
#        (0,0), "images/BetsyBJFace/Betsy_TJ_RefLine.png",
#        (0,0), "images/BetsyBJFace/Betsy_TJ_RefLine2.png",
        )
    transform_anchor True
#    anchor (0.6, 1.0)#(0.6, 562)
#    xoffset 155#300
#    yoffset 325#125
#    yoffset -925#-625#-325
#    zoom .75  #.76
    rotate 0

image Betsy_TJ_Hands:
    LiveComposite(
        (800,950),       #550,950
        (0,0), ConditionSwitch(
            #right hand layer
            # Modification mode
            "BetsyX.Arms == 'cammy gloves'", "images/BetsyBJFace/modification/[BetsyX.skin_image.skin_path]Betsy_TJ_Hands_Cammy.png",
            # -----------------
            "BetsyX.Arms", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_TJ_Hands_G.png",
            "True", "images/BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_TJ_Hands.png",
            ),
        (0,0), ConditionSwitch(
            #nips
            "BetsyX.Uptop", "images/BetsyBJFace/Betsy_TJ_Nip.png",

            "BetsyX.Over == 'tank'", "images/BetsyBJFace/Betsy_TJ_Nip_Blue.png",
            "BetsyX.Over == 'pink top'", "images/BetsyBJFace/Betsy_TJ_Nip_Pink.png",

            "BetsyX.Chest == 'lace bra'", "images/BetsyBJFace/Betsy_TJ_Nip_Lace.png",
            "BetsyX.Chest == 'swimsuit' and Player.Sprite", "images/BetsyBJFace/Betsy_TJ_Nip.png",
            "BetsyX.Chest", "images/BetsyBJFace/Betsy_TJ_Nip_Blue.png",
#            "BetsyX.Chest == 'swimsuit'", "images/BetsyBJFace/Betsy_TJ_Nip_Blue.png",

            "True", "images/BetsyBJFace/Betsy_TJ_Nip.png",
            ),
        (0,0), ConditionSwitch(
            #Piercings layer
            "not BetsyX.Pierce", Null(),
            "BetsyX.Pierce == 'ring' and (BetsyX.Uptop or (not BetsyX.Over and not BetsyX.Chest))", "images/BetsyBJFace/Betsy_TJ_Pierce_R_Right.png",
            "BetsyX.Pierce == 'ring' and BetsyX.Chest == 'swimsuit' and Player.Sprite", "images/BetsyBJFace/Betsy_TJ_Pierce_R_Right.png",

            "BetsyX.Uptop", "images/BetsyBJFace/Betsy_TJ_Pierce_B_Right.png",

            "BetsyX.Over == 'tank'", "images/BetsyBJFace/Betsy_TJ_Pierce_B_Right_Blue.png",
            "BetsyX.Over == 'pink top'", "images/BetsyBJFace/Betsy_TJ_Pierce_B_Right_Pink.png",

            "BetsyX.Chest == 'lace bra'", "images/BetsyBJFace/Betsy_TJ_Pierce_B_Right_Lace.png",
            "BetsyX.Chest == 'swimsuit' and Player.Sprite", "images/BetsyBJFace/Betsy_TJ_Pierce_B_Right.png",
            # Modification mode
            "BetsyX.Chest == 'cammy leotard'", "images/BetsyBJFace/modification/Betsy_TJ_Pierce_B_Right_Cammy.png",
            # ----------------
            "BetsyX.Chest", "images/BetsyBJFace/Betsy_TJ_Pierce_B_Right_Blue.png",
#            "BetsyX.Chest == 'swimsuit'", "images/BetsyBJFace/Betsy_TJ_Pierce_B_Right_Blue.png",

            "True", "images/BetsyBJFace/Betsy_TJ_Pierce_B_Right.png",
            ),
        (0,0), ConditionSwitch(
            #right hand layer
            "BetsyX.Over == 'pink top'", Recolor("Betsy", "Over", "images/BetsyBJFace/Betsy_TJ_Arms_Pink.png"),
            "True", Null(),
            ),
        )
    transform_anchor True
#    anchor (0.6, 1.0)#(0.6, 0.0)
#    xoffset 155#300
#    yoffset 125#-600
#    zoom .75  #.76
    rotate 0

#image Betsy_TJ_Braback:
#            #back fo the bra straps
#            contains:
#                ConditionSwitch(
#                        #"BetsyX.Chest == 'corset' and not BetsyX.Uptop","images/BetsyBJFace/Betsy_TJ_Chest_Corset.png",
##                        "BetsyX.Over",Null(),
#                        "BetsyX.Chest == 'sports bra'","images/BetsyBJFace/Betsy_TJ_Chest_Sports_Back.png",
##                        "BetsyX.Chest == 'lace bra'","images/BetsyBJFace/Betsy_TJ_Chest_Lace_Back.png",
#                        "BetsyX.Chest == 'swimsuit' and BetsyX.Uptop","images/BetsyBJFace/Betsy_TJ_Chest_Bikini_Up_Back.png",
#                        "BetsyX.Chest == 'swimsuit'","images/BetsyBJFace/Betsy_TJ_Chest_Bikini_Back.png",
#                        "True", Null(),
#                        )
#            transform_anchor True
#            zoom 1
#            anchor (0.4, 1.0)
#            #offset (410,770) # (300,275)
#            rotate 0

image Betsy_TJ_BraStretch:
            #bra streching effect
            contains:
                ConditionSwitch(
                    #Over tits layer
                    "BetsyX.Over == 'tank'", "images/BetsyBJFace/Betsy_TJ_Tent_Blue.png",
                    "True", Null(),
                    )
#            contains:
#                    "images/BetsyBJFace/Betsy_TJ_RefLine2.png"
            transform_anchor True
#            zoom 1
#            offset (50,0) # (300,275)
#            anchor (.1,.1)#(0.1, .2)
#            alpha 0.7
            rotate 0

#image Betsy_TJ_Tits:
#            #layer with left tit and all clothing
#            contains:
#                "images/BetsyBJFace/Betsy_TJ_Tits.png"
##            contains:
##                ConditionSwitch(
##                        "not BetsyX.Water",Null(),
##                        "True",       "images/BetsyBJFace/Betsy_TJ_Tits_Wet.png",
##                        )
#            contains:
#                #Chest
#                ConditionSwitch(
#                        "BetsyX.Chest == 'lace bra' and BetsyX.Uptop","images/BetsyBJFace/Betsy_TJ_Chest_Lace_Up.png",  #fix, add "no straps" version here
#                        "BetsyX.Chest == 'lace bra'","images/BetsyBJFace/Betsy_TJ_Chest_Lace.png",
#                        "BetsyX.Chest == 'sports bra'","images/BetsyBJFace/Betsy_TJ_Chest_Sports.png",
#                        "BetsyX.Chest == 'swimsuit' and BetsyX.Uptop","images/BetsyBJFace/Betsy_TJ_Chest_Bikini_Up.png",
#                        "BetsyX.Chest == 'swimsuit'","images/BetsyBJFace/Betsy_TJ_Chest_Bikini.png",
#                        "True", Null(),
#                        )
#            contains:
#                #Over
#                ConditionSwitch(
#                        "BetsyX.Over == 'tube top' and BetsyX.Uptop","images/BetsyBJFace/Betsy_TJ_Over_Tube_Up.png",
#                        "BetsyX.Over == 'tube top'","images/BetsyBJFace/Betsy_TJ_Over_Tube.png",
#                        "True", Null(),
#                        )
#            contains:
#                #Piercings clothing
#                ConditionSwitch(
#                        "not BetsyX.Pierce", Null(),
#                        "BetsyX.Pierce == 'ring'", ConditionSwitch(
#                                #if she's got ring piercings
#                                "BetsyX.Uptop", "images/BetsyBJFace/Betsy_TJ_Pierce_Ring.png",
#                                "BetsyX.Over == 'tube top'", "images/BetsyBJFace/Betsy_TJ_Pierce_Ring_Pink.png",
#                                "BetsyX.Chest == 'swimsuit'", "images/BetsyBJFace/Betsy_TJ_Pierce_Ring_Pink.png",
#                                "BetsyX.Chest == 'lace bra'", "images/BetsyBJFace/Betsy_TJ_Pierce_Ring_Lace.png",
#                                "True", "images/BetsyBJFace/Betsy_TJ_Pierce_Ring.png",
#                                ),
#                        "BetsyX.Uptop", "images/BetsyBJFace/Betsy_TJ_Pierce_Barbell.png",
#                        "BetsyX.Over == 'tube top'", "images/BetsyBJFace/Betsy_TJ_Pierce_Barbell_Pink.png",
#                        "BetsyX.Chest == 'swimsuit'", "images/BetsyBJFace/Betsy_TJ_Pierce_Barbell_Pink.png",
#                        "BetsyX.Chest == 'lace bra'", "images/BetsyBJFace/Betsy_TJ_Pierce_Barbell_Lace.png",
#                        "True", "images/BetsyBJFace/Betsy_TJ_Pierce_Barbell.png",
#                        )
#            contains:
#                #Over
#                ConditionSwitch(
#                        "'tits' in BetsyX.Spunk and Player.Male","images/BetsyBJFace/Betsy_TJ_Spunk_Tits_Over.png",
#                        "True", Null(),
#                        )
#            transform_anchor True
#            zoom 1
#            anchor (0.4, 1.0)
#            #offset (410,770) # (300,275)
#            rotate 0


## Animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start 0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Betsy_TJ_0:
        #Her Body in the TJ pose, static
        contains:
                #hair back
                "Betsy_BJ_HairBack"
                subpixel True
#                offset (90,-480)
                pos (-70,0) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos 30
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
                parallel:
                    pause .1
                    ease 2 rotate 10
                    pause .3
                    ease 2 rotate 0
                    pause .3
                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "Betsy_TJ_Body"
                subpixel True
#                anchor (0.6, 1.0)#(0.6, 0.0)
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos 30
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
        contains:
                #head
                "Betsy_BJ_Head"
                subpixel True
#                offset (90,-480)
                pos (-70,0) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos 30
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
                parallel:
                    pause .1
                    ease 2 rotate 10
                    pause .3
                    ease 2 rotate 0
                    pause .3
                    repeat
        contains:
                #underside tit
                "Betsy_TJ_Tits_Under"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 150#200
                yoffset -271#125
                parallel:
                    ease 2 ypos 30
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
                parallel:
                    pause .1
                    ease .8 yzoom .95
                    pause 1.2
                    ease 1.2 yzoom 1
                    pause .8
                    ease 0.6 yzoom .98
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Betsy_TJ_ZeroCock"
#                ConditionSwitch(
#                            "Player.Sprite","Betsy_TJ_ZeroCock",
#                            "True",  Null(),
#                            )
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (0,50)#(5,50)
        contains:
                #bra stretch
                "Betsy_TJ_BraStretch"
                subpixel True
                pos (0,0) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 818)#(0.6, 700)
                xoffset 270#315
                yoffset -245#-265
                yzoom .2
                parallel:
                    ease 2 ypos 30
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
                parallel:
                    pause .2
                    ease 1.8 yzoom .4
                    pause .3
                    ease 2 yzoom .2
                    pause .4
                    repeat
        contains:
                #overside tit
                "Betsy_TJ_Tits_Over"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 150#200
                yoffset -271#125
                yzoom 1
                parallel:
                    ease 2 ypos 30
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
                parallel:
                    pause .1
                    ease .8 yzoom .95
                    pause 1.2
                    ease 1.2 yzoom 1
                    pause .8
                    ease 0.6 yzoom .98
                    repeat
        contains:
                #hands over everything
                "Betsy_TJ_Hands"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 150#200
                yoffset -271#125
                parallel:
                    ease 2 ypos 30
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat


# End Betsy TJ Pose 0 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



## Start 1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Betsy_TJ_1:
        #Her Body in the TJ pose, slow
        contains:
                #hair back
                "Betsy_BJ_HairBack"
                subpixel True
#                offset (90,-480)
                pos (-70,0) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos 120
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
                parallel:
                    pause .1
                    ease 2 rotate 10
                    pause .3
                    ease 2 rotate 0
                    pause .3
                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "Betsy_TJ_Body"
                subpixel True
#                anchor (0.6, 1.0)#(0.6, 0.0)
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos 120
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
        contains:
                #head
                "Betsy_BJ_Head"
                subpixel True
#                offset (90,-480)
                pos (-70,0) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos 120
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
                parallel:
                    pause .1
                    ease 2 rotate 10
                    pause .3
                    ease 2 rotate 0
                    pause .3
                    repeat
        contains:
                #underside tit
                "Betsy_TJ_Tits_Under"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 150#200
                yoffset -271#125
                parallel:
                    ease 2 ypos 120
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
                parallel:
                    pause .1
                    ease .8 yzoom .90
                    pause 1.2
                    ease 1.2 yzoom 1
                    pause .8
                    ease 0.6 yzoom .98
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Betsy_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (0,50)#(5,50)
        contains:
                #bra stretch
                "Betsy_TJ_BraStretch"
                subpixel True
                pos (0,-30) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 818)#(0.6, 700)
                xoffset 270#315
                yoffset -245#-265
                yzoom .15
#                alpha 0.7
                parallel:
                    ease 2 ypos 110
                    pause .3
                    ease 2 ypos -30
                    pause .4
                    repeat
                parallel:
                    pause .2
                    ease 1.8 yzoom .75#1.2
                    pause .3
                    ease 2 yzoom .15
                    pause .4
                    repeat
        contains:
                #overside tit
                "Betsy_TJ_Tits_Over"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 150#200
                yoffset -271#-271
                yzoom 1
                parallel:
                    ease 2 ypos 120
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
                parallel:
                    pause .1
                    ease .8 yzoom .90
                    pause 1.2
                    ease 1.2 yzoom 1
                    pause .8
                    ease 0.6 yzoom .98
                    repeat
        contains:
                #hands over everything
                "Betsy_TJ_Hands"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 150#200
                yoffset -271#125
                parallel:
                    pause .1
                    ease 1.9 ypos 110
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
## End Betsy TJ Pose 1 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




## Start 2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Betsy_TJ_2:
        #Her Body in the TJ pose, fast
        contains:
                #hair back
                "Betsy_BJ_HairBack"
                subpixel True
#                offset (90,-480)
                pos (-70,0) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel: #4.7s total -> 1.7
                    ease .6 ypos 60 #120
                    pause .1
                    ease .8 ypos 0
                    pause .2
                    repeat
                parallel:
                    ease .5 rotate -5
                    pause .2
                    ease .8 rotate 0
                    pause .2
                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "Betsy_TJ_Body"
                subpixel True
#                anchor (0.6, 1.0)#(0.6, 0.0)
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel: #4.7s total -> 1.7
                    ease .6 ypos 60 #120
                    pause .1
                    ease .8 ypos 0
                    pause .2
                    repeat
        contains:
                #head
                "Betsy_BJ_Head"
                subpixel True
#                offset (90,-480)
                pos (-70,0) #top (0,0)
                transform_anchor True
                rotate 0
                parallel: #4.7s total -> 1.7
                    ease .6 ypos 60 #120
                    pause .1
                    ease .8 ypos 0
                    pause .2
                    repeat
                parallel:
                    ease .5 rotate -5
                    pause .2
                    ease .8 rotate 0
                    pause .2
                    repeat
        contains:
                #underside tit
                "Betsy_TJ_Tits_Under"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 150#200
                yoffset -271#125
                yzoom 1
                parallel: #4.7s total -> 1.7
                    ease .6 ypos 60 #120
                    pause .1
                    ease .8 ypos 0
                    pause .2
                    repeat
                parallel:
                    ease .4 yzoom .90
                    pause .3
                    ease .3 yzoom 1.05
                    ease .2 yzoom .98
                    ease .2 yzoom 1
                    pause .3
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Betsy_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (0,50)#(5,50)
        contains:
                #bra stretch
                "Betsy_TJ_BraStretch"
                subpixel True
                pos (0,-40) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 818)#(0.6, 700)
                xoffset 270#315
                yoffset -245#-265
                yzoom .1
                parallel: #4.7s total -> 1.9
                    ease .6 ypos 30 #120
                    pause .1
                    ease .8 ypos -40
                    pause .2
                    repeat
                parallel: #4.7s total -> 1.9
                    ease .6 yzoom .35 #120
                    pause .1
                    ease .8 yzoom .1
                    pause .2
                    repeat
        contains:
                #overside tit
                "Betsy_TJ_Tits_Over"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 150#200
                yoffset -271#125
                yzoom 1
                parallel: #4.7s total -> 1.7
                    ease .6 ypos 60 #120
                    pause .1
                    ease .8 ypos 0
                    pause .2
                    repeat
                parallel:
                    ease .4 yzoom .90
                    pause .3
                    ease .3 yzoom 1.05
                    ease .2 yzoom .98
                    ease .2 yzoom 1
                    pause .3
                    repeat
        contains:
                #hands over everything
                "Betsy_TJ_Hands"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 150#200
                yoffset -271#125
                parallel: #4.7s total -> 1.9
#                    ease .75 ypos 60 #60
##                    pause .05
#                    ease .75 ypos 0
#                    pause .2
#                    repeat

                    ease .5 ypos 45
#                    ease .2 ypos 45
                    pause .4
#                    ease .2 ypos 40
                    ease .5 ypos 0
                    pause .3
                    repeat

## End Betsy TJ Pose 2 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

## Start 3 (licking) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Betsy_TJ_3:
        #Her Body in the TJ pose, licking
        contains:
                #hair back
                "Betsy_BJ_HairBack"
                subpixel True
                pos (-70,110) #top (0,0)
                transform_anchor True
                rotate 0
                parallel: #4.7s total -> 3.8
                    ease 1.9 ypos 130
                    pause .3
                    ease .6 ypos 100
                    pause 1
                    repeat
                parallel:
                    ease 1.9 rotate -15
                    pause .3
                    ease .6 rotate 0
                    pause 1
                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "Betsy_TJ_Body"
                subpixel True
#                anchor (0.6, 1.0)#(0.6, 0.0)
                pos (0,100) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos 130
                    pause .3
                    ease .5 ypos 100
                    pause 1
                    repeat
        contains:
                #head
                "Betsy_BJ_Head"
                subpixel True
                pos (-70,110) #top (0,0)
                transform_anchor True
                rotate 0
                parallel: #4.7s total -> 3.8
                    ease 1.9 ypos 130
                    pause .3
                    ease .6 ypos 100
                    pause 1
                    repeat
                parallel:
                    ease 1.9 rotate -15
                    pause .3
                    ease .6 rotate 0
                    pause 1
                    repeat
        contains:
                #underside tit
                "Betsy_TJ_Tits_Under"
                subpixel True
                pos (0,100) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 150#200
                yoffset -271#125
                parallel:
                    ease 2 ypos 130
                    pause .3
                    ease .5 ypos 100
                    pause 1
                    repeat
                parallel:
                    pause .1
                    ease .8 yzoom .95
                    pause 1.2
                    ease 1.2 yzoom 1
                    pause .8
                    ease 0.6 yzoom .98
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Betsy_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (0,50)#(5,50)
                rotate 0
                parallel:
                    pause .1
                    ease 2 rotate 3
                    pause .3
                    ease .5 rotate 0
                    pause .9
                    repeat
        contains:
                #bra stretch
                "Betsy_TJ_BraStretch"
                subpixel True
                pos (0,100) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 818)#(0.6, 700)
                xoffset 270#315
                yoffset -245#-265
                yzoom .7
#                alpha 0.7
                parallel:
                    ease 2 pos (10,130)#(10,130)
                    pause .3
                    ease .5 pos (0,100)
                    pause 1
                    repeat
                parallel:
                    ease 2 yzoom .9#1.2
                    pause .3
                    ease .5 yzoom .7
                    pause 1
                    repeat
        contains:
                #overside tit
                "Betsy_TJ_Tits_Over"
                subpixel True
                pos (0,100) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 150#200
                yoffset -271#125
                yzoom 1
                parallel:
                    ease 2 ypos 130
                    pause .3
                    ease .5 ypos 100
                    pause 1
                    repeat
                parallel:
                    pause .1
                    ease .8 yzoom .95
                    pause 1.2
                    ease 1.2 yzoom 1
                    pause .8
                    ease 0.6 yzoom .98
                    repeat
        contains:
                #hands over everything
                "Betsy_TJ_Hands"
                subpixel True
                pos (0,100) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 150#200
                yoffset -271#125
                parallel:
                    ease 2 ypos 130
                    pause .3
                    ease .5 ypos 100
                    pause 1
                    repeat


## End Betsy TJ Pose 3 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



## Start 4 (cumming high) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
#image Betsy_TJ_4:
#        #Her Body in the TJ pose, cummming high
#        contains:
#                #jacket
#                "Betsy_TJ_Jacketback"
#                subpixel True
#                pos (0,0) #top (0,-10)
#                transform_anchor True
#                parallel:
#                    ease 2 ypos -20
#                    pause .1
#                    ease 2 ypos 0
#                    pause .1
#                    repeat
#        contains:
#                #bra strap backing
#                "Betsy_TJ_Braback"
#                subpixel True
#                pos (0,5) #top (0,-10)
#                transform_anchor True
#                parallel:
#                    pause .2
#                    ease 1.9 ypos -30
#                    pause .2
#                    ease 1.9 ypos 5
#                    repeat
#        contains:
#                #base body test / / / / / / / / / / / / / / / / / / / /
#                "Betsy_TJ_Body"
#                subpixel True
#                pos (0,0) #top (0,-10)
#                transform_anchor True
#                parallel:
#                    ease 2 ypos -20
#                    pause .1
#                    ease 2 ypos 0
#                    pause .1
#                    repeat
#        contains:
#                #head
#                "Betsy_TJ_Head"
#                subpixel True
#                pos (20,0) #top (0,-10)
#                transform_anchor True
#                rotate 0
#                parallel:
#                    ease 2 ypos -20
#                    pause .1
#                    ease 2 ypos 0
#                    pause .1
#                    repeat
#                parallel:
#                    pause .1
#                    ease 2 rotate 20#-5
#                    pause .1
#                    ease 2 rotate 15#0
#                    repeat
#        contains:
#                #zero cock / / / / / / / / / / / / / / / / / / / /
#                subpixel True
#                "Betsy_TJ_ZeroCock"
#                pos (0,20) #top (0,-10)
#                transform_anchor True
#                rotate 0
#                parallel:
#                    ease 2 ypos 0
#                    pause .1
#                    ease 2 ypos 20
#                    pause .1
#                    repeat
#        contains:
#                contains:
#                    "Betsy_TJ_Tits"
#                subpixel True
#                pos (0,5) #top (0,-10)
#                transform_anchor True
#                parallel:
#                    pause .2
#                    ease 1.9 ypos -30
#                    pause .2
#                    ease 1.9 ypos 5
#                    repeat

## End Betsy TJ Pose 4 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start 5 (cumming low) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Betsy_TJ_5:
        #Her Body in the TJ pose, cumming low
        contains:
                #hair back
                "Betsy_BJ_HairBack"
                subpixel True
#                offset (90,-480)
                pos (-60,115) #top (0,-10)
                transform_anchor True
                rotate 5
                parallel:
                    ease 2 ypos 120
                    pause .3
                    ease 1.5 ypos 115
                    pause .5
                    repeat
                parallel:
                    pause .1
                    ease 1 rotate -5
                    pause .3
                    ease .5 rotate 5
                    pause .9
                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "Betsy_TJ_Body"
                subpixel True
#                anchor (0.6, 1.0)#(0.6, 0.0)
                pos (0,100) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos 130
                    pause .3
                    ease 1.5 ypos 120
                    pause .5
                    repeat
        contains:
                #head
                "Betsy_BJ_Head"
                subpixel True
#                offset (90,-480)
                pos (-60,115) #top (0,-10)
                transform_anchor True
                rotate 5
                parallel:
                    ease 2 ypos 120
                    pause .3
                    ease 1.5 ypos 115
                    pause .5
                    repeat
                parallel:
                    pause .1
                    ease 1 rotate -5
                    pause .3
                    ease .5 rotate 5
                    pause .9
                    repeat
        contains:
                #underside tit
                "Betsy_TJ_Tits_Under"
                subpixel True
                pos (0,120) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 150#200
                yoffset -271#125
                parallel:
                    ease 2 ypos 130
                    pause .3
                    ease 1.5 ypos 120 #.5
                    pause .5
                    repeat
                parallel:
                    pause .1
                    ease .8 yzoom .95
                    pause 1.2
                    ease 1.2 yzoom 1
                    pause .8
                    ease 0.6 yzoom .98
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Betsy_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (0,50)#(5,50)
                rotate 0
                parallel:
#                    pause .1
#                    ease 1.1 rotate 0
                    pause 1.5
                    ease .5 rotate -5
                    ease .8 rotate 0
                    repeat
        contains:
                #bra stretch
                "Betsy_TJ_BraStretch"
                subpixel True
                pos (-5,120) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 818)#(0.6, 700)
                xoffset 270#315
                yoffset -245#-265
                yzoom .8
#                alpha 0.7
                parallel:
                    ease 2 pos (-5,130)
                    pause .3
                    ease 1.5 pos (-5,120)
                    pause .5
                    repeat
                parallel:
                    ease 2 yzoom .85#1.21
                    pause .3
                    ease 1.5 yzoom .8#1.18
                    pause .5
                    repeat
        contains:
                #overside tit
                "Betsy_TJ_Tits_Over"
                subpixel True
                pos (0,120) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 150#200
                yoffset -271#125
                yzoom 1
                parallel:
                    ease 2 ypos 130
                    pause .3
                    ease 1.5 ypos 120 #.5
                    pause .5
                    repeat
        contains:
                #hands over everything
                "Betsy_TJ_Hands"
                subpixel True
                pos (0,120) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 150#200
                yoffset -271#125
                parallel:
                    ease 2 ypos 130
                    pause .3
                    ease 1.5 ypos 120 #.5
                    pause .5
                    repeat

# End Betsy TJ Pose 5 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

## Betsy's TJ animations end / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Betsy_TJ_Launch(Line = Trigger):    # The sequence to launch the Betsy Titfuck animations

#    #temporary, remove / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
#    return
#    #temporary, remove / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

    if renpy.showing("Betsy_TJ_Animation"):
        return

    if Line == "L": # Betsy gets started. . .
            if Taboo:
                if len(Present) >= 2:
                    if Present[0] != BetsyX:
                            "[BetsyX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                    elif Present[1] != BetsyX:
                            "[BetsyX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
                else:
                            "[BetsyX.Name] небрежно глядывается по сторонам, чтобы убедиться, что никто не наблюдает."
#            "[BetsyX.Name] bends over and places your cock between her breasts."
    if BetsyX.Chest == "suit" and not BetsyX.Uptop:
        $ BetsyX.Uptop = 1
        "Она слегка расстегивает свой костюм."
#    if BetsyX.Chest and BetsyX.Over:
#        "She throws off her [BetsyX.Over] and her [BetsyX.Chest]."
#    elif BetsyX.Over:
#        "She throws off her [BetsyX.Over], baring her breasts underneath."
#    elif BetsyX.Chest:
#        "She tugs off her [BetsyX.Chest] and throws it aside."
#    $ BetsyX.Over = 0
#    $ BetsyX.Chest = 0
#    $ BetsyX.ArmPose = 0
    call Girl_First_Topless(BetsyX)

    show blackscreen onlayer black with dissolve

    if renpy.showing("Betsy_BJ_Animation"):
            hide Betsy_BJ_Animation
    else:
            call Girl_Hide(BetsyX)
            show Betsy_Sprite at SpriteLoc(BetsyX.SpriteLoc) zorder 150:
                alpha 1
                ease 1 zoom 2.3 xpos 750 yoffset -100
            show Betsy_Sprite:
                alpha 0

#    if BetsyX.Over == "towel" or BetsyX.Chest == "corset": #pulls top down because these tops are incompatible with TJ.
#        $ BetsyX.Uptop = 1

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "titjob"
    show Betsy_TJ_Animation zorder 150:
        pos (1000,1050)#(1000,1000)#(700,520)
    $ Player.Sprite = 1
    hide blackscreen onlayer black with dissolve
    return

label Betsy_TJ_Reset:
    # The sequence to the Betsy animations from Titfuck to default
    if not renpy.showing("Betsy_TJ_Animation"):
        return
#    hide Betsy_TJ_Animation
    call Girl_Hide(BetsyX)
    $ Player.Sprite = 0

    show Betsy_Sprite at SpriteLoc(BetsyX.SpriteLoc) zorder 150:
        zoom 2.3 xpos 750 yoffset -100
    show Betsy_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 xpos 700 yoffset 50
        pause .5
        ease .5 zoom 1 xpos BetsyX.SpriteLoc yoffset 0
    "[BetsyX.Name] отстраняется."
    show Betsy_Sprite at SpriteLoc(BetsyX.SpriteLoc) zorder BetsyX.Layer:
        alpha 1 zoom 1 offset (0,0) xpos BetsyX.SpriteLoc
    return

# End Betsy TJ Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Betsy Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Betsy Handjob element //////////////////////////////////////////////////////////////////////

image Betsy_HJ_Body:
    "Betsy_Sprite"
    pos (50,-1150)#(780,-1250)
    zoom 4.8#2.15


transform Betsy_HJ_Body_1():
    subpixel True
#    pos (700,-1250)#(350,-550)
    block:
        ease .5 ypos -1120
        pause 0.25
        ease 1.0 ypos -1150
        pause 0.1
        repeat

transform Betsy_HJ_Body_2():
    subpixel True
#    pos (350,-550)
    block:
        ease 0.2 ypos -1140
        pause 0.1
        ease 0.4 ypos -1150
        pause 0.1
        repeat

image Betsy_Hand_Under:
    "images/BetsySprite/handbetsy2.png"
    anchor (0.5,0.5)
    pos (-10,0)


image Betsy_Hand_Over:
    ConditionSwitch(
        "BetsyX.Arms", "images/BetsySprite/[BetsyX.skin_image.skin_path]handbetsy1g.png",
        "True", "images/BetsySprite/[BetsyX.skin_image.skin_path]handbetsy1.png",
        )
    anchor (0.5,0.5)
    pos (70,0)#(-10,0)

transform Betsy_Hand_0():
    subpixel True
    pos (70,-100)
    rotate -10
#    block:
#        ease .5 pos (90,150) rotate -20 #ypos 150 rotate 5 Bottom
#        pause 0.25
#        ease 1.0 pos (90,-100) rotate -10 #(-20,-100) #rotate -10#  Top
#        pause 0.1
#        repeat

transform Betsy_Hand_1():
    subpixel True
    pos (70,-100)
    rotate 5
    block:
        ease .5 pos (70,150) rotate -20 #ypos 150 rotate 5 Bottom
        pause 0.25
        ease 1.0 pos (70,-100) rotate -10 #(-20,-100) #rotate -10#  Top
        pause 0.1
        repeat

transform Betsy_Hand_2():
    subpixel True
    pos (80,-120)
    rotate 10
    block:
        ease 0.2 pos (80,0) rotate -20   #(-15,0)
        pause 0.1
        ease 0.4 pos (80,-120) rotate -10 #-15,-120)
        pause 0.1
        repeat

transform Handcock_3():
    subpixel True
    rotate_pad False
    ypos 400
    rotate 0 #400
    block:
        ease .5 ypos 450 rotate -2 #450
        pause 0.25
        ease 1.0 ypos 400 rotate 0 #400
        pause 0.1
        repeat

transform Handcock_4():
    subpixel True
    rotate_pad False
    ypos 400
    rotate 0
    block:
        ease .2 ypos 430 rotate -3 #410
        ease .5 ypos 400 rotate 0
        pause 0.1
        repeat

transform Handcock_1L():
    subpixel True
    rotate_pad False
    ypos 400
    rotate 0 #400
    block:
        ease .5 ypos 450 rotate -2 #450
        pause 0.25
        ease 1.0 ypos 400 rotate 0 #400
        pause 0.1
        repeat

transform Handcock_2L():
    subpixel True
    rotate_pad False
    ypos 400
    rotate 0
    block:
        ease .2 ypos 430 rotate -3 #410
        ease .5 ypos 400 rotate 0
        pause 0.1
        repeat

image Betsy_HJ_Animation:
    contains:
        ConditionSwitch(
            # backside of the hand
            "not Speed", Transform("Betsy_HJ_Body"),
            "Speed == 1", At("Betsy_HJ_Body", Betsy_HJ_Body_1()),
            "Speed >= 2", At("Betsy_HJ_Body", Betsy_HJ_Body_2()),
            "Speed", Null(),
            ),
#    contains:
#        ConditionSwitch(
#            # backside of the hand
#            "not Speed", Transform("Betsy_Hand_Under"),
#            "Speed == 1", At("Betsy_Hand_Under", Betsy_Hand_1()),
#            "Speed >= 2", At("Betsy_Hand_Under", Betsy_Hand_2()),
#            "Speed", Null(),
#            ),
    contains:
        ConditionSwitch(
            # cock
            "not Speed", Transform("Zero_Handcock"),
            "Speed == 1", At("Zero_Handcock", Handcock_1L()),
            "Speed >= 2", At("Zero_Handcock", Handcock_2L()),
            "Speed", Null(),
            ),
        offset (0,0)
    contains:
        ConditionSwitch(
            # fingers of the hand
            "not Speed", At("Betsy_Hand_Over", Betsy_Hand_0()), #Transform("Betsy_Hand_Over"),
            "Speed == 1", At("Betsy_Hand_Over", Betsy_Hand_1()),
            "Speed >= 2", At("Betsy_Hand_Over", Betsy_Hand_2()),
            "Speed", Null(),
            ),
    anchor (0.51, -1.3)
#    xzoom -0.4#0.6
    zoom 0.4#0.6


label Betsy_HJ_Launch(Line = Trigger):
    if renpy.showing("Betsy_HJ_Animation"):
        $ Trigger = "hand"
        return
    if not Player.Male:
        call Betsy_Finger_Launch
        return
    call Girl_Hide(BetsyX)
    $ BetsyX.ArmPose = 1
    if Line == "L":
        show Betsy_Sprite at SpriteLoc(StageRight) zorder 150:
            alpha 1
            ease 1 zoom 1.9 offset (50,200)#(0,200)
    else:
        show Betsy_Sprite at SpriteLoc(StageRight) zorder 150:
            alpha 1
            ease 1 zoom 1.9 offset (50,150)#(150,150)
        with dissolve

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    else:
        $ Speed = 1
    pause .5
    show Betsy_Sprite:
        alpha 0
    show Betsy_HJ_Animation at SpriteLoc(StageCenter) zorder 150 with fade:
        #xoffset 150
        offset (150,250)#(250,250)
    return

label Betsy_HJ_Reset: # The sequence to the Betsy animations from handjob to default
    if not renpy.showing("Betsy_HJ_Animation"):
        return
    $ Speed = 0
    hide Betsy_HJ_Animation with dissolve
    call Girl_Hide(BetsyX)
    show Betsy_Sprite at SpriteLoc(BetsyX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 1.5 offset (-250,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Betsy_Sprite at SpriteLoc(BetsyX.SpriteLoc) zorder BetsyX.Layer:
        alpha 1 zoom 1 offset (0,0)
#    $ BetsyX.ArmPose = 1
    return

# End Betsy Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# Core Betsy CUN element ///////////////////////////////////////////////////////////////////////////                                     Core Betsy CUN element
#Betsy CUN Over Sprite Compositing

image Betsy_CUN_Animation: #core CUN animation
    LiveComposite(
        (787,913),
        (0,0), ConditionSwitch(                                                                 # back of the hair, which needs to go behind the body
            "Speed == 0",  "Betsy_CUN_Anim_Static",
            "Speed == 1",  "Betsy_CUN_Anim_Licking1",
            "Speed == 2",  "Betsy_CUN_Anim_Licking2",
            "Speed == 3",  "Betsy_CUN_Anim_Licking3",
            "Speed > 3",  "Betsy_CUN_Anim_Licking1",
            "True", "Betsy_CUN_Anim_Static",
            ),
        )
    zoom .55
    anchor (.5,.5)

image Betsy_CUN_Anim_Static:
    #Animation for licking speed 1
    contains:
        #hair
        "Betsy_BJ_HairBack"
        subpixel True
        zoom 1.4
        pos (-50,530)
        offset (70,0)#(-10,0)
        rotate 00
        block:
            ease 2 yoffset 10
            ease 2 yoffset 0
            repeat
    contains:
        #body 2
        "Betsy_BJ_Backdrop"
        zoom 1.4
#        pos (-50,600)
        pos (-300,350)#(-440,-290)
        subpixel True
        offset (70,20)  #top(0,-35)
        block:
            ease 2 yoffset 30
            ease 2 yoffset 20
            repeat
    contains:
        #head
        "Betsy_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.4
        pos (-50,530)
        offset (70,0)#(-10,0)
        rotate 0
        block:
            ease 2 yoffset 10
            ease 2 yoffset 0
            repeat
    contains:
        #pussy
        "Zero_Pussy"
        anchor (.5,.5)
        zoom 1.7
        pos (235,790)#(410,790)
        offset (0,0)
        pause 0.1
        block:
            ease 2 yoffset 10
            ease 2 yoffset 0
            repeat


image Betsy_CUN_Anim_Licking1:
    #Animation for licking speed 1
    contains:
        #hair
        "Betsy_BJ_HairBack"
        subpixel True
        zoom 1.4
        pos (-50,520)#(-50,570)
        offset (40,40)#(40,40)
        rotate 10
        block: #5s total
            ease 2.5 offset (45,100) #bottom (0,75)
            easeout 1.5 offset (45,60)  #top (0,60)
            ease .5 offset (40,20)  #top
            ease .5 offset (42,30)  #top
            repeat
    contains:
        #body 2
        "Betsy_BJ_Backdrop"#"Betsy_Sprite"
#        zoom 1 #4.5
#        pos (-350,-290)#(-440,-290)
        zoom 1.4
        pos (-300,350)#(-440,-290)
        subpixel True
        offset (0,0)# -70,0
        block:
            ease 2.5 offset (0,75) #bottom (30,90)
            ease 2.3 offset (0,0)  #top
            pause .2
            repeat
    contains:
        #head
        "Betsy_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.4
        pos (-50,520)
        offset (40,40)#490)
        rotate 10
        block: #5s total
            ease 2.5 offset (45,100) #bottom (0,75)
            easeout 1.5 offset (45,60)  #top (0,60)
            ease .5 offset (40,20)  #top
            ease .5 offset (42,30)  #top
            repeat
    contains:
        #pussy
        "Zero_Pussy"
        subpixel True
        anchor (.5,.5)
        zoom 1.7
        pos (235,790)#(410,790)
        offset (0,5)#490)
        block:
            easein 1 yoffset 10 #510 bottom
            pause 1.5
            easeout 1 yoffset 0#490
            linear .3 yoffset -5#490
            easein .2 yoffset -3#490
            easeout 1 yoffset 5 #510 bottom
            repeat
#End Betsy Licking 1

image Betsy_CUN_Anim_Licking2:
    #Animation for licking speed 2
    contains:
        #hair
        "Betsy_BJ_HairBack"
        subpixel True
        zoom 1.4
        pos (-50,520)
        offset (40,30)#490)
        rotate 10
        parallel: #2s total
            ease 1 offset (30,100) #bottom
            easeout .65 offset (40,70)  #top -35)
            linear .35 offset (40,30)  #top -35)
            pause .10
            repeat
        parallel: #2s total
            ease 1 rotate 4 #bottom
            easeout .65 rotate 7  #top -35)
            linear .35 rotate 10  #top -35)
            pause .10
            repeat
    contains:
        #body 2
        "Betsy_BJ_Backdrop"
        zoom 1.4
        pos (-300,350)#(-440,-290)
        subpixel True
        offset (10,50)#490)
        block:
            ease .75 offset (10,70) #bottom (30,90)
            ease .95 offset (10,50)  #top
            pause .40
            repeat
    contains:
        #head
        "Betsy_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.4
        pos (-50,520)
        offset (40,30)#490)
        rotate 10
        parallel: #2s total
            ease 1 offset (30,100) #bottom
            easeout .65 offset (40,70)  #top -35)
            linear .35 offset (40,30)  #top -35)
            pause .10
            repeat
        parallel: #2s total
            ease 1 rotate 4 #bottom
            easeout .65 rotate 7  #top -35)
            linear .35 rotate 10  #top -35)
            pause .10
            repeat
    contains:
        #pussy
        "Zero_Pussy"
        subpixel True
        anchor (.5,.5)
        zoom 1.7
        pos (235,790)#(410,790)
        offset (0,-3)#490)
        block:
            ease .5 yoffset 10 #510 bottom
            pause .5
            easeout .6 yoffset 0#490
            linear .1 yoffset -5#490
            easein .1 yoffset -3#490
            pause .3
            repeat
#End Betsy Licking 2

image Betsy_CUN_Anim_Licking3:
    #Animation for licking speed 3
    contains:
        #hair
        "Betsy_BJ_HairBack"
        subpixel True
        zoom 1.4
        pos (-30,500)
        offset (20,110)#490)
        block: #2s total
            ease .5 offset (20,130) #bottom
            ease .5 offset (20,110)  #top -35)
            repeat
    contains:
        #body 2
        "Betsy_BJ_Backdrop"
        zoom 1.4
        pos (-300,350)#(-440,-290)
        subpixel True
        offset (0,110)#490)
        block:
            ease .4 offset (0,100) #bottom (30,90)
            ease .4 offset (0,110)  #top
            pause .2
            repeat
    contains:
        #head
        "Betsy_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.4
        pos (-30,500)
        offset (20,110)#490)
        block: #2s total
            ease .5 offset (20,130) #bottom
            ease .5 offset (20,110)  #top -35)
            repeat
    contains:
        #pussy
        "Zero_Pussy"
        subpixel True
        anchor (.5,.5)
        zoom 1.7
        pos (235,790)#(410,790)
        offset (0,5)#490)
        block:
            ease .25 yoffset 10 #510 bottom
            pause .25
            ease .25 yoffset 5#490
            ease .25 yoffset 6#490
            repeat
#End Betsy Licking 3

#CUN Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Betsy_CUN_Launch(Line = Trigger):
    # The sequence to launch the Betsy CUN animations
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    return
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
    if renpy.showing("Betsy_CUN_Animation") and BetsyX.Pose != "69":
        return
    elif renpy.showing("Betsy_69_CUN") and BetsyX.Pose == "69":
        return

    if Player.Male == 1:
        call Betsy_BJ_Launch
        return

    call Girl_Hide(BetsyX)
    if Line == "L" or Line == "cum":
        show Betsy_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1
#            zoom 1 offset (0,0)
            ease 1 zoom 2.5 offset (70,240) #(-90,140) offset (150,80)
        with dissolve
    else:
        show Betsy_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1 zoom 2.5 offset (70,240) #(-90,140)
        with dissolve

    if Taboo and Line == "L":
            # Betsy gets started. . .
            if len(Present) >= 2:
                if Present[0] != BetsyX:
                        "[BetsyX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                elif Present[1] != BetsyX:
                        "[BetsyX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
            else:
                        "[BetsyX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
    $ Speed = 1
    if Line == "L":
            if not BetsyX.Blow:
                "[BetsyX.Name] нерешительно стягивает с вас штаны и касается своим ртом вашей киски."
            else:
                "[BetsyX.Name] наклоняется и начинает лизать вашу киску."

    if Line != "cum":
        $ Trigger = "cun"
    $ Player.Cock = 0
    show Betsy_Sprite zorder BetsyX.Layer:
        alpha 0
    if BetsyX.Pose == "69":
            show Betsy_69_CUN zorder 150
    else:
            show Betsy_CUN_Animation zorder 150:
                pos (800,830)#(645,610)
    return

label Betsy_CUN_Reset: # The sequence to the Betsy animations from CUN to default
    if not renpy.showing("Betsy_CUN_Animation") and not renpy.showing("Betsy_69_CUN"):
        return
#    hide Betsy_69_CUN
#    hide Betsy_CUN_Animation
    call Girl_Hide(BetsyX)
    $ Speed = 0

    show Betsy_Sprite at SpriteLoc(BetsyX.SpriteLoc) zorder 150:
        zoom 2 offset (70,140) alpha 1
        pause .5
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Betsy_Sprite at SpriteLoc(BetsyX.SpriteLoc) zorder BetsyX.Layer:
        alpha 1 zoom 1 offset (0,0)
    $ BetsyX.FaceChange("sexy")
    return

#End Betsy Cunnilingus Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

image Betsy_Finger_Animation:
    # Core Animation for Fingering Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
        ConditionSwitch(                                                # backside of the hand
            "Speed == 1", "Betsy_Finger_1",
            "Speed >= 2", "Betsy_Finger_2",
            "True", "Betsy_Finger_0",
            ),
    anchor (0.5,0.5)#anchor (0.51, -1.3)
    offset (400,945)#700,1190
    zoom 0.8
    # end Core Animation for Fingering Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <

image Betsy_Finger_0:
    # Animation for Fingering Zero's pussy, static < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Betsy_Sprite"
            pos (0,-500)
            zoom 2.15
    contains:
            ConditionSwitch(
                "Player.Wet", "BetsyBJFace/Betsy_Fingering_wet.png",
                "True", "BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_Fingering_Under.png",
                )
            anchor (0.5,0.6)
            pos (-40,50)

#            "Betsy_Finger_Under"
    contains:
            "Zero_Pussy"
    contains:
            "BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_Fingering_Over.png"
            anchor (0.5,0.6)
            pos (-40,50)
#            "Betsy_Finger_Over"
    # end Animation for Fingering Zero's pussy, static < < < < < < < < < < < < < < < < < < < < < < < <

image Betsy_Finger_1:
    # Animation for Fingering Zero's pussy, slow < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Betsy_Sprite"
            pos (0,-500)
            zoom 2.15
            block:
                ease 0.5 ypos -490 #rotate 3   100
                pause 0.25
                ease 1.0 ypos -500 #rotate -3  40
                repeat
    contains:
            ConditionSwitch(
                "Player.Wet", "BetsyBJFace/Betsy_Fingering_wet.png",
                "True", "BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_Fingering_Under.png",
                )
            subpixel True
        #    xpos 10
            anchor (0.5,0.6)
            transform_anchor True
            pos (-35,40)
            rotate -5
            block:
                ease .5 pos (-30,100) rotate -15 #(40,65)   Bottom
                pause 0.25
                ease 1.0 pos (-25,40) rotate -5 #(40,0) Top                 pause 0.1
                repeat
    contains:
            "Zero_Pussy"
            subpixel True
            rotate_pad False
            block:
                pause 0.1
                ease .5 yoffset 10 #rotate -2 #30
                pause 0.15
                ease 1.0 yoffset 0 #rotate 0 #20
                repeat
    contains:
            "BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_Fingering_Over.png"
#            "Betsy_Finger_Over"
            subpixel True
        #    xpos 10
            anchor (0.5,0.6)
            transform_anchor True
            pos (-35,40)
            rotate -5
            block:
                ease .5 pos (-30,100) rotate -15 #(-40,115)   Bottom
                pause 0.25
                ease 1.0 pos (-25,40) rotate -5 #(40,0) Top                 pause 0.1
                repeat
    # end Animation for Fingering Zero's pussy, slow < < < < < < < < < < < < < < < < < < < < < < < <

image Betsy_Finger_2:
    # Animation for Fingering Zero's pussy, fast < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Betsy_Sprite"
            pos (0,-500)
            zoom 2.15
            block:
                ease 0.15 ypos -490 #rotate 3   100
                pause 0.1
                ease 0.45 ypos -500 #rotate -3  40
                pause 0.1
                repeat
    contains:
            ConditionSwitch(
                "Player.Wet", "BetsyBJFace/Betsy_Fingering_wet.png",
                "True", "BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_Fingering_Under.png",
                )
            subpixel True
            anchor (0.5,0.6)
            transform_anchor True
#            rotate -15
            pos (-40,30)
            block:
                ease 0.15 ypos 100 #rotate 3   65
                pause 0.1
                ease 0.45 ypos 60 #rotate -3  30
                pause 0.1
                repeat
    contains:
            "Zero_Pussy"
            subpixel True
            rotate_pad False
            block:
                pause 0.05
                ease 0.15 yoffset 15 #rotate 35
                pause 0.15
                ease 0.45 yoffset 0 #rotate 20
                repeat
    contains:
            "BetsyBJFace/[BetsyX.skin_image.skin_path]Betsy_Fingering_Over.png"
#            "Betsy_Finger_Over"
            subpixel True
            anchor (0.5,0.6)
            transform_anchor True
#            rotate -15
            pos (-40,30)
            block:
                ease 0.15 ypos 100 #rotate 3   65
                pause 0.1
                ease 0.45 ypos 60 #rotate -3  30
                pause 0.1
                repeat
    # end Animation for Fingering Zero's pussy, fast < < < < < < < < < < < < < < < < < < < < < < < <

label Betsy_Finger_Launch(Line = Trigger):
    if renpy.showing("Betsy_Finger_Animation"):
        $ Trigger = "finger"
        return

    if Player.Male == 1:
        call Betsy_HJ_Launch
        return

    call Girl_Hide(BetsyX)
    $ BetsyX.Arms = 0
    $ BetsyX.ArmPose = 1
    if not renpy.showing("Betsy_Sprite"):
        show Betsy_Sprite at SpriteLoc(BetsyX.SpriteLoc) zorder 150:
            alpha 1 zoom 1.7 xpos 850 yoffset 200 #offset (-50,200)
        with dissolve
    show Betsy_Sprite at SpriteLoc(BetsyX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 1.7 xpos 850 yoffset 200 #offset (-50,200)

    if Taboo and Line == "L":
        # Betsy gets started. . .
        if len(Present) >= 2:
            if Present[0] != BetsyX:
                    "[BetsyX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
            elif Present[1] != BetsyX:
                    "[BetsyX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
        else:
                    "[BetsyX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
        if not BetsyX.Hand and BetsyX.Arms:
            "Когда вы стягиваете свои штаны, [BetsyX.Name] снимает перчатки и нерешительно тянется к вашей киске. Затем она начинает грубо ласкать ее."
        else:
            "Затем она наклоняется и хватает ваш член."
    elif Line == "L":
        if not BetsyX.Hand and BetsyX.Arms:
            "Когда вы стягиваете свои штаны, [BetsyX.Name] снимает перчатки и нерешительно тянется к вашей киске. Затем она начинает грубо ласкать ее."
        else:
            "[BetsyX.Name] наклоняется и кладет руку вам на киску."
    else:
            "[BetsyX.Name] наклоняется и кладет руку вам на киску."

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "finger"
    show Betsy_Sprite:
        alpha 0
    show Betsy_Finger_Animation at SpriteLoc(BetsyX.SpriteLoc) zorder 150 with fade
    return

label Betsy_Finger_Reset: # The sequence to the Betsy animations from handjob to default
    if not renpy.showing("Betsy_Finger_Animation"):
        return
    $ Speed = 0
    hide Betsy_Finger_Animation
    with dissolve
    call Girl_Hide(BetsyX)
    show Betsy_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 yoffset 50
        pause .5
        ease .5 zoom 1 xpos BetsyX.SpriteLoc yoffset 0
    show Betsy_Sprite at SpriteLoc(BetsyX.SpriteLoc) zorder BetsyX.Layer:
        alpha 1 zoom 1 xpos BetsyX.SpriteLoc yoffset 0
    return

# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


# Start Betsy 69 Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

image Betsy_69_Animation:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
                #Shows different upper body motion depending on events
#                "True", "Betsy_69_Anim1",
                "Speed == 2", "Betsy_69_Anim2",
                "Speed == 3", "Betsy_69_Anim3",
                "Speed == 4", "Betsy_69_Anim4",
                "Speed == 5", "Betsy_69_Anim5",
                "Speed == 6", "Betsy_69_Anim6",
                "Speed", "Betsy_69_Anim1",
                "True", "Betsy_69_Static",
                ),
        )
    align (0.6,0.0)
    pos (475,-700)#(550,-350)
    zoom 1.8#1/3

#Start Animations for Betsy's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Betsy 69 Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Betsy_69_Body:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Betsy_SexSprite
        (1120,840),

        (0,0), ConditionSwitch(
            #rear sleeve
            # Modification mode
            "BetsyX.Arms == 'cammy gloves'", "images/BetsySex/modification/[BetsyX.skin_image.skin_path]Betsy_69_BodyCammy.png",
            # -----------------
            "BetsyX.Arms", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_69_BodyG.png",
            "True", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_69_Body.png",
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "BetsyX.Water", "images/BetsySex/Betsy_69_Water_Body.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #bra layer
            "(BetsyX.Chest == 'swimsuit' and BetsyX.Uptop) or BetsyX.Panties == 'swimsuit'", Recolor("Betsy", "Chest", "images/BetsySex/Betsy_69_Chest_Bikini_Up.png"),
            # Modification mode
            "(BetsyX.Chest == 'cammy leotard' and BetsyX.Uptop) or BetsyX.Panties == 'cammy leotard'", "images/BetsySex/modification/Betsy_69_Chest_Cammy_Up.png",
            # -----------------
            "BetsyX.Uptop", ConditionSwitch(
                    #if top's up
                    "BetsyX.Chest == 'sports bra'", Recolor("Betsy", "Chest", "images/BetsySex/Betsy_69_Chest_Sports_Up.png"),
                    "BetsyX.Chest == 'bra'", Recolor("Betsy", "Chest", "images/BetsySex/Betsy_69_Chest_Bra_Up.png"),
                    "BetsyX.Chest == 'lace bra'", Recolor("Betsy", "Chest", "images/BetsySex/Betsy_69_Chest_Lace_Up.png"),
                    "True", Null(),
                    ),
            #if the top's down. . .
            "BetsyX.Chest == 'swimsuit' or BetsyX.Panties == 'swimsuit'", Recolor("Betsy", "Chest", "images/BetsySex/Betsy_69_Chest_Bikini.png"),
            "BetsyX.Chest == 'sports bra'", Recolor("Betsy", "Chest", "images/BetsySex/Betsy_69_Chest_Sports.png"),
            "BetsyX.Chest == 'bra'", Recolor("Betsy", "Chest", "images/BetsySex/Betsy_69_Chest_Bra.png"),
            "BetsyX.Chest == 'lace bra'", Recolor("Betsy", "Chest", "images/BetsySex/Betsy_69_Chest_Lace.png"),
            # Modification mode
            "BetsyX.Chest == 'cammy leotard' or BetsyX.Panties == 'cammy leotard'", "images/BetsySex/modification/Betsy_69_Chest_Cammy.png",
            # ----------------
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #shorts X layer
#            "BetsyX.Legs == 'shorts' and not BetsyX.Upskirt", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_Sex_Over_Shorts.png"),
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(                                                                         
            #shirt layer
            "BetsyX.Over == 'pink top' and BetsyX.Uptop", Recolor("Betsy", "Over", "images/BetsySex/Betsy_69_Over_Pink_Up.png"),
            "BetsyX.Over == 'tank' and BetsyX.Uptop", Recolor("Betsy", "Over", "images/BetsySex/Betsy_69_Over_Tank_Up.png"),
            "BetsyX.Uptop", Null(),
            "BetsyX.Over == 'towel'", Recolor("Betsy", "Over", "images/BetsySex/Betsy_69_Over_Towel.png"),
            "BetsyX.Over == 'jacket'", Recolor("Betsy", "Over", "images/BetsySex/Betsy_69_Over_Jacket.png"),
            "BetsyX.Over == 'pink top'", Recolor("Betsy", "Over", "images/BetsySex/Betsy_69_Over_Pink.png"),
            "BetsyX.Over == 'tank'", Recolor("Betsy", "Over", "images/BetsySex/Betsy_69_Over_Tank.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #piercings
            "not BetsyX.Pierce", Null(),
            "BetsyX.Pierce == 'ring'", ConditionSwitch(
                    # ring pierce
                    "BetsyX.Uptop", "images/BetsySex/Betsy_69_Pierce_Ring.png",

                    "BetsyX.Over == 'tank'", "images/BetsySex/Betsy_69_Pierce_Ring_Blue.png",
                    "BetsyX.Over == 'pink top' or BetsyX.Over == 'towel'", "images/BetsySex/Betsy_69_Pierce_Ring_Pink.png",                  #pink top or towel

                    "BetsyX.Panties == 'swimsuit'", "images/BetsySex/Betsy_69_Pierce_Ring_Blue.png",
                    "BetsyX.Chest == 'lace bra'", "images/BetsySex/Betsy_69_Pierce_Ring_Lace.png",
                    # Modification mode
                    "BetsyX.Panties == 'cammy leotard'", "images/BetsySex/modification/Betsy_69_Pierce_Ring_Cammy.png",
                    # ----------------
                    "BetsyX.Chest", "images/BetsySex/Betsy_69_Pierce_Ring_Blue.png",

                    "True", "images/BetsySex/Betsy_69_Pierce_Ring.png",
                    ),
            "BetsyX.Uptop", "images/BetsySex/Betsy_69_Pierce_Barbell.png",

            "BetsyX.Over == 'tank'", "images/BetsySex/Betsy_69_Pierce_Barbell_Blue.png",
            "BetsyX.Over == 'pink top' or BetsyX.Over == 'towel'", "images/BetsySex/Betsy_69_Pierce_Barbell_Pink.png",                  #pink top or towel

            "BetsyX.Panties == 'swimsuit'", "images/BetsySex/Betsy_69_Pierce_Barbell_Blue.png",
            "BetsyX.Chest == 'lace bra'", "images/BetsySex/Betsy_69_Pierce_Barbell_Lace.png",
            # Modification mode
            "BetsyX.Panties == 'cammy leotard'", "images/BetsySex/modification/Betsy_69_Pierce_Barbell_Cammy.png",
            # ----------------
            "BetsyX.Chest", "images/BetsySex/Betsy_69_Pierce_Barbell_Blue.png",

            "True", "images/BetsySex/Betsy_69_Pierce_Barbell.png",
            ),

        (0,0),ConditionSwitch(
            #Outside Spunk
            "'belly' in BetsyX.Spunk and Player.Male", "images/BetsySex/Betsy_69_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'tits' in BetsyX.Spunk and Player.Male", "images/BetsySex/Betsy_69_Spunk_Tits.png",
            "True", Null(),
            ),
#        (0,0), "images/BetsySex/Betsy_Sex_HeadRef.png",
        )
    offset (250,250)#(175,175)
#    yoffset -163
# End Betsy 69 Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Betsy 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Betsy_69_Head:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Betsy_SexSprite
        (1120,840),
        (0,0), ConditionSwitch(
            #tongue
            "renpy.showing('Betsy_69_CUN') and Speed != 3", "images/BetsySex/Betsy_69_Tongue.png",
            "Speed == 1", "images/BetsySex/Betsy_69_Tongue.png",
            "True", Null(),
            ),
        (0,0), "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_69_Head.png",
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'mouth' in BetsyX.Spunk and Player.Male", "images/BetsySex/Betsy_69_Spunk_Mouth.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #collar
            "Speed == 1 and Player.Male", Null(),
            "BetsyX.Chest == 'swimsuit' or BetsyX.Panties == 'swimsuit'", "images/BetsySex/Betsy_69_Collar.png",
            # Modification mode
            "BetsyX.Chest == 'cammy leotard' or BetsyX.Panties == 'cammy leotard'", "images/BetsySex/modification/Betsy_69_Cammy_Collar.png",
            # ----------------
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Hair over
            "Speed == 1 and Player.Male", Null(),
            "BetsyX.Hair == 'blonde'", Recolor("Betsy", "Hair", "images/BetsySex/Betsy_69_Hair_Blonde_Over.png"),
            "BetsyX.Hair == 'long' or BetsyX.Hair == 'wetlong'", Recolor("Betsy", "Hair", "images/BetsySex/Betsy_69_Hair_Long_Over.png"),
            "True", Recolor("Betsy", "Hair", "images/BetsySex/Betsy_69_Hair_Short_Over.png"),
            ),
        )
    offset (175,175)#(180,100)
#    yoffset -163
# End Betsy 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Betsy 69 Pose Hair Over / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Betsy_69_HairOver:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Betsy_SexSprite
        (1120,840),
        (0,0), ConditionSwitch(
            #collar
            "BetsyX.Chest == 'swimsuit' or BetsyX.Panties == 'swimsuit'", "images/BetsySex/Betsy_69_Collar.png",
            # Modification mode
            "BetsyX.Chest == 'cammy leotard' or BetsyX.Panties == 'cammy leotard'", "images/BetsySex/modification/Betsy_69_Cammy_Collar.png",
            # ----------------
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Hair over
#            "renpy.showing('Betsy_TJ_Animation')", Null(),
            "BetsyX.Hair == 'blonde'", Recolor("Betsy", "Hair", "images/BetsySex/Betsy_69_Hair_Blonde_Lick.png"),
            "BetsyX.Hair == 'long' or BetsyX.Hair == 'wetlong'", Recolor("Betsy", "Hair", "images/BetsySex/Betsy_69_Hair_Long_Lick.png"),
            "True", Recolor("Betsy", "Hair", "images/BetsySex/Betsy_69_Hair_Short_Lick.png"),
            ),
        )
    offset (175,175)#(180,100)
#    yoffset -163
# End Betsy 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Betsy 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Betsy_69_HairBack:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Betsy_SexSprite
        (1120,840),
#        (0,0), "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_69_Head.png",
        (0,0), ConditionSwitch(
            #Hair over
#            "renpy.showing('Betsy_TJ_Animation')", Null(),
            "BetsyX.Hair == 'blonde'", Recolor("Betsy", "Hair", "images/BetsySex/Betsy_69_Hair_Blonde_Under.png"),
            "BetsyX.Hair == 'long' or BetsyX.Hair == 'wetlong'", Recolor("Betsy", "Hair", "images/BetsySex/Betsy_69_Hair_Long_Under.png"),
#            "BetsyX.Hair == 'wet' or BetsyX.Hair == 'wetlong' or BetsyX.Water", "images/BetsySex/Betsy_69_Hair_Long.png",
#            "not Player.Male and 'facial' in BetsyX.Spunk","images/BetsySex/Betsy_Sprite_Hair_Wet.png",
            "True", Recolor("Betsy", "Hair", "images/BetsySex/Betsy_69_Hair_Short_Under.png"),
            ),
        )
    offset (175,175)#(175,175)
#    yoffset -163
# End Betsy 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Betsy 69 Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Betsy_69_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Betsy_SexSprite
        (1120,880),
        (0,0), ConditionSwitch(
            #scarf
            # Modification mode
            "BetsyX.Acc and 'scarf' in BetsyX.Acc", "images/BetsySex/Betsy_69_Scarf.png",
            # -----------------
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #back of skirt Layer
            "BetsyX.Legs == 'skirt'", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_69_Legs_Skirt.png"),
            "BetsyX.Over == 'towel'", Recolor("Betsy", "Over", "images/BetsySex/Betsy_69_Legs_Towel.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs
#            "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_FBase.png",
#            "Player.Sprite and Player.Cock == 'in' and Speed", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_FBase.png",
#            "Player.Sprite and Player.Cock == 'in' and Speed", "Betsy_Sex_Heading_Pussy",
#            "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Ass.png",
#            "Trigger == 'lick pussy'", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Ass.png",
            "True", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_69_Legs.png",
            ),

#        (0,0), ConditionSwitch(
#            "Player.Sprite and Player.Cock == 'anal'", "images/BetsySex/Betsy_Sex_Anus_Cover.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #Wet look
            "not BetsyX.Water", Null(),
            "True", "images/BetsySex/Betsy_69_Water_Legs.png",
            ),

        (0,0), "Betsy_69_Anus",
            #Anus Composite  (0,-10)

        (0,0), "Betsy_69_Pussy",
            #Pussy Composite


        (0,0), ConditionSwitch(    #165,560
            #Personal Wetness
            "not BetsyX.Wet", Null(),
            "(BetsyX.Legs == 'yoga pants' or BetsyX.Legs == 'shorts') and not BetsyX.Upskirt", Null(),
            "BetsyX.Panties and not BetsyX.PantiesDown", Null(),
            "BetsyX.Wet == 1", AlphaMask("Wet_Drip_69","images/BetsySex/Betsy_69_Mask_Pussy.png"), #"Wet_Drip_69",
            "True", AlphaMask("Wet_Drip2_69","images/BetsySex/Betsy_69_Mask_Pussy.png"), #"Wet_Drip2_69",
            ),

        (0,0), ConditionSwitch(    #-695,-480
            #anal Spunk
            "'anal' not in BetsyX.Spunk or not Player.Male", Null(),
            "(BetsyX.Legs == 'yoga pants' or BetsyX.Legs == 'shorts') and not BetsyX.Upskirt", Null(),
#            "True", "Spunk_Drip2_69", #"Spunk_Drip_69",
            "True", AlphaMask("Spunk_Drip_69_Anal","images/BetsySex/Betsy_69_Mask_Ass.png"), #"Spunk_Drip_69",
            ),
        (0,0), ConditionSwitch(
            #anal Spunk
            "'anal' in BetsyX.Spunk", "images/BetsySex/Betsy_69_Spunk_Ass.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #hose layer
            "BetsyX.Hose == 'socks'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_69_Hose_Socks.png"),
            "BetsyX.Hose == 'stockings and garterbelt'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_69_Hose_StockingsGarter.png"),
            "BetsyX.Hose == 'garterbelt'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_69_Hose_Garter.png"),
            "BetsyX.Hose == 'stockings'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_69_Hose_Stockings.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Panties if up
            "(BetsyX.Panties == 'swimsuit' or BetsyX.Chest == 'swimsuit') and BetsyX.PantiesDown", Recolor("Betsy", "Panties", "images/BetsySex/Betsy_69_Panties_Bikini_Down.png"),
            # Modification mode
            "(BetsyX.Panties == 'cammy leotard' or BetsyX.Chest == 'cammy leotard') and BetsyX.PantiesDown", "images/BetsySex/modification/Betsy_69_Panties_Cammy_Down.png",
            # -----------------
            "BetsyX.PantiesDown", Null(),
            "BetsyX.Panties == 'lace panties'", Recolor("Betsy", "Panties", "images/BetsySex/Betsy_69_Panties_Lace.png"),
            "BetsyX.Panties == 'swimsuit' or BetsyX.Chest == 'swimsuit'", Recolor("Betsy", "Panties", "images/BetsySex/Betsy_69_Panties_Bikini.png"),
            # Modification mode
            "BetsyX.Panties == 'cammy leotard' or BetsyX.Chest == 'cammy leotard'", "images/BetsySex/modification/Betsy_69_Panties_Cammy.png",
            # -----------------
            "BetsyX.Panties and BetsyX.Wet", Recolor("Betsy", "Panties", "images/BetsySex/Betsy_69_Panties_Blue_Wet.png"),
            "BetsyX.Panties", Recolor("Betsy", "Panties", "images/BetsySex/Betsy_69_Panties_Blue.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #pantyhose layer
            "BetsyX.Panties and BetsyX.PantiesDown", Null(),
            "BetsyX.Hose == 'pantyhose'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_69_Hose_Pantyhose.png"),
            "BetsyX.Hose == 'ripped pantyhose'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_69_Hose_Pantyhose_Holed.png"),
            "True", Null(),
            ),


        (0,0), ConditionSwitch(
            #Legs Layer
#            "BetsyX.Legs == 'skirt' and BetsyX.Upskirt", "images/BetsySex/Betsy_Sex_Legs_Skirt_Up.png",
#            "BetsyX.Legs == 'skirt'", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_Sex_Legs_Skirt.png"),
            "BetsyX.Upskirt", Null(),
#            "BetsyX.Legs == 'skirt'", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_Sex_Legs_Skirt.png"),
            "BetsyX.Legs == 'shorts' and BetsyX.Wet > 1", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_69_Legs_Shorts_Wet.png"),
            "BetsyX.Legs == 'shorts'", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_69_Legs_Shorts.png"),
            "BetsyX.Legs == 'yoga pants' and BetsyX.Wet > 1", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_69_Legs_Yoga_Wet.png"),
            "BetsyX.Legs == 'yoga pants'", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_69_Legs_Yoga.png"),
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #pussy fondling animation
##            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Betsy_Sex_Fondle_Pussy",
#            "True", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Hand.png",
#            ),

        (0,0), ConditionSwitch(
            #Piercings over pants and pantyhose
            "not BetsyX.Pierce", Null(),
            "BetsyX.Pierce == 'ring'",ConditionSwitch(
                    #If she has panties down. . .
                    "Player.Sprite and Player.Cock == 'in'", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R_Fucking.png",

                    "BetsyX.Legs == 'shorts' and not BetsyX.Upskirt", "images/BetsySex/Betsy_69_Pierce_Pussy_Blue_R.png",
                    "BetsyX.Legs == 'yoga pants' and not BetsyX.Upskirt", "images/BetsySex/Betsy_69_Pierce_Pussy_Black_R.png",
                    "BetsyX.Hose == 'pantyhose' and not (BetsyX.Panties and BetsyX.PantiesDown)", "images/BetsySex/Betsy_69_Pierce_Pussy_Lace_R.png",

                    "BetsyX.PantiesDown", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R.png",
#                    "BetsyX.Chest == 'swimsuit'", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R_Blue.png",
                    "BetsyX.Panties == 'lace panties'", "images/BetsySex/Betsy_69_Pierce_Pussy_Lace_R.png",
                    "BetsyX.Panties", "images/BetsySex/Betsy_69_Pierce_Pussy_Blue_R.png",
                    "True", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R.png",

                    "True", Null(),
                    ),
            #else, it's barbell
            "BetsyX.Legs == 'shorts' and not BetsyX.Upskirt", "images/BetsySex/Betsy_69_Pierce_Pussy_Blue_B.png",
            "BetsyX.Legs == 'yoga pants' and not BetsyX.Upskirt", "images/BetsySex/Betsy_69_Pierce_Pussy_Black_B.png",
            "BetsyX.Hose == 'pantyhose' and not (BetsyX.Panties and BetsyX.PantiesDown)", "images/BetsySex/Betsy_69_Pierce_Pussy_Lace_B.png",

            "BetsyX.PantiesDown", "images/BetsySex/Betsy_Sex_Pierce_Pussy_B.png",
#            "BetsyX.Chest == 'swimsuit'", "images/BetsySex/Betsy_Sex_Pierce_Pussy_B_Blue.png",
            "BetsyX.Panties == 'lace panties'", "images/BetsySex/Betsy_69_Pierce_Pussy_Lace_B.png",
            "BetsyX.Panties", "images/BetsySex/Betsy_69_Pierce_Pussy_Blue_B.png",
            "True", "images/BetsySex/Betsy_Sex_Pierce_Pussy_B.png",
            ),
#        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer
#            "not Player.Sprite or Player.Cock != 'out'", Null(),
#            "Speed >= 2", "Betsy_Hotdog_Zero_Anim2",
#            "Speed", "Betsy_Hotdog_Zero_Anim1",
#            "True", "Betsy_Hotdog_Zero_Anim0",
#            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
#            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy' or Trigger2 == 'lick pussy'", "Betsy_69_Lick_Pussy",
            "Trigger == 'lick ass' or Trigger2 == 'lick ass'", "Betsy_69_Lick_Ass",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy fondling animation
            "BetsyX.Offhand == 'fondle pussy' and BetsyX.Lust > 60 and not (Player.Sprite)",  At("BetsyFingerHand", GirlFingerPussyX()), #"Betsy_Sex_Mast2",
            "BetsyX.Offhand == 'fondle pussy'", At("BetsyMastHand", GirlGropePussyX()), #"Betsy_Sex_Mast",
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Betsy_Sex_Fondle_Pussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Footjob overlay
            "Player.Cock == 'foot'", Null(),
            "Player.Sprite and Player.Cock == 'anal'",AlphaMask("Betsy_69_Feet", "images/BetsySex/Betsy_Sex_Feet_Mask.png"),
            "renpy.showing('Anal_Plug_In_Sex') or renpy.showing('Anal_Plug_Out_Sex')",AlphaMask("Betsy_69_Feet", "images/BetsySex/Betsy_Sex_Feet_Mask.png"),
            "ShowFeet", "Betsy_69_Feet",
#            "Player.Sprite", AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_Feet_Mask.png"),
#            "Trigger == 'lick pussy'", AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_Feet_Mask.png"),
#            "Trigger == 'lick ass'", AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_Feet_Mask.png"),
            "True", AlphaMask("Betsy_69_Feet", "images/BetsySex/Betsy_Sex_Feet_Mask.png"),
            ),

#        (0,0), ConditionSwitch(                                                                                 #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
#            "not Speed", "Betsy_Sex_Feet",
#            "Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_FeetMask.png"),
#            "True", "Betsy_Sex_Feet",
#            ),
        )
    offset (0,20)#(175,175)
# End Betsy 69 Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_69_Feet:
    LiveComposite(
        #the lower legs used in the sex pose, referenced by Betsy_Sex_Legs
        (1120,840),
#        (0,0), "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Feet.png",                                                         #Legs Base

        (0,0), ConditionSwitch(
            #hose layer
            "(BetsyX.Hose == 'pantyhose' or BetsyX.Hose == 'ripped pantyhose') and BetsyX.Panties and BetsyX.PantiesDown", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Feet.png",
            "(BetsyX.Hose == 'tights' or BetsyX.Hose == 'ripped tights') and BetsyX.Panties and BetsyX.PantiesDown", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Feet.png",
            "BetsyX.Hose == 'socks'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_Sex_Feet_Socks.png"),
            "BetsyX.Hose == 'ripped pantyhose'", Recolor("Betsy", "Hose", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Feet_Hose_Holed.png"),
            "BetsyX.Hose and BetsyX.Hose != 'garterbelt'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_Sex_Feet_Hose.png"),
            "True", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Feet.png",   #Null(),
            ),

        (0,0), ConditionSwitch(
            #Wet look
            "not BetsyX.Water", Null(),
            "True", "images/BetsySex/Betsy_69_Water_Feet.png",
            ),
        (0,0), ConditionSwitch(
            #panties if down
            "not BetsyX.PantiesDown", Null(),
            "BetsyX.Panties == 'lace panties'", Recolor("Betsy", "Panties", "images/BetsySex/Betsy_69_Panties_Lace_Down.png"),
            "BetsyX.Panties == 'swimsuit' or BetsyX.Chest == 'swimsuit'", Null(),
            "BetsyX.Panties", Recolor("Betsy", "Panties", "images/BetsySex/Betsy_69_Panties_Blue_Down.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Legs Layer
            "BetsyX.Legs == 'yoga pants' and not BetsyX.Upskirt", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_Sex_Feet_Yoga.png"),
            "BetsyX.Legs == 'shorts' and BetsyX.Upskirt", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_69_Legs_Shorts_Down.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk
            "'feet' in BetsyX.Spunk", "images/BetsySex/Betsy_Sex_Spunk_Feet.png",
            "True", Null(),
            ),
        )

#image Spunk_Drip_69:
#    contains:
#        "Spunk_Drip2"
#        rotate 180
#        offset(-700,-500)

#image Spunk_Drip_69_Anal:
#    contains:
##        Solid("#159457", xysize=(1120,840))
#        "Spunk_Drip2"
#        rotate 180
#        offset(-695,-450)




# Start Betsy 69 Pose Pussy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Betsy_69_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).

    contains:
            # The background plate of her pussy
            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pussy_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed", "Betsy_Sex_Heading_Pussy",
#                "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_69_Pussy_Open.png",
                "BetsyX.Offhand == 'fondle pussy' and BetsyX.Lust > 60", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_69_Pussy_Open.png",
                "True", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_69_Pussy_Closed.png",
                )
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "not BetsyX.Wet", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/JubesSex/Jubes_Sex_WetPussy_F.png",
                "True", "images/BetsySex/Betsy_69_Water_Pussy.png",
                )
    contains:
            # pubes
            ConditionSwitch(
                "not BetsyX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/BetsySex/Betsy_Sex_Pubes_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 1", "images/BetsySex/Betsy_Sex_Pubes_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in'", Recolor("Betsy", "Pubes", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pubes_Open.png"),
#                "Player.Sprite and Player.Cock == 'out'", Recolor("Betsy", "Pubes", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pubes_Open.png"),
                "Trigger == 'lick pussy'", Recolor("Betsy", "Pubes", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_69_Pubes_Open.png"),
                "BetsyX.Offhand == 'fondle pussy' and BetsyX.Lust > 60", Recolor("Betsy", "Pubes", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_69_Pubes_Open.png"),
                "True", Recolor("Betsy", "Pubes", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_69_Pubes_Closed.png"),
                )
    contains:
            #Spunk
            ConditionSwitch(
                "'in' not in BetsyX.Spunk or not Player.Male", Null(),
                "(BetsyX.Legs == 'yoga pants' or BetsyX.Legs == 'shorts') and not BetsyX.Upskirt", Null(),
                "BetsyX.Panties and not BetsyX.PantiesDown", Null(),
#                "True", "Spunk_Drip_69",
                "True", AlphaMask("Spunk_Drip_69","images/BetsySex/Betsy_69_Mask_Pussy.png"),
                )
#            offset (-700,-570)

    contains:
            ConditionSwitch(
                #Outside Spunk
#                "'in' in BetsyX.Spunk and Player.Sprite and Player.Cock == 'in' and Speed and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_PussyF.png",
                "'in' in BetsyX.Spunk and Player.Male", "images/BetsySex/Betsy_69_Spunk_Pussy.png",
                "True", Null(),
                )
#            offset (0,-15)
#    contains:
#            #Spunk under penis
#            ConditionSwitch(
#                "'in' in BetsyX.Spunk", "images/BetsySex/Betsy_Sex_Spunk_Puss_Under.png",
#                "True", Null(),
#                )
#    contains:
#            #hose layer
#            ConditionSwitch(
#                "BetsyX.Panties and BetsyX.PantiesDown", Null(),
#                "BetsyX.Hose == 'ripped pantyhose' and ShowFeet", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_Sex_Hose_Pantyhose_Holed.png"),
#                "BetsyX.Hose == 'ripped pantyhose'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_Sex_Hose_Pantyhose_Holed.png"),
#                "True", Null(),
#                ),
#    contains:
#            # The animation of Zero's moving penis, masked by her pussy shape
#            ConditionSwitch(
##                "not Player.Sprite", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 3", AlphaMask("Betsy_Sex_Fucking_Zero_Anim3", "Betsy_Sex_Fucking_Mask"),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", AlphaMask("Betsy_Sex_Fucking_Zero_Anim2", "Betsy_Sex_Fucking_Mask"),
#                "Player.Sprite and Player.Cock == 'in' and Speed == 1", AlphaMask("Betsy_Sex_Fucking_Zero_Anim1", "Betsy_Sex_Heading_Mask"),
#                "Player.Sprite and Player.Cock == 'in'", "Betsy_Sex_Fucking_Zero_Anim0",
#                "True", Null(),
#                )
#    contains:
#            #Piercings
#            ConditionSwitch(
#                "BetsyX.Pierce == 'barbell' and Player.Sprite and Player.Cock == 'in' and Speed", "images/BetsySex/Betsy_Sex_Pierce_Pussy_BarbellF.png",
#                "BetsyX.Pierce == 'ring' and Player.Sprite and Player.Cock == 'in' and Speed", "images/BetsySex/Betsy_Sex_Pierce_Pussy_RingF.png",
#                "BetsyX.Pierce == 'barbell'", "images/BetsySex/Betsy_Sex_Pierce_Pussy_Barbell.png",
#                "BetsyX.Pierce == 'ring'", "images/BetsySex/Betsy_Sex_Pierce_Pussy_Ring.png",
#                "True", Null(),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed == 1", "Betsy_Pussy_Spunk_Heading",
#                "True", Null(),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "Speed == 1", Null(),
#                "'in' not in BetsyX.Spunk or not Player.Sprite or Player.Cock != 'in' or not Speed or not Player.Male", Null(),
##                "Speed <= 1", Null(), #"Betsy_Pussy_Spunk_Heading",
#                "True", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
#                )

    #End Betsy Pussy composite


image Betsy_69_Lick_Pussy:
        "Lick_AnimF"
        zoom 0.7
        rotate 180
        offset (510,500)#(535,500
image Betsy_69_Lick_Ass:
        "Lick_AnimF"
        zoom 0.7
        rotate 180
        offset (535,580)#(535,550)

image Betsy_69_Fondle_Pussy:
        "GropePussy_Betsy"
        xzoom -1.5
        yzoom 1.5
        offset(-710,-300) #(-890,-300)
#        block:
#            ease 1 offset(-1000,0) #(535,500)
#            ease 1 offset(-1000,-1000) #(535,500)
#            ease 1 offset(0,-1000) #(535,500)
#            ease 1 offset(0,0) #(535,500)
#            repeat

image Betsy_69_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/JubesSex/Jubes_Sex_Anal.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/JubesSex/Jubes_Sex_Anal.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Anus.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Anus.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed", "Betsy_Sex_Anal_Heading",
#            "Player.Sprite and Player.Cock == 'anal'", "Betsy_Sex_Anal_Tip",
            "BetsyX.Plug", "images/PlugBase_Sex.png",
            "BetsyX.Loose > 2", "Betsy_Gape_Anal_Sex",
            "BetsyX.Loose", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Anus_Loose.png",
            "True", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Anus_Tight.png",
            "True", Null(),
            )
#    contains:
#            #Spunk under penis
#            ConditionSwitch(
#                "'anal' not in BetsyX.Spunk or not Player.Male", Null(),
##                "Player.Sprite and Player.Cock != 'anal' and Speed >= 1", "images/BetsySex/Betsy_Sex_Spunk_Anal_Under.png",
##                "Player.Sprite and Player.Cock == 'anal' and Speed == 1", "Betsy_Sex_Anal_Spunk_Heading_Under",
#                "True", "images/BetsySex/Betsy_69_Spunk_Ass.png",
#                )
#            offset (5,0)
#    contains:
#            # The animation of Zero's moving penis, masked by her anus shape
#            ConditionSwitch(
#                "not Player.Sprite or Player.Cock != 'anal'", Null(),
#                "Speed >= 3",  AlphaMask("Betsy_Sex_Anal_Zero_Anim3", "Betsy_Sex_Anal_MaskF"),
#                "Speed >= 2", AlphaMask("Betsy_Sex_Anal_Zero_Anim2", "Betsy_Sex_Anal_MaskF"),
#                "Speed", AlphaMask("Betsy_Sex_Anal_Zero_Anim1", "Betsy_Sex_Anal_Mask"),
#                "True", AlphaMask("Betsy_Sex_Anal_Zero_Anim0", "Betsy_Sex_Anal_Mask"),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "'anal' not in BetsyX.Spunk or not Player.Sprite or Player.Cock != 'anal' or not Speed or not Player.Male", Null(),
#                "Speed == 1", "Betsy_Sex_Anal_Spunk_Heading_Over",
#                "True", "Betsy_Sex_Anal_Spunk",
#                )


#Start Animations for Betsy's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Betsy_69_Static:
        #this is the animation for Betsy's hairback during 69, Speed 0 (static)
        contains:
            subpixel True
            "Betsy_69_HairBack"
            rotate 180
            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-35) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-40) #top
#                pause .5
                ease 1.25 pos (0,-35) #bottom
                repeat
        #this is the animation for Zero's cock during 69, Speed 0 (static)
        contains:
            subpixel True
            ConditionSwitch(
                "Player.Male and Player.Sprite", "Zero_Blowcock",
                "True",Null(),
                )
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (690,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Betsy's head during 69, Speed 0 (static)
        contains:
            subpixel True
            "Betsy_69_Head"
            rotate 180
            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-35) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-40) #top
#                pause .5
                ease 1.25 pos (0,-35) #bottom
                repeat
        #this is the animation for Betsy's upper body during 69, Speed 0 (static)
        contains:
            "Betsy_69_Body"
            subpixel True
            rotate 180
            zoom .65
            pos (0,-10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,-20) #top
                pause .25
                ease 1 pos (0,-10) #bottom
                repeat
        #this is the animation for Betsy's lower body during 69, Speed 0 (static)
        contains:
            "Betsy_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat

#Start Animations for Betsy's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Betsy_69_Anim1:
        #this is the animation for Betsy's hairback during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Betsy_69_HairBack"
            rotate 180
            zoom .75
#            offset (180,50)#(180,100)
            pos (45,60) #X less is left, Y less is up
            block:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (15,-25) #top(10,-25
                pause 1.25
                ease 2.5 pos (45,60) #bottom(30,60)
                repeat
        #this is the animation for Zero's cock during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (690,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .50 rotate 0
                pause 1.75
                ease 1.5 rotate -5
                pause .75
                repeat
        #this is the animation for Betsy's head during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Betsy_69_Head"
            rotate 220
            zoom .75
#            offset (180,50)#(180,100)
            pos (50,60) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (20,-25) #top
                pause 1.25
                ease 2.5 pos (50,60) #bottom
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .50 rotate 200
                pause 1.5
                ease 1.25 rotate 220
                pause 1.25
                repeat
        #this is the animation for Betsy's upper body during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Betsy_69_HairOver"
            rotate 180
            zoom .75
#            offset (180,50)#(180,100)
            pos (45,60) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (15,-25) #top(10,-25
                pause 1.25
                ease 2.5 pos (45,60) #bottom(30,60)
                repeat
        contains:
            subpixel True
            "Betsy_69_Body"
            rotate 180
            zoom .65
            pos (30,40) #X less is left, Y less is up
            block:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (10,0) #top
                pause 1.25
                ease 2.5 pos (30,40) #bottom
                repeat
        #this is the animation for Betsy's lower body during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Betsy_69_Legs"
            rotate 180
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 5 seconds
                pause .25
                easein 1 pos (0,-5)
                pause 1
                ease 2.75 pos (0,0)
                repeat

#Start Animations for Betsy's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Betsy_69_Anim2:
        #this is the animation for Betsy's hairback during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Betsy_69_HairBack"
            rotate 180
            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-5) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-30) #top
#                pause .5
                ease 1.25 pos (0,-5) #bottom
                repeat
        #this is the animation for Zero's cock during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (690,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Betsy's head during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Betsy_69_Head"
            rotate 180
            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-5) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-30) #top
#                pause .5
                ease 1.25 pos (0,-5) #bottom
                repeat
        #this is the animation for Betsy's upper body during 69, Speed 2 (heading)
        contains:
            "Betsy_69_Body"
            subpixel True
            rotate 180
            zoom .65
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,10) #bottom
                repeat
        #this is the animation for Betsy's lower body during 69, Speed 2 (heading)
        contains:
            "Betsy_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat

#Start Animations for Betsy's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Betsy_69_Anim3:
        #this is the animation for Betsy's hairback during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Betsy_69_HairBack"
            rotate 180
            zoom .75
#            offset (180,50)#(180,100)
            pos (0,50) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,0) #top
#                pause .5
                ease 1.25 pos (0,50) #bottom
                repeat
        #this is the animation for Zero's cock during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (690,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Betsy's head during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Betsy_69_Head"
            rotate 180
            zoom .75
#            offset (180,50)#(180,100)
            pos (0,50) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,0) #top
#                pause .5
                ease 1.25 pos (0,50) #bottom
                repeat
        #this is the animation for Betsy's upper body during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Betsy_69_Body"
            rotate 180
            zoom .65
            pos (0,40) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,5) #top
#                pause .5
                ease 1.25 pos (0,40) #bottom
                repeat
        #this is the animation for Betsy's lower body during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Betsy_69_Legs"
            rotate 180
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,-5)
#                pause .5
                ease 1.25 pos (0,10)
                repeat

#Start Animations for Betsy's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Betsy_69_Anim4:
        #this is the animation for Betsy's hairback during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Betsy_69_HairBack"
            rotate 180
            zoom .75
#            offset (180,50)#(180,100)
            pos (0,70) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,20) #top
                pause .5
                ease 1.75 pos (0,70) #bottom
                repeat
        #this is the animation for Zero's cock during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (690,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Betsy's head during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Betsy_69_Head"
            rotate 180
            zoom .75
#            offset (180,50)#(180,100)
            pos (0,70) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,20) #top
                pause .5
                ease 1.75 pos (0,70) #bottom
                repeat
        #this is the animation for Betsy's upper body during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Betsy_69_Body"
            rotate 180
            zoom .65
            pos (0,40) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,5) #top
                pause .5
                ease 1.75 pos (0,40) #bottom
                repeat
        #this is the animation for Betsy's lower body during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Betsy_69_Legs"
            rotate 180
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,-5)
#                pause .5
                ease 2.25 pos (0,10)
                repeat

#Start Animations for Betsy's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Betsy_69_Anim5:
        #this is the animation for Betsy's hairback during 69, Speed 5 (cum high)
        contains:
            subpixel True
            "Betsy_69_HairBack"
            rotate 180
            zoom .75
#            offset (180,50)#(180,100)
            pos (0,5) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,0) #top
#                pause .5
                ease 1.25 pos (0,5) #bottom
                repeat
        #this is the animation for Zero's cock during 69, Speed 5 (cum high)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (690,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Betsy's head during 69, Speed 5 (cum high)
        contains:
            subpixel True
            "Betsy_69_Head"
            rotate 180
            zoom .75
#            offset (180,50)#(180,100)
            pos (0,5) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,0) #top
#                pause .5
                ease 1.25 pos (0,5) #bottom
                repeat
        #this is the animation for Betsy's upper body during 69, Speed 5 (cum high)
        contains:
            "Betsy_69_Body"
            subpixel True
            rotate 180
            zoom .65
            pos (0,5) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .5
                easein 1.75 pos (0,0) #top
#                pause .5
                ease 1.25 pos (0,5) #bottom
                repeat
        #this is the animation for Betsy's lower body during 69, Speed 5 (cum high)
        contains:
            "Betsy_69_Legs"
            subpixel True
            rotate 180
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein 1.75 pos (0,-5)
                pause .5
                ease 1.25 pos (0,0)
                repeat

#Start Animations for Betsy's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Betsy_69_Anim6:
        #this is the animation for Betsy's hairback during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Betsy_69_HairBack"
            rotate 180
            zoom .75
#            offset (180,50)#(180,100)
            pos (0,70) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,60) #top
                pause .5
                ease 1.75 pos (0,70) #bottom
                repeat
        #this is the animation for Zero's cock during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (690,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Betsy's head during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Betsy_69_Head"
            rotate 180
            zoom .75
#            offset (180,50)#(180,100)
            pos (0,70) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,60) #top
                pause .5
                ease 1.75 pos (0,70) #bottom
                repeat
        #this is the animation for Betsy's upper body during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Betsy_69_Body"
            rotate 180
            zoom .65
            pos (0,60) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,55) #top
                pause .5
                ease 1.75 pos (0,60) #bottom
                repeat
        #this is the animation for Betsy's lower body during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Betsy_69_Legs"
            rotate 180
            pos (0,20) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,10)
#                pause .5
                ease 2.25 pos (0,20)
                repeat

#End Animations for Betsy's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#Start Betsy 69 Cunnilingus Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

#Start Animations for Betsy's 69 Cunnalingus pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_69_CUN:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
#                "True", "Betsy_69_Anim1",
                "Speed == 2",   "Betsy_69_Cun2",
                "Speed == 3",   "Betsy_69_Cun3",
                "Speed",        "Betsy_69_Cun1",
                "True",         "Betsy_69_Cun0",
                ),
        )
    align (0.6,0.0)
    pos (475,-700)
    zoom 1.8#1/3

#Start Animations for Betsy's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Animations for Betsy's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Betsy_69_Cun0:
        #this is the animation for Betsy's hairback during 69, Speed 0 (static)
        contains:
            subpixel True
            "Betsy_69_HairBack"
            rotate 180
            zoom .75
#            offset (180,50)#(180,100)
            pos (0,30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,20) #top
#                pause .5
                ease 1.25 pos (0,30) #bottom
                repeat
        #this is the animation for Zero's cock during 69, Speed 0 (static)
        contains:
            #pussy
            "Zero_Pussy"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (840,920)#(590,620)
#        contains:
#            subpixel True
#            "Zero_Blowcock"
#            align (0.5,0.6)
#            transform_anchor True
#            rotate 0
#            zoom .3
#            alpha .5
#            offset (690,900)#(180,100)
#            pos (0,0) #X less is left, Y less is up
#            parallel:
#                #Total time, 5 seconds
#                easein 1 rotate 20
#                easein 1 rotate 0
#                repeat
#            parallel:
#                #Total time, 5 seconds
##                easein 1 pos (0,500)
#                easein 1 pos (700,850)
##                easein 1 pos (500,0)
##                easein 1 pos (0,0)
#                repeat
#            block:
#                #Total time, 5 seconds
#                pause .5
#                easein .75 pos (0,-5)
#                pause 1.25
#                ease 2.5 pos (0,0)
#                repeat
        #this is the animation for Betsy's head during 69, Speed 0 (static)
        contains:
            subpixel True
            "Betsy_69_Head"
            rotate 180
            zoom .75
#            offset (180,50)#(180,100)
            pos (0,30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,20) #top
#                pause .5
                ease 1.25 pos (0,30) #bottom
                repeat
        #this is the animation for Betsy's upper body during 69, Speed 0 (static)
        contains:
            "Betsy_69_Body"
            subpixel True
            rotate 180
            zoom .65
            pos (0,20) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,10) #top
                pause .25
                ease 1 pos (0,20) #bottom
                repeat
        #this is the animation for Betsy's lower body during 69, Speed 0 (static)
        contains:
            "Betsy_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat
        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (728,920)#(590,620)

#Start Animations for Betsy's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Betsy_69_Cun1:
        #this is the animation for Betsy's hairback during 69, Speed 1 (lick)
        contains:
            subpixel True
            "Betsy_69_HairBack"
            rotate 180
            zoom .75
#            offset (180,50)#(180,100)
            pos (0,40) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.0 pos (0,35) #top
                easeout .5 pos (0,15) #top
                ease 1.0 pos (0,40) #bottom
                pause .5
                repeat
        #this is the animation for Zero's cock during 69, Speed 1 (lick)
        contains:
            #pussy
            "Zero_Pussy"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (840,920)#(590,620)
#        contains:
#            subpixel True
#            "Zero_Blowcock"
#            align (0.5,0.6)
#            transform_anchor True
#            rotate 0
#            zoom .3
#            alpha .5
#            offset (690,900)#(180,100)
#            pos (0,0) #X less is left, Y less is up
#            parallel:
#                #Total time, 5 seconds
#                easein 1 rotate 20
#                easein 1 rotate 0
#                repeat
#            parallel:
#                #Total time, 5 seconds
##                easein 1 pos (0,500)
#                easein 1 pos (700,850)
##                easein 1 pos (500,0)
##                easein 1 pos (0,0)
#                repeat
#            block:
#                #Total time, 5 seconds
#                pause .5
#                easein .75 pos (0,-5)
#                pause 1.25
#                ease 2.5 pos (0,0)
#                repeat
        #this is the animation for Betsy's head during 69, Speed 1 (lick)
        contains:
            subpixel True
            "Betsy_69_Head"
            rotate 180
            zoom .75
#            offset (180,50)#(180,100)
            pos (0,40) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.0 pos (0,35) #top
                easeout .5 pos (0,15) #top
                ease 1.0 pos (0,40) #bottom
                pause .5
                repeat
        #this is the animation for Betsy's upper body during 69, Speed 1 (lick)
        contains:
            "Betsy_69_Body"
            subpixel True
            rotate 180
            zoom .65
            pos (0,30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.25 pos (0,20) #top
                pause .25
                ease 1.25 pos (0,30) #bottom
                repeat
        #this is the animation for Betsy's lower body during 69, Speed 1 (lick)
        contains:
            "Betsy_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat
        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (728,920)#(590,620)


#Start Animations for Betsy's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Betsy_69_Cun2:
        #this is the animation for Betsy's hairback during 69, Speed 2 (clit)
        contains:
            subpixel True
            "Betsy_69_HairBack"
            rotate 180
            zoom .75
#            offset (180,50)#(180,100)
            pos (0,35) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                easein .9 pos (0,25) #top
                easein 1.1 pos (0,35) #bottom
                repeat
            parallel:
                #Total time, 3 seconds
                easein 1.0 rotate 185 #top
                easein 1.0 rotate 175 #bottom
                repeat
        #this is the animation for Zero's cock during 69, Speed 2 (clit)
        contains:
            #pussy
            "Zero_Pussy"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (840,920)#(590,620)
#        contains:
#            subpixel True
#            "Zero_Blowcock"
#            align (0.5,0.6)
#            transform_anchor True
#            rotate 0
#            zoom .3
#            alpha .5
#            offset (690,900)#(180,100)
#            pos (0,0) #X less is left, Y less is up
#            parallel:
#                #Total time, 5 seconds
#                easein 1 rotate 20
#                easein 1 rotate 0
#                repeat
#            parallel:
#                #Total time, 5 seconds
##                easein 1 pos (0,500)
#                easein 1 pos (700,850)
##                easein 1 pos (500,0)
##                easein 1 pos (0,0)
#                repeat
#            block:
#                #Total time, 5 seconds
#                pause .5
#                easein .75 pos (0,-5)
#                pause 1.25
#                ease 2.5 pos (0,0)
#                repeat
        #this is the animation for Betsy's head during 69, Speed 2 (clit)
        contains:
            subpixel True
            "Betsy_69_Head"
            rotate 180
            zoom .75
#            offset (180,50)#(180,100)
            pos (0,35) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                easein .9 pos (0,25) #top
                easein 1.1 pos (0,35) #bottom
                repeat
            parallel:
                #Total time, 3 seconds
                easein 1.0 rotate 185 #top
                easein 1.0 rotate 175 #bottom
                repeat
        #this is the animation for Betsy's upper body during 69, Speed 2 (clit)
        contains:
            "Betsy_69_Body"
            subpixel True
            rotate 180
            zoom .65
            pos (0,30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1 pos (0,20) #top
                ease 1 pos (0,30) #bottom
                repeat
        #this is the animation for Betsy's lower body during 69, Speed 2 (clit)
        contains:
            "Betsy_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat
        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (728,920)#(590,620)

#Start Animations for Betsy's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Betsy_69_Cun3:
        #this is the animation for Betsy's hairback during 69, Speed 3 (suck)
        contains:
            subpixel True
            "Betsy_69_HairBack"
            rotate 180
            zoom .75
#            offset (180,50)#(180,100)
            pos (0,50) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,40) #top
#                pause .5
                ease 1.25 pos (0,50) #bottom
                repeat
        #this is the animation for Zero's cock during 69, Speed 3 (suck)
        contains:
            #pussy
            "Zero_Pussy"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (840,920)#(590,620)
#        contains:
#            subpixel True
#            "Zero_Blowcock"
#            align (0.5,0.6)
#            transform_anchor True
#            rotate 0
#            zoom .3
#            alpha .5
#            offset (690,900)#(180,100)
#            pos (0,0) #X less is left, Y less is up
#            parallel:
#                #Total time, 5 seconds
#                easein 1 rotate 20
#                easein 1 rotate 0
#                repeat
#            parallel:
#                #Total time, 5 seconds
##                easein 1 pos (0,500)
#                easein 1 pos (700,850)
##                easein 1 pos (500,0)
##                easein 1 pos (0,0)
#                repeat
#            block:
#                #Total time, 5 seconds
#                pause .5
#                easein .75 pos (0,-5)
#                pause 1.25
#                ease 2.5 pos (0,0)
#                repeat
        #this is the animation for Betsy's head during 69, Speed 3 (suck)
        contains:
            subpixel True
            "Betsy_69_Head"
            rotate 180
            zoom .75
#            offset (180,50)#(180,100)
            pos (0,50) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,40) #top
#                pause .5
                ease 1.25 pos (0,50) #bottom
                repeat
        #this is the animation for Betsy's upper body during 69, Speed 3 (suck)
        contains:
            "Betsy_69_Body"
            subpixel True
            rotate 180
            zoom .65
            pos (0,40) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,30) #top
                pause .25
                ease 1 pos (0,40) #bottom
                repeat
        #this is the animation for Betsy's lower body during 69, Speed 3 (suck)
        contains:
            "Betsy_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat
        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (728,920)#(590,620)
#End Animations for Betsy's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#End Betsy 69 Animations

# Start Betsy Scissor Pose content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_SC_Sprite:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
                #if the top's down. . .
                "Speed >= 2", "Betsy_SC_Anim_2",
                "Speed", "Betsy_SC_Anim_1",
                "True", "Betsy_SC_Anim_0",
                ),
        )
    align (0.6,0.0)
    pos (650,300)#(650,200)(925,740)#(910,850)
    zoom 0.85#0.8

# End Betsy Sex Pose Speed 2 Scissor / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Betsy Sex Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Betsy_SC_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Betsy_SexSprite
        (1120,880),
        (0,0), ConditionSwitch(
            #back of skirt Layer
            "BetsyX.Legs == 'skirt'", "images/BetsySex/Betsy_Sex_Legs_Skirt_Back.png",
            "True", Null(),
            ),
        (545,540), ConditionSwitch(    #165,560
            #Personal Wetness
            "not BetsyX.Wet", Null(),
            "(BetsyX.Legs == 'pants' or BetsyX.Legs == 'shorts') and not BetsyX.Upskirt", Null(),
            "BetsyX.Panties and not BetsyX.PantiesDown", Null(),
            "BetsyX.Wet == 1", "Wet_Drip",
            "True", "Wet_Drip2",
            ),

        (545,540), ConditionSwitch(    #205,530
            #Spunk
            "'anal' not in BetsyX.Spunk or not Player.Male", Null(),
            "(BetsyX.Legs == 'pants' or BetsyX.Legs == 'shorts') and not BetsyX.Upskirt", Null(),
            "BetsyX.Wet == 1", "Spunk_Drip",
            "True", "Spunk_Drip2",
            ),

        (0,0), ConditionSwitch(
            #Legs
#            "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_FBase.png",
            "Player.Sprite and Player.Cock == 'in' and Speed", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_FBase.png",
#            "Player.Sprite and Player.Cock == 'in' and Speed", "Betsy_Sex_Heading_Pussy",
#            "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Ass.png",
#            "Trigger == 'lick pussy'", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Ass.png",
            "True", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Ass.png",
            ),

#        (0,0), ConditionSwitch(
#            "Player.Sprite and Player.Cock == 'anal'", "images/BetsySex/Betsy_Sex_Anus_Cover.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #Wet look
            "not BetsyX.Water", Null(),
            "True", "images/BetsySex/Betsy_Sex_Water_Legs.png",
            ),

#        (0,0), "Betsy_Sex_Anus",
            #Anus Composite  (0,-10)

        (0,0), "Betsy_SC_Pussy",
            #Pussy Composite


        (0,0), ConditionSwitch(
            #hose layer
            "BetsyX.Hose == 'socks'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_Sex_Hose_Socks.png"),
            "BetsyX.Hose == 'stockings and garterbelt'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_Sex_Hose_StockingsGarter.png"),
            "BetsyX.Hose == 'garterbelt'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_Sex_Hose_Garter.png"),
            "BetsyX.Hose == 'stockings'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_Sex_Hose_Stockings.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Panties if up
            "(BetsyX.Panties == 'swimsuit' or BetsyX.Chest == 'swimsuit') and BetsyX.PantiesDown", Recolor("Betsy", "Panties", "images/BetsySex/Betsy_Sex_Panties_Bikini_Down.png"),
            "BetsyX.PantiesDown", Null(),
            "BetsyX.Panties == 'lace panties'", Recolor("Betsy", "Panties", "images/BetsySex/Betsy_Sex_Panties_Lace.png"),
            "BetsyX.Panties == 'swimsuit' or BetsyX.Chest == 'swimsuit'", Recolor("Betsy", "Panties", "images/BetsySex/Betsy_Sex_Panties_Bikini.png"),
            "BetsyX.Panties and BetsyX.Wet", Recolor("Betsy", "Panties", "images/BetsySex/Betsy_Sex_Panties_Blue_Wet.png"),
            "BetsyX.Panties", Recolor("Betsy", "Panties", "images/BetsySex/Betsy_Sex_Panties_Blue.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #pantyhose layer
            "BetsyX.Panties and BetsyX.PantiesDown", Null(),
#            "BetsyX.Hose == 'tights'", "images/BetsySex/Betsy_Sex_Hose_Tights.png",
#            "BetsyX.Hose == 'ripped tights'", "images/BetsySex/Betsy_Sex_Hose_Tights_Holed.png",
            "BetsyX.Hose == 'pantyhose'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_Sex_Hose_Pantyhose.png"),
            "BetsyX.Hose == 'ripped pantyhose'", Recolor("Betsy", "Hose", "images/BetsySex/Betsy_Sex_Hose_Pantyhose_Holed.png"),
            "True", Null(),
            ),


        (0,0), ConditionSwitch(
            #Legs Layer
#            "BetsyX.Legs == 'skirt' and BetsyX.Upskirt", "images/BetsySex/Betsy_Sex_Legs_Skirt_Up.png",
            "BetsyX.Legs == 'skirt'", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_Sex_Legs_Skirt.png"),
            "BetsyX.Upskirt", Null(),
#            "BetsyX.Legs == 'skirt'", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_Sex_Legs_Skirt.png"),
            "BetsyX.Legs == 'shorts' and BetsyX.Wet > 1", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_Sex_Legs_Shorts_Wet.png"),
            "BetsyX.Legs == 'shorts'", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_Sex_Legs_Shorts.png"),
            "BetsyX.Legs == 'yoga pants' and BetsyX.Wet > 1", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_Sex_Legs_Yoga_Wet.png"),
            "BetsyX.Legs == 'yoga pants'", Recolor("Betsy", "Legs", "images/BetsySex/Betsy_Sex_Legs_Yoga.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #scarf
            "BetsyX.Acc", "images/BetsySex/Betsy_Sex_Scarf.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #towel
            "BetsyX.Over == 'towel'", Recolor("Betsy", "Over", "images/BetsySex/Betsy_Sex_Legs_Towel.png"),
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #pussy fondling animation
##            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Betsy_Sex_Fondle_Pussy",
#            "True", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Hand.png",
#            ),

        (0,0), ConditionSwitch(
            #Piercings over pants and pantyhose
            "not BetsyX.Pierce", Null(),
            "BetsyX.Pierce == 'ring'",ConditionSwitch(
                    #If she has panties down. . .
                    "Player.Sprite and Player.Cock == 'in'", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R_Fucking.png",

                    "BetsyX.Legs == 'shorts' and not BetsyX.Upskirt", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R_Blue.png",
                    "BetsyX.Legs == 'yoga pants' and not BetsyX.Upskirt", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R_Black.png",
                    "BetsyX.Hose == 'pantyhose' and not (BetsyX.Panties and BetsyX.PantiesDown)", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R_Lace.png",

                    "BetsyX.PantiesDown", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R.png",
                    "BetsyX.Chest == 'swimsuit'", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R_Blue.png",
                    "BetsyX.Panties == 'lace panties'", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R_Lace.png",
                    "BetsyX.Panties", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R_Blue.png",
                    "True", "images/BetsySex/Betsy_Sex_Pierce_Pussy_R.png",

                    "True", Null(),
                    ),
            #else, it's barbell
            "BetsyX.Legs == 'shorts' and not BetsyX.Upskirt", "images/BetsySex/Betsy_Sex_Pierce_Pussy_B_Blue.png",
            "BetsyX.Legs == 'yoga pants' and not BetsyX.Upskirt", "images/BetsySex/Betsy_Sex_Pierce_Pussy_B_Black.png",
            "BetsyX.Hose == 'pantyhose' and not (BetsyX.Panties and BetsyX.PantiesDown)", "images/BetsySex/Betsy_Sex_Pierce_Pussy_B_Lace.png",

            "BetsyX.PantiesDown", "images/BetsySex/Betsy_Sex_Pierce_Pussy_B.png",
            "BetsyX.Chest == 'swimsuit'", "images/BetsySex/Betsy_Sex_Pierce_Pussy_B_Blue.png",
            "BetsyX.Panties == 'lace panties'", "images/BetsySex/Betsy_Sex_Pierce_Pussy_B_Lace.png",
            "BetsyX.Panties", "images/BetsySex/Betsy_Sex_Pierce_Pussy_B_Blue.png",
            "True", "images/BetsySex/Betsy_Sex_Pierce_Pussy_B.png",
            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy'", "Betsy_Sex_Lick_Pussy",
            "Trigger == 'lick ass'", "Betsy_Sex_Lick_Ass",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy fondling animation
            "BetsyX.Offhand == 'fondle pussy' and BetsyX.Lust > 60 and not (Player.Sprite)",  At("BetsyFingerHand", GirlFingerPussyX()), #"Betsy_Sex_Mast2",
            "BetsyX.Offhand == 'fondle pussy'", At("BetsyMastHand", GirlGropePussyX()), #"Betsy_Sex_Mast",
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Betsy_Sex_Fondle_Pussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Footjob overlay
            "Player.Cock == 'foot'", Null(),
            "Player.Sprite and Player.Cock == 'anal'",AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_Feet_Mask.png"),
            "renpy.showing('Anal_Plug_In_Sex') or renpy.showing('Anal_Plug_Out_Sex')",AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_Feet_Mask.png"),
            "ShowFeet", "Betsy_Sex_Feet",
#            "Player.Sprite", AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_Feet_Mask.png"),
#            "Trigger == 'lick pussy'", AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_Feet_Mask.png"),
#            "Trigger == 'lick ass'", AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_Feet_Mask.png"),
            "True", AlphaMask("Betsy_Sex_Feet", "images/BetsySex/Betsy_Sex_Feet_Mask.png"),
            ),
        )
# End Betsy Sex Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Betsy Sex Pose Pussy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Betsy_SC_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).
    contains:
            # The background plate of her pussy
            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pussy_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed", "Betsy_Sex_Heading_Pussy",
#                "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pussy_Open.png",
                "BetsyX.Offhand == 'fondle pussy' and BetsyX.Lust > 60", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pussy_Open.png",
                "True", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pussy_Closed.png",
                )
    contains:
            # pubes
            ConditionSwitch(
                "not BetsyX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/BetsySex/Betsy_Sex_Pubes_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 1", "images/BetsySex/Betsy_Sex_Pubes_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in'", Recolor("Betsy", "Pubes", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pubes_Open.png"),
#                "Player.Sprite and Player.Cock == 'out'", Recolor("Betsy", "Pubes", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pubes_Open.png"),
                "Trigger == 'lick pussy'", Recolor("Betsy", "Pubes", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pubes_Open.png"),
                "BetsyX.Offhand == 'fondle pussy' and BetsyX.Lust > 60", Recolor("Betsy", "Pubes", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pubes_Open.png"),
                "True", Recolor("Betsy", "Pubes", "images/BetsySex/[BetsyX.skin_image.skin_path]Betsy_Sex_Pubes_Closed.png"),
                )

    #End Betsy Pussy composite
# End Betsy Scissor Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_SC_Anim_0:
        #this is the animation for Betsy's lower body during Scissoring, Speed 0 (static)
        contains:
            subpixel True
            "Betsy_Sex_Body"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 10
            pos (0,50) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                ease 2 pos (0,60)
                pause .5
                ease 2 pos (0,50)
                pause .5
                repeat
        contains:
            subpixel True
            "Betsy_SC_Legs"
            anchor (560,580)#(560,420)
            offset (560,580) #(560,580)
            transform_anchor True
            zoom 1.2
            rotate 35
            pos (0,0) #X less is left, Y less is up
            parallel:
                pause .5
                ease 2 rotate 30
                pause .5
                ease 2 rotate 35
                repeat
        contains:
            #pussy
            "Zero_Pussy_Full"
            transform_anchor True
            anchor (.5,.5)
            zoom .7#.45
            pos (0,0)#(410,790)
            rotate -15
            offset (925,740)#(910,850)
#        contains:
#            subpixel True
##            "Betsy_Sex_Feet"
#            ConditionSwitch(
#                #Shows different lower body motion depending on events
#                "ShowFeet", "Betsy_Sex_Feet",
#                "True", AlphaMask("Betsy_Sex_Feet","images/BetsySex/Betsy_Sex_FeetMask2.png")
#                )
#            anchor (560,580)#(560,420)
#            offset (560,580) #(845,340)    #(840,390)
#            transform_anchor True
#            zoom 1.2
#            rotate 35
#            pos (0,0) #X less is left, Y less is up
#            parallel:
#                pause .5
#                ease 2 rotate 30
#                pause .5
#                ease 2 rotate 35
#                repeat
        contains:
            #Betsy's Hand
            subpixel True
            "Betsy_Sex_Hand"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 10
            pos (0,50) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                ease 2 pos (0,60)
                pause .5
                ease 2 pos (0,50)
                pause .5
                repeat
        #end animation for Betsy's lower body during Scissoring, Speed 0 (static) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Betsy_SC_Anim_1:
        #this is the animation for Betsy's lower body during Scissoring, Speed 1 (slow)
        contains:
            subpixel True
            "Betsy_Sex_Body"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 20
            pos (-20,40) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                ease 1 pos (-20,60)
                pause .5
                ease 1 pos (-20,40)
                pause .5
                repeat
        contains:
            subpixel True
            "Betsy_SC_Legs"
            anchor (560,580)#(560,420)
            offset (560,580) #(560,580)
            transform_anchor True
            zoom 1.2
            rotate 35
            pos (0,-10) #X less is left, Y less is up
            parallel:
#                pause .5
                ease 1.5 rotate 30
#                pause .5
                ease 1.5 rotate 35
                repeat
            parallel:
                ease 1 pos (0,20)
                pause .5
                ease 1 pos (0,-10)
                pause .5
                repeat
        contains:
            #pussy
            "Zero_Pussy_Full"
            transform_anchor True
            anchor (.5,.5)
            zoom .7#.45
            pos (0,0)#(410,790)
            rotate -15
            offset (925,740)#(910,850)
            parallel:
                pause .5
                ease 1 pos (0,-5)
                pause .5
                ease 1 pos (0,0)
                repeat
        contains:
            subpixel True
            "Betsy_Sex_Hand"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 20
            pos (-20,40) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                ease 1 pos (-20,60)
                pause .5
                ease 1 pos (-20,40)
                pause .5
                repeat
#        contains:
#            subpixel True
##            "Betsy_Sex_Feet"
#            ConditionSwitch(
#                #Shows different lower body motion depending on events
#                "ShowFeet", "Betsy_Sex_Feet",
#                "True", AlphaMask("Betsy_Sex_Feet","images/BetsySex/Betsy_Sex_FeetMask2.png")
#                )
#            anchor (560,580)#(560,420)
#            offset (560,580) #(845,340)    #(840,390)
#            transform_anchor True
#            zoom 1.2
#            rotate 35
#            pos (0,-10) #X less is left, Y less is up
#            parallel:
##                pause .5
#                ease 1.5 rotate 30
##                pause .5
#                ease 1.5 rotate 35
#                repeat
#            parallel:
#                ease 1 pos (0,20)
#                pause .5
#                ease 1 pos (0,-10)
#                pause .5
#                repeat
        #End animation for Betsy's lower body during Scissoring, Speed 1 (slow) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Betsy_SC_Anim_2:
        #this is the animation for Betsy's lower body during Scissoring, Speed 2 (fast)
        contains:
            subpixel True
            "Betsy_Sex_Body"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 20
            pos (-30,40) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                pause .1
                ease .5 pos (-30,50)
                ease .5 pos (-30,40)
                repeat
        contains:
            subpixel True
            "Betsy_SC_Legs"
            anchor (560,580)#(560,420)
            offset (560,580) #(560,580)
            transform_anchor True
            zoom 1.2
            rotate 35
            pos (0,-10) #X less is left, Y less is up
            parallel:
                ease .5 rotate 30
                pause .1
                ease .5 rotate 35
                repeat
            parallel:
                ease .5 pos (0,20)
                ease .5 pos (0,-10)
                pause .1
                repeat
        contains:
            #pussy
            "Zero_Pussy_Full"
            transform_anchor True
            anchor (.5,.5)
            zoom .7#.45
            pos (0,0)#(410,790)
            rotate -15
            offset (925,740)#(910,850)
            parallel:
                ease .5 pos (0,-5)
                ease .5 pos (0,0)
                pause .1
                repeat
        contains:
            subpixel True
            "Betsy_Sex_Hand"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 20
            pos (-30,40) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                pause .1
                ease .5 pos (-30,50)
                ease .5 pos (-30,40)
                repeat
#        contains:
#            subpixel True
##            "Betsy_Sex_Feet"
#            ConditionSwitch(
#                #Shows different lower body motion depending on events
#                "ShowFeet", "Betsy_Sex_Feet",
#                "True", AlphaMask("Betsy_Sex_Feet","images/BetsySex/Betsy_Sex_FeetMask2.png")
#                )
#            anchor (560,580)#(560,420)
#            offset (560,580) #(845,340)    #(840,390)
#            transform_anchor True
#            zoom 1.2
#            rotate 35
#            pos (0,-10) #X less is left, Y less is up
#            parallel:
#                ease .5 rotate 30
#                pause .1
#                ease .5 rotate 35
#                repeat
#            parallel:
#                ease .5 pos (0,20)
#                ease .5 pos (0,-10)
#                pause .1
#                repeat
        #End animation for Betsy's lower body during Scissoring, Speed 2 (fast) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     SC Launch/Reset
label Betsy_SC_Launch(Line = Trigger):
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    return
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary

    $ Trigger = Line

    if renpy.showing("Betsy_SC_Sprite"):
        return
    $ Speed = 0
    call Girl_Hide(BetsyX,1) #call Rogue_Hide
    show Betsy_SC_Sprite zorder 150
    with dissolve
    return

label Betsy_SC_Reset:
    if not renpy.showing("Betsy_SC_Sprite"):
        return
    $ BetsyX.ArmPose = 2
    hide Betsy_SC_Sprite
    call Girl_Hide(BetsyX) #call Rogue_Hide
#    call Set_The_Scene(Dress = 0)
    show Betsy_Sprite at SpriteLoc(BetsyX.SpriteLoc) zorder BetsyX.Layer:
        alpha 1 zoom 1 offset (0,0) anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return
# End Betsy Scissor Pose content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# Animation components / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Betsy Misc Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#label Betsy_Kissing_Launch(T = Trigger,Set=1):
#    call Betsy_Hide
#    $ Trigger = T
#    $ BetsyX.Pose = "kiss" if Set else BetsyX.Pose
#    show Betsy_Sprite at SpriteLoc(BetsyX.SpriteLoc) zorder BetsyX.Layer
#    show Betsy_Sprite at SpriteLoc(StageCenter) zorder BetsyX.Layer:
##        ease 0.5 offset (300,0) zoom 2 alpha 1
#        ease 0.5 pos (600,50) offset (0,0) zoom 2.5 alpha 1
#    return

#label Betsy_Kissing_Smooch:
#    $ BetsyX.FaceChange("kiss")
#    show Betsy_Sprite at SpriteLoc(StageCenter) zorder BetsyX.Layer:
#        ease 0.5 xpos StageCenter offset (0,0) zoom 2 alpha 1
#        pause 1
#        ease 0.5 xpos BetsyX.SpriteLoc zoom 1
#    show Betsy_Sprite at SpriteLoc(BetsyX.SpriteLoc) zorder BetsyX.Layer:
#        zoom 1
#    $ BetsyX.FaceChange("sexy")
#    return

#label Betsy_Breasts_Launch(T = Trigger,Set=1):
#    call Betsy_Hide
#    $ Trigger = T
#    $ BetsyX.Pose = "breasts" if Set else BetsyX.Pose
#    show Betsy_Sprite at SpriteLoc(BetsyX.SpriteLoc) zorder BetsyX.Layer:
##        ease 0.5 offset (-100,-200) zoom 2
#        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
#    return

#label Betsy_Middle_Launch(T = Trigger,Set=1):
#    call Betsy_Hide
#    $ Trigger = T
#    $ BetsyX.Pose = "mid" if Set else BetsyX.Pose
#    show Betsy_Sprite at SpriteLoc(BetsyX.SpriteLoc) zorder BetsyX.Layer:
##        ease 0.5 offset (-100,-200) zoom 2
#        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
#    return

#label Betsy_Pussy_Launch(T = Trigger,Set=1):
#    call Betsy_Hide
#    $ Trigger = T
#    $ BetsyX.Pose = "pussy" if Set else BetsyX.Pose
#    show Betsy_Sprite at SpriteLoc(BetsyX.SpriteLoc) zorder BetsyX.Layer:
#        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
#    return

#label Betsy_Pos_Reset(T = 0,Set=0):
#    if BetsyX.Loc != bg_current:
#            return
#    call Betsy_Hide
#    show Betsy_Sprite at SpriteLoc(BetsyX.SpriteLoc) zorder BetsyX.Layer:
#            ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
#    show Betsy_Sprite zorder BetsyX.Layer:
#            offset (0,0)
#            anchor (0.5, 0.0)
#            zoom 1
#            xzoom 1
#            yzoom 1
#            alpha 1
#            pos (BetsyX.SpriteLoc,50)
#    $ BetsyX.Pose = "full" if Set else 0
#    $ Trigger = T
#    return

#label Betsy_Hide(Sprite=0):
##        call Betsy_Sex_Reset
#        hide Betsy_SexSprite
#        hide Betsy_Doggy_Animation
#        hide Betsy_HJ_Animation
#        hide Betsy_BJ_Animation
#        hide Betsy_TJ_Animation
#        hide Betsy_Finger_Animation
#        hide Betsy_CUN_Animation
#        hide Betsy_69_Animation
#        hide Betsy_69_CUN
#        hide Betsy_Seated
#        if Sprite:
#                hide Betsy_Sprite
#        return



# Interface items //////////////////////////////////////////////////////////////////////////////

image GropeLeftBreast_Betsy:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65#.7
        pos (240,330)#(290,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 60
        block:
            ease 1 rotate 30
            ease 1 rotate 60
            repeat

image GropeRightBreast_Betsy:
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (160,330)#(190,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block:
            ease 1 rotate -30 #-30
            ease 1 rotate -60 #-60
            repeat

image LickRightBreast_Betsy:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5
        xzoom -0.45
        pos (235,305)#(95,355)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (215,295)#(85,345)  top
            pause .5
            ease 1.5 rotate 30 pos (235,305)#(105,375) bottom
            repeat

image LickLeftBreast_Betsy:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5
        xzoom -0.45
        pos (150,315) #(175,340)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (130,295)#(190,380)
            pause .5
            ease 1.5 rotate 30 pos (150,315)#(200,410)
            repeat

image GropeThigh_Betsy:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (190,580)#(180,670)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        block:
            pause .5
            ease 1 rotate 110 pos (200,640) #(205,750) bottom
            ease 1 rotate 100 pos (190,580)   #215
            repeat

image GropePussy_Betsy:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (220,510)#(260,580)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease .5 rotate 190 ypos 495 #(200,585)
                ease .75 rotate 170 ypos 510
            choice:
                ease .5 rotate 190 ypos 495
                pause .25
                ease 1 rotate 170 ypos 510
            repeat

image FingerPussy_Betsy:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.65
        pos (225,590)#(225,590))
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (235,565)#(150,665)
                pause .5
                ease 1 rotate 50 pos (225,590)  #(140,700)
            choice:
                ease .5 rotate 40 pos (235,565)
                pause .5
                ease 1.75 rotate 50 pos (225,590)
            choice:
                ease 2 rotate 40 pos (235,565)
                pause .5
                ease 1 rotate 50 pos (225,590)
            choice:
                ease .25 rotate 40 pos (235,565)
                ease .25 rotate 50 pos (225,590)
                ease .25 rotate 40 pos (235,565)
                ease .25 rotate 50 pos (225,590)
            repeat

image Lickpussy_Betsy:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (235,550)#(155,650)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout .5 rotate -50 pos (225,530) #(210,605)
            linear .5 rotate -60 pos (205,540) #(200,615)
            easein 1 rotate 10 pos (235,550) #(230,625)
            repeat

image VibratorRightBreast_Betsy:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (130,300)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            pause .25
            ease 1 rotate 35 ypos 290
            pause .25
            ease 1 rotate 55 ypos 300
            repeat

image VibratorLeftBreast_Betsy:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (215,305) #(270,400)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 295
            pause .25
            ease 1 rotate 55 ypos 305
            pause .25
            repeat

image VibratorPussy_Betsy:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (235,550) #(240,665)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 70
        block:
            ease 1 rotate 35 pos (225,540)
            pause .25
            ease 1 rotate 70 pos (235,550)
            pause .25
            repeat

image VibratorAnal_Betsy:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (255,520)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 10
#        block:
#            ease 1 rotate 0 xpos 260 ypos 655
#            pause .25
#            ease 1 rotate 10 xpos 270 ypos 665
#            pause .25
#            repeat
        block:
            ease 1 rotate 0 pos (245,530)
            pause .25
            ease 1 rotate 10 pos (255,540)
            pause .25
            repeat

image VibratorPussyInsert_Betsy:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (235,530)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_Betsy:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (245,510)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0



#Lesbian action animations.
image GirlGropeBothBreast_Betsy:
    contains:
        "GirlGropeLeftBreast_Betsy"
    contains:
        "GirlGropeRightBreast_Betsy"

image GirlGropeLeftBreast_Betsy:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (270,310) #290,340)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate 10 ypos 320#(280,390)
            ease 1 rotate -10 ypos 310
            repeat

image GirlGropeRightBreast_Betsy:
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (140,342) #(90,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block:
            ease 1 rotate -40 ypos 330#(90,410)
            ease 1 rotate -10 ypos 320
            repeat

image GirlGropeThigh_Betsy:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (200,580)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        parallel:
            pause .5
            ease 1 ypos 650
            ease 1 ypos 580
            repeat
        parallel:
            pause .5
            ease .5 xpos 208
            ease .5 xpos 205
            ease .5 xpos 208
            ease .5 xpos 200
            repeat

image GirlGropePussy_BetsySelf:
    contains:
        "GirlGropePussy_Betsy"
        anchor (0.5,0.5)
        rotate -40
#        yzoom -1
        pos (270,540)#(190,500)

image GirlGropePussy_Betsy:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (215,505) #(265,575
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 ypos 500
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 ypos 500#-10+20
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 ypos 500 #(205,590)
                ease .75 rotate 200 ypos 505 #(205,595)
                ease .5 rotate 205 ypos 500
                ease .75 rotate 200 ypos 505
            choice: #Fast stroke
                ease .3 rotate 205 ypos 500
                ease .3 rotate 200 ypos 510
                ease .3 rotate 205 ypos 500
                ease .3 rotate 200 ypos 510
            repeat

image GirlFingerPussy_Betsy:
    contains:
        subpixel True
        "UI_GirlFinger"
        zoom .6
        pos (225,510)#(220,640)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 ypos 515
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 ypos 515
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 ypos 515
                ease .75 rotate 200 ypos 520
                ease .5 rotate 205 ypos 515
                ease .75 rotate 200 ypos 520
            choice: #Fast stroke
                ease .3 rotate 205 ypos 515
                ease .3 rotate 200 ypos 525
                ease .3 rotate 205 ypos 515
                ease .3 rotate 200 ypos 525
            repeat



image BetsyMastHand:
        "images/UI_GirlHand_Jean.png"
        zoom 0.8
        rotate 240
        offset (385,270)

image BetsyFingerHand:
        "images/UI_GirlFinger_Jean.png"
        zoom 0.8
        rotate 220
        offset (360,330)

image Betsy_Butterfly:
    "images/BetsySprite/Betsy_Sprite_Splush.png",
    on show:
        alpha 1
        linear 0.5 alpha 1
        pause 0.1
        linear 0.5 alpha 0
