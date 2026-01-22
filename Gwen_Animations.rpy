# Basic character Sprites

image Gwen_Sprite:
    LiveComposite(
        (550,950),       #550,950
        (0,0), "images/GwenSprite/Gwen_Sprite_Shadow.png",
        (-10,-90), "Gwen_Sprite_HairBack", #(75,-10)
        (0,0), ConditionSwitch(
            #pants down back
            "not GwenX.Legs or not GwenX.Upskirt", Null(),
#            "GwenX.Legs == 'pants'", "images/GwenSprite/Gwen_Sprite_Legs_Pants_Back.png",
            "GwenX.Legs == 'shorts'", Recolor("Gwen", "Legs", "images/GwenSprite/Gwen_Sprite_Legs_Shorts_Back.png"),
            "GwenX.Legs == 'suit'", "images/GwenSprite/Gwen_Sprite_Legs_Suit_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #panties down back
            "not GwenX.Panties or not GwenX.PantiesDown", Null(),
            #if the panties are down
            "GwenX.Legs and not GwenX.Upskirt and (GwenX.Legs != 'skirt' and GwenX.Legs != 'cheer skirt')", Null(),
            #if she's wearing a skirt or nothing else
            "GwenX.Panties == 'lace panties'", Recolor("Gwen", "Panties", "images/GwenSprite/Gwen_Sprite_Panties_Lace_Back.png"),
            "GwenX.Panties == 'bikini bottoms'", Recolor("Gwen", "Panties", "images/GwenSprite/Gwen_Sprite_Panties_Lace_Back.png"),
            "True", Recolor("Gwen", "Panties", "images/GwenSprite/Gwen_Sprite_Panties_White_Back.png"),
            ),

        (275,560), ConditionSwitch(    #165,560
            #Personal Wetness
            "not GwenX.Wet", Null(),
            "GwenX.Wet == 1 or (GwenX.Legs and (GwenX.Legs != 'skirt' and GwenX.Legs != 'cheer skirt') and not GwenX.Upskirt)", "Wet_Drip", #ConditionSwitch( #Wet = 1
#                    "(GwenX.Legs == 'pants' or GwenX.Legs == 'shorts') and not GwenX.Upskirt", Null(),
#                    "GwenX.Panties and not GwenX.PantiesDown", Null(),
#                    "(GwenX.Legs == 'pants' or GwenX.Legs == 'shorts')", AlphaMask("Wet_Drip","Gwen_Drip_MaskP"),
#                    "GwenX.Panties and GwenX.PantiesDown", AlphaMask("Wet_Drip","Gwen_Drip_MaskP"),
#                    "True", AlphaMask("Wet_Drip","Gwen_Drip_Mask"), #only plays if nothing is in the way
#                    ),
            "True", "Wet_Drip2", #ConditionSwitch( #Wet = 2+
#                    "(GwenX.Legs == 'pants' or GwenX.Legs == 'shorts') and GwenX.Upskirt", AlphaMask("Wet_Drip2","Gwen_Drip_MaskP"),
#                    "GwenX.Panties and GwenX.PantiesDown", AlphaMask("Wet_Drip2","Gwen_Drip_MaskP"),
#                    "True", AlphaMask("Wet_Drip2","Gwen_Drip_Mask"), #only plays if nothing is in the way
#                    ),
            ),

        (275,560), ConditionSwitch(    #165,560
            #Spunk
            "('in' not in GwenX.Spunk and 'anal' not in GwenX.Spunk) or not Player.Male", Null(),
            "GwenX.Panties and not GwenX.PantiesDown", "Spunk_Drip", #ConditionSwitch( #Wet = 1
            "GwenX.Legs and (GwenX.Legs != 'skirt' and GwenX.Legs != 'cheer skirt') and not GwenX.Upskirt", "Spunk_Drip", #ConditionSwitch( #Wet = 1
#                    "GwenX.Panties and GwenX.PantiesDown", AlphaMask("Spunk_Drip","Gwen_Drip_MaskP"),
#                    "(GwenX.Legs == 'pants' or GwenX.Legs == 'shorts') and GwenX.Upskirt", AlphaMask("Spunk_Drip","Gwen_Drip_MaskP"),
#                    "True", AlphaMask("Spunk_Drip","Gwen_Drip_Mask"), #only plays if nothing is in the way
#                    ),
            "True", "Spunk_Drip2", #ConditionSwitch( #Wet = 2+
#                    "(GwenX.Legs == 'pants' or GwenX.Legs == 'shorts') and GwenX.Upskirt", AlphaMask("Spunk_Drip2","Gwen_Drip_MaskP"),
#                    "GwenX.Panties and GwenX.PantiesDown", AlphaMask("Spunk_Drip2","Gwen_Drip_MaskP"),
#                    "True", AlphaMask("Spunk_Drip2","Gwen_Drip_Mask"), #only plays if nothing is in the way
#                    ),
            ),

        (0,0), ConditionSwitch(
            #body
            "GwenX.ArmPose != 1", "images/GwenSprite/[GwenX.skin_image.skin_path]Gwen_Sprite_Body2.png",         # right hand up/left down
            "True", "images/GwenSprite/[GwenX.skin_image.skin_path]Gwen_Sprite_Body1.png", #if GwenX.Arms == 1   # right Hand on hip/left raised
            ),

        (0,0), ConditionSwitch(
            #Water effect
            "GwenX.Water and GwenX.ArmPose == 1", "images/GwenSprite/Gwen_Sprite_Water1.png",
            "GwenX.Water", "images/GwenSprite/Gwen_Sprite_Water2.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Arms2 behind the body
            "GwenX.ArmPose != 1 and GwenX.Over == 'suit' and GwenX.Arms", "images/GwenSprite/Gwen_Sprite_Over_Suit_2G_Back.png",                #gloved 2
            "GwenX.ArmPose != 1 and (GwenX.Over == 'suit' or GwenX.Over == 'open suit')", "images/GwenSprite/Gwen_Sprite_Over_Suit_2_Back.png", #no gloved 2
            "True", Null(),  #if GwenX.Arms ==2
            ),

        (0,0), ConditionSwitch(
            #Personal Wetness  over
            "not GwenX.Wet", Null(),
            "GwenX.Panties and not GwenX.PantiesDown", Null(),
            "GwenX.Legs and (GwenX.Legs != 'skirt' and GwenX.Legs != 'cheer skirt') and not GwenX.Upskirt", Null(),
            "True", "images/GwenSprite/Gwen_Sprite_Wet_Pussy.png", #ConditionSwitch( #Wet = 2+
            ),
        (0,0), ConditionSwitch(
            #Spunk over
            "('in' not in GwenX.Spunk and 'anal' not in GwenX.Spunk) or not Player.Male", Null(),
            "GwenX.Legs and (GwenX.Legs != 'skirt' and GwenX.Legs != 'cheer skirt') and not GwenX.Upskirt", Null(),
            "GwenX.Panties and not GwenX.PantiesDown", Null(),
            "True", "images/GwenSprite/Gwen_Sprite_Spunk_Pussy.png",
            ),

        (0,0), ConditionSwitch(
            #pubes
            "GwenX.Pubes", Recolor("Gwen", "Pubes", "images/GwenSprite/Gwen_Sprite_Pubes.png"),
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Necklaces
#            "GwenX.Neck == 'choker'", "images/GwenSprite/Gwen_Sprite_Neck_Choker.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Chest layer
            "GwenX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "GwenX.Chest == 'lace bra'", Recolor("Gwen", "Chest", "images/GwenSprite/Gwen_Sprite_Chest_Lace_Up.png"),
                    "GwenX.Chest == 'bra'", Recolor("Gwen", "Chest", "images/GwenSprite/Gwen_Sprite_Chest_Bra_Up.png"),
                    "GwenX.Chest == 'tank'", Recolor("Gwen", "Chest", "images/GwenSprite/Gwen_Sprite_Chest_Tank_Up.png"),
                    "GwenX.Chest == 'bikini top'", Recolor("Gwen", "Chest", "images/GwenSprite/Gwen_Sprite_Chest_Bikini_Up.png"),
                    "True", Null(),
                    ),
            "GwenX.Chest == 'lace bra'", Recolor("Gwen", "Chest", "images/GwenSprite/Gwen_Sprite_Chest_Lace.png"),
            "GwenX.Chest == 'bra'", Recolor("Gwen", "Chest", "images/GwenSprite/Gwen_Sprite_Chest_Bra.png"),
            "GwenX.Chest == 'tank'", Recolor("Gwen", "Chest", "images/GwenSprite/Gwen_Sprite_Chest_Tank.png"),
            "GwenX.Chest == 'bikini top'", Recolor("Gwen", "Chest", "images/GwenSprite/Gwen_Sprite_Chest_Bikini.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #stockings
            "GwenX.Hose == 'stockings'", Recolor("Gwen", "Hose", "images/GwenSprite/Gwen_Sprite_Hose_Stockings.png"),
            "GwenX.Hose == 'socks'", Recolor("Gwen", "Hose", "images/GwenSprite/Gwen_Sprite_Hose_Socks.png"),
            "GwenX.Hose == 'stockings and garterbelt'", Recolor("Gwen", "Hose", "images/GwenSprite/Gwen_Sprite_Hose_StockingsGarter.png"),
            "GwenX.Hose == 'garterbelt'", Recolor("Gwen", "Hose", "images/GwenSprite/Gwen_Sprite_Hose_Garter.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #panties
            "not GwenX.Panties", Null(),
            "GwenX.PantiesDown", ConditionSwitch(
                    #if the panties are down
                    "not GwenX.Legs or GwenX.Upskirt or GwenX.Legs == 'skirt' or GwenX.Legs == 'cheer skirt'", ConditionSwitch(
                            #if she's wearing a skirt or nothing else
                            "GwenX.Panties == 'lace panties'", Recolor("Gwen", "Panties", "images/GwenSprite/Gwen_Sprite_Panties_Lace_Down.png"),
#                            "GwenX.Panties == 'bikini bottoms' and GwenX.Wet", "images/GwenSprite/Gwen_Sprite_Panties_Bikini_Down_Wet.png",
                            "GwenX.Panties == 'bikini bottoms'", Recolor("Gwen", "Panties", "images/GwenSprite/Gwen_Sprite_Panties_Bikini_Down.png"),
                            "GwenX.Wet", Recolor("Gwen", "Panties", "images/GwenSprite/Gwen_Sprite_Panties_White_Down_Wet.png"),
                            "True", Recolor("Gwen", "Panties", "images/GwenSprite/Gwen_Sprite_Panties_White_Down.png"),
                            ),
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                #if she's not wet
                "GwenX.Panties == 'lace panties'", Recolor("Gwen", "Panties", "images/GwenSprite/Gwen_Sprite_Panties_Lace.png"),
                "GwenX.Panties == 'bikini bottoms'", Recolor("Gwen", "Panties", "images/GwenSprite/Gwen_Sprite_Panties_Bikini.png"),
                "GwenX.Wet", Recolor("Gwen", "Panties", "images/GwenSprite/Gwen_Sprite_Panties_White_Wet.png"),
                "True", Recolor("Gwen", "Panties", "images/GwenSprite/Gwen_Sprite_Panties_White.png"),
                ),
            ),
        (0,0), ConditionSwitch(
            #pantyhose
            "GwenX.Hose == 'pantyhose' and (not GwenX.PantiesDown or not GwenX.Panties)", Recolor("Gwen", "Hose", "images/GwenSprite/Gwen_Sprite_Hose_Pantyhose.png"),
            "GwenX.Hose == 'tights' and GwenX.Wet and (not GwenX.PantiesDown or not GwenX.Panties)", Recolor("Gwen", "Hose", "images/GwenSprite/Gwen_Sprite_Hose_Tights.png"),
            "GwenX.Hose == 'tights' and (not GwenX.PantiesDown or not GwenX.Panties)", Recolor("Gwen", "Hose", "images/GwenSprite/Gwen_Sprite_Hose_Tights.png"),
            "GwenX.Hose == 'ripped pantyhose' and (not GwenX.PantiesDown or not GwenX.Panties)", Recolor("Gwen", "Hose", "images/GwenSprite/Gwen_Sprite_Hose_Pantyhose_Holed.png"),
            "GwenX.Hose == 'ripped tights' and (not GwenX.PantiesDown or not GwenX.Panties)", Recolor("Gwen", "Hose", "images/GwenSprite/Gwen_Sprite_Hose_Tights_Holed.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over
#            "GwenX.Over == 'open suit' and GwenX.ArmPose == 1", "images/GwenSprite/Gwen_Sprite_Over_Suit_1_Mid.png",                 #no gloved 1
            "GwenX.Over == 'open suit'", Null(), #"images/GwenSprite/Gwen_Sprite_Over_Suit_2_Mid.png",                                        #no gloved 2
            "GwenX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "GwenX.Over == 'suit' or GwenX.Over == 'open suit'", Null(),
                    "GwenX.Over == 'tshirt' and GwenX.ArmPose == 1", Recolor("Gwen", "Over", "images/GwenSprite/Gwen_Sprite_Over_Tshirt_1_Up.png"),
                    "GwenX.Over == 'tshirt'", Recolor("Gwen", "Over", "images/GwenSprite/Gwen_Sprite_Over_Tshirt_2_Up.png"),
                    "GwenX.Over == 'cheer top'", Recolor("Gwen", "Over", "images/GwenSprite/Gwen_Sprite_Over_Cheer_Up.png"),
                    "True", Null(),
                    ),
            #If she's using arm pose 1, left arm pointing
            #If she's using arm pose 2, Left arm on hip
            "GwenX.Over == 'suit' and GwenX.ArmPose == 1 and GwenX.Arms", "images/GwenSprite/Gwen_Sprite_Over_Suit_1G_Mid.png", #gloved 1
            "GwenX.Over == 'suit' and GwenX.ArmPose == 1", "images/GwenSprite/Gwen_Sprite_Over_Suit_1_Mid.png",                 #no gloved 1
#            "GwenX.Over == 'suit' and GwenX.Arms", "images/GwenSprite/Gwen_Sprite_Over_Suit_2G_Mid.png",                        #gloved 2
            "GwenX.Over == 'suit'", "images/GwenSprite/Gwen_Sprite_Over_Suit_2_Mid.png",                                        #no gloved 2


            "GwenX.Over == 'cheer top'", Recolor("Gwen", "Over", "images/GwenSprite/Gwen_Sprite_Over_Cheer.png"),
            "GwenX.Over == 'tshirt' and GwenX.ArmPose == 1", Recolor("Gwen", "Over", "images/GwenSprite/Gwen_Sprite_Over_Tshirt_1_Mid.png"),
            "GwenX.Over == 'tshirt'", Recolor("Gwen", "Over", "images/GwenSprite/Gwen_Sprite_Over_Tshirt_2_Mid.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #pants
            "not GwenX.Legs", Null(),
            "GwenX.Upskirt", ConditionSwitch(
                        #if the skirt's up or pants down
#                        "GwenX.Legs == 'dress' and GwenX.Over == 'dress'", "images/GwenSprite/Gwen_Sprite_Legs_Dress_Up.png",
                        "GwenX.Legs == 'skirt' and GwenX.Over != 'towel'", Recolor("Gwen", "Legs", "images/GwenSprite/Gwen_Sprite_Legs_Skirt_Up.png"),
                        "GwenX.Legs == 'cheer skirt' and GwenX.Over != 'towel'", Recolor("Gwen", "Legs", "images/GwenSprite/Gwen_Sprite_Legs_Cheer_Up.png"),
#                        "GwenX.Legs == 'pants'", "images/GwenSprite/Gwen_Sprite_Legs_Pants_Down.png",
                        "GwenX.Legs == 'shorts' and GwenX.Wet > 1", Recolor("Gwen", "Legs", "images/GwenSprite/Gwen_Sprite_Legs_Shorts_Down_Wet.png"),
                        "GwenX.Legs == 'shorts'", Recolor("Gwen", "Legs", "images/GwenSprite/Gwen_Sprite_Legs_Shorts_Down.png"),
                        "GwenX.Legs == 'suit' and GwenX.Wet > 1", "images/GwenSprite/Gwen_Sprite_Legs_Suit_Down_Wet.png",
                        "GwenX.Legs == 'suit'", "images/GwenSprite/Gwen_Sprite_Legs_Suit_Down.png",
                        "True", Null(),
                        ),
#            "GwenX.Legs == 'dress' and GwenX.Over == 'dress'", "images/GwenSprite/Gwen_Sprite_Legs_Dress.png",
            "GwenX.Legs == 'skirt' and GwenX.Over != 'towel'", Recolor("Gwen", "Legs", "images/GwenSprite/Gwen_Sprite_Legs_Skirt.png"),
            "GwenX.Legs == 'cheer skirt' and GwenX.Over != 'towel'", Recolor("Gwen", "Legs", "images/GwenSprite/Gwen_Sprite_Legs_Cheer.png"),
            "GwenX.Wet > 1", ConditionSwitch(
                #if she's wet
#                "GwenX.Legs == 'pants'", "images/GwenSprite/Gwen_Sprite_Legs_Pants.png",
                "GwenX.Legs == 'shorts'", Recolor("Gwen", "Legs", "images/GwenSprite/Gwen_Sprite_Legs_Shorts_Wet.png"),
                "GwenX.Legs == 'suit'", "images/GwenSprite/Gwen_Sprite_Legs_Suit_Wet.png",
                "True", Null(),
                ),
            #if she's not wet
#            "GwenX.Legs == 'pants'", "images/GwenSprite/Gwen_Sprite_Legs_Pants.png",
            "GwenX.Legs == 'shorts'", Recolor("Gwen", "Legs", "images/GwenSprite/Gwen_Sprite_Legs_Shorts.png"),
            "GwenX.Legs == 'suit'", "images/GwenSprite/Gwen_Sprite_Legs_Suit.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #nude lower piercings
            "not GwenX.Pierce", Null(),
            "(GwenX.Legs == 'skirt' or GwenX.Legs == 'cheer skirt') and not GwenX.Upskirt", Null(),
            "GwenX.Pierce == 'ring'", ConditionSwitch(
                    # if top is up. . .
                    "GwenX.Legs == 'shorts' and not GwenX.Upskirt", "images/GwenSprite/Gwen_Sprite_Pierce_Pussy_Ring_Pink.png",
                    "GwenX.Legs == 'suit' and not GwenX.Upskirt", "images/GwenSprite/Gwen_Sprite_Pierce_Pussy_Ring_White.png",

                    "GwenX.Hose == 'tights'", Null(),

                    "GwenX.Panties == 'lace panties' and not GwenX.PantiesDown", "images/GwenSprite/Gwen_Sprite_Pierce_Pussy_Ring_Lace.png",
#                    "GwenX.Panties == 'bikini bottoms' and not GwenX.PantiesDown", "images/GwenSprite/Gwen_Sprite_Pierce_Pussy_Ring_Pink.png",
                    "GwenX.Panties and not GwenX.PantiesDown", "images/GwenSprite/Gwen_Sprite_Pierce_Pussy_Ring_White.png",

                    "GwenX.Hose == 'pantyhose'", "images/GwenSprite/Gwen_Sprite_Pierce_Pussy_Ring_Lace.png",

                    "True", "images/GwenSprite/Gwen_Sprite_Pierce_Pussy_Ring.png",
                    ),

            "GwenX.Legs == 'shorts' and not GwenX.Upskirt", "images/GwenSprite/Gwen_Sprite_Pierce_Pussy_Barbell_Pink.png",
            "GwenX.Legs == 'suit' and not GwenX.Upskirt", "images/GwenSprite/Gwen_Sprite_Pierce_Pussy_Barbell_White.png",

            "GwenX.Hose == 'tights'", Null(),

            "GwenX.Panties == 'lace panties' and not GwenX.PantiesDown", "images/GwenSprite/Gwen_Sprite_Pierce_Pussy_Barbell_Lace.png",
#            "GwenX.Panties == 'bikini bottoms' and not GwenX.PantiesDown", "images/GwenSprite/Gwen_Sprite_Pierce_Pussy_Barbell_Pink.png",
            "GwenX.Panties and not GwenX.PantiesDown", "images/GwenSprite/Gwen_Sprite_Pierce_Pussy_Barbell_White.png",

            "GwenX.Hose == 'pantyhose'", "images/GwenSprite/Gwen_Sprite_Pierce_Pussy_Barbell_Lace.png",

            "GwenX.Pierce == 'barbell'", "images/GwenSprite/Gwen_Sprite_Pierce_Pussy_Barbell.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #towel
            "GwenX.Uptop", Null(),
            "GwenX.Over == 'towel'", "images/GwenSprite/Gwen_Sprite_Over_Towel.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #naked tit piercings
            "not GwenX.Pierce", Null(),
#            "not GwenX.Pierce or ((GwenX.Over or GwenX.Chest) and not GwenX.Uptop)", Null(),
#            "GwenX.Uptop", Null(),
            #Only does this if she has piercings, has no tops, or has her top up
            "GwenX.Pierce == 'ring'", ConditionSwitch(
                    # if top is up. . .
                    "GwenX.Uptop", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Ring.png",

                    "GwenX.Over == 'suit'", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Ring_Pink.png", #change if new tops added in other colors
                    "GwenX.Over == 'towel' or GwenX.Over == 'tshirt'", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Ring_White.png", #change if new tops added in other colors
                    "GwenX.Over == 'cheer top'", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Ring_Cheer.png", #change if new tops added in other colors

                    "GwenX.Chest == 'lace bra'", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Ring_Lace.png",
                    "GwenX.Chest == 'tank' or GwenX.Chest == 'bra'", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Ring_White.png",
                    "GwenX.Chest == 'bikini top'", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Ring_Pink.png",
                    "True", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Ring.png",
                    ),
            # Pierce is "barbell"
            "GwenX.Uptop", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Barbell.png",

            "GwenX.Over == 'suit'", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Barbell_Pink.png", #change if new tops added in other colors
            "GwenX.Over == 'towel' or GwenX.Over == 'tshirt' or GwenX.Over == 'cheer top'", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Barbell_White.png", #change if new tops added in other colors

            "GwenX.Chest == 'lace bra'", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Barbell_Lace.png",
            "GwenX.Chest == 'tank' or GwenX.Chest == 'bra'", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Barbell_White.png",
            "GwenX.Chest == 'bikini top'", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Barbell_Pink.png",

            "True", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Barbell.png",
            ),

        (0,0), ConditionSwitch(
            #Boots/Shoes
            "GwenX.Boots == 'boots'", Recolor("Gwen", "Boots", "images/GwenSprite/Gwen_Sprite_Boots.png"),
            "GwenX.Boots == 'sneaks'", Recolor("Gwen", "Boots", "images/GwenSprite/Gwen_Sprite_Boots_Sneaks.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Arms 1 upper layer

            "GwenX.Over == 'open suit' and GwenX.ArmPose == 1", "images/GwenSprite/[GwenX.skin_image.skin_path]Gwen_Sprite_Arms1_Top_Suit_Up.png",                                  #no gloved 1
            "GwenX.Over == 'open suit'", "images/GwenSprite/[GwenX.skin_image.skin_path]Gwen_Sprite_Arms2_Top_Suit_Up.png",

            "GwenX.Uptop and GwenX.Over == 'suit' and GwenX.ArmPose == 1 and GwenX.Arms", "images/GwenSprite/Gwen_Sprite_Arms1_Top_SuitG_Up.png", #gloved 1
            "GwenX.Uptop and GwenX.Over == 'suit' and GwenX.ArmPose == 1", "images/GwenSprite/[GwenX.skin_image.skin_path]Gwen_Sprite_Arms1_Top_Suit_Up.png",                 #no gloved 1
            "GwenX.Uptop and GwenX.Over == 'suit' and GwenX.Arms", "images/GwenSprite/Gwen_Sprite_Arms2_Top_SuitG_Up.png",                        #gloved 2
            "GwenX.Uptop and GwenX.Over == 'suit'", "images/GwenSprite/[GwenX.skin_image.skin_path]Gwen_Sprite_Arms2_Top_Suit_Up.png",

            "GwenX.Over == 'suit' and GwenX.ArmPose == 1 and GwenX.Arms", "images/GwenSprite/Gwen_Sprite_Arms1_Top_SuitG.png",                   #gloved 1
            "GwenX.Over == 'suit' and GwenX.ArmPose == 1", "images/GwenSprite/[GwenX.skin_image.skin_path]Gwen_Sprite_Arms1_Top_Suit.png",                                  #no gloved 1
            "GwenX.Over == 'suit' and GwenX.Arms", "images/GwenSprite/Gwen_Sprite_Arms2_Top_SuitG.png",                                          #gloved 2
            "GwenX.Over == 'suit'", "images/GwenSprite/[GwenX.skin_image.skin_path]Gwen_Sprite_Arms2_Top_Suit.png",                                                         #no gloved 2

            "GwenX.ArmPose == 1", "images/GwenSprite/[GwenX.skin_image.skin_path]Gwen_Sprite_Arms1_Top.png",        #If she's using arm pose 1, right arm high
            "True", "images/GwenSprite/[GwenX.skin_image.skin_path]Gwen_Sprite_Arms2_Top.png",  #if GwenX.Arms ==2                                        #If she's using arm pose 2, Left arm high
            ),
#        (0,0), ConditionSwitch(
#            #Water effect
#            "GwenX.Water and GwenX.ArmPose == 1", "images/GwenSprite/Gwen_Sprite_Water1_Arm.png",
#            "True", Null(),
#            ),


        (0,0), ConditionSwitch(
            #Chest layer over shirt
            "GwenX.Uptop and GwenX.Over != 'cheer top'", ConditionSwitch(
                    # if top is up. . .
                    "GwenX.Chest == 'lace bra' or GwenX.Chest == 'bra'", Recolor("Gwen", "Chest", "images/GwenSprite/Gwen_Sprite_Chest_Lace_Up_Top.png"),
                    "GwenX.Chest == 'tank'", Recolor("Gwen", "Chest", "images/GwenSprite/Gwen_Sprite_Chest_Tank_Up_Top.png"),
                    "GwenX.Chest == 'bikini top'", Recolor("Gwen", "Chest", "images/GwenSprite/Gwen_Sprite_Chest_Bikini_Up_Top.png"),
                    "True", Null(),
                    ),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #belly spunk
            "'belly' in GwenX.Spunk and Player.Male", "images/GwenSprite/Gwen_Sprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast spunk
            "'tits' in GwenX.Spunk and Player.Male", "images/GwenSprite/Gwen_Sprite_Spunk_Tits.png",
            "True", Null(),
            ),

        (-10,-90), "Gwen_Sprite_Head", #(75,-10)


#        (0,0), "images/GwenSprite/Gwen_Sprite_Headref.png", #53,-45


#        (0,0), ConditionSwitch(
#            #hand spunk
#            "GwenX.ArmPose == 2 or 'hand' not in GwenX.Spunk", Null(),
#            "True", "images/GwenSprite/Gwen_Sprite_Spunk_Hand.png",
#            ),
#        (0,0), ConditionSwitch(                                                                         #Props
#            "not GwenX.Held or GwenX.ArmPose != 2", Null(),
#            "GwenX.ArmPose == 2 and GwenX.Held == 'phone'", "images/GwenSprite/Gwen_held_phone.png",
#            "GwenX.ArmPose == 2 and GwenX.Held == 'dildo'", "images/GwenSprite/Gwen_held_dildo.png",
#            "GwenX.ArmPose == 2 and GwenX.Held == 'vibrator'", "images/GwenSprite/Gwen_held_vibrator.png",
#            "GwenX.ArmPose == 2 and GwenX.Held == 'panties'", "images/GwenSprite/Gwen_held_panties.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #UI tool for When Rogue is masturbating using RogueX.Offhand actions while lead
            "Trigger == 'lesbian' or not GwenX.Offhand",Null(),# or Ch_Focus is not GwenX", Null(),
            "GwenX.Offhand == 'fondle pussy' and Trigger != 'sex' and GwenX.Lust >= 70", "GirlFingerPussy_Gwen",
            "GwenX.Offhand == 'fondle pussy'", "GirlGropePussy_Gwen",
            "GwenX.Offhand == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeLeftBreast_Gwen",    #When zero is working the right breast, fondle left
            "GwenX.Offhand == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeRightBreast_Gwen", #When zero is working the left breast, fondle right
            "GwenX.Offhand == 'fondle breasts'", "GirlGropeRightBreast_Gwen",
            "GwenX.Offhand == 'vibrator breasts'", "VibratorRightBreast_Gwen",
            "GwenX.Offhand == 'vibrator pussy'", "VibratorPussy_Gwen",
            "GwenX.Offhand == 'vibrator pussy insert'", "VibratorPussy_Gwen",
            "GwenX.Offhand == 'vibrator anal'", "VibratorAnal_Gwen",
            "GwenX.Offhand == 'vibrator anal insert'", "VibratorPussy_Gwen",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #UI tool for RogueX.Offhand(lesbian) actions (ie Kitty's hand on her when Rogue is secondary)
            "not Partner or Partner is GwenX or GwenX in Nearby", Null(),
            "Partner.Offhand == 'fondle girl pussy' and Trigger != 'sex' and GwenX.Lust >= 70", "GirlFingerPussy_Gwen",
            "Partner.Offhand == 'fondle girl pussy'", "GirlGropePussy_Gwen",
            "Partner.Offhand == 'lick girl pussy'", "Lickpussy_Gwen",
            "Partner.Offhand == 'suck girl breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Gwen",
            "Partner.Offhand == 'suck girl breasts'", "LickRightBreast_Gwen",
            "Partner.Offhand == 'fondle girl breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Gwen",    #When zero is working the right breast, fondle left
            "Partner.Offhand == 'fondle girl breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Gwen", #When zero is working the left breast, fondle right
            "Partner.Offhand == 'fondle girl breasts'", "GirlGropeRightBreast_Gwen",
            "Partner.Offhand == 'vibrator girl breasts'", "VibratorRightBreast_Gwen",
            "Partner.Offhand == 'vibrator girl pussy'", "VibratorPussy_Gwen",
            "Partner.Offhand == 'vibrator girl pussy insert'", "VibratorPussy_Gwen",
            "Partner.Offhand == 'vibrator girl anal'", "VibratorAnal_Gwen",
            "Partner.Offhand == 'vibrator girl anal insert'", "VibratorPussy_Gwen",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for when RogueX is the partner in the scene, and the lead is working on her
            "not Partner or Partner is not GwenX", Null(),
            "Ch_Focus.Offhand == 'fondle girl pussy' and Trigger != 'sex' and GwenX.Lust >= 70", "GirlFingerPussy_Gwen",
            "Ch_Focus.Offhand == 'fondle girl pussy'", "GirlGropePussy_Gwen",
            "Ch_Focus.Offhand == 'lick girl pussy'", "Lickpussy_Gwen",
            "Ch_Focus.Offhand == 'suck girl breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Gwen",
            "Ch_Focus.Offhand == 'suck girl breasts'", "LickRightBreast",
            "Ch_Focus.Offhand == 'fondle girl breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Gwen",    #When zero is working the right breast, fondle left
            "Ch_Focus.Offhand == 'fondle girl breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Gwen", #When zero is working the left breast, fondle right
            "Ch_Focus.Offhand == 'fondle girl breasts'", "GirlGropeRightBreast_Gwen",
            "Ch_Focus.Offhand == 'vibrator girl breasts'", "VibratorRightBreast_Gwen",
            "Ch_Focus.Offhand == 'vibrator girl pussy'", "VibratorPussy_Gwen",
            "Ch_Focus.Offhand == 'vibrator girl pussy insert'", "VibratorPussy_Gwen",
            "Ch_Focus.Offhand == 'vibrator girl anal'", "VibratorAnal_Gwen",
            "Ch_Focus.Offhand == 'vibrator girl anal insert'", "VibratorPussy_Gwen",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger1(primary) actions
            "not Trigger or Ch_Focus is not GwenX", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast_Gwen",
            "Trigger == 'fondle thighs'", "GropeThigh_Gwen",
            "Trigger == 'fondle breasts'", "GropeLeftBreast_Gwen",
            "Trigger == 'suck breasts'", "LickRightBreast_Gwen",
            "Trigger == 'vibrator pussy'", "VibratorPussy_Gwen",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy_Gwen",
            "Trigger == 'vibrator anal'", "VibratorAnal_Gwen",
            "Trigger == 'vibrator anal insert'", "VibratorPussy_Gwen",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_Gwen",
            "Trigger == 'fondle pussy'", "GropePussy_Gwen",
            "Trigger == 'lick pussy'", "Lickpussy_Gwen",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus is not GwenX", Null(),
#            "Trigger == 'fondle breasts' and not GwenX.Offhand", "GropeRightBreast_Gwen",  #"Trigger == 'fondle breasts' and not RogueX.Offhand",
            #When doing nothing offhand, use both hands on breasts.
            "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast_Gwen",
            #When sucking right breast, fondle left
            "Trigger2 == 'fondle breasts'", "GropeLeftBreast_Gwen",
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast_Gwen",
            #When sucking right breast, vibrator left
            "Trigger2 == Trigger", Null(),
            #When both triggers are the same, do nothing
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast_Gwen",
            "Trigger2 == 'suck breasts'", "LickLeftBreast_Gwen",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy_Gwen",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy_Gwen",
            "Trigger2 == 'vibrator anal'", "VibratorAnal_Gwen",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy_Gwen",
            "Trigger2 == 'fondle pussy'", "GropePussy_Gwen",
            "Trigger2 == 'lick pussy'", "Lickpussy_Gwen",
            "Trigger2 == 'fondle thighs'", "GropeThigh_Gwen",
            "True", Null(),
            ),

        )
    anchor (0.5, 0.0)
    offset (25,20)#30
    zoom .78  #.75


image Gwen_Sprite_HairBack:
    LiveComposite(
        (900,900),
        (0,0), ConditionSwitch(
                #hair back
    #            "renpy.showing('Gwen_BJ_Animation')", Null(),
    #            "renpy.showing('Gwen_SexSprite')", "images/GwenSex/Gwen_Sprite_Hair_Long_UnderSex.png",
    #            "GwenX.Hair == 'wet' or GwenX.Water", "images/GwenSprite/Gwen_Sprite_Hair_Wet_Under.png",
                "GwenX.Hat == 'mask'", Null(),
                "GwenX.Hair == 'wet' or GwenX.Water", Recolor("Gwen", "Hair", "images/GwenSprite/Gwen_Sprite_Hair_Wet_Back.png"),
                "not Player.Male and 'facial' in GwenX.Spunk",Recolor("Gwen", "Hair", "images/GwenSprite/Gwen_Sprite_Hair_Wet_Back.png"),
                "GwenX.Hair == 'pony'", Recolor("Gwen", "Hair", "images/GwenSprite/Gwen_Sprite_Hair_Pony_Back.png"),
                "True", Recolor("Gwen", "Hair", "images/GwenSprite/Gwen_Sprite_Hair_Short_Back.png"),
                ),
        )
#    contains:
#        ConditionSwitch(
#                #hair back
#    #            "renpy.showing('Gwen_BJ_Animation')", Null(),
#    #            "renpy.showing('Gwen_SexSprite')", "images/GwenSex/Gwen_Sprite_Hair_Long_UnderSex.png",
#    #            "GwenX.Hair == 'wet' or GwenX.Water", "images/GwenSprite/Gwen_Sprite_Hair_Wet_Under.png",
#                "GwenX.Hat == 'mask'", Null(),
#                "GwenX.Hair == 'wet' or GwenX.Water", Recolor("Gwen", "Hair", "images/GwenSprite/Gwen_Sprite_Hair_Wet_Back.png"),
#                "not Player.Male and 'facial' in GwenX.Spunk",Recolor("Gwen", "Hair", "images/GwenSprite/Gwen_Sprite_Hair_Wet_Back.png"),
#                "True", Recolor("Gwen", "Hair", "images/GwenSprite/Gwen_Sprite_Hair_Short_Back.png"),
#                ),
#    "images/GwenSprite/Gwen_Sprite_Hair_Long_Under.png"
    anchor (0.5, 0.5)
    zoom .47#.47
    transform_anchor True
    rotate -10


image Gwen_Sprite_Head:
    LiveComposite(
        (900,900),
        (0,0), ConditionSwitch(
                # Face background plate
#                "renpy.showing('Gwen_SexSprite') and GwenX.Blush >= 2", "images/GwenSprite/Gwen_Sprite_Head_Sex_Blush2.png",
#                "renpy.showing('Gwen_SexSprite') and GwenX.Blush", "images/GwenSprite/Gwen_Sprite_Head_Sex_Blush1.png",
#                "renpy.showing('Gwen_SexSprite')", "images/GwenSprite/Gwen_Sprite_Head_Sex.png",
                "GwenX.Hat == 'mask' and GwenX.Blush", Recolor("Gwen", "Hat", "images/GwenSprite/[GwenX.skin_image.skin_path]Gwen_Sprite_Mask_Blush.png"),
                "GwenX.Hat == 'mask'", Recolor("Gwen", "Hat", "images/GwenSprite/[GwenX.skin_image.skin_path]Gwen_Sprite_Mask.png"),
                "GwenX.Blush >= 2", "images/GwenSprite/[GwenX.skin_image.skin_path]Gwen_Sprite_Head_Blush2.png",
                "GwenX.Blush", "images/GwenSprite/[GwenX.skin_image.skin_path]Gwen_Sprite_Head_Blush.png",
                "True", "images/GwenSprite/[GwenX.skin_image.skin_path]Gwen_Sprite_Head.png",
                ),
        (0,0), ConditionSwitch(
            #chin spunk
            "'chin' in GwenX.Spunk and Player.Male", "images/GwenSprite/Gwen_Sprite_Spunk_Chin.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Mouths
            "GwenX.Mouth == 'lipbite'", Recolor("Gwen", "Lips", "images/GwenSprite/Gwen_Sprite_Mouth_Lipbite.png"),
            "GwenX.Mouth == 'sucking'", Recolor("Gwen", "Lips", "images/GwenSprite/Gwen_Sprite_Mouth_Open.png"),
            "GwenX.Mouth == 'kiss'", Recolor("Gwen", "Lips", "images/GwenSprite/Gwen_Sprite_Mouth_Kiss.png"),
            "GwenX.Mouth == 'sad'", Recolor("Gwen", "Lips", "images/GwenSprite/Gwen_Sprite_Mouth_Sad.png"),
            "GwenX.Mouth == 'smile'", Recolor("Gwen", "Lips", "images/GwenSprite/Gwen_Sprite_Mouth_Smile.png"),
            "GwenX.Mouth == 'surprised'", Recolor("Gwen", "Lips", "images/GwenSprite/Gwen_Sprite_Mouth_Open.png"),
            "not Player.Male and 'mouth' in GwenX.Spunk and GwenX.Mouth == 'tongue'", Recolor("Gwen", "Lips", "images/GwenSprite/Gwen_Sprite_Mouth_Tongue_Wet.png"),
            "GwenX.Mouth == 'tongue'", Recolor("Gwen", "Lips", "images/GwenSprite/Gwen_Sprite_Mouth_Tongue.png"),
            "GwenX.Mouth == 'grimace'", Recolor("Gwen", "Lips", "images/GwenSprite/Gwen_Sprite_Mouth_Smile.png"),
            "GwenX.Mouth == 'smirk'", Recolor("Gwen", "Lips", "images/GwenSprite/Gwen_Sprite_Mouth_Smirk.png"),
            "GwenX.Mouth == 'open'", Recolor("Gwen", "Lips", "images/GwenSprite/Gwen_Sprite_Mouth_Open.png"),
            "True", Recolor("Gwen", "Lips", "images/GwenSprite/Gwen_Sprite_Mouth_Normal.png"),
            ),
        (0,0), ConditionSwitch(
            #Mouths spunk
            "'mouth' not in GwenX.Spunk or not Player.Male", Null(),
            "GwenX.Mouth == 'sucking'", "images/GwenSprite/Gwen_Sprite_Spunk_Open.png",
            "GwenX.Mouth == 'kiss'", "images/GwenSprite/Gwen_Sprite_Spunk_Sad.png",
            "GwenX.Mouth == 'sad'", "images/GwenSprite/Gwen_Sprite_Spunk_Sad.png",
            "GwenX.Mouth == 'smile'", "images/GwenSprite/Gwen_Sprite_Spunk_Smile.png",
            "GwenX.Mouth == 'surprised'", "images/GwenSprite/Gwen_Sprite_Spunk_Open.png",
            "GwenX.Mouth == 'tongue'", "images/GwenSprite/Gwen_Sprite_Spunk_Open.png",
            "GwenX.Mouth == 'grimace'", "images/GwenSprite/Gwen_Sprite_Spunk_Smile.png",
            "True", "images/GwenSprite/Gwen_Sprite_Spunk_Smirk.png",
            ),
        (0,0), ConditionSwitch(
            #wet face
            "Player.Male", Null(),
            "'mouth' not in GwenX.Spunk and 'chin' not in GwenX.Spunk", Null(),
#            "'chin' not in GwenX.Spunk and GwenX.Mouth == 'tongue'", "images/GwenSprite/Gwen_Sprite_Wet_Tongue.png",
#            "GwenX.Mouth == 'tongue'", "images/GwenSprite/Gwen_Sprite_Wet_Tongue2.png",
            "'chin' in GwenX.Spunk", "images/GwenSprite/Gwen_Sprite_Wet_Mouth.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(     #    (0,5)
            #brows
            "GwenX.Hat == 'mask' and GwenX.Brows == 'angry' and GwenX.Blush", "images/GwenSprite/Gwen_Sprite_Brows_Angry_MBlush.png",
            "GwenX.Hat == 'mask' and GwenX.Brows == 'angry'", "images/GwenSprite/Gwen_Sprite_Brows_Angry_M.png",
            "GwenX.Hat == 'mask' and GwenX.Brows == 'sad' and GwenX.Blush", "images/GwenSprite/Gwen_Sprite_Brows_Sad_MBlush.png",
            "GwenX.Hat == 'mask' and GwenX.Brows == 'sad'", "images/GwenSprite/Gwen_Sprite_Brows_Sad_M.png",
            "GwenX.Hat == 'mask' and GwenX.Blush >= 2", "images/GwenSprite/Gwen_Sprite_Brows_Normal_MBlush.png",
            "GwenX.Hat == 'mask'", "images/GwenSprite/Gwen_Sprite_Brows_Normal_M.png",
            "GwenX.Brows == 'angry'", "images/GwenSprite/Gwen_Sprite_Brows_Angry.png",
            "GwenX.Brows == 'sad'", "images/GwenSprite/Gwen_Sprite_Brows_Sad.png",
            "GwenX.Brows == 'surprised'", "images/GwenSprite/Gwen_Sprite_Brows_Surprised.png",
            "GwenX.Brows == 'confused'", "images/GwenSprite/Gwen_Sprite_Brows_Confused.png",
            "True", "images/GwenSprite/Gwen_Sprite_Brows_Normal.png",
            ),
        (0,0), "Gwen Blink",     #Eyes  (0,5)
        (0,0), ConditionSwitch(
            #Hair over
#            "renpy.showing('Gwen_TJ_Animation')", Null(),
            "GwenX.Hat == 'mask'", Null(),
            "GwenX.Hair == 'wet' or GwenX.Water", Recolor("Gwen", "Hair", "images/GwenSprite/Gwen_Sprite_Hair_Wet.png"),
            "not Player.Male and 'facial' in GwenX.Spunk",Recolor("Gwen", "Hair", "images/GwenSprite/Gwen_Sprite_Hair_Wet.png"),
            "GwenX.Hair == 'pony'", Recolor("Gwen", "Hair", "images/GwenSprite/Gwen_Sprite_Hair_Pony.png"),
            "True", Recolor("Gwen", "Hair", "images/GwenSprite/Gwen_Sprite_Hair_Short.png"),
            ),
        (0,0), ConditionSwitch(
            #Hair Water
            "GwenX.Water", "images/GwenSprite/Gwen_Sprite_Wet_Face.png",
            "not Player.Male and 'facial' in GwenX.Spunk", "images/GwenSprite/Gwen_Sprite_Wet_Face.png",
            "True",Null(),
            ),
        (0,0), ConditionSwitch(
            #facial spunk
            "'hair' in GwenX.Spunk and Player.Male", "images/GwenSprite/Gwen_Sprite_Spunk_Hair.png",
            "'facial' in GwenX.Spunk and Player.Male", "images/GwenSprite/Gwen_Sprite_Spunk_Facial.png",
            "True", Null(),
            ),
        )
    anchor (0.5, 0.5)
    zoom .47#.38
    transform_anchor True
    rotate -10
#    alpha 0.9

image Gwen Blink:
    ConditionSwitch(
    "GwenX.Eyes == 'closed'", "images/GwenSprite/Gwen_Sprite_Eyes_Closed.png",
    "GwenX.Hat == 'mask' and GwenX.Brows == 'angry'", "images/GwenSprite/Gwen_Sprite_Eyes_MAngry.png",
    "GwenX.Hat == 'mask' and (GwenX.Eyes == 'surprised' or GwenX.Brows == 'surprised')", "images/GwenSprite/Gwen_Sprite_Eyes_MSurprised.png",
    "GwenX.Hat == 'mask'", "images/GwenSprite/Gwen_Sprite_Eyes_MNormal.png",
    "GwenX.Eyes == 'sexy'", "images/GwenSprite/Gwen_Sprite_Eyes_Sexy.png",
    "GwenX.Eyes == 'side'", "images/GwenSprite/Gwen_Sprite_Eyes_Side.png",
    "GwenX.Eyes == 'surprised'", "images/GwenSprite/Gwen_Sprite_Eyes_Surprised.png",
    "GwenX.Eyes == 'normal'", "images/GwenSprite/Gwen_Sprite_Eyes_Normal.png",
    "GwenX.Eyes == 'stunned'", "images/GwenSprite/Gwen_Sprite_Eyes_Stunned.png",
    "GwenX.Eyes == 'down'", "images/GwenSprite/Gwen_Sprite_Eyes_Down.png",
    "GwenX.Eyes == 'leftside'", "images/GwenSprite/Gwen_Sprite_Eyes_Leftside.png",
    "GwenX.Eyes == 'manic'", "images/GwenSprite/Gwen_Sprite_Eyes_Sexy.png",#"images/GwenSprite/Gwen_Sprite_Eyes_Squint.png",
    "GwenX.Eyes == 'squint'", "images/GwenSprite/Gwen_Sprite_Eyes_Sexy.png",#"Gwen_Squint",
    "True", "images/GwenSprite/Gwen_Sprite_Eyes_Normal.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/GwenSprite/Gwen_Sprite_Eyes_Closed.png"
    .25
    repeat

#image Gwen_Squint:
#    "images/GwenSprite/Gwen_Sprite_Eyes_Sexy.png"
#    choice:
#        3.5
#    choice:
#        3.25
#    choice:
#        3
#    "images/GwenSprite/Gwen_Sprite_Eyes_Squint.png"
#    .25
#    repeat


#image Gwen_Drip_Mask:
#    #This is the mask for her drip pattern
#    contains:
#        "images/GwenSprite/Gwen_Sprite_WetMask.png"
#        offset (-275,-560)#(-145,-560)#(-225,-560)

#image Gwen_Drip_MaskPanties:
#    #This is the mask for her drip pattern in panties down mode
#    contains:
#        "images/GwenSprite/Gwen_Sprite_DripMaskPanties.png"
#        offset (-145,-560)#(-225,-560)

#image Gwen_Drip_MaskP:
#    #This is the mask for her drip pattern in panties down mode
#    contains:
#        "images/GwenSprite/Gwen_Sprite_WetMask_Pants.png"
#        offset (-275,-560)#(-145,-560)

# End Gwen Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Gwen Doggy Compositing ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#image Gwen_Doggy_Base = LiveComposite(
image Gwen_Doggy_Animation: #nee Gwen_Doggy
    LiveComposite(
        #Base body
        (420,750),
        (0,0), ConditionSwitch(
            #Shows different upper body motion depending on events
            "not Player.Sprite", "Gwen_Doggy_Body",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Gwen_Doggy_Fuck2_Top",
                    "Speed > 1", "Gwen_Doggy_Fuck_Top",
                    "Speed", "Gwen_Doggy_Anal_Head_Top",
                    "True", "Gwen_Doggy_Body",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Gwen_Doggy_Fuck2_Top",
                    "Speed > 1", "Gwen_Doggy_Fuck_Top",
                    "True", "Gwen_Doggy_Body",
                    ),
            "Player.Cock == 'foot'", ConditionSwitch(
                    "Speed > 1", "Gwen_Doggy_Foot2_Top",
                    "Speed", "Gwen_Doggy_Foot1_Top",
                    "True", "Gwen_Doggy_Foot0_Top",
                    ),
            "True", "Gwen_Doggy_Body",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events
            "not Player.Sprite", "Gwen_Doggy_Ass",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Gwen_Doggy_Fuck2_Ass",
                    "Speed > 1", "Gwen_Doggy_Fuck_Ass",
                    "Speed", "Gwen_Doggy_Anal_Head_Ass",
                    "True", "Gwen_Doggy_Ass",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Gwen_Doggy_Fuck2_Ass",
                    "Speed > 1", "Gwen_Doggy_Fuck_Ass",
                    "True", "Gwen_Doggy_Ass",
                    ),
            "Player.Cock == 'foot'", ConditionSwitch(
                    "Speed > 1", "Gwen_Doggy_Foot2_Ass",
                    "Speed", "Gwen_Doggy_Foot1_Ass",
                    "True", "Gwen_Doggy_Foot0_Ass",
                    ),
            "True", "Gwen_Doggy_Ass",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
#            "not Player.Sprite", "Gwen_Doggy_Shins0",
            "Player.Sprite and Player.Cock == 'foot'", ConditionSwitch(
                    "Speed > 1", "Gwen_Doggy_Feet2",
                    "Speed", "Gwen_Doggy_Feet1",
                    "True", "Gwen_Doggy_Feet0",
                    ),
            "ShowFeet", "Gwen_Doggy_Shins0",# "not Player.Sprite and ShowFeet", "Gwen_Doggy_Shins",
            "True", Null(),
            ),
        )
    align (0.6,0.0)
    #yoffset 50
# End Base / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Gwen_Doggy_Body:
    LiveComposite(
        #Upper body
        (610,750),
        #(165,0),"Gwen_Doggy_Hair_Under", #back of the hair
#        (0,60), "Gwen_Doggy_Head",               #Head

        (0,0), ConditionSwitch(
            #head
            "GwenX.Facing", "Gwen_Doggy_Head_Fore",
            "GwenX.Hat", "Gwen_Doggy_Head_Mask",
            "True", "Gwen_Doggy_Head",
            ),
        #(0,0), "images/GwenDoggy/Gwen_Doggy_HeadRef.png",               #Head

        (0,0), "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Body.png", #Body base
        (0,0), ConditionSwitch(
            #tanktop
            "not GwenX.Chest", Null(),
            "GwenX.Uptop", ConditionSwitch(
                    "GwenX.Chest == 'tank'", Recolor("Gwen", "Chest", "images/GwenDoggy/Gwen_Doggy_Chest_Tank_Up.png"),
                    "GwenX.Chest == 'bikini top'", Recolor("Gwen", "Chest", "images/GwenDoggy/Gwen_Doggy_Chest_Bikini_Up.png"),
                    "True", Recolor("Gwen", "Chest", "images/GwenDoggy/Gwen_Doggy_Chest_Bra_Up.png"),
                    ),
            "GwenX.Chest == 'tank'", Recolor("Gwen", "Chest", "images/GwenDoggy/Gwen_Doggy_Chest_Tank.png"),
            "GwenX.Chest == 'bikini top'", Recolor("Gwen", "Chest", "images/GwenDoggy/Gwen_Doggy_Chest_Bikini.png"),
            "True", Recolor("Gwen", "Chest", "images/GwenDoggy/Gwen_Doggy_Chest_Bra.png"),
            ),
#        (0,0), ConditionSwitch(
#            #Wet look
#            "GwenX.Water", "images/RogueDoggy/Rogue_Doggy_WetTop.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Overshirt
            "not GwenX.Over", Null(),
            "GwenX.Over == 'tshirt' and GwenX.Uptop", Recolor("Gwen", "Over", "images/GwenDoggy/Gwen_Doggy_Over_TShirt_Up.png"),
            "GwenX.Over == 'tshirt'", Recolor("Gwen", "Over", "images/GwenDoggy/Gwen_Doggy_Over_TShirt.png"),
            "GwenX.Over == 'cheer top' and GwenX.Uptop", Recolor("Gwen", "Over", "images/GwenDoggy/Gwen_Doggy_Over_Cheer_Up.png"),
            "GwenX.Over == 'cheer top'", Recolor("Gwen", "Over", "images/GwenDoggy/Gwen_Doggy_Over_Cheer.png"),
            "GwenX.Over == 'suit' or GwenX.Over == 'open suit'", "images/GwenDoggy/Gwen_Doggy_Over_Suit.png",
            "GwenX.Over == 'towel' and GwenX.Uptop", "images/GwenDoggy/Gwen_Doggy_Over_Towel_Up.png",
            "GwenX.Over == 'towel'", "images/GwenDoggy/Gwen_Doggy_Over_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #spunk back Layer
            "'back' in GwenX.Spunk and Player.Male", "images/GwenDoggy/Gwen_Doggy_Spunk_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast fondling animation
            "Trigger == 'fondle breasts' or Trigger2 == 'fondle breasts'", "Gwen_Doggy_GropeBreast",
            "True", Null()
            ),
        #(161,-1), "Gwen_Doggy_Head",               #Head
        #(165,0),"Gwen_Doggy_Hair_Over", #front of the hair
        )
