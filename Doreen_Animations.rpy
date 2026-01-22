# Basic character Sprites

image Doreen_Sprite:
    LiveComposite(
        (600,1300),       #550,950
        (0,0), "images/DoreenSprite/Doreen_Sprite_Shadow.png",
        (0,0), ConditionSwitch(
            #Tail
            "DoreenX.Tail","images/DoreenSprite/Doreen_Sprite_Tail.png",
            "True", Null(),
            ),
        (95,20), "Doreen_Sprite_HairBack", #(15,-80)
#        (0,0), ConditionSwitch(
#            #skirt back
#            "DoreenX.Upskirt", Null(),
##            "DoreenX.Legs == 'pants'", "images/DoreenSprite/Doreen_Sprite_Legs_Pants_Back.png",
#            "DoreenX.Legs == 'skirt'", "images/DoreenSprite/Doreen_Sprite_Legs_Skirt_Back.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #panties down back
            "not DoreenX.Panties or not DoreenX.PantiesDown", Null(),
            #if the panties are down
            "DoreenX.Legs and not DoreenX.Upskirt and DoreenX.Legs != 'skirt'", Null(),
            #if she's wearing a skirt or nothing else
            "DoreenX.Panties == 'lace panties' and DoreenX.Legs == 'shorts'", "images/DoreenSprite/Doreen_Sprite_Panties_Lace_BackS.png",
            "DoreenX.Panties == 'lace panties'", "images/DoreenSprite/Doreen_Sprite_Panties_Lace_Back.png",
            "DoreenX.Panties == 'bikini bottoms'", "images/DoreenSprite/Doreen_Sprite_Panties_Bikini_Back.png",
            "True", "images/DoreenSprite/Doreen_Sprite_Panties_Tan_Back.png",
            ),

        (275,560), ConditionSwitch(    #165,560
            #Personal Wetness
            "not DoreenX.Wet", Null(),
            "DoreenX.Wet == 1 or (DoreenX.Legs and DoreenX.Legs != 'skirt' and not DoreenX.Upskirt)", "Wet_Drip", #ConditionSwitch( #Wet = 1
#                    "(DoreenX.Legs == 'pants' or DoreenX.Legs == 'shorts') and not DoreenX.Upskirt", Null(),
#                    "DoreenX.Panties and not DoreenX.PantiesDown", Null(),
#                    "(DoreenX.Legs == 'pants' or DoreenX.Legs == 'shorts')", AlphaMask("Wet_Drip","Doreen_Drip_MaskP"),
#                    "DoreenX.Panties and DoreenX.PantiesDown", AlphaMask("Wet_Drip","Doreen_Drip_MaskP"),
#                    "True", AlphaMask("Wet_Drip","Doreen_Drip_Mask"), #only plays if nothing is in the way
#                    ),
            "True", "Wet_Drip2", #ConditionSwitch( #Wet = 2+
#                    "(DoreenX.Legs == 'pants' or DoreenX.Legs == 'shorts') and DoreenX.Upskirt", AlphaMask("Wet_Drip2","Doreen_Drip_MaskP"),
#                    "DoreenX.Panties and DoreenX.PantiesDown", AlphaMask("Wet_Drip2","Doreen_Drip_MaskP"),
#                    "True", AlphaMask("Wet_Drip2","Doreen_Drip_Mask"), #only plays if nothing is in the way
#                    ),
            ),

        (275,560), ConditionSwitch(    #165,560
            #Spunk
            "('in' not in DoreenX.Spunk and 'anal' not in DoreenX.Spunk) or not Player.Male", Null(),
            "DoreenX.Panties and not DoreenX.PantiesDown", "Spunk_Drip", #ConditionSwitch( #Wet = 1
            "DoreenX.Legs and DoreenX.Legs != 'skirt' and not DoreenX.Upskirt", "Spunk_Drip", #ConditionSwitch( #Wet = 1
#                    "DoreenX.Panties and DoreenX.PantiesDown", AlphaMask("Spunk_Drip","Doreen_Drip_MaskP"),
#                    "(DoreenX.Legs == 'pants' or DoreenX.Legs == 'shorts') and DoreenX.Upskirt", AlphaMask("Spunk_Drip","Doreen_Drip_MaskP"),
#                    "True", AlphaMask("Spunk_Drip","Doreen_Drip_Mask"), #only plays if nothing is in the way
#                    ),
            "True", "Spunk_Drip2", #ConditionSwitch( #Wet = 2+
#                    "(DoreenX.Legs == 'pants' or DoreenX.Legs == 'shorts') and DoreenX.Upskirt", AlphaMask("Spunk_Drip2","Doreen_Drip_MaskP"),
#                    "DoreenX.Panties and DoreenX.PantiesDown", AlphaMask("Spunk_Drip2","Doreen_Drip_MaskP"),
#                    "True", AlphaMask("Spunk_Drip2","Doreen_Drip_Mask"), #only plays if nothing is in the way
#                    ),
            ),

        (0,0), ConditionSwitch(
            #body
            "DoreenX.ArmPose != 1", "images/DoreenSprite/[DoreenX.skin_image.skin_path]Doreen_Sprite_Body2.png",         # right hand up/left down
            "True", "images/DoreenSprite/[DoreenX.skin_image.skin_path]Doreen_Sprite_Body1.png", #if DoreenX.Arms == 1   # right Hand on hip/left raised
            ),
        (0,0), ConditionSwitch(
            #pubes
            "DoreenX.Pubes", "images/DoreenSprite/Doreen_Sprite_Pubes.png",         # right hand up/left down
            "True", Null(), #if DoreenX.Arms == 1   # right Hand on hip/left raised
            ),
        (0,0), ConditionSwitch(
            #Jacket back
            "DoreenX.Acc == 'vest'", "images/DoreenSprite/Doreen_Sprite_Vest_Base.png",         # right hand up/left down
            "DoreenX.ArmPose != 1 and DoreenX.Acc == 'jacket'", "images/DoreenSprite/Doreen_Sprite_Jacket2_Base.png",         # right hand up/left down
            "DoreenX.Acc == 'jacket'", "images/DoreenSprite/Doreen_Sprite_Jacket1_Base.png",         # right hand up/left down
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Water effect
#            "DoreenX.Water and DoreenX.ArmPose == 1", "images/DoreenSprite/Doreen_Sprite_Water1.png",
            "DoreenX.Water", "images/DoreenSprite/Doreen_Sprite_Water.png",
            "True", Null(),
            ),


        (0,0), ConditionSwitch(
            #Personal Wetness  over
            "not DoreenX.Wet", Null(),
            "DoreenX.Panties and not DoreenX.PantiesDown", Null(),
            "DoreenX.Legs and DoreenX.Legs != 'skirt' and not DoreenX.Upskirt", Null(),
            "True", "images/DoreenSprite/Doreen_Sprite_Wet.png", #ConditionSwitch( #Wet = 2+
            ),
        (0,0), ConditionSwitch(
            #Spunk over
            "('in' not in DoreenX.Spunk and 'anal' not in DoreenX.Spunk) or not Player.Male", Null(),
            "DoreenX.Legs and DoreenX.Legs != 'skirt' and not DoreenX.Upskirt", Null(),
            "DoreenX.Panties and not DoreenX.PantiesDown", Null(),
            "True", "images/DoreenSprite/Doreen_Sprite_Spunk_Pussy.png",
            ),

#        (0,0), ConditionSwitch(
#            #Necklaces
#            "DoreenX.Neck == 'choker'", "images/DoreenSprite/Doreen_Sprite_Neck_Choker.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #stockings
            "DoreenX.Hose == 'stockings'", "images/DoreenSprite/Doreen_Sprite_Hose_Stockings.png",
            "DoreenX.Hose == 'stockings and garterbelt'", "images/DoreenSprite/Doreen_Sprite_Hose_StockingsGarter.png",
            "DoreenX.Hose == 'garterbelt'", "images/DoreenSprite/Doreen_Sprite_Hose_Garter.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #panties
#            "not DoreenX.Panties", Null(),
            "DoreenX.PantiesDown", ConditionSwitch(
                    #if the panties are down
                    "not DoreenX.Legs or DoreenX.Upskirt or DoreenX.Legs == 'skirt'", ConditionSwitch(
                            #if she's wearing a skirt or nothing else
                            "DoreenX.Panties == 'bikini bottoms'", "images/DoreenSprite/Doreen_Sprite_Panties_Bikini_Down.png",
                            "DoreenX.Panties == 'lace panties'", "images/DoreenSprite/Doreen_Sprite_Panties_Lace_Down.png",
                            "DoreenX.Panties", "images/DoreenSprite/Doreen_Sprite_Panties_Tan_Down.png",
                            "True", Null(),
                            ),
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                #if she's not wet
                "DoreenX.Panties == 'bikini bottoms'", "images/DoreenSprite/Doreen_Sprite_Panties_Bikini.png",
                "DoreenX.Panties == 'lace panties'", "images/DoreenSprite/Doreen_Sprite_Panties_Lace.png",
                "DoreenX.Panties and DoreenX.Wet", "images/DoreenSprite/Doreen_Sprite_Panties_Tan_Wet.png",
                "DoreenX.Panties", "images/DoreenSprite/Doreen_Sprite_Panties_Tan.png",
                "True", Null(),
                ),
            ),
        (0,0), ConditionSwitch(
            #pantyhose
            "DoreenX.Hose == 'pantyhose' and (not DoreenX.PantiesDown or not DoreenX.Panties)", "images/DoreenSprite/Doreen_Sprite_Hose_Pantyhose.png",
            "DoreenX.Hose == 'tights' and DoreenX.Wet and (not DoreenX.PantiesDown or not DoreenX.Panties)", "images/DoreenSprite/Doreen_Sprite_Hose_Tights_Wet.png",
            "DoreenX.Hose == 'tights' and (not DoreenX.PantiesDown or not DoreenX.Panties)", "images/DoreenSprite/Doreen_Sprite_Hose_Tights.png",
            "DoreenX.Hose == 'ripped pantyhose' and (not DoreenX.PantiesDown or not DoreenX.Panties)", "images/DoreenSprite/Doreen_Sprite_Hose_Pantyhose_Holed.png",
            "DoreenX.Hose == 'ripped tights' and (not DoreenX.PantiesDown or not DoreenX.Panties)", "images/DoreenSprite/Doreen_Sprite_Hose_Tights_Holed.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #pants
            "not DoreenX.Legs", Null(),
            "DoreenX.Upskirt", ConditionSwitch(
                        #if the skirt's up or pants down
                        "DoreenX.Legs == 'skirt'", "images/DoreenSprite/Doreen_Sprite_Legs_Skirt_Up.png",
                        "DoreenX.Legs == 'red skirt'", "images/DoreenSprite/Doreen_Sprite_Legs_RedSkirt_Up.png",
                        "DoreenX.Legs == 'shorts'", "images/DoreenSprite/Doreen_Sprite_Legs_Shorts_Down.png",
                        "True", Null(),
                        ),
            "DoreenX.Legs == 'skirt' and DoreenX.Over != 'towel'", "images/DoreenSprite/Doreen_Sprite_Legs_Skirt.png",
            "DoreenX.Legs == 'red skirt' and DoreenX.Over != 'towel'", "images/DoreenSprite/Doreen_Sprite_Legs_RedSkirt.png",
            "DoreenX.Wet > 1", ConditionSwitch(
                #if she's wet
                "DoreenX.Legs == 'shorts'", "images/DoreenSprite/Doreen_Sprite_Legs_Shorts_Wet.png",
                "True", Null(),
                ),
            #if she's not wet
            "DoreenX.Legs == 'shorts'", "images/DoreenSprite/Doreen_Sprite_Legs_Shorts.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #nude lower piercings
            "not DoreenX.Pierce", Null(),
            "(DoreenX.Legs == 'skirt' or DoreenX.Legs == 'red skirt') and not DoreenX.Upskirt", Null(),
            "DoreenX.Pierce == 'ring'", ConditionSwitch(
                    # if top is up. . .
                    "DoreenX.Legs == 'shorts' and not DoreenX.Upskirt", "images/DoreenSprite/Doreen_Sprite_Pierce_Pussy_R_Brown.png",

                    "DoreenX.Panties and DoreenX.PantiesDown", "images/DoreenSprite/Doreen_Sprite_Pierce_Pussy_R.png",
                    "DoreenX.Hose == 'tights'", "images/DoreenSprite/Doreen_Sprite_Pierce_Pussy_R_Gray.png",
                    "DoreenX.Hose == 'pantyhose'", "images/DoreenSprite/Doreen_Sprite_Pierce_Pussy_R_Hose.png",

                    "DoreenX.Panties == 'bikini bottoms'", "images/DoreenSprite/Doreen_Sprite_Pierce_Pussy_R_Green.png",

                    "DoreenX.Panties == 'lace panties'", "images/DoreenSprite/Doreen_Sprite_Pierce_Pussy_R_Lace.png",
                    "DoreenX.Panties", "images/DoreenSprite/Doreen_Sprite_Pierce_Pussy_R_Tan.png",

                    "True", "images/DoreenSprite/Doreen_Sprite_Pierce_Pussy_R.png",
                    ),

            "DoreenX.Panties and DoreenX.PantiesDown", "images/DoreenSprite/Doreen_Sprite_Pierce_Pussy_B.png",
            "DoreenX.Legs == 'shorts' and not DoreenX.Upskirt", "images/DoreenSprite/Doreen_Sprite_Pierce_Pussy_B_Brown.png",

            "DoreenX.Hose == 'tights'", "images/DoreenSprite/Doreen_Sprite_Pierce_Pussy_B_Gray.png",
            "DoreenX.Hose == 'pantyhose'", "images/DoreenSprite/Doreen_Sprite_Pierce_Pussy_B_Hose.png",

            "DoreenX.Panties == 'bikini bottoms'", "images/DoreenSprite/Doreen_Sprite_Pierce_Pussy_B_Green.png",

            "DoreenX.Panties == 'lace panties'", "images/DoreenSprite/Doreen_Sprite_Pierce_Pussy_B_Lace.png",
            "DoreenX.Panties", "images/DoreenSprite/Doreen_Sprite_Pierce_Pussy_B_Tan.png",

            "True", "images/DoreenSprite/Doreen_Sprite_Pierce_Pussy_B.png",
            ),

        (0,0), ConditionSwitch(
            #Chest layer
            "DoreenX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "DoreenX.Chest == 'bikini top'", "images/DoreenSprite/Doreen_Sprite_Chest_Bikini_Up.png",
                    "DoreenX.Chest == 'sports bra'", "images/DoreenSprite/Doreen_Sprite_Chest_Sports_Up.png",
                    "DoreenX.Chest == 'lace bra'", "images/DoreenSprite/Doreen_Sprite_Chest_Lace_Up.png",
                    "DoreenX.Chest", "images/DoreenSprite/Doreen_Sprite_Chest_Bra_Up.png",
                    "True", Null(),
                    ),
            "DoreenX.Chest == 'bikini top'", "images/DoreenSprite/Doreen_Sprite_Chest_Bikini.png",
            "DoreenX.Chest == 'sports bra'", "images/DoreenSprite/Doreen_Sprite_Chest_Sports.png",
            "DoreenX.Chest == 'lace bra'", "images/DoreenSprite/Doreen_Sprite_Chest_Lace.png",
            "DoreenX.Chest", "images/DoreenSprite/Doreen_Sprite_Chest_Bra.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over
            "DoreenX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "DoreenX.Over == 'tube top'", "images/DoreenSprite/Doreen_Sprite_Over_Tube_Up.png",
                    "DoreenX.Over == 'tshirt' and DoreenX.Acc == 'jacket'", "images/DoreenSprite/Doreen_Sprite_Over_Tshirt_JUp.png",
                    "DoreenX.Over == 'tshirt' and DoreenX.ArmPose == 1", "images/DoreenSprite/Doreen_Sprite_Over_Tshirt1_Up.png",
                    "DoreenX.Over == 'tshirt'", "images/DoreenSprite/Doreen_Sprite_Over_Tshirt2_Up.png",
                    "DoreenX.Over == 'sweater' and DoreenX.Acc == 'jacket'", "images/DoreenSprite/Doreen_Sprite_Over_Sweater_Under_Up.png",
                    "DoreenX.Over == 'sweater' and DoreenX.ArmPose == 1", "images/DoreenSprite/Doreen_Sprite_Over_Sweater1_Up.png",
                    "DoreenX.Over == 'sweater'", "images/DoreenSprite/Doreen_Sprite_Over_Sweater2_Up.png",
                    "True", Null(),
                    ),
            #If she's using arm pose 1, left arm pointing
            #If she's using arm pose 2, Left arm on hip
            "DoreenX.Over == 'tube top'", "images/DoreenSprite/Doreen_Sprite_Over_Tube.png",
            "DoreenX.Over == 'tshirt' and DoreenX.Acc == 'jacket'", "images/DoreenSprite/Doreen_Sprite_Over_Tshirt_J.png",
            "DoreenX.Over == 'tshirt' and DoreenX.ArmPose == 1", "images/DoreenSprite/Doreen_Sprite_Over_Tshirt1.png",
            "DoreenX.Over == 'tshirt'", "images/DoreenSprite/Doreen_Sprite_Over_Tshirt2.png",
            "DoreenX.Over == 'sweater' and DoreenX.Acc == 'jacket'", "images/DoreenSprite/Doreen_Sprite_Over_Sweater_Under.png",
            "DoreenX.Over == 'sweater' and DoreenX.ArmPose == 1", "images/DoreenSprite/Doreen_Sprite_Over_Sweater1.png",
            "DoreenX.Over == 'sweater'", "images/DoreenSprite/Doreen_Sprite_Over_Sweater2.png",
            "DoreenX.Over == 'towel'", "images/DoreenSprite/Doreen_Sprite_Over_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #naked tit piercings
            "not DoreenX.Pierce", Null(),
#            "not DoreenX.Pierce or ((DoreenX.Over or DoreenX.Chest) and not DoreenX.Uptop)", Null(),
#            "DoreenX.Uptop", Null(),
            #Only does this if she has piercings, has no tops, or has her top up
            "DoreenX.Pierce == 'ring'", ConditionSwitch(
                    # if top is up. . .
                    "DoreenX.Uptop", "images/DoreenSprite/Doreen_Sprite_Pierce_Tits_R.png",

                    "DoreenX.Over == 'tube top'", "images/DoreenSprite/Doreen_Sprite_Pierce_Tits_R_Brown.png",
                    "DoreenX.Over == 'tshirt'", "images/DoreenSprite/Doreen_Sprite_Pierce_Tits_R_Gray.png", #change if new tops added in other colors
                    "DoreenX.Over == 'towel'", "images/DoreenSprite/Doreen_Sprite_Pierce_Tits_R_Green.png", #change if new tops added in other colors
                    "DoreenX.Over == 'sweater'", "images/DoreenSprite/Doreen_Sprite_Pierce_Tits_R_Sweater.png", #change if new tops added in other colors

                    "DoreenX.Chest == 'lace bra'", "images/DoreenSprite/Doreen_Sprite_Pierce_Tits_R_Lace.png",
                    "DoreenX.Chest == 'bikini top' or DoreenX.Chest == 'sports bra'", "images/DoreenSprite/Doreen_Sprite_Pierce_Tits_R_Green.png",
                    "DoreenX.Chest", "images/DoreenSprite/Doreen_Sprite_Pierce_Tits_R_Tan.png",
                    "True", "images/DoreenSprite/Doreen_Sprite_Pierce_Tits_R.png",
                    ),
            # Pierce is "barbell"
            "DoreenX.Uptop", "images/DoreenSprite/Doreen_Sprite_Pierce_Tits_B.png",

            "DoreenX.Over == 'tube top'", "images/DoreenSprite/Doreen_Sprite_Pierce_Tits_B_Brown.png",
            "DoreenX.Over == 'tshirt'", "images/DoreenSprite/Doreen_Sprite_Pierce_Tits_B_Gray.png", #change if new tops added in other colors
            "DoreenX.Over == 'towel'", "images/DoreenSprite/Doreen_Sprite_Pierce_Tits_B_Green.png", #change if new tops added in other colors
            "DoreenX.Over == 'sweater'", "images/DoreenSprite/Doreen_Sprite_Pierce_Tits_B_Sweater.png", #change if new tops added in other colors

            "DoreenX.Chest == 'lace bra'", "images/DoreenSprite/Doreen_Sprite_Pierce_Tits_B_Lace.png",
            "DoreenX.Chest == 'bikini top' or DoreenX.Chest == 'sports bra'", "images/DoreenSprite/Doreen_Sprite_Pierce_Tits_B_Green.png",
            "DoreenX.Chest", "images/DoreenSprite/Doreen_Sprite_Pierce_Tits_B_Tan.png",

            "True", "images/DoreenSprite/Doreen_Sprite_Pierce_Tits_B.png",
            ),

        (0,0), ConditionSwitch(
            #Boots/Shoes
            "DoreenX.Boots == 'boots'", "images/DoreenSprite/Doreen_Sprite_Boots.png",
            "DoreenX.Boots == 'sneaks'", "images/DoreenSprite/Doreen_Sprite_Boots_Sneaks.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #jacket over
            "DoreenX.Uptop and DoreenX.Acc == 'vest'", "images/DoreenSprite/Doreen_Sprite_Vest_Over_Up.png",         # right hand up/left down
            "DoreenX.Acc == 'vest'", "images/DoreenSprite/Doreen_Sprite_Vest_Over.png",         # right hand up/left down
            "DoreenX.Uptop and DoreenX.ArmPose != 1 and DoreenX.Acc == 'jacket'", "images/DoreenSprite/Doreen_Sprite_Jacket_Over2_Up.png",         # right hand up/left down
            "DoreenX.Uptop and DoreenX.Acc == 'jacket'", "images/DoreenSprite/Doreen_Sprite_Jacket_Over1_Up.png",         # right hand up/left down
            "DoreenX.ArmPose != 1 and DoreenX.Acc == 'jacket'", "images/DoreenSprite/Doreen_Sprite_Jacket_Over2.png",         # right hand up/left down
            "DoreenX.Acc == 'jacket'", "images/DoreenSprite/Doreen_Sprite_Jacket_Over1.png",         # right hand up/left down
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #arms top
            "renpy.showing('Doreen_HJ_Animation')",Null(),
            "DoreenX.ArmPose != 1", "images/DoreenSprite/[DoreenX.skin_image.skin_path]Doreen_Sprite_Arm2.png",         # right hand up/left down
            "True", "images/DoreenSprite/[DoreenX.skin_image.skin_path]Doreen_Sprite_Arm1.png", #if DoreenX.Arms == 1   # right Hand on hip/left raised
            ),

#        (0,0), ConditionSwitch(
#            #Water effect
#            "DoreenX.Water", "images/DoreenSprite/Doreen_Sprite_Water2.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #belly spunk
            "'belly' in DoreenX.Spunk and Player.Male", "images/DoreenSprite/Doreen_Sprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast spunk
            "'tits' in DoreenX.Spunk and Player.Male", "images/DoreenSprite/Doreen_Sprite_Spunk_Tits.png",
            "True", Null(),
            ),

        (95,20), "Doreen_Sprite_Head", #(-10,-90)


#        (0,0), "images/DoreenSprite/Doreen_Sprite_Headref.png", #53,-45


#        (0,0), ConditionSwitch(
#            #hand spunk
#            "DoreenX.ArmPose == 2 or 'hand' not in DoreenX.Spunk", Null(),
#            "True", "images/DoreenSprite/Doreen_Sprite_Spunk_Hand.png",
#            ),
#        (0,0), ConditionSwitch(                                                                         #Props
#            "not DoreenX.Held or DoreenX.ArmPose != 2", Null(),
#            "DoreenX.ArmPose == 2 and DoreenX.Held == 'phone'", "images/DoreenSprite/Doreen_held_phone.png",
#            "DoreenX.ArmPose == 2 and DoreenX.Held == 'dildo'", "images/DoreenSprite/Doreen_held_dildo.png",
#            "DoreenX.ArmPose == 2 and DoreenX.Held == 'vibrator'", "images/DoreenSprite/Doreen_held_vibrator.png",
#            "DoreenX.ArmPose == 2 and DoreenX.Held == 'panties'", "images/DoreenSprite/Doreen_held_panties.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #UI tool for When Rogue is masturbating using RogueX.Offhand actions while lead
            "Trigger == 'lesbian' or not DoreenX.Offhand",Null(),# or Ch_Focus is not DoreenX", Null(),
            "DoreenX.Offhand == 'fondle pussy' and Trigger != 'sex' and DoreenX.Lust >= 70", "GirlFingerPussy_Doreen",
            "DoreenX.Offhand == 'fondle pussy'", "GirlGropePussy_Doreen",
            "DoreenX.Offhand == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeLeftBreast_Doreen",    #When zero is working the right breast, fondle left
            "DoreenX.Offhand == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeRightBreast_Doreen", #When zero is working the left breast, fondle right
            "DoreenX.Offhand == 'fondle breasts'", "GirlGropeRightBreast_Doreen",
            "DoreenX.Offhand == 'vibrator breasts'", "VibratorRightBreast_Doreen",
            "DoreenX.Offhand == 'vibrator pussy'", "VibratorPussy_Doreen",
            "DoreenX.Offhand == 'vibrator pussy insert'", "VibratorPussy_Doreen",
            "DoreenX.Offhand == 'vibrator anal'", "VibratorAnal_Doreen",
            "DoreenX.Offhand == 'vibrator anal insert'", "VibratorPussy_Doreen",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #UI tool for RogueX.Offhand(lesbian) actions (ie Kitty's hand on her when Rogue is secondary)
            "not Partner or Partner is DoreenX or DoreenX in Nearby", Null(),
            "Partner.Offhand == 'fondle girl pussy' and Trigger != 'sex' and DoreenX.Lust >= 70", "GirlFingerPussy_Doreen",
            "Partner.Offhand == 'fondle girl pussy'", "GirlGropePussy_Doreen",
            "Partner.Offhand == 'lick girl pussy'", "Lickpussy_Doreen",
            "Partner.Offhand == 'suck girl breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Doreen",
            "Partner.Offhand == 'suck girl breasts'", "LickRightBreast",
            "Partner.Offhand == 'fondle girl breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Doreen",    #When zero is working the right breast, fondle left
            "Partner.Offhand == 'fondle girl breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Doreen", #When zero is working the left breast, fondle right
            "Partner.Offhand == 'fondle girl breasts'", "GirlGropeRightBreast_Doreen",
            "Partner.Offhand == 'vibrator girl breasts'", "VibratorRightBreast_Doreen",
            "Partner.Offhand == 'vibrator girl pussy'", "VibratorPussy_Doreen",
            "Partner.Offhand == 'vibrator girl pussy insert'", "VibratorPussy_Doreen",
            "Partner.Offhand == 'vibrator girl anal'", "VibratorAnal_Doreen",
            "Partner.Offhand == 'vibrator girl anal insert'", "VibratorPussy_Doreen",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for when RogueX is the partner in the scene, and the lead is working on her
            "not Partner or Partner is not DoreenX", Null(),
            "Ch_Focus.Offhand == 'fondle girl pussy' and Trigger != 'sex' and DoreenX.Lust >= 70", "GirlFingerPussy_Doreen",
            "Ch_Focus.Offhand == 'fondle girl pussy'", "GirlGropePussy_Doreen",
            "Ch_Focus.Offhand == 'lick girl pussy'", "Lickpussy_Doreen",
            "Ch_Focus.Offhand == 'suck girl breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Doreen",
            "Ch_Focus.Offhand == 'suck girl breasts'", "LickRightBreast",
            "Ch_Focus.Offhand == 'fondle girl breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Doreen",    #When zero is working the right breast, fondle left
            "Ch_Focus.Offhand == 'fondle girl breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Doreen", #When zero is working the left breast, fondle right
            "Ch_Focus.Offhand == 'fondle girl breasts'", "GirlGropeRightBreast_Doreen",
            "Ch_Focus.Offhand == 'vibrator girl breasts'", "VibratorRightBreast_Doreen",
            "Ch_Focus.Offhand == 'vibrator girl pussy'", "VibratorPussy_Doreen",
            "Ch_Focus.Offhand == 'vibrator girl pussy insert'", "VibratorPussy_Doreen",
            "Ch_Focus.Offhand == 'vibrator girl anal'", "VibratorAnal_Doreen",
            "Ch_Focus.Offhand == 'vibrator girl anal insert'", "VibratorPussy_Doreen",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger1(primary) actions
            "not Trigger or Ch_Focus is not DoreenX", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast_Doreen",
            "Trigger == 'fondle thighs'", "GropeThigh_Doreen",
            "Trigger == 'fondle breasts'", "GropeLeftBreast_Doreen",
            "Trigger == 'suck breasts'", "LickRightBreast_Doreen",
            "Trigger == 'vibrator pussy'", "VibratorPussy_Doreen",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy_Doreen",
            "Trigger == 'vibrator anal'", "VibratorAnal_Doreen",
            "Trigger == 'vibrator anal insert'", "VibratorPussy_Doreen",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_Doreen",
            "Trigger == 'fondle pussy'", "GropePussy_Doreen",
            "Trigger == 'lick pussy'", "Lickpussy_Doreen",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus is not DoreenX", Null(),
#            "Trigger == 'fondle breasts' and not DoreenX.Offhand", "GropeRightBreast_Doreen",  #"Trigger == 'fondle breasts' and not RogueX.Offhand",
            #When doing nothing offhand, use both hands on breasts.
            "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast_Doreen",
            #When sucking right breast, fondle left
            "Trigger2 == 'fondle breasts'", "GropeLeftBreast_Doreen",
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast_Doreen",
            #When sucking right breast, vibrator left
            "Trigger2 == Trigger", Null(),
            #When both triggers are the same, do nothing
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast_Doreen",
            "Trigger2 == 'suck breasts'", "LickLeftBreast_Doreen",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy_Doreen",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy_Doreen",
            "Trigger2 == 'vibrator anal'", "VibratorAnal_Doreen",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy_Doreen",
            "Trigger2 == 'fondle pussy'", "GropePussy_Doreen",
            "Trigger2 == 'lick pussy'", "Lickpussy_Doreen",
            "Trigger2 == 'fondle thighs'", "GropeThigh_Doreen",
            "True", Null(),
            ),

        )
    anchor (0.5, 0.0)
    offset (40,0)
    zoom .80  #.75


image Doreen_Sprite_HairBack:
    LiveComposite(
        (820,820),
        (0,0), ConditionSwitch(
                #hair back
    #            "renpy.showing('Doreen_BJ_Animation')", Null(),
    #            "renpy.showing('Doreen_SexSprite')", "images/DoreenSex/Doreen_Sprite_Hair_Long_UnderSex.png",
                "DoreenX.Hair == 'wetlong' or (DoreenX.Hair == 'long' and DoreenX.Water)", "images/DoreenSprite/Doreen_Sprite_Hair_Long_Wet_Back.png",
                "DoreenX.Hair == 'long' and (not Player.Male and 'facial' in DoreenX.Spunk)","images/DoreenSprite/Doreen_Sprite_Hair_Long_Wet_Back.png",
                "DoreenX.Hair == 'wet' or DoreenX.Water", "images/DoreenSprite/Doreen_Sprite_Hair_Short_Wet_Back.png",
                "not Player.Male and 'facial' in DoreenX.Spunk","images/DoreenSprite/Doreen_Sprite_Hair_Short_Wet_Back.png",
                "DoreenX.Hair == 'long'", "images/DoreenSprite/Doreen_Sprite_Hair_Long_Back.png",
                "True", "images/DoreenSprite/Doreen_Sprite_Hair_Short_Back.png",
                ),
        )
    anchor (0.5, 0.5)
    zoom .50#.47
    transform_anchor True
#    rotate -10


image Doreen_Sprite_Head:
    LiveComposite(
        (820,820),
        (0,0), ConditionSwitch(
                # Face background plate
#                "renpy.showing('Doreen_SexSprite') and DoreenX.Blush >= 2", "images/DoreenSprite/Doreen_Sprite_Head_Sex_Blush2.png",
#                "renpy.showing('Doreen_SexSprite') and DoreenX.Blush", "images/DoreenSprite/Doreen_Sprite_Head_Sex_Blush1.png",
#                "renpy.showing('Doreen_SexSprite')", "images/DoreenSprite/Doreen_Sprite_Head_Sex.png",
                "DoreenX.Blush >= 2", "images/DoreenSprite/[DoreenX.skin_image.skin_path]Doreen_Sprite_Head_Blush2.png",
                "DoreenX.Blush", "images/DoreenSprite/[DoreenX.skin_image.skin_path]Doreen_Sprite_Head_Blush1.png",
                "True", "images/DoreenSprite/[DoreenX.skin_image.skin_path]Doreen_Sprite_Head.png",
                ),
        (0,0), ConditionSwitch(
            #chin spunk
            "'chin' in DoreenX.Spunk and Player.Male", "images/DoreenSprite/Doreen_Sprite_Spunk_Chin.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Mouths
            "DoreenX.Mouth == 'lipbite'", "images/DoreenSprite/Doreen_Sprite_Mouth_Lipbite.png",
            "DoreenX.Mouth == 'sucking'", "images/DoreenSprite/Doreen_Sprite_Mouth_Shocked.png",
            "DoreenX.Mouth == 'kiss'", "images/DoreenSprite/Doreen_Sprite_Mouth_Kiss.png",
            "DoreenX.Mouth == 'sad'", "images/DoreenSprite/Doreen_Sprite_Mouth_Sad.png",
            "DoreenX.Mouth == 'smile'", "images/DoreenSprite/Doreen_Sprite_Mouth_Smile.png",
            "DoreenX.Mouth == 'surprised'", "images/DoreenSprite/Doreen_Sprite_Mouth_Open.png",
#            "not Player.Male and 'mouth' in DoreenX.Spunk and DoreenX.Mouth == 'tongue'", "images/DoreenSprite/Doreen_Sprite_Mouth_Tongue_Wet.png",
            "DoreenX.Mouth == 'tongue'", "images/DoreenSprite/Doreen_Sprite_Mouth_Tongue.png",
            "DoreenX.Mouth == 'grimace'", "images/DoreenSprite/Doreen_Sprite_Mouth_Smile.png",
            "DoreenX.Mouth == 'smirk'", "images/DoreenSprite/Doreen_Sprite_Mouth_Smirk.png",
            "DoreenX.Mouth == 'open'", "images/DoreenSprite/Doreen_Sprite_Mouth_Open.png",
            "True", "images/DoreenSprite/Doreen_Sprite_Mouth_Smirk.png",
            ),
        (0,0), ConditionSwitch(
            #Mouths spunk
            "'mouth' not in DoreenX.Spunk or not Player.Male", Null(),
            "DoreenX.Mouth == 'sucking'", "images/DoreenSprite/Doreen_Sprite_Spunk_Open.png",
            "DoreenX.Mouth == 'kiss'", "images/DoreenSprite/Doreen_Sprite_Spunk_Kiss.png",
            "DoreenX.Mouth == 'sad'", "images/DoreenSprite/Doreen_Sprite_Spunk_Sad.png",
            "DoreenX.Mouth == 'smirk'", "images/DoreenSprite/Doreen_Sprite_Spunk_Sad.png",
            "DoreenX.Mouth == 'lipbite'", "images/DoreenSprite/Doreen_Sprite_Spunk_Sad.png",
            "DoreenX.Mouth == 'surprised'", "images/DoreenSprite/Doreen_Sprite_Spunk_Open.png",
            "DoreenX.Mouth == 'open'", "images/DoreenSprite/Doreen_Sprite_Spunk_Open.png",
            "DoreenX.Mouth == 'tongue'", "images/DoreenSprite/Doreen_Sprite_Spunk_Tongue.png",
            "True", "images/DoreenSprite/Doreen_Sprite_Spunk_Sad.png",
            ),
        (0,0), ConditionSwitch(
            #wet face
            "Player.Male", Null(),
            "'mouth' not in DoreenX.Spunk and 'chin' not in DoreenX.Spunk", Null(),
            "DoreenX.Mouth == 'tongue'", "images/DoreenSprite/Doreen_Sprite_Wet_Tongue.png",
            "'chin' in DoreenX.Spunk", "images/DoreenSprite/Doreen_Sprite_Wet_Mouth.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(     #    (0,5)
            #brows
            "DoreenX.Brows == 'angry'", "images/DoreenSprite/[DoreenX.skin_image.skin_path]Doreen_Sprite_Brows_Angry.png",
            "DoreenX.Brows == 'sad'", "images/DoreenSprite/[DoreenX.skin_image.skin_path]Doreen_Sprite_Brows_Sad.png",
            "DoreenX.Brows == 'surprised'", "images/DoreenSprite/[DoreenX.skin_image.skin_path]Doreen_Sprite_Brows_Surprised.png",
            "DoreenX.Brows == 'confused'", "images/DoreenSprite/[DoreenX.skin_image.skin_path]Doreen_Sprite_Brows_Confused.png",
            "True", "images/DoreenSprite/[DoreenX.skin_image.skin_path]Doreen_Sprite_Brows_Normal.png",
            ),
        (0,0), "Doreen Blink",     #Eyes  (0,5)
        (0,0), ConditionSwitch(
                #hair over
    #            "renpy.showing('Doreen_BJ_Animation')", Null(),
    #            "renpy.showing('Doreen_SexSprite')", "images/DoreenSex/Doreen_Sprite_Hair_Long_UnderSex.png",
                "DoreenX.Hair == 'wet' or DoreenX.Hair == 'wetlong' or DoreenX.Water", "images/DoreenSprite/Doreen_Sprite_Hair_Short_Wet.png",
                "not Player.Male and 'facial' in DoreenX.Spunk","images/DoreenSprite/Doreen_Sprite_Hair_Short_Wet.png",
                "True", "images/DoreenSprite/Doreen_Sprite_Hair_Short.png",
                ),
        (0,0), ConditionSwitch(
                #hairband
    #            "renpy.showing('Doreen_BJ_Animation')", Null(),
    #            "renpy.showing('Doreen_SexSprite')", "images/DoreenSex/Doreen_Sprite_Hair_Long_UnderSex.png",
                "not DoreenX.Hat",Null(),
                "DoreenX.Hat == 'glasses'","images/DoreenSprite/Doreen_Sprite_Glasses.png",
                "DoreenX.Hair == 'wet' or DoreenX.Hair == 'wetlong' or DoreenX.Water", "images/DoreenSprite/Doreen_Sprite_Headband_Wet.png",
                "not Player.Male and 'facial' in DoreenX.Spunk","images/DoreenSprite/Doreen_Sprite_Headband_Wet.png",
                "True", "images/DoreenSprite/Doreen_Sprite_Headband.png",
                ),

        (0,0), "images/DoreenSprite/Doreen_Sprite_Earring.png",     #Eyes  (0,5)
        (0,0), ConditionSwitch(
            #Hair Water
            "DoreenX.Water", "images/DoreenSprite/Doreen_Sprite_Wet_Face.png",
            "not Player.Male and 'facial' in DoreenX.Spunk", "images/DoreenSprite/Doreen_Sprite_Wet_Face.png",
            "True",Null(),
            ),
        (0,0), ConditionSwitch(
            #facial spunk
            "'hair' in DoreenX.Spunk and Player.Male", "images/DoreenSprite/Doreen_Sprite_Spunk_Hair.png",
            "'facial' in DoreenX.Spunk and Player.Male", "images/DoreenSprite/Doreen_Sprite_Spunk_Facial.png",
            "True", Null(),
            ),
        # Modification mode
        (0,0), ConditionSwitch(
            #facial fix
            "DoreenX.Fix", "images/DoreenSprite/modification/Doreen_Sprite_Head_Fix.png",
            "True", Null(),
            ),
        # -----------------
        )
    anchor (0.5, 0.5)
    zoom .50#.45
    transform_anchor True
#    rotate -10
#    alpha 0.9

image Doreen Blink:
    ConditionSwitch(
    "DoreenX.Eyes == 'closed'", "images/DoreenSprite/Doreen_Sprite_Eyes_Closed.png",
    "DoreenX.Eyes == 'sexy'", "images/DoreenSprite/Doreen_Sprite_Eyes_Sexy.png",
    "DoreenX.Eyes == 'side'", "images/DoreenSprite/Doreen_Sprite_Eyes_Side.png",
    "DoreenX.Eyes == 'surprised'", "images/DoreenSprite/Doreen_Sprite_Eyes_Surprised.png",
    "DoreenX.Eyes == 'normal'", "images/DoreenSprite/Doreen_Sprite_Eyes_Normal.png",
    "DoreenX.Eyes == 'stunned'", "images/DoreenSprite/Doreen_Sprite_Eyes_Stunned.png",
    "DoreenX.Eyes == 'down'", "images/DoreenSprite/Doreen_Sprite_Eyes_Down.png",
    "DoreenX.Eyes == 'leftside'", "images/DoreenSprite/Doreen_Sprite_Eyes_Leftside.png",
    "DoreenX.Eyes == 'manic'", "images/DoreenSprite/Doreen_Sprite_Eyes_Sexy.png",#"images/DoreenSprite/Doreen_Sprite_Eyes_Squint.png",
    "DoreenX.Eyes == 'squint'", "images/DoreenSprite/Doreen_Sprite_Eyes_Sexy.png",#"Doreen_Squint",
    "True", "images/DoreenSprite/Doreen_Sprite_Eyes_Normal.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/DoreenSprite/Doreen_Sprite_Eyes_Closed.png"
    .25
    repeat

##image Doreen_Squint:
##    "images/DoreenSprite/Doreen_Sprite_Eyes_Sexy.png"
##    choice:
##        3.5
##    choice:
##        3.25
##    choice:
##        3
##    "images/DoreenSprite/Doreen_Sprite_Eyes_Squint.png"
##    .25
##    repeat


##image Doreen_Drip_Mask:
##    #This is the mask for her drip pattern
##    contains:
##        "images/DoreenSprite/Doreen_Sprite_WetMask.png"
##        offset (-275,-560)#(-145,-15)#(-212,-4834)

##image Doreen_Drip_MaskPanties:
##    #This is the mask for her drip pattern in panties down mode
##    contains:
##        "images/DoreenSprite/Doreen_Sprite_DripMaskPanties.png"
##        offset (-145,-560)#(-225,-560)

##image Doreen_Drip_MaskP:
##    #This is the mask for her drip pattern in panties down mode
##    contains:
##        "images/DoreenSprite/Doreen_Sprite_WetMask_Pants.png"
##        offset (-275,-560)#(-145,-560)

## End Doreen Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Doreen Doggy Compositing ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#image Doreen_Doggy_Base = LiveComposite(
image Doreen_Doggy_Animation: #nee Doreen_Doggy
    LiveComposite(
        #Base body
        (420,750),
        (0,0), ConditionSwitch(
            #Shows different upper body motion depending on events
            "not Player.Sprite", "Doreen_Doggy_Body",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Doreen_Doggy_Fuck2_Top",
                    "Speed > 1", "Doreen_Doggy_Fuck_Top",
                    "Speed", "Doreen_Doggy_Anal_Head_Top",
                    "True", "Doreen_Doggy_Body",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Doreen_Doggy_Fuck2_Top",
                    "Speed > 1", "Doreen_Doggy_Fuck_Top",
                    "True", "Doreen_Doggy_Body",
                    ),
            "Player.Cock == 'foot'", ConditionSwitch(
                    "Speed > 1", "Doreen_Doggy_Foot2_Top",
                    "Speed", "Doreen_Doggy_Foot1_Top",
                    "True", "Doreen_Doggy_Foot0_Top",
                    ),
            "True", "Doreen_Doggy_Body",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events
            "not Player.Sprite", "Doreen_Doggy_Ass",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Doreen_Doggy_Fuck2_Ass",
                    "Speed > 1", "Doreen_Doggy_Fuck_Ass",
                    "Speed", "Doreen_Doggy_Anal_Head_Ass",
                    "True", "Doreen_Doggy_Ass",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Doreen_Doggy_Fuck2_Ass",
                    "Speed > 1", "Doreen_Doggy_Fuck_Ass",
                    "True", "Doreen_Doggy_Ass",
                    ),
            "Player.Cock == 'foot'", ConditionSwitch(
                    "Speed > 1", "Doreen_Doggy_Foot2_Ass",
                    "Speed", "Doreen_Doggy_Foot1_Ass",
                    "True", "Doreen_Doggy_Foot0_Ass",
                    ),
            "True", "Doreen_Doggy_Ass",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
#            "not Player.Sprite", "Doreen_Doggy_Shins0",
            "Player.Sprite and Player.Cock == 'foot'", ConditionSwitch(
                    "Speed > 1", "Doreen_Doggy_Feet2",
                    "Speed", "Doreen_Doggy_Feet1",
                    "True", "Doreen_Doggy_Feet0",
                    ),
            "ShowFeet", "Doreen_Doggy_Shins0",# "not Player.Sprite and ShowFeet", "Doreen_Doggy_Shins",
            "True", Null(),
            ),
        )
    align (0.6,0.0)
    #yoffset 50
# End Base / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Doreen_Doggy_Body:
    LiveComposite(
        #Upper body
        (610,750),
        #(165,0),"Doreen_Doggy_Hair_Under", #back of the hair
#        (0,60), "Doreen_Doggy_Head",               #Head

#        (0,0), "images/DoreenDoggy/Doreen_Doggy_HeadRef.png",               #Head
        (0,127), ConditionSwitch(
            #head
            "DoreenX.Facing", "Doreen_Doggy_Head_Fore",
            "True", "Doreen_Doggy_Head",
            ),

        (0,0), "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Body.png", #Body base
        (0,0), ConditionSwitch(
            #bra
            "not DoreenX.Chest", Null(),
#            "DoreenX.Uptop", ConditionSwitch(
#                    "DoreenX.Chest == 'lace bra'", "images/DoreenDoggy/Doreen_Doggy_Chest_Lace_Up.png",
#                    "DoreenX.Chest == 'sports bra'", "images/DoreenDoggy/Doreen_Doggy_Chest_Sport_Up.png",
#                    "DoreenX.Chest == 'bikini top'", "images/DoreenDoggy/Doreen_Doggy_Chest_Bikini_Up.png",
#                    "True", "images/DoreenDoggy/Doreen_Doggy_Chest_Bra_Up.png",
#                    ),
            "DoreenX.Chest == 'lace bra'", "images/DoreenDoggy/Doreen_Doggy_Chest_Lace.png",
            "DoreenX.Chest == 'sports bra'", "images/DoreenDoggy/Doreen_Doggy_Chest_Sports.png",
            "DoreenX.Chest == 'bikini top'", "images/DoreenDoggy/Doreen_Doggy_Chest_Bikini.png",
            "True", "images/DoreenDoggy/Doreen_Doggy_Chest_Bra.png",
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "DoreenX.Water", "images/DoreenDoggy/Doreen_Doggy_Water_Body.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Overshirt
            "not DoreenX.Over", Null(),
            "DoreenX.Over == 'tshirt'", "images/DoreenDoggy/Doreen_Doggy_Over_TShirt.png",
            "DoreenX.Over == 'sweater'", "images/DoreenDoggy/Doreen_Doggy_Over_Sweater.png",
            "DoreenX.Over == 'tube top'", "images/DoreenDoggy/Doreen_Doggy_Over_Tube.png",
            "DoreenX.Over == 'towel'", "images/DoreenDoggy/Doreen_Doggy_Over_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #jacket
            "DoreenX.Acc == 'jacket'", "images/DoreenDoggy/Doreen_Doggy_Jacket.png",
            "DoreenX.Acc == 'vest'", "images/DoreenDoggy/Doreen_Doggy_Vest.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #long Hair
            "DoreenX.Hair != 'long' and DoreenX.Hair != 'wetlong'", Null(),
            "DoreenX.Facing", ConditionSwitch(
                    "DoreenX.Water or DoreenX.Hair == 'wetlong'", "images/DoreenDoggy/Doreen_Doggy_Hair_Long_Wet_Fore.png",
                    "not Player.Male and 'facial' in DoreenX.Spunk","images/DoreenDoggy/Doreen_Doggy_Hair_Long_Wet_Fore.png",
                    "True", "images/DoreenDoggy/Doreen_Doggy_Hair_Long_Fore.png",
                    ),
            "DoreenX.Water or DoreenX.Hair == 'wetlong'", "images/DoreenDoggy/Doreen_Doggy_Hair_Long_Wet.png",
            "not Player.Male and 'facial' in DoreenX.Spunk","images/DoreenDoggy/Doreen_Doggy_Hair_Long_Wet.png",
            "True", "images/DoreenDoggy/Doreen_Doggy_Hair_Long.png",
            ),
        (0,0), ConditionSwitch(             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #spunk back Layer
            "'back' in DoreenX.Spunk and Player.Male", "images/DoreenDoggy/Doreen_Doggy_Spunk_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast fondling animation
            "Trigger == 'fondle breasts' or Trigger2 == 'fondle breasts'", "Doreen_Doggy_GropeBreast",
            "True", Null()
            ),
        #(161,-1), "Doreen_Doggy_Head",               #Head
        #(165,0),"Doreen_Doggy_Hair_Over", #front of the hair
        )
#    zoom 2
#    transform_anchor True
#    anchor (225,1400)
#    offset (-175,25)#(-200,0)
#    offset (0,25)#(-200,0)
#    zoom .95
#    offset (-350,-180)#(-190,-40)
#    rotate 20
# End Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Doreen_Doggy_Head:
    LiveComposite(
        #Head
        (420,525),
        #(0,0), "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Head.png", #Body base
        #(0,0), "images/DoreenDoggy/Doreen_Doggy_TestArm.png",#Eyes
#        (0,0), ConditionSwitch(
#            #Hair back
#            "DoreenX.Water or DoreenX.Hair == 'wet'", "images/DoreenDoggy/Doreen_Doggy_Hair_Wet_Back.png",
#            "not Player.Male and 'facial' in DoreenX.Spunk","images/DoreenDoggy/Doreen_Doggy_Hair_Wet_Back.png",
#            "DoreenX.Hair == 'pony'", Null(),
#            "True", "images/DoreenDoggy/Doreen_Doggy_Hair_Short_Back.png",
#            ),
        (0,0), ConditionSwitch(
            #Head
            #"DoreenX.Blush > 1", "images/DoreenDoggy/Doreen_Doggy_Head_Blush2.png",
            "DoreenX.Blush", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Head_Blush.png",
            "True", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Head.png",
            ),
        (0,0), ConditionSwitch(
            #Mouth
            "DoreenX.Mouth == 'normal'", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Mouth_Normal.png",
            "DoreenX.Mouth == 'lipbite'", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Mouth_Normal.png",
            "DoreenX.Mouth == 'sucking'", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Mouth_Open.png",
            "DoreenX.Mouth == 'kiss'", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Mouth_Sad.png",
            "DoreenX.Mouth == 'sad'", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Mouth_Sad.png",
            "DoreenX.Mouth == 'smile'", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Mouth_Open.png",
            "DoreenX.Mouth == 'grimace'", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Mouth_Open.png",
            "DoreenX.Mouth == 'surprised'", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Mouth_Open.png",
            "DoreenX.Mouth == 'tongue'", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Mouth_Tongue.png",
            "True", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Mouth_Normal.png",
            ),
#        (0,0), ConditionSwitch(
#            #chin spunk
#            "'chin' in DoreenX.Spunk", "images/DoreenDoggy/Doreen_Doggy_Spunk_Chin.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Mouth spunk
            "'mouth' not in DoreenX.Spunk", Null(),
#            #"DoreenX.Mouth == 'normal'", "images/DoreenDoggy/Doreen_Doggy_Spunk_Normal.png",
#            #"DoreenX.Mouth == 'sad'", "images/DoreenDoggy/Doreen_Doggy_Spunk_Normal.png",
#            "DoreenX.Mouth == 'lipbite'", "images/DoreenDoggy/Doreen_Doggy_Spunk_Sad.png",
#            "DoreenX.Mouth == 'smile'", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Mouth_Open.png",
#            "DoreenX.Mouth == 'grimace'", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Mouth_Open.png",
#            "DoreenX.Mouth == 'sucking'", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Mouth_Open.png",
#            #"DoreenX.Mouth == 'kiss'", "images/DoreenDoggy/Doreen_Doggy_Spunk_Open.png",
#            "DoreenX.Mouth == 'surprised'", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Mouth_Open.png",
#            "DoreenX.Mouth == 'tongue'", "images/DoreenDoggy/Doreen_Doggy_Spunk_Smile.png",
            "True", "images/DoreenDoggy/Doreen_Doggy_Spunk_Mouth.png",
            ),
        (0,0), ConditionSwitch(
            #Brows
            #"DoreenX.Brows == 'normal'", "images/DoreenDoggy/Doreen_Doggy_Brows_Normal.png",
            "DoreenX.Brows == 'angry'", "images/DoreenDoggy/Doreen_Doggy_Brows_Angry.png",
            "DoreenX.Brows == 'sad'", "images/DoreenDoggy/Doreen_Doggy_Brows_Sad.png",
            "DoreenX.Brows == 'surprised'", "images/DoreenDoggy/Doreen_Doggy_Brows_Surprised.png",
            #"DoreenX.Brows == 'confused'", "images/DoreenDoggy/Doreen_Doggy_Brows_Normal.png",
            "True", "images/DoreenDoggy/Doreen_Doggy_Brows_Normal.png",
            ),
        (0,0), "Doreen Doggy Blink",#Eyes
#        (0,0), ConditionSwitch(
#            #Wet look
#            "DoreenX.Water", "images/RogueDoggy/Rogue_Doggy_WetTop.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #suit collar
            "DoreenX.Chest == 'sports bra'", "images/DoreenDoggy/Doreen_Doggy_Head_Sport.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #face spunk
            "'facial' in DoreenX.Spunk and Player.Male", "images/DoreenDoggy/Doreen_Doggy_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hair
            "DoreenX.Water or DoreenX.Hair == 'wet' or DoreenX.Hair == 'wetlong'", "images/DoreenDoggy/Doreen_Doggy_Hair_Wet.png",
            "not Player.Male and 'facial' in DoreenX.Spunk","images/DoreenDoggy/Doreen_Doggy_Hair_Wet.png",
            "True", "images/DoreenDoggy/Doreen_Doggy_Hair_Short.png",
            ),
        (0,0), ConditionSwitch(
            #headband
            "not DoreenX.Hat", Null(),
            "DoreenX.Hat == 'glasses'","images/DoreenDoggy/Doreen_Doggy_Glasses.png",
            "DoreenX.Water or DoreenX.Hair == 'wet' or DoreenX.Hair == 'wetlong'", "images/DoreenDoggy/Doreen_Doggy_Headband_Wet.png",
            "not Player.Male and 'facial' in DoreenX.Spunk","images/DoreenDoggy/Doreen_Doggy_Headband_Wet.png",
            "True", "images/DoreenDoggy/Doreen_Doggy_Headband_Short.png",
            ),
        (0,0), ConditionSwitch(
            #face spunk
            "'hair' in DoreenX.Spunk and Player.Male", "images/DoreenDoggy/Doreen_Doggy_Spunk_Hair.png",
#            "DoreenX.Water or DoreenX.Hair == 'wet'", "images/DoreenDoggy/Doreen_Doggy_Head_Wet.png",
#            "not Player.Male and 'facial' in DoreenX.Spunk","images/DoreenDoggy/Doreen_Doggy_Head_Wet.png",
            "True", Null(),
            ),
        )
    #zoom 0.95
    #alpha 0.5
# End Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen Doggy Blink:
        #Eyes
        ConditionSwitch(
        "DoreenX.Eyes == 'sexy'", "images/DoreenDoggy/Doreen_Doggy_Eyes_Sexy.png",
        "DoreenX.Eyes == 'side'", "images/DoreenDoggy/Doreen_Doggy_Eyes_Side.png",
#        "DoreenX.Eyes == 'normal'", "images/DoreenDoggy/Doreen_Doggy_Eyes_Normal.png",
        "DoreenX.Eyes == 'closed'", "images/DoreenDoggy/Doreen_Doggy_Eyes_Closed.png",
        "DoreenX.Eyes == 'manic'", "images/DoreenDoggy/Doreen_Doggy_Eyes_Stunned.png",
        "DoreenX.Eyes == 'down'", "images/DoreenDoggy/Doreen_Doggy_Eyes_Down.png",
        "DoreenX.Eyes == 'stunned'", "images/DoreenDoggy/Doreen_Doggy_Eyes_Stunned.png",
        "DoreenX.Eyes == 'surprised'", "images/DoreenDoggy/Doreen_Doggy_Eyes_Surprised.png",
        "DoreenX.Eyes == 'squint'", "images/DoreenDoggy/Doreen_Doggy_Eyes_Sexy.png",
        "True", "images/DoreenDoggy/Doreen_Doggy_Eyes_Normal.png",
        ),
    #    choice:
    #        3.5
    #    choice:
    #        3.25
    #    choice:
    #        3
        3
        # This randomizes the time between blinking.
        "images/DoreenDoggy/Doreen_Doggy_Eyes_Closed.png"
        .25
        repeat

# End Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_Doggy_Head_Fore:
    LiveComposite(
        #Head
        (420,525),
        (0,0), ConditionSwitch(
            #Hair
            "DoreenX.Water or DoreenX.Hair == 'wet' or DoreenX.Hair == 'wetlong'", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Hair_Wet_Fore.png",
            "not Player.Male and 'facial' in DoreenX.Spunk","images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Hair_Wet_Fore.png",
            "True", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Hair_Short_Fore.png",
            ),
        (0,0), ConditionSwitch(
            #headband
            "not DoreenX.Hat or DoreenX.Hat == 'glasses'", Null(),
            "DoreenX.Water or DoreenX.Hair == 'wet' or DoreenX.Hair == 'wetlong'", "images/DoreenDoggy/Doreen_Doggy_Headband_Wet_Fore.png",
            "not Player.Male and 'facial' in DoreenX.Spunk","images/DoreenDoggy/Doreen_Doggy_Headband_Wet_Fore.png",
            "True", "images/DoreenDoggy/Doreen_Doggy_Headband_Short_Fore.png",
            ),
        )
    #zoom 0.95
    #alpha 0.5
# End Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_Doggy_Ass:
    LiveComposite(
        #Lower body
        (420,750),
#        (0,0), ConditionSwitch(
#            #Legs backside
#            "DoreenX.Legs == 'skirt'","images/DoreenDoggy/Doreen_Doggy_Legs_Skirt_Back.png",
#            "not DoreenX.Upskirt", Null(),
#            "DoreenX.Legs == 'pants'", "images/DoreenDoggy/Doreen_Doggy_Legs_Pants_Back.png",
#            "DoreenX.Legs == 'yoga pants'", "images/DoreenDoggy/Doreen_Doggy_Legs_Yoga_Back.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #Panties back
#            "not DoreenX.PantiesDown or (DoreenX.Legs == 'pants' and not DoreenX.Upskirt)", Null(),
#            "DoreenX.Panties == 'wolvie panties'", "images/DoreenDoggy/Doreen_Doggy_Panties_Wolvie_Back.png",
#            "DoreenX.Panties == 'lace panties'", "images/DoreenDoggy/Doreen_Doggy_Panties_Lace_Back.png",
#            "DoreenX.Panties", "images/DoreenDoggy/Doreen_Doggy_Panties_Back.png",
#            "True", Null(),
#            ),
#        (0,0), "images/DoreenDoggy/Doreen_Doggy_Ass.png", #Ass Base


        (0,0), ConditionSwitch(
            #Pussy base
            "DoreenX.Legs and not DoreenX.Upskirt", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Ass_Closed.png",
            "DoreenX.Panties and not DoreenX.PantiesDown", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Ass_Closed.png",
            "Player.Sprite and Player.Cock == 'in'", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Ass_Fucking.png",
            "Trigger == 'lick pussy'", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Ass_Open.png",
            "'dildo pussy' in (Trigger,Trigger2,DoreenX.Offhand)", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Ass_Fucking.png",#Null(),
            "'fondle pussy' in (Trigger,Trigger2,DoreenX.Offhand)", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Ass_Fucking.png",#Null(),
            "Trigger == 'insert pussy'", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Ass_Fucking.png",#Null(),
            "True", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Ass_Closed.png",
            ),
        (0,0), ConditionSwitch(
            #Hotdogging plate
            "not Player.Sprite or Player.Cock != 'out'", Null(),
            "True", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Hotdog.png",
            ),
        (0,0), ConditionSwitch(
            #ass red
            "DoreenX.Red", "images/DoreenDoggy/Doreen_Doggy_Red.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Anus base
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    "Speed", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Anal_FullBase.png",      #Speed 1
                    "True", Null(),               #Speed 0
                    ),
            "'insert ass' in (Trigger,Trigger2,DoreenX.Offhand)", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Anal_FullBase.png",
            "'dildo anal' in (Trigger,Trigger2,DoreenX.Offhand)", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Anal_FullBase.png",
            "DoreenX.Loose > 2", "Doreen_Gape_Anal",    #intentional
            "DoreenX.Loose", "images/DoreenDoggy/Doreen_Doggy_Asshole_Loose.png",
            "True", "images/DoreenDoggy/Doreen_Doggy_Asshole_Tight.png",
            ),

        (0,0), ConditionSwitch(
            #Wet look
            "DoreenX.Water", "images/DoreenDoggy/Doreen_Doggy_Water_Ass.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #Hose
            "DoreenX.Hose == 'stockings'", "images/DoreenDoggy/Doreen_Doggy_Hose_Stockings.png",
#            "DoreenX.Hose == 'socks'", "images/DoreenDoggy/Doreen_Doggy_Hose_Socks.png",
#            "Player.Sprite and Player.Cock == 'in'", Null(),
#            "Player.Sprite and Player.Cock == 'anal'", Null(),
            "DoreenX.Hose == 'stockings and garterbelt'", "images/DoreenDoggy/Doreen_Doggy_Hose_StockingsGarter.png",
            "DoreenX.Hose == 'garterbelt'", "images/DoreenDoggy/Doreen_Doggy_Hose_Garter.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Panties if Down
            "not DoreenX.PantiesDown or (DoreenX.Legs == 'pants' and not DoreenX.Upskirt)", Null(),
            "DoreenX.Panties == 'lace panties'", "images/DoreenDoggy/Doreen_Doggy_Panties_Lace_Down.png",
            "DoreenX.Panties == 'bikini bottoms'", "images/DoreenDoggy/Doreen_Doggy_Panties_Bikini_Down.png",
            "DoreenX.Panties", "images/DoreenDoggy/Doreen_Doggy_Panties_Tan_Down.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunkpussy Layer
            "'in' in DoreenX.Spunk and Player.Cock == 'in' and Player.Male",Null(),# "images/DoreenDoggy/Doreen_Doggy_SpunkPussyOpen.png",  #fix for DoreenX.Spunk is used later
            "'in' in DoreenX.Spunk and Player.Male", "images/JeanDoggy/Jean_Doggy_SpunkPussyClosed.png",
            "DoreenX.Wet and Player.Cock == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "DoreenX.Wet", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pubes
            "not DoreenX.Pubes", Null(),
            "Player.Sprite and Player.Cock == 'in'", Null(), # "images/DoreenDoggy/Doreen_Doggy_Pubes_Fuckingucked.png",
            "'dildo pussy' in (Trigger,Trigger2,DoreenX.Offhand)", Null(),
            "'fondle pussy' in (Trigger,Trigger2,DoreenX.Offhand)",Null(),
            "Trigger == 'insert pussy'", Null(),
            "DoreenX.Legs == 'pants' and not DoreenX.Upskirt", "images/DoreenDoggy/Doreen_Doggy_Pubes_Clothed.png",
            "DoreenX.Legs == 'mesh pants' and not DoreenX.Upskirt", "images/DoreenDoggy/Doreen_Doggy_Pubes_Clothed.png",
            "DoreenX.PantiesDown and Trigger == 'lick pussy'", "images/DoreenDoggy/Doreen_Doggy_Pubes_Open.png",
            "DoreenX.PantiesDown", "images/DoreenDoggy/Doreen_Doggy_Pubes_Closed.png",
            "DoreenX.Panties", "images/DoreenDoggy/Doreen_Doggy_Pubes_Clothed.png",
            "DoreenX.Hose and DoreenX.Hose == 'pantyhose'", "images/DoreenDoggy/Doreen_Doggy_Pubes_Clothed.png",
            "Trigger == 'lick pussy'", "images/DoreenDoggy/Doreen_Doggy_Pubes_Open.png",
            "True", "images/DoreenDoggy/Doreen_Doggy_Pubes_Closed.png",
            ),
        (0,0), ConditionSwitch(
            #Pussy Piercings
            "Player.Sprite", Null(),
            "DoreenX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_Ring.png",
            "DoreenX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_Barbell.png",
            "True", Null(),
            ),


        (2,-8), ConditionSwitch(
            #spunkanal Layer
            "'anal' not in DoreenX.Spunk or (Player.Sprite and Player.Cock == 'anal' and Speed >= 1) or not Player.Male", Null(),
#            "Player.Cock == 'anal'", "images/DoreenDoggy/Doreen_Doggy_SpunkAnalOpen.png",
            "DoreenX.Loose", "images/JeanDoggy/Jean_Doggy_SpunkAnalLoose.png",
            "True", "images/JeanDoggy/Jean_Doggy_SpunkAnalLoose.png",
            ),
        (0,0), ConditionSwitch(
            #Panties if up
            "DoreenX.PantiesDown or not DoreenX.Panties", Null(),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),
            "DoreenX.Panties == 'lace panties'", "images/DoreenDoggy/Doreen_Doggy_Panties_Lace.png",
            "DoreenX.Panties == 'bikini bottoms'", "images/DoreenDoggy/Doreen_Doggy_Panties_Bikini.png",
            "DoreenX.Wet", "images/DoreenDoggy/Doreen_Doggy_Panties_Tan_Wet.png",
            "True", "images/DoreenDoggy/Doreen_Doggy_Panties_Tan.png",
            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #full hose/tights
            "DoreenX.Panties and DoreenX.PantiesDown", Null(),
            "DoreenX.Hose == 'ripped pantyhose'", "images/DoreenDoggy/Doreen_Doggy_Hose_Pantyhose_Holed.png",
            "DoreenX.Hose == 'ripped tights'", "images/DoreenDoggy/Doreen_Doggy_Hose_Tights_Holed.png",
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
            "DoreenX.Hose == 'pantyhose'", "images/DoreenDoggy/Doreen_Doggy_Hose_Pantyhose.png",
            "DoreenX.Hose == 'tights' and DoreenX.Wet", "images/DoreenDoggy/Doreen_Doggy_Hose_Tights_Wet.png",
            "DoreenX.Hose == 'tights'", "images/DoreenDoggy/Doreen_Doggy_Hose_Tights.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Legs Layer
            "DoreenX.Legs == 'skirt'", ConditionSwitch(
                    "Player.Sprite and Player.Cock == 'anal' and Speed" , "images/DoreenDoggy/Doreen_Doggy_Legs_Skirt_Up.png",   #Rogue_Doggy_Legs_Skirt_UpAnal.png",
                    "DoreenX.Upskirt", "images/DoreenDoggy/Doreen_Doggy_Legs_Skirt_Up.png",
                    "True", "images/DoreenDoggy/Doreen_Doggy_Legs_Skirt.png",
                    ),
            "DoreenX.Legs == 'red skirt'", ConditionSwitch(
                    "Player.Sprite and Player.Cock == 'anal' and Speed" , "images/DoreenDoggy/Doreen_Doggy_Legs_RedSkirt_Up.png",   #Rogue_Doggy_Legs_Skirt_UpAnal.png",
                    "DoreenX.Upskirt", "images/DoreenDoggy/Doreen_Doggy_Legs_RedSkirt_Up.png",
                    "True", "images/DoreenDoggy/Doreen_Doggy_Legs_RedSkirt.png",
                    ),
            "DoreenX.Legs == 'shorts'", ConditionSwitch(
                    "DoreenX.Upskirt or DoreenX.PantiesDown", "images/DoreenDoggy/Doreen_Doggy_Legs_Shorts_Down.png",
                    "DoreenX.Wet > 1", "images/DoreenDoggy/Doreen_Doggy_Legs_Shorts_Wet.png",
                    "True", "images/DoreenDoggy/Doreen_Doggy_Legs_Shorts.png",
                    ),
#            "DoreenX.Legs == 'yoga pants'", ConditionSwitch(
#                    "DoreenX.Upskirt", "images/DoreenDoggy/Doreen_Doggy_Legs_Yoga_Down.png",
#                    "DoreenX.Wet > 1", "images/DoreenDoggy/Doreen_Doggy_Legs_Yoga_Wet.png",
#                    "True", "images/DoreenDoggy/Doreen_Doggy_Legs_Yoga.png",
#                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #Over Layer
            "DoreenX.Over == 'towel' and DoreenX.Legs == 'skirt' and DoreenX.Upskirt", Null(),
            "DoreenX.Over == 'towel' and (DoreenX.Upskirt or DoreenX.Legs == 'skirt')", "images/DoreenDoggy/Doreen_Doggy_Legs_Skirt_Up.png",
            "DoreenX.Over == 'towel'", "images/DoreenDoggy/Doreen_Doggy_Legs_Towel.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Pussy Piercings clothed
#            "Player.Sprite", Null(),
#            "DoreenX.PantiesDown or (not DoreenX.Panties and DoreenX.Legs != 'leather pants')", Null(), #if not panties or legs, skip this
#            "DoreenX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_RingC.png",
#            "DoreenX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_BarbellC.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Pussy Composite
            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Doreen_Pussy_Fucking3",#Speed 3
                    "Speed > 1", "Doreen_Pussy_Fucking2",#Speed 2
                    "Speed", "Doreen_Pussy_Heading",      #Speed 1
                    "True", "Doreen_Pussy_Static",              #Speed 0
                    ),
            "DoreenX.Legs and not DoreenX.Upskirt",Null(),
            "DoreenX.Panties and not DoreenX.PantiesDown", Null(),
            "'dildo pussy' in (Trigger,Trigger2,DoreenX.Offhand)", "Doreen_Pussy_Fucking2",
            "'fondle pussy' in (Trigger,Trigger2,DoreenX.Offhand)", "Doreen_Pussy_Fingering",
            "Trigger == 'insert pussy'", "Doreen_Pussy_Fingering",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Anus Composite
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Doreen_Anal_Fucking2", #Speed 3
                    "Speed > 1", "Doreen_Anal_Fucking",  #Speed 2
                    "Speed", "Doreen_Anal_Heading",      #Speed 1
                    "True", "Doreen_Anal",               #Speed 0
                    ),
            "DoreenX.Legs and not DoreenX.Upskirt",Null(),
            "DoreenX.Panties and not DoreenX.PantiesDown", Null(),
            "'dildo anal' in (Trigger,Trigger2,DoreenX.Offhand)", "Doreen_Anal_Fucking",
            "'insert ass' in (Trigger,Trigger2,DoreenX.Offhand)", "Doreen_Anal_Fingering",
            "DoreenX.Plug", "images/PlugIn.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk back Layer
            "'back' in DoreenX.Spunk and Player.Male", "images/DoreenDoggy/Doreen_Doggy_Spunk_Ass.png",
            "True", Null(),
            ),
        (0,0), "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Hands.png", #Ass Base
        (0,0), ConditionSwitch(
            #tail
#            "DoreenX.Tail > 1", "images/DoreenDoggy/Doreen_Doggy_Tail2.png",
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),    #or Player.Cock == 'feet'?
            "'dildo anal' in (Trigger,Trigger2,DoreenX.Offhand)", Null(),
            "'dildo pussy' in (Trigger,Trigger2,DoreenX.Offhand)", Null(),
            "DoreenX.Tail and GhostTail", "images/DoreenDoggy/Doreen_Doggy_Tail3.png",
            "DoreenX.Tail", "images/DoreenDoggy/Doreen_Doggy_Tail.png",
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
#            "DoreenX.Over == 'towel'", Null(),
#            "(DoreenX.Legs == 'skirt' or DoreenX.Legs == 'other skirt') and DoreenX.Upskirt", "images/DoreenDoggy/Doreen_Doggy_Hotdog_Upskirt.png",
#            "True", "images/DoreenDoggy/Doreen_Doggy_HotdogBack.png",
#            ),
        (0,0), ConditionSwitch(
            #Hotdogging Cock w/ alpha
            "not Player.Sprite or Player.Cock != 'out'", Null(),
            "(DoreenX.Legs == 'skirt' or DoreenX.Legs == 'other skirt') and DoreenX.Upskirt and Speed", AlphaMask("Zero_Hotdog_Moving", "images/DoreenDoggy/Doreen_Doggy_HotdogMask.png"),
            "(DoreenX.Legs == 'skirt' or DoreenX.Legs == 'other skirt') and DoreenX.Upskirt", AlphaMask("Zero_Hotdog_Static", "images/DoreenDoggy/Doreen_Doggy_HotdogMask.png"),
            "Speed", AlphaMask("Zero_Hotdog_Moving", "images/DoreenDoggy/Doreen_Doggy_HotdogMask.png"),
            "True", AlphaMask("Zero_Hotdog_Static", "images/DoreenDoggy/Doreen_Doggy_HotdogMask.png"),
            ),
#        (0,0), ConditionSwitch(
#            #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
        )
# End Ass / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_Doggy_Feet:         #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
    contains:
            AlphaMask("Doreen_Doggy_Shins", "images/DoreenDoggy/Doreen_Doggy_Feet_Mask.png")

image Doreen_Doggy_Shins:             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
    #Doreen's footjob shins
#    contains:
#        "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Feet.png"
    contains:
            #hose legs
        ConditionSwitch(
            "DoreenX.Panties and DoreenX.PantiesDown", Null(),
            "DoreenX.Hose == 'garterbelt'", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Feet.png",
            "DoreenX.Hose == 'ripped pantyhose'", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Feet_Holed.png",
            "DoreenX.Hose == 'tights' or DoreenX.Hose == 'ripped tights'", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Feet_Tights.png",
#            "DoreenX.Hose == 'socks'", "images/DoreenDoggy/Doreen_Doggy_Feet_Socks.png",
            "DoreenX.Hose", "images/DoreenDoggy/Doreen_Doggy_Feet_Hose.png",
            "True", "images/DoreenDoggy/[DoreenX.skin_image.skin_path]Doreen_Doggy_Feet.png",
            )
#    contains:
#        #boots
#        ConditionSwitch(
#            "DoreenX.Boots == 'boots'", "images/DoreenDoggy/Doreen_Doggy_Feet_Boots.png",
#            "True", Null(),
#            )
    contains:
        #spunk
        ConditionSwitch(
            "'feet' in DoreenX.Spunk and Player.Male", "images/DoreenDoggy/Doreen_Doggy_Spunk_Feet.png",
            "True", Null(),
            )
#    pos (0,0)

image Doreen_Doggy_Shins0:
        #static animation
        "Doreen_Doggy_Shins"
        offset (0, 0) #(0,150) top


image Doreen_Doggy_GropeBreast:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        xzoom -.55
        yzoom .55
        offset (270,410)#(150,340)
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
        block:
            ease 1 rotate 10#60
            ease 1 rotate 0#90
            repeat

image Doreen_Gape_Anal:
        #animation for her asshole growing and shrinking a bit when over 2 Looseness
        contains:
            subpixel True
            "images/EmmaDoggy/Emma_Doggy_Anal_GapeBase.png"
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

image Zero_Doreen_Hotdog_Static:
    # The unmoving version of the hotdog cock
    # called in Doggy Ass LC
    contains:
        "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Doreen_Hotdog_Moving:
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


image Doreen_Pussy_Mask:
    #AlphaMask used to prevent the cock from moving past the pussy
    #Called in "Doreen_Pussy_Moving"
    contains:
        #Base
        "images/RogueDoggy/Rogue_Doggy_SexMask.png"
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat

image Doreen_Pussy_Mask_Static:
    #AlphaMask used to prevent the cock from moving past the pussy in static pose
    #Called in "Doreen_Pussy_Moving"
    contains:
        #Base
        "images/RogueDoggy/Rogue_Doggy_SexMask.png"
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Pussy fucking animations


image Doreen_Pussy_Static:
    #Full Animation for speed 0
    subpixel True
    contains:
        #moving hole
        "images/DoreenDoggy/Doreen_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat
#    contains:
#        #pubes
#        ConditionSwitch(
#            "DoreenX.Pubes", "images/DoreenDoggy/Doreen_Doggy_Pubes_Open.png",
#            "True", Null(),
#            )
#        subpixel True
#        transform_anchor True
#        anchor (0.515,0.69)#(0.52,0.69)
#        pos (217,518) #(219,518)
#        xzoom 1.1
    contains:
        #pubes
        ConditionSwitch(
            "DoreenX.Pubes", "images/DoreenDoggy/Doreen_Doggy_Pubes_Open.png",
            "True", Null(),
            )
        subpixel True
        transform_anchor True
        anchor (0.515,0.69)#(0.52,0.69)
        pos (213,518) #(217,518)
        xzoom .9
        block:
            ease .9 xzoom 1
            pause 1.6
            ease 2.5 xzoom .9
            repeat
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "DoreenX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_Barbell.png",
            "DoreenX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_Ring.png",
            "True", Null(),
            )
        offset (-3,8)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in DoreenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
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
        AlphaMask("Zero_Doreen_Doggy_Static", "Doreen_Pussy_Mask_Static")
    contains:
        #tail
        ConditionSwitch(
            "DoreenX.Tail and GhostTail", "images/DoreenDoggy/Doreen_Doggy_Tail3.png",
            "DoreenX.Tail", "images/DoreenDoggy/Doreen_Doggy_Tail.png",
            "True", Null(),
            )
        subpixel True
        transform_anchor True
        anchor (218,440)
        pos (216,440)
        block:
            rotate 0
            ease 2 rotate 15
            ease 3 rotate 0
            repeat
    xoffset 2

image Doreen_Pussy_Hole_Mask_Static:
    # This is the alpha used for the little flap in the heading animation "Doreen_Pussy_Moving"
    contains:
        #Base
        AlphaMask("images/DoreenDoggy/Doreen_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat

#image Doreen_PussyHole_Static:
#    #This is the image impacted by the mask for the pussy flap in "Doreen_Pussy_Moving"
#    contains:
#        #Mask
#        "images/DoreenDoggy/Doreen_Doggy_Pussy_FHeading.png"
#        anchor (0.52,0.69)
#        pos (217,515)
#        zoom 1
#        alpha .9
#        block:
#            ease 1 ypos 512
#            pause 1
#            ease 3 ypos 515
#            repeat


image Zero_Doreen_Doggy_Static:
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

image Doreen_Pussy_Heading:
    #Full Animation for speed 1
    subpixel True
    contains:
        #moving hole
        "images/DoreenDoggy/Doreen_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.51,0.69)#(0.52,0.69)
#        anchor (0.52,0.69)
        pos (213,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat
#    contains:
#        #pubes
#        ConditionSwitch(
#            "DoreenX.Pubes", "images/DoreenDoggy/Doreen_Doggy_Pubes_Fucking.png",
#            "True", Null(),
#            )
#        subpixel True
#        anchor (0.51,0.69)
#        pos (213,518) #(213,518)
#        xzoom .75
#        block:
#            ease 1 xzoom 1
#            pause 1
#            ease 3 xzoom .77
#            repeat
    contains:
        #pubes
        ConditionSwitch(
            "DoreenX.Pubes", "images/DoreenDoggy/Doreen_Doggy_Pubes_Fucking.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.51,0.69)
        pos (213,522) #(213,518)
        xzoom .75
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .65
            repeat
    contains:
        #pubes
        ConditionSwitch(
            "DoreenX.Pubes", "images/DoreenDoggy/Doreen_Doggy_Pubes_Fucking.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.51,0.69)
        pos (213,518) #(213,518)
        xzoom .77
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .77
            repeat
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "DoreenX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_Barbell.png",
            "DoreenX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_Ring.png",
            "True", Null(),
            )
        offset (-3,8)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in DoreenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
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
        AlphaMask("Zero_Doreen_Doggy_Heading", "Doreen_Pussy_Mask")


#    contains:
#        # expanding pussy flap
#        AlphaMask("Doreen_Pussy_Heading_Flap", "Doreen_Pussy_Hole_Mask")
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in DoreenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
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
    contains:
        #tail
        ConditionSwitch(
            "DoreenX.Tail and GhostTail", "images/DoreenDoggy/Doreen_Doggy_Tail3.png",
            "DoreenX.Tail", "images/DoreenDoggy/Doreen_Doggy_Tail.png",
            "True", Null(),
            )
        subpixel True
        transform_anchor True
        anchor (218,440)
        pos (216,440)
        block: #5
            rotate 6
            ease .2 rotate 6
            ease .8 rotate 12
            ease 1 rotate 0
            ease 1 rotate 6
            ease 1 rotate 0
            ease 1 rotate 6
            repeat
    xoffset 2


image Doreen_Pussy_Hole_Mask:
    # This is the alpha used for the little flap in the heading animation "Doreen_Pussy_Heading"
    contains:
        #Base
        AlphaMask("images/DoreenDoggy/Doreen_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat

#image Doreen_Pussy_Heading_Flap:
#    #This is the image impacted by the mask for the pussy flap in "Doreen_Pussy_Heading"
#    contains:
#        #Mask
#        "images/DoreenDoggy/Doreen_Doggy_Pussy_FHeading.png"
#        anchor (0.52,0.69)
#        pos (217,515)
#        zoom 1
#        alpha .9
#        block:
#            ease 1 ypos 505
#            pause 1
#            ease 3 ypos 515
#            repeat

image Doreen_Pussy_Fingering:
    #Full Animation for speed 1
    subpixel True
    contains:
        #moving hole
        "images/DoreenDoggy/Doreen_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .9#1
            pause 1
            ease 3 xzoom .6
            repeat
    contains:
        #pubes
        ConditionSwitch(
            "DoreenX.Pubes", "images/DoreenDoggy/Doreen_Doggy_Pubes_Open.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.51,0.69)
        pos (213,518) #(213,518)
        xzoom .75
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .77
            repeat
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "DoreenX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_Barbell.png",
            "DoreenX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_Ring.png",
            "True", Null(),
            )
        offset (-3,8)

    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in DoreenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
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
        AlphaMask("Zero_Pussy_Finger", "Rogue_Pussy_Mask")
#    contains:
#        # expanding pussy flap
#        AlphaMask("Doreen_Pussy_Heading_Flap", "Doreen_Pussy_Hole_Mask")

    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in DoreenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
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


image Zero_Doreen_Doggy_Heading:
    # Sex Speed 1 motions
    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (171,545)
        block:
            ease 1 xpos 168 ypos 500 #in stroke
            pause 1
            ease 3 xpos 171 ypos 545 #out stroke
            repeat


# > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

image Doreen_Pussy_Fucking2:
    #Full Animation for speed 2
    contains:
        #Base
        "images/DoreenDoggy/Doreen_Doggy_Pussy_FHole.png"
    contains:
        #pubes
        ConditionSwitch(
            "DoreenX.Pubes", "images/DoreenDoggy/Doreen_Doggy_Pubes_Fucking.png",
            "True", Null(),
            )
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "DoreenX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_Barbell.png",
            "DoreenX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_Ring.png",
            "True", Null(),
            )
        offset (-3,8)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in DoreenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            "'dildo pussy' in (Trigger,Trigger2,DoreenX.Offhand)", AlphaMask("Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "True",AlphaMask("Zero_Doreen_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            ),
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in DoreenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )
    contains:
        #tail
        ConditionSwitch(
            "DoreenX.Tail and GhostTail", "images/DoreenDoggy/Doreen_Doggy_Tail3.png",
            "DoreenX.Tail", "images/DoreenDoggy/Doreen_Doggy_Tail.png",
            "True", Null(),
            )
        subpixel True
        transform_anchor True
        anchor (218,440)
        pos (218,440)
        block:
            rotate 5
            ease .5 rotate 3
            ease .3 rotate 15
            ease .7 rotate 0
            ease 1.0 rotate 5
            repeat


image Zero_Doreen_Doggy_Fucking2:
    # Sex Speed 2 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat


image Doreen_Pussy_Fucking3:
    #Full Animation for speed 3
    contains:
        #Base
        "images/DoreenDoggy/Doreen_Doggy_Pussy_FHole.png"
    contains:
        #pubes
        ConditionSwitch(
            "DoreenX.Pubes", "images/DoreenDoggy/Doreen_Doggy_Pubes_Fucking.png",
            "True", Null(),
            )
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "DoreenX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_Barbell.png",
            "DoreenX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_Ring.png",
            "True", Null(),
            )
        offset (-3,8)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in DoreenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Doreen_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in DoreenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )
    contains:
        #tail
        ConditionSwitch(
            "DoreenX.Tail and GhostTail", "images/DoreenDoggy/Doreen_Doggy_Tail3.png",
            "DoreenX.Tail", "images/DoreenDoggy/Doreen_Doggy_Tail.png",
            "True", Null(),
            )
        subpixel True
        transform_anchor True
        anchor (218,440)
        pos (218,440)
        block:
            rotate 2
            ease .15 rotate 3
            ease .2 rotate 15
            ease .5 rotate 0
            ease .05 rotate 2
            repeat


image Zero_Doreen_Doggy_Fucking3:
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

image Doreen_Anal:
    #Anal static Loose
    contains:
        #Base
        "images/DoreenDoggy/Doreen_Doggy_Asshole_Loose.png"
        anchor (0.50,0.69)
        pos (208,515)#(208,500)
        zoom 1.25
    contains:
        #Cock
        "Zero_Doggy_Insert"
        pos (172,500)
    contains:
        #tail
        ConditionSwitch(
            "DoreenX.Tail and GhostTail", "images/DoreenDoggy/Doreen_Doggy_Tail3.png",
            "DoreenX.Tail", "images/DoreenDoggy/Doreen_Doggy_Tail.png",
            "True", Null(),
            )
        subpixel True
        transform_anchor True
        anchor (218,440)
        pos (218,440)
        block:
            rotate 0
            ease 2 rotate 15
            ease 2 rotate 0
            repeat



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Doreen_Anal_Fingering:
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
            "'anal' in DoreenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
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
        AlphaMask("Zero_Doreen_Doggy_Anal_Finger", "Doreen_Doggy_Anal_Fingering_Mask")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in DoreenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
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
#    contains:
#        #tail
#        ConditionSwitch(
#            "DoreenX.Tail and GhostTail", "images/DoreenDoggy/Doreen_Doggy_Tail3.png",
#            "DoreenX.Tail", "images/DoreenDoggy/Doreen_Doggy_Tail.png",
#            "True", Null(),
#            )
#        subpixel True
#        transform_anchor True
#        anchor (218,440)
#        pos (218,440)
#        block:
#            rotate 3
#            ease .5 rotate 2
#            ease .4 rotate 10
#            ease .8 rotate 0
#            ease .8 rotate 3
#            repeat

image Zero_Doreen_Doggy_Anal_Finger:
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
image Doreen_Doggy_Anal_Fingering_Mask:
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
image Doreen_Anal_Heading:
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
            "'anal' in DoreenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
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
        AlphaMask("Zero_Doreen_Doggy_Anal_Heading", "Doreen_Doggy_Anal_Heading_Mask")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in DoreenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
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
    contains:
        #tail
        ConditionSwitch(
            "DoreenX.Tail and GhostTail", "images/DoreenDoggy/Doreen_Doggy_Tail3.png",
            "DoreenX.Tail", "images/DoreenDoggy/Doreen_Doggy_Tail.png",
            "True", Null(),
            )
        subpixel True
        transform_anchor True
        anchor (218,440)
        pos (218,440)
        block:
            rotate 3
            ease .5 rotate 2
            ease .4 rotate 10
            ease .8 rotate 0
            ease .8 rotate 3
            repeat

image Zero_Doreen_Doggy_Anal_Heading:
        #the cock anal heading animation
    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500#505
            repeat

image Zero_Doreen_Doggy_Anal_HeadingJunk:
    #this is a mask to correct an annoying glitch in the core mask
    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease .5 ypos 550
            pause .25
            ease 1.75 ypos 600#505
            repeat

image Doreen_Doggy_Anal_Heading_Mask:
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

image Doreen_Doggy_Anal_Head_Top:
#animation for anal fucking top half
    contains:
        subpixel True
        "Doreen_Doggy_Body"
        ypos 0
        block:
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat

image Doreen_Doggy_Anal_Head_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Doreen_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -10
            easeout .1 ypos -7
            easein .9 ypos 0
            pause .9
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Doreen_Doggy_Anal1:
    #Animation for speed 2 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat

image Doreen_Anal_Fucking:
    #Animation for speed 2 Ass
    contains:
        #Hole
        "images/GwenDoggy/Gwen_Doggy_Anal_FullHole.png"
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in DoreenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            #full hose/tights
            "'dildo anal' in (Trigger,Trigger2,DoreenX.Offhand)", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", AlphaMask("Zero_Doreen_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            )
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in DoreenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )
    contains:
        #tail
        ConditionSwitch(
            "DoreenX.Tail and GhostTail", "images/DoreenDoggy/Doreen_Doggy_Tail3.png",
            "DoreenX.Tail", "images/DoreenDoggy/Doreen_Doggy_Tail.png",
            "True", Null(),
            )
        subpixel True
        transform_anchor True
        anchor (218,440)
        pos (218,440)
        block:
            rotate 5
            ease .5 rotate 3
            ease .3 rotate 15
            ease .7 rotate 0
            ease 1.0 rotate 5
            repeat

image Doreen_Doggy_Fuck_Top:
    #animation for anal fucking top half
    contains:
        subpixel True
        "Doreen_Doggy_Body"
        ypos 15#28
        pause .4
        block:
            ease .2 ypos 5#10
            pause .3
            ease 2 ypos 15#28
            repeat

image Doreen_Doggy_Fuck_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Doreen_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15#-25
            ease .1 ypos -5#-15
            pause .2
            ease 1.6 ypos 0
            repeat


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Doreen_Doggy_Anal2:
    #Animation for speed 3 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat

image Doreen_Anal_Fucking2:
    #Animation for speed 3 Ass
    contains:
        #Hole
        "images/GwenDoggy/Gwen_Doggy_Anal_FullHole.png"
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in DoreenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Doreen_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in DoreenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )
    contains:
        #tail
        ConditionSwitch(
            "DoreenX.Tail and GhostTail", "images/DoreenDoggy/Doreen_Doggy_Tail3.png",
            "DoreenX.Tail", "images/DoreenDoggy/Doreen_Doggy_Tail.png",
            "True", Null(),
            )
        subpixel True
        transform_anchor True
        anchor (218,440)
        pos (218,440)
        block:
            rotate 2
            ease .15 rotate 3
            ease .2 rotate 15
            ease .5 rotate 0
            ease .05 rotate 2
            repeat

image Doreen_Doggy_Fuck2_Top:
    #animation for anal fucking2 top half
    contains:
        subpixel True
        "Doreen_Doggy_Body"
        ypos 20
        block:
            pause .15
            ease .1 ypos 0
            pause .1
            easein .5 ypos 20
            pause .05
            repeat

image Doreen_Doggy_Fuck2_Ass:
    #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Doreen_Doggy_Ass"
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

image Doreen_Doggy_Feet0:
    #static animation
    contains:
        "Doreen_Doggy_Shins"
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
        "Doreen_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            subpixel True
            pause .5
            ease 2 ypos 20
            pause .5
            ease 2 ypos 0
            repeat

image Doreen_Doggy_Foot0_Top:
    #animation for footjob top half
    contains:
        subpixel True
        "Doreen_Doggy_Body"
        ypos 10#28
        #pause .4
        block:
            pause .5
            ease 2 ypos 14
            pause .5
            ease 2 ypos 10
            repeat

image Doreen_Doggy_Foot0_Ass:
    #animation for footjob ass half
    contains:
        subpixel True
        "Doreen_Doggy_Ass"
        ypos 0
        block:     #total 3
            pause .1 #.5
            ease 2 ypos 10
            pause .5
            ease 2.4 ypos 0
            repeat


image Doreen_Doggy_Feet1:
    #slow animation
    contains:
        "Doreen_Doggy_Shins"
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
        "Doreen_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat

image Doreen_Doggy_Foot1_Top:
    #animation for footjob top half
    contains:
        subpixel True
        "Doreen_Doggy_Body"
        ypos 70#28
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 70
            repeat

image Doreen_Doggy_Foot1_Ass:
    #animation for footjob ass half
    contains:
        subpixel True
        "Doreen_Doggy_Ass"
        ypos 0
        block: #total 3
            pause .3
            ease 2 ypos 80
            ease .7 ypos 0
            repeat


image Doreen_Doggy_Feet2:
    #fast animation
    contains:
        "Doreen_Doggy_Shins"
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
        "Doreen_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat

image Doreen_Doggy_Foot2_Top:
    #animation for footjob top half
    contains:
        subpixel True
        "Doreen_Doggy_Body"
        ypos 70#28
        block:
            pause .05
            ease .6 ypos 90#90#110
            ease .3 ypos 70#70
            repeat

image Doreen_Doggy_Foot2_Ass:
    #animation for footjob ass half
    contains:
        subpixel True
        "Doreen_Doggy_Ass"
        ypos 70
        block: #total .95
            pause .15#.05
            ease .6 ypos 90#110
            ease .2 ypos 70
            repeat

# Footjob animations end > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Doggy Launch/Reset
label Doreen_Doggy_Launch(Line = Trigger):
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    return
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
    if renpy.showing("Doreen_Doggy_Animation"):
        return
    $ Speed = 0
    call Girl_Hide(DoreenX,1)
    show Doreen_Doggy_Animation at SpriteLoc(StageCenter+48) zorder 150
    with dissolve
    return

label Doreen_Doggy_Reset:
    if not renpy.showing("Doreen_Doggy_Animation"):
        return
#    $ Trigger = 0               #fix, not sure this is a good idea
    $ DoreenX.ArmPose = 2
    $ DoreenX.SpriteVer = 0
    hide Doreen_Doggy_Animation
    call Girl_Hide(DoreenX)
    show Doreen_Sprite at SpriteLoc(DoreenX.SpriteLoc) zorder DoreenX.Layer:
            alpha 1 zoom 1 offset (0,0) anchor (0.6, 0.0)
    with dissolve
    $ Speed = 0
    return

# End Doreen Doggy Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



## Start Doreen Sex Pose Content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Doreen Sex Pose core / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_SexSprite:
    LiveComposite(
        (1120,840),

#        (0,0), ConditionSwitch(
#                #Shows different upper body motion depending on events
#                "True", "Doreen_Sex_Speed2",
#                ),
        (0,0), ConditionSwitch(
                #Shows different motion depending on events
#                "not Player.Sprite", "Doreen_Sex_Body_Static",
                "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Doreen_Sex_Fucking_Speed3",
                        "Speed >= 2", "Doreen_Sex_Fucking_Speed2",
                        "Speed", "Doreen_Sex_Fucking_Speed1",
                        "True", "Doreen_Sex_Fucking_Speed0",
                        ),
                "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Doreen_Sex_Anal_Speed3",
                        "Speed >= 2", "Doreen_Sex_Anal_Speed2",
                        "Speed", "Doreen_Sex_Anal_Speed1",
                        "True", "Doreen_Sex_Anal_Speed0",
                        ),
                "Player.Sprite and Player.Cock == 'out' and Speed >= 2","Doreen_Sex_Hotdog_Speed2",
                "Player.Sprite and Player.Cock == 'out' and Speed >= 1","Doreen_Sex_Hotdog_Speed1",
                "Player.Cock == 'foot'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 2", "Doreen_Sex_FJ_Speed2",
                        "Speed", "Doreen_Sex_FJ_Speed1",
                        "True", "Doreen_Sex_FJ_Speed0",
                        ),
#                "Player.Cock == 'out' and Speed >= 2","Doreen_Hotdog_Body_Anim2",
                "True", "Doreen_Sex_Static",
                ),
        )
    align (0.6,0.0)
    pos (650,203)#(650,303)
    zoom 1#0..85

# End Doreen Sex Pose core / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Doreen Sex Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_Sex_Body:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Doreen_SexSprite
        (1120,840),
#        (0,-100), "images/DoreenSex/Doreen_Sex_Headref.png",
        (335,60), "Doreen_HairBack_Sex",
        (335,60), "Doreen_Head_Sex",  #(50,-325)(335,-40)
        (0,0), "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Body.png",
        (0,0), ConditionSwitch(
            #bra layer
            "DoreenX.Uptop", Null(),
            #if the top's down. . .
            "DoreenX.Chest == 'sports bra'", "images/DoreenSex/Doreen_Sex_Chest_Sports_Under.png",
#            "DoreenX.Chest == 'bikini top'", "images/DoreenSex/Doreen_Sex_Chest_Sports.png",
            "DoreenX.Chest == 'lace bra'", "images/DoreenSex/Doreen_Sex_Chest_Lace_Under.png",
#            "DoreenX.Chest", "images/DoreenSex/Doreen_Sex_Chest_Bra.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "DoreenX.Water", "images/DoreenSex/Doreen_Sex_Water_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #shirt layer
            "DoreenX.Uptop", Null(),
            "DoreenX.Over == 'towel'", "images/DoreenSex/Doreen_Sex_Over_Towel_Under.png",
            "DoreenX.Over == 'tshirt'", "images/DoreenSex/Doreen_Sex_Over_Tshirt_Under.png",
            "DoreenX.Over == 'sweater'", "images/DoreenSex/Doreen_Sex_Over_Sweater_Under.png",
            "DoreenX.Over == 'tube top'", "images/DoreenSex/Doreen_Sex_Over_Tube_Under.png",
            "True", Null(),
            ),

        (0,0),ConditionSwitch(
            #Outside Spunk
            "'belly' in DoreenX.Spunk and Player.Male", "images/DoreenSex/Doreen_Sex_Spunk_Belly.png",
            "True", Null(),
            ),
#        (0,0), "images/DoreenSex/Doreen_Sex_HeadRef.png",
        )
#    yoffset -163
# End Doreen Sex Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_Sex_Tits:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Doreen_SexSprite
        (1120,840),

        (0,0), ConditionSwitch(
            #if uptop
            "not DoreenX.Uptop", Null(),
#            "DoreenX.Over == 'towel'", "images/DoreenSex/Doreen_Sex_Over_Green_Up.png",  #change to lower thing
#            "DoreenX.Over == 'tshirt'", "images/DoreenSex/Doreen_Sex_Over_Tshirt_Up.png",
            "DoreenX.Over == 'sweater'", "images/DoreenSex/Doreen_Sex_Over_Sweater_Up.png",
            "DoreenX.Over == 'tube top'", "images/DoreenSex/Doreen_Sex_Over_Brown_Up.png",

            "DoreenX.Chest == 'sports bra'", "images/DoreenSex/Doreen_Sex_Over_Green_Up.png",
            "DoreenX.Chest == 'bikini top'", "images/DoreenSex/Doreen_Sex_Over_Green_Up.png",
            "DoreenX.Chest == 'lace bra'", "images/DoreenSex/Doreen_Sex_Over_Lace_Up.png",
#            "DoreenX.Chest", "images/DoreenSex/Doreen_Sex_Chest_Bra.png",
            "True", Null(),
            ),

        (0,0), "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Tits.png",

        (0,0), ConditionSwitch(
            #bra layer
            "DoreenX.Uptop", Null(),
            #if the top's down. . .
            "DoreenX.Chest == 'sports bra'", "images/DoreenSex/Doreen_Sex_Chest_Sports.png",
            "DoreenX.Chest == 'bikini top'", "images/DoreenSex/Doreen_Sex_Chest_Sports.png",
            "DoreenX.Chest == 'lace bra'", "images/DoreenSex/Doreen_Sex_Chest_Lace.png",
            "DoreenX.Chest", "images/DoreenSex/Doreen_Sex_Chest_Bra.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "DoreenX.Water", "images/DoreenSex/Doreen_Sex_Water_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #shirt layer
            "DoreenX.Uptop", Null(),
            "DoreenX.Over == 'towel'", "images/DoreenSex/Doreen_Sex_Over_Towel.png",
            "DoreenX.Over == 'tshirt'", "images/DoreenSex/Doreen_Sex_Over_Tshirt.png",
            "DoreenX.Over == 'sweater'", "images/DoreenSex/Doreen_Sex_Over_Sweater.png",
            "DoreenX.Over == 'tube top'", "images/DoreenSex/Doreen_Sex_Over_Tube.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #piercings
#            "not DoreenX.Pierce", Null(),
#            "DoreenX.Uptop", ConditionSwitch(
#                    #if the top's down. . .
#                    "DoreenX.Pierce == 'ring'", "images/DoreenSex/Doreen_Sex_Pierce_Tits_R.png",
#                    "DoreenX.Pierce", "images/DoreenSex/Doreen_Sex_Pierce_Tits_B.png",
#                    "True", Null(),
#                    ),
#            "DoreenX.Pierce == 'ring'", ConditionSwitch(
#                    # ring pierce
#                    "DoreenX.Over == 'suit'", "images/DoreenSex/Doreen_Sex_Pierce_Tits_R_Pink.png",
#                    "DoreenX.Over == 'tshirt'", "images/DoreenSex/Doreen_Sex_Pierce_Tits_R_White.png",
#                    "DoreenX.Over == 'cheer top'", "images/DoreenSex/Doreen_Sex_Pierce_Tits_R_Cheer.png",

#                    "DoreenX.Chest == 'swimsuit'", "images/DoreenSex/Doreen_Sex_Pierce_Tits_R_Pink.png",
#                    "DoreenX.Chest == 'lace bra'", "images/DoreenSex/Doreen_Sex_Pierce_Tits_R_Lace.png",
#                    "DoreenX.Chest == 'tank' or DoreenX.Chest", "images/DoreenSex/Doreen_Sex_Pierce_Tits_R_White.png",

#                    "True", "images/DoreenSex/Doreen_Sex_Pierce_Tits_R.png",
#                    ),
#            "DoreenX.Over == 'suit'", "images/DoreenSex/Doreen_Sex_Pierce_Tits_B_Pink.png",
#            "DoreenX.Over == 'tshirt' or DoreenX.Over == 'cheer top'", "images/DoreenSex/Doreen_Sex_Pierce_Tits_B_White.png",

#            "DoreenX.Chest == 'swimsuit'", "images/DoreenSex/Doreen_Sex_Pierce_Tits_B_Pink.png",
#            "DoreenX.Chest == 'lace bra'", "images/DoreenSex/Doreen_Sex_Pierce_Tits_B_Lace.png",
#            "DoreenX.Chest == 'tank' or DoreenX.Chest", "images/DoreenSex/Doreen_Sex_Pierce_Tits_B_White.png",

#            "True", "images/DoreenSex/Doreen_Sex_Pierce_Tits_B.png",
#            ),

        (0,0), ConditionSwitch(
            #piercings
            "not DoreenX.Pierce", Null(),
            "DoreenX.Pierce == 'ring'", ConditionSwitch(
                    # ring pierce
                    "DoreenX.Uptop", "images/DoreenSex/Doreen_Sex_Pierce_Tits_R.png",

                    "DoreenX.Over == 'tube top'", "images/DoreenSex/Doreen_Sex_Pierce_Tits_R_Brown.png",
                    "DoreenX.Over == 'towel'", "images/DoreenSex/Doreen_Sex_Pierce_Tits_R_Green.png",
                    "DoreenX.Over == 'sweater'", "images/DoreenSex/Doreen_Sex_Pierce_Tits_R_Sweater.png",
                    "DoreenX.Over", "images/DoreenSex/Doreen_Sex_Pierce_Tits_R_Tshirt.png",                  #tshirt

                    "DoreenX.Chest == 'lace bra'", "images/DoreenSex/Doreen_Sex_Pierce_Tits_R_Lace.png",
                    "DoreenX.Chest == 'tan bra'", "images/DoreenSex/Doreen_Sex_Pierce_Tits_R_Tan.png",
                    "DoreenX.Chest", "images/DoreenSex/Doreen_Sex_Pierce_Tits_R_Green.png",

                    "True", "images/DoreenSex/Doreen_Sex_Pierce_Tits_R.png",
                    ),
            "DoreenX.Uptop", "images/DoreenSex/Doreen_Sex_Pierce_Tits_B.png",

            "DoreenX.Over == 'tube top'", "images/DoreenSex/Doreen_Sex_Pierce_Tits_B_Brown.png",
            "DoreenX.Over == 'towel'", "images/DoreenSex/Doreen_Sex_Pierce_Tits_B_Green.png",
            "DoreenX.Over == 'sweater'", "images/DoreenSex/Doreen_Sex_Pierce_Tits_B_Sweater.png",
            "DoreenX.Over", "images/DoreenSex/Doreen_Sex_Pierce_Tits_B_Tshirt.png",                  #tshirt

            "DoreenX.Chest == 'lace bra'", "images/DoreenSex/Doreen_Sex_Pierce_Tits_B_Lace.png",
            "DoreenX.Chest == 'tan bra'", "images/DoreenSex/Doreen_Sex_Pierce_Tits_B_Tan.png",
            "DoreenX.Chest", "images/DoreenSex/Doreen_Sex_Pierce_Tits_B_Green.png",

            "True", "images/DoreenSex/Doreen_Sex_Pierce_Tits_B.png",
            ),

        (0,0),ConditionSwitch(
            #Outside Spunk
            "'tits' in DoreenX.Spunk and Player.Male", "images/DoreenSex/Doreen_Sex_Spunk_Tits.png",
            "True", Null(),
            ),
#        (0,0), "images/DoreenSex/Doreen_Sex_HeadRef.png",
        )
#    yoffset -163
# End Doreen Sex Pose Tits / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_Head_Sex:
    # The head used for the sex pose, referenced by Doreen_Sex_Body
    "Doreen_Sprite_Head"
    zoom 1.0#1.24
    anchor (0.5,0.5)
    rotate 20#17
#    alpha 0.5

image Doreen_HairBack_Sex:
    # The hair behind the head for the sex pose, referenced by Doreen_Sex_Body
    "Doreen_Sprite_HairBack"
    zoom 1.#1.36
    anchor (0.5,0.5)
    rotate 20#15


image Doreen_Sex_Lick_Breasts:
        "Lick_Anim"
        zoom 0.7
        offset (400,350)#(390,620)

image Doreen_Sex_Fondle_Breasts:
        "GropeLeftBreast"
        zoom 1.5
        offset (190,-200)#(160,-40)

# Start Doreen Sex Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_Sex_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Doreen_SexSprite
        (1120,880),
        (545,540), ConditionSwitch(    #165,560
            #Personal Wetness
            "not DoreenX.Wet", Null(),
            "(DoreenX.Legs == 'pants' or DoreenX.Legs == 'shorts') and not DoreenX.Upskirt", Null(),
            "DoreenX.Panties and not DoreenX.PantiesDown", Null(),
            "DoreenX.Wet == 1", "Wet_Drip",
            "True", "Wet_Drip2",
            ),

        (545,540), ConditionSwitch(    #205,530
            #Spunk
            "'anal' not in DoreenX.Spunk or not Player.Male", Null(),
            "(DoreenX.Legs == 'pants' or DoreenX.Legs == 'shorts') and not DoreenX.Upskirt", Null(),
            "DoreenX.Wet == 1", "Spunk_Drip",
            "True", "Spunk_Drip2",
            ),

        (0,0), ConditionSwitch(
            #Legs
#            "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_FBase.png",
            "Player.Sprite and Player.Cock == 'in' and Speed", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_FBase.png",
#            "Player.Sprite and Player.Cock == 'in' and Speed", "Doreen_Sex_Heading_Pussy",
#            "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Ass.png",
#            "Trigger == 'lick pussy'", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Ass.png",
            "True", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Ass.png",
            ),

        (0,0), ConditionSwitch(
            #ass red
            "DoreenX.Red", "images/DoreenSex/Doreen_Sex_Red.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            "Player.Sprite and Player.Cock == 'anal'", "images/DoreenSex/Doreen_Sex_Anus_Cover.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #Wet look
            "not DoreenX.Water", Null(),
            "True", "images/DoreenSex/Doreen_Sex_Water_Legs.png",
            ),

        (0,0), "Doreen_Sex_Anus",
            #Anus Composite

        (0,0), "Doreen_Sex_Pussy",
            #Pussy Composite


        (0,0), ConditionSwitch(
            #hose layer
            "DoreenX.Hose == 'stockings and garterbelt'", "images/DoreenSex/Doreen_Sex_Hose_StockingsGarter.png",
            "DoreenX.Hose == 'garterbelt'", "images/DoreenSex/Doreen_Sex_Hose_Garter.png",
            "DoreenX.Hose == 'stockings'", "images/DoreenSex/Doreen_Sex_Hose_Stockings.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Panties if up
            "DoreenX.PantiesDown", Null(),
            "DoreenX.Panties == 'lace panties'", "images/DoreenSex/Doreen_Sex_Panties_Lace.png",
            "DoreenX.Panties == 'bikini bottoms'", "images/DoreenSex/Doreen_Sex_Panties_Bikini.png",
            "DoreenX.Panties and DoreenX.Wet", "images/DoreenSex/Doreen_Sex_Panties_Tan_Wet.png",
            "DoreenX.Panties", "images/DoreenSex/Doreen_Sex_Panties_Tan.png",
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #Piercings under hose
#            "not DoreenX.Pierce", Null(),
#            "DoreenX.Pierce == 'ring'",ConditionSwitch(
#                    #If she has panties down. . .
#                    "Player.Sprite and Player.Cock == 'in'", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_R_Fucking.png",
#                    "not DoreenX.Panties or DoreenX.PantiesDown", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_R.png",
#                    "DoreenX.Panties == 'lace panties' and not DoreenX.PantiesDown", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_R_Lace.png",
##                    "DoreenX.Panties == 'swimsuit' and not DoreenX.PantiesDown", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_R_White.png",
#                    "True", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_R_White.png",
#                    ),
#            #else, it's barbell
#            "not DoreenX.Panties or DoreenX.PantiesDown", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_B.png",
#            "DoreenX.Panties == 'lace panties' and not DoreenX.PantiesDown", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_B_Lace.png",
##            "DoreenX.Panties == 'swimsuit' and not DoreenX.PantiesDown", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_B_White.png",
#            "True", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_B_White.png",
#            ),
        (0,0), ConditionSwitch(
            #Piercings under pants and pantyhose
            "not DoreenX.Pierce", Null(),
            "DoreenX.Pierce == 'ring'",ConditionSwitch(
                    #If she has panties down. . .
                    "Player.Sprite and Player.Cock == 'in'", "images/DoreenSex/Doreen_69_Pierce_Pussy_R_Fucking.png",

                    "DoreenX.PantiesDown", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_R.png",
                    "DoreenX.Panties == 'lace panties'", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_R_Lace.png",
                    "DoreenX.Panties == 'bikini bottoms'", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_R_Green.png",
                    "DoreenX.Panties", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_R_Tan.png",
                    "True", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_R.png",

                    "True", Null(),
                    ),
            #else, it's barbell
            "DoreenX.Legs == 'shorts' and not DoreenX.Upskirt", "images/DoreenSex/Doreen_69_Pierce_Pussy_B_Clothed.png",

            "DoreenX.PantiesDown", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_B.png",
            "DoreenX.Panties == 'lace panties'", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_B_Lace.png",
            "DoreenX.Panties == 'bikini bottoms'", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_B_Green.png",
            "DoreenX.Panties", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_B_Tan.png",
            "True", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_B.png",
            ),
        (0,0), ConditionSwitch(
            #pantyhose layer
            "DoreenX.Panties and DoreenX.PantiesDown", Null(),
            "DoreenX.Hose == 'tights'", "images/DoreenSex/Doreen_Sex_Hose_Tights.png",
            "DoreenX.Hose == 'ripped tights'", "images/DoreenSex/Doreen_Sex_Hose_Tights_Holed.png",
            "DoreenX.Hose == 'pantyhose'", "images/DoreenSex/Doreen_Sex_Hose_Pantyhose.png",
            "DoreenX.Hose == 'ripped pantyhose'", "images/DoreenSex/Doreen_Sex_Hose_Pantyhose_Holed.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs Layer
            "DoreenX.Legs == 'skirt'", "images/DoreenSex/Doreen_Sex_Legs_Skirt.png",
            "DoreenX.Legs == 'red skirt'", "images/DoreenSex/Doreen_Sex_Legs_RedSkirt.png",
            "DoreenX.Legs == 'shorts' and DoreenX.Upskirt and DoreenX.Wet > 1", "images/DoreenSex/Doreen_Sex_Legs_Shorts_Down_Wet.png",
            "DoreenX.Legs == 'shorts' and DoreenX.Upskirt", "images/DoreenSex/Doreen_Sex_Legs_Shorts_Down.png",
            "DoreenX.Legs == 'shorts' and DoreenX.Wet > 1", "images/DoreenSex/Doreen_Sex_Legs_Shorts_Wet.png",
            "DoreenX.Legs == 'shorts'", "images/DoreenSex/Doreen_Sex_Legs_Shorts.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #towel Layer
            "DoreenX.Over == 'towel'", "images/DoreenSex/Doreen_Sex_Legs_Towel.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Piercings over pants and pantyhose
#            "not DoreenX.Pierce", Null(),
#            "DoreenX.Pierce == 'ring'",ConditionSwitch(
#                    #If she has panties down. . .
#                    "DoreenX.Legs == 'shorts' and not DoreenX.Upskirt", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_R_Pink.png",
#                    "DoreenX.Legs == 'suit' and not DoreenX.Upskirt", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_R_White.png",
#                    "DoreenX.Panties and DoreenX.PantiesDown", Null(),
#                    "DoreenX.Hose == 'tights'", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_R_Tights.png",
#                    "True", Null(),
#                    ),
#            #else, it's barbell
#            "DoreenX.Legs == 'shorts' and not DoreenX.Upskirt", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_B_Pink.png",
#            "DoreenX.Legs == 'pants' and not DoreenX.Upskirt", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_B_White.png",
#            "DoreenX.Panties and DoreenX.PantiesDown", Null(),
#            "DoreenX.Hose == 'tights'", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_B_Tights.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Piercings over pants and pantyhose
            "not DoreenX.Pierce", Null(),
            "DoreenX.Pierce == 'ring'",ConditionSwitch(
                    #If she has panties down. . .
                    "Player.Sprite and Player.Cock == 'in'", Null(),
                    "DoreenX.Legs == 'shorts' and not DoreenX.Upskirt", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_R_Brown.png",
                    "DoreenX.Hose == 'tights' and not (DoreenX.Panties and DoreenX.PantiesDown)", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_R_Tights.png",
                    "True", Null(),
                    ),
            #else, it's barbell
            "DoreenX.Legs == 'shorts' and not DoreenX.Upskirt", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_B_Brown.png",
            "DoreenX.Hose == 'tights' and not (DoreenX.Panties and DoreenX.PantiesDown)", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_B_Tights.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer
#            "not Player.Sprite or Player.Cock != 'out'", Null(),
#            "Speed >= 2", "Doreen_Hotdog_Zero_Anim2",
#            "Speed", "Doreen_Hotdog_Zero_Anim1",
#            "True", "Doreen_Hotdog_Zero_Anim0",
#            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy'", "Doreen_Sex_Lick_Pussy",
            "Trigger == 'lick ass'", "Doreen_Sex_Lick_Ass",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy fondling animation
            "Trigger3 == 'fondle pussy' and DoreenX.Lust > 60 and not (Player.Sprite)",  At("DoreenFingerHand", GirlFingerPussyX()), #"Doreen_Sex_Mast2",
            "Trigger3 == 'fondle pussy'", At("DoreenMastHand", GirlGropePussyX()), #"Doreen_Sex_Mast",
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Doreen_Sex_Fondle_Pussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #tail
            "Player.Sprite and (Player.Cock == 'anal' or Player.Cock == 'in')", Null(),
            "True", "Doreen_Sex_Tail_P0",
            ),
#        (0,0), ConditionSwitch(
#            #calves
#            "(DoreenX.Hose == 'pantyhose' or DoreenX.Hose == 'ripped pantyhose') and DoreenX.Panties and DoreenX.PantiesDown", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Calves.png",
#            "(DoreenX.Hose == 'tights' or DoreenX.Hose == 'ripped tights') and DoreenX.Panties and DoreenX.PantiesDown", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Calves.png",
#            "DoreenX.Hose == 'ripped pantyhose'", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Calves_Holed.png",
#            "DoreenX.Hose == 'ripped tights'", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Calves_Tights_Holed.png",
#            "DoreenX.Hose == 'tights'", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Calves_Tights.png",
#            "DoreenX.Hose and DoreenX.Hose != 'garterbelt'", "images/DoreenSex/Doreen_Sex_Calves_Hose.png",
#            "True", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Calves.png",   #Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #Footjob overlay
#            "Player.Cock == 'foot'", Null(),
##            "renpy.showing('Anal_Plug_In_Sex') or renpy.showing('Anal_Plug_Out_Sex')",AlphaMask("Doreen_Sex_Feet", "images/DoreenSex/Doreen_Sex_Feet_Mask.png"),
##            "ShowFeet", "Doreen_Sex_Feet",
##            "Player.Sprite", AlphaMask("Doreen_Sex_Feet", "images/DoreenSex/Doreen_Sex_Feet_Mask.png"),
##            "Trigger == 'lick pussy'", AlphaMask("Doreen_Sex_Feet", "images/DoreenSex/Doreen_Sex_Feet_Mask.png"),
##            "Trigger == 'lick ass'", AlphaMask("Doreen_Sex_Feet", "images/DoreenSex/Doreen_Sex_Feet_Mask.png"),
#            "True", "Doreen_Sex_Feet",
##            "True", AlphaMask("Doreen_Sex_Feet", "images/DoreenSex/Doreen_Sex_Feet_Mask.png"),
#            ),

#        (0,0), ConditionSwitch(                                                                                 #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
#            "not Speed", "Doreen_Sex_Feet",
#            "Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Doreen_Sex_Feet", "images/DoreenSex/Doreen_Sex_FeetMask.png"),
#            "True", "Doreen_Sex_Feet",
#            ),
        )
# End Doreen Sex Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_Sex_Calves:
    LiveComposite(
        #the lower legs used in the sex pose, referenced by Doreen_Sex_Legs
        (1120,840),
        (0,0), ConditionSwitch(
            #hose layer
            "(DoreenX.Hose == 'pantyhose' or DoreenX.Hose == 'ripped pantyhose') and DoreenX.Panties and DoreenX.PantiesDown", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Calves.png",
            "(DoreenX.Hose == 'tights' or DoreenX.Hose == 'ripped tights') and DoreenX.Panties and DoreenX.PantiesDown", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Calves.png",
            "DoreenX.Hose == 'ripped pantyhose'", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Calves_Holed.png",
            "DoreenX.Hose == 'ripped tights'", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Calves_Tights_Holed.png",
            "DoreenX.Hose == 'tights'", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Calves_Tights.png",
            "DoreenX.Hose and DoreenX.Hose != 'garterbelt'", "images/DoreenSex/Doreen_Sex_Calves_Hose.png",
            "True", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Calves.png",   #Null(),
            ),

        (0,0), ConditionSwitch(
            #Wet look
            "not DoreenX.Water", Null(),
            "True", "images/DoreenSex/Doreen_Sex_Water_Calves.png",
            ),
        (0,0), "Doreen_Sex_Feet_L", #left foot, stable
        (0,0), ConditionSwitch(
            #right foot, used in footjob
            "Player.Cock == 'foot'", Null(),
            "True", "Doreen_Sex_Feet_R",
            ),
        )

image Doreen_Sex_Feet_L:
    LiveComposite(
        #the lower legs used in the sex pose, referenced by Doreen_Sex_Legs
        (1120,840),
#        (0,0), "images/DoreenSex/Doreen_Sex_Feet.png",                                                         #Legs Base

        (0,0), ConditionSwitch(
            #hose layer
            "(DoreenX.Hose == 'pantyhose' or DoreenX.Hose == 'ripped pantyhose') and DoreenX.Panties and DoreenX.PantiesDown", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Feet_L.png",
            "DoreenX.Hose == 'tights' or DoreenX.Hose == 'ripped tights'", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Feet_L.png",
            "DoreenX.Hose == 'ripped pantyhose'", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Feet_Holed_L.png",
            "DoreenX.Hose and DoreenX.Hose != 'garterbelt'", "images/DoreenSex/Doreen_Sex_Feet_Hose_L.png",
            "True", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Feet_L.png",   #Null(),
            ),

#        (0,0), ConditionSwitch(
#            #Wet look
#            "not DoreenX.Water", Null(),
#            "True", "images/DoreenSex/Doreen_Sex_Water_Feet_L.png",
#            ),
        )

image Doreen_Sex_Feet_R:
    LiveComposite(
        #the lower legs used in the sex pose, referenced by Doreen_Sex_Legs
        (1120,840),
        (0,0), ConditionSwitch(
            #hose layer
            "(DoreenX.Hose == 'pantyhose' or DoreenX.Hose == 'ripped pantyhose') and DoreenX.Panties and DoreenX.PantiesDown", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Feet_R.png",
            "DoreenX.Hose == 'tights' or DoreenX.Hose == 'ripped tights'", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Feet_R.png",
            "DoreenX.Hose == 'ripped pantyhose'", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Feet_Holed_R.png",
            "DoreenX.Hose and DoreenX.Hose != 'garterbelt'", "images/DoreenSex/Doreen_Sex_Feet_Hose_R.png",
            "True", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Feet_R.png",   #Null(),
            ),

#        (0,0), ConditionSwitch(
#            #Wet look
#            "not DoreenX.Water", Null(),
#            "True", "images/DoreenSex/Doreen_Sex_Water_Feet_R.png",
#            ),
        (0,0), ConditionSwitch(
            #spunk
            "'feet' in DoreenX.Spunk", "images/DoreenSex/Doreen_Sex_Spunk_Feet.png",
            "True", Null(),
            ),
        )
# Start Doreen Sex Pose Pussy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_Sex_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).

    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/DoreenSex/Doreen_Sex_Pussy_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and Speed", "Doreen_Sex_Heading_Pussy",
                "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/DoreenSex/Doreen_Sex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/DoreenSex/Doreen_Sex_Pussy_Open.png",
                "Trigger3 == 'fondle pussy' and DoreenX.Lust > 60", "images/DoreenSex/Doreen_Sex_Pussy_Open.png",
                "True", "images/DoreenSex/Doreen_Sex_Pussy_Closed.png",
                )
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "not DoreenX.Wet", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/KittySex/Kitty_Sex_WetPussy_F.png",
                "True", "images/DoreenSex/Doreen_Sex_Wet.png",
                )
    contains:
            # pubes
            ConditionSwitch(
                "not DoreenX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/DoreenSex/Doreen_Sex_Pubes_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and Speed >= 1", "images/DoreenSex/Doreen_Sex_Pubes_Fucking.png",
                "Player.Sprite and Player.Cock == 'in'", "images/DoreenSex/Doreen_Sex_Pubes_Open.png",
                "Player.Sprite and Player.Cock == 'out'", "images/DoreenSex/Doreen_Sex_Pubes_Open.png",
                "Trigger == 'lick pussy'", "images/DoreenSex/Doreen_Sex_Pubes_Open.png",
                "Trigger3 == 'fondle pussy' and DoreenX.Lust > 60", "images/DoreenSex/Doreen_Sex_Pubes_Open.png",
                "True", "images/DoreenSex/Doreen_Sex_Pubes_Closed.png",
                )
    contains:
            #Spunk
            ConditionSwitch(
                "'in' not in DoreenX.Spunk or not Player.Male", Null(),
                "(DoreenX.Legs == 'pants' or DoreenX.Legs == 'shorts') and not DoreenX.Upskirt", Null(),
                "DoreenX.Panties and not DoreenX.PantiesDown", Null(),
                "True", AlphaMask("Spunk_Drip2","Doreen_Sex_Drip_Mask"),
                )
            offset (545,540)

    contains:
            ConditionSwitch(
                #Outside Spunk
                "'in' in DoreenX.Spunk and Player.Sprite and Player.Cock == 'in' and Speed and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_PussyF.png",
                "'in' in DoreenX.Spunk and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Pussy.png",
                "True", Null(),
                )
#    contains:
#            #Spunk under penis
#            ConditionSwitch(
#                "'in' in DoreenX.Spunk", "images/DoreenSex/Doreen_Sex_Spunk_Puss_Under.png",
#                "True", Null(),
#                )
#    contains:
#            #hose layer
#            ConditionSwitch(
#                "DoreenX.Panties and DoreenX.PantiesDown", Null(),
#                "DoreenX.Hose == 'ripped pantyhose' and ShowFeet", "images/DoreenSex/Doreen_Sex_Hose_Pantyhose_Holed.png",
#                "DoreenX.Hose == 'ripped pantyhose'", "images/DoreenSex/Doreen_Sex_Hose_Pantyhose_Holed.png",
#                "True", Null(),
#                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            ConditionSwitch(
#                "not Player.Sprite", Null(),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 3", AlphaMask("Doreen_Sex_Fucking_Zero_Anim3", "Doreen_Sex_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", AlphaMask("Doreen_Sex_Fucking_Zero_Anim2", "Doreen_Sex_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and Speed == 1", AlphaMask("Doreen_Sex_Fucking_Zero_Anim1", "Doreen_Sex_Heading_Mask"),
                "Player.Sprite and Player.Cock == 'in'", "Doreen_Sex_Fucking_Zero_Anim0",
                "True", Null(),
                )
#    contains:
#            #Piercings
#            ConditionSwitch(
#                "DoreenX.Pierce == 'barbell' and Player.Sprite and Player.Cock == 'in' and Speed", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_BarbellF.png",
#                "DoreenX.Pierce == 'ring' and Player.Sprite and Player.Cock == 'in' and Speed", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_RingF.png",
#                "DoreenX.Pierce == 'barbell'", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_Barbell.png",
#                "DoreenX.Pierce == 'ring'", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_Ring.png",
#                "True", Null(),
#                )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and Speed == 1", "Doreen_Pussy_Spunk_Heading",
                "True", Null(),
                )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "Speed == 1", Null(),
                "'in' not in DoreenX.Spunk or not Player.Sprite or Player.Cock != 'in' or not Speed or not Player.Male", Null(),
#                "Speed <= 1", Null(), #"Doreen_Pussy_Spunk_Heading",
                "True", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
                )

    #End Doreen Pussy composite

image Doreen_Sex_Drip_Mask:
    #This is the mask for her drip pattern
    contains:
        "images/JubesSex/Jubes_Sex_Mask_Anal.png"
        offset (-545,-450)#(-275,-560)#(-145,-560)#(-225,-560)

image Doreen_Sex_Lick_Pussy:
        "Lick_Anim"
        zoom 0.7
        offset (535,500)#(505,680)

image Doreen_Sex_Lick_Ass:
        "Lick_Anim"
        zoom 0.7
        offset (535,580)#(535,550)

image Doreen_Sex_Fondle_Pussy:
        "GropePussy_Doreen"
        xzoom -1.5
        yzoom 1.5
        offset(-710,-300) #(-890,-300)
#        block:
#            ease 1 offset(-1000,0) #(535,500)
#            ease 1 offset(-1000,-1000) #(535,500)
#            ease 1 offset(0,-1000) #(535,500)
#            ease 1 offset(0,0) #(535,500)
#            repeat

#End Animations for Doreen's Pussy during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_Sex_Zero_Cock:
        #this is the cock generally used by Doreen's sex pose
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

image Doreen_Sex_Fucking_Mask:
        #This is the mask image for Kitty's wide open pussy
        # Used in "Doreen_Sex_Speed2" and "Doreen_Sex_Speed3"
        contains:
            "images/JubesSex/Jubes_Sex_Mask_Fucking.png"
            yoffset 3

# Start Doreen Sex Pose Static / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_Sex_Static:
    # Pose for Doreen's Sex Pose in which she is static
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
#                pause 0.3
                ease 1.5 ypos -185 #-120
                pause .3
                ease 1.45 ypos -180 #-130
                pause 0.25
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Legs"
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
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Tits"
            anchor (560,330)
            offset (560,330)
            transform_anchor True
            pos (0,-180) #X less is left, Y less is up
            yzoom .95
            parallel:
#                pause 0.3
                ease 1.5 ypos -185 #-120
                pause .3
                ease 1.45 ypos -180 #-130
                pause 0.25
                repeat
            parallel:
                ease 1.5 yzoom 1 #-120
                pause .3
                ease 1.45 yzoom .95 #-130
                pause 0.25
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Calves"
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
            "Doreen_Sex_Zero_Cock"
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

#    contains:
#            Doreen's Feet
#            subpixel True
#            "Doreen_Sex_Feet"
#            ConditionSwitch(
#                #Footjob overlay
#                "ShowFeet", AlphaMask("Doreen_Sex_Feet", "images/DoreenSex/Doreen_Sex_Feet_Mask.png"),
#                "True", Null(),
#                )
#            pos (0,-180) #X less is left, Y less is up
#            block:
#                pause 0.3
#                ease 1.4 ypos -185 #-120
#                pause .3
#                ease 1.25 ypos -180 #-130
#                ease 0.15 ypos -177 #-130
#                ease 0.1 ypos -180 #-130
#                repeat

# End Doreen Sex Pose Speed Static / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Doreen Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Doreen Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_Sex_Fucking_Speed0:
    # Pose for Doreen's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                ease 2 ypos -160 #0
                pause 0.8
                ease 2 ypos -180 #-130
                pause 0.2
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -160 #0
                pause 0.8
                ease 2 ypos -180 #-130
                repeat
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Tits"
            anchor (560,330)
            offset (560,330)
            transform_anchor True
            pos (0,-180) #X less is left, Y less is up
            yzoom 1
            parallel: #adds to 5
                ease 2 ypos -160 #0
                pause 0.8
                ease 2 ypos -180 #-130
                pause 0.2
                repeat
            parallel:
                pause .2
                ease 2 yzoom .95 #-120
                pause .8
                ease 2 yzoom 1 #-130
#                pause 0.6
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Calves"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -160 #0
                pause 0.8
                ease 2 ypos -180 #-130
                repeat
# End main animation for Sex Pose Fucking Speed 1


image Doreen_Sex_Fucking_Zero_Anim0:
        #this is Doreen's sex animation, Speed 1 Fucking
        contains:
            subpixel True
            "Doreen_Sex_Zero_Cock"
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

# End Doreen Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Doreen Sex Pose Speed 1 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_Sex_Fucking_Speed1:
    # Pose for Doreen's Sex Pose in which she is fucking at speed 1 (heading)
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause 1
                ease 1.5 ypos -190 #0
                pause 1.6
                ease 0.9 ypos -180 #-130
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause 0.7
                ease 1.5 ypos -200 #0
                pause 1.6
                ease 1.2 ypos -180 #-130
                repeat
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Tits"
            anchor (560,330)
            offset (560,330)
            transform_anchor True
            pos (0,-180) #X less is left, Y less is up
            yzoom 1
            parallel: #adds to 5
                pause 1
                ease 1.5 ypos -190 #0
                pause 1.6
                ease 0.9 ypos -180 #-130
                repeat
            parallel:
                pause .9
                ease 1.6 yzoom .9 #-120
                pause 1.6
                ease 0.8 yzoom 1 #-130
                pause .1
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Calves"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause 0.7
                ease 1.5 ypos -200 #0
                pause 1.6
                ease 1.2 ypos -180 #-130
                repeat
# End main animation for Sex Pose Fucking Speed 1


image Doreen_Sex_Fucking_Zero_Anim1:
        #this is Doreen's sex animation, Speed 1 Fucking
        contains:
            subpixel True
            "Doreen_Sex_Zero_Cock"
            subpixel True
            pos (0,40)#(498,530)
            block:
                pause 0.2
#                ease 0.95 ypos -145
                ease 2 ypos -10#-10 #-140
                pause .8
                ease 2 ypos 40 #-10
                repeat

image Doreen_Sex_Heading_Mask:
        #This is the mask image for Doreen's heading pussy
        contains:
            "images/JubesSex/Jubes_Sex_Mask_Fucking.png"
            yoffset 10
            block:
                pause 0.2
                ease 2 yoffset 3
                pause 0.8
                ease 2 yoffset 10
                repeat


image Doreen_Sex_Heading_Pussy:
        #This is the image for Doreen's heading pussy growing
#        contains:
#            "images/DoreenSex/Doreen_Sex_Pussy_Fucking_Base.png"
        contains:
            "images/DoreenSex/Doreen_Sex_Pussy_Fucking.png"
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
#    "images/DoreenDoggy/Doreen_Doggy_Pussy_HHole.png"
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

image Doreen_Pussy_Spunk_Heading:
        #This is the image for Doreen's heading pussy cum
        contains:
            ConditionSwitch(
                "'in' in DoreenX.Spunk and Player.Sprite and Player.Cock == 'in' and Speed == 1 and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
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

# End Doreen Sex Pose Speed 1 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Doreen Sex Pose Speed 2 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_Sex_Fucking_Speed2:
    # Pose for Doreen's Sex Pose in which she is fucking at speed 2
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 4.2
                pause 0.5
                ease .9 ypos -190 # 0
                pause 0.8
                ease 2.0 ypos -180 # -130
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 4.2
                pause 0.4
                ease 0.95 ypos -205 # 5
                ease 0.45 ypos -200 # 0
                pause 0.6
                ease 1.8 ypos -180 # -130
                repeat
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Tits"
            anchor (560,330)
            offset (560,330)
            transform_anchor True
            pos (0,-180) #X less is left, Y less is up
            yzoom 1
            parallel: #adds to 4.2
                pause 0.5
                ease .9 ypos -190 # 0
                pause 0.8
                ease 2.0 ypos -180 # -130
                repeat
            parallel:
                pause 0.4
                ease 1 yzoom .9 #-120
                pause .8
                ease 1.9 yzoom 1 #-130
                pause .1
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Calves"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 4.2
                pause 0.4
                ease 0.95 ypos -205 # 5
                ease 0.45 ypos -200 # 0
                pause 0.6
                ease 1.8 ypos -180 # -130
                repeat
# End main animation for Sex Pose Fucking Speed 2


image Doreen_Sex_Fucking_Zero_Anim2:
        #this is Doreen's sex animation, Speed 2 Fucking
        contains:
            subpixel True
            "Doreen_Sex_Zero_Cock"
            subpixel True
            pos (0,20)#(498,530)
            block:
                pause 0.2
                ease 0.95 ypos -100 # -145
                ease 0.25 ypos -90 # -140
                pause .8
                ease 2 ypos 20 #-10
                repeat

# End Doreen Sex Pose Speed 2 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Doreen Sex Pose Speed 3 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_Sex_Fucking_Speed3:
    # Pose for Doreen's Sex Pose in which she is fucking at speed 3
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.6
                ease 0.4 ypos -210
#                pause 0.35
                ease 0.8 ypos -180
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.4
                ease 0.45 ypos -220
                ease 0.15 ypos -210
#                pause 0.35
                ease 0.8 ypos -180
                repeat
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Tits"
            anchor (560,330)
            offset (560,330)
            transform_anchor True
            pos (0,-180) #X less is left, Y less is up
            yzoom 1
            parallel:
                pause 0.6
                ease 0.4 ypos -205
#                pause 0.35
                ease 0.8 ypos -180
                repeat
            parallel:
                pause 0.3
                ease 0.7 yzoom .85 #-120
#                pause 0.02
                ease 0.8 yzoom 1 #-130
#                pause 0.22
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Calves"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.45
                ease 0.45 ypos -230
                ease 0.1 ypos -220
#                pause 0.35
                ease 0.8 ypos -180
                repeat


# End main animation for Sex Pose Fucking Speed 3


image Doreen_Sex_Fucking_Zero_Anim3:
        #this is Doreen's sex animation, Speed3 Fucking
        contains:
            subpixel True
            "Doreen_Sex_Zero_Cock"
            subpixel True
            pos (0,10)
            block:
                pause 0.1
                ease 0.55 ypos -100
                ease 0.15 ypos -90
                pause 0.25
                ease 0.75 ypos 10
                repeat

# End Doreen Sex Pose Speed 3 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Animations for Doreen's Ass during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Doreen's Ass during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_Sex_Anus:
    contains:
            #tail
            ConditionSwitch(
            "Player.Sprite and Player.Cock == 'in' and Speed >= 3", "Doreen_Sex_Tail_P3",
            "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "Doreen_Sex_Tail_P2",
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "Doreen_Sex_Tail_A3",
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "Doreen_Sex_Tail_A2",
#            "Player.Sprite and Player.Cock == 'anal' and Speed", "Doreen_Sex_Tail_A1",
            "Player.Sprite and (Player.Cock == 'anal' or Player.Cock == 'in')", "Doreen_Sex_Tail_P0",
            "True", Null(), #"Doreen_Sex_Tail_P0",
            )
    contains:
            #Anus background plate
            ConditionSwitch(
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/BetsySex/Betsy_Sex_Anus.png",
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/BetsySex/Betsy_Sex_Anus.png",
            "Player.Sprite and Player.Cock == 'anal' and Speed", "Doreen_Sex_Anal_Heading",
            "Player.Sprite and Player.Cock == 'anal'", "Doreen_Sex_Anal_Tip",
            "DoreenX.Plug", "images/PlugBase_Sex.png",
            "DoreenX.Loose > 2", "Doreen_Gape_Anal_Sex",
            "DoreenX.Loose", "images/DoreenSex/Doreen_Sex_Anus_Loose.png",
            "True", "images/DoreenSex/Doreen_Sex_Anus_Loose.png",
            )
    contains:
            #Spunk under penis
            ConditionSwitch(
                "'anal' not in DoreenX.Spunk or not Player.Male", Null(),
#                "Player.Sprite and Player.Cock != 'anal' and Speed >= 1", "images/DoreenSex/Doreen_Sex_Spunk_Anal_Under.png",
                "Player.Sprite and Player.Cock != 'anal' and Speed == 1", "Doreen_Sex_Anal_Spunk_Heading_Under",
                "True", "images/JubesSex/Jubes_Sex_Spunk_Anal.png",
                )
            yoffset 5
    contains:
            # The animation of Zero's moving penis, masked by her anus shape
            ConditionSwitch(
                "not Player.Sprite or Player.Cock != 'anal'", Null(),
                "Speed >= 3",  AlphaMask("Doreen_Sex_Anal_Zero_Anim3", "Doreen_Sex_Anal_MaskF"),
                "Speed >= 2", AlphaMask("Doreen_Sex_Anal_Zero_Anim2", "Doreen_Sex_Anal_MaskF"),
                "Speed", AlphaMask("Doreen_Sex_Anal_Zero_Anim1", "Doreen_Sex_Anal_Mask"),
                "True", AlphaMask("Doreen_Sex_Anal_Zero_Anim0", "Doreen_Sex_Anal_Mask"),
                )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "'anal' not in DoreenX.Spunk or not Player.Sprite or Player.Cock != 'anal' or not Speed or not Player.Male", Null(),
                "Speed == 1", "Doreen_Sex_Anal_Spunk_Heading_Over",
                "True", "Doreen_Sex_Anal_Spunk",
                )

image Doreen_Sex_Tail_P0:
        #Tail when in Sex Pussy speed 0, attached to Sex Anus
        contains:
            ConditionSwitch(
#                "DoreenX.Tail and renpy.showing('Betsy_69_Animation'", "images/DoreenDoggy/Doreen_Doggy_Tail3.png",
                "DoreenX.Tail", "images/DoreenSex/Doreen_Sex_Tail.png",
                "True", Null(),
                )
            transform_anchor True
            subpixel True
            anchor (555,520)#(555,520)#(0.52,0.69)
            offset (560,675)#(560,480)
            rotate -20
#            zoom .40 # tight
            block:
                ease 3 rotate 40 #in.87
                ease 3 rotate -3 #out
                repeat

image Doreen_Sex_Tail_P2:
        #Tail when in Sex Pussy speed 0, attached to Sex Anus
        contains:
            ConditionSwitch(
#                "DoreenX.Tail and GhostTail", "images/DoreenDoggy/Doreen_Doggy_Tail3.png",
                "DoreenX.Tail", "images/DoreenSex/Doreen_Sex_Tail.png",
                "True", Null(),
                )
            transform_anchor True
            subpixel True
            anchor (555,520)#(0.52,0.69)
            offset (560,675)#(560,480)
            rotate 0
            block:
                pause 0.3
                ease 0.75 rotate 40 # -145
                easeout 0.35 rotate 30 # -140
#                pause .6
                ease 2.1 rotate 5 #-10
                ease .7 rotate 10 #-10
                repeat

image Doreen_Sex_Tail_P3:
        #Tail when in Sex Pussy speed 0, attached to Sex Anus
        contains:
            ConditionSwitch(
#                "DoreenX.Tail and GhostTail", "images/DoreenDoggy/Doreen_Doggy_Tail3.png",
                "DoreenX.Tail", "images/DoreenSex/Doreen_Sex_Tail.png",
                "True", Null(),
                )
            transform_anchor True
            subpixel True
            anchor (555,520)#(0.52,0.69)
            offset (560,675)#(560,480)
            rotate 5
            block:
                ease 0.4 rotate 10
                ease 0.45 rotate 40
                ease 0.15 rotate 30
#                pause 0.35
                ease 0.8 rotate 5
                repeat


image Doreen_Sex_Tail_A2:
        #Tail when in Sex Pussy speed 0, attached to Sex Anus
        contains:
            ConditionSwitch(
#                "DoreenX.Tail and GhostTail", "images/DoreenDoggy/Doreen_Doggy_Tail3.png",
                "DoreenX.Tail", "images/DoreenSex/Doreen_Sex_Tail.png",
                "True", Null(),
                )
            transform_anchor True
            subpixel True
            anchor (555,520)#(0.52,0.69)
            offset (560,675)#(560,480)
            rotate 0
            block:
                pause 0.3
                ease 0.75 rotate 40 # -145
                easeout 0.35 rotate 30 # -140
#                pause .6
                ease 2.1 rotate 5 #-10
                ease .7 rotate 10 #-10
                repeat

image Doreen_Sex_Tail_A3:
        #Tail when in Sex Pussy speed 0, attached to Sex Anus
        contains:
            ConditionSwitch(
#                "DoreenX.Tail and GhostTail", "images/DoreenDoggy/Doreen_Doggy_Tail3.png",
                "DoreenX.Tail", "images/DoreenSex/Doreen_Sex_Tail.png",
                "True", Null(),
                )
            transform_anchor True
            subpixel True
            anchor (555,520)#(0.52,0.69)
            offset (560,675)#(560,480)
            rotate 5
            block:
                ease 0.4 rotate 10
                ease 0.45 rotate 40
                ease 0.15 rotate 30
#                pause 0.35
                ease 0.8 rotate 5
                repeat

image Doreen_Gape_Anal_Sex:
        #removing an anal plug
        contains:
            #Hole
            "images/DoreenSex/Doreen_Sex_Anus_Loose.png"
            transform_anchor True
            subpixel True
            anchor (560,620)#(0.52,0.69)
            offset (560,617)#(218,518)
            zoom 1 # tight
            block:
                ease 3 zoom 1.2 #in.87
                ease 3 zoom 1 #out
                repeat

image Doreen_Sex_Anal_Spunk:
    ConditionSwitch(
                "'anal' in DoreenX.Spunk and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Anal_Over.png",
                "True", Null(),
                )
    anchor (0.5,0.5)
    pos (0.5,0.5)
#    xoffset 20
    yoffset -23#68
    xzoom .9#1.2

image Doreen_Sex_Anal_Mask:
        #This is the mask image for small stuff
        # Used in "Doreen_Sex_Speed2" and "Doreen_Sex_Speed3"
        contains:
            "images/JubesSex/Jubes_Sex_Mask_Anal.png"
            yoffset 98 #-9
            xoffset 3 #3
#            xoffset -5

image Doreen_Sex_Anal_MaskF:
        #This is the mask image for deep stuff
        # Used in "Doreen_Sex_Speed2" and "Doreen_Sex_Speed3"
        contains:
            "images/JubesSex/Jubes_Sex_Mask_AnalB.png"
            yoffset 98 #-9
            xoffset 3



# Start Doreen Sex Pose Speed 0 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_Sex_Anal_Speed0:
    # Pose for Doreen's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.5
                ease 1 ypos -185 #40
                pause 1.0
                ease 1.5 ypos -180 #90
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.2
                ease 1 ypos -190 #40
                pause 1.3
                ease 1.5 ypos -180 #90
                repeat
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Tits"
            anchor (560,330)
            offset (560,330)
            transform_anchor True
            pos (0,-180) #X less is left, Y less is up
            yzoom 1
            parallel: #adds to 5
                pause 1.5
                ease 1 ypos -185 #40
                pause 1.0
                ease 1.5 ypos -180 #90
                repeat
            parallel:
                pause .2
                ease 2 yzoom .95 #-120
                pause .8
                ease 2 yzoom 1 #-130
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Calves"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.2
                ease 1 ypos -190 #40
                pause 1.3
                ease 1.5 ypos -180 #90
                repeat

# End main animation for Sex Pose Anal Speed 1


image Doreen_Sex_Anal_Zero_Anim0:
        #this is Doreen's sex animation, Speed 0 Anal
        contains:
            subpixel True
            "Doreen_Sex_Zero_Cock"
#            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            subpixel True
            pos (3,135)#(498,530)
            block:
                pause 0.2
                ease 2 ypos 130 #90
                pause .8
                ease 2 ypos  135 #130
                repeat

image Doreen_Sex_Anal_Tip:
    "images/BetsySex/Betsy_Sex_Anus.png"
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

# End Doreen Sex Pose Speed 0 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Doreen Sex Pose Speed 1 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_Sex_Anal_Heading:
    "images/BetsySex/Betsy_Sex_Anus.png"
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

image Doreen_Sex_Anal_Spunk_Heading_Over:
    ConditionSwitch(
                "'anal' in DoreenX.Spunk and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Anal_Over.png",
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

image Doreen_Sex_Anal_Spunk_Heading_Under:
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

image Doreen_Sex_Anal_Speed1:
    # Pose for Doreen's Sex Pose in which she is fucking at speed 1 (heading)
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.5
                ease 1 ypos -185 #40
                pause 1.0
                ease 1.5 ypos -180 #90
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.2
                ease 1 ypos -190 #40
                pause 1.3
                ease 1.5 ypos -180 #90
                repeat
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Tits"
            anchor (560,330)
            offset (560,330)
            transform_anchor True
            pos (0,-180) #X less is left, Y less is up
            yzoom 1
            parallel: #adds to 5
                pause 1.5
                ease 1 ypos -185 #40
                pause 1.0
                ease 1.5 ypos -180 #90
                repeat
            parallel:
                pause .9
                ease 1.6 yzoom .9 #-120
                pause 1.6
                ease 0.8 yzoom 1 #-130
                pause .1
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Calves"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.2
                ease 1 ypos -190 #40
                pause 1.3
                ease 1.5 ypos -180 #90
                repeat

# End main animation for Sex Pose Anal Speed 1


image Doreen_Sex_Anal_Zero_Anim1:
        #this is Doreen's sex animation, Speed 1 Anal
        contains:
            subpixel True
            "Doreen_Sex_Zero_Cock"
#            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            subpixel True
            pos (3,130)#(498,530)
            block:
                pause 0.2
                ease 2 ypos 90 #40
                pause .8
                ease 2 ypos  130 #90
                repeat

# End Doreen Sex Pose Speed 1 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Doreen Sex Pose Speed 2 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_Sex_Anal_Speed2:
    # Pose for Doreen's Sex Pose in which she is doing anal at speed 2
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.6
                ease 1.0 ypos -200
                pause .9
                ease 1.7 ypos -180
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.4
                ease 0.95 ypos -215
                ease 0.25 ypos -210
                pause .8
                ease 1.8 ypos -180
                repeat
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Tits"
            anchor (560,330)
            offset (560,330)
            transform_anchor True
            pos (0,-180) #X less is left, Y less is up
            yzoom 1
            parallel: #adds to 4.2
                pause 0.6
                ease 1.0 ypos -200
                pause .9
                ease 1.7 ypos -180
                repeat
            parallel:
                pause 0.4
                ease 1 yzoom .9 #-120
                pause .8
                ease 1.9 yzoom 1 #-130
                pause .1
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Calves"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 4.2
                pause 0.4
                ease 0.95 ypos -215
                ease 0.25 ypos -210
                pause .8
                ease 1.8 ypos -180
                repeat
#    contains:
#            #Zero's cock in the sex pose
#            AlphaMask("Doreen_Sex_Fucking_Zero_Anim2", "Doreen_Sex_Fucking_Mask")
# End main animation for Sex Pose Fucking Speed 2


image Doreen_Sex_Anal_Zero_Anim2:
        #this is Doreen's sex animation, Speed 2 Fucking
        contains:
            subpixel True
            "Doreen_Sex_Zero_Cock"
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

# End Doreen Sex Pose Speed 2 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Doreen Sex Pose Speed 3 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_Sex_Anal_Speed3:
    # Pose for Doreen's Sex Pose in which she is Anal at speed 3
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 1.8
#                pause 0.5
                easein .5 ypos -180
                ease .4 ypos -200
                pause .4
                ease .5 ypos -185
                repeat

    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Legs"
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
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Tits"
            anchor (560,330)
            offset (560,330)
            transform_anchor True
            pos (0,-180) #X less is left, Y less is up
            yzoom 1
            parallel:
#                pause 0.5
                easein .5 ypos -180
                ease .4 ypos -200
                pause .4
                ease .5 ypos -185
                repeat
            parallel:
                pause 0.3
                ease 0.7 yzoom .85 #-120
#                pause 0.02
                ease 0.8 yzoom 1 #-130
#                pause 0.22
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Calves"
            pos (0,-180) #X less is left, Y less is up
            block:
#                pause 0.4
                easein 0.4 ypos -180
                ease 0.3 ypos -215
                ease 0.1 ypos -210
                pause 0.4
                easeout 0.6 ypos -185
                repeat

# End main animation for Sex Pose Fucking Speed 3


image Doreen_Sex_Anal_Zero_Anim3:
        #this is Doreen's sex animation, Speed3 Anal
        contains:
            subpixel True
            "Doreen_Sex_Zero_Cock"
            subpixel True
            pos (3,-40)
            block:
                pause 0.1
                ease 0.55 ypos -25
                ease 0.15 ypos -20
                pause 0.25
                ease 0.75 ypos 90
                repeat

# End Doreen Sex Pose Speed 3 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Doreen Sex Pose Speed 1 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_Sex_Hotdog_Speed1:
    # Pose for Doreen's Sex Pose in which she is hotdogging at speed 1 (slow)
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.8
                ease 0.8 ypos -190 #-120
                pause .5
                ease 1.0 ypos -180 #-130
                pause 0.4
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Legs"
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
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Tits"
            anchor (560,330)
            offset (560,330)
            transform_anchor True
            pos (0,-180) #X less is left, Y less is up
            yzoom 1
            parallel:
                pause 0.8
                ease 0.8 ypos -190 #-120
                pause .5
                ease 1.0 ypos -180 #-130
                pause 0.4
                repeat
            parallel:
                pause 0.4
                ease 1.3 yzoom .9 #-120
                ease 1.4 yzoom 1 #-130
                pause 0.4
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Calves"
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
            "Doreen_Sex_Zero_Cock"
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
#    contains:
#            #Doreen's Feet
#            subpixel True
#            "Doreen_Sex_Feet"
##            ConditionSwitch(
##                #Footjob overlay
##                "ShowFeet", AlphaMask("Doreen_Sex_Feet", "images/DoreenSex/Doreen_Sex_FeetMask.png"),
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

# End Doreen Sex Pose Speed 1 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Doreen Sex Pose Speed 2 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_Sex_Hotdog_Speed2:
    # Pose for Doreen's Sex Pose in which she is hotdogging at speed 2 (fast)
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.25
                ease 0.45 ypos -195 #-120
                pause .1
                ease 0.8 ypos -180 #-130
#                pause 0.2
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Legs"
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
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Tits"
            anchor (560,330)
            offset (560,330)
            transform_anchor True
            pos (0,-180) #X less is left, Y less is up
            yzoom 1
            parallel:
                pause 0.25
                ease 0.45 ypos -200 #-120
                pause .1
                ease 0.8 ypos -180 #-130
                repeat
            parallel:
                pause 0.1
                ease 0.45 yzoom .90 #-120
                ease 0.9 yzoom 1 #-130
                pause 0.15
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Calves"
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
            "Doreen_Sex_Zero_Cock"
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
#    contains:
#            #Doreen's Feet
#            subpixel True
#            "Doreen_Sex_Feet"
##            ConditionSwitch(
##                #Footjob overlay
##                "ShowFeet", AlphaMask("Doreen_Sex_Feet", "images/DoreenSex/Doreen_Sex_FeetMask.png"),
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

# End Doreen Sex Pose Speed 2 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Doreen Sex Pose Speed 0 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_Sex_FJ_Speed0:
    # Pose for Doreen's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Body"
            pos (240,-60) #(50,-180) #X less is left, Y less is up
            block: #adds to 5
                ease 2 ypos -50#-40 #-140
                pause 0.8
                ease 2 ypos -60#-60 #-180
                pause 0.2
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Legs"
            pos (240,-60) #(50,-220) #X less is left, Y less is up (80,0)
            block: #adds to 5
                pause 0.2
                ease 2 ypos -60 #10
                pause 0.8
                ease 2 ypos -50 #0
                repeat
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Tits"
            anchor (560,330)
            offset (560,330)
            transform_anchor True
            pos (240,-60) #X less is left, Y less is up
            yzoom 1
            parallel:
                ease 2 ypos -50#-40 #-140
                pause 0.8
                ease 2 ypos -60#-60 #-180
                pause 0.2
                repeat
            parallel:
                ease 2.8 yzoom .85 #-120
                ease 2 yzoom 1 #-130
                pause 0.2
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Calves"
            pos (240,-60) #X less is left, Y less is up
            block:
                pause 0.2
                ease 2 ypos -50 #10
                pause 0.8
                ease 2 ypos -60 #0
                repeat
    contains:
            #Doreen's Feet
            subpixel True
            "Doreen_Sex_Feet_R"
            anchor (410,470)
            offset (410,470)    #(560,330)
            transform_anchor True
            pos (240,-60) #X less is left, Y less is up (200,-180)
            rotate -45
#            parallel:
#                pause 0.2
#                ease 2 ypos -230 #10
#                pause 0.8
#                ease 2 ypos -220 #0
#                repeat
            parallel:
                pause 0.2
                ease 2 rotate -10 #10
                pause 0.8
                ease 2 rotate -45 #0
                repeat
    contains:
            subpixel True
#            "Doreen_Sex_Zero_Cock"
            "Zero_Blowcock"
            zoom .5
            subpixel True
            pos (630,520) #(0,-380)
#    contains:
#            #Doreen's Legs
#            subpixel True
#            "Doreen_Sex_Feet"
##            alpha 0.5
##            AlphaMask("Doreen_Sex_Feet", "images/DoreenSex/Doreen_Sex_Feet_Mask.png")
#            pos (50,-270) #X less is left, Y less is up (80,0)
#            block: #adds to 5
##                pause 0.2
#                ease 2 ypos -290 #10
#                pause 0.8
#                ease 2 ypos -270 #0
#                pause 0.2
#                repeat

# End main animation for Sex Pose Footjob Speed 0

# End Doreen Sex Pose Speed 0 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Doreen Sex Pose Speed 1 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_Sex_FJ_Speed1:
    # Pose for Doreen's Sex Pose in which she is fucking at speed 1 (slow)
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Body"
            pos (240,-60) #X less is left, Y less is up
            block: #adds to 5
                ease 2 ypos 20#-40 #-140
                pause 0.8
                ease 2 ypos -60#-60 #-180
                pause 0.2
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Legs"
            pos (240,-60) #X less is left, Y less is up
            block:
                pause 0.2
                ease 2 ypos 20 #10
                pause 0.8
                ease 2 ypos -60 #0
                repeat
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Tits"
            anchor (560,330)
            offset (560,330)
            transform_anchor True
            pos (240,-60) #X less is left, Y less is up
            yzoom .9
            parallel:
                ease 2 ypos 20#-40 #-140
                pause 0.8
                ease 2 ypos -60#-60 #-180
                pause 0.2
                repeat
            parallel:
#                ease .8 yzoom 1 #-120
                pause .8
                ease .8 yzoom .90 #-130 #bottom
                ease .7 yzoom 1.05 #-120
                ease .7 yzoom 1 #-120
                pause 1.1
                ease .9 yzoom .90 #-120 #top
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Calves"
            pos (240,-60) #X less is left, Y less is up
            block:
                pause 0.2
                ease 2 ypos 20 #10
                pause 0.8
                ease 2 ypos -60 #0
                repeat
    contains:
            #Doreen's Feet
            subpixel True
            "Doreen_Sex_Feet_R"
            anchor (410,470)
            offset (410,470)    #(560,330)
            transform_anchor True
            pos (240,-60) #X less is left, Y less is up (200,-180)
            rotate -30
            parallel:
                pause 0.2
                ease 2 ypos 30 #10
                pause 0.8
                ease 2 ypos -60 #0
                repeat
            parallel:
                easeout 1 rotate -38 #10
                easein 1.5 rotate -45 #10
                easeout 1.5 rotate -48 #10
#                pause 3
                easein 1 rotate -30 #0
                repeat
    contains:
            subpixel True
#            "Doreen_Sex_Zero_Cock"
            "Zero_Blowcock"
            zoom .5
            subpixel True
            pos (630,520) #(0,-380)
            block: #adds to 5
                pause 0.8
                ease 1.5 ypos 550 #40
                pause 0.7
                ease 1 ypos 520 #-100
                pause 1
                repeat

# End main animation for Sex Pose Footjob Speed 1

# End Doreen Sex Pose Speed 1 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Doreen Sex Pose Speed 2 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_Sex_FJ_Speed2:
    # Pose for Doreen's Sex Pose in which she is fucking at speed 2 (fast)
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Body"
            pos (240,-60) #X less is left, Y less is up
            block: #adds to 5
                ease .8 ypos 20#-40 #-140
#                pause 0.8
                ease 1.2 ypos -60#-60 #-180
#                pause 0.2
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Legs"
            pos (240,-60) #X less is left, Y less is up
            block:
#                pause 0.2
                ease .9 ypos 20 #10
#                pause 0.8
                ease 1.1 ypos -60 #0
                repeat
    contains:
            #Doreen's underlying body
            subpixel True
            "Doreen_Sex_Tits"
            anchor (560,330)
            offset (560,330)
            transform_anchor True
            pos (240,-60) #X less is left, Y less is up
            yzoom 1
            parallel:
                ease .8 ypos 25#-40 #-140
                ease .2 ypos 20#-40 #-140
#                pause 0.8
                ease 1 ypos -60#-60 #-180
#                pause 0.2
                repeat
            parallel:
                pause .5
                ease .3 yzoom .90 #-130 #bottom
                ease .4 yzoom 1 #-120 #top
                pause .8
                repeat
    contains:
            #Doreen's Legs
            subpixel True
            "Doreen_Sex_Calves"
            pos (240,-60) #X less is left, Y less is up
            block:
#                pause 0.2
                ease .8 ypos 20 #10
#                pause 0.8
                ease 1.2 ypos -60 #0
                repeat
    contains:
            #Doreen's Feet
            subpixel True
            "Doreen_Sex_Feet_R"
            anchor (410,470)
            offset (410,470)    #(560,330)
            transform_anchor True
            pos (240,-60) #X less is left, Y less is up (200,-180)
            rotate -45
            parallel:
#                pause 0.2
                ease .8 ypos 0 #10
#                pause 0.8
                ease 1.2 ypos -60 #0
                repeat
            parallel:
                ease 1 rotate -50 #10
                ease 1 rotate -45 #0
                repeat
    contains:
            subpixel True
#            "Doreen_Sex_Zero_Cock"
            "Zero_Blowcock"
            zoom .5
            subpixel True
            pos (630,520) #(0,-380)
            block: #adds to 2
                pause 0.4
                ease .6 ypos 530 #40
#                pause .2
                ease .6 ypos 520 #-100
                pause .4
                repeat

# End main animation for Sex Pose Footjob Speed 2

# End Doreen Sex Pose Speed 2 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     Sex Launch/Reset
label Doreen_Sex_Launch(Line = Trigger):
    $ DoreenX.Offhand = 0 if DoreenX.Offhand == "hand" else DoreenX.Offhand

###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    return
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    $ DoreenX.Pose = "doggy"
#    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary

    $ Line = "solo" if not Line else Line
    if Line == "sex":
        $ Player.Sprite = 1
        $ Player.Cock = "in"
        call Cock_Occupied(DoreenX,"pussy")
        if Trigger2 in ("fondle pussy","dildo pussy","lick pussy"):
                $ Trigger2 = 0
    elif Line == "anal":
        $ Player.Sprite = 1
        $ Player.Cock = "anal"
        call Cock_Occupied(DoreenX,"anal")
        if Trigger2 in ("insert ass","dildo anal","lick ass"):
                $ Trigger2 = 0
    elif Line == "hotdog":
        $ Player.Sprite = 1
        if DoreenX.PantsNum() == 5: #upskirts her if she's in a skirt
                $ DoreenX.Upskirt = 1
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
        call Zero_Strapped(DoreenX) #puts strap-on on.
    $ Trigger = Line

    if DoreenX.Pose == "doggy":
            call Doreen_Doggy_Launch(Line)
            return
    if renpy.showing("Doreen_SexSprite"):
        return
    $ Speed = 0
    call Girl_Hide(DoreenX,1)
    show Doreen_SexSprite zorder 150
    with dissolve
    return

label Doreen_Sex_Reset:
    if renpy.showing("Doreen_Doggy_Animation"):
        call Doreen_Doggy_Reset
        return
    if not renpy.showing("Doreen_SexSprite"):
        return
    $ DoreenX.ArmPose = 2
    hide Doreen_SexSprite
    call Girl_Hide(DoreenX)
#    call Set_The_Scene(Dress = 0)
    show Doreen_Sprite at SpriteLoc(DoreenX.SpriteLoc) zorder DoreenX.Layer:
        alpha 1 zoom 1 offset (0,0) anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return


## End Doreen Sex Pose Content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


### End Doreen Sex Pose Content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




## Doreen's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





## Doreen's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Doreen_BJ_Animation:#BJ_NewTest:                                                                #core BJ animation
    LiveComposite(
        (800,950),
        (0,0), ConditionSwitch( #-270,-160
            # Doreen's hair backside
            "Speed == 0", "Doreen_BJ_Anim0",               #Static
            "Speed == 1", "Doreen_BJ_Anim1",               #Licking

#            "True", "Doreen_BJ_Anim2",               #Heading

            "Speed == 2", "Doreen_BJ_Anim2",               #Heading
            "Speed == 3", "Doreen_BJ_Anim3",               #Sucking
            "Speed == 4", "Doreen_BJ_Anim4",               #Deepthroat
            "Speed == 5", "Doreen_BJ_Anim5",               #Cumming High
            "Speed == 6", "Doreen_BJ_Anim6",               #Cumming Deep
            "True", Null(),
            ),
        )
#    zoom 1
#    anchor (.5,.5)
    zoom .8 #.7
    transform_anchor True
    anchor (.5,.5)
    offset (-95,85) #(-90,100)


image Doreen_BJ_Backdrop:
    LiveComposite(
        (800,950),       #550,950
#        (-10,-90), "Doreen_BJ_HairBack", #(75,-10)
        (0,0), "Doreen_BJ_Ass",
        (0,0), ConditionSwitch(
            #bra back
#            "DoreenX.Over == 'tshirt'", Null(),
            "DoreenX.Uptop", Null(),
            "DoreenX.Over == 'tube top' or DoreenX.Over == 'towel' or DoreenX.Chest == 'lace bra'", "images/DoreenBJFace/Doreen_BJ_Chest_Back.png",
            "True", Null(),
            ),
        (0,0), "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_BJ_Body.png",
#        (0,0), ConditionSwitch(
#            #Water effect
#            "DoreenX.Water and DoreenX.ArmPose == 1", "images/DoreenSprite/Doreen_Sprite_Water1.png",
#            "DoreenX.Water", "images/DoreenSprite/Doreen_Sprite_Water2.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Chest layer under tits
#            "DoreenX.Over == 'tshirt'", Null(),
            "DoreenX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "DoreenX.Chest == 'lace bra'", "images/DoreenBJFace/Doreen_BJ_Chest_Lace_Up.png",
                    "DoreenX.Chest == 'sports bra'", "images/DoreenBJFace/Doreen_BJ_Chest_Sports_Up.png",
                    "DoreenX.Chest == 'bikini top'", "images/DoreenBJFace/Doreen_BJ_Chest_Bikini_Up.png",
                    "DoreenX.Chest", "images/DoreenBJFace/Doreen_BJ_Chest_Bra_Up.png",
                    "True", Null(),
                    ),
            "DoreenX.Chest == 'lace bra'", "images/DoreenBJFace/Doreen_BJ_Chest_Lace.png",
            "DoreenX.Chest == 'sports bra'", "images/DoreenBJFace/Doreen_BJ_Chest_Sports.png",
            "DoreenX.Chest == 'bikini top'", "images/DoreenBJFace/Doreen_BJ_Chest_Bikini.png",
            "DoreenX.Chest", "images/DoreenBJFace/Doreen_BJ_Chest_Bra.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over body layer
            "DoreenX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "DoreenX.Over == 'tshirt'", "images/DoreenBJFace/Doreen_BJ_Over_Tshirt_Up.png",
                    "DoreenX.Over == 'tube top'", "images/DoreenBJFace/Doreen_BJ_Over_Tube_Up.png",
                    "DoreenX.Over == 'sweater'", "images/DoreenBJFace/Doreen_BJ_Over_Sweater_Up.png",
                    "DoreenX.Over == 'towel'", "images/DoreenBJFace/Doreen_TJ_Over_Towel_Body.png",
                    "True", Null(),
                    ),
            "DoreenX.Over == 'tshirt'", "images/DoreenBJFace/Doreen_BJ_Over_Tshirt.png",
            "DoreenX.Over == 'tube top'", "images/DoreenBJFace/Doreen_BJ_Over_Tube.png",
            "DoreenX.Over == 'sweater'", "images/DoreenBJFace/Doreen_BJ_Over_Sweater.png",
            "DoreenX.Over == 'towel'", "images/DoreenBJFace/Doreen_BJ_Over_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Jacket layer
            "DoreenX.Acc == 'jacket'", "images/DoreenBJFace/Doreen_BJ_Jacket.png",
            "DoreenX.Acc == 'vest'", "images/DoreenBJFace/Doreen_BJ_Vest.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Piercings layer
            "not DoreenX.Pierce", Null(),
            "DoreenX.Pierce == 'ring'", ConditionSwitch(
                    #if it's the ring pericings
                    "DoreenX.Uptop", "images/DoreenBJFace/Doreen_BJ_Pierce_Ring.png",
                    "DoreenX.Over == 'towel'", "images/DoreenBJFace/Doreen_BJ_Pierce_Ring_Green.png",
                    "DoreenX.Over == 'tube top'", "images/DoreenBJFace/Doreen_BJ_Pierce_Ring_Brown.png",
                    "DoreenX.Over == 'sweater'", "images/DoreenBJFace/Doreen_BJ_Pierce_Ring_Sweater.png",
                    "DoreenX.Over == 'tshirt'", "images/DoreenBJFace/Doreen_BJ_Pierce_Ring_Gray.png",
                    "DoreenX.Chest == 'lace bra'", "images/DoreenBJFace/Doreen_BJ_Pierce_Ring_Lace.png",
                    "DoreenX.Chest == 'bikini top' or DoreenX.Chest == 'sports bra'", "images/DoreenBJFace/Doreen_BJ_Pierce_Ring_Green.png",
                    "DoreenX.Chest", "images/DoreenBJFace/Doreen_BJ_Pierce_Ring_Tan.png",
                    "True", "images/DoreenBJFace/Doreen_BJ_Pierce_Ring.png",
                    ),
            "DoreenX.Uptop", "images/DoreenBJFace/Doreen_BJ_Pierce_Barbell.png",
            "DoreenX.Over == 'towel'", "images/DoreenBJFace/Doreen_BJ_Pierce_Barbell_Green.png",
            "DoreenX.Over == 'tube top'", "images/DoreenBJFace/Doreen_BJ_Pierce_Barbell_Brown.png",
            "DoreenX.Over == 'sweater'", "images/DoreenBJFace/Doreen_BJ_Pierce_Barbell_Sweater.png",
            "DoreenX.Over == 'tshirt'", "images/DoreenBJFace/Doreen_BJ_Pierce_Barbell_Gray.png",
            "DoreenX.Chest == 'lace bra'", "images/DoreenBJFace/Doreen_BJ_Pierce_Barbell_Lace.png",
            "DoreenX.Chest == 'bikini top' or DoreenX.Chest == 'sports bra'", "images/DoreenBJFace/Doreen_BJ_Pierce_Barbell_Green.png",
            "DoreenX.Chest", "images/DoreenBJFace/Doreen_BJ_Pierce_Barbell_Tan.png",
            "True", "images/DoreenBJFace/Doreen_BJ_Pierce_Barbell.png",
            ),
        (0,0), ConditionSwitch(
            # spunk over tits
            "'tits' not in DoreenX.Spunk", Null(),
#            "DoreenX.Over == 'tshirt'", "images/DoreenBJFace/Doreen_TJ_Spunk_Clothed.png",
#            "not DoreenX.Uptop and DoreenX.Over", "images/DoreenBJFace/Doreen_TJ_Spunk_Clothed.png",
            "True", "images/DoreenBJFace/Doreen_BJ_Spunk_Tits.png",
            ),
        (0,0), ConditionSwitch(
            #Hair overlay
            "DoreenX.Hair != 'long' and DoreenX.Hair != 'wetlong'", Null(),
            "DoreenX.Water or DoreenX.Hair == 'wetlong'", "images/DoreenBJFace/Doreen_TJ_Hair_Wet.png",
            "not Player.Male and 'facial' in DoreenX.Spunk","images/DoreenBJFace/Doreen_TJ_Hair_Wet.png",
            "True", "images/DoreenBJFace/Doreen_TJ_Hair_Long.png",
            ),
#        (0,0), "images/DoreenBJFace/Doreen_TJ_RefLine.png",
#        (-10,-90), "Doreen_Sprite_Head", #(75,-10)
        )
    transform_anchor True
    anchor (0.45, 0.35)#(0.6, 1.0)
    xoffset 50#30
    yoffset -530#-530
#    zoom .75  #.76
    rotate 0
# image Doreen_BJ_Backdrop # image Doreen_BJ_Backdrop # image Doreen_BJ_Backdrop End # image Doreen_BJ_Backdrop # image Doreen_BJ_Backdrop End

image Doreen_BJ_Ass:
    LiveComposite(
        (800,950),       #550,950
#        (-10,-90), "Doreen_BJ_HairBack", #(75,-10)
        (0,0), ConditionSwitch(
            #Tail
            "DoreenX.Tail","images/DoreenBJFace/Doreen_TJ_Tail_Under.png",
            "True", Null(),
            ),
        (0,0), "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_TJ_Ass.png",

#        (0,0), ConditionSwitch(
#            #Water effect
#            "DoreenX.Water and DoreenX.ArmPose == 1", "images/DoreenBJFace/Doreen_Sprite_Water1.png",
#            "DoreenX.Water", "images/DoreenBJFace/Doreen_Sprite_Water2.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #stockings
            "DoreenX.Hose == 'stockings'", "images/DoreenBJFace/Doreen_TJ_Hose_Stockings.png",
            "DoreenX.Hose == 'stockings and garterbelt'", "images/DoreenBJFace/Doreen_TJ_Hose_StockingsGarter.png",
            "DoreenX.Hose == 'garterbelt'", "images/DoreenBJFace/Doreen_TJ_Hose_Garter.png",
            "True", Null(),
            ),
         (0,0), ConditionSwitch(
            #panties
#            "not DoreenX.Panties", Null(),
#            "DoreenX.PantiesDown", ConditionSwitch(
#                    #if the panties are down
#                    "not DoreenX.Legs or DoreenX.Upskirt or DoreenX.Legs == 'skirt'", ConditionSwitch(
#                            #if she's wearing a skirt or nothing else
#                            "DoreenX.Panties == 'bikini bottoms'", "images/DoreenBJFace/Doreen_Sprite_Panties_Bikini_Down.png",
#                            "DoreenX.Panties == 'lace panties'", "images/DoreenBJFace/Doreen_Sprite_Panties_Lace_Down.png",
#                            "DoreenX.Panties", "images/DoreenBJFace/Doreen_Sprite_Panties_Tan_Down.png",
#                            "True", Null(),
#                            ),
#                    "True", Null(),
#                    ),
            "DoreenX.PantiesDown", Null(),
            "DoreenX.Panties == 'bikini bottoms'", "images/DoreenBJFace/Doreen_TJ_Panties_Bikini.png",
            "DoreenX.Panties == 'lace panties'", "images/DoreenBJFace/Doreen_TJ_Panties_Lace.png",
            "DoreenX.Panties", "images/DoreenBJFace/Doreen_TJ_Panties_Tan.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pantyhose
            "DoreenX.Hose == 'pantyhose' and (not DoreenX.PantiesDown or not DoreenX.Panties)", "images/DoreenBJFace/Doreen_TJ_Hose_Pantyhose.png",
            "DoreenX.Hose == 'tights' and (not DoreenX.PantiesDown or not DoreenX.Panties)", "images/DoreenBJFace/Doreen_TJ_Hose_Tights.png",
            "DoreenX.Hose == 'ripped pantyhose' and (not DoreenX.PantiesDown or not DoreenX.Panties)", "images/DoreenBJFace/Doreen_TJ_Hose_Pantyhose_Holed.png",
            "DoreenX.Hose == 'ripped tights' and (not DoreenX.PantiesDown or not DoreenX.Panties)", "images/DoreenBJFace/Doreen_TJ_Hose_Tights_Holed.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #pants
            "not DoreenX.Legs", Null(),
            "DoreenX.Upskirt", ConditionSwitch(
                        #if the skirt's up or pants down
                        "DoreenX.Legs == 'skirt'", "images/DoreenBJFace/Doreen_TJ_Legs_Skirt_Up.png",
#                        "DoreenX.Legs == 'shorts'", "images/DoreenBJFace/Doreen_TJ_Legs_Shorts.png",
                        "True", Null(),
                        ),
#            "DoreenX.Legs == 'skirt' and DoreenX.Over != 'towel'", "images/DoreenBJFace/Doreen_TJ_Legs_Skirt.png",
            "DoreenX.Legs == 'skirt'", "images/DoreenBJFace/Doreen_TJ_Legs_Skirt.png",
            "DoreenX.Legs == 'shorts'", "images/DoreenBJFace/Doreen_TJ_Legs_Shorts.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Over body layer
            "DoreenX.Over == 'towel' and DoreenX.Upskirt", "images/DoreenBJFace/Doreen_TJ_Over_Towel_Up.png",
            "DoreenX.Over == 'towel'", "images/DoreenBJFace/Doreen_TJ_Over_Towel.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Tail
            "not DoreenX.Tail",Null(),
            "DoreenX.Legs == 'skirt'","images/DoreenBJFace/Doreen_TJ_Tail_Cover.png",
            "DoreenX.Over == 'towel'","images/DoreenBJFace/Doreen_TJ_Tail_Cover.png",
            "DoreenX.Legs and not DoreenX.Upskirt","images/DoreenBJFace/Doreen_TJ_Tail_Cover.png",
            "DoreenX.Hose == 'pantyhose' and (not DoreenX.PantiesDown or not DoreenX.Panties)", "images/DoreenBJFace/Doreen_TJ_Tail_Cover.png",
            "DoreenX.Hose == 'tights' and (not DoreenX.PantiesDown or not DoreenX.Panties)", "images/DoreenBJFace/Doreen_TJ_Tail_Cover.png",
            "DoreenX.Panties == 'lace panties'","images/DoreenBJFace/Doreen_TJ_Tail_Over.png",
            "DoreenX.Panties and not DoreenX.PantiesDown","images/DoreenBJFace/Doreen_TJ_Tail_Cover.png",
            "True","images/DoreenBJFace/Doreen_TJ_Tail_Over.png",
            ),
#        (0,0), ConditionSwitch(
#            #Chest layer under tits
#            "DoreenX.Over == 'tshirt'", Null(),
#            "DoreenX.Uptop", ConditionSwitch(
#                    # if top is up. . .
#                    "DoreenX.Chest == 'lace bra'", "images/DoreenBJFace/Doreen_BJ_Chest_Lace_Up.png",
#                    "DoreenX.Chest == 'bra'", "images/DoreenBJFace/Doreen_BJ_Chest_Bra_Up.png",
#                    "DoreenX.Chest == 'tank'", "images/DoreenBJFace/Doreen_BJ_Chest_Tank_Up.png",
#                    "DoreenX.Chest == 'swimsuit'", "images/DoreenBJFace/Doreen_BJ_Chest_Bikini_Up.png",
#                    "True", Null(),
#                    ),
#            "DoreenX.Chest == 'lace bra'", "images/DoreenBJFace/Doreen_BJ_Chest_Lace.png",
#            "DoreenX.Chest == 'bra'", "images/DoreenBJFace/Doreen_BJ_Chest_Bra.png",
#            "DoreenX.Chest == 'tank'", "images/DoreenBJFace/Doreen_BJ_Chest_Tank.png",
#            "DoreenX.Chest == 'swimsuit'", "images/DoreenBJFace/Doreen_BJ_Chest_Bikini.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #Over body layer
#            "DoreenX.Over == 'open suit'", "images/DoreenBJFace/Doreen_BJ_Over_Suit_Open.png",
#            "DoreenX.Uptop", ConditionSwitch(
#                    # if top is up. . .
#                    "DoreenX.Over == 'suit'", "images/DoreenBJFace/Doreen_BJ_Over_Suit_Open.png",
#                    "DoreenX.Over == 'tshirt'", "images/DoreenBJFace/Doreen_BJ_Over_Tshirt_Up.png",
#                    "DoreenX.Over == 'cheer top'", "images/DoreenBJFace/Doreen_BJ_Over_Cheer_Up.png",
#                    "True", Null(),
#                    ),
#            "DoreenX.Over == 'suit'", "images/DoreenBJFace/Doreen_BJ_Over_Suit.png",
#            "DoreenX.Over == 'tshirt'", "images/DoreenBJFace/Doreen_BJ_Over_Tshirt.png",
#            "DoreenX.Over == 'cheer top'", "images/DoreenBJFace/Doreen_BJ_Over_Cheer.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #Piercings layer
#            "not DoreenX.Pierce", Null(),
#            "DoreenX.Pierce == 'ring'", ConditionSwitch(
#                    #if it's the ring pericings
#                    "DoreenX.Uptop", "images/DoreenBJFace/Doreen_TJ_Pierce_Ring.png",
#                    "DoreenX.Over == 'suit'", "images/DoreenBJFace/Doreen_TJ_Pierce_Ring_Pink.png",
#                    "DoreenX.Over == 'tshirt' or DoreenX.Over == 'cheer top'", "images/DoreenBJFace/Doreen_TJ_Pierce_Ring_White.png",
#                    "DoreenX.Chest == 'lace bra'", "images/DoreenBJFace/Doreen_TJ_Pierce_Ring_Lace.png",
#                    "DoreenX.Chest == 'bra'", "images/DoreenBJFace/Doreen_TJ_Pierce_Ring_White.png",
#                    "DoreenX.Chest == 'swimsuit'", "images/DoreenBJFace/Doreen_TJ_Pierce_Ring_Pink.png",
#                    "DoreenX.Chest == 'tank'", "images/DoreenBJFace/Doreen_TJ_Pierce_Ring_White.png",
#                    "True", "images/DoreenBJFace/Doreen_TJ_Pierce_Ring.png",
#                    ),
#            "DoreenX.Uptop", "images/DoreenBJFace/Doreen_TJ_Pierce_Barbell.png",
#            "DoreenX.Over == 'suit'", "images/DoreenBJFace/Doreen_TJ_Pierce_Barbell_Pink.png",
#            "DoreenX.Over == 'tshirt' or DoreenX.Over == 'cheer top'", "images/DoreenBJFace/Doreen_TJ_Pierce_Barbell_White.png",
#            "DoreenX.Chest == 'lace bra'", "images/DoreenBJFace/Doreen_TJ_Pierce_Barbell_Lace.png",
#            "DoreenX.Chest == 'bra'", "images/DoreenBJFace/Doreen_TJ_Pierce_Barbell_White.png",
#            "DoreenX.Chest == 'swimsuit'", "images/DoreenBJFace/Doreen_TJ_Pierce_Barbell_Pink.png",
#            "DoreenX.Chest == 'tank'", "images/DoreenBJFace/Doreen_TJ_Pierce_Barbell_White.png",
#            "True", "images/DoreenBJFace/Doreen_TJ_Pierce_Barbell.png",
#            ),
        (0,0), ConditionSwitch(
            # spunk over tits
            "'back' not in DoreenX.Spunk", Null(),
#            "DoreenX.Over == 'tshirt'", "images/DoreenBJFace/Doreen_TJ_Spunk_Clothed.png",
#            "not DoreenX.Uptop and DoreenX.Over", "images/DoreenBJFace/Doreen_TJ_Spunk_Clothed.png",
            "True", "images/DoreenBJFace/Doreen_TJ_Spunk_Back.png",
            ),
#        (0,0), "images/DoreenBJFace/Doreen_TJ_RefLine.png",
#        (-10,-90), "Doreen_Sprite_Head", #(75,-10)
        )
    transform_anchor True
    anchor (0.45, 0.35)#(0.6, 1.0)
    xoffset -675#-520
    yoffset -805#-670
    zoom 1.75  #1.5
    rotate 0
# image Doreen_BJ_Backdrop # image Doreen_BJ_Backdrop # image Doreen_BJ_Backdrop End # image Doreen_BJ_Backdrop # image Doreen_BJ_Backdrop End

# image Doreen_BJ_Backdrop # image Doreen_BJ_Backdrop # image Doreen_BJ_Backdrop End # image Doreen_BJ_Backdrop # image Doreen_BJ_Backdrop End



image Doreen_BJ_Head:
    #These are all the details of the face, over
    LiveComposite(
        (695,695),
        (-90,480), ConditionSwitch(
            "renpy.showing('Doreen_BJ_Animation') and Speed > 1",Null(),
#            "renpy.showing('Doreen_BJ_Animation') and (Speed == 3 or Speed == 4 or Speed == 6)",Null(),
            "True", "Doreen_BJ_Head_Under"
            ),

        (0,0), ConditionSwitch(
            # Basic Face layer
            "DoreenX.Blush and renpy.showing('Doreen_BJ_Animation') and (Speed == 3 or Speed == 4 or Speed == 6)","images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_BJ_Head_Over_Blush.png",
            "renpy.showing('Doreen_BJ_Animation') and (Speed == 3 or Speed == 4 or Speed == 6)","images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_BJ_Head_Over.png",
            "DoreenX.Blush and renpy.showing('Doreen_BJ_Animation') and (Speed == 2 or Speed == 5)","images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_BJ_Head_Heading_Blush.png",
            "renpy.showing('Doreen_BJ_Animation') and (Speed == 2 or Speed == 5)","images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_BJ_Head_Heading.png",
#            "True","images/DoreenBJFace/Doreen_BJ_Head_Sucking_Overlay.png",

#            "DoreenX.Blush == 2", "images/DoreenBJFace/Doreen_BJ_Head_Sucking_Over_Blush2.png",
            "DoreenX.Blush", "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_BJ_Head_Blush.png",
            "True", "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_BJ_Head.png"
            ),

        (0,0), ConditionSwitch(
            #Mouth
#            "True", Null(), #cumming
            "Speed and renpy.showing('Doreen_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
#                    "Speed == 1", "images/DoreenBJFace/Doreen_BJ_Mouth_TongueW.png",  #licking
                    "Speed == 1", "images/DoreenBJFace/Doreen_BJ_Mouth_Tongue.png",  #licking
                    "Speed == 2 or Speed == 5", "images/DoreenBJFace/Doreen_BJ_Mouth_Over.png",  #licking
                    "True", Null(),                          #heading
#                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
#                    "Speed == 3", "images/DoreenBJFace/Doreen_BJ_Mouth_Sucking.png", #sucking
#                    "Speed == 4", "images/DoreenBJFace/Doreen_BJ_Mouth_Sucking.png", #deepthroat
#                    "Speed == 6", "images/DoreenBJFace/Doreen_BJ_Mouth_Sucking.png", #cumming
                    ),
            "renpy.showing('Doreen_CUN_Animation') and Speed", "images/DoreenBJFace/Doreen_BJ_Mouth_Tongue.png",
            "Speed >= 3 and renpy.showing('Doreen_TJ_Animation')", "images/DoreenBJFace/Doreen_BJ_Mouth_Tongue.png",
#            "DoreenX.Mouth == 'normal'", "images/DoreenBJFace/Doreen_BJ_Mouth_Smile.png",
            "DoreenX.Mouth == 'lipbite'", "images/DoreenBJFace/Doreen_BJ_Mouth_Smirk.png",
            "DoreenX.Mouth == 'sucking'", "images/DoreenBJFace/Doreen_BJ_Mouth_Open.png",
            "DoreenX.Mouth == 'kiss'", "images/DoreenBJFace/Doreen_BJ_Mouth_Kiss.png",
            "DoreenX.Mouth == 'sad'", "images/DoreenBJFace/Doreen_BJ_Mouth_Sad.png",
#            "DoreenX.Mouth == 'smile'", "images/DoreenBJFace/Doreen_BJ_Mouth_Smile.png",
            "DoreenX.Mouth == 'smirk'", "images/DoreenBJFace/Doreen_BJ_Mouth_Smirk.png",
#            "DoreenX.Mouth == 'grimace'", "images/DoreenBJFace/Doreen_BJ_Mouth_Smile.png",
            "DoreenX.Mouth == 'surprised'", "images/DoreenBJFace/Doreen_BJ_Mouth_Open.png",
            "DoreenX.Mouth == 'tongue'", "images/DoreenBJFace/Doreen_BJ_Mouth_Tongue.png",
            "True", "images/DoreenBJFace/Doreen_BJ_Mouth_Smile.png",
            ),
        (0,0), ConditionSwitch(
            #Spunk layer
            "'mouth' not in DoreenX.Spunk or not Player.Male", Null(),
            "Speed and renpy.showing('Doreen_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
                    "Speed == 1", "images/DoreenBJFace/Doreen_BJ_Spunk_Tongue.png",  #licking
#                    "True", Null(),                          #heading
                    "(Speed == 2 or Speed == 5)", "Doreen_BJ_Heading_Spunk",                          #heading
#                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", "images/DoreenBJFace/Doreen_BJ_Spunk_Sucking.png", #sucking
                    "Speed == 4", "images/DoreenBJFace/Doreen_BJ_Spunk_Sucking.png", #deepthroat
                    "Speed == 6", "images/DoreenBJFace/Doreen_BJ_Spunk_Sucking.png", #cumming
                    ),
#            "DoreenX.Mouth == 'normal'", "images/DoreenBJFace/Doreen_BJ_Spunk_Smile.png",
#            "DoreenX.Mouth == 'lipbite'", "images/DoreenBJFace/Doreen_BJ_Spunk_Smile.png",
            "DoreenX.Mouth == 'kiss'", "images/DoreenBJFace/Doreen_BJ_Spunk_Kiss.png",
            "DoreenX.Mouth == 'sad'", "images/DoreenBJFace/Doreen_BJ_Spunk_Kiss.png",
#            "DoreenX.Mouth == 'smile'", "images/DoreenBJFace/Doreen_BJ_Spunk_Smile.png",
#            "DoreenX.Mouth == 'smirk'", "images/DoreenBJFace/Doreen_BJ_Spunk_Kiss.png",
            "DoreenX.Mouth == 'surprised'", "images/DoreenBJFace/Doreen_BJ_Spunk_Open.png",
            "DoreenX.Mouth == 'open'", "images/DoreenBJFace/Doreen_BJ_Spunk_Open.png",
            "DoreenX.Mouth == 'tongue'", "images/DoreenBJFace/Doreen_BJ_Spunk_Tongue.png",
            "DoreenX.Mouth == 'sucking'", "images/DoreenBJFace/Doreen_BJ_Spunk_Tongue.png",
            "True", "images/DoreenBJFace/Doreen_BJ_Spunk_Smirk.png",
            ),
        (0,0), ConditionSwitch(
            #wet face
            "Player.Male", Null(),
            "'mouth' not in DoreenX.Spunk and 'chin' not in DoreenX.Spunk", Null(),
#            "'chin' not in DoreenX.Spunk and (DoreenX.Mouth == 'tongue' or Speed)", "images/DoreenBJFace/Doreen_BJ_Wet_Tongue.png",
#            "DoreenX.Mouth == 'tongue' or Speed", "images/DoreenBJFace/Doreen_BJ_Wet_Tongue2.png",
            "'mouth' in DoreenX.Spunk or 'chin' in DoreenX.Spunk", "images/DoreenBJFace/Doreen_BJ_Wet_Mouth.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Brows
            "DoreenX.Brows == 'angry'", "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_BJ_Brows_Angry.png",
            "DoreenX.Brows == 'sad'", "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_BJ_Brows_Sad.png",
            "DoreenX.Brows == 'surprised'", "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_BJ_Brows_Surprised.png",
            "DoreenX.Brows == 'confused'", "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_BJ_Brows_Confused.png",
            "True", "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_BJ_Brows_Normal.png",
            ),
        (0,0),"Doreen BJ Blink",
            #Eyes
        (0,0), ConditionSwitch(
            #Hair overlay
            "DoreenX.Hat == 'headband' and (DoreenX.Water or DoreenX.Hair == 'wet' or DoreenX.Hair == 'wetlong')", "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_BJ_Hair_Wet_H.png",
            "DoreenX.Water or DoreenX.Hair == 'wet' or DoreenX.Hair == 'wetlong'", "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_BJ_Hair_Wet.png",
            "DoreenX.Hat == 'headband' and (not Player.Male and 'facial' in DoreenX.Spunk)","images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_BJ_Hair_Wet_H.png",
            "not Player.Male and 'facial' in DoreenX.Spunk","images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_BJ_Hair_Wet.png",
            "DoreenX.Hat == 'headband'", "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_BJ_Hair_Short_H.png",
            "True", "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_BJ_Hair_Short.png",
            ),

        (0,0), ConditionSwitch(
            #glasses
            "DoreenX.Hat == 'glasses'","images/DoreenBJFace/Doreen_BJ_Glasses.png",
            "True", Null(),
            ),
        (0,0),"images/DoreenBJFace/Doreen_BJ_Earring.png",
        (0,0), ConditionSwitch(
            # water overlay
            "DoreenX.Water", "images/DoreenBJFace/Doreen_BJ_Wet.png",
            "not Player.Male and 'facial' in DoreenX.Spunk", "images/DoreenBJFace/Doreen_BJ_Wet.png",
            "True",Null(),
            ),

#        (0,0), "Doreen_Tester",
        (0,0), ConditionSwitch(
            #cum on the face
            "'hair' in DoreenX.Spunk and Player.Male", "images/DoreenBJFace/Doreen_BJ_Spunk_Hair.png",
            "'facial' in DoreenX.Spunk and Player.Male", "images/DoreenBJFace/Doreen_BJ_Spunk_Facial.png",
            "True", Null(),
            ),
        # Modification mode
        (0,0), ConditionSwitch(
            #facial fix
            "DoreenX.Fix", "images/DoreenBJFace/modification/Doreen_BJ_Head_Head_Fix.png",
            "True", Null(),
            ),
        # -----------------
        (250,400), ConditionSwitch( #(250,400)(-500,-400)
            #steam
            "True", "Big_Steam",
            "DoreenX.Lust > 70", "Big_Steam",
            "True", Null(),
            ),
        )
    zoom 1
    anchor (0.5, 0.5)
    offset (90,-480)

# image Doreen_BJ_Head End        # image Doreen_BJ_Head End        # image Doreen_BJ_Head End        # image Doreen_BJ_Head End

#image Doreen_Tester:
#            "images/DoreenBJFace/Doreen_BJ_tester.jpg"
#            alpha 0.5
image Doreen BJ Blink:
        #eyeblinks
        ConditionSwitch(
            "DoreenX.Eyes == 'normal'", "images/DoreenBJFace/Doreen_BJ_Eyes_Normal.png",
            "DoreenX.Eyes == 'sexy'", "images/DoreenBJFace/Doreen_BJ_Eyes_Sexy.png",
            "DoreenX.Eyes == 'closed'", "images/DoreenBJFace/Doreen_BJ_Eyes_Closed.png",
            "DoreenX.Eyes == 'surprised'", "images/DoreenBJFace/Doreen_BJ_Eyes_Surprised.png",
            "DoreenX.Eyes == 'side'", "images/DoreenBJFace/Doreen_BJ_Eyes_Side.png",
            "DoreenX.Eyes == 'leftside'", "images/DoreenBJFace/Doreen_BJ_Eyes_Side.png",
            "DoreenX.Eyes == 'stunned'", "images/DoreenBJFace/Doreen_BJ_Eyes_Stunned.png",
            "DoreenX.Eyes == 'down'", "images/DoreenBJFace/Doreen_BJ_Eyes_Down.png",
            "DoreenX.Eyes == 'manic'", "images/DoreenBJFace/Doreen_BJ_Eyes_Surprised.png",
            "DoreenX.Eyes == 'squint'", "images/DoreenBJFace/Doreen_BJ_Eyes_Sexy.png",
            "True", "images/DoreenBJFace/Doreen_BJ_Eyes_Normal.png",
            ),
        choice:
            3.5
        choice:
            3.25
        choice:
            3
        "images/DoreenBJFace/Doreen_BJ_Eyes_Closed.png"
        .25
        repeat

#image Doreen_BJ_HairBack:
#    LiveComposite(
#        (695,695),

#        (0,0), ConditionSwitch(
#            #Hair overlay
##            "DoreenX.Water or DoreenX.Hair == 'wet'", "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_BJ_Hair_Wet.png",
##            "not Player.Male and 'facial' in DoreenX.Spunk","images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_BJ_Hair_Wet.png",
#            "True", Null(),
#            ),

#        )
#    zoom 1
#    anchor (0.5, 0.5)
#    offset (90,-480)

image Doreen_BJ_Head_Under:
    LiveComposite(
        (695,695),
#        (0,0), "images/DoreenBJFace/Doreen_BJ_Head_Sucking_Under.png",
        (0,0), "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_BJ_Head.png",
#         (0,0), ConditionSwitch(
#            # Basic Face layer
#            "Speed and renpy.showing('Doreen_BJ_Animation') and Speed != 1 and Speed != 2 and Speed != 5","images/DoreenBJFace/Doreen_BJ_Head_Sucking_Overlay.png",
##            "True","images/DoreenBJFace/Doreen_BJ_Head_Sucking_Overlay.png",
#            "DoreenX.Blush == 2", "images/DoreenBJFace/Doreen_BJ_Head_Blush2.png",
#            "DoreenX.Blush", "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_BJ_Head_Blush.png",
#            "True", "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_BJ_Head.png"
#            ),

         (0,0), ConditionSwitch(
            #cum on the chin
            "'chin' in DoreenX.Spunk and Player.Male", "images/DoreenBJFace/Doreen_BJ_Spunk_Chin.png",
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #cum on the chin
#            "'chin' in DoreenX.Spunk and Player.Male", "images/DoreenBJFace/Doreen_BJ_Spunk_Chin.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #Spunk layer
#            "'mouth' not in DoreenX.Spunk or not Player.Male", Null(),
#            "True", "images/DoreenBJFace/Doreen_BJ_Spunk_SuckingUnder.png",
#            ),
#        (0,0), "images/DoreenBJFace/Doreen_BJ_Mouth_Open.png",
        )
    zoom 1
    anchor (0.5, 0.5)
    offset (90,-480)

image Doreen_BJ_Heading_Mouth:
    LiveComposite(
        (695,695),
        (0,0), "images/DoreenBJFace/Doreen_BJ_Mouth_Heading.png",
        (0,0), ConditionSwitch(
            #cum in mouth
            "'mouth' in DoreenX.Spunk and Player.Male", "images/DoreenBJFace/Doreen_BJ_Spunk_Open.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Hair overlay
#            "True", "images/DoreenBJFace/Doreen_BJ_Hair_Short_Back.png",
#            ),
        )
    zoom 1
    anchor (0.5, 0.5)
    offset (90,-480)

image Doreen_BJ_Heading_Spunk:
        "images/DoreenBJFace/Doreen_BJ_Spunk_Sucking.png"
        yoffset -8

## End Doreen BJ Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_BJ_Anim0:
        #Static animation
#        contains:
#                # Doreen's hair back
#                "Doreen_BJ_HairBack"
#                subpixel True
##                alpha .9
#                offset (-90,-105)     #top (350,190), - is up
#                rotate 5
#                parallel:
#                    ease 1 offset (-90,-90)           #bottom
#                    pause .2
#                    ease 1.5 offset (-90,-105)     #top
#                    repeat
#                parallel:
#                    ease 1 rotate 0          #bottom
#                    pause .2
#                    ease 1.5 rotate 5    #top
#                    repeat
        contains:
                #  Doreen's body, everything below the chin
                "Doreen_BJ_Backdrop"
                subpixel True
                offset (-60,-60)     #top
                alpha 1
                transform_anchor True
                rotate 0
                parallel:
                    ease 1 offset (-60,-50)           #bottom
                    pause .2
                    ease 1.5 offset (-60,-60)     #top
                    repeat
#                parallel:
#                    ease 1 rotate -10
#                    pause .2
#                    ease 1.5 rotate -5#-20
#                    repeat
        contains:
                # head overlay
                "Doreen_BJ_Head"
#                AlphaMask("Doreen_BJ_Head", "Doreen_BJ_MaskHeadingComposite") #"Doreen_BJ_MouthHeadingComposite")
                subpixel True
#                alpha .9
                offset (-90,-105)     #top (350,190), - is up
                rotate 5
                parallel:
                    ease 1 offset (-90,-90)           #bottom
                    pause .2
                    ease 1.5 offset (-90,-105)     #top
                    repeat
                parallel:
                    ease 1 rotate 0          #bottom
                    pause .2
                    ease 1.5 rotate 5    #top
                    repeat
        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Doreen_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                rotate 0
                parallel:
                    pause 1
                    ease .2 rotate .5
#                    pause .2
                    ease .3 rotate -0.2
                    ease .3 rotate 0
                    pause .9
                    repeat
#end Doreen_BJ_Anim0 Static

image Doreen_BJ_Anim1:
        #Licking animation
#        contains:
#                # Doreen's hair back
#                "Doreen_BJ_HairBack"
#                subpixel True
##                alpha .9
#                offset (15,-105)     #top (350,190), - is up
#                rotate 16
#                parallel:
#                    ease 1.3 xoffset 15           #bottom
#                    ease .8 xoffset 5           #bottom
#                    ease .5 xoffset 40     #top
#                    ease 1.6 xoffset 15     #top
#                    repeat
#                parallel: #4.2
#                    ease 1 yoffset -5           #bottom
#                    pause .4
#                    ease 1.5 yoffset -125     #top
#                    ease 1.3 yoffset -105     #top
#                    repeat
#                parallel:
#                    easein 1.3 rotate 13          #bottom
#                    ease .8 rotate 10    #top
#                    ease .5 rotate 28          #bottom
#                    ease .3 rotate 26          #bottom
#                    pause .1
#                    ease 1.2 rotate 16    #top
#                    repeat
        contains:
                #  Doreen's body, everything below the chin
                "Doreen_BJ_Backdrop"
                subpixel True
                offset (-5,-60)     #top
                alpha 1
                transform_anchor True
#                rotate -20
#                parallel: #2.4 down, 1.8 up
#                    ease 1 xoffset -40           #bottom
#                    pause 1.4
##                    ease 1 xoffset -40     #top
#                    ease .3 xoffset -45     #top
#                    pause .3
#                    ease 1.2 xoffset -60     #top
#                    repeat
                parallel:
                    ease .9 yoffset 0           #bottom
                    pause .5
                    ease 1.6 yoffset -60     #top
                    pause .2
                    ease 1 yoffset -50           #bottom
                    repeat
#                parallel:
#                    ease .2 rotate -5          #bottom
#                    ease 1.0 rotate -20          #bottom
#                    ease 1.0 rotate -15          #bottom
#                    ease .5 rotate -5          #bottom
#                    pause 1.5
#                    repeat
        contains:
                # head overlay
                "Doreen_BJ_Head"
#                AlphaMask("Doreen_BJ_Head", "Doreen_BJ_MaskHeadingComposite") #"Doreen_BJ_MouthHeadingComposite")
                subpixel True
#                alpha .9
                offset (15,-105)     #top (350,190), - is up
                rotate 16
                parallel:
                    ease 1.3 xoffset 15           #bottom
                    ease .8 xoffset 5           #bottom
                    ease .5 xoffset 40     #top
                    ease 1.6 xoffset 15     #top
                    repeat
                parallel: #4.2
                    ease 1 yoffset -5           #bottom
                    pause .4
                    ease 1.5 yoffset -125     #top
                    ease 1.3 yoffset -105     #top
                    repeat
                parallel:
                    easein 1.3 rotate 13          #bottom
                    ease .8 rotate 10    #top
                    ease .5 rotate 28          #bottom
                    ease .3 rotate 26          #bottom
                    pause .1
                    ease 1.2 rotate 16    #top
                    repeat
        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Doreen_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                rotate 0
                parallel:
#                    pause 2.5
                    pause .3
                    ease .7 rotate -3
                    pause .5
                    ease .9 rotate -2           #bottom
                    pause .1
                    ease .2 rotate -2
                    ease .3 rotate 1
                    ease .2 rotate 0
                    pause 1
                    repeat
#end Doreen_BJ_Anim1 Licking


image Doreen_BJ_Anim2:
        #Heading animation
#        contains:
#                # Doreen's head Underlay
#                "Doreen_BJ_HairBack"
#                subpixel True
#                offset (-90,-130)     #top (-20,130), - is up
#                rotate 0
#                parallel:
#                    ease 1 yoffset -90#400    #bottom
#                    pause .4
#                    ease 1 yoffset -130         #top
#                    repeat
##                parallel:
##                    ease .4 rotate 5          #bottom
##                    pause .1
##                    ease .5 rotate 0    #top
##                    repeat
        contains:
                #  Doreen's body, everything below the chin
                "Doreen_BJ_Backdrop"
                subpixel True
                offset (-60,-60)     #top (-20,130), - is up
                alpha 1
                transform_anchor True
                rotate 0
#                parallel:
#                    ease .4 rotate -30
#                    pause .05
#                    ease .55 rotate -20#-20
#                    repeat
                parallel:
                    ease 1 yoffset -40#-90   #bottom
                    pause .4
                    ease 1 yoffset -60#-130         #top
                    repeat
        contains:
                # Doreen's head Underlay
                "Doreen_BJ_Head_Under"
                subpixel True
                offset (-90,-130)     #top (-20,130), - is up
                rotate 0
                parallel:
                    ease 1 yoffset -90#400    #bottom
                    pause .4
                    ease 1 yoffset -130         #top
                    repeat
#                parallel:
#                    ease .4 rotate 5          #bottom
#                    pause .1
#                    ease .5 rotate 0    #top
#                    repeat
        contains:
                # Doreen's open mouth
                "Doreen_BJ_Heading_Mouth"
                subpixel True
                transform_anchor True
                anchor (350,640)#(350,630)
                pos (0,293) #(-64,283)
                offset (-85,-130)     #top (-20,130), - is up
                rotate 0
                xzoom 1
                yzoom 1
                parallel:
                    ease 1 xzoom 1.2    #bottom
                    pause .4
                    ease 1 xzoom .8      #top
                    repeat
#                parallel:
#                    ease 1 xzoom 1    #bottom
#                    pause .4
#                    ease 1 xzoom .8      #top
#                    repeat
                parallel:
                    ease 1 yzoom 1.2    #bottom
                    pause .4
                    ease 1 yzoom 1      #top
                    repeat
                parallel:
                    ease 1 yoffset -90#400    #bottom
                    pause .4
                    ease 1 yoffset -130         #top
                    repeat
        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Doreen_TJ_ZeroCock"
                offset(0,0)
                transform_anchor True
                rotate -1
                alpha 1
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
#                "Doreen_BJ_Heading_Overlay"
##                AlphaMask("Doreen_BJ_Head", "Doreen_BJ_MaskHeadingComposite") #"Doreen_BJ_MouthHeadingComposite")
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
#        contains:
#                # head overlay
#                "Doreen_BJ_Head"
##                AlphaMask("Doreen_BJ_Head", "Doreen_BJ_MaskHeadingComposite") #"Doreen_BJ_MouthHeadingComposite")
#                subpixel True
#                alpha 1
#                offset (-20,130)     #top (350,190), - is up
#                rotate 0
#                parallel:
#                    ease 1 yoffset 180#400    #bottom
#                    pause .4
#                    ease 1 yoffset 130         #top
#                    repeat
##                parallel:
##                    ease .4 rotate 5          #bottom
##                    pause .1
##                    ease .5 rotate 0    #top
##                    repeat
        contains:
                # Doreen's head Underlay
                "Doreen_BJ_Head"
                subpixel True
                offset (-90,-130)     #top (-20,130), - is up
                rotate 0
                parallel:
                    ease 1 yoffset -90#400    #bottom
                    pause .4
                    ease 1 yoffset -130         #top
                    repeat
#                parallel:
#                    ease .4 rotate 5          #bottom
#                    pause .1
#                    ease .5 rotate 0    #top
#                    repeat
#end Doreen_BJ_Anim2 Heading


image Doreen_BJ_Anim3:
        #sucking fast animation
#        contains:
#                # Doreen's head Underlay
#                "Doreen_BJ_HairBack"
#                subpixel True
##                alpha .9
#                offset (-90,-75)     #top (-20,130), - is up
#                rotate 0
#                parallel: #2.7 -> 1.0
#                    ease .4 offset (-90,20)           #bottom
#                    pause .05
#                    ease .55 offset (-90,-75)     #top
#                    repeat #(-20,270)
##                parallel:
##                    ease .4 rotate 5          #bottom
##                    pause .1
##                    ease .5 rotate 0    #top
##                    repeat
        contains:
                #  Doreen's body, everything below the chin
                "Doreen_BJ_Backdrop"
                subpixel True
                offset (-60,-50)     #top (-20,130), - is up
                alpha 1
                transform_anchor True
#                rotate -20
#                parallel:
#                    ease .4 rotate -30
#                    pause .05
#                    ease .55 rotate -20#-20
#                    repeat
                parallel:
                    ease .35 yoffset 0#400           #bottom
                    pause .05
                    ease .6 yoffset -50     #top
                    repeat
        contains:
                # Doreen's head Underlay
                "Doreen_BJ_Head_Under"
                subpixel True
                offset (-90,-75)     #top (350,190), - is up
                rotate 0
                parallel: #2.7 -> 1.0
                    ease .4 offset (-90,20)           #bottom
                    pause .05
                    ease .55 offset (-90,-75)     #top
                    repeat #(-20,270)
#                parallel:
#                    ease .4 rotate 5          #bottom
#                    pause .1
#                    ease .5 rotate 0    #top
#                    repeat
        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Doreen_TJ_ZeroCock"
                offset(0,0)
                transform_anchor True
                rotate 0
#                parallel:
#                    pause .1
#                    ease .3 rotate 2
#                    ease .4 rotate 0
#                    pause .2
#                    repeat
                parallel:
                    pause .1
                    ease .3 yoffset 20
                    ease .5 yoffset 0
                    pause .1
                    repeat
        contains:
                # head overlay
                "Doreen_BJ_Head"
#                AlphaMask("Doreen_BJ_Head", "Doreen_BJ_MaskHeadingComposite") #"Doreen_BJ_MouthHeadingComposite")
                subpixel True
#                alpha .9
                offset (-90,-75)     #top (-20,130), - is up
                rotate 0
                parallel: #2.7 -> 1.0
                    ease .4 offset (-90,20)           #bottom
                    pause .05
                    ease .55 offset (-90,-75)     #top
                    repeat #(-20,270)
#                parallel:
#                    ease .4 rotate 5          #bottom
#                    pause .1
#                    ease .5 rotate 0    #top
#                    repeat
##end Doreen_BJ_Anim3 Sucking

image Doreen_BJ_Anim4:
        #Deep animation
#        contains:
#                # Doreen's head Underlay
#                "Doreen_BJ_HairBack"
#                subpixel True
##                alpha .9
#                offset (-90,80)     #top (-20,130), - is up
#                rotate 0
#                parallel: #2.7s
#                    ease 1 offset (-90,230)          #bottom
#                    pause .2
#                    ease 1.5 offset (-90,80)     #top
#                    repeat #(-20,270)
##                parallel:
##                    ease 1 rotate 20          #bottom
##                    pause .2
##                    ease 1.5 rotate 0    #top
##                    repeat
        contains:
                #  Doreen's body, everything below the chin
                "Doreen_BJ_Backdrop"
                subpixel True
                offset (-60,-40)     #top
                alpha 1
                transform_anchor True
#                rotate -20
#                parallel:
#                    ease 1 rotate -45
#                    pause .2
#                    ease 1.5 rotate -20#-20
#                    repeat
                parallel:
                    ease 1 yoffset 50#400           #bottom
                    pause .2
                    ease 1.5 yoffset -40     #top
                    repeat
        contains:
                # Doreen's head Underlay
                "Doreen_BJ_Head_Under"
                subpixel True
                offset (-90,80)     #top (-20,130), - is up
                rotate 0
                parallel: #2.7s
                    ease 1 offset (-90,230)          #bottom
                    pause .2
                    ease 1.5 offset (-90,80)     #top
                    repeat #(-20,270)
#                parallel:
#                    ease 1 rotate 20          #bottom
#                    pause .2
#                    ease 1.5 rotate 0    #top
#                    repeat
        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Doreen_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                rotate 0
#                parallel:
#                    pause .2
#                    ease .8 rotate 15
#                    pause .2
#                    ease 1.2 rotate 0
#                    pause .3
#                    repeat
        contains:
                # head overlay
                "Doreen_BJ_Head"
#                AlphaMask("Doreen_BJ_Head", "Doreen_BJ_MaskHeadingComposite") #"Doreen_BJ_MouthHeadingComposite")
                subpixel True
#                alpha .9
                offset (-90,80)     #top (-20,130), - is up
                rotate 0
                parallel: #2.7s
                    ease 1 offset (-90,230)          #bottom
                    pause .2
                    ease 1.5 offset (-90,80)     #top
                    repeat #(-20,270)
#                parallel:
#                    ease 1 rotate 20          #bottom
#                    pause .2
#                    ease 1.5 rotate 0    #top
#                    repeat
#end Doreen_BJ_Anim4 Deep


image Doreen_BJ_Anim5:
        #Cum high animation
#        contains:
#                # Doreen's head Underlay
#                "Doreen_BJ_HairBack"
#                subpixel True
#                offset (-90,-130)     #top (-20,130), - is up
#                rotate 0
#                parallel:
#                    ease 1.5 yoffset -90#400    #bottom
#                    pause .2
#                    ease 1.5 yoffset -110         #top
#                    repeat
#        contains:
#                #  Doreen's body, everything below the chin
#                "Doreen_BJ_Backdrop"
#                subpixel True
#                offset (-60,-60)     #top (-20,130), - is up
#                alpha 1
#                transform_anchor True
#                rotate 0
#                parallel:
#                    ease 1.5 yoffset -40#-90   #bottom
#                    pause .2
#                    ease 1.5 yoffset -50#-130         #top
#                    repeat
        contains:
                # Doreen's head Underlay
                "Doreen_BJ_Head_Under"
                subpixel True
                offset (-90,-130)     #top (-20,130), - is up
                rotate 0
                parallel:
                    ease 1.5 yoffset -90#400    #bottom
                    pause .2
                    ease 1.5 yoffset -110         #top
                    repeat
        contains:
                # Doreen's open mouth
                "Doreen_BJ_Heading_Mouth"
                subpixel True
                transform_anchor True
                anchor (350,640)#(285,365)
                pos (0,293) #(-64,13)
                offset (-85,-130)     #top (-20,130), - is up
                rotate 0
                xzoom 1
                yzoom 1
                parallel:
                    ease 1.5 xzoom 1    #bottom
                    pause .2
                    ease 1.5 xzoom .8     #top
                    repeat
                parallel:
                    ease 1.5 yzoom 1.2    #bottom
                    pause .2
                    ease 1.5 yzoom 1      #top
                    repeat
                parallel:
                    ease 1.5 yoffset -90#400    #bottom
                    pause .2
                    ease 1.5 yoffset -110         #top
                    repeat

#        contains:
#                # Doreen's open mouth
#                "Doreen_BJ_Heading_Mouth"
#                subpixel True
#                transform_anchor True
#                anchor (350,640)#(350,630)
#                pos (0,293) #(-64,283)
#                offset (-85,-130)     #top (-20,130), - is up
#                rotate 0
#                xzoom 1
#                yzoom 1
#                parallel:
#                    ease 1 xzoom 1.2    #bottom
#                    pause .4
#                    ease 1 xzoom .8      #top
#                    repeat
##                parallel:
##                    ease 1 xzoom 1    #bottom
##                    pause .4
##                    ease 1 xzoom .8      #top
##                    repeat
#                parallel:
#                    ease 1 yzoom 1.2    #bottom
#                    pause .4
#                    ease 1 yzoom 1      #top
#                    repeat
#                parallel:
#                    ease 1 yoffset -90#400    #bottom
#                    pause .4
#                    ease 1 yoffset -130         #top
#                    repeat
        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Doreen_TJ_ZeroCock"
                offset(0,0)
                transform_anchor True
                rotate -1
                alpha 1
#                parallel:
#                    easeout .4 rotate 0    #bottom
#                    pause 1.6
#                    easein .4 rotate -1      #top
#                    repeat
#                parallel:
#                    pause .1
#                    ease .3 yoffset 20
#                    ease .5 yoffset 0
#                    pause .1
#                    repeat
        contains:
                # Doreen's head Underlay
                "Doreen_BJ_Head"
                subpixel True
                offset (-90,-130)     #top (-20,130), - is up
                rotate 0
                parallel:
                    ease 1.5 yoffset -90#400    #bottom
                    pause .2
                    ease 1.5 yoffset -110         #top
                    repeat
#        contains:
#                # mouth area overlay
#                "Doreen_BJ_Heading_Overlay"
##                AlphaMask("Doreen_BJ_Head", "Doreen_BJ_MaskHeadingComposite") #"Doreen_BJ_MouthHeadingComposite")
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
#        contains:
#                # head overlay
#                "Doreen_BJ_Head"
##                AlphaMask("Doreen_BJ_Head", "Doreen_BJ_MaskHeadingComposite") #"Doreen_BJ_MouthHeadingComposite")
#                subpixel True
#                alpha 1
#                offset (-20,130)     #top (350,190), - is up
#                rotate 0
#                parallel:
#                    ease 1 yoffset 180#400    #bottom
#                    pause .4
#                    ease 1 yoffset 130         #top
#                    repeat
##                parallel:
##                    ease .4 rotate 5          #bottom
##                    pause .1
##                    ease .5 rotate 0    #top
##                    repeat
#end Doreen_BJ_Anim5 Cum high


image Doreen_BJ_Anim6:
        #Cum Deep animation
#        contains:
#                # Doreen's head Underlay
#                "Doreen_BJ_HairBack"
#                subpixel True
##                alpha .9
#                offset (-90,200)     #top (-20,130), - is up
#                rotate 0
#                parallel: #2.7s
#                    ease 1.1 offset (-90,230)          #bottom
#                    pause .2
#                    ease .7 offset (-90,200)     #top
#                    repeat #(-20,270)
        contains:
                #  Doreen's body, everything below the chin
                "Doreen_BJ_Backdrop"
                subpixel True
                offset (-60,110)     #top
                alpha 1
                transform_anchor True
#                rotate -20
#                parallel:
#                    ease 1 rotate -45
#                    pause .2
#                    ease 1.5 rotate -20#-20
#                    repeat
                parallel:
                    ease 1 yoffset 120#400           #bottom
                    pause .2
                    ease .8 yoffset 110     #top
                    repeat
        contains:
                # Doreen's head Underlay
                "Doreen_BJ_Head_Under"
                subpixel True
                offset (-90,200)     #top (-20,130), - is up
                rotate 0
                parallel: #2.7s
                    ease 1.1 offset (-90,230)          #bottom
                    pause .2
                    ease .7 offset (-90,200)     #top
                    repeat #(-20,270)
#                parallel:
#                    ease 1 rotate 20          #bottom
#                    pause .2
#                    ease 1.5 rotate 0    #top
#                    repeat
        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Doreen_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                rotate 0
#                parallel:
#                    pause .2
#                    ease .8 rotate 15
#                    pause .2
#                    ease 1.2 rotate 0
#                    pause .3
#                    repeat
        contains:
                # head overlay
                "Doreen_BJ_Head"
#                AlphaMask("Doreen_BJ_Head", "Doreen_BJ_MaskHeadingComposite") #"Doreen_BJ_MouthHeadingComposite")
                subpixel True
#                alpha .9
                offset (-90,200)     #top (-20,130), - is up
                rotate 0
                parallel: #2.7s
                    ease 1.1 offset (-90,230)          #bottom
                    pause .2
                    ease .7 offset (-90,200)     #top
                    repeat #(-20,270)
#                parallel:
#                    ease 1 rotate 20          #bottom
#                    pause .2
#                    ease 1.5 rotate 0    #top
#                    repeat
#end Doreen_BJ_Anim6 Cum Deep

#Head and Body Animations for Doreen's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
#                                                               #BJ Launchers
##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Doreen_BJ_Launch(Line = Trigger):    # The sequence to launch the Doreen BJ animations

##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    return
##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary

    if renpy.showing("Doreen_BJ_Animation") and DoreenX.Pose != "69":
        return
    elif renpy.showing("Doreen_69_Animation") and DoreenX.Pose == "69":
        return

    if not Player.Male:
        call Doreen_CUN_Launch
        return

    if renpy.showing("Doreen_TJ_Animation"):
            hide Doreen_TJ_Animation
    else:
            call Girl_Hide(DoreenX)
            if Line == "L" or Line == "cum":
                show Doreen_Sprite at SpriteLoc(StageCenter) zorder 150:
                    alpha 1
                    ease 1 zoom 2.5 offset (150,80)
                with dissolve
            else:
                show Doreen_Sprite at SpriteLoc(StageCenter) zorder 150:
                    alpha 1 zoom 2.5 offset (150,80)
                with dissolve
            hide Doreen_Sprite
    #". . ."
    $ Speed = 0
    $ Player.Sprite = 1

    if Line != "cum":
        $ Trigger = "blow"

#    show Doreen_BJ_Animation zorder 150:
#        pos (630,650) #(645,510)


    $ Player.Cock = 0
    if DoreenX.Pose == "69":
            show Doreen_69_Animation zorder 150
    else:
            show Doreen_BJ_Animation zorder 150:
                pos (1000,1050)#(1000,1000)#(700,520)


    if Taboo and Line == "L": # Doreen gets started. . .
            if len(Present) >= 2:
                if Present[0] != DoreenX:
                        "[DoreenX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                elif Present[1] != DoreenX:
                        "[DoreenX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
            else:
                        "[DoreenX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
            "Затем она наклоняется и берет ваш член в свой рот."
    elif Line == "L":
            "[DoreenX.Name] плавно наклоняется и прислоняет ваш член к своей щеке."

    return

label Doreen_BJ_Reset: # The sequence to the Doreen animations from BJ to default
    if Player.Male != 1:
            call Doreen_CUN_Reset
    if not renpy.showing("Doreen_BJ_Animation") and not renpy.showing("Doreen_69_Animation"):
        return
#    hide Doreen_BJ_Animation
    call Girl_Hide(DoreenX)
    $ Speed = 0

    show Doreen_Sprite at SpriteLoc(StageCenter) zorder 150:
        alpha 1 zoom 2.5 offset (150,80)
    with dissolve

    show Doreen_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .2
        ease .3 zoom 1 offset (0,0)
    pause 1.5
    show Doreen_Sprite at SpriteLoc(DoreenX.SpriteLoc) zorder DoreenX.Layer:
        alpha 1 zoom 1 offset (0,0)
    return

# End Doreen Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Doreen's TJ animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Animation components / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# start base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_TJ_Animation:
            #core TJ animation
            contains:
                ConditionSwitch(
                    # Doreen's upper body
                    "not Player.Sprite","Doreen_TJ_0",#Static
                    "Speed == 1", "Doreen_TJ_1",#slow
                    "Speed == 3", "Doreen_TJ_3",#licking
                    "Speed == 4", "Doreen_TJ_4",#cumming high
                    "Speed == 5", "Doreen_TJ_5",#cumming low
                    "Speed >= 2", "Doreen_TJ_2",#fast
                    "True",       "Doreen_TJ_0",#Static
                    )
            zoom .8 #.7
            transform_anchor True
            anchor (.5,.5)
# end base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#image Doreen_TJ_Head:
#            #Hair underlay
#            "Doreen_BJ_Head"
#            transform_anchor True
#            zoom .7
#            anchor (0.5, 0.5)
#            offset (30,-450)
#            rotate 0


image Doreen_TJ_ZeroCock:
            #cock used in Doreen's sex pose
            "Zero_Blowcock"
            transform_anchor True
            zoom .6
            anchor (0.5, 0.6)
            offset (-5,50)#(45,50)
            rotate 0


image Doreen_TJ_Body:
    LiveComposite(
        (800,950),       #550,950
#        (-10,-90), "Doreen_BJ_HairBack", #(75,-10)

#        (0,0), "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_TJ_Body.png",

        (0,0), "Doreen_BJ_Ass",
        (0,0), "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_TJ_Body.png",
#        (0,0), ConditionSwitch(
#            #Water effect
#            "DoreenX.Water and DoreenX.ArmPose == 1", "images/DoreenSprite/Doreen_Sprite_Water1.png",
#            "DoreenX.Water", "images/DoreenSprite/Doreen_Sprite_Water2.png",
#            "True", Null(),
#            ),
#        (0,0), "images/DoreenBJFace/Doreen_TJ_RefCock.png",

#        (0,0), ConditionSwitch(
#            # under tit smoosh
#            "not Player.Sprite", Null(),
#            "True", "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_TJ_Tits_Under.png",
#            ),
        (0,0), ConditionSwitch(
            #Chest layer under tits
#            "DoreenX.Over == 'tshirt'", Null(),
#            "DoreenX.Uptop", ConditionSwitch(
#                    # if top is up. . .
#                    "DoreenX.Chest == 'lace bra'", "images/DoreenBJFace/Doreen_TJ_Chest_Lace_Body_Up.png",
#                    "DoreenX.Chest == 'bra'", "images/DoreenBJFace/Doreen_TJ_Chest_Lace_Body_Up.png",
#                    "DoreenX.Chest == 'tank'", "images/DoreenBJFace/Doreen_TJ_Chest_Tank_Body_Up.png",
#                    "DoreenX.Chest == 'swimsuit'", "images/DoreenBJFace/Doreen_TJ_Chest_Bikini_Body_Up.png",
#                    "True", Null(),
#                    ),
            "DoreenX.Chest == 'lace bra'", "images/DoreenBJFace/Doreen_TJ_Chest_Lace_Body.png",
#            "Player.Sprite and renpy.showing('Doreen_TJ_Animation') and DoreenX.Chest == 'tank'", "images/DoreenBJFace/Doreen_TJ_Chest_Tank_Body_Fucking.png",
            "DoreenX.Chest == 'sports bra'", "images/DoreenBJFace/Doreen_TJ_Chest_Sports_Body.png",
            "DoreenX.Chest == 'bikini top'", "images/DoreenBJFace/Doreen_TJ_Chest_Bikini_Body.png",
            "DoreenX.Chest", "images/DoreenBJFace/Doreen_TJ_Chest_Bra_Body.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over body layer
            "DoreenX.Over == 'suit' and DoreenX.Arms", "images/DoreenBJFace/Doreen_TJ_Over_Suit_Body_Gloved.png",
            "DoreenX.Over == 'suit'", "images/DoreenBJFace/Doreen_TJ_Over_Suit_Body.png",

            "DoreenX.Over == 'tshirt'", "images/DoreenBJFace/Doreen_TJ_Over_Tshirt_Body.png",
            "DoreenX.Over == 'sweater'", "images/DoreenBJFace/Doreen_TJ_Over_Sweater_Body.png",
            "DoreenX.Over == 'tube top'", "images/DoreenBJFace/Doreen_TJ_Over_Tube_Body.png",
#            "DoreenX.Over == 'towel'", "images/DoreenBJFace/Doreen_TJ_Over_Towel_Body.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #jacket body layer
            "DoreenX.Acc == 'jacket'", "images/DoreenBJFace/Doreen_TJ_Jacket.png",
            "DoreenX.Acc == 'vest'", "images/DoreenBJFace/Doreen_TJ_Vest.png",
            "True", Null(),
            ),
#        (0,0), "images/DoreenBJFace/Doreen_TJ_RefLine.png",

        (0,0), ConditionSwitch(
            #Hair overlay
            "DoreenX.Hair != 'long' and DoreenX.Hair != 'wetlong'", Null(),
            "DoreenX.Water or DoreenX.Hair == 'wetlong'", "images/DoreenBJFace/Doreen_TJ_Hair_Wet.png",
            "not Player.Male and 'facial' in DoreenX.Spunk","images/DoreenBJFace/Doreen_TJ_Hair_Wet.png",
            "True", "images/DoreenBJFace/Doreen_TJ_Hair_Long.png",
            ),
#        (-10,-90), "Doreen_Sprite_Head", #(75,-10)
        )
    transform_anchor True
    anchor (0.6, 1.0)#(0.6, 0.0)
    xoffset 155#155
    yoffset 125#-600
#    zoom .75  #.76
    rotate 0

#    transform_anchor True
#    zoom 1
#    anchor (0.4, 1.0)
#    #offset (410,770) # (300,275)
#    rotate 0


image Doreen_TJ_Tits_Under:
    LiveComposite(
        (800,950),       #550,950
        (0,0), ConditionSwitch(
            # under tit
            "Player.Sprite and renpy.showing('Doreen_TJ_Animation')", "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_TJ_Tits_Under.png",
            "True", "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_TJ_Tits.png",
            ),
        (0,0), ConditionSwitch(
            #Chest tits layer
            "not DoreenX.Uptop", Null(),
            "DoreenX.Over == 'tshirt'", "images/DoreenBJFace/Doreen_TJ_Over_Tshirt_Mask.png",
            "DoreenX.Chest == 'sports bra'", "images/DoreenBJFace/Doreen_TJ_Chest_Sports_Mask.png",
#            "DoreenX.Chest == 'swimsuit'", "images/DoreenBJFace/Doreen_TJ_Chest_Bikini_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # spunk under tits
            "'tits' not in DoreenX.Spunk", Null(),
            "True", "images/DoreenBJFace/Doreen_TJ_Spunk_Tits.png",
            ),
        )
    transform_anchor True
#    anchor (0.6, 1.0)#(0.6, 0.0)
#    xoffset 155#300
#    yoffset 125#-600
##    zoom .75  #.76
    rotate 0


image Doreen_TJ_Tits_Over:
    LiveComposite(
        (800,950),    #800,950
#        (0,0), ConditionSwitch(
#            # under tit smoosh
#            "DoreenX.Water", Null(),
#            "True", "images/DoreenBJFace/Doreen_TJ_Tit_Under_Smoosh.png",
#            ),
        (0,0), ConditionSwitch(
            # over tit
            "Player.Sprite and renpy.showing('Doreen_TJ_Animation')", "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_TJ_Tits_Over.png",
            "True", Null(),
            ),

#        (0,0),  "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_TJ_TitsRef.png",
        (0,0), ConditionSwitch(
            #Chest tits layer
            "DoreenX.Over == 'tshirt'", Null(),
            "DoreenX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "DoreenX.Chest == 'lace bra'", "images/DoreenBJFace/Doreen_TJ_Chest_Lace_Up.png",
                    "DoreenX.Chest == 'bikini top'", "images/DoreenBJFace/Doreen_TJ_Chest_Bikini_Up.png",
                    "DoreenX.Chest == 'sports bra'", "images/DoreenBJFace/Doreen_TJ_Chest_Bikini_Up.png",
                    "DoreenX.Chest", "images/DoreenBJFace/Doreen_TJ_Chest_Bra_Up.png",
                    "True", Null(),
                    ),
            "DoreenX.Chest == 'lace bra'", "images/DoreenBJFace/Doreen_TJ_Chest_Lace_Tits.png",
            "DoreenX.Chest == 'bikini top'", "images/DoreenBJFace/Doreen_TJ_Chest_Bikini_Tits.png",
            "DoreenX.Chest == 'sports bra'", "images/DoreenBJFace/Doreen_TJ_Chest_Sports_Tits.png",
            "DoreenX.Chest", "images/DoreenBJFace/Doreen_TJ_Chest_Bra_Tits.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Over tits layer
            "DoreenX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "DoreenX.Over == 'tshirt'", "images/DoreenBJFace/Doreen_TJ_Over_Tshirt_Up.png",
                    "DoreenX.Over == 'tube top'", "images/DoreenBJFace/Doreen_TJ_Over_Tube_Up.png",
                    "DoreenX.Over == 'sweater'", "images/DoreenBJFace/Doreen_TJ_Over_Sweater_Up.png",
                    "True", Null(),
                    ),
            "DoreenX.Over == 'tshirt'", "images/DoreenBJFace/Doreen_TJ_Over_Tshirt_Tits.png",
            "DoreenX.Over == 'tube top'", "images/DoreenBJFace/Doreen_TJ_Over_Tube_Tits.png",
            "DoreenX.Over == 'sweater'", "images/DoreenBJFace/Doreen_TJ_Over_Sweater_Tits.png",
            "DoreenX.Over == 'towel' and not Player.Sprite", "images/DoreenBJFace/Doreen_TJ_Over_Towel_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Piercings layer
            "not DoreenX.Pierce", Null(),
            "DoreenX.Pierce == 'ring'", ConditionSwitch(
                    #if it's the ring pericings
                    "DoreenX.Uptop", "images/DoreenBJFace/Doreen_TJ_Pierce_Ring.png",
                    "DoreenX.Over == 'towel'", "images/DoreenBJFace/Doreen_TJ_Pierce_Ring_Green.png",
                    "DoreenX.Over == 'tube top'", "images/DoreenBJFace/Doreen_TJ_Pierce_Ring_Brown.png",
                    "DoreenX.Over == 'sweater'", "images/DoreenBJFace/Doreen_TJ_Pierce_Ring_Sweater.png",
                    "DoreenX.Over == 'tshirt'", "images/DoreenBJFace/Doreen_TJ_Pierce_Ring_Gray.png",
                    "DoreenX.Chest == 'lace bra'", "images/DoreenBJFace/Doreen_TJ_Pierce_Ring_Lace.png",
                    "DoreenX.Chest == 'bikini top' or DoreenX.Chest == 'sports bra'", "images/DoreenBJFace/Doreen_TJ_Pierce_Ring_Green.png",
                    "DoreenX.Chest", "images/DoreenBJFace/Doreen_TJ_Pierce_Ring_Tan.png",
                    "True", "images/DoreenBJFace/Doreen_TJ_Pierce_Ring.png",
                    ),
            "DoreenX.Uptop", "images/DoreenBJFace/Doreen_TJ_Pierce_Barbell.png",
            "DoreenX.Over == 'towel'", "images/DoreenBJFace/Doreen_TJ_Pierce_Barbell_Green.png",
            "DoreenX.Over == 'tube top'", "images/DoreenBJFace/Doreen_TJ_Pierce_Barbell_Brown.png",
                    "DoreenX.Over == 'sweater'", "images/DoreenBJFace/Doreen_TJ_Pierce_Barbell_Sweater.png",
            "DoreenX.Over == 'tshirt'", "images/DoreenBJFace/Doreen_TJ_Pierce_Barbell_Gray.png",
            "DoreenX.Chest == 'lace bra'", "images/DoreenBJFace/Doreen_TJ_Pierce_Barbell_Lace.png",
            "DoreenX.Chest == 'bikini top' or DoreenX.Chest == 'sports bra'", "images/DoreenBJFace/Doreen_TJ_Pierce_Barbell_Green.png",
            "DoreenX.Chest", "images/DoreenBJFace/Doreen_TJ_Pierce_Barbell_Tan.png",
            "True", "images/DoreenBJFace/Doreen_TJ_Pierce_Barbell.png",
            ),
#        (0,0), ConditionSwitch(
#            # spunk over tits
#            "'tits' not in DoreenX.Spunk", Null(),
##            "DoreenX.Over == 'tshirt'", "images/DoreenBJFace/Doreen_TJ_Spunk_Clothed.png",
#            "not DoreenX.Uptop and DoreenX.Over", "images/DoreenBJFace/Doreen_TJ_Spunk_Clothed.png",
#            "True", "images/DoreenBJFace/Doreen_TJ_Spunk_Over.png",
#            ),
#        (0,0), "images/DoreenBJFace/Doreen_TJ_RefLine.png",
#        (0,0), "images/DoreenBJFace/Doreen_TJ_RefLine2.png",
        )
    transform_anchor True
#    anchor (0.6, 1.0)#(0.6, 562)
#    xoffset 155#300
#    yoffset 325#125
#    yoffset -925#-625#-325
#    zoom .75  #.76
    rotate 0


image Doreen_TJ_BraStretch:
            #bra streching effect
            contains:
                ConditionSwitch(
                    #Over tits layer
                    "DoreenX.Over == 'tshirt'", "images/DoreenBJFace/Doreen_TJ_Stretch_Tshirt.png",
                    "DoreenX.Over == 'sweater'", "images/DoreenBJFace/Doreen_TJ_Stretch_Sweater.png",
                    "DoreenX.Chest == 'sports bra'", "images/DoreenBJFace/Doreen_TJ_Stretch_Green.png",
                    "True", Null(),
                    )
#            contains:
#                    "images/DoreenBJFace/Doreen_TJ_RefLine2.png"
            transform_anchor True
#            zoom 1
#            offset (50,0) # (300,275)
#            anchor (.1,.1)#(0.1, .2)
            rotate 0

#image Doreen_TJ_Tits:
#            #layer with left tit and all clothing
#            contains:
#                "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_TJ_Tits.png"
##            contains:
##                ConditionSwitch(
##                        "not DoreenX.Water",Null(),
##                        "True",       "images/DoreenBJFace/Doreen_TJ_Tits_Wet.png",
##                        )
#            contains:
#                #Chest
#                ConditionSwitch(
#                        "DoreenX.Chest == 'lace bra' and DoreenX.Uptop","images/DoreenBJFace/Doreen_TJ_Chest_Lace_Up.png",  #fix, add "no straps" version here
#                        "DoreenX.Chest == 'lace bra'","images/DoreenBJFace/Doreen_TJ_Chest_Lace.png",
#                        "DoreenX.Chest == 'sports bra'","images/DoreenBJFace/Doreen_TJ_Chest_Sports.png",
#                        "DoreenX.Chest == 'swimsuit' and DoreenX.Uptop","images/DoreenBJFace/Doreen_TJ_Chest_Bikini_Up.png",
#                        "DoreenX.Chest == 'swimsuit'","images/DoreenBJFace/Doreen_TJ_Chest_Bikini.png",
#                        "True", Null(),
#                        )
#            contains:
#                #Over
#                ConditionSwitch(
#                        "DoreenX.Over == 'tube top' and DoreenX.Uptop","images/DoreenBJFace/Doreen_TJ_Over_Tube_Up.png",
#                        "DoreenX.Over == 'tube top'","images/DoreenBJFace/Doreen_TJ_Over_Tube.png",
#                        "True", Null(),
#                        )
#            contains:
#                #Piercings clothing
#                ConditionSwitch(
#                        "not DoreenX.Pierce", Null(),
#                        "DoreenX.Pierce == 'ring'", ConditionSwitch(
#                                #if she's got ring piercings
#                                "DoreenX.Uptop", "images/DoreenBJFace/Doreen_TJ_Pierce_Ring.png",
#                                "DoreenX.Over == 'tube top'", "images/DoreenBJFace/Doreen_TJ_Pierce_Ring_Pink.png",
#                                "DoreenX.Chest == 'swimsuit'", "images/DoreenBJFace/Doreen_TJ_Pierce_Ring_Pink.png",
#                                "DoreenX.Chest == 'lace bra'", "images/DoreenBJFace/Doreen_TJ_Pierce_Ring_Lace.png",
#                                "True", "images/DoreenBJFace/Doreen_TJ_Pierce_Ring.png",
#                                ),
#                        "DoreenX.Uptop", "images/DoreenBJFace/Doreen_TJ_Pierce_Barbell.png",
#                        "DoreenX.Over == 'tube top'", "images/DoreenBJFace/Doreen_TJ_Pierce_Barbell_Pink.png",
#                        "DoreenX.Chest == 'swimsuit'", "images/DoreenBJFace/Doreen_TJ_Pierce_Barbell_Pink.png",
#                        "DoreenX.Chest == 'lace bra'", "images/DoreenBJFace/Doreen_TJ_Pierce_Barbell_Lace.png",
#                        "True", "images/DoreenBJFace/Doreen_TJ_Pierce_Barbell.png",
#                        )
#            contains:
#                #Over
#                ConditionSwitch(
#                        "'tits' in DoreenX.Spunk and Player.Male","images/DoreenBJFace/Doreen_TJ_Spunk_Tits_Over.png",
#                        "True", Null(),
#                        )
#            transform_anchor True
#            zoom 1
#            anchor (0.4, 1.0)
#            #offset (410,770) # (300,275)
#            rotate 0


## Animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start 0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Doreen_TJ_0:
        #Her Body in the TJ pose, static
#        contains:
#                #hair back
#                "Doreen_BJ_HairBack"
#                subpixel True
##                offset (90,-480)
#                pos (-10,0) #top (0,-10)
#                transform_anchor True
#                rotate 0
#                parallel:
#                    ease 2 ypos 30
#                    pause .3
#                    ease 2 ypos 0
#                    pause .4
#                    repeat
#                parallel:
#                    pause .1
#                    ease 2 rotate 10
#                    pause .3
#                    ease 2 rotate 0
#                    pause .3
#                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "Doreen_TJ_Body"
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
                #underside tit
                "Doreen_TJ_Tits_Under"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 810)#(0.6, 700)
                xoffset 200#200
                yoffset -161#271
                yzoom 1
                parallel:
                    ease 2 ypos 30
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
                parallel:
                    pause .2
                    ease 1.1 yzoom .85
                    pause 1.2
                    ease 1.5 yzoom 1.1
                    pause .1
                    ease 0.6 yzoom 1 #.7 is max
                    repeat
        contains:
                #head
                "Doreen_BJ_Head"
                subpixel True
#                offset (90,-480)
                pos (-10,0) #top (0,-10)
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
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Doreen_TJ_ZeroCock"
#                ConditionSwitch(
#                            "Player.Sprite","Doreen_TJ_ZeroCock",
#                            "True",  Null(),
#                            )
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (40,50)#(5,50)
        contains:
                #bra stretch
                "Doreen_TJ_BraStretch"
                subpixel True
                pos (0,0) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 833)#(0.6, 700)
                xoffset 315#68
                yoffset -278#-265
                yzoom 1.5
#                alpha 0.7
                parallel:
                    ease 2 yzoom 2
                    pause .3
                    ease 2 yzoom 1.5
                    pause .4
                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_TJ_Thumbs.png"
                subpixel True
                anchor (0.6, 1.0)#(0.6, 0.0)
                pos (0,0) #top (0,-10)
                xoffset 155#155
                yoffset 125#-600
                transform_anchor True
                parallel:
                    ease 2 ypos 30
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
        contains:
                #overside tit
                "Doreen_TJ_Tits_Over"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 810)#(0.6, 700)
                xoffset 200#200
                yoffset -161#271
                yzoom 1
                parallel:
                    ease 2 ypos 30
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
                parallel:
                    pause .2
                    ease 1.1 yzoom .85
                    pause 1.2
                    ease 1.5 yzoom 1.1
                    pause .1
                    ease 0.6 yzoom 1 #.7 is max
                    repeat


# End Doreen TJ Pose 0 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start 1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

## Start 1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Doreen_TJ_1:
        #Her Body in the TJ pose, slow
#        contains:
#                #hair back
#                "Doreen_BJ_HairBack"
#                subpixel True
##                offset (90,-480)
#                pos (-20,-80) #top (0,-10)
#                transform_anchor True
#                rotate 0
#                parallel:
#                    ease 2 ypos 40
#                    pause .3
#                    ease 2 ypos -80
#                    pause .4
#                    repeat
#                parallel:
#                    pause .1
#                    ease 2 rotate 3
#                    pause .3
#                    ease 2 rotate 0
#                    pause .3
#                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "Doreen_TJ_Body"
                subpixel True
#                anchor (0.6, 1.0)#(0.6, 0.0)
                pos (0,-80) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos 40
                    pause .3
                    ease 2 ypos -80
                    pause .4
                    repeat
        contains:
                #underside tit
                "Doreen_TJ_Tits_Under"
                subpixel True
                pos (0,-80) #top (0,-15)
                transform_anchor True
                anchor (0.6, 810)#(0.6, 562)
                xoffset 200#200
                yoffset -161#125
                yzoom 1
                parallel:
                    ease 2 ypos 40
                    pause .3
                    ease 2 ypos -80
                    pause .4
                    repeat
                parallel:
                    pause .1
                    ease .8 yzoom .80
                    pause 1.2
                    ease 1.2 yzoom 1.1
                    pause .8
                    ease 0.6 yzoom .98
                    repeat
        contains:
                #head
                "Doreen_BJ_Head"
                subpixel True
#                offset (90,-480)
                pos (-20,-80) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos 40
                    pause .3
                    ease 2 ypos -80
                    pause .4
                    repeat
                parallel:
                    pause .1
                    ease 2 rotate 3
                    pause .3
                    ease 2 rotate 0
                    pause .3
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Doreen_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (40,50)#(5,50)
        contains:
                #bra stretch
                "Doreen_TJ_BraStretch"
                subpixel True
                pos (0,0) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 833)#(0.6, 700)
                xoffset 315#68
                yoffset -278#-265
                yzoom .4
#                alpha 0.7
                parallel:
                    ease 2 yzoom 2
                    pause .3
                    ease 2 yzoom .4
                    pause .4
                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_TJ_Thumbs.png"
                subpixel True
                anchor (0.6, 1.0)#(0.6, 0.0)
                pos (0,-80) #top (0,-10)
                xoffset 155#155
                yoffset 125#-600
                transform_anchor True
                parallel:
                    ease 2 ypos 40
                    pause .3
                    ease 2 ypos -80
                    pause .4
                    repeat
        contains:
                #overside tit
                "Doreen_TJ_Tits_Over"
                subpixel True
                pos (0,-80) #top (0,-15)
                transform_anchor True
                anchor (0.6, 810)#(0.6, 562)
                xoffset 200#200
                yoffset -161#125
                yzoom 1
                parallel:
                    ease 2 ypos 40
                    pause .3
                    ease 2 ypos -80
                    pause .4
                    repeat
                parallel:
                    pause .1
                    ease .8 yzoom .80
                    pause 1.2
                    ease 1.2 yzoom 1.1
                    pause .8
                    ease 0.6 yzoom .98
                    repeat


## End Doreen TJ Pose 1 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




## Start 2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Doreen_TJ_2:
        #Her Body in the TJ pose, fast
#        contains:
#                #hair back
#                "Doreen_BJ_HairBack"
#                subpixel True
##                offset (90,-480)
#                pos (-30,-80) #top (0,-10)
#                transform_anchor True
#                rotate 0
#                parallel: #4.7s total -> 1.7
#                    ease .6 ypos -20 #120
#                    pause .1
#                    ease .8 ypos -80
#                    pause .2
#                    repeat
#                parallel:
#                    ease .5 rotate -2
#                    pause .2
#                    ease .8 rotate 0
#                    pause .2
#                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "Doreen_TJ_Body"
                subpixel True
#                anchor (0.6, 1.0)#(0.6, 0.0)
                pos (0,-80) #top (0,-10)
                transform_anchor True
                parallel: #4.7s total -> 1.7
                    ease .6 ypos -20 #120
                    pause .1
                    ease .8 ypos -80
                    pause .2
                    repeat
        contains:
                #underside tit
                "Doreen_TJ_Tits_Under"
                subpixel True
                pos (0,-80) #top (0,-15)
                transform_anchor True
                anchor (0.6, 810)#(0.6, 562)
                xoffset 200#200
                yoffset -161#125
                yzoom 1
                parallel: #4.7s total -> 1.7
                    ease .6 ypos -20 #120
                    pause .1
                    ease .8 ypos -80
                    pause .2
                    repeat
                parallel:
#                    pause .1
                    ease .5 yzoom .80
                    pause .3
                    ease .3 yzoom 1.1
                    ease .2 yzoom .98
                    ease .2 yzoom 1
                    pause .2
                    repeat
        contains:
                #head
                "Doreen_BJ_Head"
                subpixel True
#                offset (90,-480)
                pos (-30,-80) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel: #4.7s total -> 1.7
                    ease .6 ypos -20 #120
                    pause .1
                    ease .8 ypos -80
                    pause .2
                    repeat
                parallel:
                    ease .5 rotate -2
                    pause .2
                    ease .8 rotate 0
                    pause .2
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Doreen_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (40,50)#(5,50)
        contains:
                #bra stretch
                "Doreen_TJ_BraStretch"
                subpixel True
                pos (0,0) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 833)#(0.6, 700)
                xoffset 315#68
                yoffset -278#-265
                yzoom .4
#                alpha 0.7
                parallel: #4.7s total -> 1.7
                    ease .6 yzoom 1.2#2
                    pause .1
                    ease .8 yzoom .4
                    pause .2
                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_TJ_Thumbs.png"
                subpixel True
                anchor (0.6, 1.0)#(0.6, 0.0)
                pos (0,-80) #top (0,-10)
                xoffset 155#155
                yoffset 125#-600
                transform_anchor True
                parallel: #4.7s total -> 1.7
                    ease .6 ypos -20 #120
                    pause .1
                    ease .8 ypos -80
                    pause .2
                    repeat
        contains:
                #overside tit
                "Doreen_TJ_Tits_Over"
                subpixel True
                pos (0,-80) #top (0,-15)
                transform_anchor True
                anchor (0.6, 810)#(0.6, 562)
                xoffset 200#200
                yoffset -161#125
                yzoom 1
                parallel: #4.7s total -> 1.7
                    ease .6 ypos -20 #120
                    pause .1
                    ease .8 ypos -80
                    pause .2
                    repeat
                parallel:
#                    pause .1
                    ease .5 yzoom .80
                    pause .3
                    ease .3 yzoom 1.1
                    ease .2 yzoom .98
                    ease .2 yzoom 1
                    pause .2
                    repeat

## End Doreen TJ Pose 2 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

## Start 3 (licking) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Doreen_TJ_3:
        #Her Body in the TJ pose, licking
#        contains:
#                #hair back
#                "Doreen_BJ_HairBack"
#                subpixel True
##                offset (90,-480)
#                pos (-60,-80) #top (0,-10)
#                transform_anchor True
#                rotate 0
##                parallel:
##                    ease 2 xpos 20
##                    pause .3
##                    easeout .5 xpos 0
##                    easeout 1 xpos 5
###                    pause .5
##                    repeat
#                parallel:
#                    ease 2 ypos -20
#                    pause .3
#                    ease .5 ypos -80
#                    pause 1
#                    repeat
#                parallel:
#                    pause .1
#                    ease 2 rotate -12
#                    pause .3
#                    ease .5 rotate 5
#                    easein .9 rotate 0
##                    pause .4
#                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "Doreen_TJ_Body"
                subpixel True
#                anchor (0.6, 1.0)#(0.6, 0.0)
                pos (0,-40) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos 0
                    pause .3
                    ease .5 ypos -40
                    pause 1
                    repeat
        contains:
                #underside tit
                "Doreen_TJ_Tits_Under"
                subpixel True
                pos (0,-40) #top (0,-15)
                transform_anchor True
                anchor (0.6, 810)#(0.6, 562)
                xoffset 200#200
                yoffset -161#125
                yzoom 1
                parallel:
                    ease 2 ypos 0
                    pause .3
                    ease .5 ypos -40
                    pause 1
                    repeat
                parallel:
                    pause .2
                    ease 1.2 yzoom .85
                    pause 1
                    ease .4 yzoom 1.1
                    ease 0.3 yzoom 1
                    pause .7
                    repeat
        contains:
                #head
                "Doreen_BJ_Head"
                subpixel True
#                offset (90,-480)
                pos (-60,-80) #top (0,-10)
                transform_anchor True
                rotate 0
#                parallel:
#                    ease 2 xpos 20
#                    pause .3
#                    easeout .5 xpos 0
#                    easeout 1 xpos 5
##                    pause .5
#                    repeat
                parallel:
                    ease 2 ypos -20
                    pause .3
                    ease .5 ypos -80
                    pause 1
                    repeat
                parallel:
                    pause .1
                    ease 2 rotate -12
                    pause .3
                    ease .5 rotate 5
                    easein .9 rotate 0
#                    pause .4
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Doreen_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (40,50)#(5,50)
                rotate 0
                parallel:
                    pause .1
                    ease 2 rotate 2
                    pause .3
                    ease .5 rotate -1
                    ease .2 rotate 0
                    pause .7
                    repeat
        contains:
                #bra stretch
                "Doreen_TJ_BraStretch"
                subpixel True
                pos (0,0) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 833)#(0.6, 700)
                xoffset 315#68
                yoffset -278#-265
                yzoom .9
#                alpha 0.7
                parallel:
                    ease 2 yzoom 1.4
                    pause .3
                    ease .5 yzoom .9
                    pause 1
                    repeat
                parallel:
                    ease 2 xpos 10
                    pause .3
                    ease .5 xpos 0
                    pause 1
                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_TJ_Thumbs.png"
                subpixel True
                anchor (0.6, 1.0)#(0.6, 0.0)
                pos (0,-40) #top (0,-10)
                xoffset 155#155
                yoffset 125#-600
                transform_anchor True
                parallel:
                    ease 2 ypos 0
                    pause .3
                    ease .5 ypos -40
                    pause 1
                    repeat
        contains:
                #overside tit
                "Doreen_TJ_Tits_Over"
                subpixel True
                pos (0,-40) #top (0,-15)
                transform_anchor True
                anchor (0.6, 810)#(0.6, 562)
                xoffset 200#200
                yoffset -161#125
                yzoom 1
                parallel:
                    ease 2 ypos 0
                    pause .3
                    ease .5 ypos -40
                    pause 1
                    repeat
                parallel:
                    pause .2
                    ease 1.2 yzoom .85
                    pause 1
                    ease .4 yzoom 1.1
                    ease 0.3 yzoom 1
                    pause .7
                    repeat

## End Doreen TJ Pose 3 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start 4 (cumming high) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Doreen_TJ_4:
        #Her Body in the TJ pose, cummming high
        #Her Body in the TJ pose, static
#        contains:
#                #hair back
#                "Doreen_BJ_HairBack"
#                subpixel True
##                offset (90,-480)
#                pos (-30,-90) #top (0,-10)
#                transform_anchor True
#                rotate 0
#                parallel:
#                    ease 2 ypos -80
#                    pause .3
#                    ease 2 ypos -90
#                    pause .4
#                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "Doreen_TJ_Body"
                subpixel True
#                anchor (0.6, 1.0)#(0.6, 0.0)
                pos (0,-40) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -10
                    pause .3
                    ease 2 ypos -40
                    pause .4
                    repeat
        contains:
                #underside tit
                "Doreen_TJ_Tits_Under"
                subpixel True
                pos (0,-40) #top (0,-15)
                transform_anchor True
                anchor (0.6, 810)#(0.6, 700)
                xoffset 200#200
                yoffset -161#271
                yzoom 1
                parallel:
                    ease 2 ypos -10
                    pause .3
                    ease 2 ypos -40
                    pause .4
                    repeat
                parallel:
                    pause .2
                    ease 1.1 yzoom .9
                    pause 1.2
                    ease 1.5 yzoom 1.1
                    pause .1
                    ease 0.6 yzoom 1 #.7 is max
                    repeat
        contains:
                #head
                "Doreen_BJ_Head"
                subpixel True
#                offset (90,-480)
                pos (-30,-90) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos -80
                    pause .3
                    ease 2 ypos -90
                    pause .4
                    repeat
#                parallel:
#                    pause .1
#                    ease 2 rotate 10
#                    pause .3
#                    ease 2 rotate 0
#                    pause .3
#                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Doreen_TJ_ZeroCock"
#                ConditionSwitch(
#                            "Player.Sprite","Doreen_TJ_ZeroCock",
#                            "True",  Null(),
#                            )
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (40,50)#(5,50)
        contains:
                #bra stretch
                "Doreen_TJ_BraStretch"
                subpixel True
                pos (0,0) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 833)#(0.6, 700)
                xoffset 315#68
                yoffset -278#-265
                yzoom .9
#                alpha 0.7
                parallel:
                    ease 2 yzoom 1.3
                    pause .3
                    ease 2 yzoom .9
                    pause .4
                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_TJ_Thumbs.png"
                subpixel True
                anchor (0.6, 1.0)#(0.6, 0.0)
                pos (0,-40) #top (0,-10)
                xoffset 155#155
                yoffset 125#-600
                transform_anchor True
                parallel:
                    ease 2 ypos -10
                    pause .3
                    ease 2 ypos -40
                    pause .4
                    repeat
        contains:
                #overside tit
                "Doreen_TJ_Tits_Over"
                subpixel True
                pos (0,-40) #top (0,-15)
                transform_anchor True
                anchor (0.6, 810)#(0.6, 700)
                xoffset 200#200
                yoffset -161#271
                yzoom 1
                parallel:
                    ease 2 ypos -10
                    pause .3
                    ease 2 ypos -40
                    pause .4
                    repeat
                parallel:
                    pause .2
                    ease 1.1 yzoom .9
                    pause 1.2
                    ease 1.5 yzoom 1.1
                    pause .1
                    ease 0.6 yzoom 1 #.7 is max
                    repeat

# End Doreen TJ Pose 4 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start 5 (cumming low) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Doreen_TJ_5:
        #Her Body in the TJ pose, cumming low
#        contains:
#                #hair back
#                "Doreen_BJ_HairBack"
#                subpixel True
##                offset (90,-480)
#                pos (0,-20) #top (0,-10)
#                transform_anchor True
#                rotate 10
#                parallel:
#                    ease 2 ypos -10
#                    pause .3
#                    ease 1.5 ypos -20
#                    pause .5
#                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "Doreen_TJ_Body"
                subpixel True
#                anchor (0.6, 1.0)#(0.6, 0.0)
                pos (0,10) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos 20
                    pause .3
                    ease 1.5 ypos 10
                    pause .5
                    repeat
        contains:
                #underside tit
                "Doreen_TJ_Tits_Under"
                subpixel True
                pos (0,10) #top (0,-15)
                transform_anchor True
                anchor (0.6, 810)#(0.6, 562)
                xoffset 200#200
                yoffset -161#125
                yzoom 1
                parallel:
                    ease 2 ypos 20
                    pause .3
                    ease 1.5 ypos 10 #.5
                    pause .5
                    repeat
#                parallel:
#                    pause .1
#                    ease .8 yzoom .95
#                    pause 1.2
#                    ease 1.2 yzoom 1
#                    pause 1.3
#                    ease 0.6 yzoom .98
#                    repeat
        contains:
                #head
                "Doreen_BJ_Head"
                subpixel True
#                offset (90,-480)
                pos (0,-20) #top (0,-10)
                transform_anchor True
                rotate 10
                parallel:
                    ease 2 ypos -10
                    pause .3
                    ease 1.5 ypos -20
                    pause .5
                    repeat
#                parallel:
#                    pause .1
#                    ease 2 rotate 10
#                    pause .3
#                    ease .5 rotate 40
#                    pause .9
#                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Doreen_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (40,50)#(5,50)
                rotate 0
#                parallel:
#                    pause .1
#                    ease 2 rotate 3
#                    pause .3
#                    ease .5 rotate 0
#                    pause .9
#                    repeat
        contains:
                #bra stretch
                "Doreen_TJ_BraStretch"
                subpixel True
                pos (0,0) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 833)#(0.6, 700)
                xoffset 315#68
                yoffset -278#-265
                yzoom 1.6
#                alpha 0.7
                parallel:
                    ease 2 yzoom 1.8
                    pause .3
                    ease 1.5 yzoom 1.6
                    pause .5
                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "images/DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_TJ_Thumbs.png"
                subpixel True
                anchor (0.6, 1.0)#(0.6, 0.0)
                pos (0,10) #top (0,-10)
                xoffset 155#155
                yoffset 125#-600
                transform_anchor True
                parallel:
                    ease 2 ypos 20
                    pause .3
                    ease 1.5 ypos 10
                    pause .5
                    repeat
        contains:
                #overside tit
                "Doreen_TJ_Tits_Over"
                subpixel True
                pos (0,10) #top (0,-15)
                transform_anchor True
                anchor (0.6, 810)#(0.6, 562)
                xoffset 200#200
                yoffset -161#125
                yzoom 1
                parallel:
                    ease 2 ypos 20#90
                    pause .3
                    ease 1.5 ypos 10 #80
                    pause .5
                    repeat
#                parallel:
#                    pause .1
#                    ease .8 yzoom .95
#                    pause 1.2
#                    ease 1.2 yzoom 1
#                    pause 1.3
#                    ease 0.6 yzoom .98
#                    repeat

## End Doreen TJ Pose 5 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

## Doreen's TJ animations end / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Doreen_TJ_Launch(Line = Trigger):    # The sequence to launch the Doreen Titfuck animations
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    return
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
    if renpy.showing("Doreen_TJ_Animation"):
        return

    if Line == "L": # Doreen gets started. . .
            if Taboo:
                if len(Present) >= 2:
                    if Present[0] != DoreenX:
                            "[DoreenX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                    elif Present[1] != DoreenX:
                            "[DoreenX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
                else:
                            "[DoreenX.Name] небрежно оглядывается по сторонам, чтобы убедиться, что никто не наблюдает."
#            "[DoreenX.Name] bends over and places your cock between her breasts."
    if DoreenX.Chest == "suit" and not DoreenX.Uptop:
        $ DoreenX.Uptop = 1
        "Она слегка расстегивает свой костюм."
#    if DoreenX.Chest and DoreenX.Over:
#        "She throws off her [DoreenX.Over] and her [DoreenX.Chest]."
#    elif DoreenX.Over:
#        "She throws off her [DoreenX.Over], baring her breasts underneath."
#    elif DoreenX.Chest:
#        "She tugs off her [DoreenX.Chest] and throws it aside."
#    $ DoreenX.Over = 0
#    $ DoreenX.Chest = 0
#    $ DoreenX.ArmPose = 0
    call Girl_First_Topless(DoreenX)

    show blackscreen onlayer black with dissolve

    if renpy.showing("Doreen_BJ_Animation"):
            hide Doreen_BJ_Animation
    else:
            call Girl_Hide(DoreenX)
            show Doreen_Sprite at SpriteLoc(DoreenX.SpriteLoc) zorder 150:
                alpha 1
                ease 1 zoom 2.3 xpos 750 yoffset -100
            show Doreen_Sprite:
                alpha 0

#    if DoreenX.Over == "towel" or DoreenX.Chest == "corset": #pulls top down because these tops are incompatible with TJ.
#        $ DoreenX.Uptop = 1

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "titjob"
    show Doreen_TJ_Animation zorder 150:
        pos (950,1050)#(1000,1000)#(700,520)
    $ Player.Sprite = 1
    hide blackscreen onlayer black with dissolve
    return

label Doreen_TJ_Reset:
    # The sequence to the Doreen animations from Titfuck to default
    if not renpy.showing("Doreen_TJ_Animation"):
        return
#    hide Doreen_TJ_Animation
    call Girl_Hide(DoreenX)
    $ Player.Sprite = 0

    show Doreen_Sprite at SpriteLoc(DoreenX.SpriteLoc) zorder 150:
        zoom 2.3 xpos 750 yoffset -100
    show Doreen_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 xpos 700 yoffset 50
        pause .5
        ease .5 zoom 1 xpos DoreenX.SpriteLoc yoffset 0
    "[DoreenX.Name] отстраняется"
    show Doreen_Sprite at SpriteLoc(DoreenX.SpriteLoc) zorder DoreenX.Layer:
        alpha 1 zoom 1 offset (0,0) xpos DoreenX.SpriteLoc
    return

## End Doreen TJ Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Doreen Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Doreen Handjob element //////////////////////////////////////////////////////////////////////

image Doreen_HJ_Body:
    "Doreen_Sprite"
    pos (00,-1250)#(780,-1250)
    zoom 4.8#2.15


transform Doreen_HJ_Body_1():
    subpixel True
#    pos (700,-1250)#(350,-550)
    block:
        ease .5 ypos -1220
        pause 0.25
        ease 1.0 ypos -1250
        pause 0.1
        repeat

transform Doreen_HJ_Body_2():
    subpixel True
#    pos (350,-550)
    block:
        ease 0.2 ypos -1240
        pause 0.1
        ease 0.4 ypos -1250
        pause 0.1
        repeat

image Doreen_Hand_Under:
    "images/DoreenSprite/[DoreenX.skin_image.skin_path]handdoreen2.png"
#    "images/LauraSprite/handlaura2.png"
    anchor (0.5,0.5)
    pos (170,0) #(-10,0)


image Doreen_Hand_Over:
    "images/DoreenSprite/[DoreenX.skin_image.skin_path]handdoreen1.png"
#    "images/LauraSprite/handlaura1.png"
    anchor (0.5,0.5)
    pos (170,0)

transform Doreen_Hand_1():
    subpixel True
    pos (160,-100)
    rotate 5
    block:
        ease .5 pos (160,150) rotate -5 #ypos 150 rotate 5 Bottom
        pause 0.25
        ease 1.0 pos (160,-100) rotate 5 #(-20,-100) #rotate -10#  Top
        pause 0.1
        repeat

transform Doreen_Hand_2():
    subpixel True
    pos (155,-120)
    rotate 10
    block:
        ease 0.2 pos (155,0) rotate 0   #(-15,0)
        pause 0.1
        ease 0.4 pos (155,-120) rotate 5 #-15,-120)
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

image Doreen_HJ_Animation:
    contains:
        ConditionSwitch(
            # backside of the hand
            "not Speed", Transform("Doreen_HJ_Body"),
            "Speed == 1", At("Doreen_HJ_Body", Doreen_HJ_Body_1()),
            "Speed >= 2", At("Doreen_HJ_Body", Doreen_HJ_Body_2()),
            "Speed", Null(),
            ),
    contains:
        ConditionSwitch(
            # backside of the hand
            "not Speed", Transform("Doreen_Hand_Under"),
            "Speed == 1", At("Doreen_Hand_Under", Doreen_Hand_1()),
            "Speed >= 2", At("Doreen_Hand_Under", Doreen_Hand_2()),
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
            "not Speed", Transform("Doreen_Hand_Over"),
            "Speed == 1", At("Doreen_Hand_Over", Doreen_Hand_1()),
            "Speed >= 2", At("Doreen_Hand_Over", Doreen_Hand_2()),
            "Speed", Null(),
            ),
    anchor (0.51, -1.3)
#    xzoom -0.4#0.6
    zoom 0.4#0.6


label Doreen_HJ_Launch(Line = Trigger):
    if renpy.showing("Doreen_HJ_Animation"):
        $ Trigger = "hand"
        return
    if not Player.Male:
        call Doreen_Finger_Launch
        return
    call Girl_Hide(DoreenX)
    $ DoreenX.ArmPose = 1
    if Line == "L":
        show Doreen_Sprite at SpriteLoc(StageRight) zorder 150:
            alpha 1
            ease 1 zoom 1.7 offset (-150,200)#(0,200)
    else:
        show Doreen_Sprite at SpriteLoc(StageRight) zorder 150:
            alpha 1
            ease 1 zoom 1.9 offset (-150,150)#(150,150)
        with dissolve

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    else:
        $ Speed = 1
    pause .5
    show Doreen_Sprite:
        alpha 0
    show Doreen_HJ_Animation at SpriteLoc(StageCenter) zorder 150 with fade:
        #xoffset 150
        offset (200,250)#(150,250)
    $ DoreenX.ArmPose = 2
    return

label Doreen_HJ_Reset: # The sequence to the Doreen animations from handjob to default
    if not renpy.showing("Doreen_HJ_Animation"):
        return
    $ Speed = 0
    $ DoreenX.ArmPose = 1
    hide Doreen_HJ_Animation with dissolve
    call Girl_Hide(DoreenX)
    show Doreen_Sprite at SpriteLoc(DoreenX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 1.5 offset (-250,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Doreen_Sprite at SpriteLoc(DoreenX.SpriteLoc) zorder DoreenX.Layer:
        alpha 1 zoom 1 offset (0,0)
#    $ DoreenX.ArmPose = 1
    return

## End Doreen Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# Core Doreen CUN element ///////////////////////////////////////////////////////////////////////////                                     Core Doreen CUN element
#Doreen CUN Over Sprite Compositing

image Doreen_CUN_Animation: #core CUN animation
    LiveComposite(
        (787,913),
        (0,0), ConditionSwitch(                                                                 # back of the hair, which needs to go behind the body
            "Speed == 0",  "Doreen_CUN_Anim_Static",
            "Speed == 1",  "Doreen_CUN_Anim_Licking1",
            "Speed == 2",  "Doreen_CUN_Anim_Licking2",
            "Speed >= 3",  "Doreen_CUN_Anim_Licking3",
            "Speed == 4",  "Doreen_CUN_Anim_Licking1",
            "True", "Doreen_CUN_Anim_Static",
            ),
        )
    zoom .55
    anchor (.5,.5)

image Doreen_CUN_Anim_Static:
    #Animation for licking speed 1
#    contains:
#        #hair
#        "Doreen_BJ_HairBack"
#        subpixel True
#        zoom 1.4
#        pos (-50,570)
#        offset (70,0)#(-10,0)
#        rotate 20
#        block:
#            ease 2 yoffset 10
#            ease 2 yoffset 0
#            repeat
    contains:
        #body 2
        "Doreen_BJ_Backdrop"
        zoom 1.4
#        pos (-50,600)
        pos (-300,70)#(-440,-290)
        subpixel True
        offset (70,20)  #top(0,-35)
        block:
            ease 2 yoffset 30
            ease 2 yoffset 20
            repeat
    contains:
        #head
        "Doreen_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.4
        pos (-50,290)
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


image Doreen_CUN_Anim_Licking1:
    #Animation for licking speed 1
#    contains:
#        #hair
#        "Doreen_BJ_HairBack"
#        subpixel True
#        zoom 1.4
#        pos (-50,570)
#        offset (40,40)#490)
#        rotate 10
#        block: #5s total
#            ease 2.5 offset (45,100) #bottom (0,75)
#            easeout 1.5 offset (45,60)  #top (0,60)
#            ease .5 offset (40,20)  #top
#            ease .5 offset (42,30)  #top
#            repeat
    contains:
        #body 2
        "Doreen_BJ_Backdrop"#"Doreen_Sprite"
#        zoom 1 #4.5
#        pos (-350,-290)#(-440,-290)
        zoom 1.4
        pos (-300,0)#(-300,350)
        subpixel True
        offset (0,0)# -70,0
        block:
            ease 2.5 offset (0,75) #bottom (30,90)
            ease 2.3 offset (0,0)  #top
            pause .2
            repeat
    contains:
        #head
        "Doreen_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.4
        pos (-150,220)#(-50,570)
        offset (40,40)#490)
        rotate 0
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
#End Doreen Licking 1

image Doreen_CUN_Anim_Licking2:
    #Animation for licking speed 2
#    contains:
#        #hair
#        "Doreen_BJ_HairBack"
#        subpixel True
#        zoom 1.4
#        pos (-50,570)
#        offset (40,30)#490)
#        rotate 10
#        parallel: #2s total
#            ease 1 offset (30,100) #bottom
#            easeout .65 offset (40,70)  #top -35)
#            linear .35 offset (40,30)  #top -35)
#            pause .10
#            repeat
#        parallel: #2s total
#            ease 1 rotate 4 #bottom
#            easeout .65 rotate 7  #top -35)
#            linear .35 rotate 10  #top -35)
#            pause .10
#            repeat
    contains:
        #body 2
        "Doreen_BJ_Backdrop"
        zoom 1.4
        pos (-300,0)#(-440,-290)
        subpixel True
        offset (10,50)#490)
        block:
            ease .75 offset (10,70) #bottom (30,90)
            ease .95 offset (10,50)  #top
            pause .40
            repeat
    contains:
        #head
        "Doreen_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.4
        pos (-90,220)
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
#End Doreen Licking 2

image Doreen_CUN_Anim_Licking3:
    #Animation for licking speed 3
#    contains:
#        #hair
#        "Doreen_BJ_HairBack"
#        subpixel True
#        zoom 1.4
#        pos (-50,570)
#        offset (20,110)#490)
#        block: #2s total
#            ease .5 offset (20,130) #bottom
#            ease .5 offset (20,110)  #top -35)
#            repeat
    contains:
        #body 2
        "Doreen_BJ_Backdrop"
        zoom 1.4
        pos (-300,0)#(-440,-290)
        subpixel True
        offset (0,110)#490)
        block:
            ease .4 offset (0,100) #bottom (30,90)
            ease .4 offset (0,110)  #top
            pause .2
            repeat
    contains:
        #head
        "Doreen_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.4
        pos (-120,220)
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
#End Doreen Licking 3

#CUN Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Doreen_CUN_Launch(Line = Trigger):
    # The sequence to launch the Doreen CUN animations
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    return
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
    if renpy.showing("Doreen_CUN_Animation") and DoreenX.Pose != "69":
        return
    elif renpy.showing("Doreen_69_CUN") and DoreenX.Pose == "69":
        return

    if Player.Male == 1:
        call Doreen_BJ_Launch
        return

    call Girl_Hide(DoreenX)
    if Line == "L" or Line == "cum":
        show Doreen_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1
            ease 1 zoom 2.5 offset (70,240) #(-90,140) offset (150,80)
        with dissolve
    else:
        show Doreen_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1 zoom 2.5 offset (70,240) #(-90,140)
        with dissolve

    if Taboo and Line == "L":
            # Doreen gets started. . .
            if len(Present) >= 2:
                if Present[0] != DoreenX:
                        "[DoreenX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                elif Present[1] != DoreenX:
                        "[DoreenX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
            else:
                        "[DoreenX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
    $ Speed = 1
    if Line == "L":
            if not DoreenX.Blow:
                "[DoreenX.Name] нерешительно стягивает с вас штаны и касается своим ртом вашей киски."
            else:
                "[DoreenX.Name] наклоняется и начинает лизать вашу киску."

    if Line != "cum":
        $ Trigger = "cun"

    $ Player.Cock = 0
    show Doreen_Sprite:
        alpha 0
    if DoreenX.Pose == "69":
            show Doreen_69_CUN zorder 150
    else:
            show Doreen_CUN_Animation zorder 150:
                pos (800,830)#(645,610)
    return

label Doreen_CUN_Reset: # The sequence to the Doreen animations from CUN to default
    if not renpy.showing("Doreen_CUN_Animation") and not renpy.showing("Doreen_69_CUN"):
        return
    call Girl_Hide(DoreenX)
    $ Speed = 0

    show Doreen_Sprite at SpriteLoc(DoreenX.SpriteLoc) zorder 150:
        zoom 2 offset (70,140) alpha 1
        pause .5
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Doreen_Sprite at SpriteLoc(DoreenX.SpriteLoc) zorder DoreenX.Layer:
        alpha 1 zoom 1 offset (0,0)
    $ DoreenX.FaceChange("sexy")
    return

##End Doreen Cunnilingus Animations
## ////////////////////////////////                                                                                      ///////////////////////////////
## ////////////////////////////////                                                                                      ///////////////////////////////
## ////////////////////////////////                                                                                      ///////////////////////////////


## ////////////////////////////////                                                                                      ///////////////////////////////
## ////////////////////////////////                                                                                      ///////////////////////////////
## ////////////////////////////////                                                                                      ///////////////////////////////

image Doreen_Finger_Animation:
    # Core Animation for Fingering Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
        ConditionSwitch(                                                # backside of the hand
            "Speed == 1", "Doreen_Finger_1",
            "Speed >= 2", "Doreen_Finger_2",
            "True", "Doreen_Finger_0",
            ),
    anchor (0.5,0.5)#anchor (0.51, -1.3)
    offset (400,945)#700,1190
    zoom 0.8
    # end Core Animation for Fingering Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <

image Doreen_Finger_0:
    # Animation for Fingering Zero's pussy, static < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Doreen_Sprite"
            pos (350,-550)
            zoom 2.15
    contains:
            ConditionSwitch(
                "Player.Wet", "DoreenBJFace/Doreen_Fingering_wet.png",
                "True", "DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_Fingering_Under.png",
                )
            anchor (0.5,0.6)
            pos (-5,50)#(20,50)
            xzoom -1

#            "Doreen_Finger_Under"
    contains:
            "Zero_Pussy"
    contains:
            "DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_Fingering_Over.png"
            anchor (0.5,0.6)
            pos (-5,50)#(20,50)
            xzoom -1
#            "Doreen_Finger_Over"
    # end Animation for Fingering Zero's pussy, static < < < < < < < < < < < < < < < < < < < < < < < <

image Doreen_Finger_1:
    # Animation for Fingering Zero's pussy, slow < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Doreen_Sprite"
            pos (350,-550)
            zoom 2.15
            block:
                ease 0.5 ypos -540 #rotate 3   100
                pause 0.25
                ease 1.0 ypos -550 #rotate -3  40
                repeat
    contains:
            ConditionSwitch(
                "Player.Wet", "DoreenBJFace/Doreen_Fingering_wet.png",
                "True", "DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_Fingering_Under.png",
                )
            subpixel True
        #    xpos 10
            anchor (0.5,0.6)
            xzoom -1
            transform_anchor True
            pos (-5,50)#(15,50)
            rotate -5
            block:
                ease .5 pos (-10,115) rotate 0 #(40,65)   Bottom
                pause 0.25
                ease 1.0 pos (-5,40) rotate -5 #(40,0) Top                 pause 0.1
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
            "DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_Fingering_Over.png"
#            "Doreen_Finger_Over"
            subpixel True
        #    xpos 10
            anchor (0.5,0.6)
            xzoom -1
            transform_anchor True
            pos (-5,50)#(15,50)
            rotate -5
            block:
                ease .5 pos (-10,115) rotate 0 #(40,65)   Bottom
                pause 0.25
                ease 1.0 pos (-5,40) rotate -5 #(40,0) Top                 pause 0.1
                repeat
    # end Animation for Fingering Zero's pussy, slow < < < < < < < < < < < < < < < < < < < < < < < <

image Doreen_Finger_2:
    # Animation for Fingering Zero's pussy, fast < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Doreen_Sprite"
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
                "Player.Wet", "DoreenBJFace/Doreen_Fingering_wet.png",
                "True", "DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_Fingering_Under.png",
                )
            subpixel True
            anchor (0.5,0.6)
            xzoom -1
            transform_anchor True
#            rotate -15
            pos (-10,30)#(10,30)
            block:
                ease 0.15 ypos 125 #rotate 3   65
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
            "DoreenBJFace/[DoreenX.skin_image.skin_path]Doreen_Fingering_Over.png"
#            "Doreen_Finger_Over"
            subpixel True
            anchor (0.5,0.6)
            xzoom -1
            transform_anchor True
#            rotate -15
            pos (-10,30)#(10,30)
            block:
                ease 0.15 ypos 125 #rotate 3   65
                pause 0.1
                ease 0.45 ypos 60 #rotate -3  30
                pause 0.1
                repeat
    # end Animation for Fingering Zero's pussy, fast < < < < < < < < < < < < < < < < < < < < < < < <

label Doreen_Finger_Launch(Line = Trigger):
    if renpy.showing("Doreen_Finger_Animation"):
        $ Trigger = "finger"
        return

    if Player.Male == 1:
        call Doreen_HJ_Launch
        return

    call Girl_Hide(DoreenX)
    $ DoreenX.Arms = 0
    $ DoreenX.ArmPose = 2
    if not renpy.showing("Doreen_Sprite"):
        show Doreen_Sprite at SpriteLoc(DoreenX.SpriteLoc) zorder 150:
            alpha 1 zoom 1.7 xpos 850 yoffset 200 #offset (-50,200)
        with dissolve
    show Doreen_Sprite at SpriteLoc(DoreenX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 1.7 xpos 850 yoffset 200 #offset (-50,200)

    if Taboo and Line == "L":
        # Doreen gets started. . .
        if len(Present) >= 2:
            if Present[0] != DoreenX:
                    "[DoreenX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
            elif Present[1] != DoreenX:
                    "[DoreenX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
        else:
                    "[DoreenX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
        if not DoreenX.Hand and DoreenX.Arms:
            "Когда вы стягиваете свои штаны, [DoreenX.Name] снимает перчатки и нерешительно тянется к вашей киске. Затем она начинает грубо ласкать ее."
        else:
            "Затем она наклоняется и хватает ваш член."
    elif Line == "L":
        if not DoreenX.Hand and DoreenX.Arms:
            "Когда вы стягиваете свои штаны, [DoreenX.Name] снимает перчатки и нерешительно тянется к вашей киске. Затем она начинает грубо ласкать ее."
        else:
            "[DoreenX.Name] наклоняется и кладет руку вам на киску."
    else:
            "[DoreenX.Name] наклоняется и кладет руку вам на киску."

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "finger"
    show Doreen_Sprite:
        alpha 0
    show Doreen_Finger_Animation at SpriteLoc(DoreenX.SpriteLoc) zorder 150 with fade
    return

label Doreen_Finger_Reset: # The sequence to the Doreen animations from handjob to default
    if not renpy.showing("Doreen_Finger_Animation"):
        return
    $ Speed = 0
    hide Doreen_Finger_Animation
    with dissolve
    call Girl_Hide(DoreenX)
    show Doreen_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 yoffset 50
        pause .5
        ease .5 zoom 1 xpos DoreenX.SpriteLoc yoffset 0
    show Doreen_Sprite at SpriteLoc(DoreenX.SpriteLoc) zorder DoreenX.Layer:
        alpha 1 zoom 1 xpos DoreenX.SpriteLoc yoffset 0
    return

## ////////////////////////////////                                                                                      ///////////////////////////////
## ////////////////////////////////                                                                                      ///////////////////////////////
## ////////////////////////////////                                                                                      ///////////////////////////////


# Start Doreen 69 Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

image Doreen_69_Animation:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
                #Shows different upper body motion depending on events
#                "True", "Doreen_69_Anim1",
                "Speed == 2", "Doreen_69_Anim2",
                "Speed == 3", "Doreen_69_Anim3",
                "Speed == 4", "Doreen_69_Anim4",
                "Speed == 5", "Doreen_69_Anim5",
                "Speed == 6", "Doreen_69_Anim6",
                "Speed", "Doreen_69_Anim1",
                "True", "Doreen_69_Static",
                ),
        )
    align (0.6,0.0)
    pos (475,-700)#(475,-700)
    zoom 1.8#1/3

#Start Animations for Doreen's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Doreen 69 Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_69_Body:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Doreen_SexSprite
        (1120,840),

        (0,0), ConditionSwitch(
            #Base belly
            "True", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_69_Body.png",
            ),
#        (0,0), ConditionSwitch(
#            #Wet look
#            "DoreenX.Water", "images/DoreenSex/Doreen_69_Water_Body.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #bra layer
            "DoreenX.Uptop", Null(),
            #if the top's down. . .
#            "DoreenX.Chest == 'bikini top'", "images/DoreenSex/Doreen_69_Over_Green.png",
            "DoreenX.Chest == 'sports bra'", "images/DoreenSex/Doreen_69_Over_Green.png",
#            "DoreenX.Chest == 'tan bra'", "images/DoreenSex/Doreen_69_Over_Bra.png",
            "DoreenX.Chest == 'lace bra'", "images/DoreenSex/Doreen_69_Over_Lace.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #shirt layer
            "DoreenX.Uptop", Null(),
            "DoreenX.Over == 'towel'", "images/DoreenSex/Doreen_69_Over_Towel.png",
            "DoreenX.Over == 'sweater'", "images/DoreenSex/Doreen_69_Over_Sweater.png",
            "DoreenX.Over == 'tshirt'", "images/DoreenSex/Doreen_69_Over_Tshirt.png",
            "DoreenX.Over == 'tube top'", "images/DoreenSex/Doreen_69_Over_Tube.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'belly' in DoreenX.Spunk and Player.Male", "images/DoreenSex/Doreen_69_Spunk_Belly.png",
            "True", Null(),
            ),
#        (0,0), "images/DoreenSex/Doreen_Sex_HeadRef.png",
        )
    offset (10,0)#(50,0)#(250,250)#(175,175)
#    yoffset -163
# End Doreen 69 Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Doreen 69 Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_69_Tits:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Doreen_SexSprite
        (1120,840),

        (0,0), ConditionSwitch(
            #tops under
            "not DoreenX.Uptop", Null(),
            #if the top's down. . .
            "DoreenX.Chest == 'bikini top'", "images/DoreenSex/Doreen_69_Under_Green.png",
            "DoreenX.Chest == 'sports bra'", "images/DoreenSex/Doreen_69_Under_Green.png",
            "DoreenX.Chest == 'tan bra'", "images/DoreenSex/Doreen_69_Under_Bra.png",
            "DoreenX.Chest == 'lace bra'", "images/DoreenSex/Doreen_69_Under_Lace.png",
            #shirt layer
            "DoreenX.Over == 'sweater'", "images/DoreenSex/Doreen_69_Under_Sweater.png",
            "DoreenX.Over == 'tshirt'", "images/DoreenSex/Doreen_69_Under_Lace.png",
            "DoreenX.Over == 'tube top'", "images/DoreenSex/Doreen_69_Under_Tube.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            # base tits
            "True", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_69_Tits.png",
            ),
#        (0,0), ConditionSwitch(
#            #Wet look
#            "DoreenX.Water", "images/DoreenSex/Doreen_69_Water_Body.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #bra layer
#            "(DoreenX.Chest == 'swimsuit' and DoreenX.Uptop) or DoreenX.Panties == 'swimsuit'", "images/DoreenSex/Doreen_69_Chest_Bikini_Up.png",
#            "DoreenX.Uptop", ConditionSwitch(
#                    #if top's up
#                    "DoreenX.Chest == 'sports bra'", "images/DoreenSex/Doreen_69_Chest_Sports_Up.png",
#                    "DoreenX.Chest == 'bra'", "images/DoreenSex/Doreen_69_Chest_Bra_Up.png",
#                    "DoreenX.Chest == 'lace bra'", "images/DoreenSex/Doreen_69_Chest_Lace_Up.png",
#                    "True", Null(),
#                    ),
#            #if the top's down. . .
#            "DoreenX.Chest == 'swimsuit' or DoreenX.Panties == 'swimsuit'", "images/DoreenSex/Doreen_69_Chest_Bikini.png",
#            "DoreenX.Chest == 'sports bra'", "images/DoreenSex/Doreen_69_Chest_Sports.png",
#            "DoreenX.Chest == 'bra'", "images/DoreenSex/Doreen_69_Chest_Bra.png",
#            "DoreenX.Chest == 'lace bra'", "images/DoreenSex/Doreen_69_Chest_Lace.png",
#            "True", Null(),
#            ),

#        (0,0), ConditionSwitch(
#            #shorts X layer
#            "DoreenX.Legs == 'shorts' and not DoreenX.Upskirt", "images/DoreenSex/Doreen_Sex_Over_Shorts.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #shirt layer
#            "DoreenX.Over == 'pink top' and DoreenX.Uptop", "images/DoreenSex/Doreen_69_Over_Pink_Up.png",
#            "DoreenX.Over == 'tank' and DoreenX.Uptop", "images/DoreenSex/Doreen_69_Over_Tank_Up.png",
#            "DoreenX.Uptop", Null(),
#            "DoreenX.Over == 'towel'", "images/DoreenSex/Doreen_69_Over_Towel.png",
#            "DoreenX.Over == 'jacket'", "images/DoreenSex/Doreen_69_Over_Jacket.png",
#            "DoreenX.Over == 'pink top'", "images/DoreenSex/Doreen_69_Over_Pink.png",
#            "DoreenX.Over == 'tank'", "images/DoreenSex/Doreen_69_Over_Tank.png",
#            "True", Null(),
#            ),


        (0,0), ConditionSwitch(
            #bra layer
            "DoreenX.Uptop", Null(),
            #if the top's down. . .
            "DoreenX.Chest == 'bikini top'", "images/DoreenSex/Doreen_69_Tits_Green.png",
            "DoreenX.Chest == 'sports bra'", "images/DoreenSex/Doreen_69_Tits_Green.png",
            "DoreenX.Chest == 'tan bra'", "images/DoreenSex/Doreen_69_Tits_Bra.png",
            "DoreenX.Chest == 'lace bra'", "images/DoreenSex/Doreen_69_Tits_Lace.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #shirt layer
            "DoreenX.Uptop", Null(),
            "DoreenX.Over == 'towel'", "images/DoreenSex/Doreen_69_Tits_Towel.png",
            "DoreenX.Over == 'sweater'", "images/DoreenSex/Doreen_69_Tits_Sweater.png",
            "DoreenX.Over == 'tshirt'", "images/DoreenSex/Doreen_69_Tits_Tshirt.png",
            "DoreenX.Over == 'tube top'", "images/DoreenSex/Doreen_69_Tits_Tube.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #piercings
            "not DoreenX.Pierce", Null(),
            "DoreenX.Pierce == 'ring'", ConditionSwitch(
                    # ring pierce
                    "DoreenX.Uptop", "images/DoreenSex/Doreen_69_Pierce_Tits_R.png",

                    "DoreenX.Over == 'tube top'", "images/DoreenSex/Doreen_69_Pierce_Tits_R_Brown.png",
                    "DoreenX.Over == 'towel'", "images/DoreenSex/Doreen_69_Pierce_Tits_R_Green.png",
                    "DoreenX.Over == 'sweater'", "images/DoreenSex/Doreen_69_Pierce_Tits_R_Sweater.png",
                    "DoreenX.Over", "images/DoreenSex/Doreen_69_Pierce_Tits_R_Tshirt.png",                  #tshirt

                    "DoreenX.Chest == 'lace bra'", "images/DoreenSex/Doreen_69_Pierce_Tits_R_Lace.png",
                    "DoreenX.Chest == 'tan bra'", "images/DoreenSex/Doreen_69_Pierce_Tits_R_Tan.png",
                    "DoreenX.Chest", "images/DoreenSex/Doreen_69_Pierce_Tits_R_Green.png",

                    "True", "images/DoreenSex/Doreen_69_Pierce_Tits_R.png",
                    ),
            "DoreenX.Uptop", "images/DoreenSex/Doreen_69_Pierce_Tits_B.png",

            "DoreenX.Over == 'tube top'", "images/DoreenSex/Doreen_69_Pierce_Tits_B_Brown.png",
            "DoreenX.Over == 'towel'", "images/DoreenSex/Doreen_69_Pierce_Tits_B_Green.png",
            "DoreenX.Over == 'sweater'", "images/DoreenSex/Doreen_69_Pierce_Tits_B_Sweater.png",
            "DoreenX.Over", "images/DoreenSex/Doreen_69_Pierce_Tits_B_Tshirt.png",                  #tshirt

            "DoreenX.Chest == 'lace bra'", "images/DoreenSex/Doreen_69_Pierce_Tits_B_Lace.png",
            "DoreenX.Chest == 'tan bra'", "images/DoreenSex/Doreen_69_Pierce_Tits_B_Tan.png",
            "DoreenX.Chest", "images/DoreenSex/Doreen_69_Pierce_Tits_B_Green.png",

            "True", "images/DoreenSex/Doreen_69_Pierce_Tits_B.png",
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'tits' in DoreenX.Spunk and Player.Male", "images/DoreenSex/Doreen_69_Spunk_Tits.png",
            "True", Null(),
            ),
#        (0,0), "images/DoreenSex/Doreen_Sex_HeadRef.png",
        )
    offset (10,0)#(250,250)#(175,175)
#    yoffset -163
# End Doreen 69 Pose Tits / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Doreen 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_69_Head:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Doreen_SexSprite
        (1120,840),
        (0,0), ConditionSwitch(
            #tongue
            "renpy.showing('Doreen_69_CUN') and Speed != 3", "images/DoreenSex/Doreen_69_Tongue.png",
            "Speed == 1", "images/DoreenSex/Doreen_69_Tongue.png",
            "True", Null(),
            ),
        (0,0), "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_69_Head.png",
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'mouth' in DoreenX.Spunk and Player.Male", "images/DoreenSex/Doreen_69_Spunk_Mouth.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #collar
#            "Speed == 1 and Player.Male", Null(),
#            "DoreenX.Chest == 'swimsuit' or DoreenX.Panties == 'swimsuit'", "images/DoreenSex/Doreen_69_Collar.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #Hair over
            "Speed == 1 and Player.Male", Null(),
            "True", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_69_Hair.png",
            ),
        )
    offset (10,0)#(175,175)#(180,100)
#    yoffset -163
# End Doreen 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Doreen 69 Pose Hair Over / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_69_HairOver:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Doreen_SexSprite
        (1120,840),
        (0,0), ConditionSwitch(
            #Hair over
#            "renpy.showing('Doreen_TJ_Animation')", Null(),
            "DoreenX.Hair == 'blonde'", "images/DoreenSex/Doreen_69_Hair_Blonde_Lick.png",
            "DoreenX.Hair == 'long' or DoreenX.Hair == 'wetlong'", "images/DoreenSex/Doreen_69_Hair_Long_Lick.png",
            "True", "images/DoreenSex/Doreen_69_Hair_Short_Lick.png",
            ),
        )
    offset (175,175)#(180,100)
#    yoffset -163
# End Doreen 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Doreen 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_69_HairBack:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Doreen_SexSprite
        (1120,840),
#        (0,0), "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_69_Head.png",
        (0,0), ConditionSwitch(
            #Hair over
#            "renpy.showing('Doreen_TJ_Animation')", Null(),
            "DoreenX.Hair == 'blonde'", "images/DoreenSex/Doreen_69_Hair_Blonde_Under.png",
            "DoreenX.Hair == 'long' or DoreenX.Hair == 'wetlong'", "images/DoreenSex/Doreen_69_Hair_Long_Under.png",
#            "DoreenX.Hair == 'wet' or DoreenX.Hair == 'wetlong' or DoreenX.Water", "images/DoreenSex/Doreen_69_Hair_Long.png",
#            "not Player.Male and 'facial' in DoreenX.Spunk","images/DoreenSex/Doreen_Sprite_Hair_Wet.png",
            "True", "images/DoreenSex/Doreen_69_Hair_Short_Under.png",
            ),
        )
    offset (175,175)#(175,175)
#    yoffset -163
# End Doreen 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Doreen 69 Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_69_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Doreen_SexSprite
        (1120,880),
#        (0,0), ConditionSwitch(
#            #scarf
#            "DoreenX.Acc", "images/DoreenSex/Doreen_69_Scarf.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #back of skirt Layer
            "DoreenX.Legs == 'skirt'", "images/DoreenSex/Doreen_69_Legs_Skirt.png",
            "DoreenX.Legs == 'red skirt'", "images/DoreenSex/Doreen_69_Legs_RedSkirt.png",
            "DoreenX.Over == 'towel'", "images/DoreenSex/Doreen_69_Legs_Towel.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs
#            "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_FBase.png",
#            "Player.Sprite and Player.Cock == 'in' and Speed", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_FBase.png",
#            "Player.Sprite and Player.Cock == 'in' and Speed", "Doreen_Sex_Heading_Pussy",
#            "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Ass.png",
#            "Trigger == 'lick pussy'", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Ass.png",
            "True", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_69_Ass.png",
            ),

        (0,0), ConditionSwitch(
            #ass red
            "DoreenX.Red", "images/DoreenSex/Doreen_Sex_Red.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            "Player.Sprite and Player.Cock == 'anal'", "images/DoreenSex/Doreen_Sex_Anus_Cover.png",
#            "True", Null(),
#            ),

#        (0,0), ConditionSwitch(
#            #Wet look
#            "not DoreenX.Water", Null(),
#            "True", "images/DoreenSex/Doreen_69_Water_Legs.png",
#            ),

        (0,0), "Doreen_69_Anus",
            #Anus Composite  (0,-10)

        (0,0), "Doreen_69_Pussy",
            #Pussy Composite


        (0,0), ConditionSwitch(    #165,560
            #Personal Wetness
            "not DoreenX.Wet", Null(),
            "(DoreenX.Legs == 'yoga pants' or DoreenX.Legs == 'shorts') and not DoreenX.Upskirt", Null(),
            "DoreenX.Panties and not DoreenX.PantiesDown", Null(),
            "DoreenX.Wet == 1", AlphaMask("Wet_Drip_69","images/BetsySex/Betsy_69_Mask_Pussy.png"), #"Wet_Drip_69",
            "True", AlphaMask("Wet_Drip2_69","images/BetsySex/Betsy_69_Mask_Pussy.png"), #"Wet_Drip2_69",
            ),

        (-6,12), ConditionSwitch(    #-695,-480
            #anal Spunk
            "'anal' not in DoreenX.Spunk or not Player.Male", Null(),
            "(DoreenX.Legs == 'yoga pants' or DoreenX.Legs == 'shorts') and not DoreenX.Upskirt", Null(),
#            "True", "Spunk_Drip2_69", #"Spunk_Drip_69",
            "True", AlphaMask("Spunk_Drip_69_Anal","images/BetsySex/Betsy_69_Mask_Ass.png"), #"Spunk_Drip_69",
            ),
        (-6,12), ConditionSwitch(
            #anal Spunk
            "'anal' in DoreenX.Spunk", "images/BetsySex/Betsy_69_Spunk_Ass.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #hose layer
            "DoreenX.Hose == 'stockings and garterbelt'", "images/DoreenSex/Doreen_69_Hose_StockingsGarter.png",
            "DoreenX.Hose == 'garterbelt'", "images/DoreenSex/Doreen_69_Hose_Garter.png",
            "DoreenX.Hose == 'stockings'", "images/DoreenSex/Doreen_69_Hose_Stockings.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Panties if up
            "DoreenX.PantiesDown", ConditionSwitch(
                    #If she has panties down. . .
                    "DoreenX.Panties == 'lace panties'", "images/DoreenSex/Doreen_69_Panties_Lace_Down.png",
                    "DoreenX.Panties == 'bikini bottoms'", "images/DoreenSex/Doreen_69_Panties_Bikini_Down.png",
                    "DoreenX.Panties and DoreenX.Wet", "images/DoreenSex/Doreen_69_Panties_Tan_Down_Wet.png",
                    "DoreenX.Panties", "images/DoreenSex/Doreen_69_Panties_Tan_Down.png",
                    "True", Null(),
                    ),

            "DoreenX.Panties == 'lace panties'", "images/DoreenSex/Doreen_69_Panties_Lace.png",
            "DoreenX.Panties == 'bikini bottoms'", "images/DoreenSex/Doreen_69_Panties_Bikini.png",
            "DoreenX.Panties and DoreenX.Wet", "images/DoreenSex/Doreen_69_Panties_Tan_Wet.png",
            "DoreenX.Panties", "images/DoreenSex/Doreen_69_Panties_Tan.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Piercings over pants and pantyhose
            "not DoreenX.Pierce", Null(),
            "DoreenX.Pierce == 'ring'",ConditionSwitch(
                    #If she has panties down. . .
                    "Player.Sprite and Player.Cock == 'in'", "images/DoreenSex/Doreen_69_Pierce_Pussy_R_Fucking.png",

#                    "DoreenX.Legs == 'shorts' and not DoreenX.Upskirt", "images/DoreenSex/Doreen_69_Pierce_Pussy_R_Brown.png",
                    "DoreenX.Hose == 'pantyhose' and not (DoreenX.Panties and DoreenX.PantiesDown)", "images/DoreenSex/Doreen_69_Pierce_Pussy_R.png",

                    "DoreenX.PantiesDown", "images/DoreenSex/Doreen_69_Pierce_Pussy_R_Fucking.png",
                    "DoreenX.Panties == 'lace panties'", "images/DoreenSex/Doreen_69_Pierce_Pussy_R_Lace.png",
                    "DoreenX.Panties == 'bikini bottoms'", "images/DoreenSex/Doreen_69_Pierce_Pussy_R_Green.png",
                    "DoreenX.Panties", "images/DoreenSex/Doreen_69_Pierce_Pussy_R_Tan.png",
                    "True", "images/DoreenSex/Doreen_69_Pierce_Pussy_R_Fucking.png",

                    "True", Null(),
                    ),
            #else, it's barbell
#            "DoreenX.Legs == 'shorts' and not DoreenX.Upskirt", "images/DoreenSex/Doreen_69_Pierce_Pussy_B_Clothed.png",
#            "DoreenX.Hose == 'pantyhose' and not (DoreenX.Panties and DoreenX.PantiesDown)", "images/DoreenSex/Doreen_69_Pierce_Pussy_Lace_B.png",

            "DoreenX.PantiesDown", "images/DoreenSex/Doreen_69_Pierce_Pussy_B.png",
#            "DoreenX.Chest == 'swimsuit'", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_B_Blue.png",
            "DoreenX.Panties == 'lace panties'", "images/DoreenSex/Doreen_69_Pierce_Pussy_B_Lace.png",
            "DoreenX.Panties", "images/DoreenSex/Doreen_69_Pierce_Pussy_B_Clothed.png",
            "True", "images/DoreenSex/Doreen_69_Pierce_Pussy_B.png",
            ),
        (0,0), ConditionSwitch(
            #pantyhose layer
            "DoreenX.Panties and DoreenX.PantiesDown", Null(),
            "DoreenX.Hose == 'pantyhose'", "images/DoreenSex/Doreen_69_Hose_Pantyhose.png",
            "DoreenX.Hose == 'tights'", "images/DoreenSex/Doreen_69_Hose_Tights.png",
            "DoreenX.Hose == 'ripped pantyhose'", "images/DoreenSex/Doreen_69_Hose_Pantyhose_Holed.png",
            "DoreenX.Hose == 'ripped tights'", "images/DoreenSex/Doreen_69_Hose_Tights_Holed.png",
            "True", Null(),
            ),


        (0,0), ConditionSwitch(
            #Legs Layer
#            "DoreenX.Legs == 'skirt' and DoreenX.Upskirt", "images/DoreenSex/Doreen_Sex_Legs_Skirt_Up.png",
#            "DoreenX.Legs == 'skirt'", "images/DoreenSex/Doreen_Sex_Legs_Skirt.png",
#            "DoreenX.Upskirt", Null(),
#            "DoreenX.Legs == 'skirt'", "images/DoreenSex/Doreen_Sex_Legs_Skirt.png",

            "DoreenX.Legs == 'shorts' and DoreenX.Upskirt and DoreenX.Wet > 1", "images/DoreenSex/Doreen_69_Legs_Shorts_Down_Wet.png",
            "DoreenX.Legs == 'shorts' and DoreenX.Upskirt", "images/DoreenSex/Doreen_69_Legs_Shorts_Down.png",
            "DoreenX.Legs == 'shorts' and DoreenX.Wet > 1", "images/DoreenSex/Doreen_69_Legs_Shorts_Wet.png",
            "DoreenX.Legs == 'shorts'", "images/DoreenSex/Doreen_69_Legs_Shorts.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Piercings over pants and pantyhose
            "not DoreenX.Pierce", Null(),
            "DoreenX.Pierce == 'ring'",ConditionSwitch(
                    #If she has panties down. . .
                    "Player.Sprite and Player.Cock == 'in'", Null(),
                    "DoreenX.Legs == 'shorts' and not DoreenX.Upskirt", "images/DoreenSex/Doreen_69_Pierce_Pussy_R_Brown.png",
                    "DoreenX.Hose == 'tights' and not (DoreenX.Panties and DoreenX.PantiesDown)", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_R_Tights.png",
                    "True", Null(),
                    ),
            #else, it's barbell
            "DoreenX.Legs == 'shorts' and not DoreenX.Upskirt", "images/DoreenSex/Doreen_69_Pierce_Pussy_B_Clothed.png",
            "DoreenX.Hose == 'tights' and not (DoreenX.Panties and DoreenX.PantiesDown)", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_B_Tights.png",
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer
#            "not Player.Sprite or Player.Cock != 'out'", Null(),
#            "Speed >= 2", "Doreen_Hotdog_Zero_Anim2",
#            "Speed", "Doreen_Hotdog_Zero_Anim1",
#            "True", "Doreen_Hotdog_Zero_Anim0",
#            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
#            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy' or Trigger2 == 'lick pussy'", "Doreen_69_Lick_Pussy",
            "Trigger == 'lick ass' or Trigger2 == 'lick ass'", "Doreen_69_Lick_Ass",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy fondling animation
            "DoreenX.Offhand == 'fondle pussy' and DoreenX.Lust > 60 and not (Player.Sprite)",  At("DoreenFingerHand", GirlFingerPussyX()), #"Doreen_Sex_Mast2",
            "DoreenX.Offhand == 'fondle pussy'", At("DoreenMastHand", GirlGropePussyX()), #"Doreen_Sex_Mast",
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Doreen_Sex_Fondle_Pussy",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Footjob overlay
#            "Player.Cock == 'foot'", Null(),
#            "Player.Sprite and Player.Cock == 'anal'",AlphaMask("Doreen_69_Feet", "images/DoreenSex/Doreen_Sex_Feet_Mask.png"),
#            "renpy.showing('Anal_Plug_In_Sex') or renpy.showing('Anal_Plug_Out_Sex')",AlphaMask("Doreen_69_Feet", "images/DoreenSex/Doreen_Sex_Feet_Mask.png"),
#            "ShowFeet", "Doreen_69_Feet",
##            "Player.Sprite", AlphaMask("Doreen_Sex_Feet", "images/DoreenSex/Doreen_Sex_Feet_Mask.png"),
##            "Trigger == 'lick pussy'", AlphaMask("Doreen_Sex_Feet", "images/DoreenSex/Doreen_Sex_Feet_Mask.png"),
##            "Trigger == 'lick ass'", AlphaMask("Doreen_Sex_Feet", "images/DoreenSex/Doreen_Sex_Feet_Mask.png"),
#            "True", AlphaMask("Doreen_69_Feet", "images/DoreenSex/Doreen_Sex_Feet_Mask.png"),
#            ),

        (0,0), "Doreen_69_Feet",
        (0,0), "Doreen_69_Tail",

#        (0,0), ConditionSwitch(                                                                                 #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
#            "not Speed", "Doreen_Sex_Feet",
#            "Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Doreen_Sex_Feet", "images/DoreenSex/Doreen_Sex_FeetMask.png"),
#            "True", "Doreen_Sex_Feet",
#            ),
        )
#    offset (0,20)#(175,175)
# End Doreen 69 Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_69_Feet:
    LiveComposite(
        #the lower legs used in the sex pose, referenced by Doreen_Sex_Legs
        (1120,840),
#        (0,0), "images/DoreenSex/Doreen_Sex_Feet.png",                                                         #Legs Base

        (0,0), ConditionSwitch(
            #hose layer
            "(DoreenX.Hose == 'pantyhose' or DoreenX.Hose == 'ripped pantyhose') and DoreenX.Panties and DoreenX.PantiesDown", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_69_Feet.png",
            "(DoreenX.Hose == 'tights' or DoreenX.Hose == 'ripped tights') and DoreenX.Panties and DoreenX.PantiesDown", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_69_Feet.png",
            "DoreenX.Hose == 'tights'", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_69_Feet_Tights.png",
            "DoreenX.Hose == 'ripped pantyhose'", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_69_Feet_Holed.png",
            "DoreenX.Hose == 'ripped tights'", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_69_Feet_Tights_Holed.png",
            "DoreenX.Hose and DoreenX.Hose != 'garterbelt'", "images/DoreenSex/Doreen_69_Feet_Hose.png",
            "True", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_69_Feet.png",   #Null(),
            ),

#        (0,0), ConditionSwitch(
#            #Wet look
#            "not DoreenX.Water", Null(),
#            "True", "images/DoreenSex/Doreen_69_Water_Feet.png",
#            ),
        (0,0), ConditionSwitch(
            #spunk
            "'feet' in DoreenX.Spunk", "images/DoreenSex/Doreen_Sex_Spunk_Feet.png",
            "True", Null(),
            ),
        )


image Doreen_69_Tail:
        #Tail when in Sex Pussy speed 0, attached to Sex Anus
        contains:
            ConditionSwitch(
#                "DoreenX.Tail and GhostTail", "images/DoreenDoggy/Doreen_Doggy_Tail3.png",
                "DoreenX.Tail", "images/DoreenDoggy/Doreen_Doggy_Tail.png",
                "True", Null(),
                )
            transform_anchor True
            subpixel True
#            anchor (555,520)#(0.52,0.69)
#            offset (560,660)#(560,480)
            anchor (220,440)#210,520
            offset (560,675)#(560,480)
            rotate 160
            zoom 1.5 # tight
            block:
                ease 3 rotate 190 #in.87
                ease 3 rotate 160 #out
                repeat


# Start Doreen 69 Pose Pussy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_69_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).

    contains:
            # The background plate of her pussy
            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/DoreenSex/Doreen_Sex_Pussy_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed", "Doreen_Sex_Heading_Pussy",
#                "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/DoreenSex/Doreen_Sex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/DoreenSex/Doreen_69_Pussy_Open.png",
                "DoreenX.Offhand == 'fondle pussy' and DoreenX.Lust > 60", "images/DoreenSex/Doreen_69_Pussy_Open.png",
                "True", "images/DoreenSex/Doreen_69_Pussy_Closed.png",
                )
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "not DoreenX.Wet", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/JubesSex/Jubes_Sex_WetPussy_F.png",
                "True", "images/BetsySex/Betsy_69_Water_Pussy.png",
                )
    contains:
            # pubes
            ConditionSwitch(
                "not DoreenX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/DoreenSex/Doreen_Sex_Pubes_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 1", "images/DoreenSex/Doreen_Sex_Pubes_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in'", "images/DoreenSex/Doreen_Sex_Pubes_Open.png",
#                "Player.Sprite and Player.Cock == 'out'", "images/DoreenSex/Doreen_Sex_Pubes_Open.png",
                "Trigger == 'lick pussy'", "images/DoreenSex/Doreen_69_Pubes_Open.png",
                "DoreenX.Offhand == 'fondle pussy' and DoreenX.Lust > 60", "images/DoreenSex/Doreen_69_Pubes_Open.png",
                "True", "images/DoreenSex/Doreen_69_Pubes_Closed.png",
                )
    contains:
            #Spunk
            ConditionSwitch(
                "'in' not in DoreenX.Spunk or not Player.Male", Null(),
                "(DoreenX.Legs == 'yoga pants' or DoreenX.Legs == 'shorts') and not DoreenX.Upskirt", Null(),
                "DoreenX.Panties and not DoreenX.PantiesDown", Null(),
#                "True", "Spunk_Drip_69",
                "True", AlphaMask("Spunk_Drip_69","images/BetsySex/Betsy_69_Mask_Pussy.png"),
                )
#            offset (-700,-570)

    contains:
            ConditionSwitch(
                #Outside Spunk
#                "'in' in DoreenX.Spunk and Player.Sprite and Player.Cock == 'in' and Speed and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_PussyF.png",
                "'in' in DoreenX.Spunk and Player.Male", "images/BetsySex/Betsy_69_Spunk_Pussy.png",
                "True", Null(),
                )
            offset (0,10)
#    contains:
#            #Spunk under penis
#            ConditionSwitch(
#                "'in' in DoreenX.Spunk", "images/DoreenSex/Doreen_Sex_Spunk_Puss_Under.png",
#                "True", Null(),
#                )
#    contains:
#            #hose layer
#            ConditionSwitch(
#                "DoreenX.Panties and DoreenX.PantiesDown", Null(),
#                "DoreenX.Hose == 'ripped pantyhose' and ShowFeet", "images/DoreenSex/Doreen_Sex_Hose_Pantyhose_Holed.png",
#                "DoreenX.Hose == 'ripped pantyhose'", "images/DoreenSex/Doreen_Sex_Hose_Pantyhose_Holed.png",
#                "True", Null(),
#                ),
#    contains:
#            # The animation of Zero's moving penis, masked by her pussy shape
#            ConditionSwitch(
##                "not Player.Sprite", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 3", AlphaMask("Doreen_Sex_Fucking_Zero_Anim3", "Doreen_Sex_Fucking_Mask"),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", AlphaMask("Doreen_Sex_Fucking_Zero_Anim2", "Doreen_Sex_Fucking_Mask"),
#                "Player.Sprite and Player.Cock == 'in' and Speed == 1", AlphaMask("Doreen_Sex_Fucking_Zero_Anim1", "Doreen_Sex_Heading_Mask"),
#                "Player.Sprite and Player.Cock == 'in'", "Doreen_Sex_Fucking_Zero_Anim0",
#                "True", Null(),
#                )
#    contains:
#            #Piercings
#            ConditionSwitch(
#                "DoreenX.Pierce == 'barbell' and Player.Sprite and Player.Cock == 'in' and Speed", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_BarbellF.png",
#                "DoreenX.Pierce == 'ring' and Player.Sprite and Player.Cock == 'in' and Speed", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_RingF.png",
#                "DoreenX.Pierce == 'barbell'", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_Barbell.png",
#                "DoreenX.Pierce == 'ring'", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_Ring.png",
#                "True", Null(),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed == 1", "Doreen_Pussy_Spunk_Heading",
#                "True", Null(),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "Speed == 1", Null(),
#                "'in' not in DoreenX.Spunk or not Player.Sprite or Player.Cock != 'in' or not Speed or not Player.Male", Null(),
##                "Speed <= 1", Null(), #"Doreen_Pussy_Spunk_Heading",
#                "True", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
#                )

    #End Doreen Pussy composite


image Doreen_69_Lick_Pussy:
        "Lick_AnimF"
        zoom 0.7
        rotate 180
        offset (510,500)#(535,500
image Doreen_69_Lick_Ass:
        "Lick_AnimF"
        zoom 0.7
        rotate 180
        offset (535,580)#(535,550)

image Doreen_69_Fondle_Pussy:
        "GropePussy_Doreen"
        xzoom -1.5
        yzoom 1.5
        offset(-710,-300) #(-890,-300)
#        block:
#            ease 1 offset(-1000,0) #(535,500)
#            ease 1 offset(-1000,-1000) #(535,500)
#            ease 1 offset(0,-1000) #(535,500)
#            ease 1 offset(0,0) #(535,500)
#            repeat

image Doreen_69_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/JubesSex/Jubes_Sex_Anal.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/JubesSex/Jubes_Sex_Anal.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/DoreenSex/Doreen_Sex_Anus.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/DoreenSex/Doreen_Sex_Anus.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed", "Doreen_Sex_Anal_Heading",
#            "Player.Sprite and Player.Cock == 'anal'", "Doreen_Sex_Anal_Tip",
            "DoreenX.Plug", "images/PlugBase_Sex.png",
            "DoreenX.Loose > 2", "Doreen_Gape_Anal_Sex",
#            "DoreenX.Loose", "images/DoreenSex/Doreen_Sex_Anus_Loose.png",
            "True", "images/DoreenSex/Doreen_Sex_Anus_Loose.png",
            "True", Null(),
            )
#    contains:
#            #Spunk under penis
#            ConditionSwitch(
#                "'anal' not in DoreenX.Spunk or not Player.Male", Null(),
##                "Player.Sprite and Player.Cock != 'anal' and Speed >= 1", "images/DoreenSex/Doreen_Sex_Spunk_Anal_Under.png",
##                "Player.Sprite and Player.Cock == 'anal' and Speed == 1", "Doreen_Sex_Anal_Spunk_Heading_Under",
#                "True", "images/DoreenSex/Doreen_69_Spunk_Ass.png",
#                )
#            offset (5,0)
#    contains:
#            # The animation of Zero's moving penis, masked by her anus shape
#            ConditionSwitch(
#                "not Player.Sprite or Player.Cock != 'anal'", Null(),
#                "Speed >= 3",  AlphaMask("Doreen_Sex_Anal_Zero_Anim3", "Doreen_Sex_Anal_MaskF"),
#                "Speed >= 2", AlphaMask("Doreen_Sex_Anal_Zero_Anim2", "Doreen_Sex_Anal_MaskF"),
#                "Speed", AlphaMask("Doreen_Sex_Anal_Zero_Anim1", "Doreen_Sex_Anal_Mask"),
#                "True", AlphaMask("Doreen_Sex_Anal_Zero_Anim0", "Doreen_Sex_Anal_Mask"),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "'anal' not in DoreenX.Spunk or not Player.Sprite or Player.Cock != 'anal' or not Speed or not Player.Male", Null(),
#                "Speed == 1", "Doreen_Sex_Anal_Spunk_Heading_Over",
#                "True", "Doreen_Sex_Anal_Spunk",
#                )


#Start Animations for Doreen's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_69_Static:
        #this is the animation for Doreen's hairback during 69, Speed 0 (static)
#        contains:
#            subpixel True
#            "Doreen_69_HairBack"
#            rotate 180
#            zoom .75
##            offset (180,50)#(180,100)
#            pos (0,-35) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                easein 1.75 pos (0,-40) #top
##                pause .5
#                ease 1.25 pos (0,-35) #bottom
#                repeat
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
            offset (675,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Doreen's head during 69, Speed 0 (static)
        contains:
            subpixel True
            "Doreen_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-65) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-70) #top
#                pause .5
                ease 1.25 pos (0,-65) #bottom
                repeat
        #this is the animation for Doreen's upper body during 69, Speed 0 (static)
        contains:
            "Doreen_69_Tits"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,-35) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,-40) #top
                pause .25
                ease 1 pos (0,-35) #bottom
                repeat
        contains:
            "Doreen_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,-10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,-20) #top
                pause .25
                ease 1 pos (0,-10) #bottom
                repeat
        #this is the animation for Doreen's lower body during 69, Speed 0 (static)
        contains:
            "Doreen_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat

#Start Animations for Doreen's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_69_Anim1:
        #this is the animation for Doreen's hairback during 69, Speed 1 (licking)
#        contains:
#            subpixel True
#            "Doreen_69_HairBack"
#            rotate 180
#            zoom .75
##            offset (180,50)#(180,100)
#            pos (45,60) #X less is left, Y less is up
#            block:
#                #Total time, 5 seconds
#                pause .5
#                easein .75 pos (15,-25) #top(10,-25
#                pause 1.25
#                ease 2.5 pos (45,60) #bottom(30,60)
#                repeat
        #this is the animation for Zero's cock during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (675,900)#(690,900)
            pos (0,0) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .50 rotate 0
                pause 1.75
                ease 1.5 rotate -5
                pause .75
                repeat
        #this is the animation for Doreen's head during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Doreen_69_Head"
            rotate 220
#            zoom .75
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
        #this is the animation for Doreen's upper body during 69, Speed 1 (licking)
        contains:
            subpixel True
            "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_69_Hair.png"
            rotate 180
#            zoom .75
            offset (10,0)
#            offset (180,50)#(180,100)
            pos (30,40) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (10,-30) #top(10,-25
                pause 1.50
                ease 2.25 pos (45,55) #bottom(30,60)
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 rotate 180
                pause 1.50
                ease 2.25 rotate 210
                repeat
        contains:
            subpixel True
            "Doreen_69_Tits"
            rotate 180
#            zoom .65
            pos (30,40) #X less is left, Y less is up
            block:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (10,-10) #top
                pause 1.25
                ease 2.5 pos (30,40) #bottom
                repeat
        contains:
            subpixel True
            "Doreen_69_Body"
            rotate 180
#            zoom .65
            pos (30,40) #X less is left, Y less is up
            block:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (10,0) #top
                pause 1.25
                ease 2.5 pos (30,40) #bottom
                repeat
        #this is the animation for Doreen's lower body during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Doreen_69_Legs"
            rotate 180
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 5 seconds
                pause .25
                easein 1 pos (0,-5)
                pause 1
                ease 2.75 pos (0,0)
                repeat

#Start Animations for Doreen's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_69_Anim2:
        #this is the animation for Doreen's hairback during 69, Speed 2 (heading)
#        contains:
#            subpixel True
#            "Doreen_69_HairBack"
#            rotate 180
#            zoom .75
##            offset (180,50)#(180,100)
#            pos (0,-5) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                easein 1.75 pos (0,-30) #top
##                pause .5
#                ease 1.25 pos (0,-5) #bottom
#                repeat
        #this is the animation for Zero's cock during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (675,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Doreen's head during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Doreen_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-60) #top
#                pause .5
                ease 1.25 pos (0,-30) #bottom
                repeat
        #this is the animation for Doreen's upper body during 69, Speed 2 (heading)
        contains:
            "Doreen_69_Tits"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,-20) #top
                pause .25
                ease 1 pos (0,0) #bottom
                repeat
        contains:
            "Doreen_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,-10) #top
                pause .25
                ease 1 pos (0,0) #bottom
                repeat
        #this is the animation for Doreen's lower body during 69, Speed 2 (heading)
        contains:
            "Doreen_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat

#Start Animations for Doreen's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_69_Anim3:
        #this is the animation for Doreen's hairback during 69, Speed 3 (sucking)
#        contains:
#            subpixel True
#            "Doreen_69_HairBack"
#            rotate 180
#            zoom .75
##            offset (180,50)#(180,100)
#            pos (0,50) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                easein .75 pos (0,0) #top
##                pause .5
#                ease 1.25 pos (0,50) #bottom
#                repeat
#        #this is the animation for Zero's cock during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (675,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Doreen's head during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Doreen_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-20) #top
#                pause .5
                ease 1.25 pos (0,30) #bottom
                repeat
        #this is the animation for Doreen's upper body during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Doreen_69_Tits"
            rotate 180
            anchor (560,400)#(560,330) + is right and down
            offset (700,715)#(-560,-330) + is right and down
            transform_anchor True
#            zoom .65
            pos (0,30) #X less is left, Y less is up
#            alpha .9
            parallel:
                #Total time, 3 seconds
                easein .75 pos (0,-5) #top
                ease 1.25 pos (0,30) #bottom
                repeat
            parallel:
                #Total time, 3 seconds
                ease .15 yzoom 1.2
                ease .25 yzoom 1
                ease .35 yzoom 1.1

                ease .5 yzoom .8
                ease .75 yzoom 1         #bottom
                repeat
        #this is the animation for Doreen's lower body during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Doreen_69_Body"
            rotate 180
#            zoom .65
            pos (0,30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-5) #top
#                pause .5
                ease 1.25 pos (0,30) #bottom
                repeat
        #this is the animation for Doreen's lower body during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Doreen_69_Legs"
            rotate 180
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,-5)
#                pause .5
                ease 1.25 pos (0,10)
                repeat

#Start Animations for Doreen's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_69_Anim4:
        #this is the animation for Doreen's hairback during 69, Speed 4 (deep)
#        contains:
#            subpixel True
#            "Doreen_69_HairBack"
#            rotate 180
#            zoom .75
##            offset (180,50)#(180,100)
#            pos (0,70) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                easein .75 pos (0,20) #top
#                pause .5
#                ease 1.75 pos (0,70) #bottom
#                repeat
        #this is the animation for Zero's cock during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (675,900)#(690,900)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Doreen's head during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Doreen_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,50) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,10) #top
                pause .5
                ease 1.75 pos (0,50) #bottom
                repeat
        #this is the animation for Doreen's upper body during 69, Speed 4 (deep)
#        contains:
#            subpixel True
#            "Doreen_69_Tits"
#            rotate 180
##            zoom .65
#            pos (0,40) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                easein .75 pos (0,5) #top
#                pause .5
#                ease 1.75 pos (0,40) #bottom
#                repeat
        contains:
            subpixel True
            "Doreen_69_Tits"
            rotate 180
            anchor (560,400)#(560,330) + is right and down
            offset (700,715)#(-560,-330) + is right and down
            transform_anchor True
#            zoom .65
            pos (0,40) #X less is left, Y less is up
#            alpha .9
            parallel:
                #Total time, 3 seconds
                easein .75 pos (0,5) #top
                pause .5
                ease 1.75 pos (0,40) #bottom
                repeat
            parallel:
                #Total time, 3 seconds
                ease .15 yzoom 1.2
                ease .25 yzoom 1
                ease .35 yzoom 1.1
                pause .5
                ease .5 yzoom .9
                ease 1.25 yzoom 1         #bottom
                repeat
        contains:
            subpixel True
            "Doreen_69_Body"
            rotate 180
#            zoom .65
            pos (0,40) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,5) #top
                pause .5
                ease 1.75 pos (0,40) #bottom
                repeat
        #this is the animation for Doreen's lower body during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Doreen_69_Legs"
            rotate 180
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,-5)
#                pause .5
                ease 2.25 pos (0,10)
                repeat

#Start Animations for Doreen's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_69_Anim5:
        #this is the animation for Doreen's hairback during 69, Speed 5 (cum high)
#        contains:
#            subpixel True
#            "Doreen_69_HairBack"
#            rotate 180
#            zoom .75
##            offset (180,50)#(180,100)
#            pos (0,5) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                easein .75 pos (0,0) #top
##                pause .5
#                ease 1.25 pos (0,5) #bottom
#                repeat
        #this is the animation for Zero's cock during 69, Speed 5 (cum high)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (675,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Doreen's head during 69, Speed 5 (cum high)
        contains:
            subpixel True
            "Doreen_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-50) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-60) #top
#                pause .5
                ease 1.25 pos (0,-50) #bottom
                repeat
        #this is the animation for Doreen's upper body during 69, Speed 5 (cum high)
        contains:
            "Doreen_69_Tits"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,-10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .5
                easein 1.75 pos (0,-20) #top
#                pause .5
                ease 1.25 pos (0,-10) #bottom
                repeat
        contains:
            "Doreen_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .5
                easein 1.75 pos (0,-10) #top
#                pause .5
                ease 1.25 pos (0,0) #bottom
                repeat
        #this is the animation for Doreen's lower body during 69, Speed 5 (cum high)
        contains:
            "Doreen_69_Legs"
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

#Start Animations for Doreen's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_69_Anim6:
        #this is the animation for Doreen's hairback during 69, Speed 6 (cum deep)
#        contains:
#            subpixel True
#            "Doreen_69_HairBack"
#            rotate 180
#            zoom .75
##            offset (180,50)#(180,100)
#            pos (0,70) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                easein .75 pos (0,60) #top
#                pause .5
#                ease 1.75 pos (0,70) #bottom
#                repeat
        #this is the animation for Zero's cock during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (675,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Doreen's head during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Doreen_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,40) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,30) #top
                pause .5
                ease 1.75 pos (0,40) #bottom
                repeat
        #this is the animation for Doreen's upper body during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Doreen_69_Tits"
            rotate 180
#            zoom .65
            pos (0,30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,35) #top
                pause .5
                ease 1.75 pos (0,30) #bottom
                repeat
        contains:
            subpixel True
            "Doreen_69_Body"
            rotate 180
#            zoom .65
            pos (0,30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,35) #top
                pause .5
                ease 1.75 pos (0,30) #bottom
                repeat
        #this is the animation for Doreen's lower body during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Doreen_69_Legs"
            rotate 180
            pos (0,20) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,10)
#                pause .5
                ease 2.25 pos (0,20)
                repeat

#End Animations for Doreen's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#Start Doreen 69 Cunnilingus Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

#Start Animations for Doreen's 69 Cunnalingus pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_69_CUN:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
#                "True", "Doreen_69_Anim1",
                "Speed == 2",   "Doreen_69_Cun2",
                "Speed == 3",   "Doreen_69_Cun3",
                "Speed",        "Doreen_69_Cun1",
                "True",         "Doreen_69_Cun0",
                ),
        )
    align (0.6,0.0)
    pos (475,-700)
    zoom 1.8#1/3

#Start Animations for Doreen's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Animations for Doreen's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_69_Cun0:
        #this is the animation for Doreen's hairback during 69, Speed 0 (static)
#        contains:
#            subpixel True
#            "Doreen_69_HairBack"
#            rotate 180
#            zoom .75
##            offset (180,50)#(180,100)
#            pos (0,30) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                easein 1.75 pos (0,20) #top
##                pause .5
#                ease 1.25 pos (0,30) #bottom
#                repeat
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
        #this is the animation for Doreen's head during 69, Speed 0 (static)
        contains:
            subpixel True
            "Doreen_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (15,-20) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (15,-25) #top
#                pause .5
                ease 1.25 pos (15,-20) #bottom
                repeat
        #this is the animation for Doreen's upper body during 69, Speed 0 (static)
        contains:
            "Doreen_69_Tits"
            subpixel True
            rotate 180
#            zoom .65
            pos (10,-20) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (10,-25) #top
                pause .25
                ease 1 pos (10,-20) #bottom
                repeat
        contains:
            "Doreen_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (10,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (10,-5) #top
                pause .25
                ease 1 pos (10,0) #bottom
                repeat

#            subpixel True
#            "Doreen_69_Body"
#            rotate 180
##            zoom .65
#            pos (0,30) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                easein .75 pos (0,35) #top
#                pause .5
#                ease 1.75 pos (0,30) #bottom
#                repeat

        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (728,920)#(590,620)
        #this is the animation for Doreen's lower body during 69, Speed 0 (static)
        contains:
            "Doreen_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat

#Start Animations for Doreen's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_69_Cun1:
        #this is the animation for Doreen's hairback during 69, Speed 1 (lick)
#        contains:
#            subpixel True
#            "Doreen_69_HairBack"
#            rotate 180
#            zoom .75
##            offset (180,50)#(180,100)
#            pos (0,40) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                easein 1.0 pos (0,35) #top
#                easeout .5 pos (0,15) #top
#                ease 1.0 pos (0,40) #bottom
#                pause .5
#                repeat
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
        #this is the animation for Doreen's head during 69, Speed 1 (lick)
        contains:
            subpixel True
            "Doreen_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (18,-20) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                ease 1.0 pos (18,5) #top
                easeout .5 pos (18,-15) #top
                easein 1.0 pos (18,-20) #bottom
                pause .5
                repeat
        #this is the animation for Doreen's upper body during 69, Speed 1 (lick)
        contains:
            "Doreen_69_Tits"
            subpixel True
            rotate 180
#            zoom .65
            pos (15,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.25 pos (15,-5) #top
                pause .25
                ease 1.25 pos (15,0) #bottom
                repeat
        contains:
            "Doreen_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (10,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.25 pos (10,-5) #top
                pause .25
                ease 1.25 pos (10,0) #bottom
                repeat
        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (728,920)#(590,620)
        #this is the animation for Doreen's lower body during 69, Speed 1 (lick)
        contains:
            "Doreen_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat


#Start Animations for Doreen's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_69_Cun2:
        #this is the animation for Doreen's hairback during 69, Speed 2 (clit)
#        contains:
#            subpixel True
#            "Doreen_69_HairBack"
#            rotate 180
#            zoom .75
##            offset (180,50)#(180,100)
#            pos (0,35) #X less is left, Y less is up
#            parallel:
#                #Total time, 3 seconds
#                easein .9 pos (0,25) #top
#                easein 1.1 pos (0,35) #bottom
#                repeat
#            parallel:
#                #Total time, 3 seconds
#                easein 1.0 rotate 185 #top
#                easein 1.0 rotate 175 #bottom
#                repeat
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
        #this is the animation for Doreen's head during 69, Speed 2 (clit)
        contains:
            subpixel True
            "Doreen_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (18,0) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                easein .9 pos (18,5) #top
                easein 1.1 pos (18,0) #bottom
                repeat
            parallel:
                #Total time, 3 seconds
                easein 1.0 rotate 185 #top
                easein 1.0 rotate 175 #bottom
                repeat
        #this is the animation for Doreen's upper body during 69, Speed 2 (clit)
        contains:
            "Doreen_69_Tits"
            subpixel True
            rotate 180
#            zoom .65
            pos (10,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1 pos (10,-5) #top
                ease 1 pos (10,0) #bottom
                repeat
        contains:
            "Doreen_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (10,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1 pos (10,-5) #top
                ease 1 pos (10,0) #bottom
                repeat
        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (728,920)#(590,620)
        #this is the animation for Doreen's lower body during 69, Speed 2 (clit)
        contains:
            "Doreen_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat

#Start Animations for Doreen's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_69_Cun3:
        #this is the animation for Doreen's hairback during 69, Speed 3 (suck)
#        contains:
#            subpixel True
#            "Doreen_69_HairBack"
#            rotate 180
#            zoom .75
##            offset (180,50)#(180,100)
#            pos (0,50) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                easein 1.75 pos (0,40) #top
##                pause .5
#                ease 1.25 pos (0,50) #bottom
#                repeat
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
        #this is the animation for Doreen's head during 69, Speed 3 (suck)
        contains:
            subpixel True
            "Doreen_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (18,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (18,5) #top
#                pause .5
                ease 1.25 pos (18,10) #bottom
                repeat
        #this is the animation for Doreen's upper body during 69, Speed 3 (suck)
        contains:
            "Doreen_69_Tits"
            subpixel True
            rotate 180
#            zoom .65
            pos (10,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .3
                easein 1.5 pos (10,-5) #top
                pause .3
                ease .9 pos (10,0) #bottom
                repeat
        contains:
            "Doreen_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (10,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (10,-5) #top
                pause .25
                ease 1 pos (10,0) #bottom
                repeat
        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (728,920)#(590,620)
        #this is the animation for Doreen's lower body during 69, Speed 3 (suck)
        contains:
            "Doreen_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat
#End Animations for Doreen's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#End Doreen 69 Animations

# Start Doreen Scissor Pose content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_SC_Sprite:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
                #if the top's down. . .
                "Speed >= 2", "Doreen_SC_Anim_2",
                "Speed", "Doreen_SC_Anim_1",
                "True", "Doreen_SC_Anim_0",
                ),
        )
    align (0.6,0.0)
    pos (650,300)#(650,200)(925,740)#(910,850)
    zoom 0.85#0.8

# End Doreen Sex Pose Speed 2 Scissor / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Doreen Sex Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_SC_Body:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Doreen_SexSprite
        (1120,840),
#        (0,-100), "images/DoreenSex/Doreen_Sex_Headref.png",
#        (335,60), "Doreen_HairBack_Sex",
        (560,-30), "Doreen_Head_SC",  #(50,-325)(335,-40)
        (0,0), "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Body.png",
        (0,0), ConditionSwitch(
            #bra layer
            "DoreenX.Uptop", Null(),
            #if the top's down. . .
            "DoreenX.Chest == 'sports bra'", "images/DoreenSex/Doreen_Sex_Chest_Sports_Under.png",
#            "DoreenX.Chest == 'bikini top'", "images/DoreenSex/Doreen_Sex_Chest_Sports.png",
            "DoreenX.Chest == 'lace bra'", "images/DoreenSex/Doreen_Sex_Chest_Lace_Under.png",
#            "DoreenX.Chest", "images/DoreenSex/Doreen_Sex_Chest_Bra.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "DoreenX.Water", "images/DoreenSex/Doreen_Sex_Water_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #shirt layer
            "DoreenX.Uptop", Null(),
            "DoreenX.Over == 'towel'", "images/DoreenSex/Doreen_Sex_Over_Towel_Under.png",
            "DoreenX.Over == 'tshirt'", "images/DoreenSex/Doreen_Sex_Over_Tshirt_Under.png",
            "DoreenX.Over == 'sweater'", "images/DoreenSex/Doreen_Sex_Over_Sweater_Under.png",
            "DoreenX.Over == 'tube top'", "images/DoreenSex/Doreen_Sex_Over_Tube_Under.png",
            "True", Null(),
            ),

        (0,0),ConditionSwitch(
            #Outside Spunk
            "'belly' in DoreenX.Spunk and Player.Male", "images/DoreenSex/Doreen_Sex_Spunk_Belly.png",
            "True", Null(),
            ),
#        (0,0), "images/DoreenSex/Doreen_Sex_HeadRef.png",
        )
#    yoffset -163
# End Doreen Sex Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Doreen_Head_SC:
    # The head used for the sex pose, referenced by Doreen_Sex_Body
    contains:
        "Doreen_Sprite_HairBack"
    contains:
        "Doreen_Sprite_Head"
    anchor (10,10)
    transform_anchor True
    rotate -10#17
#    block:
#        ease 1 rotate -10#17
#        ease 1 rotate -30#17
#        repeat
#    alpha 0.5

image Doreen_HairBack_SC:
    # The hair behind the head for the sex pose, referenced by Doreen_Sex_Body
    "Doreen_Sprite_HairBack"
    zoom 1#1.36
    anchor (0.5,0.5)
    rotate 20#15

image Doreen_SC_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Doreen_SexSprite
        (1120,880),
        (545,540), ConditionSwitch(    #165,560
            #Personal Wetness
            "not DoreenX.Wet", Null(),
            "(DoreenX.Legs == 'pants' or DoreenX.Legs == 'shorts') and not DoreenX.Upskirt", Null(),
            "DoreenX.Panties and not DoreenX.PantiesDown", Null(),
            "DoreenX.Wet == 1", "Wet_Drip",
            "True", "Wet_Drip2",
            ),

        (545,540), ConditionSwitch(    #205,530
            #Spunk
            "'anal' not in DoreenX.Spunk or not Player.Male", Null(),
            "(DoreenX.Legs == 'pants' or DoreenX.Legs == 'shorts') and not DoreenX.Upskirt", Null(),
            "DoreenX.Wet == 1", "Spunk_Drip",
            "True", "Spunk_Drip2",
            ),

        (0,0), ConditionSwitch(
            #Legs
#            "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_FBase.png",
            "Player.Sprite and Player.Cock == 'in' and Speed", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_FBase.png",
#            "Player.Sprite and Player.Cock == 'in' and Speed", "Doreen_Sex_Heading_Pussy",
#            "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Ass.png",
#            "Trigger == 'lick pussy'", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Ass.png",
            "True", "images/DoreenSex/[DoreenX.skin_image.skin_path]Doreen_Sex_Ass.png",
            ),

        (0,0), ConditionSwitch(
            #ass red
            "DoreenX.Red", "images/DoreenSex/Doreen_Sex_Red.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Wet look
            "not DoreenX.Water", Null(),
            "True", "images/DoreenSex/Doreen_Sex_Water_Legs.png",
            ),

#        (0,0), "Doreen_Sex_Anus",
            #Anus Composite

        (0,0), "Doreen_SC_Pussy",
            #Pussy Composite


        (0,0), ConditionSwitch(
            #hose layer
            "DoreenX.Hose == 'stockings and garterbelt'", "images/DoreenSex/Doreen_Sex_Hose_StockingsGarter.png",
            "DoreenX.Hose == 'garterbelt'", "images/DoreenSex/Doreen_Sex_Hose_Garter.png",
            "DoreenX.Hose == 'stockings'", "images/DoreenSex/Doreen_Sex_Hose_Stockings.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Panties if up
            "DoreenX.PantiesDown", Null(),
            "DoreenX.Panties == 'lace panties'", "images/DoreenSex/Doreen_Sex_Panties_Lace.png",
            "DoreenX.Panties == 'bikini bottoms'", "images/DoreenSex/Doreen_Sex_Panties_Bikini.png",
            "DoreenX.Panties and DoreenX.Wet", "images/DoreenSex/Doreen_Sex_Panties_Tan_Wet.png",
            "DoreenX.Panties", "images/DoreenSex/Doreen_Sex_Panties_Tan.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Piercings under pants and pantyhose
            "not DoreenX.Pierce", Null(),
            "DoreenX.Pierce == 'ring'",ConditionSwitch(
                    #If she has panties down. . .
                    "Player.Sprite and Player.Cock == 'in'", "images/DoreenSex/Doreen_69_Pierce_Pussy_R_Fucking.png",

                    "DoreenX.PantiesDown", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_R.png",
                    "DoreenX.Panties == 'lace panties'", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_R_Lace.png",
                    "DoreenX.Panties == 'bikini bottoms'", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_R_Green.png",
                    "DoreenX.Panties", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_R_Tan.png",
                    "True", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_R.png",

                    "True", Null(),
                    ),
            #else, it's barbell
            "DoreenX.Legs == 'shorts' and not DoreenX.Upskirt", "images/DoreenSex/Doreen_69_Pierce_Pussy_B_Clothed.png",

            "DoreenX.PantiesDown", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_B.png",
            "DoreenX.Panties == 'lace panties'", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_B_Lace.png",
            "DoreenX.Panties == 'bikini bottoms'", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_B_Green.png",
            "DoreenX.Panties", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_B_Tan.png",
            "True", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_B.png",
            ),
        (0,0), ConditionSwitch(
            #pantyhose layer
            "DoreenX.Panties and DoreenX.PantiesDown", Null(),
            "DoreenX.Hose == 'tights'", "images/DoreenSex/Doreen_Sex_Hose_Tights.png",
            "DoreenX.Hose == 'ripped tights'", "images/DoreenSex/Doreen_Sex_Hose_Tights_Holed.png",
            "DoreenX.Hose == 'pantyhose'", "images/DoreenSex/Doreen_Sex_Hose_Pantyhose.png",
            "DoreenX.Hose == 'ripped pantyhose'", "images/DoreenSex/Doreen_Sex_Hose_Pantyhose_Holed.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs Layer
            "DoreenX.Legs == 'skirt'", "images/DoreenSex/Doreen_Sex_Legs_Skirt.png",
            "DoreenX.Legs == 'red skirt'", "images/DoreenSex/Doreen_Sex_Legs_RedSkirt.png",
            "DoreenX.Legs == 'shorts' and DoreenX.Upskirt and DoreenX.Wet > 1", "images/DoreenSex/Doreen_Sex_Legs_Shorts_Down_Wet.png",
            "DoreenX.Legs == 'shorts' and DoreenX.Upskirt", "images/DoreenSex/Doreen_Sex_Legs_Shorts_Down.png",
            "DoreenX.Legs == 'shorts' and DoreenX.Wet > 1", "images/DoreenSex/Doreen_Sex_Legs_Shorts_Wet.png",
            "DoreenX.Legs == 'shorts'", "images/DoreenSex/Doreen_Sex_Legs_Shorts.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #towel Layer
            "DoreenX.Over == 'towel'", "images/DoreenSex/Doreen_Sex_Legs_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Piercings over pants and pantyhose
            "not DoreenX.Pierce", Null(),
            "DoreenX.Pierce == 'ring'",ConditionSwitch(
                    #If she has panties down. . .
                    "Player.Sprite and Player.Cock == 'in'", Null(),
                    "DoreenX.Legs == 'shorts' and not DoreenX.Upskirt", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_R_Brown.png",
                    "DoreenX.Hose == 'tights' and not (DoreenX.Panties and DoreenX.PantiesDown)", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_R_Tights.png",
                    "True", Null(),
                    ),
            #else, it's barbell
            "DoreenX.Legs == 'shorts' and not DoreenX.Upskirt", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_B_Brown.png",
            "DoreenX.Hose == 'tights' and not (DoreenX.Panties and DoreenX.PantiesDown)", "images/DoreenSex/Doreen_Sex_Pierce_Pussy_B_Tights.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy'", "Doreen_Sex_Lick_Pussy",
            "Trigger == 'lick ass'", "Doreen_Sex_Lick_Ass",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy fondling animation
            "Trigger3 == 'fondle pussy' and DoreenX.Lust > 60 and not (Player.Sprite)",  At("DoreenFingerHand", GirlFingerPussyX()), #"Doreen_Sex_Mast2",
            "Trigger3 == 'fondle pussy'", At("DoreenMastHand", GirlGropePussyX()), #"Doreen_Sex_Mast",
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Doreen_Sex_Fondle_Pussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #tail
            "Player.Sprite and (Player.Cock == 'anal' or Player.Cock == 'in')", Null(),
            "True", "Doreen_Sex_Tail_P0",
            ),
        )
# End Doreen Scissor Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Doreen Sex Pose Pussy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Doreen_SC_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).

    contains:
            # The background plate of her pussy
            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/DoreenSex/Doreen_Sex_Pussy_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed", "Doreen_Sex_Heading_Pussy",
#                "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/DoreenSex/Doreen_Sex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/DoreenSex/Doreen_Sex_Pussy_Open.png",
                "Trigger3 == 'fondle pussy' and DoreenX.Lust > 60", "images/DoreenSex/Doreen_Sex_Pussy_Open.png",
                "True", "images/DoreenSex/Doreen_Sex_Pussy_Closed.png",
                )
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "not DoreenX.Wet", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/KittySex/Kitty_Sex_WetPussy_F.png",
                "True", "images/DoreenSex/Doreen_Sex_Wet.png",
                )
    contains:
            # pubes
            ConditionSwitch(
                "not DoreenX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/DoreenSex/Doreen_Sex_Pubes_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 1", "images/DoreenSex/Doreen_Sex_Pubes_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in'", "images/DoreenSex/Doreen_Sex_Pubes_Open.png",
#                "Player.Sprite and Player.Cock == 'out'", "images/DoreenSex/Doreen_Sex_Pubes_Open.png",
                "Trigger == 'lick pussy'", "images/DoreenSex/Doreen_Sex_Pubes_Open.png",
                "Trigger3 == 'fondle pussy' and DoreenX.Lust > 60", "images/DoreenSex/Doreen_Sex_Pubes_Open.png",
                "True", "images/DoreenSex/Doreen_Sex_Pubes_Closed.png",
                )

    #End Doreen Pussy composite

image Doreen_SC_Anim_0:
        #this is the animation for Doreen's lower body during Scissoring, Speed 0 (static)
        contains:
            subpixel True
            "Doreen_SC_Body"
            anchor (560,580)#(560,420)
            offset (560,580) #(560,580)
            transform_anchor True
            zoom 1.4
            rotate 23
            pos (10,0) #X less is left, Y less is up
            parallel:
                pause .5
                ease 2 rotate 20
                pause .5
                ease 2 rotate 23
                repeat

#            anchor (560,580)#(560,420)
#            offset (560,580) #(845,340)    #(840,390)
#            transform_anchor True
#            zoom 1.1
#            rotate 10
#            pos (30,80) #X less is left, Y less is up (0,0)
##            parallel:
##                ease 2 rotate 15
##                pause .5
##                ease 2 rotate 20
##                pause .5
##                repeat
#            parallel:
#                ease 2 pos (30,90)
#                pause .5
#                ease 2 pos (30,80)
#                pause .5
#                repeat
        contains:
            subpixel True
            "Doreen_SC_Legs"
            anchor (560,580)#(560,420)
            offset (560,580) #(560,580)
            transform_anchor True
            zoom 1.5
            rotate 25
            pos (10,0) #X less is left, Y less is up
            parallel:
                pause .5
                ease 2 rotate 20
                pause .5
                ease 2 rotate 25
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
            "Doreen_Sex_Tits"
            anchor (560,580)#(560,420)
            offset (560,580) #(560,580)
            transform_anchor True
            zoom 1.4
            rotate 25
            pos (10,0) #X less is left, Y less is up
            parallel:
                pause .8
                ease 2 rotate 20
                pause .2
                ease 2 rotate 25
                repeat
        contains:
            subpixel True
            "Doreen_Sex_Calves"
            anchor (560,580)#(560,420)
            offset (560,580) #(560,580)
            transform_anchor True
            zoom 1.5
            rotate 25
            pos (0,0) #X less is left, Y less is up
            parallel:
                pause .5
                ease 2 rotate 20
                pause .5
                ease 2 rotate 25
                repeat
        #end animation for Doreen's lower body during Scissoring, Speed 0 (static) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Doreen_SC_Anim_1:
        #this is the animation for Doreen's lower body during Scissoring, Speed 1 (slow)
        contains:
            subpixel True
            "Doreen_SC_Body"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.4
            rotate 30
            pos (10,10) #X less is left, Y less is up (0,0)
            parallel:
                ease 1.5 rotate 25
                ease 1.5 rotate 30
                repeat
            parallel:
                ease 1 pos (0,20)
                pause .5
                ease 1 pos (10,10)
                pause .5
                repeat
        contains:
            subpixel True
            "Doreen_SC_Legs"
            anchor (560,580)#(560,420)
            offset (560,580) #(560,580)
            transform_anchor True
            zoom 1.5
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
            subpixel True
            "Doreen_Sex_Tits"
            anchor (560,580)#(560,420)
            offset (560,580) #(560,580)
            transform_anchor True
            zoom 1.4
            rotate 35
            pos (-20,0) #X less is left, Y less is up
            parallel:
                ease 1.5 rotate 30
                ease 1.5 rotate 35
                repeat
            parallel:
                ease 1 pos (-20,20)
                pause .8
                ease 1 pos (-20,0)
                pause .2
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
            "Doreen_Sex_Calves"
            anchor (560,580)#(560,420)
            offset (560,580) #(560,580)
            transform_anchor True
            zoom 1.5
            rotate 35
            pos (0,-10) #X less is left, Y less is up
            parallel:
#                pause .5
                ease 1.5 rotate 30
#                pause .5
                ease 1.5 rotate 35
                repeat
            parallel:
                ease 1.2 pos (0,20)
                pause .3
                ease 1.2 pos (0,-10)
                pause .3
                repeat
        #End animation for Doreen's lower body during Scissoring, Speed 1 (slow) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Doreen_SC_Anim_2:
        #this is the animation for Doreen's lower body during Scissoring, Speed 2 (fast)
        contains:
            subpixel True
            "Doreen_SC_Body"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.4
            rotate 35
            pos (0,0) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                pause .1
                ease .5 pos (-20,10)
                ease .5 pos (0,0)
                repeat
        contains:
            subpixel True
            "Doreen_SC_Legs"
            anchor (560,580)#(560,420)
            offset (560,580) #(560,580)
            transform_anchor True
            zoom 1.5
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
            subpixel True
            "Doreen_Sex_Tits"
            anchor (560,580)#(560,420)
            offset (560,580) #(560,580)
            transform_anchor True
            zoom 1.4
            rotate 35
            pos (-10,20) #X less is left, Y less is up
            parallel:
                ease .5 rotate 30
                pause .1
                ease .5 rotate 35
                repeat
            parallel:
                pause .1
                ease .5 pos (-10,50)
                ease .5 pos (-10,20)
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
            "Doreen_Sex_Calves"
            anchor (560,580)#(560,420)
            offset (560,580) #(560,580)
            transform_anchor True
            zoom 1.5
            rotate 35
            pos (0,-10) #X less is left, Y less is up
            parallel:
                ease .5 rotate 30
                pause .1
                ease .5 rotate 35
                repeat
            parallel:
                pause .1
                ease .5 pos (0,20)
                ease .5 pos (0,-10)
                repeat
        #End animation for Doreen's lower body during Scissoring, Speed 2 (fast) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     SC Launch/Reset
label Doreen_SC_Launch(Line = Trigger):
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    return
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary

    $ Trigger = Line

    if renpy.showing("Doreen_SC_Sprite"):
        return
    $ Speed = 0
    call Girl_Hide(DoreenX,1) #call Rogue_Hide
    show Doreen_SC_Sprite zorder 150
    with dissolve
    return

label Doreen_SC_Reset:
    if not renpy.showing("Doreen_SC_Sprite"):
        return
    $ DoreenX.ArmPose = 2
    hide Doreen_SC_Sprite
    call Girl_Hide(DoreenX) #call Rogue_Hide
#    call Set_The_Scene(Dress = 0)
    show Doreen_Sprite at SpriteLoc(DoreenX.SpriteLoc) zorder DoreenX.Layer:
        alpha 1 zoom 1 offset (0,0) anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return
# End Doreen Scissor Pose content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

## Animation components / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

## Doreen Misc Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#label Doreen_Kissing_Launch(T = Trigger,Set=1):
#    call Doreen_Hide
#    $ Trigger = T
#    $ DoreenX.Pose = "kiss" if Set else DoreenX.Pose
#    show Doreen_Sprite at SpriteLoc(DoreenX.SpriteLoc) zorder DoreenX.Layer
#    show Doreen_Sprite at SpriteLoc(StageCenter) zorder DoreenX.Layer:
#        ease 0.5 offset (100,0) zoom 2 alpha 1
#    return

#label Doreen_Kissing_Smooch:
#    $ DoreenX.FaceChange("kiss")
#    show Doreen_Sprite at SpriteLoc(StageCenter) zorder DoreenX.Layer:
#        ease 0.5 xpos StageCenter offset (100,0) zoom 2 alpha 1
#        pause 1
#        ease 0.5 xpos DoreenX.SpriteLoc zoom 1
#    show Doreen_Sprite at SpriteLoc(DoreenX.SpriteLoc) zorder DoreenX.Layer:
#        zoom 1
#    $ DoreenX.FaceChange("sexy")
#    return

#label Doreen_Breasts_Launch(T = Trigger,Set=1):
#    call Doreen_Hide
#    $ Trigger = T
#    $ DoreenX.Pose = "breasts" if Set else DoreenX.Pose
#    show Doreen_Sprite at SpriteLoc(DoreenX.SpriteLoc) zorder DoreenX.Layer:
##        ease 0.5 offset (-100,-200) zoom 2
#        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
#    return

#label Doreen_Middle_Launch(T = Trigger,Set=1):
#    call Doreen_Hide
#    $ Trigger = T
#    $ DoreenX.Pose = "mid" if Set else DoreenX.Pose
#    show Doreen_Sprite at SpriteLoc(DoreenX.SpriteLoc) zorder DoreenX.Layer:
##        ease 0.5 offset (-100,-200) zoom 2
#        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
#    return

#label Doreen_Pussy_Launch(T = Trigger,Set=1):
#    call Doreen_Hide
#    $ Trigger = T
#    $ DoreenX.Pose = "pussy" if Set else DoreenX.Pose
#    show Doreen_Sprite at SpriteLoc(DoreenX.SpriteLoc) zorder DoreenX.Layer:
#        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
#    return

#label Doreen_Pos_Reset(T = 0,Set=0):
#    if DoreenX.Loc != bg_current:
#            return
#    call Doreen_Hide
#    show Doreen_Sprite at SpriteLoc(DoreenX.SpriteLoc) zorder DoreenX.Layer:
#            ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
#    show Doreen_Sprite zorder DoreenX.Layer:
#            offset (0,0)
#            anchor (0.5, 0.0)
#            zoom 1
#            xzoom 1
#            yzoom 1
#            alpha 1
#            pos (DoreenX.SpriteLoc,50)
#    $ DoreenX.Pose = "full" if Set else 0
#    $ Trigger = T
#    return

#label Doreen_Hide(Sprite=0):
##        call Doreen_Sex_Reset
#        hide Doreen_SexSprite
#        hide Doreen_Doggy_Animation
#        hide Doreen_HJ_Animation
#        hide Doreen_BJ_Animation
#        hide Doreen_TJ_Animation
#        hide Doreen_Finger_Animation
#        hide Doreen_CUN_Animation
#        hide Doreen_69_Animation
#        hide Doreen_69_CUN
#        hide Doreen_Seated
#        if Sprite:
#                hide Doreen_Sprite
#        return



## Interface items //////////////////////////////////////////////////////////////////////////////

image GropeLeftBreast_Doreen:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65#.7
        pos (310,370)#(290,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 60
        block:
            ease 1 rotate 30
            ease 1 rotate 60
            repeat

image GropeRightBreast_Doreen:
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

image LickRightBreast_Doreen:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5
        xzoom -0.45
        pos (290,360)#(95,355)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (270,340)#(85,345)  top
            pause .5
            ease 1.5 rotate 30 pos (290,360)#(105,375) bottom
            repeat

image LickLeftBreast_Doreen:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5
        xzoom -0.45
        pos (170,360) #(195,360)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (165,340)#(190,380)
            pause .5
            ease 1.5 rotate 30 pos (170,360)#(200,410)
            repeat

image GropeThigh_Doreen:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (245,640)#(180,670)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        block:
            pause .5
            ease 1 rotate 110 pos (205,740) #(205,750) bottom
            ease 1 rotate 100 pos (245,640)   #215
            repeat

image GropePussy_Doreen:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (240,580)#(120,620) -20
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

image FingerPussy_Doreen:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.65
        pos (255,650)#(275,650)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (265,625)#(150,665)
                pause .5
                ease 1 rotate 50 pos (255,650)  #(140,700)
            choice:
                ease .5 rotate 40 pos (265,625)
                pause .5
                ease 1.75 rotate 50 pos (255,650)
            choice:
                ease 2 rotate 40 pos (265,625)
                pause .5
                ease 1 rotate 50 pos (255,650)
            choice:
                ease .25 rotate 40 pos (265,625)
                ease .25 rotate 50 pos (255,650)
                ease .25 rotate 40 pos (265,625)
                ease .25 rotate 50 pos (255,650)
            repeat

image Lickpussy_Doreen:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (265,610)#(155,650)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout .5 rotate -50 pos (255,590) #(210,605)
            linear .5 rotate -60 pos (245,600) #(200,615)
            easein 1 rotate 10 pos (265,610) #(230,625)
            repeat

image VibratorRightBreast_Doreen:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (160,355)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            pause .25
            ease 1 rotate 35 ypos 345
            pause .25
            ease 1 rotate 55 ypos 355
            repeat

image VibratorLeftBreast_Doreen:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (275,360) #(270,400)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 350
            pause .25
            ease 1 rotate 55 ypos 360
            pause .25
            repeat

image VibratorPussy_Doreen:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (265,615) #(240,665)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 70
        block:
            ease 1 rotate 35 pos (255,605)
            pause .25
            ease 1 rotate 70 pos (265,615)
            pause .25
            repeat

image VibratorAnal_Doreen:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (295,590)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 10
        block:
            ease 1 rotate 0 pos (285,580)
            pause .25
            ease 1 rotate 10 pos (295,590)
            pause .25
            repeat

image VibratorPussyInsert_Doreen:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (270,580)#(240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_Doreen:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (290,570)#(250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0



#Lesbian action animations.
image GirlGropeBothBreast_Doreen:
    contains:
        "GirlGropeLeftBreast_Doreen"
    contains:
        "GirlGropeRightBreast_Doreen"

image GirlGropeLeftBreast_Doreen:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (330,350) #(220,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate 10 ypos 360#(280,390)
            ease 1 rotate -10 ypos 350
            repeat

image GirlGropeRightBreast_Doreen:
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (170,360) #(90,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block:
            ease 1 rotate -40 ypos 370#(90,410)
            ease 1 rotate -10 ypos 360
            repeat

image GirlGropeThigh_Doreen:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (250,730)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        parallel:
            pause .5
            ease 1 ypos 740
            ease 1 ypos 650
            repeat
        parallel:
            pause .5
            ease .5 xpos 243
            ease .5 xpos 220
            ease .5 xpos 243
            ease .5 xpos 250
            repeat

image GirlGropePussy_DoreenSelf:
    contains:
        "GirlGropePussy_Doreen"
        anchor (0.5,0.5)
        rotate -40
#        yzoom -1
        pos (325,625)#(190,500)

image GirlGropePussy_Doreen:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (255,575)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 ypos 560
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

image GirlFingerPussy_Doreen:
    contains:
        subpixel True
        "UI_GirlFinger"
        zoom .6
        pos (255,580)#(220,640)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 ypos 585
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 ypos 585
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 ypos 585
                ease .75 rotate 200 ypos 590
                ease .5 rotate 205 ypos 585
                ease .75 rotate 200 ypos 590
            choice: #Fast stroke
                ease .3 rotate 205 ypos 585
                ease .3 rotate 200 ypos 595
                ease .3 rotate 205 ypos 585
                ease .3 rotate 200 ypos 595
            repeat



image DoreenMastHand:
        "images/UI_GirlHand_Jean.png"
        zoom 0.8
        rotate 240
        offset (385,270)

image DoreenFingerHand:
        "images/UI_GirlFinger_Jean.png"
        zoom 0.8
        rotate 220
        offset (360,330)
