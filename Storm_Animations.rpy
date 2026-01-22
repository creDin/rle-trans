# Basic character Sprites

image Storm_Sprite:
    LiveComposite(
        (450,950),
        (0,0), "images/StormSprite/Storm_Sprite_Shadow.png",
        (53,-45), "Storm_Sprite_HairBack",
        (0,0), ConditionSwitch(
            #back of the skirt/pants
            "StormX.Legs == 'skirt'", Recolor("Storm", "Legs", "images/StormSprite/Storm_Sprite_Legs_SkirtB.png"),
            "StormX.Upskirt", ConditionSwitch(
                        #if the skirt's up or pants down
                        "StormX.Legs == 'pants'", Recolor("Storm", "Legs", "images/StormSprite/Storm_Sprite_Legs_Pants_UpB.png"),
                        "StormX.Legs == 'yoga pants'", Recolor("Storm", "Legs", "images/StormSprite/Storm_Sprite_Legs_YogaPants_UpB.png"),
                        "True", Null(),
                        ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Jacket backplate
            "StormX.Over == 'jacket'", Recolor("Storm", "Over", "images/StormSprite/Storm_Sprite_Over_Jacket_Under.png"),
            "True", Null(),
            ),
#        (0,0), "images/StormSprite/Storm_Sprite_Body.png",

        (0,0), ConditionSwitch(
            #panties down back
            "not StormX.Panties", Null(),
            "StormX.PantiesDown", ConditionSwitch(
                    #if the panties are down
                    "not StormX.Legs or StormX.Upskirt or StormX.Legs == 'skirt'", ConditionSwitch(
                            #if she's wearing a skirt or nothing else
                            "StormX.Panties == 'cos panties'", Recolor("Storm", "Panties", "images/StormSprite/Storm_Sprite_Panties_Cos_DB.png"),
                            "StormX.Panties == 'white panties'", Recolor("Storm", "Panties", "images/StormSprite/Storm_Sprite_Panties_White_DB.png"),
                            #"StormX.Panties == 'lace panties'", "images/StormSprite/Storm_Sprite_Panties_Lace_DB.png",
                            #"StormX.Panties == 'bikini bottoms'", "images/StormSprite/Storm_Sprite_Panties_Bikini_DB.png",
                            "True", Recolor("Storm", "Panties", "images/StormSprite/Storm_Sprite_Panties_Black_DB.png"),
                            ),
                    "True", Null(),
                    ),
            "True", Null(),
            ),

        (165,560), ConditionSwitch(    #145,560
            #Personal Wetness
            "not StormX.Wet", Null(),
            "StormX.Legs and StormX.Legs != 'skirt' and not StormX.Upskirt", Null(),
            "StormX.Panties and not StormX.PantiesDown and StormX.Wet <= 1", Null(),
            "StormX.Wet == 1", ConditionSwitch( #Wet = 1
                    "StormX.Panties and StormX.PantiesDown", AlphaMask("Wet_Drip","Storm_Drip_MaskP"),
                    "StormX.Legs and StormX.Legs != 'skirt'", AlphaMask("Wet_Drip","Storm_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip","Storm_Drip_Mask"), #only plays if nothing is in the way
                    ),
            "True", ConditionSwitch( #Wet = 2+
                    "StormX.Panties and StormX.PantiesDown", AlphaMask("Wet_Drip2","Storm_Drip_MaskP"),
                    "StormX.Legs and StormX.Legs != 'skirt'", AlphaMask("Wet_Drip2","Storm_Drip_MaskP"),
                    "StormX.Panties", AlphaMask("Wet_Drip","Storm_Drip_Mask"), #"Wet_Drip2",#
                    "True", AlphaMask("Wet_Drip2","Storm_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (165,560), ConditionSwitch(    #145,560
            #dripping spunk
            "('in' not in StormX.Spunk and 'anal' not in StormX.Spunk) or not Player.Male", Null(),
            "StormX.Legs and StormX.Legs != 'skirt' and not StormX.Upskirt", Null(),
            "StormX.Panties and not StormX.PantiesDown and StormX.Wet <= 1", Null(),
            "True", ConditionSwitch( #Wet = 2+
                    "StormX.Panties and StormX.PantiesDown", AlphaMask("Spunk_Drip2","Storm_Drip_MaskP"),
#                    "StormX.Legs and StormX.Legs != 'skirt'", AlphaMask("Spunk_Drip2","Storm_Drip_MaskP"), #add if pantes have down art
                    "StormX.Panties", AlphaMask("Spunk_Drip","Storm_Drip_Mask"), #"Wet_Drip2",#
                    "True", AlphaMask("Spunk_Drip2","Storm_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),

        (0,0), ConditionSwitch(
            #body
            "StormX.ArmPose != 1", "images/StormSprite/Storm_Sprite_Body2.png",         # right hand up/left down
            "True", "images/StormSprite/Storm_Sprite_Body1.png", #if StormX.Arms == 1   # right Hand on hip/left raised
            ),
#        (0,0), ConditionSwitch(
#            #Water effect
#            "StormX.Water and StormX.ArmPose == 1", "images/StormSprite/Storm_Sprite_Water1.png",
#            "StormX.Water", "images/StormSprite/Storm_Sprite_Water2.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #pubes
            "StormX.Pubes", Recolor("Storm", "Pubes", "images/StormSprite/Storm_Sprite_Pubes.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #nude lower piercings
            "not StormX.Pierce", Null(),
            "StormX.Panties and not StormX.PantiesDown", Null(),
            "StormX.Legs != 'skirt' and StormX.Legs and not StormX.Upskirt", Null(), #skirt if wearing a skirt
            "StormX.Pierce == 'barbell'", "images/StormSprite/Storm_Sprite_Barbell_Pussy.png",
            "StormX.Pierce == 'ring'", "images/StormSprite/Storm_Sprite_Ring_Pussy.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #arm rings base
            "not StormX.Acc == 'rings' or StormX.Over == 'jacket'", Null(),
            "StormX.ArmPose == 1", "images/StormSprite/Storm_Sprite_ArmRings1.png",
            "True", "images/StormSprite/Storm_Sprite_ArmRings2.png", #StormX.ArmPose == 2
            ),
        (0,0), ConditionSwitch(
            #Tits
            "StormX.Uptop", "images/StormSprite/Storm_Sprite_Tits.png",
            "StormX.Chest == 'black bra' or StormX.Chest == 'lace bra' or StormX.Chest == 'sports bra'", "images/StormSprite/Storm_Sprite_Tits_Up.png",
            "True", "images/StormSprite/Storm_Sprite_Tits.png",
            ),
        (0,0), ConditionSwitch(
            #naked tit piercings
            "not StormX.Pierce", Null(),
#            "not StormX.Pierce or ((StormX.Over or StormX.Chest) and not StormX.Uptop)", Null(),
            "StormX.Uptop", Null(),
            #Only does this if she has piercings, has no tops, or has her top up
            "StormX.Pierce == 'barbell'", ConditionSwitch(
                    # if top is up. . .
                    "StormX.Chest == 'black bra' or StormX.Chest == 'lace bra' or StormX.Chest == 'sports bra'", "images/StormSprite/Storm_Sprite_Barbell_TitsU.png",
                    "True", "images/StormSprite/Storm_Sprite_Barbell_TitsL.png",
                    ),
            # Pierce is "ring"
            "StormX.Chest == 'black bra' or StormX.Chest == 'lace bra' or StormX.Chest == 'sports bra'", "images/StormSprite/Storm_Sprite_Ring_TitsUCU.png",
            "StormX.Over or StormX.Chest", "images/StormSprite/Storm_Sprite_Ring_TitsLCU.png",
            "True", "images/StormSprite/Storm_Sprite_Ring_TitsL.png",
            ),


        (0,0), ConditionSwitch(
            #Necklaces
#            "StormX.Neck == 'silver'", "images/StormSprite/Storm_Sprite_Necklace2.png",
            "StormX.Neck == 'gold necklace'", "images/StormSprite/Storm_Sprite_Necklace1.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Chest layer
            "StormX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "StormX.Chest == 'cos bra'", Recolor("Storm", "Chest", "images/StormSprite/Storm_Sprite_Chest_Cos_Up.png"),
                    "StormX.Chest == 'black bra'", Recolor("Storm", "Chest", "images/StormSprite/Storm_Sprite_Chest_Bra_Up.png"),
                    "StormX.Chest == 'lace bra'", Recolor("Storm", "Chest", "images/StormSprite/Storm_Sprite_Chest_Bra_Up.png"),
                    "StormX.Chest == 'sports bra'", Recolor("Storm", "Chest", "images/StormSprite/Storm_Sprite_Chest_Sportsbra_Up.png"),
                    "StormX.Chest == 'bikini top'", Recolor("Storm", "Chest", "images/StormSprite/Storm_Sprite_Chest_Bikini_Up.png"),
                    "StormX.Chest == 'tube top'", Recolor("Storm", "Chest", "images/StormSprite/Storm_Sprite_Chest_Tube_Up.png"),
                    "True", Null(),
                    ),
            "StormX.Chest == 'cos bra'", Recolor("Storm", "Chest", "images/StormSprite/Storm_Sprite_Chest_Cos.png"),
            "StormX.Chest == 'black bra'", Recolor("Storm", "Chest", "images/StormSprite/Storm_Sprite_Chest_Bra.png"),
            "StormX.Chest == 'lace bra'", "images/StormSprite/Storm_Sprite_Chest_LaceBra.png",
            "StormX.Chest == 'sports bra'", Recolor("Storm", "Chest", "images/StormSprite/Storm_Sprite_Chest_Sportsbra.png"),
            "StormX.Chest == 'bikini top'", Recolor("Storm", "Chest", "images/StormSprite/Storm_Sprite_Chest_Bikini.png"),
            "StormX.Chest == 'tube top'", Recolor("Storm", "Chest", "images/StormSprite/Storm_Sprite_Chest_Tube.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #clothed tit peircings  under jacket
            "not StormX.Pierce or (not StormX.Over and not StormX.Chest and not StormX.Uptop)", Null(),
            "StormX.Uptop", Null(),
            "StormX.Pierce == 'barbell'", ConditionSwitch(
                    # if top is up. . .
                    "StormX.Chest == 'black bra' or StormX.Chest == 'lace bra' or StormX.Chest == 'sports bra'", "images/StormSprite/Storm_Sprite_Barbell_TitsUC.png",
                    "True", "images/StormSprite/Storm_Sprite_Barbell_TitsLC.png",
                    ),
            "StormX.Pierce == 'ring' and (StormX.Chest == 'black bra' or StormX.Chest == 'lace bra' or StormX.Chest == 'sports bra')", "images/StormSprite/Storm_Sprite_Ring_TitsUC.png",
            "StormX.Pierce == 'ring'", "images/StormSprite/Storm_Sprite_Ring_TitsLC.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #stockings
            "StormX.Hose == 'stockings'", Recolor("Storm", "Hose", "images/StormSprite/Storm_Sprite_Hose_Stockings.png"),
            "StormX.Hose == 'stockings and garterbelt'", Recolor("Storm", "Hose", "images/StormSprite/Storm_Sprite_Hose_StockingsandGarter.png"),
            "StormX.Hose == 'garterbelt'", Recolor("Storm", "Hose", "images/StormSprite/Storm_Sprite_Hose_Garter.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #panties
            "not StormX.Panties", Null(),
            "StormX.PantiesDown", ConditionSwitch(
                    #if the panties are down
                    "not StormX.Legs or StormX.Upskirt or StormX.Legs == 'skirt'", ConditionSwitch(
                            #if she's wearing a skirt or nothing else
                            "StormX.Panties == 'cos panties'", Recolor("Storm", "Panties", "images/StormSprite/Storm_Sprite_Panties_Cos_D.png"),
                            "StormX.Panties == 'white panties'", Recolor("Storm", "Panties", "images/StormSprite/Storm_Sprite_Panties_White_D.png"),
                            "StormX.Panties == 'lace panties'", Recolor("Storm", "Panties", "images/StormSprite/Storm_Sprite_Panties_Lace_D.png"),
                            "StormX.Panties == 'bikini bottoms'", Recolor("Storm", "Panties", "images/StormSprite/Storm_Sprite_Panties_Bikini_D.png"),
                            "True", Recolor("Storm", "Panties", "images/StormSprite/Storm_Sprite_Panties_Black_D.png"),
                            ),
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                    #if she's got panties and they are not down
                    "StormX.Wet", ConditionSwitch(
                        #if she's  wet
                        "StormX.Panties == 'cos panties'", Recolor("Storm", "Panties", "images/StormSprite/Storm_Sprite_Panties_Cos.png"),
                        "StormX.Panties == 'white panties'", Recolor("Storm", "Panties", "images/StormSprite/Storm_Sprite_Panties_WhiteW.png"),
                        "StormX.Panties == 'lace panties'", Recolor("Storm", "Panties", "images/StormSprite/Storm_Sprite_Panties_Lace.png"),
                        "StormX.Panties == 'bikini bottoms' and (StormX.Chest != 'bikini top' or StormX.Uptop)", Recolor("Storm", "Panties", "images/StormSprite/Storm_Sprite_Panties_BikiniL.png"),
                        "StormX.Panties == 'bikini bottoms'", Recolor("Storm", "Panties", "images/StormSprite/Storm_Sprite_Panties_Bikini.png"),
                        "True", Recolor("Storm", "Panties", "images/StormSprite/Storm_Sprite_Panties_BlackW.png"),
                        ),
                    "True", ConditionSwitch(
                        #if she's not wet
                        "StormX.Panties == 'cos panties'", Recolor("Storm", "Panties", "images/StormSprite/Storm_Sprite_Panties_Cos.png"),
                        "StormX.Panties == 'white panties'", Recolor("Storm", "Panties", "images/StormSprite/Storm_Sprite_Panties_White.png"),
                        "StormX.Panties == 'lace panties'", Recolor("Storm", "Panties", "images/StormSprite/Storm_Sprite_Panties_Lace.png"),
                        "StormX.Panties == 'bikini bottoms' and (StormX.Chest != 'bikini top' or StormX.Uptop)", Recolor("Storm", "Panties", "images/StormSprite/Storm_Sprite_Panties_BikiniL.png"),
                        "StormX.Panties == 'bikini bottoms'", Recolor("Storm", "Panties", "images/StormSprite/Storm_Sprite_Panties_Bikini.png"),
                        "True", Recolor("Storm", "Panties", "images/StormSprite/Storm_Sprite_Panties_Black.png"),
                        ),
                    ),
            ),
        (0,0), ConditionSwitch(
            #pantyhose
            "StormX.Hose == 'pantyhose' and (not StormX.PantiesDown or not StormX.Panties)", Recolor("Storm", "Hose", "images/StormSprite/Storm_Sprite_Hose_Pantyhose.png"),
            "StormX.Hose == 'ripped pantyhose' and (not StormX.PantiesDown or not StormX.Panties)", Recolor("Storm", "Hose", "images/StormSprite/Storm_Sprite_Hose_Pantyhose_Holed.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Leg rings
            "not StormX.Acc == 'rings' or StormX.Legs == 'pants' or StormX.Legs == 'yoga pants'", Null(),
            "True", "images/StormSprite/Storm_Sprite_LegRings.png",
            ),
        (0,0), ConditionSwitch(
            #pants
            "not StormX.Legs", Null(),
            "StormX.Upskirt", ConditionSwitch(
                        #if the skirt's up or pants down
                        "StormX.Legs == 'pants'", Recolor("Storm", "Legs", "images/StormSprite/Storm_Sprite_Legs_Pants_Up.png"),
                        "StormX.Legs == 'yoga pants'", Recolor("Storm", "Legs", "images/StormSprite/Storm_Sprite_Legs_YogaPants_Up.png"),
                        "StormX.Legs == 'skirt'", Recolor("Storm", "Legs", "images/StormSprite/Storm_Sprite_Legs_Skirt_Up.png"),
                        "True", Null(),
                        ),
            "True", ConditionSwitch(
                    #if it's the ring pericings
                    "StormX.Wet", ConditionSwitch(
                        #if she's not wet
                        "StormX.Legs == 'pants'", Recolor("Storm", "Legs", "images/StormSprite/Storm_Sprite_Legs_PantsW.png"),
                        "StormX.Legs == 'yoga pants'", Recolor("Storm", "Legs", "images/StormSprite/Storm_Sprite_Legs_YogaPantsW.png"),
                        "StormX.Legs == 'skirt'", Recolor("Storm", "Legs", "images/StormSprite/Storm_Sprite_Legs_Skirt.png"),
                        "True", Null(),
                        ),
                    "True", ConditionSwitch(
                        #if she's wet
                        "StormX.Legs == 'pants'", Recolor("Storm", "Legs", "images/StormSprite/Storm_Sprite_Legs_Pants.png"),
                        "StormX.Legs == 'yoga pants'", Recolor("Storm", "Legs", "images/StormSprite/Storm_Sprite_Legs_YogaPants.png"),
                        "StormX.Legs == 'skirt'", Recolor("Storm", "Legs", "images/StormSprite/Storm_Sprite_Legs_Skirt.png"),
                        "True", Null(),
                        ),
                    ),
            ),
        (0,0), ConditionSwitch(
            #shoes
            "StormX.Boots == 'sandals'", "images/StormSprite/Storm_Sprite_Boots_Sandals.png",
            "StormX.Boots == 'rings'", "images/StormSprite/Storm_Sprite_Boots_Rings.png",
            "StormX.Boots and StormX.Legs == 'pants'", "images/StormSprite/Storm_Sprite_Boots_Pants.png",
            "StormX.Boots", "images/StormSprite/Storm_Sprite_Boots.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #clothed lower piercings
            "StormX.Legs == 'skirt' or StormX.Legs == 'pants'", Null(),
            "StormX.Pierce == 'barbell'", ConditionSwitch(
                    #if it's the barbell pericings
                    "StormX.Legs and not StormX.Upskirt", "images/StormSprite/Storm_Sprite_Barbell_PussyC.png",
                    "StormX.Panties and not StormX.PantiesDown", "images/StormSprite/Storm_Sprite_Barbell_PussyC.png",
                    "True", Null(),
                    ),
            "StormX.Pierce == 'ring'", ConditionSwitch(
                    #if it's the ring pericings
                    "StormX.Legs and not StormX.Upskirt", "images/StormSprite/Storm_Sprite_Ring_PussyC.png",
                    "StormX.Panties and not StormX.PantiesDown", "images/StormSprite/Storm_Sprite_Ring_PussyC.png",
                    "True", Null(),
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy spunk
            "StormX.Legs and not StormX.Upskirt", Null(),
            "('in' in StormX.Spunk or 'anal' in StormX.Spunk) and Player.Male", "images/StormSprite/Storm_Sprite_Spunk_Pussy.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Water effect
            "not StormX.Water", Null(),
            "(StormX.Chest == 'black bra' or StormX.Chest == 'lace bra' or StormX.Chest == 'sports bra') and StormX.ArmPose == 1", "images/StormSprite/Storm_Sprite_Water_Tight1.png",
            "StormX.Chest == 'black bra' or StormX.Chest == 'lace bra' or StormX.Chest == 'sports bra'", "images/StormSprite/Storm_Sprite_Water_Tight2.png",
            "StormX.ArmPose == 1", "images/StormSprite/Storm_Sprite_Water_Loose1.png",
            "True", "images/StormSprite/Storm_Sprite_Water_Loose2.png",
            ),


        (0,0), ConditionSwitch(
            #neck
            "StormX.Neck == 'rings'", "images/StormSprite/Storm_Sprite_Necklace3.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over
            "StormX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "StormX.Over == 'white shirt'", Recolor("Storm", "Over", "images/StormSprite/Storm_Sprite_Over_WhiteShirt_Up.png"),
                    "StormX.Over == 'jacket' and StormX.ArmPose != 1", Recolor("Storm", "Over", "images/StormSprite/Storm_Sprite_Over_Jacket2_Up.png"),
                    "StormX.Over == 'jacket'", Recolor("Storm", "Over", "images/StormSprite/Storm_Sprite_Over_Jacket1_Up.png"),
#                    "StormX.Over == 'towel'", "images/StormSprite/Storm_Sprite_Towel.png",
                    "True", Null(),
                    ),
            #If she's using arm pose 1, right arm high
            #If she's using arm pose 2, Left arm high
            "StormX.Chest == 'black bra' or StormX.Chest == 'lace bra' or StormX.Chest == 'sports bra'", ConditionSwitch(
                    # if she's using a breast-raising bra
                    "StormX.Over == 'white shirt'", Recolor("Storm", "Over", "images/StormSprite/Storm_Sprite_Over_WhiteShirtU.png"),
                    "StormX.Over == 'jacket' and StormX.ArmPose != 1", Recolor("Storm", "Over", "images/StormSprite/Storm_Sprite_Over_Jacket2U.png"),
                    "StormX.Over == 'jacket'", Recolor("Storm", "Over", "images/StormSprite/Storm_Sprite_Over_Jacket1U.png"),
                    "True", Null(),
                    ),
            "StormX.Over == 'white shirt'", Recolor("Storm", "Over", "images/StormSprite/Storm_Sprite_Over_WhiteShirtL.png"),
            "StormX.Over == 'jacket' and StormX.ArmPose != 1", Recolor("Storm", "Over", "images/StormSprite/Storm_Sprite_Over_Jacket2L.png"),
            "StormX.Over == 'jacket'", Recolor("Storm", "Over", "images/StormSprite/Storm_Sprite_Over_Jacket1L.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Chest layer over jacket
            "not StormX.Uptop or StormX.Over != 'jacket'", Null(),
            # if top is up. . .
            "StormX.Chest == 'black bra'", Recolor("Storm", "Chest", "images/StormSprite/Storm_Sprite_Chest_Bra_UpJ.png"),
            "StormX.Chest == 'lace bra'", Recolor("Storm", "Chest", "images/StormSprite/Storm_Sprite_Chest_Bra_UpJ.png"),
            "StormX.Chest == 'sports bra'", Recolor("Storm", "Chest", "images/StormSprite/Storm_Sprite_Chest_Sportsbra_UpJ.png"),
            "StormX.Chest == 'bikini top'", Recolor("Storm", "Chest", "images/StormSprite/Storm_Sprite_Chest_Bikini_UpJ.png"),
            "StormX.Chest == 'tube top'", Recolor("Storm", "Chest", "images/StormSprite/Storm_Sprite_Chest_Tube_UpJ.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #clothed tit peircings
            "not StormX.Pierce or (not StormX.Over and not StormX.Chest and not StormX.Uptop)", Null(),
            "StormX.Over == 'jacket' and not StormX.Uptop", Null(),
            "StormX.Pierce == 'barbell'", ConditionSwitch(
                    # if top is up. . .
                    "StormX.Uptop", "images/StormSprite/Storm_Sprite_Barbell_TitsL.png",
                    "StormX.Chest == 'black bra' or StormX.Chest == 'lace bra' or StormX.Chest == 'sports bra'", "images/StormSprite/Storm_Sprite_Barbell_TitsUC.png",
                    "True", "images/StormSprite/Storm_Sprite_Barbell_TitsLC.png",
                    ),
            "StormX.Uptop", "images/StormSprite/Storm_Sprite_Ring_TitsL.png",
            "StormX.Pierce == 'ring' and (StormX.Chest == 'black bra' or StormX.Chest == 'lace bra' or StormX.Chest == 'sports bra')", "images/StormSprite/Storm_Sprite_Ring_TitsUC.png",
            "StormX.Pierce == 'ring'", "images/StormSprite/Storm_Sprite_Ring_TitsLC.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #belly spunk
            "'belly' in StormX.Spunk and Player.Male", "images/StormSprite/Storm_Sprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast spunk
            "'tits' in StormX.Spunk and (StormX.Chest == 'black bra' or StormX.Chest == 'lace bra' or StormX.Chest == 'sports bra') and Player.Male", "images/StormSprite/Storm_Sprite_Spunk_TitsU.png",
            "'tits' in StormX.Spunk and Player.Male", "images/StormSprite/Storm_Sprite_Spunk_TitsL.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Arms 1 upper layer
            "StormX.ArmPose == 1", "images/StormSprite/Storm_Sprite_Arms1a.png",        #If she's using arm pose 1, right arm high
            "True", Null(),  #if StormX.Arms ==2                                        #If she's using arm pose 2, Left arm high
            ),
        (0,0), ConditionSwitch(
            #Jacket Collar, so it passes over Hand 1
            "StormX.Over == 'jacket'", Recolor("Storm", "Over", "images/StormSprite/Storm_Sprite_Over_JacketC.png"),
            "True", Null(),
            ),
        (53,-45), "Storm_Sprite_Head", #(53,-38)#(50,-48)
        (0,0), ConditionSwitch(
            #Arms 2 layer
            "StormX.ArmPose != 1 and renpy.showing('Storm_HJ_Animation')", Null(),
            "StormX.ArmPose != 1", "images/StormSprite/Storm_Sprite_Arms2a.png",                #If she's using arm pose 2, Left arm high
            "True", Null(),                                                                     #If she's using arm pose 1, right arm high
            ),
        (0,0), ConditionSwitch(
            #Water effect on arm
            "StormX.Water and StormX.ArmPose != 1", "images/StormSprite/Storm_Sprite_Water_Arm2.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Arms clothing layer
            "StormX.ArmPose != 1 and StormX.Over == 'jacket' and renpy.showing('Storm_HJ_Animation')", Recolor("Storm", "Over", "images/StormSprite/Storm_Sprite_Over_Jacket2H.png"),     #If she's using arm pose 2, Left arm high
            "StormX.ArmPose != 1 and StormX.Over == 'jacket'", Recolor("Storm", "Over", "images/StormSprite/Storm_Sprite_Over_Jacket2A.png"),     #If she's using arm pose 2, Left arm high
            "StormX.ArmPose != 1 and StormX.Acc == 'rings'", "images/StormSprite/Storm_Sprite_ArmRings2Top.png",                                #If she's using arm pose 2, Left arm high
            "True", Null(),                                                                                             #If she's using arm pose 1, right arm high
            ),

#        (0,0), ConditionSwitch(
#            #hand spunk
#            "StormX.ArmPose == 2 or 'hand' not in StormX.Spunk", Null(),
#            "True", "images/StormSprite/Storm_Sprite_Spunk_Hand.png",
#            ),
#        (0,0), ConditionSwitch(                                                                         #Props
#            "not StormX.Held or StormX.ArmPose != 2", Null(),
#            "StormX.ArmPose == 2 and StormX.Held == 'phone'", "images/StormSprite/Storm_held_phone.png",
#            "StormX.ArmPose == 2 and StormX.Held == 'dildo'", "images/StormSprite/Storm_held_dildo.png",
#            "StormX.ArmPose == 2 and StormX.Held == 'vibrator'", "images/StormSprite/Storm_held_vibrator.png",
#            "StormX.ArmPose == 2 and StormX.Held == 'panties'", "images/StormSprite/Storm_held_panties.png",
#            "True", Null(),
#            ),


#        (0,0), ConditionSwitch(
#            #UI tool for When Storm is masturbating using StormX.Offhand actions while lead
#            "Trigger == 'lesbian' or not StormX.Offhand or Ch_Focus is not StormX", Null(),

#            #this is not a lesbian thing, and a trigger is set, and Storm is the primary. . .
#            "StormX.Offhand == 'fondle pussy' and Trigger != 'sex' and StormX.Lust >= 70", At('GirlGropePussy_StormSelf',GirlFingerPussy_Storm1()),
#            "StormX.Offhand == 'fondle pussy'", At('GirlGropePussy_StormSelf',GirlGropePussy_Storm1()),
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #UI tool for When Storm is masturbating using StormX.Offhand actions while lead
            "Trigger == 'lesbian' or not StormX.Offhand",Null(),# or Ch_Focus is not StormX", Null(),
#            "StormX.Offhand == 'fondle pussy' and Trigger != 'sex' and StormX.Lust >= 70", At('GirlGropePussy_StormSelf',GirlFingerPussy_Storm1()),
#            "StormX.Offhand == 'fondle pussy'", At('GirlGropePussy_StormSelf',GirlGropePussy_Storm1()),
            "StormX.Offhand == 'fondle pussy' and Trigger != 'sex' and StormX.Lust >= 70", "GirlFingerPussy_Storm",
            "StormX.Offhand == 'fondle pussy'", "GirlGropePussy_Storm",
            "StormX.Offhand == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Storm",    #When zero is working the right breast, fondle left
            "StormX.Offhand == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Storm", #When zero is working the left breast, fondle right
            "StormX.Offhand == 'fondle breasts'", "GirlGropeRightBreast_Storm",
            "StormX.Offhand == 'vibrator breasts'", "VibratorRightBreast_Storm",
            "StormX.Offhand == 'vibrator pussy'", "VibratorPussy_Storm",
            "StormX.Offhand == 'vibrator pussy insert'", "VibratorPussy_Storm",
            "StormX.Offhand == 'vibrator anal'", "VibratorAnal_Storm",
            "StormX.Offhand == 'vibrator anal insert'", "VibratorPussy_Storm",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for StormX.Offhand(lesbian) actions (ie Kitty's hand on her when Storm is secondary)
            "not Partner or Partner is StormX or StormX in Nearby", Null(),
            "Partner.Offhand == 'fondle girl pussy' and Trigger != 'sex' and StormX.Lust >= 70", "GirlFingerPussy_Storm",
            "Partner.Offhand == 'fondle girl pussy'", "GirlGropePussy_Storm",
            "Partner.Offhand == 'lick girl pussy'", "Lickpussy_Storm",
            "Partner.Offhand == 'suck girl breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Storm",
            "Partner.Offhand == 'suck girl breasts'", "LickRightBreast_Storm",
            "Partner.Offhand == 'fondle girl breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Storm",    #When zero is working the right breast, fondle left
            "Partner.Offhand == 'fondle girl breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Storm", #When zero is working the left breast, fondle right
            "Partner.Offhand == 'fondle girl breasts'", "GirlGropeRightBreast_Storm",
            "Partner.Offhand == 'vibrator girl breasts'", "VibratorRightBreast_Storm",
            "Partner.Offhand == 'vibrator girl pussy'", "VibratorPussy_Storm",
            "Partner.Offhand == 'vibrator girl pussy insert'", "VibratorPussy_Storm",
            "Partner.Offhand == 'vibrator girl anal'", "VibratorAnal_Storm",
            "Partner.Offhand == 'vibrator girl anal insert'", "VibratorPussy_Storm",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for when RogueX is the partner in the scene, and the lead is working on her
            "not Partner or Partner is not StormX", Null(),
            "Ch_Focus.Offhand == 'fondle girl pussy' and Trigger != 'sex' and StormX.Lust >= 70", "GirlFingerPussy_Storm",
            "Ch_Focus.Offhand == 'fondle girl pussy'", "GirlGropePussy_Storm",
            "Ch_Focus.Offhand == 'lick girl pussy'", "Lickpussy_Storm",
            "Ch_Focus.Offhand == 'suck girl breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Storm",
            "Ch_Focus.Offhand == 'suck girl breasts'", "LickRightBreast",
            "Ch_Focus.Offhand == 'fondle girl breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Storm",    #When zero is working the right breast, fondle left
            "Ch_Focus.Offhand == 'fondle girl breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Storm", #When zero is working the left breast, fondle right
            "Ch_Focus.Offhand == 'fondle girl breasts'", "GirlGropeRightBreast_Storm",
            "Ch_Focus.Offhand == 'vibrator girl breasts'", "VibratorRightBreast_Storm",
            "Ch_Focus.Offhand == 'vibrator girl pussy'", "VibratorPussy_Storm",
            "Ch_Focus.Offhand == 'vibrator girl pussy insert'", "VibratorPussy_Storm",
            "Ch_Focus.Offhand == 'vibrator girl anal'", "VibratorAnal_Storm",
            "Ch_Focus.Offhand == 'vibrator girl anal insert'", "VibratorPussy_Storm",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger1(primary) actions
            #Storm is primary and a sex trigger is active
            "not Trigger or Ch_Focus is not StormX", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast_Storm",
            "Trigger == 'fondle thighs'", "GropeThigh_Storm",
            "Trigger == 'fondle breasts'", "GropeLeftBreast_Storm",
            "Trigger == 'suck breasts'", "LickRightBreast_Storm",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_Storm",
            "Trigger == 'fondle pussy'", "GropePussy_Storm",
            "Trigger == 'lick pussy'", "Lickpussy_Storm",
            "Trigger == 'vibrator pussy'", "VibratorPussy_Storm",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy_Storm",
            "Trigger == 'vibrator anal'", "VibratorAnal_Storm",
            "Trigger == 'vibrator anal insert'", "VibratorPussy_Storm",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus is not StormX", Null(),
#            "Trigger == 'fondle breasts' and not StormX.Offhand", "GropeRightBreast_Storm",  #"Trigger == 'fondle breasts' and not StormX.Offhand",
            #When doing nothing offhand, use both hands on breasts.
            "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast_Storm",
            #When sucking right breast, fondle left
            "Trigger2 == 'fondle breasts'", "GropeLeftBreast_Storm",
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast_Storm",
            #When sucking right breast, vibrator left
            "Trigger2 == Trigger", Null(),
            #When both triggers are the same, do nothing
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast_Storm",
            "Trigger2 == 'suck breasts'", "LickLeftBreast_Storm",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy_Storm",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy_Storm",
            "Trigger2 == 'vibrator anal'", "VibratorAnal_Storm",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy_Storm",
            "Trigger2 == 'fondle pussy'", "GropePussy_Storm",
            "Trigger2 == 'lick pussy'", "Lickpussy_Storm",
            "Trigger2 == 'fondle thighs'", "GropeThigh_Storm",
            "True", Null(),
            ),
        )
    anchor (0.5, 0.0)
    offset (60,0)#15   (20,0)
    zoom .80#.75

image Storm_Sprite_HairBack:
    contains:
        ConditionSwitch(
                #towel back
                "StormX.Over == 'towel'", "images/StormSprite/Storm_Sprite_Over_Towel_Under.png",
                "True", Null(),
                ),
    contains:
        ConditionSwitch(
                #hair back
    #            "renpy.showing('Storm_BJ_Animation')", Null(),
    #            "renpy.showing('Storm_SexSprite')", "images/StormSex/Storm_Sprite_Hair_Long_UnderSex.png",
    #            "StormX.Hair == 'wet' or StormX.Water", "images/StormSprite/Storm_Sprite_Hair_Wet_Under.png",
                "StormX.Over == 'towel'", Null(),
                "StormX.Hair == 'short'", Null(),

                "StormX.Hair == 'wethawk'", Recolor("Storm", "Hair", "images/StormSprite/Storm_Sprite_Hair_Mohawk_Back_Wet.png"),
                "StormX.Hair == 'mohawk' and StormX.Water", Recolor("Storm", "Hair", "images/StormSprite/Storm_Sprite_Hair_Mohawk_Back_Wet.png"),
                "StormX.Hair == 'mohawk' and not Player.Male and 'facial' in StormX.Spunk",Recolor("Storm", "Hair", "images/StormSprite/Storm_Sprite_Hair_Mohawk_Back_Wet.png"),
                "StormX.Hair == 'mohawk'", Recolor("Storm", "Hair", "images/StormSprite/Storm_Sprite_Hair_Mohawk_Back.png"),

                "StormX.Hair == 'wet'", Recolor("Storm", "Hair", "images/StormSprite/Storm_Sprite_Hair_Long_Back_Wet.png"),
                "StormX.Hair and StormX.Water", Recolor("Storm", "Hair", "images/StormSprite/Storm_Sprite_Hair_Long_Back_Wet.png"),
                "not Player.Male and 'facial' in StormX.Spunk",Recolor("Storm", "Hair", "images/StormSprite/Storm_Sprite_Hair_Long_Back_Wet.png"),
                "StormX.Hair", Recolor("Storm", "Hair", "images/StormSprite/Storm_Sprite_Hair_Long_Back.png"),
                "True", Null(),
                ),
#    "images/StormSprite/Storm_Sprite_Hair_Long_Under.png"
    anchor (0.5, 0.5)
    zoom .47

#image Storm_Sprite_HairMid:
#    ConditionSwitch(
#            #hair back
#            "not StormX.Hair", Null(),
#            "renpy.showing('Storm_BJ_Animation')", Null(),
##            "renpy.showing('Storm_SexSprite')", "images/StormSex/Storm_Sprite_Hair_Long_UnderSex.png",
#            "StormX.Hair == 'wet' or StormX.Water", Null(),
#            "StormX.Hair", "images/StormSprite/Storm_Sprite_Hair_Short_Mid.png",
#            "True", Null(),
#            ),
#    anchor (0.6, 0.0)
#    zoom .5

#image Storm_Sprite_HairTop:
#    ConditionSwitch(
#            #hair back
#            "not StormX.Hair", Null(),
##            "renpy.showing('Storm_SexSprite')", "images/StormSex/Storm_Sprite_Hair_Short_OverSex.png",
##            "StormX.Hair == 'wet' or StormX.Water", "images/StormSprite/Storm_Sprite_Hair_Wet_Over.png",
#            "StormX.Hair == 'mohawk'", Recolor("Storm", "Hair", "images/StormSprite/Storm_Sprite_Hair_Mohawk_Back.png"),
#            "StormX.Hair", Recolor("Storm", "Hair", "images/StormSprite/Storm_Sprite_Hair_Long_Back.png"),
#            "True", Null(),
#            ),
##    "images/StormSprite/Storm_Sprite_Hair_Long_Under.png"
#    anchor (0.6, 0.0)
#    zoom .5

image Storm_Sprite_Head:
    LiveComposite(
        (900,900),
#        (0,0), ConditionSwitch(
#                # hair behind face
#                "renpy.showing('Storm_SexSprite')", "images/StormSex/Storm_Sprite_Hair_Long_UnderSex.png",
#                "True", Null(),
#                ),
        (0,0), ConditionSwitch(
            # Face background plate
            "StormX.Blush >= 2", "images/StormSprite/Storm_Sprite_Head_Blush.png",
#                "StormX.Blush", "images/StormSprite/Storm_Sprite_Head_Blush.png",
            "True", "images/StormSprite/Storm_Sprite_Head_Base.png",
            ),
        (0,0), ConditionSwitch(
            #chin spunk
            "'chin' in StormX.Spunk and Player.Male", "images/StormSprite/Storm_Sprite_Spunk_Chin.png",
#            "renpy.showing('Storm_BJ_Animation') and Speed >= 2", Null(),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Mouths
            "True", ConditionSwitch(
                    "StormX.Mouth == 'lipbite'", Recolor("Storm", "Lips", "images/StormSprite/Storm_Sprite_Mouth_Lipbite.png"),
                    "StormX.Mouth == 'sucking' or StormX.Mouth == 'open'", Recolor("Storm", "Lips", "images/StormSprite/Storm_Sprite_Mouth_Open.png"),
                    "StormX.Mouth == 'kiss'", Recolor("Storm", "Lips", "images/StormSprite/Storm_Sprite_Mouth_Kiss.png"),
                    "StormX.Mouth == 'sad'", Recolor("Storm", "Lips", "images/StormSprite/Storm_Sprite_Mouth_Sad.png"),
                    "StormX.Mouth == 'smile'", Recolor("Storm", "Lips", "images/StormSprite/Storm_Sprite_Mouth_Smile.png"),
                    "StormX.Mouth == 'surprised'", Recolor("Storm", "Lips", "images/StormSprite/Storm_Sprite_Mouth_Kiss.png"),
                    "StormX.Mouth == 'tongue'", Recolor("Storm", "Lips", "images/StormSprite/Storm_Sprite_Mouth_Tongue.png"),
                    "StormX.Mouth == 'grimace'", Recolor("Storm", "Lips", "images/StormSprite/Storm_Sprite_Mouth_Smile.png"),
                    "StormX.Mouth == 'smirk'", Recolor("Storm", "Lips", "images/StormSprite/Storm_Sprite_Mouth_Smirk.png"),
                    "True", Recolor("Storm", "Lips", "images/StormSprite/Storm_Sprite_Mouth_Normal.png"),
                    ),
            ),
        (0,0), ConditionSwitch(
            #Mouths spunk
            "'mouth' not in StormX.Spunk or not Player.Male", Null(),
#            "StormX.Mouth == 'normal'", "images/StormSprite/Storm_Sprite_Spunk_Smirk.png",
#            "StormX.Mouth == 'lipbite'", "images/StormSprite/Storm_Sprite_Spunk_Smirk.png",
            "StormX.Mouth == 'sucking' or StormX.Mouth == 'open'", "images/StormSprite/Storm_Sprite_Spunk_Tongue.png",
            "StormX.Mouth == 'kiss'", "images/StormSprite/Storm_Sprite_Spunk_Kiss.png",
            "StormX.Mouth == 'sad'", "images/StormSprite/Storm_Sprite_Spunk_Sad.png",
            "StormX.Mouth == 'smile'", "images/StormSprite/Storm_Sprite_Spunk_Smile.png",
            "StormX.Mouth == 'surprised'", "images/StormSprite/Storm_Sprite_Spunk_Kiss.png",
            "StormX.Mouth == 'tongue'", "images/StormSprite/Storm_Sprite_Spunk_Tongue.png",
#            "StormX.Mouth == 'grimace'", "images/StormSprite/Storm_Sprite_Mouth_Smile_Spunk.png",
#            "StormX.Mouth == 'smirk'", "images/StormSprite/Storm_Sprite_Mouth_Smirk_Spunk.png",
            "True", "images/StormSprite/Storm_Sprite_Spunk_Smirk.png",
            ),

        (0,0), ConditionSwitch(
            #wet face
            "Player.Male", Null(),
            "'mouth' not in StormX.Spunk and 'chin' not in StormX.Spunk", Null(),
            "'chin' not in StormX.Spunk and StormX.Mouth == 'tongue'", "images/StormSprite/Storm_Sprite_Wet_Tongue.png",
            "StormX.Mouth == 'tongue'", "images/StormSprite/Storm_Sprite_Wet_Tongue2.png",
            "'chin' in StormX.Spunk", "images/StormSprite/Storm_Sprite_Wet_Mouth.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #brows
            "StormX.Brows == 'angry'", "images/StormSprite/Storm_Sprite_Brows_Angry.png",
            "StormX.Brows == 'sad'", "images/StormSprite/Storm_Sprite_Brows_Sad.png",
            "StormX.Brows == 'surprised'", "images/StormSprite/Storm_Sprite_Brows_Surprised.png",
            "StormX.Brows == 'confused'", "images/StormSprite/Storm_Sprite_Brows_Confused.png",
            "True", "images/StormSprite/Storm_Sprite_Brows_Normal.png",
            ),
        (0,0), "Storm Blink",     #Eyes
        (0,0), ConditionSwitch(
            #Face Water
            "not StormX.Water and not (not Player.Male and 'facial' in StormX.Spunk)", Null(),
            "True", "images/StormSprite/Storm_Sprite_Head_Water.png",
            ),
        (0,0), "images/StormSprite/Storm_Sprite_Earrings.png",     #Eyes
        (0,0), ConditionSwitch(
            #Hair over
#            "renpy.showing('Storm_TJ_Animation')", Null(),
            "StormX.Over == 'towel'", Null(),
            "StormX.Hair == 'short'", Recolor("Storm", "Hair", "images/StormSprite/Storm_Sprite_Hair_Short.png"),

            "StormX.Hair == 'wethawk'", Recolor("Storm", "Hair", "images/StormSprite/Storm_Sprite_Hair_Mohawk_Wet.png"),
            "StormX.Hair == 'mohawk' and StormX.Water", Recolor("Storm", "Hair", "images/StormSprite/Storm_Sprite_Hair_Mohawk_Wet.png"),
            "StormX.Hair == 'mohawk' and not Player.Male and 'facial' in StormX.Spunk",Recolor("Storm", "Hair", "images/StormSprite/Storm_Sprite_Hair_Mohawk_Wet.png"),
            "StormX.Hair == 'mohawk'", Recolor("Storm", "Hair", "images/StormSprite/Storm_Sprite_Hair_Mohawk.png"),

            "StormX.Hair == 'wet'", Recolor("Storm", "Hair", "images/StormSprite/Storm_Sprite_Hair_Long_Wet.png"),
            "StormX.Hair and StormX.Water", Recolor("Storm", "Hair", "images/StormSprite/Storm_Sprite_Hair_Long_Wet.png"),
            "not Player.Male and 'facial' in StormX.Spunk",Recolor("Storm", "Hair", "images/StormSprite/Storm_Sprite_Hair_Long_Wet.png"),
            "renpy.showing('Storm_SexSprite')", Recolor("Storm", "Hair", "images/StormSprite/Storm_Sprite_Hair_Long_Sex.png"),
            "StormX.Hair", Recolor("Storm", "Hair", "images/StormSprite/Storm_Sprite_Hair_Long.png"),
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            #towel back
            "StormX.Over == 'towel'", "images/StormSprite/Storm_Sprite_Over_Towel.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Hair Water
#            "not StormX.Water", Null(),
#            "True", "images/StormSprite/Storm_Sprite_Head_Wet.png",
##            "True", "images/StormSprite/Storm_Sprite_Hair_Wet.png",
#            ),
        (0,0), ConditionSwitch(
            #facial spunk
            "'hair' in StormX.Spunk and StormX.Hair == 'short' and Player.Male", "images/StormSprite/Storm_Sprite_Spunk_Hair3.png",
            "'hair' in StormX.Spunk and StormX.Hair == 'mohawk' and Player.Male", "images/StormSprite/Storm_Sprite_Spunk_Hair2.png",
            "'hair' in StormX.Spunk and StormX.Hair == 'long' and Player.Male", "images/StormSprite/Storm_Sprite_Spunk_Hair1.png",
            "'facial' in StormX.Spunk and Player.Male", "images/StormSprite/Storm_Sprite_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #earring over short hair
            "StormX.Hair == 'short'", "images/StormSprite/Storm_Sprite_Earrings.png",
            "True", Null(),
            ),
        )
    anchor (0.5, 0.5)
    zoom .47#.48
#    alpha 0.9

image Storm Blink:
    ConditionSwitch(
    "StormX.Eyes == 'sexy'", "images/StormSprite/Storm_Sprite_Eyes_Sexy.png",
    "StormX.Eyes == 'side'", "images/StormSprite/Storm_Sprite_Eyes_Side.png",
    "StormX.Eyes == 'surprised'", "images/StormSprite/Storm_Sprite_Eyes_Surprised.png",
    "StormX.Eyes == 'normal'", "images/StormSprite/Storm_Sprite_Eyes_Normal.png",
    "StormX.Eyes == 'stunned'", "images/StormSprite/Storm_Sprite_Eyes_Stunned.png",
    "StormX.Eyes == 'down'", "images/StormSprite/Storm_Sprite_Eyes_Down.png",
    "StormX.Eyes == 'closed'", "images/StormSprite/Storm_Sprite_Eyes_Closed.png",
    "StormX.Eyes == 'leftside'", "images/StormSprite/Storm_Sprite_Eyes_Leftside.png",
    "StormX.Eyes == 'manic'", "images/StormSprite/Storm_Sprite_Eyes_Normal.png",
    "StormX.Eyes == 'white'", "images/StormSprite/Storm_Sprite_Eyes_White.png",
    "StormX.Eyes == 'squint'", "Storm_Squint",
    "True", "images/StormSprite/Storm_Sprite_Eyes_Normal.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/StormSprite/Storm_Sprite_Eyes_Closed.png"
    .25
    repeat

image Storm_Squint:
    "images/StormSprite/Storm_Sprite_Eyes_Normal.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/StormSprite/Storm_Sprite_Eyes_Sexy.png"
    .25
    repeat



image Storm_Photo:
    "images/StormSprite/StormPhoto.png"


image Storm_Drip_Mask:
    #This is the mask for her drip pattern
    contains:
        "images/StormSprite/Storm_Sprite_WetMask.png"
        offset (-145,-560)#(-225,-560)

image Storm_Drip_MaskP:
    #This is the mask for her drip pattern in panties down mode
    contains:
        "images/StormSprite/Storm_Sprite_WetMaskP.png"
        offset (-145,-560)#(-225,-560)

# End Storm Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#label Storm_Sex_Launch(Line = Trigger):
#            # placeholder
#            return

#label Storm_Sex_Reset:
#            # placeholder
#            return

#label Storm_Doggy_Launch(Line = Trigger):
#            # placeholder
#            return

#label Storm_Doggy_Reset:
#            # placeholder
#            return


#label Storm_BJ_Launch(Line = Trigger):
#            # placeholder
#            return

#label Storm_BJ_Reset:
#            # placeholder
#            return

#label Storm_TJ_Launch(Line = Trigger):
#            # placeholder
#            return

#label Storm_TJ_Reset:
#            # placeholder
#            return

#label Storm_HJ_Launch(Line = Trigger):
#            # placeholder
#            return

#label Storm_HJ_Reset:
#            # placeholder
#            return



# Storm Doggy Compositing ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#image Storm_Doggy_Base = LiveComposite(
image Storm_Doggy_Animation:
    LiveComposite(
        #Base body
        (420,750),
        (0,0), ConditionSwitch(
            #Shows different upper body motion depending on events
            "not Player.Sprite", "Storm_Doggy_Boob_Static",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Storm_Doggy_Boob_Fuck2",
                    "Speed > 1", "Storm_Doggy_Boob_Fuck",
                    "Speed", "Storm_Doggy_Boob_Static",
                    "True", "Storm_Doggy_Boob_Static",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Storm_Doggy_Boob_Fuck2",
                    "Speed > 1", "Storm_Doggy_Boob_Fuck",
                    "True", "Storm_Doggy_Boob_Static",
                    ),
            "True", "Storm_Doggy_Boob_Static",
            ),
        (0,0), ConditionSwitch(
            #Shows different upper body motion depending on events
            "not Player.Sprite", "Storm_Doggy_Body",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Storm_Doggy_Fuck2_Top",
                    "Speed > 1", "Storm_Doggy_Fuck_Top",
                    "Speed", "Storm_Doggy_Anal_Head_Top",
                    "True", "Storm_Doggy_Body",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Storm_Doggy_Fuck2_Top",
                    "Speed > 1", "Storm_Doggy_Fuck_Top",
                    "True", "Storm_Doggy_Body",
                    ),
            "True", "Storm_Doggy_Body",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events
            "not Player.Sprite", "Storm_Doggy_Ass",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Storm_Doggy_Fuck2_Ass",
                    "Speed > 1", "Storm_Doggy_Fuck_Ass",
                    "Speed", "Storm_Doggy_Anal_Head_Ass",
                    "True", "Storm_Doggy_Ass",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Storm_Doggy_Fuck2_Ass",
                    "Speed > 1", "Storm_Doggy_Fuck_Ass",
                    "True", "Storm_Doggy_Ass",
                    ),
            "True", "Storm_Doggy_Ass",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events
#            "not Player.Sprite", "Storm_Doggy_Shins0",
            "Player.Sprite and Player.Cock == 'foot'", ConditionSwitch(
                    "Speed > 1", "Storm_Doggy_Feet2",
                    "Speed", "Storm_Doggy_Feet1",
                    "True", "Storm_Doggy_Feet0",
                    ),
            "ShowFeet", "Storm_Doggy_Shins0",
            "True", Null(),
            ),
        )
    align (0.6,0.0)
#    yoffset 0
# End Base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Storm_Doggy_Body:
    LiveComposite(
        #Upper body
        (420,750),
#        (-40,5), ConditionSwitch(
#            #hair back
#            "StormX.Hair == 'mohawk' or StormX.Hair == 'wethawk'", Null(),
#            "StormX.Hair == 'short'", Null(),
#            "StormX.Water or StormX.Hair == 'wet'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Long_Wet_Back.png"),
#            "not Player.Male and 'facial' in StormX.Spunk",Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Long_Wet_Back.png"),
#            "StormX.Hair == 'long'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Long_Back.png"),
#            "True", Null(),
#            ),
#        (-40,5), ConditionSwitch(
#            #Head
##            "StormX.Blush > 1", "images/StormDoggy/Storm_Doggy_Head_Blush2.png",
##            "StormX.Blush", "images/StormDoggy/Storm_Doggy_Head_Blush.png",
#            "True", "images/StormDoggy/Storm_Doggy_Head.png",
#            ),
#        (-40,5), ConditionSwitch(
#            #Mouth
##            "StormX.Mouth == 'lipbite'", Recolor("Storm", "Lips", "images/StormDoggy/Storm_Doggy_Mouth_Lipbite.png"),
#            "StormX.Mouth == 'kiss'", Recolor("Storm", "Lips", "images/StormDoggy/Storm_Doggy_Mouth_Kiss.png"),
#            "StormX.Mouth == 'sad'", Recolor("Storm", "Lips", "images/StormDoggy/Storm_Doggy_Mouth_Kiss.png"),
#            "StormX.Mouth == 'smile'", Recolor("Storm", "Lips", "images/StormDoggy/Storm_Doggy_Mouth_Open.png"),
##            "StormX.Mouth == 'grimace'", Recolor("Storm", "Lips", "images/StormDoggy/Storm_Doggy_Mouth_Smile.png"),
##            "StormX.Mouth == 'smirk'", Recolor("Storm", "Lips", "images/StormDoggy/Storm_Doggy_Mouth_Smirk.png"),
#            "StormX.Mouth == 'surprised'", Recolor("Storm", "Lips", "images/StormDoggy/Storm_Doggy_Mouth_Open.png"),
#            "StormX.Mouth == 'sucking'", Recolor("Storm", "Lips", "images/StormDoggy/Storm_Doggy_Mouth_Open.png"),
#            "StormX.Mouth == 'tongue'", Recolor("Storm", "Lips", "images/StormDoggy/Storm_Doggy_Mouth_Tongue.png"),
#            "True", Recolor("Storm", "Lips", "images/StormDoggy/Storm_Doggy_Mouth_Normal.png"),
#            ),
#        (-40,5), ConditionSwitch(
#            #Mouth spunk
#            "'mouth' not in StormX.Spunk or not Player.Male", Null(),
#            "StormX.Mouth == 'surprised'", "images/StormDoggy/Storm_Doggy_Spunk_Open.png",
#            "StormX.Mouth == 'sucking'", "images/StormDoggy/Storm_Doggy_Spunk_Open.png",
#            "StormX.Mouth == 'tongue'", "images/StormDoggy/Storm_Doggy_Spunk_Open.png",
#            "True", "images/StormDoggy/Storm_Doggy_Spunk_Mouth.png",
#            ),
##        (-40,5), ConditionSwitch(
##            #chin spunk
##            "'chin' in StormX.Spunk", "images/JeanDoggy/Jean_Doggy_Spunk_Chin.png",
##            "True", Null(),
##            ),
#        (-40,5), ConditionSwitch(
#            #Brows
#            "StormX.Brows == 'angry'", "images/StormDoggy/Storm_Doggy_Brows_Angry.png",
#            "StormX.Brows == 'sad'", "images/StormDoggy/Storm_Doggy_Brows_Sad.png",
#            "StormX.Brows == 'surprised'", "images/StormDoggy/Storm_Doggy_Brows_Surprised.png",
#            "True", "images/StormDoggy/Storm_Doggy_Brows_Normal.png",
#            ),
#        (-40,5), "Storm Doggy Blink",#Eyes
#        (-40,5), ConditionSwitch(
#            #Hair
##            "StormX.Water or StormX.Hair == 'wet'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Long_Wet_Over.png"),
#            "StormX.Water and StormX.Hair == 'short'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Short_Wet.png"),
#            "(StormX.Water and StormX.Hair == 'mohawk') or StormX.Hair == 'wethawk'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Mohawk_Wet.png"),
##            "StormX.Water or StormX.Hair == 'wet'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Long_Wet_Over.png"),
#            "StormX.Hair == 'short'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Short.png"),
#            "StormX.Hair == 'mohawk'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Mohawk.png"),
##            "True", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Long_Over.png"),

##            "StormX.Water or StormX.Hair == 'wet'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Long_Wet_Over.png"),
##            "StormX.Hair == 'long'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Long_Over.png"),
#            "True", Null(),
#            ),
#        #End head

        (-40,5), ConditionSwitch(
            #head
            "StormX.Facing", "Storm_Doggy_Head_Fore",
            "True", "Storm_Doggy_Head",
            ),

#        (0,0), "images/StormDoggy/Storm_Doggy_BoobRef.png", #Body base
#        (-12,0), "Storm_Doggy_Head",               #Head(165,0)
        (0,0), "images/StormDoggy/Storm_Doggy_Body.png", #Body base

        (0,0), ConditionSwitch(
            #bra
#            "StormX.Uptop", ConditionSwitch(
#                    "StormX.Over and StormX.Over != 'towel'", Null(),
#                    "StormX.Chest == 'cami'", "images/StormDoggy/Storm_Doggy_Bra_Cami_Up.png",
#                    "StormX.Chest == 'lace bra'", "images/StormDoggy/Storm_Doggy_Bra_Lace.png",
#                    "StormX.Chest == 'sports bra'", "images/StormDoggy/Storm_Doggy_Bra_Sport_Up.png",
#                    "StormX.Chest == 'bikini top'", "images/StormDoggy/Storm_Doggy_Bra_Bikini_Up.png",
#                    "True", "images/StormDoggy/Storm_Doggy_Bra.png",
#                    ),
            "StormX.Chest == 'black bra'", Recolor("Storm", "Chest", "images/StormDoggy/Storm_Doggy_Chest_Bra.png"),
            "StormX.Chest == 'lace bra'", Recolor("Storm", "Chest", "images/StormDoggy/Storm_Doggy_Chest_Bra.png"),
            "StormX.Chest == 'cos bra'", Recolor("Storm", "Chest", "images/StormDoggy/Storm_Doggy_Chest_Cos.png"),
            "StormX.Chest == 'tube top'", Recolor("Storm", "Chest", "images/StormDoggy/Storm_Doggy_Chest_Tube.png"),
            "StormX.Chest == 'sports bra'", Recolor("Storm", "Chest", "images/StormDoggy/Storm_Doggy_Chest_Sport.png"),
            "StormX.Chest == 'bikini top'", Recolor("Storm", "Chest", "images/StormDoggy/Storm_Doggy_Chest_Bikini.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "StormX.Water", "images/StormDoggy/Storm_Doggy_Water_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Overshirt
            "StormX.Over == 'white shirt'", Recolor("Storm", "Over", "images/StormDoggy/Storm_Doggy_Over_WhiteShirt.png"),
            "StormX.Over == 'jacket'", Recolor("Storm", "Over", "images/StormDoggy/Storm_Doggy_Over_Jacket.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #arm rings
            "StormX.Over == 'jacket'", Null(),
            "StormX.Acc == 'rings'", "images/StormDoggy/Storm_Doggy_ArmRings.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #neck
            "StormX.Over == 'jacket'", Null(),
            "StormX.Neck == 'rings'", "images/StormDoggy/Storm_Doggy_Necklace3.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk back Layer
            "'back' in StormX.Spunk and Player.Male", "images/StormDoggy/Storm_Doggy_Spunk_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast fondling animation
            "Trigger == 'fondle breasts' or Trigger2 == 'fondle breasts'", "Storm_Doggy_GropeBreast",
            "True", Null()
            ),
#        (-40,5), "images/StormDoggy/Storm_Doggy_Head_ref.png",#Eyes
        (-40,5), ConditionSwitch(
            #Hair over
#            "StormX.Water or StormX.Hair == 'wet'", "images/StormDoggy/Storm_Doggy_Hair_Wet_Back.png",
#            "StormX.Water and StormX.Hair == 'short'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Short_Wet.png"),
#            "(StormX.Water and StormX.Hair == 'mohawk') or StormX.Hair == 'wethawk'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Mohawk_Wet.png"),
#            "StormX.Water or StormX.Hair == 'wet'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Long_Wet_Over.png"),
#            "StormX.Hair == 'short'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Short.png"),
#            "StormX.Hair == 'mohawk'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Mohawk.png"),
#            "True", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Long_Over.png"),

            "((StormX.Water and StormX.Hair == 'long') or StormX.Hair == 'wet') and StormX.Facing", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Long_Wet_Fore.png"),
            "StormX.Hair == 'long' and StormX.Facing", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Long_Fore.png"),
            "StormX.Facing", Null(),
            "(StormX.Water and StormX.Hair == 'long') or StormX.Hair == 'wet'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Long_Wet_Over.png"),
            "StormX.Hair == 'long' and not Player.Male and 'facial' in StormX.Spunk",Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Long_Wet_Over.png"),
            "StormX.Hair == 'long'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Long_Over.png"),
            "True", Null(),
            ),
        (-40,5), ConditionSwitch(
            #earring
            "StormX.Facing", Null(),
            "(StormX.Water and StormX.Hair == 'long') or StormX.Hair == 'wet'", "images/StormDoggy/Storm_Doggy_Earring_Wet.png",
            "True", "images/StormDoggy/Storm_Doggy_Earring.png",
            ),

        (-40,5), ConditionSwitch(
            #face spunk
#            "'hair' in StormX.Spunk", "images/StormDoggy/Storm_Doggy_Spunk_Hair.png",
            "StormX.Facing", Null(),
            "'facial' in StormX.Spunk and Player.Male", "images/StormDoggy/Storm_Doggy_Spunk_Facial.png",
            "True", Null(),
            ),
        )
#    transform_anchor True
#    anchor (225,1400)
    offset (-20,0)#(-30,0)#(-190,-40)
#    rotate 20
# End body animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Storm_Doggy_Head:
    LiveComposite(
        #Head
        (420,750),
        (0,0), ConditionSwitch(
            #hair back
            "StormX.Water or StormX.Hair == 'wet'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Long_Wet_Back.png"),
            "StormX.Hair == 'short'", Null(),
            "StormX.Hair == 'mohawk'", Null(),
            "True", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Long_Back.png"),
            ),
        (0,0), ConditionSwitch(
            #Head
#            "StormX.Blush > 1", "images/StormDoggy/Storm_Doggy_Head_Blush2.png",
#            "StormX.Blush", "images/StormDoggy/Storm_Doggy_Head_Blush.png",
            "True", "images/StormDoggy/Storm_Doggy_Head.png",
            ),
        (0,0), ConditionSwitch(
            #Mouth
#            "StormX.Mouth == 'lipbite'", Recolor("Storm", "Lips", "images/StormDoggy/Storm_Doggy_Mouth_Lipbite.png"),
            "StormX.Mouth == 'kiss'", Recolor("Storm", "Lips", "images/StormDoggy/Storm_Doggy_Mouth_Kiss.png"),
            "StormX.Mouth == 'sad'", Recolor("Storm", "Lips", "images/StormDoggy/Storm_Doggy_Mouth_Kiss.png"),
            "StormX.Mouth == 'smile'", Recolor("Storm", "Lips", "images/StormDoggy/Storm_Doggy_Mouth_Open.png"),
#            "StormX.Mouth == 'grimace'", Recolor("Storm", "Lips", "images/StormDoggy/Storm_Doggy_Mouth_Smile.png"),
#            "StormX.Mouth == 'smirk'", Recolor("Storm", "Lips", "images/StormDoggy/Storm_Doggy_Mouth_Smirk.png"),
            "StormX.Mouth == 'surprised'", Recolor("Storm", "Lips", "images/StormDoggy/Storm_Doggy_Mouth_Open.png"),
            "StormX.Mouth == 'sucking'", Recolor("Storm", "Lips", "images/StormDoggy/Storm_Doggy_Mouth_Open.png"),
            "StormX.Mouth == 'tongue'", Recolor("Storm", "Lips", "images/StormDoggy/Storm_Doggy_Mouth_Tongue.png"),
            "True", Recolor("Storm", "Lips", "images/StormDoggy/Storm_Doggy_Mouth_Normal.png"),
            ),
#        (0,0), ConditionSwitch(
#            #chin spunk
#            "'chin' in StormX.Spunk", "images/JeanDoggy/Jean_Doggy_Spunk_Chin.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #Mouth spunk
#            "'mouth' not in StormX.Spunk", Null(),
#            #"StormX.Mouth == 'normal'", "images/StormDoggy/Storm_Doggy_Spunk_Normal.png",
#            #"StormX.Mouth == 'sad'", "images/StormDoggy/Storm_Doggy_Spunk_Normal.png",
##            "StormX.Mouth == 'lipbite'", "images/StormDoggy/Storm_Doggy_Spunk_Smile.png",
#            "StormX.Mouth == 'smile'", "images/StormDoggy/Storm_Doggy_Head_Spunk_Smile.png",
#            "StormX.Mouth == 'grimace'", "images/StormDoggy/Storm_Doggy_Head_Spunk_Smile.png",
#            "StormX.Mouth == 'sucking'", "images/StormDoggy/Storm_Doggy_Head_Spunk_Tongue.png",
#            #"StormX.Mouth == 'kiss'", "images/StormDoggy/Storm_Doggy_Spunk_Open.png",
##            "StormX.Mouth == 'surprised'", "images/StormDoggy/Storm_Doggy_Spunk_Normal.png",
#            "StormX.Mouth == 'tongue'", "images/StormDoggy/Storm_Doggy_Head_Spunk_Tongue.png",
#            "True", "images/StormDoggy/Storm_Doggy_Head_Spunk_Normal.png",
#            ),
        (0,0), ConditionSwitch(
            #Brows
            "StormX.Brows == 'angry'", "images/StormDoggy/Storm_Doggy_Brows_Angry.png",
            "StormX.Brows == 'sad'", "images/StormDoggy/Storm_Doggy_Brows_Sad.png",
            "StormX.Brows == 'surprised'", "images/StormDoggy/Storm_Doggy_Brows_Surprised.png",
            "True", "images/StormDoggy/Storm_Doggy_Brows_Normal.png",
            ),
        (0,0), "Storm Doggy Blink",#Eyes
#        (0,0), ConditionSwitch(
#            #wet hair strand
#            "StormX.Water or StormX.Hair == 'wet'", "images/JeanDoggy/Jean_Doggy_Hair_Wet_Under.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Hair
#            "StormX.Water or StormX.Hair == 'wet'", "images/StormDoggy/Storm_Doggy_Hair_Wet_Back.png",
            "StormX.Water and StormX.Hair == 'short'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Short_Wet.png"),
            "StormX.Hair == 'short' and not Player.Male and 'facial' in StormX.Spunk",Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Short_Wet.png"),
            "(StormX.Water and StormX.Hair == 'mohawk') or StormX.Hair == 'wethawk'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Mohawk_Wet.png"),
            "StormX.Hair == 'mohawk' and not Player.Male and 'facial' in StormX.Spunk",Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Mohawk_Wet.png"),
            "StormX.Water or StormX.Hair == 'wet'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Long_Wet_Over.png"),
            "not Player.Male and 'facial' in StormX.Spunk",Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Long_Wet_Over.png"),
            "StormX.Hair == 'short'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Short.png"),
            "StormX.Hair == 'mohawk'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Mohawk.png"),
            "True", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Long_Over.png"),
            ),
#        (0,0), ConditionSwitch(
#            #Wet look
#            "StormX.Water", "images/StormDoggy/Storm_Doggy_Head_Wet.png",
#            "True", Null(),
#            ),
#        (0,0), "images/StormDoggy/Storm_Doggy_Head_Bodyref.png",
        )
#    zoom 0.83 #.83
    #alpha 0.9
# End Head animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Storm_Doggy_Head_Fore:
    LiveComposite(
        #Head
        (420,750),
        (0,0), ConditionSwitch(
            #hair back
            "StormX.Hair == 'mohawk' and StormX.Water", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Mohawk_Wet_Fore.png"),
            "StormX.Hair == 'wethawk'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Mohawk_Wet_Fore.png"),
#            "StormX.Water or StormX.Hair == 'wet'", "images/StormDoggy/Storm_Doggy_Hair_Wet_Back.png",
            "StormX.Hair == 'short'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Short_Fore.png"),
            "StormX.Hair == 'mohawk'", Recolor("Storm", "Hair", "images/StormDoggy/Storm_Doggy_Hair_Mohawk_Fore.png"),
            "True", Null(),
            ),
        )
#    zoom 0.83 #.83
    #alpha 0.9
# End Head forward animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm Doggy Blink:
        #Eyes
        ConditionSwitch(
#        "StormX.Eyes == 'sexy'", "images/StormDoggy/Storm_Doggy_Eyes_Sexy.png",
        "StormX.Eyes == 'side'", "images/StormDoggy/Storm_Doggy_Eyes_Side.png",
#        "StormX.Eyes == 'normal'", "images/StormDoggy/Storm_Doggy_Eyes_Normal.png",
        "StormX.Eyes == 'closed'", "images/StormDoggy/Storm_Doggy_Eyes_Closed.png",
#        "StormX.Eyes == 'manic'", "images/StormDoggy/Storm_Doggy_Eyes_Normal.png",
#        "StormX.Eyes == 'down'", "images/StormDoggy/Storm_Doggy_Eyes_Down.png",
        "StormX.Eyes == 'stunned'", "images/StormDoggy/Storm_Doggy_Eyes_Stunned.png",
        "StormX.Eyes == 'surprised'", "images/StormDoggy/Storm_Doggy_Eyes_Surprised.png",
#        "StormX.Eyes == 'squint'", "images/StormDoggy/Storm_Doggy_Eyes_Sexy.png",
        "True", "images/StormDoggy/Storm_Doggy_Eyes_Normal.png",
        ),
    #    choice:
    #        3.5
    #    choice:
    #        3.25
    #    choice:
    #        3
        3
        # This randomizes the time between blinking.
        "images/StormDoggy/Storm_Doggy_Eyes_Closed.png"
        .25
        repeat

image Storm_Doggy_Ass:
    LiveComposite(
        #Lower body
        (420,750),

        (0,0), ConditionSwitch(
            #Panties backside if Down
            "not StormX.PantiesDown or (StormX.Legs and StormX.Legs != 'skirt' and not StormX.Upskirt)", Null(),
            "StormX.Panties == 'cos panties'", Recolor("Storm", "Panties", "images/StormDoggy/Storm_Doggy_Panties_Cos_Under.png"),
            "StormX.Panties == 'white panties'", Recolor("Storm", "Panties", "images/StormDoggy/Storm_Doggy_Panties_White_Under.png"),
            "StormX.Panties == 'bikini bottoms'", Recolor("Storm", "Panties", "images/StormDoggy/Storm_Doggy_Panties_Black_Under.png"),
            "StormX.Panties == 'lace panties'",Recolor("Storm", "Panties", "images/StormDoggy/Storm_Doggy_Panties_Lace_Under.png"),
            "StormX.Panties",Recolor("Storm", "Panties", "images/StormDoggy/Storm_Doggy_Panties_Black_Under.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #New ass base check
            "Trigger == 'lick pussy'", "images/StormDoggy/Storm_Doggy_Ass_Open.png",
            "StormX.Legs and not StormX.Upskirt", "images/StormDoggy/Storm_Doggy_Ass_Closed.png",
            "StormX.Panties and not StormX.PantiesDown", "images/StormDoggy/Storm_Doggy_Ass_Closed.png",
            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
#                    "Speed > 2", "Storm_Pussy_Fucking3",#Speed 3
#                    "Speed > 1", "Storm_Pussy_Fucking2",#Speed 2
                    "Speed", "images/StormDoggy/Storm_Doggy_Ass_Fucking.png",      #Speed 1
                    "True", "images/StormDoggy/Storm_Doggy_Ass_Fucking.png",              #Speed 0
                    ),
            "'dildo pussy' in (Trigger,Trigger2,StormX.Offhand)", "images/StormDoggy/Storm_Doggy_Ass_Fucking.png",
            "'fondle pussy' in (Trigger,Trigger2,StormX.Offhand)", "images/StormDoggy/Storm_Doggy_Ass_Fucking.png",
            "Trigger == 'insert pussy'", "images/StormDoggy/Storm_Doggy_Ass_Fucking.png",
            "True", "images/StormDoggy/Storm_Doggy_Ass_Closed.png",
            ),

        (0,0), ConditionSwitch(
            #ass red
            "StormX.Red", "images/StormDoggy/Storm_Doggy_Red.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "StormX.Water", "images/StormDoggy/Storm_Doggy_Water_Ass.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #Hose
            "StormX.Hose == 'stockings'", Recolor("Storm", "Hose", "images/StormDoggy/Storm_Doggy_Hose_Stockings.png"),
            "StormX.Hose == 'garterbelt'", Recolor("Storm", "Hose", "images/StormDoggy/Storm_Doggy_Hose_Garter.png"),
            "StormX.Hose == 'stockings and garterbelt'", Recolor("Storm", "Hose", "images/StormDoggy/Storm_Doggy_Hose_StockingGarter.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Panties if Down
            "not StormX.PantiesDown or (StormX.Legs and StormX.Legs != 'skirt' and not StormX.Upskirt)", Null(),
            "StormX.Panties == 'cos panties'", Recolor("Storm", "Panties", "images/StormDoggy/Storm_Doggy_Panties_Cos_Down.png"),
            "StormX.Panties == 'white panties'", Recolor("Storm", "Panties", "images/StormDoggy/Storm_Doggy_Panties_White_Down.png"),
            "StormX.Panties == 'bikini bottoms'", Recolor("Storm", "Panties", "images/StormDoggy/Storm_Doggy_Panties_Black_Down.png"),
            "StormX.Panties == 'lace panties'",Recolor("Storm", "Panties", "images/StormDoggy/Storm_Doggy_Panties_Black_Down.png"),
            "StormX.Panties",Recolor("Storm", "Panties", "images/StormDoggy/Storm_Doggy_Panties_Black_Down.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Legs Layer if down
            "StormX.Legs == 'pants' and StormX.Upskirt", Recolor("Storm", "Legs", "images/StormDoggy/Storm_Doggy_Legs_Pants_Down.png"),
#            "StormX.Legs == 'yoga pants' and StormX.Upskirt", Recolor("Storm", "Legs", "images/StormDoggy/Storm_Doggy_Legs_Yoga_Down.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #spunkpussy Layer
            "'in' in StormX.Spunk and Player.Cock == 'in' and Player.Male",Null(),# "images/JeanDoggy/Jean_Doggy_SpunkPussyOpen.png",  #fix for StormX.Spunk is used later
            "'in' in StormX.Spunk and Player.Male", "images/JeanDoggy/Jean_Doggy_SpunkPussyClosed.png",
#            "StormX.Wet and Player.Cock == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "StormX.Wet", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pubes
            "not StormX.Pubes", Null(),
            "Player.Sprite and Player.Cock == 'in'", Null(), # "images/StormDoggy/Storm_Doggy_Pubes_Fucked.png",
            "'dildo pussy' in (Trigger,Trigger2,StormX.Offhand)", Null(),
            "'fondle pussy' in (Trigger,Trigger2,StormX.Offhand)",Null(),
            "Trigger == 'insert pussy'", Null(),
            "(StormX.Legs and StormX.Legs != 'skirt') and not StormX.Upskirt", Null(),
            "StormX.PantiesDown and Trigger == 'lick pussy'", Recolor("Storm", "Pubes", "images/StormDoggy/Storm_Doggy_Pubes_Open.png"),
            "StormX.Panties and StormX.PantiesDown", Recolor("Storm", "Pubes", "images/StormDoggy/Storm_Doggy_Pubes_Closed.png"),
            "StormX.Panties", Recolor("Storm", "Pubes", "images/StormDoggy/Storm_Doggy_Pubes_ClosedC.png"),
            "StormX.Hose == 'pantyhose' and Trigger == 'lick pussy'", Recolor("Storm", "Pubes", "images/StormDoggy/Storm_Doggy_Pubes_OpenC.png"),
            "StormX.Hose == 'pantyhose'", Recolor("Storm", "Pubes", "images/StormDoggy/Storm_Doggy_Pubes_ClosedC.png"),
            "Trigger == 'lick pussy'", Recolor("Storm", "Pubes", "images/StormDoggy/Storm_Doggy_Pubes_Open.png"),
            "True", Recolor("Storm", "Pubes", "images/StormDoggy/Storm_Doggy_Pubes_Closed.png"),
            ),

        (0,0), ConditionSwitch( #remove later if works                                                                                #remove later if works
            #New ass base check
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 1", "images/StormDoggy/Storm_Doggy_Anal_FullBase.png",
            "'insert ass' in (Trigger,Trigger2,StormX.Offhand)", "images/StormDoggy/Storm_Doggy_Anal_FullBase.png",
            "'dildo anal' in (Trigger,Trigger2,StormX.Offhand)", "images/StormDoggy/Storm_Doggy_Anal_FullBase.png",
            "renpy.showing('Anal_Plug_In_Doggy') or renpy.showing('Anal_Plug_Out_Doggy')", "images/StormDoggy/Storm_Doggy_Anal_FullBase.png",
            "StormX.Plug", "images/StormDoggy/Storm_Doggy_Anal_PlugPlate.png",
#            "StormX.Legs and not StormX.Upskirt", "images/StormDoggy/Storm_Doggy_Asshole_Loose.png",
#            "StormX.Panties and not StormX.PantiesDown", "images/StormDoggy/Storm_Doggy_Asshole_Loose.png",
#            "StormX.Loose", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
#            "True", "images/JeanDoggy/Jean_Doggy_Asshole_Tight.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #spunkanal Layer
            "'anal' not in StormX.Spunk or (Player.Sprite and Speed) or not Player.Male", Null(),
#            "Player.Cock == 'anal'", "images/RogueDoggy/Rogue_Doggy_SpunkAnalOpen.png",
#            "StormX.Loose", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png",
            "True", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png",
            ),

        (0,0), ConditionSwitch(
            #Panties if up
            "StormX.PantiesDown or not StormX.Panties", Null(),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),
            "StormX.Panties == 'cos panties' and StormX.Wet", Recolor("Storm", "Panties", "images/StormDoggy/Storm_Doggy_Panties_CosW.png"),
            "StormX.Panties == 'cos panties'", Recolor("Storm", "Panties", "images/StormDoggy/Storm_Doggy_Panties_Cos.png"),
            "StormX.Panties == 'lace panties'", Recolor("Storm", "Panties", "images/StormDoggy/Storm_Doggy_Panties_Lace.png"),
            "StormX.Panties == 'white panties' and StormX.Wet", Recolor("Storm", "Panties", "images/StormDoggy/Storm_Doggy_Panties_WhiteW.png"),
            "StormX.Panties == 'white panties'", Recolor("Storm", "Panties", "images/StormDoggy/Storm_Doggy_Panties_White.png"),
            "StormX.Panties == 'bikini bottoms'", Recolor("Storm", "Panties", "images/StormDoggy/Storm_Doggy_Panties_Black.png"),
            "StormX.Wet", Recolor("Storm", "Panties", "images/StormDoggy/Storm_Doggy_Panties_BlackW.png"),
            "True", Recolor("Storm", "Panties", "images/StormDoggy/Storm_Doggy_Panties_Black.png"),
            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #full hose/tights
#            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),
#            "StormX.Panties and StormX.PantiesDown and StormX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
#            "StormX.Hose == 'garterbelt'", Recolor("Storm", "Hose", "images/StormDoggy/Storm_Doggy_Hose_Garter.png"),
#            "StormX.Hose == 'stockings and garterbelt'", Recolor("Storm", "Hose", "images/StormDoggy/Storm_Doggy_Hose_StockingGarter.png"),
            "StormX.Panties and StormX.PantiesDown", Null(),
            "StormX.Hose == 'pantyhose'", Recolor("Storm", "Hose", "images/StormDoggy/Storm_Doggy_Hose_Full.png"),
            "StormX.Hose == 'ripped pantyhose'", Recolor("Storm", "Hose", "images/StormDoggy/Storm_Doggy_Hose_Full_Holed.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Legs Layer
            "StormX.Legs == 'pants'", ConditionSwitch(
#                    "StormX.Upskirt", Null(),
                    "StormX.Upskirt", Recolor("Storm", "Legs", "images/StormDoggy/Storm_Doggy_Legs_Pants_Down.png"),
                    "StormX.Wet > 1", Recolor("Storm", "Legs", "images/StormDoggy/Storm_Doggy_Legs_Pants_W.png"),
                    "True", Recolor("Storm", "Legs", "images/StormDoggy/Storm_Doggy_Legs_Pants.png"),
                    ),
            "StormX.Legs == 'yoga pants'", ConditionSwitch(
#                    "StormX.Upskirt", Null(),
                    "StormX.Upskirt", Recolor("Storm", "Legs", "images/StormDoggy/Storm_Doggy_Legs_Yoga_Down.png"),
                    "StormX.Wet > 1", Recolor("Storm", "Legs", "images/StormDoggy/Storm_Doggy_Legs_Yoga_W.png"),
                    "True", Recolor("Storm", "Legs", "images/StormDoggy/Storm_Doggy_Legs_Yoga.png"),
                    ),

            "StormX.Legs == 'skirt'", ConditionSwitch(
                    "Player.Sprite and Player.Cock == 'anal' and Speed" , Recolor("Storm", "Legs", "images/StormDoggy/Storm_Doggy_Legs_Skirt_Up.png"),
                    "StormX.Upskirt", Recolor("Storm", "Legs", "images/StormDoggy/Storm_Doggy_Legs_Skirt_Up.png"),
                    "True", Recolor("Storm", "Legs", "images/StormDoggy/Storm_Doggy_Legs_Skirt.png"),
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Pussy Piercings over clothes
            "Player.Sprite and Player.Cock == 'in'", Null(),
            "'dildo pussy' in (Trigger,Trigger2,StormX.Offhand)", Null(),
            "'fondle pussy' in (Trigger,Trigger2,StormX.Offhand)",Null(),
            "Trigger == 'insert pussy'", Null(),
            "StormX.Legs == 'skirt' and not StormX.Upskirt", Null(),
            "StormX.Pierce == 'barbell'",  ConditionSwitch(
                    #pants if not down
                    "StormX.Legs == 'pants' and not StormX.Upskirt", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy_Black.png",
                    "StormX.Legs == 'yoga pants' and not StormX.Upskirt", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy_White.png",
                    #panties if not down
                    "StormX.PantiesDown", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy.png",
                    "StormX.Panties == 'white panties'", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy_White.png",
                    "StormX.Panties == 'cos panties'", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy_White.png",
                    "StormX.Panties == 'bikini bottoms'", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy_Black.png",
                    "StormX.Panties == 'lace panties'", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy_Lace.png",
                    "StormX.Panties", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy_Black.png",
                    "StormX.Hose == 'pantyhose'", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy_Lace.png",
                    "True", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy.png",
                    ),
            "StormX.Pierce == 'ring'",  ConditionSwitch(
                    #pants if not down
                    "StormX.Legs == 'pants' and not StormX.Upskirt", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy_Black.png",
                    "StormX.Legs == 'yoga pants' and not StormX.Upskirt", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy_White.png",
                    #panties if not down
                    "StormX.PantiesDown", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy.png",
                    "StormX.Panties == 'white panties'", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy_White.png",
                    "StormX.Panties == 'cos panties'", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy_White.png",
                    "StormX.Panties == 'bikini bottoms'", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy_Black.png",
                    "StormX.Panties == 'lace panties'", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy_Lace.png",
                    "StormX.Panties", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy_Black.png",
                    #hose up
                    "StormX.Hose == 'pantyhose'", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy_Lace.png",
                    "True", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy.png",
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Pussy Composite
            "StormX.Legs and not StormX.Upskirt",Null(),
            "StormX.Panties and not StormX.PantiesDown", Null(),
            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Storm_Pussy_Fucking3",#Speed 3
                    "Speed > 1", "Storm_Pussy_Fucking2",#Speed 2
                    "Speed", "Storm_Pussy_Heading",      #Speed 1
                    "True", "Storm_Pussy_Static",              #Speed 0
                    ),
            "'dildo pussy' in (Trigger,Trigger2,StormX.Offhand)", "Storm_Pussy_Fucking2",
            "'fondle pussy' in (Trigger,Trigger2,StormX.Offhand)", "Storm_Pussy_Fingering",
            "Trigger == 'insert pussy'", "Storm_Pussy_Fingering",
            "True",Null(),
            ),

        (0,0), ConditionSwitch(
            #Anus Composite
            "StormX.Legs and not StormX.Upskirt",Null(),
            "StormX.Panties and not StormX.PantiesDown", Null(),
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Storm_Anal_Fucking2", #Speed 3
                    "Speed > 1", "Storm_Anal_Fucking",  #Speed 2
                    "Speed", "Storm_Anal_Heading",      #Speed 1
                    "True", "Storm_Anal",               #Speed 0
                    ),
            "'insert ass' in (Trigger,Trigger2,StormX.Offhand)", "Storm_Anal_Fingering",
            "'dildo anal' in (Trigger,Trigger2,StormX.Offhand)", "Storm_Anal_Fucking",
            "StormX.Plug", "images/PlugIn.png",
            "StormX.Loose > 2", "Storm_Gape_Anal",
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #Pussy Piercings over clothes
#            "Player.Sprite", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),
#            "StormX.Legs == 'skirt' and not StormX.Upskirt", Null(),
#            "StormX.Pierce == 'barbell'",  ConditionSwitch(
#                    #pants if not down
#                    "StormX.Legs == 'pants' and not StormX.Upskirt", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy_Black.png",
#                    "StormX.Legs == 'yoga pants' and not StormX.Upskirt", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy_White.png",
#                    #panties if not down
#                    "StormX.PantiesDown", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy.png",
#                    "StormX.Panties == 'white panties'", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy_White.png",
#                    "StormX.Panties == 'cos panties'", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy_White.png",
#                    "StormX.Panties == 'bikini bottoms'", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy_Black.png",
#                    "StormX.Panties == 'lace panties'", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy_Lace.png",
#                    "StormX.Panties", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy_Black.png",
#                    "StormX.Hose == 'pantyhose'", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy_Lace.png",
#                    "True", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy.png",
#                    ),
#            "StormX.Pierce == 'ring'",  ConditionSwitch(
#                    #pants if not down
#                    "StormX.Legs == 'pants' and not StormX.Upskirt", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy_Black.png",
#                    "StormX.Legs == 'yoga pants' and not StormX.Upskirt", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy_White.png",
#                    #panties if not down
#                    "StormX.PantiesDown", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy.png",
#                    "StormX.Panties == 'white panties'", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy_White.png",
#                    "StormX.Panties == 'cos panties'", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy_White.png",
#                    "StormX.Panties == 'bikini bottoms'", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy_Black.png",
#                    "StormX.Panties == 'lace panties'", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy_Lace.png",
#                    "StormX.Panties", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy_Black.png",
#                    #hose up
#                    "StormX.Hose == 'pantyhose'", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy_Lace.png",
#                    "True", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy.png",
#                    ),
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy'", "Rogue_Doggy_Lick_Pussy",
            "Trigger == 'lick ass'", "Rogue_Doggy_Lick_Ass",
            "True", Null()
            ),
        (0,0), ConditionSwitch(
            #spunk back Layer
            "'back' in StormX.Spunk and Player.Male", "images/StormDoggy/Storm_Doggy_Spunk_Ass.png",
            "True", Null(),
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


image Storm_Doggy_Feet:
    contains:
            AlphaMask("Storm_Doggy_Shins", "images/StormDoggy/Storm_Doggy_Feet_Mask.png")
    contains:
        #spunk
        ConditionSwitch(
            "'feet' in StormX.Spunk", "images/StormDoggy/Storm_Doggy_Spunk_Feet.png",
            "True", Null(),
            )

image Storm_Doggy_Shins:
    #Storm's footjob shins
    contains:
            #hose legs
        ConditionSwitch(
            "StormX.Hose == 'ripped pantyhose'", Recolor("Storm", "Hose", "images/StormDoggy/Storm_Doggy_Feet_Holed.png"),
            "StormX.Hose and StormX.Hose != 'garterbelt'", Recolor("Storm", "Hose", "images/StormDoggy/Storm_Doggy_Feet_Stockings.png"),
            "True", "images/StormDoggy/Storm_Doggy_Feet.png"
            )
    contains:
        #pants
        ConditionSwitch(
            "StormX.Legs == 'pants'", Recolor("Storm", "Legs", "images/StormDoggy/Storm_Doggy_Feet_Pants.png"),
            "StormX.Legs == 'yoga pants'", Recolor("Storm", "Legs", "images/StormDoggy/Storm_Doggy_Feet_Yoga.png"),
            "True", Null(),
            )
    contains:
        #spunk
        ConditionSwitch(
            "'feet' in StormX.Spunk", "images/StormDoggy/Storm_Doggy_Spunk_Feet.png",
            "True", Null(),
            )

image Storm_Doggy_Shins_Ghost:
        "Storm_Doggy_Shins"
        alpha 0.5

image Storm_Doggy_Shins0:
        #static animation
        "Storm_Doggy_Shins"
        offset (0, 80) #(0,0) top

image Storm_Doggy_GropeBreast:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        xzoom -.55
        yzoom .55
        offset (90,390)#(110,420)
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
        block:
            ease 1 rotate 10#60
            ease 1 rotate 0#90
            repeat

image Storm_Doggy_Boob:
#    contains:
#        "images/StormDoggy/Storm_Doggy_Boob.png"

#    contains:
#            #bra
#        ConditionSwitch(
#            "StormX.Uptop", ConditionSwitch(
##                    "StormX.Chest == 'corset'", "images/StormDoggy/Storm_Doggy_Bra_Corset_Boob_Down.png",
##                    "StormX.Chest == 'lace bra'", "images/StormDoggy/Storm_Doggy_Bra_Corset_Boob_Down.png",
#                    "StormX.Chest == 'sports bra'", "images/StormDoggy/Storm_Doggy_Bra_Sport_Boob_Down.png",
##                    "StormX.Chest == 'bikini top'", "images/StormDoggy/Storm_Doggy_Bra_Corset_Boob_Down.png",
#                    "StormX.Chest", "images/StormDoggy/Storm_Doggy_Bra_Corset_Boob_Down.png",
#                    "True", Null(),
#                    ),
#            "StormX.Over == 'jacket'", Null(),
#            "StormX.Chest == 'corset'", "images/StormDoggy/Storm_Doggy_Bra_Corset_Boob.png",
#            "StormX.Chest == 'lace bra'", "images/StormDoggy/Storm_Doggy_Bra_Lace_Boob.png",
#            "StormX.Chest == 'sports bra'", "images/StormDoggy/Storm_Doggy_Bra_Sport_Boob.png",
#            "StormX.Chest == 'bikini top'", "images/StormDoggy/Storm_Doggy_Bra_Corset_Boob.png",
#            "True", Null(),
#            )
    contains:
            #when not uptop
        ConditionSwitch(
            "StormX.Uptop", "images/StormDoggy/Storm_Doggy_Boob.png",
            "StormX.Over == 'white shirt' and StormX.Chest in ('black bra','lace bra','sports bra')", Recolor("Storm", "Over", "images/StormDoggy/Storm_Doggy_Boob_White_Up.png"),
            "StormX.Over == 'white shirt'", Recolor("Storm", "Over", "images/StormDoggy/Storm_Doggy_Boob_White.png"),

            "StormX.Chest == 'black bra'", Recolor("Storm", "Chest", "images/StormDoggy/Storm_Doggy_Boob_Bra.png"),
            "StormX.Chest == 'lace bra'", Recolor("Storm", "Chest", "images/StormDoggy/Storm_Doggy_Boob_LaceBra.png"),
            "StormX.Chest == 'sports bra'", Recolor("Storm", "Chest", "images/StormDoggy/Storm_Doggy_Boob_Black_Up.png"),
            "StormX.Chest == 'bikini top'", Recolor("Storm", "Chest", "images/StormDoggy/Storm_Doggy_Boob_Black.png"),
            "StormX.Chest == 'tube top'", Recolor("Storm", "Chest", "images/StormDoggy/Storm_Doggy_Boob_Tube.png"),
            "StormX.Chest == 'cos bra'", Recolor("Storm", "Chest", "images/StormDoggy/Storm_Doggy_Boob_Cos.png"),

            "True", "images/StormDoggy/Storm_Doggy_Boob.png",
            )
#    contains:
#            #Wet look
#        ConditionSwitch(
#            "StormX.Water", "images/StormDoggy/Storm_Doggy_Wet_Boob.png",
#            "True", Null(),
#            )
    contains:
            #piercings
        ConditionSwitch(
            "not StormX.Pierce", Null(),
            "StormX.Uptop", ConditionSwitch(
                    "StormX.Pierce == 'ring'", ConditionSwitch(
                            #ring piercings
                            "True", "images/StormDoggy/Storm_Doggy_Boob_Pierce_Ring.png",
                            ),
                    #if barbell piercings
                    "True", "images/StormDoggy/Storm_Doggy_Boob_Pierce_Ball.png",
                    ),
            #if not uptop
            "StormX.Pierce == 'ring'", ConditionSwitch(
                    #ring piercings
                    "StormX.Over == 'white shirt' and StormX.Chest in ('black bra','lace bra','sports bra')", "images/StormDoggy/Storm_Doggy_Boob_Pierce_Ring_Cream_Up.png",
                    "StormX.Over == 'white shirt'", "images/StormDoggy/Storm_Doggy_Boob_Pierce_Ring_Cream.png",
                    "StormX.Chest == 'black bra'", "images/StormDoggy/Storm_Doggy_Boob_Pierce_Ring_Black_Up.png",
                    "StormX.Chest == 'lace bra'", "images/StormDoggy/Storm_Doggy_Boob_Pierce_Ring_Lace_Up.png",
                    "StormX.Chest == 'sports bra'", "images/StormDoggy/Storm_Doggy_Boob_Pierce_Ring_Black_Up.png",
                    "StormX.Chest == 'bikini top'", "images/StormDoggy/Storm_Doggy_Boob_Pierce_Ring_Black.png",
                    "StormX.Chest == 'tube top'", "images/StormDoggy/Storm_Doggy_Boob_Pierce_Ring_White.png",
                    "StormX.Chest == 'cos bra'", "images/StormDoggy/Storm_Doggy_Boob_Pierce_Ring_White.png",
                    "True", "images/StormDoggy/Storm_Doggy_Boob_Pierce_Ring.png",
                    ),
            "StormX.Over == 'white shirt' and StormX.Chest in ('black bra','lace bra','sports bra')", "images/StormDoggy/Storm_Doggy_Boob_Pierce_Ball_Cream_Up.png",
            "StormX.Over == 'white shirt'", "images/StormDoggy/Storm_Doggy_Boob_Pierce_Ball_Cream.png",
            "StormX.Chest == 'black bra'", "images/StormDoggy/Storm_Doggy_Boob_Pierce_Ball_Black_Up.png",
            "StormX.Chest == 'lace bra'", "images/StormDoggy/Storm_Doggy_Boob_Pierce_Ball_Lace_Up.png",
            "StormX.Chest == 'sports bra'", "images/StormDoggy/Storm_Doggy_Boob_Pierce_Ball_Black_Up.png",
            "StormX.Chest == 'bikini top'", "images/StormDoggy/Storm_Doggy_Boob_Pierce_Ball_Black.png",
            "StormX.Chest == 'tube top'", "images/StormDoggy/Storm_Doggy_Boob_Pierce_Ball_White.png",
            "StormX.Chest == 'cos bra'", "images/StormDoggy/Storm_Doggy_Boob_Pierce_Ball_White.png",
            "True", "images/StormDoggy/Storm_Doggy_Boob_Pierce_Ball.png",
            )

    contains:
            #when uptop
        ConditionSwitch(
            "not StormX.Uptop", Null(),
            "StormX.Over == 'white shirt'", Recolor("Storm", "Over", "images/StormDoggy/Storm_Doggy_Boob_White_Up_Up.png"),

            "StormX.Chest == 'black bra'", Recolor("Storm", "Chest", "images/StormDoggy/Storm_Doggy_Boob_Bra_Up.png"),
            "StormX.Chest == 'lace bra'", Recolor("Storm", "Chest", "images/StormDoggy/Storm_Doggy_Boob_Bra_Up.png"),
            "StormX.Chest == 'sports bra'", Recolor("Storm", "Chest", "images/StormDoggy/Storm_Doggy_Boob_Bikini_Up.png"),
            "StormX.Chest == 'bikini top'", Recolor("Storm", "Chest", "images/StormDoggy/Storm_Doggy_Boob_Bikini_Up.png"),
            "StormX.Chest == 'tube top'", Recolor("Storm", "Chest", "images/StormDoggy/Storm_Doggy_Boob_Tube_Up.png"),
            "StormX.Chest == 'cos bra'", Recolor("Storm", "Chest", "images/StormDoggy/Storm_Doggy_Boob_Tube_Up.png"),

            "True", Null(),
            )

    xoffset 25#-20
    yoffset 285#350#325
#    yoffset 500
#    anchor (0.5,0.5)



image Storm_Doggy_Boob_Static:
    #animation for anal fucking top half
    contains:
        subpixel True
        ConditionSwitch(
            "StormX.Uptop", "Storm_Doggy_Boob",
            "StormX.Chest not in ('black bra','lace bra','sports bra')", "Storm_Doggy_Boob",
            "True", Null(),
            )
#        "Storm_Doggy_Boob"
        xpos 0#300
        ypos 0#0
        anchor (0.1,0.01)
        transform_anchor True
        rotate 0
    contains:
        subpixel True
        ConditionSwitch(
            "not StormX.Uptop and StormX.Chest in ('black bra','lace bra','sports bra')", "Storm_Doggy_Boob",
            "True", Null(),
            )
#        "Storm_Doggy_Boob"
        xpos 20#300
        ypos -10#0
        anchor (0.1,0.01)
        transform_anchor True
        rotate 20

image Storm_Doggy_Boob_Fuck:
    #animation for anal fucking top half
    contains:
        #swinging
        subpixel True
        ConditionSwitch(
            "StormX.Uptop", "Storm_Doggy_Boob",
            "StormX.Chest not in ('black bra','lace bra','sports bra')", "Storm_Doggy_Boob",
            "True", Null(),
            )
#        "Storm_Doggy_Boob"
        xpos 0#300
        ypos 0#0
        anchor (0.1,0.01)
        transform_anchor True
        rotate 0
        pause .4
        parallel: #total 2.5
            pause .05
            ease .25 ypos -20
            pause .2
            ease .3 ypos -5
            ease .2 ypos -10
            easein 1.5 ypos 0
            repeat
        parallel:
            pause .05
            ease .45 rotate 10#5#-10
            ease 1 rotate -5#-5
            ease 1 rotate 5#0
            repeat
    contains:
        #Up
        subpixel True
        ConditionSwitch(
            "not StormX.Uptop and StormX.Chest in ('black bra','lace bra','sports bra')", "Storm_Doggy_Boob",
            "True", Null(),
            )
#        "Storm_Doggy_Boob"
        xpos 20#300
        ypos -10#0
        anchor (0.1,0.01)
        transform_anchor True
        rotate 20
        pause .4
        parallel: #total 2.5
            pause .05
            ease .25 ypos -20#-10
            pause .2
            ease .3 ypos -15#-5
            ease .2 ypos -20#-10
            easein 1.5 ypos -10#0
            repeat


image Storm_Doggy_Boob_Fuck2:
    #animation for anal fucking2 top half
    contains:
        #swinging
        subpixel True
        ConditionSwitch(
            "StormX.Uptop", "Storm_Doggy_Boob",
            "StormX.Chest not in ('black bra','lace bra','sports bra')", "Storm_Doggy_Boob",
            "True", Null(),
            )
#        "Storm_Doggy_Boob"
        xpos 0#300
        ypos 0#0
        anchor (0.1,0.01)
        transform_anchor True
        rotate 0
        parallel: #total 0.9
            pause .15
            ease .1 ypos -30#-20
            pause .1
            ease .55 ypos 5#0      easein
            repeat
        parallel:
#            pause .15
            ease .25 rotate 0#-10
            ease .3 rotate 10#-10
            ease .35 rotate -10#0
#            ease .1 rotate 0#0
            repeat
    contains:
        #Up
        subpixel True
        ConditionSwitch(
            "not StormX.Uptop and StormX.Chest in ('black bra','lace bra','sports bra')", "Storm_Doggy_Boob",
            "True", Null(),
            )
#        "Storm_Doggy_Boob"
        xpos 20#300
        ypos -5#0
        anchor (0.1,0.01)
        transform_anchor True
        rotate 20
        parallel: #total 0.9
            pause .15
            ease .1 ypos -30#-20
            pause .1
            ease .55 ypos -5#5      easein
            repeat

image Storm_Gape_Anal:
        #animation for her asshole growing and shrinking a bit when over 2 Looseness
        contains:
            subpixel True
            "images/StormDoggy/Storm_Doggy_Anal_GapePlate.png"
            anchor (0.52,0.69)
            offset (218,513)#(218,513)
        contains:
            subpixel True
            "images/StormDoggy/Storm_Doggy_Anal_GapeBase.png"
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


image Zero_Storm_Hotdog_Static:
    # The unmoving version of the hotdog cock
    # called in Doggy Ass LC
    contains:
        "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Storm_Hotdog_Moving:
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
image Storm_Pussy_Static:
    #Full Animation for speed 0
    subpixel True
    contains:
        #pubes
        ConditionSwitch(
            "StormX.Pubes", Recolor("Storm", "Pubes", "images/StormDoggy/Storm_Doggy_Pubes_Fucking.png"),
            "True", Null(),
            )
        offset (2,0)
    contains:
        #moving hole
        "images/StormDoggy/Storm_Doggy_Pussy_Heading.png"
        subpixel True
        anchor (0.515,0.69)#(0.52,0.69)
        pos (217,518) #(219,518)
        xzoom .9
        block:
            ease 1 xzoom 1.1
            pause 1
            ease 3 xzoom .9
            repeat
    contains:
        #moving hole
        "images/JubesDoggy/Jubes_Doggy_Pussy_HHole.png"
#        "images/StormDoggy/Storm_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (215,550)#(0.50,0.69)
        transform_anchor True
        pos (220,550) #(217,540)
        xzoom .2
        yzoom .2
        parallel:
            ease 1 xzoom .6
            pause 1
            ease 3 xzoom .2
            repeat
        parallel:
            ease 1 yzoom .6
            pause 1
            ease 3 yzoom .2
            repeat
    contains:
        #pubes
        ConditionSwitch(
            "StormX.Pubes", Recolor("Storm", "Pubes", "images/StormDoggy/Storm_Doggy_Pubes_Open.png"),
            "True", Null(),
            )
        subpixel True
        transform_anchor True
        anchor (0.515,0.69)#(0.52,0.69)
        pos (216,525) #(219,518)
        xzoom .9
        block:
            ease .9 xzoom 1 #.95
            pause 1.6
            ease 2.5 xzoom .9#.8
            repeat
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "StormX.Pierce == 'barbell'", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy.png",
            "StormX.Pierce == 'ring'", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy.png",
            "True", Null(),
            )
        offset (2,0)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in StormX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.52,0.69)
        pos (219,516) #(221,516)
        xzoom .9
        block:
            ease 1 xzoom 1.1
            pause 1
            ease 3 xzoom .9
            repeat
    contains:
        #Cock
        AlphaMask("Zero_Storm_Doggy_Static", "Storm_Pussy_Mask_Static")

image Zero_Storm_Doggy_Static:
    # Sex Speed 0 motions
    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (173,550)
#        alpha 0.9
        block:
            ease 1 ypos 540 #in stroke
            pause 1
            ease 3 ypos 550 #out stroke 545
            repeat

image Storm_Pussy_Mask_Static:
    #AlphaMask used to prevent the cock from moving past the pussy in static pose
    #Called in "Storm_Pussy_Moving"
    contains:
        #Base
        subpixel True
        "images/StormDoggy/Storm_Doggy_Pussy_MaskHeading.png"
        anchor (0.52,0.69)
        pos (220,525)
        xzoom 1
        parallel:
            ease .9 ypos 524#526
            pause 2.1
            ease 2 ypos 525#528
            repeat




# Animation for pussy heading action / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_Pussy_Heading:
    #Full Animation for speed 1
    subpixel True
    contains:
        #moving hole
        "images/StormDoggy/Storm_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.515,0.69)#(0.52,0.69)
        pos (218,518) #(221,518)
        xzoom .6
        block:
            ease .9 xzoom 1
            pause 1.6
            ease 2.5 xzoom .6
            repeat
    contains:
        #pubes
        ConditionSwitch(
            "StormX.Pubes", Recolor("Storm", "Pubes", "images/StormDoggy/Storm_Doggy_Pubes_Open.png"),
            "True", Null(),
            )
        subpixel True
        anchor (0.52,0.69)
        pos (218,518) #(221,518)
        xzoom 1
        block:
            ease .9 xzoom 1.2
            pause 1.6
            ease 2.5 xzoom 1.15
            repeat
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "StormX.Pierce == 'barbell'", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy.png",
            "StormX.Pierce == 'ring'", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy.png",
            "True", Null(),
            )
        offset (2,0)

    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in StormX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
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
        AlphaMask("Zero_Storm_Doggy_Heading", "Storm_Pussy_Mask")
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in StormX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
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

image Zero_Storm_Doggy_Heading:
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

image Storm_Pussy_Mask:
    #AlphaMask used to prevent the cock from moving past the pussy
    contains:
        #Base
        "images/StormDoggy/Storm_Doggy_Pussy_MaskHeading.png"
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


image Storm_Pussy_Fingering:
    #Full Animation for speed 1
    subpixel True
    contains:
        #Base
        "images/StormDoggy/Storm_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:
        #moving hole
        "images/StormDoggy/Storm_Doggy_Pussy_FHole.png"
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
            "StormX.Pubes", Recolor("Storm", "Pubes", "images/StormDoggy/Storm_Doggy_Pubes_Open.png"),
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
            "StormX.Pierce == 'barbell'", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy.png",
            "StormX.Pierce == 'ring'", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy.png",
            "True", Null(),
            )
        offset (2,0)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in StormX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
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
        AlphaMask("Zero_Pussy_Finger", "Storm_Pussy_Mask_Finger")
        xoffset 3
        alpha .6

image Storm_Pussy_Mask_Finger:
    #AlphaMask used to prevent the cock from moving past the pussy
    #Called in "Jean_Pussy_Moving"
    contains:
        #Base
        "images/StormDoggy/Storm_Doggy_Pussy_MaskHeading.png"
        anchor (0.52,0.69)
        pos (218,526) #(221,518)
        xzoom .8
        parallel:
            ease 1 ypos 521 #518
            pause 1
            ease 3 ypos 526#528
            repeat

# > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

image Storm_Pussy_Fucking2:
    #Full Animation for speed 2
    contains:
        #Base
        offset (2,0)
        "images/StormDoggy/Storm_Doggy_Pussy_FHole.png"
    contains:
        #pubes
        ConditionSwitch(
            "StormX.Pubes", Recolor("Storm", "Pubes", "images/StormDoggy/Storm_Doggy_Pubes_Fucking.png"),
            "True", Null(),
            )
        offset (2,0)

        anchor (0.52,0.69)
        pos (218,518) #(221,518)
        xzoom 1.15
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "StormX.Pierce == 'barbell'", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy.png",
            "StormX.Pierce == 'ring'", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy.png",
            "True", Null(),
            )
        offset (0,0)
    contains:
        #spunk
        ConditionSwitch(
            "'in' in StormX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
        offset (2,0)
    contains:
        #Cock
        offset (2,0)
        ConditionSwitch(
            "'dildo pussy' in (Trigger,Trigger2,StormX.Offhand)", AlphaMask("Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "True",AlphaMask("Zero_Storm_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            ),
    contains:
        #spunk
        ConditionSwitch(
            "'in' in StormX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )
        offset (2,0)

image Zero_Storm_Doggy_Fucking2:
    # Sex Speed 2 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat


image Storm_Pussy_Fucking3:
    #Full Animation for speed 3
    contains:
        #Base
        offset (2,0)
        "images/StormDoggy/Storm_Doggy_Pussy_FHole.png"
    contains:
        #pubes
        ConditionSwitch(
            "StormX.Pubes", Recolor("Storm", "Pubes", "images/StormDoggy/Storm_Doggy_Pubes_Fucking.png"),
            "True", Null(),
            )
        offset (2,0)
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "StormX.Pierce == 'barbell'", "images/StormDoggy/Storm_Doggy_Pierce_Barbell_Pussy.png",
            "StormX.Pierce == 'ring'", "images/StormDoggy/Storm_Doggy_Pierce_Ring_Pussy.png",
            "True", Null(),
            )
        offset (0,0)
    contains:
        #spunk
        ConditionSwitch(
            "'in' in StormX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
        offset (2,0)
    contains:
        #Cock
        offset (2,0)
        AlphaMask("Zero_Storm_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
    contains:
        #spunk
        ConditionSwitch(
            "'in' in StormX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )
        offset (2,0)

image Zero_Storm_Doggy_Fucking3:
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

image Storm_Anal:
    #Anal static Loose
    contains:
        #Cock
        "Zero_Doggy_Insert"
        pos (172,500)

image Storm_Anal_Fingering:
    #Animation for speed 1
    contains:
        #Hole
        "images/StormDoggy/Storm_Doggy_Anal_FullHole.png"
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
            "'anal' in StormX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
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
        AlphaMask("Zero_Storm_Doggy_Anal_Finger", "Storm_Doggy_Anal_Fingering_Mask")
    contains:
        #spunk over cock
        subpixel True
        ConditionSwitch(
            "'anal' in StormX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
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

image Zero_Storm_Doggy_Anal_Finger:
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
image Storm_Doggy_Anal_Fingering_Mask:
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
image Storm_Anal_Heading:
    #Animation for speed 1
    contains:
        #Hole
        "images/StormDoggy/Storm_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .5
            repeat
    contains:
        #spunk under cock
        ConditionSwitch(
            "'anal' in StormX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
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
        AlphaMask("Zero_Storm_Doggy_Anal_Heading", "Storm_Doggy_Anal_Heading_Mask")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in StormX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )
        anchor (0.52,0.71) #(0.52,0.69)
        pos (218,530)#(218,518)
        zoom .5
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .6 #.5
            repeat

image Zero_Storm_Doggy_Anal_Heading:
        #the cock anal heading animation
    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500#505
            repeat

image Zero_Storm_Doggy_Anal_HeadingJunk:
    #this is a mask to correct an annoying glitch in the core mask
    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease .5 ypos 550
            pause .25
            ease 1.75 ypos 600#505
            repeat

image Storm_Doggy_Anal_Heading_Mask:
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

image Storm_Doggy_Anal_Head_Top:
#animation for anal fucking top half
    contains:
        subpixel True
        "Storm_Doggy_Body"
        ypos 0
        block:
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat

image Storm_Doggy_Anal_Head_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Storm_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -10
            easeout .1 ypos -7
            easein .9 ypos 0
            pause .9
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Storm_Doggy_Anal1:
    #Animation for speed 2 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat

image Storm_Anal_Fucking:
    #Animation for speed 2 Ass
    contains:
        #Hole
        "images/StormDoggy/Storm_Doggy_Anal_FullHole.png"
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
            "'anal' in StormX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            #full hose/tights
            "'dildo anal' in (Trigger,Trigger2,StormX.Offhand)", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", AlphaMask("Zero_Storm_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            )
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in StormX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )

image Storm_Doggy_Fuck_Top:
    #animation for anal fucking top half
    contains:
        subpixel True
        "Storm_Doggy_Body"
        ypos 0#15
        pause .4
        block:
            ease .2 ypos -10#5
            pause .3
            ease 2 ypos 0#15
            repeat

image Storm_Doggy_Fuck_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Storm_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15#-25
            ease .1 ypos -5#-15
            pause .2
            ease 1.6 ypos 0
            repeat


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Storm_Doggy_Anal2:
    #Animation for speed 3 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat

image Storm_Anal_Fucking2:
    #Animation for speed 3 Ass
    contains:
        #Hole
        "images/StormDoggy/Storm_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .95
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
            "'anal' in StormX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Storm_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in StormX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )

image Storm_Doggy_Fuck2_Top:
    #animation for anal fucking2 top half
    contains:
        subpixel True
        "Storm_Doggy_Body"
        ypos 0#20
        block:
            pause .15
            ease .1 ypos -20#0
            pause .1
            easein .5 ypos 0#20
            pause .05
            repeat

image Storm_Doggy_Fuck2_Ass:
    #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Storm_Doggy_Ass"
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

image Storm_Doggy_Feet0:
    #static animation
    contains:
        "Storm_Doggy_Shins"
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
        "Storm_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            subpixel True
            pause .5
            ease 2 ypos 20#20
            pause .5
            ease 2 ypos 0#0
            repeat

image Storm_Doggy_Feet1:
    #slow animation
    contains:
        "Storm_Doggy_Shins"
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
        "Storm_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            pause .3
            ease 1.7 ypos 120
            ease 1 ypos 0
            repeat

image Storm_Doggy_Feet2:
    #fast animation
    contains:
        "Storm_Doggy_Shins"
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
        "Storm_Doggy_Feet"
        pos (0, 20) #(0,0) top
        block:
            pause .05
            ease .6 ypos 130
            ease .3 ypos 20
            repeat
# Footjob animations end > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Doggy Launch/Reset
label Storm_Doggy_Launch(Line = Trigger):
    if renpy.showing("Storm_Doggy_Animation"):
        return
    $ Speed = 0
    call Girl_Hide(StormX,1)
    show Storm_Doggy_Animation at SpriteLoc(StageCenter+50) zorder 150
    with dissolve
    return

label Storm_Doggy_Reset:
    if not renpy.showing("Storm_Doggy_Animation"):
        return
#    $ Trigger = 0               #fix, not sure this is a good idea
    $ StormX.ArmPose = 2
    $ StormX.SpriteVer = 0
    hide Storm_Doggy_Animation
    call Girl_Hide(StormX)
    show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) zorder StormX.Layer:
            alpha 1 zoom 1 offset (0,0) anchor (0.6, 0.0)
    with dissolve
    $ Speed = 0
    return

# End Storm Doggy Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Storm Sex Pose Content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Storm Sex Pose core / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_SexSprite:
    LiveComposite(
        (1120,960),

#        (0,0), ConditionSwitch(
#                #Shows different upper body motion depending on events
#                "True", "Storm_Sex_Speed2",
#                ),
        (0,0), ConditionSwitch(
                #Shows different motion depending on events
#                "not Player.Sprite", "Storm_Sex_Body_Static",
                "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Storm_Sex_Fucking_Speed3",
                        "Speed >= 2", "Storm_Sex_Fucking_Speed2",
                        "Speed", "Storm_Sex_Fucking_Speed1",
                        "True", "Storm_Sex_Fucking_Speed0",
                        ),
                "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Storm_Sex_Anal_Speed3",
                        "Speed >= 2", "Storm_Sex_Anal_Speed2",
                        "Speed", "Storm_Sex_Anal_Speed1",
                        "True", "Storm_Sex_Anal_Speed0",
                        ),
                "Player.Sprite and Player.Cock == 'out' and Speed >= 2","Storm_Sex_Hotdog_Speed2",
                "Player.Sprite and Player.Cock == 'out' and Speed >= 1","Storm_Sex_Hotdog_Speed1",
                "Player.Sprite and Player.Cock == 'foot'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 2", "Storm_Sex_FJ_Speed2",
                        "Speed", "Storm_Sex_FJ_Speed1",
                        "True", "Storm_Sex_FJ_Speed0",
                        ),
#                "Player.Cock == 'out' and Speed >= 2","Storm_Hotdog_Body_Anim2",
                "True", "Storm_Sex_Static",
                ),
        )
    align (0.6,0.0)
    pos (650,393)#(650,230)
    zoom 0.7

# End Storm Sex Pose core / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Storm Sex Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_Sex_Body:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Storm_SexSprite
        (1120,840),
        (245,-225), "Storm_HairBack_Sex",                                                                 #Hair underlayer
        (0,0), "images/StormSex/Storm_Sex_Body.png",
        #Eyes
#        (0,0), ConditionSwitch(                                                                                 #necklace
#            "StormX.Neck == 'gold necklace'", "images/StormSex/Storm_Sex_Neck_Gold.png",
#            "StormX.Neck == 'star necklace'", "images/StormSex/Storm_Sex_Neck_Star.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #arm rings base
            "not StormX.Acc == 'rings' or StormX.Over == 'jacket'", Null(),
            "True", "images/StormSex/Storm_Sex_Arms_Ring.png", #StormX.ArmPose == 2
            ),
        (0,0), ConditionSwitch(
            #bra layer
            "not StormX.Chest", Null(),
            "StormX.Chest == 'tube top'", Recolor("Storm", "Chest", "images/StormSex/Storm_Sex_Chest_Tube.png"),
            "StormX.Chest == 'black bra'", Recolor("Storm", "Chest", "images/StormSex/Storm_Sex_Chest_Bra.png"),
            "StormX.Chest == 'lace bra'", Recolor("Storm", "Chest", "images/StormSex/Storm_Sex_Chest_Bra.png"),
            "not StormX.Uptop", ConditionSwitch(
                    #if the top's down. . .
                    "StormX.Chest == 'cos bra'", Recolor("Storm", "Chest", "images/StormSex/Storm_Sex_Chest_Cos.png"),
                    "StormX.Chest == 'sports bra'", Recolor("Storm", "Chest", "images/StormSex/Storm_Sex_Chest_SportsBra.png"),
                    "StormX.Chest == 'bikini top' and StormX.Panties == 'bikini bottoms'", Recolor("Storm", "Chest", "images/StormSex/Storm_Sex_Chest_Bikini_Combo.png"),
                    "StormX.Chest == 'bikini top'", Recolor("Storm", "Chest", "images/StormSex/Storm_Sex_Chest_Bikini.png"),
#                    "StormX.Chest == 'lace bra'", "images/StormSex/Storm_Sex_Chest_LaceBra.png",
                    "True", Null(),
                    ),
#            "StormX.Over", ConditionSwitch(
#                    # If she's wearing a shirt over the bra
#                    "StormX.Chest == 'cami'", "images/StormSex/Storm_Sex_Under_Cami_UpS.png",
#                    "StormX.Chest == 'bikini top'", "images/StormSex/Storm_Sex_Under_Bikini_Up.png",
#                    "StormX.Chest == 'sports bra' and StormX.Over == 'red shirt'", "images/StormSex/Storm_Sex_Under_SportsBra_UpS.png",
#                    "StormX.Chest == 'sports bra'", "images/StormSex/Storm_Sex_Under_SportsBra_Up.png",
#                    "True", Null(),
#                    ),
            "True", ConditionSwitch(
                    # if she's not wearing a shirt
                    "StormX.Chest == 'cos bra'", "images/StormSex/Storm_Sex_Chest_Cos_Up.png",
                    "StormX.Chest == 'sports bra'", Recolor("Storm", "Chest", "images/StormSex/Storm_Sex_Chest_SportsBra_Up.png"),
#                    "StormX.Chest == 'black bra'", "images/StormSex/Storm_Sex_Chest_Bra_Up.png",
                    "StormX.Chest == 'bikini top'", Recolor("Storm", "Chest", "images/StormSex/Storm_Sex_Chest_Bikini_Up.png"),
#                    "StormX.Chest == 'lace bra'", "images/StormSex/Storm_Sex_Chest_LaceBra_Up.png",
                    "True", Null(),
                    ),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "StormX.Water", "images/StormSex/Storm_Sex_Wet_Body.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #shirt layer
            "StormX.Over == 'white shirt' and StormX.Uptop", Recolor("Storm", "Over", "images/StormSex/Storm_Sex_Chest_Shirt_Up.png"),
            "StormX.Over == 'white shirt'", Recolor("Storm", "Over", "images/StormSex/Storm_Sex_Chest_Shirt.png"),
            "StormX.Over == 'jacket'", Recolor("Storm", "Over", "images/StormSex/Storm_Sex_Chest_Jacket.png"),
            "True", Null(),
#            "not StormX.Uptop", ConditionSwitch(
#                    #if the top's down. . .
#                    "StormX.Over == 'white shirt'", "images/StormSex/Storm_Sex_Over_RedShirt.png",
##                    "StormX.Over == 'towel'", "images/StormSex/Storm_Sex_Over_Towel.png",
#                    "True", Null(),
#                    ),
#            "True", ConditionSwitch(
#                    # if she's not wearing a shirt
##                    "StormX.Over == 'pink top' and StormX.Chest == 'sports bra'", "images/StormSex/Storm_Sex_Over_PinkShirt_UpS.png",
#                    "StormX.Over == 'jacket'", "images/StormSex/Storm_Sex_Over_PinkShirt_Up.png",
##                    "StormX.Over == 'towel'", "images/StormSex/Storm_Sex_Over_Towel.png",
#                    "True", Null(),
#                    ),
            ),
#        (0,0), ConditionSwitch(
#            #bra layer over the shirt
#            "not StormX.Chest or not StormX.Over or not StormX.Uptop", Null(),
#            # if she's not wearing a shirt
#            "StormX.Chest == 'bra'", "images/StormSex/Storm_Sex_Under_Bra_Up.png",
#            "StormX.Chest == 'lace bra'", "images/StormSex/Storm_Sex_Under_LaceBra_UpS.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #neck
            "StormX.Neck == 'rings'", "images/StormSex/Storm_Sex_Neck_Ring.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'belly' in StormX.Spunk and Player.Male", "images/StormSex/Storm_Sex_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'tits' in StormX.Spunk and Player.Male", "images/StormSex/Storm_Sex_Spunk_Tits_Back.png",
            "True", Null(),
            ),
#        (0,0), "images/StormSex/Storm_Sex_HeadRef.png",
        (220,-162), "Storm_Head_Sex",  #(260,-350) (205,-180)
        )
    zoom 0.9
    offset (65,-100)
    #yoffset -163
# End Storm Sex Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Storm_Head_Sex:
    # The head used for the sex pose, referenced by Storm_Sex_Body
    "Storm_Sprite_Head"
    zoom 1.25
    anchor (0.5,0.5)
    rotate -7

image Storm_HairBack_Sex:
    # The hair behind the head for the sex pose, referenced by Storm_Sex_Body
    "Storm_Sprite_HairBack"
    zoom 1.25
    anchor (0.5,0.5)
    rotate -7

# Start Storm Sex Pose Tits / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_Sex_Tits:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Storm_SexSprite
        (1120,960),                                                                                     #Hair underlayer

#        (0,0), "images/StormSex/Storm_Sex_Tits.png",

        (0,0), ConditionSwitch(
            #Tits
            "StormX.Chest == 'cos bra' and StormX.Uptop", "images/StormSex/Storm_Sex_Tits_Cos.png",
            "StormX.Chest == 'cos bra'", "images/StormSex/Storm_Sex_Tits_Cos_Under.png",
            "True", "images/StormSex/Storm_Sex_Tits.png",
            ),

        (0,0), ConditionSwitch(
            #Piercings
            "StormX.Pierce == 'barbell'", "images/StormSex/Storm_Sex_Pierce_Tits_Barbell.png",
            "StormX.Pierce == 'ring'", "images/StormSex/Storm_Sex_Pierce_Tits_Ring.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #bra layer
            "not StormX.Chest", Null(),
            "not StormX.Uptop", ConditionSwitch(
                    #if the top's down. . .
                    "StormX.Chest == 'cos bra'", "images/StormSex/Storm_Sex_Tits_Cos_Over.png",
                    "StormX.Chest == 'tube top'", "images/StormSex/Storm_Sex_Tits_Tube.png",
                    "StormX.Chest == 'black bra'", Recolor("Storm", "Chest", "images/StormSex/Storm_Sex_Tits_Bra.png"),
                    "StormX.Chest == 'lace bra'", "images/StormSex/Storm_Sex_Tits_LaceBra.png",
                    "StormX.Chest == 'sports bra'", "images/StormSex/Storm_Sex_Tits_SportsBra.png",
                    "StormX.Chest == 'bikini top'", "images/StormSex/Storm_Sex_Tits_Bikini.png",
                    "True", Null(),
                    ),
#            "StormX.Over", ConditionSwitch(
#                    # If she's wearing a shirt over the bra
#                    "StormX.Chest == 'cami'", "images/StormSex/Storm_Sex_Under_Cami_UpS.png",
#                    "StormX.Chest == 'bikini top'", "images/StormSex/Storm_Sex_Under_Bikini_Up.png",
#                    "StormX.Chest == 'sports bra' and StormX.Over == 'red shirt'", "images/StormSex/Storm_Sex_Under_SportsBra_UpS.png",
#                    "StormX.Chest == 'sports bra'", "images/StormSex/Storm_Sex_Under_SportsBra_Up.png",
#                    "True", Null(),
#                    ),
            "True", ConditionSwitch(
                    # if she's not wearing a shirt
                    "StormX.Chest == 'tube top'", "images/StormSex/Storm_Sex_Tits_Tube_Down.png",
#                    "StormX.Chest == 'black bra'", "images/StormSex/Storm_Sex_Tits_Bra_Up.png",
#                    "StormX.Chest == 'lace bra'", "images/StormSex/Storm_Sex_Tits_LaceBra_Up.png",
                    "StormX.Chest == 'sports bra'", "images/StormSex/Storm_Sex_Tits_SportsBra_Up.png",
                    "StormX.Chest == 'bikini top'", "images/StormSex/Storm_Sex_Tits_Bikini_Up.png",
                    "True", Null(),
                    ),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "StormX.Water", "images/StormSex/Storm_Sex_Wet_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Overshirt
            "not StormX.Over", Null(),
            "StormX.Over == 'white shirt' and StormX.Uptop", Recolor("Storm", "Over", "images/StormSex/Storm_Sex_Tits_Shirt_Up.png"),
            "StormX.Over == 'white shirt'", Recolor("Storm", "Over", "images/StormSex/Storm_Sex_Tits_Shirt.png"),
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #shirt layer
#            "not StormX.Over", Null(),
#            "not StormX.Uptop", ConditionSwitch(
#                    #if the top's down. . .
#                    "StormX.Over == 'pink top'", "images/StormSex/Storm_Sex_Over_PinkShirt.png",
#                    "StormX.Over == 'red shirt'", "images/StormSex/Storm_Sex_Over_RedShirt.png",
#                    "StormX.Over == 'towel'", "images/StormSex/Storm_Sex_Over_Towel.png",
#                    "True", Null(),
#                    ),
#            "True", ConditionSwitch(
#                    # if she's not wearing a shirt
#                    "StormX.Over == 'pink top' and StormX.Chest == 'sports bra'", "images/StormSex/Storm_Sex_Over_PinkShirt_UpS.png",
#                    "StormX.Over == 'pink top'", "images/StormSex/Storm_Sex_Over_PinkShirt_Up.png",
#                    "StormX.Over == 'red shirt'", "images/StormSex/Storm_Sex_Over_RedShirt_Up.png",
##                    "StormX.Over == 'towel'", "images/StormSex/Storm_Sex_Over_Towel.png",
#                    "True", Null(),
#                    ),
#            ),
#        (0,0), ConditionSwitch(
#            #bra layer over the shirt
#            "not StormX.Chest or not StormX.Over or not StormX.Uptop", Null(),
#            # if she's not wearing a shirt
#            "StormX.Chest == 'bra'", "images/StormSex/Storm_Sex_Under_Bra_Up.png",
#            "StormX.Chest == 'lace bra'", "images/StormSex/Storm_Sex_Under_LaceBra_UpS.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Piercings
            "(not StormX.Chest and not StormX.Over) or StormX.Uptop", Null(),
            "StormX.Pierce == 'barbell'", "images/StormSex/Storm_Sex_Pierce_Tits_BarbellC.png",
            "StormX.Pierce == 'ring'", "images/StormSex/Storm_Sex_Pierce_Tits_RingC.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'tits' in StormX.Spunk and Player.Male", "images/StormSex/Storm_Sex_Spunk_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast licking animation
            "Trigger == 'suck breasts' or Trigger2 == 'suck breasts'", "Storm_Sex_Lick_Breasts",
            "True", Null()
            ),
        (0,0), ConditionSwitch(
            #breast fondling animation
            "Trigger == 'fondle breasts' or Trigger2 == 'fondle breasts'", "Storm_Sex_Fondle_Breasts",
            "True", Null()
            ),
#        (260,-350), "Storm_Head_Sex",  #
        )
    zoom 0.9
    offset (65,-100)
#    yoffset -163
# End Storm Sex Pose Tits / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_Sex_Lick_Breasts:
        "Lick_Anim"
        zoom 0.7
        offset (400,350)#(390,620)

image Storm_Sex_Fondle_Breasts:
        "GropeLeftBreast"
        zoom 1.5
        offset (190,-200)#(160,-40)

# Start Storm Sex Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_Sex_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Storm_SexSprite
        (1120,960),
#        (0,0), ConditionSwitch(
#Legs Layer
#            "StormX.Legs == 'blue skirt'", "images/StormSex/Storm_Sex_Skirt_Back.png",
#            "True", Null(),
#            ),
#        (0,0), "images/StormSex/Storm_Sex_Legs.png",
#Legs Base

        (0,0), ConditionSwitch(
            #Skirt back
            "StormX.Legs == 'skirt'", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_Skirt_Back.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #plug
            "StormX.Plug", "Storm_Sex_Plug",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'anal' in StormX.Spunk and Player.Male", "images/StormSex/Storm_Sex_Spunk_Anal_Closed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Legs Base
            "Player.Sprite and Player.Cock == 'anal' and ShowFeet", "images/StormSex/Storm_Sex_Legs_FJ_Anal.png",
            "ShowFeet", "images/StormSex/Storm_Sex_Legs_FJ.png",
            "Player.Sprite and Player.Cock == 'anal'", "images/StormSex/Storm_Sex_Legs_Anal.png",
            "True", "images/StormSex/Storm_Sex_Legs.png",
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "not StormX.Water", Null(),
            "ShowFeet", "images/StormSex/Storm_Sex_Wet_Legs_FJ.png",
            "True", "images/StormSex/Storm_Sex_Wet_Legs.png",
            ),

        (0,0), "Storm_Sex_Anus",
            #Anus Composite

        (0,0), "Storm_Sex_Pussy",
            #Pussy Composite


        (0,0), ConditionSwitch(
            #hose layer
            "ShowFeet",ConditionSwitch(
                    #If she has panties down. . .
                    "StormX.Hose == 'stockings and garterbelt'", Recolor("Storm", "Hose", "images/StormSex/Storm_Sex_Hose_StockingsGarter_FJ.png"),
                    "StormX.Hose == 'garterbelt'", Recolor("Storm", "Hose", "images/StormSex/Storm_Sex_Hose_Garter_FJ.png"),
                    "StormX.Hose == 'stockings'", Recolor("Storm", "Hose", "images/StormSex/Storm_Sex_Hose_Stockings_FJ.png"),
                    "True", Null(),
                    ),
            "StormX.Hose == 'stockings and garterbelt'", Recolor("Storm", "Hose", "images/StormSex/Storm_Sex_Hose_StockingsGarter.png"),
            "StormX.Hose == 'garterbelt'", Recolor("Storm", "Hose", "images/StormSex/Storm_Sex_Hose_Garter.png"),
            "StormX.Hose == 'stockings'", Recolor("Storm", "Hose", "images/StormSex/Storm_Sex_Hose_Stockings.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #leg rings
            "not StormX.Acc == 'rings' or StormX.Legs == 'pants' or StormX.Legs == 'yoga pants'", Null(),
            "ShowFeet", "images/StormSex/Storm_Sex_LegRings_FJ.png",
            "True", "images/StormSex/Storm_Sex_LegRings.png", #StormX.ArmPose == 2
            ),
        (0,0), ConditionSwitch(
            #Panties if up
            "StormX.Legs and StormX.Legs != 'skirt' and not StormX.Upskirt", Null(),
            "StormX.PantiesDown",ConditionSwitch(
                    #If she has panties down. . .
                    "StormX.Panties == 'cos panties' and ShowFeet", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Cos_FJ_Down.png"),
                    "StormX.Panties == 'cos panties'", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Cos_Down.png"),
                    "StormX.Panties == 'white panties' and ShowFeet", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_White_FJ_Down.png"),
                    "StormX.Panties == 'white panties'", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_White_Down.png"),
                    "StormX.Panties and ShowFeet", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Black_FJ_Down.png"),
                    "StormX.Panties", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Black_Down.png"),
                    "True", Null(),
                    ),
            "ShowFeet",ConditionSwitch(
                    #If she has panties down. . .
                    "StormX.Panties == 'cos panties' and StormX.Wet", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Cos_FJ_Wet.png"),
                    "StormX.Panties == 'cos panties'", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Cos_FJ.png"),
                    "StormX.Panties == 'white panties' and StormX.Wet", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_White_FJ_Wet.png"),
                    "StormX.Panties == 'white panties'", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_White_FJ.png"),
                    "StormX.Panties == 'lace panties'", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Lace_FJ.png"),
                    "StormX.Panties == 'bikini bottoms' and (StormX.Chest != 'bikini top' or StormX.Uptop)", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Bikini_FJ_Top.png"),
                    "StormX.Panties == 'bikini bottoms'", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Bikini_FJ.png"),
                    "StormX.Panties and StormX.Wet", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Black_FJ_Wet.png"),
                    "StormX.Panties", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Black_FJ.png"),
                    "True", Null(),
                    ),
            "StormX.Panties == 'cos panties' and StormX.Wet", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Cos_Wet.png"),
            "StormX.Panties == 'cos panties'", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Cos.png"),
            "StormX.Panties == 'white panties' and StormX.Wet", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_White_Wet.png"),
            "StormX.Panties == 'white panties'", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_White.png"),
            "StormX.Panties == 'lace panties'", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Lace.png"),
            "StormX.Panties == 'bikini bottoms' and (StormX.Chest != 'bikini top' or StormX.Uptop)", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Bikini_Top.png"),
            "StormX.Panties == 'bikini bottoms'", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Bikini.png"),
            "StormX.Panties and StormX.Wet", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Black_Wet.png"),
            "StormX.Panties", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Black.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Piercings
#            "Player.Sprite", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),
            "not StormX.Panties and StormX.Hose != 'pantyhose'", Null(),
            "((StormX.Panties or StormX.Hose == 'pantyhose') and StormX.PantiesDown)", Null(),
                #if she has panties, but they are down, or pantyhose, or Legs that are not a skirt and are not down, skip these. . .
            "StormX.Pierce == 'barbell'", "images/StormSex/Storm_Sex_Pierce_Pussy_BarbellC.png",
            "StormX.Pierce == 'ring'", "images/StormSex/Storm_Sex_Pierce_Pussy_RingC.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #pantyhose layer
            "StormX.Panties and StormX.PantiesDown", Null(),
            "ShowFeet",ConditionSwitch(
                    #If she has panties down. . .
                    "StormX.Hose == 'pantyhose'", Recolor("Storm", "Hose", "images/StormSex/Storm_Sex_Hose_Pantyhose_FJ.png"),
                    "StormX.Hose == 'ripped pantyhose'", Recolor("Storm", "Hose", "images/StormSex/Storm_Sex_Hose_Pantyhose_FJHoled.png"),
                    "True", Null(),
                    ),
            "StormX.Hose == 'pantyhose'", Recolor("Storm", "Hose", "images/StormSex/Storm_Sex_Hose_Pantyhose.png"),
            "StormX.Hose == 'ripped pantyhose'", Recolor("Storm", "Hose", "images/StormSex/Storm_Sex_Hose_Pantyhose_Holed.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs Layer
            "StormX.Legs == 'skirt' and ShowFeet", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_Skirt_FJ.png"),
            "StormX.Upskirt",ConditionSwitch(
                    #If she has panties down. . .
                    "StormX.Legs == 'skirt'", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_Skirt_Up.png"),
                    "StormX.Legs == 'pants' and ShowFeet", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_Pants_FJ_Down.png"),
                    "StormX.Legs == 'pants'", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_Pants_Down.png"),
                    "StormX.Legs == 'yoga pants' and ShowFeet", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_YogaPants_FJ_Down.png"),
                    "StormX.Legs == 'yoga pants'", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_YogaPants_Down.png"),
                    "True", Null(),
                    ),
            "ShowFeet",ConditionSwitch(
                    #If she has panties down. . .
                    "StormX.Legs == 'pants' and StormX.Wet > 1", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_Pants_FJ_Wet.png"),
                    "StormX.Legs == 'pants'", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_Pants_FJ.png"),
                    "StormX.Legs == 'yoga pants' and StormX.Wet > 1", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_YogaPants_FJ_Wet.png"),
                    "StormX.Legs == 'yoga pants'", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_YogaPants_FJ.png"),
                    "True", Null(),
                    ),
            "StormX.Legs == 'skirt'", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_Skirt.png"),
            "StormX.Legs == 'pants' and StormX.Wet > 1", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_Pants_Wet.png"),
            "StormX.Legs == 'pants'", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_Pants.png"),
            "StormX.Legs == 'yoga pants' and StormX.Wet > 1", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_YogaPants_Wet.png"),
            "StormX.Legs == 'yoga pants'", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_YogaPants.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Piercings
#            "Player.Sprite", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),
            "not StormX.Legs", Null(),
            "StormX.Legs and StormX.Legs != 'skirt' and StormX.Upskirt", Null(),
                #if she has panties, but they are down, or pantyhose, or Legs that are not a skirt and are not down, skip these. . .
            "StormX.Pierce == 'barbell'", "images/StormSex/Storm_Sex_Pierce_Pussy_BarbellC.png",
            "StormX.Pierce == 'ring'", "images/StormSex/Storm_Sex_Pierce_Pussy_RingC.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer
#            "not Player.Sprite or Player.Cock != 'out'", Null(),
#            "Speed >= 2", "Storm_Hotdog_Zero_Anim2",
#            "Speed", "Storm_Hotdog_Zero_Anim1",
#            "True", "Storm_Hotdog_Zero_Anim0",
#            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy'", "Storm_Sex_Lick_Pussy",
            "Trigger == 'lick ass'", "Storm_Sex_Lick_Ass",
            "True", Null()
            ),
        (0,0), ConditionSwitch(
            #pussy fondling animation
            "Player.Sprite", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Storm_Sex_Fondle_Pussy",
            "StormX.Offhand == 'fondle pussy' and StormX.Lust > 60", At("StormFingerHand", GirlFingerPussyX()),
            "StormX.Offhand == 'fondle pussy'", At("StormMastHand", GirlGropePussyX()),
            "True", Null()
            ),
        (0,0), ConditionSwitch(
            #Footjob overlay
            "ShowFeet", AlphaMask("Storm_Sex_Feet", "images/StormSex/Storm_Sex_Mask_Foot2.png"),
#            "ShowFeet", AlphaMask("Storm_Sex_Feet", "images/StormSex/Storm_Sex_Mask_Foot.png"),
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer
#            "not Player.Sprite or Player.Cock != 'foot'", Null(),
#            "Speed >= 2", "Storm_Footcock_Zero_Anim2",
#            "Speed", "Storm_Footcock_Zero_Anim1",
#            "True", "Storm_Footcock_Static",
#            ),
#        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer
#            "not Player.Sprite or Player.Cock != 'foot'", Null(),
#            "Speed >= 2", At("Storm_Footcock", Storm_Footcock_Zero_Anim2A()),
#            "Speed", At("Storm_Footcock", Storm_Footcock_Zero_Anim1A()),
#            "True", At("Storm_Footcock", Storm_Footcock_StaticA()),
#            ),
#        (0,0), ConditionSwitch(                                                                                 #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
#            "not Speed", "Storm_Sex_Feet",
#            "Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Storm_Sex_Feet", "images/StormSex/Storm_Sex_FeetMask.png"),
#            "True", "Storm_Sex_Feet",
#            ),
        )

image Storm_Sex_Plug:
        "images/PlugBase_Sex.png"
        offset (-225,-290) #(-285,-140)
        zoom 1.4


# End Storm Sex Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_Sex_Feet:
    LiveComposite(
        #the lower legs used in the sex pose, referenced by Storm_Sex_Legs
        (1120,960),
        (0,0), "images/StormSex/Storm_Sex_Legs_FJ.png",                                                         #Legs Base
#        (0,0), ConditionSwitch(                                                                                 #Wet look
#            "StormX.Water", "images/StormSex/Storm_Sex_Water_Feet.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #hose layer
            "StormX.Hose == 'ripped pantyhose' and (not StormX.Panties or not StormX.PantiesDown)", Recolor("Storm", "Hose", "images/StormSex/Storm_Sex_Hose_Pantyhose_FJHoled.png"),
            "StormX.Hose and StormX.Hose != 'garterbelt' and StormX.Hose != 'pantyhose'", Recolor("Storm", "Hose", "images/StormSex/Storm_Sex_Hose_Pantyhose_FJ.png"),
            "StormX.Panties and StormX.PantiesDown", Null(),
            "StormX.Hose == 'pantyhose'", Recolor("Storm", "Hose", "images/StormSex/Storm_Sex_Hose_Pantyhose_FJ.png"),
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(                                                                                 #Legs Layer
#            "StormX.Upskirt", Null(),
#            "StormX.Legs == 'capris'", "images/StormSex/Storm_Sex_Feet_Blue.png",
#            "StormX.Legs == 'black jeans'", "images/StormSex/Storm_Sex_Feet_Black.png",
#            "StormX.Legs == 'yoga pants'", "images/StormSex/Storm_Sex_Feet_Yoga.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #spunk
            "'feet' in StormX.Spunk", "images/StormSex/Storm_Sex_Spunk_Feet.png",
            "True", Null(),
            ),
        )

# Start Storm Sex Pose Pussy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_Sex_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).

    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/StormSex/Storm_Sex_Pussy_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and Speed", "Storm_Sex_Heading_Pussy",
                "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'out')", "images/StormSex/Storm_Sex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/StormSex/Storm_Sex_Pussy_Open.png",
                "StormX.Offhand == 'fondle pussy' and StormX.Lust > 60", "images/StormSex/Storm_Sex_Pussy_Open.png",
                "True", "images/StormSex/Storm_Sex_Pussy_Closed.png",
                )
#    contains:
#            # The background plate of her pussy
#            ConditionSwitch(
#                "not StormX.Wet", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/StormSex/Storm_Sex_WetPussy_F.png",
#                "True", "images/StormSex/Storm_Sex_WetPussy_C.png",
#                )
    contains:
            # pubes
            ConditionSwitch(
                "not StormX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Fucking.png"),
                "Player.Sprite and Player.Cock == 'in' and Speed and ShowFeet", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Fucking_FJ.png"),
                "Player.Sprite and Player.Cock == 'in' and Speed", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Fucking.png"),
                "Player.Sprite and Player.Cock == 'in' and ShowFeet", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Open_FJ.png"),
                "Player.Sprite and Player.Cock == 'in'", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Open.png"),
                "Trigger == 'lick pussy' and ShowFeet", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Open_FJ.png"),
                "Trigger == 'lick pussy'", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Open.png"),
                "StormX.Offhand == 'fondle pussy' and StormX.Lust > 60", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Open.png"),
                "ShowFeet", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Closed_FJ.png"),
                "True", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Closed.png"),
                )
    contains:
            ConditionSwitch(
                #Outside Spunk
                "'in' in StormX.Spunk and Player.Male", "images/StormSex/Storm_Sex_Spunk_Pussy.png",
                "True", Null(),
                )
#    contains:
#            #Spunk under penis
#            ConditionSwitch(
#                "'in' in StormX.Spunk", "images/StormSex/Storm_Sex_Spunk_Puss_Under.png",
#                "True", Null(),
#                )
#    contains:
#            #hose layer
#            ConditionSwitch(
#                "StormX.Panties and StormX.PantiesDown", Null(),
#                "StormX.Hose == 'ripped pantyhose' and ShowFeet", Recolor("Storm", "Hose", "images/StormSex/Storm_Sex_Hose_Pantyhose_Holed.png"),
#                "StormX.Hose == 'ripped pantyhose'", Recolor("Storm", "Hose", "images/StormSex/Storm_Sex_Hose_Pantyhose_Holed.png"),
#                "True", Null(),
#                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            ConditionSwitch(
#                "not Player.Sprite", Null(),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 3", AlphaMask("Storm_Sex_Fucking_Zero_Anim3", "Storm_Sex_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", AlphaMask("Storm_Sex_Fucking_Zero_Anim2", "Storm_Sex_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and Speed == 1", AlphaMask("Storm_Sex_Fucking_Zero_Anim1", "Storm_Sex_Heading_Mask"),
                "Player.Sprite and Player.Cock == 'in'", "Storm_Sex_Fucking_Zero_Anim0",
                "True", Null(),
                )
    contains:
            #Piercings
            ConditionSwitch(
                "StormX.Pierce == 'barbell' and Player.Sprite and Player.Cock == 'in' and Speed", "images/StormSex/Storm_Sex_Pierce_Pussy_BarbellF.png",
                "StormX.Pierce == 'ring' and Player.Sprite and Player.Cock == 'in' and Speed", "images/StormSex/Storm_Sex_Pierce_Pussy_RingF.png",
                "StormX.Pierce == 'barbell'", "images/StormSex/Storm_Sex_Pierce_Pussy_Barbell.png",
                "StormX.Pierce == 'ring'", "images/StormSex/Storm_Sex_Pierce_Pussy_Ring.png",
                "True", Null(),
                )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and Speed == 1", "Storm_Pussy_Spunk_Heading",
                "True", Null(),
                )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "Speed == 1", Null(),
                "'in' in StormX.Spunk and Player.Sprite and Player.Cock == 'in' and Speed and Player.Male", "images/StormSex/Storm_Sex_Spunk_Pussy_Over.png",
                "True", Null(),
                )

    #End Storm Pussy composite

image Storm_Sex_Lick_Pussy:
        "Lick_Anim"
        zoom 0.7
        offset (535,500)#(505,680)

image Storm_Sex_Lick_Ass:
        "Lick_Anim"
        zoom 0.7
        offset (535,550)

image Storm_Sex_Fondle_Pussy:
        "GropePussy_Storm"
        xzoom -1.5
        yzoom 1.5
        offset(-890,-300) #(535,500)
#        block:
#            ease 1 offset(-1000,0) #(535,500)
#            ease 1 offset(-1000,-1000) #(535,500)
#            ease 1 offset(0,-1000) #(535,500)
#            ease 1 offset(0,0) #(535,500)
#            repeat

#End Animations for Storm's Pussy during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_Sex_Zero_Cock:
        #this is the cock generally used by Storm's sex pose
        contains:
            subpixel True
#            "Zero_Blowcock"
            ConditionSwitch(
                "Player.Sprite and AlphaCock", "Zero_Blowcock" ,
                "Player.Sprite", "Zero_Ghostcock",
                "True", Null(),
                )
            subpixel True
            anchor (0.5,1.0)
            transform_anchor True
            offset (546,1007) #(546,1170)
            zoom 0.48

#            ConditionSwitch(
#                "AlphaCock", "Blowcock",
#                "True", "Ghostcock",
#                )
image Storm_Sex_Fucking_Mask:
        #This is the mask image for Kitty's wide open pussy
        # Used in "Storm_Sex_Speed2" and "Storm_Sex_Speed3"
        contains:
            "images/StormSex/Storm_Sex_Mask_Fucking.png"
            yoffset 3

# Start Storm Sex Pose Static / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_Sex_Static:
    # Pose for Storm's Sex Pose in which she is static
    contains:
            #Storm's underlying body
            subpixel True
            "Storm_Sex_Body"
            pos (0,-140) #X less is left, Y less is up
            block: #adds to 5
                ease 2 pos (0,-130) #0
                pause 0.8
                ease 2 ypos -140 #-140 high point, more negative = higher
                pause 0.2
                repeat
    contains:
            #Storm's Tits
            subpixel True
            "Storm_Sex_Tits"
            pos (0,-140) #X less is left, Y less is up
            block: #adds to 5
                pause 0.6
                ease 1.5 pos (0,-125)
                ease .5 ypos -130
                pause 0.9
                ease 1.5 ypos -140
                repeat
#            block: #adds to 5
#                pause 0.6
#                ease 1.8 pos (0,-125)
#                ease .5 ypos -130
#                pause 0.3
#                ease 1.8 ypos -140
#                repeat
    contains:
            #Storm's Legs
            subpixel True
            "Storm_Sex_Legs"
            pos (0,-140) #X less is left, Y less is up
#            block: #adds to 5
#                pause 0.2
#                ease 2 ypos -130 #0
#                pause 0.8
#                ease 2 ypos -140 #-130
#                repeat
    contains:
            subpixel True
            ConditionSwitch(
                "Player.Sprite", "Zero_Blowcock" ,
                "True", Null(),
                )
            subpixel True
            anchor (0.5,1.0)
            transform_anchor True
            offset (506,870) #1170 #546,1020
            zoom 0.48
            rotate 10
            block: #intentionally out of synch, just slaps
                pause 1
                ease .4 rotate 9
                ease .2 rotate 10
                repeat
    contains:
            #Storm's Feet
            subpixel True
            ConditionSwitch(
                #Footjob overlay
#                "ShowFeet", "Storm_Sex_Feet",
                "ShowFeet", AlphaMask("Storm_Sex_Feet", "images/StormSex/Storm_Sex_Mask_Foot2.png"),
                "True", Null(),
                )
            pos (0,-140) #X less is left, Y less is up
#            block: #adds to 5
#                pause 0.2
#                ease 2 ypos -130 #0
#                pause 0.8
#                ease 2 ypos -140 #-130
#                repeat
# End main animation for Sex Pose Static

# End Storm Sex Pose Speed Static / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Storm Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Storm Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_Sex_Fucking_Speed0:
    # Pose for Storm's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Storm's underlying body
            subpixel True
            "Storm_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                ease 2 pos (0,-140) #0
                pause 0.8
                ease 2 ypos -180 #-130
                pause 0.2
                repeat
    contains:
            #Storm's Tits
            subpixel True
            "Storm_Sex_Tits"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 pos (0,-120)
                ease 0.9 ypos -130
                pause 0.1
                ease 1.8 ypos -180
                repeat
    contains:
            #Storm's Legs
            subpixel True
            "Storm_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -140 #0
                pause 0.8
                ease 2 ypos -180 #-130
                repeat
# End main animation for Sex Pose Fucking Speed 1


image Storm_Sex_Fucking_Zero_Anim0:
        #this is Storm's sex animation, Speed 1 Fucking
        contains:
            subpixel True
            "Storm_Sex_Zero_Cock"
#            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            subpixel True
            pos (0,40)#(498,530)
            block:
                pause 0.2
                easeout 1 ypos 20 #-140
                easein .8 ypos 10 #-140
                pause 1.4
                easeout 0.6 ypos 10 #-140
                easein 1 ypos 40 #-10
                repeat

# End Storm Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Storm Sex Pose Speed 1 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_Sex_Fucking_Speed1:
    # Pose for Storm's Sex Pose in which she is fucking at speed 1 (heading)
    contains:
            #Storm's underlying body
            subpixel True
            "Storm_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                ease 2 pos (0,-130)
                pause 0.8
                ease 2 ypos -180
                pause 0.2
                repeat
    contains:
            #Storm's Tits
            subpixel True
            "Storm_Sex_Tits"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 1.9 pos (0,-120) #2.1
                ease 0.6 ypos -130 #.8
                pause 0.3
                ease 2 ypos -180 #1.9
                repeat
    contains:
            #Storm's Legs
            subpixel True
            "Storm_Sex_Legs"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -130 #0
                pause 0.8
                ease 2 ypos -180 #-130
                repeat
# End main animation for Sex Pose Fucking Speed 1


image Storm_Sex_Fucking_Zero_Anim1:
        #this is Storm's sex animation, Speed 1 Fucking
        contains:
            subpixel True
            "Storm_Sex_Zero_Cock"
#            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            subpixel True
            pos (0,40)#(498,530)
            block:
                pause 0.2
                ease 2 ypos -10 #-140
                pause .8
                ease 2 ypos 40 #-10
                repeat

image Storm_Sex_Heading_Mask:
        #This is the mask image for Storm's heading pussy
        contains:
            "images/StormSex/Storm_Sex_Mask_Fucking.png"
            yoffset 10
            block:
                pause 0.2
                ease 2 yoffset 3
                pause 0.8
                ease 2 yoffset 10
                repeat


image Storm_Sex_Heading_Pussy:
        #This is the image for Storm's heading pussy growing
        contains:
            "images/StormSex/Storm_Sex_Pussy_Fucking_Base.png"
        contains:
            "images/StormSex/Storm_Sex_Pussy_Fucking.png"
            anchor (0.5,0)
            transform_anchor True
            subpixel True
            xoffset 560
            xzoom .7
            block:
                pause 0.2
                ease 1.2 xzoom 1
                ease 0.4 xzoom .9
                pause 1.2
                ease 0.2 xzoom 1
                ease 1.8 xzoom .7
                repeat

image Storm_Pussy_Spunk_Heading:
        #This is the image for Storm's heading pussy cum
        contains:
            ConditionSwitch(
                "'in' in StormX.Spunk and Player.Sprite and Player.Cock == 'in' and Speed == 1 and Player.Male", "images/StormSex/Storm_Sex_Spunk_Pussy_Over.png",
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
                ease 0.4 xzoom .9
                pause 1.2
                ease 0.2 xzoom 1
                ease 1.8 xzoom .7
                repeat

# End Storm Sex Pose Speed 1 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Storm Sex Pose Speed 2 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_Sex_Fucking_Speed2:
    # Pose for Storm's Sex Pose in which she is fucking at speed 2
    contains:
            #Storm's underlying body
            subpixel True
            "Storm_Sex_Body"
            pos (0,-130) #X less is left, Y less is up
            block: #adds to 4.2
                ease 1 pos (0,0)
                pause 1
                ease 2 ypos -130
                pause 0.2
                repeat
    contains:
            #Storm's Tits
            subpixel True
            "Storm_Sex_Tits"
            pos (0,-130) #X less is left, Y less is up
            block: #adds to 4.2
                pause 0.1
                ease 0.9 pos (0,15) #1
                ease 0.5 ypos -5 #0.5
                ease 0.3 ypos 0 #0.3
                pause 0.3 #0.3
                ease 2 ypos -135 #2
                pause 0.1
                repeat
    contains:
            #Storm's Legs
            subpixel True
            "Storm_Sex_Legs"
            pos (0,-130) #X less is left, Y less is up
            block: #adds to 4.2
                pause 0.2
                ease 0.95 ypos 5
                ease 0.25 ypos 0
                pause 0.8
                ease 2 ypos -130
                repeat
#    contains:
#            #Zero's cock in the sex pose
#            AlphaMask("Storm_Sex_Fucking_Zero_Anim2", "Storm_Sex_Fucking_Mask")
# End main animation for Sex Pose Fucking Speed 2


image Storm_Sex_Fucking_Zero_Anim2:
        #this is Storm's sex animation, Speed 2 Fucking
        contains:
            subpixel True
            "Storm_Sex_Zero_Cock"
#            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            subpixel True
            pos (0,-10)#(498,530)
            block:
                pause 0.2
                ease 0.95 ypos -145
                ease 0.25 ypos -140
                pause .8
                ease 2 ypos -10
                repeat

# End Storm Sex Pose Speed 2 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Storm Sex Pose Speed 3 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_Sex_Fucking_Speed3:
    # Pose for Storm's Sex Pose in which she is fucking at speed 3
    contains:
            #Storm's underlying body
            subpixel True
            "Storm_Sex_Body"
            pos (0,-100) #X less is left, Y less is up
            block: #adds to 1.8
                ease .5 pos (0,0)
                pause .4
                ease .9 ypos -100
                repeat
    contains:
            #Storm's Tits
            subpixel True
            "Storm_Sex_Tits"
            pos (0,-100) #X less is left, Y less is up
            block: #adds to 1.8
                pause 0.05
                ease 0.55 pos (0,15)
                ease 0.2 ypos -5
                ease 0.2 ypos 0
                ease 0.75 ypos -100
                pause 0.05
                repeat
    contains:
            #Storm's Legs
            subpixel True
            "Storm_Sex_Legs"
            pos (0,-100) #X less is left, Y less is up
            block: #adds to 1.8
                pause 0.1
                ease 0.55 ypos 15
                ease 0.15 ypos 0
                pause 0.25
                ease 0.75 ypos -100
                repeat

# End main animation for Sex Pose Fucking Speed 3


image Storm_Sex_Fucking_Zero_Anim3:
        #this is Storm's sex animation, Speed3 Fucking
        contains:
            subpixel True
            "Storm_Sex_Zero_Cock"
            subpixel True
            pos (0,-40)
            block:
                pause 0.1
                ease 0.55 ypos -155
                ease 0.15 ypos -140
                pause 0.25
                ease 0.75 ypos -40
                repeat

# End Storm Sex Pose Speed 3 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Animations for Storm's Ass during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Storm's Ass during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_Sex_Anus:
#    contains:
#            #Anus background plate
#            ConditionSwitch(
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/StormSex/Storm_Sex_Hole_Open.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/StormSex/Storm_Sex_Hole_Open.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed", "Storm_Sex_Anal_Heading",
#            "Player.Sprite and Player.Cock == 'anal'", "Storm_Sex_Anal_Tip",
#            "StormX.Loose", "images/StormSex/Storm_Sex_Hole_Loose.png",
#            "True", "images/StormSex/Storm_Sex_Hole_Tight.png",
#            )
#    contains:
#            #Spunk under penis
#            ConditionSwitch(
#                "'anal' not in StormX.Spunk", Null(),
#                "Player.Sprite and Player.Cock != 'anal' and Speed >= 1", "images/StormSex/Storm_Sex_Spunk_Anal_Under.png",
#                "Player.Sprite and Player.Cock != 'anal' and Speed == 1", "Storm_Sex_Anal_Spunk_Heading_Under",
#                "True", "images/StormSex/Storm_Sex_Spunk_Anal_Closed.png",
#                )
    contains:
            # The animation of Zero's moving penis, masked by her anus shape
            ConditionSwitch(
                "not Player.Sprite or Player.Cock != 'anal'", Null(),
                "Speed >= 3",  AlphaMask("Storm_Sex_Anal_Zero_Anim3", "Storm_Sex_Anal_Mask"),
                "Speed >= 2", AlphaMask("Storm_Sex_Anal_Zero_Anim2", "Storm_Sex_Anal_Mask"),
                "Speed", AlphaMask("Storm_Sex_Anal_Zero_Anim1", "Storm_Sex_Anal_Mask"),
                "True", AlphaMask("Storm_Sex_Anal_Zero_Anim0", "Storm_Sex_Anal_Mask"),
                )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "'anal' not in StormX.Spunk or not Player.Sprite or Player.Cock != 'anal' or not Speed or not Player.Male", Null(),
                "Speed == 1", "Storm_Sex_Anal_Spunk_Heading_Over",
                "True", "images/StormSex/Storm_Sex_Spunk_Anal_Over.png",
                )

image Storm_Sex_Anal_Spunk_Heading_Over:
    "images/StormSex/Storm_Sex_Spunk_Anal_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8
    block:
        #total 5 second
        ease .75 xzoom 1.0   #(1.0)
        pause 1.75
        ease .25 xzoom 1.0  #(1.0)
        ease 2.25 xzoom 0.8   #(0.6)
        repeat
image Storm_Sex_Anal_Spunk_Heading_Under:
    "images/StormSex/Storm_Sex_Spunk_Anal_Under.png"
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

image Storm_Sex_Anal_Mask:
        #This is the mask image for Kitty's wide open pussy
        # Used in "Storm_Sex_Speed2" and "Storm_Sex_Speed3"
        contains:
            "images/StormSex/Storm_Sex_Mask_Anal.png"
            yoffset 3

# Start Storm Sex Pose Speed 0 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_Sex_Anal_Speed0:
    # Pose for Storm's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Storm's underlying body
            subpixel True
            "Storm_Sex_Body"
            pos (0,-235) #X less is left, Y less is up
            parallel: #adds to 2.5
                ease 1 xpos 7 #0
                ease 1 xpos -14 #-180
                pause 0.5
                repeat
            parallel: #adds to 5
                ease 2 ypos -230
                pause 0.8
                ease 2 ypos -235
                pause 0.2
                repeat
    contains:
            #Storm's Tits
            subpixel True
            "Storm_Sex_Tits"
            pos (0,-235) #X less is left, Y less is up
            parallel: #adds to 2.5
                pause 0.1
                ease .9 pos (10,-235) #0
                ease .3 xpos 7 #0
                ease .9 xpos -20 #-180
                ease .3 xpos -14 #-180
                repeat
#            parallel: #adds to 5
#                pause 0.2
#                ease 2.1 ypos -220
#                ease .8 ypos -230
#                ease 1.9 ypos -235
#                repeat
    contains:
            #Storm's Legs
            subpixel True
            "Storm_Sex_Legs"
            pos (-20,-235) #X less is left, Y less is up
            parallel: #adds to 2.5
                ease 1 xpos 10 #0
                ease 1 xpos -20 #-180
                pause 0.5
                repeat
            parallel: #adds to 5
                pause 0.2
                ease 2 ypos -230 #0
                pause 0.8
                ease 2 ypos -235 #-180
                repeat
# End main animation for Sex Pose Anal Speed 0

image Storm_Sex_Anal_Zero_Anim0:
    contains:
            subpixel True
            ConditionSwitch(
                "not Player.Sprite", Null(),
                "True", "Zero_Blowcock" ,
                )
            subpixel True
            anchor (0.5,1.0)
            transform_anchor True
            offset (545,1007) #(546,1020)
            zoom 0.48
            rotate -1
            pos (25,95)#(498,530)
            parallel: #adds to 2.5
                ease 1 rotate 1
                ease 1 rotate -1
                pause 0.5
                repeat
            parallel: #adds to 2.5
                ease 1 xpos -5 #-140
                ease 1 xpos 25 #-10
                pause 0.5
                repeat
            parallel:  #adds to 5
                pause 0.2
                ease 2 ypos 90 #-140
                pause .8
                ease 2 ypos 95 #-10
                repeat

# End Storm Sex Pose Speed 0 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Storm Sex Pose Speed 1 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_Sex_Anal_Speed1:
    # Pose for Storm's Sex Pose in which she is fucking at speed 1 (heading)
    contains:
            #Storm's underlying body
            subpixel True
            "Storm_Sex_Body"
            pos (0,-230) #X less is left, Y less is up
            block: #adds to 5
                ease 2 pos (0,-180)
                pause 0.8
                ease 2 ypos -230
                pause 0.2
                repeat
    contains:
            #Storm's Tits
            subpixel True
            "Storm_Sex_Tits"
            pos (0,-230) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 pos (0,-170) #2.1
                ease 0.6 ypos -180 #.8
                pause 0.2
                ease 2 ypos -230 #1.9
                repeat
    contains:
            #Storm's Legs
            subpixel True
            "Storm_Sex_Legs"
            pos (0,-230) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -180 #0
                pause 0.8
                ease 2 ypos -230 #-180
                repeat
# End main animation for Sex Pose Anal Speed 1


image Storm_Sex_Anal_Zero_Anim1:
        #this is Storm's sex animation, Speed 1 Anal
        contains:
            subpixel True
            "Storm_Sex_Zero_Cock"
#            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            subpixel True
            pos (5,90)#(498,530)
            block: #adds to 5
                pause 0.2
                ease 2 ypos 40 #-140
                pause .8
                ease 2 ypos 90 #-10
                repeat

# End Storm Sex Pose Speed 1 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Storm Sex Pose Speed 2 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_Sex_Anal_Speed2:
    # Pose for Storm's Sex Pose in which she is doing anal at speed 2
    contains:
            #Storm's underlying body
            subpixel True
            "Storm_Sex_Body"
            pos (0,-130) #X less is left, Y less is up
            block: #adds to 4.2
                ease 1 pos (0,0)
                pause 1
                ease 2 ypos -130
                pause 0.2
                repeat
    contains:
            #Storm's Tits
            subpixel True
            "Storm_Sex_Tits"
            pos (0,-130) #X less is left, Y less is up
            block: #adds to 4.2
                pause 0.1
                ease 0.9 pos (0,15) #1
                ease 0.5 ypos -5 #0.5
                ease 0.3 ypos 0 #0.3
                pause 0.3 #0.3
                ease 2 ypos -135 #2
                pause 0.1
                repeat
    contains:
            #Storm's Legs
            subpixel True
            "Storm_Sex_Legs"
            pos (0,-130) #X less is left, Y less is up
            block: #adds to 4.2
                pause 0.2
                ease 0.95 ypos 5
                ease 0.25 ypos 0
                pause 0.8
                ease 2 ypos -130
                repeat
#    contains:
#            #Zero's cock in the sex pose
#            AlphaMask("Storm_Sex_Fucking_Zero_Anim2", "Storm_Sex_Fucking_Mask")
# End main animation for Sex Pose Fucking Speed 2


image Storm_Sex_Anal_Zero_Anim2:
        #this is Storm's sex animation, Speed 2 Fucking
        contains:
            subpixel True
            "Storm_Sex_Zero_Cock"
#            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            subpixel True
            pos (5,-10)#(498,530)
            block:
                pause 0.2
                ease 0.95 ypos -145
                ease 0.25 ypos -140
                pause .8
                ease 2 ypos -10
                repeat

# End Storm Sex Pose Speed 2 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Storm Sex Pose Speed 3 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_Sex_Anal_Speed3:
    # Pose for Storm's Sex Pose in which she is Anal at speed 3
    contains:
            #Storm's underlying body
            subpixel True
            "Storm_Sex_Body"
            pos (0,-100) #X less is left, Y less is up
            block: #adds to 1.8
                ease .5 pos (0,0)
                pause .4
                ease .9 ypos -100
                repeat
    contains:
            #Storm's Tits
            subpixel True
            "Storm_Sex_Tits"
            pos (0,-100) #X less is left, Y less is up
            block: #adds to 1.8
                pause 0.05
                ease 0.55 pos (0,15)
                ease 0.2 ypos -5
                ease 0.2 ypos 0
                ease 0.75 ypos -100
                pause 0.05
                repeat

    contains:
            #Storm's Legs
            subpixel True
            "Storm_Sex_Legs"
            pos (0,-100) #X less is left, Y less is up
            block: #adds to 1.8
                pause 0.1
                ease 0.55 ypos 15
                ease 0.15 ypos 0
                pause 0.25
                ease 0.75 ypos -100
                repeat
# End main animation for Sex Pose Fucking Speed 3


image Storm_Sex_Anal_Zero_Anim3:
        #this is Storm's sex animation, Speed3 Anal
        contains:
            subpixel True
            "Storm_Sex_Zero_Cock"
            subpixel True
            pos (5,-40)
            block:#adds to 1.8
                pause 0.1
                ease 0.55 ypos -155
                ease 0.15 ypos -140
                pause 0.25
                ease 0.75 ypos -40
                repeat

# End Storm Sex Pose Speed 3 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Storm Sex Pose Speed 1 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_Sex_Hotdog_Speed1:
    # Pose for Storm's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Storm's underlying body
            subpixel True
            "Storm_Sex_Body"
            pos (0,-160) #X less is left, Y less is up
            block: #adds to 5
                ease 2 pos (0,-80) #-140
                pause 0.8
                ease 2 ypos -160 #-180
                pause 0.2
                repeat
    contains:
            #Storm's Tits
            subpixel True
            "Storm_Sex_Tits"
            pos (0,-160) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 pos (0,-75)
                ease .7 ypos -85 #.9
                pause 0.1
                ease 2 ypos -160 #1.8
                repeat
    contains:
            #Storm's Legs
            subpixel True
            "Storm_Sex_Legs"
            pos (0,-160) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -80 #0
                pause 0.8
                ease 2 ypos -160 #-130
                repeat
    contains:
            subpixel True
            "Storm_Sex_Zero_Cock"
            subpixel True
            pos (0,-140)
            block: #adds to 5
                pause 1.5
                ease 0.7 ypos -120 #0
                pause 1
                ease 1 ypos -145 #-130
                ease 0.2 ypos -140 #-130
                pause .6
                repeat
    contains:
            #Storm's Feet
            subpixel True
            ConditionSwitch(
                #Footjob overlay
                "ShowFeet", AlphaMask("Storm_Sex_Feet", "images/StormSex/Storm_Sex_Mask_Foot2.png"),
                "True", Null(),
                )
            pos (0,-160) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -80 #0
                pause 0.8
                ease 2 ypos -160 #-130
                repeat

# End main animation for Sex Pose Hotdog Speed 1

# End Storm Sex Pose Speed 1 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Storm Sex Pose Speed 2 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_Sex_Hotdog_Speed2:
    # Pose for Storm's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Storm's underlying body
            subpixel True
            "Storm_Sex_Body"
            pos (0,-160) #X less is left, Y less is up
            block: #adds to 2.5
                ease 1 pos (0,-80) #-140
                pause 0.4
                ease 1 ypos -160 #-180
                pause 0.1
                repeat
    contains:
            #Storm's Tits
            subpixel True
            "Storm_Sex_Tits"
            pos (0,-160) #X less is left, Y less is up
            block: #adds to 2.5
                pause 0.1
                ease .9 pos (0,-70)
                ease .5 ypos -80
                ease 1 ypos -160
                repeat
    contains:
            #Storm's Legs
            subpixel True
            "Storm_Sex_Legs"
            pos (0,-160) #X less is left, Y less is up
            block: #adds to 2.5
                pause 0.1
                ease 1 ypos -80 #0
                pause 0.4
                ease 1 ypos -160 #-130
                repeat
    contains:
            subpixel True
            "Storm_Sex_Zero_Cock"
            subpixel True
            pos (0,-140)
            block: #adds to 2.5
                pause 0.8
                ease 0.3 ypos -120 #0
                pause 0.5
                ease 0.5 ypos -145 #-130
                ease 0.1 ypos -140 #-130
                pause 0.3
                repeat
    contains:
            #Storm's Feet
            subpixel True
            ConditionSwitch(
                #Footjob overlay
                "ShowFeet", AlphaMask("Storm_Sex_Feet", "images/StormSex/Storm_Sex_Mask_Foot2.png"),
                "True", Null(),
                )
            pos (0,-160) #X less is left, Y less is up
            block: #adds to 2.5
                pause 0.1
                ease 1 ypos -80 #0
                pause 0.4
                ease 1 ypos -160 #-130
                repeat

# End main animation for Sex Pose Hotdog Speed 2

# End Storm Sex Pose Speed 2 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Storm Sex Pose Speed 0 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_Sex_FJ_Speed0:
    # Pose for Storm's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Storm's underlying body
            subpixel True
            "Storm_Sex_Body"
            pos (0,-160) #X less is left, Y less is up
            block: #adds to 5
                ease 2 pos (0,-140) #-140
                pause 0.8
                ease 2 ypos -160 #-180
                pause 0.2
                repeat
    contains:
            #Storm's Tits
            subpixel True
            "Storm_Sex_Tits"
            pos (0,-160) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 pos (0,-140)
                ease 0.7 ypos -145 #.9
                pause 0.1
                ease 2 ypos -160 #1.8
                repeat
    contains:
            #Storm's Legs
            subpixel True
            "Storm_Sex_Legs"
            pos (0,-200) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -190 #0
                pause 0.8
                ease 2 ypos -200 #-130
                repeat
    contains:
            subpixel True
            "Storm_Sex_Zero_Cock"
            subpixel True
            pos (0,-140)
    contains:
            #Storm's Legs
            subpixel True
            ConditionSwitch(
                #Footjob overlay
                "ShowFeet", AlphaMask("Storm_Sex_Feet", "images/StormSex/Storm_Sex_Mask_Foot.png"),
                "True", Null(),
                )
            pos (0,-200) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -190 #0
                pause 0.8
                ease 2 ypos -200 #-130
                repeat

# End main animation for Sex Pose Footjob Speed 0

# End Storm Sex Pose Speed 0 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Storm Sex Pose Speed 1 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_Sex_FJ_Speed1:
    # Pose for Storm's Sex Pose in which she is fucking at speed 1 (slow)
    contains:
            #Storm's underlying body
            subpixel True
            "Storm_Sex_Body"
            pos (0,-160) #X less is left, Y less is up
            block: #adds to 5
                ease 2 pos (0,-80) #-140
                pause 0.8
                ease 2 ypos -160 #-180
                pause 0.2
                repeat
    contains:
            #Storm's Tits
            subpixel True
            "Storm_Sex_Tits"
            pos (0,-160) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 pos (0,-75)
                ease 0.7 ypos -85 #.9
                pause 0.1
                ease 2 ypos -160 #1.8
                repeat
    contains:
            #Storm's Legs
            subpixel True
            "Storm_Sex_Legs"
            pos (0,-200) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -80 #0
                pause 0.8
                ease 2 ypos -200 #-130
                repeat
    contains:
            subpixel True
            "Storm_Sex_Zero_Cock"
            subpixel True
            pos (0,-140)
            block:
                pause 1.5
                ease 0.7 ypos -120 #0
                pause 1
                ease 1 ypos -140 #-130
                pause 0.8
                repeat
    contains:
            #Storm's Legs
            subpixel True
            ConditionSwitch(
                #Footjob overlay
                "ShowFeet", AlphaMask("Storm_Sex_Feet", "images/StormSex/Storm_Sex_Mask_Foot.png"),
                "True", Null(),
                )
            pos (0,-200) #X less is left, Y less is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -80 #0
                pause 0.8
                ease 2 ypos -200 #-130
                repeat

# End main animation for Sex Pose Footjob Speed 1

# End Storm Sex Pose Speed 1 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Storm Sex Pose Speed 2 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_Sex_FJ_Speed2:
    # Pose for Storm's Sex Pose in which she is fucking at speed 2 (fast)
    contains:
            #Storm's underlying body
            subpixel True
            "Storm_Sex_Body"
            pos (0,-160) #X less is left, Y less is up
            block: #adds to 2.1
                ease 0.9 pos (0,-80) #-140
                pause 0.1
                ease 1 ypos -160 #-180
                pause 0.1
                repeat
    contains:
            #Storm's Tits
            subpixel True
            "Storm_Sex_Tits"
            pos (0,-160) #X less is left, Y less is up
            block: #adds to 2.1
                pause 0.1
                ease 0.8 pos (0,-75)
                ease 0.2 ypos -85 #.9
                ease 1 ypos -160 #1.8
                repeat
    contains:
            #Storm's Legs
            subpixel True
            "Storm_Sex_Legs"
            pos (0,-200) #X less is left, Y less is up
            block: #adds to 2.1
                pause 0.1
                ease 0.9 ypos -150 #0
                pause 0.1
                ease 1 ypos -250 #-130
                repeat
    contains:
            subpixel True
            "Storm_Sex_Zero_Cock"
            subpixel True
            pos (0,-140)
            block: #adds to 2.1
                pause 0.6
                ease 0.4 ypos -120 #0
                pause 0.2
                ease 0.5 ypos -140 #-130
                pause 0.4
                repeat
    contains:
            #Storm's Legs
            subpixel True
            ConditionSwitch(
                #Footjob overlay
                "ShowFeet", AlphaMask("Storm_Sex_Feet", "images/StormSex/Storm_Sex_Mask_Foot.png"),
                "True", Null(),
                )
            pos (0,-200) #X less is left, Y less is up
            block:  #adds to 2.1
                pause 0.1
                ease 0.9 ypos -150 #0
                pause 0.1 #0.4
                ease 1 ypos -250 #-130
                repeat

# End main animation for Sex Pose Footjob Speed 2

# End Storm Sex Pose Speed 2 Footjob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     Sex Launch/Reset
label Storm_Sex_Launch(Line = Trigger):

##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    $ StormX.Pose = "sex"
##    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary

    $ Line = "solo" if not Line else Line
    if Line == "sex":
        $ Player.Sprite = 1
        $ Player.Cock = "in"
        call Cock_Occupied(StormX,"pussy")
        if Trigger2 in ("fondle pussy","dildo pussy","lick pussy"):
                $ Trigger2 = 0
    elif Line == "anal":
        $ Player.Sprite = 1
        $ Player.Cock = "anal"
        call Cock_Occupied(StormX,"anal")
        if Trigger2 in ("insert ass","dildo anal","lick ass"):
                $ Trigger2 = 0
    elif Line == "hotdog":
        $ Player.Sprite = 1
        if StormX.PantsNum() == 5: #upskirts her if she's in a skirt
                $ StormX.Upskirt = 1
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
        call Zero_Strapped(StormX) #puts strap-on on.
    $ Trigger = Line

    if StormX.Pose == "doggy":
            call Storm_Doggy_Launch(Line)
            return
    if renpy.showing("Storm_SexSprite"):
        return
    $ Speed = 0
    call Girl_Hide(StormX,1)
    show Storm_SexSprite zorder 150
    with dissolve
    return

label Storm_Sex_Reset:
    if renpy.showing("Storm_Doggy_Animation"):
        call Storm_Doggy_Reset
        return
    if not renpy.showing("Storm_SexSprite"):
        return
    $ StormX.ArmPose = 2
    hide Storm_SexSprite
    call Girl_Hide(StormX)
#    call Set_The_Scene(Dress = 0)
    show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) zorder StormX.Layer:
        alpha 1 zoom 1 offset (0,0) anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return


# End Storm Sex Pose Content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Storm's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Storm_BJ_Animation:#BJ_NewTest:                                                                #core BJ animation
    LiveComposite(
        (858,928),
        (0,0), ConditionSwitch( #-270,-160
            # Storm's hair backside
            "Speed == 0", "Storm_BJ_Anim0",               #Static
            "Speed == 1", "Storm_BJ_Anim1",               #Licking
            "Speed == 2", "Storm_BJ_Anim2",               #Heading
            "Speed == 3", "Storm_BJ_Anim3",               #Sucking
            "Speed == 4", "Storm_BJ_Anim4",               #Deepthroat
            "Speed == 5", "Storm_BJ_Anim5",               #Cumming High
            "Speed == 6", "Storm_BJ_Anim6",               #Cumming Deep
            "True", Null(),
            ),
        )
    zoom .55
    anchor (.5,.5)

image Storm_BJ_HairBack:
        #Hair underlay
        ConditionSwitch(
                "StormX.Hair == 'mohawk' or StormX.Hair == 'wethawk' or StormX.Hair == 'short'", Null(), #"images/StormBJFace/Storm_BJ_Hair_Mohawk_Under.png",
                "(StormX.Hair == 'long' and StormX.Water) or StormX.Hair == 'wet'", Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_WetL_Under.png"),
                "not Player.Male and 'facial' in StormX.Spunk",Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_WetL_Under.png"),
                "True", Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_Long_Under.png"),
                ),
        zoom 1.4
        anchor (0.5, 0.5)

image Storm_BJ_HairTop:
    contains:
        ConditionSwitch(
                "StormX.Hair == 'short'", "images/StormBJFace/Storm_BJ_Hair_Short.png",
                "(StormX.Hair == 'mohawk' and StormX.Water) or StormX.Hair == 'wethawk'", Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_WetM_Over.png"),
                "StormX.Hair == 'mohawk' and not Player.Male and 'facial' in StormX.Spunk",Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_WetM_Over.png"),
                "StormX.Water or StormX.Hair == 'wet'", Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_WetL_Over.png"),
                "not Player.Male and 'facial' in StormX.Spunk",Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_WetL_Over.png"),
                "StormX.Hair == 'mohawk'", Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_Mohawk_Over.png"),
                "True", Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_Long_Over.png"),
                )
    contains:
        ConditionSwitch(
                #cum on the hair
                "'hair' in StormX.Spunk and (StormX.Water or StormX.Hair == 'wethawk' or StormX.Hair == 'wet') and Player.Male", "images/StormBJFace/Storm_BJ_Spunk_HairW.png",
                "'hair' in StormX.Spunk and StormX.Hair == 'mohawk' and Player.Male", "images/StormBJFace/Storm_BJ_Spunk_HairM.png",
                "'hair' in StormX.Spunk and Player.Male", "images/StormBJFace/Storm_BJ_Spunk_HairL.png",
                "True", Null(),
                )
    zoom 1.4
    anchor (0.5, 0.5)


image Storm_BJ_Backdrop1: #delete if other works better. . .
    contains:
            #blanket
            ConditionSwitch(
                "'blanket' in StormX.RecentActions", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
                "True", Null(),
                ),
            zoom 2
            anchor (.5,.5)
            pos (350,600)
#    contains:
#            #body backdrop
#            "Storm_Sex_Torso"
#            zoom 2.5
#            anchor (.5,.5)
#            pos (160,750)
#    zoom 1.5
#    offset (-300,-200)

image Storm_BJ_Head:                                                                            #These are all the details of the face
    LiveComposite(
        (858,928),
#        (0,0), ConditionSwitch(
#            # hair underlayer in normal mode
##            "StormX.Water or StormX.Hair == 'wet'", Null(),
#            "StormX.Hair == 'mohawk'", Null(), #"images/StormBJFace/Storm_BJ_Hair_Mohawk_Under.png",
#            "True", Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_Long_Under.png"),
#            ),
        (0,0), ConditionSwitch(
            # Basic Face layer
#            "Speed <= 2 or Speed == 5 or not renpy.showing('Storm_BJ_Animation')", ConditionSwitch(
#                    # If the animation isn't sucking, or if not in BJ pose
#                    "StormX.Blush", "images/StormBJFace/Storm_BJ_FaceClosed_Blush.png",
#                    "True", "images/StormBJFace/Storm_BJ_FaceClosed.png",
#                    ),
            "StormX.Blush > 1", "images/StormBJFace/Storm_BJ_Head_Blush2.png",
#            "StormX.Blush", "images/StormBJFace/Storm_BJ_Head_Blush1.png",
            "True", "images/StormBJFace/Storm_BJ_Head_Blush0.png"
            ),
        (0,0), ConditionSwitch(
            #Mouth
#            "(Speed == 2 or Speed == 5) and renpy.showing('Storm_BJ_Animation')", ConditionSwitch(
#                    # If the Heading animation is active
##                    "StormX.Blush", "images/StormBJFace/Storm_BJ_FaceClosed_Blush.png",
##                    "True", "images/StormBJFace/Storm_BJ_FaceClosed.png"
#                    ),


#            "True",Recolor("Storm", "Lips", "images/StormBJFace/Storm_BJ_Mouth_Sucking.png"), #sucking
            "Speed and renpy.showing('Storm_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
                    "Speed == 1", Recolor("Storm", "Lips", "images/StormBJFace/Storm_BJ_Mouth_Tongue.png"),  #licking
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", Recolor("Storm", "Lips", "images/StormBJFace/Storm_BJ_Mouth_Sucking.png"), #sucking
                    "Speed == 4", Recolor("Storm", "Lips", "images/StormBJFace/Storm_BJ_Mouth_Sucking.png"), #deepthroat
                    "Speed == 6", Recolor("Storm", "Lips", "images/StormBJFace/Storm_BJ_Mouth_Sucking.png"), #cumming
                    ),
            "renpy.showing('Storm_CUN_Animation') and Speed", Recolor("Storm", "Lips", "images/StormBJFace/Storm_BJ_Mouth_Tongue.png"),
            "Speed == 3 and renpy.showing('Storm_TJ_Animation')", Recolor("Storm", "Lips", "images/StormBJFace/Storm_BJ_Mouth_Tongue.png"),
            "StormX.Mouth == 'normal'", Recolor("Storm", "Lips", "images/StormBJFace/Storm_BJ_Mouth_Smile.png"),
            "StormX.Mouth == 'lipbite'", Recolor("Storm", "Lips", "images/StormBJFace/Storm_BJ_Mouth_Lipbite.png"),
            "StormX.Mouth == 'sucking'", Recolor("Storm", "Lips", "images/StormBJFace/Storm_BJ_Mouth_Tongue.png"),
            "StormX.Mouth == 'kiss'", Recolor("Storm", "Lips", "images/StormBJFace/Storm_BJ_Mouth_Kiss.png"),
            "StormX.Mouth == 'sad'", Recolor("Storm", "Lips", "images/StormBJFace/Storm_BJ_Mouth_Sad.png"),
            "StormX.Mouth == 'smile'", Recolor("Storm", "Lips", "images/StormBJFace/Storm_BJ_Mouth_Smile.png"),
            "StormX.Mouth == 'smirk'", Recolor("Storm", "Lips", "images/StormBJFace/Storm_BJ_Mouth_Smirk.png"),
            "StormX.Mouth == 'grimace'", Recolor("Storm", "Lips", "images/StormBJFace/Storm_BJ_Mouth_Smile.png"),
            "StormX.Mouth == 'surprised'", Recolor("Storm", "Lips", "images/StormBJFace/Storm_BJ_Mouth_Kiss.png"),
            "StormX.Mouth == 'tongue'", Recolor("Storm", "Lips", "images/StormBJFace/Storm_BJ_Mouth_Tongue.png"),
            "True", Recolor("Storm", "Lips", "images/StormBJFace/Storm_BJ_Mouth_Smile.png"),
            ),
        (428,555), ConditionSwitch(   #(428,605)
            # Heading Mouth
#            "Speed == 2 and Trigger == 'blow'", At("Storm_BJ_MouthHeading", Storm_BJ_MouthAnim()),  #heading
            "not renpy.showing('Storm_BJ_Animation')", Null(),                       #heading
            "Speed == 2", "Storm_BJ_MouthHeading",#At("Storm_BJ_MouthHeading", Storm_BJ_MouthAnim()),  #heading
            "Speed == 5", "Storm_BJ_MouthCumHigh",#At("Storm_BJ_MouthHeading", Storm_BJ_MouthAnimC()), #cumming high
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Spunk layer
            "'mouth' not in StormX.Spunk or not Player.Male", Null(),
            "Speed and renpy.showing('Storm_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
                    "Speed == 1", "images/StormBJFace/Storm_BJ_Spunk_Tongue.png",  #licking
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", "images/StormBJFace/Storm_BJ_Spunk_SuckingUnder.png", #sucking
                    "Speed == 4", "images/StormBJFace/Storm_BJ_Spunk_SuckingUnder.png", #deepthroat
                    "Speed == 6", "images/StormBJFace/Storm_BJ_Spunk_SuckingUnder.png", #cumming
                    ),
            "StormX.Mouth == 'normal'", "images/StormBJFace/Storm_BJ_Spunk_Smile.png",
#            "StormX.Mouth == 'lipbite'", "images/StormBJFace/Storm_BJ_Spunk_Kiss.png",
#            "StormX.Mouth == 'kiss'", "images/StormBJFace/Storm_BJ_Spunk_Kiss.png",
#            "StormX.Mouth == 'sad'", "images/StormBJFace/Storm_BJ_Spunk_Kiss.png",
            "StormX.Mouth == 'smile'", "images/StormBJFace/Storm_BJ_Spunk_Smile.png",
#            "StormX.Mouth == 'smirk'", "images/StormBJFace/Storm_BJ_Spunk_Kiss.png",
#            "StormX.Mouth == 'surprised'", "images/StormBJFace/Storm_BJ_Spunk_Kiss.png",
            "StormX.Mouth == 'tongue'", "images/StormBJFace/Storm_BJ_Spunk_Tongue.png",
            "StormX.Mouth == 'sucking'", "images/StormBJFace/Storm_BJ_Spunk_SuckingUnder.png",
            "True", "images/StormBJFace/Storm_BJ_Spunk_Kiss.png",
            ),

        (0,0), ConditionSwitch(
            #wet face
            "Player.Male", Null(),
            "'mouth' not in StormX.Spunk and 'chin' not in StormX.Spunk", Null(),
            "'chin' not in StormX.Spunk and (StormX.Mouth == 'tongue' or Speed)", "images/StormBJFace/Storm_BJ_Wet_Tongue.png",
            "StormX.Mouth == 'tongue' or Speed", "images/StormBJFace/Storm_BJ_Wet_Tongue2.png",
            "'mouth' in StormX.Spunk or 'chin' in StormX.Spunk", "images/StormBJFace/Storm_BJ_Wet_Mouth.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Brows
            "StormX.Brows == 'angry'", "images/StormBJFace/Storm_BJ_Brows_Angry.png",
            "StormX.Brows == 'sad'", "images/StormBJFace/Storm_BJ_Brows_Sad.png",
            "StormX.Brows == 'surprised'", "images/StormBJFace/Storm_BJ_Brows_Surprised.png",
            "StormX.Brows == 'confused'", "images/StormBJFace/Storm_BJ_Brows_Confused.png",
            "True", "images/StormBJFace/Storm_BJ_Brows_Normal.png",
            ),
        (0,0), "Storm BJ Blink",
            #Eyes
        (0,0), "images/StormBJFace/Storm_BJ_Earring.png",
        (0,0), ConditionSwitch(
            #Hair overlay
            "StormX.Hair == 'short'", Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_Short_Over.png"),
            "(StormX.Hair == 'mohawk' and StormX.Water) or StormX.Hair == 'wethawk'", Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_WetM_Over.png"),
            "StormX.Hair == 'mohawk' and not Player.Male and 'facial' in StormX.Spunk", Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_WetM_Over.png"),
            "StormX.Water or StormX.Hair == 'wet'", Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_WetL_Over.png"),
            "not Player.Male and 'facial' in StormX.Spunk", Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_WetL_Over.png"),
            "StormX.Hair == 'mohawk'", Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_Mohawk_Over.png"),
            "True", Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_Long_Over.png"),
            ),
        (0,0), ConditionSwitch(
            # water overlay
            "not StormX.Water and not (not Player.Male and 'facial' in StormX.Spunk)", Null(),
            "True", "images/StormBJFace/Storm_BJ_Wet.png",
            ),
#        (0,0), "Storm_Tester",
        (0,0), ConditionSwitch(
            #cum on the face
            "'facial' in StormX.Spunk and Player.Male", "images/StormBJFace/Storm_BJ_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #cum on the hair
            "'hair' in StormX.Spunk and (StormX.Water or StormX.Hair == 'wethawk' or StormX.Hair == 'wet') and Player.Male", "images/StormBJFace/Storm_BJ_Spunk_HairW.png",
            "'hair' in StormX.Spunk and StormX.Hair == 'short' and Player.Male", "images/StormBJFace/Storm_BJ_Spunk_HairS.png",
            "'hair' in StormX.Spunk and StormX.Hair == 'mohawk' and Player.Male", "images/StormBJFace/Storm_BJ_Spunk_HairM.png",
            "'hair' in StormX.Spunk and Player.Male", "images/StormBJFace/Storm_BJ_Spunk_HairL.png",
            "True", Null(),
            ),
        )
    zoom 1.4
    anchor (0.5, 0.5)

image Storm_Tester:
            "images/StormBJFace/Storm_BJ_tester.jpg"
            alpha 0.5
image Storm BJ Blink:
        #eyeblinks
        ConditionSwitch(
            "StormX.Eyes == 'normal'", "images/StormBJFace/Storm_BJ_Eyes_Normal.png",
            "StormX.Eyes == 'sexy'", "images/StormBJFace/Storm_BJ_Eyes_Sexy.png",
            "StormX.Eyes == 'closed'", "images/StormBJFace/Storm_BJ_Eyes_Closed.png",
            "StormX.Eyes == 'surprised'", "images/StormBJFace/Storm_BJ_Eyes_Surprised.png",
            "StormX.Eyes == 'side'", "images/StormBJFace/Storm_BJ_Eyes_Side.png",
            "StormX.Eyes == 'stunned'", "images/StormBJFace/Storm_BJ_Eyes_Stunned.png",
            "StormX.Eyes == 'down'", "images/StormBJFace/Storm_BJ_Eyes_Down.png",
            "StormX.Eyes == 'manic'", "images/StormBJFace/Storm_BJ_Eyes_Surprised.png",
            "StormX.Eyes == 'squint'", "images/StormBJFace/Storm_BJ_Eyes_Sexy.png",
            "True", "images/StormBJFace/Storm_BJ_Eyes_Normal.png",
            ),
        choice:
            3.5
        choice:
            3.25
        choice:
            3
        "images/StormBJFace/Storm_BJ_Eyes_Closed.png"
        .25
        repeat

image Storm_BJ_MouthHeading:
    #the mouth used for the heading animations
    transform_anchor True
    contains:
#        Recolor("Storm", "Lips", "images/StormBJFace/Storm_BJ_Mouth_Sucking.png")
        "images/StormBJFace/Storm_BJ_Mouth_Heading.png"
        zoom 1.4
        anchor (0.50,0.6)  #(0.50,0.65)
    contains:
        ConditionSwitch(
            "'mouth' in StormX.Spunk and Player.Male", "images/StormBJFace/Storm_BJ_Spunk_SuckingUnder.png",#At("Storm_BJ_MaskHeading", Storm_BJ_MouthAnim()),
            "True", Null(),
            ),
        zoom 1.4
        anchor (0.50,0.6)  #(0.50,0.65)
    contains:
        ConditionSwitch(
            "'mouth' in StormX.Spunk and Player.Male", "images/StormBJFace/Storm_BJ_Spunk_SuckingOver.png",#At("Storm_BJ_MaskHeading", Storm_BJ_MouthAnim()),
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
        easein .30 zoom 0.45#0.55
        pause .30
        #1.5s to this point
        repeat

image Storm_BJ_MouthCumHigh:
    #the mouth used for the heading animations
    contains:
        Recolor("Storm", "Lips", "images/StormBJFace/Storm_BJ_Mouth_Sucking.png")
        zoom 1.4
        anchor (0.50,0.6)  #(0.50,0.65)
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

image Storm_BJ_MouthSuckingMask:
    #the mask used for sucking animations
    contains:
        "images/StormBJFace/Storm_BJ_Mouth_MaskS.png"
        zoom 1.4
#    contains: #see if this works, if not remove it
#        ConditionSwitch(
#            "'mouth' not in StormX.Spunk", Null(),
#            "Speed != 2 and Speed != 5", Null(),
#            "True", "images/StormBJFace/Storm_BJ_Spunk_SuckingOver.png",
#            )
#        zoom 1.4

#image Storm_BJ_MaskHeading:
#    #the mask used for the heading image
#    contains:
#        "images/StormBJFace/Storm_BJ_Mouth_MaskH.png"
#        #offset (-380,-595)

image Storm_BJ_MaskHeadingComposite:
    #The composite for the heading mask that goes over the face
    LiveComposite(
        (858,928),
        (300,462), ConditionSwitch(
            "Speed == 2", "Storm_BJ_MouthHeadingComposite",#At("Storm_BJ_MaskHeading", Storm_BJ_MouthAnim()),
            "Speed == 5", "Storm_BJ_MouthCumHighComposite",#At("Storm_BJ_MaskHeading", Storm_BJ_MouthAnimC()),
            "True", Null(),
            ),
        (300,462), ConditionSwitch(
            "Speed == 2 and 'mouth' in StormX.Spunk and Player.Male", "StormHeadingSpunk",#At("Storm_BJ_MaskHeading", Storm_BJ_MouthAnim()),
            "Speed == 5 and 'mouth' in StormX.Spunk and Player.Male", "StormCumHighSpunk",#At("Storm_BJ_MaskHeading", Storm_BJ_MouthAnimC()),
            "True", Null(),
            ),
        )
    zoom 1.8

image Storm_BJ_MouthHeadingComposite:
    #the mask for the overlay used for the heading animations
    transform_anchor True
    contains:
#        "Storm_BJ_MaskHeading"
        "images/StormBJFace/Storm_BJ_Mouth_MaskH.png"
#        "Storm_Tester"
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

image StormHeadingSpunk:
    #Spunk that goes over the sock when sucking
    transform_anchor True
    contains:
#        "Storm_BJ_MaskHeading"
        "images/StormBJFace/Storm_BJ_Spunk_SuckingOver.png"
#        "Storm_Tester"
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


image Storm_BJ_MouthCumHighComposite:
    #the mask for the overlay used for the cumming high animations
    contains:
#        "Storm_BJ_MaskHeading"
        "images/StormBJFace/Storm_BJ_Mouth_MaskH.png"
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

image StormCumHighSpunk:
    #Spunk that goes over the sock when sucking
    transform_anchor True
    contains:
        "images/StormBJFace/Storm_BJ_Spunk_SuckingOver.png"
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

image StormSuckingSpunk:
    #Spunk that goes over the sock when sucking
    contains:
        "images/StormBJFace/Storm_BJ_Spunk_SuckingOver.png"
        zoom 1.4
        anchor (0.5, 0.5)

# Start 0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Storm_BJ_Backdrop:
        #Her Body in the BJ pose
        contains:
            #blanket
            ConditionSwitch(
                "'blanket' in StormX.RecentActions", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
                "True", Null(),
                )
            zoom 1.2
            anchor (.5,.5)
            pos (180,-400)
#            block:
#                ease 1 pos (0,-600)
#                ease 1 pos (-350,0)
#                ease 1 pos (-350,0)
#                ease 1 pos (-350,-600)
#                repeat
#        contains:
#                #bra strap backing
#                "Storm_TJ_Braback"
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
                "Storm_TJ_Body"
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
#                "Storm_TJ_TitR"
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
                "Storm_TJ_Tits"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
#                parallel:
#                    ease 2 ypos -20
#                    pause .1
#                    ease 2 ypos -0
#                    pause .1
#                    repeat
        zoom 1.4
        offset (225,1100)

# End Storm BJ Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_BJ_Anim0:
        #Static animation
        contains:
                # Storm's hair backside
                "Storm_BJ_HairBack"
                subpixel True
                offset (350,210)#(0,0)     #-270,-160
        contains:
                #  Storm's body, everything below the chin
                "Storm_BJ_Backdrop"
                subpixel True
                offset (0,0)     #(-20,270)
        contains:
                # Storm's head Underlay
                "Storm_BJ_Head"
                subpixel True
                offset (350,210)     #-270,-160
        contains:
                # Cock
                "Blowcock"
                anchor (.5,.5)
                rotate -10
                offset (650,370)#(0,50)
#end Storm_BJ_Anim0 Static

image Storm_BJ_Anim1:
        #Licking animation
        contains:
                # Storm's hair backside
                "Storm_BJ_HairBack"
                subpixel True
                #offset (350,210)
                offset (350,175)  #top
                block:
                    ease 2.5 offset (375,310) #bottom
                    ease 2 offset (350,175)  #top
                    pause .5
                    repeat  #-270,-160
        contains:
                #  Storm's body, everything below the chin
                "Storm_BJ_Backdrop"
                subpixel True
                offset (0,-35)  #top
                block:
                    ease 2.5 offset (30,90) #bottom 25,50
                    ease 2 offset (0,-35)  #top
                    pause .5
                    repeat #(-20,270)
        contains:
                # Storm's head Underlay
                "Storm_BJ_Head"
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
                offset (650,370)
                rotate 0
                block:
                    ease 2 rotate -5 #410
                    pause .5
                    ease 2.5 rotate 0
                    repeat
#end Storm_BJ_Anim1 Licking


image Storm_BJ_Anim2:
        #Heading animation
        contains:
                # Storm's hair backside
                "Storm_BJ_HairBack"
                subpixel True
                #offset (350,210)
                offset (350,190)     #top (0,-40), -20 is crown, 0 is mid
                block:
                    ease 1 yoffset 270           #bottom
                    ease 1.5 yoffset 190     #top
                    repeat #-270,-160
        contains:
                #  Storm's body, everything below the chin
                "Storm_BJ_Backdrop"
                subpixel True
                offset (0,-40)     #top
                block:
                    ease 1 yoffset 15           #bottom
                    ease 1.5 offset (0,-40)     #top
                    repeat #(-20,270)
        contains:
                # Storm's head Underlay
                "Storm_BJ_Head"
                subpixel True
                offset (350,190)     #top (0,-40), -20 is crown, 0 is mid
                block:
                    ease 1 yoffset 270#250#40           #bottom
                    ease 1.5 yoffset 190#170 #(0,-40)     #top
                    repeat   #-270,-160
        contains:
                # Cock
                "Blowcock"
                subpixel True
                anchor (.5,.5)
                rotate 0
                alpha 1
                offset (650,370)
        contains:
                # Masked overlay for heading animaton
                AlphaMask("Storm_BJ_Head", "Storm_BJ_MaskHeadingComposite") #"Storm_BJ_MouthHeadingComposite")
                subpixel True
#                alpha .9
                offset (-250,-460)  #top (0,-40), -20 is crown, 0 is mid
                block:
                    ease 1 yoffset -380#-400           #bottom
                    ease 1.5 yoffset -460#-480     #top
                    repeat   #-270,-160
#        contains:
#                # the over part of spunk
#                ConditionSwitch(
#                        # the over part of spunk
#                        "'mouth' in StormX.Spunk", AlphaMask("Storm_BJ_Head", "StormHeadingSpunk"), #"StormHeadingSpunk",
#                        "True", Null(),
#                        )
#                subpixel True
#                offset (-250,-460)  #top (0,-40), -20 is crown, 0 is mid
#                block:
#                    ease 1 yoffset -380#-400           #bottom
#                    ease 1.5 yoffset -460#-480     #top
#                    repeat   #-270,-160
#end Storm_BJ_Anim2 Heading



image Storm_BJ_Anim3:
        #Sucking animation
        contains:
                # Storm's hair backside
                "Storm_BJ_HairBack"
                subpixel True
                offset (350,260)
                block:
                    ease 1 yoffset 330 #120
                    ease 1.5 yoffset 260 #0
                    repeat     #-270,-160
        contains:
                #  Storm's body, everything below the chin
                "Storm_BJ_Backdrop"
                subpixel True
                offset (0,50)
                block:
                    ease 1 yoffset 100 #100      #bottom
                    ease 1.5 yoffset 50 #50 #top
                    repeat #(-20,270)
        contains:
                # Storm's head Underlay
                "Storm_BJ_Head"
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
                offset (650,370)
        contains:
                # Masked overlay for sucking animaton
                AlphaMask("Storm_BJ_Head", "Storm_BJ_MouthSuckingMask")
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
                        "'mouth' in StormX.Spunk and Player.Male", "StormSuckingSpunk",
                        "True", Null(),
                        )
                subpixel True
                offset (350,260)
                block:
                    ease 1 yoffset 330 #120
                    ease 1.5 yoffset 260 #0
                    repeat     #-270,-160
#end Storm_BJ_Anim3 Sucking

image Storm_BJ_Anim4:
        #Deep animation
        contains:
                # Storm's hair backside
                "Storm_BJ_HairBack"
                subpixel True
                #offset (350,260)
                offset (350,360)#(0,100)
                block:
                    subpixel True
                    ease 1 yoffset 560#300
                    pause .5
                    ease 2 yoffset 360#100
                    repeat   #-270,-160
        contains:
                #  Storm's body, everything below the chin
                "Storm_BJ_Backdrop"
                subpixel True
                offset (0,100)
                block:
                    subpixel True
                    ease 1.2 yoffset 250
                    pause .5
                    ease 1.8 yoffset 100
                    repeat    #(-20,270)
        contains:
                # Storm's head Underlay
                "Storm_BJ_Head"
                subpixel True
                offset (350,360)
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
                offset (650,370)
        contains:
                # Masked overlay for sucking animaton
                AlphaMask("Storm_BJ_Head", "Storm_BJ_MouthSuckingMask")
                subpixel True
                offset (-250,-290)
                block:
                    subpixel True
                    ease 1 yoffset -90
                    pause .5
                    ease 2 yoffset -290
                    repeat   #-270,-160
#                offset (0,100)
#                block:
#                    subpixel True
#                    ease 1 yoffset 300
#                    pause .5
#                    ease 2 yoffset 100
#                    repeat   #-270,-160
        contains:
                # the over part of spunk
                ConditionSwitch(
                        # the over part of spunk
                        "'mouth' in StormX.Spunk and Player.Male", "StormSuckingSpunk",
                        "True", Null(),
                        )
                subpixel True
                offset (350,360)
                block:
                    subpixel True
                    ease 1 yoffset 560#300
                    pause .5
                    ease 2 yoffset 360#100
                    repeat   #-270,-160
#end Storm_BJ_Anim4 Deep


image Storm_BJ_Anim5:
        #Cum high animation
        contains:
                # Storm's hair backside
                "Storm_BJ_HairBack"
                subpixel True
                offset (350,200)     #top
                block:
                    ease 1 yoffset 210           #bottom
                    ease 1.5 yoffset 200     #top
                    repeat  #-270,-160
        contains:
                #  Storm's body, everything below the chin
                "Storm_BJ_Backdrop"
                subpixel True
                offset (0,-30)     #top
                block:
                    ease 1 yoffset -20           #bottom
                    ease 1.5 yoffset -30     #top
                    repeat     #(-20,270)
        contains:
                # Storm's head Underlay
                "Storm_BJ_Head"
                subpixel True
                #offset (350,210)
                offset (350,200)     #top
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
                offset (650,370)
        contains:
                # Masked overlay for sucking animaton
                AlphaMask("Storm_BJ_Head", "Storm_BJ_MaskHeadingComposite")
                subpixel True
                offset (-250,-450)     #top
                block:
                    ease 1 yoffset -440           #bottom
                    ease 1.5 yoffset -450     #top
                    repeat  #-270,-160
#                offset (0,-30)     #top
#                block:
#                    ease 1 yoffset -20           #bottom
#                    ease 1.5 offset (0,-30)     #top
#                    repeat  #-270,-160
#end Storm_BJ_Anim5 Cum high
#end Storm_BJ_Anim5 Cum high


image Storm_BJ_Anim6:
        #Cum Deep animation
        contains:
                # Storm's hair backside
                "Storm_BJ_HairBack"
                subpixel True
                offset (350,440)#230)
                block:
                    subpixel True
                    ease 1 yoffset 460
                    pause .5
                    ease 2 yoffset 440
                    repeat       #-270,-160
        contains:
                #  Storm's body, everything below the chin
                "Storm_BJ_Backdrop"
                subpixel True
                offset (0,190)
                block:
                    subpixel True
                    ease 1.2 yoffset 200
                    pause .5
                    ease 1.8 yoffset 190
                    repeat      #(-20,270)
        contains:
                # Storm's head Underlay
                "Storm_BJ_Head"
                subpixel True
                #offset (350,210)
                offset (350,440)#230)
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
                offset (650,370)
        contains:
                # Masked overlay for sucking animaton
                AlphaMask("Storm_BJ_Head", "Storm_BJ_MouthSuckingMask")
                subpixel True
                offset (-250,-210)#230)
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
                        "'mouth' in StormX.Spunk and Player.Male", "StormSuckingSpunk",
                        "True", Null(),
                        )
                subpixel True
                offset (350,440)#230)
                block:
                    subpixel True
                    ease 1 yoffset 460
                    pause .5
                    ease 2 yoffset 440
                    repeat       #-270,-160
#end Storm_BJ_Anim6 Cum Deep

#Head and Body Animations for Storm's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
                                                               #BJ Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Storm_BJ_Launch(Line = Trigger):    # The sequence to launch the Storm BJ animations
    if renpy.showing("Storm_BJ_Animation") and StormX.Pose != "69":
        return
    elif renpy.showing("Storm_69_Animation") and StormX.Pose == "69":
        return

    if not Player.Male:
        call Storm_CUN_Launch
        return

    if renpy.showing("Storm_TJ_Animation"):
            hide Storm_TJ_Animation
    else:
            call Girl_Hide(StormX)
            if Line == "L" or Line == "cum":
                show Storm_Sprite at SpriteLoc(StageCenter) zorder 150:
                    alpha 1
                    ease 1 zoom 2.5 offset (150,80)
                with dissolve
            else:
                show Storm_Sprite at SpriteLoc(StageCenter) zorder 150:
                    alpha 1 zoom 2.5 offset (150,80)
                with dissolve
            hide Storm_Sprite
    #". . ."
    $ Speed = 0

    if Line != "cum":
        $ Trigger = "blow"

    if StormX.Pose == "69":
            show Storm_69_Animation zorder 150
    else:
            show Storm_BJ_Animation zorder 150:
                pos (630,650) #(645,510)
    if Taboo and Line == "L": # Storm gets started. . .
            if len(Present) >= 2:
                if Present[0] != StormX:
                        "[StormX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                elif Present[1] != StormX:
                        "[StormX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
            else:
                        "[StormX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
            "Затем она наклоняется и берет ваш член в свой рот."
    elif Line == "L":
            "[StormX.Name] плавно наклоняется и прислоняет ваш член к своей щеке."

    return

label Storm_BJ_Reset: # The sequence to the Storm animations from BJ to default
    if Player.Male != 1:
            call Storm_CUN_Reset
    if not renpy.showing("Storm_BJ_Animation") and not renpy.showing("Storm_69_Animation"):
        return
#    hide Storm_BJ_Animation
    call Girl_Hide(StormX)
    $ Speed = 0

    show Storm_Sprite at SpriteLoc(StageCenter) zorder 150:
        alpha 1 zoom 2.5 offset (150,80)
    with dissolve

    show Storm_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .2
        ease .3 zoom 1 offset (0,0)
    pause 1.5
    show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) zorder StormX.Layer:
        alpha 1 zoom 1 offset (0,0)
    return

# End Storm Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Storm's TJ animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Animation components / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# start base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_TJ_Animation:
            #core TJ animation
            contains:
                ConditionSwitch(
                    # Storm's upper body
                    "not Player.Sprite","Storm_TJ_0",#Static
                    "Speed == 1", "Storm_TJ_1",#slow
                    "Speed == 3", "Storm_TJ_3",#cumming low
                    "Speed == 4", "Storm_TJ_4",#cumming high
                    "Speed == 5", "Storm_TJ_5",#cumming low
                    "Speed >= 2", "Storm_TJ_2",#fast
                    "True",       "Storm_TJ_0",#Static
                    )
            zoom .8 #.7
            transform_anchor True
            anchor (.5,.5)
# end base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



image Storm_TJ_HairBack:
            #Hair underlay
            "Storm_BJ_HairBack"
            transform_anchor True
            zoom .7
            anchor (0.5, 0.5)
            offset (30,-450)#(320,100)
            rotate 0

image Storm_TJ_Head:
            #Hair underlay
            "Storm_BJ_Head"
            transform_anchor True
            zoom .7
            anchor (0.5, 0.5)
            offset (30,-450)
            rotate 0

image Storm_TJ_HairTop:
            #Hair overlay
            contains:
                ConditionSwitch(
                        "StormX.Hair == 'short'", Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_Short_Over.png"),
                        "(StormX.Hair == 'mohawk' and StormX.Water) or StormX.Hair == 'wethawk'", Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_WetM_Over.png"),
                        "StormX.Hair == 'mohawk' and not Player.Male and 'facial' in StormX.Spunk",Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_WetM_Over.png"),
                        "StormX.Water or StormX.Hair == 'wet'", Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_WetL_Over.png"),
                        "not Player.Male and 'facial' in StormX.Spunk",Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_WetL_Over.png"),
                        "StormX.Hair == 'mohawk'", Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_Mohawk_Over.png"),
                        "True", Recolor("Storm", "Hair", "images/StormBJFace/Storm_BJ_Hair_Long_Over.png"),
                        )
                offset (83,-80)
            contains:
                ConditionSwitch(
                        #cum on the hair
                        "'hair' in StormX.Spunk and (StormX.Water or StormX.Hair == 'wethawk' or StormX.Hair == 'wet') and Player.Male", "images/StormBJFace/Storm_BJ_Spunk_HairW.png",
                        "'hair' in StormX.Spunk and StormX.Hair == 'mohawk' and Player.Male", "images/StormBJFace/Storm_BJ_Spunk_HairM.png",
                        "'hair' in StormX.Spunk and Player.Male", "images/StormBJFace/Storm_BJ_Spunk_HairL.png",
                        "True", Null(),
                        )
                offset (83,-80)
#            zoom 1.4
#            anchor (0.5, 0.5)

            #"Storm_BJ_HairBack"
            transform_anchor True
            zoom .98
            anchor (0.5, 0.5)
            offset (30,-450)
            rotate 0

image Storm_TJ_ZeroCock:
            #cock used in laura's sex pose
            "Zero_Blowcock"
            transform_anchor True
            zoom .6
            anchor (0.5, 0.5)
            offset (30,50)#(70,50)
            rotate 0

image Storm_TJ_Body:
            #bra underlayer for non-TJ poses
            contains:
                ConditionSwitch(
                        "StormX.Over or renpy.showing('Storm_TJ_Animation')", Null(),
                        "StormX.Chest == 'black bra' or StormX.Chest == 'lace bra'",Recolor("Storm", "Chest", "images/StormBJFace/Storm_TJ_Chest_Bra_Back.png"),
                        "True", Null(),
                        )
            contains:
                "images/StormBJFace/Storm_TJ_Body.png"
            contains:
                ConditionSwitch(
                        "not StormX.Water",Null(),
                        "True",       "images/StormBJFace/Storm_TJ_Body_Wet.png",
                        )
            contains:
                #arm rings base
                ConditionSwitch(
                        "not StormX.Acc == 'rings' or StormX.Over == 'jacket'", Null(),
                        "True", "images/StormBJFace/Storm_TJ_Arms_Ring.png",
                        )
            contains:
                #Chest
                ConditionSwitch(
                        #"StormX.Chest == 'bra'","images/StormBJFace/Storm_TJ_Chest_Bra_Base.png",
                        "StormX.Chest == 'cos bra'",Recolor("Storm", "Chest", "images/StormBJFace/Storm_TJ_Chest_Cos_TopD.png"),
                        "StormX.Chest == 'sports bra'",Recolor("Storm", "Chest", "images/StormBJFace/Storm_TJ_Chest_Sportsbra_Body.png"),
                        "StormX.Chest == 'bikini top'",Recolor("Storm", "Chest", "images/StormBJFace/Storm_TJ_Chest_Bikini_Body.png"),
                        "True", Null(),
                        )
            contains:
                #Over
                ConditionSwitch(
                        "StormX.Over == 'white shirt'",Recolor("Storm", "Over", "images/StormBJFace/Storm_TJ_Over_WhiteShirt_Body.png"),
                        "StormX.Over == 'jacket'",Recolor("Storm", "Over", "images/StormBJFace/Storm_TJ_Over_Jacket_Body.png"),
                        "True", Null(),
                        )
            contains:
                #tit spunk on chest
                ConditionSwitch(
                        "'tits' in StormX.Spunk and Player.Male", "images/StormBJFace/Storm_TJ_Spunk_Body.png",
                        "True", Null(),
                        )
            contains:
                # ring necklace
                ConditionSwitch(
                        "StormX.Neck == 'rings'", "images/StormBJFace/Storm_TJ_Neck_Ring.png",
                        "True", Null(),
                        )
            contains:
                #hair at the midground, behind the face but in front of body
                ConditionSwitch(
                        "StormX.Over", Null(),
                        "StormX.Hair == 'long' and not StormX.Water and not (not Player.Male and 'facial' in StormX.Spunk)", "images/StormBJFace/Storm_TJ_Hair_Long_Mid.png",
                        "True",   Null(),
                        )
            transform_anchor True
            zoom 1
            anchor (0.4, 1.0)
            #offset (410,770) # (300,275)
            rotate 0


image Storm_TJ_Tit_Under:
            #body underlay
            contains:

                ConditionSwitch(
                    # right breast overlay
                    "StormX.Chest == 'cos bra'",Null(),
                    "renpy.showing('Storm_TJ_Animation')", "images/StormBJFace/Storm_TJ_TitsUnder.png",
                    "True",  Null(),
                    )
#            contains:
#                ConditionSwitch(
#                        "'tits' not in StormX.Spunk",Null(),
#                        "True",       "images/StormBJFace/Storm_TJ_Spunk_TitsUnder.png",
#                        )
            transform_anchor True
            zoom 1
            anchor (0.4, 1.0)
            #offset (410,770) # (300,275)
            rotate 0

image Storm_TJ_Braback:
            #back fo the bra straps
            contains:
                ConditionSwitch(
                        #"StormX.Chest == 'corset' and not StormX.Uptop","images/StormBJFace/Storm_TJ_Chest_Corset.png",
                        "StormX.Over",Null(),
                        "StormX.Chest == 'black bra' or StormX.Chest == 'lace bra'",Recolor("Storm", "Chest", "images/StormBJFace/Storm_TJ_Chest_Bra_Back.png"),
                        "True", Null(),
                        )
            transform_anchor True
            zoom 1
            anchor (0.4, 1.0)
            #offset (410,770) # (300,275)
            rotate 0

image Storm_TJ_BraStretch:
            #bra streching effect
            contains:
                ConditionSwitch(
                        #"StormX.Chest == 'corset' and not StormX.Uptop","images/StormBJFace/Storm_TJ_Chest_Corset.png",
                        "StormX.Chest == 'bikini top'",Recolor("Storm", "Chest", "images/StormBJFace/Storm_TJ_Chest_Bikini_Tent.png"),
                        "StormX.Chest == 'sports bra'",Recolor("Storm", "Chest", "images/StormBJFace/Storm_TJ_Chest_Sportsbra_Tent.png"),
                        "True", Null(),
                        )
            transform_anchor True
            zoom 1
            offset (50,0) # (300,275)
            anchor (.1,.1)#(0.1, .2)
            rotate 0
            #alpha 0.9

image Storm_TJ_Tits:
            #layer with left tit and all clothing
            contains:
                "images/StormBJFace/Storm_TJ_Tits.png"
            contains:
                #Piercings
                ConditionSwitch(
                        "StormX.Pierce == 'barbell'","images/StormBJFace/Storm_TJ_Pierce_Barbell.png",
                        "StormX.Over == 'white shirt' and not StormX.Uptop",Null(),
                        "StormX.Chest and not StormX.Uptop",Null(),
                        "StormX.Pierce == 'ring'","images/StormBJFace/Storm_TJ_Pierce_Ring.png",
                        "True", Null(),
                        )
            contains:
                ConditionSwitch(
                        "not StormX.Water",Null(),
                        "True",       "images/StormBJFace/Storm_TJ_Tits_Wet.png",
                        )
            contains:
                ConditionSwitch(
                        "'tits' not in StormX.Spunk and Player.Male",Null(),
                        "True",       "images/StormBJFace/Storm_TJ_Spunk_Tits.png",
                        )
            contains:
                #Over
                ConditionSwitch(
                        "StormX.Over == 'jacket'",Recolor("Storm", "Over", "images/StormBJFace/Storm_TJ_Over_Jacket_Top.png"),
#                        "StormX.Over == 'towel' and not renpy.showing('Storm_TJ_Animation')", "images/StormBJFace/Storm_TJ_Over_Towel.png",
                        "True", Null(),
                        )
            contains:
                #Chest
                ConditionSwitch(
                        "StormX.Chest == 'black bra' and StormX.Uptop and StormX.Over",Recolor("Storm", "Chest", "images/StormBJFace/Storm_TJ_Chest_Bra_TopUS.png"),  #fix, add "no straps" version here
                        "StormX.Chest == 'black bra' and StormX.Uptop",Recolor("Storm", "Chest", "images/StormBJFace/Storm_TJ_Chest_Bra_TopU.png"),
                        "StormX.Chest == 'lace bra' and StormX.Uptop and StormX.Over",Recolor("Storm", "Chest", "images/StormBJFace/Storm_TJ_Chest_Bra_TopUS.png"),    #fix, add "no straps" version here
                        "StormX.Chest == 'lace bra' and StormX.Uptop",Recolor("Storm", "Chest", "images/StormBJFace/Storm_TJ_Chest_Bra_TopU.png"),
                        "StormX.Chest == 'sports bra' and StormX.Uptop","images/StormBJFace/Storm_TJ_Chest_SportsBra_TopU.png",
                        "StormX.Chest == 'bikini top' and StormX.Uptop",Recolor("Storm", "Chest", "images/StormBJFace/Storm_TJ_Chest_Bikini_TopU.png"),

                        "StormX.Chest == 'tube top' and not StormX.Uptop",Recolor("Storm", "Chest", "images/StormBJFace/Storm_TJ_Chest_TubeD.png"),
                        "StormX.Chest == 'black bra' and StormX.Over",Recolor("Storm", "Chest", "images/StormBJFace/Storm_TJ_Chest_Bra_TopDS.png"),  #fix, add "no straps" version here
                        "StormX.Chest == 'black bra'",Recolor("Storm", "Chest", "images/StormBJFace/Storm_TJ_Chest_Bra_TopD.png"),
                        "StormX.Chest == 'lace bra' and StormX.Over",Recolor("Storm", "Chest", "images/StormBJFace/Storm_TJ_Chest_Lacebra_TopDS.png"),  #fix, add "no straps" version here
                        "StormX.Chest == 'lace bra'",Recolor("Storm", "Chest", "images/StormBJFace/Storm_TJ_Chest_Lacebra_TopD.png"),
                        "StormX.Chest == 'sports bra'",Recolor("Storm", "Chest", "images/StormBJFace/Storm_TJ_Chest_Sportsbra_TopD.png"),
                        "StormX.Chest == 'bikini top'",Recolor("Storm", "Chest", "images/StormBJFace/Storm_TJ_Chest_Bikini_TopD.png"),
                        "True", Null(),
                        )
            contains:
                #Over
                ConditionSwitch(
                        "StormX.Over == 'white shirt' and StormX.Uptop",Recolor("Storm", "Over", "images/StormBJFace/Storm_TJ_Over_WhiteShirt_TopU.png"),
                        "StormX.Over == 'white shirt'",Recolor("Storm", "Over", "images/StormBJFace/Storm_TJ_Over_WhiteShirt_TopD.png"),
#                        "StormX.Over == 'towel' and not renpy.showing('Storm_TJ_Animation')", "images/StormBJFace/Storm_TJ_Over_Towel.png",
                        "True", Null(),
                        )
            contains:
                #arm rings base
                ConditionSwitch(
                        "not StormX.Acc == 'rings' or StormX.Over == 'jacket'", Null(),
                        "True", "images/StormBJFace/Storm_TJ_Wrists_Ring.png",
                        )
            contains:
                #Piercings clothing
                ConditionSwitch(
                        "StormX.Uptop", Null(),
                        "(not StormX.Over) and (not StormX.Chest)", Null(),
                        "StormX.Pierce == 'ring' and StormX.Over == 'white shirt'","images/StormBJFace/Storm_TJ_Pierce_Ring_Shirt.png",
                        "StormX.Pierce == 'barbell' and StormX.Over == 'white shirt'","images/StormBJFace/Storm_TJ_Pierce_Barbell_Shirt.png",
                        "StormX.Chest == 'cos bra'",Null(),
                        "StormX.Pierce == 'ring' and StormX.Chest == 'lace bra'","images/StormBJFace/Storm_TJ_Pierce_Ring_Lace.png",
                        "StormX.Pierce == 'barbell' and StormX.Chest == 'lace bra'","images/StormBJFace/Storm_TJ_Pierce_Barbell_Lace.png",
                        "StormX.Pierce == 'ring' and StormX.Chest == 'tube top'","images/StormBJFace/Storm_TJ_Pierce_Ring_Tube.png",
                        "StormX.Pierce == 'barbell' and StormX.Chest == 'tube top'","images/StormBJFace/Storm_TJ_Pierce_Barbell_Tube.png",
                        "StormX.Pierce == 'ring' and StormX.Chest","images/StormBJFace/Storm_TJ_Pierce_Ring_Bra.png",
                        "StormX.Pierce == 'barbell' and StormX.Chest","images/StormBJFace/Storm_TJ_Pierce_Barbell_Bra.png",
                        "True", Null(),
                        )
            contains:
                #Piercings over rings
                ConditionSwitch(
                        "not StormX.Acc == 'rings' or not StormX.Pierce == 'ring'", Null(),
                        "StormX.Over == 'white shirt' and not StormX.Uptop", Null(),
                        "StormX.Chest and StormX.Chest != 'cos bra' and not StormX.Uptop",Null(),
                        "True","images/StormBJFace/Storm_TJ_Pierce_Ring.png",
#                        "StormX.Chest == 'cos bra'",Null(),
#                        "StormX.Pierce == 'ring' and StormX.Chest == 'lace bra'","images/StormBJFace/Storm_TJ_Pierce_Ring_Lace.png",
#                        "StormX.Pierce == 'barbell' and StormX.Chest == 'lace bra'","images/StormBJFace/Storm_TJ_Pierce_Barbell_Lace.png",
#                        "StormX.Pierce == 'ring' and StormX.Chest == 'tube top'","images/StormBJFace/Storm_TJ_Pierce_Ring_Tube.png",
#                        "StormX.Pierce == 'barbell' and StormX.Chest == 'tube top'","images/StormBJFace/Storm_TJ_Pierce_Barbell_Tube.png",
#                        "StormX.Pierce == 'ring' and StormX.Chest","images/StormBJFace/Storm_TJ_Pierce_Ring_Bra.png",
#                        "StormX.Pierce == 'barbell' and StormX.Chest","images/StormBJFace/Storm_TJ_Pierce_Barbell_Bra.png",
#                        "True", Null(),
                        )
            transform_anchor True
            zoom 1
            anchor (0.4, 1.0)
            #offset (410,770) # (300,275)
            rotate 0


# Animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start 0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Storm_TJ_0:
        #Her Body in the TJ pose, static
        contains:
                #bra strap backing
                "Storm_TJ_Braback"
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
                #hairbelow the body
                "Storm_TJ_HairBack"
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
                #base body test / / / / / / / / / / / / / / / / / / / /
                "Storm_TJ_Body"
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
                "Storm_TJ_Head"
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
                "Storm_TJ_Tit_Under"
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
                "Storm_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                rotate -5
                parallel:
                    ease 2 rotate -3#3
                    pause .1
                    ease 2 rotate -5#-2
                    pause .1
                    repeat
        contains:
                contains:
                    "Storm_TJ_BraStretch"
                subpixel True
                pos (-70,-210) #top (0,-10)
                transform_anchor True
                xzoom .75
                yzoom .85
                parallel:
                    ease 2 yzoom .5
                    pause .1
                    ease 2 yzoom .85
                    pause .1
                    repeat
                parallel:
                    ease 2 pos (-60,-230)#-30,-160
                    pause .1
                    ease 2 pos (-70,-210)#-70,-140
                    pause .1
                    repeat
        contains:
                contains:
                    "Storm_TJ_Tits"
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
                #hairback
                "Storm_TJ_HairTop"
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

# End Storm TJ Pose 0 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start 1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Storm_TJ_1:
        #Her Body in the TJ pose, slow
        contains:
                #bra strap backing
                "Storm_TJ_Braback"
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
                #hairbelow the body
                "Storm_TJ_HairBack"
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
                    ease 2 rotate 0
                    pause .2
                    ease 2 rotate -5
                    pause .5
                    repeat
        contains:
                #base body test / / / / / / / / / / / / / / / / / / / /
                "Storm_TJ_Body"
                subpixel True
                pos (0,60) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -40#0
                    pause .2
                    ease 2 ypos 60#150
                    pause .5
                    repeat
        contains:
                #head
                "Storm_TJ_Head"
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
                    ease 2 rotate 0
                    pause .2
                    ease 2 rotate -5
                    pause .5
                    repeat
        contains:
                #right hand backside
                "Storm_TJ_Tit_Under"
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
                "Storm_TJ_ZeroCock"
                pos (0,25) #top (0,-10)
                transform_anchor True
                rotate -6
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
        contains:
                contains:
                    "Storm_TJ_BraStretch"
                subpixel True
                pos (-100,-150) #top (0,-10)
                transform_anchor True
                xzoom .9
                yzoom 1.3
                parallel:
                    pause .1
                    ease 1.6 yzoom .3#-20
                    pause .9
                    ease 1.6 yzoom 1.5#150
                    ease .5 yzoom 1.3#140
                    repeat
                parallel:
                    pause .1
                    ease 1.9 xzoom .6#-20
                    pause .4
                    ease 1.8 xzoom .9#150
                    pause .5
#                    ease .5 xzoom .8#140
                    repeat
                parallel:
                    pause .1
                    ease 1.9 pos (-50,-260)#-160 bottom
                    pause .4
                    ease 1.8 pos (-100,-140)#-90,-65
                    ease .5 pos (-100,-150)#-80,-80
                    repeat
        contains:
                contains:
                    "Storm_TJ_Tits"
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
        contains:
                #hairback
                "Storm_TJ_HairTop"
                subpixel True
                pos (0,60) #top (0,-10)
                transform_anchor True
                rotate -5
                parallel:
                    ease 2 ypos -40#0
                    pause .2
                    ease 2 ypos 60#150
                    pause .5
                    repeat
                parallel:
                    ease 2 rotate 0
                    pause .2
                    ease 2 rotate -5
                    pause .5
                    repeat

# End Storm TJ Pose 1 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Start 2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Storm_TJ_2:
        #Her Body in the TJ pose, fast
        contains:
                #bra strap backing
                "Storm_TJ_Braback"
                subpixel True
                pos (0,80) #top (0,-10)
                transform_anchor True
                block:
                    ease .3 ypos 40
                    ease .7 ypos -40
                    pause .2
                    ease .4 ypos 80
                    repeat
        contains:
                #hairbelow the body
                "Storm_TJ_HairBack"
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
                #base body test / / / / / / / / / / / / / / / / / / / /
                "Storm_TJ_Body"
                subpixel True
                pos (0,80) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 1 ypos -20
                    pause .1
                    ease .5 ypos 80
                    repeat
        contains:
                #head
                "Storm_TJ_Head"
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
                "Storm_TJ_Tit_Under"
                subpixel True
                pos (0,80) #top (0,-10)
                transform_anchor True
                block:
                    ease .3 ypos 40
                    ease .7 ypos -40
                    pause .2
                    ease .4 ypos 80
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Storm_TJ_ZeroCock"
                pos (0,30) #top (0,-10)
                transform_anchor True
                rotate -4
                parallel:
                    ease 1 ypos 0
                    pause .2
                    ease .4 ypos 30
                    repeat
                parallel:
                    ease 1 rotate -2
                    pause .1
                    ease .5 rotate -4
                    repeat
        contains:
                contains:
                    "Storm_TJ_BraStretch"
                subpixel True
                pos (-100,-120) #top (0,-10)
                transform_anchor True
                yzoom 1.7
                xzoom 1
                parallel:
                    ease .3 yzoom 1.3#-60 bottom
                    ease .7 yzoom .3#-60 bottom
                    pause .2
                    ease .4 yzoom 1.7#60
                    repeat
                parallel:
                    ease .3 pos (-100,-160)#-80 bottom
                    ease .7 pos (-80,-240)#-160 bottom
                    pause .2
                    ease .4 pos (-100,-120)#-40
                    repeat
        contains:
                contains:
                    "Storm_TJ_Tits"
                subpixel True
                pos (0,80) #top (0,-10)
                transform_anchor True
                block:
                    ease .3 ypos 40
                    ease .7 ypos -40
                    pause .2
                    ease .4 ypos 80
                    repeat

        contains:
                #hairback
                "Storm_TJ_HairTop"
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

# End Storm TJ Pose 2 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start 3 (licking) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Storm_TJ_3:
        #Her Body in the TJ pose, licking
        contains:
                #bra strap backing
                "Storm_TJ_Braback"
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
                #hairbelow the body
                "Storm_TJ_HairBack"
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
                #base body test / / / / / / / / / / / / / / / / / / / /
                "Storm_TJ_Body"
                subpixel True
                pos (0,130) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 1 ypos 100
                    pause .1
                    ease .5 ypos 130
                    repeat
        contains:
                #head
                "Storm_TJ_Head"
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
                "Storm_TJ_Tit_Under"
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
                "Storm_TJ_ZeroCock"
                pos (0,30) #top (0,-10)
                transform_anchor True
                rotate -4
                parallel:
                    ease 1 ypos 0
                    pause .2
                    ease .4 ypos 30
                    repeat
                parallel:
                    ease 1 rotate -2
                    pause .1
                    ease .5 rotate -4
                    repeat
        contains:
                contains:
                    "Storm_TJ_BraStretch"
                subpixel True
                pos (-100,-105) #top (0,-10)
                transform_anchor True
                yzoom 2
                xzoom 1
                parallel:
                    ease .3 yzoom 1.95#1.3 bottom
                    ease .7 yzoom 1.7#.3 bottom
                    pause .2
                    ease .4 yzoom 2#1.7
                    repeat
                parallel:
                    ease .3 pos (-100,-115)#-160 bottom
                    ease .7 pos (-90,-155)#-240 bottom
                    pause .2
                    ease .4 pos (-100,-105)#-120
                    repeat

        contains:
                contains:
                    "Storm_TJ_Tits"
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
                #hairback
                "Storm_TJ_HairTop"
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

# End Storm TJ Pose 3 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start 4 (cumming high) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Storm_TJ_4:
        #Her Body in the TJ pose, cummming high
        contains:
                #bra strap backing
                "Storm_TJ_Braback"
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
                #hairbelow the body
                "Storm_TJ_HairBack"
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
                #base body test / / / / / / / / / / / / / / / / / / / /
                "Storm_TJ_Body"
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
                "Storm_TJ_Head"
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
                "Storm_TJ_Tit_Under"
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
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Storm_TJ_ZeroCock"
                pos (0,20) #top (0,-10)
                transform_anchor True
                rotate -5
                parallel:
                    ease 2 ypos 0
                    pause .1
                    ease 2 ypos 20
                    pause .1
                    repeat
        contains:
                contains:
                    "Storm_TJ_BraStretch"
                subpixel True
                pos (-70,-210) #top (0,-10)
                transform_anchor True
                xzoom .75
                yzoom .5
                parallel:
                    pause .2
                    ease 1.9 pos (-65,-230)#-30,-160
                    pause .2
                    ease 1.9 pos (-75,-210)#-70,-140
                    repeat
        contains:
                contains:
                    "Storm_TJ_Tits"
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
                #hairback
                "Storm_TJ_HairTop"
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
# End Storm TJ Pose 4 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start 5 (cumming low) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Storm_TJ_5:
        #Her Body in the TJ pose, cumming low
        contains:
                #bra strap backing
                "Storm_TJ_Braback"
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
                "Storm_TJ_HairBack"
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
                "Storm_TJ_Body"
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
                "Storm_TJ_Head"
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
                "Storm_TJ_Tit_Under"
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
                "Storm_TJ_ZeroCock"
                pos (0,25) #top (0,-10)
                transform_anchor True
                rotate -5#-10
        contains:
                contains:
                    "Storm_TJ_BraStretch"
                subpixel True
                pos (-100,-105) #top (0,-10)
                transform_anchor True
                xzoom 1
                yzoom 2
                parallel:
                    pause .1
                    ease 2 yzoom 1.8 #1.6
                    pause .2
                    ease 2 yzoom 2 #1.7
                    pause .4
                    repeat
                parallel:
                    pause .1
                    ease 2 pos (-100,-115)#-100,-135
                    pause .2
                    ease 2 pos (-100,-105)#-100,-125
                    pause .4
                    repeat
        contains:
                contains:
                    "Storm_TJ_Tits"
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
                #hairback
                "Storm_TJ_HairTop"
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

# End Storm TJ Pose 5 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Storm's TJ animations end / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Storm_TJ_Launch(Line = Trigger):    # The sequence to launch the Storm Titfuck animations
    if renpy.showing("Storm_TJ_Animation"):
        return

#    if Line == "L": # Storm gets started. . .
#            if Taboo:
#                if len(Present) >= 2:
#                    if Present[0] != StormX:
#                            "[StormX.Name] looks back at [Present[0].Name] to see if she's watching."
#                    elif Present[1] != StormX:
#                            "[StormX.Name] looks back at [Present[1].Name] to see if she's watching."
#                else:
#                            "[StormX.Name] casually glances around to see if anyone can see her."
#            "[StormX.Name] bends over and places your cock between her breasts."

#    if StormX.Chest and StormX.Over:
#        "She throws off her [StormX.Over] and her [StormX.Chest]."
#    elif StormX.Over:
#        "She throws off her [StormX.Over], baring her breasts underneath."
#    elif StormX.Chest:
#        "She tugs off her [StormX.Chest] and throws it aside."
#    $ StormX.Over = 0
#    $ StormX.Chest = 0
#    $ StormX.ArmPose = 0

#    call Girl_First_Topless(StormX)

    show blackscreen onlayer black with dissolve

    if renpy.showing("Storm_BJ_Animation"):
            hide Storm_BJ_Animation
    else:
            call Girl_Hide(StormX)
            show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) zorder 150:
                alpha 1
                ease 1 zoom 2.3 xpos 750 yoffset -100
            show Storm_Sprite:
                alpha 0

#    if StormX.Over == "towel" or StormX.Chest == "corset": #pulls top down because these tops are incompatible with TJ.
#        $ StormX.Uptop = 1

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "titjob"
    show Storm_TJ_Animation zorder 150:
        pos (1000,1050)#(1000,1000)#(700,520)
    $ Player.Sprite = 1
    hide blackscreen onlayer black with dissolve
    return

label Storm_TJ_Reset:
    # The sequence to the Storm animations from Titfuck to default
    if not renpy.showing("Storm_TJ_Animation"):
        return
#    hide Storm_TJ_Animation
    call Girl_Hide(StormX)
    $ Player.Sprite = 0

    show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) zorder 150:
        zoom 2.3 xpos 750 yoffset -100
    show Storm_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 xpos 700 yoffset 50
        pause .5
        ease .5 zoom 1 xpos StormX.SpriteLoc yoffset 0
    "[StormX.Name] отстраняется"
    show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) zorder StormX.Layer:
        alpha 1 zoom 1 offset (0,0) xpos StormX.SpriteLoc
    return

# End Storm TJ Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Storm Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Storm Handjob element //////////////////////////////////////////////////////////////////////

image Storm_HJ_Body:
    "Storm_Sprite"
    pos (-380,-1250)#680,-1250
    zoom 4.8#2.15


transform Storm_HJ_Body_1():
    subpixel True
#    pos (700,-1250)#(350,-550)
    block:
        ease .5 ypos -1220
        pause 0.25
        ease 1.0 ypos -1250
        pause 0.1
        repeat

transform Storm_HJ_Body_2():
    subpixel True
#    pos (350,-550)
    block:
        ease 0.2 ypos -1240
        pause 0.1
        ease 0.4 ypos -1250
        pause 0.1
        repeat

image Storm_Hand_Under:
    "images/StormSprite/handstorm2.png"
    anchor (0.5,0.5)
    pos (-10,0)
    offset (0,130)

image Storm_Hand_Over:
    "images/StormSprite/handstorm1.png"
    anchor (0.5,0.5)
    pos (-10,0)
    offset (0,130)

transform Storm_Hand_1():
    subpixel True
    pos (-20,-100)
    rotate 5
    block:
        ease .5 pos (0,150) rotate -5 #ypos 150 rotate 5 Bottom
        pause 0.25
        ease 1.0 pos (-20,-100) rotate 5 #250#-150 #rotate -10#  Top
        pause 0.1
        repeat

transform Storm_Hand_2():
    subpixel True
    pos (-15,-120)
    rotate 10
    block:
        ease 0.2 pos (-15,0) rotate 0
        pause 0.1
        ease 0.4 pos (-15,-120) rotate 10
        pause 0.1
        repeat

#transform Handcock_3():
#    subpixel True
#    rotate_pad False
#    ypos 400
#    rotate 0 #400
#    block:
#        ease .5 ypos 450 rotate -2 #450
#        pause 0.25
#        ease 1.0 ypos 400 rotate 0 #400
#        pause 0.1
#        repeat

#transform Handcock_4():
#    subpixel True
#    rotate_pad False
#    ypos 400
#    rotate 0
#    block:
#        ease .2 ypos 430 rotate -3 #410
#        ease .5 ypos 400 rotate 0
#        pause 0.1
#        repeat

transform Handcock_1J():
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

transform Handcock_2J():
    subpixel True
    rotate_pad False
    ypos 400
    rotate 0
    block:
        ease .2 ypos 430 rotate -3 #410
        ease .5 ypos 400 rotate 0
        pause 0.1
        repeat

image Storm_HJ_Animation:
    contains:
        ConditionSwitch(
            # backside of the hand
            "not Speed", Transform("Storm_HJ_Body"),
            "Speed == 1", At("Storm_HJ_Body", Storm_HJ_Body_1()),
            "Speed >= 2", At("Storm_HJ_Body", Storm_HJ_Body_2()),
            "Speed", Null(),
            )
    contains:
        ConditionSwitch(
            # backside of the hand
            "not Speed", Transform("Storm_Hand_Under"),
            "Speed == 1", At("Storm_Hand_Under", Storm_Hand_1()),
            "Speed >= 2", At("Storm_Hand_Under", Storm_Hand_2()),
            "Speed", Null(),
            )
    contains:
        ConditionSwitch(
            # cock
            "not Speed", Transform("Zero_Handcock"),
            "Speed == 1", At("Zero_Handcock", Handcock_1J()),
            "Speed >= 2", At("Zero_Handcock", Handcock_2J()),
            "Speed", Null(),
            )
        offset (0,0)
    contains:
        ConditionSwitch(
            # fingers of the hand
            "not Speed", Transform("Storm_Hand_Over"),
            "Speed == 1", At("Storm_Hand_Over", Storm_Hand_1()),
            "Speed >= 2", At("Storm_Hand_Over", Storm_Hand_2()),
            "Speed", Null(),
            )
    anchor (0.51, -1.3)
    zoom 0.4#0.6


label Storm_HJ_Launch(Line = Trigger):
    $ StormX.ArmPose = 1
    if renpy.showing("Storm_HJ_Animation"):
        $ Trigger = "hand"
        return
    if not Player.Male:
        call Storm_Finger_Launch
        return
    call Girl_Hide(StormX)
    if Line == "L":
        show Storm_Sprite at SpriteLoc(StageRight) zorder 150:
            alpha 1
            ease 1 zoom 1.7 offset (-150,350)#(-210,350)
    else:
        show Storm_Sprite at SpriteLoc(StageRight) zorder 150:
            alpha 1
            ease 1 zoom 1.7 offset (-150,350)#(-150,350)
        with dissolve

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    else:
        $ Speed = 1
    pause .5
    show Storm_Sprite at SpriteLoc(StageRight):
        alpha 0
#        ease .5 zoom 1.7 offset (-150,200)#(-150,200)
    show Storm_HJ_Animation at SpriteLoc(StageCenter) zorder 150 with fade:
        #xoffset 150
        offset (250,250)#(100,250)
    return

label Storm_HJ_Reset: # The sequence to the Storm animations from handjob to default
    if not renpy.showing("Storm_HJ_Animation"):
        return
    $ Speed = 0
    $ StormX.ArmPose = 2
    hide Storm_HJ_Animation with dissolve
    call Girl_Hide(StormX)
#    show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) zorder StormX.Layer:
#        alpha 1
#        zoom 1.7 offset (-150,200)
    show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
        pause.5
    show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) zorder StormX.Layer:
        alpha 1 zoom 1 offset (0,0)
    return

# End Storm Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# Core Storm CUN element ///////////////////////////////////////////////////////////////////////////                                     Core Storm CUN element
#Storm CUN Over Sprite Compositing

image Storm_CUN_Animation: #core CUN animation
    LiveComposite(
        (787,913),
        (0,0), ConditionSwitch(                                                                 # back of the hair, which needs to go behind the body
            "Speed == 0",  "Storm_CUN_Anim_Static",
            "Speed == 1",  "Storm_CUN_Anim_Licking1",
            "Speed == 2",  "Storm_CUN_Anim_Licking2",
            "Speed >= 3",  "Storm_CUN_Anim_Licking3",
#            "Speed == 4",  "Storm_CUN_Anim_Licking1",
            "True", "Storm_CUN_Anim_Static",
            ),
        )
    zoom .55
    anchor (.5,.5)

image Storm_CUN_Anim_Static:
    #Animation for licking speed 1
    contains:
        #hair
        "Storm_BJ_HairBack"#"BJ_HairBack"
        subpixel True
        offset (90,0)#(-10,0)
        rotate 30
        block:
            ease 2 yoffset 10
            ease 2 yoffset 0
            repeat
    contains:
        #body 2
        "Storm_BJ_Backdrop"
        pos (-440,-290)#(-330,-500)
        subpixel True
        offset (60,20)  #top(0,-35)
        block:
            ease 2 yoffset 30
            ease 2 yoffset 20
            repeat
    contains:
        #head
        "Storm_BJ_Head"#"BJ_Head"
        subpixel True
        offset (90,0)#(-10,0)
        rotate 30
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


image Storm_CUN_Anim_Licking1:
    #Animation for licking speed 1
    contains:
        #hair
        "Storm_BJ_HairBack"#"BJ_HairBack"
        offset (30,20)#490)
        rotate 10
        block: #5s total
            ease 2.5 offset (40,100) #bottom (0,75)
            easeout 1.5 offset (40,60)  #top (0,60)
            ease .5 offset (35,20)  #top
            ease .5 offset (37,30)  #top
            repeat
    contains:
        #body 2
        "Storm_BJ_Backdrop"#"Storm_Sprite"
#        zoom 1 #4.5
        pos (-440,-290)#(-330,-500)
        subpixel True
        offset (60,0)# -70,0
        block:
            ease 2.5 offset (60,75) #bottom (30,90)
            ease 2.3 offset (60,0)  #top
            pause .2
            repeat
    contains:
        #head
        "Storm_BJ_Head"#"BJ_Head"
        subpixel True
        offset (30,20)#490)
        rotate 10
        block: #5s total
            ease 2.5 offset (40,100) #bottom (0,75)
            easeout 1.5 offset (40,60)  #top (0,60)
            ease .5 offset (35,20)  #top
            ease .5 offset (37,30)  #top
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
#End Storm Licking 1

image Storm_CUN_Anim_Licking2:
    #Animation for licking speed 2
    contains:
        #hair
        "Storm_BJ_HairBack"#"BJ_HairBack"
        subpixel True
        offset (50,30)#490)
        rotate 10
        parallel: #2s total
            ease 1 offset (10,100) #bottom
            easeout .65 offset (20,70)  #top -35)
            linear .35 offset (50,30)  #top -35)
            pause .10
            repeat
        parallel: #2s total
            ease 1 rotate 0 #bottom
            easeout .65 rotate 5  #top -35)
            linear .35 rotate 10  #top -35)
            pause .10
            repeat
    contains:
        #body 2
        "Storm_BJ_Backdrop"
        pos (-440,-290)#(-330,-500)
        subpixel True
        offset (60,0)#490)
        block:
            ease .75 offset (60,50) #bottom (30,90)
            ease .95 offset (60,30)  #top
            pause .40
            repeat
    contains:
        #head
        "Storm_BJ_Head"#"BJ_Head"
        subpixel True
        offset (50,30)#490)
        rotate 10
        parallel: #2s total
            ease 1 offset (10,100) #bottom
            easeout .65 offset (20,70)  #top -35)
            linear .35 offset (50,30)  #top -35)
            pause .10
            repeat
        parallel: #2s total
            ease 1 rotate 0 #bottom
            easeout .65 rotate 5  #top -35)
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
#End Storm Licking 2

image Storm_CUN_Anim_Licking3:
    #Animation for licking speed 3
    contains:
        #hair
        "Storm_BJ_HairBack"#"BJ_HairBack"
        subpixel True
        offset (20,90)#490)
        block: #2s total
            ease .5 offset (20,110) #bottom
            ease .5 offset (20,90)  #top -35)
            repeat
    contains:
        #body 2
        "Storm_BJ_Backdrop"
        pos (-440,-290)#(-330,-500)
        subpixel True
        offset (60,90)#490)
        block:
            ease .4 offset (60,80) #bottom (30,90)
            ease .4 offset (60,90)  #top
            pause .2
            repeat
    contains:
        #head
        "Storm_BJ_Head"#"BJ_Head"
        subpixel True
        offset (20,90)#490)
        block: #2s total
            ease .5 offset (20,110) #bottom
            ease .5 offset (20,90)  #top -35)
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
#End Storm Licking 3

#CUN Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Storm_CUN_Launch(Line = Trigger):
    # The sequence to launch the Storm CUN animations
    if renpy.showing("Storm_CUN_Animation") and StormX.Pose != "69":
        return
    elif renpy.showing("Storm_69_CUN") and StormX.Pose == "69":
        return

    if Player.Male == 1:
        call Storm_BJ_Launch
        return

    call Girl_Hide(StormX)
    if Line == "L" or Line == "cum":
        show Storm_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1
            ease 1 zoom 2.5 offset (70,240) #(-90,140) offset (150,80)
        with dissolve
    else:
        show Storm_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1 zoom 2.5 offset (70,240) #(-90,140)
        with dissolve

    if Taboo and Line == "L":
            # Storm gets started. . .
            if len(Present) >= 2:
                if Present[0] != StormX:
                        "[StormX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                elif Present[1] != StormX:
                        "[StormX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
            else:
                        "[StormX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
    $ Speed = 1
    if Line == "L":
            if not StormX.Blow:
                "[StormX.Name] нерешительно стягивает с вас штаны и касается своим ртом вашей киски."
            else:
                "[StormX.Name] наклоняется и начинает лизать вашу киску."

    if Line != "cum":
        $ Trigger = "cun"

    show Storm_Sprite:
        alpha 0

    if StormX.Pose == "69":
            show Storm_69_CUN zorder 150
    else:
            show Storm_CUN_Animation zorder 150:
                pos (800,830)#(645,610)
    return

label Storm_CUN_Reset: # The sequence to the Storm animations from CUN to default
    if not renpy.showing("Storm_CUN_Animation") and not renpy.showing("Storm_69_CUN"):
        return
    hide Storm_CUN_Animation
    call Girl_Hide(StormX)
    $ Speed = 0

    show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) zorder 150:
        zoom 2 offset (70,140) alpha 1
        pause .5
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) zorder 150:
        alpha 1 zoom 1 offset (0,0)
    $ StormX.FaceChange("sexy")
    return

#End Storm Cunnilingus Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////



# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

image Storm_Finger_Animation:
    # Core Animation for Fingering Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
        ConditionSwitch(                                                # backside of the hand
            "Speed == 1", "Storm_Finger_1",
            "Speed >= 2", "Storm_Finger_2",
            "True", "Storm_Finger_0",
            ),
    anchor (0.5,0.5)#anchor (0.51, -1.3)
    offset (400,945)#700,1190
    zoom 0.8
    # end Core Animation for Fingering Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <

image Storm_Finger_0:
    # Animation for Fingering Zero's pussy, static < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Storm_Sprite"
            pos (260,-550)
            xzoom -2.15
            yzoom 2.15
    contains:
            ConditionSwitch(
                "Player.Wet", "StormBJFace/Storm_Fingering_Wet.png",
                "True", "StormBJFace/Storm_Fingering_Under.png",
                )
            anchor (0.5,0.6)
            pos (-20,40)
            rotate -15

#            "Storm_Finger_Under"
    contains:
            "Zero_Pussy"
    contains:
            "StormBJFace/Storm_Fingering_Over.png"
            anchor (0.5,0.6)
            pos (-20,40)
            rotate -15
#            "Storm_Finger_Over"
    # end Animation for Fingering Zero's pussy, static < < < < < < < < < < < < < < < < < < < < < < < <

image Storm_Finger_1:
    # Animation for Fingering Zero's pussy, slow < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Storm_Sprite"
            pos (260,-550)
            xzoom -2.15
            yzoom 2.15
            block:
                ease 0.5 ypos -540 #rotate 3   100
                pause 0.25
                ease 1.0 ypos -550 #rotate -3  40
                repeat
    contains:
            ConditionSwitch(
                "Player.Wet", "StormBJFace/Storm_Fingering_Wet.png",
                "True", "StormBJFace/Storm_Fingering_Under.png",
                )
            subpixel True
        #    xpos 10
            anchor (0.5,0.6)
            transform_anchor True
            pos (-10,40)
            rotate -15
            block:
                ease .5 pos (-20,85) rotate 0 #(-30,50)   Bottom
                pause 0.25
                ease 1.0 pos (-10,40) rotate -15 #((20,-60) Top                 pause 0.1
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
            "StormBJFace/Storm_Fingering_Over.png"
#            "Storm_Finger_Over"
            subpixel True
        #    xpos 10
            anchor (0.5,0.6)
            transform_anchor True
            pos (-10,40)
            rotate -15
            block:
                ease .5 pos (-20,85) rotate 0 #(-30,50)   Bottom
                pause 0.25
                ease 1.0 pos (-10,40) rotate -15 #((20,-60) Top                 pause 0.1
                repeat
    # end Animation for Fingering Zero's pussy, slow < < < < < < < < < < < < < < < < < < < < < < < <

image Storm_Finger_2:
    # Animation for Fingering Zero's pussy, fast < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Storm_Sprite"
            pos (260,-550)
            xzoom -2.15
            yzoom 2.15
            block:
                ease 0.15 ypos -540 #rotate 3   100
                pause 0.1
                ease 0.45 ypos -550 #rotate -3  40
                pause 0.1
                repeat
    contains:
            ConditionSwitch(
                "Player.Wet", "StormBJFace/Storm_Fingering_Wet.png",
                "True", "StormBJFace/Storm_Fingering_Under.png",
                )
            subpixel True
            anchor (0.5,0.6)
            transform_anchor True
#            rotate -15
            pos (-10,40)
            block:
                ease 0.15 ypos 115 #rotate 3   100
                pause 0.1
                ease 0.45 ypos 40 #rotate -3  40
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
            "StormBJFace/Storm_Fingering_Over.png"
#            "Storm_Finger_Over"
            anchor (0.5,0.6)
            subpixel True
            transform_anchor True
#            rotate -15
            pos (-10,40)
            block:
                ease 0.15 ypos 115 #rotate 3
                pause 0.1
                ease 0.45 ypos 40 #rotate -3 -50
                pause 0.1
                repeat
    # end Animation for Fingering Zero's pussy, fast < < < < < < < < < < < < < < < < < < < < < < < <

label Storm_Finger_Launch(Line = Trigger):
    if renpy.showing("Storm_Finger_Animation"):
        $ Trigger = "finger"
        return

    if Player.Male == 1:
        call Storm_HJ_Launch
        return

    call Girl_Hide(StormX)
    $ StormX.Arms = 0
    $ StormX.ArmPose = 1
    if not renpy.showing("Storm_Sprite"):
        show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) zorder 150:
            alpha 1 xzoom -1 zoom 1.7 xpos 745 yoffset 200#offset (825,250)
        with dissolve
    show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) zorder 150:
        alpha 1 xzoom -1
        ease 1 zoom 1.7 xpos 745 yoffset 200 #offset (825,250)

    if Taboo and Line == "L":
        # Storm gets started. . .
        if len(Present) >= 2:
            if Present[0] != StormX:
                    "[StormX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
            elif Present[1] != StormX:
                    "[StormX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
        else:
                    "[StormX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
        if not StormX.Hand and StormX.Arms:
            "Когда вы стягиваете свои штаны, [StormX.Name] снимает перчатки и нерешительно тянется к вашей киске. Затем она начинает грубо ласкать ее."
        else:
            "Затем она наклоняется и хватает ваш член."
    elif Line == "L":
        if not StormX.Hand and StormX.Arms:
            "Когда вы стягиваете свои штаны, [StormX.Name] снимает перчатки и нерешительно тянется к вашей киске. Затем она начинает грубо ласкать ее."
        else:
            "[StormX.Name] наклоняется и кладет руку вам на киску."
    else:
            "[StormX.Name] наклоняется и кладет руку вам на киску."

    show Storm_Sprite zorder StormX.Layer:
        alpha 0
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "finger"
    show Storm_Finger_Animation at SpriteLoc(StormX.SpriteLoc) zorder 150 with fade
    return

label Storm_Finger_Reset: # The sequence to the Storm animations from handjob to default
    if not renpy.showing("Storm_Finger_Animation"):
        return
    $ Speed = 0
    hide Storm_Finger_Animation
    with dissolve
    call Girl_Hide(StormX)
    show Storm_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 yoffset 50
        pause .5
        ease .5 zoom 1 xpos StormX.SpriteLoc yoffset 0
    show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) zorder StormX.Layer:
        alpha 1 zoom 1 xpos StormX.SpriteLoc yoffset 0
    $ StormX.ArmPose = 1
    return

# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


# Start Storm 69 Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

image Storm_69_Animation:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
                #Shows different upper body motion depending on events
#                "True", "Storm_69_Anim1",
                "Speed == 2", "Storm_69_Anim2",
                "Speed == 3", "Storm_69_Anim3",
                "Speed == 4", "Storm_69_Anim4",
                "Speed == 5", "Storm_69_Anim5",
                "Speed == 6", "Storm_69_Anim6",
                "Speed", "Storm_69_Anim1",
                "True", "Storm_69_Static",
                ),
        )
    align (0.6,0.0)
    pos (475,-700)#(475,-700)
    zoom 1.8#1/3

#Start Animations for Storm's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Storm 69 Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_69_Body:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Storm_SexSprite
        (1120,840),

        (0,0), ConditionSwitch(
            # base tits
            "not StormX.Uptop and StormX.Chest in ('black bra','lace bra','sports bra')", "images/StormSex/Storm_69_Tits_Up.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Base belly
            "True", "images/StormSex/Storm_69_Body.png",
            ),
#        (0,0), ConditionSwitch(
#            #Wet look
#            "StormX.Water", "images/StormSex/Storm_69_Water_Body.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #bra layer
            "StormX.Chest == 'tube top' and StormX.Uptop", "images/StormSex/Storm_69_Chest_Tube_Up.png",
            "StormX.Uptop", Null(),
            #if the top's down. . .
#            "StormX.Chest == 'cos bra'", "images/StormSex/Storm_69_Chest_Cos.png",
            "StormX.Chest == 'tube top'", "images/StormSex/Storm_69_Chest_Tube_Body.png",
            "StormX.Chest == 'black bra'", "images/StormSex/Storm_69_Chest_Bra.png",
            "StormX.Chest == 'lace bra'", "images/StormSex/Storm_69_Chest_Lace.png",
            "StormX.Chest == 'sports bra'", "images/StormSex/Storm_69_Chest_Sports.png",
            "StormX.Chest == 'bikini top' and StormX.Panties == 'bikini bottoms' and not StormX.PantiesDown", "images/StormSex/Storm_69_Chest_Bikini_Body.png",
            "StormX.Chest == 'bikini top'", "images/StormSex/Storm_69_Chest_Bikini_Loose.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #shirt layer
            "StormX.Uptop", Null(),
            "StormX.Over == 'white shirt' and StormX.Chest in ('black bra','lace bra','sports bra')", "images/StormSex/Storm_69_Over_Shirt_Bra.png",
            "StormX.Over == 'white shirt'", "images/StormSex/Storm_69_Over_Shirt_Body.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #the ring of her bikini over her shirt layer
            "StormX.Uptop", Null(),
            "StormX.Chest == 'bikini top' and (StormX.Panties != 'bikini bottoms' or StormX.PantiesDown)", "images/StormSex/Storm_69_Chest_Bikini_Ring.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #piercings, only shows when breasts are restrained
            "not StormX.Pierce or StormX.Uptop", Null(),
            "StormX.Pierce == 'ring'", ConditionSwitch(
                    # ring pierce
#                    "StormX.Uptop", "images/StormSex/Storm_69_Pierce_Tits_R.png",

                    "StormX.Over == 'white shirt' and StormX.Chest in ('black bra','lace bra','sports bra')", "images/StormSex/Storm_69_Pierce_Tits_R_TanU.png",
                    "StormX.Over == 'white shirt'", Null(), #"images/StormSex/Storm_69_Pierce_Tits_R_TanL.png",

                    "StormX.Chest == 'lace bra'", "images/StormSex/Storm_69_Pierce_Tits_R_LaceU.png",
                    "StormX.Chest == 'black bra'", "images/StormSex/Storm_69_Pierce_Tits_R_BlackU.png",
                    "StormX.Chest == 'sports bra'", "images/StormSex/Storm_69_Pierce_Tits_R_BlackU.png",
#                    "StormX.Chest == 'bikini top'", "images/StormSex/Storm_69_Pierce_Tits_R_BlackL.png",
#                    "StormX.Chest == 'cos bra'", "images/StormSex/Storm_69_Pierce_Tits_R_WhiteL.png",

                    "True", Null(), #"images/StormSex/Storm_69_Pierce_Tits_R.png",
                    ),
#            "StormX.Uptop", "images/StormSex/Storm_69_Pierce_Tits_B.png",

            "StormX.Over == 'white shirt' and StormX.Chest in ('black bra','lace bra','sports bra')", "images/StormSex/Storm_69_Pierce_Tits_B_TanU.png",
            "StormX.Over == 'white shirt'", Null(), #"images/StormSex/Storm_69_Pierce_Tits_B_TanL.png",

            "StormX.Chest == 'lace bra'", "images/StormSex/Storm_69_Pierce_Tits_B_LaceU.png",
            "StormX.Chest == 'black bra'", "images/StormSex/Storm_69_Pierce_Tits_B_BlackU.png",
            "StormX.Chest == 'sports bra'", "images/StormSex/Storm_69_Pierce_Tits_B_BlackU.png",
#            "StormX.Chest == 'bikini top'", "images/StormSex/Storm_69_Pierce_Tits_B_BlackL.png",
#            "StormX.Chest == 'cos bra'", "images/StormSex/Storm_69_Pierce_Tits_B_WhiteL.png",

            "True", Null(), #"images/StormSex/Storm_69_Pierce_Tits_B.png",
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'belly' in StormX.Spunk and Player.Male", "images/StormSex/Storm_69_Spunk_Belly.png",
            "True", Null(),
            ),
#        (0,0), "images/StormSex/Storm_Sex_HeadRef.png",
        )
    offset (10,0)#(50,0)#(250,250)#(175,175)
#    yoffset -163
# End Storm 69 Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_69_Bikini_Behind:
    "images/StormSex/Storm_69_Chest_Bikini_Loose.png"
    offset (0,-40)

# Start Storm 69 Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_69_Tits:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Storm_SexSprite
        (1120,840),

        (0,0), ConditionSwitch(
            #shirt layer, behind tits
            "StormX.Uptop and StormX.Over == 'white shirt'", "images/StormSex/Storm_69_Over_Shirt_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #bra layer, behind tits
            "not StormX.Uptop", Null(),
            #if the top's down. . .
#            "StormX.Chest == 'cos bra'", "images/StormSex/Storm_69_Chest_Cos.png",
#            "StormX.Chest == 'tube top'", "images/StormSex/Storm_69_Chest_Tube.png",
            "StormX.Chest == 'black bra'", "images/StormSex/Storm_69_Chest_Bra.png",
            "StormX.Chest == 'lace bra'", "images/StormSex/Storm_69_Chest_Bra.png",
            "StormX.Chest == 'sports bra'", "images/StormSex/Storm_69_Chest_Sports.png",
            "StormX.Chest == 'bikini top'", "Storm_69_Bikini_Behind",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            # base tits
#            "StormX.Chest in ('black bra','lace bra','sports bra')", Null(),
            "True", "images/StormSex/Storm_69_Tits.png",
            ),
#        (0,0), ConditionSwitch(
#            #Wet look
#            "StormX.Water", "images/StormSex/Storm_69_Water_Body.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #bra layer
            "StormX.Uptop", Null(),
            #if the top's down. . .
            "StormX.Chest == 'cos bra'", "images/StormSex/Storm_69_Chest_Cos.png",
            "StormX.Chest == 'tube top'", "images/StormSex/Storm_69_Chest_Tube_Tits.png",
#            "StormX.Chest == 'black bra'", "images/StormSex/Storm_69_Chest_Bra.png",
#            "StormX.Chest == 'lace bra'", "images/StormSex/Storm_69_Chest_Lace.png",
#            "StormX.Chest == 'sports bra'", "images/StormSex/Storm_69_Chest_Sports.png",
            "StormX.Chest == 'bikini top'", "images/StormSex/Storm_69_Chest_Bikini_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #shirt layer
            "StormX.Uptop", Null(),
#            "StormX.Over == 'white shirt' and StormX.Chest in ('black bra','lace bra','sports bra')", Null(),
            "StormX.Over == 'white shirt'", "images/StormSex/Storm_69_Over_Shirt_Tits.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #piercings, only shows when breasts are loose
            "not StormX.Pierce", Null(),
            "StormX.Pierce == 'ring'", ConditionSwitch(
                    # ring pierce
                    "StormX.Uptop", "images/StormSex/Storm_69_Pierce_Tits_R.png",

#                    "StormX.Over == 'white shirt' and StormX.Chest in ('black bra','lace bra','sports bra')", Null(), #"images/StormSex/Storm_69_Pierce_Tits_R_TanU.png",
                    "StormX.Over == 'white shirt'", "images/StormSex/Storm_69_Pierce_Tits_R_TanL.png",

#                    "StormX.Chest == 'lace bra'", Null(), #"images/StormSex/Storm_69_Pierce_Tits_R_LaceU.png",
#                    "StormX.Chest == 'black bra'", Null(), #"images/StormSex/Storm_69_Pierce_Tits_R_BlackU.png",
#                    "StormX.Chest == 'sports bra'", Null(), #"images/StormSex/Storm_69_Pierce_Tits_R_BlackU.png",
                    "StormX.Chest == 'bikini top'", "images/StormSex/Storm_69_Pierce_Tits_R_BlackL.png",
                    "StormX.Chest == 'cos bra' or StormX.Chest == 'tube top'", "images/StormSex/Storm_69_Pierce_Tits_R_WhiteL.png",

                    "True", "images/StormSex/Storm_69_Pierce_Tits_R.png",
                    ),
            "StormX.Uptop", "images/StormSex/Storm_69_Pierce_Tits_B.png",

#            "StormX.Over == 'white shirt' and StormX.Chest in ('black bra','lace bra','sports bra')", Null(), #"images/StormSex/Storm_69_Pierce_Tits_B_TanU.png",
            "StormX.Over == 'white shirt'", "images/StormSex/Storm_69_Pierce_Tits_B_TanL.png",

#            "StormX.Chest == 'lace bra'", Null(), #"images/StormSex/Storm_69_Pierce_Tits_B_LaceU.png",
#            "StormX.Chest == 'black bra'", Null(), #"images/StormSex/Storm_69_Pierce_Tits_B_BlackU.png",
#            "StormX.Chest == 'sports bra'", Null(), #"images/StormSex/Storm_69_Pierce_Tits_B_BlackU.png",
            "StormX.Chest == 'bikini top'", "images/StormSex/Storm_69_Pierce_Tits_B_BlackL.png",
            "StormX.Chest == 'cos bra' or StormX.Chest == 'tube top'", "images/StormSex/Storm_69_Pierce_Tits_B_WhiteL.png",

            "True", "images/StormSex/Storm_69_Pierce_Tits_B.png",
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'tits' in StormX.Spunk and Player.Male", "images/StormSex/Storm_69_Spunk_Tits.png",
            "True", Null(),
            ),
#        (0,0), "images/StormSex/Storm_Sex_HeadRef.png",
        )
    offset (10,0)#(250,250)#(175,175)
#    yoffset -163
# End Storm 69 Pose Tits / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Storm 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_69_Head:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Storm_SexSprite
        (1120,840),
        (0,0), ConditionSwitch(
            #tongue
            "renpy.showing('Storm_69_CUN') and Speed != 3", "images/StormSex/Storm_69_Tongue.png",
            "Speed == 1", "images/StormSex/Storm_69_Tongue.png",
            "True", Null(),
            ),
        (0,0), "images/StormSex/Storm_69_Head.png",
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'chin' in StormX.Spunk and Player.Male", "images/StormSex/Storm_69_Spunk_Chin.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'mouth' in StormX.Spunk and Player.Male", "images/StormSex/Storm_69_Spunk_Mouth.png",
            "True", Null(),
            ),
        (0,0), "images/StormSex/Storm_69_Neck.png",
        (0,0),ConditionSwitch(
            #ring necklace
            "StormX.Neck == 'rings'", "images/StormSex/Storm_69_Necklace.png",
            "True", Null(),
            ),
##        (0,0), ConditionSwitch(
##            #collar
##            "Speed == 1 and Player.Male", Null(),
##            "StormX.Chest == 'swimsuit' or StormX.Panties == 'swimsuit'", "images/StormSex/Storm_69_Collar.png",
##            "True", Null(),
##            ),

#        (0,0), ConditionSwitch(
#            #Hair over
#            "Speed == 1 and Player.Male", Null(),
#            "True", "images/StormSex/Storm_69_Hair.png",
#            ),
        )
    offset (10,0)#(175,175)#(180,100)
#    yoffset -163
# End Storm 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Storm 69 Pose Hair Over / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_69_HairOver:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Storm_SexSprite
        (1120,840),
        (0,0), ConditionSwitch(
            #Hair over
#            "renpy.showing('Storm_TJ_Animation')", Null(),
#            "StormX.Hair == 'blonde'", "images/StormSex/Storm_69_Hair_Blonde_Lick.png",
            "StormX.Hair == 'long' or StormX.Hair == 'wetlong'", "images/StormSex/Storm_69_Hair_Long.png",
            "True", Null(),
            ),
        (0,0), "images/StormSex/Storm_69_Neck.png",
        (0,0),ConditionSwitch(
            #ring necklace
            "StormX.Neck == 'rings'", "images/StormSex/Storm_69_Necklace.png",
            "True", Null(),
            ),
        )
    offset (10,0)#(175,175)#(180,100)
#    yoffset -163
# End Storm 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Storm 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_69_HairBack:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Storm_SexSprite
        (1120,840),
#        (0,0), "images/StormSex/Storm_69_Head.png",
        (0,0), ConditionSwitch(
            #Hair over
#            "renpy.showing('Storm_TJ_Animation')", Null(),
#            "StormX.Hair == 'blonde'", "images/StormSex/Storm_69_Hair_Blonde_Under.png",
            "StormX.Hair == 'long' or StormX.Hair == 'wet' or StormX.Hair == 'wetlong'", "images/StormSex/Storm_69_Hair_Long_Back.png",
            "StormX.Hair == 'mohawk' or StormX.Hair == 'wethawk'", "images/StormSex/Storm_69_Hair_Mohawk.png",
#            "not Player.Male and 'facial' in StormX.Spunk","images/StormSex/Storm_Sprite_Hair_Wet.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hair mid
#            "renpy.showing('Storm_TJ_Animation')", Null(),
#            "StormX.Hair == 'blonde'", "images/StormSex/Storm_69_Hair_Blonde_Under.png",
            "StormX.Hair == 'long' or StormX.Hair == 'wet' or StormX.Hair == 'wetlong'", "images/StormSex/Storm_69_Hair_Long_Mid.png",
#            "StormX.Hair == 'mohawk' or StormX.Hair == 'wethawk'", "images/StormSex/Storm_69_Hair_Mohawk.png",
#            "not Player.Male and 'facial' in StormX.Spunk","images/StormSex/Storm_Sprite_Hair_Wet.png",
            "True", Null(),
            ),
        )
    offset (10,0)#(175,175)#(180,100)
#    yoffset -163
# End Storm 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Storm 69 Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_69_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Storm_SexSprite
        (1120,880),
#        (0,0), ConditionSwitch(
#            #scarf
#            "StormX.Acc", "images/StormSex/Storm_69_Scarf.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #behind hose layer
            "StormX.Hose == 'stockings and garterbelt'", "images/StormSex/Storm_69_BenhindLegs.png",
            "StormX.Hose == 'garterbelt'", "images/StormSex/Storm_69_BenhindLegs.png",
            "StormX.Panties and StormX.PantiesDown", Null(),
            "StormX.Hose == 'pantyhose'", "images/StormSex/Storm_69_BenhindLegs.png",
            "StormX.Hose == 'ripped pantyhose'", "images/StormSex/Storm_69_BenhindLegs.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #back of skirt Layer
            "StormX.Legs == 'skirt'", "images/StormSex/Storm_69_Legs_Skirt_Under.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs
#            "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/StormSex/Storm_Sex_FBase.png",
#            "Player.Sprite and Player.Cock == 'in' and Speed", "images/StormSex/Storm_Sex_FBase.png",
#            "Player.Sprite and Player.Cock == 'in' and Speed", "Storm_Sex_Heading_Pussy",
#            "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/StormSex/Storm_Sex_Ass.png",
#            "Trigger == 'lick pussy'", "images/StormSex/Storm_Sex_Ass.png",
            "True", "images/StormSex/Storm_69_Legs.png",
            ),

#        (0,0), ConditionSwitch(
#            #ass red
#            "StormX.Red", "images/StormSex/Storm_Sex_Red.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            "Player.Sprite and Player.Cock == 'anal'", "images/StormSex/Storm_Sex_Anus_Cover.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #Wet look
            "not StormX.Water", Null(),
            "True", "images/StormSex/Storm_69_Water_Legs.png",
            ),

#        (0,0), "Storm_69_Anus",
#            #Anus Composite  (0,-10)

        (0,0), "Storm_69_Pussy",
            #Pussy Composite


#        (0,0), ConditionSwitch(    #165,560
#            #Personal Wetness
#            "not StormX.Wet", Null(),
#            "(StormX.Legs == 'yoga pants' or StormX.Legs == 'shorts') and not StormX.Upskirt", Null(),
#            "StormX.Panties and not StormX.PantiesDown", Null(),
#            "StormX.Wet == 1", AlphaMask("Wet_Drip_69","images/BetsySex/Betsy_69_Mask_Pussy.png"), #"Wet_Drip_69",
#            "True", AlphaMask("Wet_Drip2_69","images/BetsySex/Betsy_69_Mask_Pussy.png"), #"Wet_Drip2_69",
#            ),

#        (-6,12), ConditionSwitch(    #-695,-480
#            #anal Spunk
#            "'anal' not in StormX.Spunk or not Player.Male", Null(),
#            "(StormX.Legs == 'yoga pants' or StormX.Legs == 'shorts') and not StormX.Upskirt", Null(),
##            "True", "Spunk_Drip2_69", #"Spunk_Drip_69",
#            "True", AlphaMask("Spunk_Drip_69_Anal","images/BetsySex/Betsy_69_Mask_Ass.png"), #"Spunk_Drip_69",
#            ),
#        (-6,12), ConditionSwitch(
#            #anal Spunk
#            "'anal' in StormX.Spunk", "images/BetsySex/Betsy_69_Spunk_Ass.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #hose layer
            "StormX.Hose == 'stockings and garterbelt'", "images/StormSex/Storm_69_Hose_Garter.png",
            "StormX.Hose == 'garterbelt'", "images/StormSex/Storm_69_Hose_Garter.png",
#            "StormX.Hose == 'stockings'", "images/StormSex/Storm_69_Hose_Stockings.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #hose layer
            "StormX.Hose == 'stockings and garterbelt'", "images/StormSex/Storm_69_Hose_Stockings.png",
#            "StormX.Hose == 'garterbelt'", "images/StormSex/Storm_69_Hose_Garter.png",
            "StormX.Hose == 'stockings'", "images/StormSex/Storm_69_Hose_Stockings.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Panties if up
            "StormX.PantiesDown", ConditionSwitch(
                    #If she has panties down. . .
        #            "StormX.Panties == 'cos panties' and StormX.Wet", "images/StormSex/Storm_69_Panties_Cos_Wet.png",
                    "StormX.Panties == 'cos panties'", "images/StormSex/Storm_69_Panties_White_Up.png",
#                    "StormX.Panties == 'white panties' and StormX.Wet", "images/StormSex/Storm_69_Panties_White_Wet.png",
                    "StormX.Panties == 'white panties'", "images/StormSex/Storm_69_Panties_White_Up.png",
#                    "StormX.Panties == 'lace panties'", "images/StormSex/Storm_69_Panties_Lace.png",
#                    "StormX.Panties == 'bikini bottoms' and (StormX.Chest != 'bikini top' or StormX.Uptop)", "images/StormSex/Storm_69_Panties_Bikini_Loose.png",
#                    "StormX.Panties == 'bikini bottoms'", "images/StormSex/Storm_69_Panties_Bikini.png",
        #            "StormX.Panties and StormX.Wet", "images/StormSex/Storm_69_Panties_Black_Wet.png",
                    "StormX.Panties", "images/StormSex/Storm_69_Panties_Black_Up.png",
                    "True", Null(),
                    ),
#            "StormX.Panties == 'cos panties' and StormX.Wet", "images/StormSex/Storm_69_Panties_Cos_Wet.png",
            "StormX.Panties == 'cos panties' and StormX.Wet", "images/StormSex/Storm_69_Panties_Cos_Wet.png",
            "StormX.Panties == 'cos panties'", "images/StormSex/Storm_69_Panties_Cos.png",
            "StormX.Panties == 'white panties' and StormX.Wet", "images/StormSex/Storm_69_Panties_White_Wet.png",
            "StormX.Panties == 'white panties'", "images/StormSex/Storm_69_Panties_White.png",
            "StormX.Panties == 'lace panties'", "images/StormSex/Storm_69_Panties_Lace.png",
            "StormX.Panties == 'bikini bottoms' and (StormX.Chest != 'bikini top' or StormX.Uptop)", "images/StormSex/Storm_69_Panties_Bikini_Loose.png",
            "StormX.Panties == 'bikini bottoms'", "images/StormSex/Storm_69_Panties_Bikini.png",
#            "StormX.Panties and StormX.Wet", "images/StormSex/Storm_69_Panties_Black_Wet.png",
            "StormX.Panties", "images/StormSex/Storm_69_Panties_Black.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #pantyhose layer
            "StormX.Panties and StormX.PantiesDown", Null(),
            "StormX.Hose == 'pantyhose'", "images/StormSex/Storm_69_Hose_Pantyhose.png",
            "StormX.Hose == 'ripped pantyhose'", "images/StormSex/Storm_69_Hose_Pantyhose_Holed.png",
            "True", Null(),
            ),


        (0,0), ConditionSwitch(
            #Legs Layer
            "StormX.Legs == 'skirt'", "images/StormSex/Storm_69_Legs_Skirt_Over.png",
            "StormX.Legs == 'pants' and StormX.Wet > 1", "images/StormSex/Storm_69_Legs_Pants_Wet.png",
            "StormX.Legs == 'pants' and StormX.Upskirt", "images/StormSex/Storm_69_Legs_Pants_Up.png",
            "StormX.Legs == 'yoga pants' and StormX.Upskirt", "images/StormSex/Storm_69_Legs_Yoga_Up.png",
            "StormX.Legs == 'pants'", "images/StormSex/Storm_69_Legs_Pants.png",
            "StormX.Legs == 'yoga pants' and StormX.Wet > 1", "images/StormSex/Storm_69_Legs_Yoga_Wet.png",
            "StormX.Legs == 'yoga pants'", "images/StormSex/Storm_69_Legs_Yoga.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #leg rings
            "not StormX.Acc == 'rings' or StormX.Legs == 'pants' or StormX.Legs == 'yoga pants'", Null(),
            "True", "images/StormSex/Storm_69_Legs_Rings.png", #StormX.ArmPose == 2
            ),
        (0,0), ConditionSwitch(
            #Piercings over pants and pantyhose
            "not StormX.Pierce", Null(),
            "StormX.Pierce == 'ring'",ConditionSwitch(
                    #If she has panties down. . .
                    "StormX.Wet > 1 and (StormX.Legs == 'pants' or StormX.Legs == 'yoga pants') and not StormX.Upskirt", "images/StormSex/Storm_69_Pierce_Pussy_R_BlackW.png",
                    "(StormX.Legs == 'pants' or StormX.Legs == 'yoga pants') and not StormX.Upskirt", "images/StormSex/Storm_69_Pierce_Pussy_R_Black.png",

                    "StormX.PantiesDown", "images/StormSex/Storm_69_Pierce_Pussy_R.png",
                    "StormX.Hose == 'pantyhose'", "images/StormSex/Storm_69_Pierce_Pussy_R_Black.png",
                    "StormX.Panties == 'lace panties'", "images/StormSex/Storm_69_Pierce_Pussy_R_Lace.png",
                    "StormX.Wet and (StormX.Panties == 'white panties' or StormX.Panties == 'cos panties')", "images/StormSex/Storm_69_Pierce_Pussy_R_WhiteW.png",
                    "StormX.Panties == 'white panties' or StormX.Panties == 'cos panties'", "images/StormSex/Storm_69_Pierce_Pussy_R_White.png",
#                "StormX.Wet and StormX.Panties", "images/StormSex/Storm_69_Pierce_Pussy_R_BlackW.png",
                    "StormX.Panties", "images/StormSex/Storm_69_Pierce_Pussy_R_Black.png",
                    "True", "images/StormSex/Storm_69_Pierce_Pussy_R.png",

                    "True", Null(),
                    ),
            #else, it's barbell
#            "StormX.Legs == 'shorts' and not StormX.Upskirt", "images/StormSex/Storm_69_Pierce_Pussy_B_Clothed.png",
#            "StormX.Hose == 'pantyhose' and not (StormX.Panties and StormX.PantiesDown)", "images/StormSex/Storm_69_Pierce_Pussy_Lace_B.png",

            "StormX.Wet > 1 and (StormX.Legs == 'pants' or StormX.Legs == 'yoga pants') and not StormX.Upskirt", "images/StormSex/Storm_69_Pierce_Pussy_B_BlackW.png",
            "(StormX.Legs == 'pants' or StormX.Legs == 'yoga pants') and not StormX.Upskirt", "images/StormSex/Storm_69_Pierce_Pussy_B_Black.png",

            "StormX.PantiesDown", "images/StormSex/Storm_69_Pierce_Pussy_B.png",
            "StormX.Hose == 'pantyhose'", "images/StormSex/Storm_69_Pierce_Pussy_B_Black.png",
            "StormX.Panties == 'lace panties'", "images/StormSex/Storm_69_Pierce_Pussy_B_Lace.png",
            "StormX.Wet and (StormX.Panties == 'white panties' or StormX.Panties == 'cos panties')", "images/StormSex/Storm_69_Pierce_Pussy_B_WhiteW.png",
            "StormX.Panties == 'white panties' or StormX.Panties == 'cos panties'", "images/StormSex/Storm_69_Pierce_Pussy_B_White.png",
#            "StormX.Wet and StormX.Panties", "images/StormSex/Storm_69_Pierce_Pussy_B_BlackW.png",
            "StormX.Panties", "images/StormSex/Storm_69_Pierce_Pussy_B_Black.png",
            "True", "images/StormSex/Storm_69_Pierce_Pussy_B.png",
            ),
#        (0,0), ConditionSwitch(
#            #Piercings over pants and pantyhose
#            "not StormX.Pierce", Null(),
#            "StormX.Pierce == 'ring'",ConditionSwitch(
#                    #If she has panties down. . .
#                    "Player.Sprite and Player.Cock == 'in'", Null(),
#                    "StormX.Legs == 'shorts' and not StormX.Upskirt", "images/StormSex/Storm_69_Pierce_Pussy_R_Brown.png",
#                    "StormX.Hose == 'tights' and not (StormX.Panties and StormX.PantiesDown)", "images/StormSex/Storm_Sex_Pierce_Pussy_R_Tights.png",
#                    "True", Null(),
#                    ),
#            #else, it's barbell
#            "StormX.Legs == 'shorts' and not StormX.Upskirt", "images/StormSex/Storm_69_Pierce_Pussy_B_Clothed.png",
#            "StormX.Hose == 'tights' and not (StormX.Panties and StormX.PantiesDown)", "images/StormSex/Storm_Sex_Pierce_Pussy_B_Tights.png",
#            "True", Null(),
#            ),

#        (0,0), ConditionSwitch(
#            #pussy fondling animation
##            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Storm_Sex_Fondle_Pussy",
#            "True", "images/StormSex/Storm_Sex_Hand.png",
#            ),

#        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer
#            "not Player.Sprite or Player.Cock != 'out'", Null(),
#            "Speed >= 2", "Storm_Hotdog_Zero_Anim2",
#            "Speed", "Storm_Hotdog_Zero_Anim1",
#            "True", "Storm_Hotdog_Zero_Anim0",
#            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
#            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy' or Trigger2 == 'lick pussy'", "Storm_69_Lick_Pussy",
            "Trigger == 'lick ass' or Trigger2 == 'lick ass'", "Storm_69_Lick_Ass",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy fondling animation
            "StormX.Offhand == 'fondle pussy' and StormX.Lust > 60 and not (Player.Sprite)",  At("StormFingerHand", GirlFingerPussyX()), #"Storm_Sex_Mast2",
            "StormX.Offhand == 'fondle pussy'", At("StormMastHand", GirlGropePussyX()), #"Storm_Sex_Mast",
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Storm_Sex_Fondle_Pussy",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Footjob overlay
#            "Player.Cock == 'foot'", Null(),
#            "Player.Sprite and Player.Cock == 'anal'",AlphaMask("Storm_69_Feet", "images/StormSex/Storm_Sex_Feet_Mask.png"),
#            "renpy.showing('Anal_Plug_In_Sex') or renpy.showing('Anal_Plug_Out_Sex')",AlphaMask("Storm_69_Feet", "images/StormSex/Storm_Sex_Feet_Mask.png"),
#            "ShowFeet", "Storm_69_Feet",
##            "Player.Sprite", AlphaMask("Storm_Sex_Feet", "images/StormSex/Storm_Sex_Feet_Mask.png"),
##            "Trigger == 'lick pussy'", AlphaMask("Storm_Sex_Feet", "images/StormSex/Storm_Sex_Feet_Mask.png"),
##            "Trigger == 'lick ass'", AlphaMask("Storm_Sex_Feet", "images/StormSex/Storm_Sex_Feet_Mask.png"),
#            "True", AlphaMask("Storm_69_Feet", "images/StormSex/Storm_Sex_Feet_Mask.png"),
#            ),

#        (0,0), ConditionSwitch(                                                                                 #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
#            "not Speed", "Storm_Sex_Feet",
#            "Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Storm_Sex_Feet", "images/StormSex/Storm_Sex_FeetMask.png"),
#            "True", "Storm_Sex_Feet",
#            ),
        )
#    offset (0,20)#(175,175)
# End Storm 69 Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#image Storm_69_Feet:
#    LiveComposite(
#        #the lower legs used in the sex pose, referenced by Storm_Sex_Legs
#        (1120,840),
##        (0,0), "images/StormSex/Storm_Sex_Feet.png",                                                         #Legs Base

#        (0,0), ConditionSwitch(
#            #hose layer
#            "(StormX.Hose == 'pantyhose' or StormX.Hose == 'ripped pantyhose') and StormX.Panties and StormX.PantiesDown", "images/StormSex/Storm_69_Feet.png",
#            "(StormX.Hose == 'tights' or StormX.Hose == 'ripped tights') and StormX.Panties and StormX.PantiesDown", "images/StormSex/Storm_69_Feet.png",
#            "StormX.Hose == 'tights'", "images/StormSex/Storm_69_Feet_Tights.png",
#            "StormX.Hose == 'ripped pantyhose'", "images/StormSex/Storm_69_Feet_Holed.png",
#            "StormX.Hose == 'ripped tights'", "images/StormSex/Storm_69_Feet_Tights_Holed.png",
#            "StormX.Hose and StormX.Hose != 'garterbelt'", "images/StormSex/Storm_69_Feet_Hose.png",
#            "True", "images/StormSex/Storm_69_Feet.png",   #Null(),
#            ),

##        (0,0), ConditionSwitch(
##            #Wet look
##            "not StormX.Water", Null(),
##            "True", "images/StormSex/Storm_69_Water_Feet.png",
##            ),
#        (0,0), ConditionSwitch(
#            #spunk
#            "'feet' in StormX.Spunk", "images/StormSex/Storm_Sex_Spunk_Feet.png",
#            "True", Null(),
#            ),
#        )

# Start Storm 69 Pose Pussy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_69_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).

    contains:
            # The background plate of her pussy
            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/StormSex/Storm_Sex_Pussy_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed", "Storm_Sex_Heading_Pussy",
#                "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/StormSex/Storm_Sex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/StormSex/Storm_69_Pussy_Open.png",
                "StormX.Offhand == 'fondle pussy' and StormX.Lust > 60", "images/StormSex/Storm_69_Pussy_Open.png",
                "True", "images/StormSex/Storm_69_Pussy_Closed.png",
                )
    contains:
            #wet drip
            ConditionSwitch(
                "not StormX.Wet", Null(),
                "(StormX.Legs == 'yoga pants' or StormX.Legs == 'shorts') and not StormX.Upskirt", Null(),
                "StormX.Panties and not StormX.PantiesDown", Null(),
#                "True", "Spunk_Drip_69",
                "True", AlphaMask("Wet_Drip_69","images/StormSex/Storm_69_Mask_Pussy.png"),
                )
            offset (0,0)#(-700,-570)
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "not StormX.Wet", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/JubesSex/Jubes_Sex_WetPussy_F.png",
                "True", "images/StormSex/Storm_69_Wet.png",
                )
    contains:
            # pubes
            ConditionSwitch(
                "not StormX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Fucking.png"),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 1", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Fucking.png"),
#                "Player.Sprite and Player.Cock == 'in'", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Open.png"),
#                "Player.Sprite and Player.Cock == 'out'", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Open.png"),
                "StormX.Panties == 'bikini bottoms' and StormX.Chest == 'bikini top' and not StormX.Uptop", Null(),
                "Trigger == 'lick pussy'", "images/StormSex/Storm_69_Pubes.png",
                "StormX.Offhand == 'fondle pussy' and StormX.Lust > 60", "images/StormSex/Storm_69_Pubes.png",
                "True", "images/StormSex/Storm_69_Pubes.png",
                )
    contains:
            #Spunk
            ConditionSwitch(
                "'in' not in StormX.Spunk or not Player.Male", Null(),
                "(StormX.Legs == 'yoga pants' or StormX.Legs == 'shorts') and not StormX.Upskirt", Null(),
                "StormX.Panties and not StormX.PantiesDown", Null(),
#                "True", "Spunk_Drip_69",
                "True", AlphaMask("Spunk_Drip_69","images/StormSex/Storm_69_Mask_Pussy.png"),
                )
            offset (0,0)#(-700,-570)

    contains:
            ConditionSwitch(
                #Outside Spunk
#                "'in' in StormX.Spunk and Player.Sprite and Player.Cock == 'in' and Speed and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_PussyF.png",
                "'in' in StormX.Spunk and Player.Male", "images/StormSex/Storm_69_Spunk_Pussy.png",
                "True", Null(),
                )
#            offset (0,10)
#    contains:
#            #Spunk under penis
#            ConditionSwitch(
#                "'in' in StormX.Spunk", "images/StormSex/Storm_Sex_Spunk_Puss_Under.png",
#                "True", Null(),
#                )
#    contains:
#            #hose layer
#            ConditionSwitch(
#                "StormX.Panties and StormX.PantiesDown", Null(),
#                "StormX.Hose == 'ripped pantyhose' and ShowFeet", Recolor("Storm", "Hose", "images/StormSex/Storm_Sex_Hose_Pantyhose_Holed.png"),
#                "StormX.Hose == 'ripped pantyhose'", Recolor("Storm", "Hose", "images/StormSex/Storm_Sex_Hose_Pantyhose_Holed.png"),
#                "True", Null(),
#                ),
#    contains:
#            # The animation of Zero's moving penis, masked by her pussy shape
#            ConditionSwitch(
##                "not Player.Sprite", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 3", AlphaMask("Storm_Sex_Fucking_Zero_Anim3", "Storm_Sex_Fucking_Mask"),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", AlphaMask("Storm_Sex_Fucking_Zero_Anim2", "Storm_Sex_Fucking_Mask"),
#                "Player.Sprite and Player.Cock == 'in' and Speed == 1", AlphaMask("Storm_Sex_Fucking_Zero_Anim1", "Storm_Sex_Heading_Mask"),
#                "Player.Sprite and Player.Cock == 'in'", "Storm_Sex_Fucking_Zero_Anim0",
#                "True", Null(),
#                )
#    contains:
#            #Piercings
#            ConditionSwitch(
#                "StormX.Pierce == 'barbell' and Player.Sprite and Player.Cock == 'in' and Speed", "images/StormSex/Storm_Sex_Pierce_Pussy_BarbellF.png",
#                "StormX.Pierce == 'ring' and Player.Sprite and Player.Cock == 'in' and Speed", "images/StormSex/Storm_Sex_Pierce_Pussy_RingF.png",
#                "StormX.Pierce == 'barbell'", "images/StormSex/Storm_Sex_Pierce_Pussy_Barbell.png",
#                "StormX.Pierce == 'ring'", "images/StormSex/Storm_Sex_Pierce_Pussy_Ring.png",
#                "True", Null(),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed == 1", "Storm_Pussy_Spunk_Heading",
#                "True", Null(),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "Speed == 1", Null(),
#                "'in' not in StormX.Spunk or not Player.Sprite or Player.Cock != 'in' or not Speed or not Player.Male", Null(),
##                "Speed <= 1", Null(), #"Storm_Pussy_Spunk_Heading",
#                "True", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
#                )

    #End Storm Pussy composite


image Storm_69_Lick_Pussy:
        "Lick_AnimF"
        zoom 0.7
        rotate 180
        offset (510,500)#(535,500
image Storm_69_Lick_Ass:
        "Lick_AnimF"
        zoom 0.7
        rotate 180
        offset (535,580)#(535,550)

image Storm_69_Fondle_Pussy:
        "GropePussy_Storm"
        xzoom -1.5
        yzoom 1.5
        offset(-710,-300) #(-890,-300)
#        block:
#            ease 1 offset(-1000,0) #(535,500)
#            ease 1 offset(-1000,-1000) #(535,500)
#            ease 1 offset(0,-1000) #(535,500)
#            ease 1 offset(0,0) #(535,500)
#            repeat

image Storm_69_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/JubesSex/Jubes_Sex_Anal.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/JubesSex/Jubes_Sex_Anal.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/StormSex/Storm_Sex_Anus.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/StormSex/Storm_Sex_Anus.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed", "Storm_Sex_Anal_Heading",
#            "Player.Sprite and Player.Cock == 'anal'", "Storm_Sex_Anal_Tip",
            "StormX.Plug", "images/PlugBase_Sex.png",
            "StormX.Loose > 2", "Storm_Gape_Anal_Sex",
#            "StormX.Loose", "images/StormSex/Storm_Sex_Anus_Loose.png",
            "True", "images/StormSex/Storm_Sex_Anus_Loose.png",
            "True", Null(),
            )
#    contains:
#            #Spunk under penis
#            ConditionSwitch(
#                "'anal' not in StormX.Spunk or not Player.Male", Null(),
##                "Player.Sprite and Player.Cock != 'anal' and Speed >= 1", "images/StormSex/Storm_Sex_Spunk_Anal_Under.png",
##                "Player.Sprite and Player.Cock == 'anal' and Speed == 1", "Storm_Sex_Anal_Spunk_Heading_Under",
#                "True", "images/StormSex/Storm_69_Spunk_Ass.png",
#                )
#            offset (5,0)
#    contains:
#            # The animation of Zero's moving penis, masked by her anus shape
#            ConditionSwitch(
#                "not Player.Sprite or Player.Cock != 'anal'", Null(),
#                "Speed >= 3",  AlphaMask("Storm_Sex_Anal_Zero_Anim3", "Storm_Sex_Anal_MaskF"),
#                "Speed >= 2", AlphaMask("Storm_Sex_Anal_Zero_Anim2", "Storm_Sex_Anal_MaskF"),
#                "Speed", AlphaMask("Storm_Sex_Anal_Zero_Anim1", "Storm_Sex_Anal_Mask"),
#                "True", AlphaMask("Storm_Sex_Anal_Zero_Anim0", "Storm_Sex_Anal_Mask"),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "'anal' not in StormX.Spunk or not Player.Sprite or Player.Cock != 'anal' or not Speed or not Player.Male", Null(),
#                "Speed == 1", "Storm_Sex_Anal_Spunk_Heading_Over",
#                "True", "Storm_Sex_Anal_Spunk",
#                )


#Start Animations for Storm's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_69_Static:
        #this is the animation for Storm's hairback during 69, Speed 0 (static)
        contains:
            subpixel True
            "Storm_69_HairBack"
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
        #this is the animation for Storm's head during 69, Speed 0 (static)
        contains:
            subpixel True
            "Storm_69_Head"
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
        #this is the animation for Storm's upper body during 69, Speed 0 (static)
        contains:
#            "Storm_69_Tits"

            ConditionSwitch(
                # base tits
                "not StormX.Uptop and StormX.Chest in ('black bra','lace bra','sports bra')", Null(),
                "True", "Storm_69_Tits",
                )
            subpixel True
            rotate 180
#            zoom .65
            pos (0,-25) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,-30) #top
                pause .25
                ease 1 pos (0,-25) #bottom
                repeat
        contains:
            "Storm_69_Body"
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
        #this is the animation for Storm's lower body during 69, Speed 0 (static)
        contains:
            "Storm_69_Legs"
            subpixel True
            rotate 180
            offset (-20,-20)
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat

#Start Animations for Storm's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_69_Anim1:
        #this is the animation for Storm's hairback during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Storm_69_HairBack"
            rotate 180
#            zoom .75
            offset (-10,-5)
#            offset (180,50)#(180,100)
            pos (70,60) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (35,-45) #top
                pause 1.2
                ease 2.55 pos (70,55) #bottom
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 rotate 180
                pause 1.50
                ease 2.25 rotate 200
                repeat
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
        #this is the animation for Storm's head during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Storm_69_Head"
            rotate 220
#            zoom .75
#            offset (180,50)#(180,100)
            pos (70,60) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (35,-45) #top
                pause 1.25
                ease 2.5 pos (70,60) #bottom
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .50 rotate 200
                pause 1.5
                ease 1.25 rotate 220
                pause 1.25
                repeat
        #this is the animation for Storm's upper body during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Storm_69_HairOver"
            rotate 180
#            zoom .75
            offset (-10,-5)
#            offset (180,50)#(180,100)
            pos (70,60) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (35,-45) #top
                pause 1.2
                ease 2.55 pos (70,55) #bottom
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 rotate 180
                pause 1.50
                ease 2.25 rotate 200
                repeat
        contains:
            subpixel True
#            "Storm_69_Tits"
            ConditionSwitch(
                # base tits
                "not StormX.Uptop and StormX.Chest in ('black bra','lace bra','sports bra')", Null(),
                "True", "Storm_69_Tits",
                )
            rotate 180
#            zoom .65
            pos (50,40) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (10,-10) #top
                pause 1.25
                ease 2.5 pos (50,40) #bottom
                repeat
            parallel:
                #Total time, 5 seconds
                ease .25 rotate 183
                ease .25 rotate 180
                ease .5 rotate 175
                ease .25 rotate 183
                ease .25 rotate 180

                pause 1.0
                ease 1.25 rotate 190
                pause 1
                ease .25 rotate 177
                repeat
#                ease .25 rotate 175
#                ease .25 rotate 185
#                ease .25 rotate 180
#                pause 2.25
#                ease 1.25 rotate 185
#                pause 0.75
#                repeat
        contains:
            subpixel True
            "Storm_69_Body"
            rotate 180
#            zoom .65
            pos (50,40) #X less is left, Y less is up
            block:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (10,0) #top
                pause 1.25
                ease 2.5 pos (50,40) #bottom
                repeat
        #this is the animation for Storm's lower body during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Storm_69_Legs"
            rotate 200
            offset (-20,-20)
            pos (0,0) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .25
                easein 1 pos (10,-5)
                pause 1
                ease 2.75 pos (40,10)
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 rotate 180
                pause 1.50
                ease 2.25 rotate 200
                repeat

#Start Animations for Storm's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_69_Anim2:
        #this is the animation for Storm's hairback during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Storm_69_HairBack"
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
        #this is the animation for Storm's head during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Storm_69_Head"
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
        #this is the animation for Storm's upper body during 69, Speed 2 (heading)
        contains:
#            "Storm_69_Tits"
            ConditionSwitch(
                # base tits
                "not StormX.Uptop and StormX.Chest in ('black bra','lace bra','sports bra')", Null(),
                "True", "Storm_69_Tits",
                )
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
            "Storm_69_Body"
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
        #this is the animation for Storm's lower body during 69, Speed 2 (heading)
        contains:
            "Storm_69_Legs"
            subpixel True
            rotate 180
            offset (-20,-20)
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat

#Start Animations for Storm's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_69_Anim3:
        #this is the animation for Storm's hairback during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Storm_69_HairBack"
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
        #this is the animation for Storm's head during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Storm_69_Head"
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
        contains:
            subpixel True
            "Storm_69_HairOver"
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
        #this is the animation for Storm's upper body during 69, Speed 3 (sucking)
        contains:
            subpixel True
#            "Storm_69_Tits"
            ConditionSwitch(
                # base tits
                "not StormX.Uptop and StormX.Chest in ('black bra','lace bra','sports bra')", Null(),
                "True", "Storm_69_Tits",
                )
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
                easein .2 yzoom 1.1
                easein .2 yzoom 1
                pause .35
#                ease .35 yzoom 1.1
                #moving down 1.25
                ease .5 yzoom .9
                ease .75 yzoom 1         #bottom
                repeat
        #this is the animation for Storm's lower body during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Storm_69_Body"
            rotate 180
#            zoom .65
            pos (0,30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-5) #top
#                pause .5
                ease 1.25 pos (0,30) #bottom
                repeat
        #this is the animation for Storm's lower body during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Storm_69_Legs"
            rotate 180
            offset (-20,-20)
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,-5)
#                pause .5
                ease 1.25 pos (0,10)
                repeat

#Start Animations for Storm's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_69_Anim4:
        #this is the animation for Storm's hairback during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Storm_69_HairBack"
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
        #this is the animation for Storm's head during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Storm_69_Head"
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
        #this is the animation for Storm's upper body during 69, Speed 4 (deep)
#        contains:
#            subpixel True
#            "Storm_69_Tits"
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
#            "Storm_69_Tits"
            ConditionSwitch(
                # base tits
                "not StormX.Uptop and StormX.Chest in ('black bra','lace bra','sports bra')", Null(),
                "True", "Storm_69_Tits",
                )
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
                easein .25 yzoom 1.2  #top
                easein .25 yzoom 1.1  #top
                easein .25 yzoom 1.2  #top
                ease .5 yzoom 1  #top
                #moving down 1.75
                ease .5 yzoom .9  #bottom
                ease 1.25 yzoom 1  #bottom
                repeat
        contains:
            subpixel True
            "Storm_69_Body"
            rotate 180
#            zoom .65
            pos (0,40) #X less is left, Y less is up
#            alpha .9
            block:
                #Total time, 3 seconds
                easein .75 pos (0,5) #top
                pause .5
                ease 1.75 pos (0,40) #bottom
                repeat
        #this is the animation for Storm's lower body during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Storm_69_Legs"
            rotate 180
            offset (-20,-20)
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,-5)
#                pause .5
                ease 2.25 pos (0,10)
                repeat

#Start Animations for Storm's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_69_Anim5:
        #this is the animation for Storm's hairback during 69, Speed 5 (cum high)
        contains:
            subpixel True
            "Storm_69_HairBack"
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
        #this is the animation for Storm's head during 69, Speed 5 (cum high)
        contains:
            subpixel True
            "Storm_69_Head"
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
        #this is the animation for Storm's upper body during 69, Speed 5 (cum high)
        contains:
#            "Storm_69_Tits"
            ConditionSwitch(
                # base tits
                "not StormX.Uptop and StormX.Chest in ('black bra','lace bra','sports bra')", Null(),
                "True", "Storm_69_Tits",
                )
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
            "Storm_69_Body"
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
        #this is the animation for Storm's lower body during 69, Speed 5 (cum high)
        contains:
            "Storm_69_Legs"
            subpixel True
            rotate 180
            offset (-20,-20)
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein 1.75 pos (0,-5)
                pause .5
                ease 1.25 pos (0,0)
                repeat

#Start Animations for Storm's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_69_Anim6:
        #this is the animation for Storm's hairback during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Storm_69_HairBack"
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
        #this is the animation for Storm's head during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Storm_69_Head"
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
        #this is the animation for Storm's upper body during 69, Speed 6 (cum deep)
        contains:
            subpixel True
#            "Storm_69_Tits"
            ConditionSwitch(
                # base tits
                "not StormX.Uptop and StormX.Chest in ('black bra','lace bra','sports bra')", Null(),
                "True", "Storm_69_Tits",
                )
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
            "Storm_69_Body"
            rotate 180
#            zoom .65
            pos (0,30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,35) #top
                pause .5
                ease 1.75 pos (0,30) #bottom
                repeat
        #this is the animation for Storm's lower body during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Storm_69_Legs"
            rotate 180
            offset (-20,-20)
            pos (0,20) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,10)
#                pause .5
                ease 2.25 pos (0,20)
                repeat

#End Animations for Storm's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#Start Storm 69 Cunnilingus Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

#Start Animations for Storm's 69 Cunnalingus pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_69_CUN:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
#                "True", "Storm_69_Anim1",
                "Speed == 2",   "Storm_69_Cun2",
                "Speed == 3",   "Storm_69_Cun3",
                "Speed",        "Storm_69_Cun1",
                "True",         "Storm_69_Cun0",
                ),
        )
    align (0.6,0.0)
    pos (475,-700)
    zoom 1.8#1/3

#Start Animations for Storm's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Animations for Storm's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_69_Cun0:
        #this is the animation for Storm's hairback during 69, Speed 0 (static)
        contains:
            subpixel True
            "Storm_69_HairBack"
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
        #this is the animation for Storm's head during 69, Speed 0 (static)
        contains:
            subpixel True
            "Storm_69_Head"
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
        #this is the animation for Storm's upper body during 69, Speed 0 (static)
        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (728,920)#(590,620)
        contains:
#            "Storm_69_Tits"
            ConditionSwitch(
                # base tits
                "not StormX.Uptop and StormX.Chest in ('black bra','lace bra','sports bra')", Null(),
                "True", "Storm_69_Tits",
                )
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
            "Storm_69_Body"
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
#            "Storm_69_Body"
#            rotate 180
##            zoom .65
#            pos (0,30) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                easein .75 pos (0,35) #top
#                pause .5
#                ease 1.75 pos (0,30) #bottom
#                repeat

        #this is the animation for Storm's lower body during 69, Speed 0 (static)
        contains:
            "Storm_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            offset (-20,-20)
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat

#Start Animations for Storm's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_69_Cun1:
        #this is the animation for Storm's hairback during 69, Speed 1 (lick)
        contains:
            subpixel True
            "Storm_69_HairBack"
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
        #this is the animation for Storm's head during 69, Speed 1 (lick)
        contains:
            subpixel True
            "Storm_69_Head"
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
        #this is the animation for Storm's upper body during 69, Speed 1 (lick)
        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (728,920)#(590,620)
        contains:
#            "Storm_69_Tits"
            ConditionSwitch(
                # base tits
                "not StormX.Uptop and StormX.Chest in ('black bra','lace bra','sports bra')", Null(),
                "True", "Storm_69_Tits",
                )
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
            "Storm_69_Body"
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
        #this is the animation for Storm's lower body during 69, Speed 1 (lick)
        contains:
            "Storm_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            offset (-20,-20)
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat


#Start Animations for Storm's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_69_Cun2:
        #this is the animation for Storm's hairback during 69, Speed 2 (clit)
        contains:
            subpixel True
            "Storm_69_HairBack"
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
        #this is the animation for Storm's head during 69, Speed 2 (clit)
        contains:
            subpixel True
            "Storm_69_Head"
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
        #this is the animation for Storm's upper body during 69, Speed 2 (clit)
        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (728,920)#(590,620)
        contains:
#            "Storm_69_Tits"
            ConditionSwitch(
                # base tits
                "not StormX.Uptop and StormX.Chest in ('black bra','lace bra','sports bra')", Null(),
                "True", "Storm_69_Tits",
                )
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
            "Storm_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (10,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1 pos (10,-5) #top
                ease 1 pos (10,0) #bottom
                repeat
        #this is the animation for Storm's lower body during 69, Speed 2 (clit)
        contains:
            "Storm_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            offset (-20,-20)
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat

#Start Animations for Storm's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_69_Cun3:
        #this is the animation for Storm's hairback during 69, Speed 3 (suck)
        contains:
            subpixel True
            "Storm_69_HairBack"
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
        #this is the animation for Storm's head during 69, Speed 3 (suck)
        contains:
            subpixel True
            "Storm_69_Head"
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
        #this is the animation for Storm's upper body during 69, Speed 3 (suck)
        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (728,920)#(590,620)
        contains:
#            "Storm_69_Tits"
            ConditionSwitch(
                # base tits
                "not StormX.Uptop and StormX.Chest in ('black bra','lace bra','sports bra')", Null(),
                "True", "Storm_69_Tits",
                )
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
            "Storm_69_Body"
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
        #this is the animation for Storm's lower body during 69, Speed 3 (suck)
        contains:
            "Storm_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            offset (-20,-20)
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat
#End Animations for Storm's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#End Storm 69 Animations

# Start Storm Scissor Pose content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_SC_Sprite:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
                #if the top's down. . .
                "Speed >= 2", "Storm_SC_Anim_2",
                "Speed", "Storm_SC_Anim_1",
                "True", "Storm_SC_Anim_0",
                ),
        )
    align (0.6,0.0)
    pos (650,300)#(650,200)(925,740)#(910,850)
    zoom 0.85#0.8

# End Storm Sex Pose Speed 2 Scissor / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Storm Sex Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_SC_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Storm_SexSprite
        (1120,960),
#        (0,0), ConditionSwitch(
#Legs Layer
#            "StormX.Legs == 'blue skirt'", "images/StormSex/Storm_Sex_Skirt_Back.png",
#            "True", Null(),
#            ),
#        (0,0), "images/StormSex/Storm_Sex_Legs.png",
#Legs Base

#        (0,0), ConditionSwitch(
#            #Skirt back
#            "StormX.Legs == 'skirt'", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_Skirt_Back.png"),
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #plug
#            "StormX.Plug", "Storm_Sex_Plug",
#            "True", Null(),
#            ),
#        (0,0),ConditionSwitch(
#            #Outside Spunk
#            "'anal' in StormX.Spunk and Player.Male", "images/StormSex/Storm_Sex_Spunk_Anal_Closed.png",
#            "True", Null(),
#            ),
        (0,0),"images/StormSex/Storm_Sex_Legs_FJ.png",
        (0,0), ConditionSwitch(
            #Wet look
            "not StormX.Water", Null(),
            "True", "images/StormSex/Storm_Sex_Wet_Legs_FJ.png",
            ),

#        (0,0), "Storm_Sex_Anus",
#            #Anus Composite

        (0,0), "Storm_SC_Pussy",
            #Pussy Composite


        (0,0), ConditionSwitch(
            #hose layer
            #If she has panties down. . .
            "StormX.Hose == 'stockings and garterbelt'", Recolor("Storm", "Hose", "images/StormSex/Storm_Sex_Hose_StockingsGarter_FJ.png"),
            "StormX.Hose == 'garterbelt'", Recolor("Storm", "Hose", "images/StormSex/Storm_Sex_Hose_Garter_FJ.png"),
            "StormX.Hose == 'stockings'", Recolor("Storm", "Hose", "images/StormSex/Storm_Sex_Hose_Stockings_FJ.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #leg rings
            "not StormX.Acc == 'rings' or StormX.Legs == 'pants' or StormX.Legs == 'yoga pants'", Null(),
            "True", "images/StormSex/Storm_Sex_LegRings_FJ.png", #StormX.ArmPose == 2
            ),
        (0,0), ConditionSwitch(
            #Panties if up
            "StormX.Legs and StormX.Legs != 'skirt' and not StormX.Upskirt", Null(),
            "StormX.PantiesDown",ConditionSwitch(
                    #If she has panties down. . .
                    "StormX.Panties == 'cos panties'", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Cos_FJ_Down.png"),
                    "StormX.Panties == 'white panties'", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_White_FJ_Down.png"),
                    "StormX.Panties", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Black_FJ_Down.png"),
                    "True", Null(),
                    ),
            #If she has panties down. . .
            "StormX.Panties == 'cos panties' and StormX.Wet", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Cos_FJ_Wet.png"),
            "StormX.Panties == 'cos panties'", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Cos_FJ.png"),
            "StormX.Panties == 'white panties' and StormX.Wet", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_White_FJ_Wet.png"),
            "StormX.Panties == 'white panties'", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_White_FJ.png"),
            "StormX.Panties == 'lace panties'", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Lace_FJ.png"),
            "StormX.Panties == 'bikini bottoms' and (StormX.Chest != 'bikini top' or StormX.Uptop)", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Bikini_FJ_Top.png"),
            "StormX.Panties == 'bikini bottoms'", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Bikini_FJ.png"),
            "StormX.Panties and StormX.Wet", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Black_FJ_Wet.png"),
            "StormX.Panties", Recolor("Storm", "Panties", "images/StormSex/Storm_Sex_Panties_Black_FJ.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Piercings
#            "Player.Sprite", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),
            "not StormX.Panties and StormX.Hose != 'pantyhose'", Null(),
            "((StormX.Panties or StormX.Hose == 'pantyhose') and StormX.PantiesDown)", Null(),
                #if she has panties, but they are down, or pantyhose, or Legs that are not a skirt and are not down, skip these. . .
            "StormX.Pierce == 'barbell'", "images/StormSex/Storm_Sex_Pierce_Pussy_BarbellC.png",
            "StormX.Pierce == 'ring'", "images/StormSex/Storm_Sex_Pierce_Pussy_RingC.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #pantyhose layer
            "StormX.Panties and StormX.PantiesDown", Null(),
            #If she has panties down. . .
            "StormX.Hose == 'pantyhose'", Recolor("Storm", "Hose", "images/StormSex/Storm_Sex_Hose_Pantyhose_FJ.png"),
            "StormX.Hose == 'ripped pantyhose'", Recolor("Storm", "Hose", "images/StormSex/Storm_Sex_Hose_Pantyhose_FJHoled.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs Layer
            "StormX.Legs == 'skirt'", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_Skirt_FJ.png"),
            "StormX.Upskirt",ConditionSwitch(
                    #If she has panties down. . .
                    "StormX.Legs == 'pants'", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_Pants_FJ_Down.png"),
                    "StormX.Legs == 'yoga pants'", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_YogaPants_FJ_Down.png"),
                    "True", Null(),
                    ),
            #If she has panties down. . .
            "StormX.Legs == 'pants' and StormX.Wet > 1", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_Pants_FJ_Wet.png"),
            "StormX.Legs == 'pants'", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_Pants_FJ.png"),
            "StormX.Legs == 'yoga pants' and StormX.Wet > 1", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_YogaPants_FJ_Wet.png"),
            "StormX.Legs == 'yoga pants'", Recolor("Storm", "Legs", "images/StormSex/Storm_Sex_Legs_YogaPants_FJ.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Piercings
#            "Player.Sprite", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),
            "not StormX.Legs", Null(),
            "StormX.Legs and StormX.Legs != 'skirt' and StormX.Upskirt", Null(),
                #if she has panties, but they are down, or pantyhose, or Legs that are not a skirt and are not down, skip these. . .
            "StormX.Pierce == 'barbell'", "images/StormSex/Storm_Sex_Pierce_Pussy_BarbellC.png",
            "StormX.Pierce == 'ring'", "images/StormSex/Storm_Sex_Pierce_Pussy_RingC.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy'", "Storm_Sex_Lick_Pussy",
            "Trigger == 'lick ass'", "Storm_Sex_Lick_Ass",
            "True", Null()
            ),
        (0,0), ConditionSwitch(
            #pussy fondling animation
            "Player.Sprite", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Storm_Sex_Fondle_Pussy",
            "StormX.Offhand == 'fondle pussy' and StormX.Lust > 60", At("StormFingerHand", GirlFingerPussyX()),
            "StormX.Offhand == 'fondle pussy'", At("StormMastHand", GirlGropePussyX()),
            "True", Null()
            ),
        (0,0), ConditionSwitch(
            #Footjob overlay
            "True", AlphaMask("Storm_Sex_Feet", "images/StormSex/Storm_Sex_Mask_Foot2.png"),
#            "ShowFeet", AlphaMask("Storm_Sex_Feet", "images/StormSex/Storm_Sex_Mask_Foot.png"),
            "True", Null(),
            ),
        )
# End Storm Scissor Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Storm Sex Pose Pussy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Storm_SC_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/StormSex/Storm_Sex_Pussy_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and Speed", "Storm_Sex_Heading_Pussy",
                "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'out')", "images/StormSex/Storm_Sex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/StormSex/Storm_Sex_Pussy_Open.png",
                "StormX.Offhand == 'fondle pussy' and StormX.Lust > 60", "images/StormSex/Storm_Sex_Pussy_Open.png",
                "True", "images/StormSex/Storm_Sex_Pussy_Closed.png",
                )
    contains:
            # pubes
            ConditionSwitch(
                "not StormX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Fucking.png"),
                "Player.Sprite and Player.Cock == 'in' and Speed and ShowFeet", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Fucking_FJ.png"),
                "Player.Sprite and Player.Cock == 'in' and Speed", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Fucking.png"),
                "Player.Sprite and Player.Cock == 'in' and ShowFeet", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Open_FJ.png"),
                "Player.Sprite and Player.Cock == 'in'", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Open.png"),
                "Trigger == 'lick pussy' and ShowFeet", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Open_FJ.png"),
                "Trigger == 'lick pussy'", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Open.png"),
                "StormX.Offhand == 'fondle pussy' and StormX.Lust > 60", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Open.png"),
                "ShowFeet", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Closed_FJ.png"),
                "True", Recolor("Storm", "Pubes", "images/StormSex/Storm_Sex_Pubes_Closed.png"),
                )
    contains:
            #Piercings
            ConditionSwitch(
                "StormX.Pierce == 'barbell' and Player.Sprite and Player.Cock == 'in' and Speed", "images/StormSex/Storm_Sex_Pierce_Pussy_BarbellF.png",
                "StormX.Pierce == 'ring' and Player.Sprite and Player.Cock == 'in' and Speed", "images/StormSex/Storm_Sex_Pierce_Pussy_RingF.png",
                "StormX.Pierce == 'barbell'", "images/StormSex/Storm_Sex_Pierce_Pussy_Barbell.png",
                "StormX.Pierce == 'ring'", "images/StormSex/Storm_Sex_Pierce_Pussy_Ring.png",
                "True", Null(),
                )

    #End Storm Pussy composite
image Storm_SC_Anim_0:
        #this is the animation for Storm's lower body during Scissoring, Speed 0 (static)
        contains:
            subpixel True
            "Storm_Sex_Body"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 20
            pos (70,50) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                ease 2 pos (70,60)
                pause .5
                ease 2 pos (70,50)
                pause .5
                repeat
        contains:
            subpixel True
            "Storm_Sex_Tits"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 20
            pos (70,50) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
#                pause .1
                easeout 2 pos (72,65)
                easein .5 pos (70,60)
                pause .2
                ease 2 pos (70,50)
                pause .3
                repeat
        contains:
            subpixel True
            "Storm_SC_Legs"
            anchor (560,580)#(560,420)
            offset (560,580) #(560,580)
            transform_anchor True
            zoom 1.35
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
##            "Storm_Sex_Feet"
#            ConditionSwitch(
#                #Shows different lower body motion depending on events
#                "ShowFeet", "Storm_Sex_Feet",
#                "True", AlphaMask("Storm_Sex_Feet","images/StormSex/Storm_Sex_Mask_Foot2.png")
#                )
#            anchor (560,580)#(560,420)
#            offset (560,580) #(845,340)    #(840,390)
#            transform_anchor True
#            zoom 1.35
#            rotate 35
#            pos (0,0) #X less is left, Y less is up
#            parallel:
#                pause .5
#                ease 2 rotate 30
#                pause .5
#                ease 2 rotate 35
#                repeat
        #end animation for Storm's lower body during Scissoring, Speed 0 (static) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Storm_SC_Anim_1:
        #this is the animation for Storm's lower body during Scissoring, Speed 1 (slow)
        contains:
            subpixel True
            "Storm_Sex_Body"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 20
            pos (70,80) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                ease 1 pos (70,90)
                pause .5
                ease 1 pos (70,80)
                pause .5
                repeat
        contains:
            subpixel True
            "Storm_Sex_Tits"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 20
            pos (70,80) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                easeout 1 pos (70,98)
                easein .5 pos (70,90)
                pause .3
                ease 1 pos (70,80)
                pause .2
                repeat
        contains:
            subpixel True
            "Storm_SC_Legs"
            anchor (560,580)#(560,420)
            offset (560,580) #(560,580)
            transform_anchor True
            zoom 1.35
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
#        contains:
#            subpixel True
##            "Storm_Sex_Feet"
#            ConditionSwitch(
#                #Shows different lower body motion depending on events
#                "ShowFeet", "Storm_Sex_Feet",
#                "True", AlphaMask("Storm_Sex_Feet","images/StormSex/Storm_Sex_Mask_Foot2.png")
#                )
#            anchor (560,580)#(560,420)
#            offset (560,580) #(845,340)    #(840,390)
#            transform_anchor True
#            zoom 1.35
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
        #End animation for Storm's lower body during Scissoring, Speed 1 (slow) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Storm_SC_Anim_2:
        #this is the animation for Storm's lower body during Scissoring, Speed 2 (fast)
        contains:
            subpixel True
            "Storm_Sex_Body"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 20
            pos (60,80) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                pause .1
                ease .5 pos (60,90)
                ease .5 pos (60,80)
                repeat
        contains:
            subpixel True
            "Storm_Sex_Tits"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.2
            rotate 20
            pos (60,80) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                pause .1
                ease .6 pos (60,100)
                ease .4 pos (60,80)
                repeat
        contains:
            subpixel True
            "Storm_SC_Legs"
            anchor (560,580)#(560,420)
            offset (560,580) #(560,580)
            transform_anchor True
            zoom 1.35
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
#        contains:
#            subpixel True
##            "Storm_Sex_Feet"
#            ConditionSwitch(
#                #Shows different lower body motion depending on events
#                "ShowFeet", "Storm_Sex_Feet",
#                "True", AlphaMask("Storm_Sex_Feet","images/StormSex/Storm_Sex_Mask_Foot2.png")
#                )
#            anchor (560,580)#(560,420)
#            offset (560,580) #(845,340)    #(840,390)
#            transform_anchor True
#            zoom 1.35
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
        #End animation for Storm's lower body during Scissoring, Speed 2 (fast) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     SC Launch/Reset
label Storm_SC_Launch(Line = Trigger):
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    return
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary

    $ Trigger = Line

    if renpy.showing("Storm_SC_Sprite"):
        return
    $ Speed = 0
    call Girl_Hide(StormX,1) #call Rogue_Hide
    show Storm_SC_Sprite zorder 150
    with dissolve
    return

label Storm_SC_Reset:
    if not renpy.showing("Storm_SC_Sprite"):
        return
    $ StormX.ArmPose = 2
    hide Storm_SC_Sprite
    call Girl_Hide(StormX) #call Rogue_Hide
#    call Set_The_Scene(Dress = 0)
    show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) zorder StormX.Layer:
        alpha 1 zoom 1 offset (0,0) anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return
# End Storm Scissor Pose content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

# Storm Misc Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#label Storm_Kissing_Launch(T = Trigger,Set=1):
#    call Storm_Hide
#    $ Trigger = T
#    $ StormX.Pose = "kiss" if Set else StormX.Pose
#    show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) zorder StormX.Layer
#    show Storm_Sprite at SpriteLoc(StageCenter) zorder 150:
#        ease 0.5 offset (0,0) zoom 2 alpha 1
#    return

#label Storm_Kissing_Smooch:
#    $ StormX.FaceChange("kiss")
#    show Storm_Sprite at SpriteLoc(StageCenter) zorder StormX.Layer:
#        ease 0.5 xpos StageCenter offset (0,0) zoom 2 alpha 1
#        pause 1
#        ease 0.5 xpos StormX.SpriteLoc zoom 1
#    show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) zorder StormX.Layer:
#        zoom 1
#    $ StormX.FaceChange("sexy")
#    return

#label Storm_Breasts_Launch(T = Trigger,Set=1):
#    call Storm_Hide
#    $ Trigger = T
#    $ StormX.Pose = "breasts" if Set else StormX.Pose
#    show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) zorder StormX.Layer:
##        ease 0.5 offset (-100,-200) zoom 2
#        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
#    return

#label Storm_Middle_Launch(T = Trigger,Set=1):
#    call Storm_Hide
#    $ Trigger = T
#    $ StormX.Pose = "mid" if Set else StormX.Pose
#    show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) zorder StormX.Layer:
##        ease 0.5 offset (-100,-200) zoom 2
#        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
#    return

#label Storm_Pussy_Launch(T = Trigger,Set=1):
#    call Storm_Hide
#    $ Trigger = T
#    $ StormX.Pose = "pussy" if Set else StormX.Pose
#    show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) zorder StormX.Layer:
#        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
#    return

#label Storm_Pos_Reset(T = 0,Set=0):
#    if StormX.Loc != bg_current:
#            return
#    call Storm_Hide
#    show Storm_Sprite at SpriteLoc(StormX.SpriteLoc) zorder StormX.Layer:
#            ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
#    show Storm_Sprite zorder StormX.Layer:
#            offset (0,0)
#            anchor (0.5, 0.0)
#            zoom 1
#            xzoom 1
#            yzoom 1
#            alpha 1
#            pos (StormX.SpriteLoc,50)
#    $ StormX.Pose = "full" if Set else 0
#    $ Trigger = T
#    return

#label Storm_Hide(Sprite=0):
#        #call Storm_Sex_Reset
#        hide Storm_SexSprite
#        hide Storm_Doggy_Animation
#        hide Storm_HJ_Animation
#        hide Storm_BJ_Animation
#        hide Storm_TJ_Animation
#        hide Storm_Finger_Animation
#        hide Storm_CUN_Animation
#        if Sprite:
#                hide Storm_Sprite
#        return



# Interface items //////////////////////////////////////////////////////////////////////////////

image Storm_At_Desk:
    contains:
        subpixel True
        "Storm_Sprite"
        zoom 0.29
        pos (450,190) #(500,200)

image Storm_At_Podium:
    contains:
        subpixel True
        "Storm_Sprite"
        zoom 0.29
        pos (670,180) #(500,200)

image Storm_Behind_Podium:
    contains:
        subpixel True
        "Storm_Sprite"
        zoom 0.29
        pos (640,180) #(500,200)
        block:
            subpixel True
            ease .5 ypos 183
            ease .5 ypos 180
            pause .5
            repeat


image GropeRightBreast_Storm:
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (95,340)#(185,340)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block:
            ease 1 rotate -30 #-30
            ease 1 rotate -60 #-60
            repeat

image GropeLeftBreast_Storm:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65#.7
        pos (220,350)#(290,340)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 60
        block:
            ease 1 rotate 30
            ease 1 rotate 60
            repeat

image LickRightBreast_Storm:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5
        xzoom -0.45
        pos (80,335)#(175,325)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (55,310)#(150,300)
            pause .5
            ease 1.5 rotate 30 pos (80,335)#(175,325
            repeat

#image GropeBreast:
image LickLeftBreast_Storm:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5
        xzoom -0.45
        pos (205,350)#(95,355)#(105,375)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (185,330)#(85,345)  top
            pause .5
            ease 1.5 rotate 30 pos (205,350)#(105,375) bottom
            repeat

image GropeThigh_Storm:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (145,630)#(115,690)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        block:
            pause .5
            ease 1 rotate 110 pos (145,700) #(155,700)
            ease 1 rotate 100 pos (145,630)
            repeat

image GropePussy_Storm:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (145,560)#(245,560)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease .5 rotate 190 pos (145,545)#(245,545)
                ease .75 rotate 170 pos (145,560)#(245,560)
            choice:
                ease .5 rotate 190 pos (145,545)#(245,545)
                pause .25
                ease 1 rotate 170 pos (145,560)#(245,560)
            repeat

image FingerPussy_Storm:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.65
        pos (165,640)#(265,640)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (175,615)#(275,615)
                pause .5
                ease 1 rotate 50 pos (165,640)#(265,640)
            choice:
                ease .5 rotate 40 pos (175,615)
                pause .5
                ease 1.75 rotate 50 pos (165,640)
            choice:
                ease 2 rotate 40 pos (175,615)
                pause .5
                ease 1 rotate 50 pos (165,640)
            choice:
                ease .25 rotate 40 pos (175,615)
                ease .25 rotate 50 pos (165,640)
                ease .25 rotate 40 pos (175,615)
                ease .25 rotate 50 pos (165,640)
            repeat

image Lickpussy_Storm:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (175,595)#(275,595)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout .5 rotate -50 pos (165,575)#(145,630) #(210,605)
            linear .5 rotate -60 pos (155,585)#(135,640) #(200,615)
            easein 1 rotate 10 pos (175,595)#(155,650) #(230,625)
            repeat

image VibratorRightBreast_Storm:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (75,320)#(165,310)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease .9 rotate 35 ypos 310
            pause .25
            ease .7 rotate 55 ypos 320
            pause .25
            repeat

image VibratorLeftBreast_Storm:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (200,350)#(270,310)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1.1 rotate 35 ypos 340
            pause .25
            ease .9 rotate 55 ypos 350
            pause .25
            repeat

image VibratorPussy_Storm:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (170,580)#(240,665)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 70
        block:
            ease 1 rotate 35 xpos 160 #230
            pause .25
            ease 1 rotate 70 xpos 170 #240
            pause .25
            repeat

image VibratorAnal_Storm:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (195,570)#(270,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 10
        block:
            ease 1 rotate 0 xpos 190
            pause .25
            ease 1 rotate 10 xpos 200
            pause .25
            repeat

image VibratorPussyInsert_Storm:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_Storm:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0



#Lesbian action animations.
image GirlGropeBothBreast_Storm:
    contains:
        "GirlGropeLeftBreast_Storm"
    contains:
        "GirlGropeRightBreast_Storm"

image GirlGropeLeftBreast_Storm:
    contains:
        subpixel True
        "images/UI_GirlHandS.png"
        zoom .6
        pos (220,340)#(190,340)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate 10 pos (220,350)#(220,380)
            ease 1 rotate -10 pos (220,340)#(220,370)
            repeat
#(185,340)(290,340)
image GirlGropeRightBreast_Storm:
    contains:
        subpixel True
        "images/UI_GirlHandS.png"
        yzoom 0.6
        xzoom -0.6
        pos (70,340)#(90,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block:
            ease 1 rotate -40 pos (70,350)#(90,380)
            ease 1 rotate -10 pos (70,340)#(90,370)
            repeat

image GirlGropeThigh_Storm:
    contains:
        subpixel True
        "images/UI_GirlHandS.png"
        zoom .6
        anchor (0.5,0.5)
        pos (0,0)#(240,540)#(210,730)
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

#image GirlGropePussy_StormSelf:
#    contains:
#        "images/UI_GirlHandS.png"
#        anchor (0.5,0.5)
#        rotate -40
##        yzoom -1
#        pos (100,530)#200,510

image GirlGropePussy_StormSelf:
        "images/UI_GirlHandS.png"
        offset (-40,-20)#(150,550)
        anchor (0.5,0.5)
        rotate 320

transform  GirlGropeRightBreast_Storm():
        subpixel True
        yzoom 0.6
        xzoom -0.6
        offset (-30,240)#(70,340)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block:
            ease 1 rotate -40 yoffset 250#(90,380)
            ease 1 rotate -10 yoffset 240#(90,370)
            repeat

transform  GirlGropeLeftBreast_Storm():
        subpixel True
        zoom .6
        offset (120,240)#(220,340
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate 10 yoffset 250#(220,380)
            ease 1 rotate -10 yoffset 240#(220,370)
            repeat

transform GirlGropePussy_Storm1():
        subpixel True
        zoom 0.6
        offset (60,470)#(150,550)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 yoffset 465
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 yoffset 465
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 yoffset 465
                ease .75 rotate 200 yoffset 470
                ease .5 rotate 205 yoffset 465
                ease .75 rotate 200 yoffset 470
            choice: #Fast stroke
                ease .3 rotate 205 yoffset 465
                ease .3 rotate 200 yoffset 475
                ease .3 rotate 205 yoffset 465
                ease .3 rotate 200 yoffset 475
            repeat

image GirlGropePussy_Storm:
    contains:
        subpixel True
#        "UI_PartnerHand"
        "images/UI_GirlFingerS.png"
        zoom 0.6
        pos (150,550)#((240,540)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (150,545)#(130,590)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 pos (150,545)#(130,590)#-10+20
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (150,545)#(130,590)
                ease .75 rotate 200 pos (150,550)#(130,595)
                ease .5 rotate 205 pos (150,545)
                ease .75 rotate 200 pos (150,550)
            choice: #Fast stroke
                ease .3 rotate 205 pos (150,545)#(130,590)
                ease .3 rotate 200 pos (150,555)#(130,600)
                ease .3 rotate 205 pos (150,545)
                ease .3 rotate 200 pos (150,555)
            repeat

image GirlFingerPussy_Storm:
    contains:
        subpixel True
        "images/UI_GirlFingerS.png"
        zoom .6
        pos (165,550)#(140,605)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (165,555)#(140,610)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 pos (165,555)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 ypos 565#620
                ease .75 rotate 200 ypos 570#625
                ease .5 rotate 205 ypos 565
                ease .75 rotate 200 ypos 570
            choice: #Fast stroke
                ease .3 rotate 205 ypos 565#620
                ease .3 rotate 200 ypos 575#630
                ease .3 rotate 205 ypos 565
                ease .3 rotate 200 ypos 575
            repeat

image StormMastHand:
        "images/UI_GirlHand_Storm.png"
        zoom 0.9
        rotate 210
        offset (325,220)

image StormFingerHand:
        "images/UI_GirlFingerS.png"
        zoom 0.9
        rotate 220
        offset (355,310)