#    transform_anchor True
#    anchor (225,1400)
#    offset (-175,25)#(-200,0)
#    offset (0,25)#(-200,0)
#    zoom .95
#    offset (-350,-180)#(-190,-40)
#    rotate 20
# End Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Gwen_Doggy_Head:
    LiveComposite(
        #Head
        (420,525),
        #(0,0), "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Head.png", #Body base
        #(0,0), "images/GwenDoggy/Gwen_Doggy_TestArm.png",#Eyes
        (0,0), ConditionSwitch(
            #Hair back
            "GwenX.Water or GwenX.Hair == 'wet'", Recolor("Gwen", "Hair", "images/GwenDoggy/Gwen_Doggy_Hair_Wet_Back.png"),
            "not Player.Male and 'facial' in GwenX.Spunk",Recolor("Gwen", "Hair", "images/GwenDoggy/Gwen_Doggy_Hair_Wet_Back.png"),
            "GwenX.Hair == 'pony'", Null(),
            "True", Recolor("Gwen", "Hair", "images/GwenDoggy/Gwen_Doggy_Hair_Short_Back.png"),
            ),
        (0,0), ConditionSwitch(
            #Head
            #"GwenX.Blush > 1", "images/GwenDoggy/Gwen_Doggy_Head_Blush2.png",
            "GwenX.Blush", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Head_Blush.png",
            "True", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Head.png",
            ),
        (0,0), ConditionSwitch(
            #Mouth
            "GwenX.Mouth == 'normal'", Recolor("Gwen", "Lips", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Mouth_Normal.png"),
            "GwenX.Mouth == 'lipbite'", Recolor("Gwen", "Lips", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Mouth_Normal.png"),
            "GwenX.Mouth == 'sucking'", Recolor("Gwen", "Lips", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Mouth_Open.png"),
            "GwenX.Mouth == 'kiss'", Recolor("Gwen", "Lips", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Mouth_Sad.png"),
            "GwenX.Mouth == 'sad'", Recolor("Gwen", "Lips", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Mouth_Sad.png"),
            "GwenX.Mouth == 'smile'", Recolor("Gwen", "Lips", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Mouth_Smile.png"),
            "GwenX.Mouth == 'grimace'", Recolor("Gwen", "Lips", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Mouth_Smile.png"),
            "GwenX.Mouth == 'surprised'", Recolor("Gwen", "Lips", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Mouth_Open.png"),
            "GwenX.Mouth == 'tongue'", Recolor("Gwen", "Lips", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Mouth_Tongue.png"),
            "True", Recolor("Gwen", "Lips", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Mouth_Normal.png"),
            ),
#        (0,0), ConditionSwitch(
#            #chin spunk
#            "'chin' in GwenX.Spunk", "images/GwenDoggy/Gwen_Doggy_Spunk_Chin.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Mouth spunk
            "'mouth' not in GwenX.Spunk", Null(),
            #"GwenX.Mouth == 'normal'", "images/GwenDoggy/Gwen_Doggy_Spunk_Normal.png",
            #"GwenX.Mouth == 'sad'", "images/GwenDoggy/Gwen_Doggy_Spunk_Normal.png",
            "GwenX.Mouth == 'lipbite'", "images/GwenDoggy/Gwen_Doggy_Spunk_Sad.png",
            "GwenX.Mouth == 'smile'", "images/GwenDoggy/Gwen_Doggy_Spunk_Smile.png",
            "GwenX.Mouth == 'grimace'", "images/GwenDoggy/Gwen_Doggy_Spunk_Smile.png",
            "GwenX.Mouth == 'sucking'", "images/GwenDoggy/Gwen_Doggy_Spunk_Smile.png",
            #"GwenX.Mouth == 'kiss'", "images/GwenDoggy/Gwen_Doggy_Spunk_Open.png",
            "GwenX.Mouth == 'surprised'", "images/GwenDoggy/Gwen_Doggy_Spunk_Smile.png",
            "GwenX.Mouth == 'tongue'", "images/GwenDoggy/Gwen_Doggy_Spunk_Smile.png",
            "True", "images/GwenDoggy/Gwen_Doggy_Spunk_Sad.png",
            ),
        (0,0), ConditionSwitch(
            #Brows
            #"GwenX.Brows == 'normal'", "images/GwenDoggy/Gwen_Doggy_Brows_Normal.png",
            "GwenX.Brows == 'angry'", "images/GwenDoggy/Gwen_Doggy_Brows_Angry.png",
            "GwenX.Brows == 'sad'", "images/GwenDoggy/Gwen_Doggy_Brows_Sad.png",
            "GwenX.Brows == 'surprised'", "images/GwenDoggy/Gwen_Doggy_Brows_Surprised.png",
            #"GwenX.Brows == 'confused'", "images/GwenDoggy/Gwen_Doggy_Brows_Normal.png",
            "True", "images/GwenDoggy/Gwen_Doggy_Brows_Normal.png",
            ),
        (0,0), "Gwen Doggy Blink",#Eyes
#        (0,0), ConditionSwitch(
#            #Wet look
#            "GwenX.Water", "images/RogueDoggy/Rogue_Doggy_WetTop.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #suit collar
            "GwenX.Over == 'suit' or GwenX.Over == 'open suit'", "images/GwenDoggy/Gwen_Doggy_Head_Collar.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #face spunk
            "'facial' in GwenX.Spunk and Player.Male", "images/GwenDoggy/Gwen_Doggy_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hair
            "GwenX.Water or GwenX.Hair == 'wet'", Recolor("Gwen", "Hair", "images/GwenDoggy/Gwen_Doggy_Hair_Wet.png"),
            "not Player.Male and 'facial' in GwenX.Spunk",Recolor("Gwen", "Hair", "images/GwenDoggy/Gwen_Doggy_Hair_Wet.png"),
            "GwenX.Hair == 'pony'", Recolor("Gwen", "Hair", "images/GwenDoggy/Gwen_Doggy_Hair_Pony.png"),
            "True", Recolor("Gwen", "Hair", "images/GwenDoggy/Gwen_Doggy_Hair_Short.png"),
            ),
        (0,0), ConditionSwitch(
            #face spunk
            "'hair' in GwenX.Spunk and Player.Male", "images/GwenDoggy/Gwen_Doggy_Spunk_Hair.png",
            "GwenX.Water or GwenX.Hair == 'wet'", "images/GwenDoggy/Gwen_Doggy_Head_Wet.png",
            "not Player.Male and 'facial' in GwenX.Spunk","images/GwenDoggy/Gwen_Doggy_Head_Wet.png",
            "True", Null(),
            ),
        )
    #zoom 0.95
    #alpha 0.5
# End Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen Doggy Blink:
        #Eyes
        ConditionSwitch(
        "GwenX.Eyes == 'sexy'", "images/GwenDoggy/Gwen_Doggy_Eyes_Sexy.png",
        "GwenX.Eyes == 'side'", "images/GwenDoggy/Gwen_Doggy_Eyes_Side.png",
#        "GwenX.Eyes == 'normal'", "images/GwenDoggy/Gwen_Doggy_Eyes_Normal.png",
        "GwenX.Eyes == 'closed'", "images/GwenDoggy/Gwen_Doggy_Eyes_Closed.png",
        "GwenX.Eyes == 'manic'", "images/GwenDoggy/Gwen_Doggy_Eyes_Stunned.png",
        "GwenX.Eyes == 'down'", "images/GwenDoggy/Gwen_Doggy_Eyes_Down.png",
        "GwenX.Eyes == 'stunned'", "images/GwenDoggy/Gwen_Doggy_Eyes_Stunned.png",
        "GwenX.Eyes == 'surprised'", "images/GwenDoggy/Gwen_Doggy_Eyes_Surprised.png",
        "GwenX.Eyes == 'squint'", "images/GwenDoggy/Gwen_Doggy_Eyes_Sexy.png",
        "True", "images/GwenDoggy/Gwen_Doggy_Eyes_Normal.png",
        ),
    #    choice:
    #        3.5
    #    choice:
    #        3.25
    #    choice:
    #        3
        3
        # This randomizes the time between blinking.
        "images/GwenDoggy/Gwen_Doggy_Eyes_Closed.png"
        .25
        repeat

image Gwen_Doggy_Head_Mask:
    LiveComposite(
        #Head
        (420,525),
        #(0,0), "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Head.png", #Body base
        #(0,0), "images/GwenDoggy/Gwen_Doggy_TestArm.png",#Eyes

        (0,0), ConditionSwitch(
            #Head
            #"GwenX.Blush > 1", "images/GwenDoggy/Gwen_Doggy_Head_Blush2.png",
            "GwenX.Blush", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Head_Blush.png",
            "True", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Head.png",
            ),
        (0,0), ConditionSwitch(
            #Mouth
            "GwenX.Mouth == 'normal'", Recolor("Gwen", "Lips", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Mouth_Normal.png"),
            "GwenX.Mouth == 'lipbite'", Recolor("Gwen", "Lips", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Mouth_Normal.png"),
            "GwenX.Mouth == 'sucking'", Recolor("Gwen", "Lips", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Mouth_Open.png"),
            "GwenX.Mouth == 'kiss'", Recolor("Gwen", "Lips", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Mouth_Sad.png"),
            "GwenX.Mouth == 'sad'", Recolor("Gwen", "Lips", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Mouth_Sad.png"),
            "GwenX.Mouth == 'smile'", Recolor("Gwen", "Lips", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Mouth_Smile.png"),
            "GwenX.Mouth == 'grimace'", Recolor("Gwen", "Lips", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Mouth_Smile.png"),
            "GwenX.Mouth == 'surprised'", Recolor("Gwen", "Lips", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Mouth_Open.png"),
            "GwenX.Mouth == 'tongue'", Recolor("Gwen", "Lips", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Mouth_Tongue.png"),
            "True", Recolor("Gwen", "Lips", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Mouth_Normal.png"),
            ),
#        (0,0), ConditionSwitch(
#            #chin spunk
#            "'chin' in GwenX.Spunk", "images/GwenDoggy/Gwen_Doggy_Spunk_Chin.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Mouth spunk
            "'mouth' not in GwenX.Spunk", Null(),
            #"GwenX.Mouth == 'normal'", "images/GwenDoggy/Gwen_Doggy_Spunk_Normal.png",
            #"GwenX.Mouth == 'sad'", "images/GwenDoggy/Gwen_Doggy_Spunk_Normal.png",
            "GwenX.Mouth == 'lipbite'", "images/GwenDoggy/Gwen_Doggy_Spunk_Sad.png",
            "GwenX.Mouth == 'smile'", "images/GwenDoggy/Gwen_Doggy_Spunk_Smile.png",
            "GwenX.Mouth == 'grimace'", "images/GwenDoggy/Gwen_Doggy_Spunk_Smile.png",
            "GwenX.Mouth == 'sucking'", "images/GwenDoggy/Gwen_Doggy_Spunk_Smile.png",
            #"GwenX.Mouth == 'kiss'", "images/GwenDoggy/Gwen_Doggy_Spunk_Open.png",
            "GwenX.Mouth == 'surprised'", "images/GwenDoggy/Gwen_Doggy_Spunk_Smile.png",
            "GwenX.Mouth == 'tongue'", "images/GwenDoggy/Gwen_Doggy_Spunk_Smile.png",
            "True", "images/GwenDoggy/Gwen_Doggy_Spunk_Sad.png",
            ),

        (0,0), Recolor("Gwen", "Hat", "images/GwenDoggy/Gwen_Doggy_Mask.png"),

        (0,0), ConditionSwitch(
            #blush
            "GwenX.Blush", "images/GwenDoggy/Gwen_Doggy_Mask_Blush.png",
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #Brows
#            #"GwenX.Brows == 'normal'", "images/GwenDoggy/Gwen_Doggy_Brows_Normal.png",
#            "GwenX.Brows == 'angry'", "images/GwenDoggy/Gwen_Doggy_Brows_Angry.png",
#            "GwenX.Brows == 'sad'", "images/GwenDoggy/Gwen_Doggy_Brows_Sad.png",
#            "GwenX.Brows == 'surprised'", "images/GwenDoggy/Gwen_Doggy_Brows_Surprised.png",
#            #"GwenX.Brows == 'confused'", "images/GwenDoggy/Gwen_Doggy_Brows_Normal.png",
#            "True", "images/GwenDoggy/Gwen_Doggy_Brows_Normal.png",
#            ),
        (0,0), "Gwen Doggy Mask Blink",#Eyes
#        (0,0), ConditionSwitch(
#            #Wet look
#            "GwenX.Water", "images/RogueDoggy/Rogue_Doggy_WetTop.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #suit collar
            "GwenX.Over == 'suit' or GwenX.Over == 'open suit'", "images/GwenDoggy/Gwen_Doggy_Head_Collar.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #face spunk
            "'facial' in GwenX.Spunk and Player.Male", "images/GwenDoggy/Gwen_Doggy_Spunk_Facial.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Hair
#            "GwenX.Water or GwenX.Hair == 'wet'", Recolor("Gwen", "Hair", "images/GwenDoggy/Gwen_Doggy_Hair_Wet.png"),
#            "not Player.Male and 'facial' in GwenX.Spunk",Recolor("Gwen", "Hair", "images/GwenDoggy/Gwen_Doggy_Hair_Wet.png"),
#            "True", Recolor("Gwen", "Hair", "images/GwenDoggy/Gwen_Doggy_Hair_Short.png"),
#            ),
        (0,0), ConditionSwitch(
            #face spunk
            "'hair' in GwenX.Spunk and Player.Male", "images/GwenDoggy/Gwen_Doggy_Spunk_Hair.png",
            "GwenX.Water or GwenX.Hair == 'wet'", "images/GwenDoggy/Gwen_Doggy_Head_Wet.png",
            "not Player.Male and 'facial' in GwenX.Spunk","images/GwenDoggy/Gwen_Doggy_Head_Wet.png",
            "True", Null(),
            ),
        )
    #zoom 0.95
    #alpha 0.5
# End Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen Doggy Mask Blink:
        #Eyes
        ConditionSwitch(
        "GwenX.Eyes == 'closed'", "images/GwenDoggy/Gwen_Doggy_Mask_Eyes_Closed.png",
        "GwenX.Brows == 'angry'", "images/GwenDoggy/Gwen_Doggy_Mask_Eyes_Angry.png",
        "GwenX.Brows == 'sad'", "images/GwenDoggy/Gwen_Doggy_Mask_Eyes_Sad.png",
#        "GwenX.Eyes == 'sexy'", "images/GwenDoggy/Gwen_Doggy_Eyes_Sexy.png",
#        "GwenX.Eyes == 'side'", "images/GwenDoggy/Gwen_Doggy_Eyes_Side.png",
#        "GwenX.Eyes == 'normal'", "images/GwenDoggy/Gwen_Doggy_Eyes_Normal.png",
#        "GwenX.Eyes == 'manic'", "images/GwenDoggy/Gwen_Doggy_Eyes_Stunned.png",
#        "GwenX.Eyes == 'down'", "images/GwenDoggy/Gwen_Doggy_Eyes_Down.png",
#        "GwenX.Eyes == 'stunned'", "images/GwenDoggy/Gwen_Doggy_Eyes_Stunned.png",
        "GwenX.Eyes == 'surprised' or GwenX.Brows == 'surprised'", "images/GwenDoggy/Gwen_Doggy_Mask_Eyes_Surprised.png",
#        "GwenX.Eyes == 'squint'", "images/GwenDoggy/Gwen_Doggy_Eyes_Sexy.png",
        "True", "images/GwenDoggy/Gwen_Doggy_Mask_Eyes_Normal.png",
        ),
    #    choice:
    #        3.5
    #    choice:
    #        3.25
    #    choice:
    #        3
        3
        # This randomizes the time between blinking.
        "images/GwenDoggy/Gwen_Doggy_Eyes_Closed.png"
        .25
        repeat

image Gwen_Doggy_Head_Fore:
    LiveComposite(
        #Head
        (420,525),
        (0,0), ConditionSwitch(
            #Hair
            "GwenX.Hat and (GwenX.Over == 'suit' or GwenX.Over == 'open suit')", Recolor("Gwen", "Hat", "images/GwenDoggy/Gwen_Doggy_Mask_Fore_Suit.png"),
            "GwenX.Hat", Recolor("Gwen", "Hat", "images/GwenDoggy/Gwen_Doggy_Mask_Fore_Suit.png"),
            "GwenX.Water or GwenX.Hair == 'wet'", Recolor("Gwen", "Hair", "images/GwenDoggy/Gwen_Doggy_Hair_Wet_Fore.png"),
            "not Player.Male and 'facial' in GwenX.Spunk",Recolor("Gwen", "Hair", "images/GwenDoggy/Gwen_Doggy_Hair_Wet_Fore.png"),
            "GwenX.Hair == 'pony' and (GwenX.Over == 'suit' or GwenX.Over == 'open suit')", Recolor("Gwen", "Hair", "images/GwenDoggy/Gwen_Doggy_Hair_Pony_Fore_Collar.png"),
            "GwenX.Hair == 'pony'", Recolor("Gwen", "Hair", "images/GwenDoggy/Gwen_Doggy_Hair_Pony_Fore.png"),
            "True", Recolor("Gwen", "Hair", "images/GwenDoggy/Gwen_Doggy_Hair_Short_Fore.png"),
            ),
        )
    #zoom 0.95
    #alpha 0.5
# End Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen_Doggy_Ass:
    LiveComposite(
        #Lower body
        (420,750),
#        (0,0), ConditionSwitch(
#            #Legs backside
#            "GwenX.Legs == 'skirt'","images/GwenDoggy/Gwen_Doggy_Legs_Skirt_Back.png",
#            "not GwenX.Upskirt", Null(),
#            "GwenX.Legs == 'pants'", "images/GwenDoggy/Gwen_Doggy_Legs_Pants_Back.png",
#            "GwenX.Legs == 'yoga pants'", "images/GwenDoggy/Gwen_Doggy_Legs_Yoga_Back.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #Panties back
#            "not GwenX.PantiesDown or (GwenX.Legs == 'pants' and not GwenX.Upskirt)", Null(),
#            "GwenX.Panties == 'wolvie panties'", "images/GwenDoggy/Gwen_Doggy_Panties_Wolvie_Back.png",
#            "GwenX.Panties == 'lace panties'", "images/GwenDoggy/Gwen_Doggy_Panties_Lace_Back.png",
#            "GwenX.Panties", "images/GwenDoggy/Gwen_Doggy_Panties_Back.png",
#            "True", Null(),
#            ),
#        (0,0), "images/GwenDoggy/Gwen_Doggy_Ass.png", #Ass Base


        (0,0), ConditionSwitch(
            #Pussy base
            "GwenX.Legs and not GwenX.Upskirt", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Ass_Closed.png",
            "GwenX.Panties and not GwenX.PantiesDown", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Ass_Closed.png",
            "Player.Sprite and Player.Cock == 'in'", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Ass_Fucking.png",
            "Trigger == 'lick pussy'", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Ass_Open.png",
            "'dildo pussy' in (Trigger,Trigger2,GwenX.Offhand)", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Ass_Fucking.png",#Null(),
            "'fondle pussy' in (Trigger,Trigger2,GwenX.Offhand)", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Ass_Fucking.png",#Null(),
            "Trigger == 'insert pussy'", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Ass_Fucking.png",#Null(),
            "True", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Ass_Closed.png",
            ),
        (0,0), ConditionSwitch(
            #ass red
            "GwenX.Red", "images/GwenDoggy/Gwen_Doggy_Red.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Anus base
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    "Speed", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Anal_FullBase.png",      #Speed 1
                    "True", Null(),               #Speed 0
                    ),
            "'insert ass' in (Trigger,Trigger2,GwenX.Offhand)", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Anal_FullBase.png",
            "'dildo anal' in (Trigger,Trigger2,GwenX.Offhand)", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Anal_FullBase.png",
            "GwenX.Loose > 2", "Gwen_Gape_Anal",    #intentional
            "GwenX.Loose", "images/GwenDoggy/Gwen_Doggy_Asshole_Loose.png",
            "True", "images/GwenDoggy/Gwen_Doggy_Asshole_Tight.png",
            ),

#        (0,0), ConditionSwitch(
#            #Wet look
#            "GwenX.Water", "images/RogueDoggy/Rogue_Doggy_WetAss.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #Hose
            "GwenX.Hose == 'stockings'", Recolor("Gwen", "Hose", "images/GwenDoggy/Gwen_Doggy_Hose_Stockings.png"),
            "GwenX.Hose == 'socks'", Recolor("Gwen", "Hose", "images/GwenDoggy/Gwen_Doggy_Hose_Socks.png"),
#            "Player.Sprite and Player.Cock == 'in'", Null(),
#            "Player.Sprite and Player.Cock == 'anal'", Null(),
            "GwenX.Hose == 'stockings and garterbelt'", Recolor("Gwen", "Hose", "images/GwenDoggy/Gwen_Doggy_Hose_StockingsGarter.png"),
            "GwenX.Hose == 'garterbelt'", Recolor("Gwen", "Hose", "images/GwenDoggy/Gwen_Doggy_Hose_Garter.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Panties if Down
            "not GwenX.PantiesDown or (GwenX.Legs == 'pants' and not GwenX.Upskirt)", Null(),
            "GwenX.Panties == 'lace panties'", Recolor("Gwen", "Panties", "images/GwenDoggy/Gwen_Doggy_Panties_Lace_Down.png"),
            "GwenX.Panties == 'bikini bottoms'", Recolor("Gwen", "Panties", "images/GwenDoggy/Gwen_Doggy_Panties_Bikini_Down.png"),
            "GwenX.Panties", Recolor("Gwen", "Panties", "images/GwenDoggy/Gwen_Doggy_Panties_White_Down.png"),
            "True", Null(),
            ),


        (0,0), ConditionSwitch(
            #spunkpussy Layer
            "'in' in GwenX.Spunk and Player.Cock == 'in' and Player.Male",Null(),# "images/GwenDoggy/Gwen_Doggy_SpunkPussyOpen.png",  #fix for GwenX.Spunk is used later
            "'in' in GwenX.Spunk and Player.Male", "images/JeanDoggy/Jean_Doggy_SpunkPussyClosed.png",
            "GwenX.Wet and Player.Cock == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "GwenX.Wet", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pubes
            "not GwenX.Pubes", Null(),
            "Player.Sprite and Player.Cock == 'in'", Null(), # "images/GwenDoggy/Gwen_Doggy_Pubes_Fuckingucked.png",
            "'dildo pussy' in (Trigger,Trigger2,GwenX.Offhand)", Null(),
            "'fondle pussy' in (Trigger,Trigger2,GwenX.Offhand)",Null(),
            "Trigger == 'insert pussy'", Null(),
            "GwenX.Legs == 'pants' and not GwenX.Upskirt", Recolor("Gwen", "Pubes", "images/GwenDoggy/Gwen_Doggy_Pubes_Clothed.png"),
            "GwenX.Legs == 'mesh pants' and not GwenX.Upskirt", Recolor("Gwen", "Pubes", "images/GwenDoggy/Gwen_Doggy_Pubes_Clothed.png"),
            "GwenX.PantiesDown and Trigger == 'lick pussy'", Recolor("Gwen", "Pubes", "images/GwenDoggy/Gwen_Doggy_Pubes_Open.png"),
            "GwenX.PantiesDown", Recolor("Gwen", "Pubes", "images/GwenDoggy/Gwen_Doggy_Pubes_Closed.png"),
            "GwenX.Panties", Recolor("Gwen", "Pubes", "images/GwenDoggy/Gwen_Doggy_Pubes_Clothed.png"),
            "GwenX.Hose and GwenX.Hose == 'pantyhose'", Recolor("Gwen", "Pubes", "images/GwenDoggy/Gwen_Doggy_Pubes_Clothed.png"),
            "Trigger == 'lick pussy'", Recolor("Gwen", "Pubes", "images/GwenDoggy/Gwen_Doggy_Pubes_Open.png"),
            "True", Recolor("Gwen", "Pubes", "images/GwenDoggy/Gwen_Doggy_Pubes_Closed.png"),
            ),
        (0,0), ConditionSwitch(
            #Pussy Piercings
            "Player.Sprite", Null(),
            "GwenX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_Ring.png",
            "GwenX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_Barbell.png",
            "True", Null(),
            ),


        (2,-8), ConditionSwitch(
            #spunkanal Layer
            "'anal' not in GwenX.Spunk or (Player.Sprite and Player.Cock == 'anal' and Speed >= 1) or not Player.Male", Null(),
#            "Player.Cock == 'anal'", "images/GwenDoggy/Gwen_Doggy_SpunkAnalOpen.png",
            "GwenX.Loose", "images/JeanDoggy/Jean_Doggy_SpunkAnalLoose.png",
            "True", "images/JeanDoggy/Jean_Doggy_SpunkAnalLoose.png",
            ),
        (0,0), ConditionSwitch(
            #Panties if up
            "GwenX.PantiesDown or not GwenX.Panties", Null(),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),
            "GwenX.Panties == 'lace panties'", Recolor("Gwen", "Panties", "images/GwenDoggy/Gwen_Doggy_Panties_Lace.png"),
            "GwenX.Panties == 'bikini bottoms'", Recolor("Gwen", "Panties", "images/GwenDoggy/Gwen_Doggy_Panties_Bikini.png"),
            "GwenX.Wet", Recolor("Gwen", "Panties", "images/GwenDoggy/Gwen_Doggy_Panties_White_Wet.png"),
            "True", Recolor("Gwen", "Panties", "images/GwenDoggy/Gwen_Doggy_Panties_White.png"),
            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #full hose/tights
            "GwenX.Panties and GwenX.PantiesDown", Null(),
            "GwenX.Hose == 'ripped pantyhose'", Recolor("Gwen", "Hose", "images/GwenDoggy/Gwen_Doggy_Hose_Pantyhose_Holed.png"),
            "GwenX.Hose == 'ripped tights'", Recolor("Gwen", "Hose", "images/GwenDoggy/Gwen_Doggy_Hose_Tights_Holed.png"),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
            "GwenX.Hose == 'pantyhose'", Recolor("Gwen", "Hose", "images/GwenDoggy/Gwen_Doggy_Hose_Pantyhose.png"),
            "GwenX.Hose == 'tights'", Recolor("Gwen", "Hose", "images/GwenDoggy/Gwen_Doggy_Hose_Tights.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Legs Layer
            "GwenX.Legs == 'skirt'", ConditionSwitch(
                    "Player.Sprite and Player.Cock == 'anal' and Speed" , Recolor("Gwen", "Legs", "images/GwenDoggy/Gwen_Doggy_Legs_Skirt_Up.png"),   #Rogue_Doggy_Legs_Skirt_UpAnal.png",
                    "GwenX.Upskirt", Recolor("Gwen", "Legs", "images/GwenDoggy/Gwen_Doggy_Legs_Skirt_Up.png"),
                    "True", Recolor("Gwen", "Legs", "images/GwenDoggy/Gwen_Doggy_Legs_Skirt.png"),
                    ),
            "GwenX.Legs == 'cheer skirt'", ConditionSwitch(
                    "Player.Sprite and Player.Cock == 'anal' and Speed" , Recolor("Gwen", "Legs", "images/GwenDoggy/Gwen_Doggy_Legs_Cheer_Up.png"),   #Rogue_Doggy_Legs_Skirt_UpAnal.png",
                    "GwenX.Upskirt", Recolor("Gwen", "Legs", "images/GwenDoggy/Gwen_Doggy_Legs_Cheer_Up.png"),
                    "True", Recolor("Gwen", "Legs", "images/GwenDoggy/Gwen_Doggy_Legs_Cheer.png"),
                    ),
            "GwenX.Legs == 'suit'", ConditionSwitch(
                    "GwenX.Upskirt or GwenX.PantiesDown", "images/GwenDoggy/Gwen_Doggy_Legs_Suit_Down.png",
                    "GwenX.Wet > 1", "images/GwenDoggy/Gwen_Doggy_Legs_Suit_Wet.png",
                    "True", "images/GwenDoggy/Gwen_Doggy_Legs_Suit.png",
                    ),
            "GwenX.Legs == 'shorts'", ConditionSwitch(
                    "GwenX.Upskirt or GwenX.PantiesDown", Recolor("Gwen", "Legs", "images/GwenDoggy/Gwen_Doggy_Legs_Shorts_Down.png"),
                    "GwenX.Wet > 1", Recolor("Gwen", "Legs", "images/GwenDoggy/Gwen_Doggy_Legs_Shorts_Wet.png"),
                    "True", Recolor("Gwen", "Legs", "images/GwenDoggy/Gwen_Doggy_Legs_Shorts.png"),
                    ),
#            "GwenX.Legs == 'yoga pants'", ConditionSwitch(
#                    "GwenX.Upskirt", "images/GwenDoggy/Gwen_Doggy_Legs_Yoga_Down.png",
#                    "GwenX.Wet > 1", "images/GwenDoggy/Gwen_Doggy_Legs_Yoga_Wet.png",
#                    "True", "images/GwenDoggy/Gwen_Doggy_Legs_Yoga.png",
#                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #Over Layer
            "GwenX.Over == 'towel' and GwenX.Legs == 'skirt' and GwenX.Upskirt", Null(),
            "GwenX.Over == 'towel' and (GwenX.Upskirt or GwenX.Legs == 'skirt' or GwenX.Legs == 'cheer skirt')", "images/GwenDoggy/Gwen_Doggy_Legs_Towel_Up.png",
            "GwenX.Over == 'towel'", "images/GwenDoggy/Gwen_Doggy_Legs_Towel.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Pussy Piercings clothed
#            "Player.Sprite", Null(),
#            "GwenX.PantiesDown or (not GwenX.Panties and GwenX.Legs != 'leather pants')", Null(), #if not panties or legs, skip this
#            "GwenX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_RingC.png",
#            "GwenX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_BarbellC.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Pussy Composite
            "GwenX.Legs and not GwenX.Upskirt",Null(),
            "GwenX.Panties and not GwenX.PantiesDown", Null(),
            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Gwen_Pussy_Fucking3",#Speed 3
                    "Speed > 1", "Gwen_Pussy_Fucking2",#Speed 2
                    "Speed", "Gwen_Pussy_Heading",      #Speed 1
                    "True", "Gwen_Pussy_Static",              #Speed 0
                    ),
            "'dildo pussy' in (Trigger,Trigger2,GwenX.Offhand)", "Gwen_Pussy_Fucking2",
            "'fondle pussy' in (Trigger,Trigger2,GwenX.Offhand)", "Gwen_Pussy_Fingering",
            "Trigger == 'insert pussy'", "Gwen_Pussy_Fingering",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Anus Composite
            "GwenX.Legs and not GwenX.Upskirt",Null(),
            "GwenX.Panties and not GwenX.PantiesDown", Null(),
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Gwen_Anal_Fucking2", #Speed 3
                    "Speed > 1", "Gwen_Anal_Fucking",  #Speed 2
                    "Speed", "Gwen_Anal_Heading",      #Speed 1
                    "True", "Gwen_Anal",               #Speed 0
                    ),
            "'insert ass' in (Trigger,Trigger2,GwenX.Offhand)", "Gwen_Anal_Fingering",
            "'dildo anal' in (Trigger,Trigger2,GwenX.Offhand)", "Gwen_Anal_Fucking",
            "GwenX.Plug", "images/PlugIn.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk back Layer
            "'back' in GwenX.Spunk and Player.Male", "images/GwenDoggy/Gwen_Doggy_Spunk_Ass.png",
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
#            "GwenX.Over == 'towel'", Null(),
#            "(GwenX.Legs == 'skirt' or GwenX.Legs == 'other skirt') and GwenX.Upskirt", "images/GwenDoggy/Gwen_Doggy_Hotdog_Upskirt.png",
#            "True", "images/GwenDoggy/Gwen_Doggy_HotdogBack.png",
#            ),
        (0,0), ConditionSwitch(
            #Hotdogging Cock w/ alpha
            "not Player.Sprite or Player.Cock != 'out'", Null(),
            "(GwenX.Legs == 'skirt' or GwenX.Legs == 'cheer skirt') and GwenX.Upskirt and Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "(GwenX.Legs == 'skirt' or GwenX.Legs == 'cheer skirt') and GwenX.Upskirt", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
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


image Gwen_Doggy_Feet:         #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
    contains:
            AlphaMask("Gwen_Doggy_Shins", "images/GwenDoggy/Gwen_Doggy_Feet_Mask.png")

image Gwen_Doggy_Shins:             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
    #Gwen's footjob shins
#    contains:
#        "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Feet.png"
    contains:
            #hose legs
        ConditionSwitch(
            "GwenX.Hose == 'garterbelt'", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Feet.png",
            "GwenX.Hose == 'ripped pantyhose'", Recolor("Gwen", "Hose", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Feet_Hose_Holed.png"),
            "GwenX.Hose == 'ripped tights'", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Feet_Tights_Holed.png",
            "GwenX.Hose == 'tights'", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Feet_Tights.png",
            "GwenX.Hose == 'socks'", "images/GwenDoggy/Gwen_Doggy_Feet_Socks.png",
            "GwenX.Hose", Recolor("Gwen", "Hose", "images/GwenDoggy/Gwen_Doggy_Feet_Hose.png"),
            "True", "images/GwenDoggy/[GwenX.skin_image.skin_path]Gwen_Doggy_Feet.png",
            )
    contains:
        #boots
        ConditionSwitch(
            "GwenX.Boots == 'boots'", Recolor("Gwen", "Boots", "images/GwenDoggy/Gwen_Doggy_Feet_Boots.png"),
            "True", Null(),
            )
    contains:
        #spunk
        ConditionSwitch(
            "'feet' in GwenX.Spunk and Player.Male", "images/GwenDoggy/Gwen_Doggy_Spunk_Feet.png",
            "True", Null(),
            )
#    pos (0,0)

image Gwen_Doggy_Shins0:
        #static animation
        "Gwen_Doggy_Shins"
        offset (0, 0) #(0,150) top


image Gwen_Doggy_GropeBreast:
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

image Gwen_Gape_Anal:
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

image Zero_Gwen_Hotdog_Static:
    # The unmoving version of the hotdog cock
    # called in Doggy Ass LC
    contains:
        "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Gwen_Hotdog_Moving:
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


image Gwen_Pussy_Mask:
    #AlphaMask used to prevent the cock from moving past the pussy
    #Called in "Gwen_Pussy_Moving"
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

image Gwen_Pussy_Mask_Static:
    #AlphaMask used to prevent the cock from moving past the pussy in static pose
    #Called in "Gwen_Pussy_Moving"
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


image Gwen_Pussy_Static:
    #Full Animation for speed 0
    subpixel True
    contains:
        #moving hole
        "images/GwenDoggy/Gwen_Doggy_Pussy_FHole.png"
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
            "GwenX.Pubes", Recolor("Gwen", "Pubes", "images/GwenDoggy/Gwen_Doggy_Pubes_Open.png"),
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
            "GwenX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_Barbell.png",
            "GwenX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_Ring.png",
            "True", Null(),
            )
        offset (-3,8)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in GwenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
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
        AlphaMask("Zero_Gwen_Doggy_Static", "Gwen_Pussy_Mask_Static")

#    contains:
#        # expanding pussy flap
#        AlphaMask("Gwen_PussyHole_Static", "Gwen_Pussy_Hole_Mask_Static")

image Gwen_Pussy_Hole_Mask_Static:
    # This is the alpha used for the little flap in the heading animation "Gwen_Pussy_Moving"
    contains:
        #Base
        AlphaMask("images/GwenDoggy/Gwen_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat

#image Gwen_PussyHole_Static:
#    #This is the image impacted by the mask for the pussy flap in "Gwen_Pussy_Moving"
#    contains:
#        #Mask
#        "images/GwenDoggy/Gwen_Doggy_Pussy_FHeading.png"
#        anchor (0.52,0.69)
#        pos (217,515)
#        zoom 1
#        alpha .9
#        block:
#            ease 1 ypos 512
#            pause 1
#            ease 3 ypos 515
#            repeat


image Zero_Gwen_Doggy_Static:
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

image Gwen_Pussy_Heading:
    #Full Animation for speed 1
    subpixel True
    contains:
        #moving hole
        "images/GwenDoggy/Gwen_Doggy_Pussy_FHole.png"
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
    contains:
        #pubes
        ConditionSwitch(
            "GwenX.Pubes", Recolor("Gwen", "Pubes", "images/GwenDoggy/Gwen_Doggy_Pubes_Fucking.png"),
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
            "GwenX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_Barbell.png",
            "GwenX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_Ring.png",
            "True", Null(),
            )
        offset (-3,8)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in GwenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
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
        AlphaMask("Zero_Gwen_Doggy_Heading", "Gwen_Pussy_Mask")

#    contains:
#        # expanding pussy flap
#        AlphaMask("Gwen_Pussy_Heading_Flap", "Gwen_Pussy_Hole_Mask")
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in GwenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
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


image Gwen_Pussy_Hole_Mask:
    # This is the alpha used for the little flap in the heading animation "Gwen_Pussy_Heading"
    contains:
        #Base
        AlphaMask("images/GwenDoggy/Gwen_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat

#image Gwen_Pussy_Heading_Flap:
#    #This is the image impacted by the mask for the pussy flap in "Gwen_Pussy_Heading"
#    contains:
#        #Mask
#        "images/GwenDoggy/Gwen_Doggy_Pussy_FHeading.png"
#        anchor (0.52,0.69)
#        pos (217,515)
#        zoom 1
#        alpha .9
#        block:
#            ease 1 ypos 505
#            pause 1
#            ease 3 ypos 515
#            repeat

image Gwen_Pussy_Fingering:
    #Full Animation for speed 1
    subpixel True
    contains:
        #moving hole
        "images/GwenDoggy/Gwen_Doggy_Pussy_FHole.png"
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
            "GwenX.Pubes", Recolor("Gwen", "Pubes", "images/GwenDoggy/Gwen_Doggy_Pubes_Open.png"),
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
            "GwenX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_Barbell.png",
            "GwenX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_Ring.png",
            "True", Null(),
            )
        offset (-3,8)

    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in GwenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
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
#        AlphaMask("Gwen_Pussy_Heading_Flap", "Gwen_Pussy_Hole_Mask")

    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in GwenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
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


image Zero_Gwen_Doggy_Heading:
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

image Gwen_Pussy_Fucking2:
    #Full Animation for speed 2
    contains:
        #Base
        "images/GwenDoggy/Gwen_Doggy_Pussy_FHole.png"
    contains:
        #pubes
        ConditionSwitch(
            "GwenX.Pubes", Recolor("Gwen", "Pubes", "images/GwenDoggy/Gwen_Doggy_Pubes_Fucking.png"),
            "True", Null(),
            )
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "GwenX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_Barbell.png",
            "GwenX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_Ring.png",
            "True", Null(),
            )
        offset (-3,8)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in GwenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            "'dildo pussy' in (Trigger,Trigger2,GwenX.Offhand)", AlphaMask("Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "True",AlphaMask("Zero_Gwen_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            ),
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in GwenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )


image Zero_Gwen_Doggy_Fucking2:
    # Sex Speed 2 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat


image Gwen_Pussy_Fucking3:
    #Full Animation for speed 3
    contains:
        #Base
        "images/GwenDoggy/Gwen_Doggy_Pussy_FHole.png"
    contains:
        #pubes
        ConditionSwitch(
            "GwenX.Pubes", Recolor("Gwen", "Pubes", "images/GwenDoggy/Gwen_Doggy_Pubes_Fucking.png"),
            "True", Null(),
            )
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "GwenX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_Barbell.png",
            "GwenX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_Ring.png",
            "True", Null(),
            )
        offset (-3,8)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in GwenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Gwen_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in GwenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )


image Zero_Gwen_Doggy_Fucking3:
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

image Gwen_Anal:
    #Anal static Loose
    contains:
        #Base
        "images/GwenDoggy/Gwen_Doggy_Asshole_Loose.png"
        anchor (0.50,0.69)
        pos (208,500)
        zoom 1.25
    contains:
        #Cock
        "Zero_Doggy_Insert"
        pos (172,500)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Gwen_Anal_Fingering:
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
            "'anal' in GwenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
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
        AlphaMask("Zero_Gwen_Doggy_Anal_Finger", "Gwen_Doggy_Anal_Fingering_Mask")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in GwenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
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

image Zero_Gwen_Doggy_Anal_Finger:
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
image Gwen_Doggy_Anal_Fingering_Mask:
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
image Gwen_Anal_Heading:
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
            "'anal' in GwenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
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
        AlphaMask("Zero_Gwen_Doggy_Anal_Heading", "Gwen_Doggy_Anal_Heading_Mask")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in GwenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
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

image Zero_Gwen_Doggy_Anal_Heading:
        #the cock anal heading animation
    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500#505
            repeat

image Zero_Gwen_Doggy_Anal_HeadingJunk:
    #this is a mask to correct an annoying glitch in the core mask
    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease .5 ypos 550
            pause .25
            ease 1.75 ypos 600#505
            repeat

image Gwen_Doggy_Anal_Heading_Mask:
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

image Gwen_Doggy_Anal_Head_Top:
#animation for anal fucking top half
    contains:
        subpixel True
        "Gwen_Doggy_Body"
        ypos 0
        block:
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat

image Gwen_Doggy_Anal_Head_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Gwen_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -10
            easeout .1 ypos -7
            easein .9 ypos 0
            pause .9
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Gwen_Doggy_Anal1:
    #Animation for speed 2 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat

image Gwen_Anal_Fucking:
    #Animation for speed 2 Ass
    contains:
        #Hole
        "images/GwenDoggy/Gwen_Doggy_Anal_FullHole.png"
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in GwenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            #full hose/tights
            "'dildo anal' in (Trigger,Trigger2,GwenX.Offhand)", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", AlphaMask("Zero_Gwen_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            )
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in GwenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )


image Gwen_Doggy_Fuck_Top:
    #animation for anal fucking top half
    contains:
        subpixel True
        "Gwen_Doggy_Body"
        ypos 15#28
        pause .4
        block:
            ease .2 ypos 5#10
            pause .3
            ease 2 ypos 15#28
            repeat

image Gwen_Doggy_Fuck_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Gwen_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15#-25
            ease .1 ypos -5#-15
            pause .2
            ease 1.6 ypos 0
            repeat


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Gwen_Doggy_Anal2:
    #Animation for speed 3 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat

image Gwen_Anal_Fucking2:
    #Animation for speed 3 Ass
    contains:
        #Hole
        "images/GwenDoggy/Gwen_Doggy_Anal_FullHole.png"
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in GwenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Gwen_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in GwenX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )

image Gwen_Doggy_Fuck2_Top:
    #animation for anal fucking2 top half
    contains:
        subpixel True
        "Gwen_Doggy_Body"
        ypos 20
        block:
            pause .15
            ease .1 ypos 0
            pause .1
            easein .5 ypos 20
            pause .05
            repeat

image Gwen_Doggy_Fuck2_Ass:
    #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Gwen_Doggy_Ass"
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

image Gwen_Doggy_Feet0:
    #static animation
    contains:
        "Gwen_Doggy_Shins"
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
        "Gwen_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            subpixel True
            pause .5
            ease 2 ypos 20
            pause .5
            ease 2 ypos 0
            repeat

image Gwen_Doggy_Foot0_Top:
    #animation for footjob top half
    contains:
        subpixel True
        "Gwen_Doggy_Body"
        ypos 10#28
        #pause .4
        block:
            pause .5
            ease 2 ypos 14
            pause .5
            ease 2 ypos 10
            repeat

image Gwen_Doggy_Foot0_Ass:
    #animation for footjob ass half
    contains:
        subpixel True
        "Gwen_Doggy_Ass"
        ypos 0
        block:     #total 3
            pause .1 #.5
            ease 2 ypos 10
            pause .5
            ease 2.4 ypos 0
            repeat


image Gwen_Doggy_Feet1:
    #slow animation
    contains:
        "Gwen_Doggy_Shins"
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
        "Gwen_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat

image Gwen_Doggy_Foot1_Top:
    #animation for footjob top half
    contains:
        subpixel True
        "Gwen_Doggy_Body"
        ypos 70#28
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 70
            repeat

image Gwen_Doggy_Foot1_Ass:
    #animation for footjob ass half
    contains:
        subpixel True
        "Gwen_Doggy_Ass"
        ypos 0
        block: #total 3
            pause .3
            ease 2 ypos 80
            ease .7 ypos 0
            repeat


image Gwen_Doggy_Feet2:
    #fast animation
    contains:
        "Gwen_Doggy_Shins"
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
        "Gwen_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat

image Gwen_Doggy_Foot2_Top:
    #animation for footjob top half
    contains:
        subpixel True
        "Gwen_Doggy_Body"
        ypos 70#28
        block:
            pause .05
            ease .6 ypos 90#90#110
            ease .3 ypos 70#70
            repeat

image Gwen_Doggy_Foot2_Ass:
    #animation for footjob ass half
    contains:
        subpixel True
        "Gwen_Doggy_Ass"
        ypos 70
        block: #total .95
            pause .15#.05
            ease .6 ypos 90#110
            ease .2 ypos 70
            repeat

# Footjob animations end > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Doggy Launch/Reset
label Gwen_Doggy_Launch(Line = Trigger):
    if renpy.showing("Gwen_Doggy_Animation"):
        return
    $ Speed = 0
    call Girl_Hide(GwenX,1)
    show Gwen_Doggy_Animation at SpriteLoc(StageCenter+48) zorder 150
    with dissolve
    return

label Gwen_Doggy_Reset:
    if not renpy.showing("Gwen_Doggy_Animation"):
        return
#    $ Trigger = 0               #fix, not sure this is a good idea
    $ GwenX.ArmPose = 2
    $ GwenX.SpriteVer = 0
    hide Gwen_Doggy_Animation
    call Girl_Hide(GwenX)
    show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) zorder GwenX.Layer:
            alpha 1 zoom 1 offset (0,0) anchor (0.6, 0.0)
    with dissolve
    $ Speed = 0
    return

# End Gwen Doggy Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



## Start Gwen Sex Pose Content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Gwen Sex Pose core / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen_SexSprite:
    LiveComposite(
        (1120,840),

#        (0,0), ConditionSwitch(
#                #Shows different upper body motion depending on events
#                "True", "Gwen_Sex_Speed2",
#                ),
        (0,0), ConditionSwitch(
                #Shows different motion depending on events
#                "not Player.Sprite", "Gwen_Sex_Body_Static",
                "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Gwen_Sex_Fucking_Speed3",
                        "Speed >= 2", "Gwen_Sex_Fucking_Speed2",
                        "Speed", "Gwen_Sex_Fucking_Speed1",
                        "True", "Gwen_Sex_Fucking_Speed0",
                        ),
                "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Gwen_Sex_Anal_Speed3",
                        "Speed >= 2", "Gwen_Sex_Anal_Speed2",
                        "Speed", "Gwen_Sex_Anal_Speed1",
                        "True", "Gwen_Sex_Anal_Speed0",
                        ),
                "Player.Sprite and Player.Cock == 'out' and Speed >= 2","Gwen_Sex_Hotdog_Speed2",
                "Player.Sprite and Player.Cock == 'out' and Speed >= 1","Gwen_Sex_Hotdog_Speed1",
                "Player.Cock == 'foot'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 2", "Gwen_Sex_FJ_Speed2",
                        "Speed", "Gwen_Sex_FJ_Speed1",
                        "True", "Gwen_Sex_FJ_Speed0",
                        ),
#                "Player.Cock == 'out' and Speed >= 2","Gwen_Hotdog_Body_Anim2",
                "True", "Gwen_Sex_Static",
                ),
        )
    align (0.6,0.0)
    pos (650,303)#(650,393)
    zoom 0.85#0.7

# End Gwen Sex Pose core / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Gwen Sex Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Gwen_Sex_Body:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Gwen_SexSprite
        (1120,840),
        (50,-325), "Gwen_HairBack_Sex",
#        (0,0), ConditionSwitch(
#            #shirt under layer
#            "GwenX.Over == 'red shirt' and GwenX.Uptop", "images/GwenSex/Gwen_Sex_Over_Red_Back.png",
#            "GwenX.Over == 'black shirt' and GwenX.Uptop", "images/GwenSex/Gwen_Sex_Over_Black_Back.png",
#            "True", Null(),
#            ),
        (0,0), "images/GwenSex/[GwenX.skin_image.skin_path]Gwen_Sex_Body.png",
#        (0,0), "images/GwenSex/Gwen_Sex_Headref.png",

        (0,0), ConditionSwitch(
            #shirt layer under open bra
            "(GwenX.Over == 'suit' and GwenX.Uptop) or GwenX.Over == 'open suit'", "images/GwenSex/Gwen_Sex_Over_Suit_Under.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #bra layer
            "not GwenX.Chest", Null(),
            "GwenX.Uptop", ConditionSwitch(
                    #if top's up
                    "GwenX.Chest == 'tank'", Recolor("Gwen", "Chest", "images/GwenSex/Gwen_Sex_Chest_Tank_Up.png"),
                    "GwenX.Chest == 'bikini top'", Recolor("Gwen", "Chest", "images/GwenSex/Gwen_Sex_Chest_Bikini_Up.png"),
                    "GwenX.Chest == 'bra'", Recolor("Gwen", "Chest", "images/GwenSex/Gwen_Sex_Chest_Bra_Up.png"),
                    "GwenX.Chest == 'lace bra'", Recolor("Gwen", "Chest", "images/GwenSex/Gwen_Sex_Chest_Bra_Up.png"),
                    "True", Null(),
                    ),
            #if the top's down. . .
            "GwenX.Chest == 'tank'", Recolor("Gwen", "Chest", "images/GwenSex/Gwen_Sex_Chest_Tank.png"),
            "GwenX.Chest == 'bikini top'", Recolor("Gwen", "Chest", "images/GwenSex/Gwen_Sex_Chest_Bikini.png"),
            "GwenX.Chest == 'bra' and GwenX.Over == 'open suit'", Recolor("Gwen", "Chest", "images/GwenSex/Gwen_Sex_Chest_Bra_Suit.png"),
            "GwenX.Chest == 'bra'", Recolor("Gwen", "Chest", "images/GwenSex/Gwen_Sex_Chest_Bra.png"),
            "GwenX.Chest == 'lace bra' and GwenX.Over == 'open suit'", Recolor("Gwen", "Chest", "images/GwenSex/Gwen_Sex_Chest_Lace_Suit.png"),
            "GwenX.Chest == 'lace bra'", Recolor("Gwen", "Chest", "images/GwenSex/Gwen_Sex_Chest_Lace.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "GwenX.Water", "images/GwenSex/Gwen_Sex_Water_Body.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #shirt layer
            "(GwenX.Over == 'suit' and GwenX.Uptop) or GwenX.Over == 'open suit'", "images/GwenSex/Gwen_Sex_Over_Suit_Up.png",
            "GwenX.Over == 'tshirt' and GwenX.Uptop", Recolor("Gwen", "Over", "images/GwenSex/Gwen_Sex_Over_Tshirt_Up.png"),
            "GwenX.Over == 'cheer top' and GwenX.Uptop", Recolor("Gwen", "Over", "images/GwenSex/Gwen_Sex_Over_Cheer_Up.png"),
            "GwenX.Over == 'suit'", "images/GwenSex/Gwen_Sex_Over_Suit.png",
            "GwenX.Over == 'tshirt'", Recolor("Gwen", "Over", "images/GwenSex/Gwen_Sex_Over_Tshirt.png"),
            "GwenX.Over == 'cheer top'", Recolor("Gwen", "Over", "images/GwenSex/Gwen_Sex_Over_Cheer.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #piercings
            "not GwenX.Pierce", Null(),
            "GwenX.Uptop", ConditionSwitch(
                    #if the top's down. . .
                    "GwenX.Pierce == 'ring'", "images/GwenSex/Gwen_Sex_Pierce_Tits_R.png",
                    "GwenX.Pierce", "images/GwenSex/Gwen_Sex_Pierce_Tits_B.png",
                    "True", Null(),
                    ),
            "GwenX.Pierce == 'ring'", ConditionSwitch(
                    # ring pierce
                    "GwenX.Over == 'suit'", "images/GwenSex/Gwen_Sex_Pierce_Tits_R_Pink.png",
                    "GwenX.Over == 'tshirt'", "images/GwenSex/Gwen_Sex_Pierce_Tits_R_White.png",
                    "GwenX.Over == 'cheer top'", "images/GwenSex/Gwen_Sex_Pierce_Tits_R_Cheer.png",

                    "GwenX.Chest == 'bikini top'", "images/GwenSex/Gwen_Sex_Pierce_Tits_R_Pink.png",
                    "GwenX.Chest == 'lace bra'", "images/GwenSex/Gwen_Sex_Pierce_Tits_R_Lace.png",
                    "GwenX.Chest == 'tank' or GwenX.Chest == 'bra'", "images/GwenSex/Gwen_Sex_Pierce_Tits_R_White.png",

                    "True", "images/GwenSex/Gwen_Sex_Pierce_Tits_R.png",
                    ),
            "GwenX.Over == 'suit'", "images/GwenSex/Gwen_Sex_Pierce_Tits_B_Pink.png",
            "GwenX.Over == 'tshirt' or GwenX.Over == 'cheer top'", "images/GwenSex/Gwen_Sex_Pierce_Tits_B_White.png",

            "GwenX.Chest == 'bikini top'", "images/GwenSex/Gwen_Sex_Pierce_Tits_B_Pink.png",
            "GwenX.Chest == 'lace bra'", "images/GwenSex/Gwen_Sex_Pierce_Tits_B_Lace.png",
            "GwenX.Chest == 'tank' or GwenX.Chest == 'bra'", "images/GwenSex/Gwen_Sex_Pierce_Tits_B_White.png",

            "True", "images/GwenSex/Gwen_Sex_Pierce_Tits_B.png",
            ),

        (50,-325), "Gwen_Head_Sex",  #(0,-300)
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'belly' in GwenX.Spunk and Player.Male", "images/GwenSex/Gwen_Sex_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'tits' in GwenX.Spunk and Player.Male", "images/GwenSex/Gwen_Sex_Spunk_Tits.png",
            "True", Null(),
            ),
#        (0,0), "images/GwenSex/Gwen_Sex_HeadRef.png",
        )
#    yoffset -163
# End Gwen Sex Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Gwen_Head_Sex:
    # The head used for the sex pose, referenced by Gwen_Sex_Body
    "Gwen_Sprite_Head"
    zoom 1.24#1.36
    anchor (0.5,0.5)
    rotate 17#15
#    alpha 0.5

image Gwen_HairBack_Sex:
    # The hair behind the head for the sex pose, referenced by Gwen_Sex_Body
    "Gwen_Sprite_HairBack"
    zoom 1.24#1.36
    anchor (0.5,0.5)
    rotate 17#15


image Gwen_Sex_Lick_Breasts:
        "Lick_Anim"
        zoom 0.7
        offset (400,350)#(390,620)

image Gwen_Sex_Fondle_Breasts:
        "GropeLeftBreast"
        zoom 1.5
        offset (190,-200)#(160,-40)

# Start Gwen Sex Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Gwen_Sex_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Gwen_SexSprite
        (1120,880),
        (545,540), ConditionSwitch(    #165,560
            #Personal Wetness
            "not GwenX.Wet", Null(),
            "(GwenX.Legs == 'pants' or GwenX.Legs == 'shorts') and not GwenX.Upskirt", Null(),
            "GwenX.Panties and not GwenX.PantiesDown", Null(),
            "GwenX.Wet == 1", "Wet_Drip",
            "True", "Wet_Drip2",
            ),

        (545,540), ConditionSwitch(    #205,530
            #Spunk
            "'anal' not in GwenX.Spunk or not Player.Male", Null(),
            "(GwenX.Legs == 'pants' or GwenX.Legs == 'shorts') and not GwenX.Upskirt", Null(),
            "GwenX.Wet == 1", "Spunk_Drip",
            "True", "Spunk_Drip2",
            ),

        (0,0), ConditionSwitch(
            #torso under legs
            "GwenX.Over == 'suit' and not GwenX.Uptop", "images/GwenSex/Gwen_Sex_UnderLegs.png",
            "GwenX.Hose == 'garterbelt' or GwenX.Hose == 'stockings and garterbelt'", "images/GwenSex/Gwen_Sex_UnderLegs.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Legs
            "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/GwenSex/[GwenX.skin_image.skin_path]Gwen_Sex_FBase.png",
            "Player.Sprite and Player.Cock == 'in' and Speed", "images/GwenSex/[GwenX.skin_image.skin_path]Gwen_Sex_FBase.png",
#            "Player.Sprite and Player.Cock == 'in' and Speed", "Gwen_Sex_Heading_Pussy",
#            "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/GwenSex/[GwenX.skin_image.skin_path]Gwen_Sex_Ass.png",
#            "Trigger == 'lick pussy'", "images/GwenSex/[GwenX.skin_image.skin_path]Gwen_Sex_Ass.png",
            "True", "images/GwenSex/[GwenX.skin_image.skin_path]Gwen_Sex_Ass.png",
            ),

        (0,0), ConditionSwitch(
            "Player.Sprite and Player.Cock == 'anal'", "images/GwenSex/[GwenX.skin_image.skin_path]Gwen_Sex_Anus_Cover.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Wet look
            "not GwenX.Water", Null(),
            "True", "images/GwenSex/Gwen_Sex_Water_Legs.png",
            ),

        (0,-10), "Gwen_Sex_Anus",
            #Anus Composite

        (0,0), "Gwen_Sex_Pussy",
            #Pussy Composite


        (0,0), ConditionSwitch(
            #hose layer
            "GwenX.Hose == 'socks'", Recolor("Gwen", "Hose", "images/GwenSex/Gwen_Sex_Hose_Socks.png"),
            "GwenX.Hose == 'stockings and garterbelt'", Recolor("Gwen", "Hose", "images/GwenSex/Gwen_Sex_Hose_StockingsGarter.png"),
            "GwenX.Hose == 'garterbelt'", Recolor("Gwen", "Hose", "images/GwenSex/Gwen_Sex_Hose_Garter.png"),
            "GwenX.Hose == 'stockings'", Recolor("Gwen", "Hose", "images/GwenSex/Gwen_Sex_Hose_Stockings.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Panties if up
            "GwenX.PantiesDown", Null(),
            "GwenX.Panties == 'lace panties'", Recolor("Gwen", "Panties", "images/GwenSex/Gwen_Sex_Panties_Lace.png"),
            "GwenX.Panties == 'bikini bottoms'", Recolor("Gwen", "Panties", "images/GwenSex/Gwen_Sex_Panties_Bikini.png"),
            "GwenX.Panties and GwenX.Wet", Recolor("Gwen", "Panties", "images/GwenSex/Gwen_Sex_Panties_White_Wet.png"),
            "GwenX.Panties", Recolor("Gwen", "Panties", "images/GwenSex/Gwen_Sex_Panties_White.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Piercings under hose
            "not GwenX.Pierce", Null(),
            "GwenX.Pierce == 'ring'",ConditionSwitch(
                    #If she has panties down. . .
                    "Player.Sprite and Player.Cock == 'in'", "images/GwenSex/Gwen_Sex_Pierce_Pussy_R_Fucking.png",
                    "not GwenX.Panties or GwenX.PantiesDown", "images/GwenSex/Gwen_Sex_Pierce_Pussy_R.png",
                    "GwenX.Panties == 'lace panties' and not GwenX.PantiesDown", "images/GwenSex/Gwen_Sex_Pierce_Pussy_R_Lace.png",
#                    "GwenX.Panties == 'bikini bottoms' and not GwenX.PantiesDown", "images/GwenSex/Gwen_Sex_Pierce_Pussy_R_White.png",
                    "True", "images/GwenSex/Gwen_Sex_Pierce_Pussy_R_White.png",
                    ),
            #else, it's barbell
            "not GwenX.Panties or GwenX.PantiesDown", "images/GwenSex/Gwen_Sex_Pierce_Pussy_B.png",
            "GwenX.Panties == 'lace panties' and not GwenX.PantiesDown", "images/GwenSex/Gwen_Sex_Pierce_Pussy_B_Lace.png",
#            "GwenX.Panties == 'bikini bottoms' and not GwenX.PantiesDown", "images/GwenSex/Gwen_Sex_Pierce_Pussy_B_White.png",
            "True", "images/GwenSex/Gwen_Sex_Pierce_Pussy_B_White.png",
            ),
        (0,0), ConditionSwitch(
            #pantyhose layer
            "GwenX.Panties and GwenX.PantiesDown", Null(),
            "GwenX.Hose == 'tights'", Recolor("Gwen", "Hose", "images/GwenSex/Gwen_Sex_Hose_Tights.png"),
            "GwenX.Hose == 'ripped tights'", Recolor("Gwen", "Hose", "images/GwenSex/Gwen_Sex_Hose_Tights_Holed.png"),
            "GwenX.Hose == 'pantyhose'", Recolor("Gwen", "Hose", "images/GwenSex/Gwen_Sex_Hose_Pantyhose.png"),
            "GwenX.Hose == 'ripped pantyhose'", Recolor("Gwen", "Hose", "images/GwenSex/Gwen_Sex_Hose_Pantyhose_Holed.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Suit top over legs
            "GwenX.Over == 'suit' and not GwenX.Uptop", "images/GwenSex/Gwen_Sex_Over_Suit_Waist.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs Layer
            "GwenX.Legs == 'skirt' and GwenX.Upskirt", Recolor("Gwen", "Legs", "images/GwenSex/Gwen_Sex_Legs_Skirt_Up.png"),
            "GwenX.Legs == 'skirt'", Recolor("Gwen", "Legs", "images/GwenSex/Gwen_Sex_Legs_Skirt.png"),
            "GwenX.Legs == 'cheer skirt' and GwenX.Upskirt", Recolor("Gwen", "Legs", "images/GwenSex/Gwen_Sex_Legs_Cheer_Up.png"),
            "GwenX.Legs == 'cheer skirt'", Recolor("Gwen", "Legs", "images/GwenSex/Gwen_Sex_Legs_Cheer.png"),

            "GwenX.Upskirt", Null(),
#            "GwenX.Legs == 'skirt'", Recolor("Gwen", "Legs", "images/GwenSex/Gwen_Sex_Legs_Skirt.png"),
            "GwenX.Legs == 'shorts' and GwenX.Wet > 1", Recolor("Gwen", "Legs", "images/GwenSex/Gwen_Sex_Legs_Shorts_Wet.png"),
            "GwenX.Legs == 'shorts'", Recolor("Gwen", "Legs", "images/GwenSex/Gwen_Sex_Legs_Shorts.png"),
            "GwenX.Legs == 'suit' and GwenX.Wet > 1", "images/GwenSex/Gwen_Sex_Legs_Suit_Wet.png",
            "GwenX.Legs == 'suit'", "images/GwenSex/Gwen_Sex_Legs_Suit.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Piercings over pants and pantyhose
            "not GwenX.Pierce", Null(),
            "(GwenX.Legs == 'skirt' or GwenX.Legs == 'cheer skirt') and not GwenX.Upskirt", Null(),
            "GwenX.Pierce == 'ring'",ConditionSwitch(
                    #If she has panties down. . .
                    "GwenX.Legs == 'shorts' and not GwenX.Upskirt", "images/GwenSex/Gwen_Sex_Pierce_Pussy_R_Pink.png",
                    "GwenX.Legs == 'suit' and not GwenX.Upskirt", "images/GwenSex/Gwen_Sex_Pierce_Pussy_R_WhiteLine.png",
                    "GwenX.Panties and GwenX.PantiesDown", Null(),
                    "GwenX.Hose == 'tights'", "images/GwenSex/Gwen_Sex_Pierce_Pussy_R_Tights.png",
                    "True", Null(),
                    ),
            #else, it's barbell
            "GwenX.Legs == 'shorts' and not GwenX.Upskirt", "images/GwenSex/Gwen_Sex_Pierce_Pussy_B_Pink.png",
            "GwenX.Legs == 'suit' and not GwenX.Upskirt", "images/GwenSex/Gwen_Sex_Pierce_Pussy_B_WhiteLine.png",
            "GwenX.Legs == 'pants' and not GwenX.Upskirt", "images/GwenSex/Gwen_Sex_Pierce_Pussy_B_White.png",
            "GwenX.Panties and GwenX.PantiesDown", Null(),
            "GwenX.Hose == 'tights'", "images/GwenSex/Gwen_Sex_Pierce_Pussy_B_Tights.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer
#            "not Player.Sprite or Player.Cock != 'out'", Null(),
#            "Speed >= 2", "Gwen_Hotdog_Zero_Anim2",
#            "Speed", "Gwen_Hotdog_Zero_Anim1",
#            "True", "Gwen_Hotdog_Zero_Anim0",
#            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy'", "Gwen_Sex_Lick_Pussy",
            "Trigger == 'lick ass'", "Gwen_Sex_Lick_Ass",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy fondling animation
            "GwenX.Offhand == 'fondle pussy' and GwenX.Lust > 60 and not (Player.Sprite)",  At("GwenFingerHand", GirlFingerPussyX()), #"Gwen_Sex_Mast2",
            "GwenX.Offhand == 'fondle pussy'", At("GwenMastHand", GirlGropePussyX()), #"Gwen_Sex_Mast",
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Gwen_Sex_Fondle_Pussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Footjob overlay
            "Player.Cock == 'foot'", Null(),
            "renpy.showing('Anal_Plug_In_Sex') or renpy.showing('Anal_Plug_Out_Sex')",AlphaMask("Gwen_Sex_Feet", "images/GwenSex/Gwen_Sex_Feet_Mask.png"),
            "ShowFeet", "Gwen_Sex_Feet",
#            "Player.Sprite", AlphaMask("Gwen_Sex_Feet", "images/GwenSex/Gwen_Sex_Feet_Mask.png"),
#            "Trigger == 'lick pussy'", AlphaMask("Gwen_Sex_Feet", "images/GwenSex/Gwen_Sex_Feet_Mask.png"),
#            "Trigger == 'lick ass'", AlphaMask("Gwen_Sex_Feet", "images/GwenSex/Gwen_Sex_Feet_Mask.png"),
            "True", AlphaMask("Gwen_Sex_Feet", "images/GwenSex/Gwen_Sex_Feet_Mask.png"),
            ),

#        (0,0), ConditionSwitch(                                                                                 #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
#            "not Speed", "Gwen_Sex_Feet",
#            "Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Gwen_Sex_Feet", "images/GwenSex/Gwen_Sex_FeetMask.png"),
#            "True", "Gwen_Sex_Feet",
#            ),
        )
# End Gwen Sex Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen_Sex_Feet:
    LiveComposite(
        #the lower legs used in the sex pose, referenced by Gwen_Sex_Legs
        (1120,840),
#        (0,0), "images/GwenSex/[GwenX.skin_image.skin_path]Gwen_Sex_Feet.png",                                                         #Legs Base

        (0,0), ConditionSwitch(
            #hose layer
            "(GwenX.Hose == 'pantyhose' or GwenX.Hose == 'ripped pantyhose') and GwenX.Panties and GwenX.PantiesDown", "images/GwenSex/[GwenX.skin_image.skin_path]Gwen_Sex_Feet.png",
            "(GwenX.Hose == 'tights' or GwenX.Hose == 'ripped tights') and GwenX.Panties and GwenX.PantiesDown", "images/GwenSex/[GwenX.skin_image.skin_path]Gwen_Sex_Feet.png",
            "GwenX.Hose == 'socks'", Recolor("Gwen", "Hose", "images/GwenSex/Gwen_Sex_Feet_Socks.png"),
            "GwenX.Hose == 'ripped pantyhose'", Recolor("Gwen", "Hose", "images/GwenSex/Gwen_Sex_Feet_Holed.png"),
            "GwenX.Hose == 'ripped tights'", Recolor("Gwen", "Hose", "images/GwenSex/[GwenX.skin_image.skin_path]Gwen_Sex_Feet_Tights_Holed.png"),
            "GwenX.Hose == 'tights'", Recolor("Gwen", "Hose", "images/GwenSex/[GwenX.skin_image.skin_path]Gwen_Sex_Feet_Tights.png"),
#            "GwenX.Hose and GwenX.Hose != 'garterbelt' and GwenX.Hose != 'pantyhose'", Recolor("Gwen", "Hose", "images/GwenSex/Gwen_Sex_Feet_Hose.png"),
#            "GwenX.Hose == 'ripped pantyhose' and GwenX.Panties and GwenX.PantiesDown", "images/GwenSex/[GwenX.skin_image.skin_path]Gwen_Sex_Feet.png",
            "GwenX.Hose and GwenX.Hose != 'garterbelt'", Recolor("Gwen", "Hose", "images/GwenSex/Gwen_Sex_Feet_Hose.png"),
#            "GwenX.Hose == 'pantyhose'", Recolor("Gwen", "Hose", "images/GwenSex/Gwen_Sex_Feet_Hose.png"),
            "True", "images/GwenSex/[GwenX.skin_image.skin_path]Gwen_Sex_Feet.png",   #Null(),
            ),

        (0,0), ConditionSwitch(
            #Wet look
            "not GwenX.Water", Null(),
            "True", "images/GwenSex/Gwen_Sex_Water_Feet.png",
            ),
        (0,0), ConditionSwitch(
            #Boots
            "GwenX.Panties and GwenX.PantiesDown", Null(),
            "GwenX.Legs and GwenX.Legs != 'skirt' and GwenX.Upskirt", Null(),
            "GwenX.Boots == 'boots'", Recolor("Gwen", "Boots", "images/GwenSex/Gwen_Sex_Boots.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #panties if down
            "not GwenX.PantiesDown", Null(),
            "GwenX.Panties == 'lace panties'", Recolor("Gwen", "Panties", "images/GwenSex/Gwen_Sex_Panties_Lace_Down.png"),
            "GwenX.Panties == 'bikini bottoms'", Recolor("Gwen", "Panties", "images/GwenSex/Gwen_Sex_Panties_Bikini_Down.png"),
            "GwenX.Panties", Recolor("Gwen", "Panties", "images/GwenSex/Gwen_Sex_Panties_White_Down.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Legs Layer
            "GwenX.Upskirt",ConditionSwitch(
                    #If she has panties down. . .
                    "GwenX.Legs == 'shorts'", Recolor("Gwen", "Legs", "images/GwenSex/Gwen_Sex_Legs_Shorts_Down.png"),
                    "GwenX.Legs == 'suit'", "images/GwenSex/Gwen_Sex_Legs_Suit_Down.png",
                    "True", Null(),
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk
            "'feet' in GwenX.Spunk", "images/GwenSex/Gwen_Sex_Spunk_Feet.png",
            "True", Null(),
            ),
        )

# Start Gwen Sex Pose Pussy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Gwen_Sex_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).

    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/GwenSex/Gwen_Sex_Pussy_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and Speed", "Gwen_Sex_Heading_Pussy",
                "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/GwenSex/Gwen_Sex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/GwenSex/Gwen_Sex_Pussy_Open.png",
                "GwenX.Offhand == 'fondle pussy' and GwenX.Lust > 60", "images/GwenSex/Gwen_Sex_Pussy_Open.png",
                "True", "images/GwenSex/Gwen_Sex_Pussy_Closed.png",
                )
#    contains:
#            # The background plate of her pussy
#            ConditionSwitch(
#                "not GwenX.Wet", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/GwenSex/Gwen_Sex_WetPussy_F.png",
#                "True", "images/GwenSex/Gwen_Sex_WetPussy_C.png",
#                )
    contains:
            # pubes
            ConditionSwitch(
                "not GwenX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", Recolor("Gwen", "Pubes", "images/GwenSex/Gwen_Sex_Pubes_Fucking.png"),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 1", Recolor("Gwen", "Pubes", "images/GwenSex/Gwen_Sex_Pubes_Fucking.png"),
                "Player.Sprite and Player.Cock == 'in'", Recolor("Gwen", "Pubes", "images/GwenSex/Gwen_Sex_Pubes_Open.png"),
                "Player.Sprite and Player.Cock == 'out'", Recolor("Gwen", "Pubes", "images/GwenSex/Gwen_Sex_Pubes_Open.png"),
                "Trigger == 'lick pussy'", Recolor("Gwen", "Pubes", "images/GwenSex/Gwen_Sex_Pubes_Open.png"),
                "GwenX.Offhand == 'fondle pussy' and GwenX.Lust > 60", Recolor("Gwen", "Pubes", "images/GwenSex/Gwen_Sex_Pubes_Open.png"),
                "True", Recolor("Gwen", "Pubes", "images/GwenSex/Gwen_Sex_Pubes_Closed.png"),
                )
    contains:
            #Spunk
            ConditionSwitch(
                "'in' not in GwenX.Spunk or not Player.Male", Null(),
                "(GwenX.Legs == 'pants' or GwenX.Legs == 'shorts') and not GwenX.Upskirt", Null(),
                "GwenX.Panties and not GwenX.PantiesDown", Null(),
                "True", AlphaMask("Spunk_Drip2","Gwen_Sex_Drip_Mask"),
                )
            offset (545,540)

    contains:
            ConditionSwitch(
                #Outside Spunk
                "'in' in GwenX.Spunk and Player.Sprite and Player.Cock == 'in' and Speed and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_PussyF.png",
                "'in' in GwenX.Spunk and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Pussy.png",
                "True", Null(),
                )
#    contains:
#            #Spunk under penis
#            ConditionSwitch(
#                "'in' in GwenX.Spunk", "images/GwenSex/Gwen_Sex_Spunk_Puss_Under.png",
#                "True", Null(),
#                )
#    contains:
#            #hose layer
#            ConditionSwitch(
#                "GwenX.Panties and GwenX.PantiesDown", Null(),
#                "GwenX.Hose == 'ripped pantyhose' and ShowFeet", Recolor("Gwen", "Hose", "images/GwenSex/Gwen_Sex_Hose_Pantyhose_Holed.png"),
#                "GwenX.Hose == 'ripped pantyhose'", Recolor("Gwen", "Hose", "images/GwenSex/Gwen_Sex_Hose_Pantyhose_Holed.png"),
#                "True", Null(),
#                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            ConditionSwitch(
#                "not Player.Sprite", Null(),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 3", AlphaMask("Gwen_Sex_Fucking_Zero_Anim3", "Gwen_Sex_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", AlphaMask("Gwen_Sex_Fucking_Zero_Anim2", "Gwen_Sex_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and Speed == 1", AlphaMask("Gwen_Sex_Fucking_Zero_Anim1", "Gwen_Sex_Heading_Mask"),
                "Player.Sprite and Player.Cock == 'in'", "Gwen_Sex_Fucking_Zero_Anim0",
                "True", Null(),
                )
#    contains:
#            #Piercings
#            ConditionSwitch(
#                "GwenX.Pierce == 'barbell' and Player.Sprite and Player.Cock == 'in' and Speed", "images/GwenSex/Gwen_Sex_Pierce_Pussy_BarbellF.png",
#                "GwenX.Pierce == 'ring' and Player.Sprite and Player.Cock == 'in' and Speed", "images/GwenSex/Gwen_Sex_Pierce_Pussy_RingF.png",
#                "GwenX.Pierce == 'barbell'", "images/GwenSex/Gwen_Sex_Pierce_Pussy_Barbell.png",
#                "GwenX.Pierce == 'ring'", "images/GwenSex/Gwen_Sex_Pierce_Pussy_Ring.png",
#                "True", Null(),
#                )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and Speed == 1", "Gwen_Pussy_Spunk_Heading",
                "True", Null(),
                )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "Speed == 1", Null(),
                "'in' not in GwenX.Spunk or not Player.Sprite or Player.Cock != 'in' or not Speed or not Player.Male", Null(),
#                "Speed <= 1", Null(), #"Gwen_Pussy_Spunk_Heading",
                "True", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
                )

    #End Gwen Pussy composite

image Gwen_Sex_Drip_Mask:
    #This is the mask for her drip pattern
    contains:
        "images/JubesSex/Jubes_Sex_Mask_Anal.png"
        offset (-545,-450)#(-275,-560)#(-145,-560)#(-225,-560)

image Gwen_Sex_Lick_Pussy:
        "Lick_Anim"
        zoom 0.7
        offset (535,500)#(505,680)

image Gwen_Sex_Lick_Ass:
        "Lick_Anim"
        zoom 0.7
        offset (535,580)#(535,550)

image Gwen_Sex_Fondle_Pussy:
        "GropePussy_Gwen"
        xzoom -1.5
        yzoom 1.5
        offset(-710,-300) #(-890,-300)
#        block:
#            ease 1 offset(-1000,0) #(535,500)
#            ease 1 offset(-1000,-1000) #(535,500)
#            ease 1 offset(0,-1000) #(535,500)
#            ease 1 offset(0,0) #(535,500)
#            repeat

#End Animations for Gwen's Pussy during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen_Sex_Zero_Cock:
        #this is the cock generally used by Gwen's sex pose
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

image Gwen_Sex_Fucking_Mask:
        #This is the mask image for Kitty's wide open pussy
        # Used in "Gwen_Sex_Speed2" and "Gwen_Sex_Speed3"
        contains:
            "images/JubesSex/Jubes_Sex_Mask_Fucking.png"
            yoffset 3

# Start Gwen Sex Pose Static / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen_Sex_Static:
    # Pose for Gwen's Sex Pose in which she is static
    contains:
            #Gwen's underlying body
            subpixel True
            "Gwen_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
#                pause 0.3
                ease 1.5 ypos -185 #-120
                pause .3
                ease 1.45 ypos -180 #-130
                pause 0.25
                repeat
    contains:
            #Gwen's Legs
            subpixel True
            "Gwen_Sex_Legs"
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
            "Gwen_Sex_Zero_Cock"
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
            #Gwen's Feet
            subpixel True
#            "Gwen_Sex_Feet"
            ConditionSwitch(
                #Footjob overlay
                "ShowFeet", AlphaMask("Gwen_Sex_Feet", "images/GwenSex/Gwen_Sex_Feet_Mask.png"),
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

# End Gwen Sex Pose Speed Static / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Gwen Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Gwen Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen_Sex_Fucking_Speed0:
    # Pose for Gwen's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Gwen's underlying body
            subpixel True
            "Gwen_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                ease 2 ypos -160 #0
                pause 0.8
                ease 2 ypos -180 #-130
                pause 0.2
                repeat
    contains:
            #Gwen's Legs
            subpixel True
            "Gwen_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -160 #0
                pause 0.8
                ease 2 ypos -180 #-130
                repeat
# End main animation for Sex Pose Fucking Speed 1


image Gwen_Sex_Fucking_Zero_Anim0:
        #this is Gwen's sex animation, Speed 1 Fucking
        contains:
            subpixel True
            "Gwen_Sex_Zero_Cock"
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

# End Gwen Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Gwen Sex Pose Speed 1 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen_Sex_Fucking_Speed1:
    # Pose for Gwen's Sex Pose in which she is fucking at speed 1 (heading)
    contains:
            #Gwen's underlying body
            subpixel True
            "Gwen_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause 1
                ease 1.5 ypos -190 #0
                pause 1.6
                ease 0.9 ypos -180 #-130
                repeat
    contains:
            #Gwen's Legs
            subpixel True
            "Gwen_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause 0.7
                ease 1.5 ypos -200 #0
                pause 1.6
                ease 1.2 ypos -180 #-130
                repeat
# End main animation for Sex Pose Fucking Speed 1


image Gwen_Sex_Fucking_Zero_Anim1:
        #this is Gwen's sex animation, Speed 1 Fucking
        contains:
            subpixel True
            "Gwen_Sex_Zero_Cock"
            subpixel True
            pos (0,40)#(498,530)
            block:
                pause 0.2
#                ease 0.95 ypos -145
                ease 2 ypos -10#-10 #-140
                pause .8
                ease 2 ypos 40 #-10
                repeat

image Gwen_Sex_Heading_Mask:
        #This is the mask image for Gwen's heading pussy
        contains:
            "images/JubesSex/Jubes_Sex_Mask_Fucking.png"
            yoffset 10
            block:
                pause 0.2
                ease 2 yoffset 3
                pause 0.8
                ease 2 yoffset 10
                repeat


image Gwen_Sex_Heading_Pussy:
        #This is the image for Gwen's heading pussy growing
#        contains:
#            "images/GwenSex/Gwen_Sex_Pussy_Fucking_Base.png"
        contains:
            "images/GwenSex/Gwen_Sex_Pussy_Fucking.png"
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
#    "images/GwenDoggy/Gwen_Doggy_Pussy_HHole.png"
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

image Gwen_Pussy_Spunk_Heading:
        #This is the image for Gwen's heading pussy cum
        contains:
            ConditionSwitch(
                "'in' in GwenX.Spunk and Player.Sprite and Player.Cock == 'in' and Speed == 1 and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
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

# End Gwen Sex Pose Speed 1 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Gwen Sex Pose Speed 2 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen_Sex_Fucking_Speed2:
    # Pose for Gwen's Sex Pose in which she is fucking at speed 2
    contains:
            #Gwen's underlying body
            subpixel True
            "Gwen_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 4.2
                pause 0.6
                ease .9 ypos -190 # 0
                pause 0.8
                ease 2.0 ypos -180 # -130
                repeat
    contains:
            #Gwen's Legs
            subpixel True
            "Gwen_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 4.2
                pause 0.4
                ease 0.95 ypos -205 # 5
                ease 0.45 ypos -200 # 0
                pause 0.6
                ease 1.8 ypos -180 # -130
                repeat
# End main animation for Sex Pose Fucking Speed 2


image Gwen_Sex_Fucking_Zero_Anim2:
        #this is Gwen's sex animation, Speed 2 Fucking
        contains:
            subpixel True
            "Gwen_Sex_Zero_Cock"
            subpixel True
            pos (0,20)#(498,530)
            block:
                pause 0.2
                ease 0.95 ypos -100 # -145
                ease 0.25 ypos -90 # -140
                pause .8
                ease 2 ypos 20 #-10
                repeat

# End Gwen Sex Pose Speed 2 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Gwen Sex Pose Speed 3 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen_Sex_Fucking_Speed3:
    # Pose for Gwen's Sex Pose in which she is fucking at speed 3
    contains:
            #Gwen's underlying body
            subpixel True
            "Gwen_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.6
                ease 0.4 ypos -200
#                pause 0.35
                ease 0.8 ypos -180
                repeat
    contains:
            #Gwen's Legs
            subpixel True
            "Gwen_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.4
                ease 0.45 ypos -220
                ease 0.15 ypos -210
#                pause 0.35
                ease 0.8 ypos -180
                repeat


# End main animation for Sex Pose Fucking Speed 3


image Gwen_Sex_Fucking_Zero_Anim3:
        #this is Gwen's sex animation, Speed3 Fucking
        contains:
            subpixel True
            "Gwen_Sex_Zero_Cock"
            subpixel True
            pos (0,10)
            block:
                pause 0.1
                ease 0.55 ypos -100
                ease 0.15 ypos -90
                pause 0.25
                ease 0.75 ypos 10
                repeat

# End Gwen Sex Pose Speed 3 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Animations for Gwen's Ass during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Gwen's Ass during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen_Sex_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/JubesSex/Jubes_Sex_Anal.png",
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/JubesSex/Jubes_Sex_Anal.png",
            "Player.Sprite and Player.Cock == 'anal' and Speed", "Gwen_Sex_Anal_Heading",
            "Player.Sprite and Player.Cock == 'anal'", "Gwen_Sex_Anal_Tip",
            "GwenX.Plug", "images/PlugBase_Sex.png",
            "GwenX.Loose > 2", "Gwen_Gape_Anal_Sex",
#            "GwenX.Loose", "images/GwenSex/Gwen_Sex_Hole_Loose.png",
            "True", Null(),
            )
    contains:
            #Spunk under penis
            ConditionSwitch(
                "'anal' not in GwenX.Spunk or not Player.Male", Null(),
#                "Player.Sprite and Player.Cock != 'anal' and Speed >= 1", "images/GwenSex/Gwen_Sex_Spunk_Anal_Under.png",
                "Player.Sprite and Player.Cock != 'anal' and Speed == 1", "Gwen_Sex_Anal_Spunk_Heading_Under",
                "True", "images/JubesSex/Jubes_Sex_Spunk_Anal.png",
                )
    contains:
            # The animation of Zero's moving penis, masked by her anus shape
            ConditionSwitch(
                "not Player.Sprite or Player.Cock != 'anal'", Null(),
                "Speed >= 3",  AlphaMask("Gwen_Sex_Anal_Zero_Anim3", "Gwen_Sex_Anal_MaskF"),
                "Speed >= 2", AlphaMask("Gwen_Sex_Anal_Zero_Anim2", "Gwen_Sex_Anal_MaskF"),
                "Speed", AlphaMask("Gwen_Sex_Anal_Zero_Anim1", "Gwen_Sex_Anal_Mask"),
                "True", AlphaMask("Gwen_Sex_Anal_Zero_Anim0", "Gwen_Sex_Anal_Mask"),
                )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "'anal' not in GwenX.Spunk or not Player.Sprite or Player.Cock != 'anal' or not Speed or not Player.Male", Null(),
                "Speed == 1", "Gwen_Sex_Anal_Spunk_Heading_Over",
                "True", "Gwen_Sex_Anal_Spunk",
                )


image Gwen_Gape_Anal_Sex:
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

image Gwen_Sex_Anal_Spunk:
    ConditionSwitch(
                "'anal' in GwenX.Spunk and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Anal_Over.png",
                "True", Null(),
                )
    anchor (0.5,0.5)
    pos (0.5,0.5)
#    xoffset 20
    yoffset -23#68
    xzoom .9#1.2

image Gwen_Sex_Anal_Mask:
        #This is the mask image for small stuff
        # Used in "Gwen_Sex_Speed2" and "Gwen_Sex_Speed3"
        contains:
            "images/JubesSex/Jubes_Sex_Mask_Anal.png"
            yoffset 98 #-9
            xoffset 3 #3
#            xoffset -5

image Gwen_Sex_Anal_MaskF:
        #This is the mask image for deep stuff
        # Used in "Gwen_Sex_Speed2" and "Gwen_Sex_Speed3"
        contains:
            "images/JubesSex/Jubes_Sex_Mask_AnalB.png"
            yoffset 98 #-9
            xoffset 3



# Start Gwen Sex Pose Speed 0 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen_Sex_Anal_Speed0:
    # Pose for Gwen's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Gwen's underlying body
            subpixel True
            "Gwen_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.5
                ease 1 ypos -185 #40
                pause 1.0
                ease 1.5 ypos -180 #90
                repeat
    contains:
            #Gwen's Legs
            subpixel True
            "Gwen_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.2
                ease 1 ypos -190 #40
                pause 1.3
                ease 1.5 ypos -180 #90
                repeat

# End main animation for Sex Pose Anal Speed 1


image Gwen_Sex_Anal_Zero_Anim0:
        #this is Gwen's sex animation, Speed 0 Anal
        contains:
            subpixel True
            "Gwen_Sex_Zero_Cock"
#            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            subpixel True
            pos (3,135)#(498,530)
            block:
                pause 0.2
                ease 2 ypos 130 #90
                pause .8
                ease 2 ypos  135 #130
                repeat

image Gwen_Sex_Anal_Tip:
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

# End Gwen Sex Pose Speed 0 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Gwen Sex Pose Speed 1 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen_Sex_Anal_Heading:
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

image Gwen_Sex_Anal_Spunk_Heading_Over:
    ConditionSwitch(
                "'anal' in GwenX.Spunk and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_Anal_Over.png",
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

image Gwen_Sex_Anal_Spunk_Heading_Under:
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

image Gwen_Sex_Anal_Speed1:
    # Pose for Gwen's Sex Pose in which she is fucking at speed 1 (heading)
    contains:
            #Gwen's underlying body
            subpixel True
            "Gwen_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.5
                ease 1 ypos -185 #40
                pause 1.0
                ease 1.5 ypos -180 #90
                repeat
    contains:
            #Gwen's Legs
            subpixel True
            "Gwen_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 1.2
                ease 1 ypos -190 #40
                pause 1.3
                ease 1.5 ypos -180 #90
                repeat

# End main animation for Sex Pose Anal Speed 1


image Gwen_Sex_Anal_Zero_Anim1:
        #this is Gwen's sex animation, Speed 1 Anal
        contains:
            subpixel True
            "Gwen_Sex_Zero_Cock"
#            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            subpixel True
            pos (3,130)#(498,530)
            block:
                pause 0.2
                ease 2 ypos 90 #40
                pause .8
                ease 2 ypos  130 #90
                repeat

# End Gwen Sex Pose Speed 1 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Gwen Sex Pose Speed 2 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen_Sex_Anal_Speed2:
    # Pose for Gwen's Sex Pose in which she is doing anal at speed 2
    contains:
            #Gwen's underlying body
            subpixel True
            "Gwen_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.6
                ease 1.0 ypos -200
                pause .9
                ease 1.7 ypos -180
                repeat
    contains:
            #Gwen's Legs
            subpixel True
            "Gwen_Sex_Legs"
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
#            AlphaMask("Gwen_Sex_Fucking_Zero_Anim2", "Gwen_Sex_Fucking_Mask")
# End main animation for Sex Pose Fucking Speed 2


image Gwen_Sex_Anal_Zero_Anim2:
        #this is Gwen's sex animation, Speed 2 Fucking
        contains:
            subpixel True
            "Gwen_Sex_Zero_Cock"
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

# End Gwen Sex Pose Speed 2 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Gwen Sex Pose Speed 3 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen_Sex_Anal_Speed3:
    # Pose for Gwen's Sex Pose in which she is Anal at speed 3
    contains:
            #Gwen's underlying body
            subpixel True
            "Gwen_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 1.8
#                pause 0.5
                easein .5 ypos -180
                ease .4 ypos -200
                pause .4
                ease .5 ypos -185
                repeat

    contains:
            #Gwen's Legs
            subpixel True
            "Gwen_Sex_Legs"
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


image Gwen_Sex_Anal_Zero_Anim3:
        #this is Gwen's sex animation, Speed3 Anal
        contains:
            subpixel True
            "Gwen_Sex_Zero_Cock"
            subpixel True
            pos (3,-40)
            block:
                pause 0.1
                ease 0.55 ypos -25
                ease 0.15 ypos -20
                pause 0.25
                ease 0.75 ypos 90
                repeat

# End Gwen Sex Pose Speed 3 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Gwen Sex Pose Speed 1 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen_Sex_Hotdog_Speed1:
    # Pose for Gwen's Sex Pose in which she is hotdogging at speed 1 (slow)
    contains:
            #Gwen's underlying body
            subpixel True
            "Gwen_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.8
                ease 0.8 ypos -190 #-120
                pause .5
                ease 1.0 ypos -180 #-130
                pause 0.4
                repeat
    contains:
            #Gwen's Legs
            subpixel True
            "Gwen_Sex_Legs"
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
            "Gwen_Sex_Zero_Cock"
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
            #Gwen's Feet
            subpixel True
            ConditionSwitch(
                #Footjob overlay
                "ShowFeet","Gwen_Sex_Feet",
                "True", Null(),
                )
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

# End Gwen Sex Pose Speed 1 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Gwen Sex Pose Speed 2 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen_Sex_Hotdog_Speed2:
    # Pose for Gwen's Sex Pose in which she is hotdogging at speed 2 (fast)
    contains:
            #Gwen's underlying body
            subpixel True
            "Gwen_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block:
                pause 0.25
                ease 0.45 ypos -195 #-120
                pause .1
                ease 0.8 ypos -180 #-130
#                pause 0.2
                repeat
    contains:
            #Gwen's Legs
            subpixel True
            "Gwen_Sex_Legs"
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
            "Gwen_Sex_Zero_Cock"
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
            #Gwen's Feet
            subpixel True
            ConditionSwitch(
                #Footjob overlay
                "ShowFeet","Gwen_Sex_Feet",
                "True", Null(),
                )
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

# End Gwen Sex Pose Speed 2 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Gwen Sex Pose Speed 0 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen_Sex_FJ_Speed0:
    # Pose for Gwen's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Gwen's underlying body
            subpixel True
            "Gwen_Sex_Body"
            pos (50,-180) #X less is left, Y less is up
            block: #adds to 5
                ease 2 ypos -185#-40 #-140
                pause 0.8
                ease 2 ypos -180#-60 #-180
                pause 0.2
                repeat
    contains:
            #Gwen's Legs
            subpixel True
            "Gwen_Sex_Legs"
            pos (50,-220) #X less is left, Y less is up (80,0)
            block: #adds to 5
                pause 0.2
                ease 2 ypos -230 #10
                pause 0.8
                ease 2 ypos -220 #0
                repeat
    contains:
            subpixel True
#            "Gwen_Sex_Zero_Cock"
            "Zero_Blowcock"
            zoom .5
            subpixel True
            pos (630,520) #(0,-380)
    contains:
            #Gwen's Legs
            subpixel True
            "Gwen_Sex_Feet"
#            alpha 0.5
#            AlphaMask("Gwen_Sex_Feet", "images/GwenSex/Gwen_Sex_Feet_Mask.png")
            pos (50,-270) #X less is left, Y less is up (80,0)
            block: #adds to 5
#                pause 0.2
                ease 2 ypos -290 #10
                pause 0.8
                ease 2 ypos -270 #0
                pause 0.2
                repeat

# End main animation for Sex Pose Footjob Speed 0

# End Gwen Sex Pose Speed 0 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Gwen Sex Pose Speed 1 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen_Sex_FJ_Speed1:
    # Pose for Gwen's Sex Pose in which she is fucking at speed 1 (slow)
    contains:
            #Gwen's underlying body
            subpixel True
            "Gwen_Sex_Body"
            pos (50,-190) #X less is left, Y less is up
            block: #adds to 5
                ease 2 ypos -120 #-140
                pause 0.8
                ease 2 ypos -190 #-180
                pause 0.2
                repeat
    contains:
            #Gwen's Legs
            subpixel True
            "Gwen_Sex_Legs"
            pos (50,-230) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -140 #40
                pause 0.8
                ease 2 ypos -230 #-100
                repeat
#    contains:
#            subpixel True
#            "Gwen_Sex_Zero_Cock"
#            subpixel True
#            pos (0,-360)
#            block:
#                pause 1.5
#                ease 0.7 ypos -340 #-120
#                pause 1
#                ease 1 ypos -360 #-140
#                pause 0.8
#                repeat
    contains:
            subpixel True
#            "Gwen_Sex_Zero_Cock"
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
    contains:
            #Gwen's Legs
            subpixel True
            "Gwen_Sex_Feet"
#            alpha 0.5
#            AlphaMask("Gwen_Sex_Feet", "images/GwenSex/Gwen_Sex_Toes.png")
#            ConditionSwitch(
#                #Footjob overlay
#                "ShowFeet", AlphaMask("Gwen_Sex_Feet", "images/GwenSex/Gwen_Sex_Toes.png"),
#                "True", Null(),
#                )
            pos (50,-260) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -140 #40
                pause 0.8
                ease 2 ypos -280 #-100
                repeat

# End main animation for Sex Pose Footjob Speed 1

# End Gwen Sex Pose Speed 1 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Gwen Sex Pose Speed 2 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen_Sex_FJ_Speed2:
    # Pose for Gwen's Sex Pose in which she is fucking at speed 2 (fast)
    contains:
            #Gwen's underlying body
            subpixel True
            "Gwen_Sex_Body"
            pos (50,-220) #X less is left, Y less is up
            block: #adds to 2.1
                ease 0.8 ypos -160 #-140
                pause 0.1
                ease 0.9 ypos -220 #-180
                pause 0.1
                repeat
    contains:
            #Gwen's Legs
            subpixel True
            "Gwen_Sex_Legs"
            pos (50,-230) #X less is left, Y less is up
            block: #adds to 5
                pause 0.1
                ease 0.8 ypos -160 #0
                pause 0.1 #0.4
                ease 0.9 ypos -230 #-130
                repeat
    contains:
            subpixel True
            "Zero_Blowcock"
            zoom .5
            subpixel True
            pos (630,520) #(0,-380)
            block: #adds to 5
                pause 0.5
                ease 0.4 ypos 540 #40
                pause 0.1
                ease .4 ypos 520 #-100
                pause .5
                repeat
    contains:
            #Gwen's Legs
            subpixel True
            "Gwen_Sex_Feet"
#            AlphaMask("Gwen_Sex_Feet", "images/GwenSex/Gwen_Sex_Toes.png")
#            ConditionSwitch(
#                #Footjob overlay
#                "ShowFeet", AlphaMask("Gwen_Sex_Feet", "images/GwenSex/Gwen_Sex_Toes.png"),
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

# End Gwen Sex Pose Speed 2 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     Sex Launch/Reset
label Gwen_Sex_Launch(Line = Trigger):
    $ GwenX.Offhand = 0 if GwenX.Offhand == "hand" else GwenX.Offhand

##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    $ GwenX.Pose = "sex"
##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary

    $ Line = "solo" if not Line else Line
    if Line == "sex":
        $ Player.Sprite = 1
        $ Player.Cock = "in"
        call Cock_Occupied(GwenX,"pussy")
        if Trigger2 in ("fondle pussy","dildo pussy","lick pussy"):
                $ Trigger2 = 0
    elif Line == "anal":
        $ Player.Sprite = 1
        $ Player.Cock = "anal"
        call Cock_Occupied(GwenX,"anal")
        if Trigger2 in ("insert ass","dildo anal","lick ass"):
                $ Trigger2 = 0
    elif Line == "hotdog":
        $ Player.Sprite = 1
        if GwenX.PantsNum() == 5: #upskirts her if she's in a skirt
                $ GwenX.Upskirt = 1
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
        call Zero_Strapped(GwenX) #puts strap-on on.
    $ Trigger = Line

    if GwenX.Pose == "doggy":
            call Gwen_Doggy_Launch(Line)
            return
    if renpy.showing("Gwen_SexSprite"):
        return
    $ Speed = 0
    call Girl_Hide(GwenX,1)
    show Gwen_SexSprite zorder 150
    with dissolve
    return

label Gwen_Sex_Reset:
    if renpy.showing("Gwen_Doggy_Animation"):
        call Gwen_Doggy_Reset
        return
    if not renpy.showing("Gwen_SexSprite"):
        return
    $ GwenX.ArmPose = 2
    hide Gwen_SexSprite
    call Girl_Hide(GwenX)
#    call Set_The_Scene(Dress = 0)
    show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) zorder GwenX.Layer:
        alpha 1 zoom 1 offset (0,0) anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return


# End Gwen Sex Pose Content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


## End Gwen Sex Pose Content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Gwen's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





## Gwen's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Gwen_BJ_Animation:#BJ_NewTest:                                                                #core BJ animation
    LiveComposite(
        (800,950),
        (0,0), ConditionSwitch( #-270,-160
            # Gwen's hair backside
            "Speed == 0", "Gwen_BJ_Anim0",               #Static
            "Speed == 1", "Gwen_BJ_Anim1",               #Licking

#            "True", "Gwen_BJ_Anim2",               #Heading

            "Speed == 2", "Gwen_BJ_Anim2",               #Heading
            "Speed == 3", "Gwen_BJ_Anim3",               #Sucking
            "Speed == 4", "Gwen_BJ_Anim4",               #Deepthroat
            "Speed == 5", "Gwen_BJ_Anim5",               #Cumming High
            "Speed == 6", "Gwen_BJ_Anim6",               #Cumming Deep
            "True", Null(),
            ),
        )
#    zoom 1
#    anchor (.5,.5)
    zoom .8 #.7
    transform_anchor True
    anchor (.5,.5)
    offset (-95,85) #(-90,100)


image Gwen_BJ_Backdrop:
    LiveComposite(
        (800,950),       #550,950
#        (-10,-90), "Gwen_BJ_HairBack", #(75,-10)
        (0,0), "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_BJ_Body.png",

#        (0,0), ConditionSwitch(
#            #Water effect
#            "GwenX.Water and GwenX.ArmPose == 1", "images/GwenSprite/Gwen_Sprite_Water1.png",
#            "GwenX.Water", "images/GwenSprite/Gwen_Sprite_Water2.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Chest layer under tits
            "GwenX.Over == 'tshirt'", Null(),
            "GwenX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "GwenX.Chest == 'lace bra'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_BJ_Chest_Lace_Up.png"),
                    "GwenX.Chest == 'bra'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_BJ_Chest_Bra_Up.png"),
                    "GwenX.Chest == 'tank'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_BJ_Chest_Tank_Up.png"),
                    "GwenX.Chest == 'bikini top'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_BJ_Chest_Bikini_Up.png"),
                    "True", Null(),
                    ),
            "GwenX.Chest == 'lace bra'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_BJ_Chest_Lace.png"),
            "GwenX.Chest == 'bra'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_BJ_Chest_Bra.png"),
            "GwenX.Chest == 'tank'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_BJ_Chest_Tank.png"),
            "GwenX.Chest == 'bikini top'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_BJ_Chest_Bikini.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over body layer
            "GwenX.Over == 'open suit'", "images/GwenBJFace/Gwen_BJ_Over_Suit_Open.png",
            "GwenX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "GwenX.Over == 'suit'", "images/GwenBJFace/Gwen_BJ_Over_Suit_Open.png",
                    "GwenX.Over == 'tshirt'", Recolor("Gwen", "Over", "images/GwenBJFace/Gwen_BJ_Over_Tshirt_Up.png"),
                    "GwenX.Over == 'cheer top'", Recolor("Gwen", "Over", "images/GwenBJFace/Gwen_BJ_Over_Cheer_Up.png"),
                    "True", Null(),
                    ),
            "GwenX.Over == 'suit'", "images/GwenBJFace/Gwen_BJ_Over_Suit.png",
            "GwenX.Over == 'tshirt'", Recolor("Gwen", "Over", "images/GwenBJFace/Gwen_BJ_Over_Tshirt.png"),
            "GwenX.Over == 'cheer top'", Recolor("Gwen", "Over", "images/GwenBJFace/Gwen_BJ_Over_Cheer.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Piercings layer
            "not GwenX.Pierce", Null(),
            "GwenX.Pierce == 'ring'", ConditionSwitch(
                    #if it's the ring pericings
                    "GwenX.Uptop", "images/GwenBJFace/Gwen_TJ_Pierce_Ring.png",
                    "GwenX.Over == 'suit'", "images/GwenBJFace/Gwen_TJ_Pierce_Ring_Pink.png",
                    "GwenX.Over == 'tshirt' or GwenX.Over == 'cheer top'", "images/GwenBJFace/Gwen_TJ_Pierce_Ring_White.png",
                    "GwenX.Chest == 'lace bra'", "images/GwenBJFace/Gwen_TJ_Pierce_Ring_Lace.png",
                    "GwenX.Chest == 'bra'", "images/GwenBJFace/Gwen_TJ_Pierce_Ring_White.png",
                    "GwenX.Chest == 'bikini top'", "images/GwenBJFace/Gwen_TJ_Pierce_Ring_Pink.png",
                    "GwenX.Chest == 'tank'", "images/GwenBJFace/Gwen_TJ_Pierce_Ring_White.png",
                    "True", "images/GwenBJFace/Gwen_TJ_Pierce_Ring.png",
                    ),
            "GwenX.Uptop", "images/GwenBJFace/Gwen_TJ_Pierce_Barbell.png",
            "GwenX.Over == 'suit'", "images/GwenBJFace/Gwen_TJ_Pierce_Barbell_Pink.png",
            "GwenX.Over == 'tshirt' or GwenX.Over == 'cheer top'", "images/GwenBJFace/Gwen_TJ_Pierce_Barbell_White.png",
            "GwenX.Chest == 'lace bra'", "images/GwenBJFace/Gwen_TJ_Pierce_Barbell_Lace.png",
            "GwenX.Chest == 'bra'", "images/GwenBJFace/Gwen_TJ_Pierce_Barbell_White.png",
            "GwenX.Chest == 'bikini top'", "images/GwenBJFace/Gwen_TJ_Pierce_Barbell_Pink.png",
            "GwenX.Chest == 'tank'", "images/GwenBJFace/Gwen_TJ_Pierce_Barbell_White.png",
            "True", "images/GwenBJFace/Gwen_TJ_Pierce_Barbell.png",
            ),
        (0,0), ConditionSwitch(
            # spunk over tits
            "'tits' not in GwenX.Spunk", Null(),
            "GwenX.Over == 'tshirt'", "images/GwenBJFace/Gwen_TJ_Spunk_Clothed.png",
            "not GwenX.Uptop and GwenX.Over", "images/GwenBJFace/Gwen_TJ_Spunk_Clothed.png",
            "True", "images/GwenBJFace/Gwen_TJ_Spunk_Over.png",
            ),
#        (0,0), "images/GwenBJFace/Gwen_TJ_RefLine.png",
#        (-10,-90), "Gwen_Sprite_Head", #(75,-10)
        )
    transform_anchor True
    anchor (0.45, 0.35)#(0.6, 1.0)
    xoffset 50#30
    yoffset -530#-530
#    zoom .75  #.76
    rotate 0
# image Gwen_BJ_Backdrop # image Gwen_BJ_Backdrop # image Gwen_BJ_Backdrop End # image Gwen_BJ_Backdrop # image Gwen_BJ_Backdrop End

# image Gwen_BJ_Backdrop # image Gwen_BJ_Backdrop # image Gwen_BJ_Backdrop End # image Gwen_BJ_Backdrop # image Gwen_BJ_Backdrop End



image Gwen_BJ_Head:                                                                            #These are all the details of the face
    LiveComposite(
        (695,695),
        (-90,480), ConditionSwitch(
            "renpy.showing('Gwen_BJ_Animation') and Speed > 1",Null(),
#            "renpy.showing('Gwen_BJ_Animation') and (Speed == 3 or Speed == 4 or Speed == 6)",Null(),
            "True", "Gwen_BJ_Head_Under"
            ),

        (0,0), ConditionSwitch(
            # Basic Face layer
            "GwenX.Blush == 2 and renpy.showing('Gwen_BJ_Animation') and (Speed == 3 or Speed == 4 or Speed == 6)","images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_BJ_Head_Sucking_Over_Blush2.png",
            "GwenX.Blush and renpy.showing('Gwen_BJ_Animation') and (Speed == 3 or Speed == 4 or Speed == 6)","images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_BJ_Head_Sucking_Over_Blush.png",
            "renpy.showing('Gwen_BJ_Animation') and (Speed == 3 or Speed == 4 or Speed == 6)","images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_BJ_Head_Sucking_Over.png",
#            "True","images/GwenBJFace/Gwen_BJ_Head_Sucking_Overlay.png",

            "GwenX.Blush == 2", "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_BJ_Head_Sucking_Over_Blush2.png",
            "GwenX.Blush", "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_BJ_Head_Sucking_Over_Blush.png",
            "True", "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_BJ_Head_Sucking_Over.png"

#            "GwenX.Blush == 2", "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_BJ_Head_Blush2.png",
#            "GwenX.Blush", "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_BJ_Head_Blush.png",
#            "True", "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_BJ_Head.png"
            ),

        (3,3), ConditionSwitch(
            #Mouth overlay
            "Speed > 1 and renpy.showing('Gwen_BJ_Animation')", "images/GwenBJFace/Gwen_BJ_Mouth_Over.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Mouth spunk
#            "True", Null(), #cumming
            "'mouth' not in GwenX.Spunk or not Player.Male", Null(),
            "Speed > 1 and renpy.showing('Gwen_BJ_Animation')", "images/GwenBJFace/Gwen_BJ_Spunk_Heading.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # Mask
            "not GwenX.Hat", Null(),
            "GwenX.Brows == 'angry' and GwenX.Blush", Recolor("Gwen", "Hat", "images/GwenBJFace/Gwen_BJ_Mask_Angry_Blush.png"),
            "GwenX.Brows == 'angry'", "images/GwenBJFace/Gwen_BJ_Mask_angry.png",
            "GwenX.Blush", Recolor("Gwen", "Hat", "images/GwenBJFace/Gwen_BJ_Mask_Blush.png"),
            "True", Recolor("Gwen", "Hat", "images/GwenBJFace/Gwen_BJ_Mask.png")
            ),
        (0,0), ConditionSwitch(
            #wet face
            "Player.Male", Null(),
            "'mouth' not in GwenX.Spunk and 'chin' not in GwenX.Spunk", Null(),
#            "'chin' not in GwenX.Spunk and (GwenX.Mouth == 'tongue' or Speed)", "images/GwenBJFace/Gwen_BJ_Wet_Tongue.png",
#            "GwenX.Mouth == 'tongue' or Speed", "images/GwenBJFace/Gwen_BJ_Wet_Tongue2.png",
            "'mouth' in GwenX.Spunk or 'chin' in GwenX.Spunk", "images/GwenBJFace/Gwen_BJ_Wet_Mouth.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Brows
            "GwenX.Hat and GwenX.Brows == 'angry'", Null(),
            "GwenX.Hat and GwenX.Brows == 'sad'", "images/GwenBJFace/Gwen_BJ_Mask_Brows_Sad.png",
            "GwenX.Hat and GwenX.Brows == 'surprised'", "images/GwenBJFace/Gwen_BJ_Mask_Brows_Surprised.png",
            "GwenX.Hat and GwenX.Brows == 'confused'", "images/GwenBJFace/Gwen_BJ_Mask_Brows_Surprised.png",
            "GwenX.Hat", "images/GwenBJFace/Gwen_BJ_Mask_Brows_Normal.png",

            "GwenX.Brows == 'angry'", "images/GwenBJFace/Gwen_BJ_Brows_Angry.png",
            "GwenX.Brows == 'sad'", "images/GwenBJFace/Gwen_BJ_Brows_Sad.png",
            "GwenX.Brows == 'surprised'", "images/GwenBJFace/Gwen_BJ_Brows_Surprised.png",
            "GwenX.Brows == 'confused'", "images/GwenBJFace/Gwen_BJ_Brows_Confused.png",
            "True", "images/GwenBJFace/Gwen_BJ_Brows_Normal.png",
            ),
        (0,0),  ConditionSwitch(
            #Hair overlay
            "GwenX.Hat", "Gwen BJ Blink Mask",
            "True", "Gwen BJ Blink",
            ),
            #Eyes
        (0,0), ConditionSwitch(
            #Hair overlay
            "GwenX.Hat", Null(),
            "GwenX.Water or GwenX.Hair == 'wet'", Recolor("Gwen", "Hair", "images/GwenBJFace/Gwen_BJ_Hair_Wet.png"),
            "not Player.Male and 'facial' in GwenX.Spunk",Recolor("Gwen", "Hair", "images/GwenBJFace/Gwen_BJ_Hair_Wet.png"),
            "GwenX.Hair == 'pony'", Null(),
            "True", Recolor("Gwen", "Hair", "images/GwenBJFace/Gwen_BJ_Hair_Short.png"),
            ),
        (0,0), ConditionSwitch(
            #pigtails
            "GwenX.Hat", Null(),
            "GwenX.Water or GwenX.Hair == 'wet'", Null(),
            "not Player.Male and 'facial' in GwenX.Spunk", Null(),
            "GwenX.Hair == 'pony'", Recolor("Gwen", "Hair", "images/GwenBJFace/Gwen_BJ_Hair_Cheer.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # water overlay
            "GwenX.Water", "images/GwenBJFace/Gwen_BJ_Wet.png",
            "not Player.Male and 'facial' in GwenX.Spunk", "images/GwenBJFace/Gwen_BJ_Wet.png",
            "True",Null(),
            ),

#        (0,0), "Gwen_Tester",
        (0,0), ConditionSwitch(
            #cum on the face
            "'hair' in GwenX.Spunk and Player.Male", "images/GwenBJFace/Gwen_BJ_Spunk_Hair.png",
            "'facial' in GwenX.Spunk and Player.Male", "images/GwenBJFace/Gwen_BJ_Spunk_Facial.png",
            "True", Null(),
            ),
        (250,400), ConditionSwitch( #(250,400)(-500,-400)
            #steam
            "True", "Big_Steam",
            "GwenX.Lust > 70", "Big_Steam",
            "True", Null(),
            ),
        )
    zoom 1
    anchor (0.5, 0.5)
    offset (90,-480)

# image Gwen_BJ_Head End        # image Gwen_BJ_Head End        # image Gwen_BJ_Head End        # image Gwen_BJ_Head End

#image Gwen_Tester:
#            "images/GwenBJFace/Gwen_BJ_tester.jpg"
#            alpha 0.5
image Gwen BJ Blink:
        #eyeblinks
        ConditionSwitch(
            "GwenX.Eyes == 'normal'", "images/GwenBJFace/Gwen_BJ_Eyes_Normal.png",
            "GwenX.Eyes == 'sexy'", "images/GwenBJFace/Gwen_BJ_Eyes_Sexy.png",
            "GwenX.Eyes == 'closed'", "images/GwenBJFace/Gwen_BJ_Eyes_Closed.png",
            "GwenX.Eyes == 'surprised'", "images/GwenBJFace/Gwen_BJ_Eyes_Surprised.png",
            "GwenX.Eyes == 'side'", "images/GwenBJFace/Gwen_BJ_Eyes_Side.png",
            "GwenX.Eyes == 'leftside'", "images/GwenBJFace/Gwen_BJ_Eyes_Side.png",
            "GwenX.Eyes == 'stunned'", "images/GwenBJFace/Gwen_BJ_Eyes_Stunned.png",
            "GwenX.Eyes == 'down'", "images/GwenBJFace/Gwen_BJ_Eyes_Down.png",
            "GwenX.Eyes == 'manic'", "images/GwenBJFace/Gwen_BJ_Eyes_Surprised.png",
            "GwenX.Eyes == 'squint'", "images/GwenBJFace/Gwen_BJ_Eyes_Sexy.png",
            "True", "images/GwenBJFace/Gwen_BJ_Eyes_Normal.png",
            ),
        choice:
            3.5
        choice:
            3.25
        choice:
            3
        "images/GwenBJFace/Gwen_BJ_Eyes_Closed.png"
        .25
        repeat

image Gwen BJ Blink Mask:
        #eyeblinks
        ConditionSwitch(
            "GwenX.Brows == 'angry'", "images/GwenBJFace/Gwen_BJ_Mask_Eyes_Angry.png",
            "GwenX.Eyes == 'normal'", "images/GwenBJFace/Gwen_BJ_Mask_Eyes_Normal.png",
            "GwenX.Eyes == 'sexy'", "images/GwenBJFace/Gwen_BJ_Mask_Eyes_Sexy.png",
            "GwenX.Eyes == 'closed'", "images/GwenBJFace/Gwen_BJ_Mask_Eyes_Closed.png",
            "GwenX.Eyes == 'surprised'", "images/GwenBJFace/Gwen_BJ_Mask_Eyes_Surprised.png",
            "GwenX.Eyes == 'manic'", "images/GwenBJFace/Gwen_BJ_Mask_Eyes_Surprised.png",
            "GwenX.Eyes == 'squint'", "images/GwenBJFace/Gwen_BJ_Mask_Eyes_Sexy.png",
            "True", "images/GwenBJFace/Gwen_BJ_Mask_Eyes_Normal.png",
            ),
        choice:
            3.5
        choice:
            3.25
        choice:
            3
        "images/GwenBJFace/Gwen_BJ_Mask_Eyes_Closed.png"
        .25
        repeat

image Gwen_BJ_HairBack:
    LiveComposite(
        (695,695),
        (0,0), ConditionSwitch(
            #Hair backside
            "GwenX.Hat", Null(),
            "GwenX.Water or GwenX.Hair == 'wet'", Recolor("Gwen", "Hair", "images/GwenBJFace/Gwen_BJ_Hair_Wet_Back.png"),
            "not Player.Male and 'facial' in GwenX.Spunk",Recolor("Gwen", "Hair", "images/GwenBJFace/Gwen_BJ_Hair_Wet_Back.png"),
            "GwenX.Hair == 'pony'", Null(),
            "True", Recolor("Gwen", "Hair", "images/GwenBJFace/Gwen_BJ_Hair_Short_Back.png"),
            ),
        (-73,-128), ConditionSwitch(  #(-70,-125)
            #pigtails backside
            "GwenX.Hat", Null(),
            "GwenX.Water or GwenX.Hair == 'wet'", Null(),
            "not Player.Male and 'facial' in GwenX.Spunk", Null(),
            "GwenX.Hair == 'pony'", Recolor("Gwen", "Hair", "images/GwenBJFace/Gwen_BJ_Hair_Cheer_Back.png"),
            "True", Null(),
            ),
        )
    zoom 1
    anchor (0.5, 0.5)
    offset (90,-480)

image Gwen_BJ_Head_Under:
    LiveComposite(
        (695,695),
#        (0,0), "images/GwenBJFace/Gwen_BJ_Head_Sucking_Under.png",
        (0,0), "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_BJ_Head.png",
#         (0,0), ConditionSwitch(
#            # Basic Face layer
#            "Speed and renpy.showing('Gwen_BJ_Animation') and Speed != 1 and Speed != 2 and Speed != 5","images/GwenBJFace/Gwen_BJ_Head_Sucking_Overlay.png",
##            "True","images/GwenBJFace/Gwen_BJ_Head_Sucking_Overlay.png",
#            "GwenX.Blush == 2", "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_BJ_Head_Blush2.png",
#            "GwenX.Blush", "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_BJ_Head_Blush.png",
#            "True", "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_BJ_Head.png"
#            ),

         (0,0), ConditionSwitch(
            #cum on the chin
            "'chin' in GwenX.Spunk and Player.Male", "images/GwenBJFace/Gwen_BJ_Spunk_Chin.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Mouth
#            "True", Null(), #cumming
            "Speed and renpy.showing('Gwen_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
                    "Speed == 1", Recolor("Gwen", "Lips", "images/GwenBJFace/Gwen_BJ_Mouth_TongueW.png"),  #licking
#                    "True", Null(),                          #heading
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", Recolor("Gwen", "Lips", "images/GwenBJFace/Gwen_BJ_Mouth_Sucking.png"), #sucking
                    "Speed == 4", Recolor("Gwen", "Lips", "images/GwenBJFace/Gwen_BJ_Mouth_Sucking.png"), #deepthroat
                    "Speed == 6", Recolor("Gwen", "Lips", "images/GwenBJFace/Gwen_BJ_Mouth_Sucking.png"), #cumming
                    ),
            "renpy.showing('Gwen_CUN_Animation') and Speed", Recolor("Gwen", "Lips", "images/GwenBJFace/Gwen_BJ_Mouth_TongueW.png"),
            "Speed >= 3 and renpy.showing('Gwen_TJ_Animation')", Recolor("Gwen", "Lips", "images/GwenBJFace/Gwen_BJ_Mouth_TongueW.png"),
            "GwenX.Mouth == 'normal'", Recolor("Gwen", "Lips", "images/GwenBJFace/Gwen_BJ_Mouth_Normal.png"),
            "GwenX.Mouth == 'lipbite'", Recolor("Gwen", "Lips", "images/GwenBJFace/Gwen_BJ_Mouth_Normal.png"),
            "GwenX.Mouth == 'sucking'", Recolor("Gwen", "Lips", "images/GwenBJFace/Gwen_BJ_Mouth_Open.png"),
            "GwenX.Mouth == 'kiss'", Recolor("Gwen", "Lips", "images/GwenBJFace/Gwen_BJ_Mouth_Kiss.png"),
            "GwenX.Mouth == 'sad'", Recolor("Gwen", "Lips", "images/GwenBJFace/Gwen_BJ_Mouth_Sad.png"),
            "GwenX.Mouth == 'smile'", Recolor("Gwen", "Lips", "images/GwenBJFace/Gwen_BJ_Mouth_Smile.png"),
            "GwenX.Mouth == 'smirk'", Recolor("Gwen", "Lips", "images/GwenBJFace/Gwen_BJ_Mouth_Normal.png"),
            "GwenX.Mouth == 'grimace'", Recolor("Gwen", "Lips", "images/GwenBJFace/Gwen_BJ_Mouth_Smile.png"),
            "GwenX.Mouth == 'surprised'", Recolor("Gwen", "Lips", "images/GwenBJFace/Gwen_BJ_Mouth_Open.png"),
            "GwenX.Mouth == 'tongue'", Recolor("Gwen", "Lips", "images/GwenBJFace/Gwen_BJ_Mouth_Tongue.png"),
            "True", Recolor("Gwen", "Lips", "images/GwenBJFace/Gwen_BJ_Mouth_Smile.png"),
            ),
        (0,0), ConditionSwitch(
            #Spunk layer
            "'mouth' not in GwenX.Spunk or not Player.Male", Null(),
            "Speed and renpy.showing('Gwen_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
                    "Speed == 1", "images/GwenBJFace/Gwen_BJ_Spunk_Tongue.png",  #licking
                    "True", Null(),                          #heading
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", "images/GwenBJFace/Gwen_BJ_Spunk_SuckingUnder.png", #sucking
                    "Speed == 4", "images/GwenBJFace/Gwen_BJ_Spunk_SuckingUnder.png", #deepthroat
                    "Speed == 6", "images/GwenBJFace/Gwen_BJ_Spunk_SuckingUnder.png", #cumming
                    ),
#            "GwenX.Mouth == 'normal'", "images/GwenBJFace/Gwen_BJ_Spunk_Smile.png",
#            "GwenX.Mouth == 'lipbite'", "images/GwenBJFace/Gwen_BJ_Spunk_Smile.png",
            "GwenX.Mouth == 'kiss'", "images/GwenBJFace/Gwen_BJ_Spunk_Kiss.png",
            "GwenX.Mouth == 'sad'", "images/GwenBJFace/Gwen_BJ_Spunk_Kiss.png",
#            "GwenX.Mouth == 'smile'", "images/GwenBJFace/Gwen_BJ_Spunk_Smile.png",
#            "GwenX.Mouth == 'smirk'", "images/GwenBJFace/Gwen_BJ_Spunk_Kiss.png",
            "GwenX.Mouth == 'surprised'", "images/GwenBJFace/Gwen_BJ_Spunk_Open.png",
            "GwenX.Mouth == 'open'", "images/GwenBJFace/Gwen_BJ_Spunk_Open.png",
            "GwenX.Mouth == 'tongue'", "images/GwenBJFace/Gwen_BJ_Spunk_Tongue.png",
            "GwenX.Mouth == 'sucking'", "images/GwenBJFace/Gwen_BJ_Spunk_Tongue.png",
            "True", "images/GwenBJFace/Gwen_BJ_Spunk_Normal.png",
            ),

#        (0,0), ConditionSwitch(
#            #cum on the chin
#            "'chin' in GwenX.Spunk and Player.Male", "images/GwenBJFace/Gwen_BJ_Spunk_Chin.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #Spunk layer
#            "'mouth' not in GwenX.Spunk or not Player.Male", Null(),
#            "True", "images/GwenBJFace/Gwen_BJ_Spunk_SuckingUnder.png",
#            ),
#        (0,0), Recolor("Gwen", "Lips", "images/GwenBJFace/Gwen_BJ_Mouth_Open.png"),
        )
    zoom 1
    anchor (0.5, 0.5)
    offset (90,-480)

