# Basic character Sprites

image Jubes_Sprite:
    LiveComposite(
        (500,950),
        (0,0), "images/JubesSprite/Jubes_Sprite_Shadow.png",
        (0,0), ConditionSwitch(
            #Jacket back of collar
            # Modification mode
            "JubesX.Acc == 'saiyan tail'", Null(),
            # -----------------
            "JubesX.Acc", Recolor("Jubes", "Acc", "images/JubesSprite/Jubes_Sprite_Jacket_Collar.png"),
            "True", Null(),
            ),

        (147,48), "Jubes_Sprite_HairBack",
#        (0,0), ConditionSwitch(
#            #Jacket backplate
#            "JubesX.Over == 'jacket'", "images/JubesSprite/Jubes_Sprite_Over_Jacket_Under.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #pants down back
            "not JubesX.Legs or not JubesX.Upskirt", Null(),
            "JubesX.Legs == 'pants'", Recolor("Jubes", "Legs", "images/JubesSprite/Jubes_Sprite_Legs_Pants_Back.png"),
            "JubesX.Legs == 'shorts'", Recolor("Jubes", "Legs", "images/JubesSprite/Jubes_Sprite_Legs_Shorts_Back.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #panties down back
            "not JubesX.Panties or not JubesX.PantiesDown", Null(),
            #if the panties are down
            "JubesX.Legs and not JubesX.Upskirt and JubesX.Legs != 'skirt'", Null(),
            #if she's wearing a skirt or nothing else
            # Modification mode
            "JubesX.Panties == 'saiyan leotard'", Null(),
            # -----------------
            "JubesX.Panties == 'lace panties'", Recolor("Jubes", "Panties", "images/JubesSprite/Jubes_Sprite_Panties_Lace_Back.png"),
            "JubesX.Panties == 'tiger panties'", Recolor("Jubes", "Panties", "images/JubesSprite/Jubes_Sprite_Panties_Tiger_Back.png"),
            "JubesX.Panties == 'bikini bottoms'", Recolor("Jubes", "Panties", "images/JubesSprite/Jubes_Sprite_Panties_Bikini_Back.png"),
            "True", "images/JubesSprite/Jubes_Sprite_Panties_Blue_Back.png",
            ),

        (0,0), ConditionSwitch(
            #body
            "JubesX.ArmPose != 1", "images/JubesSprite/[JubesX.skin_image.skin_path]Jubes_Sprite_Body2.png",         # right hand up/left down
            "True", "images/JubesSprite/[JubesX.skin_image.skin_path]Jubes_Sprite_Body1.png", #if JubesX.Arms == 1   # right Hand on hip/left raised
            ),
        (0,0), ConditionSwitch(
            #Water effect
            "JubesX.Water and JubesX.ArmPose == 1", "images/JubesSprite/Jubes_Sprite_Water1.png",
            "JubesX.Water", "images/JubesSprite/Jubes_Sprite_Water2.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Jacket open, behind torso
#            "JubesX.Uptop", ConditionSwitch(
#                    # if top is up. . .
#                    "(JubesX.Acc == 'jacket' or JubesX.Acc == 'shut jacket') and JubesX.ArmPose == 1", Recolor("Jubes", "Acc", "images/JubesSprite/Jubes_Sprite_Jacket_Open1_Back.png"),
#                    "JubesX.Acc == 'jacket' or JubesX.Acc == 'shut jacket'", Recolor("Jubes", "Acc", "images/JubesSprite/Jubes_Sprite_Jacket_Open2_Back.png"),
#                    "True", Null(),
#                    ),
            "not JubesX.Acc", Null(),
            # Modification mode
            "JubesX.Acc == 'saiyan tail'", Null(),
            # -----------------
            "(JubesX.Uptop or JubesX.Acc == 'open jacket') and JubesX.ArmPose == 1", Recolor("Jubes", "Acc", "images/JubesSprite/Jubes_Sprite_Jacket_Open1_Back.png"),
            "(JubesX.Uptop or JubesX.Acc == 'open jacket')", Recolor("Jubes", "Acc", "images/JubesSprite/Jubes_Sprite_Jacket_Open2_Back.png"),
            #If she's using arm pose 1, left arm pointing
            #If she's using arm pose 2, Left arm on hip
            "True", Recolor("Jubes", "Acc", "images/JubesSprite/Jubes_Sprite_Jacket_Closed_Back.png"),
#            "True", Null(),
            ),

        (275,560), ConditionSwitch(    #165,560
            #Personal Wetness
            "not JubesX.Wet", Null(),
            "JubesX.Wet == 1", ConditionSwitch( #Wet = 1
                    "(JubesX.Legs == 'pants' or JubesX.Legs == 'shorts') and not JubesX.Upskirt", Null(),
                    "JubesX.Panties and not JubesX.PantiesDown", Null(),
                    "(JubesX.Legs == 'pants' or JubesX.Legs == 'shorts')", AlphaMask("Wet_Drip","Jubes_Drip_MaskP"),
                    "JubesX.Panties and JubesX.PantiesDown", AlphaMask("Wet_Drip","Jubes_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip","Jubes_Drip_Mask"), #only plays if nothing is in the way
                    ),
            "True", ConditionSwitch( #Wet = 2+
                    "(JubesX.Legs == 'pants' or JubesX.Legs == 'shorts') and JubesX.Upskirt", AlphaMask("Wet_Drip2","Jubes_Drip_MaskP"),
                    "JubesX.Panties and JubesX.PantiesDown", AlphaMask("Wet_Drip2","Jubes_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip2","Jubes_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),

        (275,560), ConditionSwitch(    #165,560
            #Spunk
            "('in' not in JubesX.Spunk and 'anal' not in JubesX.Spunk) or not Player.Male", Null(),
            "True", ConditionSwitch( #Wet = 2+
                    "(JubesX.Legs == 'pants' or JubesX.Legs == 'shorts') and JubesX.Upskirt", AlphaMask("Spunk_Drip2","Jubes_Drip_MaskP"),
                    "JubesX.Panties and JubesX.PantiesDown", AlphaMask("Spunk_Drip2","Jubes_Drip_MaskP"),
                    "True", AlphaMask("Spunk_Drip2","Jubes_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (0,0), ConditionSwitch(
            #pubes
            "JubesX.Pubes", Recolor("Jubes", "Pubes", "images/JubesSprite/Jubes_Sprite_Pubes.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #nude lower piercings
            "not JubesX.Pierce", Null(),
#            "JubesX.Panties and not JubesX.PantiesDown", Null(),
#            "JubesX.Legs != 'skirt' and JubesX.Legs and not JubesX.Upskirt", Null(), #skirt if wearing a skirt
            "JubesX.Pierce == 'barbell'", "images/JubesSprite/Jubes_Sprite_Pierce_Barbell_Bot.png",
            "JubesX.Pierce == 'ring'", "images/JubesSprite/Jubes_Sprite_Pierce_Ring_Bot.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #naked tit piercings
            "not JubesX.Pierce", Null(),
#            "not JubesX.Pierce or ((JubesX.Over or JubesX.Chest) and not JubesX.Uptop)", Null(),
#            "JubesX.Uptop", Null(),
            #Only does this if she has piercings, has no tops, or has her top up
            "JubesX.Pierce == 'barbell'", ConditionSwitch(
                    # if top is up. . .
#                    "JubesX.Chest == 'black bra' or JubesX.Chest == 'lace bra' or JubesX.Chest == 'sports bra'", "images/JubesSprite/Jubes_Sprite_Pierce_Barbell_Top.png",
                    "True", "images/JubesSprite/Jubes_Sprite_Pierce_Barbell_Top.png",
                    ),
            # Pierce is "ring"
#            "JubesX.Chest == 'black bra' or JubesX.Chest == 'lace bra' or JubesX.Chest == 'sports bra'", "images/JubesSprite/Jubes_Sprite_Pierce_Ring_Top.png",
            "JubesX.Over or JubesX.Chest", "images/JubesSprite/Jubes_Sprite_Pierce_Ring_Top.png",
            "True", "images/JubesSprite/Jubes_Sprite_Pierce_Ring_Top.png",
            ),
        (0,0), ConditionSwitch(
            #Necklaces
            "JubesX.Neck == 'choker'", Recolor("Jubes", "Neck", "images/JubesSprite/Jubes_Sprite_Neck_Choker.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Chest layer
            "JubesX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "JubesX.Chest == 'lace bra'", Recolor("Jubes", "Chest", "images/JubesSprite/Jubes_Sprite_Chest_Lace_Up.png"),
                    "JubesX.Chest == 'sports bra'", Recolor("Jubes", "Chest", "images/JubesSprite/Jubes_Sprite_Chest_Sports_Up.png"),
                    "JubesX.Chest == 'bikini top'", Recolor("Jubes", "Chest", "images/JubesSprite/Jubes_Sprite_Chest_Bikini_Up.png"),
                    # Modification mode
                    "JubesX.Chest == 'saiyan leotard'", "images/JubesSprite/modification/Jubes_Sprite_Chest_Saiyan_Leotard_Up.png",
                    # -----------------
                    "True", Null(),
                    ),
            "JubesX.Chest == 'lace bra'", Recolor("Jubes", "Chest", "images/JubesSprite/Jubes_Sprite_Chest_Lace.png"),
            "JubesX.Chest == 'sports bra'", Recolor("Jubes", "Chest", "images/JubesSprite/Jubes_Sprite_Chest_Sports.png"),
            "JubesX.Chest == 'bikini top'", Recolor("Jubes", "Chest", "images/JubesSprite/Jubes_Sprite_Chest_Bikini.png"),
            # Modification mode
            "JubesX.Chest == 'saiyan leotard'", "images/JubesSprite/modification/Jubes_Sprite_Chest_Saiyan_Leotard.png",
            # -----------------
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #stockings
            "JubesX.Hose == 'socks'", Recolor("Jubes", "Hose", "images/JubesSprite/Jubes_Sprite_Hose_Socks.png"),
            "JubesX.Hose == 'stockings'", Recolor("Jubes", "Hose", "images/JubesSprite/Jubes_Sprite_Hose_Stockings.png"),
            "JubesX.Hose == 'stockings and garterbelt'", Recolor("Jubes", "Hose", "images/JubesSprite/Jubes_Sprite_Hose_StockingsandGarter.png"),
            "JubesX.Hose == 'garterbelt'", Recolor("Jubes", "Hose", "images/JubesSprite/Jubes_Sprite_Hose_Garter.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #panties
            "not JubesX.Panties", Null(),
            "JubesX.PantiesDown", ConditionSwitch(
                    #if the panties are down
                    "not JubesX.Legs or JubesX.Upskirt or JubesX.Legs == 'skirt'", ConditionSwitch(
                            #if she's wearing a skirt or nothing else
                            "JubesX.Panties == 'lace panties'", Recolor("Jubes", "Panties", "images/JubesSprite/Jubes_Sprite_Panties_Lace_Down.png"),
                            "JubesX.Panties == 'bikini bottoms' and JubesX.Wet", Recolor("Jubes", "Panties", "images/JubesSprite/Jubes_Sprite_Panties_Bikini_DownW.png"),
                            "JubesX.Panties == 'bikini bottoms'", Recolor("Jubes", "Panties", "images/JubesSprite/Jubes_Sprite_Panties_Bikini_Down.png"),
                            "JubesX.Panties == 'tiger panties' and JubesX.Wet", Recolor("Jubes", "Panties", "images/JubesSprite/Jubes_Sprite_Panties_Tiger_DownW.png"),
                            "JubesX.Panties == 'tiger panties'", Recolor("Jubes", "Panties", "images/JubesSprite/Jubes_Sprite_Panties_Tiger_Down.png"),
                            # Modification mode
                            "JubesX.Panties == 'saiyan leotard'", "images/JubesSprite/modification/Jubes_Sprite_Panties_Saiyan_Leotard_Down.png",
                            # -----------------
                            "JubesX.Wet", "images/JubesSprite/Jubes_Sprite_Panties_Blue_DownW.png",
                            "True", "images/JubesSprite/Jubes_Sprite_Panties_Blue_Down.png",
                            ),
                    "True", Null(),
                    ),
            "JubesX.Wet", ConditionSwitch(
                #if she's  wet
                "JubesX.Panties == 'lace panties'", Recolor("Jubes", "Panties", "images/JubesSprite/Jubes_Sprite_Panties_Lace.png"),
                "JubesX.Panties == 'bikini bottoms'", Recolor("Jubes", "Panties", "images/JubesSprite/Jubes_Sprite_Panties_Bikini_Wet.png"),
                "JubesX.Panties == 'tiger panties' and JubesX.Wet", Recolor("Jubes", "Panties", "images/JubesSprite/Jubes_Sprite_Panties_Tiger_Wet.png"),
                # Modification mode
                "JubesX.Panties == 'saiyan leotard'", "images/JubesSprite/modification/Jubes_Sprite_Panties_Saiyan_Leotard_Wet.png",
                # -----------------
                "True", "images/JubesSprite/Jubes_Sprite_Panties_Blue_Wet.png",
                ),
            "True", ConditionSwitch(
                #if she's not wet
                "JubesX.Panties == 'lace panties'", Recolor("Jubes", "Panties", "images/JubesSprite/Jubes_Sprite_Panties_Lace.png"),
                "JubesX.Panties == 'bikini bottoms'", Recolor("Jubes", "Panties", "images/JubesSprite/Jubes_Sprite_Panties_Bikini.png"),
                "JubesX.Panties == 'tiger panties'", Recolor("Jubes", "Panties", "images/JubesSprite/Jubes_Sprite_Panties_Tiger.png"),
                # Modification mode
                "JubesX.Panties == 'saiyan leotard'", "images/JubesSprite/modification/Jubes_Sprite_Panties_Saiyan_Leotard.png",
                # -----------------
                "True", "images/JubesSprite/Jubes_Sprite_Panties_Blue.png",
                ),
            ),
        (0,0), ConditionSwitch(
            #pantyhose
            "JubesX.Hose == 'pantyhose' and (not JubesX.PantiesDown or not JubesX.Panties)", Recolor("Jubes", "Hose", "images/JubesSprite/Jubes_Sprite_Hose_Pantyhose.png"),
            "JubesX.Hose == 'ripped pantyhose' and (not JubesX.PantiesDown or not JubesX.Panties)", Recolor("Jubes", "Hose", "images/JubesSprite/Jubes_Sprite_Hose_Pantyhose_Holed.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pants
            "not JubesX.Legs", Null(),
            "JubesX.Upskirt", ConditionSwitch(
                        #if the skirt's up or pants down
#                        "JubesX.Legs == 'dress' and JubesX.Over == 'dress'", Recolor("Jubes", "Over", "images/JubesSprite/Jubes_Sprite_Legs_Dress_Up.png"),
                        "JubesX.Legs == 'skirt'", Recolor("Jubes", "Legs", "images/JubesSprite/Jubes_Sprite_Legs_Skirt_Up.png"),
                        "JubesX.Legs == 'pants'", Recolor("Jubes", "Legs", "images/JubesSprite/Jubes_Sprite_Legs_Pants_Down.png"),
                        "JubesX.Legs == 'shorts' and JubesX.Wet > 1", Recolor("Jubes", "Legs", "images/JubesSprite/Jubes_Sprite_Legs_Shorts_DownW.png"),
                        "JubesX.Legs == 'shorts'", Recolor("Jubes", "Legs", "images/JubesSprite/Jubes_Sprite_Legs_Shorts_Down.png"),
                        "True", Null(),
                        ),
#            "JubesX.Legs == 'dress' and JubesX.Over == 'dress'", Recolor("Jubes", "Over", "images/JubesSprite/Jubes_Sprite_Legs_Dress.png"),
            "JubesX.Legs == 'skirt'", Recolor("Jubes", "Legs", "images/JubesSprite/Jubes_Sprite_Legs_Skirt.png"),
            "JubesX.Wet > 1", ConditionSwitch(
                #if she's wet
                "JubesX.Legs == 'pants'", Recolor("Jubes", "Legs", "images/JubesSprite/Jubes_Sprite_Legs_Pants.png"),
                "JubesX.Legs == 'shorts'", Recolor("Jubes", "Legs", "images/JubesSprite/Jubes_Sprite_Legs_Shorts_Wet.png"),
#                        "JubesX.Legs == 'skirt'", Recolor("Jubes", "Legs", "images/JubesSprite/Jubes_Sprite_Legs_Skirt.png"),
                "True", Null(),
                ),
            #if she's not wet
            "JubesX.Legs == 'pants'", Recolor("Jubes", "Legs", "images/JubesSprite/Jubes_Sprite_Legs_Pants.png"),
            "JubesX.Legs == 'shorts'", Recolor("Jubes", "Legs", "images/JubesSprite/Jubes_Sprite_Legs_Shorts.png"),
#                        "JubesX.Legs == 'skirt'", Recolor("Jubes", "Legs", "images/JubesSprite/Jubes_Sprite_Legs_Skirt.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #boots
            "JubesX.Boots == 'sneaks' and JubesX.Legs == 'pants'", "images/JubesSprite/Jubes_Sprite_Boots_SneaksP.png",
            "JubesX.Boots == 'sneaks'", "images/JubesSprite/Jubes_Sprite_Boots_Sneaks.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over
            "JubesX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "JubesX.Over == 'tube top'", Recolor("Jubes", "Over", "images/JubesSprite/Jubes_Sprite_Over_Tube_Up.png"),
                    "JubesX.Over == 'red shirt'", Recolor("Jubes", "Over", "images/JubesSprite/Jubes_Sprite_Over_Red_Up.png"),
                    "JubesX.Over == 'black shirt'", Recolor("Jubes", "Over", "images/JubesSprite/Jubes_Sprite_Over_Black_Up.png"),
                    "JubesX.Over == 'dress' and JubesX.Upskirt", Recolor("Jubes", "Over", "images/JubesSprite/Jubes_Sprite_Over_Dress_Up.png"),
                    "JubesX.Over == 'dress'", Recolor("Jubes", "Over", "images/JubesSprite/Jubes_Sprite_Over_Dress_UpT.png"),
#                    "JubesX.Over == 'towel'", "images/JubesSprite/Jubes_Sprite_Towel.png",
                    "True", Null(),
                    ),
            #If she's using arm pose 1, left arm pointing
            #If she's using arm pose 2, Left arm on hip
            "JubesX.Over == 'dress' and JubesX.Upskirt", Recolor("Jubes", "Over", "images/JubesSprite/Jubes_Sprite_Over_Dress_UpB.png"),
            "JubesX.Over == 'dress'", Recolor("Jubes", "Over", "images/JubesSprite/Jubes_Sprite_Over_Dress.png"),
            "JubesX.Over == 'tube top'", Recolor("Jubes", "Over", "images/JubesSprite/Jubes_Sprite_Over_Tube.png"),
            "JubesX.Over == 'red shirt'", Recolor("Jubes", "Over", "images/JubesSprite/Jubes_Sprite_Over_Red.png"),
            "JubesX.Over == 'black shirt'", Recolor("Jubes", "Over", "images/JubesSprite/Jubes_Sprite_Over_Black.png"),
            "JubesX.Over == 'towel' and JubesX.ArmPose == 1", Recolor("Jubes", "Over", "images/JubesSprite/Jubes_Sprite_Over_Towel1.png"),
            "JubesX.Over == 'towel'", Recolor("Jubes", "Over", "images/JubesSprite/Jubes_Sprite_Over_Towel2.png"),
            # Modification mode
            "JubesX.Over == 'saiyan armor'", "images/JubesSprite/modification/Jubes_Sprite_Over_Saiyan_Armor.png",
            # -----------------
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Jacket as an accessory
            "not JubesX.Acc", Null(),
            # Modification mode
            "JubesX.Acc == 'saiyan tail'", "images/JubesSprite/modification/Jubes_Sprite_Saiyan_Tail.png",
            # -----------------
            "JubesX.Acc == 'open jacket' and JubesX.ArmPose == 1", Recolor("Jubes", "Acc", "images/JubesSprite/Jubes_Sprite_Jacket_Open1.png"),
            "JubesX.Acc == 'open jacket'", Recolor("Jubes", "Acc", "images/JubesSprite/Jubes_Sprite_Jacket_Open2.png"),
            "JubesX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "(JubesX.Acc == 'jacket' or JubesX.Acc == 'shut jacket') and JubesX.ArmPose == 1", Recolor("Jubes", "Acc", "images/JubesSprite/Jubes_Sprite_Jacket_Open1.png"),
                    "JubesX.Acc == 'jacket' or JubesX.Acc == 'shut jacket'", Recolor("Jubes", "Acc", "images/JubesSprite/Jubes_Sprite_Jacket_Open2.png"),
                    "True", Null(),
                    ),
            #If she's using arm pose 1, left arm pointing
            #If she's using arm pose 2, Left arm on hip
            "JubesX.Acc == 'jacket' and JubesX.ArmPose == 1", Recolor("Jubes", "Acc", "images/JubesSprite/Jubes_Sprite_Jacket_Closed1.png"),
            "JubesX.Acc == 'jacket'", Recolor("Jubes", "Acc", "images/JubesSprite/Jubes_Sprite_Jacket_Closed2.png"),
            #below all assume JubesX.Acc == 'shut jacket'
            "JubesX.Upskirt and JubesX.ArmPose == 1", Recolor("Jubes", "Acc", "images/JubesSprite/Jubes_Sprite_Jacket_Shut1_Up.png"),
            "JubesX.Upskirt", Recolor("Jubes", "Acc", "images/JubesSprite/Jubes_Sprite_Jacket_Shut2_Up.png"),
            "JubesX.ArmPose == 1", Recolor("Jubes", "Acc", "images/JubesSprite/Jubes_Sprite_Jacket_Shut1.png"),
            "True", Recolor("Jubes", "Acc", "images/JubesSprite/Jubes_Sprite_Jacket_Shut2.png"),
            ),

        (0,0), ConditionSwitch(
            #belly spunk
            "'belly' in JubesX.Spunk and Player.Male", "images/JubesSprite/Jubes_Sprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast spunk
            "'tits' in JubesX.Spunk and Player.Male", "images/JubesSprite/Jubes_Sprite_Spunk_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Arms 1 upper layer
            "JubesX.ArmPose == 1", "images/JubesSprite/[JubesX.skin_image.skin_path]Jubes_Sprite_ArmOver1.png",        #If she's using arm pose 1, right arm high
            "True", "images/JubesSprite/[JubesX.skin_image.skin_path]Jubes_Sprite_ArmOver2.png",  #if JubesX.Arms ==2                                        #If she's using arm pose 2, Left arm high
            ),
        (0,0), ConditionSwitch(
            #Water effect
            "JubesX.Water and JubesX.ArmPose == 1", "images/JubesSprite/Jubes_Sprite_Water1_Arm.png",
            "True", Null(),
            ),


        (147,48), "Jubes_Sprite_Head", #(141,45)


#        (0,0), "images/JubesSprite/Jubes_Sprite_Headref.png", #53,-45


#        (0,0), ConditionSwitch(
#            #hand spunk
#            "JubesX.ArmPose == 2 or 'hand' not in JubesX.Spunk", Null(),
#            "True", "images/JubesSprite/Jubes_Sprite_Spunk_Hand.png",
#            ),
#        (0,0), ConditionSwitch(                                                                         #Props
#            "not JubesX.Held or JubesX.ArmPose != 2", Null(),
#            "JubesX.ArmPose == 2 and JubesX.Held == 'phone'", "images/JubesSprite/Jubes_held_phone.png",
#            "JubesX.ArmPose == 2 and JubesX.Held == 'dildo'", "images/JubesSprite/Jubes_held_dildo.png",
#            "JubesX.ArmPose == 2 and JubesX.Held == 'vibrator'", "images/JubesSprite/Jubes_held_vibrator.png",
#            "JubesX.ArmPose == 2 and JubesX.Held == 'panties'", "images/JubesSprite/Jubes_held_panties.png",
#            "True", Null(),
#            ),


        (0,0), ConditionSwitch(
            #UI tool for When Jubes is masturbating using JubesX.Offhand actions while lead
            "Trigger == 'lesbian' or not JubesX.Offhand",Null(),# or Ch_Focus is not JubesX", Null(),
            "JubesX.Offhand == 'fondle pussy' and Trigger != 'sex' and JubesX.Lust >= 70", "GirlFingerPussy_Jubes",
            "JubesX.Offhand == 'fondle pussy'", "GirlGropePussy_Jubes",
            "JubesX.Offhand == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Jubes",    #When zero is working the right breast, fondle left
            "JubesX.Offhand == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Jubes", #When zero is working the left breast, fondle right
            "JubesX.Offhand == 'fondle breasts'", "GirlGropeRightBreast_Jubes",
            "JubesX.Offhand == 'vibrator breasts'", "VibratorRightBreast_Jubes",
            "JubesX.Offhand == 'vibrator pussy'", "VibratorPussy_Jubes",
            "JubesX.Offhand == 'vibrator pussy insert'", "VibratorPussy_Jubes",
            "JubesX.Offhand == 'vibrator anal'", "VibratorAnal_Jubes",
            "JubesX.Offhand == 'vibrator anal insert'", "VibratorPussy_Jubes",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for JubesX.Offhand(lesbian) actions (ie Kitty's hand on her when Jubes is secondary)
            "not Partner or Partner is JubesX or JubesX in Nearby", Null(),
            "Partner.Offhand == 'fondle girl pussy' and Trigger != 'sex' and JubesX.Lust >= 70", "GirlFingerPussy_Jubes",
            "Partner.Offhand == 'fondle girl pussy'", "GirlGropePussy_Jubes",
            "Partner.Offhand == 'lick girl pussy'", "Lickpussy_Jubes",
            "Partner.Offhand == 'suck girl breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Jubes",
            "Partner.Offhand == 'suck girl breasts'", "LickRightBreast_Jubes",
            "Partner.Offhand == 'fondle girl breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Jubes",    #When zero is working the right breast, fondle left
            "Partner.Offhand == 'fondle girl breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Jubes", #When zero is working the left breast, fondle right
            "Partner.Offhand == 'fondle girl breasts'", "GirlGropeRightBreast_Jubes",
            "Partner.Offhand == 'vibrator girl breasts'", "VibratorRightBreast_Jubes",
            "Partner.Offhand == 'vibrator girl pussy'", "VibratorPussy_Jubes",
            "Partner.Offhand == 'vibrator girl pussy insert'", "VibratorPussy_Jubes",
            "Partner.Offhand == 'vibrator girl anal'", "VibratorAnal_Jubes",
            "Partner.Offhand == 'vibrator girl anal insert'", "VibratorPussy_Jubes",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for when RogueX is the partner in the scene, and the lead is working on her
            "not Partner or Partner is not JubesX", Null(),
            "Ch_Focus.Offhand == 'fondle girl pussy' and Trigger != 'sex' and JubesX.Lust >= 70", "GirlFingerPussy_Jubes",
            "Ch_Focus.Offhand == 'fondle girl pussy'", "GirlGropePussy_Jubes",
            "Ch_Focus.Offhand == 'lick girl pussy'", "Lickpussy_Jubes",
            "Ch_Focus.Offhand == 'suck girl breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Jubes",
            "Ch_Focus.Offhand == 'suck girl breasts'", "LickRightBreast",
            "Ch_Focus.Offhand == 'fondle girl breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Jubes",    #When zero is working the right breast, fondle left
            "Ch_Focus.Offhand == 'fondle girl breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Jubes", #When zero is working the left breast, fondle right
            "Ch_Focus.Offhand == 'fondle girl breasts'", "GirlGropeRightBreast_Jubes",
            "Ch_Focus.Offhand == 'vibrator girl breasts'", "VibratorRightBreast_Jubes",
            "Ch_Focus.Offhand == 'vibrator girl pussy'", "VibratorPussy_Jubes",
            "Ch_Focus.Offhand == 'vibrator girl pussy insert'", "VibratorPussy_Jubes",
            "Ch_Focus.Offhand == 'vibrator girl anal'", "VibratorAnal_Jubes",
            "Ch_Focus.Offhand == 'vibrator girl anal insert'", "VibratorPussy_Jubes",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger1(primary) actions
            #Jubes is primary and a sex trigger is active
            "not Trigger or Ch_Focus is not JubesX", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast_Jubes",
            "Trigger == 'fondle thighs'", "GropeThigh_Jubes",
            "Trigger == 'fondle breasts'", "GropeLeftBreast_Jubes",
            "Trigger == 'suck breasts'", "LickRightBreast_Jubes",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_Jubes",
            "Trigger == 'fondle pussy'", "GropePussy_Jubes",
            "Trigger == 'lick pussy'", "Lickpussy_Jubes",
            "Trigger == 'vibrator pussy'", "VibratorPussy_Jubes",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy_Jubes",
            "Trigger == 'vibrator anal'", "VibratorAnal_Jubes",
            "Trigger == 'vibrator anal insert'", "VibratorPussy_Jubes",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus is not JubesX", Null(),
#            "Trigger == 'fondle breasts' and not JubesX.Offhand", "GropeRightBreast_Jubes",  #"Trigger == 'fondle breasts' and not JubesX.Offhand",
            #When doing nothing offhand, use both hands on breasts.
            "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast_Jubes",
            #When sucking right breast, fondle left
            "Trigger2 == 'fondle breasts'", "GropeLeftBreast_Jubes",
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast_Jubes",
            #When sucking right breast, vibrator left
            "Trigger2 == Trigger", Null(),
            #When both triggers are the same, do nothing
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast_Jubes",
            "Trigger2 == 'suck breasts'", "LickLeftBreast_Jubes",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy_Jubes",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy_Jubes",
            "Trigger2 == 'vibrator anal'", "VibratorAnal_Jubes",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy_Jubes",
            "Trigger2 == 'fondle pussy'", "GropePussy_Jubes",
            "Trigger2 == 'lick pussy'", "Lickpussy_Jubes",
            "Trigger2 == 'fondle thighs'", "GropeThigh_Jubes",
            "True", Null(),
            ),
        )
    anchor (0.5, 0.0)
    yoffset -10
    zoom .85 #.85


image Jubes_Sprite_HairBack:
    contains:
        ConditionSwitch(
                #hair back
    #            "renpy.showing('Jubes_BJ_Animation')", Null(),
    #            "renpy.showing('Jubes_SexSprite')", Recolor("Jubes", "Hair", "images/JubesSex/Jubes_Sprite_Hair_Long_UnderSex.png"),
    #            "JubesX.Hair == 'wet' or JubesX.Water", Recolor("Jubes", "Hair", "images/JubesSprite/Jubes_Sprite_Hair_Wet_Under.png"),
                "JubesX.Hair == 'wet'", Recolor("Jubes", "Hair", "images/JubesSprite/Jubes_Sprite_Hair_Wet_Back.png"),
                "not Player.Male and 'facial' in JubesX.Spunk",Recolor("Jubes", "Hair", "images/JubesSprite/Jubes_Sprite_Hair_Wet_Back.png"),
                "JubesX.Water", Recolor("Jubes", "Hair", "images/JubesSprite/Jubes_Sprite_Hair_Wet_Back.png"),
                "True", Recolor("Jubes", "Hair", "images/JubesSprite/Jubes_Sprite_Hair_Short_Back.png"),
                ),
#    "images/JubesSprite/Jubes_Sprite_Hair_Long_Under.png"
    anchor (0.5, 0.5)
    zoom .37#.47


image Jubes_Sprite_Head:
    LiveComposite(
        (900,900),
#        (0,0), ConditionSwitch(
#                # hair behind face
#                "renpy.showing('Jubes_SexSprite')", Recolor("Jubes", "Hair", "images/JubesSex/Jubes_Sprite_Hair_Long_UnderSex.png"),
#                "True", Null(),
#                ),
        (0,0), ConditionSwitch(
                # Face background plate
                "renpy.showing('Jubes_SexSprite') and JubesX.Blush >= 2", "images/JubesSprite/[JubesX.skin_image.skin_path]Jubes_Sprite_Head_Sex_Blush2.png",
                "renpy.showing('Jubes_SexSprite') and JubesX.Blush", "images/JubesSprite/[JubesX.skin_image.skin_path]Jubes_Sprite_Head_Sex_Blush1.png",
                "renpy.showing('Jubes_SexSprite')", "images/JubesSprite/[JubesX.skin_image.skin_path]Jubes_Sprite_Head_Sex.png",
                "JubesX.Blush >= 2", "images/JubesSprite/[JubesX.skin_image.skin_path]Jubes_Sprite_Head_Blush2.png",
                "JubesX.Blush", "images/JubesSprite/[JubesX.skin_image.skin_path]Jubes_Sprite_Head_Blush1.png",
                "True", "images/JubesSprite/[JubesX.skin_image.skin_path]Jubes_Sprite_Head.png",
                ),
        (0,0), ConditionSwitch(#chin spunk
            "'chin' in JubesX.Spunk and Player.Male", "images/JubesSprite/Jubes_Sprite_Spunk_Chin.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(#Mouths
            "JubesX.Mouth == 'lipbite'", Recolor("Jubes", "Lips", "images/JubesSprite/Jubes_Sprite_Mouth_Lipbite.png"),
            "JubesX.Mouth == 'sucking'", Recolor("Jubes", "Lips", "images/JubesSprite/Jubes_Sprite_Mouth_Open.png"),
            "JubesX.Mouth == 'kiss'", Recolor("Jubes", "Lips", "images/JubesSprite/Jubes_Sprite_Mouth_Kiss.png"),
            "JubesX.Mouth == 'sad'", Recolor("Jubes", "Lips", "images/JubesSprite/Jubes_Sprite_Mouth_Sad.png"),
            "JubesX.Mouth == 'smile'", Recolor("Jubes", "Lips", "images/JubesSprite/Jubes_Sprite_Mouth_Smile.png"),
            "JubesX.Mouth == 'surprised'", Recolor("Jubes", "Lips", "images/JubesSprite/Jubes_Sprite_Mouth_Open.png"),
            "JubesX.Mouth == 'tongue'", Recolor("Jubes", "Lips", "images/JubesSprite/Jubes_Sprite_Mouth_Tongue.png"),
            "JubesX.Mouth == 'grimace'", Recolor("Jubes", "Lips", "images/JubesSprite/Jubes_Sprite_Mouth_Smile.png"),
            "JubesX.Mouth == 'smirk'", Recolor("Jubes", "Lips", "images/JubesSprite/Jubes_Sprite_Mouth_Smirk.png"),
            "JubesX.Mouth == 'open'", Recolor("Jubes", "Lips", "images/JubesSprite/Jubes_Sprite_Mouth_Open.png"),
            "True", Recolor("Jubes", "Lips", "images/JubesSprite/Jubes_Sprite_Mouth_Normal.png"),
            ),


        (0,0), ConditionSwitch(#Mouths spunk
            "'mouth' not in JubesX.Spunk or not Player.Male", Null(),
            "JubesX.Mouth == 'sucking'", "images/JubesSprite/Jubes_Sprite_Spunk_Open.png",
            "JubesX.Mouth == 'kiss'", "images/JubesSprite/Jubes_Sprite_Spunk_Kiss.png",
            "JubesX.Mouth == 'sad'", "images/JubesSprite/Jubes_Sprite_Spunk_Kiss.png",
            "JubesX.Mouth == 'smile'", "images/JubesSprite/Jubes_Sprite_Spunk_Lipbite.png",
            "JubesX.Mouth == 'surprised'", "images/JubesSprite/Jubes_Sprite_Spunk_Kiss.png",
            "JubesX.Mouth == 'tongue'", "images/JubesSprite/Jubes_Sprite_Spunk_Open.png",
            "JubesX.Mouth == 'grimace'", "images/JubesSprite/Jubes_Sprite_Spunk_Lipbite.png",
            "True", "images/JubesSprite/Jubes_Sprite_Spunk_Smirk.png",
            ),

        (0,0), ConditionSwitch(
            #wet face
            "Player.Male", Null(),
            "'mouth' not in JubesX.Spunk and 'chin' not in JubesX.Spunk", Null(),
            "'chin' not in JubesX.Spunk and JubesX.Mouth == 'tongue'", "images/JubesSprite/Jubes_Sprite_Wet_Tongue.png",
            "JubesX.Mouth == 'tongue'", "images/JubesSprite/Jubes_Sprite_Wet_Tongue2.png",
            "'chin' in JubesX.Spunk", "images/JubesSprite/Jubes_Sprite_Wet_Mouth.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #brows
            "JubesX.Brows == 'angry' and JubesX.Blush >= 2", "images/JubesSprite/[JubesX.skin_image.skin_path]Jubes_Sprite_Brows_AngryB.png",
            "JubesX.Brows == 'angry'", "images/JubesSprite/[JubesX.skin_image.skin_path]Jubes_Sprite_Brows_Angry.png",
            "JubesX.Brows == 'sad' and JubesX.Blush >= 2", "images/JubesSprite/Jubes_Sprite_Brows_SadB.png",
            "JubesX.Brows == 'sad'", "images/JubesSprite/Jubes_Sprite_Brows_Sad.png",
            "JubesX.Brows == 'surprised'", "images/JubesSprite/Jubes_Sprite_Brows_Surprised.png",
            "JubesX.Brows == 'sad' and JubesX.Blush >= 2", "images/JubesSprite/[JubesX.skin_image.skin_path]Jubes_Sprite_Brows_ConfusedB.png",
            "JubesX.Brows == 'confused'", "images/JubesSprite/[JubesX.skin_image.skin_path]Jubes_Sprite_Brows_Confused.png",
            "True", "images/JubesSprite/Jubes_Sprite_Brows_Normal.png",
            ),
        (0,0), "Jubes Blink",     #Eyes
#        (0,0), ConditionSwitch(
#            #Face Water
#            "not JubesX.Water", Null(),
#            "True", "images/JubesSprite/Jubes_Sprite_Head_Water.png",
#            ),
        (0,0), "images/JubesSprite/Jubes_Sprite_Earrings.png",     #Eyes
        # Modification mode
        (0,0), ConditionSwitch(
            #glasses under
            "JubesX.Hair == 'shades'", Recolor("Jubes", "Hair", "images/JubesSprite/Jubes_Sprite_Hair_Shades.png"),
            "True", Null(),
            ),
        # -----------------
        (0,0), ConditionSwitch(
            #Hair over
#            "renpy.showing('Jubes_TJ_Animation')", Null(),
            "JubesX.Hair == 'wet' or JubesX.Water", Recolor("Jubes", "Hair", "images/JubesSprite/Jubes_Sprite_Hair_Wet.png"),
            "not Player.Male and 'facial' in JubesX.Spunk",Recolor("Jubes", "Hair", "images/JubesSprite/Jubes_Sprite_Hair_Wet.png"),
            "JubesX.Hair == 'shades'", Recolor("Jubes", "Hair", "images/JubesSprite/Jubes_Sprite_Hair_Shades.png"),
            "True", Recolor("Jubes", "Hair", "images/JubesSprite/Jubes_Sprite_Hair_Short.png"),
            ),
        (0,0), ConditionSwitch(
            #Hair Water
            "JubesX.Water", "images/JubesSprite/Jubes_Sprite_Wet_Head.png",
            "not Player.Male and 'facial' in JubesX.Spunk", "images/JubesSprite/Jubes_Sprite_Wet_Head.png",
            "True",Null(),
            ),
        # Modification mode
        (0,0), ConditionSwitch(
            "JubesX.Eyewear == 'scouter'", "images/JubesSprite/modification/Jubes_Sprite_Eyewear_Scouter.png",
            "True",Null(),
            ),
        # -----------------
        (0,0), ConditionSwitch(
            #facial spunk
            "'hair' in JubesX.Spunk and Player.Male", "images/JubesSprite/Jubes_Sprite_Spunk_Shades.png",
            "'facial' in JubesX.Spunk and Player.Male", "images/JubesSprite/Jubes_Sprite_Spunk_Facial.png",
            "True", Null(),
            ),
        )
    anchor (0.5, 0.5)
    zoom .37#.38
#    alpha 0.9

image Jubes Blink:
    ConditionSwitch(
    "JubesX.Eyes == 'sexy'", "images/JubesSprite/Jubes_Sprite_Eyes_Sexy.png",
    "JubesX.Eyes == 'side'", "images/JubesSprite/Jubes_Sprite_Eyes_Side.png",
    "JubesX.Eyes == 'surprised'", "images/JubesSprite/Jubes_Sprite_Eyes_Surprised.png",
    "JubesX.Eyes == 'normal'", "images/JubesSprite/Jubes_Sprite_Eyes_Normal.png",
    "JubesX.Eyes == 'stunned'", "images/JubesSprite/Jubes_Sprite_Eyes_Stunned.png",
    "JubesX.Eyes == 'down'", "images/JubesSprite/Jubes_Sprite_Eyes_Down.png",
    "JubesX.Eyes == 'closed'", "images/JubesSprite/Jubes_Sprite_Eyes_Closed.png",
    "JubesX.Eyes == 'leftside'", "images/JubesSprite/Jubes_Sprite_Eyes_Leftside.png",
    "JubesX.Eyes == 'manic'", "images/JubesSprite/Jubes_Sprite_Eyes_Squint.png",
    "JubesX.Eyes == 'squint'", "Jubes_Squint",
    "True", "images/JubesSprite/Jubes_Sprite_Eyes_Normal.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/JubesSprite/Jubes_Sprite_Eyes_Closed.png"
    .25
    repeat

image Jubes_Squint:
    "images/JubesSprite/Jubes_Sprite_Eyes_Sexy.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/JubesSprite/Jubes_Sprite_Eyes_Squint.png"
    .25
    repeat


image Jubes_Drip_Mask:
    #This is the mask for her drip pattern
    contains:
        "images/JubesSprite/Jubes_Sprite_WetMask.png"
        offset (-275,-560)#(-145,-560)#(-225,-560)

#image Jubes_Drip_MaskPanties:
#    #This is the mask for her drip pattern in panties down mode
#    contains:
#        "images/JubesSprite/Jubes_Sprite_DripMaskPanties.png"
#        offset (-145,-560)#(-225,-560)

image Jubes_Drip_MaskP:
    #This is the mask for her drip pattern in panties down mode
    contains:
        "images/JubesSprite/Jubes_Sprite_WetMask_Pants.png"
        offset (-275,-560)#(-145,-560)

# End Jubes Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Jubes Doggy Compositing ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#image Jubes_Doggy_Base = LiveComposite(
image Jubes_Doggy_Animation:
    LiveComposite(
        #Base body
        (420,750),
        (0,0), ConditionSwitch(
            #Shows different upper body motion depending on events
            "not Player.Sprite", "Jubes_Doggy_Body",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Jubes_Doggy_Fuck2_Top",
                    "Speed > 1", "Jubes_Doggy_Fuck_Top",
                    "Speed", "Jubes_Doggy_Anal_Head_Top",
                    "True", "Jubes_Doggy_Body",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Jubes_Doggy_Fuck2_Top",
                    "Speed > 1", "Jubes_Doggy_Fuck_Top",
                    "True", "Jubes_Doggy_Body",
                    ),
            "True", "Jubes_Doggy_Body",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events
            "not Player.Sprite", "Jubes_Doggy_Ass",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Jubes_Doggy_Fuck2_Ass",
                    "Speed > 1", "Jubes_Doggy_Fuck_Ass",
                    "Speed", "Jubes_Doggy_Anal_Head_Ass",
                    "True", "Jubes_Doggy_Ass",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Jubes_Doggy_Fuck2_Ass",
                    "Speed > 1", "Jubes_Doggy_Fuck_Ass",
                    "True", "Jubes_Doggy_Ass",
                    ),
            "True", "Jubes_Doggy_Ass",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events
#            "not Player.Sprite", "Jubes_Doggy_Shins0",
            "Player.Sprite and Player.Cock == 'foot'", ConditionSwitch(
                    "Speed > 1", "Jubes_Doggy_Feet2",
                    "Speed", "Jubes_Doggy_Feet1",
                    "True", "Jubes_Doggy_Feet0",
                    ),
            "ShowFeet", "Jubes_Doggy_Shins0",
            "True", Null(),
            ),
        )
    align (0.6,0.0)
#    yoffset 0
# End Base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Jubes_Doggy_Body:
    LiveComposite(
        #Upper body
        (420,750),
#        (-40,5), ConditionSwitch(
#            #hair back
#            "JubesX.Hair == 'mohawk'", Null(),
#            "JubesX.Hair == 'short'", Null(),
#            "(JubesX.Water and JubesX.Hair == 'long') or JubesX.Hair == 'wet'", "images/JubesDoggy/Jubes_Doggy_Hair_Long_Wet_Back.png",
#            "JubesX.Hair == 'long'", "images/JubesDoggy/Jubes_Doggy_Hair_Long_Back.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #Head
##            "JubesX.Blush > 1", "images/JubesDoggy/Jubes_Doggy_Head_Blush2.png",
#            "JubesX.Blush", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Head_Blush.png",
#            "True", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Head.png",
#            ),
#        (0,0), ConditionSwitch(
#            #Mouth
#            "JubesX.Mouth == 'lipbite'", Recolor("Jubes", "Lips", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Mouth_Smile.png"),
#            "JubesX.Mouth == 'kiss'", Recolor("Jubes", "Lips", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Mouth_Kiss.png"),
#            "JubesX.Mouth == 'sad'", Recolor("Jubes", "Lips", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Mouth_Kiss.png"),
#            "JubesX.Mouth == 'smile'", Recolor("Jubes", "Lips", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Mouth_Smile.png"),
#            "JubesX.Mouth == 'grimace'", Recolor("Jubes", "Lips", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Mouth_Smile.png"),
##            "JubesX.Mouth == 'smirk'", Recolor("Jubes", "Lips", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Mouth_Smirk.png"),
#            "JubesX.Mouth == 'surprised'", Recolor("Jubes", "Lips", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Mouth_Open.png"),
#            "JubesX.Mouth == 'sucking'", Recolor("Jubes", "Lips", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Mouth_Open.png"),
#            "JubesX.Mouth == 'tongue'", Recolor("Jubes", "Lips", "images/JubesDoggy/Jubes_Doggy_Mouth_Tongue.png"),
#            "True", Recolor("Jubes", "Lips", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Mouth_Smirk.png"),
#            ),
##        (-40,5), ConditionSwitch(
##            #chin spunk
##            "'chin' in JubesX.Spunk", "images/JeanDoggy/Jean_Doggy_Spunk_Chin.png",
##            "True", Null(),
##            ),
#        (0,0), ConditionSwitch(
#            #Mouth spunk
#            "'mouth' not in JubesX.Spunk or not Player.Male", Null(),
#            #"JubesX.Mouth == 'normal'", "images/JubesDoggy/Jubes_Doggy_Spunk_Normal.png",
#            #"JubesX.Mouth == 'sad'", "images/JubesDoggy/Jubes_Doggy_Spunk_Normal.png",
##            "JubesX.Mouth == 'lipbite'", "images/JubesDoggy/Jubes_Doggy_Spunk_Smile.png",
##            "JubesX.Mouth == 'smile'", "images/JubesDoggy/Jubes_Doggy_Spunk_Smile.png",
##            "JubesX.Mouth == 'grimace'", "images/JubesDoggy/Jubes_Doggy_Spunk_Smile.png",
#            "JubesX.Mouth == 'sucking'", "images/JubesDoggy/Jubes_Doggy_Spunk_Open.png",
#            "JubesX.Mouth == 'kiss'", "images/JubesDoggy/Jubes_Doggy_Spunk_Kiss.png",
#            "JubesX.Mouth == 'surprised'", "images/JubesDoggy/Jubes_Doggy_Spunk_Open.png",
#            "JubesX.Mouth == 'tongue'", "images/JubesDoggy/Jubes_Doggy_Spunk_Open.png",
#            "True", "images/JubesDoggy/Jubes_Doggy_Spunk_Smile.png",
#            ),
#        (0,0), ConditionSwitch(
#            #Brows
#            "JubesX.Brows == 'angry'", "images/JubesDoggy/Jubes_Doggy_Brows_Angry.png",
#            "JubesX.Brows == 'sad'", "images/JubesDoggy/Jubes_Doggy_Brows_Sad.png",
#            "JubesX.Brows == 'surprised'", "images/JubesDoggy/Jubes_Doggy_Brows_Surprised.png",
#            "True", "images/JubesDoggy/Jubes_Doggy_Brows_Normal.png",
#            ),
#        (0,0), "Jubes Doggy Blink",#Eyes
#        (0,0), ConditionSwitch(
#            #Hair
#            "JubesX.Water or JubesX.Hair == 'wet'", Recolor("Jubes", "Hair", "images/JubesDoggy/Jubes_Doggy_Hair_Wet.png"),
#            "not Player.Male and 'facial' in JubesX.Spunk",Recolor("Jubes", "Hair", "images/JubesDoggy/Jubes_Doggy_Hair_Wet.png"),
#            "JubesX.Hair == 'shades'", Recolor("Jubes", "Hair", "images/JubesDoggy/Jubes_Doggy_Hair_Shades.png"),
#            "True", Recolor("Jubes", "Hair", "images/JubesDoggy/Jubes_Doggy_Hair_Short.png"),
#            ),
##        (0,0), "images/JubesDoggy/Jubes_Doggy_Earring.png",#Eyes
#        (0,0), ConditionSwitch(
#            #face spunk
##            "'hair' in JubesX.Spunk", "images/JubesDoggy/Jubes_Doggy_Spunk_Hair.png",
#            "'facial' in JubesX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Facial.png",
#            "True", Null(),
#            ),
#        #End head

        (0,0), ConditionSwitch(
            #head
            "JubesX.Facing", "Jubes_Doggy_Head_Fore",
            "True", "Jubes_Doggy_Head",
            ),
#        (0,0), "Jubes_Doggy_Head",               #Head
        (0,0), "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Body.png", #Body base

        (0,0), ConditionSwitch(
            #necklace
            "JubesX.Neck == 'choker'", Recolor("Jubes", "Neck", "images/JubesDoggy/Jubes_Doggy_Neck_Choker.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #bra
#            "JubesX.Uptop", ConditionSwitch(
#                    "JubesX.Over and JubesX.Over != 'towel'", Null(),
#                    "JubesX.Chest == 'cami'", "images/JubesDoggy/Jubes_Doggy_Bra_Cami_Up.png",
#                    "JubesX.Chest == 'lace bra'", "images/JubesDoggy/Jubes_Doggy_Bra_Lace.png",
#                    "JubesX.Chest == 'sports bra'", "images/JubesDoggy/Jubes_Doggy_Bra_Sport_Up.png",
#                    "JubesX.Chest == 'bikini top'", "images/JubesDoggy/Jubes_Doggy_Bra_Bikini_Up.png",
#                    "True", "images/JubesDoggy/Jubes_Doggy_Bra.png",
#                    ),
            "JubesX.Chest == 'lace bra'", Recolor("Jubes", "Chest", "images/JubesDoggy/Jubes_Doggy_Chest_Lace.png"),
            "JubesX.Chest == 'sports bra'", Recolor("Jubes", "Chest", "images/JubesDoggy/Jubes_Doggy_Chest_Sport.png"),
            "JubesX.Chest == 'bikini top'", Recolor("Jubes", "Chest", "images/JubesDoggy/Jubes_Doggy_Chest_Bikini.png"),
            # Modification mode
            "JubesX.Chest == 'saiyan leotard'", "images/JubesDoggy/modification/Jubes_Doggy_Chest_Saiyan_Leotard.png",
            # -----------------
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "JubesX.Water", "images/JubesDoggy/Jubes_Doggy_Wet_Body.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Overshirt
            "JubesX.Over == 'red shirt'", Recolor("Jubes", "Over", "images/JubesDoggy/Jubes_Doggy_Over_Red.png"),
            "JubesX.Over == 'black shirt'", Recolor("Jubes", "Over", "images/JubesDoggy/Jubes_Doggy_Over_Black.png"),
            "JubesX.Over == 'tube top'", Recolor("Jubes", "Over", "images/JubesDoggy/Jubes_Doggy_Over_Tube.png"),
            "JubesX.Over == 'towel'", Recolor("Jubes", "Over", "images/JubesDoggy/Jubes_Doggy_Over_Towel.png"),
            "JubesX.Uptop and JubesX.Over == 'dress'", Recolor("Jubes", "Over", "images/JubesDoggy/Jubes_Doggy_Over_Dress_Up.png"),
            "JubesX.Over == 'dress'", Recolor("Jubes", "Over", "images/JubesDoggy/Jubes_Doggy_Over_Dress.png"),
            # Modification mode
            "JubesX.Over == 'saiyan armor'", "images/JubesDoggy/modification/Jubes_Doggy_Over_Saiyan_Armor.png",
            # -----------------
            "True", Null(),
            ),
#        (0,0), "images/JubesDoggy/Jubes_Doggy_Earring.png",
        (0,0), ConditionSwitch(
            #Jacket
            # Modification mode
            "JubesX.Acc == 'saiyan tail'", "images/JubesDoggy/modification/Jubes_Doggy_Saiyan_Tail.png",
            # -----------------
            "JubesX.Acc", Recolor("Jubes", "Acc", "images/JubesDoggy/Jubes_Doggy_Jacket.png"),
            "True", Null(),
            ),


        (0,0), ConditionSwitch(
            #spunk back Layer
            "'back' in JubesX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast fondling animation
            "Trigger == 'fondle breasts' or Trigger2 == 'fondle breasts'", "Jubes_Doggy_GropeBreast",
            "True", Null()
            ),

        )
#    transform_anchor True
#    anchor (225,1400)
#    offset (-20,0)#(-30,0)#(-190,-40)
#    rotate 20
# End Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



image Jubes_Doggy_Head:
    LiveComposite(
        #Upper body
        (420,750),
#        (-40,5), ConditionSwitch(
#            #hair back
#            "JubesX.Hair == 'mohawk'", Null(),
#            "JubesX.Hair == 'short'", Null(),
#            "(JubesX.Water and JubesX.Hair == 'long') or JubesX.Hair == 'wet'", "images/JubesDoggy/Jubes_Doggy_Hair_Long_Wet_Back.png",
#            "JubesX.Hair == 'long'", "images/JubesDoggy/Jubes_Doggy_Hair_Long_Back.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Head
#            "JubesX.Blush > 1", "images/JubesDoggy/Jubes_Doggy_Head_Blush2.png",
            "JubesX.Blush", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Head_Blush.png",
            "True", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Head.png",
            ),
        (0,0), ConditionSwitch(
            #Mouth
            "JubesX.Mouth == 'lipbite'", Recolor("Jubes", "Lips", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Mouth_Smile.png"),
            "JubesX.Mouth == 'kiss'", Recolor("Jubes", "Lips", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Mouth_Kiss.png"),
            "JubesX.Mouth == 'sad'", Recolor("Jubes", "Lips", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Mouth_Kiss.png"),
            "JubesX.Mouth == 'smile'", Recolor("Jubes", "Lips", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Mouth_Smile.png"),
            "JubesX.Mouth == 'grimace'", Recolor("Jubes", "Lips", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Mouth_Smile.png"),
#            "JubesX.Mouth == 'smirk'", Recolor("Jubes", "Lips", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Mouth_Smirk.png"),
            "JubesX.Mouth == 'surprised'", Recolor("Jubes", "Lips", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Mouth_Open.png"),
            "JubesX.Mouth == 'sucking'", Recolor("Jubes", "Lips", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Mouth_Open.png"),
            "JubesX.Mouth == 'tongue'", Recolor("Jubes", "Lips", "images/JubesDoggy/Jubes_Doggy_Mouth_Tongue.png"),
            "True", Recolor("Jubes", "Lips", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Mouth_Smirk.png"),
            ),
#        (-40,5), ConditionSwitch(
#            #chin spunk
#            "'chin' in JubesX.Spunk", "images/JeanDoggy/Jean_Doggy_Spunk_Chin.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Mouth spunk
            "'mouth' not in JubesX.Spunk or not Player.Male", Null(),
            #"JubesX.Mouth == 'normal'", "images/JubesDoggy/Jubes_Doggy_Spunk_Normal.png",
            #"JubesX.Mouth == 'sad'", "images/JubesDoggy/Jubes_Doggy_Spunk_Normal.png",
#            "JubesX.Mouth == 'lipbite'", "images/JubesDoggy/Jubes_Doggy_Spunk_Smile.png",
#            "JubesX.Mouth == 'smile'", "images/JubesDoggy/Jubes_Doggy_Spunk_Smile.png",
#            "JubesX.Mouth == 'grimace'", "images/JubesDoggy/Jubes_Doggy_Spunk_Smile.png",
            "JubesX.Mouth == 'sucking'", "images/JubesDoggy/Jubes_Doggy_Spunk_Open.png",
            "JubesX.Mouth == 'kiss'", "images/JubesDoggy/Jubes_Doggy_Spunk_Kiss.png",
            "JubesX.Mouth == 'surprised'", "images/JubesDoggy/Jubes_Doggy_Spunk_Open.png",
            "JubesX.Mouth == 'tongue'", "images/JubesDoggy/Jubes_Doggy_Spunk_Open.png",
            "True", "images/JubesDoggy/Jubes_Doggy_Spunk_Smile.png",
            ),
        (0,0), ConditionSwitch(
            #Brows
            "JubesX.Brows == 'angry'", "images/JubesDoggy/Jubes_Doggy_Brows_Angry.png",
            "JubesX.Brows == 'sad'", "images/JubesDoggy/Jubes_Doggy_Brows_Sad.png",
            "JubesX.Brows == 'surprised'", "images/JubesDoggy/Jubes_Doggy_Brows_Surprised.png",
            "True", "images/JubesDoggy/Jubes_Doggy_Brows_Normal.png",
            ),
        (0,0), "Jubes Doggy Blink",#Eyes
        # Modification mode
        (0,0), ConditionSwitch(
            #glasses under
            "JubesX.Hair == 'shades'", Recolor("Jubes", "Hair", "images/JubesDoggy/Jubes_Doggy_Hair_Shades.png"),
            "True", Null(),
            ),
        # -----------------
        (0,0), ConditionSwitch(
            #Hair
            "JubesX.Water or JubesX.Hair == 'wet'", Recolor("Jubes", "Hair", "images/JubesDoggy/Jubes_Doggy_Hair_Wet.png"),
            "not Player.Male and 'facial' in JubesX.Spunk",Recolor("Jubes", "Hair", "images/JubesDoggy/Jubes_Doggy_Hair_Wet.png"),
            "JubesX.Hair == 'shades'", Recolor("Jubes", "Hair", "images/JubesDoggy/Jubes_Doggy_Hair_Shades.png"),
            "True", Recolor("Jubes", "Hair", "images/JubesDoggy/Jubes_Doggy_Hair_Short.png"),
            ),
#        (0,0), "images/JubesDoggy/Jubes_Doggy_Earring.png",#Eyes
        (0,0), ConditionSwitch(
            #face spunk
#            "'hair' in JubesX.Spunk", "images/JubesDoggy/Jubes_Doggy_Spunk_Hair.png",
            "'facial' in JubesX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Facial.png",
            "True", Null(),
            ),
        #End head
        (0,0), "images/JubesDoggy/Jubes_Doggy_Earring.png",
        # Modification mode
        (0,0), ConditionSwitch(
            "JubesX.Eyewear == 'scouter'", "images/JubesDoggy/modification/Jubes_Doggy_Eyewear_Scouter.png",
            "True",Null(),
            ),
        # ----------------
        )
#    transform_anchor True
#    anchor (225,1400)
#    offset (-20,0)#(-30,0)#(-190,-40)
#    rotate 20
# End Head animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_Doggy_Head_Fore:
    LiveComposite(
        #Upper body
        (420,750),
        (0,0), ConditionSwitch(
            #Hair
            "JubesX.Water or JubesX.Hair == 'wet'", Recolor("Jubes", "Hair", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Hair_Short_Fore.png"),
            "not Player.Male and 'facial' in JubesX.Spunk",Recolor("Jubes", "Hair", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Hair_Short_Fore.png"),
            "JubesX.Hair == 'shades'", Recolor("Jubes", "Hair", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Hair_Shades_Fore.png"),
            "True", Recolor("Jubes", "Hair", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Hair_Short_Fore.png"),
            ),
        # Modification mode
        (0,0), ConditionSwitch(
            "JubesX.Eyewear == 'scouter'", "images/JubesDoggy/modification/Jubes_Doggy_Eyewear_Scouter_Fore.png",
            "True",Null(),
            ),
        # ----------------
        )
#    transform_anchor True
#    anchor (225,1400)
#    offset (-20,0)#(-30,0)#(-190,-40)
#    rotate 20
# End Head forward animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Jubes Doggy Blink:
        #Eyes
        ConditionSwitch(
        "JubesX.Eyes == 'sexy'", "images/JubesDoggy/Jubes_Doggy_Eyes_Sexy.png",
        "JubesX.Eyes == 'side'", "images/JubesDoggy/Jubes_Doggy_Eyes_Side.png",
#        "JubesX.Eyes == 'normal'", "images/JubesDoggy/Jubes_Doggy_Eyes_Normal.png",
        "JubesX.Eyes == 'closed'", "images/JubesDoggy/Jubes_Doggy_Eyes_Closed.png",
        "JubesX.Eyes == 'manic'", "images/JubesDoggy/Jubes_Doggy_Eyes_Surprised.png",
        "JubesX.Eyes == 'down'", "images/JubesDoggy/Jubes_Doggy_Eyes_Down.png",
        "JubesX.Eyes == 'stunned'", "images/JubesDoggy/Jubes_Doggy_Eyes_Stunned.png",
        "JubesX.Eyes == 'surprised'", "images/JubesDoggy/Jubes_Doggy_Eyes_Surprised.png",
        "JubesX.Eyes == 'squint'", "images/JubesDoggy/Jubes_Doggy_Eyes_Sexy.png",
        "True", "images/JubesDoggy/Jubes_Doggy_Eyes_Normal.png",
        ),
    #    choice:
    #        3.5
    #    choice:
    #        3.25
    #    choice:
    #        3
        3
        # This randomizes the time between blinking.
        "images/JubesDoggy/Jubes_Doggy_Eyes_Closed.png"
        .25
        repeat

image Jubes_Doggy_Ass:
    LiveComposite(
        #Lower body
        (420,750),

        (205,530), ConditionSwitch(    #165,560
            #Personal Wetness
            "not JubesX.Wet", Null(),
            "(JubesX.Legs == 'pants' or JubesX.Legs == 'shorts') and not JubesX.Upskirt", Null(),
            "JubesX.Panties and not JubesX.PantiesDown", Null(),
            "JubesX.Wet == 1", "Wet_Drip",
            "True", "Wet_Drip2",
            ),

        (205,530), ConditionSwitch(    #275,560
            #Spunk
            "('in' not in JubesX.Spunk and 'anal' not in JubesX.Spunk) or not Player.Male", Null(),
            "(JubesX.Legs == 'pants' or JubesX.Legs == 'shorts') and not JubesX.Upskirt", Null(),
            "JubesX.Panties and not JubesX.PantiesDown", Null(),
            "True","Spunk_Drip2",
            ),
        (0,0), ConditionSwitch(
            #ass base
#            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
##                    "Speed > 2", "Jubes_Pussy_Fucking3",#Speed 3
##                    "Speed > 1", "Jubes_Pussy_Fucking2",#Speed 2
#                    "Speed", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Ass_Base.png",      #Speed 1
#                    "True", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Ass_Base.png",              #Speed 0
#                    ),
            "Trigger == 'lick pussy'", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Ass_Open.png",
            "JubesX.Legs and not JubesX.Upskirt", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Ass_Closed.png",
            "JubesX.Panties and not JubesX.PantiesDown", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Ass_Closed.png",
            "Player.Sprite and Player.Cock == 'in'", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Ass_Fucking.png",
            "'dildo pussy' in (Trigger,Trigger2,JubesX.Offhand)", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Ass_Fucking.png",
            "'fondle pussy' in (Trigger,Trigger2,JubesX.Offhand)", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Ass_Fucking.png",
            "Trigger == 'insert pussy'", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Ass_Fucking.png",
            "True", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Ass_Closed.png",
            ),

        (0,0), ConditionSwitch(
            #ass red
            "JubesX.Red", "images/JubesDoggy/Jubes_Doggy_Red.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "JubesX.Water", "images/JubesDoggy/Jubes_Doggy_Wet_Ass.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #Hose
            "JubesX.Hose == 'socks'", Recolor("Jubes", "Hose", "images/JubesDoggy/Jubes_Doggy_Hose_Socks.png"),
            "JubesX.Hose == 'stockings'", Recolor("Jubes", "Hose", "images/JubesDoggy/Jubes_Doggy_Hose_Stockings.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Panties if Down
            "not JubesX.PantiesDown or (JubesX.Legs and JubesX.Legs != 'skirt' and not JubesX.Upskirt)", Null(),

            "not JubesX.Panties", Null(),
            # Modification mode
            "JubesX.Panties == 'saiyan leotard'", Null(),
            # -----------------
            "JubesX.Panties == 'lace panties'", Recolor("Jubes", "Panties", "images/JubesDoggy/Jubes_Doggy_Panties_Lace_Down.png"),
            "JubesX.Panties == 'tiger panties' and JubesX.Wet", Recolor("Jubes", "Panties", "images/JubesDoggy/Jubes_Doggy_Panties_Tiger_DownW.png"),
            "JubesX.Panties == 'tiger panties'", Recolor("Jubes", "Panties", "images/JubesDoggy/Jubes_Doggy_Panties_Tiger_Down.png"),
            "JubesX.Panties == 'bikini bottoms' and JubesX.Wet", Recolor("Jubes", "Panties", "images/JubesDoggy/Jubes_Doggy_Panties_Bikini_DownW.png"),
            "JubesX.Panties == 'bikini bottoms'", Recolor("Jubes", "Panties", "images/JubesDoggy/Jubes_Doggy_Panties_Bikini_Down.png"),
            "JubesX.Wet", "images/JubesDoggy/Jubes_Doggy_Panties_Blue_DownW.png",
            "True", "images/JubesDoggy/Jubes_Doggy_Panties_Blue_Down.png",
            ),

#        (0,0), ConditionSwitch(
#            #Legs Layer if down behind cock
#            "not JubesX.Upskirt", Null(),
#            "JubesX.Legs == 'pants'",  Recolor("Jubes", "Legs", "images/JubesDoggy/Jubes_Doggy_Legs_Pants_Down.png"),
#            "JubesX.Legs == 'shorts'", Recolor("Jubes", "Legs", "images/JubesDoggy/Jubes_Doggy_Legs_Shorts_Down.png"),
#            "True", Null(),
#            ),

#        (0,0), ConditionSwitch(
#            #Legs Layer if down
#            "JubesX.Legs == 'pants' and JubesX.Upskirt", Recolor("Jubes", "Legs", "images/JubesDoggy/Jubes_Doggy_Legs_Pants_Down.png"),
##            "JubesX.Legs == 'yoga pants' and JubesX.Upskirt", "images/JubesDoggy/Jubes_Doggy_Legs_Yoga_Down.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #Pussy Composite
#            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
#                    "Speed > 2", "Jubes_Pussy_Fucking3",#Speed 3
#                    "Speed > 1", "Jubes_Pussy_Fucking2",#Speed 2
#                    "Speed", "Jubes_Pussy_Heading",      #Speed 1
#                    "True", "Jubes_Pussy_Static",              #Speed 0
#                    ),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Jubes_Pussy_Fingering",
#            "Trigger == 'dildo pussy'", "Jubes_Pussy_Fucking2",
#            "True",Null(),
##            "True", "images/JubesDoggy/Jubes_Doggy_Pussy_Closed.png",
#            ),

        (0,0), ConditionSwitch(
            #pubes
            "not JubesX.Pubes", Null(),
            "Player.Sprite and Player.Cock == 'in'", Null(), # "images/JubesDoggy/Jubes_Doggy_Pubes_Fucked.png",
            "'dildo pussy' in (Trigger,Trigger2,JubesX.Offhand)", Null(),
            "'fondle pussy' in (Trigger,Trigger2,JubesX.Offhand)",Null(),
            "Trigger == 'insert pussy'", Null(),
            "(JubesX.Legs and JubesX.Legs != 'skirt') and not JubesX.Upskirt", Null(),
            "JubesX.Panties and JubesX.PantiesDown and Trigger == 'lick pussy'", Recolor("Jubes", "Pubes", "images/JubesDoggy/Jubes_Doggy_Pubes_Open.png"),
            "JubesX.Panties and JubesX.PantiesDown", Recolor("Jubes", "Pubes", "images/JubesDoggy/Jubes_Doggy_Pubes_Closed.png"),
            "JubesX.Panties", Recolor("Jubes", "Pubes", "images/JubesDoggy/Jubes_Doggy_Pubes_Clothed.png"),
            "JubesX.Hose == 'pantyhose' and Trigger == 'lick pussy'", Recolor("Jubes", "Pubes", "images/JubesDoggy/Jubes_Doggy_Pubes_Clothed.png"),
            "JubesX.Hose == 'pantyhose'", Recolor("Jubes", "Pubes", "images/JubesDoggy/Jubes_Doggy_Pubes_Clothed.png"),
            "Trigger == 'lick pussy'", Recolor("Jubes", "Pubes", "images/JubesDoggy/Jubes_Doggy_Pubes_Open.png"),
            "True", Recolor("Jubes", "Pubes", "images/JubesDoggy/Jubes_Doggy_Pubes_Closed.png"),
            ),

        (0,0), ConditionSwitch(
            #spunkpussy Layer
#            "'in' in JubesX.Spunk and Player.Sprite and Player.Cock == 'in'",Null(),# "images/JeanDoggy/Jean_Doggy_SpunkPussyOpen.png",  #fix for JubesX.Spunk is used later
            "'in' in JubesX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "JubesX.Wet and Player.Cock == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "JubesX.Wet", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Pussy Piercings
            "Player.Sprite and Player.Cock == 'in'", Null(),
            "'dildo pussy' in (Trigger,Trigger2,JubesX.Offhand)", Null(),
            "'fondle pussy' in (Trigger,Trigger2,JubesX.Offhand)",Null(),
            "Trigger == 'insert pussy'", Null(),
            "JubesX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_Barbell.png",
            "JubesX.Panties and not JubesX.PantiesDown", Null(),
            "JubesX.Legs and not JubesX.Upskirt", Null(),
#            "JubesX.Pierce == 'ring' and JubesX.Hose == 'pantyhose' and not (JubesX.Panties and JubesX.PantiesDown)", "images/JubesDoggy/Jubes_Doggy_Pierce_RingC2.png",
#            "JubesX.Pierce == 'ring' and JubesX.Legs and JubesX.Legs != 'skirt' and not JubesX.Upskirt", "images/JubesDoggy/Jubes_Doggy_Pierce_RingC2.png",
            "JubesX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_Ring.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch( #remove later if works                                                                                #remove later if works
            #New ass base check
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 1", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Anal_FullBase.png",
            "'insert ass' in (Trigger,Trigger2,JubesX.Offhand)", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Anal_FullBase.png",
            "'dildo anal' in (Trigger,Trigger2,JubesX.Offhand)", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Anal_FullBase.png",
            "JubesX.Loose > 2", "Jubes_Gape_Anal",
#            "JubesX.Legs and not JubesX.Upskirt", "images/JubesDoggy/Jubes_Doggy_Asshole_Loose.png",
#            "JubesX.Panties and not JubesX.PantiesDown", "images/JubesDoggy/Jubes_Doggy_Asshole_Loose.png",
            "JubesX.Loose", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
            "True", "images/JeanDoggy/Jean_Doggy_Asshole_Tight.png",
            ),

        (0,4), ConditionSwitch(
            #spunkanal Layer
            "'anal' not in JubesX.Spunk or (Player.Sprite and Player.Cock == 'anal' and Speed >= 1) or not Player.Male", Null(),
#            "Player.Cock == 'anal'", "images/RogueDoggy/Rogue_Doggy_SpunkAnalOpen.png",
            "JubesX.Loose", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Loose.png",
            "True", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Loose.png",
            ),

        (0,0), ConditionSwitch(
            #Panties if up
            "JubesX.PantiesDown or not JubesX.Panties", Null(),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),
            "JubesX.Panties == 'lace panties'", Recolor("Jubes", "Panties", "images/JubesDoggy/Jubes_Doggy_Panties_Lace.png"),
            "JubesX.Panties == 'tiger panties' and JubesX.Wet", Recolor("Jubes", "Panties", "images/JubesDoggy/Jubes_Doggy_Panties_TigerW.png"),
            "JubesX.Panties == 'tiger panties'", Recolor("Jubes", "Panties", "images/JubesDoggy/Jubes_Doggy_Panties_Tiger.png"),
#            "JubesX.Panties == 'bikini bottoms' and JubesX.Wet", "images/JubesDoggy/Jubes_Doggy_Panties_BikiniW.png",
            "JubesX.Panties == 'bikini bottoms'", Recolor("Jubes", "Panties", "images/JubesDoggy/Jubes_Doggy_Panties_Bikini.png"),
            # Modification mode
            "JubesX.Panties == 'saiyan leotard'", "images/JubesDoggy/modification/Jubes_Doggy_Panties_Saiyan_Leotard.png",
            # -----------------
            "JubesX.Wet", "images/JubesDoggy/Jubes_Doggy_Panties_BlueW.png",
            "True", "images/JubesDoggy/Jubes_Doggy_Panties_Blue.png",
            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #full hose/tights
#            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),
#            "JubesX.Panties and JubesX.PantiesDown and JubesX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "JubesX.Hose == 'garterbelt'", Recolor("Jubes", "Hose", "images/JubesDoggy/Jubes_Doggy_Hose_Garter.png"),
            "JubesX.Hose == 'stockings and garterbelt'", Recolor("Jubes", "Hose", "images/JubesDoggy/Jubes_Doggy_Hose_StockingsGarter.png"),
            "JubesX.Panties and JubesX.PantiesDown", Null(),
            "JubesX.Hose == 'pantyhose'", Recolor("Jubes", "Hose", "images/JubesDoggy/Jubes_Doggy_Hose_Pantyhose.png"),
            "JubesX.Hose == 'ripped pantyhose'", Recolor("Jubes", "Hose", "images/JubesDoggy/Jubes_Doggy_Hose_Pantyhose_Holed.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Pussy Piercings over clothes
            "Player.Sprite", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),
            "not JubesX.Panties and JubesX.Hose != 'pantyhose'", Null(),
            "((JubesX.Panties or JubesX.Hose == 'pantyhose') and JubesX.PantiesDown)", Null(),
                #if she has panties, but they are down, or pantyhose, or Legs that are not a skirt and are not down, skip these. . .
            "JubesX.Pierce == 'barbell' and JubesX.Panties == 'lace panties'", "images/JubesDoggy/Jubes_Doggy_Pierce_Barbell_Lace.png",
            "JubesX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_Barbell_Blue.png",
            "JubesX.Pierce == 'ring' and JubesX.Panties == 'lace panties'", "images/JubesDoggy/Jubes_Doggy_Pierce_Ring_Lace.png",
            "JubesX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_Ring_Blue.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs Layer if down behind cock
            "not JubesX.Upskirt", Null(),
            "JubesX.Legs == 'pants'",  Recolor("Jubes", "Legs", "images/JubesDoggy/Jubes_Doggy_Legs_Pants_Down.png"),
            "JubesX.Legs == 'shorts'", Recolor("Jubes", "Legs", "images/JubesDoggy/Jubes_Doggy_Legs_Shorts_Down.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Legs Layer
#            "JubesX.Upskirt and JubesX.Legs == 'dress' and JubesX.Over == 'dress'", Recolor("Jubes", "Over", "images/JubesDoggy/Jubes_Doggy_Legs_Dress_Up.png"),
#            "JubesX.Legs == 'dress' and JubesX.Over == 'dress'", Recolor("Jubes", "Over", "images/JubesDoggy/Jubes_Doggy_Legs_Dress.png"),
            "JubesX.Upskirt and JubesX.Legs == 'skirt'", Recolor("Jubes", "Over", "images/JubesDoggy/Jubes_Doggy_Legs_Dress_Up.png"),
            "JubesX.Legs == 'skirt'", Recolor("Jubes", "Over", "images/JubesDoggy/Jubes_Doggy_Legs_Dress.png"),
            "JubesX.Upskirt", Null(),

            "JubesX.Legs == 'pants'", ConditionSwitch(
#                    "JubesX.Upskirt", Null(),
#                    "JubesX.Upskirt", Recolor("Jubes", "Legs", "images/JubesDoggy/Jubes_Doggy_Legs_Pants_Down.png"),
#                    "JubesX.Wet > 1", "images/JubesDoggy/Jubes_Doggy_Legs_Pants_W.png",
                    "True", Recolor("Jubes", "Legs", "images/JubesDoggy/Jubes_Doggy_Legs_Pants.png"),
                    ),
#            "JubesX.Legs == 'yoga pants'", ConditionSwitch(
##                    "JubesX.Upskirt", Null(),
#                    "JubesX.Upskirt", "images/JubesDoggy/Jubes_Doggy_Legs_Yoga_Down.png",
#                    "JubesX.Wet > 1", "images/JubesDoggy/Jubes_Doggy_Legs_Yoga_W.png",
#                    "True", "images/JubesDoggy/Jubes_Doggy_Legs_Yoga.png",
#                    ),
            "JubesX.Legs == 'shorts'", ConditionSwitch(
#                    "JubesX.Upskirt", Null(),
#                    "JubesX.Upskirt", Recolor("Jubes", "Legs", "images/JubesDoggy/Jubes_Doggy_Legs_Shorts_Down.png"),
                    "JubesX.Wet > 1", Recolor("Jubes", "Legs", "images/JubesDoggy/Jubes_Doggy_Legs_ShortsW.png"),
                    "True", Recolor("Jubes", "Legs", "images/JubesDoggy/Jubes_Doggy_Legs_Shorts.png"),
                    ),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Pussy Composite
            "JubesX.Legs and not JubesX.Upskirt",Null(),
            "JubesX.Panties and not JubesX.PantiesDown", Null(),
            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Jubes_Pussy_Fucking3",#Speed 3
                    "Speed > 1", "Jubes_Pussy_Fucking2",#Speed 2
                    "Speed", "Jubes_Pussy_Heading",      #Speed 1
                    "True", "Jubes_Pussy_Static",              #Speed 0
                    ),
            "'dildo pussy' in (Trigger,Trigger2,JubesX.Offhand)", "Jubes_Pussy_Fucking2",
            "'fondle pussy' in (Trigger,Trigger2,JubesX.Offhand)", "Jubes_Pussy_Fingering",
            "Trigger == 'insert pussy'", "Jubes_Pussy_Fingering",
            "True",Null(),
            ),

        (0,0), ConditionSwitch(
            #Anus Composite
            "JubesX.Legs and not JubesX.Upskirt",Null(),
            "JubesX.Panties and not JubesX.PantiesDown", Null(),
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Jubes_Anal_Fucking2", #Speed 3
                    "Speed > 1", "Jubes_Anal_Fucking",  #Speed 2
                    "Speed", "Jubes_Anal_Heading",      #Speed 1
                    "True", "Jubes_Anal",               #Speed 0
                    ),
            "'insert ass' in (Trigger,Trigger2,JubesX.Offhand)", "Jubes_Anal_Fingering",
            "'dildo anal' in (Trigger,Trigger2,JubesX.Offhand)", "Jubes_Anal_Fucking",
            "JubesX.Plug", "images/PlugIn.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #dress Layer
            "JubesX.Over == 'dress' and JubesX.Upskirt", Recolor("Jubes", "Over", "images/JubesDoggy/Jubes_Doggy_Legs_Dress_Up.png"),
            "JubesX.Over == 'dress'", Recolor("Jubes", "Over", "images/JubesDoggy/Jubes_Doggy_Legs_Dress.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Jacket
            # Modification mode
            "JubesX.Acc == 'saiyan tail'", Null(),
            # -----------------
            "(JubesX.Over == 'dress' or JubesX.Legs == 'skirt') and JubesX.Upskirt", Null(),
            "JubesX.Acc or JubesX.Over == 'towel'", Recolor("Jubes", "Acc", "images/JubesDoggy/Jubes_Doggy_Jacket_Butt.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #spunk back Layer
            "'back' in JubesX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Ass.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy'", "Rogue_Doggy_Lick_Pussy",
            "Trigger == 'lick ass'", "Rogue_Doggy_Lick_Ass",
            "True", Null()
            ),
        (-1,0), ConditionSwitch(
            #Hotdogging underlayer
            "not Player.Sprite or Player.Cock != 'out'", Null(),
#            "KittyX.Legs == 'skirt' and KittyX.Upskirt", "images/JeanDoggy/Jean_Doggy_Hotdog_Upskirt_Back.png",
            "True", "images/KittyDoggy/Kitty_Doggy_HotdogBack.png",
            ),
        (0,0), ConditionSwitch(
            #Hotdogging Cock w/ alpha
            "not Player.Sprite or Player.Cock != 'out'", Null(),
            #"KittyX.Legs == 'skirt' and KittyX.Upskirt and Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            #"KittyX.Legs == 'skirt' and KittyX.Upskirt", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
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
# End Ass animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Jubes_Doggy_Feet:
    contains:
            AlphaMask("Jubes_Doggy_Shins", "images/JubesDoggy/Jubes_Doggy_Feet_Mask.png")
    contains:
        #spunk
        ConditionSwitch(
            "'feet' in JubesX.Spunk", "images/JubesDoggy/Jubes_Doggy_Spunk_Feet.png",
            "True", Null(),
            )

image Jubes_Doggy_Shins:
    #Jubes's footjob shins
#    contains:
#            #feet
#            "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Feet.png"
    contains:
            #hose legs
        ConditionSwitch(
            "JubesX.Hose == 'ripped pantyhose'", Recolor("Jubes", "Hose", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Feet_Hose_Holed.png"),
            "JubesX.Hose == 'socks'", Recolor("Jubes", "Hose", "images/JubesDoggy/Jubes_Doggy_Feet_Socks.png"),
            "JubesX.Hose and JubesX.Hose != 'garterbelt'", Recolor("Jubes", "Hose", "images/JubesDoggy/Jubes_Doggy_Feet_Hose.png"),
            "True", "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Feet.png"
            )
    contains:
        #pants
        ConditionSwitch(
            "JubesX.Legs == 'pants'", Recolor("Jubes", "Legs", "images/JubesDoggy/Jubes_Doggy_Feet_Pants.png"),
            "True", Null(),
            )
    contains:
        #spunk
        ConditionSwitch(
            "'feet' in JubesX.Spunk", "images/JubesDoggy/Jubes_Doggy_Spunk_Feet.png",
            "True", Null(),
            )

image Jubes_Doggy_Shins0:
        #static animation
        "Jubes_Doggy_Shins"
        offset (0, 80) #(0,0) top

image Jubes_Doggy_GropeBreast:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        xzoom -.55
        yzoom .55
        offset (150,340)#(110,420)
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
        block:
            ease 1 rotate 10#60
            ease 1 rotate 0#90
            repeat


image Jubes_Gape_Anal:
        #animation for her asshole growing and shrinking a bit when over 2 Looseness
        contains:
            subpixel True
            "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Anal_GapeBase.png"
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


image Zero_Jubes_Hotdog_Static:
    # The unmoving version of the hotdog cock
    # called in Doggy Ass LC
    contains:
        "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Jubes_Hotdog_Moving:
    # The moving version of the hotdog cock
    # called in Doggy Ass LC
    contains:
        "Zero_Doggy_Up"
        pos (175, 370)
        block:
            ease 1 ypos 330
            ease 1 ypos 420
            repeat

# Animation for pussy static action / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Jubes_Pussy_Static:
    #Full Animation for speed 0
    subpixel True
#    contains:
#        #Base
#        "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Pussy_FBase.png"
#        anchor (0.52,0.69)
#        pos (220,518)
#        xzoom .8
    contains:
        #moving hole
        "images/JubesDoggy/Jubes_Doggy_Pussy_Heading.png"
        subpixel True

        transform_anchor True
        anchor (0.515,0.69)#(0.52,0.69)
        pos (219,518) #(221,518)
        xzoom .9
        block:
            ease 1 xzoom 1.1
            pause 1
            ease 3 xzoom .9
            repeat
    contains:
        #moving hole
        "images/JubesDoggy/Jubes_Doggy_Pussy_HHole.png"
        subpixel True
        anchor (217,545)#(217,550)
        transform_anchor True
        pos (220,550) #(217,540)
        xzoom .3
        yzoom .4
        parallel:
            ease 1 xzoom .8#.6
            pause 1
            ease 3 xzoom .3#.2
            repeat
        parallel:
            ease 1 yzoom .8#.6
            pause 1
            ease 3 yzoom .4#.2
            repeat
    contains:
        #pubes
        ConditionSwitch(
            "JubesX.Pubes", Recolor("Jubes", "Pubes", "images/JubesDoggy/Jubes_Doggy_Pubes_Open.png"),
            "True", Null(),
            )
        subpixel True
        transform_anchor True
        anchor (0.515,0.69)#(0.52,0.69)
        pos (219,518) #(221,518)
#        anchor (0.52,0.69)
#        pos (221,518) #(220,518)
        xzoom .9
        block:
            ease .9 xzoom 1 #.95
            pause 1.6
            ease 2.5 xzoom .9#.8
            repeat
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "JubesX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_Barbell.png",
            "JubesX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_Ring.png",
            "True", Null(),
            )
        offset (2,0)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in JubesX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.52,0.69)
        pos (221,516)
        xzoom .9
        block:
            ease 1 xzoom 1.1
            pause 1
            ease 3 xzoom .9
            repeat
    contains:
        #Cock
        AlphaMask("Zero_Jubes_Doggy_Static", "Jubes_Pussy_Mask_Static")


image Zero_Jubes_Doggy_Static:
    # Sex Speed 0 motions
    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (175,550)
#        alpha 0.9
        block:
            ease 1 ypos 540 #in stroke
            pause 1
            ease 3 ypos 550 #out stroke 545
            repeat

image Jubes_Pussy_Mask_Static:
    #AlphaMask used to prevent the cock from moving past the pussy in static pose
    #Called in "Jubes_Pussy_Moving"
    contains:
        #Base
        subpixel True
#        "images/RogueDoggy/Rogue_Doggy_SexMask.png"
        "images/JubesDoggy/Jubes_Doggy_Pussy_MaskHeading.png"
        anchor (0.52,0.69)
        pos (220,525)
        xzoom 1
        parallel:
            ease .9 ypos 524#526
            pause 2.1
            ease 2 ypos 525#528
            repeat




# Animation for pussy heading action / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Jubes_Pussy_Heading:
    #Full Animation for speed 1
    subpixel True
#    contains:
#        #Base
#        "images/JubesDoggy/[JubesX.skin_image.skin_path]Jubes_Doggy_Pussy_FBase.png"
#        anchor (0.52,0.69)
#        pos (220,518) # fix this back once re-exported(217,518)
#        xzoom 1
    contains:
        #moving hole
        "images/JubesDoggy/Jubes_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.515,0.69)#(0.52,0.69)
        pos (219,518) #(221,518)
        xzoom .6
        block:
            ease .9 xzoom 1
            pause 1.6
            ease 2.5 xzoom .6
            repeat
    contains:
        #pubes
        ConditionSwitch(
            "JubesX.Pubes", Recolor("Jubes", "Pubes", "images/JubesDoggy/Jubes_Doggy_Pubes_Open.png"),
            "True", Null(),
            )
        subpixel True
        anchor (0.52,0.69)
        pos (221,518) #(220,518)
        xzoom 1
        block:
            ease .9 xzoom 1.2
            pause 1.6
            ease 2.5 xzoom 1
            repeat
        offset (2,0)
#    contains:
#        ConditionSwitch(
#            #full hose/tights
#            "JubesX.Hose == 'socks'", Recolor("Jubes", "Hose", "images/JubesDoggy/Jubes_Doggy_Hose_Socks.png"),
#            "JubesX.Hose == 'garterbelt'", Recolor("Jubes", "Hose", "images/JubesDoggy/Jubes_Doggy_Hose_Garter.png"),
#            "JubesX.Hose == 'stockings and garterbelt'", Recolor("Jubes", "Hose", "images/JubesDoggy/Jubes_Doggy_Hose_StockingsGarter.png"),
#            "JubesX.Panties and JubesX.PantiesDown", Null(),
#            "JubesX.Hose == 'ripped pantyhose'", Recolor("Jubes", "Hose", "images/JubesDoggy/Jubes_Doggy_Hose_Pantyhose_Holed.png"),
#            "True", Null(),
#            )
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "JubesX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_BarbellF.png",
            "JubesX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_RingF.png",
            "True", Null(),
            )
        offset (2,0)

    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in JubesX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.52,0.75) #(0.52,0.69)
        pos (221,560) #(220,518)
        xzoom .6
        block:
            ease .9 xzoom 1
            pause 1.6
            ease 2.5 xzoom .6
            repeat
        offset (2,0)
    contains:
        #Cock
        AlphaMask("Zero_Jubes_Doggy_Heading", "Jubes_Pussy_Mask")
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in JubesX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.515,0.75)#(0.52,0.69)
        pos (219,560) #(221,518)
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
#        offset (2,0)

image Zero_Jubes_Doggy_Heading:
    # Sex Speed 1 motions
    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (173,545) #(171,545)
#        alpha 0.6
        block:
            ease 1 ypos 500 #in stroke xpos 168
            pause 1
            ease 3 ypos 545 #out stroke xpos 171
            repeat

image Jubes_Pussy_Mask:
    #AlphaMask used to prevent the cock from moving past the pussy
    #Called in "Jean_Pussy_Moving"
    contains:
        #Base
        "images/JubesDoggy/Jubes_Doggy_Pussy_MaskHeading.png"
        anchor (0.52,0.69)
        pos (221,518)
        xzoom .8
        parallel:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .8
            repeat
        parallel:
            ease 1 ypos 520#518
            pause 1
            ease 3 ypos 528
            repeat


image Jubes_Pussy_Fingering:
    #Full Animation for speed 1
    subpixel True
    contains:
        #moving hole
        "images/JubesDoggy/Jubes_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (221,518)
        xzoom .6
        block:
            ease .9 xzoom .85
            pause 1.6
            ease 2.5 xzoom .6
            repeat
    contains:
        #pubes
        ConditionSwitch(
            "JubesX.Pubes", Recolor("Jubes", "Pubes", "images/JubesDoggy/Jubes_Doggy_Pubes_Open.png"),
            "True", Null(),
            )
        subpixel True
        anchor (0.52,0.69)
        pos (221,518) #(220,518)
        xzoom 1
        block:
            ease .9 xzoom 1.2
            pause 1.6
            ease 2.5 xzoom 1
            repeat
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "JubesX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_BarbellF.png",
            "JubesX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_RingF.png",
            "True", Null(),
            )
        xoffset 2


    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in JubesX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.52,0.75) #(0.52,0.69)
        pos (221,560) #(220,518)
        xzoom .6
        block:
            ease .9 xzoom 1
            pause 1.6
            ease 2.5 xzoom .6
            repeat
        offset (2,0)
    contains:
        #Cock
        AlphaMask("Zero_Pussy_Finger", "Jubes_Pussy_Mask_Finger")
        xoffset 3
        alpha .6
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in JubesX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.515,0.75)#(0.52,0.69)
        pos (219,560) #(221,518)
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
#        offset (2,0)

image Jubes_Pussy_Mask_Finger:
    #AlphaMask used to prevent the cock from moving past the pussy
    #Called in "Jean_Pussy_Moving"
    contains:
        #Base
        "images/JubesDoggy/Jubes_Doggy_Pussy_MaskHeading.png"
        anchor (0.52,0.69)
        pos (218,526) #(221,518)
        xzoom .8
        parallel:
            ease 1 ypos 521 #518
            pause 1
            ease 3 ypos 526 # 528
            repeat

# > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

image Jubes_Pussy_Fucking2:
    #Full Animation for speed 2
    contains:
        #Base
        offset (2,0)
        "images/JubesDoggy/Jubes_Doggy_Pussy_FHole.png"
    contains:
        #pubes
        ConditionSwitch(
            "JubesX.Pubes", Recolor("Jubes", "Pubes", "images/JubesDoggy/Jubes_Doggy_Pubes_Fucking.png"),
            "True", Null(),
            )
        offset (2,0)
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "JubesX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_BarbellF.png",
            "JubesX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_RingF.png",
            "True", Null(),
            )
        offset (0,0)
    contains:
        #spunk
        ConditionSwitch(
            "'in' in JubesX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
        offset (2,0)
    contains:
        #Cock
        offset (2,0)
        ConditionSwitch(
            "'dildo pussy' in (Trigger,Trigger2,JubesX.Offhand)", AlphaMask("Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            #this might cause timing issue if multiple things can use it. Watch out.
            "True",AlphaMask("Zero_Jubes_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            )
    contains:
        #spunk
        ConditionSwitch(
            "'in' in JubesX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )
        offset (2,0)

image Zero_Jubes_Doggy_Fucking2:
    # Sex Speed 2 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)#(169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat


image Jubes_Pussy_Fucking3:
    #Full Animation for speed 3
    contains:
        #Base
        offset (2,0)
        "images/JubesDoggy/Jubes_Doggy_Pussy_FHole.png"
    contains:
        #pubes
        ConditionSwitch(
            "JubesX.Pubes", Recolor("Jubes", "Pubes", "images/JubesDoggy/Jubes_Doggy_Pubes_Fucking.png"),
            "True", Null(),
            )
        offset (2,0)
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "JubesX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_BarbellF.png",
            "JubesX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_RingF.png",
            "True", Null(),
            )
        offset (0,0)
    contains:
        #spunk
        ConditionSwitch(
            "'in' in JubesX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
        offset (2,0)
    contains:
        #Cock
        offset (2,0)
        AlphaMask("Zero_Jubes_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
    contains:
        #spunk
        ConditionSwitch(
            "'in' in JubesX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )
        offset (2,0)

image Zero_Jubes_Doggy_Fucking3:
    # Sex Speed 3 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .2 ypos 440
            pause .1
            ease .6 ypos 500
            repeat


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

image Jubes_Anal:
    #Anal static Loose
    contains:
        #Cock
        "Zero_Doggy_Insert"
        pos (172,500)

image Jubes_Anal_Fingering:
    #Animation for speed 1
    contains:
        #Hole
        subpixel True
        "images/JubesDoggy/Jubes_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .6
        block:
            ease .5 zoom .75#1
            pause .5
            ease 1.5 zoom .6
            repeat
    contains:
        #spunk under cock
        subpixel True
        ConditionSwitch(
            "'anal' in JubesX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
        anchor (0.52,0.71) #(0.52,0.69)
        pos (218,530)#(218,518)
        zoom .7
        block:
            ease .5 zoom .8
            pause .5
            ease 1.5 zoom .7
            repeat
    contains:
        #Cock with mask
        AlphaMask("Zero_Jubes_Doggy_Anal_Finger", "Jubes_Doggy_Anal_Fingering_Mask")
    contains:
        #spunk over cock
        subpixel True
        ConditionSwitch(
            "'anal' in JubesX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
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

image Zero_Jubes_Doggy_Anal_Finger:
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
image Jubes_Doggy_Anal_Fingering_Mask:
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
image Jubes_Anal_Heading:
    #Animation for speed 1
    contains:
        #Hole
        "images/JubesDoggy/Jubes_Doggy_Anal_FullHole.png"
        anchor (0.52,0.71) #(0.52,0.69)
        pos (218,530)#(218,518)
        zoom .5
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .5
            repeat
    contains:
        #spunk under cock
        ConditionSwitch(
            "'anal' in JubesX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
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
        AlphaMask("Zero_Jubes_Doggy_Anal_Heading", "Jubes_Doggy_Anal_Heading_Mask")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in JubesX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
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

image Zero_Jubes_Doggy_Anal_Heading:
        #the cock anal heading animation
    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 505#500 out
            repeat


image Jubes_Doggy_Anal_Heading_Mask:
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


image Jubes_Doggy_Anal_Head_Top:
#animation for anal fucking top half
    contains:
        subpixel True
        "Jubes_Doggy_Body"
        ypos 0
        block:
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat

image Jubes_Doggy_Anal_Head_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Jubes_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -10
            easeout .1 ypos -7
            easein .9 ypos 0
            pause .9
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Jubes_Doggy_Anal1:
    #Animation for speed 2 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat

image Jubes_Anal_Fucking:
    #Animation for speed 2 Ass
    contains:
        #Hole
        "images/JubesDoggy/Jubes_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .98
        block:
            pause .25
            ease .25 zoom 1
            pause .75
            ease 1 zoom .98
            pause .25
            repeat
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in JubesX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            #full hose/tights
            "'dildo anal' in (Trigger,Trigger2,JubesX.Offhand)", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", AlphaMask("Zero_Jubes_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            ),
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in JubesX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )


image Jubes_Doggy_Fuck_Top:
    #animation for anal fucking top half
    contains:
        subpixel True
        "Jubes_Doggy_Body"
        ypos 0#15
        pause .4
        block:
            ease .2 ypos -10#5
            pause .3
            ease 2 ypos 0#15
            repeat

image Jubes_Doggy_Fuck_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Jubes_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15#-25
            ease .1 ypos -5#-15
            pause .2
            ease 1.6 ypos 0
            repeat


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Jubes_Doggy_Anal2:
    #Animation for speed 3 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat

image Jubes_Anal_Fucking2:
    #Animation for speed 3 Ass
    contains:
        #Hole
        "images/JubesDoggy/Jubes_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
        block:
            pause .1
            ease .1 zoom 1
            pause .3
            ease .3 zoom .95
            pause .1
            repeat
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in JubesX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Jubes_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in JubesX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )

image Jubes_Doggy_Fuck2_Top:
    #animation for anal fucking2 top half
    contains:
        subpixel True
        "Jubes_Doggy_Body"
        ypos 0#20
        block:
            pause .15
            ease .1 ypos -20#0
            pause .1
            easein .5 ypos 0#20
            pause .05
            repeat

image Jubes_Doggy_Fuck2_Ass:
    #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Jubes_Doggy_Ass"
        ypos 5
        block:
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .4 ypos 5
            pause .05
            repeat




## Footjob animations > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

image Jubes_Doggy_Feet0:
    #static animation
    contains:
        "Jubes_Doggy_Shins"
        pos (0, 0) #(0,-20) top
        block:
            subpixel True
            pause .5
            ease 2 ypos 20#20
            pause .5
            ease 2 ypos 0#0
            repeat
    contains:
        ConditionSwitch(
                "Player.Sprite", "Zero_Doggy_Up",
                "True", Null(),
                )
        zoom 1.2
        pos (158,520)  #(160,480)
    contains:
        "Jubes_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            subpixel True
            pause .5
            ease 2 ypos 20#20
            pause .5
            ease 2 ypos 0#0
            repeat

image Jubes_Doggy_Feet1:
    #slow animation
    contains:
        "Jubes_Doggy_Shins"
        pos (0, 0) #(0,0) top
        block:
            pause .3
            ease 1.7 ypos 120
            ease 1 ypos 0
            repeat
    contains:
        "Zero_Doggy_Up"
        zoom 1.2
        pos (158,520)
        block:
            pause .4
            ease 1.7 ypos 540
            ease .9 ypos 520
            repeat
    contains:
        "Jubes_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            pause .3
            ease 1.7 ypos 120
            ease 1 ypos 0
            repeat

image Jubes_Doggy_Feet2:
    #fast animation
    contains:
        "Jubes_Doggy_Shins"
        pos (0, 20) #(0,0) top
        block:
            pause .05
            ease .6 ypos 130
            ease .3 ypos 20
            repeat
    contains:
        "Zero_Doggy_Up"
        zoom 1.2
        pos (158,520)
        block:
            pause .07
            ease .6 ypos 540
            ease .28 ypos 520
            repeat
    contains:
        "Jubes_Doggy_Feet"
        pos (0, 20) #(0,0) top
        block:
            pause .05
            ease .6 ypos 130
            ease .3 ypos 20
            repeat
# Footjob animations end > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Doggy Launch/Reset
label Jubes_Doggy_Launch(Line = Trigger):
    if renpy.showing("Jubes_Doggy_Animation"):
        return
    $ Speed = 0
    call Girl_Hide(JubesX,1)
    show Jubes_Doggy_Animation at SpriteLoc(StageCenter+50) zorder 150
    with dissolve
    return

label Jubes_Doggy_Reset:
    if not renpy.showing("Jubes_Doggy_Animation"):
        return
#    $ Trigger = 0               #fix, not sure this is a good idea
    $ JubesX.ArmPose = 2
    $ JubesX.SpriteVer = 0
    hide Jubes_Doggy_Animation
    call Girl_Hide(JubesX)
    show Jubes_Sprite at SpriteLoc(JubesX.SpriteLoc) zorder JubesX.Layer:
            alpha 1 zoom 1 offset (0,0) anchor (0.6, 0.0)
    with dissolve
    $ Speed = 0
    return

# End Jubes Doggy Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Jubes Sex Pose Content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Jubes Sex Pose core / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_SexSprite:
    LiveComposite(
        (1120,840),

#        (0,0), ConditionSwitch(
#                #Shows different upper body motion depending on events
#                "True", "Jubes_Sex_Speed2",
#                ),
        (0,0), ConditionSwitch(
                #Shows different motion depending on events
#                "not Player.Sprite", "Jubes_Sex_Body_Static",
                "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Jubes_Sex_Fucking_Speed3",
                        "Speed >= 2", "Jubes_Sex_Fucking_Speed2",
                        "Speed", "Jubes_Sex_Fucking_Speed1",
                        "True", "Jubes_Sex_Fucking_Speed0",
                        ),
                "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Jubes_Sex_Anal_Speed3",
                        "Speed >= 2", "Jubes_Sex_Anal_Speed2",
                        "Speed", "Jubes_Sex_Anal_Speed1",
                        "True", "Jubes_Sex_Anal_Speed0",
                        ),
                "Player.Sprite and Player.Cock == 'out' and Speed >= 2","Jubes_Sex_Hotdog_Speed2",
                "Player.Sprite and Player.Cock == 'out' and Speed >= 1","Jubes_Sex_Hotdog_Speed1",
                "Player.Cock == 'foot'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 2", "Jubes_Sex_FJ_Speed2",
                        "Speed", "Jubes_Sex_FJ_Speed1",
                        "True", "Jubes_Sex_FJ_Speed0",
                        ),
#                "Player.Cock == 'out' and Speed >= 2","Jubes_Hotdog_Body_Anim2",
                "True", "Jubes_Sex_Static",
                ),
        )
    align (0.6,0.0)
    pos (650,303)#(650,393)
    zoom 0.85#0.7

# End Jubes Sex Pose core / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Jubes Sex Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Jubes_Sex_Body:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Jubes_SexSprite
        (1120,840),
#        (245,-225), "Jubes_HairBack_Sex",                                                                 #Hair underlayer
        (0,0), ConditionSwitch(
            #jacket under
            # Modification mode
            "JubesX.Acc == 'saiyan tail'", Null(),
            # -----------------
            "JubesX.Acc", Recolor("Jubes", "Acc", "images/JubesSex/Jubes_Sex_Jacket_Back.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #shirt under layer
            "JubesX.Over == 'red shirt' and JubesX.Uptop", Recolor("Jubes", "Over", "images/JubesSex/Jubes_Sex_Over_Red_Back.png"),
            "JubesX.Over == 'black shirt' and JubesX.Uptop", Recolor("Jubes", "Over", "images/JubesSex/Jubes_Sex_Over_Black_Back.png"),
            "True", Null(),
            ),
        (0,0), "images/JubesSex/[JubesX.skin_image.skin_path]Jubes_Sex_Body_Behind.png",
#        (0,0), "images/JubesSex/Jubes_Sex_Headref.png",
        (0,0), ConditionSwitch(
            #Necklaces
            "JubesX.Neck == 'choker'", Recolor("Jubes", "Neck", "images/JubesSex/Jubes_Sex_Neck_Choker.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #shirt under layer
            "JubesX.Uptop", Null(),
            "JubesX.Over == 'red shirt'", Recolor("Jubes", "Over", "images/JubesSex/Jubes_Sex_Over_Red_Neck.png"),
            "JubesX.Over == 'black shirt'", Recolor("Jubes", "Over", "images/JubesSex/Jubes_Sex_Over_Black_Neck.png"),
            "True", Null(),
            ),
        (300,-130), "Jubes_Head_Sex",  #(280,-140)
        (0,0), "images/JubesSex/[JubesX.skin_image.skin_path]Jubes_Sex_Body.png",
        #Eyes
#        (0,0), ConditionSwitch(                                                                                 #necklace
#            "JubesX.Neck == 'gold necklace'", "images/JubesSex/Jubes_Sex_Neck_Gold.png",
#            "JubesX.Neck == 'star necklace'", "images/JubesSex/Jubes_Sex_Neck_Star.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #bra layer
            "not JubesX.Chest", Null(),
            "not JubesX.Uptop", ConditionSwitch(
                    #if the top's down. . .
                    "JubesX.Chest == 'sports bra'", Recolor("Jubes", "Chest", "images/JubesSex/Jubes_Sex_Chest_Sports.png"),
                    "JubesX.Chest == 'bikini top'", Recolor("Jubes", "Chest", "images/JubesSex/Jubes_Sex_Chest_Bikini.png"),
                    "JubesX.Chest == 'lace bra'", Recolor("Jubes", "Chest", "images/JubesSex/Jubes_Sex_Chest_Lace.png"),
                    # Modification mode
                    "JubesX.Chest == 'saiyan leotard'", "images/JubesSex/modification/Jubes_Sex_Chest_Saiyan_Leotard.png",
                    # -----------------
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                    #if she's not wearing a shirt
                    "JubesX.Chest == 'sports bra'", Recolor("Jubes", "Chest", "images/JubesSex/Jubes_Sex_Chest_Sports_Up.png"),
                    "JubesX.Chest == 'bikini top'", Recolor("Jubes", "Chest", "images/JubesSex/Jubes_Sex_Chest_Bikini_Up.png"),
                    "JubesX.Chest == 'lace bra'", Recolor("Jubes", "Chest", "images/JubesSex/Jubes_Sex_Chest_Lace_Up.png"),
                    # Modification mode
                    "JubesX.Chest == 'saiyan leotard'", "images/JubesSex/modification/Jubes_Sex_Chest_Saiyan_Leotard_Up.png",
                    # -----------------
                    "True", Null(),
                    ),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "JubesX.Water", "images/JubesSex/Jubes_Sex_Wet_Body.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #shirt layer
            "not JubesX.Uptop", ConditionSwitch(
                    #if the top's down. . .
                    "JubesX.Over == 'dress'", Recolor("Jubes", "Over", "images/JubesSex/Jubes_Sex_Over_Dress.png"),
                    "JubesX.Over == 'tube top'", Recolor("Jubes", "Over", "images/JubesSex/Jubes_Sex_Over_Tube.png"),
                    "JubesX.Over == 'red shirt'", Recolor("Jubes", "Over", "images/JubesSex/Jubes_Sex_Over_Red.png"),
                    "JubesX.Over == 'black shirt'", Recolor("Jubes", "Over", "images/JubesSex/Jubes_Sex_Over_Black.png"),
                    # Modification mode
                    "JubesX.Over == 'saiyan armor'", "images/JubesSex/modification/Jubes_Sex_Over_Saiyan_Armor.png",
                    # -----------------
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                    # if she's not wearing a shirt
                    "JubesX.Over == 'dress'", Recolor("Jubes", "Over", "images/JubesSex/Jubes_Sex_Over_Dress_Up.png"),
                    "JubesX.Over == 'tube top'", Recolor("Jubes", "Over", "images/JubesSex/Jubes_Sex_Over_Tube_Up.png"),
                    "JubesX.Over == 'red shirt'", Recolor("Jubes", "Over", "images/JubesSex/Jubes_Sex_Over_Red_Up.png"),
                    "JubesX.Over == 'black shirt'", Recolor("Jubes", "Over", "images/JubesSex/Jubes_Sex_Over_Black_Up.png"),
                    "True", Null(),
                    ),
            ),
        (0,0), ConditionSwitch(
            #piercings
            "JubesX.Uptop", ConditionSwitch(
                    #if the top's down. . .
                    "JubesX.Pierce == 'ring'", "images/JubesSex/Jubes_Sex_Pierce_Tits_Ring.png",
                    "JubesX.Pierce", "images/JubesSex/Jubes_Sex_Pierce_Tits_Barbell.png",
                    "True", Null(),
                    ),
            "JubesX.Pierce == 'ring'", ConditionSwitch(
                    # if she's not wearing a shirt
                    # Modification mode
                    "JubesX.Over == 'saiyan armor'", Null(),
                    # -----------------
                    "JubesX.Over == 'tube top'", "images/JubesSex/Jubes_Sex_Pierce_Tits_Ring_Pink.png",
                    "JubesX.Over == 'red shirt'", "images/JubesSex/Jubes_Sex_Pierce_Tits_Ring_Red.png",
                    "JubesX.Over == 'dress'", "images/JubesSex/Jubes_Sex_Pierce_Tits_Ring_Red.png",
                    "JubesX.Over == 'black shirt'", "images/JubesSex/Jubes_Sex_Pierce_Tits_Ring_Black.png",
                    # Modification mode
                    "JubesX.Chest == 'saiyan leotard'", "images/JubesSex/Jubes_Sex_Pierce_Tits_Ring_Blue.png",
                    # -----------------
                    "JubesX.Chest == 'sports bra'", "images/JubesSex/Jubes_Sex_Pierce_Tits_Ring_Blue.png",
                    "JubesX.Chest == 'bikini top'", "images/JubesSex/Jubes_Sex_Pierce_Tits_Ring_Pink.png",
                    "JubesX.Chest == 'lace bra'", "images/JubesSex/Jubes_Sex_Pierce_Tits_Ring_Lace.png",
                    "True", "images/JubesSex/Jubes_Sex_Pierce_Tits_Ring.png",
                    ),
            "JubesX.Pierce", ConditionSwitch(
                    # Barbell over shirts
                    # Modification mode
                    "JubesX.Over == 'saiyan armor'", Null(),
                    # -----------------
                    "JubesX.Over == 'tube top'", "images/JubesSex/Jubes_Sex_Pierce_Tits_Barbell_Pink.png",
                    "JubesX.Over == 'red shirt'", "images/JubesSex/Jubes_Sex_Pierce_Tits_Barbell_Red.png",
                    "JubesX.Over == 'dress'", "images/JubesSex/Jubes_Sex_Pierce_Tits_Barbell_Red.png",
                    "JubesX.Over == 'black shirt'", "images/JubesSex/Jubes_Sex_Pierce_Tits_Barbell_Black.png",
                    # Modification mode
                    "JubesX.Chest == 'saiyan leotard'", "images/JubesSex/Jubes_Sex_Pierce_Tits_Barbell_Blue.png",
                    # -----------------
                    "JubesX.Chest == 'sports bra'", "images/JubesSex/Jubes_Sex_Pierce_Tits_Barbell_Blue.png",
                    "JubesX.Chest == 'bikini top'", "images/JubesSex/Jubes_Sex_Pierce_Tits_Barbell_Pink.png",
                    "JubesX.Chest == 'lace bra'", "images/JubesSex/Jubes_Sex_Pierce_Tits_Barbell_Lace.png",
                    "True", "images/JubesSex/Jubes_Sex_Pierce_Tits_Barbell.png",
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #jacket
            # Modification mode
            "JubesX.Acc == 'saiyan tail'", Null(),
            # -----------------
            "JubesX.Acc", Recolor("Jubes", "Acc", "images/JubesSex/Jubes_Sex_Jacket.png"),
            "True", Null(),
            ),

        (0,0),ConditionSwitch(
            #Outside Spunk
            "'belly' in JubesX.Spunk and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'tits' in JubesX.Spunk and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Tits.png",
            "True", Null(),
            ),
#        (0,0), "images/JubesSex/Jubes_Sex_HeadRef.png",
        )
#    yoffset -163
# End Jubes Sex Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Jubes_Head_Sex:
    # The head used for the sex pose, referenced by Jubes_Sex_Body
    "Jubes_Sprite_Head"
    zoom 1.36#1.36
    anchor (0.5,0.5)
    rotate -15#-7
#    alpha 0.5

image Jubes_HairBack_Sex:
    # The hair behind the head for the sex pose, referenced by Jubes_Sex_Body
    "Jubes_Sprite_HairBack"
    zoom 1.25
    anchor (0.5,0.5)
    rotate -7


image Jubes_Sex_Lick_Breasts:
        "Lick_Anim"
        zoom 0.7
        offset (400,350)#(390,620)

image Jubes_Sex_Fondle_Breasts:
        "GropeLeftBreast"
        zoom 1.5
        offset (190,-200)#(160,-40)

# Start Jubes Sex Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Jubes_Sex_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Jubes_SexSprite
        (1120,880),
#        (0,0), ConditionSwitch(
#Legs Layer
#            "JubesX.Legs == 'blue skirt'", "images/JubesSex/Jubes_Sex_Skirt_Back.png",
#            "True", Null(),
#            ),
#        (0,0), "images/JubesSex/[JubesX.skin_image.skin_path]Jubes_Sex_Legs.png",
#Legs Base

#        (0,0), ConditionSwitch(
#            #Skirt back
#            "JubesX.Legs == 'skirt'", "images/JubesSex/Jubes_Sex_Legs_Skirt_Back.png",
#            "True", Null(),
#            ),
#        (0,0),ConditionSwitch(
#            #Outside Spunk
#            "'anal' in JubesX.Spunk", "images/JubesSex/Jubes_Sex_Spunk_Anal_Closed.png",
#            "True", Null(),
#            ),

        (545,540), ConditionSwitch(    #165,560
            #Personal Wetness
            "not JubesX.Wet", Null(),
            "(JubesX.Legs == 'pants' or JubesX.Legs == 'shorts') and not JubesX.Upskirt", Null(),
            "JubesX.Panties and not JubesX.PantiesDown", Null(),
            "JubesX.Wet == 1", "Wet_Drip",
            "True", "Wet_Drip2",
            ),

        (545,540), ConditionSwitch(    #205,530
            #Spunk
            "'anal' not in JubesX.Spunk or not Player.Male", Null(),
            "(JubesX.Legs == 'pants' or JubesX.Legs == 'shorts') and not JubesX.Upskirt", Null(),
            "JubesX.Wet == 1", "Spunk_Drip",
            "True", "Spunk_Drip2",
            ),

        (0,0),"images/JubesSex/[JubesX.skin_image.skin_path]Jubes_Sex_Legs.png",
            #Legs

        (0,0), ConditionSwitch(
            #Wet look
            "not JubesX.Water", Null(),
            "True", "images/JubesSex/Jubes_Sex_Wet_Legs.png",
            ),

        (0,0), "Jubes_Sex_Anus",
            #Anus Composite

        (0,0), "Jubes_Sex_Pussy",
            #Pussy Composite


        (0,0), ConditionSwitch(
            #hose layer
            "JubesX.Hose == 'stockings and garterbelt'", Recolor("Jubes", "Hose", "images/JubesSex/Jubes_Sex_Hose_StockingsGarter.png"),
            "JubesX.Hose == 'socks'", Recolor("Jubes", "Hose", "images/JubesSex/Jubes_Sex_Hose_Socks.png"),
            "JubesX.Hose == 'garterbelt'", Recolor("Jubes", "Hose", "images/JubesSex/Jubes_Sex_Hose_Garter.png"),
            "JubesX.Hose == 'stockings'", Recolor("Jubes", "Hose", "images/JubesSex/Jubes_Sex_Hose_Stockings.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Panties if up
            # Modification mode
            "JubesX.Panties == 'saiyan leotard' and JubesX.PantiesDown", "images/JubesSex/modification/Jubes_Sex_Panties_Saiyan_Leotard_Up.png",
            "JubesX.Panties == 'saiyan leotard'", "images/JubesSex/modification/Jubes_Sex_Panties_Saiyan_Leotard.png",
            # -----------------
            "JubesX.PantiesDown", Null(),
            "JubesX.Panties == 'lace panties'", Recolor("Jubes", "Panties", "images/JubesSex/Jubes_Sex_Panties_Lace.png"),
            "JubesX.Panties == 'tiger panties' and JubesX.Wet", Recolor("Jubes", "Panties", "images/JubesSex/Jubes_Sex_Panties_Tiger_Wet.png"),
            "JubesX.Panties == 'tiger panties'", Recolor("Jubes", "Panties", "images/JubesSex/Jubes_Sex_Panties_Tiger.png"),
            "JubesX.Panties == 'bikini bottoms' and JubesX.Wet", Recolor("Jubes", "Panties", "images/JubesSex/Jubes_Sex_Panties_Bikini_Wet.png"),
            "JubesX.Panties == 'bikini bottoms'", Recolor("Jubes", "Panties", "images/JubesSex/Jubes_Sex_Panties_Bikini.png"),
            "JubesX.Panties and JubesX.Wet", "images/JubesSex/Jubes_Sex_Panties_Blue_Wet.png",
            "JubesX.Panties", "images/JubesSex/Jubes_Sex_Panties_Blue.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Piercings
##            "Player.Sprite", Null(),
##            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
##            "Trigger == 'dildo pussy'", Null(),
#            "not JubesX.Panties and JubesX.Hose != 'pantyhose'", Null(),
#            "((JubesX.Panties or JubesX.Hose == 'pantyhose') and JubesX.PantiesDown)", Null(),
#                #if she has panties, but they are down, or pantyhose, or Legs that are not a skirt and are not down, skip these. . .
#            "JubesX.Pierce == 'barbell'", "images/JubesSex/Jubes_Sex_Pierce_Pussy_BarbellC.png",
#            "JubesX.Pierce == 'ring'", "images/JubesSex/Jubes_Sex_Pierce_Pussy_RingC.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #Piercings
#            "Player.Sprite", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),

#            "Player.Sprite and Player.Cock == 'in' and Speed == 0", Null(),
            "JubesX.Pierce == 'ring'",ConditionSwitch(
                    #If she has panties down. . .
                    "Player.Sprite and Player.Cock == 'in'", "images/JubesSex/Jubes_Sex_Pierce_Ring_Fucking.png",
                    "JubesX.Legs == 'shorts' and not JubesX.Upskirt", "images/JubesSex/Jubes_Sex_Pierce_Ring_Shorts.png",
                    "JubesX.Legs == 'pants' and not JubesX.Upskirt", "images/JubesSex/Jubes_Sex_Pierce_Ring_Pants.png",
                    "JubesX.Panties == 'lace panties' and not JubesX.PantiesDown", "images/JubesSex/Jubes_Sex_Pierce_Ring_Lace.png",
                    "JubesX.Panties == 'tiger panties' and not JubesX.PantiesDown", "images/JubesSex/Jubes_Sex_Pierce_Ring_Tiger.png",
                    "JubesX.Panties == 'bikini bottoms' and not JubesX.PantiesDown", "images/JubesSex/Jubes_Sex_Pierce_Ring_Bikini.png",
                    "JubesX.Panties and not JubesX.PantiesDown", "images/JubesSex/Jubes_Sex_Pierce_Ring_Blue.png",
                    "True", "images/JubesSex/Jubes_Sex_Pierce_Ring.png",
                    ),
            "not JubesX.Pierce", Null(),
            #else, it's barbell

            "JubesX.Legs == 'shorts' and not JubesX.Upskirt", "images/JubesSex/Jubes_Sex_Pierce_Barbell_Shorts.png",
            "JubesX.Legs == 'pants' and not JubesX.Upskirt", "images/JubesSex/Jubes_Sex_Pierce_Barbell_Pants.png",
            "JubesX.Panties == 'lace panties' and not JubesX.PantiesDown", "images/JubesSex/Jubes_Sex_Pierce_Barbell_Lace.png",
            "JubesX.Panties == 'tiger panties' and not JubesX.PantiesDown", "images/JubesSex/Jubes_Sex_Pierce_Barbell_Tiger.png",
            "JubesX.Panties == 'bikini bottoms' and not JubesX.PantiesDown", "images/JubesSex/Jubes_Sex_Pierce_Barbell_Bikini.png",
            "JubesX.Panties and not JubesX.PantiesDown", "images/JubesSex/Jubes_Sex_Pierce_Barbell_Blue.png",
            "True", "images/JubesSex/Jubes_Sex_Pierce_Barbell.png",
            ),
        (0,0), ConditionSwitch(
            #pantyhose layer
            "JubesX.Panties and JubesX.PantiesDown", Null(),
            "JubesX.Hose == 'pantyhose'", Recolor("Jubes", "Hose", "images/JubesSex/Jubes_Sex_Hose_Pantyhose.png"),
            "JubesX.Hose == 'ripped pantyhose'", Recolor("Jubes", "Hose", "images/JubesSex/Jubes_Sex_Hose_Pantyhose_Holed.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs Layer
#            "JubesX.Upskirt",ConditionSwitch(
#                    #If she has panties down. . .
##                    "JubesX.Legs == 'skirt'", "images/JubesSex/Jubes_Sex_Legs_Skirt_Up.png",
#                    "JubesX.Legs == 'shorts'", Recolor("Jubes", "Legs", "images/JubesSex/Jubes_Sex_Legs_Shorts_Up.png"),
#                    "JubesX.Legs == 'pants'", Recolor("Jubes", "Legs", "images/JubesSex/Jubes_Sex_Legs_Pants_Up.png"),
#                    "True", Null(),
#                    ),

#            "JubesX.Legs == 'dress' and JubesX.Over == 'dress'", Recolor("Jubes", "Over", "images/JubesSex/Jubes_Sex_Legs_Dress.png"),
            "JubesX.Legs == 'skirt'", Recolor("Jubes", "Legs", "images/JubesSex/Jubes_Sex_Legs_Skirt.png"),

            "JubesX.Upskirt", Null(),
#            "JubesX.Legs == 'skirt'", Recolor("Jubes", "Legs", "images/JubesSex/Jubes_Sex_Legs_Skirt.png"),
            "JubesX.Legs == 'shorts' and JubesX.Wet > 1", Recolor("Jubes", "Legs", "images/JubesSex/Jubes_Sex_Legs_Shorts_Wet.png"),
            "JubesX.Legs == 'shorts'", Recolor("Jubes", "Legs", "images/JubesSex/Jubes_Sex_Legs_Shorts.png"),
            "JubesX.Legs == 'pants'", Recolor("Jubes", "Legs", "images/JubesSex/Jubes_Sex_Legs_Pants.png"),
            "True", Null(),
            ),
        # Modification mode
        (0,0), ConditionSwitch(
            "JubesX.Acc == 'saiyan tail'", "images/JubesSex/modification/Jubes_Sex_Saiyan_Tail.png",
            "True", Null(),
            ),
        # -----------------

        (0,0), ConditionSwitch(
            #Piercings
            "JubesX.Pierce == 'ring'",ConditionSwitch(
                    #If she has panties down. . .
                    "JubesX.Legs == 'shorts' and not JubesX.Upskirt", "images/JubesSex/Jubes_Sex_Pierce_Ring_Shorts.png",
                    "JubesX.Legs == 'pants' and not JubesX.Upskirt", "images/JubesSex/Jubes_Sex_Pierce_Ring_Pants.png",
                    "True", Null(),
                    ),
            #else, it's barbell
            "JubesX.Legs == 'shorts' and not JubesX.Upskirt", "images/JubesSex/Jubes_Sex_Pierce_Barbell_Shorts.png",
            "JubesX.Legs == 'pants' and not JubesX.Upskirt", "images/JubesSex/Jubes_Sex_Pierce_Barbell_Pants.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #dress Layer
            "JubesX.Over == 'dress'", Recolor("Jubes", "Over", "images/JubesSex/Jubes_Sex_Legs_Dress.png"),
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer
#            "not Player.Sprite or Player.Cock != 'out'", Null(),
#            "Speed >= 2", "Jubes_Hotdog_Zero_Anim2",
#            "Speed", "Jubes_Hotdog_Zero_Anim1",
#            "True", "Jubes_Hotdog_Zero_Anim0",
#            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy'", "Jubes_Sex_Lick_Pussy",
            "Trigger == 'lick ass'", "Jubes_Sex_Lick_Ass",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy fondling animation
            "Player.Sprite", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Jubes_Sex_Fondle_Pussy",
            "JubesX.Offhand == 'fondle pussy' and JubesX.Lust > 60", At("JubesFingerHand", GirlFingerPussyX()),
            "JubesX.Offhand == 'fondle pussy'", At("JubesMastHand", GirlGropePussyX()),
            "True", Null(),
            ),
        (0,0), "Jubes_Sex_Feet",

#        (0,0), ConditionSwitch(                                                                                 #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
#            "not Speed", "Jubes_Sex_Feet",
#            "Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Jubes_Sex_Feet", "images/JubesSex/Jubes_Sex_FeetMask.png"),
#            "True", "Jubes_Sex_Feet",
#            ),
        )
# End Jubes Sex Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_Sex_Feet:
    LiveComposite(
        #the lower legs used in the sex pose, referenced by Jubes_Sex_Legs
        (1120,840),
#        (0,0), "images/JubesSex/[JubesX.skin_image.skin_path]Jubes_Sex_Feet.png",                                                         #Legs Base

        (0,0), ConditionSwitch(
            #hose layer
            "JubesX.Hose == 'socks'", Recolor("Jubes", "Hose", "images/JubesSex/Jubes_Sex_Hose_Socks_Feet.png"),
            "JubesX.Hose == 'ripped pantyhose' and (not JubesX.Panties or not JubesX.PantiesDown)", Recolor("Jubes", "Hose", "images/JubesSex/[JubesX.skin_image.skin_path]Jubes_Sex_Hose_Feet_Holed.png"),
            "JubesX.Hose and JubesX.Hose != 'garterbelt' and JubesX.Hose != 'pantyhose'", Recolor("Jubes", "Hose", "images/JubesSex/Jubes_Sex_Hose_Feet.png"),
            "JubesX.Hose == 'ripped pantyhose' and JubesX.Panties and JubesX.PantiesDown", "images/JubesSex/[JubesX.skin_image.skin_path]Jubes_Sex_Feet.png",
            "JubesX.Hose == 'pantyhose' and JubesX.Panties and JubesX.PantiesDown", "images/JubesSex/[JubesX.skin_image.skin_path]Jubes_Sex_Feet.png",
            "JubesX.Hose == 'pantyhose'", Recolor("Jubes", "Hose", "images/JubesSex/Jubes_Sex_Hose_Feet.png"),
            "True", "images/JubesSex/[JubesX.skin_image.skin_path]Jubes_Sex_Feet.png",   #Null(),
            ),

        (0,0), ConditionSwitch(
            #Wet look
            "not JubesX.Water", Null(),
            "True", "images/JubesSex/Jubes_Sex_Wet_Feet.png",
            ),
        (0,0), ConditionSwitch(
            #panties if down
            "not JubesX.PantiesDown", Null(),
            "JubesX.Panties == 'lace panties'", Recolor("Jubes", "Panties", "images/JubesSex/Jubes_Sex_Panties_Lace_Up.png"),
            "JubesX.Panties == 'tiger panties'", Recolor("Jubes", "Panties", "images/JubesSex/Jubes_Sex_Panties_Tiger_Up.png"),
            "JubesX.Panties == 'bikini bottoms'", Recolor("Jubes", "Panties", "images/JubesSex/Jubes_Sex_Panties_Bikini_Up.png"),
            # Modification mode
            "JubesX.Panties == 'saiyan leotard'", Null(),
            # -----------------
            "JubesX.Panties", "images/JubesSex/Jubes_Sex_Panties_Blue_Up.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Legs Layer
            "JubesX.Upskirt",ConditionSwitch(
                    #If she has panties down. . .
                    "JubesX.Legs == 'shorts'", Recolor("Jubes", "Legs", "images/JubesSex/Jubes_Sex_Legs_Shorts_Up.png"),
                    "JubesX.Legs == 'pants'", Recolor("Jubes", "Legs", "images/JubesSex/Jubes_Sex_Legs_Pants_Up.png"),
                    "True", Null(),
                    ),
            "JubesX.Legs == 'pants'", Recolor("Jubes", "Legs", "images/JubesSex/Jubes_Sex_Legs_Pants_Feet.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk
            "'feet' in JubesX.Spunk", "images/JubesSex/Jubes_Sex_Spunk_Feet.png",
            "True", Null(),
            ),
        )

# Start Jubes Sex Pose Pussy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Jubes_Sex_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).

    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/JubesSex/Jubes_Sex_Pussy_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and Speed", "Jubes_Sex_Heading_Pussy",
                "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/JubesSex/Jubes_Sex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/JubesSex/Jubes_Sex_Pussy_Open.png",
                "JubesX.Offhand == 'fondle pussy' and JubesX.Lust > 60", "images/JubesSex/Jubes_Sex_Pussy_Open.png",
                "True", "images/JubesSex/Jubes_Sex_Pussy_Closed.png",
                )
#    contains:
#            # The background plate of her pussy
#            ConditionSwitch(
#                "not JubesX.Wet", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/JubesSex/Jubes_Sex_WetPussy_F.png",
#                "True", "images/JubesSex/Jubes_Sex_WetPussy_C.png",
#                )
    contains:
            # pubes
            ConditionSwitch(
                "not JubesX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", Recolor("Jubes", "Pubes", "images/JubesSex/Jubes_Sex_Pubes_Fucking.png"),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 1", Recolor("Jubes", "Pubes", "images/JubesSex/Jubes_Sex_Pubes_Fucking.png"),
                "Player.Sprite and Player.Cock == 'in'", Recolor("Jubes", "Pubes", "images/JubesSex/Jubes_Sex_Pubes_Open.png"),
                "Player.Sprite and Player.Cock == 'out'", Recolor("Jubes", "Pubes", "images/JubesSex/Jubes_Sex_Pubes_Open.png"),
                "Trigger == 'lick pussy'", Recolor("Jubes", "Pubes", "images/JubesSex/Jubes_Sex_Pubes_Open.png"),
                "JubesX.Offhand == 'fondle pussy' and JubesX.Lust > 60", Recolor("Jubes", "Pubes", "images/JubesSex/Jubes_Sex_Pubes_Open.png"),
                "True", Recolor("Jubes", "Pubes", "images/JubesSex/Jubes_Sex_Pubes_Closed.png"),
                )
    contains:
            #Spunk
            ConditionSwitch(
                "'in' not in JubesX.Spunk or not Player.Male", Null(),
                "(JubesX.Legs == 'pants' or JubesX.Legs == 'shorts') and not JubesX.Upskirt", Null(),
                "JubesX.Panties and not JubesX.PantiesDown", Null(),
                "True", AlphaMask("Spunk_Drip2","Jubes_Sex_Drip_Mask"),
                )
            offset (545,540)

    contains:
            ConditionSwitch(
                #Outside Spunk
                "'in' in JubesX.Spunk and Player.Sprite and Player.Cock == 'in' and Speed and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_PussyF.png",
                "'in' in JubesX.Spunk and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Pussy.png",
                "True", Null(),
                )
#    contains:
#            #Spunk under penis
#            ConditionSwitch(
#                "'in' in JubesX.Spunk", "images/JubesSex/Jubes_Sex_Spunk_Puss_Under.png",
#                "True", Null(),
#                )
#    contains:
#            #hose layer
#            ConditionSwitch(
#                "JubesX.Panties and JubesX.PantiesDown", Null(),
#                "JubesX.Hose == 'ripped pantyhose' and ShowFeet", Recolor("Jubes", "Hose", "images/JubesSex/Jubes_Sex_Hose_Pantyhose_Holed.png"),
#                "JubesX.Hose == 'ripped pantyhose'", Recolor("Jubes", "Hose", "images/JubesSex/Jubes_Sex_Hose_Pantyhose_Holed.png"),
#                "True", Null(),
#                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            ConditionSwitch(
#                "not Player.Sprite", Null(),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 3", AlphaMask("Jubes_Sex_Fucking_Zero_Anim3", "Jubes_Sex_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", AlphaMask("Jubes_Sex_Fucking_Zero_Anim2", "Jubes_Sex_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and Speed == 1", AlphaMask("Jubes_Sex_Fucking_Zero_Anim1", "Jubes_Sex_Heading_Mask"),
                "Player.Sprite and Player.Cock == 'in'", "Jubes_Sex_Fucking_Zero_Anim0",
                "True", Null(),
                )
#    contains:
#            #Piercings
#            ConditionSwitch(
#                "JubesX.Pierce == 'barbell' and Player.Sprite and Player.Cock == 'in' and Speed", "images/JubesSex/Jubes_Sex_Pierce_Pussy_BarbellF.png",
#                "JubesX.Pierce == 'ring' and Player.Sprite and Player.Cock == 'in' and Speed", "images/JubesSex/Jubes_Sex_Pierce_Pussy_RingF.png",
#                "JubesX.Pierce == 'barbell'", "images/JubesSex/Jubes_Sex_Pierce_Pussy_Barbell.png",
#                "JubesX.Pierce == 'ring'", "images/JubesSex/Jubes_Sex_Pierce_Pussy_Ring.png",
#                "True", Null(),
#                )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and Speed == 1", "Jubes_Pussy_Spunk_Heading",
                "True", Null(),
                )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "Speed == 1", Null(),
                "'in' not in JubesX.Spunk or not Player.Sprite or Player.Cock != 'in' or not Speed or not Player.Male", Null(),
#                "Speed <= 1", Null(), #"Jubes_Pussy_Spunk_Heading",
                "True", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
                )

    #End Jubes Pussy composite

image Jubes_Sex_Drip_Mask:
    #This is the mask for her drip pattern
    contains:
        "images/JubesSex/Jubes_Sex_Mask_Anal.png"
        offset (-545,-450)#(-275,-560)#(-145,-560)#(-225,-560)

image Jubes_Sex_Lick_Pussy:
        "Lick_Anim"
        zoom 0.7
        offset (535,500)#(505,680)

image Jubes_Sex_Lick_Ass:
        "Lick_Anim"
        zoom 0.7
        offset (535,580)#(535,550)

image Jubes_Sex_Fondle_Pussy:
        "GropePussy_Jubes"
        xzoom -1.5
        yzoom 1.5
        offset(-710,-300) #(-890,-300)
#        block:
#            ease 1 offset(-1000,0) #(535,500)
#            ease 1 offset(-1000,-1000) #(535,500)
#            ease 1 offset(0,-1000) #(535,500)
#            ease 1 offset(0,0) #(535,500)
#            repeat

#End Animations for Jubes's Pussy during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_Sex_Zero_Cock:
        #this is the cock generally used by Jubes's sex pose
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

image Jubes_Sex_Fucking_Mask:
        #This is the mask image for Kitty's wide open pussy
        # Used in "Jubes_Sex_Speed2" and "Jubes_Sex_Speed3"
        contains:
            "images/JubesSex/Jubes_Sex_Mask_Fucking.png"
            yoffset 3

# Start Jubes Sex Pose Static / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_Sex_Static:
    # Pose for Jubes's Sex Pose in which she is static
    contains:
            #Jubes's underlying body
            subpixel True
            "Jubes_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            pos (0,-180) #X less is left, Y less is up
            block:
#                pause 0.3
                ease 1.5 ypos -185 #-120
                pause .3
                ease 1.45 ypos -180 #-130
                pause 0.25
                repeat
    contains:
            #Jubes's Legs
            subpixel True
            "Jubes_Sex_Legs"
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
            "Jubes_Sex_Zero_Cock"
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
            #Jubes's Feet
            subpixel True
            "Jubes_Sex_Feet"
#            ConditionSwitch(
#                #Footjob overlay
#                "ShowFeet", AlphaMask("Jubes_Sex_Feet", "images/JubesSex/Jubes_Sex_FeetMask.png"),
#                "True", Null(),
#                )
            pos (0,-180) #X less is left, Y less is up
#            block:
#                pause 0.3
#                ease 1.4 ypos -185 #-120
#                pause .3
#                ease 1.25 ypos -180 #-130
#                ease 0.15 ypos -177 #-130
#                ease 0.1 ypos -180 #-130
#                repeat

# End Jubes Sex Pose Speed Static / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Jubes Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Jubes Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_Sex_Fucking_Speed0:
    # Pose for Jubes's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Jubes's underlying body
            subpixel True
            "Jubes_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                ease 2 ypos -160 #0
                pause 0.8
                ease 2 ypos -180 #-130
                pause 0.2
                repeat
    contains:
            #Jubes's Legs
            subpixel True
            "Jubes_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -160 #0
                pause 0.8
                ease 2 ypos -180 #-130
                repeat
# End main animation for Sex Pose Fucking Speed 1


image Jubes_Sex_Fucking_Zero_Anim0:
        #this is Jubes's sex animation, Speed 1 Fucking
        contains:
            subpixel True
            "Jubes_Sex_Zero_Cock"
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

# End Jubes Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Jubes Sex Pose Speed 1 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_Sex_Fucking_Speed1:
    # Pose for Jubes's Sex Pose in which she is fucking at speed 1 (heading)
    contains:
            #Jubes's underlying body
            subpixel True
            "Jubes_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause 1
                ease 1.5 ypos -190 #0
                pause 1.6
                ease 0.9 ypos -180 #-130
                repeat
    contains:
            #Jubes's Legs
            subpixel True
            "Jubes_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause 0.7
                ease 1.5 ypos -200 #0
                pause 1.6
                ease 1.2 ypos -180 #-130
                repeat
# End main animation for Sex Pose Fucking Speed 1


image Jubes_Sex_Fucking_Zero_Anim1:
        #this is Jubes's sex animation, Speed 1 Fucking
        contains:
            subpixel True
            "Jubes_Sex_Zero_Cock"
            subpixel True
            pos (0,40)#(498,530)
            block:
                pause 0.2
#                ease 0.95 ypos -145
                ease 2 ypos -10#-10 #-140
                pause .8
                ease 2 ypos 40 #-10
                repeat

image Jubes_Sex_Heading_Mask:
        #This is the mask image for Jubes's heading pussy
        contains:
            "images/JubesSex/Jubes_Sex_Mask_Fucking.png"
            yoffset 10
            block:
                pause 0.2
                ease 2 yoffset 3
                pause 0.8
                ease 2 yoffset 10
                repeat


image Jubes_Sex_Heading_Pussy:
        #This is the image for Jubes's heading pussy growing
#        contains:
#            "images/JubesSex/Jubes_Sex_Pussy_Fucking_Base.png"
        contains:
            "images/JubesSex/Jubes_Sex_Pussy_Fucking.png"
            anchor (0.5,0)
            transform_anchor True
            subpixel True
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
            transform_anchor True
            subpixel True
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

#image Kitty_Sex_Pussy_Hole:
#    "images/JubesDoggy/Jubes_Doggy_Pussy_HHole.png"
#    transform_anchor True
#    anchor (212,580)#(210,600)
#    pos (558,580)#(400,-10)
#    xzoom 0.8
#    parallel:
#        ease 1 yzoom 1.2
#        pause 1
#        ease 3 yzoom 1
#        repeat
#    parallel:
#        ease 1 xzoom 1.2
#        pause 2
#        ease 2  xzoom 0.8
#        repeat

image Jubes_Pussy_Spunk_Heading:
        #This is the image for Jubes's heading pussy cum
        contains:
            ConditionSwitch(
                "'in' in JubesX.Spunk and Player.Sprite and Player.Cock == 'in' and Speed == 1 and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
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

# End Jubes Sex Pose Speed 1 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Jubes Sex Pose Speed 2 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_Sex_Fucking_Speed2:
    # Pose for Jubes's Sex Pose in which she is fucking at speed 2
    contains:
            #Jubes's underlying body
            subpixel True
            "Jubes_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 4.2
                pause 0.6
                ease .9 ypos -190 # 0
                pause 0.8
                ease 2.0 ypos -180 # -130
                repeat
    contains:
            #Jubes's Legs
            subpixel True
            "Jubes_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 4.2
                pause 0.4
                ease 0.95 ypos -205 # 5
                ease 0.45 ypos -200 # 0
                pause 0.6
                ease 1.8 ypos -180 # -130
                repeat
# End main animation for Sex Pose Fucking Speed 2


image Jubes_Sex_Fucking_Zero_Anim2:
        #this is Jubes's sex animation, Speed 2 Fucking
        contains:
            subpixel True
            "Jubes_Sex_Zero_Cock"
            subpixel True
            pos (0,20)#(498,530)
            block:
                pause 0.2
                ease 0.95 ypos -100 # -145
                ease 0.25 ypos -90 # -140
                pause .8
                ease 2 ypos 20 #-10
                repeat

# End Jubes Sex Pose Speed 2 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Jubes Sex Pose Speed 3 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_Sex_Fucking_Speed3:
    # Pose for Jubes's Sex Pose in which she is fucking at speed 3
    contains:
            #Jubes's underlying body
            subpixel True
            "Jubes_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.6
                ease 0.4 ypos -200
#                pause 0.35
                ease 0.8 ypos -180
                repeat
    contains:
            #Jubes's Legs
            subpixel True
            "Jubes_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.4
                ease 0.45 ypos -220
                ease 0.15 ypos -210
#                pause 0.35
                ease 0.8 ypos -180
                repeat


# End main animation for Sex Pose Fucking Speed 3


image Jubes_Sex_Fucking_Zero_Anim3:
        #this is Jubes's sex animation, Speed3 Fucking
        contains:
            subpixel True
            "Jubes_Sex_Zero_Cock"
            subpixel True
            pos (0,10)
            block:
                pause 0.1
                ease 0.55 ypos -100
                ease 0.15 ypos -90
                pause 0.25
                ease 0.75 ypos 10
                repeat

# End Jubes Sex Pose Speed 3 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Animations for Jubes's Ass during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Jubes's Ass during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_Sex_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/JubesSex/Jubes_Sex_Anal.png",
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/JubesSex/Jubes_Sex_Anal.png",
            "Player.Sprite and Player.Cock == 'anal' and Speed", "Jubes_Sex_Anal_Heading",
            "Player.Sprite and Player.Cock == 'anal'", "Jubes_Sex_Anal_Tip",
            "JubesX.Plug", "images/PlugBase_Sex.png",
            "JubesX.Loose > 2", "Jubes_Gape_Anal_Sex",
#            "JubesX.Loose", "images/JubesSex/Jubes_Sex_Hole_Loose.png",
            "True", Null(),
            )
    contains:
            #Spunk under penis
            ConditionSwitch(
                "'anal' not in JubesX.Spunk or not Player.Male", Null(),
#                "Player.Sprite and Player.Cock != 'anal' and Speed >= 1", "images/JubesSex/Jubes_Sex_Spunk_Anal_Under.png",
                "Player.Sprite and Player.Cock != 'anal' and Speed == 1", "Jubes_Sex_Anal_Spunk_Heading_Under",
                "True", "images/JubesSex/Jubes_Sex_Spunk_Anal.png",
                )
    contains:
            # The animation of Zero's moving penis, masked by her anus shape
            ConditionSwitch(
                "not Player.Sprite or Player.Cock != 'anal'", Null(),
                "Speed >= 3",  AlphaMask("Jubes_Sex_Anal_Zero_Anim3", "Jubes_Sex_Anal_MaskF"),
                "Speed >= 2", AlphaMask("Jubes_Sex_Anal_Zero_Anim2", "Jubes_Sex_Anal_MaskF"),
                "Speed", AlphaMask("Jubes_Sex_Anal_Zero_Anim1", "Jubes_Sex_Anal_Mask"),
                "True", AlphaMask("Jubes_Sex_Anal_Zero_Anim0", "Jubes_Sex_Anal_Mask"),
                )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "'anal' not in JubesX.Spunk or not Player.Sprite or Player.Cock != 'anal' or not Speed or not Player.Male", Null(),
                "Speed == 1", "Jubes_Sex_Anal_Spunk_Heading_Over",
                "True", "Jubes_Sex_Anal_Spunk",
                )


image Jubes_Gape_Anal_Sex:
        #removing an anal plug
        contains:
            #Hole
            "images/JubesSex/Jubes_Sex_Anal.png"
            transform_anchor True
            subpixel True
            anchor (560,620)#(0.52,0.69)
            offset (560,617)#(218,518)
            zoom .40 # tight
            block:
                ease 3 zoom .50 #in.87
                ease 3 zoom .40 #out
                repeat

image Jubes_Sex_Anal_Spunk:
    ConditionSwitch(
                "'anal' in JubesX.Spunk and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Anal_Over.png",
                "True", Null(),
                )
    anchor (0.5,0.5)
    pos (0.5,0.5)
#    xoffset 20
    yoffset -23#68
    xzoom .9#1.2

image Jubes_Sex_Anal_Mask:
        #This is the mask image for small stuff
        # Used in "Jubes_Sex_Speed2" and "Jubes_Sex_Speed3"
        contains:
            "images/JubesSex/Jubes_Sex_Mask_Anal.png"
            yoffset 98 #-9
            xoffset 3 #3
#            xoffset -5

image Jubes_Sex_Anal_MaskF:
        #This is the mask image for deep stuff
        # Used in "Jubes_Sex_Speed2" and "Jubes_Sex_Speed3"
        contains:
            "images/JubesSex/Jubes_Sex_Mask_AnalB.png"
            yoffset 98 #-9
            xoffset 3



# Start Jubes Sex Pose Speed 0 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_Sex_Anal_Speed0:
    # Pose for Jubes's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Jubes's underlying body
            subpixel True
            "Jubes_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.5
                ease 1 ypos -185 #40
                pause 1.0
                ease 1.5 ypos -180 #90
                repeat
    contains:
            #Jubes's Legs
            subpixel True
            "Jubes_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.2
                ease 1 ypos -190 #40
                pause 1.3
                ease 1.5 ypos -180 #90
                repeat

# End main animation for Sex Pose Anal Speed 1


image Jubes_Sex_Anal_Zero_Anim0:
        #this is Jubes's sex animation, Speed 0 Anal
        contains:
            subpixel True
            "Jubes_Sex_Zero_Cock"
#            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            subpixel True
            pos (3,135)#(498,530)
            block:
                pause 0.2
                ease 2 ypos 130 #90
                pause .8
                ease 2 ypos  135 #130
                repeat

image Jubes_Sex_Anal_Tip:
    "images/JubesSex/Jubes_Sex_Anal.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    yoffset -20
    xzoom 0.4
    block:
        #total 5 second
        pause 0.5   #
        ease 1.50 xzoom 0.55   #.75 (1.0)
        pause 0.5   #
        ease .25 xzoom 0.55  #(1.0)
        ease 2.25 xzoom 0.4   #(0.6)
        repeat

# End Jubes Sex Pose Speed 0 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Jubes Sex Pose Speed 1 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_Sex_Anal_Heading:
    "images/JubesSex/Jubes_Sex_Anal.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    yoffset -20
    xzoom 0.6
    block:
        #total 5 second
        pause 0.5   #
        ease 1.50 xzoom 1.0   #.75 (1.0)
        pause 0.5   #
        ease .25 xzoom 1.0  #(1.0)
        ease 2.25 xzoom 0.6   #(0.6)
        repeat

image Jubes_Sex_Anal_Spunk_Heading_Over:
    ConditionSwitch(
                "'anal' in JubesX.Spunk and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Anal_Over.png",
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

image Jubes_Sex_Anal_Spunk_Heading_Under:
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

image Jubes_Sex_Anal_Speed1:
    # Pose for Jubes's Sex Pose in which she is fucking at speed 1 (heading)
    contains:
            #Jubes's underlying body
            subpixel True
            "Jubes_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.5
                ease 1 ypos -185 #40
                pause 1.0
                ease 1.5 ypos -180 #90
                repeat
    contains:
            #Jubes's Legs
            subpixel True
            "Jubes_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.2
                ease 1 ypos -190 #40
                pause 1.3
                ease 1.5 ypos -180 #90
                repeat

# End main animation for Sex Pose Anal Speed 1


image Jubes_Sex_Anal_Zero_Anim1:
        #this is Jubes's sex animation, Speed 1 Anal
        contains:
            subpixel True
            "Jubes_Sex_Zero_Cock"
#            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            subpixel True
            pos (3,130)#(498,530)
            block:
                pause 0.2
                ease 2 ypos 90 #40
                pause .8
                ease 2 ypos  130 #90
                repeat

# End Jubes Sex Pose Speed 1 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Jubes Sex Pose Speed 2 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_Sex_Anal_Speed2:
    # Pose for Jubes's Sex Pose in which she is doing anal at speed 2
    contains:
            #Jubes's underlying body
            subpixel True
            "Jubes_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.6
                ease 1.0 ypos -200
                pause .9
                ease 1.7 ypos -180
                repeat
    contains:
            #Jubes's Legs
            subpixel True
            "Jubes_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.4
                ease 0.95 ypos -215
                ease 0.25 ypos -210
                pause .8
                ease 1.8 ypos -180
                repeat
#    contains:
#            #Zero's cock in the sex pose
#            AlphaMask("Jubes_Sex_Fucking_Zero_Anim2", "Jubes_Sex_Fucking_Mask")
# End main animation for Sex Pose Fucking Speed 2


image Jubes_Sex_Anal_Zero_Anim2:
        #this is Jubes's sex animation, Speed 2 Fucking
        contains:
            subpixel True
            "Jubes_Sex_Zero_Cock"
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

# End Jubes Sex Pose Speed 2 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Jubes Sex Pose Speed 3 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_Sex_Anal_Speed3:
    # Pose for Jubes's Sex Pose in which she is Anal at speed 3
    contains:
            #Jubes's underlying body
            subpixel True
            "Jubes_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 1.8
#                pause 0.5
                easein .5 ypos -180
                ease .4 ypos -200
                pause .4
                ease .5 ypos -185
                repeat

    contains:
            #Jubes's Legs
            subpixel True
            "Jubes_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 1.8
#                pause 0.4
                easein 0.4 ypos -180
                ease 0.3 ypos -215
                ease 0.1 ypos -210
                pause 0.4
                easeout 0.6 ypos -185
                repeat

# End main animation for Sex Pose Fucking Speed 3


image Jubes_Sex_Anal_Zero_Anim3:
        #this is Jubes's sex animation, Speed3 Anal
        contains:
            subpixel True
            "Jubes_Sex_Zero_Cock"
            subpixel True
            pos (3,-40)
            block:
                pause 0.1
                ease 0.55 ypos -25
                ease 0.15 ypos -20
                pause 0.25
                ease 0.75 ypos 90
                repeat

# End Jubes Sex Pose Speed 3 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Jubes Sex Pose Speed 1 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_Sex_Hotdog_Speed1:
    # Pose for Jubes's Sex Pose in which she is hotdogging at speed 1 (slow)
    contains:
            #Jubes's underlying body
            subpixel True
            "Jubes_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.8
                ease 0.8 ypos -190 #-120
                pause .5
                ease 1.0 ypos -180 #-130
                pause 0.4
                repeat
    contains:
            #Jubes's Legs
            subpixel True
            "Jubes_Sex_Legs"
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
            "Jubes_Sex_Zero_Cock"
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
            #Jubes's Feet
            subpixel True
            "Jubes_Sex_Feet"
#            ConditionSwitch(
#                #Footjob overlay
#                "ShowFeet", AlphaMask("Jubes_Sex_Feet", "images/JubesSex/Jubes_Sex_FeetMask.png"),
#                "True", Null(),
#                )
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.6
                ease 0.7 ypos -200 #-120
                ease 0.2 ypos -195 #-130
                pause .5
                ease 1.0 ypos -180 #-130
                pause 0.5
                repeat

# End main animation for Sex Pose Hotdog Speed 1

# End Jubes Sex Pose Speed 1 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Jubes Sex Pose Speed 2 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_Sex_Hotdog_Speed2:
    # Pose for Jubes's Sex Pose in which she is hotdogging at speed 2 (fast)
    contains:
            #Jubes's underlying body
            subpixel True
            "Jubes_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.25
                ease 0.45 ypos -195 #-120
                pause .1
                ease 0.8 ypos -180 #-130
#                pause 0.2
                repeat
    contains:
            #Jubes's Legs
            subpixel True
            "Jubes_Sex_Legs"
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
            "Jubes_Sex_Zero_Cock"
            subpixel True
            pos (0,-180)
            block:
#                pause 1.2
                ease 0.5 ypos -330 #-120
                pause 0.25
                ease 0.75 ypos -205 #-130
                ease 0.1 ypos -210 #-130
#                pause 0.3
                repeat
    contains:
            #Jubes's Feet
            subpixel True
            "Jubes_Sex_Feet"
#            ConditionSwitch(
#                #Footjob overlay
#                "ShowFeet", AlphaMask("Jubes_Sex_Feet", "images/JubesSex/Jubes_Sex_FeetMask.png"),
#                "True", Null(),
#                )
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.1
                ease 0.4 ypos -215 #-120
                ease 0.1 ypos -205 #-130
                pause 0.25
                ease 0.75 ypos -180 #-130
#                pause 0.25
                repeat

# End main animation for Sex Pose Hotdog Speed 2

# End Jubes Sex Pose Speed 2 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Jubes Sex Pose Speed 0 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_Sex_FJ_Speed0:
    # Pose for Jubes's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Jubes's underlying body
            subpixel True
            "Jubes_Sex_Body"
            pos (80,-140) #X less is left, Y less is up
            block: #adds to 5
                ease 2 ypos -120#-40 #-140
                pause 0.8
                ease 2 ypos -140#-60 #-180
                pause 0.2
                repeat
    contains:
            #Jubes's Legs
            subpixel True
            "Jubes_Sex_Legs"
            pos (80,-180) #X less is left, Y less is up (80,0)
            block: #adds to 5
                pause 0.2
                ease 2 ypos -190 #10
                pause 0.8
                ease 2 ypos -180 #0
                repeat
    contains:
            subpixel True
            "Jubes_Sex_Zero_Cock"
            subpixel True
            pos (0,-380) #(0,-140)
    contains:
            #Jubes's Legs
            subpixel True
            AlphaMask("Jubes_Sex_Feet", "images/JubesSex/Jubes_Sex_Toes.png")
            pos (80,-180) #X less is left, Y less is up (80,0)
            block: #adds to 5
                pause 0.2
                ease 2 ypos -190 #10
                pause 0.8
                ease 2 ypos -180 #0
                repeat

# End main animation for Sex Pose Footjob Speed 0

# End Jubes Sex Pose Speed 0 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Jubes Sex Pose Speed 1 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_Sex_FJ_Speed1:
    # Pose for Jubes's Sex Pose in which she is fucking at speed 1 (slow)
    contains:
            #Jubes's underlying body
            subpixel True
            "Jubes_Sex_Body"
            pos (80,-160) #X less is left, Y less is up
            block: #adds to 5
                ease 2 ypos -120 #-140
                pause 0.8
                ease 2 ypos -160 #-180
                pause 0.2
                repeat
    contains:
            #Jubes's Legs
            subpixel True
            "Jubes_Sex_Legs"
            pos (80,-200) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -140 #40
                pause 0.8
                ease 2 ypos -200 #-100
                repeat
    contains:
            subpixel True
            "Jubes_Sex_Zero_Cock"
            subpixel True
            pos (0,-360)
            block:
                pause 1.5
                ease 0.7 ypos -340 #-120
                pause 1
                ease 1 ypos -360 #-140
                pause 0.8
                repeat
    contains:
            #Jubes's Legs
            subpixel True
            AlphaMask("Jubes_Sex_Feet", "images/JubesSex/Jubes_Sex_Toes.png")
#            ConditionSwitch(
#                #Footjob overlay
#                "ShowFeet", AlphaMask("Jubes_Sex_Feet", "images/JubesSex/Jubes_Sex_Toes.png"),
#                "True", Null(),
#                )
            pos (80,-200) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -140 #40
                pause 0.8
                ease 2 ypos -200 #-100
                repeat

# End main animation for Sex Pose Footjob Speed 1

# End Jubes Sex Pose Speed 1 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Jubes Sex Pose Speed 2 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_Sex_FJ_Speed2:
    # Pose for Jubes's Sex Pose in which she is fucking at speed 2 (fast)
    contains:
            #Jubes's underlying body
            subpixel True
            "Jubes_Sex_Body"
            pos (80,-220) #X less is left, Y less is up
            block: #adds to 2.1
                ease 0.8 ypos -160 #-140
                pause 0.1
                ease 0.9 ypos -220 #-180
                pause 0.1
                repeat
    contains:
            #Jubes's Legs
            subpixel True
            "Jubes_Sex_Legs"
            pos (80,-230) #X less is left, Y less is up
            block: #adds to 5
                pause 0.1
                ease 0.8 ypos -160 #0
                pause 0.1 #0.4
                ease 0.9 ypos -230 #-130
                repeat
    contains:
            subpixel True
            "Jubes_Sex_Zero_Cock"
            subpixel True
            transform_anchor True
            anchor (0.5,0.9)
            pos (560,380)#(530,540)   #(0,-180)
            rotate 0
            parallel:
                pause 0.4
                ease 0.6 rotate 10#0
                ease 0.2 rotate 8#0
                pause 0.3
                ease 0.4 rotate 0 #-130
#                pause 0.1
                repeat
            parallel:
                pause 0.6
                ease 0.3 ypos 400 #0
                pause 0.2
                ease 0.4 ypos 380 #-130
                pause 0.4
                repeat
    contains:
            #Jubes's Legs
            subpixel True
            AlphaMask("Jubes_Sex_Feet", "images/JubesSex/Jubes_Sex_Toes.png")
#            ConditionSwitch(
#                #Footjob overlay
#                "ShowFeet", AlphaMask("Jubes_Sex_Feet", "images/JubesSex/Jubes_Sex_Toes.png"),
#                "True", Null(),
#                )
            pos (80,-230) #X less is left, Y less is up
            block: #adds to 5
                pause 0.1
                ease 0.8 ypos -160 #0
                pause 0.1 #0.4
                ease 0.9 ypos -230 #-130
                repeat

# End main animation for Sex Pose Footjob Speed 2

# End Jubes Sex Pose Speed 2 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     Sex Launch/Reset
label Jubes_Sex_Launch(Line = Trigger):
    $ JubesX.Offhand = 0 if JubesX.Offhand == "hand" else JubesX.Offhand

##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    $ JubesX.Pose = "sex"
##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary

    $ Line = "solo" if not Line else Line
    if Line == "sex":
        $ Player.Sprite = 1
        $ Player.Cock = "in"
        call Cock_Occupied(JubesX,"pussy")
        if Trigger2 in ("fondle pussy","dildo pussy","lick pussy"):
                $ Trigger2 = 0
    elif Line == "anal":
        $ Player.Sprite = 1
        $ Player.Cock = "anal"
        call Cock_Occupied(JubesX,"anal")
        if Trigger2 in ("insert ass","dildo anal","lick ass"):
                $ Trigger2 = 0
    elif Line == "hotdog":
        $ Player.Sprite = 1
        if JubesX.PantsNum() == 5: #upskirts her if she's in a skirt
                $ JubesX.Upskirt = 1
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
        call Zero_Strapped(JubesX) #puts strap-on on.
    $ Trigger = Line

    if JubesX.Pose == "doggy":
            call Jubes_Doggy_Launch(Line)
            return
    if renpy.showing("Jubes_SexSprite"):
        return
    $ Speed = 0
    call Girl_Hide(JubesX,1)
    show Jubes_SexSprite zorder 150
    with dissolve
    return

label Jubes_Sex_Reset:
    if renpy.showing("Jubes_Doggy_Animation"):
        call Jubes_Doggy_Reset
        return
    if not renpy.showing("Jubes_SexSprite"):
        return
    $ JubesX.ArmPose = 2
    hide Jubes_SexSprite
    call Girl_Hide(JubesX)
#    call Set_The_Scene(Dress = 0)
    show Jubes_Sprite at SpriteLoc(JubesX.SpriteLoc) zorder JubesX.Layer:
        alpha 1 zoom 1 offset (0,0) anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return


# End Jubes Sex Pose Content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Jubes's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Jubes's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Jubes_BJ_Animation:#BJ_NewTest:                                                                #core BJ animation
    LiveComposite(
        (858,928),
        (0,0), ConditionSwitch( #-270,-160
            # Jubes's hair backside
            "Speed == 0", "Jubes_BJ_Anim0",               #Static
            "Speed == 1", "Jubes_BJ_Anim1",               #Licking
            "Speed == 2", "Jubes_BJ_Anim2",               #Heading
            "Speed == 3", "Jubes_BJ_Anim3",               #Sucking
            "Speed == 4", "Jubes_BJ_Anim4",               #Deepthroat
            "Speed == 5", "Jubes_BJ_Anim5",               #Cumming High
            "Speed == 6", "Jubes_BJ_Anim6",               #Cumming Deep
            "True", Null(),
            ),
        )
    zoom .55
    anchor (.5,.5)

image Jubes_BJ_Backdrop:
            contains:
                #blanket
                ConditionSwitch(
                    "'blanket' in JubesX.RecentActions", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
                    "True", Null(),
                    )
                zoom 1.2
                anchor (.5,.5)
                pos (440,550)#(180,-400)
            contains:
                #jacket underlayer
                ConditionSwitch(
                        "not JubesX.Acc", Null(),
                        # Modification mode
                        "JubesX.Acc == 'saiyan tail'", Null(),
                        # -----------------
                        "True", Recolor("Jubes", "Acc", "images/JubesBJFace/Jubes_TJ_JacketBack.png"),
                        )
#            contains:
#                #bra straps
#                ConditionSwitch(
#                        "JubesX.Chest == 'sports bra'",Recolor("Jubes", "Chest", "images/JubesBJFace/Jubes_TJ_Chest_Sports_Back.png"),
#                        "JubesX.Chest == 'bikini top'",Recolor("Jubes", "Chest", "images/JubesBJFace/Jubes_TJ_Chest_Bikini_Back.png"),
#                        "True", Null(),
#                        )

            contains:
                "images/JubesBJFace/[JubesX.skin_image.skin_path]Jubes_TJ_Body.png"
            contains:
                #jacket
                ConditionSwitch(
                        "not JubesX.Acc", Null(),
                        # Modification mode
                        "JubesX.Acc == 'saiyan tail'", Null(),
                        # -----------------
                        "True", Recolor("Jubes", "Acc", "images/JubesBJFace/Jubes_TJ_Jacket.png"),
                        )
            contains:
                #Chest
                ConditionSwitch(
                        "JubesX.Chest == 'lace bra' and JubesX.Uptop",Recolor("Jubes", "Chest", "images/JubesBJFace/Jubes_TJ_Chest_Lace_Loose.png"),
                        "JubesX.Chest == 'sports bra' and not JubesX.Uptop",Recolor("Jubes", "Chest", "images/JubesBJFace/Jubes_TJ_Chest_Sports_Loose_Back.png"),
                        "JubesX.Chest == 'bikini top' and not JubesX.Uptop",Recolor("Jubes", "Chest", "images/JubesBJFace/Jubes_TJ_Chest_Bikini_Loose_Back.png"),
                        "True", Null(),
                        )
            contains:
                #Over
                ConditionSwitch(
                        "JubesX.Over == 'red shirt'",Recolor("Jubes", "Over", "images/JubesBJFace/Jubes_TJ_Over_Red.png"),
                        "JubesX.Over == 'black shirt'",Recolor("Jubes", "Over", "images/JubesBJFace/Jubes_TJ_Over_Black.png"),
                        "JubesX.Over == 'tube top'",Recolor("Jubes", "Over", "images/JubesBJFace/Jubes_TJ_Over_Tube_Under.png"),
                        "True", Null(),
                        )
            contains:
                "images/JubesBJFace/[JubesX.skin_image.skin_path]Jubes_TJ_Tits_Loose.png"
            contains:
                #Chest
                ConditionSwitch(
                        "JubesX.Chest == 'lace bra' and not JubesX.Uptop",Recolor("Jubes", "Chest", "images/JubesBJFace/Jubes_TJ_Chest_Lace_Loose.png"),
                        "JubesX.Chest == 'sports bra' and JubesX.Uptop",Recolor("Jubes", "Chest", "images/JubesBJFace/Jubes_TJ_Chest_Sports_Loose_Up.png"),
                        "JubesX.Chest == 'sports bra'",Recolor("Jubes", "Chest", "images/JubesBJFace/Jubes_TJ_Chest_Sports_Loose.png"),
                        "JubesX.Chest == 'bikini top' and JubesX.Uptop",Recolor("Jubes", "Chest", "images/JubesBJFace/Jubes_TJ_Chest_Bikini_Loose_Up.png"),
                        "JubesX.Chest == 'bikini top'",Recolor("Jubes", "Chest", "images/JubesBJFace/Jubes_TJ_Chest_Bikini_Loose.png"),
                        "True", Null(),
                        )
            contains:
                #Over
                ConditionSwitch(
                        "JubesX.Over == 'dress' and not JubesX.Uptop",Recolor("Jubes", "Over", "images/JubesBJFace/Jubes_TJ_Over_Dress.png"),
                        "JubesX.Over == 'tube top' and not JubesX.Uptop",Recolor("Jubes", "Over", "images/JubesBJFace/Jubes_TJ_Over_Tube_Loose.png"),
                        "True", Null(),
                        )
            contains:
                #Over
                ConditionSwitch(
                        "'tits' in JubesX.Spunk and Player.Male","images/JubesBJFace/Jubes_TJ_Spunk_Tits_Loose.png",
                        "True", Null(),
                        )
#            contains:
#                #Piercings clothing
#                ConditionSwitch(
#                        "not JubesX.Pierce", Null(),
#                        "JubesX.Pierce == 'ring'", ConditionSwitch(
#                                #if she's got ring piercings
#                                "JubesX.Uptop", "images/JubesBJFace/Jubes_TJ_Pierce_Ring.png",
#                                "JubesX.Over == 'tube top'", "images/JubesBJFace/Jubes_TJ_Pierce_Ring_Pink.png",
#                                "JubesX.Chest == 'bikini top'", "images/JubesBJFace/Jubes_TJ_Pierce_Ring_Pink.png",
#                                "JubesX.Chest == 'lace bra'", "images/JubesBJFace/Jubes_TJ_Pierce_Ring_Lace.png",
#                                "True", "images/JubesBJFace/Jubes_TJ_Pierce_Ring.png",
#                                ),
#                        "JubesX.Uptop", "images/JubesBJFace/Jubes_TJ_Pierce_Barbell.png",
#                        "JubesX.Over == 'tube top'", "images/JubesBJFace/Jubes_TJ_Pierce_Barbell_Pink.png",
#                        "JubesX.Chest == 'bikini top'", "images/JubesBJFace/Jubes_TJ_Pierce_Barbell_Pink.png",
#                        "JubesX.Chest == 'lace bra'", "images/JubesBJFace/Jubes_TJ_Pierce_Barbell_Lace.png",
#                        "True", "images/JubesBJFace/Jubes_TJ_Pierce_Barbell.png",
#                        )
            transform_anchor True
            zoom 1.3
            anchor (0.4, 1.0)
            offset (225,1000) #1100
            #offset (410,770) # (300,275)
            rotate 0


#        zoom 1.4
#        offset (225,1100)

image Jubes_BJ_Head:                                                                            #These are all the details of the face
    LiveComposite(
        (858,928),
        (0,0), ConditionSwitch(
            # Basic Face layer
            "JubesX.Blush", "images/JubesBJFace/[JubesX.skin_image.skin_path]Jubes_BJ_Head_Blush2.png",
            "True", "images/JubesBJFace/[JubesX.skin_image.skin_path]Jubes_BJ_Head_Blush0.png"
            ),
        (0,0), ConditionSwitch(
            #Mouth
            "Speed and renpy.showing('Jubes_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
                    "Speed == 1", Recolor("Jubes", "Lips", "images/JubesBJFace/Jubes_BJ_Mouth_Tongue.png"),  #licking
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", Recolor("Jubes", "Lips", "images/JubesBJFace/Jubes_BJ_Mouth_Sucking.png"), #sucking
                    "Speed == 4", Recolor("Jubes", "Lips", "images/JubesBJFace/Jubes_BJ_Mouth_Sucking.png"), #deepthroat
                    "Speed == 6", Recolor("Jubes", "Lips", "images/JubesBJFace/Jubes_BJ_Mouth_Sucking.png"), #cumming
                    ),
            "renpy.showing('Jubes_CUN_Animation') and Speed", Recolor("Jubes", "Lips", "images/JubesBJFace/Jubes_BJ_Mouth_Tongue.png"),
            "Speed >= 3 and renpy.showing('Jubes_TJ_Animation')", Recolor("Jubes", "Lips", "images/JubesBJFace/Jubes_BJ_Mouth_Tongue.png"),
            "JubesX.Mouth == 'normal'", Recolor("Jubes", "Lips", "images/JubesBJFace/Jubes_BJ_Mouth_Smile.png"),
            "JubesX.Mouth == 'lipbite'", Recolor("Jubes", "Lips", "images/JubesBJFace/Jubes_BJ_Mouth_Lipbite.png"),
            "JubesX.Mouth == 'sucking'", Recolor("Jubes", "Lips", "images/JubesBJFace/Jubes_BJ_Mouth_Open.png"),
            "JubesX.Mouth == 'kiss'", Recolor("Jubes", "Lips", "images/JubesBJFace/Jubes_BJ_Mouth_Kiss.png"),
            "JubesX.Mouth == 'sad'", Recolor("Jubes", "Lips", "images/JubesBJFace/Jubes_BJ_Mouth_Sad.png"),
            "JubesX.Mouth == 'smile'", Recolor("Jubes", "Lips", "images/JubesBJFace/Jubes_BJ_Mouth_Smile.png"),
            "JubesX.Mouth == 'smirk'", Recolor("Jubes", "Lips", "images/JubesBJFace/Jubes_BJ_Mouth_Smirk.png"),
            "JubesX.Mouth == 'grimace'", Recolor("Jubes", "Lips", "images/JubesBJFace/Jubes_BJ_Mouth_Smile.png"),
            "JubesX.Mouth == 'surprised'", Recolor("Jubes", "Lips", "images/JubesBJFace/Jubes_BJ_Mouth_Kiss.png"),
            "JubesX.Mouth == 'tongue'", Recolor("Jubes", "Lips", "images/JubesBJFace/Jubes_BJ_Mouth_Tongue.png"),
            "True", Recolor("Jubes", "Lips", "images/JubesBJFace/Jubes_BJ_Mouth_Smile.png"),
            ),
        (428,555), ConditionSwitch(   #(428,605)
            # Heading Mouth
#            "Speed == 2 and Trigger == 'blow'", At("Jubes_BJ_MouthHeading", Jubes_BJ_MouthAnim()),  #heading
            "not renpy.showing('Jubes_BJ_Animation')", Null(),                       #heading
            "Speed == 2", "Jubes_BJ_MouthHeading",#At("Jubes_BJ_MouthHeading", Jubes_BJ_MouthAnim()),  #heading
            "Speed == 5", "Jubes_BJ_MouthCumHigh",#At("Jubes_BJ_MouthHeading", Jubes_BJ_MouthAnimC()), #cumming high
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Spunk layer
            "'mouth' not in JubesX.Spunk or not Player.Male", Null(),
            "Speed and renpy.showing('Jubes_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
                    "Speed == 1", "images/JubesBJFace/Jubes_BJ_Spunk_Tongue.png",  #licking
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", "images/JubesBJFace/Jubes_BJ_Spunk_SuckingUnder.png", #sucking
                    "Speed == 4", "images/JubesBJFace/Jubes_BJ_Spunk_SuckingUnder.png", #deepthroat
                    "Speed == 6", "images/JubesBJFace/Jubes_BJ_Spunk_SuckingUnder.png", #cumming
                    ),
#            "JubesX.Mouth == 'normal'", "images/JubesBJFace/Jubes_BJ_Spunk_Smile.png",
            "JubesX.Mouth == 'lipbite'", "images/JubesBJFace/Jubes_BJ_Spunk_Smile.png",
#            "JubesX.Mouth == 'kiss'", "images/JubesBJFace/Jubes_BJ_Spunk_Kiss.png",
#            "JubesX.Mouth == 'sad'", "images/JubesBJFace/Jubes_BJ_Spunk_Kiss.png",
            "JubesX.Mouth == 'smile'", "images/JubesBJFace/Jubes_BJ_Spunk_Smile.png",
#            "JubesX.Mouth == 'smirk'", "images/JubesBJFace/Jubes_BJ_Spunk_Kiss.png",
#            "JubesX.Mouth == 'surprised'", "images/JubesBJFace/Jubes_BJ_Spunk_Kiss.png",
            "JubesX.Mouth == 'open'", "images/JubesBJFace/Jubes_BJ_Spunk_Tongue.png",
            "JubesX.Mouth == 'tongue'", "images/JubesBJFace/Jubes_BJ_Spunk_Tongue.png",
            "JubesX.Mouth == 'sucking'", "images/JubesBJFace/Jubes_BJ_Spunk_Tongue.png",
            "True", "images/JubesBJFace/Jubes_BJ_Spunk_Smirk.png",
            ),

        (0,0), ConditionSwitch(
            #wet face
            "Player.Male", Null(),
            "'mouth' not in JubesX.Spunk and 'chin' not in JubesX.Spunk", Null(),
            "'chin' not in JubesX.Spunk and (JubesX.Mouth == 'tongue' or Speed)", "images/JubesBJFace/Jubes_BJ_Wet_Tongue.png",
            "JubesX.Mouth == 'tongue' or Speed", "images/JubesBJFace/Jubes_BJ_Wet_Tongue2.png",
            "'mouth' in JubesX.Spunk or 'chin' in JubesX.Spunk", "images/JubesBJFace/Jubes_BJ_Wet_Mouth.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Brows
            "JubesX.Brows == 'angry'", "images/JubesBJFace/[JubesX.skin_image.skin_path]Jubes_BJ_Brows_Angry.png",
            "JubesX.Brows == 'sad'", "images/JubesBJFace/[JubesX.skin_image.skin_path]Jubes_BJ_Brows_Sad.png",
            "JubesX.Brows == 'surprised'", "images/JubesBJFace/[JubesX.skin_image.skin_path]Jubes_BJ_Brows_Surprised.png",
            "JubesX.Brows == 'confused'", "images/JubesBJFace/[JubesX.skin_image.skin_path]Jubes_BJ_Brows_Confused.png",
            "True", "images/JubesBJFace/[JubesX.skin_image.skin_path]Jubes_BJ_Brows_Normal.png",
            ),
        (0,0), "Jubes BJ Blink",
            #Eyes
        (0,0), "images/JubesBJFace/Jubes_BJ_Earring.png",
        # Modification mode
        (0,0), ConditionSwitch(
            #glasses under
            "JubesX.Hair == 'shades'", Recolor("Jubes", "Hair", "images/JubesBJFace/Jubes_BJ_Hair_Shades.png"),
            "True", Null(),
            ),
        # -----------------
        (0,0), ConditionSwitch(
            #Hair overlay
            "JubesX.Water or JubesX.Hair == 'wet'", Recolor("Jubes", "Hair", "images/JubesBJFace/Jubes_BJ_Hair_Wet.png"),
            "not Player.Male and 'facial' in JubesX.Spunk",Recolor("Jubes", "Hair", "images/JubesBJFace/Jubes_BJ_Hair_Wet.png"),
            "JubesX.Hair == 'shades'", Recolor("Jubes", "Hair", "images/JubesBJFace/Jubes_BJ_Hair_Shades.png"),
            "True", Recolor("Jubes", "Hair", "images/JubesBJFace/Jubes_BJ_Hair_Short.png"),
            ),
        (0,0), ConditionSwitch(
            # water overlay
            "JubesX.Water", "images/JubesBJFace/Jubes_BJ_Wet.png",
            "not Player.Male and 'facial' in JubesX.Spunk", "images/JubesBJFace/Jubes_BJ_Wet.png",
            "True",Null(),
            ),

#        (0,0), "Jubes_Tester",
        (0,0), ConditionSwitch(
            #cum on the face
            "'hair' in JubesX.Spunk and Player.Male", "images/JubesBJFace/Jubes_BJ_Spunk_Hair.png",
            "'facial' in JubesX.Spunk and Player.Male", "images/JubesBJFace/Jubes_BJ_Spunk_Facial.png",
            "True", Null(),
            ),
        )
    zoom 1.4
    anchor (0.5, 0.5)

image Jubes_Tester:
            "images/JubesBJFace/Jubes_BJ_tester.jpg"
            alpha 0.5
image Jubes BJ Blink:
        #eyeblinks
        ConditionSwitch(
            "JubesX.Eyes == 'normal'", "images/JubesBJFace/Jubes_BJ_Eyes_Normal.png",
            "JubesX.Eyes == 'sexy'", "images/JubesBJFace/Jubes_BJ_Eyes_Sexy.png",
            "JubesX.Eyes == 'closed'", "images/JubesBJFace/Jubes_BJ_Eyes_Closed.png",
            "JubesX.Eyes == 'surprised'", "images/JubesBJFace/Jubes_BJ_Eyes_Surprised.png",
            "JubesX.Eyes == 'side'", "images/JubesBJFace/Jubes_BJ_Eyes_Side.png",
            "JubesX.Eyes == 'leftside'", "images/JubesBJFace/Jubes_BJ_Eyes_Leftside.png",
            "JubesX.Eyes == 'stunned'", "images/JubesBJFace/Jubes_BJ_Eyes_Stunned.png",
            "JubesX.Eyes == 'down'", "images/JubesBJFace/Jubes_BJ_Eyes_Down.png",
            "JubesX.Eyes == 'manic'", "images/JubesBJFace/Jubes_BJ_Eyes_Surprised.png",
            "JubesX.Eyes == 'squint'", "images/JubesBJFace/Jubes_BJ_Eyes_Squint.png",
            "True", "images/JubesBJFace/Jubes_BJ_Eyes_Normal.png",
            ),
        choice:
            3.5
        choice:
            3.25
        choice:
            3
        "images/JubesBJFace/Jubes_BJ_Eyes_Closed.png"
        .25
        repeat

image Jubes_BJ_MouthHeading:
    #the mouth used for the heading animations
    transform_anchor True
    contains:
        Recolor("Jubes", "Lips", "images/JubesBJFace/Jubes_BJ_Mouth_Sucking.png")
#        Recolor("Jubes", "Lips", "images/JubesBJFace/Jubes_BJ_Mouth_Heading.png")
        zoom 1.4
        anchor (0.50,0.6)  #(0.50,0.65)
    contains:
        ConditionSwitch(
            "'mouth' in JubesX.Spunk and Player.Male", "images/JubesBJFace/Jubes_BJ_Spunk_SuckingUnder.png",#At("Jubes_BJ_MaskHeading", Jubes_BJ_MouthAnim()),
            "True", Null(),
            ),
        zoom 1.4
        anchor (0.50,0.6)  #(0.50,0.65)
    contains:
        ConditionSwitch(
            "'mouth' in JubesX.Spunk and Player.Male", "images/JubesBJFace/Jubes_BJ_Spunk_SuckingOver.png",#At("Jubes_BJ_MaskHeading", Jubes_BJ_MouthAnim()),
            "True", Null(),
            ),
        zoom 1.4
        anchor (0.50,0.6)  #(0.50,0.65)
    subpixel True
    zoom 0.58 #0.58 = top of heading, 0.66 = crown, 0.60 = valley, 0.68 = base
    block: #total time 1.0 down, 1.5 back up 2.5 total
        pause .20
        easeout .15 zoom 0.6#0.66
        linear .15 zoom 0.60
        easein .25 zoom 0.65
        pause .25
        #1.0s to this point
        pause .40
        easeout .40 zoom 0.58
        linear .10 zoom 0.66
        easein .30 zoom 0.45#0.45
        pause .30
        #1.5s to this point
        repeat

image Jubes_BJ_MouthCumHigh:
    #the mouth used for the heading animations
    contains:
        Recolor("Jubes", "Lips", "images/JubesBJFace/Jubes_BJ_Mouth_Sucking.png")
        zoom 1.4
        anchor (0.50,0.6)  #(0.50,0.65)
    contains:
        ConditionSwitch(
            "'mouth' in JubesX.Spunk and Player.Male", "images/JubesBJFace/Jubes_BJ_Spunk_SuckingOver.png",#At("Jubes_BJ_MaskHeading", Jubes_BJ_MouthAnim()),
            "True", Null(),
            ),
        zoom 1.4
        anchor (0.50,0.6)  #(0.50,0.65)
    subpixel True
    zoom 0.55 #0.70
    block: #total time 10 down, 15 back up
        pause .20
        ease .50 zoom 0.48#0.65
        pause .60
        ease .30 zoom 0.52#0.7
        pause .10
        ease .30 zoom 0.48#0.65
        pause .20
        ease .30 zoom 0.52#0.7
        repeat

image Jubes_BJ_MouthSuckingMask:
    #the mask used for sucking animations
    contains:
        "images/JubesBJFace/Jubes_BJ_Mouth_MaskS.png"
        zoom 1.4
    contains: #see if this works, if not remove it
        ConditionSwitch(
            "'mouth' not in JubesX.Spunk and Player.Male", Null(),
            "Speed != 2 and Speed != 5", Null(),
            "True", "images/JubesBJFace/Jubes_BJ_Spunk_SuckingOver.png",
            )
        zoom 1.4

#image Jubes_BJ_MaskHeading:
#    #the mask used for the heading image
#    contains:
#        "images/JubesBJFace/Jubes_BJ_Mouth_MaskH.png"
#        #offset (-380,-595)

image Jubes_BJ_MaskHeadingComposite:
    #The composite for the heading mask that goes over the face
    LiveComposite(
        (858,928),
        (300,462), ConditionSwitch(
            "Speed == 2", "Jubes_BJ_MouthHeadingComposite",#At("Jubes_BJ_MaskHeading", Jubes_BJ_MouthAnim()),
            "Speed == 5", "Jubes_BJ_MouthCumHighComposite",#At("Jubes_BJ_MaskHeading", Jubes_BJ_MouthAnimC()),
            "True", Null(),
            ),
        (300,462), ConditionSwitch(
            "Speed == 2 and 'mouth' in JubesX.Spunk and Player.Male", "JubesHeadingSpunk",#At("Jubes_BJ_MaskHeading", Jubes_BJ_MouthAnim()),
            "Speed == 5 and 'mouth' in JubesX.Spunk and Player.Male", "JubesCumHighSpunk",#At("Jubes_BJ_MaskHeading", Jubes_BJ_MouthAnimC()),
            "True", Null(),
            ),
        )
    zoom 1.8

image Jubes_BJ_MouthHeadingComposite:
    #the mask for the overlay used for the heading animations
    transform_anchor True
    contains:
#        "images/JubesBJFace/Jubes_BJ_Mouth_MaskH.png"
        "images/JubesBJFace/Jubes_BJ_Mouth_MaskS.png"
#        zoom 1.4
        anchor (0.50,0.6)  #(0.50,0.65)
    offset (30,-30)
    subpixel True
    zoom 0.58 #0.58 = top of heading, 0.66 = crown, 0.60 = valley, 0.68 = base
    block: #total time 1.0 down, 1.5 back up 2.5 total
        pause .20
        easeout .15 zoom 0.6#0.66
        linear .15 zoom 0.60
        easein .25 zoom 0.65
        pause .25
        #1.0s to this point
        pause .40
        easeout .40 zoom 0.58
        linear .10 zoom 0.66
        easein .30 zoom 0.45#0.55
        pause .30
        #1.5s to this point
        repeat

image JubesHeadingSpunk:
    #Spunk that goes over the sock when sucking
    transform_anchor True
    contains:
        "images/JubesBJFace/Jubes_BJ_Spunk_SuckingOver.png"
#        zoom 1.4
        anchor (0.50,0.6)  #(0.50,0.65)
    offset (30,-30)
    subpixel True
    zoom 0.58 #0.58 = top of heading, 0.66 = crown, 0.60 = valley, 0.68 = base
    block: #total time 1.0 down, 1.5 back up 2.5 total
        pause .20
        easeout .15 zoom 0.6#0.66
        linear .15 zoom 0.60
        easein .25 zoom 0.65
        pause .25
        #1.0s to this point
        pause .40
        easeout .40 zoom 0.58
        linear .10 zoom 0.66
        easein .30 zoom 0.45#0.55
        pause .30
        #1.5s to this point
        repeat


image Jubes_BJ_MouthCumHighComposite:
    #the mask for the overlay used for the cumming high animations
    contains:
#        "Jubes_BJ_MaskHeading"
        "images/JubesBJFace/Jubes_BJ_Mouth_MaskH.png"
        anchor (0.50,0.6)  #(0.50,0.65)
    subpixel True
    offset (30,-30)
    zoom 0.65 #0.70
    block: #total time 10 down, 15 back up
        pause .20
        ease .50 zoom 0.58#0.65
        pause .60
        ease .30 zoom 0.62#0.7
        pause .10
        ease .30 zoom 0.58#0.65
        pause .20
        ease .30 zoom 0.62#0.7
        repeat

image JubesCumHighSpunk:
    #Spunk that goes over the sock when sucking
    transform_anchor True
    contains:
        "images/JubesBJFace/Jubes_BJ_Spunk_SuckingOver.png"
        anchor (0.50,0.6)  #(0.50,0.65)
    offset (30,-30)
    subpixel True
    zoom 0.65 #0.70
    block: #total time 10 down, 15 back up
        pause .20
        ease .50 zoom 0.58#0.65
        pause .60
        ease .30 zoom 0.62#0.7
        pause .10
        ease .30 zoom 0.58#0.65
        pause .20
        ease .30 zoom 0.62#0.7
        repeat




image JubesSuckingSpunk:
    #Spunk that goes over the sock when sucking
    contains:
        "images/JubesBJFace/Jubes_BJ_Spunk_SuckingOver.png"
        zoom 1.4
        anchor (0.5, 0.5)

# Start 0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jubes_BJ_Backdrop1:
        #Her Body in the BJ pose
#        contains:
#            #blanket
#            ConditionSwitch(
#                "'blanket' in JubesX.RecentActions", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
#                "True", Null(),
#                )
#            zoom 1.2
#            anchor (.5,.5)
#            pos (180,-400)
#            block:
#                ease 1 pos (0,-600)
#                ease 1 pos (-350,0)
#                ease 1 pos (-350,0)
#                ease 1 pos (-350,-600)
#                repeat
#        contains:
#                #bra strap backing
#                "Jubes_TJ_Jacketback"
#                subpixel True
#                pos (0,0) #top (0,-15)
#                transform_anchor True
#        contains:
#                #bra strap backing
#                "Jubes_TJ_Braback"
#                subpixel True
#                pos (0,0) #top (0,-15)
#                transform_anchor True
##                parallel:
##                    ease 2 ypos -20
##                    pause .1
##                    ease 2 ypos -0
##                    pause .1
##                    repeat
        contains:
                #base body test / / / / / / / / / / / / / / / / / / / /
                "Jubes_BJ_Body"
                subpixel True
                pos (0,0) #top (0,-10)
                transform_anchor True
#                parallel:
#                    ease 2 ypos -20
#                    pause .1
#                    ease 2 ypos 0
#                    pause .1
#                    repeat
#        contains:
#                #right hand backside
#                "Jubes_TJ_TitR"
#                subpixel True
#                pos (0,0) #top (0,-15)
#                transform_anchor True
##                parallel:
##                    ease 2 ypos -20
##                    pause .1
##                    ease 2 ypos -0
##                    pause .1
##                    repeat
#        contains:
#                "Jubes_TJ_Tits"
#                subpixel True
#                pos (0,0) #top (0,-15)
#                transform_anchor True
##                parallel:
##                    ease 2 ypos -20
##                    pause .1
##                    ease 2 ypos -0
##                    pause .1
##                    repeat
        zoom 1.4
        offset (225,1100)

# End Jubes BJ Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_BJ_Anim0:
        #Static animation
        contains:
                #  Jubes's body, everything below the chin
                "Jubes_BJ_Backdrop"
                subpixel True
                offset (0,0)     #(-20,270)
        contains:
                # Jubes's head Underlay
                "Jubes_BJ_Head"
                subpixel True
                offset (350,210)     #-270,-160
        contains:
                # Cock
                "Blowcock"
                anchor (.5,.5)
                rotate -10
                offset (645,370)#(0,50)
#end Jubes_BJ_Anim0 Static

image Jubes_BJ_Anim1:
        #Licking animation
        contains:
                #  Jubes's body, everything below the chin
                "Jubes_BJ_Backdrop"
                subpixel True
                offset (0,-35)  #top
                block:
                    ease 2.5 offset (30,90) #bottom 25,50
                    ease 2 offset (0,-35)  #top
                    pause .5
                    repeat #(-20,270)
        contains:
                # Jubes's head Underlay
                "Jubes_BJ_Head"
                subpixel True
                offset (350,175)  #top
                block:
                    ease 2.5 offset (375,310) #bottom
                    ease 2 offset (350,175)  #top
                    pause .5
                    repeat  #-270,-160
        contains:
                # Cock
                "Blowcock"
                subpixel True
                anchor (.5,.5)
                offset (645,370)
                rotate 0
                block:
                    ease 2 rotate -5 #410
                    pause .5
                    ease 2.5 rotate 0
                    repeat
#end Jubes_BJ_Anim1 Licking


image Jubes_BJ_Anim2:
        #Heading animation
        contains:
                #  Jubes's body, everything below the chin
                "Jubes_BJ_Backdrop"
                subpixel True
                offset (0,-40)     #top
                block:
                    ease 1 yoffset 15           #bottom
                    ease 1.5 yoffset -40     #top
                    repeat #(-20,270)
        contains:
                # Jubes's head Underlay
                "Jubes_BJ_Head"
                subpixel True
                offset (340,190)     #top (350,190), -20 is crown, 0 is mid
                block:
                    ease 1 offset (355,270)  #250#40           #bottom
                    ease 1.5 offset (340,190)   #170 #(0,-40)     #top
                    repeat   #-270,-160
        contains:
                # Cock
                "Blowcock"
                subpixel True
                anchor (.5,.5)
                rotate 0
                alpha 1
                offset (645,370)  #(650,370)
        contains:
                # Masked overlay for heading animaton
                AlphaMask("Jubes_BJ_Head", "Jubes_BJ_MaskHeadingComposite") #"Jubes_BJ_MouthHeadingComposite")
                subpixel True
#                alpha .9
                offset (-260,-460)  #top (-250,-460), -20 is crown, 0 is mid
                block:
                    ease 1 offset (-245,-380)#-400           #bottom
                    ease 1.5 offset (-260,-460)#-480     #top
                    repeat   #-270,-160
#end Jubes_BJ_Anim2 Heading



image Jubes_BJ_Anim3:
        #Sucking animation
        contains:
                #  Jubes's body, everything below the chin
                "Jubes_BJ_Backdrop"
                subpixel True
                offset (0,50)
                block:
                    ease 1 yoffset 100 #100      #bottom
                    ease 1.5 yoffset 50 #50 #top
                    repeat #(-20,270)
        contains:
                # Jubes's head Underlay
                "Jubes_BJ_Head"
                subpixel True
                #offset (350,210)
                offset (350,260)
                block:
                    ease 1 yoffset 330 #120
                    ease 1.5 yoffset 260 #0
                    repeat     #-270,-160
        contains:
                # Cock
                "Blowcock"
                subpixel True
                anchor (.5,.5)
                rotate 0
                alpha 1
                offset (645,370)
        contains:
                # Masked overlay for sucking animaton
                AlphaMask("Jubes_BJ_Head", "Jubes_BJ_MouthSuckingMask")
                subpixel True
                offset (-250,-390)#(-250,-500) #is -600x,-650y from normal
                block:
                    ease 1 yoffset -320 #120
                    ease 1.5 yoffset -390 #50
                    repeat     #-270,-160
        contains:
                # the over part of spunk
                ConditionSwitch(
                        # the over part of spunk
                        "'mouth' in JubesX.Spunk and Player.Male", "JubesSuckingSpunk",
                        "True", Null(),
                        )
                subpixel True
                offset (350,260)
                block:
                    ease 1 yoffset 330 #120
                    ease 1.5 yoffset 260 #0
                    repeat     #-270,-160
#end Jubes_BJ_Anim3 Sucking

image Jubes_BJ_Anim4:
        #Deep animation
        contains:
                #  Jubes's body, everything below the chin
                "Jubes_BJ_Backdrop"
                subpixel True
                offset (0,100)
                block:
                    subpixel True
                    ease 1.2 yoffset 250
                    pause .5
                    ease 1.8 yoffset 100
                    repeat    #(-20,270)
        contains:
                # Jubes's head Underlay
                "Jubes_BJ_Head"
                subpixel True
                offset (355,360)
                block:
                    subpixel True
                    ease 1 yoffset 560#300
                    pause .5
                    ease 2 yoffset 360#100
                    repeat   #-270,-160
        contains:
                # Cock
                "Blowcock"
                subpixel True
                anchor (.5,.5)
                rotate 0
                alpha 1
                offset (645,370)
        contains:
                # Masked overlay for sucking animaton
                AlphaMask("Jubes_BJ_Head", "Jubes_BJ_MouthSuckingMask")
                subpixel True
                offset (-245,-290)
                block:
                    subpixel True
                    ease 1 yoffset -90
                    pause .5
                    ease 2 yoffset -290
                    repeat   #-270,-160
        contains:
                # the over part of spunk
                ConditionSwitch(
                        # the over part of spunk
                        "'mouth' in JubesX.Spunk and Player.Male", "JubesSuckingSpunk",
                        "True", Null(),
                        )
                subpixel True
                offset (355,360)
                block:
                    subpixel True
                    ease 1 yoffset 560#300
                    pause .5
                    ease 2 yoffset 360#100
                    repeat   #-270,-160
#end Jubes_BJ_Anim4 Deep


image Jubes_BJ_Anim5:
        #Cum high animation
        contains:
                #  Jubes's body, everything below the chin
                "Jubes_BJ_Backdrop"
                subpixel True
                offset (0,-30)     #top
                block:
                    ease 1 yoffset -20           #bottom
                    ease 1.5 yoffset -30     #top
                    repeat     #(-20,270)
        contains:
                # Jubes's head Underlay
                "Jubes_BJ_Head"
                subpixel True
                #offset (350,210)
                offset (340,200)     #top
                block:
                    ease 1 yoffset 210           #bottom
                    ease 1.5 yoffset 200     #top
                    repeat  #-270,-160
        contains:
                # Cock
                "Blowcock"
                subpixel True
                anchor (.5,.5)
                rotate 0
                alpha 1
                offset (645,370)
        contains:
                # Masked overlay for sucking animaton
                AlphaMask("Jubes_BJ_Head", "Jubes_BJ_MaskHeadingComposite")
                subpixel True
                offset (-260,-450)     #top
                block:
                    ease 1 yoffset -440           #bottom
                    ease 1.5 yoffset -450     #top
                    repeat  #-270,-160
        contains:
                # Jubes's spunk
                ConditionSwitch(
                        # the over part of spunk
                        "'mouth' in JubesX.Spunk and Player.Male", "JubesCumHighSpunk",
                        "True", Null(),
                        )
                subpixel True
                #offset (350,210)
                offset (340,200)     #top
                block:
                    ease 1 yoffset 210           #bottom
                    ease 1.5 yoffset 200     #top
                    repeat  #-270,-160

#end Jubes_BJ_Anim5 Cum high
#end Jubes_BJ_Anim5 Cum high


image Jubes_BJ_Anim6:
        #Cum Deep animation
        contains:
                #  Jubes's body, everything below the chin
                "Jubes_BJ_Backdrop"
                subpixel True
                offset (0,190)
                block:
                    subpixel True
                    ease 1.2 yoffset 200
                    pause .5
                    ease 1.8 yoffset 190
                    repeat      #(-20,270)
        contains:
                # Jubes's head Underlay
                "Jubes_BJ_Head"
                subpixel True
                #offset (350,210)
                offset (355,440)#230)
                block:
                    subpixel True
                    ease 1 yoffset 460
                    pause .5
                    ease 2 yoffset 440
                    repeat       #-270,-160
        contains:
                # Cock
                "Blowcock"
                subpixel True
                anchor (.5,.5)
                rotate 0
                alpha 1
                offset (645,370)
        contains:
                # Masked overlay for sucking animaton
                AlphaMask("Jubes_BJ_Head", "Jubes_BJ_MouthSuckingMask")
                subpixel True
                offset (-245,-210)#230)
                block:
                    subpixel True
                    ease 1 yoffset -190
                    pause .5
                    ease 2 yoffset -210
                    repeat       #-270,-160
        contains:
                # the over part of spunk
                ConditionSwitch(
                        # the over part of spunk
                        "'mouth' in JubesX.Spunk and Player.Male", "JubesSuckingSpunk",
                        "True", Null(),
                        )
                subpixel True
                offset (355,440)#230)
                block:
                    subpixel True
                    ease 1 yoffset 460
                    pause .5
                    ease 2 yoffset 440
                    repeat       #-270,-160
#end Jubes_BJ_Anim6 Cum Deep

#Head and Body Animations for Jubes's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
                                                               #BJ Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Jubes_BJ_Launch(Line = Trigger):    # The sequence to launch the Jubes BJ animations
    if renpy.showing("Jubes_BJ_Animation"):
        return

    if not Player.Male:
        call Jubes_CUN_Launch
        return

    if renpy.showing("Jubes_TJ_Animation"):
            hide Jubes_TJ_Animation
    else:
            call Girl_Hide(JubesX)
            if Line == "L" or Line == "cum":
                show Jubes_Sprite at SpriteLoc(StageCenter) zorder 150:
                    alpha 1
                    ease 1 zoom 2.5 offset (150,80)
                with dissolve
            else:
                show Jubes_Sprite at SpriteLoc(StageCenter) zorder 150:
                    alpha 1 zoom 2.5 offset (150,80)
                with dissolve
            hide Jubes_Sprite
    #". . ."
    $ Speed = 0

    if Line != "cum":
        $ Trigger = "blow"

    show Jubes_BJ_Animation zorder 150:
        pos (630,650) #(645,510)
    if Taboo and Line == "L": # Jubes gets started. . .
            if len(Present) >= 2:
                if Present[0] != JubesX:
                        "[JubesX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                elif Present[1] != JubesX:
                        "[JubesX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
            else:
                        "[JubesX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
            "Затем она наклоняется и берет ваш член в свой рот."
    elif Line == "L":
            "[JubesX.Name] плавно наклоняется и прислоняет ваш член к своей щеке."

    return

label Jubes_BJ_Reset: # The sequence to the Jubes animations from BJ to default
    if Player.Male != 1:
            call Jubes_CUN_Reset
    if not renpy.showing("Jubes_BJ_Animation"):
        return
#    hide Jubes_BJ_Animation
    call Girl_Hide(JubesX)
    $ Speed = 0

    show Jubes_Sprite at SpriteLoc(StageCenter) zorder 150:
        alpha 1 zoom 2.5 offset (150,80)
    with dissolve

    show Jubes_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .2
        ease .3 zoom 1 offset (0,0)
    pause 1.5
    show Jubes_Sprite at SpriteLoc(JubesX.SpriteLoc) zorder JubesX.Layer:
        alpha 1 zoom 1 offset (0,0)
    return

# End Jubes Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Jubes's TJ animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Animation components / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# start base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Jubes_TJ_Animation:
            #core TJ animation
            contains:
                ConditionSwitch(
                    # Jubes's upper body
                    "not Player.Sprite","Jubes_TJ_0",#Static
                    "Speed == 1", "Jubes_TJ_1",#slow
                    "Speed == 3", "Jubes_TJ_3",#licking
                    "Speed == 4", "Jubes_TJ_4",#cumming high
                    "Speed == 5", "Jubes_TJ_5",#cumming low
                    "Speed >= 2", "Jubes_TJ_2",#fast
                    "True",       "Jubes_TJ_0",#Static
                    )
            zoom .8 #.7
            transform_anchor True
            anchor (.5,.5)
# end base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Jubes_TJ_Head:
            #Hair underlay
            "Jubes_BJ_Head"
            transform_anchor True
            zoom .7
            anchor (0.5, 0.5)
            offset (30,-450)
            rotate 0


image Jubes_TJ_ZeroCock:
            #cock used in jubes's sex pose
            "Zero_Blowcock"
            transform_anchor True
            zoom .6
            anchor (0.5, 0.5)
            offset (5,50)#(30,50)
            rotate 0

image Jubes_TJ_Body:
            #bra underlayer for non-TJ poses
#            contains:
#                ConditionSwitch(
#                        "JubesX.Over or renpy.showing('Jubes_TJ_Animation')", Null(),
#                        "JubesX.Chest == 'black bra' or JubesX.Chest == 'lace bra'","images/JubesBJFace/Jubes_TJ_Chest_Bra_Back.png",
#                        "True", Null(),
#                        )
            contains:
                "images/JubesBJFace/[JubesX.skin_image.skin_path]Jubes_TJ_Body.png"
#            contains:
#                ConditionSwitch(
#                        "not JubesX.Water",Null(),
#                        "True",       "images/JubesBJFace/Jubes_TJ_Body_Wet.png",
#                        )
            contains:
                #jacket
                ConditionSwitch(
                        "not JubesX.Acc", Null(),
                        # Modification mode
                        "JubesX.Acc == 'saiyan tail'", Null(),
                        # -----------------
                        "True", Recolor("Jubes", "Acc", "images/JubesBJFace/Jubes_TJ_Jacket.png"),
                        )
#            contains:
#                #Chest
#                ConditionSwitch(
#                        #"JubesX.Chest == 'bra'","images/JubesBJFace/Jubes_TJ_Chest_Bra_Base.png",
#                        "JubesX.Chest == 'cos bra'","images/JubesBJFace/Jubes_TJ_Chest_Cos_TopD.png",
#                        "JubesX.Chest == 'sports bra'","images/JubesBJFace/Jubes_TJ_Chest_Sportsbra_Body.png",
#                        "JubesX.Chest == 'bikini top'","images/JubesBJFace/Jubes_TJ_Chest_Bikini_Body.png",
#                        "True", Null(),
#                        )
            contains:
                #Over
                ConditionSwitch(
                        "JubesX.Over == 'red shirt'",Recolor("Jubes", "Over", "images/JubesBJFace/Jubes_TJ_Over_Red.png"),
                        "JubesX.Over == 'black shirt'",Recolor("Jubes", "Over", "images/JubesBJFace/Jubes_TJ_Over_Black.png"),
                        "JubesX.Over == 'tube top'",Recolor("Jubes", "Over", "images/JubesBJFace/Jubes_TJ_Over_Tube_Under.png"),
                        "True", Null(),
                        )
#            contains:
#                #tit spunk on chest
#                ConditionSwitch(
#                        "'tits' not in JubesX.Spunk",Null(),
#                        "True",       "images/JubesBJFace/Jubes_TJ_Spunk_Body.png",
#                        )

#            contains:
#                #hair at the midground, behind the face but in front of body
#                ConditionSwitch(
#                        "JubesX.Over", Null(),
#                        "JubesX.Hair == 'long' and not JubesX.Water", "images/JubesBJFace/Jubes_TJ_Hair_Long_Mid.png",
#                        "True",   Null(),
#                        )
            contains:
                #Over
                ConditionSwitch(
                        "'tits' in JubesX.Spunk and Player.Male","images/JubesBJFace/Jubes_TJ_Spunk_Tits_Under.png",
                        "True", Null(),
                        )
            transform_anchor True
            zoom 1
            anchor (0.4, 1.0)
            #offset (410,770) # (300,275)
            rotate 0


image Jubes_TJ_Tit_Under:
            #body underlay
            contains:
                "images/JubesBJFace/Jubes_TJ_TitsUnder.png",
#                ConditionSwitch(
#                    # right breast overlay
#                    "JubesX.Chest == 'cos bra'",Null(),
#                    "renpy.showing('Jubes_TJ_Animation')", "images/JubesBJFace/Jubes_TJ_TitsUnder.png",
#                    "True",  Null(),
#                    )
#            contains:
#                ConditionSwitch(
#                        "'tits' not in JubesX.Spunk",Null(),
#                        "True",       "images/JubesBJFace/Jubes_TJ_Spunk_TitsUnder.png",
#                        )
            transform_anchor True
            zoom 1
            anchor (0.4, 1.0)
            #offset (410,770) # (300,275)
            rotate 0

image Jubes_TJ_Jacketback:
            #back fo the bra straps
            contains:
                ConditionSwitch(
                        "not JubesX.Acc", Null(),
                        # Modification mode
                        "JubesX.Acc == 'saiyan tail'", Null(),
                        # -----------------
                        "True", Recolor("Jubes", "Acc", "images/JubesBJFace/Jubes_TJ_JacketBack.png"),
                        )
            transform_anchor True
            zoom 1
            anchor (0.4, 1.0)
            #offset (410,770) # (300,275)
            rotate 0

image Jubes_TJ_Braback:
            #back fo the bra straps
            contains:
                ConditionSwitch(
                        #"JubesX.Chest == 'corset' and not JubesX.Uptop","images/JubesBJFace/Jubes_TJ_Chest_Corset.png",
#                        "JubesX.Over",Null(),
                        "JubesX.Chest == 'sports bra'",Recolor("Jubes", "Chest", "images/JubesBJFace/Jubes_TJ_Chest_Sports_Back.png"),
#                        "JubesX.Chest == 'lace bra'","images/JubesBJFace/Jubes_TJ_Chest_Lace_Back.png",
                        "JubesX.Chest == 'bikini top' and JubesX.Uptop",Recolor("Jubes", "Chest", "images/JubesBJFace/Jubes_TJ_Chest_Bikini_Up_Back.png"),
                        "JubesX.Chest == 'bikini top'",Recolor("Jubes", "Chest", "images/JubesBJFace/Jubes_TJ_Chest_Bikini_Back.png"),
                        "True", Null(),
                        )
            transform_anchor True
            zoom 1
            anchor (0.4, 1.0)
            #offset (410,770) # (300,275)
            rotate 0

#image Jubes_TJ_BraStretch:
#            #bra streching effect
#            contains:
#                ConditionSwitch(
#                        #"JubesX.Chest == 'corset' and not JubesX.Uptop","images/JubesBJFace/Jubes_TJ_Chest_Corset.png",
#                        "JubesX.Chest == 'bikini top'","images/JubesBJFace/Jubes_TJ_Chest_Bikini_Tent.png",
#                        "JubesX.Chest == 'sports bra'","images/JubesBJFace/Jubes_TJ_Chest_Sportsbra_Tent.png",
#                        "True", Null(),
#                        )
#            transform_anchor True
#            zoom 1
#            offset (50,0) # (300,275)
#            anchor (.1,.1)#(0.1, .2)
#            rotate 0
#            #alpha 0.9

image Jubes_TJ_Tits:
            #layer with left tit and all clothing
            contains:
                "images/JubesBJFace/[JubesX.skin_image.skin_path]Jubes_TJ_Tits.png"
#            contains:
#                ConditionSwitch(
#                        "not JubesX.Water",Null(),
#                        "True",       "images/JubesBJFace/Jubes_TJ_Tits_Wet.png",
#                        )
            contains:
                #Chest
                ConditionSwitch(
                        "JubesX.Chest == 'lace bra' and JubesX.Uptop",Recolor("Jubes", "Chest", "images/JubesBJFace/Jubes_TJ_Chest_Lace_Up.png"),  #fix, add "no straps" version here
                        "JubesX.Chest == 'lace bra'",Recolor("Jubes", "Chest", "images/JubesBJFace/Jubes_TJ_Chest_Lace.png"),
                        "JubesX.Chest == 'sports bra'",Recolor("Jubes", "Chest", "images/JubesBJFace/Jubes_TJ_Chest_Sports.png"),
                        "JubesX.Chest == 'bikini top' and JubesX.Uptop",Recolor("Jubes", "Chest", "images/JubesBJFace/Jubes_TJ_Chest_Bikini_Up.png"),
                        "JubesX.Chest == 'bikini top'",Recolor("Jubes", "Chest", "images/JubesBJFace/Jubes_TJ_Chest_Bikini.png"),
                        # Modification mode
                        "JubesX.Chest == 'saiyan leotard'","images/JubesBJFace/modification/Jubes_TJ_Chest_Saiyan_Leotard.png",
                        # -----------------
                        "True", Null(),
                        )
            contains:
                #Over
                ConditionSwitch(
                        "JubesX.Over == 'tube top' and JubesX.Uptop",Recolor("Jubes", "Over", "images/JubesBJFace/Jubes_TJ_Over_Tube_Up.png"),
                        "JubesX.Over == 'tube top'",Recolor("Jubes", "Over", "images/JubesBJFace/Jubes_TJ_Over_Tube.png"),
                        "True", Null(),
                        )
            contains:
                #Piercings clothing
                ConditionSwitch(
                        "not JubesX.Pierce", Null(),
                        "JubesX.Pierce == 'ring'", ConditionSwitch(
                                #if she's got ring piercings
                                "JubesX.Uptop", "images/JubesBJFace/Jubes_TJ_Pierce_Ring.png",
                                "JubesX.Over == 'tube top'", "images/JubesBJFace/Jubes_TJ_Pierce_Ring_Pink.png",
                                "JubesX.Chest == 'bikini top'", "images/JubesBJFace/Jubes_TJ_Pierce_Ring_Pink.png",
                                "JubesX.Chest == 'lace bra'", "images/JubesBJFace/Jubes_TJ_Pierce_Ring_Lace.png",
                                "True", "images/JubesBJFace/Jubes_TJ_Pierce_Ring.png",
                                ),
                        "JubesX.Uptop", "images/JubesBJFace/Jubes_TJ_Pierce_Barbell.png",
                        "JubesX.Over == 'tube top'", "images/JubesBJFace/Jubes_TJ_Pierce_Barbell_Pink.png",
                        "JubesX.Chest == 'bikini top'", "images/JubesBJFace/Jubes_TJ_Pierce_Barbell_Pink.png",
                        "JubesX.Chest == 'lace bra'", "images/JubesBJFace/Jubes_TJ_Pierce_Barbell_Lace.png",
                        "True", "images/JubesBJFace/Jubes_TJ_Pierce_Barbell.png",
                        )
            contains:
                #Over
                ConditionSwitch(
                        "'tits' in JubesX.Spunk and Player.Male","images/JubesBJFace/Jubes_TJ_Spunk_Tits_Over.png",
                        "True", Null(),
                        )
            transform_anchor True
            zoom 1
            anchor (0.4, 1.0)
            #offset (410,770) # (300,275)
            rotate 0


# Animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start 0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jubes_TJ_0:
        #Her Body in the TJ pose, static

        contains:
                #jacket
                "Jubes_TJ_Jacketback"
                subpixel True
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat
        contains:
                #bra strap backing
                "Jubes_TJ_Braback"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat
        contains:
                #base body test / / / / / / / / / / / / / / / / / / / /
                "Jubes_TJ_Body"
                subpixel True
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat
        contains:
                #head
                "Jubes_TJ_Head"
                subpixel True
                pos (0,0) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat
                parallel:
                    pause .1
                    ease 2 rotate -5
                    pause .1
                    ease 2 rotate 0
                    repeat
        contains:
                #right hand backside
                "Jubes_TJ_Tit_Under"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos -0
                    pause .1
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Jubes_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
#                rotate -5
#                parallel:
#                    ease 2 rotate -3#3
#                    pause .1
#                    ease 2 rotate -5#-2
#                    pause .1
#                    repeat
#        contains:
#                contains:
#                    "Jubes_TJ_BraStretch"
#                subpixel True
#                pos (-70,-210) #top (0,-10)
#                transform_anchor True
#                xzoom .75
#                yzoom .85
#                parallel:
#                    ease 2 yzoom .5
#                    pause .1
#                    ease 2 yzoom .85
#                    pause .1
#                    repeat
#                parallel:
#                    ease 2 pos (-60,-230)#-30,-160
#                    pause .1
#                    ease 2 pos (-70,-210)#-70,-140
#                    pause .1
#                    repeat
        contains:
                contains:
                    "Jubes_TJ_Tits"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat

# End Jubes TJ Pose 0 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start 1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jubes_TJ_1:
        #Her Body in the TJ pose, slow
        contains:
                #jacket
                "Jubes_TJ_Jacketback"
                subpixel True
                pos (0,60) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -50#-40
                    pause .2
                    ease 2 ypos 60#60
                    pause .5
                    repeat
        contains:
                #bra strap backing
                "Jubes_TJ_Braback"
                subpixel True
#                pos (0,140) #top (0,-10)
#                transform_anchor True
#                block:
#                    pause .1
#                    ease 1.9 ypos -20
#                    pause .4
#                    ease 1.8 ypos 150
#                    ease .5 ypos 140
#                    repeat

                pos (0,50) #top (0,-10)
                transform_anchor True
                block:
                    pause .1
                    ease 1.9 ypos -60#-20
                    pause .4
                    ease 1.8 ypos 60#150
                    ease .5 ypos 50#140
                    repeat
        contains:
                #base body test / / / / / / / / / / / / / / / / / / / /
                "Jubes_TJ_Body"
                subpixel True
                pos (0,60) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -50#-40
                    pause .2
                    ease 2 ypos 60#60
                    pause .5
                    repeat
        contains:
                #head
                "Jubes_TJ_Head"
                subpixel True
                pos (0,60) #top (0,-10)
                transform_anchor True
                rotate -5
                parallel:
                    ease 2 ypos -40
                    pause .2
                    ease 2 ypos 60
                    pause .5
                    repeat
                parallel:
                    ease 2.3 rotate 0
                    pause .2
                    ease 2.2 rotate -5
                    pause .5
                    repeat
#                    ease 2 rotate 0
#                    pause .2
#                    ease 2 rotate -5
#                    pause .5
#                    repeat
        contains:
                #right hand backside
                "Jubes_TJ_Tit_Under"
                subpixel True
                pos (0,60) #top (0,-10)
                transform_anchor True
                block:
                    pause .1
                    ease 1.9 ypos -60
                    pause .4
                    ease 1.8 ypos 60
                    ease .5 ypos 50
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Jubes_TJ_ZeroCock"
                pos (0,25) #top (0,-10)
                transform_anchor True
                rotate 0#-6
                parallel:
                    ease 2 ypos 0
                    pause .4
                    ease 1.8 ypos 25
                    pause .5
                    repeat
#                parallel:
#                    ease 2 rotate 0
#                    pause .2
#                    ease 2 rotate -5
#                    pause .5
#                    repeat
#        contains:
#                contains:
#                    "Jubes_TJ_BraStretch"
#                subpixel True
#                pos (-100,-150) #top (0,-10)
#                transform_anchor True
#                xzoom .9
#                yzoom 1.3
#                parallel:
#                    pause .1
#                    ease 1.6 yzoom .3#-20
#                    pause .9
#                    ease 1.6 yzoom 1.5#150
#                    ease .5 yzoom 1.3#140
#                    repeat
#                parallel:
#                    pause .1
#                    ease 1.9 xzoom .6#-20
#                    pause .4
#                    ease 1.8 xzoom .9#150
#                    pause .5
##                    ease .5 xzoom .8#140
#                    repeat
#                parallel:
#                    pause .1
#                    ease 1.9 pos (-50,-260)#-160 bottom
#                    pause .4
#                    ease 1.8 pos (-100,-140)#-90,-65
#                    ease .5 pos (-100,-150)#-80,-80
#                    repeat
        contains:
                contains:
                    "Jubes_TJ_Tits"
                subpixel True
                pos (0,50) #top (0,-10)
                transform_anchor True
                block:
                    pause .1
                    ease 1.9 ypos -60#-20
                    pause .4
                    ease 1.8 ypos 60#150
                    ease .5 ypos 50#140
                    repeat

# End Jubes TJ Pose 1 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Start 2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jubes_TJ_2:
        #Her Body in the TJ pose, fast
        contains:
                #jacket
                "Jubes_TJ_Jacketback"
                subpixel True
                pos (0,80) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 1 ypos -05#-35
                    pause .2 #1
                    ease .4 ypos 80#80
                    repeat
        contains:
                #bra strap backing
                "Jubes_TJ_Braback"
                subpixel True
                pos (0,80) #top (0,-10)
                transform_anchor True
                block:
                    ease .3 ypos 60#40
                    ease .7 ypos -20#-40
                    pause .2
                    ease .4 ypos 80#80
                    repeat
        contains:
                #base body test / / / / / / / / / / / / / / / / / / / /
                "Jubes_TJ_Body"
                subpixel True
                pos (0,80) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 1 ypos -05#-35
                    pause .2 #1
                    ease .4 ypos 80#80
                    repeat
        contains:
                #head
                "Jubes_TJ_Head"
                subpixel True
                pos (0,80) #top (0,-10)
                transform_anchor True
                rotate -5
                parallel:
                    ease 1 ypos -20
                    pause .1
                    ease .5 ypos 80
                    repeat
                parallel:
                    ease 1 rotate 0
                    pause .1
                    ease .5 rotate -5
                    repeat
        contains:
                #right hand backside
                "Jubes_TJ_Tit_Under"
                subpixel True
                pos (0,80) #top (0,-10)
                transform_anchor True
                block:
                    ease .3 ypos 60#40
                    ease .7 ypos -20#-40
                    pause .2
                    ease .4 ypos 80#80
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Jubes_TJ_ZeroCock"
                pos (0,30) #top (0,-10)
                transform_anchor True
                rotate 0#-4
                parallel:
                    ease 1 ypos 0
                    pause .2
                    ease .4 ypos 30
                    repeat
#                parallel:
#                    ease 1 rotate -2
#                    pause .1
#                    ease .5 rotate -4
#                    repeat
#        contains:
#                contains:
#                    "Jubes_TJ_BraStretch"
#                subpixel True
#                pos (-100,-120) #top (0,-10)
#                transform_anchor True
#                yzoom 1.7
#                xzoom 1
#                parallel:
#                    ease .3 yzoom 1.3#-60 bottom
#                    ease .7 yzoom .3#-60 bottom
#                    pause .2
#                    ease .4 yzoom 1.7#60
#                    repeat
#                parallel:
#                    ease .3 pos (-100,-160)#-80 bottom
#                    ease .7 pos (-80,-240)#-160 bottom
#                    pause .2
#                    ease .4 pos (-100,-120)#-40
#                    repeat
        contains:
                contains:
                    "Jubes_TJ_Tits"
                subpixel True
                pos (0,80) #top (0,-10)
                transform_anchor True
                block:
                    ease .3 ypos 60#40
                    ease .7 ypos -20#-40
                    pause .2
                    ease .4 ypos 80#80
                    repeat


# End Jubes TJ Pose 2 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start 3 (licking) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jubes_TJ_3:
        #Her Body in the TJ pose, licking
        contains:
                #jacket
                "Jubes_TJ_Jacketback"
                subpixel True
                pos (0,130) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 1 ypos 60#100
                    pause .15
                    ease .45 ypos 110#130
                    repeat
        contains:
                #bra strap backing
                "Jubes_TJ_Braback"
                subpixel True
                pos (0,110) #top (0,-10)
                transform_anchor True
                block:
                    ease .3 ypos 100
                    ease .7 ypos 60
                    pause .2
                    ease .4 ypos 110
                    repeat
        contains:
                #base body test / / / / / / / / / / / / / / / / / / / /
                "Jubes_TJ_Body"
                subpixel True
                pos (0,130) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 1 ypos 60#100
                    pause .15
                    ease .45 ypos 110#130
                    repeat
        contains:
                #head
                "Jubes_TJ_Head"
                subpixel True
                pos (0,140) #top (0,-10)
                transform_anchor True
                rotate -5
                parallel:
                    ease 1 ypos 70
                    pause .1
                    ease .5 ypos 140
                    repeat
                parallel:
                    ease 1 rotate 0
                    pause .1
                    ease .5 rotate -5
                    repeat
        contains:
                #right hand backside
                "Jubes_TJ_Tit_Under"
                subpixel True
                pos (0,110) #top (0,-10)
                transform_anchor True
                block:
                    ease .3 ypos 100
                    ease .7 ypos 60
                    pause .2
                    ease .4 ypos 110
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Jubes_TJ_ZeroCock"
                pos (0,30) #top (0,-10)
                transform_anchor True
                rotate 0#-4
                parallel:
                    ease 1 ypos 0
                    pause .2
                    ease .4 ypos 30
                    repeat
#        contains:
#                contains:
#                    "Jubes_TJ_BraStretch"
#                subpixel True
#                pos (-100,-105) #top (0,-10)
#                transform_anchor True
#                yzoom 2
#                xzoom 1
#                parallel:
#                    ease .3 yzoom 1.95#1.3 bottom
#                    ease .7 yzoom 1.7#.3 bottom
#                    pause .2
#                    ease .4 yzoom 2#1.7
#                    repeat
#                parallel:
#                    ease .3 pos (-100,-115)#-160 bottom
#                    ease .7 pos (-90,-155)#-240 bottom
#                    pause .2
#                    ease .4 pos (-100,-105)#-120
#                    repeat

        contains:
                contains:
                    "Jubes_TJ_Tits"
                subpixel True
                pos (0,110) #top (0,-10)
                transform_anchor True
                block:
                    ease .3 ypos 100
                    ease .7 ypos 60
                    pause .2
                    ease .4 ypos 110
                    repeat


# End Jubes TJ Pose 3 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start 4 (cumming high) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jubes_TJ_4:
        #Her Body in the TJ pose, cummming high
        contains:
                #jacket
                "Jubes_TJ_Jacketback"
                subpixel True
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat
        contains:
                #bra strap backing
                "Jubes_TJ_Braback"
                subpixel True
                pos (0,5) #top (0,-10)
                transform_anchor True
                parallel:
                    pause .2
                    ease 1.9 ypos -30
                    pause .2
                    ease 1.9 ypos 5
                    repeat
        contains:
                #base body test / / / / / / / / / / / / / / / / / / / /
                "Jubes_TJ_Body"
                subpixel True
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat
        contains:
                #head
                "Jubes_TJ_Head"
                subpixel True
                pos (20,0) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat
                parallel:
                    pause .1
                    ease 2 rotate 20#-5
                    pause .1
                    ease 2 rotate 15#0
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Jubes_TJ_ZeroCock"
                pos (0,20) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos 0
                    pause .1
                    ease 2 ypos 20
                    pause .1
                    repeat
        contains:
                contains:
                    "Jubes_TJ_Tits"
                subpixel True
                pos (0,5) #top (0,-10)
                transform_anchor True
                parallel:
                    pause .2
                    ease 1.9 ypos -30
                    pause .2
                    ease 1.9 ypos 5
                    repeat

# End Jubes TJ Pose 4 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start 5 (cumming low) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jubes_TJ_5:
        #Her Body in the TJ pose, cumming low
        contains:
                #jacket
                "Jubes_TJ_Jacketback"
                subpixel True
                pos (0,140) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos 130
                    pause .2
                    ease 2 ypos 140
                    pause .5
                    repeat
        contains:
                #bra strap backing
                "Jubes_TJ_Braback"
                subpixel True
                pos (0,90) #top (0,-10)
                transform_anchor True
                parallel:
                    pause .1
                    ease 2 ypos 100
                    pause .2
                    ease 2 ypos 110
                    pause .4
                    repeat
        contains:
                #hairbelow the body
                "Jubes_TJ_HairBack"
                subpixel True
                pos (0,130)
                transform_anchor True
                rotate -5
                parallel:
                    ease 2 ypos 125
                    pause .2
                    ease 2 ypos 130
                    pause .5
                    repeat
                parallel:
                    ease 2 rotate -5
                    pause .5
                    repeat
        contains:
                #base body test / / / / / / / / / / / / / / / / / / / /
                "Jubes_TJ_Body"
                subpixel True
                pos (0,140) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos 130
                    pause .2
                    ease 2 ypos 140
                    pause .5
                    repeat
        contains:
                #head
                "Jubes_TJ_Head"
                subpixel True
                pos (0,130)
                transform_anchor True
                rotate -5
                parallel:
                    ease 2 ypos 125
                    pause .2
                    ease 2 ypos 130
                    pause .5
                    repeat
                parallel:
                    ease 2 rotate -5
                    pause .5
                    repeat
        contains:
                #right hand backside
                "Jubes_TJ_Tit_Under"
                subpixel True
                pos (0,90) #top (0,-10)
                transform_anchor True
                parallel:
                    pause .1
                    ease 2 ypos 100
                    pause .2
                    ease 2 ypos 110
                    pause .4
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Jubes_TJ_ZeroCock"
                pos (0,25) #top (0,-10)
                transform_anchor True
                rotate 0#-10
        contains:
                contains:
                    "Jubes_TJ_Tits"
                subpixel True
                pos (0,90) #top (0,-10)
                transform_anchor True
                parallel:
                    pause .1
                    ease 2 ypos 100
                    pause .2
                    ease 2 ypos 110
                    pause .4
                    repeat

# End Jubes TJ Pose 5 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Jubes's TJ animations end / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jubes_TJ_Launch(Line = Trigger):    # The sequence to launch the Jubes Titfuck animations
    if renpy.showing("Jubes_TJ_Animation"):
        return

#    if Line == "L": # Jubes gets started. . .
#            if Taboo:
#                if len(Present) >= 2:
#                    if Present[0] != JubesX:
#                            "[JubesX.Name] looks back at [Present[0].Name] to see if she's watching."
#                    elif Present[1] != JubesX:
#                            "[JubesX.Name] looks back at [Present[1].Name] to see if she's watching."
#                else:
#                            "[JubesX.Name] casually glances around to see if anyone can see her."
#            "[JubesX.Name] bends over and places your cock between her breasts."

#    if JubesX.Chest and JubesX.Over:
#        "She throws off her [JubesX.Over] and her [JubesX.Chest]."
#    elif JubesX.Over:
#        "She throws off her [JubesX.Over], baring her breasts underneath."
#    elif JubesX.Chest:
#        "She tugs off her [JubesX.Chest] and throws it aside."
#    $ JubesX.Over = 0
#    $ JubesX.Chest = 0
#    $ JubesX.ArmPose = 0

#    call Girl_First_Topless(JubesX)

    show blackscreen onlayer black with dissolve

    if renpy.showing("Jubes_BJ_Animation"):
            hide Jubes_BJ_Animation
    else:
            call Girl_Hide(JubesX)
            show Jubes_Sprite at SpriteLoc(JubesX.SpriteLoc) zorder 150:
                alpha 1
                ease 1 zoom 2.3 xpos 750 yoffset -100
            show Jubes_Sprite zorder JubesX.Layer:
                alpha 0

#    if JubesX.Over == "towel" or JubesX.Chest == "corset": #pulls top down because these tops are incompatible with TJ.
#        $ JubesX.Uptop = 1

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "titjob"
    show Jubes_TJ_Animation zorder 150:
        pos (1000,1050)#(1000,1000)#(700,520)
    $ Player.Sprite = 1
    hide blackscreen onlayer black with dissolve
    return

label Jubes_TJ_Reset:
    # The sequence to the Jubes animations from Titfuck to default
    if not renpy.showing("Jubes_TJ_Animation"):
        return
#    hide Jubes_TJ_Animation
    call Girl_Hide(JubesX)
    $ Player.Sprite = 0

    show Jubes_Sprite at SpriteLoc(JubesX.SpriteLoc) zorder 150:
        zoom 2.3 xpos 750 yoffset -100
    show Jubes_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 xpos 700 yoffset 50
        pause .5
        ease .5 zoom 1 xpos JubesX.SpriteLoc yoffset 0
    "[JubesX.Name] отстраняется"
    show Jubes_Sprite at SpriteLoc(JubesX.SpriteLoc) zorder JubesX.Layer:
        alpha 1 zoom 1 offset (0,0) xpos JubesX.SpriteLoc
    return

# End Jubes TJ Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Jubes Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Jubes Handjob element //////////////////////////////////////////////////////////////////////

image Jubes_HJ_Body:
    "Jubes_Sprite"
    pos (680,-1250)#(350,-550)
    zoom 4.8#2.15


transform Jubes_HJ_Body_1():
    subpixel True
#    pos (700,-1250)#(350,-550)
    block:
        ease .5 ypos -1220
        pause 0.25
        ease 1.0 ypos -1250
        pause 0.1
        repeat

transform Jubes_HJ_Body_2():
    subpixel True
#    pos (350,-550)
    block:
        ease 0.2 ypos -1240
        pause 0.1
        ease 0.4 ypos -1250
        pause 0.1
        repeat

image Jubes_Hand_Under:
    "images/JubesSprite/[JubesX.skin_image.skin_path]handjubes2.png"
    anchor (0.5,0.5)
    pos (-10,0)


image Jubes_Hand_Over:
    "images/JubesSprite/[JubesX.skin_image.skin_path]handjubes1.png"
    anchor (0.5,0.5)
    pos (-10,0)

transform Jubes_Hand_1():
    subpixel True
    pos (-20,-100)
    rotate 5
    block:
        ease .5 pos (-20,150) rotate -5 #ypos 150 rotate 5 Bottom
        pause 0.25
        ease 1.0 pos (-20,-100) rotate 5 #(-20,-100) #rotate -10#  Top
        pause 0.1
        repeat

transform Jubes_Hand_2():
    subpixel True
    pos (-15,-120)
    rotate 10
    block:
        ease 0.2 pos (-15,0) rotate 0   #(-15,0)
        pause 0.1
        ease 0.4 pos (-15,-120) rotate 5 #-15,-120)
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

image Jubes_HJ_Animation:
    contains:
        ConditionSwitch(
            # backside of the hand
            "not Speed", Transform("Jubes_HJ_Body"),
            "Speed == 1", At("Jubes_HJ_Body", Jubes_HJ_Body_1()),
            "Speed >= 2", At("Jubes_HJ_Body", Jubes_HJ_Body_2()),
            "Speed", Null(),
            ),
    contains:
        ConditionSwitch(
            # backside of the hand
            "not Speed", Transform("Jubes_Hand_Under"),
            "Speed == 1", At("Jubes_Hand_Under", Jubes_Hand_1()),
            "Speed >= 2", At("Jubes_Hand_Under", Jubes_Hand_2()),
            "Speed", Null(),
            ),
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
            "not Speed", Transform("Jubes_Hand_Over"),
            "Speed == 1", At("Jubes_Hand_Over", Jubes_Hand_1()),
            "Speed >= 2", At("Jubes_Hand_Over", Jubes_Hand_2()),
            "Speed", Null(),
            ),
    anchor (0.51, -1.3)
#    xzoom -0.4#0.6
    zoom 0.4#0.6


label Jubes_HJ_Launch(Line = Trigger):
    if renpy.showing("Jubes_HJ_Animation"):
        $ Trigger = "hand"
        return
    if not Player.Male:
        call Jubes_Finger_Launch
        return
    call Girl_Hide(JubesX)
    $ JubesX.ArmPose = 2
    if Line == "L":
        show Jubes_Sprite at SpriteLoc(StageRight) zorder 150:
            alpha 1
            ease 1 zoom 1.7 offset (-150,200)#(0,200)
    else:
        show Jubes_Sprite at SpriteLoc(StageRight) zorder 150:
            alpha 1
            ease 1 zoom 1.9 offset (-150,150)#(150,150)
        with dissolve

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    else:
        $ Speed = 1
    pause .5
    show Jubes_Sprite:
        alpha 0
    show Jubes_HJ_Animation at SpriteLoc(StageCenter) zorder 150 with fade:
        #xoffset 150
        offset (150,250)#(250,250)
    return

label Jubes_HJ_Reset: # The sequence to the Jubes animations from handjob to default
    if not renpy.showing("Jubes_HJ_Animation"):
        return
    $ Speed = 0
    $ JubesX.ArmPose = 1
    hide Jubes_HJ_Animation with dissolve
    call Girl_Hide(JubesX)
    show Jubes_Sprite at SpriteLoc(JubesX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Jubes_Sprite at SpriteLoc(JubesX.SpriteLoc) zorder JubesX.Layer:
        alpha 1 zoom 1 offset (0,0)
    return

# End Jubes Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# Core Jubes CUN element ///////////////////////////////////////////////////////////////////////////                                     Core Jubes CUN element
#Jubes CUN Over Sprite Compositing

image Jubes_CUN_Animation: #core CUN animation
    LiveComposite(
        (787,913),
        (0,0), ConditionSwitch(                                                                 # back of the hair, which needs to go behind the body
            "Speed == 0",  "Jubes_CUN_Anim_Static",
            "Speed == 1",  "Jubes_CUN_Anim_Licking1",
            "Speed == 2",  "Jubes_CUN_Anim_Licking2",
            "Speed >= 3",  "Jubes_CUN_Anim_Licking3",
#            "Speed == 4",  "Jubes_CUN_Anim_Licking1",
            "True", "Jubes_CUN_Anim_Static",
            ),
        )
    zoom .55
    anchor (.5,.5)

image Jubes_CUN_Anim_Static:
    #Animation for licking speed 1
#    contains:
#        #hair
#        "Jubes_BJ_HairBack"#"BJ_HairBack"
#        subpixel True
#        offset (40,0)#(-10,0)
#        block:
#            ease 2 yoffset 10
#            ease 2 yoffset 0
#            repeat
    contains:
        #body 2
        "Jubes_BJ_Backdrop"
        pos (-350,-290)#(-440,-290)
        subpixel True
        offset (70,20)  #top(0,-35)
        block:
            ease 2 yoffset 30
            ease 2 yoffset 20
            repeat
    contains:
        #head
        "Jubes_BJ_Head"#"BJ_Head"
        subpixel True
        offset (70,0)#(-10,0)
        rotate 20
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


image Jubes_CUN_Anim_Licking1:
    #Animation for licking speed 1
#    contains:
#        #hair
#        "Jubes_BJ_HairBack"#"BJ_HairBack"
#        offset (30,20)#490)
#        rotate 10
#        block: #5s total
#            ease 2.5 offset (40,100) #bottom (0,75)
#            easeout 1.5 offset (40,60)  #top (0,60)
#            ease .5 offset (35,20)  #top
#            ease .5 offset (37,30)  #top
#            repeat
    contains:
        #body 2
        "Jubes_BJ_Backdrop"#"Jubes_Sprite"
#        zoom 1 #4.5
        pos (-350,-290)#(-440,-290)
        subpixel True
        offset (0,0)# -70,0
        block:
            ease 2.5 offset (0,75) #bottom (30,90)
            ease 2.3 offset (0,0)  #top
            pause .2
            repeat
    contains:
        #head
        "Jubes_BJ_Head"#"BJ_Head"
        subpixel True
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
#End Jubes Licking 1

image Jubes_CUN_Anim_Licking2:
    #Animation for licking speed 2
#    contains:
#        #hair
#        "Jubes_BJ_HairBack"#"BJ_HairBack"
#        subpixel True
#        offset (0,30)#490)
#        rotate 0
#        parallel: #2s total
#            ease 1 offset (0,100) #bottom
#            easeout .65 offset (10,70)  #top -35)
#            linear .35 offset (40,30)  #top -35)
#            pause .10
#            repeat
#        parallel: #2s total
#            ease 1 rotate -5 #bottom
#            easeout .65 rotate 0  #top -35)
#            linear .35 rotate 10  #top -35)
#            pause .10
#            repeat
    contains:
        #body 2
        "Jubes_BJ_Backdrop"
        pos (-350,-290)#(-440,-290)
        subpixel True
        offset (10,50)#490)
        block:
            ease .75 offset (10,70) #bottom (30,90)
            ease .95 offset (10,50)  #top
            pause .40
            repeat
    contains:
        #head
        "Jubes_BJ_Head"#"BJ_Head"
        subpixel True
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
#End Jubes Licking 2

image Jubes_CUN_Anim_Licking3:
    #Animation for licking speed 3
#    contains:
#        #hair
#        "Jubes_BJ_HairBack"#"BJ_HairBack"
#        subpixel True
#        offset (20,90)#490)
#        block: #2s total
#            ease .5 offset (20,110) #bottom
#            ease .5 offset (20,90)  #top -35)
#            repeat
    contains:
        #body 2
        "Jubes_BJ_Backdrop"
        pos (-350,-290)#(-440,-290)
        subpixel True
        offset (0,110)#490)
        block:
            ease .4 offset (0,100) #bottom (30,90)
            ease .4 offset (0,110)  #top
            pause .2
            repeat
    contains:
        #head
        "Jubes_BJ_Head"#"BJ_Head"
        subpixel True
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
#End Jubes Licking 3

#CUN Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Jubes_CUN_Launch(Line = Trigger):
    # The sequence to launch the Jubes CUN animations
    if renpy.showing("Jubes_CUN_Animation"):
        return

    if Player.Male == 1:
        call Jubes_BJ_Launch
        return


    call Girl_Hide(JubesX)
    if Line == "L" or Line == "cum":
        show Jubes_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1
            ease 1 zoom 2.5 offset (70,240) #(-90,140) offset (150,80)
        with dissolve
    else:
        show Jubes_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1 zoom 2.5 offset (70,240) #(-90,140)
        with dissolve

    if Taboo and Line == "L":
            # Jubes gets started. . .
            if len(Present) >= 2:
                if Present[0] != JubesX:
                        "[JubesX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                elif Present[1] != JubesX:
                        "[JubesX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
            else:
                        "[JubesX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
    $ Speed = 1
    if Line == "L":
            if not JubesX.Blow:
                "[JubesX.Name] нерешительно стягивает с вас штаны и касается своим ртом вашей киски."
            else:
                "[JubesX.Name] наклоняется и начинает лизать вашу киску."

    if Line != "cum":
        $ Trigger = "cun"

    show Jubes_Sprite:
        alpha 0
    show Jubes_CUN_Animation zorder 150:
        pos (800,830)#(645,610)
    return

label Jubes_CUN_Reset: # The sequence to the Jubes animations from CUN to default
    if not renpy.showing("Jubes_CUN_Animation"):
        return
    hide Jubes_CUN_Animation
    call Girl_Hide(JubesX)
    $ Speed = 0

    show Jubes_Sprite at SpriteLoc(JubesX.SpriteLoc) zorder 150:
        zoom 2 offset (70,140) alpha 1
        pause .5
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Jubes_Sprite at SpriteLoc(JubesX.SpriteLoc) zorder JubesX.Layer:
        alpha 1 zoom 1 offset (0,0)
    $ JubesX.FaceChange("sexy")
    return

#End Jubilee Cunnilingus Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

image Jubes_Finger_Animation:
    # Core Animation for Fingering Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
        ConditionSwitch(                                                # backside of the hand
            "Speed == 1", "Jubes_Finger_1",
            "Speed >= 2", "Jubes_Finger_2",
            "True", "Jubes_Finger_0",
            ),
    anchor (0.5,0.5)#anchor (0.51, -1.3)
    offset (400,945)#700,1190
    zoom 0.8
    # end Core Animation for Fingering Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <

image Jubes_Finger_0:
    # Animation for Fingering Zero's pussy, static < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Jubes_Sprite"
            pos (350,-550)
            zoom 2.15
    contains:
            ConditionSwitch(
                "Player.Wet", "JubesBJFace/Jubes_Fingering_wet.png",
                "True", "JubesBJFace/[JubesX.skin_image.skin_path]Jubes_Fingering_Under.png",
                )
            anchor (0.5,0.6)
            pos (50,00)#(20,40)

#            "Jubes_Finger_Under"
    contains:
            "Zero_Pussy"
#    contains:
#            "JubesBJFace/Jubes_Fingering_Over.png"
#            anchor (0.5,0.6)
#            pos (20,40)
##            "Jubes_Finger_Over"
    # end Animation for Fingering Zero's pussy, static < < < < < < < < < < < < < < < < < < < < < < < <

image Jubes_Finger_1:
    # Animation for Fingering Zero's pussy, slow < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Jubes_Sprite"
            pos (350,-550)
            zoom 2.15
            block:
                ease 0.5 ypos -540 #rotate 3   100
                pause 0.25
                ease 1.0 ypos -550 #rotate -3  40
                repeat
    contains:
            ConditionSwitch(
                "Player.Wet", "JubesBJFace/Jubes_Fingering_wet.png",
                "True", "JubesBJFace/[JubesX.skin_image.skin_path]Jubes_Fingering_Under.png",
                )
            subpixel True
        #    xpos 10
            anchor (0.5,0.6)
            transform_anchor True
            pos (45,0)
            rotate -5
            block:
                ease .5 pos (40,65) rotate 0 #(-30,50)   Bottom
                pause 0.25
                ease 1.0 pos (45,0) rotate -5 #((20,-60) Top                 pause 0.1
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
#    contains:
#            "JubesBJFace/Jubes_Fingering_Over.png"
##            "Jubes_Finger_Over"
#            subpixel True
#        #    xpos 10
#            anchor (0.5,0.6)
#            transform_anchor True
#            pos (10,40)
#            rotate -5
#            block:
#                ease .5 pos (10,85) rotate -15 #(-30,50)   Bottom
#                pause 0.25
#                ease 1.0 pos (10,40) rotate -5 #((20,-60) Top                 pause 0.1
#                repeat
    # end Animation for Fingering Zero's pussy, slow < < < < < < < < < < < < < < < < < < < < < < < <

image Jubes_Finger_2:
    # Animation for Fingering Zero's pussy, fast < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Jubes_Sprite"
            pos (350,-550)
            zoom 2.15
            block:
                ease 0.15 ypos -540 #rotate 3   100
                pause 0.1
                ease 0.45 ypos -550 #rotate -3  40
                pause 0.1
                repeat
    contains:
            ConditionSwitch(
                "Player.Wet", "JubesBJFace/Jubes_Fingering_wet.png",
                "True", "JubesBJFace/[JubesX.skin_image.skin_path]Jubes_Fingering_Under.png",
                )
            subpixel True
            anchor (0.5,0.6)
            transform_anchor True
#            rotate -15
            pos (40,30)
            block:
                ease 0.15 ypos 65 #rotate 3   100
                pause 0.1
                ease 0.45 ypos 30 #rotate -3  40
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
#    contains:
#            "JubesBJFace/Jubes_Fingering_Over.png"
##            "Jubes_Finger_Over"
#            anchor (0.5,0.6)
#            subpixel True
#            transform_anchor True
#            rotate -15
#            pos (10,40)
#            block:
#                ease 0.15 ypos 85 #rotate 3
#                pause 0.1
#                ease 0.45 ypos 40 #rotate -3 -50
#                pause 0.1
#                repeat
    # end Animation for Fingering Zero's pussy, fast < < < < < < < < < < < < < < < < < < < < < < < <

label Jubes_Finger_Launch(Line = Trigger):
    if renpy.showing("Jubes_Finger_Animation"):
        $ Trigger = "finger"
        return

    if Player.Male == 1:
        call Jubes_HJ_Launch
        return

    call Girl_Hide(JubesX)
    $ JubesX.Arms = 0
    $ JubesX.ArmPose = 2
    if not renpy.showing("Jubes_Sprite"):
        show Jubes_Sprite at SpriteLoc(JubesX.SpriteLoc) zorder 150:
            alpha 1 zoom 1.7 xpos 850 yoffset 200 #offset (-50,200)
        with dissolve
    show Jubes_Sprite at SpriteLoc(JubesX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 1.7 xpos 850 yoffset 200 #offset (-50,200)

    if Taboo and Line == "L":
        # Jubes gets started. . .
        if len(Present) >= 2:
            if Present[0] != JubesX:
                    "[JubesX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
            elif Present[1] != JubesX:
                    "[JubesX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
        else:
                    "[JubesX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
        if not JubesX.Hand and JubesX.Arms:
            "Когда вы стягиваете свои штаны, [JubesX.Name] снимает перчатки и нерешительно тянется к вашей киске. Затем она начинает грубо ласкать ее."
        else:
            "Затем она наклоняется и хватает ваш член."
    elif Line == "L":
        if not JubesX.Hand and JubesX.Arms:
            "Когда вы стягиваете свои штаны, [JubesX.Name] снимает перчатки и нерешительно тянется к вашей киске. Затем она начинает грубо ласкать ее."
        else:
            "[JubesX.Name] наклоняется и кладет руку вам на киску."
    else:
            "[JubesX.Name] наклоняется и кладет руку вам на киску."

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "finger"
    show Jubes_Sprite:
        alpha 0
    show Jubes_Finger_Animation at SpriteLoc(JubesX.SpriteLoc) zorder 150 with fade
    return

label Jubes_Finger_Reset: # The sequence to the Jubes animations from handjob to default
    if not renpy.showing("Jubes_Finger_Animation"):
        return
    $ Speed = 0
    hide Jubes_Finger_Animation
    with dissolve
    call Girl_Hide(JubesX)
    show Jubes_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 yoffset 50
        pause .5
        ease .5 zoom 1 xpos JubesX.SpriteLoc yoffset 0
    show Jubes_Sprite at SpriteLoc(JubesX.SpriteLoc) zorder JubesX.Layer:
        alpha 1 zoom 1  xpos JubesX.SpriteLoc yoffset 0
    return

# Start Jubes Scissor Pose content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_SC_Sprite:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
                #if the top's down. . .
                "Speed >= 2", "Jubes_SC_Anim_2",
                "Speed", "Jubes_SC_Anim_1",
                "True", "Jubes_SC_Anim_0",
                ),
        )
    align (0.6,0.0)
    pos (650,300)#(650,200)(925,740)#(910,850)
    zoom 0.85#0.8

# End Jubes Sex Pose Speed 2 Scissor / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Jubes Sex Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Jubes_SC_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Jubes_SexSprite
        (1120,880),

#        (545,540), ConditionSwitch(    #165,560
#            #Personal Wetness
#            "not JubesX.Wet", Null(),
#            "(JubesX.Legs == 'pants' or JubesX.Legs == 'shorts') and not JubesX.Upskirt", Null(),
#            "JubesX.Panties and not JubesX.PantiesDown", Null(),
#            "JubesX.Wet == 1", "Wet_Drip",
#            "True", "Wet_Drip2",
#            ),

#        (545,540), ConditionSwitch(    #205,530
#            #Spunk
#            "'anal' not in JubesX.Spunk or not Player.Male", Null(),
#            "(JubesX.Legs == 'pants' or JubesX.Legs == 'shorts') and not JubesX.Upskirt", Null(),
#            "JubesX.Wet == 1", "Spunk_Drip",
#            "True", "Spunk_Drip2",
#            ),

        (0,0),"images/JubesSex/[JubesX.skin_image.skin_path]Jubes_Sex_Legs.png",
            #Legs

        (0,0), ConditionSwitch(
            #Wet look
            "not JubesX.Water", Null(),
            "True", "images/JubesSex/Jubes_Sex_Wet_Legs.png",
            ),

#        (0,0), "Jubes_Sex_Anus",
#            #Anus Composite

        (0,0), "Jubes_SC_Pussy",
            #Pussy Composite

        (0,0), ConditionSwitch(
            #hose layer
            "JubesX.Hose == 'stockings and garterbelt'", Recolor("Jubes", "Hose", "images/JubesSex/Jubes_Sex_Hose_StockingsGarter.png"),
            "JubesX.Hose == 'socks'", Recolor("Jubes", "Hose", "images/JubesSex/Jubes_Sex_Hose_Socks.png"),
            "JubesX.Hose == 'garterbelt'", Recolor("Jubes", "Hose", "images/JubesSex/Jubes_Sex_Hose_Garter.png"),
            "JubesX.Hose == 'stockings'", Recolor("Jubes", "Hose", "images/JubesSex/Jubes_Sex_Hose_Stockings.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Panties if up
            "JubesX.PantiesDown", Null(),
            "JubesX.Panties == 'lace panties'", Recolor("Jubes", "Panties", "images/JubesSex/Jubes_Sex_Panties_Lace.png"),
            "JubesX.Panties == 'tiger panties' and JubesX.Wet", Recolor("Jubes", "Panties", "images/JubesSex/Jubes_Sex_Panties_Tiger_Wet.png"),
            "JubesX.Panties == 'tiger panties'", Recolor("Jubes", "Panties", "images/JubesSex/Jubes_Sex_Panties_Tiger.png"),
            "JubesX.Panties == 'bikini bottoms' and JubesX.Wet", Recolor("Jubes", "Panties", "images/JubesSex/Jubes_Sex_Panties_Bikini_Wet.png"),
            "JubesX.Panties == 'bikini bottoms'", Recolor("Jubes", "Panties", "images/JubesSex/Jubes_Sex_Panties_Bikini.png"),
            "JubesX.Panties and JubesX.Wet", "images/JubesSex/Jubes_Sex_Panties_Blue_Wet.png",
            "JubesX.Panties", "images/JubesSex/Jubes_Sex_Panties_Blue.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Piercings
#            "Player.Sprite", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),

#            "Player.Sprite and Player.Cock == 'in' and Speed == 0", Null(),
            "JubesX.Pierce == 'ring'",ConditionSwitch(
                    #If she has panties down. . .
                    "Player.Sprite and Player.Cock == 'in'", "images/JubesSex/Jubes_Sex_Pierce_Ring_Fucking.png",
                    "JubesX.Legs == 'shorts' and not JubesX.Upskirt", "images/JubesSex/Jubes_Sex_Pierce_Ring_Shorts.png",
                    "JubesX.Legs == 'pants' and not JubesX.Upskirt", "images/JubesSex/Jubes_Sex_Pierce_Ring_Pants.png",
                    "JubesX.Panties == 'lace panties' and not JubesX.PantiesDown", "images/JubesSex/Jubes_Sex_Pierce_Ring_Lace.png",
                    "JubesX.Panties == 'tiger panties' and not JubesX.PantiesDown", "images/JubesSex/Jubes_Sex_Pierce_Ring_Tiger.png",
                    "JubesX.Panties == 'bikini bottoms' and not JubesX.PantiesDown", "images/JubesSex/Jubes_Sex_Pierce_Ring_Bikini.png",
                    "JubesX.Panties and not JubesX.PantiesDown", "images/JubesSex/Jubes_Sex_Pierce_Ring_Blue.png",
                    "True", "images/JubesSex/Jubes_Sex_Pierce_Ring.png",
                    ),
            "not JubesX.Pierce", Null(),
            #else, it's barbell

            "JubesX.Legs == 'shorts' and not JubesX.Upskirt", "images/JubesSex/Jubes_Sex_Pierce_Barbell_Shorts.png",
            "JubesX.Legs == 'pants' and not JubesX.Upskirt", "images/JubesSex/Jubes_Sex_Pierce_Barbell_Pants.png",
            "JubesX.Panties == 'lace panties' and not JubesX.PantiesDown", "images/JubesSex/Jubes_Sex_Pierce_Barbell_Lace.png",
            "JubesX.Panties == 'tiger panties' and not JubesX.PantiesDown", "images/JubesSex/Jubes_Sex_Pierce_Barbell_Tiger.png",
            "JubesX.Panties == 'bikini bottoms' and not JubesX.PantiesDown", "images/JubesSex/Jubes_Sex_Pierce_Barbell_Bikini.png",
            "JubesX.Panties and not JubesX.PantiesDown", "images/JubesSex/Jubes_Sex_Pierce_Barbell_Blue.png",
            "True", "images/JubesSex/Jubes_Sex_Pierce_Barbell.png",
            ),
        (0,0), ConditionSwitch(
            #pantyhose layer
            "JubesX.Panties and JubesX.PantiesDown", Null(),
            "JubesX.Hose == 'pantyhose'", Recolor("Jubes", "Hose", "images/JubesSex/Jubes_Sex_Hose_Pantyhose.png"),
            "JubesX.Hose == 'ripped pantyhose'", Recolor("Jubes", "Hose", "images/JubesSex/Jubes_Sex_Hose_Pantyhose_Holed.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs Layer
#            "JubesX.Upskirt",ConditionSwitch(
#                    #If she has panties down. . .
##                    "JubesX.Legs == 'skirt'", "images/JubesSex/Jubes_Sex_Legs_Skirt_Up.png",
#                    "JubesX.Legs == 'shorts'", Recolor("Jubes", "Legs", "images/JubesSex/Jubes_Sex_Legs_Shorts_Up.png"),
#                    "JubesX.Legs == 'pants'", Recolor("Jubes", "Legs", "images/JubesSex/Jubes_Sex_Legs_Pants_Up.png"),
#                    "True", Null(),
#                    ),

#            "JubesX.Legs == 'dress' and JubesX.Over == 'dress'", Recolor("Jubes", "Over", "images/JubesSex/Jubes_Sex_Legs_Dress.png"),
            "JubesX.Legs == 'skirt'", Recolor("Jubes", "Legs", "images/JubesSex/Jubes_Sex_Legs_Skirt.png"),

            "JubesX.Upskirt", Null(),
#            "JubesX.Legs == 'skirt'", Recolor("Jubes", "Legs", "images/JubesSex/Jubes_Sex_Legs_Skirt.png"),
            "JubesX.Legs == 'shorts' and JubesX.Wet > 1", Recolor("Jubes", "Legs", "images/JubesSex/Jubes_Sex_Legs_Shorts_Wet.png"),
            "JubesX.Legs == 'shorts'", Recolor("Jubes", "Legs", "images/JubesSex/Jubes_Sex_Legs_Shorts.png"),
            "JubesX.Legs == 'pants'", Recolor("Jubes", "Legs", "images/JubesSex/Jubes_Sex_Legs_Pants.png"),
            "True", Null(),
            ),


        (0,0), ConditionSwitch(
            #Piercings
            "JubesX.Pierce == 'ring'",ConditionSwitch(
                    #If she has panties down. . .
                    "JubesX.Legs == 'shorts' and not JubesX.Upskirt", "images/JubesSex/Jubes_Sex_Pierce_Ring_Shorts.png",
                    "JubesX.Legs == 'pants' and not JubesX.Upskirt", "images/JubesSex/Jubes_Sex_Pierce_Ring_Pants.png",
                    "True", Null(),
                    ),
            #else, it's barbell
            "JubesX.Legs == 'shorts' and not JubesX.Upskirt", "images/JubesSex/Jubes_Sex_Pierce_Barbell_Shorts.png",
            "JubesX.Legs == 'pants' and not JubesX.Upskirt", "images/JubesSex/Jubes_Sex_Pierce_Barbell_Pants.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #dress Layer
            "JubesX.Over == 'dress'", Recolor("Jubes", "Over", "images/JubesSex/Jubes_Sex_Legs_Dress.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy'", "Jubes_Sex_Lick_Pussy",
            "Trigger == 'lick ass'", "Jubes_Sex_Lick_Ass",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy fondling animation
            "Player.Sprite", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Jubes_Sex_Fondle_Pussy",
            "JubesX.Offhand == 'fondle pussy' and JubesX.Lust > 60", At("JubesFingerHand", GirlFingerPussyX()),
            "JubesX.Offhand == 'fondle pussy'", At("JubesMastHand", GirlGropePussyX()),
            "True", Null(),
            ),
#        (0,0), "Jubes_Sex_Feet",
        )
# End Jubes Sex Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Jubes SC Pose Pussy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Jubes_SC_Pussy:
    contains:
            # The background plate of her pussy
            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/JubesSex/Jubes_Sex_Pussy_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed", "Jubes_Sex_Heading_Pussy",
                "Speed", "images/JubesSex/Jubes_Sex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/JubesSex/Jubes_Sex_Pussy_Open.png",
                "JubesX.Offhand == 'fondle pussy' and JubesX.Lust > 60", "images/JubesSex/Jubes_Sex_Pussy_Open.png",
                "True", "images/JubesSex/Jubes_Sex_Pussy_Closed.png",
                )
    contains:
            # pubes
            ConditionSwitch(
                "not JubesX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", Recolor("Jubes", "Pubes", "images/JubesSex/Jubes_Sex_Pubes_Fucking.png"),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 1", Recolor("Jubes", "Pubes", "images/JubesSex/Jubes_Sex_Pubes_Fucking.png"),
#                "Player.Sprite and Player.Cock == 'in'", Recolor("Jubes", "Pubes", "images/JubesSex/Jubes_Sex_Pubes_Open.png"),
                "Speed", Recolor("Jubes", "Pubes", "images/JubesSex/Jubes_Sex_Pubes_Open.png"),
                "Trigger == 'lick pussy'", Recolor("Jubes", "Pubes", "images/JubesSex/Jubes_Sex_Pubes_Open.png"),
                "JubesX.Offhand == 'fondle pussy' and JubesX.Lust > 60", Recolor("Jubes", "Pubes", "images/JubesSex/Jubes_Sex_Pubes_Open.png"),
                "True", Recolor("Jubes", "Pubes", "images/JubesSex/Jubes_Sex_Pubes_Closed.png"),
                )

# End Jubes Scissor Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_SC_Anim_0:
        #this is the animation for Jubes's lower body during Scissoring, Speed 0 (static)
        contains:
            subpixel True
            "Jubes_Sex_Body"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 20
            pos (30,80) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                ease 2 pos (30,90)
                pause .5
                ease 2 pos (30,80)
                pause .5
                repeat
        contains:
            subpixel True
            "Jubes_SC_Legs"
            anchor (560,580)#(560,420)
            offset (560,580) #(560,580)
            transform_anchor True
            zoom 1.3
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
        contains:
            subpixel True
            "Jubes_Sex_Feet"
#            ConditionSwitch(
#                #Shows different lower body motion depending on events
#                "ShowFeet", "Jubes_Sex_Feet",
#                "True", AlphaMask("Jubes_Sex_Feet","images/JubesSex/Jubes_Sex_FeetMask.png")
#                )
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.3
            rotate 35
            pos (0,0) #X less is left, Y less is up
            parallel:
                pause .5
                ease 2 rotate 30
                pause .5
                ease 2 rotate 35
                repeat
        #end animation for Jubes's lower body during Scissoring, Speed 0 (static) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Jubes_SC_Anim_1:
        #this is the animation for Jubes's lower body during Scissoring, Speed 1 (slow)
        contains:
            subpixel True
            "Jubes_Sex_Body"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 20
            pos (30,80) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                ease 1 pos (30,90)
                pause .5
                ease 1 pos (30,80)
                pause .5
                repeat
        contains:
            subpixel True
            "Jubes_SC_Legs"
            anchor (560,580)#(560,420)
            offset (560,580) #(560,580)
            transform_anchor True
            zoom 1.3
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
            "Jubes_Sex_Feet"
#            ConditionSwitch(
#                #Shows different lower body motion depending on events
#                "ShowFeet", "Jubes_Sex_Feet",
#                "True", AlphaMask("Jubes_Sex_Feet","images/JubesSex/Jubes_Sex_FeetMask.png")
#                )
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.3
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
        #End animation for Jubes's lower body during Scissoring, Speed 1 (slow) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_SC_Anim_2:
        #this is the animation for Jubes's lower body during Scissoring, Speed 2 (fast)
        contains:
            subpixel True
            "Jubes_Sex_Body"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 20
            pos (30,80) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                pause .1
                ease .5 pos (30,90)
                ease .5 pos (30,80)
                repeat
        contains:
            subpixel True
            "Jubes_SC_Legs"
            anchor (560,580)#(560,420)
            offset (560,580) #(560,580)
            transform_anchor True
            zoom 1.3
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
            "Jubes_Sex_Feet"
#            ConditionSwitch(
#                #Shows different lower body motion depending on events
#                "ShowFeet", "Jubes_Sex_Feet",
#                "True", AlphaMask("Jubes_Sex_Feet","images/JubesSex/Jubes_Sex_FeetMask.png")
#                )
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.3
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
        #End animation for Jubes's lower body during Scissoring, Speed 2 (fast) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     SC Launch/Reset
label Jubes_SC_Launch(Line = Trigger):
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    return
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary

    $ Trigger = Line

    if renpy.showing("Jubes_SC_Sprite"):
        return
    $ Speed = 0
    call Girl_Hide(JubesX,1) #call Rogue_Hide
    show Jubes_SC_Sprite zorder 150
    with dissolve
    return

label Jubes_SC_Reset:
    if not renpy.showing("Jubes_SC_Sprite"):
        return
    $ JubesX.ArmPose = 2
    hide Jubes_SC_Sprite
    call Girl_Hide(JubesX) #call Rogue_Hide
#    call Set_The_Scene(Dress = 0)
    show Jubes_Sprite at SpriteLoc(JubesX.SpriteLoc) zorder JubesX.Layer:
        alpha 1 zoom 1 offset (0,0) anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return
# End Jubes Scissor Pose content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


# Animation components / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Jubes Misc Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#label Jubes_Kissing_Launch(T = Trigger,Set=1):
#    call Jubes_Hide
#    $ Trigger = T
#    $ JubesX.Pose = "kiss" if Set else JubesX.Pose
#    show Jubes_Sprite at SpriteLoc(JubesX.SpriteLoc) zorder JubesX.Layer
#    show Jubes_Sprite at SpriteLoc(StageCenter) zorder JubesX.Layer:
#        ease 0.5 offset (0,0) zoom 2 alpha 1
#    return

#label Jubes_Kissing_Smooch:
#    $ JubesX.FaceChange("kiss")
#    show Jubes_Sprite at SpriteLoc(StageCenter) zorder JubesX.Layer:
#        ease 0.5 xpos StageCenter offset (0,0) zoom 2 alpha 1
#        pause 1
#        ease 0.5 xpos JubesX.SpriteLoc zoom 1
#    show Jubes_Sprite at SpriteLoc(JubesX.SpriteLoc) zorder JubesX.Layer:
#        zoom 1
#    $ JubesX.FaceChange("sexy")
#    return

#label Jubes_Breasts_Launch(T = Trigger,Set=1):
#    call Jubes_Hide
#    $ Trigger = T
#    $ JubesX.Pose = "breasts" if Set else JubesX.Pose
#    show Jubes_Sprite at SpriteLoc(JubesX.SpriteLoc) zorder JubesX.Layer:
##        ease 0.5 offset (-100,-200) zoom 2
#        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
#    return

#label Jubes_Middle_Launch(T = Trigger,Set=1):
#    call Jubes_Hide
#    $ Trigger = T
#    $ JubesX.Pose = "mid" if Set else JubesX.Pose
#    show Jubes_Sprite at SpriteLoc(JubesX.SpriteLoc) zorder JubesX.Layer:
##        ease 0.5 offset (-100,-200) zoom 2
#        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
#    return

#label Jubes_Pussy_Launch(T = Trigger,Set=1):
#    call Jubes_Hide
#    $ Trigger = T
#    $ JubesX.Pose = "pussy" if Set else JubesX.Pose
#    show Jubes_Sprite at SpriteLoc(JubesX.SpriteLoc) zorder JubesX.Layer:
#        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
#    return

#label Jubes_Pos_Reset(T = 0,Set=0):
#    if JubesX.Loc != bg_current:
#            return
#    call Jubes_Hide
#    show Jubes_Sprite at SpriteLoc(JubesX.SpriteLoc) zorder JubesX.Layer:
#            ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
#    show Jubes_Sprite zorder JubesX.Layer:
#            offset (0,0)
#            anchor (0.5, 0.0)
#            zoom 1
#            xzoom 1
#            yzoom 1
#            alpha 1
#            pos (JubesX.SpriteLoc,50)
#    $ JubesX.Pose = "full" if Set else 0
#    $ Trigger = T
#    return

#label Jubes_Hide(Sprite=0):
##        call Jubes_Sex_Reset
#        hide Jubes_SexSprite
#        hide Jubes_Doggy_Animation
#        hide Jubes_HJ_Animation
#        hide Jubes_BJ_Animation
#        hide Jubes_TJ_Animation
#        hide Jubes_Finger_Animation
#        hide Jubes_CUN_Animation
#        hide Jubes_Seated
#        if Sprite:
#                hide Jubes_Sprite
#        return



# Interface items //////////////////////////////////////////////////////////////////////////////

image GropeLeftBreast_Jubes:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65#.7
        pos (290,370)#(195,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 60
        block:
            ease 1 rotate 30
            ease 1 rotate 60
            repeat

image GropeRightBreast_Jubes:
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (190,370)#(110,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block:
            ease 1 rotate -30 #-30
            ease 1 rotate -60 #-60
            repeat

image LickRightBreast_Jubes:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5
        xzoom -0.45
        pos (290,350)#(95,355)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (270,330)#(85,345)  top
            pause .5
            ease 1.5 rotate 30 pos (290,350)#(105,375) bottom
            repeat

image LickLeftBreast_Jubes:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5
        xzoom -0.45
        pos (175,340) #(195,360)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (170,320)#(190,380)
            pause .5
            ease 1.5 rotate 30 pos (175,340)#(200,410)
            repeat

image GropeThigh_Jubes:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (235,640)#(180,670)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        block:
            pause .5
            ease 1 rotate 110 pos (195,740) #(205,750) bottom
            ease 1 rotate 100 pos (235,640)   #215
            repeat

image GropePussy_Jubes:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (260,580)#(120,620) -20
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease .5 rotate 190 ypos 565 #(200,585)
                ease .75 rotate 170 ypos 580
            choice:
                ease .5 rotate 190 ypos 565
                pause .25
                ease 1 rotate 170 ypos 580
            repeat

image FingerPussy_Jubes:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.65
        pos (275,650)#(140,700)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (285,625)#(150,665)
                pause .5
                ease 1 rotate 50 pos (275,650)  #(140,700)
            choice:
                ease .5 rotate 40 pos (285,625)
                pause .5
                ease 1.75 rotate 50 pos (275,650)
            choice:
                ease 2 rotate 40 pos (285,625)
                pause .5
                ease 1 rotate 50 pos (275,650)
            choice:
                ease .25 rotate 40 pos (285,625)
                ease .25 rotate 50 pos (275,650)
                ease .25 rotate 40 pos (285,625)
                ease .25 rotate 50 pos (275,650)
            repeat

image Lickpussy_Jubes:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (285,610)#(155,650)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout .5 rotate -50 pos (275,590) #(210,605)
            linear .5 rotate -60 pos (265,600) #(200,615)
            easein 1 rotate 10 pos (285,610) #(230,625)
            repeat

image VibratorRightBreast_Jubes:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (180,330)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            pause .25
            ease 1 rotate 35 ypos 320
            pause .25
            ease 1 rotate 55 ypos 330
            repeat

image VibratorLeftBreast_Jubes:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (285,340) #(270,400)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 330
            pause .25
            ease 1 rotate 55 ypos 340
            pause .25
            repeat

image VibratorPussy_Jubes:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (285,600) #(240,665)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 70
        block:
            ease 1 rotate 35 pos (275,590)
            pause .25
            ease 1 rotate 70 pos (285,600)
            pause .25
            repeat

image VibratorAnal_Jubes:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (305,590)
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
            ease 1 rotate 0 pos (295,580)
            pause .25
            ease 1 rotate 10 pos (305,590)
            pause .25
            repeat

image VibratorPussyInsert_Jubes:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_Jubes:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0



#Lesbian action animations.
image GirlGropeBothBreast_Jubes:
    contains:
        "GirlGropeLeftBreast_Jubes"
    contains:
        "GirlGropeRightBreast_Jubes"

image GirlGropeLeftBreast_Jubes:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (290,340) #(220,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate 10 ypos 350#(280,390)
            ease 1 rotate -10 ypos 340
            repeat

image GirlGropeRightBreast_Jubes:
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (190,340) #(90,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block:
            ease 1 rotate -40 ypos 350#(90,410)
            ease 1 rotate -10 ypos 340
            repeat

image GirlGropeThigh_Jubes:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (210,730)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        parallel:
            pause .5
            ease 1 ypos 780
            ease 1 ypos 730
            repeat
        parallel:
            pause .5
            ease .5 xpos 213
            ease .5 xpos 210
            ease .5 xpos 213
            ease .5 xpos 210
            repeat

image GirlGropePussy_JubesSelf:
    contains:
        "GirlGropePussy_Jubes"
        anchor (0.5,0.5)
        rotate -40
#        yzoom -1
        pos (180,525)

image GirlGropePussy_Jubes:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (265,575) #(130,595
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 ypos 570
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 ypos 570#-10+20
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 ypos 570 #(205,590)
                ease .75 rotate 200 ypos 575 #(205,595)
                ease .5 rotate 205 ypos 570
                ease .75 rotate 200 ypos 575
            choice: #Fast stroke
                ease .3 rotate 205 ypos 570
                ease .3 rotate 200 ypos 580
                ease .3 rotate 205 ypos 570
                ease .3 rotate 200 ypos 580
            repeat

image GirlFingerPussy_Jubes:
    contains:
        subpixel True
        "UI_GirlFinger"
        zoom .6
        pos (265,570)#(220,640)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 ypos 575
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 ypos 575
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 ypos 575
                ease .75 rotate 200 ypos 580
                ease .5 rotate 205 ypos 575
                ease .75 rotate 200 ypos 580
            choice: #Fast stroke
                ease .3 rotate 205 ypos 575
                ease .3 rotate 200 ypos 585
                ease .3 rotate 205 ypos 575
                ease .3 rotate 200 ypos 585
            repeat

image JubesMastHand:
        "images/UI_GirlHand_Jubes.png"
        zoom 0.9
        rotate 220
        offset (345,230)

image JubesFingerHand:
        "images/UI_GirlFinger_Jubes.png"
        zoom 0.9
        rotate 220
        offset (333,300)


#Start of fireworks animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Star1:
        "images/JubesSprite/Star_P.png"
        block:
            rotate 0
            ease 1 rotate 360
            repeat

image Star2:
        "images/JubesSprite/Star_B.png"
        block:
            rotate 0
            ease 1 rotate 360
            repeat

image Star3:
        "images/JubesSprite/Star_Y.png"
        block:
            rotate 0
            ease 1 rotate 360
            repeat

image Fireworks:
        #Jubilee's firework
        contains:
            alpha 1
            anchor (0.5,0.5)
            transform_anchor True
#            pos (0.5,0.5)
            offset (0,0)
            pause .2
            choice:
                "Star1"
            choice:
                "Star2"
            choice:
                "Star3"
            parallel:
                #hides image over last .3 seconds
                pause 0.7
                ease 0.3 alpha 0
            parallel:
                offset (0,0)
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (50,-100)
                        ease .5 offset (100,150)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom 1
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (-25,-120)
                        ease .5 offset (-50,130)
                    parallel:
                        #grows it
                        zoom 0.2
                        ease 1 zoom .9
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (25,-130)
                        ease .5 offset (50,140)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom 1.2
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (10,-150)
                        ease .5 offset (20,140)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom .9
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (100,-100)
                        ease .5 offset (150,150)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom 1.2
        #End Star 1
        contains:
            alpha 1
            anchor (0.5,0.5)
#            pos (0.5,0.5)
            transform_anchor True
            pause .1
            choice:
                "Star1"
            choice:
                "Star2"
            choice:
                "Star3"
            parallel:
                #hides image over last .3 seconds
                pause 0.7
                ease 0.3 alpha 0
            parallel:
                offset (0,0)
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (50,-100)
                        ease .5 offset (100,150)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom 1
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (-25,-120)
                        ease .5 offset (-50,130)
                    parallel:
                        #grows it
                        zoom 0.2
                        ease 1 zoom .9
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (25,-130)
                        ease .5 offset (50,140)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom 1.2
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (10,-150)
                        ease .5 offset (20,140)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom .9
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (100,-100)
                        ease .5 offset (150,150)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom 1.2
        #End Star 2
        contains:
            alpha 1
            anchor (0.5,0.5)
#            pos (0.5,0.5)
            transform_anchor True
            choice:
                "Star1"
            choice:
                "Star2"
            choice:
                "Star3"
            parallel:
                #hides image over last .3 seconds
                pause 0.7
                ease 0.3 alpha 0
            parallel:
                offset (0,0)
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (50,-100)
                        ease .5 offset (100,150)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom 1
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (-25,-120)
                        ease .5 offset (-50,130)
                    parallel:
                        #grows it
                        zoom 0.2
                        ease 1 zoom .9
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (25,-130)
                        ease .5 offset (50,140)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom 1.2
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (10,-150)
                        ease .5 offset (20,140)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom .9
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (100,-100)
                        ease .5 offset (150,150)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom 1.2
        #End Star 3
#end of fireworks animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
