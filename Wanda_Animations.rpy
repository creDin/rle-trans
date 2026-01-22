# Basic character Sprites

image Wanda_Sprite:
    LiveComposite(
        (600,1250),       #550,950
        (0,0), "images/WandaSprite/Wanda_Sprite_Shadow.png",
        (95,25), "Wanda_Sprite_HairBack", #(15,-80)
#        (0,0), ConditionSwitch(
#            #skirt back
#            "WandaX.Upskirt", Null(),
##            "WandaX.Legs == 'pants'", "images/WandaSprite/Wanda_Sprite_Legs_Pants_Back.png",
#            "WandaX.Legs == 'dress'", "images/WandaSprite/Wanda_Sprite_Legs_Skirt_Back.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #panties down back
#            "not WandaX.Panties or not WandaX.PantiesDown", Null(),
#            #if the panties are down
#            "WandaX.Legs and not WandaX.Upskirt and WandaX.Legs != 'dress'", Null(),
#            #if she's wearing a skirt or nothing else
#            "WandaX.Panties == 'lace panties' and WandaX.Legs == 'shorts'", "images/WandaSprite/Wanda_Sprite_Panties_Lace_BackS.png",
#            "WandaX.Panties == 'lace panties'", "images/WandaSprite/Wanda_Sprite_Panties_Lace_Back.png",
#            "WandaX.Panties == 'bikini bottoms'", "images/WandaSprite/Wanda_Sprite_Panties_Bikini_Back.png",
#            "True", "images/WandaSprite/Wanda_Sprite_Panties_Tan_Back.png",
#            ),

        (0,0), "images/WandaSprite/[WandaX.skin_image.skin_path]Wanda_Sprite_Arm.png",
            #back arm

        (0,0), ConditionSwitch(
            #Back Arm layer
            "WandaX.Over == 'purple top'", "images/WandaSprite/Wanda_Sprite_Over_Purple_Back.png",
            "WandaX.Chest == 'mesh top'", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Mesh_Arm.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #armlets
            "WandaX.Arms", "images/WandaSprite/Wanda_Sprite_Armlets1.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #jacket under
            "WandaX.Acc == 'jacket'", Recolor("Wanda", "Acc", "images/WandaSprite/Wanda_Sprite_Jacket_Back.png"),         # right hand up/left down
            "True", Null(),
            ),



        (0,0), ConditionSwitch(
            #body
#            "WandaX.ArmPose != 1", "images/WandaSprite/Wanda_Sprite_Body2.png",         # right hand up/left down
            "WandaX.Pubes", Recolor("Wanda", "Pubes", "images/WandaSprite/[WandaX.skin_image.skin_path]Wanda_Sprite_Body_Pubes.png"),         # right hand up/left down
            "True", "images/WandaSprite/[WandaX.skin_image.skin_path]Wanda_Sprite_Body.png", #if WandaX.Arms == 1   # right Hand on hip/left raised
            ),



        (0,0), ConditionSwitch(
            #stockings
            "WandaX.Hose == 'socks'", Recolor("Wanda", "Hose", "images/WandaSprite/Wanda_Sprite_Hose_Socks.png"),
            "WandaX.Hose == 'stockings'", Recolor("Wanda", "Hose", "images/WandaSprite/Wanda_Sprite_Hose_Stockings.png"),
            "WandaX.Hose == 'stockings and garterbelt'", Recolor("Wanda", "Hose", "images/WandaSprite/Wanda_Sprite_Hose_StockingsGarter.png"),
            "WandaX.Hose == 'garterbelt'", Recolor("Wanda", "Hose", "images/WandaSprite/Wanda_Sprite_Hose_Garter.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #panties
#            "not WandaX.Panties", Null(),
            "WandaX.PantiesDown", ConditionSwitch(
                    #if the panties are down
                    "not WandaX.Legs or WandaX.Upskirt or WandaX.Legs == 'dress' or WandaX.Legs == 'skirt'", ConditionSwitch(
                            #if she's wearing a skirt or nothing else
                            "WandaX.Panties == 'bikini bottoms'", Recolor("Wanda", "Panties", "images/WandaSprite/Wanda_Sprite_Panties_Bikini_Down.png"),
                            "WandaX.Panties == 'lace panties'", Recolor("Wanda", "Panties", "images/WandaSprite/Wanda_Sprite_Panties_Lace_Down.png"),
                            "WandaX.Panties", Recolor("Wanda", "Panties", "images/WandaSprite/Wanda_Sprite_Panties_Gray_Down.png"),
                            "True", Null(),
                            ),
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                #if she's not wet
                "WandaX.Panties == 'bikini bottoms'", Recolor("Wanda", "Panties", "images/WandaSprite/Wanda_Sprite_Panties_Bikini.png"),
                "WandaX.Panties == 'lace panties'", Recolor("Wanda", "Panties", "images/WandaSprite/Wanda_Sprite_Panties_Lace.png"),
                "WandaX.Panties and WandaX.Wet", Recolor("Wanda", "Panties", "images/WandaSprite/Wanda_Sprite_Panties_Gray_Wet.png"),
                "WandaX.Panties", Recolor("Wanda", "Panties", "images/WandaSprite/Wanda_Sprite_Panties_Gray.png"),
                "True", Null(),
                ),
            ),
        (0,0), ConditionSwitch(
            #pantyhose
            # Modification mode
            "WandaX.Hose == 'pantyhose2' and (not WandaX.PantiesDown or not WandaX.Panties)", Recolor("Wanda", "Hose", "images/WandaSprite/Wanda_Sprite_Hose_Pantyhose2.png"),
            "WandaX.Hose == 'pantyhose' and (not WandaX.PantiesDown or not WandaX.Panties)", Recolor("Wanda", "Hose", "images/WandaSprite/Wanda_Sprite_Hose_Pantyhose.png"),
#            "WandaX.Hose == 'tights' and WandaX.Wet and (not WandaX.PantiesDown or not WandaX.Panties)", "images/WandaSprite/Wanda_Sprite_Hose_Tights_Wet.png",
#            "WandaX.Hose == 'tights' and (not WandaX.PantiesDown or not WandaX.Panties)", "images/WandaSprite/Wanda_Sprite_Hose_Tights.png",
            "WandaX.Hose == 'ripped pantyhose' and (not WandaX.PantiesDown or not WandaX.Panties)", Recolor("Wanda", "Hose", "images/WandaSprite/Wanda_Sprite_Hose_Pantyhose_Holed.png"),
#            "WandaX.Hose == 'ripped tights' and (not WandaX.PantiesDown or not WandaX.Panties)", "images/WandaSprite/Wanda_Sprite_Hose_Tights_Holed.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Chest layer
            "WandaX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "WandaX.Chest == 'bikini top' and (WandaX.Acc == 'jacket' or WandaX.Over == 'purple top')", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Bikini_Up_Jacket.png"),
                    "WandaX.Chest == 'bikini top'", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Bikini_Up.png"),
                    "WandaX.Chest == 'mesh top'", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Mesh_Up.png"),
#                    "WandaX.Chest == 'lace bra'", "images/WandaSprite/Wanda_Sprite_Chest_Lace_Up.png",
                    "WandaX.Chest", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Bra_Up.png"),
                    "True", Null(),
                    ),
            "WandaX.Chest == 'bikini top' and (WandaX.Acc == 'jacket' or WandaX.Over == 'purple top')", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Bikini_Jacket.png"),
            "WandaX.Chest == 'bikini top'", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Bikini.png"),
            "WandaX.Chest == 'mesh top'", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Mesh.png"),
            "WandaX.Chest == 'lace bra'", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Lace.png"),
            "WandaX.Chest", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Bra.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Boots/Shoes
            "WandaX.Boots == 'boots'", "images/WandaSprite/Wanda_Sprite_Boots.png",
#            "WandaX.Boots == 'sneaks'", "images/WandaSprite/Wanda_Sprite_Boots_Sneaks.png",
            "True", Null(),
            ),

        (215,560), ConditionSwitch(    #275,560
            #Personal Wetness
            "not WandaX.Wet", Null(),
            "WandaX.Wet == 1 or (WandaX.Legs and WandaX.Legs != 'dress' and WandaX.Legs != 'skirt' and not WandaX.Upskirt)", ConditionSwitch( #Wet = 1 "Wet_Drip", #
                    "(WandaX.Legs == 'pants' or WandaX.Legs == 'shorts') and not WandaX.Upskirt", Null(),
                    "WandaX.Panties and not WandaX.PantiesDown", Null(),
#                    "(WandaX.Legs == 'pants' or WandaX.Legs == 'shorts')", AlphaMask("Wet_Drip","Wanda_Drip_MaskP"),
#                    "WandaX.Panties and WandaX.PantiesDown", AlphaMask("Wet_Drip","Wanda_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip","Wanda_Drip_Mask"), #only plays if nothing is in the way
                    ),
            "True", ConditionSwitch( #Wet = 2+  "Wet_Drip2", #
#                    "(WandaX.Legs == 'pants' or WandaX.Legs == 'shorts') and WandaX.Upskirt", AlphaMask("Wet_Drip2","Wanda_Drip_MaskP"),
#                    "WandaX.Panties and WandaX.PantiesDown", AlphaMask("Wet_Drip2","Wanda_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip2","Wanda_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (215,560), ConditionSwitch(    #275,560
            #Spunk
            "('in' not in WandaX.Spunk and 'anal' not in WandaX.Spunk) or not Player.Male", Null(),
            "WandaX.Panties and not WandaX.PantiesDown", "Spunk_Drip", #ConditionSwitch( #Wet = 1
            "WandaX.Legs and WandaX.Legs != 'dress' and WandaX.Legs != 'skirt' and not WandaX.Upskirt", ConditionSwitch( #Wet = 1 "Spunk_Drip", #
#                    "WandaX.Panties and WandaX.PantiesDown", AlphaMask("Spunk_Drip","Wanda_Drip_MaskP"),
#                    "(WandaX.Legs == 'pants' or WandaX.Legs == 'shorts') and WandaX.Upskirt", AlphaMask("Spunk_Drip","Wanda_Drip_MaskP"),
                    "True", AlphaMask("Spunk_Drip","Wanda_Drip_Mask"), #only plays if nothing is in the way
                    ),
            "True", ConditionSwitch( #Wet = 2+  "Spunk_Drip2", #
#                    "(WandaX.Legs == 'pants' or WandaX.Legs == 'shorts') and WandaX.Upskirt", AlphaMask("Spunk_Drip2","Wanda_Drip_MaskP"),
#                    "WandaX.Panties and WandaX.PantiesDown", AlphaMask("Spunk_Drip2","Wanda_Drip_MaskP"),
                    "True", AlphaMask("Spunk_Drip2","Wanda_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),

        (0,0), ConditionSwitch(
            #Water effect
##            "WandaX.Water and WandaX.ArmPose == 1", "images/WandaSprite/Wanda_Sprite_Water1.png",
            "WandaX.Water", "images/WandaSprite/Wanda_Sprite_Water.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Personal Wetness  over
            "not WandaX.Wet", Null(),
            "WandaX.Panties and not WandaX.PantiesDown", Null(),
            "WandaX.Legs and WandaX.Legs != 'dress' and WandaX.Legs != 'skirt' and not WandaX.Upskirt", Null(),
            "True", "images/WandaSprite/Wanda_Sprite_Wet_Pussy.png", #ConditionSwitch( #Wet = 2+
            ),
        (0,0), ConditionSwitch(
            #Spunk over
            "('in' not in WandaX.Spunk and 'anal' not in WandaX.Spunk) or not Player.Male", Null(),
            "WandaX.Legs and WandaX.Legs != 'dress' and WandaX.Legs != 'skirt' and not WandaX.Upskirt", Null(),
            "WandaX.Panties and not WandaX.PantiesDown", Null(),
            "True", "images/WandaSprite/Wanda_Sprite_Spunk_Pussy.png",
            ),

        (0,0), ConditionSwitch(
            #pants
            "not WandaX.Legs", Null(),
            "WandaX.Upskirt", ConditionSwitch(
                        #if the skirt's up or pants down
#                        "WandaX.Legs == 'shorts' and WandaX.Wet > 1", "images/WandaSprite/Wanda_Sprite_Legs_Shorts_Down_Wet.png",
                        "WandaX.Legs == 'skirt'", "images/WandaSprite/Wanda_Sprite_Legs_Skirt_Up.png",
                        "WandaX.Legs == 'shorts'", Recolor("Wanda", "Legs", "images/WandaSprite/Wanda_Sprite_Legs_Shorts_Down.png"),
#                        "WandaX.Legs == 'pants' and WandaX.Wet > 1", "images/WandaSprite/Wanda_Sprite_Legs_Pants_Down_Wet.png",
                        "WandaX.Legs == 'pants'", Recolor("Wanda", "Legs", "images/WandaSprite/Wanda_Sprite_Legs_Pants_Down.png"),
                        "True", Null(),
                        ),
            "WandaX.Legs == 'skirt'", "images/WandaSprite/Wanda_Sprite_Legs_Skirt.png",
            "WandaX.Legs == 'shorts' and WandaX.Wet > 1", Recolor("Wanda", "Legs", "images/WandaSprite/Wanda_Sprite_Legs_Shorts_Wet.png"),
            "WandaX.Legs == 'shorts'", Recolor("Wanda", "Legs", "images/WandaSprite/Wanda_Sprite_Legs_Shorts.png"),
            "WandaX.Legs == 'pants' and WandaX.Wet > 1", Recolor("Wanda", "Legs", "images/WandaSprite/Wanda_Sprite_Legs_Pants_Wet.png"),
            "WandaX.Legs == 'pants'", Recolor("Wanda", "Legs", "images/WandaSprite/Wanda_Sprite_Legs_Pants.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #dress
            "not WandaX.Legs", Null(),
            "WandaX.Upskirt", ConditionSwitch(
                        #if the skirt's up or pants down
                        "WandaX.Legs == 'dress' and WandaX.Uptop", Recolor("Wanda", "Legs", "images/WandaSprite/Wanda_Sprite_Legs_Dress_Up.png"),
                        "WandaX.Legs == 'dress'", Recolor("Wanda", "Legs", "images/WandaSprite/Wanda_Sprite_Legs_Dress_Upskirt.png"),
                        "True", Null(),
                        ),
            "WandaX.Legs == 'dress' and WandaX.Uptop", Recolor("Wanda", "Legs", "images/WandaSprite/Wanda_Sprite_Legs_Dress_Uptop.png"),
            "WandaX.Legs == 'dress'", Recolor("Wanda", "Legs", "images/WandaSprite/Wanda_Sprite_Legs_Dress.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #nude lower piercings
            "not WandaX.Pierce", Null(),
            "(WandaX.Legs == 'dress' or WandaX.Legs == 'skirt') and not WandaX.Upskirt", Null(),
            "WandaX.Pierce == 'ring'", ConditionSwitch(
                    # if top is up. . .
                    "WandaX.Legs == 'pants' and not WandaX.Upskirt", "images/WandaSprite/Wanda_Sprite_Pussy_Ring_Black.png",
                    "WandaX.Legs == 'shorts' and not WandaX.Upskirt", "images/WandaSprite/Wanda_Sprite_Pussy_Ring_Black.png",

                    "WandaX.Panties and WandaX.PantiesDown", "images/WandaSprite/Wanda_Sprite_Pussy_Ring.png",
                    # Modification mode
                    "WandaX.Hose == 'pantyhose2'", "images/WandaSprite/Wanda_Sprite_Pussy_Ring_Lace.png",
                    "WandaX.Hose == 'pantyhose'", "images/WandaSprite/Wanda_Sprite_Pussy_Ring_Lace.png",

                    "WandaX.Panties == 'bikini bottoms'", "images/WandaSprite/Wanda_Sprite_Pussy_Ring_Red.png",

                    "WandaX.Panties == 'lace panties'", "images/WandaSprite/Wanda_Sprite_Pussy_Ring_Lace.png",
                    "WandaX.Panties", "images/WandaSprite/Wanda_Sprite_Pussy_Ring_Gray.png",

                    "True", "images/WandaSprite/Wanda_Sprite_Pussy_Ring.png",
                    ),

            "WandaX.Legs == 'pants' and not WandaX.Upskirt", "images/WandaSprite/Wanda_Sprite_Pussy_Barbell_Black.png",
            "WandaX.Legs == 'shorts' and not WandaX.Upskirt", "images/WandaSprite/Wanda_Sprite_Pussy_Barbell_Black.png",

            "WandaX.Panties and WandaX.PantiesDown", "images/WandaSprite/Wanda_Sprite_Pussy_Barbell.png",
            # Modification mode
            "WandaX.Hose == 'pantyhose2'", "images/WandaSprite/Wanda_Sprite_Pussy_Barbell_Lace.png",
            "WandaX.Hose == 'pantyhose'", "images/WandaSprite/Wanda_Sprite_Pussy_Barbell_Lace.png",

            "WandaX.Panties == 'bikini bottoms'", "images/WandaSprite/Wanda_Sprite_Pussy_Barbell_Red.png",

            "WandaX.Panties == 'lace panties'", "images/WandaSprite/Wanda_Sprite_Pussy_Barbell_Lace.png",
            "WandaX.Panties", "images/WandaSprite/Wanda_Sprite_Pussy_Barbell_Gray.png",

            "True", "images/WandaSprite/Wanda_Sprite_Pussy_Barbell.png",
            ),

        (0,0), ConditionSwitch(
            #Over
            "WandaX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "WandaX.Over == 'corset'", Recolor("Wanda", "Over", "images/WandaSprite/Wanda_Sprite_Over_Corset_Up.png"),
                    "WandaX.Over == 'shirt'", Recolor("Wanda", "Over", "images/WandaSprite/Wanda_Sprite_Over_Shirt_Up.png"),
                    "WandaX.Over == 'purple top'", "images/WandaSprite/Wanda_Sprite_Over_Purple_Up.png",
                    "WandaX.Over == 'towel' and WandaX.Upskirt", Recolor("Wanda", "Over", "images/WandaSprite/Wanda_Sprite_Over_Towel_Up.png"),
                    "WandaX.Over == 'towel'", Recolor("Wanda", "Over", "images/WandaSprite/Wanda_Sprite_Over_Towel_Uptop.png"),
                    "True", Null(),
                    ),
            #If she's using arm pose 1, left arm pointing
            #If she's using arm pose 2, Left arm on hip
            # Modification mode
            "WandaX.Over == 'leotard'", Recolor("Wanda", "Over", "images/WandaSprite/Wanda_Sprite_Over_Leotard.png"),
            "WandaX.Over == 'corset'", Recolor("Wanda", "Over", "images/WandaSprite/Wanda_Sprite_Over_Corset.png"),
            "WandaX.Over == 'shirt'", Recolor("Wanda", "Over", "images/WandaSprite/Wanda_Sprite_Over_Shirt.png"),
            "WandaX.Over == 'purple top'", "images/WandaSprite/Wanda_Sprite_Over_Purple.png",
            "WandaX.Over == 'towel' and WandaX.Upskirt", Recolor("Wanda", "Over", "images/WandaSprite/Wanda_Sprite_Over_Towel_Upskirt.png"),
            "WandaX.Over == 'towel'", Recolor("Wanda", "Over", "images/WandaSprite/Wanda_Sprite_Over_Towel.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #armlets
            "WandaX.Arms", "images/WandaSprite/Wanda_Sprite_Armlets2.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #jacket over
            "WandaX.Acc == 'jacket'", Recolor("Wanda", "Acc", "images/WandaSprite/Wanda_Sprite_Jacket.png"),         # right hand up/left down
            "True", Null(),
            ),


        (0,0), ConditionSwitch(
            #Chest layer over jacket
            "not WandaX.Uptop", Null(),
            "WandaX.Over == 'shirt'", Recolor("Wanda", "Over", "images/WandaSprite/Wanda_Sprite_Over_Shirt_Over.png"),
            "WandaX.Chest == 'bikini top'", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Bikini_Over.png"),
            "WandaX.Chest == 'mesh top'", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Mesh_Over.png"),
            "WandaX.Chest == 'lace bra'", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Lace_Over.png"),
            "WandaX.Chest", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Bra_Over.png"),
            "True", Null(),
            ),


        (0,0), ConditionSwitch(
            #Nipples
            #Only does this if she has piercings, has no tops, or has her top up
            "WandaX.Pierce == 'ring'", ConditionSwitch(
                    "WandaX.Uptop", "images/WandaSprite/Wanda_Sprite_Nips_Ring.png",

                    "WandaX.Over == 'towel'", Null(),
                    "WandaX.Over == 'purple top'", "images/WandaSprite/Wanda_Sprite_Nips_Ring_Purp.png",
                    "WandaX.Over", "images/WandaSprite/Wanda_Sprite_Nips_Ring_Red.png", #== 'shirt' or 'corset'
                    "WandaX.Legs == 'dress'", "images/WandaSprite/Wanda_Sprite_Nips_Ring_Black.png",
#                    "WandaX.Over == 'shirt'", "images/WandaSprite/Wanda_Sprite_Nips_Ring_Red.png",

                    "WandaX.Chest == 'bikini top'", "images/WandaSprite/Wanda_Sprite_Nips_Ring_Red.png",
                    "WandaX.Chest == 'mesh top'", "images/WandaSprite/Wanda_Sprite_Nips_Ring_Mesh.png",
                    "WandaX.Chest == 'lace bra'", "images/WandaSprite/Wanda_Sprite_Nips_Ring_Lace.png",
                    "WandaX.Chest", "images/WandaSprite/Wanda_Sprite_Nips_Ring_Red.png",

                    "True", "images/WandaSprite/Wanda_Sprite_Nips_Ring.png",
                    ),
            "WandaX.Pierce == 'barbell'", ConditionSwitch(
                    "WandaX.Uptop", "images/WandaSprite/Wanda_Sprite_Nips_Barbell.png",

                    "WandaX.Over == 'towel'", Null(),
                    "WandaX.Over == 'purple top'", "images/WandaSprite/Wanda_Sprite_Nips_Barbell_Purp.png",
                    "WandaX.Over", "images/WandaSprite/Wanda_Sprite_Nips_Barbell_Red.png", #== 'shirt' or 'corset'
                    "WandaX.Legs == 'dress'", "images/WandaSprite/Wanda_Sprite_Nips_Barbell_Black.png",
#                    "WandaX.Over == 'shirt'", "images/WandaSprite/Wanda_Sprite_Nips_Barbell_Red.png",

                    "WandaX.Chest == 'bikini top'", "images/WandaSprite/Wanda_Sprite_Nips_Barbell_Red.png",
                    "WandaX.Chest == 'mesh top'", "images/WandaSprite/Wanda_Sprite_Nips_Barbell_Mesh.png",
                    "WandaX.Chest == 'lace bra'", "images/WandaSprite/Wanda_Sprite_Nips_Barbell_Lace.png",
                    "WandaX.Chest", "images/WandaSprite/Wanda_Sprite_Nips_Barbell_Red.png",

                    "True", "images/WandaSprite/Wanda_Sprite_Nips_Barbell.png",
                    ),
            # if no piercings. . .

            "WandaX.Lust < 50 and not WandaX.OCount", Null(),                                                 #nips only poke at high lust
            "WandaX.Uptop", "images/WandaSprite/Wanda_Sprite_Nips.png",

            "WandaX.Over == 'towel'", Null(),
            "WandaX.Over == 'purple top'", "images/WandaSprite/Wanda_Sprite_Nips_Purp.png",
            "WandaX.Over", "images/WandaSprite/Wanda_Sprite_Nips_Red.png",               #== 'shirt' or 'corset'
            "WandaX.Legs == 'dress'", "images/WandaSprite/Wanda_Sprite_Nips_Black.png",
#                    "WandaX.Over == 'shirt'", "images/WandaSprite/Wanda_Sprite_Nips_Red.png",

            "WandaX.Chest == 'bikini top'", "images/WandaSprite/Wanda_Sprite_Nips_Red.png",
            "WandaX.Chest == 'mesh top'", "images/WandaSprite/Wanda_Sprite_Nips_Mesh.png",
            "WandaX.Chest == 'lace bra'", "images/WandaSprite/Wanda_Sprite_Nips_Lace.png",
            "WandaX.Chest", "images/WandaSprite/Wanda_Sprite_Nips_Red.png",

            "True", "images/WandaSprite/Wanda_Sprite_Nips.png",

            ),

        (0,0), ConditionSwitch(
            #belly spunk
            "'belly' in WandaX.Spunk and Player.Male", "images/WandaSprite/Wanda_Sprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast spunk
            "'tits' in WandaX.Spunk and Player.Male", "images/WandaSprite/Wanda_Sprite_Spunk_Tits.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Necklaces
            "WandaX.Neck == 'scarf'", "images/WandaSprite/Wanda_Sprite_Neck_Scarf.png",
            "WandaX.Neck", "images/WandaSprite/Wanda_Sprite_Neck.png",
            "True", Null(),
            ),
#        (0,0), "images/WandaSprite/Wanda_Sprite_Headref.png", #53,-45
        (95,25), "Wanda_Sprite_Head", #(95,20)




#        (0,0), ConditionSwitch(
#            #hand spunk
#            "WandaX.ArmPose == 2 or 'hand' not in WandaX.Spunk", Null(),
#            "True", "images/WandaSprite/Wanda_Sprite_Spunk_Hand.png",
#            ),
#        (0,0), ConditionSwitch(                                                                         #Props
#            "not WandaX.Held or WandaX.ArmPose != 2", Null(),
#            "WandaX.ArmPose == 2 and WandaX.Held == 'phone'", "images/WandaSprite/Wanda_held_phone.png",
#            "WandaX.ArmPose == 2 and WandaX.Held == 'dildo'", "images/WandaSprite/Wanda_held_dildo.png",
#            "WandaX.ArmPose == 2 and WandaX.Held == 'vibrator'", "images/WandaSprite/Wanda_held_vibrator.png",
#            "WandaX.ArmPose == 2 and WandaX.Held == 'panties'", "images/WandaSprite/Wanda_held_panties.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #UI tool for When Rogue is masturbating using RogueX.Offhand actions while lead
            "Trigger == 'lesbian' or not WandaX.Offhand",Null(),# or Ch_Focus is not WandaX", Null(),
            "WandaX.Offhand == 'fondle pussy' and Trigger != 'sex' and WandaX.Lust >= 70", "GirlFingerPussy_Wanda",
            "WandaX.Offhand == 'fondle pussy'", "GirlGropePussy_Wanda",
            "WandaX.Offhand == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeLeftBreast_Wanda",    #When zero is working the right breast, fondle left
            "WandaX.Offhand == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeRightBreast_Wanda", #When zero is working the left breast, fondle right
            "WandaX.Offhand == 'fondle breasts'", "GirlGropeRightBreast_Wanda",
            "WandaX.Offhand == 'vibrator breasts'", "VibratorRightBreast_Wanda",
            "WandaX.Offhand == 'vibrator pussy'", "VibratorPussy_Wanda",
            "WandaX.Offhand == 'vibrator pussy insert'", "VibratorPussy_Wanda",
            "WandaX.Offhand == 'vibrator anal'", "VibratorAnal_Wanda",
            "WandaX.Offhand == 'vibrator anal insert'", "VibratorPussy_Wanda",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #UI tool for RogueX.Offhand(lesbian) actions (ie Kitty's hand on her when Rogue is secondary)
            "not Partner or Partner is WandaX or WandaX in Nearby", Null(),
            "Partner.Offhand == 'fondle girl pussy' and Trigger != 'sex' and WandaX.Lust >= 70", "GirlFingerPussy_Wanda",
            "Partner.Offhand == 'fondle girl pussy'", "GirlGropePussy_Wanda",
            "Partner.Offhand == 'lick girl pussy'", "Lickpussy_Wanda",
            "Partner.Offhand == 'suck girl breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Wanda",
            "Partner.Offhand == 'suck girl breasts'", "LickRightBreast",
            "Partner.Offhand == 'fondle girl breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Wanda",    #When zero is working the right breast, fondle left
            "Partner.Offhand == 'fondle girl breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Wanda", #When zero is working the left breast, fondle right
            "Partner.Offhand == 'fondle girl breasts'", "GirlGropeRightBreast_Wanda",
            "Partner.Offhand == 'vibrator girl breasts'", "VibratorRightBreast_Wanda",
            "Partner.Offhand == 'vibrator girl pussy'", "VibratorPussy_Wanda",
            "Partner.Offhand == 'vibrator girl pussy insert'", "VibratorPussy_Wanda",
            "Partner.Offhand == 'vibrator girl anal'", "VibratorAnal_Wanda",
            "Partner.Offhand == 'vibrator girl anal insert'", "VibratorPussy_Wanda",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for when RogueX is the partner in the scene, and the lead is working on her
            "not Partner or Partner is not WandaX", Null(),
            "Ch_Focus.Offhand == 'fondle girl pussy' and Trigger != 'sex' and WandaX.Lust >= 70", "GirlFingerPussy_Wanda",
            "Ch_Focus.Offhand == 'fondle girl pussy'", "GirlGropePussy_Wanda",
            "Ch_Focus.Offhand == 'lick girl pussy'", "Lickpussy_Wanda",
            "Ch_Focus.Offhand == 'suck girl breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Wanda",
            "Ch_Focus.Offhand == 'suck girl breasts'", "LickRightBreast",
            "Ch_Focus.Offhand == 'fondle girl breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Wanda",    #When zero is working the right breast, fondle left
            "Ch_Focus.Offhand == 'fondle girl breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Wanda", #When zero is working the left breast, fondle right
            "Ch_Focus.Offhand == 'fondle girl breasts'", "GirlGropeRightBreast_Wanda",
            "Ch_Focus.Offhand == 'vibrator girl breasts'", "VibratorRightBreast_Wanda",
            "Ch_Focus.Offhand == 'vibrator girl pussy'", "VibratorPussy_Wanda",
            "Ch_Focus.Offhand == 'vibrator girl pussy insert'", "VibratorPussy_Wanda",
            "Ch_Focus.Offhand == 'vibrator girl anal'", "VibratorAnal_Wanda",
            "Ch_Focus.Offhand == 'vibrator girl anal insert'", "VibratorPussy_Wanda",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger1(primary) actions
            "not Trigger or Ch_Focus is not WandaX", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast_Wanda",
            "Trigger == 'fondle thighs'", "GropeThigh_Wanda",
            "Trigger == 'fondle breasts'", "GropeLeftBreast_Wanda",
            "Trigger == 'suck breasts'", "LickRightBreast_Wanda",
            "Trigger == 'vibrator pussy'", "VibratorPussy_Wanda",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy_Wanda",
            "Trigger == 'vibrator anal'", "VibratorAnal_Wanda",
            "Trigger == 'vibrator anal insert'", "VibratorPussy_Wanda",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_Wanda",
            "Trigger == 'fondle pussy'", "GropePussy_Wanda",
            "Trigger == 'lick pussy'", "Lickpussy_Wanda",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus is not WandaX", Null(),
#            "Trigger == 'fondle breasts' and not WandaX.Offhand", "GropeRightBreast_Wanda",  #"Trigger == 'fondle breasts' and not RogueX.Offhand",
            #When doing nothing offhand, use both hands on breasts.
            "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast_Wanda",
            #When sucking right breast, fondle left
            "Trigger2 == 'fondle breasts'", "GropeLeftBreast_Wanda",
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast_Wanda",
            #When sucking right breast, vibrator left
            "Trigger2 == Trigger", Null(),
            #When both triggers are the same, do nothing
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast_Wanda",
            "Trigger2 == 'suck breasts'", "LickLeftBreast_Wanda",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy_Wanda",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy_Wanda",
            "Trigger2 == 'vibrator anal'", "VibratorAnal_Wanda",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy_Wanda",
            "Trigger2 == 'fondle pussy'", "GropePussy_Wanda",
            "Trigger2 == 'lick pussy'", "Lickpussy_Wanda",
            "Trigger2 == 'fondle thighs'", "GropeThigh_Wanda",
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #UI tool for When Wanda is masturbating using Trigger3 actions
#            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != WandaX", Null(),

#            #this is not a lesbian thing, and a trigger is set, and Wanda is the primary. . .
#            "Trigger3 == 'fondle pussy'", "GirlGropePussy_WandaSelf",
#            "Trigger3 == 'fondle breasts'", ConditionSwitch(
#                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeLeftBreast_Wanda",
#                        #When zero is working the right breast, fondle left
#                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeRightBreast_Wanda",
#                        #When zero is working the left breast, fondle right
#                    "True", "GirlGropeBothBreast_Wanda",
#                        #else, fondle both
#                    ),
#            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast_Wanda",
#            "Trigger3 == 'vibrator pussy'", "VibratorPussy_Wanda",
#            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy_Wanda",
#            "Trigger3 == 'vibrator anal'", "VibratorAnal_Wanda",
#            "Trigger3 == 'vibrator anal insert'", "VibratorPussy_Wanda",
#            "True", Null(),
#            ),

#        (0,0), ConditionSwitch(
#            #UI tool for Trigger3(lesbian) actions (ie Rogue's hand on her when Wanda is secondary)
#            "Trigger != 'lesbian' or Ch_Focus == WandaX or not Trigger3", Null(),

#            # If there is a Trigger3 and Wanda is not the focus
#            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and WandaX.Lust >= 70", "GirlFingerPussy_Wanda",
#            "Trigger3 == 'fondle pussy'", "GirlGropePussy_Wanda",
#            "Trigger3 == 'lick pussy'", "Lickpussy_Wanda",
#            "Trigger3 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Wanda",
#            "Trigger3 == 'suck breasts'", "LickRightBreast_Wanda",
#            "Trigger3 == 'fondle breasts'", ConditionSwitch(
#                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeLeftBreast_Wanda",
#                        #When zero is working the right breast, fondle left
#                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeRightBreast_Wanda",
#                        #When zero is working the left breast, fondle right
#                    "Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts'", "GirlGropeLeftBreast_Wanda",
#                        #When zero is working the right breast, fondle left
#                    "True", "GirlGropeRightBreast_Wanda",
#                        #else, fondle right
#                    ),
#            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast",
#            "Trigger3 == 'vibrator pussy'", "VibratorPussy",
#            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy",
#            "Trigger3 == 'vibrator anal'", "VibratorAnal",
#            "Trigger3 == 'vibrator anal insert'", "VibratorPussy",
#            "True", Null(),
#            ),
        )
    anchor (0.5, 0.0)
    offset (60,0)
    zoom .80  #.75


image Wanda_Sprite_HairBack:
    LiveComposite(
        (820,820),
        (0,0), ConditionSwitch(
                #hair back
    #            "renpy.showing('Wanda_BJ_Animation')", Null(),
    #            "renpy.showing('Wanda_SexSprite')", "images/WandaSex/Wanda_Sprite_Hair_Long_UnderSex.png",
                "WandaX.Hair == 'wetlong' or (WandaX.Hair == 'long' and WandaX.Water)", Recolor("Wanda", "Hair", "images/WandaSprite/Wanda_Sprite_Hair_Long_Wet_Back.png"),
                "WandaX.Hair == 'long' and (not Player.Male and 'facial' in WandaX.Spunk)",Recolor("Wanda", "Hair", "images/WandaSprite/Wanda_Sprite_Hair_Long_Wet_Back.png"),
#                "WandaX.Hair == 'wet' or WandaX.Water", "images/WandaSprite/Wanda_Sprite_Hair_Short_Wet_Back.png",
#                "not Player.Male and 'facial' in WandaX.Spunk","images/WandaSprite/Wanda_Sprite_Hair_Short_Wet_Back.png",
                "WandaX.Hair == 'long'", Recolor("Wanda", "Hair", "images/WandaSprite/Wanda_Sprite_Hair_Long_Back.png"),
                "True", Null(), #"images/WandaSprite/Wanda_Sprite_Hair_Short_Back.png",
                ),
        )
    anchor (0.5, 0.5)
    zoom .40#.47
    transform_anchor True
#    rotate -10


image Wanda_Sprite_Head:
    LiveComposite(
        (820,820),
        (0,0), ConditionSwitch(
                # Face background plate
#                "renpy.showing('Wanda_SexSprite') and WandaX.Blush >= 2", "images/WandaSprite/Wanda_Sprite_Head_Sex_Blush2.png",
#                "renpy.showing('Wanda_SexSprite') and WandaX.Blush", "images/WandaSprite/Wanda_Sprite_Head_Sex_Blush1.png",
#                "renpy.showing('Wanda_SexSprite')", "images/WandaSprite/Wanda_Sprite_Head_Sex.png",
                "WandaX.Blush >= 2", "images/WandaSprite/[WandaX.skin_image.skin_path]Wanda_Sprite_Head_Blush2.png",
                "WandaX.Blush", "images/WandaSprite/[WandaX.skin_image.skin_path]Wanda_Sprite_Head_Blush1.png",
                "True", "images/WandaSprite/[WandaX.skin_image.skin_path]Wanda_Sprite_Head.png",
                ),
        (0,0), ConditionSwitch(
            #chin spunk
            "'chin' in WandaX.Spunk and Player.Male", "images/WandaSprite/Wanda_Sprite_Spunk_Chin.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Mouths
            "WandaX.Mouth == 'lipbite'", "images/WandaSprite/Wanda_Sprite_Mouth_Lipbite.png",
            "WandaX.Mouth == 'sucking'", "images/WandaSprite/Wanda_Sprite_Mouth_Open.png",
            "WandaX.Mouth == 'kiss'", "images/WandaSprite/Wanda_Sprite_Mouth_Kiss.png",
            "WandaX.Mouth == 'sad'", "images/WandaSprite/Wanda_Sprite_Mouth_Sad.png",
            "WandaX.Mouth == 'smile'", "images/WandaSprite/Wanda_Sprite_Mouth_Open.png",
            "WandaX.Mouth == 'surprised'", "images/WandaSprite/Wanda_Sprite_Mouth_Open.png",
#            "not Player.Male and 'mouth' in WandaX.Spunk and WandaX.Mouth == 'tongue'", "images/WandaSprite/Wanda_Sprite_Mouth_Tongue_Wet.png",
            "WandaX.Mouth == 'tongue'", "images/WandaSprite/Wanda_Sprite_Mouth_Tongue.png",
            "WandaX.Mouth == 'grimace'", "images/WandaSprite/Wanda_Sprite_Mouth_Open.png",
            "WandaX.Mouth == 'smirk'", "images/WandaSprite/Wanda_Sprite_Mouth_Smirk.png",
            "WandaX.Mouth == 'open'", "images/WandaSprite/Wanda_Sprite_Mouth_Open.png",
            "True", "images/WandaSprite/Wanda_Sprite_Mouth_Smirk.png",
            ),
        (0,0), ConditionSwitch(
            #Mouths spunk
            "'mouth' not in WandaX.Spunk or not Player.Male", Null(),
            "WandaX.Mouth == 'sucking'", "images/WandaSprite/Wanda_Sprite_Spunk_Tongue.png",
#            "WandaX.Mouth == 'kiss'", "images/WandaSprite/Wanda_Sprite_Spunk_Kiss.png",
#            "WandaX.Mouth == 'sad'", "images/WandaSprite/Wanda_Sprite_Spunk_Sad.png",
#            "WandaX.Mouth == 'smirk'", "images/WandaSprite/Wanda_Sprite_Spunk_Sad.png",
#            "WandaX.Mouth == 'lipbite'", "images/WandaSprite/Wanda_Sprite_Spunk_Sad.png",
            "WandaX.Mouth == 'surprised'", "images/WandaSprite/Wanda_Sprite_Spunk_Tongue.png",
#            "WandaX.Mouth == 'open'", "images/WandaSprite/Wanda_Sprite_Spunk_Open.png",
            "WandaX.Mouth == 'tongue'", "images/WandaSprite/Wanda_Sprite_Spunk_Tongue.png",
            "True", "images/WandaSprite/Wanda_Sprite_Spunk_Smirk.png",
            ),
        (0,0), ConditionSwitch(
            #wet face
            "Player.Male", Null(),
            "'mouth' not in WandaX.Spunk and 'chin' not in WandaX.Spunk", Null(),
            "WandaX.Mouth == 'tongue'", "images/WandaSprite/Wanda_Sprite_Wet_MouthTongue.png",
            "'chin' in WandaX.Spunk", "images/WandaSprite/Wanda_Sprite_Wet_Mouth.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(     #    (0,5)
            #brows
            "WandaX.Brows == 'angry'", "images/WandaSprite/[WandaX.skin_image.skin_path]Wanda_Sprite_Brows_Angry.png",
            "WandaX.Brows == 'sad'", "images/WandaSprite/[WandaX.skin_image.skin_path]Wanda_Sprite_Brows_Sad.png",
            "WandaX.Brows == 'surprised'", "images/WandaSprite/[WandaX.skin_image.skin_path]Wanda_Sprite_Brows_Surprised.png",
            "WandaX.Brows == 'confused'", "images/WandaSprite/[WandaX.skin_image.skin_path]Wanda_Sprite_Brows_Confused.png",
            "True", "images/WandaSprite/[WandaX.skin_image.skin_path]Wanda_Sprite_Brows_Normal.png",
            ),
        # (0,0), "Wanda Blink",     #Eyes  (0,5)
        # Modification mode
        (0,0), ConditionSwitch(
            #eyes psychic
            "WandaX.Eyes == 'psychic'", "images/WandaSprite/Wanda_Sprite_Eyes_Psychic.png",
            "True", "Wanda Blink",
            ),
        # -----------------
        (0,0), ConditionSwitch(
                #hair over
    #            "renpy.showing('Wanda_BJ_Animation')", Null(),
    #            "renpy.showing('Wanda_SexSprite')", "images/WandaSex/Wanda_Sprite_Hair_Long_UnderSex.png",

                "WandaX.Hair == 'wetlong' or (WandaX.Hair == 'long' and WandaX.Water)", Recolor("Wanda", "Hair", "images/WandaSprite/Wanda_Sprite_Hair_Long_Wet.png"),
                "WandaX.Hair == 'long' and (not Player.Male and 'facial' in WandaX.Spunk)",Recolor("Wanda", "Hair", "images/WandaSprite/Wanda_Sprite_Hair_Long_Wet.png"),
                "WandaX.Hair == 'wet' or WandaX.Water", Recolor("Wanda", "Hair", "images/WandaSprite/Wanda_Sprite_Hair_Short_Wet.png"),
                "not Player.Male and 'facial' in WandaX.Spunk",Recolor("Wanda", "Hair", "images/WandaSprite/Wanda_Sprite_Hair_Short_Wet.png"),
                "WandaX.Hair == 'long'", Recolor("Wanda", "Hair", "images/WandaSprite/Wanda_Sprite_Hair_Long.png"),
                "True", Recolor("Wanda", "Hair", "images/WandaSprite/Wanda_Sprite_Hair_Short.png"),
                ),
        (0,0), ConditionSwitch(
                #hairband
                "not WandaX.Hat",Null(),
                "True", "images/WandaSprite/Wanda_Sprite_Headband.png",
                ),

#        (0,0), "images/WandaSprite/Wanda_Sprite_Earring.png",     #Eyes  (0,5)
        (0,0), ConditionSwitch(
            #Hair Water
            "WandaX.Water", "images/WandaSprite/Wanda_Sprite_Water_Face.png",
            "not Player.Male and 'facial' in WandaX.Spunk", "images/WandaSprite/Wanda_Sprite_Water_Face.png",
            "True",Null(),
            ),
        (0,0), ConditionSwitch(
            #facial spunk
            "'hair' in WandaX.Spunk and Player.Male", "images/WandaSprite/Wanda_Sprite_Spunk_Hair.png",
            "'facial' in WandaX.Spunk and Player.Male", "images/WandaSprite/Wanda_Sprite_Spunk_Facial.png",
            "True", Null(),
            ),
        )
    anchor (0.5, 0.5)
    zoom .4#.5
    transform_anchor True
#    rotate -10
#    alpha 0.9

image Wanda Blink:
    ConditionSwitch(
    "WandaX.Eyes == 'closed'", "images/WandaSprite/Wanda_Sprite_Eyes_Closed.png",
    "WandaX.Eyes == 'sexy'", "images/WandaSprite/Wanda_Sprite_Eyes_Sexy.png",
    "WandaX.Eyes == 'side'", "images/WandaSprite/Wanda_Sprite_Eyes_Side.png",
    "WandaX.Eyes == 'surprised'", "images/WandaSprite/Wanda_Sprite_Eyes_Surprised.png",
    "WandaX.Eyes == 'normal'", "images/WandaSprite/Wanda_Sprite_Eyes_Normal.png",
    "WandaX.Eyes == 'stunned'", "images/WandaSprite/Wanda_Sprite_Eyes_Stunned.png",
    "WandaX.Eyes == 'down'", "images/WandaSprite/Wanda_Sprite_Eyes_Down.png",
    "WandaX.Eyes == 'leftside'", "images/WandaSprite/Wanda_Sprite_Eyes_Leftside.png",
    "WandaX.Eyes == 'manic'", "images/WandaSprite/Wanda_Sprite_Eyes_Sexy.png",#"images/WandaSprite/Wanda_Sprite_Eyes_Squint.png",
    "WandaX.Eyes == 'squint'", "images/WandaSprite/Wanda_Sprite_Eyes_Sexy.png",#"Wanda_Squint",
    "WandaX.Eyes == 'psychic'", "images/WandaSprite/Wanda_Sprite_Eyes_Psychic.png",
    "True", "images/WandaSprite/Wanda_Sprite_Eyes_Normal.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/WandaSprite/Wanda_Sprite_Eyes_Closed.png"
    .25
    repeat

##image Wanda_Squint:
##    "images/WandaSprite/Wanda_Sprite_Eyes_Sexy.png"
##    choice:
##        3.5
##    choice:
##        3.25
##    choice:
##        3
##    "images/WandaSprite/Wanda_Sprite_Eyes_Squint.png"
##    .25
##    repeat


image Wanda_Drip_Mask:
    #This is the mask for her drip pattern
    contains:
        "images/WandaSprite/Wanda_Sprite_WetMask.png"
        offset (-215,-560)#(-145,-15)#(-212,-4834)

##image Wanda_Drip_MaskPanties:
##    #This is the mask for her drip pattern in panties down mode
##    contains:
##        "images/WandaSprite/Wanda_Sprite_DripMaskPanties.png"
##        offset (-145,-560)#(-225,-560)

##image Wanda_Drip_MaskP:
##    #This is the mask for her drip pattern in panties down mode
##    contains:
##        "images/WandaSprite/Wanda_Sprite_WetMask_Pants.png"
##        offset (-275,-560)#(-145,-560)

## End Wanda Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Wanda Doggy Compositing ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#image Wanda_Doggy_Base = LiveComposite(
image Wanda_Doggy_Animation: #nee Wanda_Doggy
    LiveComposite(
        #Base body
        (420,750),
        (0,0), ConditionSwitch(
            #Shows different upper body motion depending on events
            "not Player.Sprite", "Wanda_Doggy_Body",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Wanda_Doggy_Fuck2_Top",
                    "Speed > 1", "Wanda_Doggy_Fuck_Top",
                    "Speed", "Wanda_Doggy_Anal_Head_Top",
                    "True", "Wanda_Doggy_Body",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Wanda_Doggy_Fuck2_Top",
                    "Speed > 1", "Wanda_Doggy_Fuck_Top",
                    "True", "Wanda_Doggy_Body",
                    ),
            "Player.Cock == 'foot'", ConditionSwitch(
                    "Speed > 1", "Wanda_Doggy_Foot2_Top",
                    "Speed", "Wanda_Doggy_Foot1_Top",
                    "True", "Wanda_Doggy_Foot0_Top",
                    ),
            "True", "Wanda_Doggy_Body",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events
            "not Player.Sprite", "Wanda_Doggy_Ass",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Wanda_Doggy_Fuck2_Ass",
                    "Speed > 1", "Wanda_Doggy_Fuck_Ass",
                    "Speed", "Wanda_Doggy_Anal_Head_Ass",
                    "True", "Wanda_Doggy_Ass",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Wanda_Doggy_Fuck2_Ass",
                    "Speed > 1", "Wanda_Doggy_Fuck_Ass",
                    "True", "Wanda_Doggy_Ass",
                    ),
            "Player.Cock == 'foot'", ConditionSwitch(
                    "Speed > 1", "Wanda_Doggy_Foot2_Ass",
                    "Speed", "Wanda_Doggy_Foot1_Ass",
                    "True", "Wanda_Doggy_Foot0_Ass",
                    ),
            "True", "Wanda_Doggy_Ass",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
#            "not Player.Sprite", "Wanda_Doggy_Shins0",
            "Player.Sprite and Player.Cock == 'foot'", ConditionSwitch(
                    "Speed > 1", "Wanda_Doggy_Feet2",
                    "Speed", "Wanda_Doggy_Feet1",
                    "True", "Wanda_Doggy_Feet0",
                    ),
            "ShowFeet", "Wanda_Doggy_Shins0",# "not Player.Sprite and ShowFeet", "Wanda_Doggy_Shins",
            "True", Null(),
            ),
        )
    align (0.6,0.0)
    #yoffset 50
# End Base / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Wanda_Doggy_Body:
    LiveComposite(
        #Upper body
        (610,750),
        #(165,0),"Wanda_Doggy_Hair_Under", #back of the hair
#        (0,60), "Wanda_Doggy_Head",               #Head

#        (0,0), "images/WandaDoggy/Wanda_Doggy_HeadRef.png",               #Head
        (0,0), ConditionSwitch(
            #head
            "WandaX.Facing", "Wanda_Doggy_Head_Fore",
            "True", "Wanda_Doggy_Head",
            ),

        (0,0), "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Body.png", #Body base
        (0,0), ConditionSwitch(
            #bra
#            "WandaX.Uptop", ConditionSwitch(
#                    "WandaX.Chest == 'lace bra'", "images/WandaDoggy/Wanda_Doggy_Chest_Lace_Up.png",
#                    "WandaX.Chest == 'sports bra'", "images/WandaDoggy/Wanda_Doggy_Chest_Sport_Up.png",
#                    "WandaX.Chest == 'bikini top'", "images/WandaDoggy/Wanda_Doggy_Chest_Bikini_Up.png",
#                    "True", "images/WandaDoggy/Wanda_Doggy_Chest_Bra_Up.png",
#                    ),
            "WandaX.Chest == 'lace bra'", Recolor("Wanda", "Chest", "images/WandaDoggy/Wanda_Doggy_Chest_Lace.png"),
            "WandaX.Chest == 'mesh top'", Recolor("Wanda", "Chest", "images/WandaDoggy/Wanda_Doggy_Chest_Mesh.png"),
            "WandaX.Chest == 'bikini top'", Recolor("Wanda", "Chest", "images/WandaDoggy/Wanda_Doggy_Chest_Bikini.png"),
            "WandaX.Chest", Recolor("Wanda", "Chest", "images/WandaDoggy/Wanda_Doggy_Chest_Bra.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "WandaX.Water", "images/WandaDoggy/Wanda_Doggy_Water_Body.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Dress
            "WandaX.Legs == 'dress' and WandaX.Uptop", Recolor("Wanda", "Over", "images/WandaDoggy/Wanda_Doggy_Over_Towel.png"),
            "WandaX.Legs == 'dress'", Recolor("Wanda", "Legs", "images/WandaDoggy/Wanda_Doggy_Over_Dress.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Overshirt
            "WandaX.Over == 'purple top'", "images/WandaDoggy/Wanda_Doggy_Over_Purple.png",
            "WandaX.Over == 'corset'", Recolor("Wanda", "Over", "images/WandaDoggy/Wanda_Doggy_Over_Corset.png"),
            "WandaX.Over == 'shirt'", Recolor("Wanda", "Over", "images/WandaDoggy/Wanda_Doggy_Over_Shirt.png"),
            "WandaX.Over == 'towel'", Recolor("Wanda", "Over", "images/WandaDoggy/Wanda_Doggy_Over_Towel.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #armlets
            "WandaX.Arms", "images/WandaDoggy/Wanda_Doggy_Armlets.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #jacket
            "WandaX.Acc == 'jacket'", Recolor("Wanda", "Acc", "images/WandaDoggy/Wanda_Doggy_Over_Jacket.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #long Hair
            "WandaX.Hair != 'long' and WandaX.Hair != 'wetlong'", Null(),
#            "WandaX.Facing", ConditionSwitch(
#                    "WandaX.Water or WandaX.Hair == 'wetlong'", Recolor("Wanda", "Hair", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Hair_Long_Wet_Fore.png"),
#                    "not Player.Male and 'facial' in WandaX.Spunk",Recolor("Wanda", "Hair", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Hair_Long_Wet_Fore.png"),
#                    "True", Recolor("Wanda", "Hair", "images/WandaDoggy/Wanda_Doggy_Hair_Long_Fore.png"),
#                    ),
            "WandaX.Water or WandaX.Hair == 'wetlong'", Recolor("Wanda", "Hair", "images/WandaDoggy/Wanda_Doggy_Hair_Long_Wet_Over.png"),
            "not Player.Male and 'facial' in WandaX.Spunk",Recolor("Wanda", "Hair", "images/WandaDoggy/Wanda_Doggy_Hair_Long_Wet_Over.png"),
            "True", Recolor("Wanda", "Hair", "images/WandaDoggy/Wanda_Doggy_Hair_Long_Over.png"),
            ),
        (0,0), ConditionSwitch(             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #spunk back Layer
            "'back' in WandaX.Spunk and Player.Male", "images/WandaDoggy/Wanda_Doggy_Spunk_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast fondling animation
            "Trigger == 'fondle breasts' or Trigger2 == 'fondle breasts'", "Wanda_Doggy_GropeBreast",
            "True", Null()
            ),
        #(161,-1), "Wanda_Doggy_Head",               #Head
        #(165,0),"Wanda_Doggy_Hair_Over", #front of the hair
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


image Wanda_Doggy_Head:
    LiveComposite(
        #Head
        (420,420),
        #(0,0), "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Head.png", #Body base
        #(0,0), "images/WandaDoggy/Wanda_Doggy_TestArm.png",#Eyes
#        (0,0), ConditionSwitch(
#            #Hair back
#            "WandaX.Water or WandaX.Hair == 'wet'", "images/WandaDoggy/Wanda_Doggy_Hair_Wet_Back.png",
#            "not Player.Male and 'facial' in WandaX.Spunk","images/WandaDoggy/Wanda_Doggy_Hair_Wet_Back.png",
#            "WandaX.Hair == 'pony'", Null(),
#            "True", Recolor("Wanda", "Hair", "images/WandaDoggy/Wanda_Doggy_Hair_Short_Back.png"),
#            ),
        (0,0), ConditionSwitch(
            #Hair
            "WandaX.Water or WandaX.Hair == 'long' or WandaX.Hair == 'wetlong'", Null(),
            "not Player.Male and 'facial' in WandaX.Spunk",Null(),
            "True", Recolor("Wanda", "Hair", "images/WandaDoggy/Wanda_Doggy_Hair_Short_Back.png"),
            ),
        (0,0), ConditionSwitch(
            #Head
            #"WandaX.Blush > 1", "images/WandaDoggy/Wanda_Doggy_Head_Blush2.png",
            "WandaX.Blush", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Head_Blush.png",
            "True", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Head.png",
            ),
        (0,0), ConditionSwitch(
            #Mouth
            "WandaX.Mouth == 'normal'", "images/WandaDoggy/Wanda_Doggy_Mouth_Normal.png",
            "WandaX.Mouth == 'lipbite'", "images/WandaDoggy/Wanda_Doggy_Mouth_Normal.png",
            "WandaX.Mouth == 'sucking'", "images/WandaDoggy/Wanda_Doggy_Mouth_Open.png",
            "WandaX.Mouth == 'kiss'", "images/WandaDoggy/Wanda_Doggy_Mouth_Kiss.png",
            "WandaX.Mouth == 'sad'", "images/WandaDoggy/Wanda_Doggy_Mouth_Sad.png",
            "WandaX.Mouth == 'smile'", "images/WandaDoggy/Wanda_Doggy_Mouth_Smirk.png",
            "WandaX.Mouth == 'grimace'", "images/WandaDoggy/Wanda_Doggy_Mouth_Normal.png",
            "WandaX.Mouth == 'surprised'", "images/WandaDoggy/Wanda_Doggy_Mouth_Open.png",
            "WandaX.Mouth == 'tongue'", "images/WandaDoggy/Wanda_Doggy_Mouth_Open.png",
            "WandaX.Mouth == 'smirk'", "images/WandaDoggy/Wanda_Doggy_Mouth_Smirk.png",
            "True", "images/WandaDoggy/Wanda_Doggy_Mouth_Normal.png",
            ),
#        (0,0), ConditionSwitch(
#            #chin spunk
#            "'chin' in WandaX.Spunk", "images/WandaDoggy/Wanda_Doggy_Spunk_Chin.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Mouth spunk
            "'mouth' not in WandaX.Spunk", Null(),
#            #"WandaX.Mouth == 'normal'", "images/WandaDoggy/Wanda_Doggy_Spunk_Normal.png",
#            #"WandaX.Mouth == 'sad'", "images/WandaDoggy/Wanda_Doggy_Spunk_Normal.png",
#            "WandaX.Mouth == 'lipbite'", "images/WandaDoggy/Wanda_Doggy_Spunk_Sad.png",
#            "WandaX.Mouth == 'smile'", "images/WandaDoggy/Wanda_Doggy_Mouth_Open.png",
#            "WandaX.Mouth == 'grimace'", "images/WandaDoggy/Wanda_Doggy_Mouth_Open.png",
#            "WandaX.Mouth == 'sucking'", "images/WandaDoggy/Wanda_Doggy_Mouth_Open.png",
#            #"WandaX.Mouth == 'kiss'", "images/WandaDoggy/Wanda_Doggy_Spunk_Open.png",
#            "WandaX.Mouth == 'surprised'", "images/WandaDoggy/Wanda_Doggy_Mouth_Open.png",
#            "WandaX.Mouth == 'tongue'", "images/WandaDoggy/Wanda_Doggy_Spunk_Smile.png",
            "True", "images/WandaDoggy/Wanda_Doggy_Spunk_Mouth.png",
            ),
        (0,0), ConditionSwitch(
            #Brows
            #"WandaX.Brows == 'normal'", "images/WandaDoggy/Wanda_Doggy_Brows_Normal.png",
            "WandaX.Brows == 'angry'", "images/WandaDoggy/Wanda_Doggy_Brows_Angry.png",
            "WandaX.Brows == 'sad'", "images/WandaDoggy/Wanda_Doggy_Brows_Sad.png",
            "WandaX.Brows == 'surprised'", "images/WandaDoggy/Wanda_Doggy_Brows_Surprised.png",
            #"WandaX.Brows == 'confused'", "images/WandaDoggy/Wanda_Doggy_Brows_Normal.png",
            "True", "images/WandaDoggy/Wanda_Doggy_Brows_Normal.png",
            ),
        (0,0), "Wanda Doggy Blink",#Eyes
#        (0,0), ConditionSwitch(
#            #Wet look
#            "WandaX.Water", "images/RogueDoggy/Rogue_Doggy_WetTop.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #suit collar
            "WandaX.Chest == 'mesh top'", Recolor("Wanda", "Chest", "images/WandaDoggy/Wanda_Doggy_Collar_Red.png"),
            "WandaX.Neck == 'scarf'", "images/WandaDoggy/Wanda_Doggy_Scarf.png",
            "WandaX.Neck", "images/WandaDoggy/Wanda_Doggy_Collar_Black.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #face spunk
#            "'facial' in WandaX.Spunk and Player.Male", "images/WandaDoggy/Wanda_Doggy_Spunk_Facial.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Hair
            "(WandaX.Water and WandaX.Hair == 'long') or WandaX.Hair == 'wetlong'", Recolor("Wanda", "Hair", "images/WandaDoggy/Wanda_Doggy_Hair_Long_Wet.png"),
            "(WandaX.Water and WandaX.Hair == 'long') and not Player.Male and 'facial' in WandaX.Spunk",Recolor("Wanda", "Hair", "images/WandaDoggy/Wanda_Doggy_Hair_Long_Wet.png"),
            "WandaX.Hair == 'long'", Recolor("Wanda", "Hair", "images/WandaDoggy/Wanda_Doggy_Hair_Long.png"),
            "WandaX.Water or WandaX.Hair == 'wet' or WandaX.Hair == 'wetlong'", Recolor("Wanda", "Hair", "images/WandaDoggy/Wanda_Doggy_Hair_Short_Wet.png"),
            "not Player.Male and 'facial' in WandaX.Spunk",Recolor("Wanda", "Hair", "images/WandaDoggy/Wanda_Doggy_Hair_Short_Wet.png"),
            "True", Recolor("Wanda", "Hair", "images/WandaDoggy/Wanda_Doggy_Hair_Short.png"),
            ),
        (0,0), ConditionSwitch(
                #hairband
                "not WandaX.Hat",Null(),
                "WandaX.Water or WandaX.Hair == 'wet' or WandaX.Hair == 'wetlong'", "images/WandaDoggy/Wanda_Doggy_Hairband_Wet.png",
                "not Player.Male and 'facial' in WandaX.Spunk","images/WandaDoggy/Wanda_Doggy_Hairband_Wet.png",
                "True", "images/WandaDoggy/Wanda_Doggy_Hairband_Short.png",
                ),
        (0,0), ConditionSwitch(
            #face spunk
            "'hair' in WandaX.Spunk and Player.Male", "images/WandaDoggy/Wanda_Doggy_Spunk_Hair.png",
            "'facial' in WandaX.Spunk and Player.Male", "images/WandaDoggy/Wanda_Doggy_Spunk_Facial.png",
#            "WandaX.Water or WandaX.Hair == 'wet'", "images/WandaDoggy/Wanda_Doggy_Head_Wet.png",
#            "not Player.Male and 'facial' in WandaX.Spunk","images/WandaDoggy/Wanda_Doggy_Head_Wet.png",
            "True", Null(),
            ),
        )
    #zoom 0.95
    #alpha 0.5
# End Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda Doggy Blink:
        #Eyes
        ConditionSwitch(
        "WandaX.Eyes == 'sexy'", "images/WandaDoggy/Wanda_Doggy_Eyes_Sexy.png",
        "WandaX.Eyes == 'side'", "images/WandaDoggy/Wanda_Doggy_Eyes_Side.png",
#        "WandaX.Eyes == 'normal'", "images/WandaDoggy/Wanda_Doggy_Eyes_Normal.png",
        "WandaX.Eyes == 'closed'", "images/WandaDoggy/Wanda_Doggy_Eyes_Closed.png",
        "WandaX.Eyes == 'manic'", "images/WandaDoggy/Wanda_Doggy_Eyes_Stunned.png",
        "WandaX.Eyes == 'down'", "images/WandaDoggy/Wanda_Doggy_Eyes_Down.png",
        "WandaX.Eyes == 'stunned'", "images/WandaDoggy/Wanda_Doggy_Eyes_Stunned.png",
        "WandaX.Eyes == 'surprised'", "images/WandaDoggy/Wanda_Doggy_Eyes_Surprised.png",
        "WandaX.Eyes == 'squint'", "images/WandaDoggy/Wanda_Doggy_Eyes_Sexy.png",
        "True", "images/WandaDoggy/Wanda_Doggy_Eyes_Normal.png",
        ),
    #    choice:
    #        3.5
    #    choice:
    #        3.25
    #    choice:
    #        3
        3
        # This randomizes the time between blinking.
        "images/WandaDoggy/Wanda_Doggy_Eyes_Closed.png"
        .25
        repeat

# End Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_Doggy_Head_Fore:
    LiveComposite(
        #Head
        (420,420),
        (0,0), ConditionSwitch(
            #Hair
            "(WandaX.Water and WandaX.Hair == 'long') or WandaX.Hair == 'wetlong'", Recolor("Wanda", "Hair", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Hair_Long_Wet_Fore.png"),
            "(WandaX.Water and WandaX.Hair == 'long') and not Player.Male and 'facial' in WandaX.Spunk",Recolor("Wanda", "Hair", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Hair_Long_Wet_Fore.png"),
            "WandaX.Hair == 'long'", Recolor("Wanda", "Hair", "images/WandaDoggy/Wanda_Doggy_Hair_Long_Fore.png"),
            "WandaX.Water or WandaX.Hair == 'wet' or WandaX.Hair == 'wetlong'", Recolor("Wanda", "Hair", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Hair_Short_Wet_Fore.png"),
            "not Player.Male and 'facial' in WandaX.Spunk",Recolor("Wanda", "Hair", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Hair_Short_Wet_Fore.png"),
            "True", Recolor("Wanda", "Hair", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Hair_Short_Fore.png"),
            ),
        (0,0), ConditionSwitch(
                #hairband
                "not WandaX.Hat",Null(),
                "WandaX.Water or WandaX.Hair == 'wet' or WandaX.Hair == 'wetlong'", "images/WandaDoggy/Wanda_Doggy_Hairband_Fore_Wet.png",
                "not Player.Male and 'facial' in WandaX.Spunk","images/WandaDoggy/Wanda_Doggy_Hairband_Fore_Wet.png",
                "True", "images/WandaDoggy/Wanda_Doggy_Hairband_Fore_Short.png",
                ),
        )
    #zoom 0.95
    #alpha 0.5
# End Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_Doggy_Ass:
    LiveComposite(
        #Lower body
        (420,750),
        (0,0), ConditionSwitch(
            #Legs backside
#            "WandaX.Legs == 'dress'",Recolor("Wanda", "Legs", "images/WandaDoggy/Wanda_Doggy_Legs_Dress_Under.png"),
            "WandaX.Upskirt", Null(),
            "WandaX.Legs == 'skirt'","images/WandaDoggy/Wanda_Doggy_Legs_Skirt_Under.png",
            "WandaX.Legs == 'dress'",Recolor("Wanda", "Legs", "images/WandaDoggy/Wanda_Doggy_Legs_Dress_Under.png"),
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Panties back
#            "not WandaX.PantiesDown or (WandaX.Legs == 'pants' and not WandaX.Upskirt)", Null(),
#            "WandaX.Panties == 'wolvie panties'", "images/WandaDoggy/Wanda_Doggy_Panties_Wolvie_Back.png",
#            "WandaX.Panties == 'lace panties'", "images/WandaDoggy/Wanda_Doggy_Panties_Lace_Back.png",
#            "WandaX.Panties", "images/WandaDoggy/Wanda_Doggy_Panties_Back.png",
#            "True", Null(),
#            ),
#        (0,0), "images/WandaDoggy/Wanda_Doggy_Ass.png", #Ass Base


        (0,0), ConditionSwitch(
            #Pussy base
            "WandaX.Legs and not WandaX.Upskirt", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Ass_Closed.png",
            "WandaX.Panties and not WandaX.PantiesDown", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Ass_Closed.png",
            "Player.Sprite and Player.Cock == 'in'", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Ass_Base.png",
            "Trigger == 'lick pussy'", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Ass_Open.png",
            "'dildo pussy' in (Trigger,Trigger2,WandaX.Offhand)", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Ass_Base.png",#Null(),
            "'fondle pussy' in (Trigger,Trigger2,WandaX.Offhand)", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Ass_Base.png",#Null(),
            "Trigger == 'insert pussy'", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Ass_Base.png",#Null(),
            "True", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Ass_Closed.png",
            ),
#        (0,0), ConditionSwitch(
#            #Hotdogging plate
#            "not Player.Sprite or Player.Cock != 'out'", Null(),
#            "True", "images/RogueDoggy/Rogue_Doggy_Hotdog.png",
#            ),
        (0,0), ConditionSwitch(
            #ass red
            "WandaX.Red", "images/WandaDoggy/Wanda_Doggy_Red.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Anus base
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    "Speed", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Anal_FullBase.png",      #Speed 1
                    "True", Null(),               #Speed 0
                    ),
            "'insert ass' in (Trigger,Trigger2,WandaX.Offhand)", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Anal_FullBase.png",
            "'dildo anal' in (Trigger,Trigger2,WandaX.Offhand)", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Anal_FullBase.png",
            "WandaX.Loose > 2", "Wanda_Gape_Anal",    #intentional
            "WandaX.Loose", "images/WandaDoggy/Wanda_Doggy_Asshole_Loose.png",
            "True", "images/WandaDoggy/Wanda_Doggy_Asshole_Tight.png",
            ),

        (0,0), ConditionSwitch(
            #Wet look
            "WandaX.Water", "images/WandaDoggy/Wanda_Doggy_Water_Ass.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #Hose
            "WandaX.Hose == 'stockings'", Recolor("Wanda", "Hose", "images/WandaDoggy/Wanda_Doggy_Hose_Stockings.png"),
#            "WandaX.Hose == 'socks'", "images/WandaDoggy/Wanda_Doggy_Hose_Socks.png",
#            "Player.Sprite and Player.Cock == 'in'", Null(),
#            "Player.Sprite and Player.Cock == 'anal'", Null(),
            "WandaX.Hose == 'stockings and garterbelt'", Recolor("Wanda", "Hose", "images/WandaDoggy/Wanda_Doggy_Hose_StockingsGarter.png"),
            "WandaX.Hose == 'garterbelt'", Recolor("Wanda", "Hose", "images/WandaDoggy/Wanda_Doggy_Hose_Garter.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Panties if Down
            "not WandaX.PantiesDown or (WandaX.Legs == 'pants' and not WandaX.Upskirt)", Null(),
            "WandaX.Panties == 'lace panties'", Recolor("Wanda", "Panties", "images/WandaDoggy/Wanda_Doggy_Panties_Bikini_Down.png"),
            "WandaX.Panties == 'bikini bottoms'", Recolor("Wanda", "Panties", "images/WandaDoggy/Wanda_Doggy_Panties_Bikini_Down.png"),
            "WandaX.Panties", Recolor("Wanda", "Panties", "images/WandaDoggy/Wanda_Doggy_Panties_Gray_Down.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunkpussy Layer
            "'in' in WandaX.Spunk and Player.Cock == 'in' and Player.Male",Null(),# "images/WandaDoggy/Wanda_Doggy_SpunkPussyOpen.png",  #fix for WandaX.Spunk is used later
            "'in' in WandaX.Spunk and Player.Male", "images/JeanDoggy/Jean_Doggy_SpunkPussyClosed.png",
            "WandaX.Wet and Player.Cock == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "WandaX.Wet", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pubes
            "not WandaX.Pubes", Null(),
            "Player.Sprite and Player.Cock == 'in'", Null(), # "images/WandaDoggy/Wanda_Doggy_Pubes_Fuckingucked.png",
            "'dildo pussy' in (Trigger,Trigger2,WandaX.Offhand)", Null(),
            "'fondle pussy' in (Trigger,Trigger2,WandaX.Offhand)",Null(),
            "Trigger == 'insert pussy'", Null(),
            "WandaX.Legs == 'pants' and not WandaX.Upskirt", Recolor("Wanda", "Pubes", "images/WandaDoggy/Wanda_Doggy_Pubes_Clothed.png"),
            "WandaX.PantiesDown and Trigger == 'lick pussy'", Recolor("Wanda", "Pubes", "images/WandaDoggy/Wanda_Doggy_Pubes_Open.png"),
            "WandaX.PantiesDown", Recolor("Wanda", "Pubes", "images/WandaDoggy/Wanda_Doggy_Pubes_Open.png"),
            "WandaX.Panties", Recolor("Wanda", "Pubes", "images/WandaDoggy/Wanda_Doggy_Pubes_Clothed.png"),
            "WandaX.Hose and WandaX.Hose == 'pantyhose'", Recolor("Wanda", "Pubes", "images/WandaDoggy/Wanda_Doggy_Pubes_Clothed.png"),
            "Trigger == 'lick pussy'", Recolor("Wanda", "Pubes", "images/WandaDoggy/Wanda_Doggy_Pubes_Open.png"),
            "True", Recolor("Wanda", "Pubes", "images/WandaDoggy/Wanda_Doggy_Pubes_Open.png"),
            ),
        (0,0), ConditionSwitch(
            #Pussy Piercings
            "Player.Sprite", Null(),
            "WandaX.Panties and not WandaX.PantiesDown", Null(),
            "WandaX.Pierce == 'barbell'", "images/WandaDoggy/Wanda_Doggy_Pierce_B.png",
            "(WandaX.Legs and WandaX.Legs != 'dress' and WandaX.Legs != 'skirt') and not WandaX.Upskirt", Null(),
            "WandaX.Pierce == 'ring'", "images/WandaDoggy/Wanda_Doggy_Pierce_R.png",
            "True", Null(),
            ),


        (2,-8), ConditionSwitch(
            #spunkanal Layer
            "'anal' not in WandaX.Spunk or (Player.Sprite and Player.Cock == 'anal' and Speed >= 1) or not Player.Male", Null(),
#            "Player.Cock == 'anal'", "images/WandaDoggy/Wanda_Doggy_SpunkAnalOpen.png",
            "WandaX.Loose", "images/JeanDoggy/Jean_Doggy_SpunkAnalLoose.png",
            "True", "images/JeanDoggy/Jean_Doggy_SpunkAnalLoose.png",
            ),
        (0,0), ConditionSwitch(
            #Panties if up
            "WandaX.PantiesDown or not WandaX.Panties", Null(),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),
            "WandaX.Panties == 'lace panties'", Recolor("Wanda", "Panties", "images/WandaDoggy/Wanda_Doggy_Panties_Lace.png"),
            "WandaX.Panties == 'bikini bottoms'", Recolor("Wanda", "Panties", "images/WandaDoggy/Wanda_Doggy_Panties_Bikini.png"),
            "WandaX.Wet", Recolor("Wanda", "Panties", "images/WandaDoggy/Wanda_Doggy_Panties_Gray_Wet.png"),
            "True", Recolor("Wanda", "Panties", "images/WandaDoggy/Wanda_Doggy_Panties_Gray.png"),
            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #full hose/tights
            "WandaX.Panties and WandaX.PantiesDown", Null(),
            "WandaX.Hose == 'ripped pantyhose'", Recolor("Wanda", "Hose", "images/WandaDoggy/Wanda_Doggy_Hose_Pantyhose_Holed.png"),
#            "WandaX.Hose == 'ripped tights'", "images/WandaDoggy/Wanda_Doggy_Hose_Tights_Holed.png",
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
            "WandaX.Hose == 'pantyhose'", Recolor("Wanda", "Hose", "images/WandaDoggy/Wanda_Doggy_Hose_Pantyhose.png"),
#            "WandaX.Hose == 'tights' and WandaX.Wet", "images/WandaDoggy/Wanda_Doggy_Hose_Tights_Wet.png",
#            "WandaX.Hose == 'tights'", "images/WandaDoggy/Wanda_Doggy_Hose_Tights.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Legs Layer
            "WandaX.Legs == 'dress'", ConditionSwitch(
                    "Player.Sprite and Player.Cock == 'anal' and Speed" , Recolor("Wanda", "Legs", "images/WandaDoggy/Wanda_Doggy_Legs_Dress_Up.png"),   #Rogue_Doggy_Legs_Skirt_UpAnal.png",
                    "WandaX.Upskirt", Recolor("Wanda", "Legs", "images/WandaDoggy/Wanda_Doggy_Legs_Dress_Up.png"),
                    "True", Recolor("Wanda", "Legs", "images/WandaDoggy/Wanda_Doggy_Legs_Dress.png"),
                    ),
            "WandaX.Legs == 'skirt'", ConditionSwitch(
                    "Player.Sprite and Player.Cock == 'anal' and Speed" , "images/WandaDoggy/Wanda_Doggy_Legs_Skirt_Up.png",   #Rogue_Doggy_Legs_Skirt_UpAnal.png",
                    "WandaX.Upskirt", "images/WandaDoggy/Wanda_Doggy_Legs_Skirt_Up.png",
                    "True", "images/WandaDoggy/Wanda_Doggy_Legs_Skirt.png",
                    ),
            "WandaX.Legs == 'pants'", ConditionSwitch(
                    "WandaX.Upskirt or WandaX.PantiesDown", Recolor("Wanda", "Legs", "images/WandaDoggy/Wanda_Doggy_Legs_Shorts_Down.png"),
                    "WandaX.Wet > 1", Recolor("Wanda", "Legs", "images/WandaDoggy/Wanda_Doggy_Legs_Pants_Wet.png"),
                    "True", Recolor("Wanda", "Legs", "images/WandaDoggy/Wanda_Doggy_Legs_Pants.png"),
                    ),
            "WandaX.Legs == 'shorts'", ConditionSwitch(
                    "WandaX.Upskirt or WandaX.PantiesDown", Recolor("Wanda", "Legs", "images/WandaDoggy/Wanda_Doggy_Legs_Shorts_Down.png"),
                    "WandaX.Wet > 1", Recolor("Wanda", "Legs", "images/WandaDoggy/Wanda_Doggy_Legs_Shorts_Wet.png"),
                    "True", Recolor("Wanda", "Legs", "images/WandaDoggy/Wanda_Doggy_Legs_Shorts.png"),
                    ),
#            "WandaX.Legs == 'yoga pants'", ConditionSwitch(
#                    "WandaX.Upskirt", "images/WandaDoggy/Wanda_Doggy_Legs_Yoga_Down.png",
#                    "WandaX.Wet > 1", "images/WandaDoggy/Wanda_Doggy_Legs_Yoga_Wet.png",
#                    "True", "images/WandaDoggy/Wanda_Doggy_Legs_Yoga.png",
#                    ),
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Pussy Piercings clothed
#            "Player.Sprite", Null(),
#            "WandaX.PantiesDown or (not WandaX.Panties and WandaX.Legs != 'leather pants')", Null(), #if not panties or legs, skip this
#            "WandaX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_RingC.png",
#            "WandaX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_BarbellC.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Pussy Composite
#            "WandaX.Legs and not WandaX.Upskirt",Null(),
#            "WandaX.Panties and not WandaX.PantiesDown", Null(),
            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Wanda_Pussy_Fucking3",#Speed 3
                    "Speed > 1", "Wanda_Pussy_Fucking2",#Speed 2
                    "Speed", "Wanda_Pussy_Heading",      #Speed 1
                    "True", "Wanda_Pussy_Static",              #Speed 0
                    ),
            "'dildo pussy' in (Trigger,Trigger2,WandaX.Offhand)", "Wanda_Pussy_Fucking2",
            "'fondle pussy' in (Trigger,Trigger2,WandaX.Offhand)", "Wanda_Pussy_Fingering",
            "Trigger == 'insert pussy'", "Wanda_Pussy_Fingering",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Anus base
#            "not Player.Sprite or Player.Cock != 'in'", Null(), #only shows when cock is out
#            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
#                    "Speed", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Anal_FullBase.png",      #Speed 1
#                    "True", Null(),               #Speed 0
#                    ),
#            "'insert ass' in (Trigger,Trigger2,WandaX.Offhand)", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Anal_FullBase.png",
#            "'dildo anal' in (Trigger,Trigger2,WandaX.Offhand)", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Anal_FullBase.png",
#            "WandaX.Loose > 2", "Wanda_Gape_Anal",    #intentional
#            "WandaX.Loose", "images/WandaDoggy/Wanda_Doggy_Asshole_Loose.png",
#            "True", "images/WandaDoggy/Wanda_Doggy_Asshole_Tight.png",
#            ),
        (0,0), ConditionSwitch(
            #Anus Composite
#            "WandaX.Legs and not WandaX.Upskirt",Null(),
#            "WandaX.Panties and not WandaX.PantiesDown", Null(),
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Wanda_Anal_Fucking2", #Speed 3
                    "Speed > 1", "Wanda_Anal_Fucking",  #Speed 2
                    "Speed", "Wanda_Anal_Heading",      #Speed 1
                    "True", "Wanda_Anal",               #Speed 0
                    ),
            "'dildo anal' in (Trigger,Trigger2,WandaX.Offhand)", "Wanda_Anal_Fucking",
            "'insert ass' in (Trigger,Trigger2,WandaX.Offhand)", "Wanda_Anal_Fingering",
            "WandaX.Plug", "images/PlugIn.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #Over Layer
            "WandaX.Acc == 'jacket' and (WandaX.Upskirt or WandaX.Legs == 'dress' or WandaX.Legs == 'skirt')", Recolor("Wanda", "Acc", "images/WandaDoggy/Wanda_Doggy_Legs_Jacket_Up.png"),
            "WandaX.Acc == 'jacket'", Recolor("Wanda", "Acc", "images/WandaDoggy/Wanda_Doggy_Legs_Jacket.png"),
            "WandaX.Over == 'towel' and (WandaX.Upskirt or WandaX.Legs == 'dress' or WandaX.Legs == 'skirt')", Recolor("Wanda", "Legs", "images/WandaDoggy/Wanda_Doggy_Legs_Dress_Up.png"),
            "WandaX.Over == 'towel'", Recolor("Wanda", "Legs", "images/WandaDoggy/Wanda_Doggy_Legs_Towel.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk back Layer
            "'back' in WandaX.Spunk and Player.Male", "images/WandaDoggy/Wanda_Doggy_Spunk_Ass.png",
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
#            "WandaX.Over == 'towel'", Null(),
#            "(WandaX.Legs == 'dress' or WandaX.Legs == 'other skirt') and WandaX.Upskirt", "images/WandaDoggy/Wanda_Doggy_Hotdog_Upskirt.png",
#            "True", "images/WandaDoggy/Wanda_Doggy_HotdogBack.png",
#            ),
        (0,0), ConditionSwitch(
            #Hotdogging Cock w/ alpha
            "not Player.Sprite or Player.Cock != 'out'", Null(),
            "(WandaX.Legs == 'dress' or WandaX.Legs == 'skirt') and WandaX.Upskirt and Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            "(WandaX.Legs == 'dress' or WandaX.Legs == 'skirt') and WandaX.Upskirt", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
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

image Wanda_Doggy_Feet:         #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
    contains:
            AlphaMask("Wanda_Doggy_Shins", "images/WandaDoggy/Wanda_Doggy_Feet_Mask.png")

image Wanda_Doggy_Feet_Under:             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
    #Wanda's footjob shins
#    contains:
#        "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Feet.png"
    contains:
            #hose legs
        ConditionSwitch(
            "WandaX.Hose == 'garterbelt'", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Feet.png",
#            "WandaX.Hose == 'ripped pantyhose'", "images/WandaDoggy/Wanda_Doggy_Feet_Holed.png",
            "WandaX.Hose == 'socks'", Recolor("Wanda", "Hose", "images/WandaDoggy/Wanda_Doggy_Feet_Socks.png"),
            "WandaX.Hose", Recolor("Wanda", "Hose", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Feet_Hose.png"),
            "True", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Feet.png",
            )
    contains:
        #pants
        ConditionSwitch(
            "WandaX.Legs == 'pants'", Recolor("Wanda", "Legs", "images/WandaDoggy/Wanda_Doggy_Feet_Pants.png"),
            "True", Null(),
            )
    contains:
        #spunk
        ConditionSwitch(
            "'feet' in WandaX.Spunk and Player.Male", "images/WandaDoggy/Wanda_Doggy_Spunk_Feet_Under.png",
            "True", Null(),
            )
#    pos (0,0)

image Wanda_Doggy_Feet_Over:             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
    #Wanda's footjob shins
#    contains:
#        "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Feet.png"
    contains:
            #hose legs
        ConditionSwitch(
            "WandaX.Hose == 'garterbelt'", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Feet_Over.png",
#            "WandaX.Hose == 'ripped pantyhose'", "images/WandaDoggy/Wanda_Doggy_Feet_Holed.png",
            "WandaX.Hose == 'socks'", Recolor("Wanda", "Hose", "images/WandaDoggy/Wanda_Doggy_Feet_Socks_Over.png"),
            "WandaX.Hose", Recolor("Wanda", "Hose", "images/WandaDoggy/Wanda_Doggy_Feet_Hose_Over.png"),
            "True", "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Feet_Over.png",
            )
    contains:
        #spunk
        ConditionSwitch(
            "'feet' in WandaX.Spunk and Player.Male", "images/WandaDoggy/Wanda_Doggy_Spunk_Feet_Over.png",
            "True", Null(),
            )
#    pos (0,0)

image Wanda_Doggy_Shins0:
        #static animation
        "Wanda_Doggy_Feet_Under"
        offset (0, 100) #(0,150) top


image Wanda_Doggy_GropeBreast:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        xzoom -.55
        yzoom .55
        offset (190,350)#(270,410)
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
        block:
            ease 1 rotate 10#60
            ease 1 rotate 0#90
            repeat

image Wanda_Gape_Anal:
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

image Zero_Wanda_Hotdog_Static:
    # The unmoving version of the hotdog cock
    # called in Doggy Ass LC
    contains:
        "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Wanda_Hotdog_Moving:
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


image Wanda_Pussy_Mask:
    #AlphaMask used to prevent the cock from moving past the pussy
    #Called in "Wanda_Pussy_Moving"
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

image Wanda_Pussy_Mask_Static:
    #AlphaMask used to prevent the cock from moving past the pussy in static pose
    #Called in "Wanda_Pussy_Moving"
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


image Wanda_Pussy_Static:
    #Full Animation for speed 0
    subpixel True
    contains:
        #moving hole
        "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Pussy_FHole.png"
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
#            "WandaX.Pubes", Recolor("Wanda", "Pubes", "images/WandaDoggy/Wanda_Doggy_Pubes_Open.png"),
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
            "WandaX.Pubes", Recolor("Wanda", "Pubes", "images/WandaDoggy/Wanda_Doggy_Pubes_Open.png"),
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
            "WandaX.Pierce == 'barbell'", "images/WandaDoggy/Wanda_Doggy_Pierce_B.png",
            "WandaX.Pierce == 'ring'", "images/WandaDoggy/Wanda_Doggy_Pierce_R.png",
            "True", Null(),
            )
        offset (-1,0)#(-3,8)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in WandaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
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
        AlphaMask("Zero_Wanda_Doggy_Static", "Wanda_Pussy_Mask_Static")
    xoffset 2

image Wanda_Pussy_Hole_Mask_Static:
    # This is the alpha used for the little flap in the heading animation "Wanda_Pussy_Moving"
    contains:
        #Base
        AlphaMask("images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat

#image Wanda_PussyHole_Static:
#    #This is the image impacted by the mask for the pussy flap in "Wanda_Pussy_Moving"
#    contains:
#        #Mask
#        "images/WandaDoggy/Wanda_Doggy_Pussy_FHeading.png"
#        anchor (0.52,0.69)
#        pos (217,515)
#        zoom 1
#        alpha .9
#        block:
#            ease 1 ypos 512
#            pause 1
#            ease 3 ypos 515
#            repeat


image Zero_Wanda_Doggy_Static:
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

image Wanda_Pussy_Heading:
    #Full Animation for speed 1
    subpixel True
    contains:
        #moving hole
        "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Pussy_FHole.png"
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
#            "WandaX.Pubes", Recolor("Wanda", "Pubes", "images/WandaDoggy/Wanda_Doggy_Pubes_Fucking.png"),
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
            "WandaX.Pubes", Recolor("Wanda", "Pubes", "images/WandaDoggy/Wanda_Doggy_Pubes_Fucking.png"),
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
            "WandaX.Pubes", Recolor("Wanda", "Pubes", "images/WandaDoggy/Wanda_Doggy_Pubes_Fucking.png"),
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
            "WandaX.Pierce == 'barbell'", "images/WandaDoggy/Wanda_Doggy_Pierce_B.png",
            "WandaX.Pierce == 'ring'", "images/WandaDoggy/Wanda_Doggy_Pierce_R.png",
            "True", Null(),
            )
        offset (-1,0)#(-3,8)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in WandaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
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
        AlphaMask("Zero_Wanda_Doggy_Heading", "Wanda_Pussy_Mask")


#    contains:
#        # expanding pussy flap
#        AlphaMask("Wanda_Pussy_Heading_Flap", "Wanda_Pussy_Hole_Mask")
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in WandaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
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
    xoffset 2


image Wanda_Pussy_Hole_Mask:
    # This is the alpha used for the little flap in the heading animation "Wanda_Pussy_Heading"
    contains:
        #Base
        AlphaMask("images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat

#image Wanda_Pussy_Heading_Flap:
#    #This is the image impacted by the mask for the pussy flap in "Wanda_Pussy_Heading"
#    contains:
#        #Mask
#        "images/WandaDoggy/Wanda_Doggy_Pussy_FHeading.png"
#        anchor (0.52,0.69)
#        pos (217,515)
#        zoom 1
#        alpha .9
#        block:
#            ease 1 ypos 505
#            pause 1
#            ease 3 ypos 515
#            repeat

image Wanda_Pussy_Fingering:
    #Full Animation for speed 1
    subpixel True
    contains:
        #moving hole
        "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Pussy_FHole.png"
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
            "WandaX.Pubes", Recolor("Wanda", "Pubes", "images/WandaDoggy/Wanda_Doggy_Pubes_Open.png"),
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
            "WandaX.Pierce == 'barbell'", "images/WandaDoggy/Wanda_Doggy_Pierce_B.png",
            "WandaX.Pierce == 'ring'", "images/WandaDoggy/Wanda_Doggy_Pierce_R.png",
            "True", Null(),
            )
        offset (-1,0)#(-3,8)

    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in WandaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
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
#        AlphaMask("Wanda_Pussy_Heading_Flap", "Wanda_Pussy_Hole_Mask")

    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in WandaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
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


image Zero_Wanda_Doggy_Heading:
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

image Wanda_Pussy_Fucking2:
    #Full Animation for speed 2
    contains:
        #Base
        "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Pussy_FHole.png"
    contains:
        #pubes
        ConditionSwitch(
            "WandaX.Pubes", Recolor("Wanda", "Pubes", "images/WandaDoggy/Wanda_Doggy_Pubes_Fucking.png"),
            "True", Null(),
            )
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "WandaX.Pierce == 'barbell'", "images/WandaDoggy/Wanda_Doggy_Pierce_B.png",
            "WandaX.Pierce == 'ring'", "images/WandaDoggy/Wanda_Doggy_Pierce_R.png",
            "True", Null(),
            )
        offset (-1,0)#(-3,8)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in WandaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            "'dildo pussy' in (Trigger,Trigger2,WandaX.Offhand)", AlphaMask("Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "True",AlphaMask("Zero_Wanda_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            ),
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in WandaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )
    xoffset 1


image Zero_Wanda_Doggy_Fucking2:
    # Sex Speed 2 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat


image Wanda_Pussy_Fucking3:
    #Full Animation for speed 3
    contains:
        #Base
        "images/WandaDoggy/[WandaX.skin_image.skin_path]Wanda_Doggy_Pussy_FHole.png"
    contains:
        #pubes
        ConditionSwitch(
            "WandaX.Pubes", Recolor("Wanda", "Pubes", "images/WandaDoggy/Wanda_Doggy_Pubes_Fucking.png"),
            "True", Null(),
            )
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "WandaX.Pierce == 'barbell'", "images/WandaDoggy/Wanda_Doggy_Pierce_B.png",
            "WandaX.Pierce == 'ring'", "images/WandaDoggy/Wanda_Doggy_Pierce_R.png",
            "True", Null(),
            )
        offset (-1,0)#(-3,8)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in WandaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Wanda_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in WandaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )
    xoffset 1


image Zero_Wanda_Doggy_Fucking3:
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

image Wanda_Anal:
    #Anal static Loose
    contains:
        #Base
        "images/WandaDoggy/Wanda_Doggy_Asshole_Loose.png"
        anchor (0.50,0.69)
        pos (208,515)#(208,500)
        zoom 1.25
    contains:
        #Cock
        "Zero_Doggy_Insert"
        pos (172,500)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Wanda_Anal_Fingering:
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
            "'anal' in WandaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
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
        AlphaMask("Zero_Wanda_Doggy_Anal_Finger", "Wanda_Doggy_Anal_Fingering_Mask")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in WandaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
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

image Zero_Wanda_Doggy_Anal_Finger:
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
image Wanda_Doggy_Anal_Fingering_Mask:
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
image Wanda_Anal_Heading:
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
            "'anal' in WandaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
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
        AlphaMask("Zero_Wanda_Doggy_Anal_Heading", "Wanda_Doggy_Anal_Heading_Mask")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in WandaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
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

image Zero_Wanda_Doggy_Anal_Heading:
        #the cock anal heading animation
    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500#505
            repeat

image Zero_Wanda_Doggy_Anal_HeadingJunk:
    #this is a mask to correct an annoying glitch in the core mask
    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease .5 ypos 550
            pause .25
            ease 1.75 ypos 600#505
            repeat

image Wanda_Doggy_Anal_Heading_Mask:
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

image Wanda_Doggy_Anal_Head_Top:
#animation for anal fucking top half
    contains:
        subpixel True
        "Wanda_Doggy_Body"
        ypos 0
        block:
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat

image Wanda_Doggy_Anal_Head_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Wanda_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -10
            easeout .1 ypos -7
            easein .9 ypos 0
            pause .9
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Wanda_Doggy_Anal1:
    #Animation for speed 2 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat

image Wanda_Anal_Fucking:
    #Animation for speed 2 Ass
    contains:
        #Hole
        "images/GwenDoggy/Gwen_Doggy_Anal_FullHole.png"
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in WandaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            #full hose/tights
            "'dildo anal' in (Trigger,Trigger2,WandaX.Offhand)", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", AlphaMask("Zero_Wanda_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            )
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in WandaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )

image Wanda_Doggy_Fuck_Top:
    #animation for anal fucking top half
    contains:
        subpixel True
        "Wanda_Doggy_Body"
        ypos 10#28
        pause .4
        block:
            ease .2 ypos 0#10
            pause .3
            ease 2 ypos 10#28
            repeat

image Wanda_Doggy_Fuck_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Wanda_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15#-25
            ease .1 ypos -5#-15
            pause .2
            ease 1.6 ypos 0
            repeat


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Wanda_Doggy_Anal2:
    #Animation for speed 3 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat

image Wanda_Anal_Fucking2:
    #Animation for speed 3 Ass
    contains:
        #Hole
        "images/GwenDoggy/Gwen_Doggy_Anal_FullHole.png"
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in WandaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Wanda_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in WandaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )

image Wanda_Doggy_Fuck2_Top:
    #animation for anal fucking2 top half
    contains:
        subpixel True
        "Wanda_Doggy_Body"
        ypos 5
        block:
            pause .15
            ease .1 ypos -10#0
            pause .1
            easein .5 ypos 5#20
            pause .05
            repeat

image Wanda_Doggy_Fuck2_Ass:
    #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Wanda_Doggy_Ass"
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

image Wanda_Doggy_Feet0:
    #static animation
    contains:
        "Wanda_Doggy_Feet_Under"
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
        "Wanda_Doggy_Feet_Over"
        pos (0, 0) #(0,0) top
        block:
            subpixel True
            pause .5
            ease 2 ypos 20
            pause .5
            ease 2 ypos 0
            repeat

image Wanda_Doggy_Foot0_Top:
    #animation for footjob top half
    contains:
        subpixel True
        "Wanda_Doggy_Body"
        ypos 10#28
        #pause .4
        block:
            pause .5
            ease 2 ypos 14
            pause .5
            ease 2 ypos 10
            repeat

image Wanda_Doggy_Foot0_Ass:
    #animation for footjob ass half
    contains:
        subpixel True
        "Wanda_Doggy_Ass"
        ypos 0
        block:     #total 3
            pause .1 #.5
            ease 2 ypos 10
            pause .5
            ease 2.4 ypos 0
            repeat


image Wanda_Doggy_Feet1:
    #slow animation
    contains:
        "Wanda_Doggy_Feet_Under"
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
        "Wanda_Doggy_Feet_Over"
        pos (0, 0) #(0,0) top
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat

image Wanda_Doggy_Foot1_Top:
    #animation for footjob top half
    contains:
        subpixel True
        "Wanda_Doggy_Body"
        ypos 0#28
        block:
            pause .3
            ease 1.9 ypos 80
            ease .8 ypos 0#70
            repeat

image Wanda_Doggy_Foot1_Ass:
    #animation for footjob ass half
    contains:
        subpixel True
        "Wanda_Doggy_Ass"
        ypos 0
        block: #total 3
            pause .3
            ease 2 ypos 80
            ease .7 ypos 0
            repeat


image Wanda_Doggy_Feet2:
    #fast animation
    contains:
        "Wanda_Doggy_Feet_Under"
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
        "Wanda_Doggy_Feet_Over"
        pos (0, 0) #(0,0) top
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat

image Wanda_Doggy_Foot2_Top:
    #animation for footjob top half
    contains:
        subpixel True
        "Wanda_Doggy_Body"
        ypos 70#28
        block:
            pause .05
            ease .6 ypos 90#90#110
            ease .3 ypos 70#70
            repeat

image Wanda_Doggy_Foot2_Ass:
    #animation for footjob ass half
    contains:
        subpixel True
        "Wanda_Doggy_Ass"
        ypos 70
        block: #total .95
            pause .15#.05
            ease .6 ypos 90#110
            ease .2 ypos 70
            repeat

# Footjob animations end > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Doggy Launch/Reset
label Wanda_Doggy_Launch(Line = Trigger):
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    return
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
    if renpy.showing("Wanda_Doggy_Animation"):
        return
    $ Speed = 0
    call Girl_Hide(WandaX,1) #call Rogue_Hide
    show Wanda_Doggy_Animation at SpriteLoc(StageCenter+48) zorder 150
    with dissolve
    return

label Wanda_Doggy_Reset:
    if not renpy.showing("Wanda_Doggy_Animation"):
        return
#    $ Trigger = 0               #fix, not sure this is a good idea
    $ WandaX.ArmPose = 2
    $ WandaX.SpriteVer = 0
    hide Wanda_Doggy_Animation
    call Girl_Hide(WandaX) #call Rogue_Hide
    show Wanda_Sprite at SpriteLoc(WandaX.SpriteLoc) zorder WandaX.Layer:
                    alpha 1 zoom 1 offset (0,0) anchor (0.6, 0.0)
    with dissolve
    $ Speed = 0
    return

# End Wanda Doggy Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



## Start Wanda Sex Pose Content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Wanda Sex Pose core / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_SexSprite:
    LiveComposite(
        (1120,840),

#        (0,0), ConditionSwitch(
#                #Shows different upper body motion depending on events
#                "True", "Wanda_Sex_Speed2",
#                ),
        (0,0), ConditionSwitch(
                #Shows different motion depending on events
#                "not Player.Sprite", "Wanda_Sex_Body_Static",
                "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Wanda_Sex_Fucking_Speed3",
                        "Speed >= 2", "Wanda_Sex_Fucking_Speed2",
                        "Speed", "Wanda_Sex_Fucking_Speed1",
                        "True", "Wanda_Sex_Fucking_Speed0",
                        ),
                "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Wanda_Sex_Anal_Speed3",
                        "Speed >= 2", "Wanda_Sex_Anal_Speed2",
                        "Speed", "Wanda_Sex_Anal_Speed1",
                        "True", "Wanda_Sex_Anal_Speed0",
                        ),
                "Player.Sprite and Player.Cock == 'out' and Speed >= 2","Wanda_Sex_Hotdog_Speed2",
                "Player.Sprite and Player.Cock == 'out' and Speed >= 1","Wanda_Sex_Hotdog_Speed1",
                "Player.Cock == 'foot'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 2", "Wanda_Sex_FJ_Speed2",
                        "Speed", "Wanda_Sex_FJ_Speed1",
                        "True", "Wanda_Sex_FJ_Speed0",
                        ),
#                "Player.Cock == 'out' and Speed >= 2","Wanda_Hotdog_Body_Anim2",
                "True", "Wanda_Sex_Static",
                ),
        )
    align (0.6,0.0)
    pos (700,200)#(650,303)
    zoom 1#0.85

# End Wanda Sex Pose core / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Wanda Sex Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Wanda_Sex_Body:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Wanda_SexSprite
        (1120,840),
#        (0,-100), "images/WandaSex/Wanda_Sex_Headref.png",
        (460,120), "Wanda_HairBack_Sex",
        (0,0), "images/WandaSex/[WandaX.skin_image.skin_path]Wanda_Sex_Body.png",

        (0,0), ConditionSwitch(
            #mesh arm layer
            "WandaX.Over == 'purple top'", "images/WandaSex/Wanda_Sex_Over_Purple_Arm.png",
            "WandaX.Chest == 'mesh top'", Recolor("Wanda", "Chest", "images/WandaSex/Wanda_Sex_Chest_Mesh_Arm.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #jacket arm layer
            "WandaX.Acc == 'jacket'", Recolor("Wanda", "Acc", "images/WandaSex/Wanda_Sex_Jacket_Arm.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #bra layer
            "WandaX.Uptop", ConditionSwitch(
                    #if the top's down. . .
                    "WandaX.Chest == 'mesh top'", Recolor("Wanda", "Chest", "images/WandaSex/Wanda_Sex_Chest_Mesh_Up.png"),
                    "WandaX.Chest == 'bikini top'", Recolor("Wanda", "Chest", "images/WandaSex/Wanda_Sex_Chest_Bikini_Up.png"),
#                    "WandaX.Chest == 'lace bra'", "images/WandaSex/Wanda_Sex_Chest_Lace_Up.png",
                    "WandaX.Chest", Recolor("Wanda", "Chest", "images/WandaSex/Wanda_Sex_Chest_Bra_Up.png"),
                    "True", Null(),
                    ),
            "WandaX.Chest == 'mesh top'", Recolor("Wanda", "Chest", "images/WandaSex/Wanda_Sex_Chest_Mesh.png"),
            "WandaX.Chest == 'bikini top'", Recolor("Wanda", "Chest", "images/WandaSex/Wanda_Sex_Chest_Bikini.png"),
            "WandaX.Chest == 'lace bra'", Recolor("Wanda", "Chest", "images/WandaSex/Wanda_Sex_Chest_Lace.png"),
            "WandaX.Chest", Recolor("Wanda", "Chest", "images/WandaSex/Wanda_Sex_Chest_Bra.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "WandaX.Water", "images/WandaSex/Wanda_Sex_Water_Body.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #dress layer
            "WandaX.Uptop and WandaX.Legs == 'dress'", Recolor("Wanda", "Legs", "images/WandaSex/Wanda_Sex_Over_Dress_Up.png"),
            "WandaX.Legs == 'dress'", Recolor("Wanda", "Legs", "images/WandaSex/Wanda_Sex_Over_Dress.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #shirt layer
            "WandaX.Uptop", ConditionSwitch(
                    #if the top's down. . .
#                    "WandaX.Over == 'towel'", Recolor("Wanda", "Over", "images/WandaSex/Wanda_Sex_Over_Towel.png"),
                    "WandaX.Over == 'purple top'", "images/WandaSex/Wanda_Sex_Over_Purple_Up.png",
                    "WandaX.Over == 'shirt'", Recolor("Wanda", "Over", "images/WandaSex/Wanda_Sex_Over_Shirt_Up.png"),
                    "WandaX.Over == 'corset'", Recolor("Wanda", "Over", "images/WandaSex/Wanda_Sex_Over_Corset_Up.png"),
                    "True", Null(),
                    ),
            "WandaX.Over == 'towel'", Recolor("Wanda", "Over", "images/WandaSex/Wanda_Sex_Over_Towel.png"),
            "WandaX.Over == 'purple top'", "images/WandaSex/Wanda_Sex_Over_Purple.png",
            "WandaX.Over == 'shirt'", Recolor("Wanda", "Over", "images/WandaSex/Wanda_Sex_Over_Shirt.png"),
            "WandaX.Over == 'corset'", Recolor("Wanda", "Over", "images/WandaSex/Wanda_Sex_Over_Corset.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #necklace layer
            "WandaX.Neck == 'scarf'", "images/WandaSex/Wanda_Sex_Scarf.png",
            "WandaX.Neck", "images/WandaSex/Wanda_Sex_Neck.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #jacket layer
            "WandaX.Acc == 'jacket'", Recolor("Wanda", "Acc", "images/WandaSex/Wanda_Sex_Jacket.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #over jacket layer layer
            "not WandaX.Uptop", Null(),
            "WandaX.Over == 'shirt' or WandaX.Chest", Recolor("Wanda", "Chest", "images/WandaSex/Wanda_Sex_Chest_Red_Over.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #nipples layer
            "WandaX.Pierce == 'ring'", ConditionSwitch(
                    "WandaX.Uptop", "images/WandaSex/Wanda_Sex_Nips_R.png",

                    "WandaX.Over == 'towel'", "images/WandaSex/Wanda_Sex_Nips_R_Black.png",
                    "WandaX.Over == 'purple top'", "images/WandaSex/Wanda_Sex_Nips_R_Purp.png",
                    "WandaX.Over", "images/WandaSex/Wanda_Sex_Nips_R_Red.png",
                    "WandaX.Legs == 'dress'", "images/WandaSex/Wanda_Sex_Nips_R_Black.png",
                    #"WandaX.Over == 'corset'", "images/WandaSex/Wanda_Sex_Nips_R_Red.png",

                    "WandaX.Chest == 'mesh top'", "images/WandaSex/Wanda_Sex_Nips_R_Mesh.png",
                    "WandaX.Chest == 'lace bra'", "images/WandaSex/Wanda_Sex_Nips_R_Lace.png",
                    #"WandaX.Chest == 'bikini top'", "images/WandaSex/Wanda_Sex_Nips_R_Red.png",
                    "WandaX.Chest", "images/WandaSex/Wanda_Sex_Nips_R_Red.png",
                    "True", "images/WandaSex/Wanda_Sex_Nips_R.png",
                    ),
            "WandaX.Pierce", ConditionSwitch( #barbells
                    "WandaX.Uptop", "images/WandaSex/Wanda_Sex_Nips_B.png",

                    "WandaX.Over == 'towel'", "images/WandaSex/Wanda_Sex_Nips_B_Black.png",
                    "WandaX.Over == 'purple top'", "images/WandaSex/Wanda_Sex_Nips_B_Purp.png",
                    "WandaX.Over", "images/WandaSex/Wanda_Sex_Nips_B_Red.png",
                    "WandaX.Legs == 'dress'", "images/WandaSex/Wanda_Sex_Nips_B_Black.png",
                    #"WandaX.Over == 'corset'", "images/WandaSex/Wanda_Sex_Nips_B_Red.png",

                    "WandaX.Chest == 'mesh top'", "images/WandaSex/Wanda_Sex_Nips_B_Mesh.png",
                    "WandaX.Chest == 'lace bra'", "images/WandaSex/Wanda_Sex_Nips_B_Lace.png",
                    #"WandaX.Chest == 'bikini top'", "images/WandaSex/Wanda_Sex_Nips_B_Red.png",
                    "WandaX.Chest", "images/WandaSex/Wanda_Sex_Nips_B_Red.png",
                    "True", "images/WandaSex/Wanda_Sex_Nips_B.png",
                    ),
            "WandaX.Lust < 50 and not WandaX.OCount", Null(),                                                 #nips only poke at high lust
            "WandaX.Uptop", "images/WandaSex/Wanda_Sex_Nips.png",

            "WandaX.Over == 'towel'", "images/WandaSex/Wanda_Sex_Nips_Black.png",
            "WandaX.Over == 'purple top'", "images/WandaSex/Wanda_Sex_Nips_Purp.png",
            "WandaX.Over", "images/WandaSex/Wanda_Sex_Nips_Red.png",
            "WandaX.Legs == 'dress'", "images/WandaSex/Wanda_Sex_Nips_Black.png",
            #"WandaX.Over == 'corset'", "images/WandaSex/Wanda_Sex_Nips_Red.png",

            "WandaX.Chest == 'mesh top'", "images/WandaSex/Wanda_Sex_Nips_Mesh.png",
            "WandaX.Chest == 'lace bra'", "images/WandaSex/Wanda_Sex_Nips_Lace.png",
            #"WandaX.Chest == 'bikini top'", "images/WandaSex/Wanda_Sex_Nips_Red.png",
            "WandaX.Chest", "images/WandaSex/Wanda_Sex_Nips_Red.png",
            "True", "images/WandaSex/Wanda_Sex_Nips.png",
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'belly' in WandaX.Spunk and Player.Male", "images/WandaSex/Wanda_Sex_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'tits' in WandaX.Spunk and Player.Male", "images/WandaSex/Wanda_Sex_Spunk_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast fondling animation
            "Trigger == 'fondle breasts' or Trigger2 == 'fondle breasts'", "Wanda_Sex_Fondle_Breasts",
            "True", Null()
            ),
        (0,0), ConditionSwitch(
            #breast licking animation
            "Trigger == 'suck breasts' or Trigger2 == 'suck breasts'", "Wanda_Sex_Lick_Breasts",
            "True", Null()
            ),
        (455,120), "Wanda_Head_Sex",  #(50,-325)(335,-40)
#        (0,0), "images/WandaSex/Wanda_Sex_HeadRef.png",
        )
#    yoffset -163
# End Wanda Sex Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Wanda_Head_Sex:
    LiveComposite(
        (820,820),
        (0,0), ConditionSwitch(
            # Face background plate
            "WandaX.Blush >= 2", "images/WandaSprite/[WandaX.skin_image.skin_path]Wanda_Sprite_Head_Blush2.png",
            "WandaX.Blush", "images/WandaSprite/[WandaX.skin_image.skin_path]Wanda_Sprite_Head_Blush1.png",
            "True", "images/WandaSprite/[WandaX.skin_image.skin_path]Wanda_Sprite_Head.png",
            ),
        (0,0), ConditionSwitch(
            #chin spunk
            "'chin' in WandaX.Spunk and Player.Male", "images/WandaSprite/Wanda_Sprite_Spunk_Chin.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Mouths
            "WandaX.Mouth == 'lipbite'", "images/WandaSprite/Wanda_Sprite_Mouth_Lipbite.png",
            "WandaX.Mouth == 'sucking'", "images/WandaSprite/Wanda_Sprite_Mouth_Open.png",
            "WandaX.Mouth == 'kiss'", "images/WandaSprite/Wanda_Sprite_Mouth_Kiss.png",
            "WandaX.Mouth == 'sad'", "images/WandaSprite/Wanda_Sprite_Mouth_Sad.png",
            "WandaX.Mouth == 'smile'", "images/WandaSprite/Wanda_Sprite_Mouth_Open.png",
            "WandaX.Mouth == 'surprised'", "images/WandaSprite/Wanda_Sprite_Mouth_Open.png",
#            "not Player.Male and 'mouth' in WandaX.Spunk and WandaX.Mouth == 'tongue'", "images/WandaSprite/Wanda_Sprite_Mouth_Tongue_Wet.png",
            "WandaX.Mouth == 'tongue'", "images/WandaSprite/Wanda_Sprite_Mouth_Tongue.png",
            "WandaX.Mouth == 'grimace'", "images/WandaSprite/Wanda_Sprite_Mouth_Open.png",
            "WandaX.Mouth == 'smirk'", "images/WandaSprite/Wanda_Sprite_Mouth_Smirk.png",
            "WandaX.Mouth == 'open'", "images/WandaSprite/Wanda_Sprite_Mouth_Open.png",
            "True", "images/WandaSprite/Wanda_Sprite_Mouth_Smirk.png",
            ),
        (0,0), ConditionSwitch(
            #Mouths spunk
            "'mouth' not in WandaX.Spunk or not Player.Male", Null(),
            "WandaX.Mouth == 'sucking'", "images/WandaSprite/Wanda_Sprite_Spunk_Tongue.png",
#            "WandaX.Mouth == 'kiss'", "images/WandaSprite/Wanda_Sprite_Spunk_Kiss.png",
#            "WandaX.Mouth == 'sad'", "images/WandaSprite/Wanda_Sprite_Spunk_Sad.png",
#            "WandaX.Mouth == 'smirk'", "images/WandaSprite/Wanda_Sprite_Spunk_Sad.png",
#            "WandaX.Mouth == 'lipbite'", "images/WandaSprite/Wanda_Sprite_Spunk_Sad.png",
            "WandaX.Mouth == 'surprised'", "images/WandaSprite/Wanda_Sprite_Spunk_Tongue.png",
#            "WandaX.Mouth == 'open'", "images/WandaSprite/Wanda_Sprite_Spunk_Open.png",
            "WandaX.Mouth == 'tongue'", "images/WandaSprite/Wanda_Sprite_Spunk_Tongue.png",
            "True", "images/WandaSprite/Wanda_Sprite_Spunk_Smirk.png",
            ),
        (0,0), ConditionSwitch(
            #wet face
            "Player.Male", Null(),
            "'mouth' not in WandaX.Spunk and 'chin' not in WandaX.Spunk", Null(),
            "WandaX.Mouth == 'tongue'", "images/WandaSprite/Wanda_Sprite_Wet_MouthTongue.png",
            "'chin' in WandaX.Spunk", "images/WandaSprite/Wanda_Sprite_Wet_Mouth.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(     #    (0,5)
            #brows
            "WandaX.Brows == 'angry'", "images/WandaSprite/[WandaX.skin_image.skin_path]Wanda_Sprite_Brows_Angry.png",
            "WandaX.Brows == 'sad'", "images/WandaSprite/[WandaX.skin_image.skin_path]Wanda_Sprite_Brows_Sad.png",
            "WandaX.Brows == 'surprised'", "images/WandaSprite/[WandaX.skin_image.skin_path]Wanda_Sprite_Brows_Surprised.png",
            "WandaX.Brows == 'confused'", "images/WandaSprite/[WandaX.skin_image.skin_path]Wanda_Sprite_Brows_Confused.png",
            "True", "images/WandaSprite/[WandaX.skin_image.skin_path]Wanda_Sprite_Brows_Normal.png",
            ),
        (0,0), "Wanda Blink",     #Eyes  (0,5)
        (0,0), ConditionSwitch(
            #hair over
#            "renpy.showing('Wanda_BJ_Animation')", Null(),
#            "renpy.showing('Wanda_SexSprite')", "images/WandaSex/Wanda_Sprite_Hair_Long_UnderSex.png",

            "WandaX.Hair == 'wetlong' or (WandaX.Hair == 'long' and WandaX.Water)", "images/WandaSprite/Wanda_Sprite_Hair_Long_Wet_Sex.png",
            "WandaX.Hair == 'long' and (not Player.Male and 'facial' in WandaX.Spunk)","images/WandaSprite/Wanda_Sprite_Hair_Long_Wet_Sex.png",
            "WandaX.Hair == 'wet' or WandaX.Water", Recolor("Wanda", "Hair", "images/WandaSprite/Wanda_Sprite_Hair_Short_Wet.png"),
            "not Player.Male and 'facial' in WandaX.Spunk",Recolor("Wanda", "Hair", "images/WandaSprite/Wanda_Sprite_Hair_Short_Wet.png"),
            "WandaX.Hair == 'long'", "images/WandaSprite/Wanda_Sprite_Hair_Long_Sex.png",
            "True", Recolor("Wanda", "Hair", "images/WandaSprite/Wanda_Sprite_Hair_Short.png"),
            ),
        (0,0), ConditionSwitch(
                #hairband
                "not WandaX.Hat",Null(),
                "True", "images/WandaSprite/Wanda_Sprite_Headband.png",
                ),
        (0,0), ConditionSwitch(
            #Hair Water
            "WandaX.Water", "images/WandaSprite/Wanda_Sprite_Water_Face.png",
            "not Player.Male and 'facial' in WandaX.Spunk", "images/WandaSprite/Wanda_Sprite_Water_Face.png",
            "True",Null(),
            ),
        (0,0), ConditionSwitch(
            #facial spunk
            "'hair' in WandaX.Spunk and Player.Male", "images/WandaSprite/Wanda_Sprite_Spunk_Hair.png",
            "'facial' in WandaX.Spunk and Player.Male", "images/WandaSprite/Wanda_Sprite_Spunk_Facial.png",
            "True", Null(),
            ),
        )
    anchor (0.5, 0.5)
    zoom .37#.5
    transform_anchor True
#    rotate -10
#    alpha 0.7

image Wanda_Head_Sexb:
    # The head used for the sex pose, referenced by Wanda_Sex_Body
    "Wanda_Sprite_Head"
    zoom 1.0#1.24
    anchor (0.5,0.5)
    rotate 20#17
#    alpha 0.5

image Wanda_HairBack_Sex:
    # The hair behind the head for the sex pose, referenced by Wanda_Sex_Body
    "Wanda_Sprite_HairBack"
    zoom .9#1.36
    anchor (0.5,0.5)
#    rotate 20#15


image Wanda_Sex_Lick_Breasts:
        "Lick_Anim"
        zoom 0.5
        offset (490,340)#(390,620)

image Wanda_Sex_Fondle_Breasts:
        "GropeLeftBreast"
        zoom .93#1.5
        offset (360,0)#(190,-200)

# Start Wanda Sex Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Wanda_Sex_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Wanda_SexSprite
        (1120,880),
        (545,540), ConditionSwitch(    #165,560
            #Personal Wetness
            "not WandaX.Wet", Null(),
            "(WandaX.Legs == 'pants' or WandaX.Legs == 'shorts') and not WandaX.Upskirt", Null(),
            "WandaX.Panties and not WandaX.PantiesDown", Null(),
            "Player.Cock == 'foot'", Null(),
            "WandaX.Wet == 1", "Wet_Drip",
            "True", "Wet_Drip2",
            ),

        (545,540), ConditionSwitch(    #205,530
            #Spunk
            "'anal' not in WandaX.Spunk or not Player.Male", Null(),
            "Player.Cock == 'foot'", Null(),
            "(WandaX.Legs == 'pants' or WandaX.Legs == 'shorts') and not WandaX.Upskirt", Null(),
            "WandaX.Wet == 1", "Spunk_Drip",
            "True", "Spunk_Drip2",
            ),

        (0,0), ConditionSwitch(
            #skin behind hose layer
            "WandaX.Hose == 'stockings and garterbelt'", "images/WandaSex/Wanda_Sex_UnderLegs.png",
            "WandaX.Hose == 'garterbelt'", "images/WandaSex/Wanda_Sex_UnderLegs.png",
            "WandaX.Panties and WandaX.PantiesDown", Null(),
            "WandaX.Hose == 'pantyhose'", "images/WandaSex/Wanda_Sex_UnderLegs.png",
            "WandaX.Hose == 'ripped pantyhose'", "images/WandaSex/Wanda_Sex_UnderLegs.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs
#            "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/WandaSex/Wanda_Sex_FBase.png",
#            "Player.Sprite and Player.Cock == 'in' and Speed", "images/WandaSex/Wanda_Sex_FBase.png",
#            "Player.Sprite and Player.Cock == 'in' and Speed", "Wanda_Sex_Heading_Pussy",
#            "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/WandaSex/[WandaX.skin_image.skin_path]Wanda_Sex_Ass.png",
#            "Trigger == 'lick pussy'", "images/WandaSex/[WandaX.skin_image.skin_path]Wanda_Sex_Ass.png",
            "True", "images/WandaSex/[WandaX.skin_image.skin_path]Wanda_Sex_Ass.png",
            ),

        (0,0), ConditionSwitch(
            #ass red
            "WandaX.Red", "images/WandaSex/Wanda_Sex_Red.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            "Player.Sprite and Player.Cock == 'anal'", "images/WandaSex/Wanda_Sex_Anus_Cover.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #Wet look
            "not WandaX.Water", Null(),
            "True", "images/WandaSex/Wanda_Sex_Water_Legs.png",
            ),

        (0,0), "Wanda_Sex_Anus",
            #Anus Composite

        (0,0), "Wanda_Sex_Pussy",
            #Pussy Composite


        (0,0), ConditionSwitch(
            #hose layer
            "WandaX.Hose == 'stockings and garterbelt'", Recolor("Wanda", "Hose", "images/WandaSex/Wanda_Sex_Hose_StockingsGarter.png"),
            "WandaX.Hose == 'socks'", Recolor("Wanda", "Hose", "images/WandaSex/Wanda_Sex_Hose_Socks.png"),
            "WandaX.Hose == 'garterbelt'", Recolor("Wanda", "Hose", "images/WandaSex/Wanda_Sex_Hose_Garter.png"),
            "WandaX.Hose == 'stockings'", Recolor("Wanda", "Hose", "images/WandaSex/Wanda_Sex_Hose_Stockings.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Panties if up
            "WandaX.PantiesDown", ConditionSwitch(
                    #If she has panties down. . .
                    "WandaX.Panties == 'lace panties'", Recolor("Wanda", "Panties", "images/WandaSex/Wanda_Sex_Panties_Lace_Down.png"),
                    "WandaX.Panties == 'bikini bottoms'", Recolor("Wanda", "Panties", "images/WandaSex/Wanda_Sex_Panties_Bikini_Down.png"),
                    "WandaX.Panties", Recolor("Wanda", "Panties", "images/WandaSex/Wanda_Sex_Panties_Gray_Down.png"),
                    "True", Null(),
                    ),
            "WandaX.Panties == 'lace panties'", Recolor("Wanda", "Panties", "images/WandaSex/Wanda_Sex_Panties_Lace.png"),
            "WandaX.Panties == 'bikini bottoms'", Recolor("Wanda", "Panties", "images/WandaSex/Wanda_Sex_Panties_Bikini.png"),
            "WandaX.Panties and WandaX.Wet", Recolor("Wanda", "Panties", "images/WandaSex/Wanda_Sex_Panties_Gray_Wet.png"),
            "WandaX.Panties", Recolor("Wanda", "Panties", "images/WandaSex/Wanda_Sex_Panties_Gray.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pantyhose layer
            "WandaX.Panties and WandaX.PantiesDown", Null(),
#            "WandaX.Hose == 'tights'", "images/WandaSex/Wanda_Sex_Hose_Tights.png",
#            "WandaX.Hose == 'ripped tights'", "images/WandaSex/Wanda_Sex_Hose_Tights_Holed.png",
            "WandaX.Hose == 'pantyhose'", Recolor("Wanda", "Hose", "images/WandaSex/Wanda_Sex_Hose_Pantyhose.png"),
            "WandaX.Hose == 'ripped pantyhose'", Recolor("Wanda", "Hose", "images/WandaSex/Wanda_Sex_Hose_Pantyhose_Holed.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs Layer
            "WandaX.Legs == 'skirt'", "images/WandaSex/Wanda_Sex_Legs_Skirt.png",
            "WandaX.Legs == 'dress'", Recolor("Wanda", "Legs", "images/WandaSex/Wanda_Sex_Legs_Dress.png"),
            "WandaX.Legs == 'pants' and WandaX.Upskirt", Recolor("Wanda", "Legs", "images/WandaSex/Wanda_Sex_Legs_Pants_Down.png"),
            "WandaX.Legs == 'pants' and WandaX.Wet > 1", Recolor("Wanda", "Legs", "images/WandaSex/Wanda_Sex_Legs_Pants_Wet.png"),
            "WandaX.Legs == 'pants'", Recolor("Wanda", "Legs", "images/WandaSex/Wanda_Sex_Legs_Pants.png"),
            "WandaX.Legs == 'shorts' and WandaX.Upskirt", Recolor("Wanda", "Legs", "images/WandaSex/Wanda_Sex_Legs_Shorts_Down.png"),
            "WandaX.Legs == 'shorts' and WandaX.Wet > 1", Recolor("Wanda", "Legs", "images/WandaSex/Wanda_Sex_Legs_Shorts_Wet.png"),
            "WandaX.Legs == 'shorts'", Recolor("Wanda", "Legs", "images/WandaSex/Wanda_Sex_Legs_Shorts.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Piercings
            "not WandaX.Pierce", Null(),
            "WandaX.Legs == 'dress' or WandaX.Legs == 'skirt'", Null(),
            "Player.Sprite and Player.Cock == 'in' and Speed", Null(),
            "WandaX.Pierce == 'ring'",ConditionSwitch(
                    "WandaX.Legs == 'pants' and not WandaX.Upskirt", "images/WandaSex/Wanda_Sex_Pierce_R_Black.png",
                    "WandaX.Legs == 'shorts' and not WandaX.Upskirt", "images/WandaSex/Wanda_Sex_Pierce_R_Black.png",

                    "WandaX.PantiesDown", Null(), #"images/WandaSex/Wanda_Sex_Pierce_Pussy_R.png",
                    "WandaX.Panties == 'bikini bottoms'", "images/WandaSex/Wanda_Sex_Pierce_R_Red.png",
                    "WandaX.Hose == 'pantyhose'", "images/WandaSex/Wanda_Sex_Pierce_R_Lace.png",
                    "WandaX.Panties == 'lace panties'", "images/WandaSex/Wanda_Sex_Pierce_R_Lace.png",
                    "WandaX.Panties", "images/WandaSex/Wanda_Sex_Pierce_R_Gray.png",
                    "True", Null(), #"images/WandaSex/Wanda_Sex_Pierce_R.png",
                    ),
            #else, it's barbell
            "WandaX.Legs == 'pants' and not WandaX.Upskirt", "images/WandaSex/Wanda_Sex_Pierce_B_Black.png",
            "WandaX.Legs == 'shorts' and not WandaX.Upskirt", "images/WandaSex/Wanda_Sex_Pierce_B_Black.png",

            "WandaX.PantiesDown", Null(), #"images/WandaSex/Wanda_Sex_Pierce_B.png",
            "WandaX.Panties == 'bikini bottoms'", "images/WandaSex/Wanda_Sex_Pierce_B_Red.png",
            "WandaX.Hose == 'pantyhose'", "images/WandaSex/Wanda_Sex_Pierce_B_Lace.png",
            "WandaX.Panties == 'lace panties'", "images/WandaSex/Wanda_Sex_Pierce_B_Lace.png",
            "WandaX.Panties", "images/WandaSex/Wanda_Sex_Pierce_B_Gray.png",
            "True", Null(), #"images/WandaSex/Wanda_Sex_Pierce_B.png",
            ),
        (0,0), ConditionSwitch(
            #towel Layer
            "WandaX.Over == 'towel'", Recolor("Wanda", "Over", "images/WandaSex/Wanda_Sex_Legs_Towel.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk
            "'feet' in WandaX.Spunk and Player.Male", "images/WandaSex/Wanda_Sex_Spunk_Foot2.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer
#            "not Player.Sprite or Player.Cock != 'out'", Null(),
#            "Speed >= 2", "Wanda_Hotdog_Zero_Anim2",
#            "Speed", "Wanda_Hotdog_Zero_Anim1",
#            "True", "Wanda_Hotdog_Zero_Anim0",
#            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy'", "Wanda_Sex_Lick_Pussy",
            "Trigger == 'lick ass'", "Wanda_Sex_Lick_Ass",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy fondling animation
            "Trigger3 == 'fondle pussy' and WandaX.Lust > 60 and not (Player.Sprite)",  At("WandaFingerHand", GirlFingerPussyX()), #"Wanda_Sex_Mast2",
            "Trigger3 == 'fondle pussy'", At("WandaMastHand", GirlGropePussyX()), #"Wanda_Sex_Mast",
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Wanda_Sex_Fondle_Pussy",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Footjob overlay
            "Player.Cock == 'foot'", Null(),
#            "renpy.showing('Anal_Plug_In_Sex') or renpy.showing('Anal_Plug_Out_Sex')",AlphaMask("Wanda_Sex_Feet", "images/WandaSex/Wanda_Sex_Feet_Mask.png"),
#            "ShowFeet", "Wanda_Sex_Feet",
#            "Player.Sprite", AlphaMask("Wanda_Sex_Feet", "images/WandaSex/Wanda_Sex_Feet_Mask.png"),
#            "Trigger == 'lick pussy'", AlphaMask("Wanda_Sex_Feet", "images/WandaSex/Wanda_Sex_Feet_Mask.png"),
#            "Trigger == 'lick ass'", AlphaMask("Wanda_Sex_Feet", "images/WandaSex/Wanda_Sex_Feet_Mask.png"),
            "True", "Wanda_Sex_Foot",
#            "True", AlphaMask("Wanda_Sex_Feet", "images/WandaSex/Wanda_Sex_Feet_Mask.png"),
            ),

#        (0,0), ConditionSwitch(                                                                                 #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
#            "not Speed", "Wanda_Sex_Feet",
#            "Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Wanda_Sex_Feet", "images/WandaSex/Wanda_Sex_FeetMask.png"),
#            "True", "Wanda_Sex_Feet",
#            ),
        )
# End Wanda Sex Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Wanda_Sex_Foot:
    LiveComposite(
        #the lower legs used in the sex pose, referenced by Wanda_Sex_Legs
        (1120,840),
#        (0,0), "images/WandaSex/Wanda_Sex_Feet.png",                                                         #Legs Base

        (0,0), ConditionSwitch(
            #hose layer
            "(WandaX.Hose == 'pantyhose' or WandaX.Hose == 'ripped pantyhose') and WandaX.Panties and WandaX.PantiesDown", "images/WandaSex/[WandaX.skin_image.skin_path]Wanda_Sex_Foot.png",
            "WandaX.Hose == 'socks'", Recolor("Wanda", "Hose", "images/WandaSex/Wanda_Sex_Foot_Socks.png"),
            "WandaX.Hose == 'pantyhose' or WandaX.Hose == 'ripped pantyhose'", Recolor("Wanda", "Hose", "images/WandaSex/[WandaX.skin_image.skin_path]Wanda_Sex_Foot_Pantyhose.png"),
            "WandaX.Hose and WandaX.Hose != 'garterbelt'", Recolor("Wanda", "Hose", "images/WandaSex/Wanda_Sex_Foot_Stockings.png"),
            "True", "images/WandaSex/[WandaX.skin_image.skin_path]Wanda_Sex_Foot.png",   #Null(),
            ),

        (0,0), ConditionSwitch(
            #Wet look
            "not WandaX.Water", Null(),
            "True", "images/WandaSex/Wanda_Sex_Water_Foot.png",
            ),
        (0,0), ConditionSwitch(
            #spunk
            "'feet' in WandaX.Spunk and Player.Male", "images/WandaSex/Wanda_Sex_Spunk_Foot.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pants layer
            "WandaX.Legs == 'pants' and not WandaX.Upskirt", Recolor("Wanda", "Hose", "images/WandaSex/Wanda_Sex_Foot_Pants.png"),
            "True", Null(),   #Null(),
            ),
        )

image Wanda_Sex_Foot_Over:
        #this is the foot part that goes over the cock in the fj pose
        contains:
            AlphaMask("Wanda_Sex_Foot", "images/WandaSex/Wanda_Sex_Foot_Mask.png")
#        contains:
#            ConditionSwitch(
#                "'feet' in WandaX.Spunk and Player.Male", "images/WandaSex/Wanda_Sex_Spunk_Foot.png",
#                "True", Null(),
#                )

# Start Wanda Sex Pose Pussy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Wanda_Sex_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).

    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/WandaSex/Wanda_Sex_Pussy_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and Speed", "Wanda_Sex_Heading_Pussy",
                "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'out')", "images/WandaSex/Wanda_Sex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/WandaSex/Wanda_Sex_Pussy_Open.png",
                "Trigger3 == 'fondle pussy' and WandaX.Lust > 60", "images/WandaSex/Wanda_Sex_Pussy_Open.png",
                "True", "images/WandaSex/Wanda_Sex_Pussy_Closed.png",
                )
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "not WandaX.Wet", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/KittySex/Kitty_Sex_WetPussy_F.png",
                "True", "images/DoreenSex/Doreen_Sex_Wet.png",
                )
    contains:
            # pubes
            ConditionSwitch(
                "not WandaX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", Recolor("Wanda", "Pubes", "images/WandaSex/Wanda_Sex_Pubes_Fucking.png"),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 1", Recolor("Wanda", "Pubes", "images/WandaSex/Wanda_Sex_Pubes_Fucking.png"),
#                "Player.Sprite and Player.Cock == 'in'", "images/WandaSex/Wanda_Sex_Pubes_Open.png",
#                "Player.Sprite and Player.Cock == 'out'", "images/WandaSex/Wanda_Sex_Pubes_Open.png",
#                "Trigger == 'lick pussy'", "images/WandaSex/Wanda_Sex_Pubes_Open.png",
#                "Trigger3 == 'fondle pussy' and WandaX.Lust > 60", "images/WandaSex/Wanda_Sex_Pubes_Open.png",
                "True", Recolor("Wanda", "Pubes", "images/WandaSex/Wanda_Sex_Pubes_Closed.png"),
                )
    contains:
            #Spunk
            ConditionSwitch(
                "'in' not in WandaX.Spunk or not Player.Male", Null(),
                "(WandaX.Legs == 'pants' or WandaX.Legs == 'shorts') and not WandaX.Upskirt", Null(),
                "WandaX.Panties and not WandaX.PantiesDown", Null(),
                "True", AlphaMask("Spunk_Drip2","Wanda_Sex_Drip_Mask"),
                )
            offset (545,540)

    contains:
            ConditionSwitch(
                #Outside Spunk
                "'in' in WandaX.Spunk and Player.Sprite and Player.Cock == 'in' and Speed and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_PussyF.png",
                "'in' in WandaX.Spunk and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Pussy.png",
                "True", Null(),
                )
#    contains:
#            #Spunk under penis
#            ConditionSwitch(
#                "'in' in WandaX.Spunk", "images/WandaSex/Wanda_Sex_Spunk_Puss_Under.png",
#                "True", Null(),
#                )
#    contains:
#            #hose layer
#            ConditionSwitch(
#                "WandaX.Panties and WandaX.PantiesDown", Null(),
#                "WandaX.Hose == 'ripped pantyhose' and ShowFeet", Recolor("Wanda", "Hose", "images/WandaSex/Wanda_Sex_Hose_Pantyhose_Holed.png"),
#                "WandaX.Hose == 'ripped pantyhose'", Recolor("Wanda", "Hose", "images/WandaSex/Wanda_Sex_Hose_Pantyhose_Holed.png"),
#                "True", Null(),
#                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            ConditionSwitch(
#                "not Player.Sprite", Null(),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 3", AlphaMask("Wanda_Sex_Fucking_Zero_Anim3", "Wanda_Sex_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", AlphaMask("Wanda_Sex_Fucking_Zero_Anim2", "Wanda_Sex_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and Speed == 1", AlphaMask("Wanda_Sex_Fucking_Zero_Anim1", "Wanda_Sex_Heading_Mask"),
                "Player.Sprite and Player.Cock == 'in'", "Wanda_Sex_Fucking_Zero_Anim0",
                "True", Null(),
                )
    contains:
            #Piercings
            ConditionSwitch(
#                "WandaX.Pierce == 'barbell' and Player.Sprite and Player.Cock == 'in' and Speed", "images/WandaSex/Wanda_Sex_Pierce_Pussy_BarbellF.png",
                "WandaX.Pierce == 'ring' and Player.Sprite and Player.Cock == 'in' and Speed", "images/WandaSex/Wanda_Sex_Pierce_R_Fucking.png",
                "WandaX.Pierce == 'barbell'", "images/WandaSex/Wanda_Sex_Pierce_B.png",
                "WandaX.Pierce == 'ring'", "images/WandaSex/Wanda_Sex_Pierce_R.png",
                "True", Null(),
                )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and Speed == 1", "Wanda_Pussy_Spunk_Heading",
                "True", Null(),
                )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "Speed == 1", Null(),
                "'in' not in WandaX.Spunk or not Player.Sprite or Player.Cock != 'in' or not Speed or not Player.Male", Null(),
#                "Speed <= 1", Null(), #"Wanda_Pussy_Spunk_Heading",
                "True", "Wanda_Sex_Spunk",
                )

    #End Wanda Pussy composite


image Wanda_Sex_Drip_Mask:
    #This is the mask for her drip pattern
    contains:
        "images/JubesSex/Jubes_Sex_Mask_Anal.png"
        offset (-545,-450)#(-275,-560)#(-145,-560)#(-225,-560)

image Wanda_Sex_Lick_Pussy:
        "Lick_Anim"
        zoom 0.7
        offset (535,500)#(505,680)

image Wanda_Sex_Lick_Ass:
        "Lick_Anim"
        zoom 0.7
        offset (535,580)#(535,550)

image Wanda_Sex_Fondle_Pussy:
        "GropePussy_Wanda"
        xzoom -1.2
        yzoom 1.2
        offset(-530,-150) #(-710,-450)
#        block:
#            ease 1 offset(-1000,0) #(535,500)
#            ease 1 offset(-1000,-1000) #(535,500)
#            ease 1 offset(0,-1000) #(535,500)
#            ease 1 offset(0,0) #(535,500)
#            repeat

image Wanda_Sex_Spunk:
    #This is the mask for her drip pattern
    contains:
        "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
        anchor (0.5,0)
        transform_anchor True
        xoffset 560
        yoffset 3
        xzoom .9

#End Animations for Wanda's Pussy during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_Sex_Zero_Cock:
        #this is the cock generally used by Wanda's sex pose
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

image Wanda_Sex_Fucking_Mask:
        #This is the mask image for Kitty's wide open pussy
        # Used in "Wanda_Sex_Speed2" and "Wanda_Sex_Speed3"
        contains:
            "images/JubesSex/Jubes_Sex_Mask_Fucking.png"
            yoffset 3

# Start Wanda Sex Pose Static / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_Sex_Static:
    # Pose for Wanda's Sex Pose in which she is static
    contains:
            #Wanda's underlying body
            subpixel True
            "Wanda_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
#                pause 0.3
                ease 1.5 ypos -185 #-120
                pause .3
                ease 1.45 ypos -180 #-130
                pause 0.25
                repeat
    contains:
            #Wanda's Legs
            subpixel True
            "Wanda_Sex_Legs"
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
            "Wanda_Sex_Zero_Cock"
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
#            Wanda's Feet
#            subpixel True
#            "Wanda_Sex_Feet"
#            ConditionSwitch(
#                #Footjob overlay
#                "ShowFeet", AlphaMask("Wanda_Sex_Feet", "images/WandaSex/Wanda_Sex_Feet_Mask.png"),
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

# End Wanda Sex Pose Speed Static / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Wanda Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Wanda Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_Sex_Fucking_Speed0:
    # Pose for Wanda's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Wanda's underlying body
            subpixel True
            "Wanda_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                ease 2 ypos -160 #0
                pause 0.8
                ease 2 ypos -180 #-130
                pause 0.2
                repeat
    contains:
            #Wanda's Legs
            subpixel True
            "Wanda_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -160 #0
                pause 0.8
                ease 2 ypos -180 #-130
                repeat
# End main animation for Sex Pose Fucking Speed 1


image Wanda_Sex_Fucking_Zero_Anim0:
        #this is Wanda's sex animation, Speed 1 Fucking
        contains:
            subpixel True
            "Wanda_Sex_Zero_Cock"
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

# End Wanda Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Wanda Sex Pose Speed 1 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_Sex_Fucking_Speed1:
    # Pose for Wanda's Sex Pose in which she is fucking at speed 1 (heading)
    contains:
            #Wanda's underlying body
            subpixel True
            "Wanda_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause 1
                ease 1.5 ypos -190 #0
                pause 1.6
                ease 0.9 ypos -180 #-130
                repeat
    contains:
            #Wanda's Legs
            subpixel True
            "Wanda_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause 0.7
                ease 1.5 ypos -200 #0
                pause 1.6
                ease 1.2 ypos -180 #-130
                repeat
# End main animation for Sex Pose Fucking Speed 1


image Wanda_Sex_Fucking_Zero_Anim1:
        #this is Wanda's sex animation, Speed 1 Fucking
        contains:
            subpixel True
            "Wanda_Sex_Zero_Cock"
            subpixel True
            pos (0,40)#(498,530)
            block:
                pause 0.2
#                ease 0.95 ypos -145
                ease 2 ypos -10#-10 #-140
                pause .8
                ease 2 ypos 40 #-10
                repeat

image Wanda_Sex_Heading_Mask:
        #This is the mask image for Wanda's heading pussy
        contains:
            "images/JubesSex/Jubes_Sex_Mask_Fucking.png"
            yoffset 10
            block:
                pause 0.2
                ease 1.8 yoffset 0#3
                pause 1#0.8
                ease 2 yoffset 10
                repeat


image Wanda_Sex_Heading_Pussy:
        #This is the image for Wanda's heading pussy growing
#        contains:
#            "images/WandaSex/Wanda_Sex_Pussy_Fucking_Base.png"
        contains:
            "images/WandaSex/Wanda_Sex_Pussy_Fucking.png"
            anchor (0.5,0)
            transform_anchor True
            subpixel True
            xoffset 560
            xzoom .7
            block:
                pause 0.2
                ease 1.2 xzoom 1
                ease .4 xzoom 1#.9
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
#    "images/WandaDoggy/Wanda_Doggy_Pussy_HHole.png"
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

image Wanda_Pussy_Spunk_Heading:
        #This is the image for Wanda's heading pussy cum
        contains:
            ConditionSwitch(
                "'in' in WandaX.Spunk and Player.Sprite and Player.Cock == 'in' and Speed == 1 and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
                "True", Null(),
                )
            anchor (0.5,0)
            transform_anchor True
            xoffset 560
            yoffset 5
            xzoom .7
            block:
                pause 0.7
                ease 0.7 xzoom .9
#                ease .4 xzoom .9#.9
                pause 1.8
#                ease .2 xzoom .9
                ease 1.8 xzoom .7
                repeat

# End Wanda Sex Pose Speed 1 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Wanda Sex Pose Speed 2 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_Sex_Fucking_Speed2:
    # Pose for Wanda's Sex Pose in which she is fucking at speed 2
    contains:
            #Wanda's underlying body
            subpixel True
            "Wanda_Sex_Body"
            pos (0,-170) #X less is left, Y less is up
            block: #adds to 4.2
                pause 0.5
                ease .9 ypos -190 # 0
                pause 0.8
                ease 2.0 ypos -170 # -130
                repeat
    contains:
            #Wanda's Legs
            subpixel True
            "Wanda_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 4.2
                pause 0.4
                ease 0.95 ypos -205 # 5
                ease 0.45 ypos -200 # 0
                pause 0.6
                ease 1.8 ypos -180 # -130
                repeat
# End main animation for Sex Pose Fucking Speed 2


image Wanda_Sex_Fucking_Zero_Anim2:
        #this is Wanda's sex animation, Speed 2 Fucking
        contains:
            subpixel True
            "Wanda_Sex_Zero_Cock"
            subpixel True
            pos (0,20)#(498,530)
            block:
                pause 0.2
                ease 0.95 ypos -100 # -145
                ease 0.25 ypos -90 # -140
                pause .8
                ease 2 ypos 20 #-10
                repeat

# End Wanda Sex Pose Speed 2 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Wanda Sex Pose Speed 3 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_Sex_Fucking_Speed3:
    # Pose for Wanda's Sex Pose in which she is fucking at speed 3
    contains:
            #Wanda's underlying body
            subpixel True
            "Wanda_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.5
                ease 0.4 ypos -200
                pause 0.1
#                pause 0.35
                ease 0.8 ypos -170
                repeat
    contains:
            #Wanda's Legs
            subpixel True
            "Wanda_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.4
                ease 0.45 ypos -220
                ease 0.15 ypos -210
#                pause 0.35
                ease 0.8 ypos -180
                repeat

# End main animation for Sex Pose Fucking Speed 3


image Wanda_Sex_Fucking_Zero_Anim3:
        #this is Wanda's sex animation, Speed3 Fucking
        contains:
            subpixel True
            "Wanda_Sex_Zero_Cock"
            subpixel True
            pos (0,10)
            block:
                pause 0.1
                ease 0.55 ypos -100
                ease 0.15 ypos -90
                pause 0.25
                ease 0.75 ypos 10
                repeat

# End Wanda Sex Pose Speed 3 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Animations for Wanda's Ass during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Wanda's Ass during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_Sex_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/BetsySex/Betsy_Sex_Anus.png",
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/BetsySex/Betsy_Sex_Anus.png",
            "Player.Sprite and Player.Cock == 'anal' and Speed", "Wanda_Sex_Anal_Heading",
            "Player.Sprite and Player.Cock == 'anal'", "Wanda_Sex_Anal_Tip",
            "WandaX.Plug", "images/PlugBase_Sex.png",
            "WandaX.Loose > 2", "Wanda_Gape_Anal_Sex",
#            "WandaX.Loose", "images/WandaSex/Wanda_Sex_Anus_Loose.png",
            "True", "images/WandaSex/Wanda_Sex_Anus.png",
            )
    contains:
            #Spunk under penis
            ConditionSwitch(
                "'anal' not in WandaX.Spunk or not Player.Male", Null(),
#                "Player.Sprite and Player.Cock != 'anal' and Speed >= 1", "images/WandaSex/Wanda_Sex_Spunk_Anal_Under.png",
                "Player.Sprite and Player.Cock != 'anal' and Speed == 1", "Wanda_Sex_Anal_Spunk_Heading_Under",
                "True", "images/JubesSex/Jubes_Sex_Spunk_Anal.png",
                )
            yoffset 5
    contains:
            # The animation of Zero's moving penis, masked by her anus shape
            ConditionSwitch(
                "not Player.Sprite or Player.Cock != 'anal'", Null(),
                "Speed >= 3",  AlphaMask("Wanda_Sex_Anal_Zero_Anim3", "Wanda_Sex_Anal_MaskF"),
                "Speed >= 2", AlphaMask("Wanda_Sex_Anal_Zero_Anim2", "Wanda_Sex_Anal_MaskF"),
                "Speed", AlphaMask("Wanda_Sex_Anal_Zero_Anim1", "Wanda_Sex_Anal_Mask"),
                "True", AlphaMask("Wanda_Sex_Anal_Zero_Anim0", "Wanda_Sex_Anal_Mask"),
                )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "'anal' not in WandaX.Spunk or not Player.Sprite or Player.Cock != 'anal' or not Speed or not Player.Male", Null(),
                "Speed == 1", "Wanda_Sex_Anal_Spunk_Heading_Over",
                "True", "Wanda_Sex_Anal_Spunk",
                )

image Wanda_Gape_Anal_Sex:
        #removing an anal plug
        contains:
            #Hole
            "images/JubesSex/Jubes_Sex_Anal.png"
            transform_anchor True
            subpixel True
            anchor (560,620)#(0.52,0.69)
            offset (560,625)#(218,518)
            zoom .4 # tight
            block:
                ease 3 zoom .50 #in.87
                ease 3 zoom .40 #out
                repeat

image Wanda_Sex_Anal_Spunk:
    ConditionSwitch(
                "'anal' in WandaX.Spunk and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Anal_Over.png",
                "True", Null(),
                )
    anchor (0.5,0.5)
    pos (0.5,0.5)
#    xoffset 20
    yoffset -23#68
    xzoom .9#1.2

image Wanda_Sex_Anal_Mask:
        #This is the mask image for small stuff
        # Used in "Wanda_Sex_Speed2" and "Wanda_Sex_Speed3"
        contains:
            "images/JubesSex/Jubes_Sex_Mask_Anal.png"
            yoffset 98 #-9
            xoffset 3 #3
#            xoffset -5

image Wanda_Sex_Anal_MaskF:
        #This is the mask image for deep stuff
        # Used in "Wanda_Sex_Speed2" and "Wanda_Sex_Speed3"
        contains:
            "images/JubesSex/Jubes_Sex_Mask_AnalB.png"
            yoffset 98 #-9
            xoffset 3



# Start Wanda Sex Pose Speed 0 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_Sex_Anal_Speed0:
    # Pose for Wanda's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Wanda's underlying body
            subpixel True
            "Wanda_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.5
                ease 1 ypos -185 #40
                pause 1.0
                ease 1.5 ypos -180 #90
                repeat
    contains:
            #Wanda's Legs
            subpixel True
            "Wanda_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.2
                ease 1 ypos -190 #40
                pause 1.3
                ease 1.5 ypos -180 #90
                repeat

# End main animation for Sex Pose Anal Speed 1


image Wanda_Sex_Anal_Zero_Anim0:
        #this is Wanda's sex animation, Speed 0 Anal
        contains:
            subpixel True
            "Wanda_Sex_Zero_Cock"
#            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            subpixel True
            pos (3,135)#(498,530)
            block:
                pause 0.2
                ease 2 ypos 130 #90
                pause .8
                ease 2 ypos  135 #130
                repeat

image Wanda_Sex_Anal_Tip:
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

# End Wanda Sex Pose Speed 0 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Wanda Sex Pose Speed 1 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_Sex_Anal_Heading:
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

image Wanda_Sex_Anal_Spunk_Heading_Over:
    ConditionSwitch(
                "'anal' in WandaX.Spunk and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Anal_Over.png",
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

image Wanda_Sex_Anal_Spunk_Heading_Under:
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

image Wanda_Sex_Anal_Speed1:
    # Pose for Wanda's Sex Pose in which she is fucking at speed 1 (heading)
    contains:
            #Wanda's underlying body
            subpixel True
            "Wanda_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.5
                ease 1 ypos -185 #40
                pause 1.0
                ease 1.5 ypos -180 #90
                repeat
    contains:
            #Wanda's Legs
            subpixel True
            "Wanda_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.2
                ease 1 ypos -190 #40
                pause 1.3
                ease 1.5 ypos -180 #90
                repeat

# End main animation for Sex Pose Anal Speed 1


image Wanda_Sex_Anal_Zero_Anim1:
        #this is Wanda's sex animation, Speed 1 Anal
        contains:
            subpixel True
            "Wanda_Sex_Zero_Cock"
#            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            subpixel True
            pos (3,130)#(498,530)
            block:
                pause 0.2
                ease 2 ypos 90 #40
                pause .8
                ease 2 ypos  130 #90
                repeat

# End Wanda Sex Pose Speed 1 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Wanda Sex Pose Speed 2 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_Sex_Anal_Speed2:
    # Pose for Wanda's Sex Pose in which she is doing anal at speed 2
    contains:
            #Wanda's underlying body
            subpixel True
            "Wanda_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.6
                ease 1.0 ypos -200
                pause .9
                ease 1.7 ypos -180
                repeat
    contains:
            #Wanda's Legs
            subpixel True
            "Wanda_Sex_Legs"
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
#            AlphaMask("Wanda_Sex_Fucking_Zero_Anim2", "Wanda_Sex_Fucking_Mask")
# End main animation for Sex Pose Fucking Speed 2


image Wanda_Sex_Anal_Zero_Anim2:
        #this is Wanda's sex animation, Speed 2 Fucking
        contains:
            subpixel True
            "Wanda_Sex_Zero_Cock"
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

# End Wanda Sex Pose Speed 2 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Wanda Sex Pose Speed 3 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_Sex_Anal_Speed3:
    # Pose for Wanda's Sex Pose in which she is Anal at speed 3
    contains:
            #Wanda's underlying body
            subpixel True
            "Wanda_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 1.8
#                pause 0.5
                easein .5 ypos -180
                ease .4 ypos -200
                pause .4
                ease .5 ypos -185
                repeat

    contains:
            #Wanda's Legs
            subpixel True
            "Wanda_Sex_Legs"
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


image Wanda_Sex_Anal_Zero_Anim3:
        #this is Wanda's sex animation, Speed3 Anal
        contains:
            subpixel True
            "Wanda_Sex_Zero_Cock"
            subpixel True
            pos (3,-40)
            block:
                pause 0.1
                ease 0.55 ypos -25
                ease 0.15 ypos -20
                pause 0.25
                ease 0.75 ypos 90
                repeat

# End Wanda Sex Pose Speed 3 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Wanda Sex Pose Speed 1 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_Sex_Hotdog_Speed1:
    # Pose for Wanda's Sex Pose in which she is hotdogging at speed 1 (slow)
    contains:
            #Wanda's underlying body
            subpixel True
            "Wanda_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.8
                ease 0.8 ypos -190 #-120
                pause .5
                ease 1.0 ypos -180 #-130
                pause 0.4
                repeat
    contains:
            #Wanda's Legs
            subpixel True
            "Wanda_Sex_Legs"
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
            "Wanda_Sex_Zero_Cock"
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
#            #Wanda's Feet
#            subpixel True
#            "Wanda_Sex_Feet"
##            ConditionSwitch(
##                #Footjob overlay
##                "ShowFeet", AlphaMask("Wanda_Sex_Feet", "images/WandaSex/Wanda_Sex_FeetMask.png"),
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

# End Wanda Sex Pose Speed 1 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Wanda Sex Pose Speed 2 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_Sex_Hotdog_Speed2:
    # Pose for Wanda's Sex Pose in which she is hotdogging at speed 2 (fast)
    contains:
            #Wanda's underlying body
            subpixel True
            "Wanda_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.25
                ease 0.45 ypos -195 #-120
                pause .1
                ease 0.8 ypos -180 #-130
#                pause 0.2
                repeat
    contains:
            #Wanda's Legs
            subpixel True
            "Wanda_Sex_Legs"
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
            "Wanda_Sex_Zero_Cock"
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
#            #Wanda's Feet
#            subpixel True
#            "Wanda_Sex_Feet"
##            ConditionSwitch(
##                #Footjob overlay
##                "ShowFeet", AlphaMask("Wanda_Sex_Feet", "images/WandaSex/Wanda_Sex_FeetMask.png"),
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

# End Wanda Sex Pose Speed 2 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Wanda Sex Pose Speed 0 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_Sex_FJ_Speed0:
    # Pose for Wanda's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Wanda's underlying body
            subpixel True
            "Wanda_Sex_Body"
            anchor (800,325)#(410,470)
            offset (1025,440)    #(840,390)
            transform_anchor True
            rotate 25
            pos (50,5) #(70,-60) #X less is left, Y less is up
            block: #adds to 5
                ease 2 ypos 0#-40 #-140
                pause 0.8
                ease 2 ypos 5#-60 #-180
                pause 0.2
                repeat
    contains:
            #Wanda's Legs
            subpixel True
            "Wanda_Sex_Legs"
            anchor (800,325)#(410,470)
            offset (1020,490)    #(560,390)
            transform_anchor True
            rotate 40
            pos (70,10) #(50,-220) #X less is left, Y less is up (80,0)
            block: #adds to 5
                pause 0.2
                ease 2 ypos 0 #10
                pause 0.8
                ease 2 ypos 10 #0
                repeat
    contains:
            #Wanda's Feet
            subpixel True
            "Wanda_Sex_Foot"
            anchor (800,325)#(410,470)
            offset (1020,490)    #(560,390)
            transform_anchor True
            rotate 40
            pos (70,10) #X less is left, Y less is up (200,-180)
            parallel:
                pause 0.2
                ease 2 ypos 0 #10
                pause 0.8
                ease 2 ypos 10 #0
                repeat
#            parallel:
#                pause 0.2
#                ease 2 rotate 40 #10
#                pause 0.8
#                ease 2 rotate 35 #0
#                repeat
    contains:
            subpixel True
#            "Wanda_Sex_Zero_Cock"
            "Zero_Blowcock"
            zoom .4#.5
            subpixel True
            pos (550,550) #(630,520)
            rotate -5 #0
            parallel:
                pause 0.2
                ease 2 rotate 0 #10
                pause 0.8
                ease 2 rotate -5 #0
                repeat
#    contains:
#            #Wanda's Legs
#            subpixel True
#            "Wanda_Sex_Foot_Over"
##            alpha 0.5
##            AlphaMask("Wanda_Sex_Feet", "images/WandaSex/Wanda_Sex_Feet_Mask.png")
#            pos (50,-270) #X less is left, Y less is up (80,0)
#            block: #adds to 5
##                pause 0.2
#                ease 2 ypos -290 #10
#                pause 0.8
#                ease 2 ypos -270 #0
#                pause 0.2
#                repeat

# End main animation for Sex Pose Footjob Speed 0

# End Wanda Sex Pose Speed 0 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Wanda Sex Pose Speed 1 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_Sex_FJ_Speed1:
    # Pose for Wanda's Sex Pose in which she is fucking at speed 1 (slow)
    contains:
            #Wanda's underlying body
            subpixel True
            "Wanda_Sex_Body"
            anchor (800,325)#(410,470)
            offset (845,340)    #(840,390)
            transform_anchor True
            rotate 25
            pos (50,5) #(70,-60) #X less is left, Y less is up
            block: #adds to 5
                ease 1 ypos 0#-40 #-140
                pause 0.8
                ease 1 ypos 5#-60 #-180
                pause 0.2
                repeat
    contains:
            #Wanda's Legs
            subpixel True
            "Wanda_Sex_Legs"
            anchor (800,325)#(410,470)
            offset (840,390)    #(560,330)
            transform_anchor True
            rotate 40
            pos (70,10) #(50,-220) #X less is left, Y less is up (80,0)
            block: #adds to 5
                pause 0.2
                ease 1 ypos 0 #10
                pause 0.8
                ease 1 ypos 10 #0
                repeat
    contains:
            #Wanda's Feet
            subpixel True
            "Wanda_Sex_Foot"
            anchor (800,325)#(410,470)
            offset (840,395)    #(560,330)
            transform_anchor True
            rotate 35
            pos (70,0) #X less is left, Y less is up (200,-180)
            parallel:
#                pause 0.2
                ease 1.2 rotate 50 #10
                pause 0.8
                ease 1 rotate 35 #0
                repeat
    contains:
            subpixel True
#            "Wanda_Sex_Zero_Cock"
            "Zero_Blowcock"
            zoom .4#.5
            subpixel True
            pos (550,550) #(630,520)
            rotate -5 #0
            parallel:
                pause 0.2
                ease 1 rotate -10 #10
                pause 0.8
                ease 1 rotate -5 #0
                repeat
#    contains:
#            #Wanda's Feet
#            subpixel True
#            "Wanda_Sex_Foot_Over"
#            anchor (800,325)#(410,470)
#            offset (840,395)    #(560,330)
#            transform_anchor True
#            rotate 35
#            pos (70,0) #X less is left, Y less is up (200,-180)
#            parallel:
#                pause 0.2
#                ease 1 rotate 50 #10
#                pause 0.8
#                ease 1 rotate 35 #0
#                repeat

# End main animation for Sex Pose Footjob Speed 1

# End Wanda Sex Pose Speed 1 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Wanda Sex Pose Speed 2 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_Sex_FJ_Speed2:
    # Pose for Wanda's Sex Pose in which she is fucking at speed 2 (fast)
    contains:
            #Wanda's underlying body
            subpixel True
            "Wanda_Sex_Body"
            anchor (800,325)#(410,470)
            offset (845,280)    #(840,390)
            transform_anchor True
            rotate 25
            pos (50,5) #(70,-60) #X less is left, Y less is up
            block: #adds to 5
                ease 0.5 ypos 0#-40 #-140
#                pause 0.8
                ease 0.5 ypos 5#-60 #-180
                pause 0.1
                repeat
    contains:
            #Wanda's Legs
            subpixel True
            "Wanda_Sex_Legs"
            anchor (800,325)#(410,470)
            offset (840,330)    #(560,330)
            transform_anchor True
            rotate 40
            pos (70,10) #(50,-220) #X less is left, Y less is up (80,0)
            block: #adds to 5
                pause 0.1
                ease 0.5 ypos 0 #10
#                pause 0.8
                ease 0.5 ypos 10 #0
                repeat
    contains:
            #Wanda's Feet
            subpixel True
            "Wanda_Sex_Foot"
            anchor (800,325)#(410,470)
            offset (840,345)    #(560,330)
            transform_anchor True
            rotate 35
            pos (70,0) #X less is left, Y less is up (200,-180)
            parallel:
                pause 0.1
                ease 0.5 rotate 55 #10
#                pause 0.2
                ease 0.5 rotate 45 #0
                repeat
    contains:
            subpixel True
#            "Wanda_Sex_Zero_Cock"
            "Zero_Blowcock"
            zoom .4#.5
            subpixel True
            pos (550,550) #(630,520)
            rotate -5 #0
            parallel:
                pause 0.1
                ease 0.5 rotate -10 #10
#                pause 0.2
                ease 0.5 rotate -5 #0
                repeat
    contains:
            #Wanda's Feet
            subpixel True
            "Wanda_Sex_Foot_Over"
            anchor (800,325)#(410,470)
            offset (840,345)    #(560,330)
            transform_anchor True
            rotate 35
            pos (70,0) #X less is left, Y less is up (200,-180)
            parallel:
                pause 0.1
                ease 0.5 rotate 55 #10
#                pause 0.2
                ease 0.5 rotate 45 #0
                repeat

# End main animation for Sex Pose Footjob Speed 2

# End Wanda Sex Pose Speed 2 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     Sex Launch/Reset
label Wanda_Sex_Launch(Line = Trigger):
    $ WandaX.Offhand = 0 if WandaX.Offhand == "hand" else WandaX.Offhand

###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    return
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    $ WandaX.Pose = "doggy"
#    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary

    $ Line = "solo" if not Line else Line
    if Line == "sex":
        $ Player.Sprite = 1
        $ Player.Cock = "in"
        call Cock_Occupied(WandaX,"pussy")
        if Trigger2 in ("fondle pussy","dildo pussy","lick pussy"):
                $ Trigger2 = 0
    elif Line == "anal":
        $ Player.Sprite = 1
        $ Player.Cock = "anal"
        call Cock_Occupied(WandaX,"anal")
        if Trigger2 in ("insert ass","dildo anal","lick ass"):
                $ Trigger2 = 0
    elif Line == "hotdog":
        $ Player.Sprite = 1
        if WandaX.PantsNum() == 5: #upskirts her if she's in a skirt
                $ WandaX.Upskirt = 1
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
        call Zero_Strapped(WandaX) #puts strap-on on.
    $ Trigger = Line

    if WandaX.Pose == "doggy":
            call Wanda_Doggy_Launch(Line)
            return
    if renpy.showing("Wanda_SexSprite"):
        return
    $ Speed = 0
    call Girl_Hide(WandaX,1) #call Rogue_Hide
    show Wanda_SexSprite zorder 150
    with dissolve
    return

label Wanda_Sex_Reset:
    if renpy.showing("Wanda_Doggy_Animation"):
        call Wanda_Doggy_Reset
        return
    if not renpy.showing("Wanda_SexSprite"):
        return
    $ WandaX.ArmPose = 2
    hide Wanda_SexSprite
    call Girl_Hide(WandaX) #call Rogue_Hide
#    call Set_The_Scene(Dress = 0)
    show Wanda_Sprite at SpriteLoc(WandaX.SpriteLoc) zorder WandaX.Layer:
        alpha 1 zoom 1 offset (0,0) anchor (0.5,0.0)
    with dissolve
    $ Speed = 0
    return


## End Wanda Sex Pose Content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


### End Wanda Sex Pose Content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Wanda Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Wanda BJ element ///////////////////////////////////////////////////////////////////////////                                     Core Wanda BJ element
#Wanda BJ Over Sprite Compositing


image Wanda_BJ_Animation:#                                                                #core BJ animation
    LiveComposite(
        (858,928),
        (0,0), ConditionSwitch(
            "Speed == 1", "Wanda_BJ_Anim1",               #Licking
            "Speed == 2", "Wanda_BJ_Anim2",               #Heading
            "Speed == 3", "Wanda_BJ_Anim3",               #Sucking
            "Speed == 4", "Wanda_BJ_Anim4",               #Deepthroat
            "Speed == 5", "Wanda_BJ_Anim5",               #Cumming High
            "Speed == 6", "Wanda_BJ_Anim6",               #Cumming Deep
            "Speed == 0", "Wanda_BJ_Anim0",               #Static
            ),
        )
    zoom .55
    transform_anchor True
    anchor (.5,.5)
    offset (300,0)

image Wanda_BJ_Backdrop:
    #Her Body under the head
    LiveComposite(
        (600,1250),       #550,950
        (-500,120), ConditionSwitch(      #-375,250
            #blanket
            "'blanket' in WandaX.RecentActions", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
            "True", Null(),
            ),
        (130,100), "Wanda_BJ_HairBack2", #(50,25)
        (0,0), "images/WandaSprite/[WandaX.skin_image.skin_path]Wanda_Sprite_Arm.png",
            #back arm

        (0,0), ConditionSwitch(
            #Chest layer
            "WandaX.Over == 'purple top'", "images/WandaSprite/Wanda_Sprite_Over_Purple_Back.png",
            "WandaX.Chest == 'mesh top'", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Mesh_Arm.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #armlets
            "WandaX.Arms", "images/WandaSprite/Wanda_Sprite_Armlets1.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #jacket under
            "WandaX.Acc == 'jacket'", Recolor("Wanda", "Acc", "images/WandaSprite/Wanda_Sprite_Jacket_Back.png"),         # right hand up/left down
            "True", Null(),
            ),
        (0,0), "images/WandaSprite/[WandaX.skin_image.skin_path]Wanda_Sprite_Body.png",


        (0,0), ConditionSwitch(
            #Chest layer
            "WandaX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "WandaX.Chest == 'bikini top' and (WandaX.Acc == 'jacket' or WandaX.Over == 'purple top')", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Bikini_Up_Jacket.png"),
                    "WandaX.Chest == 'bikini top'", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Bikini_Up.png"),
                    "WandaX.Chest == 'mesh top'", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Mesh_Up.png"),
#                    "WandaX.Chest == 'lace bra'", "images/WandaSprite/Wanda_Sprite_Chest_Lace_Up.png",
                    "WandaX.Chest", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Bra_Up.png"),
                    "True", Null(),
                    ),
            "WandaX.Chest == 'bikini top' and WandaX.Acc == 'jacket'", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Bikini_Jacket.png"),
            "WandaX.Chest == 'bikini top'", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Bikini.png"),
            "WandaX.Chest == 'mesh top'", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Mesh.png"),
            "WandaX.Chest == 'lace bra'", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Lace.png"),
            "WandaX.Chest", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Bra.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Water effect
##            "WandaX.Water and WandaX.ArmPose == 1", "images/WandaSprite/Wanda_Sprite_Water1.png",
            "WandaX.Water", "images/WandaSprite/Wanda_Sprite_Water.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #dress
            "not WandaX.Legs", Null(),
            "WandaX.Upskirt", ConditionSwitch(
                        #if the skirt's up or pants down
                        "WandaX.Legs == 'dress' and WandaX.Uptop", Recolor("Wanda", "Legs", "images/WandaSprite/Wanda_Sprite_Legs_Dress_Up.png"),
                        "WandaX.Legs == 'dress'", Recolor("Wanda", "Legs", "images/WandaSprite/Wanda_Sprite_Legs_Dress_Upskirt.png"),
                        "True", Null(),
                        ),
            "WandaX.Legs == 'dress' and WandaX.Uptop", Recolor("Wanda", "Legs", "images/WandaSprite/Wanda_Sprite_Legs_Dress_Uptop.png"),
            "WandaX.Legs == 'dress'", Recolor("Wanda", "Legs", "images/WandaSprite/Wanda_Sprite_Legs_Dress.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over
            "WandaX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "WandaX.Over == 'purple top'", "images/WandaSprite/Wanda_Sprite_Over_Purple_Up.png",
                    "WandaX.Over == 'corset'", Recolor("Wanda", "Over", "images/WandaSprite/Wanda_Sprite_Over_Corset_Up.png"),
                    "WandaX.Over == 'shirt'", Recolor("Wanda", "Over", "images/WandaSprite/Wanda_Sprite_Over_Shirt_Up.png"),
                    "WandaX.Over == 'towel' and WandaX.Upskirt", Recolor("Wanda", "Over", "images/WandaSprite/Wanda_Sprite_Over_Towel_Up.png"),
                    "WandaX.Over == 'towel'", Recolor("Wanda", "Over", "images/WandaSprite/Wanda_Sprite_Over_Towel_Uptop.png"),
                    "True", Null(),
                    ),
            "WandaX.Over == 'purple top'", "images/WandaSprite/Wanda_Sprite_Over_Purple.png",
            "WandaX.Over == 'corset'", Recolor("Wanda", "Over", "images/WandaSprite/Wanda_Sprite_Over_Corset.png"),
            "WandaX.Over == 'shirt'", Recolor("Wanda", "Over", "images/WandaSprite/Wanda_Sprite_Over_Shirt.png"),
            "WandaX.Over == 'towel' and WandaX.Upskirt", Recolor("Wanda", "Over", "images/WandaSprite/Wanda_Sprite_Over_Towel_Upskirt.png"),
            "WandaX.Over == 'towel'", Recolor("Wanda", "Over", "images/WandaSprite/Wanda_Sprite_Over_Towel.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #armlets
            "WandaX.Arms", "images/WandaSprite/Wanda_Sprite_Armlets2.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #jacket over
            "WandaX.Acc == 'jacket'", Recolor("Wanda", "Acc", "images/WandaSprite/Wanda_Sprite_Jacket.png"),         # right hand up/left down
            "True", Null(),
            ),


        (0,0), ConditionSwitch(
            #Chest layer over jacket
            "not WandaX.Uptop", Null(),
            "WandaX.Over == 'shirt'", Recolor("Wanda", "Over", "images/WandaSprite/Wanda_Sprite_Over_Shirt_Over.png"),
            "WandaX.Chest == 'bikini top'", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Bikini_Over.png"),
            "WandaX.Chest == 'mesh top'", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Mesh_Over.png"),
            "WandaX.Chest == 'lace bra'", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Lace_Over.png"),
            "WandaX.Chest", Recolor("Wanda", "Chest", "images/WandaSprite/Wanda_Sprite_Chest_Bra_Over.png"),
            "True", Null(),
            ),


        (0,0), ConditionSwitch(
            #Nipples
            #Only does this if she has piercings, has no tops, or has her top up
            "WandaX.Pierce == 'ring'", ConditionSwitch(
                    "WandaX.Uptop", "images/WandaSprite/Wanda_Sprite_Nips_Ring.png",

                    "WandaX.Over == 'towel'", Null(),
                    "WandaX.Over == 'purple top'", "images/WandaSprite/Wanda_Sprite_Nips_Ring_Purp.png",
                    "WandaX.Over", "images/WandaSprite/Wanda_Sprite_Nips_Ring_Red.png", #== 'shirt' or 'corset'
                    "WandaX.Legs == 'dress'", "images/WandaSprite/Wanda_Sprite_Nips_Ring_Black.png",
#                    "WandaX.Over == 'shirt'", "images/WandaSprite/Wanda_Sprite_Nips_Ring_Red.png",

                    "WandaX.Chest == 'bikini top'", "images/WandaSprite/Wanda_Sprite_Nips_Ring_Red.png",
                    "WandaX.Chest == 'mesh top'", "images/WandaSprite/Wanda_Sprite_Nips_Ring_Mesh.png",
                    "WandaX.Chest == 'lace bra'", "images/WandaSprite/Wanda_Sprite_Nips_Ring_Lace.png",
                    "WandaX.Chest", "images/WandaSprite/Wanda_Sprite_Nips_Ring_Red.png",

                    "True", "images/WandaSprite/Wanda_Sprite_Nips_Ring.png",
                    ),
            "WandaX.Pierce == 'barbell'", ConditionSwitch(
                    "WandaX.Uptop", "images/WandaSprite/Wanda_Sprite_Nips_Barbell.png",

                    "WandaX.Over == 'towel'", Null(),
                    "WandaX.Over == 'purple top'", "images/WandaSprite/Wanda_Sprite_Nips_Barbell_Purp.png",
                    "WandaX.Over", "images/WandaSprite/Wanda_Sprite_Nips_Barbell_Red.png", #== 'shirt' or 'corset'
                    "WandaX.Legs == 'dress'", "images/WandaSprite/Wanda_Sprite_Nips_Barbell_Black.png",
#                    "WandaX.Over == 'shirt'", "images/WandaSprite/Wanda_Sprite_Nips_Barbell_Red.png",

                    "WandaX.Chest == 'bikini top'", "images/WandaSprite/Wanda_Sprite_Nips_Barbell_Red.png",
                    "WandaX.Chest == 'mesh top'", "images/WandaSprite/Wanda_Sprite_Nips_Barbell_Mesh.png",
                    "WandaX.Chest == 'lace bra'", "images/WandaSprite/Wanda_Sprite_Nips_Barbell_Lace.png",
                    "WandaX.Chest", "images/WandaSprite/Wanda_Sprite_Nips_Barbell_Red.png",

                    "True", "images/WandaSprite/Wanda_Sprite_Nips_Barbell.png",
                    ),
            # if no piercings. . .

            "WandaX.Lust < 50 and not WandaX.OCount", Null(),                                                 #nips only poke at high lust
            "WandaX.Uptop", "images/WandaSprite/Wanda_Sprite_Nips.png",

            "WandaX.Over == 'towel'", Null(),
            "WandaX.Over == 'purple top'", "images/WandaSprite/Wanda_Sprite_Nips_Purp.png",               #== 'shirt' or 'corset'
            "WandaX.Over", "images/WandaSprite/Wanda_Sprite_Nips_Red.png",               #== 'shirt' or 'corset'
            "WandaX.Legs == 'dress'", "images/WandaSprite/Wanda_Sprite_Nips_Black.png",
#                    "WandaX.Over == 'shirt'", "images/WandaSprite/Wanda_Sprite_Nips_Red.png",

            "WandaX.Chest == 'bikini top'", "images/WandaSprite/Wanda_Sprite_Nips_Red.png",
            "WandaX.Chest == 'mesh top'", "images/WandaSprite/Wanda_Sprite_Nips_Mesh.png",
            "WandaX.Chest == 'lace bra'", "images/WandaSprite/Wanda_Sprite_Nips_Lace.png",
            "WandaX.Chest", "images/WandaSprite/Wanda_Sprite_Nips_Red.png",

            "True", "images/WandaSprite/Wanda_Sprite_Nips.png",

            ),

        (0,0), ConditionSwitch(
            #Necklaces
            "WandaX.Neck == 'scarf'", "images/WandaSprite/Wanda_Sprite_Neck_Scarf.png",
            "WandaX.Neck", "images/WandaSprite/Wanda_Sprite_Neck.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #belly spunk
            "'belly' in WandaX.Spunk and Player.Male", "images/WandaSprite/Wanda_Sprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast spunk
            "'tits' in WandaX.Spunk and Player.Male", "images/WandaSprite/Wanda_Sprite_Spunk_Tits.png",
            "True", Null(),
            ),
        (75,50), "Wanda_BJ_HairBack", #(50,25)
#        (30,-300), ConditionSwitch(    #(30,-300)
#            #Hair overlay
#            "WandaX.Hair == 'wetlong' or (WandaX.Hair == 'long' and WandaX.Water)", Recolor("Wanda", "Hair", "images/WandaBJFace/Wanda_BJ_Hair_Long_Wet_Under.png"),
#            "WandaX.Hair == 'long' and (not Player.Male and 'facial' in WandaX.Spunk)",Recolor("Wanda", "Hair", "images/WandaBJFace/Wanda_BJ_Hair_Long_Wet_Under.png"),

#            "WandaX.Hair == 'long'",Recolor("Wanda", "Hair", "images/WandaBJFace/Wanda_BJ_Hair_Long_Under.png"),
#            "True", Null(),
#            ),
        )
#    anchor (0.5, 0.0)
    zoom 3.2#.80
    anchor (300,525)#(300,625)
    offset (-410,-100)#(-400,0)
#    offset (230,-650)#(60,0)

image Wanda_BJ_HairBack:
    LiveComposite(
        (1000,1000),
        (0,0), ConditionSwitch(
            #Hair overlay
            "WandaX.Hair == 'wetlong' or (WandaX.Hair == 'long' and WandaX.Water)", Recolor("Wanda", "Hair", "images/WandaBJFace/Wanda_BJ_Hair_Long_Wet_Under.png"),
            "WandaX.Hair == 'long' and (not Player.Male and 'facial' in WandaX.Spunk)",Recolor("Wanda", "Hair", "images/WandaBJFace/Wanda_BJ_Hair_Long_Wet_Under.png"),

            "WandaX.Hair == 'long'",Recolor("Wanda", "Hair", "images/WandaBJFace/Wanda_BJ_Hair_Long_Under.png"),
            "True", Null(),
            ),
        )
    anchor (0.5, 0.5)
    zoom .35#.40
    transform_anchor True
#    rotate -10

image Wanda_BJ_HairBack2:
    LiveComposite(
        (1000,1000),
        (0,0), ConditionSwitch(
            #Hair overlay
            "WandaX.Hair == 'wetlong' or (WandaX.Hair == 'long' and WandaX.Water)", Recolor("Wanda", "Hair", "images/WandaBJFace/Wanda_BJ_Hair_Long_Wet_Under.png"),
            "WandaX.Hair == 'long' and (not Player.Male and 'facial' in WandaX.Spunk)",Recolor("Wanda", "Hair", "images/WandaBJFace/Wanda_BJ_Hair_Long_Wet_Under.png"),

            "WandaX.Hair == 'long'",Recolor("Wanda", "Hair", "images/WandaBJFace/Wanda_BJ_Hair_Long_Under.png"),
            "True", Null(),
            ),
        )
    anchor (0.5, 0.5)
    zoom .25#.40
    transform_anchor True
#    rotate -10

image Wanda_BJ_Head:                                                                            #These are all the details of the face
    LiveComposite(
        (858,928),
#        (0,0), ConditionSwitch(
#            #Hair back
#            "WandaX.Water or WandaX.Hair == 'wet'", "images/WandaBJFace/Wanda_BJ_HairBackWet.png", #AlphaMask("images/WandaBJFace/Wanda_BJ_HairBackWet.png", "Wanda_BJ_Backdrop"),
#            "not Player.Male and 'facial' in WandaX.Spunk","images/WandaBJFace/Wanda_BJ_HairBackWet.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #scarf
            "WandaX.Neck == 'scarf' and renpy.showing('Wanda_TJ_Animation')", "images/WandaBJFace/Wanda_BJ_Scarf.png",
            "True",Null(),
            ),
        (0,0), ConditionSwitch(
            # Basic Face layer
            "WandaX.Blush > 1", "images/WandaBJFace/[WandaX.skin_image.skin_path]Wanda_BJ_Head_Blush2.png",
            "WandaX.Blush", "images/WandaBJFace/[WandaX.skin_image.skin_path]Wanda_BJ_Head_Blush1.png",
            "True",  "images/WandaBJFace/[WandaX.skin_image.skin_path]Wanda_BJ_Head.png"
            ),
        (0,0), ConditionSwitch(
            #chin spunk
            "Player.Male and 'chin'  in WandaX.Spunk", "images/WandaBJFace/Wanda_BJ_Spunk_Chin.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Mouth
            "Speed and renpy.showing('Wanda_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
                    "Speed == 1", "images/WandaBJFace/Wanda_BJ_Mouth_Tongue.png",  #licking
                    "(Speed == 2 or Speed == 5)", Null(),#"Wanda_BJ_MouthHeadingB",#Null(),                          #heading
                    "Speed == 3", "images/WandaBJFace/Wanda_BJ_Mouth_Sucking.png", #sucking
                    "Speed == 4", "images/WandaBJFace/Wanda_BJ_Mouth_Sucking.png", #deepthroat
                    "Speed == 6", "images/WandaBJFace/Wanda_BJ_Mouth_Sucking.png", #cumming
                    "True", "images/WandaBJFace/Wanda_BJ_Mouth_Sucking.png", #cumming
                    ),
            "renpy.showing('Wanda_CUN_Animation') and Speed", "images/WandaBJFace/Wanda_BJ_Mouth_Tongue.png",
            "Speed == 3 and renpy.showing('Wanda_TJ_Animation')", "images/WandaBJFace/Wanda_BJ_Mouth_Tongue.png",
            "Speed >= 5 and renpy.showing('Wanda_TJ_Animation')", "images/WandaBJFace/Wanda_BJ_Mouth_Tongue.png",
#            "WandaX.Mouth == 'normal'", "images/WandaBJFace/Wanda_BJ_Mouth_Smile.png",
            "WandaX.Mouth == 'lipbite'", "images/WandaBJFace/Wanda_BJ_Mouth_Lipbite.png",
            "WandaX.Mouth == 'sucking'", "images/WandaBJFace/Wanda_BJ_Mouth_Heading.png",
            "WandaX.Mouth == 'kiss'", "images/WandaBJFace/Wanda_BJ_Mouth_Kiss.png",
            "WandaX.Mouth == 'sad'", "images/WandaBJFace/Wanda_BJ_Mouth_Sad.png",
#            "WandaX.Mouth == 'smile'", "images/WandaBJFace/Wanda_BJ_Mouth_Smile.png",
#            "WandaX.Mouth == 'grimace'", "images/WandaBJFace/Wanda_BJ_Mouth_Smile.png",
            "WandaX.Mouth == 'surprised'", "images/WandaBJFace/Wanda_BJ_Mouth_Heading.png",
            "WandaX.Mouth == 'tongue'", "images/WandaBJFace/Wanda_BJ_Mouth_Tongue.png",
            "True", "images/WandaBJFace/Wanda_BJ_Mouth_Normal.png",
            ),
        (425,530), ConditionSwitch(  #(428,555)
            # Heading Mouth
            "not renpy.showing('Wanda_BJ_Animation')", Null(),
            "Speed == 2", "Wanda_BJ_MouthHeading",  #heading
            "Speed == 5", "Wanda_BJ_MouthHigh", #cumming high
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #wet face
            "Player.Male", Null(),
            "'mouth' not in WandaX.Spunk and 'chin' not in WandaX.Spunk", Null(),
            "'chin' not in WandaX.Spunk and (WandaX.Mouth == 'tongue' or Speed)", "images/WandaBJFace/Wanda_BJ_Wet_Tongue.png",
            "WandaX.Mouth == 'tongue' or Speed", "images/WandaBJFace/Wanda_BJ_Wet_Tongue2.png",
            "'mouth' in WandaX.Spunk or 'chin' in WandaX.Spunk", "images/WandaBJFace/Wanda_BJ_Wet_Mouth.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Spunk layer
            "'mouth' not in WandaX.Spunk or not Player.Male", Null(),
            "Speed and renpy.showing('Wanda_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
                    "Speed == 1", "images/WandaBJFace/Wanda_BJ_Spunk_Tongue.png",  #licking
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", "images/WandaBJFace/Wanda_BJ_Spunk_Sucking_O.png", #sucking
                    "Speed == 4", "images/WandaBJFace/Wanda_BJ_Spunk_Sucking_O.png", #deepthroat
                    "Speed == 6", "images/WandaBJFace/Wanda_BJ_Spunk_Sucking_O.png", #cumming
                    "True", "images/WandaBJFace/Wanda_BJ_Spunk_Tongue.png", #cumming
                    ),
            "(Speed == 3 or Speed >= 5) and renpy.showing('Wanda_TJ_Animation')", "images/WandaBJFace/Wanda_BJ_Spunk_Tongue.png",
#            "WandaX.Mouth == 'normal'", "images/WandaBJFace/Wanda_BJ_Spunk_Smile.png",
#            "WandaX.Mouth == 'lipbite'", "images/WandaBJFace/Wanda_BJ_Spunk_Lipbite.png",
#            "WandaX.Mouth == 'kiss'", "images/WandaBJFace/Wanda_BJ_Spunk_Kiss.png",
#            "WandaX.Mouth == 'sad'", "images/WandaBJFace/Wanda_BJ_Spunk_Kiss.png",
#            "WandaX.Mouth == 'smile'", "images/WandaBJFace/Wanda_BJ_Spunk_Smile.png",
            "WandaX.Mouth == 'surprised'", "images/WandaBJFace/Wanda_BJ_Spunk_Tongue.png",
            "WandaX.Mouth == 'tongue'", "images/WandaBJFace/Wanda_BJ_Spunk_Tongue.png",
            "WandaX.Mouth == 'sucking'", "images/WandaBJFace/Wanda_BJ_Spunk_Tongue.png", #fix add
            "True", "images/WandaBJFace/Wanda_BJ_Spunk_Mouth.png",
            ),
        (0,0), ConditionSwitch(
            #Brows
            "WandaX.Brows == 'normal'", "images/WandaBJFace/[WandaX.skin_image.skin_path]Wanda_BJ_Brows_Normal.png",
            "WandaX.Brows == 'angry'", "images/WandaBJFace/[WandaX.skin_image.skin_path]Wanda_BJ_Brows_Angry.png",
            "WandaX.Brows == 'sad'", "images/WandaBJFace/[WandaX.skin_image.skin_path]Wanda_BJ_Brows_Sad.png",
            "WandaX.Brows == 'surprised'", "images/WandaBJFace/[WandaX.skin_image.skin_path]Wanda_BJ_Brows_Surprised.png",
            "WandaX.Brows == 'confused'", "images/WandaBJFace/[WandaX.skin_image.skin_path]Wanda_BJ_Brows_Confused.png",
            "True", "images/WandaBJFace/[WandaX.skin_image.skin_path]Wanda_BJ_Brows_Normal.png",
            ),
        (0,0), "Wanda BJ Blink",
            #Eyes
        (0,0), ConditionSwitch(
            #cum on the face
            "'facial' in WandaX.Spunk and Player.Male", "images/WandaBJFace/Wanda_BJ_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hair overlay
            "WandaX.Hair == 'wetlong' or (WandaX.Hair == 'long' and WandaX.Water)", Recolor("Wanda", "Hair", "images/WandaBJFace/Wanda_BJ_Hair_Long_Wet_Over.png"),
            "WandaX.Hair == 'long' and (not Player.Male and 'facial' in WandaX.Spunk)",Recolor("Wanda", "Hair", "images/WandaBJFace/Wanda_BJ_Hair_Long_Wet_Over.png"),

            "WandaX.Water or WandaX.Hair == 'wet'", Recolor("Wanda", "Hair", "images/WandaBJFace/Wanda_BJ_Hair_Wet.png"),
            "not Player.Male and 'facial' in WandaX.Spunk",Recolor("Wanda", "Hair", "images/WandaBJFace/Wanda_BJ_Hair_Wet.png"),

            "WandaX.Hair == 'long'", Recolor("Wanda", "Hair", "images/WandaBJFace/Wanda_BJ_Hair_Long_Over.png"),
            "True", Recolor("Wanda", "Hair", "images/WandaBJFace/Wanda_BJ_Hair_Short.png"),
            ),
        (0,0), ConditionSwitch(
            #hairband
            "not WandaX.Hat",Null(),
            "True", "images/WandaBJFace/Wanda_BJ_Headband.png",
            ),
        (0,0), ConditionSwitch(
            #Hair water overlay
            "not WandaX.Water and not (not Player.Male and 'facial' in WandaX.Spunk)", Null(),
            "True", "images/WandaBJFace/Wanda_BJ_Water.png",
            ),
        (0,0), ConditionSwitch(
            #cum on the hair
            "'hair' in WandaX.Spunk and Player.Male", "images/WandaBJFace/Wanda_BJ_Spunk_Hair.png",
            "True", Null(),
            ),
        )
    zoom 1.1
    anchor (0.5, 0.5)
#end image Wanda_BJ_Head:

image Wanda BJ Blink:
        #eyeblinks
        ConditionSwitch(
            "WandaX.Eyes == 'normal'", "images/WandaBJFace/Wanda_BJ_Eyes_Normal.png",
            "WandaX.Eyes == 'sexy'", "images/WandaBJFace/Wanda_BJ_Eyes_Sexy.png",
            "WandaX.Eyes == 'closed'", "images/WandaBJFace/Wanda_BJ_Eyes_Closed.png",
            "WandaX.Eyes == 'surprised'", "images/WandaBJFace/Wanda_BJ_Eyes_Surprised.png",
            "WandaX.Eyes == 'side'", "images/WandaBJFace/Wanda_BJ_Eyes_Side.png",
            "WandaX.Eyes == 'leftside'", "images/WandaBJFace/Wanda_BJ_Eyes_Leftside.png",
            "WandaX.Eyes == 'stunned'", "images/WandaBJFace/Wanda_BJ_Eyes_Stunned.png",
            "WandaX.Eyes == 'down'", "images/WandaBJFace/Wanda_BJ_Eyes_Down.png",
            "WandaX.Eyes == 'manic'", "images/WandaBJFace/Wanda_BJ_Eyes_Surprised.png",
            "WandaX.Eyes == 'squint'", "images/WandaBJFace/Wanda_BJ_Eyes_Sexy.png",
            "True", "images/WandaBJFace/Wanda_BJ_Eyes_Normal.png",
            ),
        choice:
            3.5
        choice:
            3.25
        choice:
            3
        "images/WandaBJFace/Wanda_BJ_Eyes_Closed.png"
        .25
        repeat
#end image Wanda BJ Blink:

image Wanda_BJ_MouthHeadingB:
    #the mouth used for the heading animations
    contains:
        "images/WandaBJFace/Wanda_BJ_Mouth_Heading.png"
        alpha .5
# end image Wanda_BJ_MouthHeading:

image Wanda_BJ_MouthSuckingMask:
    #the mask used for sucking animations, Wanda_BJ_Anim3, Wanda_BJ_Anim4, Wanda_BJ_Anim6
    contains:
        "images/WandaBJFace/Wanda_BJ_Mask_Sucking.png"
#    contains:
#        ConditionSwitch(
#            "'mouth' not in WandaX.Spunk or not Player.Male", Null(),
#            "Speed != 2 and Speed != 5", Null(),
#            "True", "images/WandaBJFace/Wanda_BJ_Spunk_SuckingU.png",
#            )
    zoom 1.1

image Wanda_BJ_SpunkSucking:
    #the mouth used for the sucking animations
    contains:
        ConditionSwitch(
            "'mouth' in WandaX.Spunk", "images/WandaBJFace/Wanda_BJ_Spunk_Sucking_O.png",
            "True", Null(),
            )
        zoom 1.1
        anchor (0.5, 0.5)
        offset (75,40)


#Head and Body Animations for Wanda's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
#Head and Body Animations for Wanda's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_BJ_Anim0:
    #Animation for Wanda BJ static (Speed 0)
    contains:
            # Wanda's body, everything below the chin (Speed 0)
            "Wanda_BJ_Backdrop"
            subpixel True
            offset (0,0)
    contains:
            # Wanda's head Underlay (Speed 0)
            "Wanda_BJ_Head"
            subpixel True
            offset (0,0)
    contains:
            # Cock (Speed 0)
            "Blowcock"
            anchor (.5,.5)
            offset (305,170)
            rotate -10
#end Wanda_BJ_Anim0 Static (Speed 0)


image Wanda_BJ_Anim1:
    #Animation for Wanda BJ Licking (Speed 1)
    contains:
            # Wanda's body, everything below the chin (Speed 1)
            "Wanda_BJ_Backdrop"
            subpixel True
            transform_anchor True
            pos (0,-50)  #top
            rotate 0  #top
            parallel:
                ease 2.5 pos (0,140) #bottom (30,90)
                ease 2 pos (0,-50)  #top
                pause .5
                repeat
            parallel:
                ease 2.5 rotate -10 #bottom 25,50
                ease 2 rotate 0  #top
                pause .5
                repeat

    contains:
            # Wanda's head Underlay (Speed 1)
            "Wanda_BJ_Head"
            subpixel True
            offset (0,-35)  #top
            block:
                ease 2.5 offset (25,100) #bottom
                ease 2 offset (0,-35)  #top
                pause .5
                repeat
    contains:
            # Cock (Speed 1)
            "Blowcock"
            subpixel True
            anchor (.5,.5)
            offset (305,170)
            rotate 0
            block:
                ease 2 rotate -5 #410
                pause .5
                ease 2.5 rotate 0
                repeat
#end Wanda_BJ_Anim1 Licking (Speed 1)


image Wanda_BJ_Anim2:
    #Animation for Wanda BJ Heading (Speed 2)
    contains:
            # Wanda's body, everything below the chin (Speed 2)
            "Wanda_BJ_Backdrop"
            subpixel True
            transform_anchor True
            pos (0,0)  #top
            rotate -5  #top
            parallel:
                ease 1 pos (0,100) #bottom (30,90)
                ease 1.5 pos (0,0)  #top
                repeat
            parallel:
                ease 1 rotate -10 #bottom 25,50
                ease 1.5 rotate -5  #top
                repeat
    contains:
            # Wanda's head Underlay (Speed 2)
            "Wanda_BJ_Head"
            subpixel True
            offset (0,35)     #top
            block:
                ease 1 yoffset 90#35           #bottom
                ease 1.5 offset (0,35)     #top
                repeat
    contains:
            # Cock (Speed 2)
            "Blowcock"
            anchor (.5,.5)
            offset (305,170)
            rotate 0
    contains:
            # Her face overlay for the heading animation  (Speed 2)
            contains:
                AlphaMask("Wanda_BJ_HeadingHead", "Wanda_BJ_MaskHeadingMask")
                anchor (0.5, 0.5)
            subpixel True
            offset (0,35)     #top
            block:
                ease 1 yoffset 90#35           #bottom
                ease 1.5 offset (0,35)     #top
                repeat
    contains:
            # Her spunk for the heading animation (Speed 2)
            "Wanda_BJ_SpunkHeading"
            subpixel True
#            offset (0,-40)     #top
#            anchor (0.5, 0.5)
#            block:
#                ease 1 yoffset 35           #bottom
#                ease 1.5 offset (0,-40)     #top
#                repeat
            pos (0,77)
            offset (0,35)     #top
            block:
                ease 1 yoffset 90#35           #bottom
                ease 1.5 offset (0,35)     #top
                repeat
#end Wanda_BJ_Anim2 Heading (Speed 2)


image Wanda_BJ_MouthHeading:
    #the mouth used for the heading animations
    contains:
        "images/WandaBJFace/Wanda_BJ_Mouth_Heading.png"
        anchor (430,530)#(460,464)
        transform_anchor True
        subpixel True
        zoom .8 #0.45
        block:
            ease .6      zoom 1.1          #bottom
            ease .4      zoom 1          #bottom
            ease .4      zoom 1.1          #bottom
            ease 1.1    zoom .8     #top
            repeat
    contains:
        ConditionSwitch(
            "'mouth' in WandaX.Spunk", "images/WandaBJFace/Wanda_BJ_Spunk_Heading_U.png",
            "True", Null(),
            )
        anchor (430,530)#(460,464)
        transform_anchor True
        subpixel True
        zoom .8 #0.45
        block:
            ease .6      zoom 1.1          #bottom
            ease .4      zoom 1          #bottom
            ease .4      zoom 1.1          #bottom
            ease 1.1    zoom .8     #top
            repeat
# end image Wanda_BJ_MouthHeading:

image Wanda_BJ_MaskHeadingMask:
    #the mask used for the heading image
    contains:
        "images/WandaBJFace/Wanda_BJ_Mask_Heading.png"
        subpixel True
        transform_anchor True
        anchor (430,530)#429,464)
        offset (430,540)#(415,490)
        zoom .8 #0.70
        block:
            ease .6      zoom 1.1          #bottom
            ease .4      zoom 1          #bottom
            ease .4      zoom 1.1          #bottom
            ease 1.1    zoom .8     #top
            repeat
#end image Wanda_BJ_MaskHeadingMask:

image Wanda_BJ_HeadingHead:
    #An alt copy of her head that is alphaed by Wanda_BJ_MaskHeadingMask
    #used in Wanda_BJ_Anim2
    contains:
        "Wanda_BJ_Head"
        anchor (460,530)#429,464)
        offset (417,484)#(460,530)#(257,279)

image Wanda_BJ_SpunkHeading:
    #the mouth used for the heading animations
    contains:
        contains:
            ConditionSwitch(
                "'mouth' in WandaX.Spunk", "images/WandaBJFace/Wanda_BJ_Spunk_Heading_O.png",
                "True", Null(),
                )
        anchor (430,530)#(460,464)
        transform_anchor True
        subpixel True
        zoom .8 #0.45
        block:
            ease .6      zoom 1.1          #bottom
            ease .4      zoom 1          #bottom
            ease .4      zoom 1.1          #bottom
            ease 1.1    zoom .8     #top
            repeat
#end image Wanda_BJ_SpunkHeading:
#end Wanda_BJ_Anim2 Heading (Speed 2) Elements / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Wanda_BJ_Anim3:
    #Animation for Wanda BJ Sucking (Speed 3)
    contains:
            # Wanda's body, everything below the chin (Speed 3)
            "Wanda_BJ_Backdrop"
            subpixel True
            transform_anchor True
            pos (0,200)  #top
            rotate -20  #top
            parallel:
                ease 1 pos (0,350) #bottom (30,90)
                ease 1.5 pos (0,200)  #top
                repeat
            parallel:
                ease 1 rotate -25 #bottom 25,50
                ease 1.5 rotate -20  #top
                repeat
    contains:
            # Wanda's head Underlay (Speed 3)
            "Wanda_BJ_Head"
            subpixel True
            offset (0,50)
            parallel:
                ease 1   yoffset 250 #100
                ease 1.5 yoffset 120
                repeat
            parallel:
                easeout .5  xoffset -2 #100
                easein .5  xoffset 0 #100
                easeout .5  xoffset -2 #100
                easein 1   xoffset -10
                repeat
    contains:
            # Cock (Speed 3)
            "Blowcock"
            anchor (.5,.5)
            offset (305,170)
            rotate 0
    contains:
            # the masked overlay for when her head overlaps the cock (Speed 3)
            AlphaMask("Wanda_BJ_Head", "Wanda_BJ_MouthSuckingMask")
            subpixel True
            anchor (0.5, 0.5)
            offset (0,50)
            parallel:
                ease 1   yoffset 250 #100
                ease 1.5 yoffset 120
                repeat
            parallel:
                easeout .5  xoffset -2 #100
                easein .5  xoffset 0 #100
                easeout .5  xoffset -2 #100
                easein 1   xoffset -10
                repeat
    contains:
            # Her spunk for the heading animation (Speed 3)
            "Wanda_BJ_SpunkSucking"
            subpixel True
            offset (0,50)
            parallel:
                ease 1   yoffset 250 #100
                ease 1.5 yoffset 120
                repeat
            parallel:
                easeout .5  xoffset -2 #100
                easein .5  xoffset 0 #100
                easeout .5  xoffset -2 #100
                easein 1   xoffset -10
                repeat
#end Wanda_BJ_Anim3 Sucking (Speed 3)


image Wanda_BJ_Anim4:
    #Animation for Wanda BJ Deep (Speed 4)
    contains:
            # Wanda's body, everything below the chin (Speed 4)
            "Wanda_BJ_Backdrop"
            subpixel True
            transform_anchor True
            pos (0,350)  #top
            rotate -25  #top
            parallel:
                ease 1 pos (0,500) #bottom (30,90)
                pause .5
                ease 2 pos (0,350)  #top
                repeat
            parallel:
                ease 1 rotate -30 #bottom 25,50
                pause .5
                ease 2 rotate -25  #top
                repeat
    contains:
            # Wanda's head Underlay (Speed 4)
            "Wanda_BJ_Head"
            offset (0,175)
            block:
                subpixel True
                ease 1 yoffset 375
                pause .5
                ease 2 yoffset 175
                repeat
    contains:
            # Cock (Speed 4)
            "Blowcock"
            anchor (.5,.5)
            offset (305,170)#(300,170)
            rotate 0
    contains:
            # the masked overlay for when her head overlaps the cock (Speed 4)
            AlphaMask("Wanda_BJ_Head", "Wanda_BJ_MouthSuckingMask")
            anchor (0.5, 0.5)
            offset (0,175)
            block:
                subpixel True
                ease 1 yoffset 375
                pause .5
                ease 2 yoffset 175
                repeat
    contains:
            # Her spunk for the heading animation (Speed 4)
            "Wanda_BJ_SpunkSucking"
            subpixel True
            offset (0,175)
            block:
                subpixel True
                ease 1 yoffset 375
                pause .5
                ease 2 yoffset 175
                repeat
#end Wanda_BJ_Anim4 Deep (Speed 4)


image Wanda_BJ_Anim5:
    #Animation for Wanda BJ cum high (Speed 5)
    contains:
            # Wanda's body, everything below the chin (Speed 5)
            "Wanda_BJ_Backdrop"
            subpixel True
            offset (0,-30)     #top
            block:
                ease 1 yoffset -20           #bottom
                ease 1.5 offset (0,-30)     #top
                repeat
    contains:
            # Wanda's head Underlay (Speed 5)
            "Wanda_BJ_Head"
            subpixel True
            offset (0,50)     #top
            block:
                ease 1 yoffset 60           #bottom
                ease 1.5 offset (0,50)     #top
                repeat
    contains:
            # Cock (Speed 5)
            "Blowcock"
            anchor (.5,.5)
            offset (305,170)
            rotate 0
    contains:
            # Her face overlay for the heading animation  (Speed 5)
            contains:
                AlphaMask("Wanda_BJ_CumHighHead", "Wanda_BJ_MaskCumHighMask")
                anchor (0.5, 0.5)
            subpixel True
            offset (0,50)     #top
            block:
                ease 1 yoffset 60           #bottom
                ease 1.5 offset (0,50)     #top
                repeat
    contains:
            # Her spunk for the heading animation (Speed 5)
            "Wanda_BJ_SpunkCumHigh"
            subpixel True
            pos (0,77)
            offset (0,50)     #top
            block:
                ease 1 yoffset 60           #bottom
                ease 1.5 offset (0,50)     #top
                repeat
            #redo animation process for this one.
#end Wanda_BJ_Anim5 Cum High (Speed 5)

image Wanda_BJ_MouthHigh:
    #the mouth used for the cumming high animations
    contains:
        "images/WandaBJFace/Wanda_BJ_Mouth_Heading.png"
        anchor (430,530)#(460,464)
        transform_anchor True
        subpixel True
        zoom .9 #0.45
        block:
            ease 1      zoom 1          #bottom
            ease 1.5    zoom .9     #top
            repeat
#    contains:
#        ConditionSwitch(
#            "'mouth' in WandaX.Spunk", "images/WandaBJFace/Wanda_BJ_Spunk_SuckingU.png",
#            "True", Null(),
#            )
#        zoom 1.1
#        anchor (0.50,0.6)#(0.50,0.65)  #(0.40,0.65)
# end image Wanda_BJ_MouthHigh:

image Wanda_BJ_MaskCumHighMask:
    #the mask used for the cumming high image
    contains:
        "images/WandaBJFace/Wanda_BJ_Mask_Heading.png"
        subpixel True
        transform_anchor True
        anchor (430,530)#429,464)
        offset (430,540)#(415,490)
        zoom .9 #0.70
        block:
            ease 1      zoom 1          #bottom
            ease 1.5    zoom .9     #top
            repeat
#end image Wanda_BJ_MaskCumHighMask:

image Wanda_BJ_CumHighHead:
    #An alt copy of her head that is alphaed by Wanda_BJ_MaskCumHighMask
    #used in Wanda_BJ_Anim5
    contains:
        "Wanda_BJ_Head"
        anchor (460,530)#429,464)
        offset (417,484)#(460,530)#(257,279)

image Wanda_BJ_SpunkCumHigh:
    #the spunk used for the cumming high animations
    contains:
        contains:
            ConditionSwitch(
                "'mouth' in WandaX.Spunk", "images/WandaBJFace/Wanda_BJ_Spunk_Heading_O.png",
                "True", Null(),
                )
        anchor (430,530)#(460,464)
        transform_anchor True
        subpixel True
        zoom 1 #0.45
        block:
            ease .6      zoom 1.1          #bottom
            ease .4      zoom 1.05          #bottom
            ease .4      zoom 1.1          #bottom
            ease 1.1    zoom 1     #top
            repeat
#end image Wanda_BJ_SpunkCumHigh:
#end Wanda_BJ_Anim5 Cum High (Speed 5) Elements / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_BJ_Anim6:
    #Animation for Wanda BJ cum deep (Speed 6)
    contains:
            # Wanda's body, everything below the chin (Speed 6)
            "Wanda_BJ_Backdrop"
            subpixel True
            transform_anchor True
            pos (0,450)  #top
            rotate -28  #top
            parallel:
                ease 1 pos (0,500) #bottom (30,90)
                pause .5
                ease 2 pos (0,450)  #top
                repeat
            parallel:
                ease 1 rotate -30 #bottom 25,50
                pause .5
                ease 2 rotate -28  #top
                repeat
    contains:
            # Wanda's head Underlay (Speed 6)
            "Wanda_BJ_Head"
            offset (0,330)
            block:
                subpixel True
                ease 1 yoffset 375#250
                pause .5
                ease 2 yoffset 330#230
                repeat
    contains:
            # Cock (Speed 6)
            "Blowcock"
            anchor (.5,.5)
            offset (305,170)
            rotate 0
    contains:
            # the masked overlay for when her head overlaps the cock (Speed 6)
            AlphaMask("Wanda_BJ_Head", "Wanda_BJ_MouthSuckingMask")
            anchor (0.5, 0.5)
            offset (0,330)
            block:
                subpixel True
                ease 1 yoffset 375#250
                pause .5
                ease 2 yoffset 330#230
                repeat
    contains:
            # Her spunk for the heading animation (Speed 6)
            "Wanda_BJ_SpunkSucking"
            subpixel True
            offset (0,330)
            block:
                subpixel True
                ease 1 yoffset 375#250
                pause .5
                ease 2 yoffset 330#230
                repeat
#end Wanda_BJ_Anim6 cum deep (Speed 6)

#end Wanda_BJ_Anims / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
#BJ Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Wanda_BJ_Launch(Line = Trigger):    # The sequence to launch the Wanda BJ animations
    if renpy.showing("Wanda_BJ_Animation") and WandaX.Pose != "69":
        return
    elif renpy.showing("Wanda_69_Animation") and WandaX.Pose == "69":
        return

    if not Player.Male:
        call Wanda_CUN_Launch
        return

    call Girl_Hide(WandaX) #call Rogue_Hide
    if Line == "L" or Line == "cum":
        show Wanda_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1
            ease 1 zoom 2.5 offset (150,80)
        with dissolve
    else:
        show Wanda_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1 zoom 2.5 offset (150,80)
        with dissolve

    if Line == "L":
            if Taboo:
                if len(Present) >= 2:
                    if Present[0] != WandaX:
                            "[WandaX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                    elif Present[1] != WandaX:
                            "[WandaX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
                else:
                            "[WandaX.Name] небрежно оглядывается по сторонам, чтобы убедиться, что никто не наблюдает."
            if not WandaX.Blow:
                "[WandaX.Name] нерешительно опускается на колени и прикасается своим ртом к вашему члену."
            else:
                "[WandaX.Name] встает на колени и начинает сосать ваш член."

    $ Speed = 0

    if Line != "cum":
        $ Trigger = "blow"

    show Wanda_Sprite:
        alpha 0
    if WandaX.Pose == "69":
            show Wanda_69_Animation zorder 150
    else:
            show Wanda_BJ_Animation zorder 150

    return

label Wanda_BJ_Reset: # The sequence to the Wanda animations from BJ to default
    if not renpy.showing("Wanda_BJ_Animation") and not renpy.showing("Wanda_69_Animation"):
        return
    call Girl_Hide(WandaX) #call Rogue_Hide
    $ Speed = 0

    show Wanda_Sprite at SpriteLoc(StageCenter) zorder 150:
        alpha 1 zoom 2.5 offset (150,80)
    with dissolve

    show Wanda_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Wanda_Sprite at SpriteLoc(WandaX.SpriteLoc) zorder WandaX.Layer:
        alpha 1 zoom 1 offset (0,0)
    return

# End Wanda Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Wanda's TJ animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Animation components / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# start base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Wanda_TJ_Animation:
            #core TJ animation
            contains:
                ConditionSwitch(
                    # Wanda's upper body
                    "not Player.Sprite","Wanda_TJ_0",#Static
                    "Speed == 1", "Wanda_TJ_1",#slow
                    "Speed == 3", "Wanda_TJ_3",#licking
                    "Speed == 4", "Wanda_TJ_4",#cumming high
                    "Speed == 5", "Wanda_TJ_5",#cumming low
                    "Speed >= 2", "Wanda_TJ_2",#fast
                    "True",       "Wanda_TJ_0",#Static
                    )
            zoom .6 #.7
            transform_anchor True
            anchor (.5,.5)
            offset (400,250)#(950,1050)
# end base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#image Wanda_TJ_Head:
#            #Hair underlay
#            "Wanda_BJ_Head"
#            transform_anchor True
#            zoom .7
#            anchor (0.5, 0.5)
#            offset (30,-450)
#            rotate 0


image Wanda_TJ_ZeroCock:
            #cock used in Wanda's sex pose
            "Zero_Blowcock"
            transform_anchor True
            zoom .8#.6
            anchor (0.5, 0.6)
            offset (-5,50)#(45,50)
            rotate 0


image Wanda_TJ_Body:
    LiveComposite(
        (1000,1000),       #550,950
#        (-10,-90), "Wanda_BJ_HairBack", #(75,-10)

#        (0,0), "images/WandaBJFace/[WandaX.skin_image.skin_path]Wanda_TJ_Body.png",

        (0,0), "images/WandaBJFace/[WandaX.skin_image.skin_path]Wanda_TJ_Body.png",
        (0,0), ConditionSwitch(
            # water drops
            "WandaX.Water", "images/WandaBJFace/Wanda_TJ_Wet_Body.png",
            "True", Null(),
            ),
#        (0,0), "images/WandaBJFace/Wanda_TJ_RefCock.png",

#        (0,0), ConditionSwitch(
#            # under tit smoosh
#            "not Player.Sprite", Null(),
#            "True", "images/WandaBJFace/[WandaX.skin_image.skin_path]Wanda_TJ_Tits_Under.png",
#            ),
        (0,0), ConditionSwitch(
            #Chest layer under tits
#            "WandaX.Uptop", ConditionSwitch(
#                    # if top is up. . .
#                    "WandaX.Chest == 'lace bra'", "images/WandaBJFace/Wanda_TJ_Chest_Lace_Body_Up.png",
#                    "WandaX.Chest == 'bra'", "images/WandaBJFace/Wanda_TJ_Chest_Lace_Body_Up.png",
#                    "WandaX.Chest == 'tank'", "images/WandaBJFace/Wanda_TJ_Chest_Tank_Body_Up.png",
#                    "WandaX.Chest == 'swimsuit'", "images/WandaBJFace/Wanda_TJ_Chest_Bikini_Body_Up.png",
#                    "True", Null(),
#                    ),
#            "WandaX.Chest == 'lace bra'", Recolor("Wanda", "Chest", "images/WandaBJFace/Wanda_TJ_Chest_Bra.png"),
            "WandaX.Chest == 'mesh top'", Recolor("Wanda", "Chest", "images/WandaBJFace/Wanda_TJ_Chest_Mesh.png"),
            "WandaX.Chest == 'bikini top'", Recolor("Wanda", "Chest", "images/WandaBJFace/Wanda_TJ_Chest_Bikini.png"),
            "WandaX.Chest", Recolor("Wanda", "Chest", "images/WandaBJFace/Wanda_TJ_Chest_Bra.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over body layer
#            "WandaX.Over == 'corset'", "images/WandaBJFace/Wanda_TJ_Over_Corset.png",
            "WandaX.Over == 'shirt'", Recolor("Wanda", "Over", "images/WandaBJFace/Wanda_TJ_Over_Shirt.png"),
            "WandaX.Over == 'purple top'", "images/WandaBJFace/Wanda_TJ_Over_Purple.png",
            "WandaX.Legs == 'dress'", Recolor("Wanda", "Legs", "images/WandaBJFace/Wanda_TJ_Tits_Dress_Under.png"),
#            "WandaX.Over == 'towel'", "images/WandaBJFace/Wanda_TJ_Over_Towel_Body.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #jacket body layer
            "WandaX.Acc == 'jacket'", Recolor("Wanda", "Acc", "images/WandaBJFace/Wanda_TJ_Jacket.png"),
            "True", Null(),
            ),
#        (0,0), "images/WandaBJFace/Wanda_TJ_RefLine.png",

#        (0,0), ConditionSwitch(
#            #Hair overlay
#            "WandaX.Hair != 'long' and WandaX.Hair != 'wetlong'", Null(),
#            "WandaX.Water or WandaX.Hair == 'wetlong'", "images/WandaBJFace/Wanda_TJ_Hair_Wet.png",
#            "not Player.Male and 'facial' in WandaX.Spunk","images/WandaBJFace/Wanda_TJ_Hair_Wet.png",
#            "True", "images/WandaBJFace/Wanda_TJ_Hair_Long.png",
#            ),

        (30,-300), ConditionSwitch(
            #Hair overlay
            "WandaX.Hair == 'wetlong' or (WandaX.Hair == 'long' and WandaX.Water)", Recolor("Wanda", "Hair", "images/WandaBJFace/Wanda_BJ_Hair_Long_Wet_Under.png"),
            "WandaX.Hair == 'long' and (not Player.Male and 'facial' in WandaX.Spunk)",Recolor("Wanda", "Hair", "images/WandaBJFace/Wanda_BJ_Hair_Long_Wet_Under.png"),

            "WandaX.Hair == 'long'",Recolor("Wanda", "Hair", "images/WandaBJFace/Wanda_BJ_Hair_Long_Under.png"),
            "True", Null(),
            ),
#        (-10,-90), "Wanda_Sprite_Head", #(75,-10)
        )
    transform_anchor True
    anchor (0.6, 1.0)#(0.6, 0.0)
    xoffset 118#150
    yoffset 240#271#125
#    zoom .75  #.76
    rotate 0

#    transform_anchor True
#    zoom 1
#    anchor (0.4, 1.0)
#    #offset (410,770) # (300,275)
#    rotate 0


image Wanda_TJ_Tits_Under:
    LiveComposite(
        (1000,1000),       #550,950
        (0,0), ConditionSwitch(
            # under tit
#            "Player.Sprite and renpy.showing('Wanda_TJ_Animation')", "images/WandaBJFace/[WandaX.skin_image.skin_path]Wanda_TJ_Tits_Under.png",
            "True", "images/WandaBJFace/[WandaX.skin_image.skin_path]Wanda_TJ_Tits_Under.png",
            ),
#        (0,0), ConditionSwitch(
#            #Chest tits layer
#            "not WandaX.Uptop", Null(),
#            "WandaX.Over == 'tshirt'", "images/WandaBJFace/Wanda_TJ_Over_Tshirt_Mask.png",
#            "WandaX.Chest == 'sports bra'", "images/WandaBJFace/Wanda_TJ_Chest_Sports_Mask.png",
##            "WandaX.Chest == 'swimsuit'", "images/WandaBJFace/Wanda_TJ_Chest_Bikini_Tits.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            # spunk under tits
            "'tits' not in WandaX.Spunk", Null(),
            "True", "images/WandaBJFace/Wanda_TJ_Spunk_Tits_Under.png",
            ),
        )
    transform_anchor True
#    anchor (0.6, 1.0)#(0.6, 0.0)
#    xoffset 155#300
#    yoffset 125#-600
##    zoom .75  #.76
    rotate 0


image Wanda_TJ_Tits_Over:
    LiveComposite(
        (1000,1000),    #800,950
        (0,0), ConditionSwitch(
            # over tit
            "Player.Sprite and renpy.showing('Wanda_TJ_Animation')", "images/WandaBJFace/[WandaX.skin_image.skin_path]Wanda_TJ_Tits_Over.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            # water drops
            "WandaX.Water", "images/WandaBJFace/Wanda_TJ_Wet_Tits.png",
            "True", Null(),
            ),
#        (0,0),  "images/WandaBJFace/Wanda_TJ_TitsRef.png",
        (0,0), ConditionSwitch(
            #Chest tits layer
            "WandaX.Over == 'tshirt'", Null(),
            "WandaX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "WandaX.Chest == 'lace bra'", Recolor("Wanda", "Chest", "images/WandaBJFace/Wanda_TJ_Tits_Chest_Bra_Up.png"),
                    "WandaX.Chest == 'bikini top'", Recolor("Wanda", "Chest", "images/WandaBJFace/Wanda_TJ_Tits_Chest_Bikini_Up.png"),
                    "WandaX.Chest == 'mesh top'", Recolor("Wanda", "Chest", "images/WandaBJFace/Wanda_TJ_Tits_Chest_Mesh_Up.png"),
                    "WandaX.Chest", Recolor("Wanda", "Chest", "images/WandaBJFace/Wanda_TJ_Tits_Chest_Bra_Up.png"),
                    "True", Null(),
                    ),
            "WandaX.Chest == 'lace bra'", Recolor("Wanda", "Chest", "images/WandaBJFace/Wanda_TJ_Tits_Chest_Lace.png"),
            "WandaX.Chest == 'bikini top'", Recolor("Wanda", "Chest", "images/WandaBJFace/Wanda_TJ_Tits_Chest_Bikini.png"),
            "WandaX.Chest == 'mesh top'", Recolor("Wanda", "Chest", "images/WandaBJFace/Wanda_TJ_Tits_Chest_Mesh.png"),
            "WandaX.Chest", Recolor("Wanda", "Chest", "images/WandaBJFace/Wanda_TJ_Tits_Chest_Bra.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #dress layer
            "WandaX.Uptop or WandaX.Over == 'shirt'", Null(),
            "WandaX.Legs == 'dress'", Recolor("Wanda", "Legs", "images/WandaBJFace/Wanda_TJ_Tits_Dress.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over tits layer
            "WandaX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "WandaX.Over == 'shirt'", Recolor("Wanda", "Over", "images/WandaBJFace/Wanda_TJ_Tits_Over_Shirt_Up.png"),
                    "True", Null(),
                    ),
            "WandaX.Over == 'purple top'", "images/WandaBJFace/Wanda_TJ_Tits_Over_Purple.png",
            "WandaX.Over == 'shirt'", Recolor("Wanda", "Over", "images/WandaBJFace/Wanda_TJ_Tits_Over_Shirt.png"),
            "WandaX.Over == 'corset'", Recolor("Wanda", "Over", "images/WandaBJFace/Wanda_TJ_Tits_Over_Corset.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # spunk over tits
            "'tits' not in WandaX.Spunk", Null(),
#            "WandaX.Over == 'tshirt'", "images/WandaBJFace/Wanda_TJ_Spunk_Clothed.png",
#            "not WandaX.Uptop and WandaX.Over", "images/WandaBJFace/Wanda_TJ_Spunk_Clothed.png",
            "WandaX.Chest == 'mesh top'", Null(),
            "True", "images/WandaBJFace/Wanda_TJ_Spunk_Tits_Over.png",
            ),
#        (0,0), "images/WandaBJFace/Wanda_TJ_RefLine.png",
#        (0,0), "images/WandaBJFace/Wanda_TJ_RefLine2.png",
        )
    transform_anchor True
#    anchor (0.6, 1.0)#(0.6, 562)
#    xoffset 155#300
#    yoffset 325#125
#    yoffset -925#-625#-325
#    zoom .75  #.76
    rotate 0


image Wanda_TJ_BraStretch:
            #bra streching effect
            contains:
                ConditionSwitch(
                    #Over tits layer
#                    "WandaX.Over == 'tshirt'", "images/WandaBJFace/Wanda_TJ_Stretch_Tshirt.png",
#                    "WandaX.Over == 'sweater'", "images/WandaBJFace/Wanda_TJ_Stretch_Sweater.png",
                    "WandaX.Chest == 'mesh top'", Recolor("Wanda", "Chest", "images/WandaBJFace/Wanda_TJ_Brastretch_Mesh.png"),
                    "True", Null(),
                    )
#            contains:
#                    "images/WandaBJFace/Wanda_TJ_RefLine2.png"
            transform_anchor True
#            zoom 1
#            offset (50,0) # (300,275)
#            anchor (.1,.1)#(0.1, .2)
            rotate 0

image Wanda_TJ_Hands:
    LiveComposite(
        (1000,1000),       #550,950
        (0,0), ConditionSwitch(
            # hands
            "WandaX.Chest == 'mesh top'", "images/WandaBJFace/[WandaX.skin_image.skin_path]Wanda_TJ_Hands_Mesh.png",
            "True", "images/WandaBJFace/[WandaX.skin_image.skin_path]Wanda_TJ_Hands.png",
            ),
        (0,0), ConditionSwitch(
            # sleeves
            "WandaX.Over == 'purple top'", "images/WandaBJFace/Wanda_TJ_Sleeves.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # wrists
            "WandaX.Arms", "images/WandaBJFace/Wanda_TJ_Hands_Armlet.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            # nips
#            "True", "images/WandaBJFace/Wanda_TJ_Nips.png",
#            ),
#        (0,0), ConditionSwitch(
#            #Chest tits layer
#            "not WandaX.Uptop", Null(),
#            "WandaX.Over == 'tshirt'", "images/WandaBJFace/Wanda_TJ_Over_Tshirt_Mask.png",
#            "WandaX.Chest == 'sports bra'", "images/WandaBJFace/Wanda_TJ_Chest_Sports_Mask.png",
##            "WandaX.Chest == 'swimsuit'", "images/WandaBJFace/Wanda_TJ_Chest_Bikini_Tits.png",
#            "True", Null(),
#            ),


        (0,0), ConditionSwitch(
            #Piercings layer
#            "not WandaX.Pierce", Null(),
            "WandaX.Pierce == 'ring'", ConditionSwitch(
                    #if it's the ring pericings
                    "WandaX.Uptop", "images/WandaBJFace/Wanda_TJ_Pierce_R.png",

                    "WandaX.Over == 'purple top'", "images/WandaBJFace/Wanda_TJ_Pierce_R_Purp.png",
                    "WandaX.Over == 'shirt' or WandaX.Over == 'corset'", "images/WandaBJFace/Wanda_TJ_Pierce_R_Red.png",
                    "WandaX.Legs == 'dress'", "images/WandaBJFace/Wanda_TJ_Pierce_R_Black.png",

                    "WandaX.Chest == 'lace bra'", "images/WandaBJFace/Wanda_TJ_Pierce_R_Lace.png",
                    "WandaX.Chest == 'mesh top'", "images/WandaBJFace/Wanda_TJ_Pierce_R_Mesh.png",
                    "WandaX.Chest", "images/WandaBJFace/Wanda_TJ_Pierce_R_Red.png",
                    "True", "images/WandaBJFace/Wanda_TJ_Pierce_R.png",
                    ),

            "WandaX.Pierce", ConditionSwitch(
                    #if it's the ring pericings
                    "WandaX.Uptop", "images/WandaBJFace/Wanda_TJ_Pierce_B.png",

                    "WandaX.Over == 'purple top'", "images/WandaBJFace/Wanda_TJ_Pierce_B_Purp.png",
                    "WandaX.Over == 'shirt' or WandaX.Over == 'corset'", "images/WandaBJFace/Wanda_TJ_Pierce_B_Red.png",
                    "WandaX.Legs == 'dress'", "images/WandaBJFace/Wanda_TJ_Pierce_B_Black.png",

                    "WandaX.Chest == 'lace bra'", "images/WandaBJFace/Wanda_TJ_Pierce_B_Lace.png",
                    "WandaX.Chest == 'mesh top'", "images/WandaBJFace/Wanda_TJ_Pierce_B_Mesh.png",
                    "WandaX.Chest", "images/WandaBJFace/Wanda_TJ_Pierce_B_Red.png",
                    "True", "images/WandaBJFace/Wanda_TJ_Pierce_B.png",
                    ),

            "WandaX.Lust < 50", Null(),
            "WandaX.Uptop", "images/WandaBJFace/Wanda_TJ_Nips.png",
            "WandaX.Over == 'purple top'", "images/WandaBJFace/Wanda_TJ_Nips_Purp.png",
            "WandaX.Over == 'shirt' or WandaX.Over == 'corset'", "images/WandaBJFace/Wanda_TJ_Nips_Red.png",
            "WandaX.Legs == 'dress'", "images/WandaBJFace/Wanda_TJ_Nips_Black.png",

            "WandaX.Chest == 'lace bra'", "images/WandaBJFace/Wanda_TJ_Nips_Lace.png",
            "WandaX.Chest == 'mesh top'", "images/WandaBJFace/Wanda_TJ_Nips_Mesh.png",
            "WandaX.Chest", "images/WandaBJFace/Wanda_TJ_Nips_Red.png",
            "True", "images/WandaBJFace/Wanda_TJ_Nips.png",
            ),

#        (0,0), ConditionSwitch(
#            # spunk under tits
#            "'tits' not in WandaX.Spunk", Null(),
#            "True", "images/WandaBJFace/Wanda_TJ_Spunk_Tits.png",
#            ),
        )
    transform_anchor True
#    anchor (0.6, 1.0)#(0.6, 0.0)
#    xoffset 155#300
#    yoffset 125#-600
##    zoom .75  #.76
    rotate 0


## Animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start 0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Wanda_TJ_0:
        #Her Body in the TJ pose, static
#        contains:
#                #hair back
#                "Wanda_BJ_HairBack"
#                subpixel True
##                offset (90,-480)
#                pos (-70,0) #top (0,-10)
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
                "Wanda_TJ_Body"
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
                "Wanda_TJ_Tits_Under"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#150
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
                #head
                "Wanda_BJ_Head"
                subpixel True
                zoom 0.9
                offset (50,-600)#(70,-480)
                pos (-90,0) #top (0,-10)
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
                "Wanda_TJ_ZeroCock"
#                ConditionSwitch(
#                            "Player.Sprite","Wanda_TJ_ZeroCock",
#                            "True",  Null(),
#                            )
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (0,50)#(5,50)
        contains:
                #bra stretch
                "Wanda_TJ_BraStretch"
                subpixel True
                pos (0,0) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 680)#(0.6, 818)
                xoffset 160#270
                yoffset -355#-245
                yzoom .3
                parallel:
                    ease 2 ypos 30
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
                parallel:
#                    pause .2
                    ease 2 yzoom .53
                    pause .3
                    ease 2 yzoom .3
                    pause .4
                    repeat
        contains:
                #overside tit
                "Wanda_TJ_Tits_Over"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#160
                yoffset -271#271
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
                "Wanda_TJ_Hands"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
                yoffset -271#125
                parallel:
                    ease 2 ypos 30
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat


# End Wanda TJ Pose 0 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



## Start 1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Wanda_TJ_1:
        #Her Body in the TJ pose, slow
#        contains:
#                #hair back
#                "Wanda_BJ_HairBack"
#                subpixel True
##                offset (90,-480)
#                pos (-70,0) #top (0,-10)
#                transform_anchor True
#                rotate 0
#                parallel:
#                    ease 2 ypos 120
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
                "Wanda_TJ_Body"
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
                #underside tit
                "Wanda_TJ_Tits_Under"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
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
                #head
                "Wanda_BJ_Head"
                subpixel True
                zoom 0.9
                offset (50,-600)#(50,-600)
                pos (-90,0) #top (0,-10)
                transform_anchor True
                rotate 10
                parallel:
                    ease 2 ypos 120
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
                parallel:
                    pause .1
                    ease 2 rotate -5#0
                    pause .3
                    ease .5 rotate 20#14
                    ease 1.8 rotate 10
#                    pause 1.3
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Wanda_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (0,50)#(5,50)
        contains:
                #bra stretch
                "Wanda_TJ_BraStretch"
                subpixel True
                pos (0,0) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 680)#(0.6, 818)
                xoffset 160#270
                yoffset -355#-245
                yzoom .3
#                alpha 0.7
                parallel:
                    ease 2 ypos 150
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
                parallel:
#                    pause .2
                    ease 2 yzoom 1.36#1.2
                    pause .3
                    ease 2 yzoom .3
                    pause .4
                    repeat
        contains:
                #overside tit
                "Wanda_TJ_Tits_Over"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
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
                "Wanda_TJ_Hands"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
                yoffset -271#125
                parallel:
                    pause .1
                    ease 1.9 ypos 110
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
## End Wanda TJ Pose 1 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




## Start 2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Wanda_TJ_2:
        #Her Body in the TJ pose, fast
#        contains:
#                #hair back
#                "Wanda_BJ_HairBack"
#                subpixel True
##                offset (90,-480)
#                pos (-70,0) #top (0,-10)
#                transform_anchor True
#                rotate 0
#                parallel: #4.7s total -> 1.7
#                    ease .6 ypos 60 #120
#                    pause .1
#                    ease .8 ypos 0
#                    pause .2
#                    repeat
#                parallel:
#                    ease .5 rotate -5
#                    pause .2
#                    ease .8 rotate 0
#                    pause .2
#                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "Wanda_TJ_Body"
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
                #underside tit
                "Wanda_TJ_Tits_Under"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
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
                #head
                "Wanda_BJ_Head"
                subpixel True
                zoom 0.9
                offset (50,-600)#(70,-480)
                pos (-90,0) #top (0,0)
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
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Wanda_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (0,50)#(5,50)
        contains:
                #bra stretch
                "Wanda_TJ_BraStretch"
                subpixel True
                pos (0,0) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 680)#(0.6, 818)
                xoffset 160#270
                yoffset -355#-245
                yzoom .3
                parallel: #4.7s total -> 1.9
                    ease .6 ypos 60 #120
                    pause .1
                    ease .8 ypos 0
                    pause .2
                    repeat
                parallel: #4.7s total -> 1.9
                    ease .6 yzoom .72 #.35
                    pause .1
                    ease .8 yzoom .3
                    pause .2
                    repeat
        contains:
                #overside tit
                "Wanda_TJ_Tits_Over"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
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
                "Wanda_TJ_Hands"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
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

## End Wanda TJ Pose 2 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

## Start 3 (licking) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Wanda_TJ_3:
        #Her Body in the TJ pose, licking
#        contains:
#                #hair back
#                "Wanda_BJ_HairBack"
#                subpixel True
#                pos (-70,110) #top (0,0)
#                transform_anchor True
#                rotate 0
#                parallel: #4.7s total -> 3.8
#                    ease 1.9 ypos 130
#                    pause .3
#                    ease .6 ypos 100
#                    pause 1
#                    repeat
#                parallel:
#                    ease 1.9 rotate -15
#                    pause .3
#                    ease .6 rotate 0
#                    pause 1
#                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "Wanda_TJ_Body"
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
                #underside tit
                "Wanda_TJ_Tits_Under"
                subpixel True
                pos (0,100) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
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
                #head
                "Wanda_BJ_Head"
                subpixel True
                zoom 0.9
                offset (50,-600)#(70,-480)
                pos (-90,110) #top (0,0)
                transform_anchor True
                rotate 0
                parallel: #4.7s total -> 3.8
                    ease 1.9 ypos 130
                    pause .3
                    ease .6 ypos 100
                    pause 1
                    repeat
                parallel:
                    ease 1.9 xpos -90
                    pause .3
                    ease .6 xpos -120
                    pause 1
                    repeat
                parallel:
                    ease 1.9 rotate -15
                    pause .3
                    ease .6 rotate 0
                    pause 1
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Wanda_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (0,50)#(5,50)
                rotate 0
                parallel:
                    pause .1
                    ease 2 rotate -3
                    pause .3
                    ease .5 rotate 0
                    pause .9
                    repeat
        contains:
                #bra stretch
                "Wanda_TJ_BraStretch"
                subpixel True
                pos (0,120) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 680)#(0.6, 818)
                xoffset 160#270
                yoffset -355#-245
                yzoom 1.15
#                alpha 0.7
                parallel:
                    ease 2 pos (-25,150)#(-25,120)
                    pause .3
                    ease .5 pos (0,120)#(0,90)
                    pause 1
                    repeat
                parallel:
                    ease 2 yzoom 1.38#1.25
                    pause .3
                    ease .5 yzoom 1.15#1.05
                    pause 1
                    repeat
        contains:
                #overside tit
                "Wanda_TJ_Tits_Over"
                subpixel True
                pos (0,100) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
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
                "Wanda_TJ_Hands"
                subpixel True
                pos (0,100) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
                yoffset -271#125
                parallel:
                    ease 2 ypos 130
                    pause .3
                    ease .5 ypos 100
                    pause 1
                    repeat


## End Wanda TJ Pose 3 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



## Start 4 (cumming high) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
#image Wanda_TJ_4:
#        #Her Body in the TJ pose, cummming high
#        contains:
#                #jacket
#                "Wanda_TJ_Jacketback"
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
#                "Wanda_TJ_Braback"
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
#                "Wanda_TJ_Body"
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
#                "Wanda_TJ_Head"
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
#                "Wanda_TJ_ZeroCock"
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
#                    "Wanda_TJ_Tits"
#                subpixel True
#                pos (0,5) #top (0,-10)
#                transform_anchor True
#                parallel:
#                    pause .2
#                    ease 1.9 ypos -30
#                    pause .2
#                    ease 1.9 ypos 5
#                    repeat

## End Wanda TJ Pose 4 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start 5 (cumming low) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Wanda_TJ_5:
        #Her Body in the TJ pose, cumming low
#        contains:
#                #hair back
#                "Wanda_BJ_HairBack"
#                subpixel True
##                offset (90,-480)
#                pos (-60,115) #top (0,-10)
#                transform_anchor True
#                rotate 5
#                parallel:
#                    ease 2 ypos 120
#                    pause .3
#                    ease 1.5 ypos 115
#                    pause .5
#                    repeat
#                parallel:
#                    pause .1
#                    ease 1 rotate -5
#                    pause .3
#                    ease .5 rotate 5
#                    pause .9
#                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "Wanda_TJ_Body"
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
                parallel:
                    pause .1
                    ease 1 xpos 20
                    pause .3
                    ease .5 xpos 0
                    pause .9
                    repeat
        contains:
                #underside tit
                "Wanda_TJ_Tits_Under"
                subpixel True
                pos (0,120) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
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
                parallel:
                    pause .1
                    ease 1 xpos 20
                    pause .3
                    ease .5 xpos 0
                    pause .9
                    repeat
        contains:
                #head
                "Wanda_BJ_Head"
                subpixel True
                zoom 0.9
                offset (50,-600)#(70,-480)
                pos (-95,115) #top (0,-10)
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
                    ease 1 xpos -40
                    pause .3
                    ease .5 xpos -95
                    pause .9
                    repeat
                parallel:
                    pause .1
                    ease 1 rotate -5
                    pause .3
                    ease .5 rotate 5
                    pause .9
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Wanda_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (0,50)#(5,50)
                rotate 0
                parallel:
                    pause .1
                    ease 1.1 rotate 3
                    pause .3#1.5
                    ease .5 rotate -5
                    ease .8 rotate 0
                    repeat
        contains:
                #bra stretch
                "Wanda_TJ_BraStretch"
                subpixel True
                pos (-5,120) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 680)#(0.6, 818)
                xoffset 160#270
                yoffset -355#-245
                yzoom .8
#                alpha 0.7
                parallel:
                    pause 1.5
                    ease .5 xpos -45
                    ease .8 xpos -5
                    repeat
                parallel:
                    ease 2 yzoom 1.30#1.21
                    pause .3
                    ease 1.5 yzoom 1.25#1.18
                    pause .5
                    repeat
                parallel:
                    ease 2 ypos 140
                    pause .3
                    ease 1.5 ypos 130
                    pause .5
                    repeat
        contains:
                #overside tit
                "Wanda_TJ_Tits_Over"
                subpixel True
                pos (0,120) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
                yoffset -271#125
                yzoom 1
                parallel:
                    ease 2 ypos 130
                    pause .3
                    ease 1.5 ypos 120 #.5
                    pause .5
                    repeat
                parallel:
                    pause .1
                    ease 1 xpos 20
                    pause .3
                    ease .5 xpos 0
                    pause .9
                    repeat
        contains:
                #hands over everything
                "Wanda_TJ_Hands"
                subpixel True
                pos (0,120) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 160#200
                yoffset -271#125
                parallel:
                    ease 2 ypos 130
                    pause .3
                    ease 1.5 ypos 120 #.5
                    pause .5
                    repeat
                parallel:
                    pause .1
                    ease 1 xpos 20
                    pause .3
                    ease .5 xpos 0
                    pause .9
                    repeat

# End Wanda TJ Pose 5 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

## Wanda's TJ animations end / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Wanda_TJ_Launch(Line = Trigger):    # The sequence to launch the Wanda Titfuck animations
##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    return
##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
    if renpy.showing("Wanda_TJ_Animation"):
        return

    if Line == "L": # Wanda gets started. . .
            if Taboo:
                if len(Present) >= 2:
                    if Present[0] != WandaX:
                            "[WandaX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                    elif Present[1] != WandaX:
                            "[WandaX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
                else:
                            "[WandaX.Name]  небрежно оглядывается по сторонам, чтобы убедиться, что никто не наблюдает."
#            "[WandaX.Name] bends over and places your cock between her breasts."
    if WandaX.Chest == "suit" and not WandaX.Uptop:
        $ WandaX.Uptop = 1
        "Она слегка расстегивает свой костюм."
#    if WandaX.Chest and WandaX.Over:
#        "She throws off her [WandaX.Over] and her [WandaX.Chest]."
#    elif WandaX.Over:
#        "She throws off her [WandaX.Over], baring her breasts underneath."
#    elif WandaX.Chest:
#        "She tugs off her [WandaX.Chest] and throws it aside."
#    $ WandaX.Over = 0
#    $ WandaX.Chest = 0
#    $ WandaX.ArmPose = 0
    call Girl_First_Topless(WandaX)

    show blackscreen onlayer black with dissolve

    if renpy.showing("Wanda_BJ_Animation"):
            hide Wanda_BJ_Animation
    else:
            call Girl_Hide(WandaX) #call Rogue_Hide
            show Wanda_Sprite at SpriteLoc(WandaX.SpriteLoc) zorder 150:
                alpha 1
                ease 1 zoom 2.3 xpos 750 yoffset -100
            show Wanda_Sprite:
                alpha 0

#    if WandaX.Over == "towel" or WandaX.Chest == "corset": #pulls top down because these tops are incompatible with TJ.
#        $ WandaX.Uptop = 1

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "titjob"
    show Wanda_TJ_Animation zorder 150#:
        #pos (950,1050)#(1000,1000)#(700,520)
    $ Player.Sprite = 1
    hide blackscreen onlayer black with dissolve
    return

label Wanda_TJ_Reset:
    # The sequence to the Wanda animations from Titfuck to default
    if not renpy.showing("Wanda_TJ_Animation"):
        return
#    hide Wanda_TJ_Animation
    call Girl_Hide(WandaX) #call Rogue_Hide
    $ Player.Sprite = 0

    show Wanda_Sprite at SpriteLoc(WandaX.SpriteLoc) zorder 150:
        zoom 2.3 xpos 750 yoffset -100
    show Wanda_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 xpos 700 yoffset 50
        pause .5
        ease .5 zoom 1 xpos WandaX.SpriteLoc yoffset 50
    "[WandaX.Name] pulls back"
    show Wanda_Sprite at SpriteLoc(WandaX.SpriteLoc) zorder WandaX.Layer:
        alpha 1 zoom 1 offset (0,50) xpos WandaX.SpriteLoc
    return

## End Wanda TJ Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Wanda Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Wanda Handjob element //////////////////////////////////////////////////////////////////////

image Wanda_HJ_Body:
    "Wanda_Sprite"
    pos (200,-1250)#(0,-1250)
    zoom 4.8#2.15


transform Wanda_HJ_Body_1():
    subpixel True
#    pos (700,-1250)#(350,-550)
    block:
        ease .5 ypos -1220
        pause 0.25
        ease 1.0 ypos -1250
        pause 0.1
        repeat

transform Wanda_HJ_Body_2():
    subpixel True
#    pos (350,-550)
    block:
        ease 0.2 ypos -1240
        pause 0.1
        ease 0.4 ypos -1250
        pause 0.1
        repeat

image Wanda_Hand_Under:
    contains:
        ConditionSwitch(
            "WandaX.Chest == 'mesh top'", "images/WandaSprite/[WandaX.skin_image.skin_path]handwanda2_red.png",
            "True", "images/WandaSprite/[WandaX.skin_image.skin_path]handwanda2.png",
            )
    #    "images/WandaSprite/[WandaX.skin_image.skin_path]handwanda2.png"
    anchor (0.5,0.5)
    pos (-125,0) #(170,0)
    xzoom -1


image Wanda_Hand_Over:
    contains:
        ConditionSwitch(
            "WandaX.Chest == 'mesh top'", "images/WandaSprite/[WandaX.skin_image.skin_path]handwanda1_red.png",
            "True", "images/WandaSprite/[WandaX.skin_image.skin_path]handwanda1.png",
            )
    contains:
        ConditionSwitch(
            "WandaX.Arms", "images/WandaSprite/handwanda_arm.png",
            "True", Null(),
            )
#    "images/WandaSprite/[WandaX.skin_image.skin_path]handwanda1.png"
    anchor (0.5,0.5)
    pos (-125,0) #(100,0)
    xzoom -1

transform Wanda_Hand_1():
    subpixel True
    pos (90,-100)
    rotate 5
    block:
        ease .5 pos (-120,150) rotate -5 #ypos 150 rotate 5 Bottom 90
        pause 0.25
        ease 1.0 pos (-120,-100) rotate 5 #(-20,-100) #rotate -10#  Top
        pause 0.1
        repeat

transform Wanda_Hand_2():
    subpixel True
    pos (155,-120)
    rotate 10
    block:
        ease 0.2 pos (-130,0) rotate 0   #(-15,0) 85
        pause 0.1
        ease 0.4 pos (-130,-120) rotate 5 #-15,-120)
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

image Wanda_HJ_Animation:
    contains:
        ConditionSwitch(
            # body
            "not Speed", Transform("Wanda_HJ_Body"),
            "Speed == 1", At("Wanda_HJ_Body", Wanda_HJ_Body_1()),
            "Speed >= 2", At("Wanda_HJ_Body", Wanda_HJ_Body_2()),
            "Speed", Null(),
            ),
    contains:
        ConditionSwitch(
            # backside of the hand
            "not Speed", Transform("Wanda_Hand_Under"),
            "Speed == 1", At("Wanda_Hand_Under", Wanda_Hand_1()),
            "Speed >= 2", At("Wanda_Hand_Under", Wanda_Hand_2()),
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
            "not Speed", Transform("Wanda_Hand_Over"),
            "Speed == 1", At("Wanda_Hand_Over", Wanda_Hand_1()),
            "Speed >= 2", At("Wanda_Hand_Over", Wanda_Hand_2()),
            "Speed", Null(),
            ),
    anchor (0.51, -1.3)
#    xzoom -0.4#0.6
    zoom 0.4#0.6


label Wanda_HJ_Launch(Line = Trigger):
    if renpy.showing("Wanda_HJ_Animation"):
        $ Trigger = "hand"
        return
    if not Player.Male:
        call Wanda_Finger_Launch
        return
    call Girl_Hide(WandaX) #call Rogue_Hide
    $ WandaX.ArmPose = 1
    if Line == "L":
        show Wanda_Sprite at SpriteLoc(StageRight) zorder 150:
            alpha 1
            ease 1 zoom 1.7 offset (-150,200)#(0,200)
    else:
        show Wanda_Sprite at SpriteLoc(StageRight) zorder 150:
            alpha 1
            ease 1 zoom 1.9 offset (-150,150)#(150,150)
        with dissolve

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    else:
        $ Speed = 1
    pause .5
    show Wanda_Sprite:
        alpha 0
    show Wanda_HJ_Animation at SpriteLoc(StageCenter) zorder 150 with fade:
        #xoffset 150
        offset (200,250)#(150,250)
    $ WandaX.ArmPose = 2
    return

label Wanda_HJ_Reset: # The sequence to the Wanda animations from handjob to default
    if not renpy.showing("Wanda_HJ_Animation"):
        return
    $ Speed = 0
    $ WandaX.ArmPose = 1
    hide Wanda_HJ_Animation with dissolve
    call Girl_Hide(WandaX) #call Rogue_Hide
    show Wanda_Sprite at SpriteLoc(WandaX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 1.5 offset (-250,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Wanda_Sprite at SpriteLoc(WandaX.SpriteLoc) zorder WandaX.Layer:
        alpha 1 zoom 1 offset (0,0)
#    $ WandaX.ArmPose = 1
    return

## End Wanda Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# Core Wanda CUN element ///////////////////////////////////////////////////////////////////////////                                     Core Wanda CUN element
#Wanda CUN Over Sprite Compositing

image Wanda_CUN_Animation: #core CUN animation
    LiveComposite(
        (787,913),
        (0,0), ConditionSwitch(                                                                 # back of the hair, which needs to go behind the body
            "Speed == 0",  "Wanda_CUN_Anim_Static",
            "Speed == 1",  "Wanda_CUN_Anim_Licking1",
            "Speed == 2",  "Wanda_CUN_Anim_Licking2",
            "Speed >= 3",  "Wanda_CUN_Anim_Licking3",
            "Speed == 4",  "Wanda_CUN_Anim_Licking1",
            "True", "Wanda_CUN_Anim_Static",
            ),
        )
    zoom .55
    anchor (.5,.5)

image Wanda_CUN_Anim_Static:
    #Animation for licking speed 1
#    contains:
#        #hair
#        "Wanda_BJ_HairBack"
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
        "Wanda_BJ_Backdrop"
        zoom 1.2
        pos (-180,-150)#(-300,0)
        subpixel True
        offset (0,20)  #top(0,-35)
        block:
            ease 2 yoffset 30
            ease 2 yoffset 20
            repeat
    contains:
        #head
        "Wanda_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.2
        pos (-100,0)#(-150,220)
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


image Wanda_CUN_Anim_Licking1:
    #Animation for licking speed 1
#    contains:
#        #hair
#        "Wanda_BJ_HairBack"
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
        "Wanda_BJ_Backdrop"#"Wanda_Sprite"
#        zoom 1 #4.5
#        pos (-350,-290)#(-440,-290)
        zoom 1.2
        pos (-180,-150)#(-300,0)
        subpixel True
        offset (0,0)# -70,0
        block:
            ease 2.5 offset (0,75) #bottom (30,90)
            ease 2.3 offset (0,0)  #top
            pause .2
            repeat
    contains:
        #head
        "Wanda_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.2
        pos (-70,0)#(-150,220)
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
#End Wanda Licking 1

image Wanda_CUN_Anim_Licking2:
    #Animation for licking speed 2
#    contains:
#        #hair
#        "Wanda_BJ_HairBack"
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
        "Wanda_BJ_Backdrop"
        zoom 1.2
        pos (-180,-150)#(-300,0)
        subpixel True
        offset (10,50)#490)
        block:
            ease .75 offset (10,70) #bottom (30,90)
            ease .95 offset (10,50)  #top
            pause .40
            repeat
    contains:
        #head
        "Wanda_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.2
        pos (-40,0)#(-150,220)
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
#End Wanda Licking 2

image Wanda_CUN_Anim_Licking3:
    #Animation for licking speed 3
#    contains:
#        #hair
#        "Wanda_BJ_HairBack"
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
        "Wanda_BJ_Backdrop"
        zoom 1.2
        pos (-180,-150)#(-300,0)
        subpixel True
        offset (0,110)#490)
        block:
            ease .4 offset (0,100) #bottom (30,90)
            ease .4 offset (0,110)  #top
            pause .2
            repeat
    contains:
        #head
        "Wanda_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.2
        pos (-40,0)#(-70,0)
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
#End Wanda Licking 3

#CUN Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Wanda_CUN_Launch(Line = Trigger):
    # The sequence to launch the Wanda CUN animations
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    return
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
    if renpy.showing("Wanda_CUN_Animation") and WandaX.Pose != "69":
        return
    elif renpy.showing("Wanda_69_Animation") and WandaX.Pose == "69":
        return

    if Player.Male == 1:
        call Wanda_BJ_Launch
        return


    call Girl_Hide(WandaX) #call Rogue_Hide
    if Line == "L" or Line == "cum":
        show Wanda_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1
#            zoom 1 offset (0,0)
            ease 1 zoom 2.5 offset (70,240) #(-90,140) offset (150,80)
        with dissolve
    else:
        show Wanda_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1 zoom 2.5 offset (70,240) #(-90,140)
        with dissolve

    if Taboo and Line == "L":
            # Wanda gets started. . .
            if len(Present) >= 2:
                if Present[0] != WandaX:
                        "[WandaX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                elif Present[1] != WandaX:
                        "[WandaX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
            else:
                        "[WandaX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
    $ Speed = 1
    if Line == "L":
            if not WandaX.Blow:
                "[WandaX.Name] нерешительно стягивает с вас штаны и касается своим ртом вашей киски."
            else:
                "[WandaX.Name] наклоняется и начинает лизать вашу киску."

    if Line != "cum":
        $ Trigger = "cun"

    $ Player.Cock = 0
    show Wanda_Sprite:
        alpha 0
    if WandaX.Pose == "69":
            show Wanda_69_CUN zorder 150
    else:
            show Wanda_CUN_Animation zorder 150:
                pos (800,830)#(645,610)
    return

label Wanda_CUN_Reset: # The sequence to the Wanda animations from CUN to default
    if not renpy.showing("Wanda_CUN_Animation") and not renpy.showing("Wanda_69_CUN"):
        return
    call Girl_Hide(WandaX) #call Rogue_Hide
    $ Speed = 0

    show Wanda_Sprite at SpriteLoc(WandaX.SpriteLoc) zorder 150:
        zoom 2 offset (70,140) alpha 1
        pause .5
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Wanda_Sprite at SpriteLoc(WandaX.SpriteLoc) zorder WandaX.Layer:
        alpha 1 zoom 1 offset (0,0)
    $ WandaX.FaceChange("sexy")
    return

##End Wanda Cunnilingus Animations
## ////////////////////////////////                                                                                      ///////////////////////////////
## ////////////////////////////////                                                                                      ///////////////////////////////
## ////////////////////////////////                                                                                      ///////////////////////////////


## ////////////////////////////////                                                                                      ///////////////////////////////
## ////////////////////////////////                                                                                      ///////////////////////////////
## ////////////////////////////////                                                                                      ///////////////////////////////

image Wanda_Finger_Animation:
    # Core Animation for Fingering Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
        ConditionSwitch(                                                # backside of the hand
            "Speed == 1", "Wanda_Finger_1",
            "Speed >= 2", "Wanda_Finger_2",
            "True", "Wanda_Finger_0",
            ),
    anchor (0.5,0.5)#anchor (0.51, -1.3)
    offset (400,945)#700,1190
    zoom 0.8
    # end Core Animation for Fingering Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <

image Wanda_Finger_0:
    # Animation for Fingering Zero's pussy, static < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Wanda_Sprite"
            pos (350,-550)
            zoom 2.15
    contains:
            ConditionSwitch(
                "Player.Wet", "WandaBJFace/Wanda_Fingering_wet.png",
                "True", "WandaBJFace/[WandaX.skin_image.skin_path]Wanda_Fingering_Under.png",
                )
            anchor (0.5,0.6)
            pos (-5,50)#(20,50)
            xzoom -1

#            "Wanda_Finger_Under"
    contains:
            "Zero_Pussy"
#    contains:
#            "WandaBJFace/Wanda_Fingering_Over.png"
#            anchor (0.5,0.6)
#            pos (-5,50)#(20,50)
#            xzoom -1
#            "Wanda_Finger_Over"
    # end Animation for Fingering Zero's pussy, static < < < < < < < < < < < < < < < < < < < < < < < <

image Wanda_Finger_1:
    # Animation for Fingering Zero's pussy, slow < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Wanda_Sprite"
            pos (350,-550)
            zoom 2.15
            block:
                ease 0.5 ypos -540 #rotate 3   100
                pause 0.25
                ease 1.0 ypos -550 #rotate -3  40
                repeat
    contains:
            ConditionSwitch(
                "Player.Wet", "WandaBJFace/Wanda_Fingering_wet.png",
                "True", "WandaBJFace/[WandaX.skin_image.skin_path]Wanda_Fingering_Under.png",
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
#    contains:
#            "WandaBJFace/Wanda_Fingering_Over.png"
##            "Wanda_Finger_Over"
#            subpixel True
#        #    xpos 10
#            anchor (0.5,0.6)
#            xzoom -1
#            transform_anchor True
#            pos (-5,50)#(15,50)
#            rotate -5
#            block:
#                ease .5 pos (-10,115) rotate 0 #(40,65)   Bottom
#                pause 0.25
#                ease 1.0 pos (-5,40) rotate -5 #(40,0) Top                 pause 0.1
#                repeat
    # end Animation for Fingering Zero's pussy, slow < < < < < < < < < < < < < < < < < < < < < < < <

image Wanda_Finger_2:
    # Animation for Fingering Zero's pussy, fast < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Wanda_Sprite"
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
                "Player.Wet", "WandaBJFace/Wanda_Fingering_wet.png",
                "True", "WandaBJFace/[WandaX.skin_image.skin_path]Wanda_Fingering_Under.png",
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
#    contains:
#            "WandaBJFace/Wanda_Fingering_Over.png"
##            "Wanda_Finger_Over"
#            subpixel True
#            anchor (0.5,0.6)
#            xzoom -1
#            transform_anchor True
##            rotate -15
#            pos (-10,30)#(10,30)
#            block:
#                ease 0.15 ypos 125 #rotate 3   65
#                pause 0.1
#                ease 0.45 ypos 60 #rotate -3  30
#                pause 0.1
#                repeat
    # end Animation for Fingering Zero's pussy, fast < < < < < < < < < < < < < < < < < < < < < < < <

label Wanda_Finger_Launch(Line = Trigger):
    if renpy.showing("Wanda_Finger_Animation"):
        $ Trigger = "finger"
        return

    if Player.Male == 1:
        call Wanda_HJ_Launch
        return

    call Girl_Hide(WandaX) #call Rogue_Hide
    $ WandaX.Arms = 0
    $ WandaX.ArmPose = 2
    if not renpy.showing("Wanda_Sprite"):
        show Wanda_Sprite at SpriteLoc(WandaX.SpriteLoc) zorder 150:
            alpha 1 zoom 1.7 xpos 850 yoffset 200 #offset (-50,200)
        with dissolve
    show Wanda_Sprite at SpriteLoc(WandaX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 1.7 xpos 850 yoffset 200 #offset (-50,200)

    if Taboo and Line == "L":
        # Wanda gets started. . .
        if len(Present) >= 2:
            if Present[0] != WandaX:
                    "[WandaX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
            elif Present[1] != WandaX:
                    "[WandaX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
        else:
                    "[WandaX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
        if not WandaX.Hand and WandaX.Arms:
            "Когда вы стягиваете свои штаны, [WandaX.Name] снимает перчатки и нерешительно тянется к вашей киске. Затем она начинает грубо ласкать ее."
        else:
            "Затем она наклоняется и хватает ваш член."
    elif Line == "L":
        if not WandaX.Hand and WandaX.Arms:
            "Когда вы стягиваете свои штаны, [WandaX.Name] снимает перчатки и нерешительно тянется к вашей киске. Затем она начинает грубо ласкать ее."
        else:
            "[WandaX.Name] наклоняется и кладет руку вам на киску."
    else:
            "[WandaX.Name] наклоняется и кладет руку вам на киску."

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "finger"
    show Wanda_Sprite zorder WandaX.Layer:
        alpha 0
    show Wanda_Finger_Animation at SpriteLoc(WandaX.SpriteLoc) zorder 150 with fade
    return

label Wanda_Finger_Reset: # The sequence to the Wanda animations from handjob to default
    if not renpy.showing("Wanda_Finger_Animation"):
        return
    $ Speed = 0
    hide Wanda_Finger_Animation
    with dissolve
    call Girl_Hide(WandaX) #call Rogue_Hide
#    show Wanda_Sprite at SpriteLoc(WandaX.SpriteLoc) zorder WandaX.Layer:
#        alpha 1
#        zoom 1.7  xpos 850 yoffset 200
    show Wanda_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 yoffset 50
        pause .5
        ease .5 zoom 1 xpos WandaX.SpriteLoc yoffset 0
    show Wanda_Sprite at SpriteLoc(WandaX.SpriteLoc) zorder WandaX.Layer:
        alpha 1 zoom 1 xpos WandaX.SpriteLoc yoffset 0
    return

## ////////////////////////////////                                                                                      ///////////////////////////////
## ////////////////////////////////                                                                                      ///////////////////////////////
## ////////////////////////////////                                                                                      ///////////////////////////////


# Start Wanda 69 Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

image Wanda_69_Animation:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
                #Shows different upper body motion depending on events
#                "True", "Wanda_69_Anim1",
                "Speed == 2", "Wanda_69_Anim2",
                "Speed == 3", "Wanda_69_Anim3",
                "Speed == 4", "Wanda_69_Anim4",
                "Speed == 5", "Wanda_69_Anim5",
                "Speed == 6", "Wanda_69_Anim6",
                "Speed", "Wanda_69_Anim1",
                "True", "Wanda_69_Static",
                ),
        )
    align (0.6,0.0)
    pos (475,-800)#(475,-700)
    zoom 1.8#1/3

#Start Animations for Wanda's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Wanda 69 Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Wanda_69_Body:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Wanda_SexSprite
        (1120,840),

        (0,0), ConditionSwitch(
            #shirt layer
            "WandaX.Over == 'shirt' and WandaX.Uptop", "images/WandaSex/Wanda_69_Over_Shirt_Up.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #bra layer
            "not WandaX.Uptop", Null(),
            #if top's up
            "WandaX.Chest == 'bikini top'", "images/WandaSex/Wanda_69_Chest_Bikini.png",
            "WandaX.Chest == 'mesh top'", "images/WandaSex/Wanda_69_Chest_Mesh.png",
#            "WandaX.Chest == 'lace bra'", "images/WandaSex/Wanda_69_Chest_Lace.png",
            "WandaX.Chest", "images/WandaSex/Wanda_69_Chest_Bra.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #body
#            "WandaX.Arms", "images/WandaSex/Wanda_69_BodyG.png",
            "True", "images/WandaSex/Wanda_69_Body.png",
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "WandaX.Water", "images/WandaSex/Wanda_69_Water_Body.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #bra layer
            "WandaX.Uptop", Null(),
            #if top's up
            "WandaX.Chest == 'bikini top'", "images/WandaSex/Wanda_69_Chest_Bikini.png",
            "WandaX.Chest == 'mesh top'", "images/WandaSex/Wanda_69_Chest_Mesh.png",
            "WandaX.Chest == 'lace bra'", "images/WandaSex/Wanda_69_Chest_Lace.png",
            "WandaX.Chest", "images/WandaSex/Wanda_69_Chest_Bra.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #dress layer
            "WandaX.Uptop", ConditionSwitch(
                    # ring pierce
                    "WandaX.Legs == 'dress'", "images/WandaSex/Wanda_69_Over_Dress_Up.png",
                    "True", Null(),
                    ),
            "WandaX.Legs == 'dress'", "images/WandaSex/Wanda_69_Over_Dress.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #shirt layer
            "WandaX.Uptop", ConditionSwitch(
                    # ring pierce
#                    "WandaX.Over == 'towel'", Null(),
#                    "WandaX.Over == 'shirt'", Null(),
                    "WandaX.Over == 'purple top'", "images/WandaSex/Wanda_69_Over_Purple_Up.png",
                    "WandaX.Over == 'corset'", "images/WandaSex/Wanda_69_Over_Corset_Up.png",
                    "True", Null(),
                    ),
            "WandaX.Over == 'towel'", "images/WandaSex/Wanda_69_Over_Towel.png",
            "WandaX.Over == 'purple top'", "images/WandaSex/Wanda_69_Over_Purple.png",
            "WandaX.Over == 'shirt'", "images/WandaSex/Wanda_69_Over_Shirt.png",
            "WandaX.Over == 'corset'", "images/WandaSex/Wanda_69_Over_Corset.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #piercings
#            "not WandaX.Pierce", Null(),
            "WandaX.Pierce == 'ring'", ConditionSwitch(
                    # ring pierce
                    "WandaX.Uptop", "images/WandaSex/Wanda_69_Pierce_Tits_R.png",

                    "WandaX.Over == 'towel'", "images/WandaSex/Wanda_69_Pierce_Tits_R_Black.png",
                    "WandaX.Over == 'purple top'", "images/WandaSex/Wanda_69_Pierce_Tits_R_Purp.png",
                    "WandaX.Over", "images/WandaSex/Wanda_69_Pierce_Tits_R_Red.png", #Shirt or Corset
                    "WandaX.Legs == 'dress'", "images/WandaSex/Wanda_69_Pierce_Tits_R_Black.png",

                    "WandaX.Chest == 'mesh top'", "images/WandaSex/Wanda_69_Pierce_Tits_R_Mesh.png",
                    "WandaX.Chest == 'lace bra'", "images/WandaSex/Wanda_69_Pierce_Tits_R_Lace.png",
                    "WandaX.Chest", "images/WandaSex/Wanda_69_Pierce_Tits_R_Red.png",

                    "True", "images/WandaSex/Wanda_69_Pierce_Tits_R.png",
                    ),

            "WandaX.Pierce", ConditionSwitch( #barbells
                    "WandaX.Uptop", "images/WandaSex/Wanda_69_Pierce_Tits_B.png",

                    "WandaX.Over == 'towel'", "images/WandaSex/Wanda_69_Pierce_Tits_B_Black.png",
                    "WandaX.Over == 'purple top'", "images/WandaSex/Wanda_69_Pierce_Tits_B_Purp.png",
                    "WandaX.Over", "images/WandaSex/Wanda_69_Pierce_Tits_B_Red.png", #Shirt or Corset
                    "WandaX.Legs == 'dress'", "images/WandaSex/Wanda_69_Pierce_Tits_B_Black.png",

                    "WandaX.Chest == 'mesh top'", "images/WandaSex/Wanda_69_Pierce_Tits_B_Mesh.png",
                    "WandaX.Chest == 'lace bra'", "images/WandaSex/Wanda_69_Pierce_Tits_B_Lace.png",
                    "WandaX.Chest", "images/WandaSex/Wanda_69_Pierce_Tits_B_Red.png",

                    "True", "images/WandaSex/Wanda_69_Pierce_Tits_B.png",
                    ),
            "WandaX.Lust < 50 and not WandaX.OCount", Null(),                           #nips only poke at high lust
            "WandaX.Uptop", "images/WandaSex/Wanda_69_Nips.png",

            "WandaX.Over == 'towel'", "images/WandaSex/Wanda_69_Nips_Black.png",
            "WandaX.Over == 'purple top'", "images/WandaSex/Wanda_69_Nips_Purp.png",
            "WandaX.Over", "images/WandaSex/Wanda_69_Nips_Red.png", #Shirt or Corset
            "WandaX.Legs == 'dress'", "images/WandaSex/Wanda_69_Nips_Black.png",

            "WandaX.Chest == 'mesh top'", "images/WandaSex/Wanda_69_Nips_Mesh.png",
            "WandaX.Chest == 'lace bra'", "images/WandaSex/Wanda_69_Nips_Lace.png",
            "WandaX.Chest", "images/WandaSex/Wanda_69_Nips_Red.png",

            "True", "images/WandaSex/Wanda_69_Nips.png",
            ),

        (0,0),ConditionSwitch(
            #Outside Spunk
            "'tits' in WandaX.Spunk and Player.Male", "images/WandaSex/Wanda_69_Spunk_Tits.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'belly' in WandaX.Spunk and Player.Male", "images/WandaSex/Wanda_69_Spunk_Belly.png",
            "True", Null(),
            ),
#        (0,0), "images/WandaSex/Wanda_Sex_HeadRef.png",
        )
    zoom 1.0#.9#.8
    offset (15,80)#(85,150)#(75,30)#(145,150)#(250,210)#(175,175)
#    yoffset -163
# End Wanda 69 Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Wanda 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Wanda_69_Head:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Wanda_SexSprite
        (1120,840),
        (0,0), ConditionSwitch(
            #tongue
            "renpy.showing('Wanda_69_CUN') and Speed != 3", "images/WandaSex/Wanda_69_Tongue.png",
            "Speed == 1", "images/WandaSex/Wanda_69_Tongue.png",
            "True", Null(),
            ),
        (0,0), "images/WandaSex/Wanda_69_Head.png",
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'mouth' in WandaX.Spunk and Player.Male", "images/WandaSex/Wanda_69_Spunk_Mouth.png",
            "('mouth' in WandaX.Spunk or 'chin' in WandaX.Spunk) and not Player.Male", "images/WandaSex/Wanda_69_WetFace.png",
            "True", Null(),
            ),

        (0,0),ConditionSwitch(
            #Outside Spunk
            "'chin' in WandaX.Spunk and Player.Male", "images/WandaSex/Wanda_69_Spunk_Chin.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Hair over
#            "Speed == 1 and Player.Male", Null(),
#            "Speed == 4 and Player.Male", Null(),
#            "Speed == 6 and Player.Male", Null(),
#            "WandaX.Water or WandaX.Hair == 'wet'", "images/WandaSex/Wanda_69_Hair_Wet.png",
#            "not Player.Male and ('hair' in WandaX.Spunk or 'facial' in WandaX.Spunk)","images/WandaSex/Wanda_69_Hair_Pony.png",

##            "WandaX.Hair == 'long'", "images/WandaSex/Wanda_69_Hair_Long_Over.png",
#            "True", Null(),
#            ),

#        (0,0), "images/WandaSex/Wanda_69_Hair_Short.png",
        (0,0), ConditionSwitch(
            #Hair over
            "Speed == 1", Null(), # and Player.Male", Null(),
            "Speed == 4", Null(), # and Player.Male", Null(),
            "Speed == 6", Null(), # and Player.Male", Null(),
            "(WandaX.Hair == 'long' and WandaX.Water) or WandaX.Hair == 'wetlong'", "images/WandaSex/Wanda_69_Hair_Wet.png",
            "WandaX.Hair == 'long' and not Player.Male and ('hair' in WandaX.Spunk or 'facial' in WandaX.Spunk)","images/WandaSex/Wanda_69_Hair_Wet.png",
            "WandaX.Hair == 'long'", "images/WandaSex/Wanda_69_Hair_Long.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #neck over
            "(Speed == 0 or Speed == 2 or Speed == 3 or Speed == 5) and Player.Male", "images/WandaSex/Wanda_69_Neck.png",
            "not Player.Male", "images/WandaSex/Wanda_69_Neck.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #collar
            "not WandaX.Neck", Null(),
            "(Speed == 0 or Speed == 2 or Speed == 3 or Speed == 5) and Player.Male", "images/WandaSex/Wanda_69_Collar.png",
            "not Player.Male", "images/WandaSex/Wanda_69_Collar.png",
            "True", Null(),
            ),
        )
    zoom .8
    offset (153,260)#(0,0)#(145,150)
#    offset (0,0)#(175,135)#(175,175)
#    yoffset -163
# End Wanda 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Wanda 69 Pose Hair Over / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Wanda_69_HairOver:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Wanda_SexSprite
        (1120,840),
        (0,0), ConditionSwitch(
            #Hair over
            "(WandaX.Hair == 'long' and WandaX.Water) or WandaX.Hair == 'wetlong'", "images/WandaSex/Wanda_69_Hair_Wet.png",
            "WandaX.Hair == 'long' and not Player.Male and ('hair' in WandaX.Spunk or 'facial' in WandaX.Spunk)","images/WandaSex/Wanda_69_Hair_Wet.png",
            "WandaX.Hair == 'long'", "images/WandaSex/Wanda_69_Hair_Long.png",

#            "WandaX.Water or WandaX.Hair == 'wet'", "images/WandaSex/Wanda_69_Hair_Wet.png",
#            "not Player.Male and ('hair' in WandaX.Spunk or 'facial' in WandaX.Spunk)","images/WandaSex/Wanda_69_Hair_Wet.png",
#            "True", "images/WandaSex/Wanda_69_Hair_Short.png",
            "True", Null(),
            ),

        (0,0), "images/WandaSex/Wanda_69_Neck.png",
        (0,0), ConditionSwitch(
            #collar
            "WandaX.Neck", "images/WandaSex/Wanda_69_Collar.png",     # == 'spiked collar'
            "True", Null(),
            ),
        )
    zoom .8
    offset (153,260)#(0,0)#(145,150)
#    offset (0,0)#(175,135)#(180,100)
#    yoffset -163
# End Wanda 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Wanda 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Wanda_69_HairBack:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Wanda_SexSprite
        (1120,840),
        (0,0), ConditionSwitch(
            #Hair under
#            "Speed == 1 and Player.Male", Null(),
#            "Speed == 4 and Player.Male", Null(),
#            "Speed == 6 and Player.Male", Null(),
            "(WandaX.Hair == 'long' and WandaX.Water) or WandaX.Hair == 'wetlong'", "images/WandaSex/Wanda_69_Hair_Wet_Under.png",
            "WandaX.Hair == 'long' and not Player.Male and ('hair' in WandaX.Spunk or 'facial' in WandaX.Spunk)","images/WandaSex/Wanda_69_Hair_Wet_Under.png",
            "WandaX.Hair == 'long'", "images/WandaSex/Wanda_69_Hair_Long_Under.png",

            "WandaX.Water or WandaX.Hair == 'wet'", "images/WandaSex/Wanda_69_Hair_Short_Wet_Under.png",
            "not Player.Male and ('hair' in WandaX.Spunk or 'facial' in WandaX.Spunk)","images/WandaSex/Wanda_69_Hair_Short_Wet_Under.png",
            "True", "images/WandaSex/Wanda_69_Hair_Short_Under.png",
            ),
        (0,0), ConditionSwitch(
            #Hair over
#            "renpy.showing('Wanda_TJ_Animation')", Null(),
#            "WandaX.Hair == 'blonde'", "images/WandaSex/Wanda_69_Hair_Blonde_Under.png",
#            "WandaX.Hair == 'long' or WandaX.Hair == 'wetlong'", "images/WandaSex/Wanda_69_Hair_Long_Under.png",
#            "WandaX.Hair == 'wet' or WandaX.Hair == 'wetlong' or WandaX.Water", "images/WandaSex/Wanda_69_Hair_Long.png",
#            "not Player.Male and 'facial' in WandaX.Spunk","images/WandaSex/Wanda_Sprite_Hair_Wet.png",
            "True", Null(),#"images/WandaSex/Wanda_69_Hair_Under.png",
            ),
        )
    zoom .8
    offset (153,260)#(145,150)#(175,135)#(175,175)
#    yoffset -163
# End Wanda 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#image Wanda_Sex_Legs = LiveComposite(
image Wanda_69_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Wanda_SexSprite
        (1120,840),
#        (0,0), "images/WandaSex/Wanda_69_Hips.png",
        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            "WandaX.Legs == 'dress'", "images/WandaSex/Wanda_69_Legs_Dress_Under.png",
            "WandaX.Legs == 'skirt'", "images/WandaSex/Wanda_69_Legs_Skirt_Under.png",
            "WandaX.Over == 'towel' and not WandaX.Uptop", "images/WandaSex/Wanda_69_Legs_Towel_Under.png",
            "WandaX.Hose == 'stockings and garterbelt' or WandaX.Hose == 'garterbelt'", "images/WandaSex/Wanda_69_Hose_Garter_Under.png",
            "WandaX.Hose == 'pantyhose' or WandaX.Hose == 'ripped pantyhose'", "images/WandaSex/Wanda_69_Under.png",
            "True", Null(),
            ),
        (0,0), "images/WandaSex/Wanda_69_Legs.png",                                                         #Legs Base
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "WandaX.Water", "images/WandaSex/Wanda_Sex_Water_Legs.png",
            "True", Null(),
            ),

        (0,0), "Wanda_69_Anus",                                                                          #Anus Composite

        (0,0), "Wanda_69_Pussy",                                                                         #Pussy Composite

        (0,0), ConditionSwitch(
            #hose layer
            "WandaX.Hose == 'stockings and garterbelt'", "images/WandaSex/Wanda_69_Hose_StockingsGarter.png",
            "WandaX.Hose == 'garterbelt'", "images/WandaSex/Wanda_69_Hose_Garter.png",
            "WandaX.Hose == 'stockings'", "images/WandaSex/Wanda_69_Hose_Stockings.png",
            "WandaX.Hose == 'socks'", "images/WandaSex/Wanda_69_Hose_Socks.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Panties if up
            "WandaX.PantiesDown", ConditionSwitch(
                    "WandaX.Panties == 'lace panties'", "images/WandaSex/Wanda_69_Panties_Bikini_Down.png",
                    "WandaX.Panties == 'bikini bottoms'", "images/WandaSex/Wanda_69_Panties_Bikini_Down.png",
        #            "WandaX.Panties and WandaX.Wet", "images/WandaSex/Wanda_69_Panties_Gray_Up_Wet.png",
                    "WandaX.Panties", "images/WandaSex/Wanda_69_Panties_Gray_Down.png",
                    "True", Null(),
                    ),
            "WandaX.Panties == 'lace panties'", "images/WandaSex/Wanda_69_Panties_Lace.png",
            "WandaX.Panties == 'bikini bottoms'", "images/WandaSex/Wanda_69_Panties_Bikini.png",
#            "WandaX.Panties and WandaX.Wet", "images/WandaSex/Wanda_69_Panties_Gray_Wet.png",
            "WandaX.Panties", "images/WandaSex/Wanda_69_Panties_Gray.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #hose layer
            "WandaX.Panties and WandaX.PantiesDown", Null(),
            "WandaX.Hose == 'pantyhose'", "images/WandaSex/Wanda_69_Hose_Pantyhose.png",
            "WandaX.Hose == 'ripped pantyhose'", "images/WandaSex/Wanda_69_Hose_Pantyhose_Holed.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs Layer
            "WandaX.Upskirt", ConditionSwitch(
#                    "WandaX.Legs == 'shorts' and WandaX.Wet > 1", "images/WandaSex/Wanda_69_Legs_Shorts_Wet.png",
                    "WandaX.Legs == 'shorts'", "images/WandaSex/Wanda_69_Legs_Shorts_Down.png",
#                    "WandaX.Legs == 'pants' and WandaX.Wet > 1", "images/WandaSex/Wanda_69_Legs_Yoga_Wet.png",
                    "WandaX.Legs == 'pants'", "images/WandaSex/Wanda_69_Legs_Pants_Down.png",
                    "True", Null(),
                    ),
#            "WandaX.Legs == 'shorts' and WandaX.Wet > 1", "images/WandaSex/Wanda_69_Legs_Shorts_Wet.png",
            "WandaX.Legs == 'shorts'", "images/WandaSex/Wanda_69_Legs_Shorts.png",
#            "WandaX.Legs == 'pants' and WandaX.Wet > 1", "images/WandaSex/Wanda_69_Legs_Yoga_Wet.png",
            "WandaX.Legs == 'pants'", "images/WandaSex/Wanda_69_Legs_Pants.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Dress Layer
            "WandaX.Legs == 'skirt'", "images/WandaSex/Wanda_69_Legs_Skirt.png",
            "WandaX.Legs == 'dress'", "images/WandaSex/Wanda_69_Legs_Dress.png",
            "WandaX.Over == 'towel' and not WandaX.Uptop", "images/WandaSex/Wanda_69_Legs_Dress.png",
#            "WandaX.Upskirt", Null(),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Piercings over pants and pantyhose
            "not WandaX.Pierce", Null(),
            "WandaX.Pierce == 'ring'",ConditionSwitch(
                    #If she has panties down. . .
#                    "Player.Sprite and Player.Cock == 'in'", "images/WandaSex/Wanda_Sex_Pussy_RingF.png",

                    "WandaX.Legs and WandaX.Legs != 'dress' and WandaX.Legs != 'skirt' and not WandaX.Upskirt", "images/WandaSex/Wanda_69_Pierce_Pussy_R_Black.png",

                    "WandaX.PantiesDown", "images/WandaSex/Wanda_69_Pierce_Pussy_R.png",
                    "WandaX.Panties == 'lace panties'", "images/WandaSex/Wanda_69_Pierce_Pussy_R_Lace.png",
                    "WandaX.Panties == 'bikini bottoms'", "images/WandaSex/Wanda_69_Pierce_Pussy_R_Red.png",
                    "WandaX.Hose == 'pantyhose' and not (WandaX.Panties and WandaX.PantiesDown)", "images/WandaSex/Wanda_69_Pierce_Pussy_R_Red.png",
                    "WandaX.Panties", "images/WandaSex/Wanda_69_Pierce_Pussy_R_Gray.png",

                    "True", "images/WandaSex/Wanda_69_Pierce_Pussy_R.png",
                    ),
            #else, it's barbell
#            "Player.Sprite and Player.Cock == 'in'", "images/WandaSex/Wanda_Sex_Pussy_BarbellF.png",

            "WandaX.Legs and WandaX.Legs != 'dress' and WandaX.Legs != 'skirt' and not WandaX.Upskirt", "images/WandaSex/Wanda_69_Pierce_Pussy_B_Black.png",

            "WandaX.PantiesDown", "images/WandaSex/Wanda_69_Pierce_Pussy_B.png",
            "WandaX.Panties == 'lace panties'", "images/WandaSex/Wanda_69_Pierce_Pussy_B_Lace.png",
            "WandaX.Panties == 'bikini bottoms'", "images/WandaSex/Wanda_69_Pierce_Pussy_B_Red.png",
            "WandaX.Hose == 'pantyhose' and not (WandaX.Panties and WandaX.PantiesDown)", "images/WandaSex/Wanda_69_Pierce_Pussy_B_Red.png",
            "WandaX.Panties", "images/WandaSex/Wanda_69_Pierce_Pussy_B_Gray.png",

            "True", "images/WandaSex/Wanda_69_Pierce_Pussy_B.png",
            ),

#        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
#            "'belly' in WandaX.Spunk and Player.Male", "images/WandaSex/Wanda_Sex_Spunk_Pelvis.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer
#            "not Player.Sprite or Player.Cock != 'out'", Null(),
#            "Speed >= 2", "Wanda_Hotdog_Zero_Anim2",
#            "Speed", "Wanda_Hotdog_Zero_Anim1",
#            "True", "Wanda_Hotdog_Zero_Anim0",
#            ),

        (0,0), ConditionSwitch(
            #pussy licking animation
#            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy' or Trigger2 == 'lick pussy'", "Wanda_69_Lick_Pussy",
            "Trigger == 'lick ass' or Trigger2 == 'lick ass'", "Wanda_69_Lick_Ass",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy fondling animation
            "WandaX.Offhand == 'fondle pussy' and WandaX.Lust > 60 and not (Player.Sprite)",  At("WandaFingerHand", GirlFingerPussyX()), #"Betsy_Sex_Mast2",
            "WandaX.Offhand == 'fondle pussy'", At("WandaMastHand", GirlGropePussyX()), #"Betsy_Sex_Mast",
#            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Wanda_69_Fondle_Pussy",
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer
#            "not Player.Sprite or Player.Cock != 'foot'", Null(),
#            "Speed >= 2", "Wanda_Footcock_Zero_Anim2",
#            "Speed", "Wanda_Footcock_Zero_Anim1",
#            "True", "Wanda_Footcock_Static",
#            ),
#        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer
#            "not Player.Sprite or Player.Cock != 'foot'", Null(),
#            "Speed >= 2", At("Wanda_Footcock", Wanda_Footcock_Zero_Anim2A()),
#            "Speed", At("Wanda_Footcock", Wanda_Footcock_Zero_Anim1A()),
#            "True", At("Wanda_Footcock", Wanda_Footcock_StaticA()),
#            ),
#        (0,0), ConditionSwitch(                                                                                 #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
#            "renpy.showing('Anal_Plug_In_Sex') or renpy.showing('Anal_Plug_Out_Sex')", AlphaMask("Wanda_69_Feet", "images/WandaSex/Wanda_69_FeetMask.png"),
#            "not Speed", "Wanda_69_Feet",
#            "Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Wanda_69_Feet", "images/WandaSex/Wanda_69_FeetMask.png"),
#            "True", "Wanda_69_Feet",
#            ),
#        (0,0), ConditionSwitch(                                                                                 #Legs Layer
#            "WandaX.Upskirt", Null(),
#            "WandaX.Legs == 'dress'", "images/WandaSex/Wanda_69_Feet_Dress.png",
#            "True", Null(),
#            ),
        )
    offset (10,25)#(15,80)

#image Wanda_69_Feet = LiveComposite(
#        #the lower legs used in the sex pose, referenced by Wanda_Sex_Legs
#        (1120,840),
##        (0,0), "images/WandaSex/Wanda_Sex_Feet.png",                                                         #Legs Base
##        (0,0), ConditionSwitch(                                                                                 #Wet look
##            "WandaX.Water", "images/WandaSex/Wanda_Sex_Water_Feet.png",
##            "True", Null(),
##            ),

#        (0,0), ConditionSwitch(
#            #hose layer
#            "WandaX.Legs and not WandaX.Upskirt and WandaX.Legs != 'blue skirt' and WandaX.Legs != 'shorts'",ConditionSwitch(
#                    #If she has pants on, I need alternate kneesocks to not clip through knees
#                    "WandaX.Hose == 'stockings and garterbelt'", "images/WandaSex/Wanda_69_Feet_Stockings.png",
#                    "WandaX.Hose == 'stockings'", "images/WandaSex/Wanda_69_Feet_Stockings.png",
#                    "WandaX.Hose == 'knee stockings'", "images/WandaSex/Wanda_69_Feet_Kneesocks.png",
#                    "WandaX.Panties and WandaX.PantiesDown", "images/WandaSex/Wanda_69_Feet.png",
#                    "WandaX.Hose == 'pantyhose'", "images/WandaSex/Wanda_69_Feet_Stockings.png",
#                    "WandaX.Hose == 'ripped pantyhose'", "images/WandaSex/Wanda_69_Feet_Stockings_Holed.png",
#                    "True", "images/WandaSex/Wanda_69_Feet.png",
#                    ),
##            "WandaX.Legs and (not WandaX.Upskirt and WandaX.Legs != 'blue skirt' and WandaX.Legs != 'shorts') and WandaX.Hose == 'stockings and garterbelt'", "images/WandaSex/Wanda_Sex_Hose_Stockings_FeetP.png",
##            "WandaX.Legs and (not WandaX.Upskirt and WandaX.Legs != 'blue skirt' and WandaX.Legs != 'blue skirt') and WandaX.Hose == 'stockings'", "images/WandaSex/Wanda_Sex_Hose_Stockings_FeetP.png",
##            "WandaX.Legs and (not WandaX.Upskirt and WandaX.Legs != 'blue skirt' and WandaX.Legs != 'blue skirt') and WandaX.Hose == 'knee stockings'", "images/WandaSex/Wanda_Sex_Hose_Stockings_FeetP.png",
#            "WandaX.Hose == 'stockings' or WandaX.Hose == 'stockings and garterbelt'", "images/WandaSex/Wanda_69_Feet_Stockings.png",
#            "WandaX.Hose == 'knee stockings'", "images/WandaSex/Wanda_69_Feet_Kneesocks.png",
#            "WandaX.Panties and WandaX.PantiesDown", Null(),
#            "WandaX.Hose == 'pantyhose'", "images/WandaSex/Wanda_69_Feet_Stockings.png",
##            "WandaX.Legs and (not WandaX.Upskirt and WandaX.Legs != 'blue skirt' and WandaX.Legs != 'blue skirt') and WandaX.Hose == 'ripped pantyhose'", "images/WandaSex/Wanda_Sex_Hose_RippedPantyhose_FeetP.png",
#            "WandaX.Hose == 'ripped pantyhose'", "images/WandaSex/Wanda_69_Feet_Stockings_Holed.png",
#            "True", "images/WandaSex/Wanda_69_Feet.png",
#            ),

#        (0,0), ConditionSwitch(                                                                                 #Legs Layer
#            "WandaX.Upskirt", Null(),
#            "WandaX.Legs == 'dress'", "images/WandaSex/Wanda_69_Feet_Dress.png",
#            "WandaX.Legs == 'capris'", "images/WandaSex/Wanda_69_Feet_Blue.png",
#            "WandaX.Legs == 'black jeans'", "images/WandaSex/Wanda_69_Feet_Black.png",
#            "WandaX.Legs == 'yoga pants'", "images/WandaSex/Wanda_69_Feet_Yoga.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #spunk
#            "'feet' in WandaX.Spunk", "images/WandaSex/Wanda_Sex_Spunk_Feet.png",
#            "True", Null(),
#            ),
#        )


# Start Wanda 69 Pose Pussy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Wanda_69_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).

    contains:
            # The background plate of her pussy
            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/WandaSex/Wanda_Sex_Pussy_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed", "Wanda_Sex_Heading_Pussy",
#                "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/WandaSex/Wanda_Sex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/WandaSex/Wanda_69_Pussy_Open.png",
                "WandaX.Offhand == 'fondle pussy' and WandaX.Lust > 60", "images/WandaSex/Wanda_69_Pussy_Open.png",
                "True", "images/WandaSex/Wanda_69_Pussy_Closed.png",
                )
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "not WandaX.Wet", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/JubesSex/Jubes_Sex_WetPussy_F.png",
                "True", "images/BetsySex/Betsy_69_Water_Pussy.png",
                )
            xzoom -1
#            offset (5,0)
    contains:
            # pubes
            ConditionSwitch(
                "not WandaX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", Recolor("Wanda", "Pubes", "images/WandaSex/Wanda_Sex_Pubes_Fucking.png"),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 1", Recolor("Wanda", "Pubes", "images/WandaSex/Wanda_Sex_Pubes_Fucking.png"),
#                "Player.Sprite and Player.Cock == 'in'", "images/WandaSex/Wanda_Sex_Pubes_Open.png",
#                "Player.Sprite and Player.Cock == 'out'", "images/WandaSex/Wanda_Sex_Pubes_Open.png",
#                "Trigger == 'lick pussy'", "images/WandaSex/Wanda_69_Pubes_Open.png",
#                "WandaX.Offhand == 'fondle pussy' and WandaX.Lust > 60", "images/WandaSex/Wanda_69_Pubes_Open.png",
                "True", "images/WandaSex/Wanda_69_Pubes.png",
                )
    contains:
            #Wet
            ConditionSwitch(
                "not WandaX.Wet", Null(),
                "(WandaX.Legs == 'yoga pants' or WandaX.Legs == 'shorts') and not WandaX.Upskirt", Null(),
                "WandaX.Panties and not WandaX.PantiesDown", Null(),
#                "True", "Spunk_Drip_69",
                "True", AlphaMask("Wet_Drip_69","images/BetsySex/Betsy_69_Mask_Pussy.png"),
                )
            offset (15,0)
    contains:
            #Spunk
            ConditionSwitch(
                "'in' not in WandaX.Spunk or not Player.Male", Null(),
                "(WandaX.Legs == 'yoga pants' or WandaX.Legs == 'shorts') and not WandaX.Upskirt", Null(),
                "WandaX.Panties and not WandaX.PantiesDown", Null(),
#                "True", "Spunk_Drip_69",
                "True", AlphaMask("Spunk_Drip_69","images/BetsySex/Betsy_69_Mask_Pussy.png"),
                )
            offset (15,0)

    contains:
            ConditionSwitch(
                #Outside Spunk
#                "'in' in WandaX.Spunk and Player.Sprite and Player.Cock == 'in' and Speed and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_PussyF.png",
                "'in' in WandaX.Spunk and Player.Male", "images/BetsySex/Betsy_69_Spunk_Pussy.png",
                "True", Null(),
                )
#            offset (0,-15)
#    contains:
#            #Spunk under penis
#            ConditionSwitch(
#                "'in' in WandaX.Spunk", "images/WandaSex/Wanda_Sex_Spunk_Puss_Under.png",
#                "True", Null(),
#                )
#    contains:
#            #hose layer
#            ConditionSwitch(
#                "WandaX.Panties and WandaX.PantiesDown", Null(),
#                "WandaX.Hose == 'ripped pantyhose' and ShowFeet", Recolor("Wanda", "Hose", "images/WandaSex/Wanda_Sex_Hose_Pantyhose_Holed.png"),
#                "WandaX.Hose == 'ripped pantyhose'", Recolor("Wanda", "Hose", "images/WandaSex/Wanda_Sex_Hose_Pantyhose_Holed.png"),
#                "True", Null(),
#                ),
#    contains:
#            # The animation of Zero's moving penis, masked by her pussy shape
#            ConditionSwitch(
##                "not Player.Sprite", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 3", AlphaMask("Wanda_Sex_Fucking_Zero_Anim3", "Wanda_Sex_Fucking_Mask"),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", AlphaMask("Wanda_Sex_Fucking_Zero_Anim2", "Wanda_Sex_Fucking_Mask"),
#                "Player.Sprite and Player.Cock == 'in' and Speed == 1", AlphaMask("Wanda_Sex_Fucking_Zero_Anim1", "Wanda_Sex_Heading_Mask"),
#                "Player.Sprite and Player.Cock == 'in'", "Wanda_Sex_Fucking_Zero_Anim0",
#                "True", Null(),
#                )
#    contains:
#            #Piercings
#            ConditionSwitch(
#                "WandaX.Pierce == 'barbell' and Player.Sprite and Player.Cock == 'in' and Speed", "images/WandaSex/Wanda_Sex_Pierce_Pussy_BarbellF.png",
#                "WandaX.Pierce == 'ring' and Player.Sprite and Player.Cock == 'in' and Speed", "images/WandaSex/Wanda_Sex_Pierce_Pussy_RingF.png",
#                "WandaX.Pierce == 'barbell'", "images/WandaSex/Wanda_Sex_Pierce_Pussy_Barbell.png",
#                "WandaX.Pierce == 'ring'", "images/WandaSex/Wanda_Sex_Pierce_Pussy_Ring.png",
#                "True", Null(),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed == 1", "Wanda_Pussy_Spunk_Heading",
#                "True", Null(),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "Speed == 1", Null(),
#                "'in' not in WandaX.Spunk or not Player.Sprite or Player.Cock != 'in' or not Speed or not Player.Male", Null(),
##                "Speed <= 1", Null(), #"Wanda_Pussy_Spunk_Heading",
#                "True", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
#                )

    #End Wanda Pussy composite


image Wanda_69_Lick_Pussy:
        "Lick_AnimF"
        zoom 0.6
        rotate 180
        offset (515,520)#(535,500
image Wanda_69_Lick_Ass:
        "Lick_AnimF"
        zoom 0.6
        rotate 180
        offset (515,580)#(535,580)

image Wanda_69_Fondle_Pussy:
        "GropePussy_Wanda"
        xzoom -1.3
        yzoom 1.3
#        rotate 180
        offset(-610,-300) #(-710,-300)
#        block:
#            ease 1 offset(-1000,0) #(535,500)
#            ease 1 offset(-1000,-1000) #(535,500)
#            ease 1 offset(0,-1000) #(535,500)
#            ease 1 offset(0,0) #(535,500)
#            repeat

image Wanda_69_Fondle_Pussy:
        "GropePussy_Wanda"
        xzoom -1.5
        yzoom 1.5
        offset(-710,-300) #(-890,-300)
#        block:
#            ease 1 offset(-1000,0) #(535,500)
#            ease 1 offset(-1000,-1000) #(535,500)
#            ease 1 offset(0,-1000) #(535,500)
#            ease 1 offset(0,0) #(535,500)
#            repeat

image Wanda_69_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/JubesSex/Jubes_Sex_Anal.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/JubesSex/Jubes_Sex_Anal.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/WandaSex/Wanda_Sex_Anus.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/WandaSex/Wanda_Sex_Anus.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed", "Wanda_Sex_Anal_Heading",
#            "Player.Sprite and Player.Cock == 'anal'", "Wanda_Sex_Anal_Tip",
            "WandaX.Plug", "images/PlugBase_Sex.png",
            "WandaX.Loose > 2", "Wanda_Gape_Anal_69",
#            "WandaX.Loose", "images/WandaSex/Wanda_Sex_Hole_Loose.png",
            "True", "images/WandaSex/Wanda_69_Anus.png",
            "True", Null(),
            )
    contains:
            #Spunk under penis
            ConditionSwitch(
                "'anal' not in WandaX.Spunk or not Player.Male", Null(),
#                "Player.Sprite and Player.Cock != 'anal' and Speed >= 1", "images/WandaSex/Wanda_Sex_Spunk_Anal_Under.png",
#                "Player.Sprite and Player.Cock == 'anal' and Speed == 1", "Wanda_Sex_Anal_Spunk_Heading_Under",
                "True", "images/BetsySex/Betsy_69_Spunk_Ass.png",
                )
            offset (-8,10)#(-8,-5)
#    contains:
#            # The animation of Zero's moving penis, masked by her anus shape
#            ConditionSwitch(
#                "not Player.Sprite or Player.Cock != 'anal'", Null(),
#                "Speed >= 3",  AlphaMask("Wanda_Sex_Anal_Zero_Anim3", "Wanda_Sex_Anal_MaskF"),
#                "Speed >= 2", AlphaMask("Wanda_Sex_Anal_Zero_Anim2", "Wanda_Sex_Anal_MaskF"),
#                "Speed", AlphaMask("Wanda_Sex_Anal_Zero_Anim1", "Wanda_Sex_Anal_Mask"),
#                "True", AlphaMask("Wanda_Sex_Anal_Zero_Anim0", "Wanda_Sex_Anal_Mask"),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "'anal' not in WandaX.Spunk or not Player.Sprite or Player.Cock != 'anal' or not Speed or not Player.Male", Null(),
#                "Speed == 1", "Wanda_Sex_Anal_Spunk_Heading_Over",
#                "True", "Wanda_Sex_Anal_Spunk",
#                )

image Wanda_Gape_Anal_Sex2:
        #removing an anal plug
        contains:
            #Hole
            "images/WandaSex/Wanda_69_Anus_Gape.png"
            transform_anchor True
            subpixel True
            anchor (730,700)#(560,620)
            offset (730,700)#(560,617)
            zoom .30 # tight
            block:
                ease 3 zoom .40 #in.87
                ease 3 zoom .30 #out
                repeat

image Wanda_Gape_Anal_69:
        "Wanda_Gape_Anal_Sex2"
#        xzoom -1.5
#        yzoom 1.5
        offset(-175,-200) #(-890,-300)

#Start Animations for Wanda's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Wanda_69_Static:
        #this is the animation for Wanda's hairback during 69, Speed 0 (static)
        contains:
            subpixel True
            "Wanda_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-125) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-130) #top -130
#                pause .5
                ease 1.25 pos (0,-125) #bottom -125
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
            offset (695,950)#(675,900)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Wanda's head during 69, Speed 0 (static)
        contains:
            subpixel True
            "Wanda_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-125) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-130) #top -130
#                pause .5
                ease 1.25 pos (0,-125) #bottom -125
                repeat
        #this is the animation for Wanda's upper body during 69, Speed 0 (static)
#        contains:
#            "Wanda_69_Tits"
#            subpixel True
#            rotate 180
##            zoom .65
#            pos (0,-35) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                pause .25
#                easein 1.5 pos (0,-40) #top
#                pause .25
#                ease 1 pos (0,-35) #bottom
#                repeat
        contains:
            "Wanda_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,-60) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,-80) #top -80
                pause .25
                ease 1 pos (0,-60) #bottom -70
                repeat
        #this is the animation for Wanda's lower body during 69, Speed 0 (static)
        contains:
            "Wanda_69_Legs"
            subpixel True
            rotate 180
            pos (0,25) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,20) #top
                pause .25
                ease 1 pos (0,25) #bottom
                repeat

#Start Animations for Wanda's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Wanda_69_Anim1:
        #this is the animation for Wanda's hairback during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Wanda_69_HairBack"
            transform_anchor True
            anchor (450,320)#(450,180)# (610,420)
            offset (605,620)#(620,720)#
            rotate 190
#            zoom .75
#            offset (180,50)#(180,100)
            pos (5,-10) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 ypos -160 #top -10(35,-65)
                pause .75#1.25
                ease 2.5 ypos -10 #bottom 150(85,50)
                pause .5#1.25
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .50 rotate 180#210
                pause 1.5
                ease 1.25 rotate 190#240
                pause 1.25
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 xpos -30 #top 125(35,-65)
                pause .75#1.25
                ease 2.0 xpos 5 #bottom 175(85,50)
                pause 1 #1.25
                repeat
        #this is the animation for Zero's cock during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (695,950)#(#(675,900)#(690,900)
            pos (0,0) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .50 rotate 0
                pause 1.75
                ease 1.5 rotate -5
                pause .75
                repeat
        #this is the animation for Wanda's head during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Wanda_69_Head"
            transform_anchor True
            anchor (450,320)#(450,180)# (610,420)
            offset (615,620)#(760,880)#(620,720)#
            rotate 240
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,0) #X less is left, Y less is up
#            parallel:
#                #Total time, 5 seconds
#                pause .5
#                easein .50 rotate 90#210
#                pause 1.5
#                ease 1.25 rotate 180#240
#                pause 1.25
#                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 ypos -160 #top -10(35,-65)
                pause .75#1.25
                ease 2.5 ypos 0 #bottom 150(85,50)
                pause .5#1.25
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .50 rotate 210#210
                pause 1.5
                ease 1.25 rotate 240#240
                pause 1.25
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 xpos -30 #top -50
                pause .75#1.25
                ease 2.0 xpos 0 #bottom 175(85,50)
                pause 1 #1.25
                repeat
        contains:
            subpixel True
            "Wanda_69_HairOver"
            transform_anchor True
            anchor (450,320)#(450,180)# (610,420)
            offset (615,620)#(620,720)#
            rotate 210
#            zoom .75
#            offset (180,50)#(180,100)
            pos (5,-10) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 ypos -160 #top -10(35,-65)
                pause .75#1.25
                ease 2.5 ypos -10 #bottom 150(85,50)
                pause .5#1.25
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .50 rotate 200#210
                pause 1.5
                ease 1.25 rotate 210#190
                pause 1.25
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 xpos -30 #top 125(35,-65)
                pause .75#1.25
                ease 2.0 xpos 5 #bottom 175(85,50)
                pause 1 #1.25
                repeat
##        contains:
##            subpixel True
##            "Wanda_69_Tits"
##            rotate 180
###            zoom .65
##            pos (30,40) #X less is left, Y less is up
##            block:
##                #Total time, 5 seconds
##                pause .5
##                easein .75 pos (10,-10) #top
##                pause 1.25
##                ease 2.5 pos (30,40) #bottom
##                repeat
        #this is the animation for Wanda's upper body during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Wanda_69_Body"
            rotate 180
            pos (85,60) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 xpos 30 #top (10,-70)
                pause .8
                ease 1.4 xpos 70 #bottom(30,-10)
                ease 1.3 xpos 85 #bottom(30,-10)
#                pause 1.3
                pause .25
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 ypos -90 #top (10,-70)
                pause .8
                ease 2.7 ypos 60 #bottom(30,-10)
                pause .25
                repeat
#        #this is the animation for Wanda's lower body during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Wanda_69_Legs"
            rotate 185
            pos (80,105) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein 1.0 pos (30,-15)#(0,-5)
                pause .5
                ease 2.5 pos (80,105)#(30,25)
                pause .5
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein 1.0 rotate 180
                pause .5
                ease 2.5 rotate 185
                pause .5
                repeat

#Start Animations for Wanda's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Wanda_69_Anim2:
        #this is the animation for Wanda's hairback during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Wanda_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-90) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-120) #top -160
#                pause .5
                ease 1.25 pos (0,-90) #bottom -130
                repeat
        #this is the animation for Zero's cock during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (695,950)#((675,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Wanda's head during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Wanda_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-90) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-120) #top -160
#                pause .5
                ease 1.25 pos (0,-90) #bottom -130
                repeat
        #this is the animation for Wanda's upper body during 69, Speed 2 (heading)
#        contains:
#            "Wanda_69_Tits"
#            subpixel True
#            rotate 180
##            zoom .65
#            pos (0,0) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                pause .25
#                easein 1.5 pos (0,-20) #top
#                pause .25
#                ease 1 pos (0,0) #bottom
#                repeat
        contains:
            "Wanda_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,-50) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,-70) #top -10
                pause .25
                ease 1 pos (0,-50) #bottom 0
                repeat
        #this is the animation for Wanda's lower body during 69, Speed 2 (heading)
        contains:
            "Wanda_69_Legs"
            subpixel True
            rotate 180
            pos (0,40) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,25) #top
                pause .25
                ease 1 pos (0,40) #bottom
                repeat

#Start Animations for Wanda's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Wanda_69_Anim3:
        #this is the animation for Wanda's hairback during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Wanda_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-80) #top -20
#                pause .5
                ease 1.25 pos (0,-30) #bottom 30
                repeat
#        #this is the animation for Zero's cock during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (695,950)#((675,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Wanda's head during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Wanda_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-80) #top -20
#                pause .5
                ease 1.25 pos (0,-30) #bottom 30
                repeat
        #this is the animation for Wanda's upper body during 69, Speed 3 (sucking)
#        contains:
#            subpixel True
#            "Wanda_69_Tits"
#            rotate 180
#            anchor (560,400)#(560,330) + is right and down
#            offset (700,715)#(-560,-330) + is right and down
#            transform_anchor True
##            zoom .65
#            pos (0,30) #X less is left, Y less is up
##            alpha .9
#            parallel:
#                #Total time, 3 seconds
#                easein .75 pos (0,-5) #top
#                ease 1.25 pos (0,30) #bottom
#                repeat
#            parallel:
#                #Total time, 3 seconds
#                ease .15 yzoom 1.2
#                ease .25 yzoom 1
#                ease .35 yzoom 1.1

#                ease .5 yzoom .8
#                ease .75 yzoom 1         #bottom
#                repeat
        #this is the animation for Wanda's lower body during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Wanda_69_Body"
            rotate 180
#            zoom .65
            pos (0,-20) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-60) #top 0
#                pause .5
                ease 1.25 pos (0,-20) #bottom 40
                repeat
        #this is the animation for Wanda's lower body during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Wanda_69_Legs"
            rotate 180
            pos (0,40) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,25) #-5
#                pause .5
                ease 1.25 pos (0,40) #10
                repeat

#Start Animations for Wanda's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Wanda_69_Anim4:
        #this is the animation for Wanda's hairback during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Wanda_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-30) #top 30
                pause .5
                ease 1.75 pos (0,10) #bottom 70
                repeat
        #this is the animation for Zero's cock during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (695,950)#((675,900)#(690,900)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Wanda's head during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Wanda_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-30) #top 30
                pause .5
                ease 1.75 pos (0,10) #bottom 70
                repeat
        contains:
            subpixel True
            "Wanda_69_HairOver"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-35) #top 25
                pause .5
                ease 1.75 pos (0,0) #bottom 60
                repeat
        #this is the animation for Wanda's upper body during 69, Speed 4 (deep)
#        contains:
#            subpixel True
#            "Wanda_69_Tits"
#            rotate 180
##            zoom .65
#            pos (0,40) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                easein .75 pos (0,5) #top
#                pause .5
#                ease 1.75 pos (0,40) #bottom
#                repeat
#        contains:
#            subpixel True
#            "Wanda_69_Tits"
#            rotate 180
#            anchor (560,400)#(560,330) + is right and down
#            offset (700,715)#(-560,-330) + is right and down
#            transform_anchor True
##            zoom .65
#            pos (0,40) #X less is left, Y less is up
##            alpha .9
#            parallel:
#                #Total time, 3 seconds
#                easein .75 pos (0,5) #top
#                pause .5
#                ease 1.75 pos (0,40) #bottom
#                repeat
#            parallel:
#                #Total time, 3 seconds
#                ease .15 yzoom 1.2
#                ease .25 yzoom 1
#                ease .35 yzoom 1.1
#                pause .5
#                ease .5 yzoom .9
#                ease 1.25 yzoom 1         #bottom
#                repeat
        contains:
            subpixel True
            "Wanda_69_Body"
            rotate 180
#            zoom .65
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-25) #top 35
                pause .5
                ease 1.75 pos (0,10) #bottom 70
                repeat
        #this is the animation for Wanda's lower body during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Wanda_69_Legs"
            rotate 180
            pos (0,60) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,55)
#                pause .5
                ease 2.25 pos (0,60)
                repeat

#Start Animations for Wanda's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Wanda_69_Anim5:
        #this is the animation for Wanda's hairback during 69, Speed 5 (cum high)
        contains:
            subpixel True
            "Wanda_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-90) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 0.5 pos (0,-110) #top -160
                pause 1.25
#                pause .5
                ease 1.25 pos (0,-90) #bottom -130
                repeat
        #this is the animation for Zero's cock during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (695,950)#((675,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Wanda's head during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Wanda_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-90) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 0.5 pos (0,-110) #top -160
                pause 1.25
#                pause .5
                ease 1.25 pos (0,-90) #bottom -130
                repeat
        #this is the animation for Wanda's upper body during 69, Speed 2 (heading)
#        contains:
#            "Wanda_69_Tits"
#            subpixel True
#            rotate 180
##            zoom .65
#            pos (0,0) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                pause .25
#                easein 1.5 pos (0,-20) #top
#                pause .25
#                ease 1 pos (0,0) #bottom
#                repeat
        contains:
            "Wanda_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,-70) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,-90) #top -10
                pause .25
                ease 1 pos (0,-70) #bottom 0
                repeat
        #this is the animation for Wanda's lower body during 69, Speed 2 (heading)
        contains:
            "Wanda_69_Legs"
            subpixel True
            rotate 180
            pos (0,40) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,25) #top
                pause .25
                ease 1 pos (0,40) #bottom
                repeat

#Start Animations for Wanda's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Wanda_69_Anim6:
        #this is the animation for Wanda's hairback during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Wanda_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .5
                easein .75 pos (0,-10) #top 30
                ease 1.75 pos (0,10) #bottom 70
                repeat
        #this is the animation for Zero's cock during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (695,950)#((675,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Wanda's head during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Wanda_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .5
                easein .75 pos (0,-10) #top 30
                ease 1.75 pos (0,10) #bottom 70
                repeat
        contains:
            subpixel True
            "Wanda_69_HairOver"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .5
                easein .75 pos (0,-15) #top 25
                ease 1.75 pos (0,0) #bottom 60
                repeat
        #this is the animation for Wanda's upper body during 69, Speed 6 (cum deep)
#        contains:
#            subpixel True
#            "Wanda_69_Tits"
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
            subpixel True
            "Wanda_69_Body"
            rotate 180
#            zoom .65
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,5) #top 35
                pause .5
                ease 1.75 pos (0,10) #bottom 70
                repeat
        #this is the animation for Wanda's lower body during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Wanda_69_Legs"
            rotate 180
            pos (0,60) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,55)
#                pause .5
                ease 2.25 pos (0,60)
                repeat

#End Animations for Wanda's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#Start Wanda 69 Cunnilingus Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

#Start Animations for Wanda's 69 Cunnalingus pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_69_CUN:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
#                "True", "Wanda_69_Anim1",
                "Speed == 2",   "Wanda_69_Cun2",
                "Speed == 3",   "Wanda_69_Cun3",
                "Speed",        "Wanda_69_Cun1",
                "True",         "Wanda_69_Cun0",
                ),
        )
    align (0.6,0.0)
    pos (475,-700)
    zoom 1.8#1/3

#Start Animations for Wanda's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Animations for Wanda's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Wanda_69_Cun0:
        #this is the animation for Wanda's hairback during 69, Speed 0 (static)
        contains:
            subpixel True
            "Wanda_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (10,-120) #(10,-120) X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (10,-115) #top
#                pause .5
                ease 1.25 pos (10,-120) #bottom
                repeat
        #this is the animation for Zero's cock during 69, Speed 0 (static)
        contains:
            #pussy
            "Zero_Pussy"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (858,920)#(840,920)
        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (745,921)#(728,920)
        #this is the animation for Wanda's head during 69, Speed 0 (static)
        contains:
            subpixel True
            "Wanda_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (10,-120) #(10,-120) X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (10,-115) #top
#                pause .5
                ease 1.25 pos (10,-120) #bottom
                repeat
        #this is the animation for Wanda's upper body during 69, Speed 0 (static)
        contains:
            "Wanda_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (5,-70) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (5,-75) #top 35
                pause .5
                ease 1.75 pos (5,-70) #bottom 70
                repeat
        #this is the animation for Wanda's lower body during 69, Speed 0 (static)
        contains:
            "Wanda_69_Legs"
            subpixel True
            rotate 180
            pos (15,25) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (15,25) #top
                pause .25
                ease 1 pos (15,25) #bottom
                repeat

#Start Animations for Wanda's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Wanda_69_Cun1:
        #this is the animation for Wanda's hairback during 69, Speed 1 (lick)
        contains:
            subpixel True
            "Wanda_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-110) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                ease 1.0 ypos -115 #top
                easeout .5 ypos -105 #top
                easein 1.0 ypos -110 #bottom
                pause .5
                repeat
#            parallel:
#                #Total time, 3 seconds
#                pause .5
#                ease .5 xpos 32 #top
#                pause .25
#                easein 1.25 xpos 0 #bottom
#                pause .5
#                repeat
#            parallel:
#                #Total time, 3 seconds
#                pause .5
#                easein .5 rotate 180 #top
#                pause .25
#                easein 1.25 rotate 185 #bottom
#                pause .5
#                repeat
        #this is the animation for Zero's cock during 69, Speed 1 (lick)
        contains:
            #pussy
            "Zero_Pussy"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (858,920)#(840,920)
        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (745,921)#(728,920)
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
        #this is the animation for Wanda's head during 69, Speed 1 (lick)
        contains:
            subpixel True
            "Wanda_69_Head"
            rotate 185
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-110) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                ease 1.0 ypos -115 #top
                easeout .5 ypos -105 #top
                easein 1.0 ypos -110 #bottom
                pause .5
                repeat
            parallel:
                #Total time, 3 seconds
                pause .5
                easein .5 rotate 175 #top
                pause .25
                easein 1.25 rotate 185 #bottom
                pause .5
                repeat
        contains:
            subpixel True
            "Wanda_69_HairOver"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-110) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                ease 1.0 ypos -115 #top
                easeout .5 ypos -105 #top
                easein 1.0 ypos -110 #bottom
                pause .5
                repeat
#            parallel:
#                #Total time, 3 seconds
#                pause .5
#                ease .5 xpos 32 #top
#                pause .25
#                easein 1.25 xpos 12 #bottom
#                pause .5
#                repeat
            parallel:
                #Total time, 3 seconds
                pause .5
                easein .5 rotate 180 #top
                pause .25
                easein 1.25 rotate 185 #bottom
                pause .5
                repeat
        #this is the animation for Wanda's upper body during 69, Speed 1 (lick)
#        contains:
#            "Wanda_69_Tits"
#            subpixel True
#            rotate 180
##            zoom .65
#            pos (15,0) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                pause .25
#                easein 1.25 pos (15,-5) #top
#                pause .25
#                ease 1.25 pos (15,0) #bottom
#                repeat
        contains:
            "Wanda_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (10,-70) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.25 pos (10,-75) #top
                pause .25
                ease 1.25 pos (10,-70) #bottom
                repeat
        #this is the animation for Wanda's lower body during 69, Speed 1 (lick)
        contains:
            "Wanda_69_Legs"
            subpixel True
            rotate 180
            pos (15,20) #X less is left, Y less is up
#            block:
#                pause .25
#                easein 1.5 pos (15,25) #top
#                pause .25
#                ease 1 pos (15,20) #bottom
#                repeat


#Start Animations for Wanda's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Wanda_69_Cun2:
        #this is the animation for Wanda's hairback during 69, Speed 2 (clit)
        contains:
            subpixel True
            "Wanda_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-105) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                easein .9 ypos -100 #top
                easein 1.1 ypos -105 #bottom
                repeat
#            parallel:
#                #Total time, 3 seconds
#                pause 0.2
#                easein .8 xpos 0 #top
#                easein 1.0 xpos 32 #bottom
#                repeat
        #this is the animation for Zero's cock during 69, Speed 2 (clit)
        contains:
            #pussy
            "Zero_Pussy"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (858,920)#(840,920)
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
        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (745,921)#(728,920)
        #this is the animation for Wanda's head during 69, Speed 2 (clit)
        contains:
            subpixel True
            "Wanda_69_Head"
            rotate 178
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-105) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                easein .9 ypos -100 #top
                easein 1.1 ypos -105 #bottom
                repeat
            parallel:
                #Total time, 3 seconds
                pause 0.2
                easein .8 rotate 183 #top
                easein 1.0 rotate 178 #bottom
                repeat
        #this is the animation for Wanda's upper body during 69, Speed 2 (clit)
#        contains:
#            "Wanda_69_Tits"
#            subpixel True
#            rotate 180
##            zoom .65
#            pos (10,0) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                easein 1 pos (10,-5) #top
#                ease 1 pos (10,0) #bottom
#                repeat
        contains:
            "Wanda_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (10,-75) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1 pos (10,-80) #top
                ease 1 pos (10,-75) #bottom
                repeat
        #this is the animation for Wanda's lower body during 69, Speed 2 (clit)
        contains:
            "Wanda_69_Legs"
            subpixel True
            rotate 180
            pos (15,25) #X less is left, Y less is up
#            block:
#                pause .25
#                easein 1.5 pos (15,-30) #top
#                pause .25
#                ease 1 pos (15,-25) #bottom
#                repeat

#Start Animations for Wanda's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Wanda_69_Cun3:
        #this is the animation for Wanda's hairback during 69, Speed 3 (suck)
        contains:
            subpixel True
            "Wanda_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-90) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .5 ypos -95 #top -150
                pause 1.25
                ease 1.25 ypos -90 #bottom -145
                repeat
        #this is the animation for Zero's cock during 69, Speed 3 (suck)
        contains:
            #pussy
            "Zero_Pussy"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (858,920)#(840,920)
        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (745,921)#(745,921)
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
        #this is the animation for Wanda's head during 69, Speed 3 (suck)
        contains:
            subpixel True
            "Wanda_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-90) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .5 ypos -95 #top -150
                pause 1.25
                ease 1.25 ypos -90 #bottom -145
                repeat
        #this is the animation for Wanda's upper body during 69, Speed 3 (suck)
#        contains:
#            "Wanda_69_Tits"
#            subpixel True
#            rotate 180
##            zoom .65
#            pos (10,0) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                pause .3
#                easein 1.5 pos (10,-5) #top
#                pause .3
#                ease .9 pos (10,0) #bottom
#                repeat
        contains:
            "Wanda_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (10,-65) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (10,-70) #top
                pause .25
                ease 1 pos (10,-65) #bottom
                repeat
        #this is the animation for Wanda's lower body during 69, Speed 3 (suck)
        contains:
            "Wanda_69_Legs"
            subpixel True
            rotate 180
            pos (15,35) #X less is left, Y less is up
#            block:
#                pause .25
#                easein 1.5 pos (15,25) #top
#                pause .25
#                ease 1 pos (15,35) #bottom
#                repeat
#End Animations for Wanda's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#End Wanda 69 Animations

# Start Wanda Scissor Pose content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_SC_Sprite:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
                #if the top's down. . .
                "Speed >= 2", "Wanda_SC_Anim_2",
                "Speed", "Wanda_SC_Anim_1",
                "True", "Wanda_SC_Anim_0",
                ),
        )
    align (0.6,0.0)
    pos (700,200)#(650,303)
    zoom 1#0.85

image Wanda_SC_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Wanda_SexSprite
        (1120,880),
        (545,540), ConditionSwitch(    #165,560
            #Personal Wetness
            "not WandaX.Wet", Null(),
            "(WandaX.Legs == 'pants' or WandaX.Legs == 'shorts') and not WandaX.Upskirt", Null(),
            "WandaX.Panties and not WandaX.PantiesDown", Null(),
            "Player.Cock == 'foot'", Null(),
            "WandaX.Wet == 1", "Wet_Drip",
            "True", "Wet_Drip2",
            ),

        (545,540), ConditionSwitch(    #205,530
            #Spunk
            "'anal' not in WandaX.Spunk or not Player.Male", Null(),
            "Player.Cock == 'foot'", Null(),
            "(WandaX.Legs == 'pants' or WandaX.Legs == 'shorts') and not WandaX.Upskirt", Null(),
            "WandaX.Wet == 1", "Spunk_Drip",
            "True", "Spunk_Drip2",
            ),

        (0,0), ConditionSwitch(
            #skin behind hose layer
            "WandaX.Hose == 'stockings and garterbelt'", "images/WandaSex/Wanda_Sex_UnderLegs.png",
            "WandaX.Hose == 'garterbelt'", "images/WandaSex/Wanda_Sex_UnderLegs.png",
            "WandaX.Panties and WandaX.PantiesDown", Null(),
            "WandaX.Hose == 'pantyhose'", "images/WandaSex/Wanda_Sex_UnderLegs.png",
            "WandaX.Hose == 'ripped pantyhose'", "images/WandaSex/Wanda_Sex_UnderLegs.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs
#            "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/WandaSex/Wanda_Sex_FBase.png",
#            "Player.Sprite and Player.Cock == 'in' and Speed", "images/WandaSex/Wanda_Sex_FBase.png",
#            "Player.Sprite and Player.Cock == 'in' and Speed", "Wanda_Sex_Heading_Pussy",
#            "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/WandaSex/[WandaX.skin_image.skin_path]Wanda_Sex_Ass.png",
#            "Trigger == 'lick pussy'", "images/WandaSex/[WandaX.skin_image.skin_path]Wanda_Sex_Ass.png",
            "True", "images/WandaSex/[WandaX.skin_image.skin_path]Wanda_Sex_Ass.png",
            ),

        (0,0), ConditionSwitch(
            #ass red
            "WandaX.Red", "images/WandaSex/Wanda_Sex_Red.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            "Player.Sprite and Player.Cock == 'anal'", "images/WandaSex/Wanda_Sex_Anus_Cover.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #Wet look
            "not WandaX.Water", Null(),
            "True", "images/WandaSex/Wanda_Sex_Water_Legs.png",
            ),

#        (0,0), "Wanda_Sex_Anus",
            #Anus Composite

        (0,0), "Wanda_SC_Pussy",
            #Pussy Composite


        (0,0), ConditionSwitch(
            #hose layer
            "WandaX.Hose == 'stockings and garterbelt'", Recolor("Wanda", "Hose", "images/WandaSex/Wanda_Sex_Hose_StockingsGarter.png"),
            "WandaX.Hose == 'socks'", Recolor("Wanda", "Hose", "images/WandaSex/Wanda_Sex_Hose_Socks.png"),
            "WandaX.Hose == 'garterbelt'", Recolor("Wanda", "Hose", "images/WandaSex/Wanda_Sex_Hose_Garter.png"),
            "WandaX.Hose == 'stockings'", Recolor("Wanda", "Hose", "images/WandaSex/Wanda_Sex_Hose_Stockings.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Panties if up
            "WandaX.PantiesDown", ConditionSwitch(
                    #If she has panties down. . .
                    "WandaX.Panties == 'lace panties'", Recolor("Wanda", "Panties", "images/WandaSex/Wanda_Sex_Panties_Lace_Down.png"),
                    "WandaX.Panties == 'bikini bottoms'", Recolor("Wanda", "Panties", "images/WandaSex/Wanda_Sex_Panties_Bikini_Down.png"),
                    "WandaX.Panties", Recolor("Wanda", "Panties", "images/WandaSex/Wanda_Sex_Panties_Gray_Down.png"),
                    "True", Null(),
                    ),
            "WandaX.Panties == 'lace panties'", Recolor("Wanda", "Panties", "images/WandaSex/Wanda_Sex_Panties_Lace.png"),
            "WandaX.Panties == 'bikini bottoms'", Recolor("Wanda", "Panties", "images/WandaSex/Wanda_Sex_Panties_Bikini.png"),
            "WandaX.Panties and WandaX.Wet", Recolor("Wanda", "Panties", "images/WandaSex/Wanda_Sex_Panties_Gray_Wet.png"),
            "WandaX.Panties", Recolor("Wanda", "Panties", "images/WandaSex/Wanda_Sex_Panties_Gray.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pantyhose layer
            "WandaX.Panties and WandaX.PantiesDown", Null(),
#            "WandaX.Hose == 'tights'", "images/WandaSex/Wanda_Sex_Hose_Tights.png",
#            "WandaX.Hose == 'ripped tights'", "images/WandaSex/Wanda_Sex_Hose_Tights_Holed.png",
            "WandaX.Hose == 'pantyhose'", Recolor("Wanda", "Hose", "images/WandaSex/Wanda_Sex_Hose_Pantyhose.png"),
            "WandaX.Hose == 'ripped pantyhose'", Recolor("Wanda", "Hose", "images/WandaSex/Wanda_Sex_Hose_Pantyhose_Holed.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs Layer
            "WandaX.Legs == 'skirt'", "images/WandaSex/Wanda_Sex_Legs_Skirt.png",
            "WandaX.Legs == 'dress'", Recolor("Wanda", "Legs", "images/WandaSex/Wanda_Sex_Legs_Dress.png"),
            "WandaX.Legs == 'pants' and WandaX.Upskirt", Recolor("Wanda", "Legs", "images/WandaSex/Wanda_Sex_Legs_Pants_Down.png"),
            "WandaX.Legs == 'pants' and WandaX.Wet > 1", Recolor("Wanda", "Legs", "images/WandaSex/Wanda_Sex_Legs_Pants_Wet.png"),
            "WandaX.Legs == 'pants'", Recolor("Wanda", "Legs", "images/WandaSex/Wanda_Sex_Legs_Pants.png"),
            "WandaX.Legs == 'shorts' and WandaX.Upskirt", Recolor("Wanda", "Legs", "images/WandaSex/Wanda_Sex_Legs_Shorts_Down.png"),
            "WandaX.Legs == 'shorts' and WandaX.Wet > 1", Recolor("Wanda", "Legs", "images/WandaSex/Wanda_Sex_Legs_Shorts_Wet.png"),
            "WandaX.Legs == 'shorts'", Recolor("Wanda", "Legs", "images/WandaSex/Wanda_Sex_Legs_Shorts.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Piercings
            "not WandaX.Pierce", Null(),
            "WandaX.Legs == 'dress' or WandaX.Legs == 'skirt'", Null(),
            "Player.Sprite and Player.Cock == 'in' and Speed", Null(),
            "WandaX.Pierce == 'ring'",ConditionSwitch(
                    "WandaX.Legs == 'pants' and not WandaX.Upskirt", "images/WandaSex/Wanda_Sex_Pierce_R_Black.png",
                    "WandaX.Legs == 'shorts' and not WandaX.Upskirt", "images/WandaSex/Wanda_Sex_Pierce_R_Black.png",

                    "WandaX.PantiesDown", Null(), #"images/WandaSex/Wanda_Sex_Pierce_Pussy_R.png",
                    "WandaX.Panties == 'bikini bottoms'", "images/WandaSex/Wanda_Sex_Pierce_R_Red.png",
                    "WandaX.Hose == 'pantyhose'", "images/WandaSex/Wanda_Sex_Pierce_R_Lace.png",
                    "WandaX.Panties == 'lace panties'", "images/WandaSex/Wanda_Sex_Pierce_R_Lace.png",
                    "WandaX.Panties", "images/WandaSex/Wanda_Sex_Pierce_R_Gray.png",
                    "True", Null(), #"images/WandaSex/Wanda_Sex_Pierce_R.png",
                    ),
            #else, it's barbell
            "WandaX.Legs == 'pants' and not WandaX.Upskirt", "images/WandaSex/Wanda_Sex_Pierce_B_Black.png",
            "WandaX.Legs == 'shorts' and not WandaX.Upskirt", "images/WandaSex/Wanda_Sex_Pierce_B_Black.png",

            "WandaX.PantiesDown", Null(), #"images/WandaSex/Wanda_Sex_Pierce_B.png",
            "WandaX.Panties == 'bikini bottoms'", "images/WandaSex/Wanda_Sex_Pierce_B_Red.png",
            "WandaX.Hose == 'pantyhose'", "images/WandaSex/Wanda_Sex_Pierce_B_Lace.png",
            "WandaX.Panties == 'lace panties'", "images/WandaSex/Wanda_Sex_Pierce_B_Lace.png",
            "WandaX.Panties", "images/WandaSex/Wanda_Sex_Pierce_B_Gray.png",
            "True", Null(), #"images/WandaSex/Wanda_Sex_Pierce_B.png",
            ),
        (0,0), ConditionSwitch(
            #towel Layer
            "WandaX.Over == 'towel'", Recolor("Wanda", "Over", "images/WandaSex/Wanda_Sex_Legs_Towel.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk
            "'feet' in WandaX.Spunk and Player.Male", "images/WandaSex/Wanda_Sex_Spunk_Foot2.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy'", "Wanda_Sex_Lick_Pussy",
            "Trigger == 'lick ass'", "Wanda_Sex_Lick_Ass",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #pussy fondling animation
#            "Trigger3 == 'fondle pussy' and WandaX.Lust > 60 and not (Player.Sprite)",  At("WandaFingerHand", GirlFingerPussyX()), #"Wanda_Sex_Mast2",
#            "Trigger3 == 'fondle pussy'", At("WandaMastHand", GirlGropePussyX()), #"Wanda_Sex_Mast",
#            "Player.Sprite and Player.Cock", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Wanda_Sex_Fondle_Pussy",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #Footjob overlay
#            "Player.Cock == 'foot'", Null(),
#            "True", "Wanda_Sex_Foot",
#            ),
        )
# End Wanda SC Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Wanda Sex Pose Pussy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Wanda_SC_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).
    contains:
            # The background plate of her pussy
            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/WandaSex/Wanda_Sex_Pussy_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed", "Wanda_Sex_Heading_Pussy",
#                "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'out')", "images/WandaSex/Wanda_Sex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/WandaSex/Wanda_Sex_Pussy_Open.png",
                "Trigger3 == 'fondle pussy' and WandaX.Lust > 60", "images/WandaSex/Wanda_Sex_Pussy_Open.png",
                "True", "images/WandaSex/Wanda_Sex_Pussy_Closed.png",
                )
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "not WandaX.Wet", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/KittySex/Kitty_Sex_WetPussy_F.png",
                "True", "images/DoreenSex/Doreen_Sex_Wet.png",
                )
    contains:
            # pubes
            ConditionSwitch(
                "not WandaX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", Recolor("Wanda", "Pubes", "images/WandaSex/Wanda_Sex_Pubes_Fucking.png"),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 1", Recolor("Wanda", "Pubes", "images/WandaSex/Wanda_Sex_Pubes_Fucking.png"),
#                "Player.Sprite and Player.Cock == 'in'", "images/WandaSex/Wanda_Sex_Pubes_Open.png",
#                "Player.Sprite and Player.Cock == 'out'", "images/WandaSex/Wanda_Sex_Pubes_Open.png",
#                "Trigger == 'lick pussy'", "images/WandaSex/Wanda_Sex_Pubes_Open.png",
#                "Trigger3 == 'fondle pussy' and WandaX.Lust > 60", "images/WandaSex/Wanda_Sex_Pubes_Open.png",
                "True", Recolor("Wanda", "Pubes", "images/WandaSex/Wanda_Sex_Pubes_Closed.png"),
                )

    #End Wanda Pussy composite

# Start Wanda Sex Pose Speed 0 Scissor / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_SC_Anim_0:
    # Pose for Wanda's Sex Pose in which she is scissoring at speed 0 (static)
    contains:
            #Wanda's underlying body
            subpixel True
            "Wanda_Sex_Body"
            anchor (800,325)#(410,470)
            offset (910,410) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 30
            pos (20,2) #(70,-60) #X less is left, Y less is up
            block: #adds to 5
                ease 1 ypos 0#-40 #-140
                pause 0.8
                ease 1 ypos 2#-60 #-180
                pause 0.2
                repeat
    contains:
            #Wanda's Legs
            subpixel True
            "Wanda_SC_Legs"
            anchor (800,325)#(410,470)
            offset (925,470)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 40
            pos (20,-23) #(50,-220) #X less is left, Y less is up (80,0)
            block: #adds to 5
                pause 0.2
                ease 1 ypos -20 #10
                pause 0.8
                ease 1 ypos -23 #0
                repeat
#    contains:
#            subpixel True
##            "Wanda_Sex_Zero_Cock"
#            "Zero_Blowcock"
#            zoom .4#.5
#            subpixel True
#            pos (550,550) #(630,520)
#            rotate -5 #0
#            alpha 0.5
#            parallel:
#                pause 0.2
#                ease 1 rotate -10 #10
#                pause 0.8
#                ease 1 rotate -5 #0
#                repeat
    contains:
            #pussy
            "Zero_Pussy_Full"
            anchor (.5,.5)
            zoom .7#.45
            pos (0,0)#(410,790)
            offset (791,785)#(750,770)
#            block: #adds to 5
#                ease 1 offset (0,0)
#                ease 1 offset (0,500)
#                ease 1 offset (750,700)
#                ease 1 offset (500,0)
#                ease 1 offset (0,0)
#                ease 1 offset (0,0)
#                ease 1 offset (0,-500)
#                ease 1 offset (-500,-500)
#                ease 1 offset (-500,0)
#                ease 1 offset (0,0)
#                repeat
    contains:
            #Wanda's Feet
            subpixel True
            "Wanda_Sex_Foot"
            anchor (800,325)#(410,470)
#            offset (840,395)    #(560,330)
            offset (925,465)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 30
            pos (20,-20) #X less is left, Y less is up (200,-180)
            parallel:
#                pause 0.2
                ease 1.2 rotate 32#50 #10
                pause 0.8
                ease 1 rotate 30 #0
                repeat

# End main animation for Sex Pose scissoring Speed 0

# End Wanda Sex Pose Speed 0 scissoring / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Wanda Sex Pose Speed 1 scissoring / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_SC_Anim_1:
    # Pose for Wanda's Sex Pose in which she is scissoring at speed 1 (slow)
    contains:
            #Wanda's underlying body
            subpixel True
            "Wanda_Sex_Body"
            anchor (800,325)#(410,470)
            offset (910,410) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 30
            pos (0,5) #(70,-60) #X less is left, Y less is up
            block: #adds to 5
                ease 1 ypos 0#-40 #-140
                pause 0.8
                ease 1 ypos 5#-60 #-180
                pause 0.2
                repeat
    contains:
            #Wanda's Legs
            subpixel True
            "Wanda_SC_Legs"
            anchor (800,325)#(410,470)
            offset (925,470)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 40
            pos (0,10) #(50,-220) #X less is left, Y less is up (80,0)
            block: #adds to 5
                pause 0.2
                ease 1 ypos 0 #10
                pause 0.8
                ease 1 ypos 10 #0
                repeat
#    contains:
#            subpixel True
##            "Wanda_Sex_Zero_Cock"
#            "Zero_Blowcock"
#            zoom .4#.5
#            subpixel True
#            pos (550,550) #(630,520)
#            rotate -5 #0
#            alpha 0.5
#            parallel:
#                pause 0.2
#                ease 1 rotate -10 #10
#                pause 0.8
#                ease 1 rotate -5 #0
#                repeat
    contains:
            #pussy
            "Zero_Pussy_Full"
            anchor (.5,.5)
            zoom .7#.45
            pos (0,-10)#(410,790)
            offset (791,785)#(750,770)
            parallel: #adds to 5
#                pause 0.2
                ease 1 ypos 0 #10
                pause 1#0.8
                ease 1 ypos -10 #0
                repeat
    contains:
            #Wanda's Feet
            subpixel True
            "Wanda_Sex_Foot"
            anchor (800,325)#(410,470)
#            offset (840,395)    #(560,330)
            offset (925,465)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 35
            pos (0,0) #X less is left, Y less is up (200,-180)
            parallel:
#                pause 0.2
                ease 1.2 rotate 30#50 #10
                pause 0.8
                ease 1 rotate 35 #0
                repeat

# End main animation for Sex Pose scissoring Speed 1

# End Wanda Sex Pose Speed 1 scissoring / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Wanda Sex Pose Speed 2 scissoring / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Wanda_SC_Anim_2:
    # Pose for Wanda's Sex Pose in which she is scissoring at speed 2 (fast)
    contains:
            #Wanda's underlying body
            subpixel True
            "Wanda_Sex_Body"
            anchor (800,325)#(410,470)
            offset (910,410) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 30
            pos (0,20) #(70,-60) #X less is left, Y less is up
            block: #adds to 5
                pause .1#0.8
                ease .3 ypos 25#-40 #-140
#                pause 0.8
                ease .5 ypos 30#-60 #-180
                repeat
    contains:
            #Wanda's Legs
            subpixel True
            "Wanda_SC_Legs"
            anchor (800,325)#(410,470)
            offset (925,470)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 40
            pos (0,10) #(50,-220) #X less is left, Y less is up (80,0)
            block: #adds to 5
                pause 0.1
                easeout .3 ypos 0 #10
                ease .5 ypos 10 #0
                repeat
#    contains:
#            subpixel True
##            "Wanda_Sex_Zero_Cock"
#            "Zero_Blowcock"
#            zoom .4#.5
#            subpixel True
#            pos (550,550) #(630,520)
#            rotate -5 #0
#            alpha 0.5
#            parallel:
#                pause 0.2
#                ease 1 rotate -10 #10
#                pause 0.8
#                ease 1 rotate -5 #0
#                repeat
    contains:
            #pussy
            "Zero_Pussy_Full"
            anchor (.5,.5)
            zoom .7#.45
            pos (0,-10)#(410,790)
            offset (791,785)#(750,770)
            parallel: #adds to 5
                easeout .3 ypos -10 #10
                pause .1#0.8
                ease .5 ypos 5 #0
                repeat
    contains:
            #Wanda's Feet
            subpixel True
            "Wanda_Sex_Foot"
            anchor (800,325)#(410,470)
#            offset (840,395)    #(560,330)
            offset (925,465)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 40
            pos (0,5) #X less is left, Y less is up (200,-180)
            parallel:
                ease .3 rotate 40#50 #10
                ease .5 rotate 38 #0
                pause .1#0.8
                repeat

# End main animation for Sex Pose Scissor Speed 2

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     SC Launch/Reset
label Wanda_SC_Launch(Line = Trigger):
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    return
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary

    $ Trigger = Line

    if renpy.showing("Wanda_SC_Sprite"):
        return
    $ Speed = 0
    call Girl_Hide(WandaX,1) #call Rogue_Hide
    show Wanda_SC_Sprite zorder 150
    with dissolve
    return

label Wanda_SC_Reset:
    if not renpy.showing("Wanda_SC_Sprite"):
        return
    $ WandaX.ArmPose = 2
    hide Wanda_SC_Sprite
    call Girl_Hide(WandaX) #call Rogue_Hide
#    call Set_The_Scene(Dress = 0)
    show Wanda_Sprite at SpriteLoc(WandaX.SpriteLoc) zorder WandaX.Layer:
        alpha 1 zoom 1 offset (0,0) anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return


## End Wanda Sex Pose Content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# End Wanda Sex Pose Speed 2 Scissor / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


## Animation components / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

## Wanda Misc Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#label Wanda_Kissing_Launch(T = Trigger,Set=1):
#    call Girl_Hide(WandaX) #call Rogue_Hide
#    $ Trigger = T
#    $ WandaX.Pose = "kiss" if Set else WandaX.Pose
#    show Wanda_Sprite at SpriteLoc(WandaX.SpriteLoc) zorder 110
#    show Wanda_Sprite at SpriteLoc(StageCenter) zorder 110:
#        ease 0.5 offset (100,0) zoom 2 alpha 1
#    return

#label Wanda_Kissing_Smooch:
#    $ WandaX.FaceChange("kiss")
#    show Wanda_Sprite at SpriteLoc(StageCenter) zorder 110:
#        ease 0.5 xpos StageCenter offset (100,0) zoom 2 alpha 1
#        pause 1
#        ease 0.5 xpos WandaX.SpriteLoc zoom 1
#    show Wanda_Sprite at SpriteLoc(WandaX.SpriteLoc) zorder 110:
#        zoom 1
#    $ WandaX.FaceChange("sexy")
#    return

#label Wanda_Breasts_Launch(T = Trigger,Set=1):
#    call Girl_Hide(WandaX) #call Rogue_Hide
#    $ Trigger = T
#    $ WandaX.Pose = "breasts" if Set else WandaX.Pose
#    show Wanda_Sprite at SpriteLoc(WandaX.SpriteLoc) zorder 110:
##        ease 0.5 offset (-100,-200) zoom 2
#        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
#    return

#label Wanda_Middle_Launch(T = Trigger,Set=1):
#    call Girl_Hide(WandaX) #call Rogue_Hide
#    $ Trigger = T
#    $ WandaX.Pose = "mid" if Set else WandaX.Pose
#    show Wanda_Sprite at SpriteLoc(WandaX.SpriteLoc) zorder 110:
##        ease 0.5 offset (-100,-200) zoom 2
#        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
#    return

#label Wanda_Pussy_Launch(T = Trigger,Set=1):
#    call Girl_Hide(WandaX) #call Rogue_Hide
#    $ Trigger = T
#    $ WandaX.Pose = "pussy" if Set else WandaX.Pose
#    show Wanda_Sprite at SpriteLoc(WandaX.SpriteLoc) zorder 110:
#        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
#    return

#label Wanda_Pos_Reset(T = 0,Set=0):
#    if WandaX.Loc != bg_current:
#            return
#    call Girl_Hide(WandaX) #call Rogue_Hide
#    show Wanda_Sprite at SpriteLoc(WandaX.SpriteLoc) zorder WandaX.Layer:
#            ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
#    show Wanda_Sprite zorder WandaX.Layer:
#            offset (0,0)
#            anchor (0.5, 0.0)
#            zoom 1
#            xzoom 1
#            yzoom 1
#            alpha 1
#            pos (WandaX.SpriteLoc,50)
#    $ WandaX.Pose = "full" if Set else 0
#    $ Trigger = T
#    return

#label Wanda_Hide(Sprite=0):
##        call Wanda_Sex_Reset
#        hide Wanda_SexSprite
#        hide Wanda_Doggy_Animation
#        hide Wanda_HJ_Animation
#        hide Wanda_BJ_Animation
#        hide Wanda_TJ_Animation
#        hide Wanda_Finger_Animation
#        hide Wanda_CUN_Animation
#        hide Wanda_69_Animation
#        hide Wanda_69_CUN
#        hide Wanda_Seated
#        if Sprite:
#                hide Wanda_Sprite
#        return



## Interface items //////////////////////////////////////////////////////////////////////////////

image GropeLeftBreast_Wanda:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65#.7
        pos (275,370)#(310,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 60
        block:
            ease 1 rotate 30
            ease 1 rotate 60
            repeat

image GropeRightBreast_Wanda:
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (160,370)#(190,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block:
            ease 1 rotate -30 #-30
            ease 1 rotate -60 #-60
            repeat

image LickRightBreast_Wanda:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5
        xzoom -0.45
        pos (270,360)#(95,355)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (250,340)#(85,345)  top
            pause .5
            ease 1.5 rotate 30 pos (270,360)#(105,375) bottom
            repeat

image LickLeftBreast_Wanda:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5
        xzoom -0.45
        pos (140,355) #(195,360)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (125,325)#(135,335)
            pause .5
            ease 1.5 rotate 30 pos (140,355)#(200,410)
            repeat

image GropeThigh_Wanda:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (215,650)#(180,670)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        block:
            pause .5
            ease 1 rotate 110 pos (205,740) #(205,740) bottom
            ease 1 rotate 100 pos (215,650)   #245,640
            repeat

image GropePussy_Wanda:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (205,580)#(240,580)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease .5 rotate 190 ypos 565 #(190)
                ease .75 rotate 170 ypos 580
            choice:
                ease .5 rotate 190 ypos 565
                pause .25
                ease 1 rotate 170 ypos 580
            repeat

image FingerPussy_Wanda:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.65
        pos (210,660)#(275,650)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (220,635)#(150,665)
                pause .5
                ease 1 rotate 50 pos (210,660)  #(140,700)
            choice:
                ease .5 rotate 40 pos (220,635)
                pause .5
                ease 1.75 rotate 50 pos (210,660)
            choice:
                ease 2 rotate 40 pos (220,635)
                pause .5
                ease 1 rotate 50 pos (210,660)
            choice:
                ease .25 rotate 40 pos (220,635)
                ease .25 rotate 50 pos (210,660)
                ease .25 rotate 40 pos (220,635)
                ease .25 rotate 50 pos (210,660)
            repeat

image Lickpussy_Wanda:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (220,620)#(155,650)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout .5 rotate -50 pos (210,600) #(210,605)
            linear .5 rotate -60 pos (200,610) #(200,615)
            easein 1 rotate 10 pos (220,620) #(230,625)
            repeat

image VibratorRightBreast_Wanda:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (135,350)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            pause .25
            ease 1 rotate 35 ypos 340
            pause .25
            ease 1 rotate 55 ypos 350
            repeat

image VibratorLeftBreast_Wanda:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (260,360) #(270,400)
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

image VibratorPussy_Wanda:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (220,615) #(240,665)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 70
        block:
            ease 1 rotate 35 pos (210,605)
            pause .25
            ease 1 rotate 70 pos (220,615)
            pause .25
            repeat

image VibratorAnal_Wanda:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (265,590)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 10
        block:
            ease 1 rotate 0 pos (255,580)
            pause .25
            ease 1 rotate 10 pos (265,590)
            pause .25
            repeat

image VibratorPussyInsert_Wanda:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (220,580)#(240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_Wanda:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (250,570)#(250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0



#Lesbian action animations.
image GirlGropeBothBreast_Wanda:
    contains:
        "GirlGropeLeftBreast_Wanda"
    contains:
        "GirlGropeRightBreast_Wanda"

image GirlGropeLeftBreast_Wanda:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (300,350) #(220,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate 10 ypos 360#(280,390)
            ease 1 rotate -10 ypos 350
            repeat

image GirlGropeRightBreast_Wanda:
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (130,360) #(90,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block:
            ease 1 rotate -40 ypos 370#(90,410)
            ease 1 rotate -10 ypos 360
            repeat

image GirlGropeThigh_Wanda:
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
            ease .5 xpos 223
            ease .5 xpos 220
            ease .5 xpos 223
            ease .5 xpos 225
            repeat

image GirlGropePussy_WandaSelf:
    contains:
        "GirlGropePussy_Wanda"
        anchor (0.5,0.5)
        rotate -40
#        yzoom -1
        pos (265,615)#(190,500)

image GirlGropePussy_Wanda:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (200,580)
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
                ease .5 rotate 205 ypos 580 #(205,590)
                ease .75 rotate 200 ypos 585 #(205,595)
                ease .5 rotate 205 ypos 580
                ease .75 rotate 200 ypos 585
            choice: #Fast stroke
                ease .3 rotate 205 ypos 580
                ease .3 rotate 200 ypos 590
                ease .3 rotate 205 ypos 580
                ease .3 rotate 200 ypos 590
            repeat

image GirlFingerPussy_Wanda:
    contains:
        subpixel True
        "UI_GirlFinger"
        zoom .6
        pos (205,580)#(220,640)
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



image WandaMastHand:
        "images/UI_GirlHand_Jean.png"
        zoom 0.8
        rotate 240
        offset (385,270)

image WandaFingerHand:
        "images/UI_GirlFinger_Jean.png"
        zoom 0.8
        rotate 220
        offset (360,330)