image Gwen_BJ_Heading_Mouth:
    LiveComposite(
        (695,695),
        (0,0), Recolor("Gwen", "Lips", "images/GwenBJFace/Gwen_BJ_Mouth_Open.png"),
         (0,0), ConditionSwitch(
            #cum in mouth
            "'mouth' in GwenX.Spunk and Player.Male", "images/GwenBJFace/Gwen_BJ_Spunk_Open.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Hair overlay
#            "True", Recolor("Gwen", "Hair", "images/GwenBJFace/Gwen_BJ_Hair_Short_Back.png"),
#            ),
        )
    zoom 1
    anchor (0.5, 0.5)
    offset (90,-480)

#image Gwen_BJ_Heading_Overlay:
#    LiveComposite(
#        (695,695),
#        (0,0), "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_BJ_Mouth_Open_Overlay.png",
##        (0,0), ConditionSwitch(
##            #Hair overlay
##            "True", Recolor("Gwen", "Hair", "images/GwenBJFace/Gwen_BJ_Hair_Short_Back.png"),
##            ),
#        )
#    zoom 1
#    anchor (0.5, 0.5)
#    offset (90,-480)

#image Gwen_BJ_MouthHeading:
#    #the mouth used for the heading animations
#    transform_anchor True
#    contains:
#        Recolor("Gwen", "Lips", "images/GwenBJFace/Gwen_BJ_Mouth_Sucking.png")
##        "images/GwenBJFace/Gwen_BJ_Mouth_Heading.png"
#        zoom 1.4
#        anchor (0.50,0.6)  #(0.50,0.65)
#    contains:
#        ConditionSwitch(
#            "'mouth' in GwenX.Spunk and Player.Male", "images/GwenBJFace/Gwen_BJ_Spunk_SuckingUnder.png",#At("Gwen_BJ_MaskHeading", Gwen_BJ_MouthAnim()),
#            "True", Null(),
#            ),
#        zoom 1.4
#        anchor (0.50,0.6)  #(0.50,0.65)
#    contains:
#        ConditionSwitch(
#            "'mouth' in GwenX.Spunk and Player.Male", "images/GwenBJFace/Gwen_BJ_Spunk_SuckingOver.png",#At("Gwen_BJ_MaskHeading", Gwen_BJ_MouthAnim()),
#            "True", Null(),
#            ),
#        zoom 1.4
#        anchor (0.50,0.6)  #(0.50,0.65)
#    subpixel True
#    zoom 0.58 #0.58 = top of heading, 0.66 = crown, 0.60 = valley, 0.68 = base
#    block: #total time 1.0 down, 1.5 back up 2.5 total
#        pause .20
#        easeout .15 zoom 0.6#0.66
#        linear .15 zoom 0.60
#        easein .25 zoom 0.65
#        pause .25
#        #1.0s to this point
#        pause .40
#        easeout .40 zoom 0.58
#        linear .10 zoom 0.66
#        easein .30 zoom 0.45#0.45
#        pause .30
#        #1.5s to this point
#        repeat

#image Gwen_BJ_MouthCumHigh:
#    #the mouth used for the heading animations
#    contains:
#        Recolor("Gwen", "Lips", "images/GwenBJFace/Gwen_BJ_Mouth_Sucking.png")
#        zoom 1.4
#        anchor (0.50,0.6)  #(0.50,0.65)
#    contains:
#        ConditionSwitch(
#            "'mouth' in GwenX.Spunk and Player.Male", "images/GwenBJFace/Gwen_BJ_Spunk_SuckingOver.png",#At("Gwen_BJ_MaskHeading", Gwen_BJ_MouthAnim()),
#            "True", Null(),
#            ),
#        zoom 1.4
#        anchor (0.50,0.6)  #(0.50,0.65)
#    subpixel True
#    zoom 0.55 #0.70
#    block: #total time 10 down, 15 back up
#        pause .20
#        ease .50 zoom 0.48#0.65
#        pause .60
#        ease .30 zoom 0.52#0.7
#        pause .10
#        ease .30 zoom 0.48#0.65
#        pause .20
#        ease .30 zoom 0.52#0.7
#        repeat

#image Gwen_BJ_MouthSuckingMask:
#    #the mask used for sucking animations
#    contains:
#        "images/GwenBJFace/Gwen_BJ_Mouth_MaskS.png"
#        zoom 1.4
#    contains: #see if this works, if not remove it
#        ConditionSwitch(
#            "'mouth' not in GwenX.Spunk and Player.Male", Null(),
#            "Speed != 2 and Speed != 5", Null(),
#            "True", "images/GwenBJFace/Gwen_BJ_Spunk_SuckingOver.png",
#            )
#        zoom 1.4

##image Gwen_BJ_MaskHeading:
##    #the mask used for the heading image
##    contains:
##        "images/GwenBJFace/Gwen_BJ_Mouth_MaskH.png"
##        #offset (-380,-595)

#image Gwen_BJ_MaskHeadingComposite:
#    #The composite for the heading mask that goes over the face
#    LiveComposite(
#        (858,928),
#        (300,462), ConditionSwitch(
#            "Speed == 2", "Gwen_BJ_MouthHeadingComposite",#At("Gwen_BJ_MaskHeading", Gwen_BJ_MouthAnim()),
#            "Speed == 5", "Gwen_BJ_MouthCumHighComposite",#At("Gwen_BJ_MaskHeading", Gwen_BJ_MouthAnimC()),
#            "True", Null(),
#            ),
#        (300,462), ConditionSwitch(
#            "Speed == 2 and 'mouth' in GwenX.Spunk and Player.Male", "GwenHeadingSpunk",#At("Gwen_BJ_MaskHeading", Gwen_BJ_MouthAnim()),
#            "Speed == 5 and 'mouth' in GwenX.Spunk and Player.Male", "GwenCumHighSpunk",#At("Gwen_BJ_MaskHeading", Gwen_BJ_MouthAnimC()),
#            "True", Null(),
#            ),
#        )
#    zoom 1.8

#image Gwen_BJ_MouthHeadingComposite:
#    #the mask for the overlay used for the heading animations
#    transform_anchor True
#    contains:
##        "images/GwenBJFace/Gwen_BJ_Mouth_MaskH.png"
#        "images/GwenBJFace/Gwen_BJ_Mouth_MaskS.png"
##        zoom 1.4
#        anchor (0.50,0.6)  #(0.50,0.65)
#    offset (30,-30)
#    subpixel True
#    zoom 0.58 #0.58 = top of heading, 0.66 = crown, 0.60 = valley, 0.68 = base
#    block: #total time 1.0 down, 1.5 back up 2.5 total
#        pause .20
#        easeout .15 zoom 0.6#0.66
#        linear .15 zoom 0.60
#        easein .25 zoom 0.65
#        pause .25
#        #1.0s to this point
#        pause .40
#        easeout .40 zoom 0.58
#        linear .10 zoom 0.66
#        easein .30 zoom 0.45#0.55
#        pause .30
#        #1.5s to this point
#        repeat

#image GwenHeadingSpunk:
#    #Spunk that goes over the sock when sucking
#    transform_anchor True
#    contains:
#        "images/GwenBJFace/Gwen_BJ_Spunk_SuckingOver.png"
##        zoom 1.4
#        anchor (0.50,0.6)  #(0.50,0.65)
#    offset (30,-30)
#    subpixel True
#    zoom 0.58 #0.58 = top of heading, 0.66 = crown, 0.60 = valley, 0.68 = base
#    block: #total time 1.0 down, 1.5 back up 2.5 total
#        pause .20
#        easeout .15 zoom 0.6#0.66
#        linear .15 zoom 0.60
#        easein .25 zoom 0.65
#        pause .25
#        #1.0s to this point
#        pause .40
#        easeout .40 zoom 0.58
#        linear .10 zoom 0.66
#        easein .30 zoom 0.45#0.55
#        pause .30
#        #1.5s to this point
#        repeat


#image Gwen_BJ_MouthCumHighComposite:
#    #the mask for the overlay used for the cumming high animations
#    contains:
##        "Gwen_BJ_MaskHeading"
#        "images/GwenBJFace/Gwen_BJ_Mouth_MaskH.png"
#        anchor (0.50,0.6)  #(0.50,0.65)
#    subpixel True
#    offset (30,-30)
#    zoom 0.65 #0.70
#    block: #total time 10 down, 15 back up
#        pause .20
#        ease .50 zoom 0.58#0.65
#        pause .60
#        ease .30 zoom 0.62#0.7
#        pause .10
#        ease .30 zoom 0.58#0.65
#        pause .20
#        ease .30 zoom 0.62#0.7
#        repeat

#image GwenCumHighSpunk:
#    #Spunk that goes over the sock when sucking
#    transform_anchor True
#    contains:
#        "images/GwenBJFace/Gwen_BJ_Spunk_SuckingOver.png"
#        anchor (0.50,0.6)  #(0.50,0.65)
#    offset (30,-30)
#    subpixel True
#    zoom 0.65 #0.70
#    block: #total time 10 down, 15 back up
#        pause .20
#        ease .50 zoom 0.58#0.65
#        pause .60
#        ease .30 zoom 0.62#0.7
#        pause .10
#        ease .30 zoom 0.58#0.65
#        pause .20
#        ease .30 zoom 0.62#0.7
#        repeat




#image GwenSuckingSpunk:
#    #Spunk that goes over the sock when sucking
#    contains:
#        "images/GwenBJFace/Gwen_BJ_Spunk_SuckingOver.png"
#        zoom 1.4
#        anchor (0.5, 0.5)

## Start 0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
#image Gwen_BJ_Backdrop1:
#        #Her Body in the BJ pose
##        contains:
##            #blanket
##            ConditionSwitch(
##                "'blanket' in GwenX.RecentActions", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
##                "True", Null(),
##                )
##            zoom 1.2
##            anchor (.5,.5)
##            pos (180,-400)
##            block:
##                ease 1 pos (0,-600)
##                ease 1 pos (-350,0)
##                ease 1 pos (-350,0)
##                ease 1 pos (-350,-600)
##                repeat
##        contains:
##                #bra strap backing
##                "Gwen_TJ_Jacketback"
##                subpixel True
##                pos (0,0) #top (0,-15)
##                transform_anchor True
##        contains:
##                #bra strap backing
##                "Gwen_TJ_Braback"
##                subpixel True
##                pos (0,0) #top (0,-15)
##                transform_anchor True
###                parallel:
###                    ease 2 ypos -20
###                    pause .1
###                    ease 2 ypos -0
###                    pause .1
###                    repeat
#        contains:
#                #base body test / / / / / / / / / / / / / / / / / / / /
#                "Gwen_BJ_Body"
#                subpixel True
#                pos (0,0) #top (0,-10)
#                transform_anchor True
##                parallel:
##                    ease 2 ypos -20
##                    pause .1
##                    ease 2 ypos 0
##                    pause .1
##                    repeat
##        contains:
##                #right hand backside
##                "Gwen_TJ_TitR"
##                subpixel True
##                pos (0,0) #top (0,-15)
##                transform_anchor True
###                parallel:
###                    ease 2 ypos -20
###                    pause .1
###                    ease 2 ypos -0
###                    pause .1
###                    repeat
##        contains:
##                "Gwen_TJ_Tits"
##                subpixel True
##                pos (0,0) #top (0,-15)
##                transform_anchor True
###                parallel:
###                    ease 2 ypos -20
###                    pause .1
###                    ease 2 ypos -0
###                    pause .1
###                    repeat
#        zoom 1.4
#        offset (225,1100)

## End Gwen BJ Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen_BJ_Anim0:
        #Static animation
        contains:
                # Gwen's hair back
                "Gwen_BJ_HairBack"
                subpixel True
                offset (10,160)     #top (350,190), - is up
                rotate 25
                parallel:
                    ease 1 offset (10,180)           #bottom
                    pause .2
                    ease 1.5 offset (10,160)     #top
                    repeat
                parallel:
                    ease 1 rotate 30          #bottom
                    pause .2
                    ease 1.5 rotate 25    #top
                    repeat
        contains:
                #  Gwen's body, everything below the chin
                "Gwen_BJ_Backdrop"
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
                "Gwen_BJ_Head"
#                AlphaMask("Gwen_BJ_Head", "Gwen_BJ_MaskHeadingComposite") #"Gwen_BJ_MouthHeadingComposite")
                subpixel True
#                alpha .9
                offset (10,160)     #top (350,190), - is up
                rotate 25
                parallel:
                    ease 1 offset (10,180)           #bottom
                    pause .2
                    ease 1.5 offset (10,160)     #top
                    repeat
                parallel:
                    ease 1 rotate 30          #bottom
                    pause .2
                    ease 1.5 rotate 25    #top
                    repeat
        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Gwen_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                rotate 0
                parallel:
                    pause 1
                    ease .2 rotate -2
#                    pause .2
                    ease .3 rotate 1
                    ease .3 rotate 0
                    pause .9
                    repeat
#end Gwen_BJ_Anim0 Static

image Gwen_BJ_Anim1:
        #Licking animation
        contains:
                # Gwen's hair back
                "Gwen_BJ_HairBack"
                subpixel True
                offset (-25,105)     #top (350,190), - is up
                rotate -20
                parallel: #2.4 down, 1.8 up
                    ease 1 xoffset -30           #bottom
                    pause 1.4
#                    ease 1 xoffset -30     #top
                    ease .3 xoffset 5     #top
                    pause .2
                    ease 1.3 xoffset -25     #top
                    repeat
                parallel:
                    ease 1 yoffset 250           #bottom
                    pause .4
                    ease 1.5 yoffset 105     #top
                    pause 1.3
                    repeat
                parallel:
                    easein .6 rotate -30          #bottom
#                    pause 1.8
                    pause 1.3
                    ease .5 rotate 0          #bottom
                    ease .3 rotate 30          #bottom
                    pause .5
                    easeout 1 rotate -20    #top
                    repeat
        contains:
                #  Gwen's body, everything below the chin
                "Gwen_BJ_Backdrop"
                subpixel True
                offset (-45,120)     #top
                alpha 1
                transform_anchor True
                rotate -20
                parallel: #2.4 down, 1.8 up
                    ease 1 xoffset -60           #bottom
                    pause 1.4
#                    ease 1 xoffset -40     #top
                    ease .3 xoffset 20     #top
                    pause .3
                    ease 1.2 xoffset -45     #top
                    repeat
                parallel:
                    ease .9 yoffset 280           #bottom
                    pause .5
                    ease 1.6 yoffset 110     #top
                    pause .9
                    ease .3 yoffset 120           #bottom
                    repeat
                parallel:
                    ease .2 rotate -5          #bottom
                    ease 1.0 rotate -20          #bottom
                    ease 1.0 rotate -15          #bottom
                    ease .5 rotate -5          #bottom
                    pause 1.5
                    repeat
#                    ease .2 rotate -25          #bottom
#                    ease 1.8 rotate -30          #bottom
#                    ease .4 rotate -25          #bottom
#                    ease .3 rotate -20          #bottom
#                    pause 1.5
#                    repeat
        contains:
                # head overlay
                "Gwen_BJ_Head"
#                AlphaMask("Gwen_BJ_Head", "Gwen_BJ_MaskHeadingComposite") #"Gwen_BJ_MouthHeadingComposite")
                subpixel True
#                alpha .9
                offset (-25,105)     #top (350,190), - is up
                rotate -20
                parallel: #2.4 down, 1.8 up
                    ease 1 xoffset -30           #bottom
                    pause 1.4
#                    ease 1 xoffset -30     #top
                    ease .3 xoffset 5     #top
                    pause .2
                    ease 1.3 xoffset -25     #top
                    repeat
                parallel:
                    ease 1 yoffset 250           #bottom
                    pause .4
                    ease 1.5 yoffset 105     #top
                    pause 1.3
                    repeat
                parallel:
                    easein .6 rotate -30          #bottom
#                    pause 1.8
                    pause 1.3
                    ease .5 rotate 0          #bottom
                    ease .3 rotate 30          #bottom
                    pause .5
                    easeout 1 rotate -20    #top
                    repeat
        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Gwen_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                rotate 0
                parallel:
#                    pause 2.5
                    pause .3
                    ease .7 rotate -3
                    pause .5
                    ease .9 rotate 1           #bottom
                    pause .1
                    ease .2 rotate -2
                    ease .3 rotate 1
                    ease .2 rotate 0
                    pause 1
                    repeat
#end Gwen_BJ_Anim1 Licking


image Gwen_BJ_Anim2:
        #Heading animation
        contains:
                # Gwen's head hair back
                "Gwen_BJ_HairBack"
                subpixel True
                offset (-20,130)     #top (350,190), - is up
                rotate 0
                parallel:
                    ease 1 yoffset 180#400    #bottom
                    pause .4
                    ease 1 yoffset 130         #top
                    repeat
        contains:
                #  Gwen's body, everything below the chin
                "Gwen_BJ_Backdrop"
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
                # Gwen's head Underlay
                "Gwen_BJ_Head_Under"
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
                # Gwen's open mouth
                "Gwen_BJ_Heading_Mouth"
                subpixel True
                transform_anchor True
                anchor (285,365)
                pos (-64,15) #(-64,13)
                offset (-20,130)     #top (350,190), - is up
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
                    ease 1 yoffset 180#400    #bottom
                    pause .4
                    ease 1 yoffset 130         #top
                    repeat
        contains:
                # Cock
#                "Blowcock"
                subpixel True
                "Gwen_TJ_ZeroCock"
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
#                "Gwen_BJ_Heading_Overlay"
##                AlphaMask("Gwen_BJ_Head", "Gwen_BJ_MaskHeadingComposite") #"Gwen_BJ_MouthHeadingComposite")
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
                "Gwen_BJ_Head"
#                AlphaMask("Gwen_BJ_Head", "Gwen_BJ_MaskHeadingComposite") #"Gwen_BJ_MouthHeadingComposite")
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
#end Gwen_BJ_Anim2 Heading


image Gwen_BJ_Anim3:
        #sucking fast animation
        contains:
                # Gwen's head hair back
                "Gwen_BJ_HairBack"
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
                #  Gwen's body, everything below the chin
                "Gwen_BJ_Backdrop"
                subpixel True
                offset (-20,180)     #top
                alpha 1
                transform_anchor True
                rotate -20
                parallel:
                    ease .4 rotate -30
                    pause .05
                    ease .55 rotate -20#-20
                    repeat
                parallel:
                    ease .35 yoffset 300#400           #bottom
                    pause .05
                    ease .6 yoffset 180     #top
                    repeat
        contains:
                # Gwen's head Underlay
                "Gwen_BJ_Head_Under"
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
                "Gwen_TJ_ZeroCock"
                offset(0,0)
                transform_anchor True
                rotate 0
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
                "Gwen_BJ_Head"
#                AlphaMask("Gwen_BJ_Head", "Gwen_BJ_MaskHeadingComposite") #"Gwen_BJ_MouthHeadingComposite")
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
##end Gwen_BJ_Anim3 Sucking

image Gwen_BJ_Anim4:
        #Deep animation
        contains:
                # Gwen's hair back
                "Gwen_BJ_HairBack"
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
                #  Gwen's body, everything below the chin
                "Gwen_BJ_Backdrop"
                subpixel True
                offset (-20,180)     #top
                alpha 1
                transform_anchor True
                rotate -20
                parallel:
                    ease 1 rotate -45
                    pause .2
                    ease 1.5 rotate -20#-20
                    repeat
                parallel:
                    ease 1 yoffset 450#400           #bottom
                    pause .2
                    ease 1.5 yoffset 180     #top
                    repeat
        contains:
                # Gwen's head Underlay
                "Gwen_BJ_Head_Under"
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
                "Gwen_TJ_ZeroCock"
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
                "Gwen_BJ_Head"
#                AlphaMask("Gwen_BJ_Head", "Gwen_BJ_MaskHeadingComposite") #"Gwen_BJ_MouthHeadingComposite")
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
#end Gwen_BJ_Anim4 Deep


image Gwen_BJ_Anim5:
        #Cum high animation
        contains:
                # Gwen's hair back
                "Gwen_BJ_HairBack"
                subpixel True
                offset (0,160)     #top (350,190), - is up
                rotate 30
                parallel:
                    ease 1 offset (-30,180)           #bottom
                    pause .2
                    ease .5 offset (-10,160)     #top
                    repeat
                parallel:
                    ease 1 rotate 25          #bottom
                    pause .2
                    ease .5 rotate 30    #top
                    repeat
        contains:
                #  Gwen's body, everything below the chin
                "Gwen_BJ_Backdrop"
                subpixel True
                offset (-10,160)     #top
                alpha 1
                transform_anchor True
                rotate -5
                parallel:
                    ease 1 offset (-30,180)           #bottom
                    pause .2
                    ease .5 offset (-10,160)     #top
                    repeat
                parallel:
                    ease 1 rotate -10
                    pause .2
                    ease .5 rotate -5#-20
                    repeat
        contains:
                # Gwen's head Underlay
                "Gwen_BJ_Head_Under"
                subpixel True
                offset (-10,160)     #top (350,190), - is up
                rotate 30
                parallel:
                    ease 1 offset (-30,180)           #bottom
                    pause .2
                    ease .5 offset (-10,160)     #top
                    repeat
                parallel:
                    ease 1 rotate 25          #bottom
                    pause .2
                    ease .5 rotate 30    #top
                    repeat
        contains:
                # Gwen's open mouth
                "Gwen_BJ_Heading_Mouth"
                subpixel True
                transform_anchor True
                anchor (285,365)
                pos (-64,-15) #(-64,15)
                offset (-10,160)     #top (350,190), - is up
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
                    ease 1 offset (-30,180)           #bottom
                    pause .2
                    ease .5 offset (-10,160)     #top
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
                "Gwen_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
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
                "Gwen_BJ_Head"
#                AlphaMask("Gwen_BJ_Head", "Gwen_BJ_MaskHeadingComposite") #"Gwen_BJ_MouthHeadingComposite")
                subpixel True
                offset (-10,160)     #top (350,190), - is up
                rotate 30
                parallel:
                    ease 1 offset (-30,180)           #bottom
                    pause .2
                    ease .5 offset (-10,160)     #top
                    repeat
                parallel:
                    ease 1 rotate 25          #bottom
                    pause .2
                    ease .5 rotate 30    #top
                    repeat
#end Gwen_BJ_Anim5 Cum high


image Gwen_BJ_Anim6:
        #Cum Deep animation
        contains:
                # Gwen's hair back
                "Gwen_BJ_HairBack"
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
                #  Gwen's body, everything below the chin
                "Gwen_BJ_Backdrop"
                subpixel True
                offset (0,450)     #top
                alpha 1
                transform_anchor True
                rotate -45
                parallel:
                    ease 1.8 yoffset 410#430           #bottom
                    pause .2
                    ease 1.8 yoffset 430#450     #top
                    pause .2
                    repeat
        contains:
                # Gwen's head Underlay
                "Gwen_BJ_Head_Under"
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
                "Gwen_TJ_ZeroCock"
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
                "Gwen_BJ_Head"
#                AlphaMask("Gwen_BJ_Head", "Gwen_BJ_MaskHeadingComposite") #"Gwen_BJ_MouthHeadingComposite")
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
#end Gwen_BJ_Anim6 Cum Deep

##Head and Body Animations for Gwen's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
#                                                               #BJ Launchers
##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Gwen_BJ_Launch(Line = Trigger):    # The sequence to launch the Gwen BJ animations

##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    return
##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary

    if renpy.showing("Gwen_BJ_Animation"):
        return

    if not Player.Male:
        call Gwen_CUN_Launch
        return

    if renpy.showing("Gwen_TJ_Animation"):
            hide Gwen_TJ_Animation
    else:
            call Girl_Hide(GwenX)
            if Line == "L" or Line == "cum":
                show Gwen_Sprite at SpriteLoc(StageCenter) zorder 150:
                    alpha 1
                    ease 1 zoom 2.5 offset (150,80)
                with dissolve
            else:
                show Gwen_Sprite at SpriteLoc(StageCenter) zorder 150:
                    alpha 1
                    zoom 2.5 offset (150,80)
                with dissolve
            hide Gwen_Sprite
    #". . ."
    $ Speed = 0

    if Line != "cum":
        $ Trigger = "blow"

    show Gwen_BJ_Animation zorder 150:
        pos (1000,1050)#(1000,1000)#(700,520)

    if Taboo and Line == "L": # Gwen gets started. . .
            if len(Present) >= 2:
                if Present[0] != GwenX:
                        "[GwenX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                elif Present[1] != GwenX:
                        "[GwenX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
            else:
                        "[GwenX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
            "Затем она наклоняется и берет ваш член в свой рот."
    elif Line == "L":
            "[GwenX.Name] плавно наклоняется и прислоняет ваш член к своей щеке."
    return

label Gwen_BJ_Reset: # The sequence to the Gwen animations from BJ to default
    if Player.Male != 1:
            call Gwen_CUN_Reset
    if not renpy.showing("Gwen_BJ_Animation"):
        return
#    hide Gwen_BJ_Animation
    call Girl_Hide(GwenX)
    $ Speed = 0

    show Gwen_Sprite at SpriteLoc(StageCenter) zorder 150:
        alpha 1 zoom 2.5 offset (150,80)
    with dissolve

    show Gwen_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .2
        ease .3 zoom 1 offset (0,0)
    pause 1.5
    show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) zorder GwenX.Layer:
        alpha 1 zoom 1 offset (0,0)
    return

# End Gwen Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Gwen's TJ animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Animation components / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# start base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Gwen_TJ_Animation:
            #core TJ animation
            contains:
                ConditionSwitch(
                    # Gwen's upper body
                    "not Player.Sprite","Gwen_TJ_0",#Static
                    "Speed == 1", "Gwen_TJ_1",#slow
                    "Speed == 3", "Gwen_TJ_3",#licking
                    "Speed == 4", "Gwen_TJ_0",#cumming high
                    "Speed == 5", "Gwen_TJ_5",#cumming low
                    "Speed >= 2", "Gwen_TJ_2",#fast
                    "True",       "Gwen_TJ_0",#Static
                    )
            zoom .8 #.7
            transform_anchor True
            anchor (.5,.5)
# end base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#image Gwen_TJ_Head:
#            #Hair underlay
#            "Gwen_BJ_Head"
#            transform_anchor True
#            zoom .7
#            anchor (0.5, 0.5)
#            offset (30,-450)
#            rotate 0


image Gwen_TJ_ZeroCock:
            #cock used in Gwen's sex pose
            "Zero_Blowcock"
            transform_anchor True
            zoom .6
            anchor (0.5, 0.6)
            offset (0,50)#(5,50)
            rotate 0


image Gwen_TJ_Body:
    LiveComposite(
        (800,950),       #550,950
#        (-10,-90), "Gwen_BJ_HairBack", #(75,-10)

        (0,0), "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_TJ_Body.png",

#        (0,0), ConditionSwitch(
#            #Water effect
#            "GwenX.Water and GwenX.ArmPose == 1", "images/GwenSprite/Gwen_Sprite_Water1.png",
#            "GwenX.Water", "images/GwenSprite/Gwen_Sprite_Water2.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            # under tit
##            "GwenX.Water", "images/GwenSprite/Gwen_Sprite_Water2.png",
#            "True", "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_TJ_Tit_Under.png",
#            ),
#        (0,0), "images/GwenBJFace/Gwen_TJ_RefCock.png",

#        (0,0), ConditionSwitch(
#            # under tit smoosh
#            "GwenX.Water", Null(),
#            "True", "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_TJ_Tit_Under_Smoosh.png",
#            ),
#        (0,0), ConditionSwitch(
#            # over tit
##            "GwenX.Water", "images/GwenSprite/Gwen_Sprite_Water2.png",
#            "True", "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_TJ_Tit_Over.png",
#            ),

        (0,0), ConditionSwitch(
            #Chest layer under tits
            "GwenX.Over == 'tshirt'", Null(),
            "GwenX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "GwenX.Chest == 'lace bra'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Lace_Body_Up.png"),
                    "GwenX.Chest == 'bra'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Lace_Body_Up.png"),
                    "GwenX.Chest == 'tank'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Tank_Body_Up.png"),
                    "GwenX.Chest == 'bikini top'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Bikini_Body_Up.png"),
                    "True", Null(),
                    ),
            "GwenX.Chest == 'lace bra'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Lace_Body.png"),
            "GwenX.Chest == 'bra'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Lace_Body.png"),
#            "Player.Sprite and renpy.showing('Gwen_TJ_Animation') and GwenX.Chest == 'tank'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Tank_Body_Fucking.png"),
            "GwenX.Chest == 'tank'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Tank_Body_Fucking.png"),
            "GwenX.Chest == 'bikini top'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Bikini_Body.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over body layer
            "GwenX.Arms and GwenX.Over == 'open suit'", "images/GwenBJFace/Gwen_TJ_Over_Suit_Open_Body_Gloved.png",
            "GwenX.Over == 'open suit'", "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_TJ_Over_Suit_Open_Body.png",
            "GwenX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "GwenX.Arms and GwenX.Over == 'suit'", "images/GwenBJFace/Gwen_TJ_Over_Suit_Open_Body_Gloved.png",
                    "GwenX.Over == 'suit'", "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_TJ_Over_Suit_Open_Body.png",
                    "GwenX.Over == 'tshirt'", Recolor("Gwen", "Over", "images/GwenBJFace/Gwen_TJ_Over_Tshirt_Body_Up.png"),
                    "GwenX.Over == 'cheer top'", Recolor("Gwen", "Over", "images/GwenBJFace/Gwen_TJ_Over_Cheer_Body_Up.png"),
                    "True", Null(),
                    ),
            "GwenX.Over == 'suit' and GwenX.Arms", "images/GwenBJFace/Gwen_TJ_Over_Suit_Body_Gloved.png",
            "GwenX.Over == 'suit'", "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_TJ_Over_Suit_Body.png",

            "GwenX.Over == 'tshirt'", Recolor("Gwen", "Over", "images/GwenBJFace/Gwen_TJ_Over_Tshirt_Body.png"),
            "GwenX.Over == 'cheer top'", Recolor("Gwen", "Over", "images/GwenBJFace/Gwen_TJ_Over_Cheer_Body.png"),
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #Chest tits layer
#            "GwenX.Uptop", ConditionSwitch(
#                    # if top is up. . .
#                    "GwenX.Chest == 'lace bra'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Lace_Tits_Up.png"),
#                    "GwenX.Chest == 'bra'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Bra_Tits_Up.png"),
#                    "GwenX.Chest == 'tank'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Tank_Tits_Up.png"),
#                    "GwenX.Chest == 'bikini top'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Bikini_Tits_Up.png"),
#                    "True", Null(),
#                    ),
#            "GwenX.Chest == 'lace bra'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Lace_Tits.png"),
#            "GwenX.Chest == 'bra'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Bra_Tits.png"),
#            "GwenX.Chest == 'tank'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Tank_Tits.png"),
#            "GwenX.Chest == 'bikini top'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Bikini_Tits.png"),
#            "True", Null(),
#            ),

#        (0,0), ConditionSwitch(
#            #Over tits layer
#            "GwenX.Uptop", ConditionSwitch(
#                    # if top is up. . .
#                    "GwenX.Over == 'suit'", "images/GwenBJFace/Gwen_TJ_Over_Suit_Tits_Up.png",
#                    "GwenX.Over == 'tshirt'", Recolor("Gwen", "Over", "images/GwenBJFace/Gwen_TJ_Over_Tshirt_Tits_Up.png"),
#                    "True", Null(),
#                    ),
#            "GwenX.Over == 'suit'", "images/GwenBJFace/Gwen_TJ_Over_Suit_Tits.png",
#            "GwenX.Over == 'tshirt'", Recolor("Gwen", "Over", "images/GwenBJFace/Gwen_TJ_Over_Tshirt_Tits.png"),
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #hands layer
            "GwenX.Arms and (GwenX.Over == 'suit' or GwenX.Over == 'open suit')", "images/GwenBJFace/Gwen_TJ_Hands_Gloved.png",
            "True", "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_TJ_Hands.png",
            ),
#        (0,0), "images/GwenBJFace/Gwen_TJ_RefLine.png",

#        (0,0), ConditionSwitch(
#            #naked tit piercings
#            "not GwenX.Pierce", Null(),
##            "not GwenX.Pierce or ((GwenX.Over or GwenX.Chest) and not GwenX.Uptop)", Null(),
##            "GwenX.Uptop", Null(),
#            #Only does this if she has piercings, has no tops, or has her top up
#            "GwenX.Pierce == 'ring'", ConditionSwitch(
#                    # if top is up. . .
#                    "GwenX.Uptop", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Ring.png",

#                    "GwenX.Over == 'suit'", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Ring_Pink.png", #change if new tops added in other colors
#                    "GwenX.Over == 'towel' or GwenX.Over == 'tshirt'", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Ring_White.png", #change if new tops added in other colors

#                    "GwenX.Chest == 'lace bra'", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Ring_Lace.png",
#                    "GwenX.Chest == 'tank' or GwenX.Chest == 'bra'", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Ring_White.png",
#                    "GwenX.Chest == 'bikini top'", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Ring_Pink.png",
#                    "True", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Ring.png",
#                    ),
#            # Pierce is "barbell"
#            "GwenX.Uptop", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Barbell.png",

#            "GwenX.Over == 'suit'", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Barbell_Pink.png", #change if new tops added in other colors
#            "GwenX.Over == 'towel' or GwenX.Over == 'tshirt'", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Barbell_White.png", #change if new tops added in other colors

#            "GwenX.Chest == 'lace bra'", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Barbell_Lace.png",
#            "GwenX.Chest == 'tank' or GwenX.Chest == 'bra'", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Barbell_White.png",
#            "GwenX.Chest == 'bikini top'", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Barbell_Pink.png",

#            "True", "images/GwenSprite/Gwen_Sprite_Pierce_Tits_Barbell.png",
#            ),

#        (0,0), ConditionSwitch(
#            #Chest layer over shirt
#            "GwenX.Uptop", ConditionSwitch(
#                    # if top is up. . .
#                    "GwenX.Chest == 'lace bra' or GwenX.Chest == 'bra'", Recolor("Gwen", "Chest", "images/GwenSprite/Gwen_Sprite_Chest_Lace_Up_Top.png"),
#                    "GwenX.Chest == 'tank'", Recolor("Gwen", "Chest", "images/GwenSprite/Gwen_Sprite_Chest_Tank_Up_Top.png"),
#                    "GwenX.Chest == 'bikini top'", Recolor("Gwen", "Chest", "images/GwenSprite/Gwen_Sprite_Chest_Bikini_Up_Top.png"),
#                    "True", Null(),
#                    ),
#            "True", Null(),
#            ),

#        (0,0), ConditionSwitch(
#            #breast spunk
#            "'tits' in GwenX.Spunk and Player.Male", "images/GwenSprite/Gwen_Sprite_Spunk_Tits.png",
#            "True", Null(),
#            ),

#        (-10,-90), "Gwen_Sprite_Head", #(75,-10)



        )
    transform_anchor True
    anchor (0.6, 1.0)#(0.6, 0.0)
    xoffset 155#300
    yoffset 125#-600
#    zoom .75  #.76
    rotate 0

#    transform_anchor True
#    zoom 1
#    anchor (0.4, 1.0)
#    #offset (410,770) # (300,275)
#    rotate 0


image Gwen_TJ_Tits_Under:
    LiveComposite(
        (800,950),       #550,950
        (0,0), ConditionSwitch(
            # under tit
#            "GwenX.Water", "images/GwenSprite/Gwen_Sprite_Water2.png",
            "True", "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_TJ_Tit_Under.png",
            ),
#        (0,0), ConditionSwitch(
#            #Chest tits layer
#            "GwenX.Uptop", Null(),
#            "GwenX.Over == 'tshirt'", Null(),
#            "GwenX.Chest == 'tank'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Tank_Body_Fucking.png"),
##            "GwenX.Chest == 'bikini top'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Bikini_Tits.png"),
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            # spunk under tits
            "'tits' not in GwenX.Spunk", Null(),
            "True", "images/GwenBJFace/Gwen_TJ_Spunk_Under.png",
            ),
        )
    transform_anchor True
#    anchor (0.6, 1.0)#(0.6, 0.0)
#    xoffset 155#300
#    yoffset 125#-600
##    zoom .75  #.76
    rotate 0


image Gwen_TJ_Tits_Over:
    LiveComposite(
        (800,950),    #800,950
#        (0,0), ConditionSwitch(
#            # under tit smoosh
#            "GwenX.Water", Null(),
#            "True", "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_TJ_Tit_Under_Smoosh.png",
#            ),
#        (0,0), ConditionSwitch(
#            # over tit
#            "Player.Sprite and renpy.showing('Gwen_TJ_Animation')", "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_TJ_Tit_Over_Smoosh.png",
#            "True", "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_TJ_Tit_Over.png",
#            ),

        (0,0),  "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_TJ_Tit_Over_Smoosh.png",
        (0,0), ConditionSwitch(
            #Chest tits layer
            "GwenX.Over == 'tshirt'", Null(),
            "GwenX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "GwenX.Chest == 'lace bra'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Lace_Tits_Up.png"),
                    "GwenX.Chest == 'bra'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Bra_Tits_Up.png"),
                    "GwenX.Chest == 'bikini top'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Bikini_Tits_Up.png"),
                    "GwenX.Chest == 'tank'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Tank_Tits_Up.png"),
                    "True", Null(),
                    ),
            "GwenX.Chest == 'lace bra'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Lace_Tits.png"),
            "GwenX.Chest == 'bra'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Bra_Tits.png"),
            "GwenX.Chest == 'bikini top'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Bikini_Tits.png"),
#            "Player.Sprite and renpy.showing('Gwen_TJ_Animation') and GwenX.Chest == 'tank'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Tank_Tits_Fucking.png"),
            "GwenX.Chest == 'tank'", Recolor("Gwen", "Chest", "images/GwenBJFace/Gwen_TJ_Chest_Tank_Tits_Fucking.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Over tits layer
            "GwenX.Uptop", ConditionSwitch(
                    # if top is up. . .
#                    "GwenX.Over == 'suit'", "images/GwenBJFace/Gwen_TJ_Over_Suit_Tits_Up.png",
                    "GwenX.Over == 'tshirt'", Recolor("Gwen", "Over", "images/GwenBJFace/Gwen_TJ_Over_Tshirt_Tits_Up.png"),
                    "GwenX.Over == 'cheer top'", Recolor("Gwen", "Over", "images/GwenBJFace/Gwen_TJ_Over_Cheer_Tits_Up.png"),
                    "True", Null(),
                    ),
            "GwenX.Over == 'suit'", "images/GwenBJFace/Gwen_TJ_Over_Suit_Tits.png",
            "GwenX.Over == 'tshirt'", Recolor("Gwen", "Over", "images/GwenBJFace/Gwen_TJ_Over_Tshirt_Tits.png"),
            "GwenX.Over == 'cheer top'", Recolor("Gwen", "Over", "images/GwenBJFace/Gwen_TJ_Over_Cheer_Tits.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Piercings layer
            "not GwenX.Pierce", Null(),
            "GwenX.Pierce == 'ring'", ConditionSwitch(
                    #if it's the ring pericings
                    "GwenX.Uptop", "images/GwenBJFace/Gwen_TJ_Pierce_Ring.png",
                    "GwenX.Over == 'suit'", "images/GwenBJFace/Gwen_TJ_Pierce_Ring_Pink.png",
                    "GwenX.Over == 'tshirt' or GwenX.Over == 'cheer top'", "images/GwenBJFace/Gwen_TJ_Pierce_Ring_White.png",
                    "GwenX.Chest == 'lace bra'", "images/GwenBJFace/Gwen_TJ_Pierce_Ring_Lace.png",
                    "GwenX.Chest == 'bra'", "images/GwenBJFace/Gwen_TJ_Pierce_Ring_White.png",
                    "GwenX.Chest == 'bikini top'", "images/GwenBJFace/Gwen_TJ_Pierce_Ring_Pink.png",
                    "GwenX.Chest == 'tank'", "images/GwenBJFace/Gwen_TJ_Pierce_Ring_White.png",
                    "True", "images/GwenBJFace/Gwen_TJ_Pierce_Ring.png",
                    ),
            "GwenX.Uptop", "images/GwenBJFace/Gwen_TJ_Pierce_Barbell.png",
            "GwenX.Over == 'suit'", "images/GwenBJFace/Gwen_TJ_Pierce_Barbell_Pink.png",
            "GwenX.Over == 'tshirt' or GwenX.Over == 'cheer top'", "images/GwenBJFace/Gwen_TJ_Pierce_Barbell_White.png",
            "GwenX.Chest == 'lace bra'", "images/GwenBJFace/Gwen_TJ_Pierce_Barbell_Lace.png",
            "GwenX.Chest == 'bra'", "images/GwenBJFace/Gwen_TJ_Pierce_Barbell_White.png",
            "GwenX.Chest == 'bikini top'", "images/GwenBJFace/Gwen_TJ_Pierce_Barbell_Pink.png",
            "GwenX.Chest == 'tank'", "images/GwenBJFace/Gwen_TJ_Pierce_Barbell_White.png",
            "True", "images/GwenBJFace/Gwen_TJ_Pierce_Barbell.png",
            ),
        (0,0), ConditionSwitch(
            # spunk over tits
            "'tits' not in GwenX.Spunk", Null(),
#            "GwenX.Over == 'tshirt'", "images/GwenBJFace/Gwen_TJ_Spunk_Clothed.png",
            "not GwenX.Uptop and GwenX.Over", "images/GwenBJFace/Gwen_TJ_Spunk_Clothed.png",
            "True", "images/GwenBJFace/Gwen_TJ_Spunk_Over.png",
            ),
#        (0,0), "images/GwenBJFace/Gwen_TJ_RefLine.png",
#        (0,0), "images/GwenBJFace/Gwen_TJ_RefLine2.png",
        )
    transform_anchor True
#    anchor (0.6, 1.0)#(0.6, 562)
#    xoffset 155#300
#    yoffset 325#125
#    yoffset -925#-625#-325
#    zoom .75  #.76
    rotate 0

image Gwen_TJ_Hands:
    LiveComposite(
        (800,950),       #550,950
        (0,0), ConditionSwitch(
            #hands layer
            "GwenX.Arms and (GwenX.Over == 'suit' or GwenX.Over == 'open suit')", "images/GwenBJFace/Gwen_TJ_Hands_Gloved.png",
            "True", "images/GwenBJFace/[GwenX.skin_image.skin_path]Gwen_TJ_Hands.png",
            ),
        )
    transform_anchor True
#    anchor (0.6, 1.0)#(0.6, 0.0)
#    xoffset 155#300
#    yoffset 125#-600
#    zoom .75  #.76
    rotate 0

#image Gwen_TJ_Tit_Under:
#            #body underlay
#            contains:
#                "images/GwenBJFace/Gwen_TJ_TitsUnder.png",
##                ConditionSwitch(
##                    # right breast overlay
##                    "GwenX.Chest == 'cos bra'",Null(),
##                    "renpy.showing('Gwen_TJ_Animation')", "images/GwenBJFace/Gwen_TJ_TitsUnder.png",
##                    "True",  Null(),
##                    )
##            contains:
##                ConditionSwitch(
##                        "'tits' not in GwenX.Spunk",Null(),
##                        "True",       "images/GwenBJFace/Gwen_TJ_Spunk_TitsUnder.png",
##                        )
#            transform_anchor True
#            zoom 1
#            anchor (0.4, 1.0)
#            #offset (410,770) # (300,275)
#            rotate 0

#image Gwen_TJ_Jacketback:
#            #back fo the bra straps
#            contains:
#                ConditionSwitch(
#                        "not GwenX.Acc", Null(),
#                        "True", "images/GwenBJFace/Gwen_TJ_JacketBack.png",
#                        )
#            transform_anchor True
#            zoom 1
#            anchor (0.4, 1.0)
#            #offset (410,770) # (300,275)
#            rotate 0

#image Gwen_TJ_Braback:
#            #back fo the bra straps
#            contains:
#                ConditionSwitch(
#                        #"GwenX.Chest == 'corset' and not GwenX.Uptop","images/GwenBJFace/Gwen_TJ_Chest_Corset.png",
##                        "GwenX.Over",Null(),
#                        "GwenX.Chest == 'sports bra'","images/GwenBJFace/Gwen_TJ_Chest_Sports_Back.png",
##                        "GwenX.Chest == 'lace bra'","images/GwenBJFace/Gwen_TJ_Chest_Lace_Back.png",
#                        "GwenX.Chest == 'bikini top' and GwenX.Uptop","images/GwenBJFace/Gwen_TJ_Chest_Bikini_Up_Back.png",
#                        "GwenX.Chest == 'bikini top'","images/GwenBJFace/Gwen_TJ_Chest_Bikini_Back.png",
#                        "True", Null(),
#                        )
#            transform_anchor True
#            zoom 1
#            anchor (0.4, 1.0)
#            #offset (410,770) # (300,275)
#            rotate 0

image Gwen_TJ_BraStretch:
            #bra streching effect
            contains:
                ConditionSwitch(
                    #Over tits layer
                    "GwenX.Over == 'tshirt'", Recolor("Gwen", "Over", "images/GwenBJFace/Gwen_TJ_Over_Tshirt_Stretch.png"),
                    "True", Null(),
                    )
#            contains:
#                    "images/GwenBJFace/Gwen_TJ_RefLine2.png"
            transform_anchor True
#            zoom 1
#            offset (50,0) # (300,275)
#            anchor (.1,.1)#(0.1, .2)
            rotate 0

#image Gwen_TJ_Tits:
#            #layer with left tit and all clothing
#            contains:
#                "images/GwenBJFace/Gwen_TJ_Tits.png"
##            contains:
##                ConditionSwitch(
##                        "not GwenX.Water",Null(),
##                        "True",       "images/GwenBJFace/Gwen_TJ_Tits_Wet.png",
##                        )
#            contains:
#                #Chest
#                ConditionSwitch(
#                        "GwenX.Chest == 'lace bra' and GwenX.Uptop","images/GwenBJFace/Gwen_TJ_Chest_Lace_Up.png",  #fix, add "no straps" version here
#                        "GwenX.Chest == 'lace bra'","images/GwenBJFace/Gwen_TJ_Chest_Lace.png",
#                        "GwenX.Chest == 'sports bra'","images/GwenBJFace/Gwen_TJ_Chest_Sports.png",
#                        "GwenX.Chest == 'bikini top' and GwenX.Uptop","images/GwenBJFace/Gwen_TJ_Chest_Bikini_Up.png",
#                        "GwenX.Chest == 'bikini top'","images/GwenBJFace/Gwen_TJ_Chest_Bikini.png",
#                        "True", Null(),
#                        )
#            contains:
#                #Over
#                ConditionSwitch(
#                        "GwenX.Over == 'tube top' and GwenX.Uptop","images/GwenBJFace/Gwen_TJ_Over_Tube_Up.png",
#                        "GwenX.Over == 'tube top'","images/GwenBJFace/Gwen_TJ_Over_Tube.png",
#                        "True", Null(),
#                        )
#            contains:
#                #Piercings clothing
#                ConditionSwitch(
#                        "not GwenX.Pierce", Null(),
#                        "GwenX.Pierce == 'ring'", ConditionSwitch(
#                                #if she's got ring piercings
#                                "GwenX.Uptop", "images/GwenBJFace/Gwen_TJ_Pierce_Ring.png",
#                                "GwenX.Over == 'tube top'", "images/GwenBJFace/Gwen_TJ_Pierce_Ring_Pink.png",
#                                "GwenX.Chest == 'bikini top'", "images/GwenBJFace/Gwen_TJ_Pierce_Ring_Pink.png",
#                                "GwenX.Chest == 'lace bra'", "images/GwenBJFace/Gwen_TJ_Pierce_Ring_Lace.png",
#                                "True", "images/GwenBJFace/Gwen_TJ_Pierce_Ring.png",
#                                ),
#                        "GwenX.Uptop", "images/GwenBJFace/Gwen_TJ_Pierce_Barbell.png",
#                        "GwenX.Over == 'tube top'", "images/GwenBJFace/Gwen_TJ_Pierce_Barbell_Pink.png",
#                        "GwenX.Chest == 'bikini top'", "images/GwenBJFace/Gwen_TJ_Pierce_Barbell_Pink.png",
#                        "GwenX.Chest == 'lace bra'", "images/GwenBJFace/Gwen_TJ_Pierce_Barbell_Lace.png",
#                        "True", "images/GwenBJFace/Gwen_TJ_Pierce_Barbell.png",
#                        )
#            contains:
#                #Over
#                ConditionSwitch(
#                        "'tits' in GwenX.Spunk and Player.Male","images/GwenBJFace/Gwen_TJ_Spunk_Tits_Over.png",
#                        "True", Null(),
#                        )
#            transform_anchor True
#            zoom 1
#            anchor (0.4, 1.0)
#            #offset (410,770) # (300,275)
#            rotate 0


## Animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start 0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Gwen_TJ_0:
        #Her Body in the TJ pose, static
        contains:
                #hair back
                "Gwen_BJ_HairBack"
                subpixel True
#                offset (90,-480)
                pos (0,0) #top (0,-10)
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
                "Gwen_TJ_Body"
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
                "Gwen_BJ_Head"
                subpixel True
#                offset (90,-480)
                pos (0,0) #top (0,-10)
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
                "Gwen_TJ_Tits_Under"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 200#200
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
                "Gwen_TJ_ZeroCock"
#                ConditionSwitch(
#                            "Player.Sprite","Gwen_TJ_ZeroCock",
#                            "True",  Null(),
#                            )
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (0,50)#(5,50)
        contains:
                #overside tit
                "Gwen_TJ_Tits_Over"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 200#200
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
                #bra stretch
                "Gwen_TJ_BraStretch"
                subpixel True
                pos (0,0) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 818)#(0.6, 700)
                xoffset 315#68
                yoffset -265#-271
                yzoom .2
                alpha 0.7
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
                #hands over everything
                "Gwen_TJ_Hands"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 200#200
                yoffset -271#125
                parallel:
                    ease 2 ypos 30
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat


# End Gwen TJ Pose 0 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start 1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
#image Gwen_TJ_0X:
#        #Her Body in the TJ pose, slow


# End Gwen TJ Pose 0 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


## Start 1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Gwen_TJ_1:
        #Her Body in the TJ pose, slow
        contains:
                #hair back
                "Gwen_BJ_HairBack"
                subpixel True
#                offset (90,-480)
                pos (0,0) #top (0,-10)
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
                "Gwen_TJ_Body"
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
                "Gwen_BJ_Head"
                subpixel True
#                offset (90,-480)
                pos (0,0) #top (0,-10)
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
                "Gwen_TJ_Tits_Under"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 200#200
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
                "Gwen_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (0,50)#(5,50)
        contains:
                #overside tit
                "Gwen_TJ_Tits_Over"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 200#200
                yoffset -271#125
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
                #bra stretch
                "Gwen_TJ_BraStretch"
                subpixel True
                pos (0,0) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 818)#(0.6, 700)
                xoffset 315#68
                yoffset -265#-271
                yzoom .2
#                alpha 0.7
                parallel:
                    ease 2 ypos 120
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
                parallel:
                    pause .2
                    ease 1.8 yzoom 1.2
                    pause .3
                    ease 2 yzoom .2
                    pause .4
                    repeat
        contains:
                #hands over everything
                "Gwen_TJ_Hands"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 200#200
                yoffset -271#125
                parallel:
                    ease 2 ypos 120
                    pause .3
                    ease 2 ypos 0
                    pause .4
                    repeat
## End Gwen TJ Pose 1 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




## Start 2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Gwen_TJ_2:
        #Her Body in the TJ pose, fast
        contains:
                #hair back
                "Gwen_BJ_HairBack"
                subpixel True
#                offset (90,-480)
                pos (0,0) #top (0,-10)
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
                "Gwen_TJ_Body"
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
                "Gwen_BJ_Head"
                subpixel True
#                offset (90,-480)
                pos (0,0) #top (0,-10)
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
                "Gwen_TJ_Tits_Under"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 200#200
                yoffset -271#125
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
                "Gwen_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (0,50)#(5,50)
        contains:
                #overside tit
                "Gwen_TJ_Tits_Over"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 200#200
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
                #bra stretch
                "Gwen_TJ_BraStretch"
                subpixel True
                pos (0,0) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 818)#(0.6, 700)
                xoffset 315#68
                yoffset -265#-271
                yzoom .2
                parallel: #4.7s total -> 1.9
                    ease .6 ypos 60 #120
                    pause .1
                    ease .8 ypos 0
                    pause .2
                    repeat
                parallel: #4.7s total -> 1.9
                    ease .6 yzoom .6 #120
                    pause .1
                    ease .8 yzoom .2
                    pause .2
                    repeat
        contains:
                #hands over everything
                "Gwen_TJ_Hands"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 200#200
                yoffset -271#125
                parallel: #4.7s total -> 1.9
                    ease .6 ypos 60 #120
                    pause .1
                    ease .8 ypos 0
                    pause .2
                    repeat


## End Gwen TJ Pose 2 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

## Start 3 (licking) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Gwen_TJ_3:
        #Her Body in the TJ pose, licking
        contains:
                #hair back
                "Gwen_BJ_HairBack"
                subpixel True
#                offset (90,-480)
                pos (0,180) #top (0,-10)
                transform_anchor True
                rotate 40
                parallel:
                    ease 2 xpos 20
                    pause .3
                    easeout .5 xpos 0
                    easeout 1 xpos 5
#                    pause .5
                    repeat
                parallel:
                    pause .1
                    ease 2 rotate 10
                    pause .3
                    ease .5 rotate 40
                    easein .9 rotate 35
#                    pause .4
                    repeat
        contains:
                #base body  / / / / / / / / / / / / / / / / / / / /
                "Gwen_TJ_Body"
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
                "Gwen_BJ_Head"
                subpixel True
#                offset (90,-480)
                pos (0,180) #top (0,-10)
                transform_anchor True
                rotate 40
                parallel:
                    ease 2 xpos 20
                    pause .3
                    easeout .5 xpos 0
                    easeout 1 xpos 5
#                    pause .5
                    repeat
                parallel:
                    pause .1
                    ease 2 rotate 10
                    pause .3
                    ease .5 rotate 40
                    easein .9 rotate 35
#                    pause .4
                    repeat
        contains:
                #underside tit
                "Gwen_TJ_Tits_Under"
                subpixel True
                pos (0,100) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 200#200
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
                "Gwen_TJ_ZeroCock"
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
                #overside tit
                "Gwen_TJ_Tits_Over"
                subpixel True
                pos (0,100) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 200#200
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
                #bra stretch
                "Gwen_TJ_BraStretch"
                subpixel True
                pos (0,100) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 818)#(0.6, 700)
                xoffset 315#68
                yoffset -265#-271
                yzoom 1
#                alpha 0.7
                parallel:
                    ease 2 pos (10,130)
                    pause .3
                    ease .5 pos (0,100)
                    pause 1
                    repeat
                parallel:
                    ease 2 yzoom 1.2
                    pause .3
                    ease .5 yzoom 1
                    pause 1
                    repeat
        contains:
                #hands over everything
                "Gwen_TJ_Hands"
                subpixel True
                pos (0,100) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 200#200
                yoffset -271#125
                parallel:
                    ease 2 ypos 130
                    pause .3
                    ease .5 ypos 100
                    pause 1
                    repeat


## End Gwen TJ Pose 3 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



## Start 4 (cumming high) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
#image Gwen_TJ_4:
#        #Her Body in the TJ pose, cummming high
#        contains:
#                #jacket
#                "Gwen_TJ_Jacketback"
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
#                "Gwen_TJ_Braback"
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
#                "Gwen_TJ_Body"
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
#                "Gwen_TJ_Head"
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
#                "Gwen_TJ_ZeroCock"
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
#                    "Gwen_TJ_Tits"
#                subpixel True
#                pos (0,5) #top (0,-10)
#                transform_anchor True
#                parallel:
#                    pause .2
#                    ease 1.9 ypos -30
#                    pause .2
#                    ease 1.9 ypos 5
#                    repeat

## End Gwen TJ Pose 4 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start 5 (cumming low) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Gwen_TJ_5:
        #Her Body in the TJ pose, cumming low
        contains:
                #hair back
                "Gwen_BJ_HairBack"
                subpixel True
#                offset (90,-480)
                pos (0,180) #top (0,-10)
                transform_anchor True
                rotate 10
                parallel:
                    ease 2 ypos 190
                    pause .3
                    ease 1.5 ypos 180
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
                #base body  / / / / / / / / / / / / / / / / / / / /
                "Gwen_TJ_Body"
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
                "Gwen_BJ_Head"
                subpixel True
#                offset (90,-480)
                pos (0,180) #top (0,-10)
                transform_anchor True
                rotate 10
                parallel:
                    ease 2 ypos 190
                    pause .3
                    ease 1.5 ypos 180
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
                #underside tit
                "Gwen_TJ_Tits_Under"
                subpixel True
                pos (0,120) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 200#200
                yoffset -271#125
                parallel:
                    ease 2 ypos 130
                    pause .3
                    ease 1.5 ypos 120 #.5
                    pause .5
                    repeat
#                parallel:
#                    pause .1
#                    ease .8 yzoom .95
#                    pause 1.2
#                    ease 1.2 yzoom 1
#                    pause .8
#                    ease 0.6 yzoom .98
#                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Gwen_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                offset (0,50)#(5,50)
                rotate 0
#                parallel:
#                    pause .1
#                    ease 2 rotate 3
#                    pause .3
#                    ease .5 rotate 0
#                    pause .9
#                    repeat
        contains:
                #overside tit
                "Gwen_TJ_Tits_Over"
                subpixel True
                pos (0,120) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 200#200
                yoffset -271#125
                yzoom 1
                parallel:
                    ease 2 ypos 130
                    pause .3
                    ease 1.5 ypos 120 #.5
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
                #bra stretch
                "Gwen_TJ_BraStretch"
                subpixel True
                pos (-5,120) #top (-70,-210)
                transform_anchor True
                anchor (0.6, 818)#(0.6, 700)
                xoffset 315#68
                yoffset -265#-271
                yzoom 1.2
#                alpha 0.7
                parallel:
                    ease 2 pos (-5,130)
                    pause .3
                    ease 1.5 pos (-5,120)
                    pause .5
                    repeat
                parallel:
                    ease 2 yzoom 1.21
                    pause .3
                    ease 1.5 yzoom 1.18
                    pause .5
                    repeat
        contains:
                #hands over everything
                "Gwen_TJ_Hands"
                subpixel True
                pos (0,120) #top (0,-15)
                transform_anchor True
                anchor (0.6, 700)#(0.6, 562)
                xoffset 200#200
                yoffset -271#125
                parallel:
                    ease 2 ypos 130
                    pause .3
                    ease 1.5 ypos 120 #.5
                    pause .5
                    repeat

# End Gwen TJ Pose 5 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

## Gwen's TJ animations end / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Gwen_TJ_Launch(Line = Trigger):    # The sequence to launch the Gwen Titfuck animations
    if renpy.showing("Gwen_TJ_Animation"):
        return

    if Line == "L": # Gwen gets started. . .
            if Taboo:
                if len(Present) >= 2:
                    if Present[0] != GwenX:
                            "[GwenX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                    elif Present[1] != GwenX:
                            "[GwenX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
                else:
                            "[GwenX.Name] небрежно глядывается по сторонам, чтобы убедиться, что никто не наблюдает."
#            "[GwenX.Name] bends over and places your cock between her breasts."
    if GwenX.Chest == "suit" and not GwenX.Uptop:
        $ GwenX.Uptop = 1
        "Она слегка расстегивает свой костюм."
#    if GwenX.Chest and GwenX.Over:
#        "She throws off her [GwenX.Over] and her [GwenX.Chest]."
#    elif GwenX.Over:
#        "She throws off her [GwenX.Over], baring her breasts underneath."
#    elif GwenX.Chest:
#        "She tugs off her [GwenX.Chest] and throws it aside."
#    $ GwenX.Over = 0
#    $ GwenX.Chest = 0
#    $ GwenX.ArmPose = 0
    call Girl_First_Topless(GwenX)

    show blackscreen onlayer black with dissolve

    if renpy.showing("Gwen_BJ_Animation"):
            hide Gwen_BJ_Animation
    else:
            call Girl_Hide(GwenX)
            show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) zorder 150:
                alpha 1
                ease 1 zoom 2.3 xpos 750 yoffset -100
            show Gwen_Sprite:
                alpha 0

#    if GwenX.Over == "towel" or GwenX.Chest == "corset": #pulls top down because these tops are incompatible with TJ.
#        $ GwenX.Uptop = 1

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "titjob"
    show Gwen_TJ_Animation zorder 150:
        pos (1000,1050)#(1000,1000)#(700,520)
    $ Player.Sprite = 1
    hide blackscreen onlayer black with dissolve
    return

label Gwen_TJ_Reset:
    # The sequence to the Gwen animations from Titfuck to default
    if not renpy.showing("Gwen_TJ_Animation"):
        return
#    hide Gwen_TJ_Animation
    call Girl_Hide(GwenX)
    $ Player.Sprite = 0

    show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) zorder 150:
        zoom 2.3 xpos 750 yoffset -100
    show Gwen_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 xpos 700 yoffset 50
        pause .5
        ease .5 zoom 1 xpos GwenX.SpriteLoc yoffset 0
    "[GwenX.Name] отстраняется"
    show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) zorder GwenX.Layer:
        alpha 1 zoom 1 offset (0,0) xpos GwenX.SpriteLoc
    return

# End Gwen TJ Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Gwen Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Gwen Handjob element //////////////////////////////////////////////////////////////////////

image Gwen_HJ_Body:
    "Gwen_Sprite"
    pos (780,-1250)#(680,-1250)
    zoom 4.8#2.15


transform Gwen_HJ_Body_1():
    subpixel True
#    pos (700,-1250)#(350,-550)
    block:
        ease .5 ypos -1220
        pause 0.25
        ease 1.0 ypos -1250
        pause 0.1
        repeat

transform Gwen_HJ_Body_2():
    subpixel True
#    pos (350,-550)
    block:
        ease 0.2 ypos -1240
        pause 0.1
        ease 0.4 ypos -1250
        pause 0.1
        repeat

image Gwen_Hand_Under:
    "images/GwenSprite/[GwenX.skin_image.skin_path]handgwen2.png"
    anchor (0.5,0.5)
    pos (-10,0)


image Gwen_Hand_Over:
    "images/GwenSprite/[GwenX.skin_image.skin_path]handgwen1.png"
    anchor (0.5,0.5)
    pos (-10,0)

transform Gwen_Hand_1():
    subpixel True
    pos (-20,-100)
    rotate 5
    block:
        ease .5 pos (-20,150) rotate -5 #ypos 150 rotate 5 Bottom
        pause 0.25
        ease 1.0 pos (-20,-100) rotate 5 #(-20,-100) #rotate -10#  Top
        pause 0.1
        repeat

transform Gwen_Hand_2():
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

image Gwen_HJ_Animation:
    contains:
        ConditionSwitch(
            # backside of the hand
            "not Speed", Transform("Gwen_HJ_Body"),
            "Speed == 1", At("Gwen_HJ_Body", Gwen_HJ_Body_1()),
            "Speed >= 2", At("Gwen_HJ_Body", Gwen_HJ_Body_2()),
            "Speed", Null(),
            ),
    contains:
        ConditionSwitch(
            # backside of the hand
            "not Speed", Transform("Gwen_Hand_Under"),
            "Speed == 1", At("Gwen_Hand_Under", Gwen_Hand_1()),
            "Speed >= 2", At("Gwen_Hand_Under", Gwen_Hand_2()),
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
            "not Speed", Transform("Gwen_Hand_Over"),
            "Speed == 1", At("Gwen_Hand_Over", Gwen_Hand_1()),
            "Speed >= 2", At("Gwen_Hand_Over", Gwen_Hand_2()),
            "Speed", Null(),
            ),
    anchor (0.51, -1.3)
#    xzoom -0.4#0.6
    zoom 0.4#0.6


label Gwen_HJ_Launch(Line = Trigger):
    if renpy.showing("Gwen_HJ_Animation"):
        $ Trigger = "hand"
        return
    if not Player.Male:
        call Gwen_Finger_Launch
        return
    call Girl_Hide(GwenX)
    $ GwenX.ArmPose = 2
    if Line == "L":
        show Gwen_Sprite at SpriteLoc(StageRight) zorder 150:
            alpha 1
            ease 1 zoom 1.7 offset (50,200)#(0,200)
    else:
        show Gwen_Sprite at SpriteLoc(StageRight) zorder 150:
            alpha 1
            ease 1 zoom 1.9 offset (50,150)#(150,150)
        with dissolve

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    else:
        $ Speed = 1
    pause .5
    show Gwen_Sprite:
        alpha 0
    show Gwen_HJ_Animation at SpriteLoc(StageCenter) zorder 150 with fade:
        #xoffset 150
        offset (150,250)#(250,250)
    return

label Gwen_HJ_Reset: # The sequence to the Gwen animations from handjob to default
    if not renpy.showing("Gwen_HJ_Animation"):
        return
    $ Speed = 0
    hide Gwen_HJ_Animation with dissolve
    call Girl_Hide(GwenX)
    show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 1.5 offset (-250,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) zorder GwenX.Layer:
        alpha 1 zoom 1 offset (0,0)
#    $ GwenX.ArmPose = 1
    return

# End Gwen Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# Core Gwen CUN element ///////////////////////////////////////////////////////////////////////////                                     Core Gwen CUN element
#Gwen CUN Over Sprite Compositing

image Gwen_CUN_Animation: #core CUN animation
    LiveComposite(
        (787,913),
        (0,0), ConditionSwitch(                                                                 # back of the hair, which needs to go behind the body
            "Speed == 0",  "Gwen_CUN_Anim_Static",
            "Speed == 1",  "Gwen_CUN_Anim_Licking1",
            "Speed == 2",  "Gwen_CUN_Anim_Licking2",
            "Speed >= 3",  "Gwen_CUN_Anim_Licking3",
            "Speed == 4",  "Gwen_CUN_Anim_Licking1",
            "True", "Gwen_CUN_Anim_Static",
            ),
        )
    zoom .55
    anchor (.5,.5)

image Gwen_CUN_Anim_Static:
    #Animation for licking speed 1
    contains:
        #hair
        "Gwen_BJ_HairBack"
        subpixel True
        zoom 1.4
        pos (-50,570)
        offset (70,0)#(-10,0)
        rotate 20
        block:
            ease 2 yoffset 10
            ease 2 yoffset 0
            repeat
    contains:
        #body 2
        "Gwen_BJ_Backdrop"
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
        "Gwen_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.4
        pos (-50,570)
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


image Gwen_CUN_Anim_Licking1:
    #Animation for licking speed 1
    contains:
        #hair
        "Gwen_BJ_HairBack"
        subpixel True
        zoom 1.4
        pos (-50,570)
        offset (40,40)#490)
        rotate 10
        block: #5s total
            ease 2.5 offset (45,100) #bottom (0,75)
            easeout 1.5 offset (45,60)  #top (0,60)
            ease .5 offset (40,20)  #top
            ease .5 offset (42,30)  #top
            repeat
    contains:
        #body 2
        "Gwen_BJ_Backdrop"#"Gwen_Sprite"
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
        "Gwen_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.4
        pos (-50,570)
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
#End Gwen Licking 1

image Gwen_CUN_Anim_Licking2:
    #Animation for licking speed 2
    contains:
        #hair
        "Gwen_BJ_HairBack"
        subpixel True
        zoom 1.4
        pos (-50,570)
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
        "Gwen_BJ_Backdrop"
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
        "Gwen_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.4
        pos (-50,570)
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
#End Gwen Licking 2

image Gwen_CUN_Anim_Licking3:
    #Animation for licking speed 3
    contains:
        #hair
        "Gwen_BJ_HairBack"
        subpixel True
        zoom 1.4
        pos (-50,570)
        offset (20,110)#490)
        block: #2s total
            ease .5 offset (20,130) #bottom
            ease .5 offset (20,110)  #top -35)
            repeat
    contains:
        #body 2
        "Gwen_BJ_Backdrop"
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
        "Gwen_BJ_Head"#"BJ_Head"
        subpixel True
        zoom 1.4
        pos (-50,570)
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
#End Gwen Licking 3

#CUN Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Gwen_CUN_Launch(Line = Trigger):
    # The sequence to launch the Gwen CUN animations
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    return
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
    if renpy.showing("Gwen_CUN_Animation"):
        return

    if Player.Male == 1:
        call Gwen_BJ_Launch
        return


    call Girl_Hide(GwenX)
    if Line == "L" or Line == "cum":
        show Gwen_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1
            ease 1 zoom 2.5 offset (70,240) #(-90,140) offset (150,80)
        with dissolve
    else:
        show Gwen_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1 zoom 2.5 offset (70,240) #(-90,140)
        with dissolve

    if Taboo and Line == "L":
            # Gwen gets started. . .
            if len(Present) >= 2:
                if Present[0] != GwenX:
                        "[GwenX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                elif Present[1] != GwenX:
                        "[GwenX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
            else:
                        "[GwenX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
    $ Speed = 1
    if Line == "L":
            if not GwenX.Blow:
                "[GwenX.Name] нерешительно стягивает с вас штаны и касается своим ртом вашей киски."
            else:
                "[GwenX.Name] наклоняется и начинает лизать вашу киску."

    if Line != "cum":
        $ Trigger = "cun"

    show Gwen_Sprite:
        alpha 0
    show Gwen_CUN_Animation zorder 150:
        pos (800,830)#(645,610)
    return

label Gwen_CUN_Reset: # The sequence to the Gwen animations from CUN to default
    if not renpy.showing("Gwen_CUN_Animation"):
        return
    hide Gwen_CUN_Animation
    call Girl_Hide(GwenX)
    $ Speed = 0

    show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) zorder 150:
        zoom 2 offset (70,140) alpha 1
        pause .5
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) zorder GwenX.Layer:
        alpha 1 zoom 1 offset (0,0)
    $ GwenX.FaceChange("sexy")
    return

#End Gwen Cunnilingus Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

image Gwen_Finger_Animation:
    # Core Animation for Fingering Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
        ConditionSwitch(                                                # backside of the hand
            "Speed == 1", "Gwen_Finger_1",
            "Speed >= 2", "Gwen_Finger_2",
            "True", "Gwen_Finger_0",
            ),
    anchor (0.5,0.5)#anchor (0.51, -1.3)
    offset (400,945)#700,1190
    zoom 0.8
    # end Core Animation for Fingering Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <

image Gwen_Finger_0:
    # Animation for Fingering Zero's pussy, static < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Gwen_Sprite"
            pos (350,-550)
            zoom 2.15
    contains:
            ConditionSwitch(
                "Player.Wet", "GwenBJFace/Gwen_Fingering_wet.png",
                "True", "GwenBJFace/[GwenX.skin_image.skin_path]Gwen_Fingering_Under.png",
                )
            anchor (0.5,0.6)
            pos (20,50)

#            "Gwen_Finger_Under"
    contains:
            "Zero_Pussy"
    contains:
            "GwenBJFace/[GwenX.skin_image.skin_path]Gwen_Fingering_Over.png"
            anchor (0.5,0.6)
            pos (20,50)
#            "Gwen_Finger_Over"
    # end Animation for Fingering Zero's pussy, static < < < < < < < < < < < < < < < < < < < < < < < <

image Gwen_Finger_1:
    # Animation for Fingering Zero's pussy, slow < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Gwen_Sprite"
            pos (350,-550)
            zoom 2.15
            block:
                ease 0.5 ypos -540 #rotate 3   100
                pause 0.25
                ease 1.0 ypos -550 #rotate -3  40
                repeat
    contains:
            ConditionSwitch(
                "Player.Wet", "GwenBJFace/Gwen_Fingering_wet.png",
                "True", "GwenBJFace/[GwenX.skin_image.skin_path]Gwen_Fingering_Under.png",
                )
            subpixel True
        #    xpos 10
            anchor (0.5,0.6)
            transform_anchor True
            pos (15,40)
            rotate -5
            block:
                ease .5 pos (10,115) rotate 0 #(40,65)   Bottom
                pause 0.25
                ease 1.0 pos (15,40) rotate -5 #(40,0) Top                 pause 0.1
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
            "GwenBJFace/[GwenX.skin_image.skin_path]Gwen_Fingering_Over.png"
#            "Gwen_Finger_Over"
            subpixel True
        #    xpos 10
            anchor (0.5,0.6)
            transform_anchor True
            pos (15,40)
            rotate -5
            block:
                ease .5 pos (10,115) rotate 0 #(40,65)   Bottom
                pause 0.25
                ease 1.0 pos (15,40) rotate -5 #(40,0) Top                 pause 0.1
                repeat
    # end Animation for Fingering Zero's pussy, slow < < < < < < < < < < < < < < < < < < < < < < < <

image Gwen_Finger_2:
    # Animation for Fingering Zero's pussy, fast < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Gwen_Sprite"
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
                "Player.Wet", "GwenBJFace/Gwen_Fingering_wet.png",
                "True", "GwenBJFace/[GwenX.skin_image.skin_path]Gwen_Fingering_Under.png",
                )
            subpixel True
            anchor (0.5,0.6)
            transform_anchor True
#            rotate -15
            pos (10,30)
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
            "GwenBJFace/[GwenX.skin_image.skin_path]Gwen_Fingering_Over.png"
#            "Gwen_Finger_Over"
            subpixel True
            anchor (0.5,0.6)
            transform_anchor True
#            rotate -15
            pos (10,30)
            block:
                ease 0.15 ypos 125 #rotate 3   65
                pause 0.1
                ease 0.45 ypos 60 #rotate -3  30
                pause 0.1
                repeat
    # end Animation for Fingering Zero's pussy, fast < < < < < < < < < < < < < < < < < < < < < < < <

label Gwen_Finger_Launch(Line = Trigger):
    if renpy.showing("Gwen_Finger_Animation"):
        $ Trigger = "finger"
        return

    if Player.Male == 1:
        call Gwen_HJ_Launch
        return

    call Girl_Hide(GwenX)
    $ GwenX.Arms = 0
    $ GwenX.ArmPose = 2
    if not renpy.showing("Gwen_Sprite"):
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) zorder 150:
            alpha 1 zoom 1.7 xpos 850 yoffset 200 #offset (-50,200)
        with dissolve
    show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 1.7 xpos 850 yoffset 200 #offset (-50,200)

    if Taboo and Line == "L":
        # Gwen gets started. . .
        if len(Present) >= 2:
            if Present[0] != GwenX:
                    "[GwenX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
            elif Present[1] != GwenX:
                    "[GwenX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
        else:
                    "[GwenX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
        if not GwenX.Hand and GwenX.Arms:
            "Когда вы стягиваете свои штаны, [GwenX.Name] снимает перчатки и нерешительно тянется к вашей киске. Затем она начинает грубо ласкать ее."
        else:
            "Затем она наклоняется и хватает ваш член."
    elif Line == "L":
        if not GwenX.Hand and GwenX.Arms:
            "Когда вы стягиваете свои штаны, [GwenX.Name] снимает перчатки и нерешительно тянется к вашей киске. Затем она начинает грубо ласкать ее."
        else:
            "[GwenX.Name] наклоняется и кладет руку вам на киску."
    else:
            "[GwenX.Name] наклоняется и кладет руку вам на киску."

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "finger"
    show Gwen_Sprite:
        alpha 0
    show Gwen_Finger_Animation at SpriteLoc(GwenX.SpriteLoc) zorder 150 with fade
    return

label Gwen_Finger_Reset: # The sequence to the Gwen animations from handjob to default
    if not renpy.showing("Gwen_Finger_Animation"):
        return
    $ Speed = 0
    hide Gwen_Finger_Animation
    with dissolve
    call Girl_Hide(GwenX)
#    show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) zorder GwenX.Layer:
#        alpha 1
#        zoom 1.7  xpos 850 yoffset 200
    show Gwen_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 yoffset 50
        pause .5
        ease .5 zoom 1 xpos GwenX.SpriteLoc yoffset 0
    show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) zorder GwenX.Layer:
        alpha 1 zoom 1 xpos GwenX.SpriteLoc yoffset 0
    return

# Start Gwen Scissor Pose content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen_SC_Sprite:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
                #if the top's down. . .
                "Speed >= 2", "Gwen_SC_Anim_2",
                "Speed", "Gwen_SC_Anim_1",
                "True", "Gwen_SC_Anim_0",
                ),
        )
    align (0.6,0.0)
    pos (650,300)#(650,200)(925,740)#(910,850)
    zoom 0.85#0.8

# End Gwen Sex Pose Speed 2 Scissor / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Gwen Sex Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Gwen_SC_Body:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Gwen_SexSprite
        (1120,840),
        (45,-325), "Gwen_HairBack_SC",
#        (0,0), ConditionSwitch(
#            #shirt under layer
#            "GwenX.Over == 'red shirt' and GwenX.Uptop", "images/GwenSex/Gwen_Sex_Over_Red_Back.png",
#            "GwenX.Over == 'black shirt' and GwenX.Uptop", "images/GwenSex/Gwen_Sex_Over_Black_Back.png",
#            "True", Null(),
#            ),
        (0,0), "images/GwenSex/[GwenX.skin_image.skin_path]Gwen_Sex_Body.png",
#        (0,0), "images/GwenSex/Gwen_Sex_Headref.png",

        (0,0), ConditionSwitch(
            #shirt layer under open bra
            "(GwenX.Over == 'suit' and GwenX.Uptop) or GwenX.Over == 'open suit'", "images/GwenSex/Gwen_Sex_Over_Suit_Under.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #bra layer
            "not GwenX.Chest", Null(),
            "GwenX.Uptop", ConditionSwitch(
                    #if top's up
                    "GwenX.Chest == 'tank'", Recolor("Gwen", "Chest", "images/GwenSex/Gwen_Sex_Chest_Tank_Up.png"),
                    "GwenX.Chest == 'bikini top'", Recolor("Gwen", "Chest", "images/GwenSex/Gwen_Sex_Chest_Bikini_Up.png"),
                    "GwenX.Chest == 'bra'", Recolor("Gwen", "Chest", "images/GwenSex/Gwen_Sex_Chest_Bra_Up.png"),
                    "GwenX.Chest == 'lace bra'", Recolor("Gwen", "Chest", "images/GwenSex/Gwen_Sex_Chest_Bra_Up.png"),
                    "True", Null(),
                    ),
            #if the top's down. . .
            "GwenX.Chest == 'tank'", Recolor("Gwen", "Chest", "images/GwenSex/Gwen_Sex_Chest_Tank.png"),
            "GwenX.Chest == 'bikini top'", Recolor("Gwen", "Chest", "images/GwenSex/Gwen_Sex_Chest_Bikini.png"),
            "GwenX.Chest == 'bra' and GwenX.Over == 'open suit'", Recolor("Gwen", "Chest", "images/GwenSex/Gwen_Sex_Chest_Bra_Suit.png"),
            "GwenX.Chest == 'bra'", Recolor("Gwen", "Chest", "images/GwenSex/Gwen_Sex_Chest_Bra.png"),
            "GwenX.Chest == 'lace bra' and GwenX.Over == 'open suit'", Recolor("Gwen", "Chest", "images/GwenSex/Gwen_Sex_Chest_Lace_Suit.png"),
            "GwenX.Chest == 'lace bra'", Recolor("Gwen", "Chest", "images/GwenSex/Gwen_Sex_Chest_Lace.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "GwenX.Water", "images/GwenSex/Gwen_Sex_Water_Body.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #shirt layer
            "(GwenX.Over == 'suit' and GwenX.Uptop) or GwenX.Over == 'open suit'", "images/GwenSex/Gwen_Sex_Over_Suit_Up.png",
            "GwenX.Over == 'tshirt' and GwenX.Uptop", Recolor("Gwen", "Over", "images/GwenSex/Gwen_Sex_Over_Tshirt_Up.png"),
            "GwenX.Over == 'cheer top' and GwenX.Uptop", Recolor("Gwen", "Over", "images/GwenSex/Gwen_Sex_Over_Cheer_Up.png"),
            "GwenX.Over == 'suit'", "images/GwenSex/Gwen_Sex_Over_Suit.png",
            "GwenX.Over == 'tshirt'", Recolor("Gwen", "Over", "images/GwenSex/Gwen_Sex_Over_Tshirt.png"),
            "GwenX.Over == 'cheer top'", Recolor("Gwen", "Over", "images/GwenSex/Gwen_Sex_Over_Cheer.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #piercings
            "not GwenX.Pierce", Null(),
            "GwenX.Uptop", ConditionSwitch(
                    #if the top's down. . .
                    "GwenX.Pierce == 'ring'", "images/GwenSex/Gwen_Sex_Pierce_Tits_R.png",
                    "GwenX.Pierce", "images/GwenSex/Gwen_Sex_Pierce_Tits_B.png",
                    "True", Null(),
                    ),
            "GwenX.Pierce == 'ring'", ConditionSwitch(
                    # ring pierce
                    "GwenX.Over == 'suit'", "images/GwenSex/Gwen_Sex_Pierce_Tits_R_Pink.png",
                    "GwenX.Over == 'tshirt'", "images/GwenSex/Gwen_Sex_Pierce_Tits_R_White.png",
                    "GwenX.Over == 'cheer top'", "images/GwenSex/Gwen_Sex_Pierce_Tits_R_Cheer.png",

                    "GwenX.Chest == 'bikini top'", "images/GwenSex/Gwen_Sex_Pierce_Tits_R_Pink.png",
                    "GwenX.Chest == 'lace bra'", "images/GwenSex/Gwen_Sex_Pierce_Tits_R_Lace.png",
                    "GwenX.Chest == 'tank' or GwenX.Chest == 'bra'", "images/GwenSex/Gwen_Sex_Pierce_Tits_R_White.png",

                    "True", "images/GwenSex/Gwen_Sex_Pierce_Tits_R.png",
                    ),
            "GwenX.Over == 'suit'", "images/GwenSex/Gwen_Sex_Pierce_Tits_B_Pink.png",
            "GwenX.Over == 'tshirt' or GwenX.Over == 'cheer top'", "images/GwenSex/Gwen_Sex_Pierce_Tits_B_White.png",

            "GwenX.Chest == 'bikini top'", "images/GwenSex/Gwen_Sex_Pierce_Tits_B_Pink.png",
            "GwenX.Chest == 'lace bra'", "images/GwenSex/Gwen_Sex_Pierce_Tits_B_Lace.png",
            "GwenX.Chest == 'tank' or GwenX.Chest == 'bra'", "images/GwenSex/Gwen_Sex_Pierce_Tits_B_White.png",

            "True", "images/GwenSex/Gwen_Sex_Pierce_Tits_B.png",
            ),

        (45,-325), "Gwen_Head_SC",  #(0,-300)
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'belly' in GwenX.Spunk and Player.Male", "images/GwenSex/Gwen_Sex_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'tits' in GwenX.Spunk and Player.Male", "images/GwenSex/Gwen_Sex_Spunk_Tits.png",
            "True", Null(),
            ),
#        (0,0), "images/GwenSex/Gwen_Sex_HeadRef.png",
        )
#    yoffset -163
# End Gwen Sex Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Gwen_Head_SC:
    # The head used for the sex pose, referenced by Gwen_Sex_Body
    "Gwen_Sprite_Head"
    zoom 1.24#1.36
    anchor (0.5,0.5)
    rotate -10#17
#    alpha 0.5

image Gwen_HairBack_SC:
    # The hair behind the head for the sex pose, referenced by Gwen_Sex_Body
    "Gwen_Sprite_HairBack"
    zoom 1.24#1.36
    anchor (0.5,0.5)
    rotate -10#17

# Start Gwen Sex Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Gwen_SC_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Gwen_SexSprite
        (1120,880),
#        (545,540), ConditionSwitch(    #165,560
#            #Personal Wetness
#            "not GwenX.Wet", Null(),
#            "(GwenX.Legs == 'pants' or GwenX.Legs == 'shorts') and not GwenX.Upskirt", Null(),
#            "GwenX.Panties and not GwenX.PantiesDown", Null(),
#            "GwenX.Wet == 1", "Wet_Drip",
#            "True", "Wet_Drip2",
#            ),

#        (545,540), ConditionSwitch(    #205,530
#            #Spunk
#            "'anal' not in GwenX.Spunk or not Player.Male", Null(),
#            "(GwenX.Legs == 'pants' or GwenX.Legs == 'shorts') and not GwenX.Upskirt", Null(),
#            "GwenX.Wet == 1", "Spunk_Drip",
#            "True", "Spunk_Drip2",
#            ),

        (0,0), ConditionSwitch(
            #torso under legs
            "GwenX.Over == 'suit' and not GwenX.Uptop", "images/GwenSex/Gwen_Sex_UnderLegs.png",
            "GwenX.Hose == 'garterbelt' or GwenX.Hose == 'stockings and garterbelt'", "images/GwenSex/Gwen_Sex_UnderLegs.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Legs
            "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/GwenSex/[GwenX.skin_image.skin_path]Gwen_Sex_FBase.png",
            "Player.Sprite and Player.Cock == 'in' and Speed", "images/GwenSex/[GwenX.skin_image.skin_path]Gwen_Sex_FBase.png",
#            "Player.Sprite and Player.Cock == 'in' and Speed", "Gwen_Sex_Heading_Pussy",
#            "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/GwenSex/[GwenX.skin_image.skin_path]Gwen_Sex_Ass.png",
#            "Trigger == 'lick pussy'", "images/GwenSex/[GwenX.skin_image.skin_path]Gwen_Sex_Ass.png",
            "True", "images/GwenSex/[GwenX.skin_image.skin_path]Gwen_Sex_Ass.png",
            ),

        (0,0), ConditionSwitch(
            "Player.Sprite and Player.Cock == 'anal'", "images/GwenSex/[GwenX.skin_image.skin_path]Gwen_Sex_Anus_Cover.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Wet look
            "not GwenX.Water", Null(),
            "True", "images/GwenSex/Gwen_Sex_Water_Legs.png",
            ),

#        (0,-10), "Gwen_Sex_Anus",
            #Anus Composite

        (0,0), "Gwen_SC_Pussy",
            #Pussy Composite


        (0,0), ConditionSwitch(
            #hose layer
            "GwenX.Hose == 'socks'", Recolor("Gwen", "Hose", "images/GwenSex/Gwen_Sex_Hose_Socks.png"),
            "GwenX.Hose == 'stockings and garterbelt'", Recolor("Gwen", "Hose", "images/GwenSex/Gwen_Sex_Hose_StockingsGarter.png"),
            "GwenX.Hose == 'garterbelt'", Recolor("Gwen", "Hose", "images/GwenSex/Gwen_Sex_Hose_Garter.png"),
            "GwenX.Hose == 'stockings'", Recolor("Gwen", "Hose", "images/GwenSex/Gwen_Sex_Hose_Stockings.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Panties if up
            "GwenX.PantiesDown", Null(),
            "GwenX.Panties == 'lace panties'", Recolor("Gwen", "Panties", "images/GwenSex/Gwen_Sex_Panties_Lace.png"),
            "GwenX.Panties == 'bikini bottoms'", Recolor("Gwen", "Panties", "images/GwenSex/Gwen_Sex_Panties_Bikini.png"),
            "GwenX.Panties and GwenX.Wet", Recolor("Gwen", "Panties", "images/GwenSex/Gwen_Sex_Panties_White_Wet.png"),
            "GwenX.Panties", Recolor("Gwen", "Panties", "images/GwenSex/Gwen_Sex_Panties_White.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Piercings under hose
            "not GwenX.Pierce", Null(),
            "GwenX.Pierce == 'ring'",ConditionSwitch(
                    #If she has panties down. . .
                    "Player.Sprite and Player.Cock == 'in'", "images/GwenSex/Gwen_Sex_Pierce_Pussy_R_Fucking.png",
                    "not GwenX.Panties or GwenX.PantiesDown", "images/GwenSex/Gwen_Sex_Pierce_Pussy_R.png",
                    "GwenX.Panties == 'lace panties' and not GwenX.PantiesDown", "images/GwenSex/Gwen_Sex_Pierce_Pussy_R_Lace.png",
#                    "GwenX.Panties == 'bikini bottoms' and not GwenX.PantiesDown", "images/GwenSex/Gwen_Sex_Pierce_Pussy_R_White.png",
                    "True", "images/GwenSex/Gwen_Sex_Pierce_Pussy_R_White.png",
                    ),
            #else, it's barbell
            "not GwenX.Panties or GwenX.PantiesDown", "images/GwenSex/Gwen_Sex_Pierce_Pussy_B.png",
            "GwenX.Panties == 'lace panties' and not GwenX.PantiesDown", "images/GwenSex/Gwen_Sex_Pierce_Pussy_B_Lace.png",
#            "GwenX.Panties == 'bikini bottoms' and not GwenX.PantiesDown", "images/GwenSex/Gwen_Sex_Pierce_Pussy_B_White.png",
            "True", "images/GwenSex/Gwen_Sex_Pierce_Pussy_B_White.png",
            ),
        (0,0), ConditionSwitch(
            #pantyhose layer
            "GwenX.Panties and GwenX.PantiesDown", Null(),
            "GwenX.Hose == 'tights'", Recolor("Gwen", "Hose", "images/GwenSex/Gwen_Sex_Hose_Tights.png"),
            "GwenX.Hose == 'ripped tights'", Recolor("Gwen", "Hose", "images/GwenSex/Gwen_Sex_Hose_Tights_Holed.png"),
            "GwenX.Hose == 'pantyhose'", Recolor("Gwen", "Hose", "images/GwenSex/Gwen_Sex_Hose_Pantyhose.png"),
            "GwenX.Hose == 'ripped pantyhose'", Recolor("Gwen", "Hose", "images/GwenSex/Gwen_Sex_Hose_Pantyhose_Holed.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Suit top over legs
            "GwenX.Over == 'suit' and not GwenX.Uptop", "images/GwenSex/Gwen_Sex_Over_Suit_Waist.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs Layer
            "GwenX.Legs == 'skirt' and GwenX.Upskirt", Recolor("Gwen", "Legs", "images/GwenSex/Gwen_Sex_Legs_Skirt_Up.png"),
            "GwenX.Legs == 'skirt'", Recolor("Gwen", "Legs", "images/GwenSex/Gwen_Sex_Legs_Skirt.png"),
            "GwenX.Legs == 'cheer skirt' and GwenX.Upskirt", Recolor("Gwen", "Legs", "images/GwenSex/Gwen_Sex_Legs_Cheer_Up.png"),
            "GwenX.Legs == 'cheer skirt'", Recolor("Gwen", "Legs", "images/GwenSex/Gwen_Sex_Legs_Cheer.png"),

            "GwenX.Upskirt", Null(),
#            "GwenX.Legs == 'skirt'", Recolor("Gwen", "Legs", "images/GwenSex/Gwen_Sex_Legs_Skirt.png"),
            "GwenX.Legs == 'shorts' and GwenX.Wet > 1", Recolor("Gwen", "Legs", "images/GwenSex/Gwen_Sex_Legs_Shorts_Wet.png"),
            "GwenX.Legs == 'shorts'", Recolor("Gwen", "Legs", "images/GwenSex/Gwen_Sex_Legs_Shorts.png"),
            "GwenX.Legs == 'suit' and GwenX.Wet > 1", "images/GwenSex/Gwen_Sex_Legs_Suit_Wet.png",
            "GwenX.Legs == 'suit'", "images/GwenSex/Gwen_Sex_Legs_Suit.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Piercings over pants and pantyhose
            "not GwenX.Pierce", Null(),
            "(GwenX.Legs == 'skirt' or GwenX.Legs == 'cheer skirt') and not GwenX.Upskirt", Null(),
            "GwenX.Pierce == 'ring'",ConditionSwitch(
                    #If she has panties down. . .
                    "GwenX.Legs == 'shorts' and not GwenX.Upskirt", "images/GwenSex/Gwen_Sex_Pierce_Pussy_R_Pink.png",
                    "GwenX.Legs == 'suit' and not GwenX.Upskirt", "images/GwenSex/Gwen_Sex_Pierce_Pussy_R_WhiteLine.png",
                    "GwenX.Panties and GwenX.PantiesDown", Null(),
                    "GwenX.Hose == 'tights'", "images/GwenSex/Gwen_Sex_Pierce_Pussy_R_Tights.png",
                    "True", Null(),
                    ),
            #else, it's barbell
            "GwenX.Legs == 'shorts' and not GwenX.Upskirt", "images/GwenSex/Gwen_Sex_Pierce_Pussy_B_Pink.png",
            "GwenX.Legs == 'suit' and not GwenX.Upskirt", "images/GwenSex/Gwen_Sex_Pierce_Pussy_B_WhiteLine.png",
            "GwenX.Legs == 'pants' and not GwenX.Upskirt", "images/GwenSex/Gwen_Sex_Pierce_Pussy_B_White.png",
            "GwenX.Panties and GwenX.PantiesDown", Null(),
            "GwenX.Hose == 'tights'", "images/GwenSex/Gwen_Sex_Pierce_Pussy_B_Tights.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy'", "Gwen_Sex_Lick_Pussy",
            "Trigger == 'lick ass'", "Gwen_Sex_Lick_Ass",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy fondling animation
            "GwenX.Offhand == 'fondle pussy' and GwenX.Lust > 60 and not (Player.Sprite)",  At("GwenFingerHand", GirlFingerPussyX()), #"Gwen_Sex_Mast2",
            "GwenX.Offhand == 'fondle pussy'", At("GwenMastHand", GirlGropePussyX()), #"Gwen_Sex_Mast",
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Gwen_Sex_Fondle_Pussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Footjob overlay
            "Player.Cock == 'foot'", Null(),
            "renpy.showing('Anal_Plug_In_Sex') or renpy.showing('Anal_Plug_Out_Sex')",AlphaMask("Gwen_Sex_Feet", "images/GwenSex/Gwen_Sex_Feet_Mask.png"),
            "ShowFeet", "Gwen_Sex_Feet",
#            "Player.Sprite", AlphaMask("Gwen_Sex_Feet", "images/GwenSex/Gwen_Sex_Feet_Mask.png"),
#            "Trigger == 'lick pussy'", AlphaMask("Gwen_Sex_Feet", "images/GwenSex/Gwen_Sex_Feet_Mask.png"),
#            "Trigger == 'lick ass'", AlphaMask("Gwen_Sex_Feet", "images/GwenSex/Gwen_Sex_Feet_Mask.png"),
            "True", AlphaMask("Gwen_Sex_Feet", "images/GwenSex/Gwen_Sex_Feet_Mask.png"),
            ),

#        (0,0), ConditionSwitch(                                                                                 #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
#            "not Speed", "Gwen_Sex_Feet",
#            "Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Gwen_Sex_Feet", "images/GwenSex/Gwen_Sex_FeetMask.png"),
#            "True", "Gwen_Sex_Feet",
#            ),
        )
# End Gwen Sex Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Gwen Sex Pose Pussy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Gwen_SC_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).
    contains:
            # The background plate of her pussy
            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/GwenSex/Gwen_Sex_Pussy_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed", "Gwen_Sex_Heading_Pussy",
#                "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/GwenSex/Gwen_Sex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/GwenSex/Gwen_Sex_Pussy_Open.png",
                "GwenX.Offhand == 'fondle pussy' and GwenX.Lust > 60", "images/GwenSex/Gwen_Sex_Pussy_Open.png",
                "True", "images/GwenSex/Gwen_Sex_Pussy_Closed.png",
                )
    contains:
            # pubes
            ConditionSwitch(
                "not GwenX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", Recolor("Gwen", "Pubes", "images/GwenSex/Gwen_Sex_Pubes_Fucking.png"),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 1", Recolor("Gwen", "Pubes", "images/GwenSex/Gwen_Sex_Pubes_Fucking.png"),
#                "Player.Sprite and Player.Cock == 'in'", Recolor("Gwen", "Pubes", "images/GwenSex/Gwen_Sex_Pubes_Open.png"),
#                "Player.Sprite and Player.Cock == 'out'", Recolor("Gwen", "Pubes", "images/GwenSex/Gwen_Sex_Pubes_Open.png"),
                "Trigger == 'lick pussy'", Recolor("Gwen", "Pubes", "images/GwenSex/Gwen_Sex_Pubes_Open.png"),
                "GwenX.Offhand == 'fondle pussy' and GwenX.Lust > 60", Recolor("Gwen", "Pubes", "images/GwenSex/Gwen_Sex_Pubes_Open.png"),
                "True", Recolor("Gwen", "Pubes", "images/GwenSex/Gwen_Sex_Pubes_Closed.png"),
                )

    #End Gwen Pussy composite
# End Gwen Scissor Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen_SC_Anim_0:
        #this is the animation for Gwen's lower body during Scissoring, Speed 0 (static)
        contains:
            subpixel True
            "Gwen_SC_Body"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 30
            pos (-10,40) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                ease 2 pos (-10,50)
                pause .5
                ease 2 pos (-10,40)
                pause .5
                repeat
        contains:
            subpixel True
            "Gwen_SC_Legs"
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
            "Gwen_Sex_Feet"
#            ConditionSwitch(
#                #Shows different lower body motion depending on events
#                "ShowFeet", "Gwen_Sex_Feet",
#                "True", AlphaMask("Gwen_Sex_Feet","images/GwenSex/Gwen_Sex_Feet_Mask.png")
#                )
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
        #end animation for Gwen's lower body during Scissoring, Speed 0 (static) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Gwen_SC_Anim_1:
        #this is the animation for Gwen's lower body during Scissoring, Speed 1 (slow)
        contains:
            subpixel True
            "Gwen_SC_Body"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 30
            pos (0,40) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                ease 1 pos (0,50)
                pause .5
                ease 1 pos (0,40)
                pause .5
                repeat
        contains:
            subpixel True
            "Gwen_SC_Legs"
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
            "Gwen_Sex_Feet"
#            ConditionSwitch(
#                #Shows different lower body motion depending on events
#                "ShowFeet", "Gwen_Sex_Feet",
#                "True", AlphaMask("Gwen_Sex_Feet","images/GwenSex/Gwen_Sex_Feet_Mask.png")
#                )
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
        #End animation for Gwen's lower body during Scissoring, Speed 1 (slow) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Gwen_SC_Anim_2:
        #this is the animation for Gwen's lower body during Scissoring, Speed 2 (fast)
        contains:
            subpixel True
            "Gwen_SC_Body"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 30
            pos (10,40) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                pause .1
                ease .5 pos (10,50)
                ease .5 pos (10,40)
                repeat
        contains:
            subpixel True
            "Gwen_SC_Legs"
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
            "Gwen_Sex_Feet"
#            ConditionSwitch(
#                #Shows different lower body motion depending on events
#                "ShowFeet", "Gwen_Sex_Feet",
#                "True", AlphaMask("Gwen_Sex_Feet","images/GwenSex/Gwen_Sex_Feet_Mask.png")
#                )
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
        #End animation for Gwen's lower body during Scissoring, Speed 2 (fast) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     SC Launch/Reset
label Gwen_SC_Launch(Line = Trigger):
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    return
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary

    $ Trigger = Line

    if renpy.showing("Gwen_SC_Sprite"):
        return
    $ Speed = 0
    call Girl_Hide(GwenX,1) #call Rogue_Hide
    show Gwen_SC_Sprite zorder 150
    with dissolve
    return

label Gwen_SC_Reset:
    if not renpy.showing("Gwen_SC_Sprite"):
        return
    $ GwenX.ArmPose = 2
    hide Gwen_SC_Sprite
    call Girl_Hide(GwenX) #call Rogue_Hide
#    call Set_The_Scene(Dress = 0)
    show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) zorder GwenX.Layer:
        alpha 1 zoom 1 offset (0,0) anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return
# End Gwen Scissor Pose content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


# Animation components / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Gwen Misc Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#label Gwen_Kissing_Launch(T = Trigger,Set=1):
#    call Gwen_Hide
#    $ Trigger = T
#    $ GwenX.Pose = "kiss" if Set else GwenX.Pose
#    show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) zorder GwenX.Layer
#    show Gwen_Sprite at SpriteLoc(StageCenter) zorder GwenX.Layer:
#        ease 0.5 offset (0,0) zoom 2 alpha 1
#    return

#label Gwen_Kissing_Smooch:
#    $ GwenX.FaceChange("kiss")
#    show Gwen_Sprite at SpriteLoc(StageCenter) zorder GwenX.Layer:
#        ease 0.5 xpos StageCenter offset (0,0) zoom 2 alpha 1
#        pause 1
#        ease 0.5 xpos GwenX.SpriteLoc zoom 1
#    show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) zorder GwenX.Layer:
#        zoom 1
#    $ GwenX.FaceChange("sexy")
#    return

#label Gwen_Breasts_Launch(T = Trigger,Set=1):
#    call Gwen_Hide
#    $ Trigger = T
#    $ GwenX.Pose = "breasts" if Set else GwenX.Pose
#    show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) zorder GwenX.Layer:
##        ease 0.5 offset (-100,-200) zoom 2
#        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
#    return

#label Gwen_Middle_Launch(T = Trigger,Set=1):
#    call Gwen_Hide
#    $ Trigger = T
#    $ GwenX.Pose = "mid" if Set else GwenX.Pose
#    show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) zorder GwenX.Layer:
##        ease 0.5 offset (-100,-200) zoom 2
#        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
#    return

#label Gwen_Pussy_Launch(T = Trigger,Set=1):
#    call Gwen_Hide
#    $ Trigger = T
#    $ GwenX.Pose = "pussy" if Set else GwenX.Pose
#    show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) zorder GwenX.Layer:
#        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
#    return

#label Gwen_Pos_Reset(T = 0,Set=0):
#    if GwenX.Loc != bg_current:
#            return
#    call Gwen_Hide
#    show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc) zorder GwenX.Layer:
#            ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
#    show Gwen_Sprite zorder GwenX.Layer:
#            offset (0,0)
#            anchor (0.5, 0.0)
#            zoom 1
#            xzoom 1
#            yzoom 1
#            alpha 1
#            pos (GwenX.SpriteLoc,50)
#    $ GwenX.Pose = "full" if Set else 0
#    $ Trigger = T
#    return

#label Gwen_Hide(Sprite=0):
##        call Gwen_Sex_Reset
#        hide Gwen_SexSprite
#        hide Gwen_Doggy_Animation
#        hide Gwen_HJ_Animation
#        hide Gwen_BJ_Animation
#        hide Gwen_TJ_Animation
#        hide Gwen_Finger_Animation
#        hide Gwen_CUN_Animation
#        hide Gwen_Seated
#        if Sprite:
#                hide Gwen_Sprite
#        return



# Interface items //////////////////////////////////////////////////////////////////////////////

image GropeLeftBreast_Gwen:
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

image GropeRightBreast_Gwen:
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

image LickRightBreast_Gwen:
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

image LickLeftBreast_Gwen:
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

image GropeThigh_Gwen:
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

image GropePussy_Gwen:
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

image FingerPussy_Gwen:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.65
        pos (275,650)#(275,650)
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

image Lickpussy_Gwen:
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

image VibratorRightBreast_Gwen:
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

image VibratorLeftBreast_Gwen:
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

image VibratorPussy_Gwen:
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

image VibratorAnal_Gwen:
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

image VibratorPussyInsert_Gwen:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_Gwen:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0



#Lesbian action animations.
image GirlGropeBothBreast_Gwen:
    contains:
        "GirlGropeLeftBreast_Gwen"
    contains:
        "GirlGropeRightBreast_Gwen"

image GirlGropeLeftBreast_Gwen:
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

image GirlGropeRightBreast_Gwen:
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

image GirlGropeThigh_Gwen:
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

image GirlGropePussy_GwenSelf:
    contains:
        "GirlGropePussy_Gwen"
        anchor (0.5,0.5)
        rotate -40
#        yzoom -1
        pos (190,500)#(180,525)

image GirlGropePussy_Gwen:
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

image GirlFingerPussy_Gwen:
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



label Gwen_Code:
        # Move she uses when in Xavier scene
        $ GwenX.ArmPose = 2
        show Gwen_Sprite at SpriteLoc(550,50) zorder GwenX.Layer:
            subpixel True
            offset (0,0)
            anchor (0.5, 0.0)
            #block:
            #Up - 1.2
            ease .2 yoffset 25
            easein .4 yoffset -200
            easeout .4 yoffset 25
            pause .2
            #Up -1.2
            easein .4 yoffset -200
            easeout .4 yoffset 25
            ease .2 yoffset 0
            pause .2
        ch_g "Ладно. . .{w=2.6}{nw}"
        show Gwen_Sprite at SpriteLoc(550,50) zorder GwenX.Layer:
            subpixel True
            offset (0,0)
            anchor (0.5, 0.0)
            #Down - 1.0
            ease .4 yoffset 200
            ease .4 yoffset 0
            pause .2
            #Down -1.0
            ease .4 yoffset 200
            ease .4 yoffset 0
            pause .2
        ch_g ". . . Ладно. . .{w=2.2}{nw}"
        $ GwenX.ArmPose = 1
        show Gwen_Sprite at SpriteLoc(550,50) zorder GwenX.Layer:
            subpixel True
            offset (0,0)
            zoom 1
            anchor (0.5, 0.0)
            #Left - .8
            ease .3 xoffset 100
            ease .4 xoffset 0
            pause .1
            #Right - .8
            ease .3 xoffset -100
            ease .4 xoffset 0
            pause .1
            #Left - .8
            ease .3 xoffset 100
            ease .4 xoffset 0
            pause .1
            #Right - .8
            ease .3 xoffset -100
            ease .4 xoffset 0
            pause .1
        ch_g ". . . затем. . .{w=3.4}{nw}"
        $ GwenX.ArmPose = 2
        $ GwenX.Uptop = 1
        ch_g "B. . ."
        $ GwenX.ArmPose = 1
        $ GwenX.Upskirt = 1
        ch_g "A. . ."
        $ GwenX.Uptop = 0
        $ GwenX.Upskirt = 0
        show Gwen_Sprite at SpriteLoc(550,50) zorder GwenX.Layer:
            subpixel True
            offset (0,0)
            anchor (0.5, 0.0)
            #Right - .3
            pause 0.5
            ease .5 offset (-75,20)
        ch_g "И наконец. . .{w=1.0}{nw}"
        menu:
            ch_g "Ладно, думаю, сработало!"
            "Начать":
                pass
        show Gwen_Sprite at SpriteLoc(550,50) zorder GwenX.Layer:
            subpixel True
            offset (0,0)
            anchor (0.5, 0.0)
            #Right - .3
            ease .3 xoffset 0
        show Gwen_Sprite at SpriteLoc(GwenX.SpriteLoc,50) zorder GwenX.Layer
        return
#end Gwen_Code scene

image GwenMastHand:
        "images/UI_GirlHand_Jean.png"
        zoom 0.8
        rotate 240
        offset (385,270)

image GwenFingerHand:
        "images/UI_GirlFinger_Jean.png"
        zoom 0.8
        rotate 220
        offset (360,330)
