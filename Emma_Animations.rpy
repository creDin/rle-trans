# Basic character Sprites
image Emma_Sprite:
    LiveComposite(
        (402,965),
        (0,0), "images/EmmaSprite/EmmaSprite_Shadow.png",
#        (55,0), ConditionSwitch(                                                                         #hair back temporary
#            "not EmmaX.Hair", Null(),
#            "EmmaX.Hair == 'wet' or EmmaX.Water", Recolor("Emma", "Hair", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_HairBackWet.png"),
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #cape layer
            "EmmaX.Uptop or EmmaX.Over == 'jacket' or EmmaX.Chest != 'corset'", Null(),
            "EmmaX.ArmPose == 2", Recolor("Emma", "Chest", "images/EmmaSprite/EmmaSprite_Cape2.png"),
            "True", Recolor("Emma", "Chest", "images/EmmaSprite/EmmaSprite_Cape1.png"),
            ),
        (0,0), ConditionSwitch(
            #Dress back layer
            "EmmaX.Legs == 'dress' and EmmaX.Upskirt", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_Dress_Back.png"),
            "EmmaX.Legs == 'dress'", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_Dress.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Overshirt back layer
            "EmmaX.Over == 'nighty'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Nighty_Under.png"),
            "EmmaX.Over and EmmaX.Uptop and EmmaX.Over == 'jacket'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Jacket_Back.png"),
            "True", Null(),
            ),
        (55,0), "EmmaSprite_HairBack",
#        ConditionSwitch(
#            #hair back
#            "EmmaX.Hair == 'short'", "images/EmmaSprite/EmmaSprite_Head_Hair_Short_Back.png",
#            "EmmaX.Hair == 'wet' or EmmaX.Water", Recolor("Emma", "Hair", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_HairbackWet.png"), #or EmmaX.Hair == 'hat wet'
#            "not Player.Male and 'facial' in EmmaX.Spunk",Recolor("Emma", "Hair", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_HairbackWet.png"),
#            "EmmaX.Hair", Recolor("Emma", "Hair", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Hairback.png"),
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #nighty underlayer
#            "EmmaX.Over == 'nighty'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Nighty_Under.png"),
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #panties down back
            "not EmmaX.Panties or not EmmaX.PantiesDown or (EmmaX.Legs == 'pants' and not EmmaX.Upskirt)", Null(),
            "EmmaX.Panties == 'sports panties'", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties_Sports_DownBack.png"),
            "EmmaX.Panties == 'bikini bottoms'", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties_Bikini_DownBack.png"),
            "True", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties_DownBack.png"),
            ),
        (0,0), ConditionSwitch(
            #legs/torso
            "EmmaX.ArmPose == 2", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Legs_Arms2.png",
            "True", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Legs_Arms1.png", #if EmmaX.Arms == 1
            ),

        (215,540), ConditionSwitch(
            #Personal Wetness
            "not EmmaX.Wet", Null(),
            "EmmaX.Legs == 'pants' and not EmmaX.Upskirt", Null(),
            "EmmaX.Panties and not EmmaX.PantiesDown and EmmaX.Wet <= 1", Null(),
            "EmmaX.Wet == 1", ConditionSwitch( #Wet = 1
                    "EmmaX.Panties and EmmaX.PantiesDown", AlphaMask("Wet_Drip","Emma_Drip_MaskP"),
                    "EmmaX.Legs == 'pants'", AlphaMask("Wet_Drip","Emma_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip","Emma_Drip_Mask"), #only plays if nothing is in the way
                    ),
            "True", ConditionSwitch( #Wet = 2+
                    "EmmaX.Panties and EmmaX.PantiesDown", AlphaMask("Wet_Drip2","Emma_Drip_MaskP"), #"Wet_Drip2",#
                    "EmmaX.Legs == 'pants'", AlphaMask("Wet_Drip2","Emma_Drip_MaskP"),
                    "EmmaX.Panties", AlphaMask("Wet_Drip","Emma_Drip_Mask"), #"Wet_Drip2",#
                    "True", AlphaMask("Wet_Drip2","Emma_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (0,0), ConditionSwitch(
            #Personal Wetness
            "not EmmaX.Wet", Null(),
            "EmmaX.Legs and EmmaX.Wet <= 1", Null(),
            "EmmaX.Legs", "images/EmmaSprite/EmmaSprite_Wet.png",
            "EmmaX.Wet == 1", "images/EmmaSprite/EmmaSprite_Wet.png",
            "True", "images/EmmaSprite/EmmaSprite_Wet.png",       #EmmaX.Wet >1
            ),

        (215,540), ConditionSwitch(
            #Spunk nethers
            "('in' not in EmmaX.Spunk and 'anal' not in EmmaX.Spunk) or not Player.Male", Null(),
            "EmmaX.Legs == 'pants' and not EmmaX.Upskirt", Null(),
            "True", ConditionSwitch( #Wet = 2+
                    "EmmaX.Panties and EmmaX.PantiesDown", AlphaMask("Spunk_Drip","Emma_Drip_MaskP"), #"Wet_Drip2",#
                    "EmmaX.Legs == 'pants'", AlphaMask("Spunk_Drip","Emma_Drip_MaskP"),
                    "True", AlphaMask("Spunk_Drip","Emma_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (0,0), ConditionSwitch(
            #pubes
            "EmmaX.Pubes", Recolor("Emma", "Pubes", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Pubes.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #nude lower piercings
            "not EmmaX.Pierce", Null(),
            "EmmaX.Panties and not EmmaX.PantiesDown", Null(),
            "EmmaX.Legs != 'skirt' and EmmaX.Legs and not EmmaX.Upskirt", Null(), #skirt if wearing a skirt
            "EmmaX.Pierce == 'barbell'", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_Barbell.png",
            "EmmaX.Pierce == 'ring'", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_Ring.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Water effect
            "EmmaX.Water", "images/EmmaSprite/EmmaSprite_Water_Legs.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # stockings
            "renpy.showing('Emma_FJ_Animation')", Null(),
            "EmmaX.Hose == 'stockings'", Recolor("Emma", "Hose", "images/EmmaSprite/EmmaSprite_Stockings.png"),
            "EmmaX.Hose == 'stockings and garterbelt'", Recolor("Emma", "Hose", "images/EmmaSprite/EmmaSprite_StockingsGarter.png"),
            "EmmaX.Hose == 'garterbelt'", Recolor("Emma", "Hose", "images/EmmaSprite/EmmaSprite_Garter.png"),
            "True", Null(),
            ),
        (-20,0), ConditionSwitch(
            #boots
            "EmmaX.Boots != 'thigh boots'", Null(),
            "EmmaX.PantiesDown", Recolor("Emma", "Boots", "images/EmmaSprite/EmmaSprite_Boots.png"),
            "EmmaX.Legs == 'dress'", Recolor("Emma", "Boots", "images/EmmaSprite/EmmaSprite_Boots.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #panties down if not wearing pants
            "not EmmaX.Panties or not EmmaX.PantiesDown or (EmmaX.Legs == 'pants' and not EmmaX.Upskirt)", Null(),
            "EmmaX.Panties == 'sports panties' and EmmaX.Wet", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties_Sports_DownWet.png"),
            "EmmaX.Panties == 'sports panties'", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties_Sports_Down.png"),
            "EmmaX.Panties == 'lace panties' and EmmaX.Wet", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties_Lace_DownWet.png"),
            "EmmaX.Panties == 'lace panties'", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties_Lace_Down.png"),
            "EmmaX.Panties == 'bikini bottoms'", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties_Bikini_Down.png"),
#            "EmmaX.Wet", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties_DownWet.png"),
            "True", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties_Down.png"),
            ),
        (0,0), ConditionSwitch(
            #panties up
            "EmmaX.PantiesDown or not EmmaX.Panties", Null(),
#            "EmmaX.Panties == 'sports panties' and EmmaX.Wet", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties_Sports_Wet.png"),
            "EmmaX.Panties == 'sports panties'", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties_Sports.png"),
            "EmmaX.Panties == 'lace panties' and EmmaX.Wet", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties_Lace_Wet.png"),
            "EmmaX.Panties == 'lace panties'", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties_Lace.png"),
            "EmmaX.Panties == 'bikini bottoms'", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties_Bikini.png"),
#            "EmmaX.Wet", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties_Wet.png"), #readd when sprite works
            "True", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties.png"),
            ),
        (0,0), ConditionSwitch(
            # pantyhose
            "renpy.showing('Emma_FJ_Animation')", Null(),
            "EmmaX.Hose == 'pantyhose' and not EmmaX.PantiesDown", Recolor("Emma", "Hose", "images/EmmaSprite/EmmaSprite_Hose.png"),
            "EmmaX.Hose == 'ripped pantyhose' and not EmmaX.PantiesDown", Recolor("Emma", "Hose", "images/EmmaSprite/EmmaSprite_HoseHoled.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy spunk
            "EmmaX.Legs and EmmaX.Legs != 'skirt' and not EmmaX.Upskirt", Null(),
            "('in' in EmmaX.Spunk or 'anal' in EmmaX.Spunk) and Player.Male", "images/EmmaSprite/EmmaSprite_Spunk_Pussy.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pants
            "not EmmaX.Legs", Null(),
            "EmmaX.Upskirt", ConditionSwitch(
                        #if the skirt's up or pants down
                        "EmmaX.Legs == 'dress'", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_Dress_Up.png"),
                        "EmmaX.Legs == 'skirt'", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_SkirtUp.png"),
                        "EmmaX.Boots == 'thigh boots'", Null(),
                        "EmmaX.Legs == 'pants'", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_Pants_Down.png"),
                        "EmmaX.Legs == 'yoga pants'", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_Pants_Yoga_Down.png"),
                        # Modification mode
                        "EmmaX.Legs == 'bottom harem'", "images/EmmaSprite/modification/Emmas_sprite_legs_harem_bottom_down.png",
                        # -----------------
                        "True", Null(),
                        ),
            "True", ConditionSwitch(
                    #if it's the ring pericings
                    "EmmaX.Legs == 'dress' and renpy.showing('Emma_FJ_Animation')",Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_Dress_Up.png"),
                    "EmmaX.Legs == 'dress'", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_Dress.png"),
                    "EmmaX.Legs == 'skirt'", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_Skirt.png"),
                    "EmmaX.Wet", ConditionSwitch(
                        #if she's not wet
                        "EmmaX.Legs == 'pants'", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_Pants.png"),
                        "EmmaX.Legs == 'yoga pants'", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_Pants_YogaWet.png"),
                        # Modification mode
                        "EmmaX.Legs == 'bottom harem'", "images/EmmaSprite/modification/Emmas_sprite_legs_harem_bottom_wet.png",
                        # -----------------
                        "True", Null(),
                        ),
                    "True", ConditionSwitch(
                        #if she's wet
                        "EmmaX.Legs == 'pants'", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_Pants.png"),
                        "EmmaX.Legs == 'yoga pants'", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_Pants_Yoga.png"),
                        # Modification mode
                        "EmmaX.Legs == 'bottom harem'", "images/EmmaSprite/modification/Emmas_sprite_legs_harem_bottom.png",
                        # -----------------
                        "True", Null(),
                        ),
                    ),
            ),
        (-20,0), ConditionSwitch(
            #boots
            "EmmaX.Boots == 'shoes'", Recolor("Emma", "Boots", "images/EmmaSprite/EmmaSprite_Boots_Shoes.png"),  #only shows if panties are up and there isn't a dress over them
            "EmmaX.PantiesDown or (EmmaX.Legs == 'dress' and not EmmaX.Upskirt)", Null(),
            "EmmaX.Boots == 'thigh boots'", Recolor("Emma", "Boots", "images/EmmaSprite/EmmaSprite_Boots.png"),  #only shows if panties are up and there isn't a dress over them
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #clothed lower piercings
            "EmmaX.Legs == 'skirt'", Null(),
            "EmmaX.Legs == 'dress'", Null(),
            "EmmaX.Pierce == 'barbell'", ConditionSwitch(
                    #if it's the barbell pericings
                    "EmmaX.Legs and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_BarOut.png",
                    "EmmaX.Panties and not EmmaX.PantiesDown", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_BarOut.png",
                    "True", Null(),
                    ),
            "EmmaX.Pierce == 'ring'", ConditionSwitch(
                    #if it's the ring pericings
                    "EmmaX.Legs and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_RingOut.png",
                    "EmmaX.Panties and not EmmaX.PantiesDown", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_RingOut.png",
                    "True", Null(),
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Chest underlayer
            "EmmaX.Chest == 'sports bra' and not EmmaX.Uptop", Recolor("Emma", "Chest", "images/EmmaSprite/EmmaSprite_Bra_Sports_Under.png"),
            "EmmaX.Chest == 'lace bra'", Recolor("Emma", "Chest", "images/EmmaSprite/EmmaSprite_Bra_Lace_Under.png"),
            "EmmaX.Chest == 'corset'", Recolor("Emma", "Chest", "images/EmmaSprite/EmmaSprite_CorsetUnder.png"),
            "EmmaX.Chest == 'bikini top'", Recolor("Emma", "Chest", "images/EmmaSprite/EmmaSprite_Bra_Bikini_Under.png"),
            # Modification mode
            "EmmaX.Chest == 'top up tits harem'", "images/EmmaSprite/modification/Emma_sprite_chest_tits_up_harem1_top.png",
            "EmmaX.Chest == 'top down tits harem'", "images/EmmaSprite/modification/Emma_sprite_chest_tits_down_harem2_top.png",
            # -----------------
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over underlayer
            "EmmaX.Over == 'dress' and not EmmaX.Upskirt and not renpy.showing('Emma_FJ_Animation')", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Dress_Loincloth.png"), #dangling strip under arms
            "EmmaX.Over == 'nighty'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Nighty_Under.png"),
            "EmmaX.Over == 'towel'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Towel_Under.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #belly spunk
            "'belly' in EmmaX.Spunk and Player.Male", "images/EmmaSprite/EmmaSprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #arms
            "EmmaX.ArmPose == 2", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Arms2.png",         # one hand up
            "True", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Arms1.png", #if EmmaX.Arms == 1   # Crossed
            ),
        (0,0), ConditionSwitch(
            #Water effect on arms
            "not EmmaX.Water", Null(),
            "EmmaX.ArmPose == 1", "images/EmmaSprite/EmmaSprite_Water_Arms1.png",
            "True", "images/EmmaSprite/EmmaSprite_Water_Arms2.png", #if EmmaX.Arms == 1
            ),
        (0,0), ConditionSwitch(
            #gloves
            "not EmmaX.Arms", Null(),
            "EmmaX.ArmPose == 2", Recolor("Emma", "Arms", "images/EmmaSprite/EmmaSprite_Gloves_Arms2.png"),
            "True", Recolor("Emma", "Arms", "images/EmmaSprite/EmmaSprite_Gloves_Arms1.png"), #if EmmaX.Arms == 1
            ),

        (0,0), ConditionSwitch(
            # jacket arms in "up" pose
            "not EmmaX.Uptop or EmmaX.Over != 'jacket'", Null(),
            "EmmaX.ArmPose == 2", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Jacket_2Arm_Up.png"),
            "True", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Jacket_1Arm_Up.png"),
            ),
        (0,0), ConditionSwitch(
            #tits
            "EmmaX.ArmPose == 1", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_TitsUp.png",   # EmmaX.TitsUp = 1
            "EmmaX.Chest in ('corset','lace bra','sports bra','bikini top')", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_TitsUp.png",   # EmmaX.TitsUp = 1
            "True", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_TitsDown.png",   # EmmaX.TitsUp = 0
            ),
        (0,0), ConditionSwitch(
            #nude peircings
            #something about this entry makes all subsequent entries mis-aligned
            "not EmmaX.Pierce", Null(),
            "EmmaX.Pierce == 'barbell'", ConditionSwitch(
                    #if it's the barbell pericings
                    "EmmaX.ArmPose == 1", "images/EmmaSprite/EmmaSprite_Pierce_Up_Barbell.png",
                    "EmmaX.Chest in ('corset','lace bra','sports bra','bikini top')", "images/EmmaSprite/EmmaSprite_Pierce_Up_Barbell.png",
#                    "EmmaX.Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Barbell.png",
#                    "EmmaX.Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Barbell.png",
                    "True", "images/EmmaSprite/EmmaSprite_Pierce_Down_Barbell.png",
                    ),
            "EmmaX.Pierce == 'ring'", ConditionSwitch(
                    #if it's the ring pericings
                    "EmmaX.ArmPose == 1", "images/EmmaSprite/EmmaSprite_Pierce_Up_Ring.png",
                    "EmmaX.Chest in ('corset','lace bra','sports bra','bikini top')", "images/EmmaSprite/EmmaSprite_Pierce_Up_Ring.png",
#                    "EmmaX.Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Ring.png",
#                    "EmmaX.Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_Ring.png",
                    "True", "images/EmmaSprite/EmmaSprite_Pierce_Down_Ring.png",
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #neck
            "EmmaX.Neck == 'choker'", Recolor("Emma", "Neck", "images/EmmaSprite/EmmaSprite_Neck_Choker.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Water effect
            "not EmmaX.Water", Null(),
            "EmmaX.ArmPose == 1 or EmmaX.Chest == 'corset'", "images/EmmaSprite/EmmaSprite_Water_TitsUp.png",
            "True", "images/EmmaSprite/EmmaSprite_Water_TitsDown.png", #if EmmaX.Arms == 1
            ),
        (0,0), ConditionSwitch(
            #Chest layer
            "EmmaX.Uptop and EmmaX.Chest", ConditionSwitch(
                            #if her top is up. . .
                            "EmmaX.Chest == 'sports bra'", Recolor("Emma", "Chest", "images/EmmaSprite/EmmaSprite_Bra_Sports_Up.png"),
                            "EmmaX.Chest == 'lace bra'", Recolor("Emma", "Chest", "images/EmmaSprite/EmmaSprite_Bra_Lace_Up.png"),
                            "EmmaX.Chest == 'bikini top'", Recolor("Emma", "Chest", "images/EmmaSprite/EmmaSprite_Bra_Bikini_Up.png"),
                            "EmmaX.Chest == 'corset'", Recolor("Emma", "Chest", "images/EmmaSprite/EmmaSprite_CorsetTits_Up.png"),
                            # Modification mode
                            "EmmaX.Chest == 'top up tits harem'", "images/EmmaSprite/modification/Emma_sprite_chest_tits_up_harem1_top.png",
                            "EmmaX.Chest == 'top down tits harem'", "images/EmmaSprite/modification/Emma_sprite_chest_tits_down_harem2_top_up.png",
                            # -----------------
                            "True", Null(),
                            ),
            "EmmaX.Chest == 'sports bra'", Recolor("Emma", "Chest", "images/EmmaSprite/EmmaSprite_Bra_Sports.png"),
            "EmmaX.Chest == 'lace bra'", Recolor("Emma", "Chest", "images/EmmaSprite/EmmaSprite_Bra_Lace.png"),
            "EmmaX.Chest == 'bikini top'", Recolor("Emma", "Chest", "images/EmmaSprite/EmmaSprite_Bra_Bikini.png"),
            "EmmaX.Chest == 'corset' and EmmaX.Over", Recolor("Emma", "Chest", "images/EmmaSprite/EmmaSprite_CorsetTitsX.png"),
            "EmmaX.Chest == 'corset'", Recolor("Emma", "Chest", "images/EmmaSprite/EmmaSprite_CorsetTits.png"),
            # Modification mode
            "EmmaX.Chest == 'top up tits harem'", "images/EmmaSprite/modification/Emma_sprite_chest_tits_up_harem1_top.png",
            "EmmaX.Chest == 'top down tits harem'", "images/EmmaSprite/modification/Emma_sprite_chest_tits_down_harem2_top.png",
            # -----------------
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(                                                                         #soap
#            "EmmaX.Water == 3", "images/EmmaSprite/Emma_body_wet3.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #cape layer
            "EmmaX.Uptop or EmmaX.Over == 'jacket' or EmmaX.Chest != 'corset'", Null(),
            "EmmaX.ArmPose == 2", Recolor("Emma", "Chest", "images/EmmaSprite/EmmaSprite_Cape2.png"),
            "True", Recolor("Emma", "Chest", "images/EmmaSprite/EmmaSprite_Cape1.png"),
            ),
        (0,0), ConditionSwitch(
            #Overshirt layer
            "not EmmaX.Over", Null(),
            "EmmaX.ArmPose == 2", ConditionSwitch(
                    #if her arms are down, allowing her breasts to sink
                    "EmmaX.Uptop", ConditionSwitch(
                                    "EmmaX.Chest in ('corset','lace bra','sports bra','bikini top')", ConditionSwitch(
                                            #If she's wearing a supporting bra. . .
                                            "EmmaX.Over == 'dress'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Dress_Top2U_Up.png"),
                                            "EmmaX.Over == 'jacket'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Jacket_2Up_Up.png"),
                                            "EmmaX.Over == 'nighty'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Nighty_Up2_Up.png"),
                                            "True", Null(),
                                            ),
                                    #if she's not wearing a supporting bra. . .
                                    "EmmaX.Over == 'dress'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Dress_Top2D_Up.png"),
                                    "EmmaX.Over == 'jacket'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Jacket_2Down_Up.png"),
                                    "EmmaX.Over == 'nighty'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Nighty_Up2_Up.png"),
                                    "True", Null(),
                                    ),
                    #if not Uptop. . .
                    "EmmaX.Chest in ('corset','lace bra','sports bra','bikini top')", ConditionSwitch(
                            #If she's wearing a supporting bra. . .
                            "EmmaX.Over == 'dress'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Dress_Top2U.png"),
                            "EmmaX.Over == 'jacket'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Jacket_2Up.png"),
                            "EmmaX.Over == 'nighty'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Nighty_2Up.png"),
                            "EmmaX.Over == 'towel'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Towel_Up2.png"),
                            "True", Null(),
                            ),
                    #if she's not wearing a supporting bra. . .
                    "EmmaX.Over == 'dress'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Dress_Top2D.png"),
                    "EmmaX.Over == 'jacket'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Jacket_2Down.png"),
                    "EmmaX.Over == 'nighty'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Nighty_2Down.png"),
                    "EmmaX.Over == 'towel'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Towel_Down2.png"),
                    "True", Null(),
                    ),
            #if her arms are up, preventng her breasts from sinking
            "EmmaX.Uptop", ConditionSwitch(
                            #if her top is up. . .
                            "EmmaX.Over == 'dress'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Dress_Top1_Up.png"),
                            "EmmaX.Over == 'jacket'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Jacket_1Up_Up.png"),
                            "EmmaX.Over == 'nighty'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Nighty_Up1_Up.png"),
                            "True", Null(),
                            ),
            #if her top is not up. . .
            "EmmaX.Over == 'dress'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Dress_Top1.png"),
            "EmmaX.Over == 'jacket'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Jacket_1Up.png"),
            "EmmaX.Over == 'nighty'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Nighty_1Up.png"),
            "EmmaX.Over == 'towel'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Towel_Up1.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                         #clothed peircings
            "not EmmaX.Pierce or EmmaX.Uptop or (not EmmaX.Over and not EmmaX.Chest)", Null(),
            "EmmaX.Pierce == 'barbell'", ConditionSwitch(
                    #if it's the barbell pericings
                    "EmmaX.ArmPose == 1", "images/EmmaSprite/EmmaSprite_Pierce_Up_BarOut.png",
                    "EmmaX.Chest in ('corset','lace bra','sports bra','bikini top')", "images/EmmaSprite/EmmaSprite_Pierce_Up_BarOut.png",
#                    "EmmaX.Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_BarOut.png",
#                    "EmmaX.Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_BarOut.png",
                    "True", "images/EmmaSprite/EmmaSprite_Pierce_Down_BarOut.png",
                    ),
            "EmmaX.Pierce == 'ring'", ConditionSwitch(
                    #if it's the ring pericings
                    "EmmaX.ArmPose == 1", "images/EmmaSprite/EmmaSprite_Pierce_Up_RingOut.png",
                    "EmmaX.Chest in ('corset','lace bra','sports bra','bikini top')", "images/EmmaSprite/EmmaSprite_Pierce_Up_RingOut.png",
#                    "EmmaX.Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_RingOut.png",
#                    "EmmaX.Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Pierce_Up_RingOut.png",
                    "True", "images/EmmaSprite/EmmaSprite_Pierce_Down_RingOut.png",
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast spunk
            "'tits' in EmmaX.Spunk and Player.Male", ConditionSwitch(
                    #if it's the barbell pericings
                    "EmmaX.ArmPose == 1", "images/EmmaSprite/EmmaSprite_Spunk_TitsU.png",
                    "EmmaX.Chest == 'corset'", "images/EmmaSprite/EmmaSprite_Spunk_TitsU.png",
                    "EmmaX.Chest == 'lace bra'", "images/EmmaSprite/EmmaSprite_Spunk_TitsU.png",
                    "EmmaX.Chest == 'sports bra'", "images/EmmaSprite/EmmaSprite_Spunk_TitsU.png",
                    "True", "images/EmmaSprite/EmmaSprite_Spunk_TitsD.png",
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #bundled dress over arms
            "(EmmaX.Legs == 'dress' or EmmaX.Over == 'dress') and EmmaX.Upskirt and EmmaX.ArmPose == 2", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Dress_Over2.png"),         # one hand up
            "(EmmaX.Legs == 'dress' or EmmaX.Over == 'dress') and EmmaX.Upskirt", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Dress_Over1.png"),         # one hand up
            "True", Null(), #if EmmaX.Arms == 1   # Crossed
            ),
        (55,0), "EmmaSprite_Head", #Head
        (0,0), ConditionSwitch(
            #hand spunk
            "EmmaX.ArmPose != 2 or 'hand' not in EmmaX.Spunk or not Player.Male", Null(),
            "'mouth' in EmmaX.Spunk", "images/EmmaSprite/EmmaSprite_Spunk_HandM.png",
            "True", "images/EmmaSprite/EmmaSprite_Spunk_Hand.png",
            ),
#        (0,0), ConditionSwitch(                                                                         #Props
#            "not EmmaX.Held or EmmaX.ArmPose != 2", Null(),
#            "EmmaX.ArmPose == 2 and EmmaX.Held == 'phone'", "images/EmmaSprite/Emma_held_phone.png",
#            "EmmaX.ArmPose == 2 and EmmaX.Held == 'dildo'", "images/EmmaSprite/Emma_held_dildo.png",
#            "EmmaX.ArmPose == 2 and EmmaX.Held == 'vibrator'", "images/EmmaSprite/Emma_held_vibrator.png",
#            "EmmaX.ArmPose == 2 and EmmaX.Held == 'panties'", "images/EmmaSprite/Emma_held_panties.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #UI tool for When Emma is masturbating using EmmaX.Offhand actions while lead
            "Trigger == 'lesbian' or not EmmaX.Offhand",Null(),# or Ch_Focus is not EmmaX", Null(),
            "EmmaX.Offhand == 'fondle pussy' and Trigger != 'sex' and EmmaX.Lust >= 70", "GirlFingerPussy_Emma",
            "EmmaX.Offhand == 'fondle pussy'", "GirlGropePussy_Emma",
            "EmmaX.Offhand == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Emma",    #When zero is working the right breast, fondle left
            "EmmaX.Offhand == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Emma", #When zero is working the left breast, fondle right
            "EmmaX.Offhand == 'fondle breasts'", "GirlGropeRightBreast_Emma",
            "EmmaX.Offhand == 'vibrator breasts'", "VibratorRightBreast_Emma",
            "EmmaX.Offhand == 'vibrator pussy'", "VibratorPussy_Emma",
            "EmmaX.Offhand == 'vibrator pussy insert'", "VibratorPussy_Emma",
            "EmmaX.Offhand == 'vibrator anal'", "VibratorAnal_Emma",
            "EmmaX.Offhand == 'vibrator anal insert'", "VibratorPussy_Emma",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for EmmaX.Offhand(lesbian) actions (ie Kitty's hand on her when Emma is secondary)
            "not Partner or Partner is EmmaX or EmmaX in Nearby", Null(),
            "Partner.Offhand == 'fondle girl pussy' and Trigger != 'sex' and EmmaX.Lust >= 70", "GirlFingerPussy_Emma",
            "Partner.Offhand == 'fondle girl pussy'", "GirlGropePussy_Emma",
            "Partner.Offhand == 'lick girl pussy'", "Lickpussy_Emma",
            "Partner.Offhand == 'suck girl breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Emma",
            "Partner.Offhand == 'suck girl breasts'", "LickRightBreast_Emma",
            "Partner.Offhand == 'fondle girl breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Emma",    #When zero is working the right breast, fondle left
            "Partner.Offhand == 'fondle girl breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Emma", #When zero is working the left breast, fondle right
            "Partner.Offhand == 'fondle girl breasts'", "GirlGropeRightBreast_Emma",
            "Partner.Offhand == 'vibrator girl breasts'", "VibratorRightBreast_Emma",
            "Partner.Offhand == 'vibrator girl pussy'", "VibratorPussy_Emma",
            "Partner.Offhand == 'vibrator girl pussy insert'", "VibratorPussy_Emma",
            "Partner.Offhand == 'vibrator girl anal'", "VibratorAnal_Emma",
            "Partner.Offhand == 'vibrator girl anal insert'", "VibratorPussy_Emma",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for when EmmaX is the partner in the scene, and the lead is working on her
            "not Partner or Partner is not EmmaX", Null(),
            "Ch_Focus.Offhand == 'fondle girl pussy' and Trigger != 'sex' and EmmaX.Lust >= 70", "GirlFingerPussy_Emma",
            "Ch_Focus.Offhand == 'fondle girl pussy'", "GirlGropePussy_Emma",
            "Ch_Focus.Offhand == 'lick girl pussy'", "Lickpussy_Emma",
            "Ch_Focus.Offhand == 'suck girl breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Emma",
            "Ch_Focus.Offhand == 'suck girl breasts'", "LickRightBreast",
            "Ch_Focus.Offhand == 'fondle girl breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Emma",    #When zero is working the right breast, fondle left
            "Ch_Focus.Offhand == 'fondle girl breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Emma", #When zero is working the left breast, fondle right
            "Ch_Focus.Offhand == 'fondle girl breasts'", "GirlGropeRightBreast_Emma",
            "Ch_Focus.Offhand == 'vibrator girl breasts'", "VibratorRightBreast_Emma",
            "Ch_Focus.Offhand == 'vibrator girl pussy'", "VibratorPussy_Emma",
            "Ch_Focus.Offhand == 'vibrator girl pussy insert'", "VibratorPussy_Emma",
            "Ch_Focus.Offhand == 'vibrator girl anal'", "VibratorAnal_Emma",
            "Ch_Focus.Offhand == 'vibrator girl anal insert'", "VibratorPussy_Emma",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger1(primary) actions
            #Emma is primary and a sex trigger is active
            "not Trigger or Ch_Focus is not EmmaX", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast_Emma",
            "Trigger == 'fondle thighs'", "GropeThigh_Emma",
            "Trigger == 'fondle breasts'", "GropeLeftBreast_Emma",
            "Trigger == 'suck breasts'", "LickRightBreast_Emma",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_Emma",
            "Trigger == 'fondle pussy'", "GropePussy_Emma",
            "Trigger == 'lick pussy'", "Lickpussy_Emma",
            "Trigger == 'vibrator pussy'", "VibratorPussy_Emma",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy_Emma",
            "Trigger == 'vibrator anal'", "VibratorAnal_Emma",
            "Trigger == 'vibrator anal insert'", "VibratorPussy_Emma",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus is not EmmaX", Null(),
#            "Trigger == 'fondle breasts' and not EmmaX.Offhand", "GropeRightBreast_Emma",  #"Trigger == 'fondle breasts' and not EmmaX.Offhand",
            #When doing nothing offhand, use both hands on breasts.
            "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast_Emma",
            #When sucking right breast, fondle left
            "Trigger2 == 'fondle breasts'", "GropeLeftBreast_Emma",
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast_Emma",
            #When sucking right breast, vibrator left
            "Trigger2 == Trigger", Null(),
            #When both triggers are the same, do nothing
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast_Emma",
            "Trigger2 == 'suck breasts'", "LickLeftBreast_Emma",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy_Emma",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy_Emma",
            "Trigger2 == 'vibrator anal'", "VibratorAnal_Emma",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy_Emma",
            "Trigger2 == 'fondle pussy'", "GropePussy_Emma",
            "Trigger2 == 'lick pussy'", "Lickpussy_Emma",
            "Trigger2 == 'fondle thighs'", "GropeThigh_Emma",
            "True", Null(),
            ),
        )
    anchor (0.5, 0.0)
    offset (20,-10)#15
    zoom .80#.75

image TempHairBack:
    Recolor("Emma", "Hair", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_HairBackWet.png")
    anchor (0.6, 0.0)
    zoom .5

image EmmaSprite_HairBack:
    LiveComposite(
        (555,673),
        (0,0), ConditionSwitch(
            #hair back
            "EmmaX.Hair == 'short'", "images/EmmaSprite/EmmaSprite_Head_Hair_Short_Back.png",
            "EmmaX.Hair == 'wet' or EmmaX.Water", Recolor("Emma", "Hair", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_HairBackWet.png"), #or EmmaX.Hair == 'hat wet'
            "not Player.Male and 'facial' in EmmaX.Spunk",Recolor("Emma", "Hair", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_HairBackWet.png"),
            "EmmaX.Hair", "images/EmmaSprite/EmmaSprite_Head_HairBack.png",
            "True", Null(),
            ),
        )
    anchor (0.6, 0.0)
    zoom .5

image EmmaSprite_Head:
    LiveComposite(
        (555,673),
        (0,0), ConditionSwitch(
                # Face background plate
                "not EmmaX.Blush", ConditionSwitch(
                    #If no Blush
                    "EmmaX.Hair == 'wet' or EmmaX.Hair == 'short' or EmmaX.Water", ConditionSwitch(
                            #If the hair is wet or EmmaX.Hair == 'hat wet'
                            "EmmaX.Brows == 'angry'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wet_Angry.png",
                            "EmmaX.Brows == 'sad'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wet_Sad.png",
                            "EmmaX.Brows == 'surprised'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wet_Surprised.png",
                            "EmmaX.Brows == 'confused'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wet_Confused.png",
                            "True", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wet_Normal.png", #EmmaX.Brows == 'normal'
                            ),
                    "True", ConditionSwitch(
                            #If the hair is not wet
                            "EmmaX.Brows == 'angry'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wave_Angry.png",
                            "EmmaX.Brows == 'sad'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wave_Sad.png",
                            "EmmaX.Brows == 'surprised'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wave_Surprised.png",
                            "EmmaX.Brows == 'confused'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wave_Confused.png",
                            "True", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wave_Normal.png", #EmmaX.Brows == 'normal'
                            ),
                    ),
                "EmmaX.Blush == 1", ConditionSwitch(
                    #If the first tier blush
                    "EmmaX.Hair == 'wet' or EmmaX.Hair == 'short' or EmmaX.Water", ConditionSwitch(
                            #If the hair is wet or EmmaX.Hair == 'hat wet'
                            "EmmaX.Brows == 'angry'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wet_AngryB1.png",
                            "EmmaX.Brows == 'sad'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wet_SadB1.png",
                            "EmmaX.Brows == 'surprised'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wet_SurprisedB1.png",
                            "EmmaX.Brows == 'confused'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wet_ConfusedB1.png",
                            "True", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wet_NormalB1.png", #EmmaX.Brows == 'normal'
                            ),
                    "True", ConditionSwitch(
                            #If the hair is not wet
                            "EmmaX.Brows == 'angry'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wave_AngryB1.png",
                            "EmmaX.Brows == 'sad'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wave_SadB1.png",
                            "EmmaX.Brows == 'surprised'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wave_SurprisedB1.png",
                            "EmmaX.Brows == 'confused'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wave_ConfusedB1.png",
                            "True", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wave_NormalB1.png", #EmmaX.Brows == 'normal'
                            ),
                    ),
                "True", ConditionSwitch(
                    #else, 2nd tier blush
                    "EmmaX.Hair == 'wet' or EmmaX.Hair == 'short' or EmmaX.Water", ConditionSwitch(
                            #If the hair is wet or EmmaX.Hair == 'hat wet'
                            "EmmaX.Brows == 'angry'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wet_AngryB2.png",
                            "EmmaX.Brows == 'sad'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wet_SadB2.png",
                            "EmmaX.Brows == 'surprised'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wet_SurprisedB2.png",
                            "EmmaX.Brows == 'confused'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wet_ConfusedB2.png",
                            "True", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wet_NormalB2.png", #EmmaX.Brows == 'normal'
                            ),
                    "True", ConditionSwitch(
                            #If the hair is not wet
                            "EmmaX.Brows == 'angry'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wave_AngryB2.png",
                            "EmmaX.Brows == 'sad'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wave_SadB2.png",
                            "EmmaX.Brows == 'surprised'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wave_SurprisedB2.png",
                            "EmmaX.Brows == 'confused'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wave_ConfusedB2.png",
                            "True", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Wave_NormalB2.png", #EmmaX.Brows == 'normal'
                            ),
                    ),
                ),
        (0,0), ConditionSwitch(
            #Mouths
            "EmmaX.Mouth == 'normal'", Recolor("Emma", "Lips", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Mouth_Normal.png"),
            "EmmaX.Mouth == 'lipbite'", Recolor("Emma", "Lips", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Mouth_Lipbite.png"),
            "EmmaX.Mouth == 'sucking' or EmmaX.Mouth == 'open'", Recolor("Emma", "Lips", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Mouth_Surprised.png"),
            "EmmaX.Mouth == 'kiss'", Recolor("Emma", "Lips", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Mouth_Kiss.png"),
            "EmmaX.Mouth == 'sad'", Recolor("Emma", "Lips", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Mouth_Sad.png"),
            "EmmaX.Mouth == 'smile'", Recolor("Emma", "Lips", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Mouth_Smile.png"),
            "EmmaX.Mouth == 'surprised'", Recolor("Emma", "Lips", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Mouth_Surprised.png"),
            "EmmaX.Mouth == 'tongue'", Recolor("Emma", "Lips", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Mouth_Tongue.png"),
            "EmmaX.Mouth == 'grimace'", Recolor("Emma", "Lips", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Mouth_Smile.png"),
            "EmmaX.Mouth == 'smirk'", Recolor("Emma", "Lips", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Mouth_Smirk.png"),
            "True", Recolor("Emma", "Lips", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Mouth_Normal.png"),
            ),

        (0,0), ConditionSwitch(
            #Mouth spunk
            "'chin' in EmmaX.Spunk and not Player.Male", "images/EmmaSprite/EmmaSprite_Head_Wet_Mouth.png",
            "'mouth' not in EmmaX.Spunk or not Player.Male", Null(),
            "EmmaX.Mouth == 'surprised' or EmmaX.Mouth == 'open'", "images/EmmaSprite/EmmaSprite_Head_Spunk_MouthOpen.png",
            "EmmaX.Mouth == 'tongue'", "images/EmmaSprite/EmmaSprite_Head_Spunk_MouthTongue.png",
            "True", "images/EmmaSprite/EmmaSprite_Head_Spunk_Mouth.png",
            ),

        (0,0), "Emma Blink",
            #Eyes
        (0,0), ConditionSwitch(
            #brows
            "EmmaX.Brows == 'normal'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Brows_Normal.png",
            "EmmaX.Brows == 'angry'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Brows_Angry.png",
            "EmmaX.Brows == 'sad'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Brows_Sad.png",
            "EmmaX.Brows == 'surprised'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Brows_Surprised.png",
            "EmmaX.Brows == 'confused'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Brows_Confused.png",
            "True", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Brows_Normal.png",
            ),
        (0,0), ConditionSwitch(
            #facial spunk
            "'facial' in EmmaX.Spunk and Player.Male", "images/EmmaSprite/EmmaSprite_Head_Spunk_Face.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hair
            "EmmaX.Hair == 'short'", "images/EmmaSprite/EmmaSprite_Head_Hair_Short.png",
            "EmmaX.Hair == 'wet' or EmmaX.Water", Recolor("Emma", "Hair", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_HairWet.png"), #or EmmaX.Hair == 'hat wet'
            "not Player.Male and 'facial' in EmmaX.Spunk",Recolor("Emma", "Hair", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_HairWet.png"),
            "True", Recolor("Emma", "Hair", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Hair.png"),
            ),
        (0,0), ConditionSwitch(
            #Hair Water
            "EmmaX.Water", "images/EmmaSprite/EmmaSprite_Head_Water.png",
            "not Player.Male and 'facial' in EmmaX.Spunk","images/EmmaSprite/EmmaSprite_Head_Water.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #hair spunk
            "not 'hair' in EmmaX.Spunk or not Player.Male", Null(),
            "EmmaX.Hair == 'wet' or EmmaX.Hair == 'short' or EmmaX.Water", "images/EmmaSprite/EmmaSprite_Head_Spunk_HairWet.png",  #or EmmaX.Hair == 'hat wet'
            "True", "images/EmmaSprite/EmmaSprite_Head_Spunk_HairWave.png",
            ),
        (-1,0), ConditionSwitch(
            #Hair shade under hat
            "not EmmaX.Hat or EmmaX.Hair == 'short'", Null(),
            "EmmaX.Hair == 'wet' or EmmaX.Water", "images/EmmaSprite/EmmaSprite_Shadow_Wet.png",
            "not Player.Male and 'facial' in EmmaX.Spunk","images/EmmaSprite/EmmaSprite_Shadow_Wet.png",
            "True", "images/EmmaSprite/EmmaSprite_Shadow_Long.png",
#            "True", Null(),
            ),
        # Modification mode
        (0,0), ConditionSwitch(
            "EmmaX.Mask == 'mask harem'", "images/EmmaSprite/modification/Emma_sprite_mask_harem.png",
            "True", Null(),
        ),
        # -----------------
        (-125,-95), ConditionSwitch(
            #Hat
            "EmmaX.Hat", "images/EmmaSprite/EmmaSprite_Hat.png",
#            "EmmaX.Hair == 'hat wet' or EmmaX.Hair == 'hat'", "images/EmmaSprite/EmmaSprite_Hat.png",
            "True", Null(),
            ),
        )
    anchor (0.6, 0.0)
    zoom .5

image Emma Blink:
    ConditionSwitch(
        "EmmaX.Eyes == 'sexy'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Eyes_Sexy.png",
        "EmmaX.Eyes == 'side'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Eyes_Side.png",
        "EmmaX.Eyes == 'leftside'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Leftside.png",
        "EmmaX.Eyes == 'surprised'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Eyes_Surprised.png",
        "EmmaX.Eyes == 'normal'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Eyes_Normal.png",
        "EmmaX.Eyes == 'stunned'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Eyes_Agao.png",
        "EmmaX.Eyes == 'down'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Eyes_Down.png",
        "EmmaX.Eyes == 'closed'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Eyes_Closed.png",
        "EmmaX.Eyes == 'manic'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Eyes_Surprised.png",
        "EmmaX.Eyes == 'squint'", "Emma_Squint",
        "True", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Eyes_Normal.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Eyes_Closed.png"
    .25
    repeat

image Emma_Squint:
    "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Eyes_Sexy.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_Head_Eyes_Squint.png"
    .25
    repeat

image Emma_Drip_Mask:
    #This is the mask for her drip pattern
    contains:
        "images/EmmaSprite/EmmaSprite_WetMask.png"
        offset (-215,-540)

image Emma_Drip_MaskP:
    #This is the mask for her drip pattern in panties down mode
    contains:
        "images/EmmaSprite/EmmaSprite_WetMaskP.png"
        offset (-215,-540)

# End Emma Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Emma Doggy Compositing ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#image Emma_Doggy_Base = LiveComposite(
image Emma_Doggy_Animation:
    LiveComposite(
        #Base body
        (420,750),
        (0,0), ConditionSwitch(
            #Shows different upper body motion depending on events
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Emma_Doggy_Boob_Fuck2",
                    "Speed > 1", "Emma_Doggy_Boob_Fuck",
                    "Speed", "Emma_Doggy_Boob",
                    "True", "Emma_Doggy_Boob",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Emma_Doggy_Boob_Fuck2",
                    "Speed > 1", "Emma_Doggy_Boob_Fuck",
                    "True", "Emma_Doggy_Boob",
                    ),
            "True", "Emma_Doggy_Boob",
            ),
        (0,0), ConditionSwitch(
            #Shows different upper body motion depending on events
            "not Player.Sprite", "Emma_Doggy_Body",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Emma_Doggy_Fuck2_Top",
                    "Speed > 1", "Emma_Doggy_Fuck_Top",
                    "Speed", "Emma_Doggy_Anal_Head_Top",
                    "True", "Emma_Doggy_Body",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Emma_Doggy_Fuck2_Top",
                    "Speed > 1", "Emma_Doggy_Fuck_Top",
                    "True", "Emma_Doggy_Body",
                    ),
            "True", "Emma_Doggy_Body",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events
            "not Player.Sprite", "Emma_Doggy_Ass",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Emma_Doggy_Fuck2_Ass",
                    "Speed > 1", "Emma_Doggy_Fuck_Ass",
                    "Speed", "Emma_Doggy_Anal_Head_Ass",
                    "True", "Emma_Doggy_Ass",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Emma_Doggy_Fuck2_Ass",
                    "Speed > 1", "Emma_Doggy_Fuck_Ass",
                    "True", "Emma_Doggy_Ass",
                    ),
            "True", "Emma_Doggy_Ass",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events
#            "not Player.Sprite", "Emma_Doggy_Shins0",
            "Player.Sprite and Player.Cock == 'foot'", ConditionSwitch(
                    "Speed > 1", "Emma_Doggy_Feet2",
                    "Speed", "Emma_Doggy_Feet1",
                    "True", "Emma_Doggy_Feet0",
                    ),
            "ShowFeet", "Emma_Doggy_Shins0",
            "True", Null(),
            ),
        )
    align (0.6,0.0)
#    yoffset 0
# End Base / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Emma_Doggy_Body:
    LiveComposite(
        #Upper body
        (420,750),
#        (165,0),"Emma_Doggy_Hair_Under", #back of the hair
        #(0,0), "images/JeanDoggy/Jean_Doggy_Breast.png", #Body base
        (-12,0), ConditionSwitch(
            #head
            "EmmaX.Facing", Null(),
            "True", "Emma_Doggy_Head",
            ),
#        (-12,0), "Emma_Doggy_Head",               #Head(165,0)
        (0,0), "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Body.png", #Body base
        (0,0), ConditionSwitch(
            #neck
            "EmmaX.Neck == 'choker'", Recolor("Emma", "Neck", "images/EmmaDoggy/Emma_Doggy_Choker.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #gloves
            "EmmaX.Arms", Recolor("Emma", "Arms", "images/EmmaDoggy/Emma_Doggy_Gloves.png"),
            "True",  Null(),
            ),

        (0,0), ConditionSwitch(
            #bra
            "EmmaX.Over == 'jacket'", Null(),
#            "EmmaX.Uptop", ConditionSwitch(
#                    "EmmaX.Over and EmmaX.Over != 'towel'", Null(),
#                    "EmmaX.Chest == 'cami'", Recolor("Emma", "Chest", "images/EmmaDoggy/Emma_Doggy_Bra_Cami_Up.png"),
#                    "EmmaX.Chest == 'lace bra'", Recolor("Emma", "Chest", "images/EmmaDoggy/Emma_Doggy_Bra_Lace.png"),
#                    "EmmaX.Chest == 'sports bra'", Recolor("Emma", "Chest", "images/EmmaDoggy/Emma_Doggy_Bra_Sport_Up.png"),
#                    "EmmaX.Chest == 'bikini top'", Recolor("Emma", "Chest", "images/EmmaDoggy/Emma_Doggy_Bra_Bikini_Up.png"),
#                    "True", Recolor("Emma", "Chest", "images/EmmaDoggy/Emma_Doggy_Bra.png"),
#                    ),
            "EmmaX.Chest == 'corset'", Recolor("Emma", "Chest", "images/EmmaDoggy/Emma_Doggy_Bra_Corset_Sleave.png"),
            "EmmaX.Chest == 'lace bra'", Recolor("Emma", "Chest", "images/EmmaDoggy/Emma_Doggy_Bra_Corset.png"),
            "EmmaX.Chest == 'sports bra'", Recolor("Emma", "Chest", "images/EmmaDoggy/Emma_Doggy_Bra_Sport.png"),
            "EmmaX.Chest == 'bikini top'", Recolor("Emma", "Chest", "images/EmmaDoggy/Emma_Doggy_Bra_Bikini.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "EmmaX.Water", "images/EmmaDoggy/Emma_Doggy_Wet_Body.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #skirt Under
            "EmmaX.Legs == 'dress'", Recolor("Emma", "Legs", "images/EmmaDoggy/Emma_Doggy_Over_Dress_Under.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Overshirt
            "EmmaX.Over == 'dress'", Recolor("Emma", "Over", "images/EmmaDoggy/Emma_Doggy_Over_Dress.png"),
            "EmmaX.Over == 'jacket'", Recolor("Emma", "Over", "images/EmmaDoggy/Emma_Doggy_Over_Jacket.png"),
            "EmmaX.Over == 'nighty' and EmmaX.Uptop", Recolor("Emma", "Over", "images/EmmaDoggy/Emma_Doggy_Over_Nighty_Down.png"),
            "EmmaX.Over == 'nighty'", Recolor("Emma", "Over", "images/EmmaDoggy/Emma_Doggy_Over_Nighty.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk back Layer
            "'back' in EmmaX.Spunk and Player.Male", "images/EmmaDoggy/Emma_Doggy_Spunk_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast fondling animation
            "Trigger == 'fondle breasts' or Trigger2 == 'fondle breasts'", "Emma_Doggy_GropeBreast",
            "True", Null()
            ),
        (-12,0), ConditionSwitch(
            #hair over
            "EmmaX.Facing", "Emma_Doggy_Head_Fore",
            "True", "Emma_Doggy_Hair_Over",
            ),
#        (-12,0), "Emma_Doggy_Hair_Over",               #Head(165,0)
        #(161,-1), "Jean_Doggy_Head",               #Head
#        (165,0),"Jean_Doggy_Hair_Over", #front of the hair
        )
#    transform_anchor True
#    anchor (225,1400)
    offset (0,0)#(-30,0)#(-190,-40)
#    rotate 20
# End Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Emma_Doggy_Head:
    LiveComposite(
        #Head
        (420,750),
        #(0,0), "images/JeanDoggy/Jean_Doggy_Head.png", #Body base
        (0,0), ConditionSwitch(
            #hair back
                "EmmaX.Hair == 'short'", Null(),
                "EmmaX.Water or EmmaX.Hair == 'wet'", Recolor("Emma", "Hair", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Hair_Wet_Back.png"),   #or EmmaX.Hair == 'hat wet'
                "not Player.Male and 'facial' in EmmaX.Spunk",Recolor("Emma", "Hair", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Hair_Wet_Back.png"),
                "True", Recolor("Emma", "Hair", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Hair_Long_Back.png"),
            ),
        (0,0), ConditionSwitch(
            #Head
#            "EmmaX.Blush > 1", "images/EmmaDoggy/Emma_Doggy_Head_Blush2.png",
            "EmmaX.Blush", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Head_Blush.png",
            "True", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Head.png",
            ),
        (0,0), ConditionSwitch(
            #Mouth
            "EmmaX.Mouth == 'lipbite'", Recolor("Emma", "Lips", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Mouth_Lipbite.png"),
            "EmmaX.Mouth == 'sucking'", Recolor("Emma", "Lips", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Mouth_Tongue.png"),
            "EmmaX.Mouth == 'kiss'", Recolor("Emma", "Lips", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Mouth_Kiss.png"),
            "EmmaX.Mouth == 'sad'", Recolor("Emma", "Lips", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Mouth_Sad.png"),
            "EmmaX.Mouth == 'smile'", Recolor("Emma", "Lips", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Mouth_Smile.png"),
            "EmmaX.Mouth == 'grimace'", Recolor("Emma", "Lips", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Mouth_Smile.png"),
            "EmmaX.Mouth == 'smirk'", Recolor("Emma", "Lips", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Mouth_Smirk.png"),
            "EmmaX.Mouth == 'surprised'", Recolor("Emma", "Lips", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Mouth_Kiss.png"),
            "EmmaX.Mouth == 'sucking'", Recolor("Emma", "Lips", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Mouth_Tongue.png"),
            "EmmaX.Mouth == 'tongue'", Recolor("Emma", "Lips", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Mouth_Tongue.png"),
            "True", Recolor("Emma", "Lips", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Mouth_Normal.png"),
            ),
#        (0,0), ConditionSwitch(
#            #chin spunk
#            "'chin' in EmmaX.Spunk", "images/JeanDoggy/Jean_Doggy_Spunk_Chin.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Mouth spunk
            "'mouth' not in EmmaX.Spunk or not Player.Male", Null(),
            #"EmmaX.Mouth == 'normal'", "images/EmmaDoggy/Emma_Doggy_Spunk_Normal.png",
            #"EmmaX.Mouth == 'sad'", "images/EmmaDoggy/Emma_Doggy_Spunk_Normal.png",
#            "EmmaX.Mouth == 'lipbite'", "images/EmmaDoggy/Emma_Doggy_Spunk_Smile.png",
            "EmmaX.Mouth == 'smile'", "images/EmmaDoggy/Emma_Doggy_Head_Spunk_Smile.png",
            "EmmaX.Mouth == 'grimace'", "images/EmmaDoggy/Emma_Doggy_Head_Spunk_Smile.png",
            "EmmaX.Mouth == 'sucking'", "images/EmmaDoggy/Emma_Doggy_Head_Spunk_Tongue.png",
            #"EmmaX.Mouth == 'kiss'", "images/EmmaDoggy/Emma_Doggy_Spunk_Open.png",
#            "EmmaX.Mouth == 'surprised'", "images/EmmaDoggy/Emma_Doggy_Spunk_Normal.png",
            "EmmaX.Mouth == 'tongue'", "images/EmmaDoggy/Emma_Doggy_Head_Spunk_Tongue.png",
            "True", "images/EmmaDoggy/Emma_Doggy_Head_Spunk_Normal.png",
            ),
        (0,0), ConditionSwitch(
            #Brows
            #"EmmaX.Brows == 'normal'", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Brows_Normal.png",
            "EmmaX.Brows == 'angry'", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Brows_Angry.png",
            "EmmaX.Brows == 'sad'", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Brows_Sad.png",
            "EmmaX.Brows == 'surprised'", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Brows_Surprised.png",
            #"EmmaX.Brows == 'confused'", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Brows_Normal.png",
            "True", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Brows_Normal.png",
            ),
        (0,0), "Emma Doggy Blink",#Eyes
#        (0,0), ConditionSwitch(
#            #wet hair strand
#            "EmmaX.Water or EmmaX.Hair == 'wet'", "images/JeanDoggy/Jean_Doggy_Hair_Wet_Under.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Hair
            "EmmaX.Hair == 'short'", Null(), #"images/EmmaDoggy/Emma_Doggy_Hair_Short.png",   #or EmmaX.Hair == 'hat wet'
            "EmmaX.Water or EmmaX.Hair == 'wet'", Recolor("Emma", "Hair", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Hair_Wet.png"),   #or EmmaX.Hair == 'hat wet'
            "not Player.Male and 'facial' in EmmaX.Spunk",Recolor("Emma", "Hair", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Hair_Wet.png"),
            "True", Recolor("Emma", "Hair", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Hair_Long.png"),
            ),
        # Modification mode
        (0,0), ConditionSwitch(
            "EmmaX.Mask == 'mask harem'", "images/EmmaDoggy/modification/Emma_doggy_mask_harem.png",
            "True", Null(),
        ),
        # ------------------
#        (0,0), ConditionSwitch(
#            #Wet look
#            "EmmaX.Water", "images/EmmaDoggy/Emma_Doggy_Head_Wet.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #face spunk
#            "'hair' in EmmaX.Spunk", "images/EmmaDoggy/Emma_Doggy_Spunk_Hair.png",
#            "'facial' in EmmaX.Spunk", "images/EmmaDoggy/Emma_Doggy_Spunk_Facial.png",
#            "True", Null(),
#            ),
#        (0,0), "images/EmmaDoggy/Emma_Doggy_Head_Bodyref.png",
        )
    zoom 0.83 #.83
    #alpha 0.9
# End Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Emma_Doggy_Head_Fore:
        #hair over body
        contains:
            ConditionSwitch(
                #Hair
                "EmmaX.Hair == 'short'", "images/EmmaDoggy/Emma_Doggy_Hair_Short_Fore.png",
                "EmmaX.Hat and (EmmaX.Water or EmmaX.Hair == 'wet')", Recolor("Emma", "Hair", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Hair_Wet_Fore_S.png"),   #or EmmaX.Hair == 'hat wet'
                "EmmaX.Hat and not Player.Male and 'facial' in EmmaX.Spunk",Recolor("Emma", "Hair", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Hair_Wet_Fore_S.png"),
                "EmmaX.Hat", Recolor("Emma", "Hair", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Hair_Wave_Fore_S.png"),
                "EmmaX.Water or EmmaX.Hair == 'wet'", Recolor("Emma", "Hair", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Hair_Wet_Fore.png"),   #or EmmaX.Hair == 'hat wet'
                "not Player.Male and 'facial' in EmmaX.Spunk",Recolor("Emma", "Hair", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Hair_Wet_Fore.png"),
                "True", Recolor("Emma", "Hair", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Hair_Wave_Fore.png"),
                )
#        contains:
#            ConditionSwitch(
#                #Wet look
#                "EmmaX.Water", "images/EmmaDoggy/Emma_Doggy_Head_Wet.png",
#                "not Player.Male and 'facial' in EmmaX.Spunk","images/EmmaDoggy/Emma_Doggy_Head_Wet.png",
#                "True", Null(),
#                )
#        contains:
#            ConditionSwitch(
#                #face spunk
#                "'hair' in EmmaX.Spunk and Player.Male", "images/EmmaDoggy/Emma_Doggy_Head_Spunk_Hair.png",
#                "'facial' in EmmaX.Spunk", "images/EmmaDoggy/Emma_Doggy_Head_Spunk_Facial.png",
#                "True", Null(),
#                )
#        contains:
#            ConditionSwitch(
#                #Hair shade under hat
#                "not EmmaX.Hat", Null(),
#                "EmmaX.Hair == 'hat' or EmmaX.Water", Recolor("Emma", "Hair", "images/EmmaDoggy/Emma_Doggy_Hair_Wet_Shadow.png"),
#                "not Player.Male and 'facial' in EmmaX.Spunk",Recolor("Emma", "Hair", "images/EmmaDoggy/Emma_Doggy_Hair_Wet_Shadow.png"),
#                "True", Recolor("Emma", "Hair", "images/EmmaDoggy/Emma_Doggy_Hair_Long_Shadow.png"),
##                "True", Null(),
#                )
        contains:
            ConditionSwitch(
            #Hat
                "EmmaX.Hat", "Emma_Doggy_Hat",
                "True", Null(),
                )
            xoffset -25
        zoom 0.83
        #alpha 0.7
# End Head Fore / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#image Emma_Doggy_Hair_Under:
#        #hair under body
#        ConditionSwitch(
#                "EmmaX.Water or EmmaX.Hair == 'wet'", "images/JeanDoggy/Jean_Doggy_Hair_Wet_Under.png",
#                "True", "images/JeanDoggy/Jean_Doggy_Hair_Short_Under.png",
#                )
#        zoom 0.83

image Emma_Doggy_Hair_Over:
        #hair over body
        contains:
            ConditionSwitch(
                #Hair
                "EmmaX.Hair == 'short'", "images/EmmaDoggy/Emma_Doggy_Hair_Short.png",   #or EmmaX.Hair == 'hat wet'
                "EmmaX.Water or EmmaX.Hair == 'wet'", Recolor("Emma", "Hair", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Hair_Wet.png"),   #or EmmaX.Hair == 'hat wet'
                "not Player.Male and 'facial' in EmmaX.Spunk",Recolor("Emma", "Hair", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Hair_Wet.png"),
                "True", Recolor("Emma", "Hair", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Hair_Long.png"),
                )
        contains:
            ConditionSwitch(
                #Wet look
                "EmmaX.Water", "images/EmmaDoggy/Emma_Doggy_Head_Wet.png",
                "not Player.Male and 'facial' in EmmaX.Spunk","images/EmmaDoggy/Emma_Doggy_Head_Wet.png",
                "True", Null(),
                )
        contains:
            ConditionSwitch(
                #face spunk
                "'hair' in EmmaX.Spunk and Player.Male", "images/EmmaDoggy/Emma_Doggy_Head_Spunk_Hair.png",
                "'facial' in EmmaX.Spunk", "images/EmmaDoggy/Emma_Doggy_Head_Spunk_Facial.png",
                "True", Null(),
                )
        contains:
            ConditionSwitch(
                #Hair shade under hat
                "not EmmaX.Hat or EmmaX.Hair == 'short'", Null(),
                "EmmaX.Hair == 'hat' or EmmaX.Water", Recolor("Emma", "Hair", "images/EmmaDoggy/Emma_Doggy_Hair_Wet_Shadow.png"),
                "not Player.Male and 'facial' in EmmaX.Spunk",Recolor("Emma", "Hair", "images/EmmaDoggy/Emma_Doggy_Hair_Wet_Shadow.png"),
                "True", Recolor("Emma", "Hair", "images/EmmaDoggy/Emma_Doggy_Hair_Long_Shadow.png"),
#                "True", Null(),
                )
        contains:
            ConditionSwitch(
            #Hat
                "EmmaX.Hat", "Emma_Doggy_Hat",
                "True", Null(),
                )
        zoom 0.83
        #alpha 0.7
# End Hair Over / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Emma_Doggy_Hat:
    #the mouth used for the heading animations
#    contains:
        "images/EmmaSprite/EmmaSprite_Hat.png"
        xzoom -0.6
        yzoom 0.6
#        zoom 0.6
        anchor (0.50,0.65)  #(0.50,0.65)
        offset(235,300)
#        alpha 0.5
        rotate 10


image Emma Doggy Blink:
        #Eyes
        ConditionSwitch(
        "EmmaX.Eyes == 'sexy'", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Eyes_Sexy.png",
        "EmmaX.Eyes == 'side'", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Eyes_Side.png",
#        "EmmaX.Eyes == 'normal'", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Eyes_Normal.png",
        "EmmaX.Eyes == 'closed'", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Eyes_Closed.png",
#        "EmmaX.Eyes == 'manic'", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Eyes_Normal.png",
        "EmmaX.Eyes == 'down'", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Eyes_Down.png",
        "EmmaX.Eyes == 'stunned'", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Eyes_Stunned.png",
        "EmmaX.Eyes == 'surprised'", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Eyes_Surprised.png",
        "EmmaX.Eyes == 'squint'", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Eyes_Sexy.png",
        "True", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Eyes_Normal.png",
        ),
    #    choice:
    #        3.5
    #    choice:
    #        3.25
    #    choice:
    #        3
        3
        # This randomizes the time between blinking.
        "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Eyes_Closed.png"
        .25
        repeat

image Emma_Doggy_Ass:
    LiveComposite(
        #Lower body
        (420,750),

        (0,0), ConditionSwitch(
            #New ass base check
            "Trigger == 'lick pussy'", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Ass_Open.png",
            "EmmaX.Legs and not EmmaX.Upskirt", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Ass_Closed.png",
            "EmmaX.Panties and not EmmaX.PantiesDown", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Ass_Closed.png",
            "Player.Sprite and Player.Cock == 'in'", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Ass_Fucking.png",
            "'dildo pussy' in (Trigger,Trigger2,EmmaX.Offhand)", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Ass_Fucking.png",
            "'fondle pussy' in (Trigger,Trigger2,EmmaX.Offhand)", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Ass_Fucking.png",
            "Trigger == 'insert pussy'", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Ass_Fucking.png",
            "True", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Ass_Closed.png",
            ),
        (0,0), ConditionSwitch(
            #Anus backing plate
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
#                    "Speed > 2", "'images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Anal_FullBase.png'", #Speed 3
#                    "Speed > 1", "'images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Anal_FullBase.png'",  #Speed 2
                    "Speed", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Anal_FullBase.png",      #Speed 1
                    "True", Null(),               #Speed 0
                    ),
            "renpy.showing('Anal_Plug_In_Doggy') or renpy.showing('Anal_Plug_Out_Doggy')", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Anal_FullBase.png",
            "EmmaX.Plug", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Anal_PlugPlate.png",
            "'insert ass' in (Trigger,Trigger2,EmmaX.Offhand)", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Anal_FullBase.png",
            "'dildo anal' in (Trigger,Trigger2,EmmaX.Offhand)", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Anal_FullBase.png",
            "EmmaX.Loose > 2", "Emma_Gape_Anal",    #intentional
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #ass red
            "EmmaX.Red", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Red.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "EmmaX.Water", "images/EmmaDoggy/Emma_Doggy_Wet_Ass.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hose
            "EmmaX.Hose == 'stockings'", Recolor("Emma", "Hose", "images/EmmaDoggy/Emma_Doggy_Hose_Stockings.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Panties if Down
            "not EmmaX.PantiesDown or (EmmaX.Legs and EmmaX.Legs != 'skirt' and not EmmaX.Upskirt)", Null(),
            "EmmaX.Panties == 'sports panties'", Recolor("Emma", "Panties", "images/EmmaDoggy/Emma_Doggy_Panties_Sport_Down.png"),
            "EmmaX.Panties == 'bikini bottoms'", Recolor("Emma", "Panties", "images/EmmaDoggy/Emma_Doggy_Panties_Bikini_Down.png"),
            "EmmaX.Panties == 'lace panties'",Recolor("Emma", "Panties", "images/EmmaDoggy/Emma_Doggy_Panties_Lace_Down.png"),
            "EmmaX.Panties",Recolor("Emma", "Panties", "images/EmmaDoggy/Emma_Doggy_Panties_White_Down.png"),
            "True", Null(),
            ),


        (0,0), ConditionSwitch(
            #Legs Layer if down
            "EmmaX.Legs == 'pants' and EmmaX.Upskirt", Recolor("Emma", "Legs", "images/EmmaDoggy/Emma_Doggy_Legs_Pants_Down.png"),
            "EmmaX.Legs == 'yoga pants' and EmmaX.Upskirt", Recolor("Emma", "Legs", "images/EmmaDoggy/Emma_Doggy_Legs_Yoga_Down.png"),
            # Modification mode
            "EmmaX.Legs == 'bottom harem' and EmmaX.Upskirt", "images/EmmaDoggy/modification/Emma_doggy_legs_harem_bottom_down.png",
            # -----------------
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #boots Layer
            "EmmaX.Legs and EmmaX.Legs != 'skirt' and EmmaX.Upskirt",Null(),
            "EmmaX.Boots == 'thigh boots'", Recolor("Emma", "Boots", "images/EmmaDoggy/Emma_Doggy_Boots.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunkpussy Layer
            "'in' in EmmaX.Spunk and Player.Cock == 'in' and Player.Male",Null(),# "images/JeanDoggy/Jean_Doggy_SpunkPussyOpen.png",  #fix for EmmaX.Spunk is used later
            "'in' in EmmaX.Spunk and Player.Male", "images/JeanDoggy/Jean_Doggy_SpunkPussyClosed.png",
            "EmmaX.Wet and Player.Cock == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "EmmaX.Wet", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pubes
            "not EmmaX.Pubes", Null(),
            "Player.Sprite and Player.Cock == 'in'", Null(), # "images/EmmaDoggy/Emma_Doggy_Pubes_Fucked.png",
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
            "'dildo pussy' in (Trigger,Trigger2,EmmaX.Offhand)", Null(),
            "(EmmaX.Legs and EmmaX.Legs != 'skirt') and not EmmaX.Upskirt", Null(),
            "EmmaX.PantiesDown and Trigger == 'lick pussy'", Recolor("Emma", "Pubes", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Pubes_Open.png"),
            "EmmaX.Panties and EmmaX.PantiesDown", Recolor("Emma", "Pubes", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Pubes_Closed.png"),
            "EmmaX.Panties", Recolor("Emma", "Pubes", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Pubes_ClosedC.png"),
            "EmmaX.Hose == 'pantyhose' and Trigger == 'lick pussy'", Recolor("Emma", "Pubes", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Pubes_OpenC.png"),
            "EmmaX.Hose == 'pantyhose'", Recolor("Emma", "Pubes", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Pubes_ClosedC.png"),
            "Trigger == 'lick pussy'", Recolor("Emma", "Pubes", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Pubes_Open.png"),
            "True", Recolor("Emma", "Pubes", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Pubes_Closed.png"),
            ),
        (0,0), ConditionSwitch(
            #Pussy Piercings
            "Player.Sprite", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
            "'dildo pussy' in (Trigger,Trigger2,EmmaX.Offhand)", Null(),
            "EmmaX.Pierce == 'barbell'", "images/EmmaDoggy/Emma_Doggy_Pierce_Barbell.png",
            "EmmaX.Pierce == 'ring' and EmmaX.Panties and not EmmaX.PantiesDown", "images/EmmaDoggy/Emma_Doggy_Pierce_RingC2.png",
            "EmmaX.Pierce == 'ring' and EmmaX.Hose == 'pantyhose' and not (EmmaX.Panties and EmmaX.PantiesDown)", "images/EmmaDoggy/Emma_Doggy_Pierce_RingC2.png",
            "EmmaX.Pierce == 'ring' and EmmaX.Legs and EmmaX.Legs != 'skirt' and not EmmaX.Upskirt", "images/EmmaDoggy/Emma_Doggy_Pierce_RingC2.png",
            "EmmaX.Pierce == 'ring'", "images/EmmaDoggy/Emma_Doggy_Pierce_Ring.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Panties if up
            "EmmaX.PantiesDown or not EmmaX.Panties", Null(),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),
            "EmmaX.Panties == 'sports panties' and EmmaX.Wet", Recolor("Emma", "Panties", "images/EmmaDoggy/Emma_Doggy_Panties_Sport_Wet.png"),
            "EmmaX.Panties == 'sports panties'", Recolor("Emma", "Panties", "images/EmmaDoggy/Emma_Doggy_Panties_Sport.png"),
            "EmmaX.Panties == 'lace panties'", Recolor("Emma", "Panties", "images/EmmaDoggy/Emma_Doggy_Panties_Lace.png"),
            "EmmaX.Panties == 'bikini bottoms'", Recolor("Emma", "Panties", "images/EmmaDoggy/Emma_Doggy_Panties_Bikini.png"),
            "EmmaX.Wet", Recolor("Emma", "Panties", "images/EmmaDoggy/Emma_Doggy_Panties_White_Wet.png"),
            "True", Recolor("Emma", "Panties", "images/EmmaDoggy/Emma_Doggy_Panties_White.png"),
            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #full hose/tights
#            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),
#            "EmmaX.Panties and EmmaX.PantiesDown and EmmaX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "EmmaX.Hose == 'garterbelt'", Recolor("Emma", "Hose", "images/EmmaDoggy/Emma_Doggy_Hose_Garter.png"),
            "EmmaX.Hose == 'stockings and garterbelt'", Recolor("Emma", "Hose", "images/EmmaDoggy/Emma_Doggy_Hose_StockingGarter.png"),
            "EmmaX.Panties and EmmaX.PantiesDown", Null(),
            "EmmaX.Hose == 'pantyhose'", Recolor("Emma", "Hose", "images/EmmaDoggy/Emma_Doggy_Hose_Pantyhose.png"),
            "EmmaX.Hose == 'ripped pantyhose'", Recolor("Emma", "Hose", "images/EmmaDoggy/Emma_Doggy_Hose_PantyhoseHoled.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Pussy Piercings over clothes
            "Player.Sprite", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
            "'dildo pussy' in (Trigger,Trigger2,EmmaX.Offhand)", Null(),
            "not EmmaX.Panties and EmmaX.Hose != 'pantyhose'", Null(),
            "((EmmaX.Panties or EmmaX.Hose == 'pantyhose') and EmmaX.PantiesDown)", Null(),
                #if she has panties, but they are down, or pantyhose, or Legs that are not a skirt and are not down, skip these. . .
            "EmmaX.Pierce == 'barbell'", "images/EmmaDoggy/Emma_Doggy_Pierce_BarbellC.png",
            "EmmaX.Pierce == 'ring'", "images/EmmaDoggy/Emma_Doggy_Pierce_RingC.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Legs Layer
            "EmmaX.Legs == 'pants'", ConditionSwitch(
                    "EmmaX.Upskirt", Null(),
                    "EmmaX.Wet > 1", Recolor("Emma", "Legs", "images/EmmaDoggy/Emma_Doggy_Legs_Pants_Wet.png"),
                    "True", Recolor("Emma", "Legs", "images/EmmaDoggy/Emma_Doggy_Legs_Pants.png"),
                    ),
            "EmmaX.Legs == 'yoga pants'", ConditionSwitch(
                    "EmmaX.Upskirt", Null(),
                    "EmmaX.Wet > 1", Recolor("Emma", "Legs", "images/EmmaDoggy/Emma_Doggy_Legs_Yoga_Wet.png"),
                    "True", Recolor("Emma", "Legs", "images/EmmaDoggy/Emma_Doggy_Legs_Yoga.png"),
                    ),
            "EmmaX.Legs == 'dress'", ConditionSwitch(
                    "EmmaX.Upskirt and Player.Sprite and Player.Cock == 'anal' and Speed" , Recolor("Emma", "Legs", "images/EmmaDoggy/Emma_Doggy_Legs_Dress_Up.png"),
                    "EmmaX.Upskirt", Recolor("Emma", "Legs", "images/EmmaDoggy/Emma_Doggy_Legs_Dress_Up.png"),
                    "True", Recolor("Emma", "Legs", "images/EmmaDoggy/Emma_Doggy_Legs_Dress.png"),
                    ),
            "EmmaX.Legs == 'skirt'", ConditionSwitch(
                    "EmmaX.Upskirt and Player.Sprite and Player.Cock == 'anal' and Speed" , Recolor("Emma", "Legs", "images/EmmaDoggy/Emma_Doggy_Legs_Skirt_Up.png"),
                    "EmmaX.Upskirt", Recolor("Emma", "Legs", "images/EmmaDoggy/Emma_Doggy_Legs_Skirt_Up.png"),
                    "True", Recolor("Emma", "Legs", "images/EmmaDoggy/Emma_Doggy_Legs_Skirt.png"),
                    ),
            # Modification mode
            "EmmaX.Legs == 'bottom harem'", ConditionSwitch(
                "EmmaX.Upskirt", Null(),
                "EmmaX.Wet > 1", Null(),
                "True", "images/EmmaDoggy/modification/Emma_doggy_legs_harem_bottom.png",
            ),
            # ----------------
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Pussy Piercings over clothes
            "Player.Sprite", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
            "'dildo pussy' in (Trigger,Trigger2,EmmaX.Offhand)", Null(),
            "not EmmaX.Legs", Null(),
            "EmmaX.Legs and EmmaX.Legs != 'skirt' and EmmaX.Legs != 'dress' and EmmaX.Upskirt", Null(),
                #if she has panties, but they are down, or pantyhose, or Legs that are not a skirt and are not down, skip these. . .
            "EmmaX.Pierce == 'barbell'", "images/EmmaDoggy/Emma_Doggy_Pierce_BarbellC.png",
            "EmmaX.Pierce == 'ring'", "images/EmmaDoggy/Emma_Doggy_Pierce_RingC.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #boots Layer
            "EmmaX.Legs and EmmaX.Legs != 'skirt' and EmmaX.Upskirt",Null(),
            "Player.Cock == 'in' or Player.Cock == 'anal'",Null(),
            "EmmaX.Boots == 'thigh boots'", Recolor("Emma", "Boots", "images/EmmaDoggy/Emma_Doggy_Boots.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over Layer
            "EmmaX.Over == 'nighty' and EmmaX.Upskirt", Recolor("Emma", "Over", "images/EmmaDoggy/Emma_Doggy_Legs_Nighty_Up.png"),
            "EmmaX.Over == 'nighty'", Recolor("Emma", "Over", "images/EmmaDoggy/Emma_Doggy_Legs_Nighty.png"),
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Over Layer
#            "EmmaX.Over == 'towel' and EmmaX.Upskirt", Recolor("Emma", "Legs", "images/EmmaDoggy/Emma_Doggy_Legs_Towel_Up.png"),
#            "EmmaX.Over == 'towel'", Recolor("Emma", "Legs", "images/EmmaDoggy/Emma_Doggy_Legs_Towel.png"),
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #spunk back Layer
            "'back' in EmmaX.Spunk and Player.Male", "images/EmmaDoggy/Emma_Doggy_Spunk_Ass.png",
            "True", Null(),
            ),
         (0,0), ConditionSwitch(
            #Pussy Composite
            "EmmaX.Legs and not EmmaX.Upskirt",Null(),
            "EmmaX.Panties and not EmmaX.PantiesDown", Null(),
            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Emma_Pussy_Fucking3",#Speed 3
                    "Speed > 1", "Emma_Pussy_Fucking2",#Speed 2
                    "Speed", "Emma_Pussy_Heading",      #Speed 1
                    "True", "Emma_Pussy_Static",              #Speed 0
                    ),
            "'dildo pussy' in (Trigger,Trigger2,EmmaX.Offhand)", "Emma_Pussy_Fucking2",
            "'fondle pussy' in (Trigger,Trigger2,EmmaX.Offhand)", "Emma_Pussy_Fingering",
            "Trigger == 'insert pussy'", "Emma_Pussy_Fingering",
            "True",Null(),
            ),
        (0,0), ConditionSwitch(
            #Anus Composite
            "EmmaX.Legs and not EmmaX.Upskirt",Null(),
            "EmmaX.Panties and not EmmaX.PantiesDown", Null(),
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Emma_Anal_Fucking2", #Speed 3
                    "Speed > 1", "Emma_Anal_Fucking",  #Speed 2
                    "Speed", "Emma_Anal_Heading",      #Speed 1
                    "True", "Emma_Anal",               #Speed 0
                    ),
            "'insert ass' in (Trigger,Trigger2,EmmaX.Offhand)", "Emma_Anal_Fingering",
            "'dildo anal' in (Trigger,Trigger2,EmmaX.Offhand)", "Emma_Anal_Fucking",
            "EmmaX.Plug", "images/PlugIn.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy'", "Rogue_Doggy_Lick_Pussy",
            "Trigger == 'lick ass'", "Rogue_Doggy_Lick_Ass",
            "True", Null()
            ),
        (0,0), ConditionSwitch(
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
# End Ass / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Emma_Doggy_Feet:
    contains:
            AlphaMask("Emma_Doggy_Shins", "images/EmmaDoggy/Emma_Doggy_Feet_Mask.png")

image Emma_Doggy_Shins:
    #Emma's footjob shins
    contains:
            #hose legs
        ConditionSwitch(
            "EmmaX.Hose == 'ripped pantyhose'", Recolor("Emma", "Hose", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Feet_StockingsHoled.png"),
            "EmmaX.Hose and EmmaX.Hose != 'garterbelt'", Recolor("Emma", "Hose", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Feet_Stockings.png"),
            "True", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Feet.png"
            )
    contains:
        #pants
        ConditionSwitch(
            "EmmaX.Legs == 'pants'", Recolor("Emma", "Legs", "images/EmmaDoggy/Emma_Doggy_Feet_Pants.png"),
            "EmmaX.Legs == 'yoga pants'", Recolor("Emma", "Legs", "images/EmmaDoggy/Emma_Doggy_Feet_YogaPants.png"),
            "True", Null(),
            )
    contains:
        #spunk
        ConditionSwitch(
            "'feet' in EmmaX.Spunk", "images/EmmaDoggy/Emma_Doggy_Spunk_Feet.png",
            "True", Null(),
            )

image Emma_Doggy_Shins0:
        "Emma_Doggy_Shins"
        offset (0, 100) #(0,0) top

image Emma_Doggy_GropeBreast:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        xzoom -.55
        yzoom .55
        offset (90,350)#(110,420)
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
        block:
            ease 1 rotate 10#60
            ease 1 rotate 0#90
            repeat

image Emma_Doggy_Boob:
    contains:
        "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Boob.png"

    contains:
            #bra
        ConditionSwitch(
            "EmmaX.Uptop", ConditionSwitch(
#                    "EmmaX.Chest == 'corset'", Recolor("Emma", "Chest", "images/EmmaDoggy/Emma_Doggy_Bra_Corset_Boob_Down.png"),
#                    "EmmaX.Chest == 'lace bra'", Recolor("Emma", "Chest", "images/EmmaDoggy/Emma_Doggy_Bra_Corset_Boob_Down.png"),
                    "EmmaX.Chest == 'sports bra'", Recolor("Emma", "Chest", "images/EmmaDoggy/Emma_Doggy_Bra_Sport_Boob_Down.png"),
#                    "EmmaX.Chest == 'bikini top'", Recolor("Emma", "Chest", "images/EmmaDoggy/Emma_Doggy_Bra_Corset_Boob_Down.png"),
                    "EmmaX.Chest", Recolor("Emma", "Chest", "images/EmmaDoggy/Emma_Doggy_Bra_Corset_Boob_Down.png"),
                    "True", Null(),
                    ),
            "EmmaX.Over == 'jacket'", Null(),
            "EmmaX.Chest == 'corset'", Recolor("Emma", "Chest", "images/EmmaDoggy/Emma_Doggy_Bra_Corset_Boob.png"),
            "EmmaX.Chest == 'lace bra'", Recolor("Emma", "Chest", "images/EmmaDoggy/Emma_Doggy_Bra_Lace_Boob.png"),
            "EmmaX.Chest == 'sports bra'", Recolor("Emma", "Chest", "images/EmmaDoggy/Emma_Doggy_Bra_Sport_Boob.png"),
            "EmmaX.Chest == 'bikini top'", Recolor("Emma", "Chest", "images/EmmaDoggy/Emma_Doggy_Bra_Corset_Boob.png"),
            "True", Null(),
            )
    contains:
            #Wet look
        ConditionSwitch(
            "EmmaX.Water", "images/EmmaDoggy/Emma_Doggy_Wet_Boob.png",
            "True", Null(),
            )
    contains:
            #Overshirt
        ConditionSwitch(
            "not EmmaX.Over", Null(),
            "EmmaX.Over == 'dress' and EmmaX.Uptop", Recolor("Emma", "Over", "images/EmmaDoggy/Emma_Doggy_Over_Dress_Boob_Down.png"),
            "EmmaX.Over == 'dress'", Recolor("Emma", "Over", "images/EmmaDoggy/Emma_Doggy_Over_Dress_Boob.png"),
            "EmmaX.Over == 'jacket' and EmmaX.Uptop", Null(),
            "EmmaX.Over == 'jacket'", Recolor("Emma", "Over", "images/EmmaDoggy/Emma_Doggy_Over_Jacket_Boob.png"),
            "EmmaX.Over == 'nighty' and EmmaX.Uptop", Recolor("Emma", "Chest", "images/EmmaDoggy/Emma_Doggy_Bra_Corset_Boob_Down.png"),
            "EmmaX.Over == 'nighty'", Recolor("Emma", "Over", "images/EmmaDoggy/Emma_Doggy_Over_Nighty_Boob.png"),
            "True", Null(),
            )
# End Boob / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



image Emma_Doggy_Boob_Fuck:
    #animation for anal fucking top half
    contains:
        subpixel True
        "Emma_Doggy_Boob"
        ypos 0#15
        pause .4
        block:
            pause .05
            ease .25 ypos -20#-10
            pause .2
            ease .3 ypos -5#0
            ease .2 ypos -10#0
            easein 1.5 ypos 0#0
            repeat
#        block:
#            ease .2 ypos -10#5
#            pause .3
#            ease 2 ypos 0#15
#            repeat

image Emma_Doggy_Boob_Fuck2:
    #animation for anal fucking2 top half
    contains:
        subpixel True
        "Emma_Doggy_Boob"
        ypos 0#20
        block:
            pause .15
            ease .1 ypos -30#-20
            pause .1
            ease .55 ypos 5#0      easein
#            pause .05
            repeat

image Emma_Gape_Anal:
        #animation for her asshole growing and shrinking a bit when over 2 Looseness
        contains:
            subpixel True
            "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Anal_GapePlate.png"
            anchor (0.52,0.69)
            offset (218,513)#(218,513)
        contains:
            subpixel True
            "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Anal_GapeBase.png"
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


image Zero_Emma_Hotdog_Static:
    # The unmoving version of the hotdog cock
    # called in Doggy Ass LC
    contains:
        "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Emma_Hotdog_Moving:
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
image Emma_Pussy_Static:
    #Full Animation for speed 0
    subpixel True
    contains:
        #moving hole
        "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Pussy_Heading.png"
        subpixel True
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
        anchor (217,550)#(0.50,0.69)
        transform_anchor True
        pos (220,555) #(220,550)
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
            "EmmaX.Pubes", Recolor("Emma", "Pubes", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Pubes_Heading.png"),
            "True", Null(),
            )
        subpixel True
        anchor (217,550)#(0.50,0.69)
        transform_anchor True
        pos (218,550) #(220,550)
        xzoom .7
        block:
            ease .9 xzoom .85
            pause 1.6
            ease 2.5 xzoom .7
            repeat
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "EmmaX.Pierce == 'barbell'", "images/EmmaDoggy/Emma_Doggy_Pierce_BarbellF.png",
            "EmmaX.Pierce == 'ring'", "images/EmmaDoggy/Emma_Doggy_Pierce_RingF.png",
            "True", Null(),
            )
        xoffset 2
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in EmmaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.52,0.69)
        pos (221,516)
        xzoom .7
        block:
            ease 1 xzoom .9
            pause 1
            ease 3 xzoom .7
            repeat
    contains:
        #Cock
        AlphaMask("Zero_Emma_Doggy_Static", "Emma_Pussy_Mask_Static")

image Zero_Emma_Doggy_Static:
    # Sex Speed 0 motions
    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (173,550)
        block:
            ease 1 ypos 543 #in stroke 540
            pause 1
            ease 3 ypos 550 #out stroke 550
            repeat

image Emma_Pussy_Mask_Static:
    #AlphaMask used to prevent the cock from moving past the pussy in static pose
    #Called in "Jean_Pussy_Moving"
    contains:
        #Base
        subpixel True
#        "images/RogueDoggy/Rogue_Doggy_SexMask.png"
        "images/EmmaDoggy/Emma_Doggy_Pussy_MaskHeading.png"
        anchor (0.52,0.69)
        pos (220,530)
        xzoom 1




# Animation for pussy heading action / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_Pussy_Heading:
    #Full Animation for speed 1
    subpixel True
    contains:
        #moving hole
        "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Pussy_FHole.png"
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
            "EmmaX.Pubes", Recolor("Emma", "Pubes", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Pubes_Heading.png"),
            "True", Null(),
            )
        subpixel True
        anchor (217,550)#(0.50,0.69)
        transform_anchor True
        pos (218,550) #(220,550)
        xzoom .75
        block:
            ease .9 xzoom .95
            pause 1.6
            ease 2.5 xzoom .75#1.15
            repeat
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "EmmaX.Pierce == 'barbell'", "images/EmmaDoggy/Emma_Doggy_Pierce_BarbellF.png",
            "EmmaX.Pierce == 'ring'", "images/EmmaDoggy/Emma_Doggy_Pierce_RingF.png",
            "True", Null(),
            )
        xoffset 2
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in EmmaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
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
        AlphaMask("Zero_Emma_Doggy_Heading", "Emma_Pussy_Mask")
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in EmmaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
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
    xoffset -2

image Zero_Emma_Doggy_Heading:
    # Sex Speed 1 motions
    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (171,545)
#        alpha 0.2
        block:
            ease 1 ypos 500 #in stroke xpos 168
            pause 1
            ease 3 ypos 545 #out stroke xpos 171
            repeat

image Emma_Pussy_Mask:
    #AlphaMask used to prevent the cock from moving past the pussy
    #Called in "Jean_Pussy_Moving"
    contains:
        #Base
        "images/EmmaDoggy/Emma_Doggy_Pussy_MaskHeading.png"
        anchor (0.52,0.69)
        pos (220,518)
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


image Emma_Pussy_Fingering:
    #Full Animation for speed 1
    subpixel True
    contains:
        #moving hole
        "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (220,518)
        xzoom .6
        block:
            ease .9 xzoom .85
            pause 1.6
            ease 2.5 xzoom .6
            repeat
    contains:
        #pubes
        ConditionSwitch(
            "EmmaX.Pubes", Recolor("Emma", "Pubes", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Pubes_Heading.png"),
            "True", Null(),
            )
        subpixel True
        anchor (0.52,0.69)
        pos (225,515) #(218,518)
        xzoom 1
        block:
            ease .9 xzoom 1.2
            pause 1.6
            ease 2.5 xzoom .9#1.15
            repeat
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "EmmaX.Pierce == 'barbell'", "images/EmmaDoggy/Emma_Doggy_Pierce_BarbellF.png",
            "EmmaX.Pierce == 'ring'", "images/EmmaDoggy/Emma_Doggy_Pierce_RingF.png",
            "True", Null(),
            )
        xoffset 2
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in EmmaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
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
        AlphaMask("Zero_Pussy_Finger", "Emma_Pussy_Mask_Finger")
        xoffset 3
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in EmmaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
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

image Emma_Pussy_Mask_Finger:
    #AlphaMask used to prevent the cock from moving past the pussy
    #Called in "Jean_Pussy_Moving"
    contains:
        #Base
        "images/EmmaDoggy/Emma_Doggy_Pussy_MaskHeading.png"
        anchor (0.52,0.69)
        pos (218,526) #(221,518)
        xzoom .8
        parallel:
            ease 1 ypos 521 #518
            pause 1
            ease 3 ypos 526#528
            repeat

# > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

image Emma_Pussy_Fucking2:
    #Full Animation for speed 2
    contains:
        #Base
        "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Pussy_FHole.png"
    contains:
        #pubes
        ConditionSwitch(
            "EmmaX.Pubes", Recolor("Emma", "Pubes", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Pubes_Fucking.png"),
            "True", Null(),
            )
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "EmmaX.Pierce == 'barbell'", "images/EmmaDoggy/Emma_Doggy_Pierce_BarbellF.png",
            "EmmaX.Pierce == 'ring'", "images/EmmaDoggy/Emma_Doggy_Pierce_RingF.png",
            "True", Null(),
            )
        xoffset 2
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in EmmaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            "'dildo pussy' in (Trigger,Trigger2,EmmaX.Offhand)", AlphaMask("Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "True",AlphaMask("Zero_Emma_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            ),
#        AlphaMask("Zero_Emma_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in EmmaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )

image Zero_Emma_Doggy_Fucking2:
    # Sex Speed 2 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat


image Emma_Pussy_Fucking3:
    #Full Animation for speed 3
    contains:
        #Base
        "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Pussy_FHole.png"
    contains:
        #pubes
        ConditionSwitch(
            "EmmaX.Pubes", Recolor("Emma", "Pubes", "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Pubes_Fucking.png"),
            "True", Null(),
            )
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "EmmaX.Pierce == 'barbell'", "images/EmmaDoggy/Emma_Doggy_Pierce_BarbellF.png",
            "EmmaX.Pierce == 'ring'", "images/EmmaDoggy/Emma_Doggy_Pierce_RingF.png",
            "True", Null(),
            )
        xoffset 2
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in EmmaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Emma_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in EmmaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )

image Zero_Emma_Doggy_Fucking3:
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

image Emma_Anal:
    #Anal static Loose
    contains:
        #Cock
        "Zero_Doggy_Insert"
        pos (172,500)

image Emma_Anal_Fingering:
    #Animation for speed 1
    contains:
        #Hole
        "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Anal_FullHole.png"
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
        ConditionSwitch(
            "'anal' in EmmaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
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
        AlphaMask("Zero_Emma_Doggy_Anal_Finger", "Emma_Doggy_Anal_Fingering_Mask")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in EmmaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
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

image Zero_Emma_Doggy_Anal_Finger:
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
image Emma_Doggy_Anal_Fingering_Mask:
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
image Emma_Anal_Heading:
    #Animation for speed 1
    contains:
        #Hole
        "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Anal_FullHole.png"
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
            "'anal' in EmmaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
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
        AlphaMask("Zero_Emma_Doggy_Anal_Heading", "Emma_Doggy_Anal_Heading_Mask")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in EmmaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
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

image Zero_Emma_Doggy_Anal_Heading:
        #the cock anal heading animation
    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500#505
            repeat

image Zero_Emma_Doggy_Anal_HeadingJunk:
    #this is a mask to correct an annoying glitch in the core mask
    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease .5 ypos 550
            pause .25
            ease 1.75 ypos 600#505
            repeat

image Emma_Doggy_Anal_Heading_Mask:
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

image Emma_Doggy_Anal_Head_Top:
#animation for anal fucking top half
    contains:
        subpixel True
        "Emma_Doggy_Body"
        ypos 0
        block:
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat

image Emma_Doggy_Anal_Head_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Emma_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -10
            easeout .1 ypos -7
            easein .9 ypos 0
            pause .9
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Emma_Doggy_Anal1:
    #Animation for speed 2 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat

image Emma_Anal_Fucking:
    #Animation for speed 2 Ass
    contains:
        #Hole
        "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .95
        block:
            pause .25
            ease .25 zoom 1
            pause .75
            ease 1 zoom .95
            pause .25
            repeat
    contains:
        #spunk under cock
        ConditionSwitch(
            "'anal' in EmmaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            #full hose/tights
            "'dildo anal' in (Trigger,Trigger2,EmmaX.Offhand)", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", AlphaMask("Zero_Emma_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            ),
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in EmmaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )


image Emma_Doggy_Fuck_Top:
    #animation for anal fucking top half
    contains:
        subpixel True
        "Emma_Doggy_Body"
        ypos 0#15
        pause .4
        block:
            ease .2 ypos -10#5
            pause .3
            ease 2 ypos 0#15
            repeat

image Emma_Doggy_Fuck_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Emma_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15#-25
            ease .1 ypos -5#-15
            pause .2
            ease 1.6 ypos 0
            repeat


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Emma_Doggy_Anal2:
    #Animation for speed 3 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat

image Emma_Anal_Fucking2:
    #Animation for speed 3 Ass
    contains:
        #Hole
        "images/EmmaDoggy/[EmmaX.skin_image.skin_path]Emma_Doggy_Anal_FullHole.png"
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
        #spunk under cock
        ConditionSwitch(
            "'anal' in EmmaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Emma_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in EmmaX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )

image Emma_Doggy_Fuck2_Top:
    #animation for anal fucking2 top half
    contains:
        subpixel True
        "Emma_Doggy_Body"
        ypos 0#20
        block:
            pause .15
            ease .1 ypos -20#0
            pause .1
            easein .5 ypos 0#20
            pause .05
            repeat

image Emma_Doggy_Fuck2_Ass:
    #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Emma_Doggy_Ass"
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

image Emma_Doggy_Feet0:
    #static animation
    contains:
        "Emma_Doggy_Shins"
        pos (0, -20) #(0,0) top
        block:
            subpixel True
            pause .5
            ease 2 ypos 0#20
            pause .5
            ease 2 ypos -20#0
            repeat
    contains:
        ConditionSwitch(
                "Player.Sprite", "Zero_Doggy_Up",
                "True", Null(),
                )
        zoom 1.2
        pos (158,520)  #(160,480)
    contains:
        "Emma_Doggy_Feet"
        pos (0, -20) #(0,0) top
        block:
            subpixel True
            pause .5
            ease 2 ypos 0#20
            pause .5
            ease 2 ypos -20#0
            repeat

image Emma_Doggy_Feet1:
    #slow animation
    contains:
        "Emma_Doggy_Shins"
        pos (0, -20) #(0,0) top
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos -20
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
        "Emma_Doggy_Feet"
        pos (0, -20) #(0,0) top
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos -20
            repeat

image Emma_Doggy_Feet2:
    #fast animation
    contains:
        "Emma_Doggy_Shins"
        pos (0, -20) #(0,0) top
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos -20
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
        "Emma_Doggy_Feet"
        pos (0, -20) #(0,0) top
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos -20
            repeat
# Footjob animations end > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Doggy Launch/Reset
label Emma_Doggy_Launch(Line = Trigger):
    if renpy.showing("Emma_Doggy_Animation"):
        return
    $ Speed = 0
    call Girl_Hide(EmmaX,1)
    show Emma_Doggy_Animation at SpriteLoc(StageCenter+50) zorder 150
    with dissolve
    return

label Emma_Doggy_Reset:
    if not renpy.showing("Emma_Doggy_Animation"):
        return
#    $ Trigger = 0               #fix, not sure this is a good idea
    $ EmmaX.ArmPose = 2
    $ EmmaX.SpriteVer = 0
    hide Emma_Doggy_Animation
    call Girl_Hide(EmmaX)
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
            alpha 1 zoom 1 offset (0,0) anchor (0.6, 0.0)
    with dissolve
    $ Speed = 0
    return

# End Emma Doggy Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Emma Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Emma Sex element ///////////////////////////////////////////////////////////////////////////
image Emma_SexSprite:
    #core sex animation
    contains:
        ConditionSwitch(
            # Emma's lower body
            "Trigger == 'lick pussy' or Trigger == 'lick ass' or renpy.showing('Anal_Plug_In_Sex_Back') or renpy.showing('Anal_Plug_Out_Sex_Back')", "Emma_Sex_Legs_Lick",#Static
            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                    # If during sex
                    "Speed == 1", "Emma_Sex_Legs_S1",#heading
                    "Speed == 2", "Emma_Sex_Legs_S2",#slow
                    "Speed == 3", "Emma_Sex_Legs_S3",#fast
                    "Speed >= 4", "Emma_Sex_Legs_S4",#cumming
                    "True", "Emma_Sex_Legs_S0",#Static
                    ),
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    # If during Anal
                    "Speed == 1", "Emma_Sex_Legs_A1",#heading
                    "Speed == 2", "Emma_Sex_Legs_A2",#slow
                    "Speed == 3", "Emma_Sex_Legs_A3",#fast
                    "Speed >= 4", "Emma_Sex_Legs_A4",#cumming
                    "True", "Emma_Sex_Legs_A0",#Static
                    ),
            "True", ConditionSwitch(
                    # If neither
                    "Speed == 1", "Emma_Sex_Legs_H1",#heading
                    "Speed == 4", "Emma_Sex_Legs_H4",#cumming
                    "Speed >= 2", "Emma_Sex_Legs_H2",#slow
                    "True", "Emma_Sex_Legs_H0",#Static
                    ),
            )
    contains:
        ConditionSwitch(
            # Emma's upper body
            "Trigger == 'lick pussy' or Trigger == 'lick ass' or renpy.showing('Anal_Plug_In_Sex_Back') or renpy.showing('Anal_Plug_Out_Sex_Back')",  "Emma_Sex_Body_Lick",#Static
            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                    # If during sex
                    "Speed == 1", "Emma_Sex_Body_S1",#heading
                    "Speed == 2", "Emma_Sex_Body_S2",#slow
                    "Speed == 3", "Emma_Sex_Body_S3",#fast
                    "Speed >= 4", "Emma_Sex_Body_S4",#cumming
                    "True",       "Emma_Sex_Body_S0",#Static
                    ),
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
#                    # If during Anal
                    "Speed == 1", "Emma_Sex_Body_A1",#heading
                    "Speed == 2", "Emma_Sex_Body_A2",#slow
                    "Speed == 3", "Emma_Sex_Body_A3",#fast
                    "Speed >= 4", "Emma_Sex_Body_A4",#cumming
                    "True",       "Emma_Sex_Body_A0",#Static
                    ),
            "True", ConditionSwitch(
                    # If neither
                    "Speed == 1", "Emma_Sex_Body_H1",#heading
                    "Speed == 4", "Emma_Sex_Body_H4",#cumming
                    "Speed >= 2", "Emma_Sex_Body_H2",#slow
                    "True",       "Emma_Sex_Body_H0",#Static
                    ),
            )
    zoom 0.8
    anchor (.5,.5)
    pos (575,470)

image Emma_Sex_HairBack:
    #Hair underlay
    "Emma_BJ_HairBack"
    zoom 0.48
    anchor (0.5, 0.5)
    pos (505,260)

image Emma_Sex_Head:
    #Hair underlay
    "Emma_BJ_Head"
    zoom 0.48
    anchor (0.5, 0.5)
    pos (505,260)



# Emma's sex body torso / / / / / torso / / / / / torso / / / / / torso / / / / / torso / / / / /

image Emma_Sex_Torso:
    #Her torso for the sex, BJ, and TJ poses
#    contains:
#            # body
#            "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Body.png"
    contains:
            # body
        ConditionSwitch(
            "EmmaX.Arms and not (EmmaX.Over == 'jacket' or EmmaX.Over == 'dress')", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Body_G.png",
            "True", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Body.png",
            )
    contains:
            # tits
        ConditionSwitch(
            "renpy.showing('Emma_TJ_Animation')", Null(),
            # Modification mode
            "EmmaX.Chest == 'top down tits harem'", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Tits_Down.png", # EmmaX.TitsUp = 0
            # -----------------
            "EmmaX.Chest and not EmmaX.Uptop", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Tits_Up.png",   # EmmaX.TitsUp = 1
            "True", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Tits_Down.png",   # EmmaX.TitsUp = 0
            )
    contains:
            # piercings tits
        ConditionSwitch(
            "renpy.showing('Emma_TJ_Animation')", Null(),
            "(EmmaX.Over or EmmaX.Chest) and not EmmaX.Uptop", Null(),
            "EmmaX.Pierce == 'barbell'", ConditionSwitch(
                    #if it's the ring pericings
                    "not EmmaX.Chest or EmmaX.Uptop", "images/EmmaSex/Emma_Pierce_Barbell_Tits_D.png",   # EmmaX.TitsUp = 1
                    "True", Null(),
                    ),
            "EmmaX.Pierce == 'ring'", ConditionSwitch(
                    #if it's the ring pericings
                    "not EmmaX.Chest or EmmaX.Uptop", "images/EmmaSex/Emma_Pierce_Ring_Tits_D.png",   # EmmaX.TitsUp = 1
                    "True", Null(),
                    ),
            "True", Null(),
            )
    contains:
            # Chest clothing layer
        ConditionSwitch(
#            "not EmmaX.Chest or renpy.showing('Emma_TJ_Animation')", Null(),   # EmmaX.TitsUp = 0
            "EmmaX.Chest == 'sports bra' and (EmmaX.Uptop or renpy.showing('Emma_TJ_Animation'))", Recolor("Emma", "Chest", "images/EmmaSex/Emma_Sex_Bra_Sports_Uptop.png"),   # Add here. . .
            "EmmaX.Chest == 'bikini top' and (EmmaX.Uptop or renpy.showing('Emma_TJ_Animation'))", Recolor("Emma", "Chest", "images/EmmaSex/Emma_Sex_Bra_Bikini_Uptop.png"),   # Add here. . .
            "EmmaX.Uptop or renpy.showing('Emma_TJ_Animation')", Null(),
            "EmmaX.Chest == 'corset'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_Sex_Bra_Corset_Up.png"),   # EmmaX.TitsUp = 1
            "EmmaX.Chest == 'sports bra'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_Sex_Bra_Sports_Up.png"),   # EmmaX.TitsUp = 1
            "EmmaX.Chest == 'bikini top'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_Sex_Bra_Bikini_Up.png"),   # Add here. . .
            "EmmaX.Chest == 'lace bra'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_Sex_Bra_Lace_Up.png"),   # EmmaX.TitsUp = 1
            # Modification mode
            "EmmaX.Chest == 'top up tits harem' and (EmmaX.Uptop or renpy.showing('Emma_TJ_Animation'))", "images/EmmaSex/modification/Emma_sex_chest_tits_up_harem_top_up.png",
            "EmmaX.Chest == 'top up tits harem'", "images/EmmaSex/modification/Emma_sex_chest_tits_up_harem_top.png",
            "EmmaX.Chest == 'top down tits harem' and (EmmaX.Uptop or renpy.showing('Emma_TJ_Animation'))", "images/EmmaSex/modification/Emma_sex_chest_tits_down_harem_top_up.png",
            "EmmaX.Chest == 'top down tits harem'", "images/EmmaSex/modification/Emma_sex_chest_tits_down_harem_top.png",
            # -----------------
            "True", Null(),   # EmmaX.TitsUp = 0
            )
    contains:
            # Over clothing layer
        ConditionSwitch(
            "EmmaX.Over == 'jacket'", ConditionSwitch(
                    #if it's the jacket
#                    "renpy.showing('Emma_TJ_Animation')", Null(),
                    "renpy.showing('Emma_TJ_Animation')", Recolor("Emma", "Over", "images/EmmaSex/Emma_Sex_Jacket_TJ.png"),
                    "EmmaX.Uptop", Recolor("Emma", "Over", "images/EmmaSex/Emma_Sex_Jacket_Down_Uptop.png"),   # EmmaX.TitsUp = 0
                    "EmmaX.Chest and not EmmaX.Uptop", Recolor("Emma", "Over", "images/EmmaSex/Emma_Sex_Jacket_Up.png"),   # EmmaX.TitsUp = 1
                    "True", Recolor("Emma", "Over", "images/EmmaSex/Emma_Sex_Jacket_Down.png"),   # EmmaX.TitsUp = 0
                    ),
            "EmmaX.Over == 'nighty'", ConditionSwitch(
                    #if she has the nighty on
#                    "renpy.showing('Emma_TJ_Animation')", Null(),
                    "EmmaX.Uptop", Recolor("Emma", "Over", "images/EmmaSex/Emma_Sex_Nighty_Uptop.png"),
                    "EmmaX.Chest and not renpy.showing('Emma_TJ_Animation')", Recolor("Emma", "Over", "images/EmmaSex/Emma_Sex_Nighty_Up.png"),   # EmmaX.TitsUp = 1
#                    "EmmaX.Chest in ('corset', 'lace bra', 'sports bra')", Recolor("Emma", "Over", "images/EmmaSex/Emma_Sex_Nighty_Up.png"),
                    "True", Recolor("Emma", "Over", "images/EmmaSex/Emma_Sex_Nighty_Down.png"),
                    ),
            "EmmaX.Over == 'dress'", ConditionSwitch(
                    #if it's the ring pericings
#                    "renpy.showing('Emma_TJ_Animation')", Null(),
                    "renpy.showing('Emma_TJ_Animation')", Recolor("Emma", "Over", "images/EmmaSex/Emma_Sex_Dress_TJ.png"),
                    "EmmaX.Uptop", Recolor("Emma", "Over", "images/EmmaSex/Emma_Sex_Dress_Uptop.png"),   # EmmaX.TitsUp = 0
                    "EmmaX.Chest and not EmmaX.Uptop", Recolor("Emma", "Over", "images/EmmaSex/Emma_Sex_Dress_Up.png"),   # EmmaX.TitsUp = 1
                    "True", Recolor("Emma", "Over", "images/EmmaSex/Emma_Sex_Dress_Down.png"),   # EmmaX.TitsUp = 0
                    ),
            "True", Null(),
            )
    contains:
            # piercings tits over clothes
        ConditionSwitch(
            "renpy.showing('Emma_TJ_Animation')", Null(),
            "EmmaX.Uptop or not EmmaX.Pierce", Null(),
            "EmmaX.Chest and not EmmaX.Uptop", "images/EmmaSex/Emma_Pierce_Barbell_Tits_UC.png",   # EmmaX.TitsUp = 1
            "EmmaX.Over and not EmmaX.Uptop", "images/EmmaSex/Emma_Pierce_Barbell_Tits_DC.png",   # EmmaX.TitsUp = 1
            "True", Null(),
            )
    contains:
            # spunk on tits
            ConditionSwitch(
                "'tits' not in EmmaX.Spunk or not Player.Male", Null(),
                "renpy.showing('Emma_TJ_Animation')", "images/EmmaSex/Emma_Spunk_Titjob_Under.png",
                "True", "images/EmmaSex/Emma_Spunk_Tits.png",
                )
    zoom 1

image Emma_Sex_Lick_Breasts_High:
        "Lick_Anim"
        zoom 0.7
        offset (400,590)#(450,270)

image Emma_Sex_Lick_Breasts:
        "Lick_Anim"
        zoom 0.7
        offset (390,620)#(450,270)

image Emma_Sex_Fondle_Breasts:
        "GropeLeftBreast"
        zoom 1.5
        offset (160,-40)#(320,-130)

image Emma_Sex_Body:
    #Her Body in the sex pose
    contains:
            "Emma_Sex_HairBack"
    contains:
            # body
            "Emma_Sex_Torso"
    contains:
            # Arms
        ConditionSwitch(
            "EmmaX.ArmPose == 3", Null(),   # Neither arms
            "EmmaX.ArmPose == 4", AlphaMask("Emma_SexArms", "images/EmmaSex/Emma_Sex_ArmsMask_R.png"),   # Right arm only
            "EmmaX.ArmPose == 5", AlphaMask("Emma_SexArms", "images/EmmaSex/Emma_Sex_ArmsMask_L.png"),   # Left arm only
            "True", AlphaMask("Emma_SexArms", "images/EmmaSex/Emma_Sex_ArmsMask.png"),  # Both Arms
            )
    contains:
        ConditionSwitch(
            #breast licking animation
            "(Trigger == 'suck breasts' or Trigger2 == 'suck breasts') and EmmaX.Chest and not EmmaX.Uptop", "Emma_Sex_Lick_Breasts_High",
            "Trigger == 'suck breasts' or Trigger2 == 'suck breasts'", "Emma_Sex_Lick_Breasts",
            "True", Null()
            )
    contains:
        ConditionSwitch(
            #breast fondling animation
            "Trigger == 'fondle breasts' or Trigger2 == 'fondle breasts'", "Emma_Sex_Fondle_Breasts",
            "True", Null()
            )
    contains:
            "Emma_Sex_Head"
    zoom 1
#    offset (0,0)
# end Emma's sex body torso / / / / / torso / / / / / torso / / / / / torso / / / / / torso / / / / /


image Emma_SexArms:
    contains:
            # Base Arms
        ConditionSwitch(
            "EmmaX.Over == 'jacket' or EmmaX.Over == 'dress'", Null(),
#            "True", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Arms_Test.png",   # EmmaX.TitsUp = 1
            "EmmaX.Chest and not EmmaX.Uptop", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Arms_U.png",   # EmmaX.TitsUp = 1
#            "EmmaX.Chest == 'corset'", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Arms_U.png",   # EmmaX.TitsUp = 1
#            "EmmaX.Chest == 'sports bra'", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Arms_U.png",   # EmmaX.TitsUp = 1
#            "EmmaX.Chest == 'lace bra'", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Arms_U.png",   # EmmaX.TitsUp = 1
#            "EmmaX.Chest == 'bikini top'", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Arms_U.png",   # EmmaX.TitsUp = 1
            "True", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Arms_D.png",   # EmmaX.TitsUp = 0
            )
    contains:
            # Arm clothing
        ConditionSwitch(
            "EmmaX.Over == 'jacket' or EmmaX.Over == 'dress'", Null(),
            "EmmaX.Chest == 'sports bra'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_Sex_Bra_Sports_Arms.png"),   # EmmaX.TitsUp = 1
            "True", Null(),
            )
#    contains:
#            # Arm clothing
#        ConditionSwitch(
#            "EmmaX.Over == 'nighty' and EmmaX.Uptop", Recolor("Emma", "Over", "images/EmmaSex/Emma_Sex_Nighty_Uptop.png"),
#            "True", Null(),
#            )
    contains:
            # Arm clothing Over
        ConditionSwitch(
            "EmmaX.Over == 'jacket' and EmmaX.Uptop", Recolor("Emma", "Over", "images/EmmaSex/Emma_Sex_Arms_Jacket_Uptop.png"),   # EmmaX.TitsUp = 1
            "EmmaX.Over == 'jacket'", Recolor("Emma", "Over", "images/EmmaSex/Emma_Sex_Arms_Jacket.png"),   # EmmaX.TitsUp = 1
            "EmmaX.Over == 'dress'", Recolor("Emma", "Over", "images/EmmaSex/Emma_Sex_Arms_Dress.png"),   # EmmaX.TitsUp = 1
            "EmmaX.Arms", Recolor("Emma", "Arms", "images/EmmaSex/Emma_Sex_Gloves.png"),
            "True", Null(),
            )



# Emma's sex body legs / / / / / legs / / / / / legs / / / / / legs / / / / / legs / / / / /
image Emma_Sex_Legs_S:
    #Her Legs during sex
    contains:
            # feet
        ConditionSwitch(
#            "EmmaX.Acc == 'thigh boots'", Recolor("Emma", "Boots", "images/EmmaSex/Emma_Sex_Feet_Boots.png"),
            "(EmmaX.Panties and EmmaX.PantiesDown) and (EmmaX.Hose == 'pantyhose' or EmmaX.Hose == 'ripped pantyhose')", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Feet.png",
            "EmmaX.Hose == 'pantyhose' and Player.Sprite and Player.Cock == 'in'","images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Feet.png",
            "EmmaX.Hose == 'garterbelt'", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Feet.png",
            "EmmaX.Hose == 'ripped pantyhose'", Recolor("Emma", "Hose", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Feet_Hose_Holed.png"),
            "EmmaX.Hose", Recolor("Emma", "Hose", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Feet_Hose.png"),
            "True", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Feet.png",
            )
    contains:
            # feet pants
        ConditionSwitch(
            "(EmmaX.Legs == 'pants' or EmmaX.Legs == 'yoga pants') and EmmaX.Upskirt", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_Pants_Down.png"),
            "EmmaX.Boots == 'thigh boots'", Recolor("Emma", "Boots", "images/EmmaSex/Emma_Sex_Feet_Boots.png"),
            "EmmaX.Legs == 'pants'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_Feet_Pants.png"),
            "EmmaX.Legs == 'yoga pants'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_Feet_YogaPants.png"),
            "True", Null(),
            )
    contains:
            # panties down pants
        ConditionSwitch(
            "(EmmaX.Legs == 'pants' or EmmaX.Legs == 'yoga pants') and not EmmaX.Upskirt", Null(),
            "not EmmaX.PantiesDown", Null(),
            "EmmaX.Panties == 'sports panties'", Recolor("Emma", "Panties", "images/EmmaSex/Emma_Sex_Panties_Sport_Down.png"),
            "EmmaX.Panties == 'bikini bottoms'", Recolor("Emma", "Panties", "images/EmmaSex/Emma_Sex_Panties_Bikini_Down.png"),
            "EmmaX.Panties", Recolor("Emma", "Panties", "images/EmmaSex/Emma_Sex_Panties_Down.png"),
            "True", Null(),
            )
    contains:
            # back of dress
        ConditionSwitch(
            "EmmaX.Legs == 'dress'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_Dress_S_Back.png"),
            "True", Null(),
            )
    contains:
            # spunk
        ConditionSwitch(
            "('anal' in EmmaX.Spunk or 'in' in EmmaX.Spunk) and Player.Male", "images/EmmaSex/Emma_Spunk_Sex.png",
            "True", Null(),
            )
    contains:
            # Legs base
        ConditionSwitch(
            "Trigger == 'hotdog'", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Legs_Hotdog.png",
            "True", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Legs_Sex.png",
            )
    contains:
            # stockings
        ConditionSwitch(
            "EmmaX.Hose == 'stockings'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_Sex_Hose_Stockings_S.png"),
            "EmmaX.Hose == 'stockings and garterbelt'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_Sex_Hose_StockingsGarter_S.png"),
            "EmmaX.Hose == 'garterbelt'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_Sex_Hose_Garter_S.png"),
            "True", Null(),
            )
    contains:
            # piercings
        ConditionSwitch(
            "EmmaX.Pierce == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_S.png",
            "(EmmaX.Legs == 'pants' or EmmaX.Legs == 'yoga pants') and not EmmaX.Upskirt", Null(),
            "EmmaX.Panties and not EmmaX.PantiesDown", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S_C2.png",
            "EmmaX.Hose == 'pantyhose' and not EmmaX.PantiesDown", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S_C2.png",
            "EmmaX.Pierce == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S.png",
            "True", Null(),
            )
    contains:
            # pubes
        ConditionSwitch(
            "EmmaX.Pubes", Recolor("Emma", "Pubes", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Pubes_Sex.png"),
            "True", Null(),
            )
    contains:
            # panties
        ConditionSwitch(
            "EmmaX.PantiesDown", Null(),
            "EmmaX.Panties == 'sports panties' and EmmaX.Wet", Recolor("Emma", "Panties", "images/EmmaSex/Emma_Sex_Panties_Sport_SW.png"),
            "EmmaX.Panties == 'sports panties'", Recolor("Emma", "Panties", "images/EmmaSex/Emma_Sex_Panties_Sport_S.png"),
            "EmmaX.Panties == 'lace panties'", Recolor("Emma", "Panties", "images/EmmaSex/Emma_Sex_Panties_Lace_S.png"),
            "EmmaX.Panties == 'bikini bottoms'", Recolor("Emma", "Panties", "images/EmmaSex/Emma_Sex_Panties_Bikini_S.png"),
            "EmmaX.Panties and EmmaX.Wet", Recolor("Emma", "Panties", "images/EmmaSex/Emma_Sex_Panties_SW.png"),
            "EmmaX.Panties", Recolor("Emma", "Panties", "images/EmmaSex/Emma_Sex_Panties_S.png"),
            "True", Null(),
            )
    contains:
            # pantyhose
        ConditionSwitch(
            "(EmmaX.Panties and EmmaX.PantiesDown)", Null(),
            "EmmaX.Hose == 'ripped pantyhose'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_Sex_Hose_PantyhoseHoled_S.png"),
            "Player.Sprite and Player.Cock == 'in'", Null(),
            "EmmaX.Hose == 'pantyhose'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_Sex_Hose_Pantyhose_S.png"),
            "True", Null(),
            )
    contains:
            # piercings
        ConditionSwitch(
            "(not EmmaX.Panties and EmmaX.Hose != 'pantyhose') or EmmaX.PantiesDown", Null(),
            "EmmaX.Hose == 'pantyhose' and EmmaX.PantiesDown", Null(),
            "EmmaX.Pierce == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_S_C.png",
            "EmmaX.Pierce == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S_C.png",
            "True", Null(),
            )
    contains:
            # legs
        ConditionSwitch(
            "EmmaX.Legs == 'dress' and (EmmaX.Upskirt or Player.Sprite)", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_Dress_S_Up.png"),
            "EmmaX.Legs == 'dress'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_Dress_S.png"),
            "EmmaX.Legs == 'skirt'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_Skirt_Pussy.png"),
            "EmmaX.Upskirt", Null(),
            "EmmaX.Legs == 'pants' and EmmaX.Wet >= 2", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_Pants_SW.png"),
            "EmmaX.Legs == 'pants'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_Pants_S.png"),
            "EmmaX.Legs == 'yoga pants' and EmmaX.Wet >= 2", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_YogaPants_SW.png"),
            "EmmaX.Legs == 'yoga pants'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_YogaPants_S.png"),
            # Modification mode
            "EmmaX.Legs == 'bottom harem' and EmmaX.Upskirt", "images/EmmaSex/modification/Emma_sex_legs_harem_bottom_down.png",
            "EmmaX.Legs == 'bottom harem'", "images/EmmaSex/modification/Emma_sex_legs_harem_bottom.png",
            # -----------------
            "True", Null(),
            )
    contains:
            # piercings over
        ConditionSwitch(
            "(EmmaX.Legs != 'pants' and EmmaX.Legs != 'yoga pants') or EmmaX.Upskirt", Null(),
            "EmmaX.Pierce == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_S_C.png",
            "EmmaX.Pierce != 'ring'", Null(),
            "EmmaX.Panties and not EmmaX.PantiesDown", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S_C.png",
            "EmmaX.Hose == 'pantyhose' and not EmmaX.PantiesDown", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S_C.png",
            "True", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S_C.png",
            )
    contains:
            # boots
        ConditionSwitch(
            "(EmmaX.Legs == 'pants' or EmmaX.Legs == 'yoga pants') and EmmaX.Upskirt", Null(),
            "EmmaX.Boots == 'thigh boots'", Recolor("Emma", "Boots", "images/EmmaSex/Emma_Sex_Boots_Pussy.png"),
            "True", Null(),
            )
    contains:
            # Over
        ConditionSwitch(
            "EmmaX.Over == 'nighty'", Recolor("Emma", "Over", "images/EmmaSex/Emma_Sex_Nighty_Pussy.png"),
            "True", Null(),
            )
    contains:
            # spunk
        ConditionSwitch(
            "'belly' in EmmaX.Spunk and Player.Male", "images/EmmaSex/Emma_Spunk_Belly.png",
            "True", Null(),
            )
    zoom 1
#    offset (0,0)

image Emma_Sex_Legs_A:
    #Her Legs during anal
    contains:
            # back of dress
        ConditionSwitch(
            "EmmaX.Legs == 'dress'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_Dress_A_Back.png"),
            "True", Null(),
            )
    contains:
        ConditionSwitch(
            #plug
            "EmmaX.Plug", "images/PlugBase_Sex.png",
            "True", Null(),
            )
#        "images/PlugBase_Sex.png"
        offset (-280,-140) #(-285,-140)
        zoom 1.4
    contains:
            # anal spunk
        ConditionSwitch(
            "'anal' in EmmaX.Spunk and not Speed and Player.Male", "images/EmmaSex/Emma_Spunk_Anal_Closed.png",
            "True", Null(),
            )
    contains:
            # Legs Base

        ConditionSwitch(
            "Trigger == 'lick pussy'", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Legs_Licking.png",
            "True", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Legs_Anal.png"
            )
    contains:
            #Anus
        ConditionSwitch(
            "Player.Sprite and Player.Cock == 'anal' and Speed", ConditionSwitch(
                    # If during Anal
                    "Speed == 1", "Emma_Sex_Anus_A1",#heading
                    "True", "Emma_Sex_Anus_A2",#faster
                    ),
            "True", "Emma_Sex_Anus_A0",
            )
    contains:
            # pubes
        ConditionSwitch(
            "EmmaX.Pubes", Recolor("Emma", "Pubes", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Pubes_Anal.png"),
            "True", Null(),
            )
    contains:
            # piercings
        ConditionSwitch(
            "EmmaX.Panties and not EmmaX.PantiesDown", Null(),
            "(EmmaX.Legs == 'pants' or EmmaX.Legs == 'yoga pants') and not EmmaX.Upskirt", Null(),
            "EmmaX.Pierce == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_A.png",
            "EmmaX.Pierce == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_A.png",
            "True", Null(),
            )
    contains:
            # stockings
        ConditionSwitch(
            "EmmaX.Hose == 'stockings'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_Sex_Hose_Stockings_A.png"),
            "EmmaX.Hose == 'stockings and garterbelt'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_Sex_Hose_StockingsGarter_A.png"),
            "EmmaX.Hose == 'garterbelt'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_Sex_Hose_Garter_A.png"),
            "True", Null(),
            )
    contains:
            # panties
        ConditionSwitch(
            "EmmaX.PantiesDown", Null(),
            "EmmaX.Panties == 'sports panties' and EmmaX.Wet", Recolor("Emma", "Panties", "images/EmmaSex/Emma_Sex_Panties_Sport_AW.png"),
            "EmmaX.Panties == 'sports panties'", Recolor("Emma", "Panties", "images/EmmaSex/Emma_Sex_Panties_Sport_A.png"),
            "EmmaX.Panties == 'lace panties'", Recolor("Emma", "Panties", "images/EmmaSex/Emma_Sex_Panties_Lace_A.png"),
            "EmmaX.Panties == 'bikini bottoms'", Recolor("Emma", "Panties", "images/EmmaSex/Emma_Sex_Panties_Bikini_A.png"),
            "EmmaX.Panties and EmmaX.Wet", Recolor("Emma", "Panties", "images/EmmaSex/Emma_Sex_Panties_AW.png"),
            "EmmaX.Panties", Recolor("Emma", "Panties", "images/EmmaSex/Emma_Sex_Panties_A.png"),
            "True", Null(),
            )
    contains:
            # pussy spunk
        ConditionSwitch(
            "'in' in EmmaX.Spunk and Player.Male", "images/EmmaSex/Emma_Spunk_Anal_Pussy.png",
            "True", Null(),
            )
    contains:
            # pantyhose
        ConditionSwitch(
            "(EmmaX.Panties and EmmaX.PantiesDown)", Null(),
            "EmmaX.Hose == 'ripped pantyhose'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_Sex_Hose_PantyhoseHoled_A.png"),
            "Player.Sprite and Player.Cock == 'anal'", Null(),
            "EmmaX.Hose == 'pantyhose'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_Sex_Hose_Pantyhose_A.png"),
            "True", Null(),
            )
    contains:
            # piercings over panties
        ConditionSwitch(
            "(not EmmaX.Panties and EmmaX.Hose != 'pantyhose') or EmmaX.PantiesDown", Null(),
            "EmmaX.Hose == 'pantyhose' and EmmaX.PantiesDown", Null(),
            "EmmaX.Pierce == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_A_C.png",
            "EmmaX.Pierce == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_A_C.png",
            "True", Null(),
            )
    contains:
            # legs
        ConditionSwitch(
            "EmmaX.Legs == 'dress' and (EmmaX.Upskirt or Player.Sprite)", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_Dress_A_Up.png"),
            "EmmaX.Legs == 'dress'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_Dress_A.png"),
            "EmmaX.Legs == 'skirt'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_Skirt_Anal.png"),
            "EmmaX.Upskirt", Null(),
            "EmmaX.Legs == 'pants' and EmmaX.Wet >= 2", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_Pants_AW.png"),
            "EmmaX.Legs == 'pants'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_Pants_A.png"),
            "EmmaX.Legs == 'yoga pants' and EmmaX.Wet >= 2", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_YogaPants_AW.png"),
            "EmmaX.Legs == 'yoga pants'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_YogaPants_A.png"),
            # Modification mode
            "EmmaX.Legs == 'bottom harem' and EmmaX.Wet >= 2", Null(),
            "EmmaX.Legs == 'bottom harem'", Null(),
            # -----------------
            "True", Null(),
            )
    contains:
            # piercings over pants
        ConditionSwitch(
            "(EmmaX.Legs != 'pants' and EmmaX.Legs != 'yoga pants') or EmmaX.Upskirt", Null(),
            "EmmaX.Pierce == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_A_C.png",
            "EmmaX.Pierce != 'ring'", Null(),
            "EmmaX.Panties and not EmmaX.PantiesDown", "images/EmmaSex/Emma_Pierce_Ring_Pussy_A_C.png",
            "EmmaX.Hose == 'pantyhose' and not EmmaX.PantiesDown", "images/EmmaSex/Emma_Pierce_Ring_Pussy_A_C.png",
            "True", "images/EmmaSex/Emma_Pierce_Ring_Pussy_A_C.png",
            )
    contains:
            # boots
        ConditionSwitch(
            "EmmaX.Boots == 'thigh boots'", Recolor("Emma", "Boots", "images/EmmaSex/Emma_Sex_Boots_Anal.png"),
            "True", Null(),
            )
    contains:
            # Over
        ConditionSwitch(
            "EmmaX.Over == 'nighty'", Recolor("Emma", "Over", "images/EmmaSex/Emma_Sex_Nighty_Anal.png"),
            "True", Null(),
            )
    contains:
            # spunk
        ConditionSwitch(
            "'belly' in EmmaX.Spunk and Player.Male", "images/EmmaSex/Emma_Spunk_Belly.png",
            "True", Null(),
            )
        ypos -40
    contains:
        ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy'", "Emma_Sex_Lick_Pussy",
            "Trigger == 'lick ass'", "Emma_Sex_Lick_Ass",
            "True", Null()
            )
    zoom 1
#    offset (0,0)

image Emma_Sex_Pussy_Mask:
    contains:
            "images/EmmaSex/Emma_Sex_Pussy_Mask.png"
    contains:
            # piercings
        ConditionSwitch(
            "EmmaX.Panties and not EmmaX.PantiesDown", Null(),
            "EmmaX.Legs and not EmmaX.Upskirt", Null(),
            "EmmaX.Pierce == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_S.png",
            "EmmaX.Pierce == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S.png",
            "True", Null(),
            )

image Emma_Sex_Hotdog_Mask:
    contains:
            "images/EmmaSex/Emma_Sex_Legs_HotdogMask.png"
#            yoffset 3
    contains:
            # piercings
        ConditionSwitch(
            "EmmaX.Panties and not EmmaX.PantiesDown", Null(),
            "EmmaX.Legs and not EmmaX.Upskirt", Null(),
            "EmmaX.Pierce == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_S.png",
            "EmmaX.Pierce == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S.png",
            "True", Null(),
            )
    contains:
            # piercings
        ConditionSwitch(
            "EmmaX.Panties and not EmmaX.PantiesDown", Null(),
            "EmmaX.Legs and not EmmaX.Upskirt", Null(),
            "EmmaX.Pierce == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_S.png",
            "EmmaX.Pierce == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S.png",
            "True", Null(),
            )

# Emma's sex body legs / / / / / legs / / / / / legs / / / / / legs / / / / / legs / / / / /



#  Sex animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Emma_Sex_Body_Lick:
    #Her Body in the licking pose
    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-80) #top (0,-40)
        block:
            ease 1 pos (0,-90) #bottom   (0,-20)
            ease 1 pos (0,-80) #top
            repeat

image Emma_Sex_Legs_Lick:
    # Her Legs in the anal pose, idle
    contains:
            #Base Legs
            "Emma_Sex_Legs_A"
            subpixel True
            pos (0,-50) #top (0,-138)
#            block:
#                ease 1 ypos -45 #bottom -15
#                ease 1 ypos -40 #top -10
#                repeat
    # End Sex Legs Anal Idle

image Emma_Sex_Lick_Pussy:
        "Lick_Anim"
        zoom 0.7
        offset (505,680) #(530,510) 680

image Emma_Sex_Lick_Ass:
        "Lick_Anim"
        zoom 0.7
        offset (500,740) # (535,590)


image Emma_Sex_Body_H0:
    #Her Body in the hotdog pose, idle
    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-10) #top
        block:
            ease 2 pos (0,0) #bottom
            ease 2 pos (0,-10) #top
            repeat

image Emma_Sex_Body_H1:
    #Her Body in the hotdog pose, slow
    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-10) #top
        block:
            ease 1.5 pos (0,0) #bottom
            ease 1.5 pos (0,-10) #top
            repeat

image Emma_Sex_Body_H2:
    #Her Body in the hotdog pose, fast
    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-10) #top
        block:
            ease .6 pos (0,10) #bottom
            ease .4 pos (0,-10) #top
            repeat

image Emma_Sex_Body_H4:
    #Her Body in the hotdog pose, cumming
    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-80) #top
        block:
            ease 1.5 pos (0,-70) #bottom
            ease 2 pos (0,-80) #top
            pause .5
            repeat

image Emma_Sex_Body_S0:
    #Her Body in the sex pose, idle
    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-60) #top (0,-10)
        block:
            ease 1 pos (0,-50) #bottom (0,0)
            ease 1 pos (0,-60) #top
            repeat

image Emma_Sex_Body_S1:
    #Her Body in the sex pose, slow
    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-20) #top
        block:
            ease .75 pos (0,0) #bottom
            ease 1.5 pos (0,-20) #top
            pause 0.75
            repeat

image Emma_Sex_Body_S2:
    #Her Body in the sex pose, fast
    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-50) #top
        block:
            ease 0.5 pos (0,20) #bottom
            ease 1.5 pos (0,-50) #top
#            pause 0.5
            repeat

image Emma_Sex_Body_S3:
    #Her Body in the sex pose, superfast
    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-50) #top
        block:
            ease 0.25 pos (0,0) #bottom
            ease 0.5 pos (0,-50) #top
            repeat

image Emma_Sex_Body_S4:
    #Her Body in the sex pose, cumming
    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-20) #top
        block:
            ease 0.5 pos (0,0) #bottom
            ease 1 pos (0,-20) #top
            repeat

image Emma_Sex_Body_A0:
    #Her Body in the anal pose, idle
    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-115) #top (0,-20)
        block:
            ease 1 pos (0,-95) #bottom (0,-10)
            ease 1 pos (0,-115) #top
            repeat

image Emma_Sex_Body_A1:
    #Her Body in the anal pose, slow
    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-80) #top (0,-40)
        block:
            easeout 1 pos (0,-60) #bottom   (0,-20)
            easein 2 pos (0,-40) #bottom  (0,0)
            pause 1
            easeout 1 pos (0,-60) #top (0,-20)
            easein 2 pos (0,-80) #top
            pause 1
            repeat

image Emma_Sex_Body_A2:
    #Her Body in the anal pose, fast
    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-10) #top
        block:
            ease .30 pos (0,10) #mid
            ease .50 pos (0,50) #bottom
            pause .3
            ease .80 pos (0,-10) #top
            pause .1
            repeat

image Emma_Sex_Body_A3:
    #Her Body in the anal pose, very fast
    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-10) #top
        block:
            ease .40 pos (0,50) #bottom
            ease .60 pos (0,-10) #top
            repeat

image Emma_Sex_Body_A4:
    #Her Body in the anal pose, cumming
    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,20) #top (0,-20)
        block:
            ease 1 pos (0,40) #bottom (0,-10)
            ease 1 pos (0,20) #top
            repeat


# Leg animations / / / / / / Legs / / / / / / Legs / / / / / / Legs / / / / / / Legs / / / / / /
image Emma_Sex_Legs_H0:
    # Her Legs in the Hotdog pose, idle
    contains:
            #Body
            "Emma_Sex_Legs_S"
            subpixel True
            anchor (.515,.5)
            pos (528,340) #top (528,300)
            zoom .95
            parallel:
                ease 2 zoom .98 #bottom
                ease 2 zoom .95 #top
#                pause .3
                repeat
            parallel:
                ease 2 ypos 360 #bottom
                ease 2 ypos 340 #top
#                pause .3
                repeat
    contains:
            #Cock
            ConditionSwitch(
                "Player.Sprite", "Zero_Doggy_Insert",
                "True", Null(),
                )
            alpha 1
            zoom 1.2
            pos (450,590)
    contains:
            #Overlay
            AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Hotdog_Mask")#"images/EmmaSex/Emma_Sex_Legs_HotdogMask.png")
            subpixel True
            anchor (.515,.5)
            pos (528,340) #top (528,300)
            zoom .95
            parallel:
                ease 2 zoom .98 #bottom
                ease 2 zoom .95 #top
#                pause .3
                repeat
            parallel:
                ease 2 ypos 360 #bottom
                ease 2 ypos 340 #top
#                pause .3
                repeat
    # End Legs Hotdog Idle

image Emma_Sex_Legs_H1:
    # Her Legs in the Hotdog pose, slow
    contains:
            #Body
            "Emma_Sex_Legs_S"
            subpixel True
            anchor (.515,.5)
            pos (528,300) #top (528,300)
            zoom .9
            parallel:
                ease 1.5 zoom 1 #bottom
                ease 1.5 zoom .9 #top
                pause .3
                repeat
            parallel:
                ease 1.5 ypos 390 #bottom
                ease 1.5 ypos 300 #top
                pause .3
                repeat
    contains:
            #Cock
            ConditionSwitch(
                "Player.Sprite", "Zero_Doggy_Insert",
                "True", Null(),
                )
            alpha 1
            zoom 1.2
            pos (450,590)
    contains:
            #Overlay
            AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Hotdog_Mask")#"images/EmmaSex/Emma_Sex_Legs_HotdogMask.png")
            subpixel True
            anchor (.515,.5)
            pos (528,300) #top(515,300)
            zoom .9
            parallel:
                ease 1.5 zoom 1 #bottom
                ease 1.5 zoom .9 #top
                pause .3
                repeat
            parallel:
                ease 1.5 ypos 390 #bottom
                ease 1.5 ypos 300 #top
                pause .3
                repeat
    # End Legs Hotdog slow

image Emma_Sex_Legs_H2:
    # Her Legs in the Hotdog pose, fast
    contains:
            #Body
            "Emma_Sex_Legs_S"
            subpixel True
            anchor (.515,.5)
            pos (528,340) #top (528,300)
            zoom .95
            parallel:
                ease .6 zoom 1 #bottom
                ease .4 zoom .95 #top
#                pause .3
                repeat
            parallel:
                ease .6 ypos 390 #bottom
                ease .4 ypos 340 #top
#                pause .3
                repeat
    contains:
            #Cock
            ConditionSwitch(
                "Player.Sprite", "Zero_Doggy_Insert",
                "True", Null(),
                )
            alpha 1
            zoom 1.2
            pos (450,590)
    contains:
            #Overlay
            AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Hotdog_Mask")#"images/EmmaSex/Emma_Sex_Legs_HotdogMask.png")
            subpixel True
            anchor (.515,.5)
            pos (528,340) #top (528,300)
            zoom .95
            parallel:
                ease .6 zoom 1 #bottom
                ease .4 zoom .95 #top
#                pause .3
                repeat
            parallel:
                ease .6 ypos 390 #bottom
                ease .4 ypos 340 #top
#                pause .3
                repeat
    # End Legs Hotdog fast

image Emma_Sex_Legs_H4:
    # Her Legs in the Hotdog pose, cumming
    contains:
            #Body
            "Emma_Sex_Legs_S"
            subpixel True
#            anchor (.515,.5)
            pos (0,-80) #top
            parallel:
                ease 2 ypos -70 #bottom
                ease 2 ypos -80 #top
                repeat

    contains:
            #Cock
            "Blowcock"
            alpha 1
            zoom 0.5
            pos (680,440)
#    contains:
#            #Cock
#            ConditionSwitch(
#                "Player.Sprite", "Zero_Doggy_Insert",
#                "True", Null(),
#                )
#            alpha 1
#            zoom 1.2
#            pos (450,590)
#    contains:
#            #Overlay
#            AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Hotdog_Mask")#"images/EmmaSex/Emma_Sex_Legs_HotdogMask.png")
#            subpixel True
#            anchor (.515,.5)
#            pos (528,340) #top (528,300)
#            zoom .95
#            parallel:
#                ease 2 zoom .98 #bottom
#                ease 2 zoom .95 #top
##                pause .3
#                repeat
#            parallel:
#                ease 2 ypos 360 #bottom
#                ease 2 ypos 340 #top
##                pause .3
#                repeat
    # End Legs Hotdog Idle

# Emma's sex legs animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_Sex_Legs_S0:
    # Her Legs in the Sex pose, idle
    contains:
            #Body
            "Emma_Sex_Legs_S"
            subpixel True
            pos (0,-140) #top
            parallel:
                ease 1 ypos -135 #bottom
                ease 1 ypos -140 #top
                repeat
            parallel:
                ease 2 xpos -8 #bottom
                ease 2 xpos 8 #top
                repeat
    contains:
            #Cock
            ConditionSwitch(
                "AlphaCock", "Blowcock",
                "True", "Ghostcock",
                )
            alpha 1
            zoom 0.5
            pos (680,400)
    contains:
            #Overlay
            AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Pussy_Mask")#"images/EmmaSex/Emma_Sex_Pussy_Mask.png")
            subpixel True
            pos (0,-140) #top
            parallel:
                ease 1 ypos -135 #bottom
                ease 1 ypos -140 #top
                repeat
            parallel:
                ease 2 xpos -8 #bottom
                ease 2 xpos 8 #top
                repeat
    # End Legs Sex Idle

image Emma_Sex_Legs_S1:
    # Her Legs in the Sex pose, slow
    contains:
            #Body
            "Emma_Sex_Legs_S"
            subpixel True
            pos (0,-120) #top
            block:
                ease 0.75 ypos -50 #bottom
                pause 0.75
                ease 1.5 ypos -120 #top
                repeat
    contains:
            #Cock
            ConditionSwitch(
                "AlphaCock", "Blowcock",
                "True", "Ghostcock",
                )
            subpixel True
            alpha 1
            zoom 0.5
            pos (680,400)
            block:
                ease 0.8 ypos 410
                pause 1
                ease 1.2 ypos 400
                repeat
    contains:
            #Overlay
            AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Pussy_Mask")
            subpixel True
            pos (0,-120) #top
            block:
                ease 0.75 ypos -50  #bottom
                pause 0.75
                ease 1.5 ypos -120 #top
                repeat
    # End Legs Sex slow

image Emma_Sex_Legs_S2:
    # Her Legs in the Sex pose, fast
    contains:
            #Body
            "Emma_Sex_Legs_S"
            subpixel True
            pos (0,-150) #top
            block:
                ease 0.5 ypos 0 #bottom
                pause 0.5
                ease 1 ypos -150 #top
                repeat
    contains:
            #Cock
            ConditionSwitch(
                "AlphaCock", "Blowcock",
                "True", "Ghostcock",
                )
            subpixel True
            alpha 1
            zoom 0.5
            pos (680,400)
            block:
                ease 0.4 ypos 430
                pause 1
                ease 0.6 ypos 400
                repeat
    contains:
            #Overlay
            AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Pussy_Mask")
            subpixel True
            pos (0,-150) #top
            block:
                ease 0.5 ypos 0 #bottom
                pause 0.5
                ease 1 ypos -150 #top
                repeat
    # End Legs Sex fast

image Emma_Sex_Legs_S3:
    # Her Legs in the Sex pose, very fast
    contains:
            #Body
            "Emma_Sex_Legs_S"
            subpixel True
            pos (0,-120) #top
            block:
                ease 0.25 ypos 10 #bottom
                ease 0.5 ypos -120 #top
                repeat
    contains:
            #Cock
            ConditionSwitch(
                "AlphaCock", "Blowcock",
                "True", "Ghostcock",
                )
            subpixel True
            alpha 1
            zoom 0.5
            pos (680,400)
            block:
                ease 0.2 ypos 430
                ease 0.55 ypos 400
                repeat
    contains:
            #Overlay
            AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Pussy_Mask")
            subpixel True
            pos (0,-120) #top
            block:
                ease 0.25 ypos 10 #bottom
                ease 0.5 ypos -120 #top
                repeat
    # End Legs Sex very fast

image Emma_Sex_Legs_S4:
    # Her Legs in the Sex pose, cumming
    contains:
            #Body
            "Emma_Sex_Legs_S"
            subpixel True
            pos (0,0) #top
            block:
                ease 0.5 ypos 10 #bottom
                ease 1 ypos 0 #top
                repeat
    contains:
            #Cock
            ConditionSwitch(
                "AlphaCock", "Blowcock",
                "True", "Ghostcock",
                )
            subpixel True
            alpha 1
            zoom 0.5
            pos (680,430)
    contains:
            #Overlay
            AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Pussy_Mask")
            subpixel True
            pos (0,0) #top
            block:
                ease 0.5 ypos 10 #bottom
                ease 1 ypos 0 #top
                repeat
    # End Legs Sex cumming
# Anal / / / / / / Anal / / / / / / Anal / / / / / / Anal / / / / / / Anal / / / / / /

image Emma_Sex_Legs_A0:
    # Her Legs in the anal pose, idle
    contains:
            #Base Legs
            "Emma_Sex_Legs_A"
            subpixel True
            pos (0,-138) #top
            block:
                ease 1 ypos -134 #bottom
                ease 1 ypos -138 #top
                repeat
    contains:
            #Cock
            ConditionSwitch(
                "AlphaCock", "Blowcock",
                "True", "Ghostcock",
                )
#            alpha .5
            zoom 0.5
            pos (681,420)
    # End Sex Legs Anal Idle

image Emma_Sex_Legs_A1:
    # Her Legs in the anal pose, slow
    contains:
            #Base Legs
            "Emma_Sex_Legs_A"
            subpixel True
            pos (0,-130) #top
            block:
                ease 4 ypos -80 #bottom
                ease 4 ypos -130 #top
                repeat
    contains:
            #Cock
            ConditionSwitch(
                "AlphaCock", "Blowcock",
                "True", "Ghostcock",
                )
#            alpha .5
            zoom 0.5
            pos (681,420)
    contains:
            #Overlay
            contains:
                AlphaMask("Emma_Sex_Legs_A", "Emma_Sex_Anus_Mask_A1")
            contains:
                    # spunk
                ConditionSwitch(
                    "'anal' in EmmaX.Spunk and Player.Male", "images/EmmaSex/Emma_Spunk_Anal_Heading.png",
                    "True", Null(),
                    )
                transform_anchor True
                xpos 500
                anchor (500,0)
                xzoom 0.6
                parallel:
                    #8 total
                    pause .2
                    ease 2.2 xzoom 0.9 #bottom
                    ease 0.6 xzoom 0.85 #bottom

                    ease 0.75 xzoom 0.9 #bottom
                    pause 0.5
                    ease 0.75 xzoom 0.85 #bottom

                    ease 0.6 xzoom 0.9 #bottom
                    ease 2.2 xzoom 0.6 #top
                    pause .2
                    repeat
            subpixel True
            pos (0,-130) #top
            block:
                ease 4 ypos -80 #bottom
                ease 4 ypos -130 #top
                repeat
    # End Sex Legs Anal slow

image Emma_Sex_Anus_Mask_A1:
    #mask for the slow anal pose
    contains:
        contains:
            "images/EmmaSex/Emma_Sex_Anus_Mask.png"
        subpixel True
        transform_anchor True
        xpos 500
        anchor (500,0)
        xzoom 0.5
        parallel:
            #8 total
            pause .2
            ease 2.2 xzoom 0.9 #bottom
            ease 0.6 xzoom 0.85 #bottom

            ease 0.75 xzoom 0.9 #bottom
            pause 0.5
            ease 0.75 xzoom 0.85 #bottom

            ease 0.6 xzoom 0.9 #bottom
            ease 2.2 xzoom 0.5 #top
            pause .2
            repeat
#        parallel:
#            pause .2
#            ease 2.2 xpos 50 #bottom
#            ease 0.6 xpos 75 #bottom 125=75%

#            ease 0.75 xpos 50 #bottom
#            pause 0.5
#            ease 0.75 xpos 75 #bottom

#            ease 0.6 xpos 50 #bottom
#            ease 2.2 xpos 250 #top
#            pause .2
#            repeat
    #end animation for mask in slow anal

image Emma_Sex_Legs_A2:
    # Her Legs in the anal pose, fast
    contains:
            #Base Legs
            "Emma_Sex_Legs_A"
            pos (0,-80) #top
            subpixel True
            block:
                ease 1 ypos 0 #bottom
                ease 1 ypos -80 #top
                repeat
    contains:
            #Cock
            ConditionSwitch(
                "AlphaCock", "Blowcock",
                "True", "Ghostcock",
                )
            subpixel True
#            alpha .5
            zoom 0.5
            pos (681,420)
            block:
                ease 1 ypos 430
                ease 1 ypos 400
                repeat
    contains:
            #Overlay
            contains:
                    AlphaMask("Emma_Sex_Legs_A", "images/EmmaSex/Emma_Sex_Anus_Mask.png" )
            contains:
                    # spunk
                ConditionSwitch(
                    "'anal' in EmmaX.Spunk and Player.Male", "images/EmmaSex/Emma_Spunk_Anal_Open.png",
                    "True", Null(),
                    )
            subpixel True
            pos (0,-80) #top
            block:
                ease 1 ypos 0 #bottom
                ease 1 ypos -80 #top
                repeat
    # End Sex Legs Anal fast

image Emma_Sex_Legs_A3:
    # Her Legs in the anal pose, very fast
    contains:
            #Base Legs
            "Emma_Sex_Legs_A"
            subpixel True
            pos (0,-80) #top
            block:
                ease 0.5 ypos 20 #bottom
                ease 0.5 ypos -80 #top
                repeat
    contains:
            #Cock
            ConditionSwitch(
                "AlphaCock", "Blowcock",
                "True", "Ghostcock",
                )
            subpixel True
#            alpha .5
            zoom 0.5
            pos (681,420)
            block:
                ease 0.5 ypos 430
                ease 0.5 ypos 400
                repeat
    contains:
            #Overlay
            contains:
                    AlphaMask("Emma_Sex_Legs_A", "images/EmmaSex/Emma_Sex_Anus_Mask.png" )
            contains:
                    # spunk
                ConditionSwitch(
                    "'anal' in EmmaX.Spunk and Player.Male", "images/EmmaSex/Emma_Spunk_Anal_Open.png",
                    "True", Null(),
                    )
            subpixel True
            pos (0,-80) #top
            block:
                ease 0.5 ypos 20 #bottom
                ease 0.5 ypos -80 #top
                repeat
    # End Sex Legs Anal very fast

image Emma_Sex_Legs_A4:
    # Her Legs in the anal pose, cumming
    contains:
            #Base Legs
            "Emma_Sex_Legs_A"
            subpixel True
            pos (0,15) #top
            block:
                ease 1 ypos 20 #bottom
                ease 1 ypos 15 #top
                repeat
    contains:
            #Cock
            ConditionSwitch(
                "AlphaCock", "Blowcock",
                "True", "Ghostcock",
                )
            subpixel True
#            alpha .5
            zoom 0.5
            pos (681,430)
    contains:
            #Overlay
            contains:
                    AlphaMask("Emma_Sex_Legs_A", "images/EmmaSex/Emma_Sex_Anus_Mask.png" )
            contains:
                    # spunk
                ConditionSwitch(
                    "'anal' in EmmaX.Spunk and Player.Male", "images/EmmaSex/Emma_Spunk_Anal_Open.png",
                    "True", Null(),
                    )
            subpixel True
            pos (0,15) #top
            block:
                ease 1 ypos 20 #bottom
                ease 1 ypos 15 #top
                repeat
    # End Sex Legs Anal cumming

image Emma_Sex_Anus_A0:
        #this is the animated stretched anus
        "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Anus_Tight.png"
        xpos  0

image Emma_Sex_Anus_A1:
        #this is the animated stretched anus
        contains:
            "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Anus_Open.png"
        contains:
                # spunk
            ConditionSwitch(
                "'anal' in EmmaX.Spunk and Player.Male", "images/EmmaSex/Emma_Spunk_Anal_Under.png",
                "True", Null(),
                )
        subpixel True
        transform_anchor True
        xpos 500
        anchor (500,0)
        xzoom 0.5
#        xpos  250
        parallel:
            #8 total
            pause .2
            ease 2.2 xzoom 0.9 #bottom
            ease 0.6 xzoom 0.85 #bottom

            ease 0.75 xzoom 0.9 #bottom
            pause 0.5
            ease 0.75 xzoom 0.85 #bottom

            ease 0.6 xzoom 0.9 #bottom
            ease 2.2 xzoom 0.5 #top
            pause .2
            repeat
#        parallel:
#            pause .2
#            ease 2.2 xpos 50 #bottom
#            ease 0.6 xpos 75 #bottom 125=75%

#            ease 0.75 xpos 50 #bottom
#            pause 0.5
#            ease 0.75 xpos 75 #bottom

#            ease 0.6 xpos 50 #bottom
#            ease 2.2 xpos 250 #top
#            pause .2
#            repeat
        #end animation for anus in slow animation

image Emma_Sex_Anus_A2:
        #this is the animated stretched anus
        contains:
            "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Anus_Open.png"
        contains:
                # spunk
            ConditionSwitch(
                "'anal' in EmmaX.Spunk and Player.Male", "images/EmmaSex/Emma_Spunk_Anal_Under.png",
                "True", Null(),
                )
        xpos  0

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Emma_Sex_Launch(Line = Trigger):
        $ EmmaX.Offhand = 0 if EmmaX.Offhand == "hand" else EmmaX.Offhand
#        #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#        $ EmmaX.Pose = 0
#        #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
        $ Line = "solo" if not Line else Line
        if Line == "sex":
            $ Player.Sprite = 1
            $ Player.Cock = "in"
            call Cock_Occupied(EmmaX,"pussy")
            if Trigger2 in ("fondle pussy","dildo pussy","lick pussy"):
                    $ Trigger2 = 0
        elif Line == "anal":
            $ Player.Sprite = 1
            $ Player.Cock = "anal"
            call Cock_Occupied(EmmaX,"anal")
            if Trigger2 in ("insert ass","dildo anal","lick ass"):
                    $ Trigger2 = 0
        elif Line == "hotdog":
            $ Player.Sprite = 1
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
            call Zero_Strapped(EmmaX) #puts strap-on on.
#        if not Trigger:
        $ Trigger = Line

        if EmmaX.Pose == "doggy":
                call Emma_Doggy_Launch(Line)
                return
        elif Line == "foot":
                call Emma_FJ_Launch
                return
        if renpy.showing("Emma_SexSprite"):
                return
        $ Speed = 0
        call Girl_Hide(EmmaX,1)

#        show Emma_SexSprite zorder 150:
#            pos (575,470)
        show Emma_SexSprite zorder 150
        with dissolve
        return

label Emma_Sex_Reset:
        if renpy.showing("Emma_Doggy_Animation"):
            call Emma_Doggy_Reset
            return
        if not renpy.showing("Emma_SexSprite"):
            return
        $ EmmaX.ArmPose = 2
        hide Emma_SexSprite
        call Girl_Hide(EmmaX)
        show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
            alpha 1 zoom 1 offset (0,0) anchor (0.5, 0.0)
        with dissolve
        $ Speed = 0
        return



# End Emma Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Emma TJ Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Emma TJ annimation element ///////////////////////////////////////////////////////////////////////////                                     Core Emma BJ element

image Emma_TJ_Animation:
    #core titjob animation
    contains:
        ConditionSwitch(
            # Emma's upper body
            "Player.Sprite", ConditionSwitch(
                    # If during sex
                    "Speed == 1", "Emma_TJ_Body_1",#slow
                    "Speed == 2", "Emma_TJ_Body_2",#fast
                    "Speed == 3", "Emma_TJ_Body_3",#licking
                    "Speed == 5", "Emma_TJ_Body_5",#cumming
                    "True",       "Emma_TJ_Body_0",#Static
                    ),
            "True","Emma_TJ_Body_0",#Static
            )
    zoom 1.35 #0.8
    anchor (.5,.5)
    pos (600,605) #(600,705)#height for bj

image Emma_TJ_Tits:
    #core titjob breasts
    contains:
            #base layer
        ConditionSwitch(
            "EmmaX.Arms or EmmaX.Over == 'jacket' or EmmaX.Over == 'dress'", "images/EmmaSex/Emma_Sex_Forearms_W.png",
            "True", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Forearms.png",
            )
        zoom 0.9
    contains:
            #base layer
        ConditionSwitch(
            "EmmaX.Arms", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Tits_TJ_Gloved.png",
            "True", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Tits_TJ.png",
            )
        zoom 0.9
    contains:
            # piercings
        ConditionSwitch(
            "not EmmaX.Pierce", Null(),
            "EmmaX.Pierce == 'barbell'", ConditionSwitch(
                    #if it's the ring pericings
#                    "EmmaX.Chest in ('corset', 'lace bra', 'sports bra')", Null(),
                    "True", "images/EmmaSex/Emma_Pierce_Barbell_Tits_T.png",
                    ),
            "EmmaX.Pierce == 'ring'", ConditionSwitch(
                    #if it's the ring pericings
#                    "EmmaX.Chest in ('corset', 'lace bra', 'sports bra')", Null(),
                    "True", "images/EmmaSex/Emma_Pierce_Ring_Tits_T.png",
                    ),
            "True", Null(),
            )
        zoom 0.9
    contains:
            #chest clothing layer
        ConditionSwitch(
            "not EmmaX.Chest", Null(),   # EmmaX.TitsUp = 0
            "EmmaX.Chest == 'sports bra' and EmmaX.Uptop", Recolor("Emma", "Chest", "images/EmmaSex/Emma_Sex_Bra_Sports_TJ_Uptop.png"),   # Add here. . .
            "EmmaX.Chest == 'sports bra'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_Sex_Bra_Sports_TJ.png"),   # EmmaX.TitsUp = 1
            "EmmaX.Uptop", Null(),   # EmmaX.TitsUp = 0
            "EmmaX.Chest == 'bikini top'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_Sex_Bra_Bikini_TJ.png"),   # Add here. . .
            "EmmaX.Chest == 'lace bra'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_Sex_Bra_Lace_TJ.png"),   # EmmaX.TitsUp = 1
#            "EmmaX.Chest == 'corset'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_Sex_Bra_Lace_TJ.png"),   # EmmaX.TitsUp = 1
            "True", Null(),   # EmmaX.TitsUp = 0
            )
        zoom 0.9
    contains:
            # piercings over clothes
        ConditionSwitch(
            "not EmmaX.Pierce or not EmmaX.Chest", Null(),
            "EmmaX.Pierce == 'barbell'", ConditionSwitch(
                    #if it's the ring pericings
                    "EmmaX.Chest in ('corset', 'lace bra', 'sports bra')", "images/EmmaSex/Emma_Pierce_Barbell_Tits_TC.png",
                    "True", Null(),
                    ),
            "EmmaX.Pierce == 'ring'", ConditionSwitch(
                    #if it's the ring pericings
                    "EmmaX.Chest in ('corset', 'lace bra', 'sports bra')", "images/EmmaSex/Emma_Pierce_Ring_Tits_TC.png",
                    "True", Null(),
                    ),
            "True", Null(),
            )
        zoom 0.9
    contains:
            # spunk on tits
        ConditionSwitch(
                "'tits' in EmmaX.Spunk and Player.Male", "images/EmmaSex/Emma_Spunk_Titjob_Over.png",
                "True", Null(),
                )
        zoom 0.9
    offset (50,50)

#image Emma_TJ_HairBack:
#    #Hair underlay
#    "Emma_BJ_HairBack"
#    zoom 0.41
#    anchor (0.5, 0.5)
#    pos (505,250)

#image Emma_TJ_Head:
#    #Hair underlay
#    "Emma_BJ_Head"
#    zoom 0.41
#    anchor (0.5, 0.5)
#    pos (505,250)

#  TJ animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_TJ_Body_0:
    #Her Body in the TJ pose, idle
    contains:
            #Hair underlay
            "Emma_BJ_HairBack"
            zoom 0.41
            anchor (0.5, 0.5)
            pos (505,260) #bottom
            subpixel True
            block:
                ease 2.4 ypos 250 #top
                ease 1.6 ypos 260 #bottom
                repeat
    contains:
            #base body
            "Emma_Sex_Torso"
            pos (0,0) #bottom
            subpixel True
            block:
                ease 2 ypos -5 #top
                ease 2 ypos 5 #bottom
                repeat

    contains:
            #head
            "Emma_BJ_Head"
            zoom 0.41
            anchor (0.5, 0.5)
            pos (505,260) #bottom  #280
            subpixel True
            block:
                ease 2.4 ypos 250 #top
                ease 1.6 ypos 260 #bottom
                repeat
    contains:
            #zero's cock
            ConditionSwitch(
                "Player.Sprite", "Blowcock",
                "True", Null(),
                )
            subpixel True
            pos (640,150) #bottom #150
            anchor (0.5,0.5)
            zoom 0.4
            rotate -3
            parallel:
                pause 0.1
                ease 1.6 ypos 170 #top
                pause 0.1
                ease 1.4 ypos 150 #bottom
                repeat
            parallel:
                pause 0.1
                ease 1.6 rotate 4 #top
                pause 0.1
                ease 1.4 rotate -3 #bottom
                repeat
    contains:
            #tits
            "Emma_TJ_Tits"
            pos (290,270) #bottom
            rotate -3
            subpixel True
            size (1000,1000)
            anchor (500,500)
            parallel:
                ease 1.5 rotate 4 #top
                pause 0.1
                ease 1.5 rotate -3 #bottom
                pause 0.1
                repeat
    #End TJ animation Speed 1


image Emma_TJ_Body_1:
    #Her Body in the TJ pose, slow
    contains:
            #Hair underlay
            "Emma_BJ_HairBack"
            zoom 0.41
            anchor (0.5, 0.5)
            pos (505,250) #bottom
            subpixel True
            block:
                pause 0.2
                ease 1.4 ypos 240 #top
                pause 0.3
                ease 0.6 ypos 250 #bottom
                repeat
    contains:
            #base body
            "Emma_Sex_Torso"
            pos (0,0) #bottom
            subpixel True
            block:
                pause 0.2
                ease 1.4 ypos -20 #top
                pause 0.3
                ease 0.6 ypos 0 #bottom
                repeat
    contains:
            #zero's cock
            "Blowcock"
            subpixel True
            pos (640,150) #bottom
            #pos (640,90) #height for bj
            anchor (0.5,0.5)
            zoom 0.4
            block:
                pause 0.2
                ease 1.4 ypos 140 #top
                pause 0.3
                ease 0.6 ypos 150 #bottom
                repeat
    contains:
            #head
            "Emma_BJ_Head"
            zoom 0.41
            anchor (0.5, 0.5)
            pos (505,250) #bottom
            subpixel True
            block:
                pause 0.2
                ease 1.4 ypos 240 #top
                pause 0.3
                ease 0.6 ypos 250 #bottom
                repeat
    contains:
            #tits
            "Emma_TJ_Tits"
            pos (290,290) #bottom
            rotate 0
            subpixel True
            size (1000,1000)
            anchor (500,500)
            parallel:
                ease 1.5 ypos 230 #top
                pause 0.3
                ease 0.7 ypos 290 #bottom
                repeat
#            parallel:
#                ease .5 rotate 1 #topS
#                ease .5 rotate -1 #bottom
#                ease .7 rotate 1 #bottom
#                ease .8 rotate 0 #bottom
#                repeat
    #End TJ animation Speed 1


image Emma_TJ_Body_2:
    #Her Body in the TJ pose, fast
    contains:
            #Hair underlay
            "Emma_BJ_HairBack"
            zoom 0.41
            anchor (0.5, 0.5)
            pos (505,250) #bottom
            subpixel True
            block:
                pause 0.1
                ease .6 ypos 250 #top
                ease .3 ypos 270 #bottom
                repeat
    contains:
            #base body
            "Emma_Sex_Torso"
            pos (0,0) #bottom
            subpixel True
            block:
                pause .1
                ease .5 ypos -20 #top
                ease .3 ypos 15 #bottom
                pause .1
                repeat
    contains:
            #zero's cock
            "Blowcock"
            subpixel True
            pos (640,150) #bottom
            #pos (640,90) #height for bj
            anchor (0.5,0.5)
            zoom 0.4
            block:
                pause .05
                ease .65 ypos 140 #top
                ease .3 ypos 150 #bottom
                repeat
    contains:
            #head
            "Emma_BJ_Head"
            zoom 0.41
            anchor (0.5, 0.5)
            pos (505,250) #bottom
            subpixel True
            block:
                pause 0.1
                ease .6 ypos 250 #top
                ease 0.3 ypos 270 #bottom
                repeat
    contains:
            #tits
            "Emma_TJ_Tits"
            pos (290,290) #bottom
            rotate 0
            subpixel True
            size (1000,1000)
            anchor (500,500)
            parallel:
                ease .6 ypos 220 #top
                ease .3 ypos 300 #bottom
                pause .1
                repeat
    #End TJ animation Speed 2

image Emma_TJ_Body_3:
    #Her Body in the TJ pose, slow with licking
    contains:
            #Hair underlay
            "Emma_BJ_HairBack"
            zoom 0.41
            anchor (0.5, 0.5)
            pos (500,290) #bottom
            subpixel True
            block:
                ease 1.5 ypos 260 #top
                pause .7
                ease .3 ypos 290 #bottom
                pause .5
                repeat
    contains:
            #base body
            "Emma_Sex_Torso"
            pos (0,0) #bottom
            subpixel True
            block:
                ease 1.6 ypos -20 #top
                pause .7
                ease .2 ypos 0 #bottom
                pause .5
                repeat
    contains:
            #head
            "Emma_BJ_Head"
            zoom 0.41
            anchor (0.5, 0.5)
            pos (500,290) #bottom  #280
            subpixel True
            block:
                ease 1.5 ypos 260 #top
                pause .7
                ease .3 ypos 290 #bottom
                pause .5
                repeat
    contains:
            #zero's cock
            "Blowcock"
            subpixel True
            pos (640,130) #bottom #150
            anchor (0.5,0.5)
            zoom 0.4
            block:
                pause .2
                ease 1.6 ypos 120 #top
                pause .4
                ease .3 ypos 130 #bottom
                pause .5
                repeat
    contains:
            #tits
            "Emma_TJ_Tits"
            pos (290,290) #bottom
            rotate 0
            subpixel True
            size (1000,1000)
            anchor (500,500)
            parallel:
                ease 1.8 ypos 240 #top
                pause .3
                ease .4 ypos 290 #bottom
                pause .5
                repeat
    #End TJ animation Speed 3



image Emma_TJ_Body_5:
    #Her Body in the TJ pose, slow with licking
    contains:
            #Hair underlay
            "Emma_BJ_HairBack"
            zoom 0.41
            anchor (0.5, 0.5)
            pos (500,290) #bottom
            subpixel True
            block:
                ease 1.5 ypos 288 #top
                pause .7
                ease .3 ypos 290 #bottom
                pause .5
                repeat
    contains:
            #base body
            "Emma_Sex_Torso"
            pos (0,0) #bottom
            subpixel True
            block:
                ease 1.3 ypos -5 #top
                pause .7
                ease .5 ypos 0 #bottom
                pause .5
                repeat
    contains:
            #head
            "Emma_BJ_Head"
            zoom 0.41
            anchor (0.5, 0.5)
            pos (500,290) #bottom  #280
            subpixel True
            block:
                ease 1.5 ypos 288 #top
                pause .7
                ease .3 ypos 290 #bottom
                pause .5
                repeat
    contains:
            #zero's cock
            "Blowcock"
            subpixel True
            pos (640,130) #bottom #150
            anchor (0.5,0.5)
            zoom 0.4
            block:
                pause .2
                ease 1.6 ypos 128 #top
                pause .4
                ease .3 ypos 130 #bottom
                pause .5
                repeat
    contains:
            #tits
            "Emma_TJ_Tits"
            pos (290,290) #bottom
            rotate 0
            subpixel True
            size (1000,1000)
            anchor (500,500)
            parallel:
                ease 1.3 ypos 270 #top
                pause .3
                ease .9 ypos 290 #bottom
                pause .5
                repeat
    #End TJ animation Speed 5
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Emma_TJ_Launch(Line = Trigger):    # The sequence to launch the Emma Titfuck animations
    if renpy.showing("Emma_TJ_Animation"):
        return
    call Girl_Hide(EmmaX)
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 2 xpos 550 yoffset 50 #offset (-100,50)
    if Taboo: # Emma gets started. . .
        if len(Present) >= 2:
            if Present[0] != EmmaX:
                    "[EmmaX.Name] looks back at [Present[0].Name] to see if she's watching."
            elif Present[1] != EmmaX:
                    "[EmmaX.Name] looks back at [Present[1].Name] to see if she's watching."
        else:
                    "[EmmaX.Name] looks around to see if anyone can see her."

#    if EmmaX.Chest and EmmaX.Over:
#        "She throws off her [EmmaX.Over] and her [EmmaX.Chest]."
#    elif EmmaX.Over:
#        "She throws off her [EmmaX.Over], baring her breasts underneath."
#    elif EmmaX.Chest:
#        "She tugs off her [EmmaX.Chest] and throws it aside."
#    $ EmmaX.Over = 0
#    $ EmmaX.Chest = 0
    $ EmmaX.ArmPose = 0

    call Girl_First_Topless(EmmaX)

    if not EmmaX.Tit and Line == "L": #first time
        if not EmmaX.Chest and not EmmaX.Over:
            "Когда вы вытаскиваете свой член, [EmmaX.Name] осторожно помещает его между грудей и начинает тереться ими вверх и вниз."
        elif EmmaX.Chest and not EmmaX.Over:
            "Когда вы вытаскиваете свой член, [EmmaX.Name] осторожно засовывает его под [get_clothing_name(EmmaX.Chest_key, vin)], между грудей, и начинает тереться ими вверх и вниз."
        elif EmmaX.Chest and EmmaX.Over:
            "Когда вы вытаскиваете свой член, [EmmaX.Name] осторожно засовывает его под [get_clothing_name(EmmaX.Over_key, vin)], между грудей, и начинает тереться ими вверх и вниз."
        else:
            "Когда вы вытаскиваете свой член, [EmmaX.Name] осторожно засовывает его под одежду,  между грудей, и начинает тереться ими вверх и вниз."
    elif Line == "L": #any other time
        if not EmmaX.Chest and not EmmaX.Over:
            "Когда вы вытаскиваете свой член, [EmmaX.Name] помещает его между грудей и начинает тереться ими вверх и вниз."
        elif EmmaX.Chest and not EmmaX.Over:
            "Когда вы вытаскиваете свой член, [EmmaX.Name] засовывает его под [get_clothing_name(EmmaX.Chest_key, vin)], между грудей, и начинает тереться ими вверх и вниз."
        elif EmmaX.Chest and EmmaX.Over:
            "Когда вы вытаскиваете свой член, [EmmaX.Name] засовывает его под [get_clothing_name(EmmaX.Over_key, vin)], между грудей, и начинает тереться ими вверх и вниз."
        else:
            "Когда вы вытаскиваете свой член, [EmmaX.Name] засовывает его под одежду, между грудей, и начинает тереться ими вверх и вниз."
    else:
            "[EmmaX.Name] обхватывает своими сиськами ваш член."
#    hide Emma_Sprite
    show blackscreen onlayer black with dissolve
    show Emma_Sprite zorder 150:
        alpha 0
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "titjob"
    show Emma_TJ_Animation zorder 150
    $ Player.Sprite = 1
    hide blackscreen onlayer black with dissolve
    return

label Emma_TJ_Reset: # The sequence to the Emma animations from Titfuck to default
    if not renpy.showing("Emma_TJ_Animation"):
        return
#    hide Emma_TJ_Animation
    call Girl_Hide(EmmaX)
    $ Player.Sprite = 0

    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder 150:
        zoom 2 xpos 550 yoffset 50 #offset (-100,50)  #zoom 2 offset (-100,50)
    show Emma_Sprite zorder EmmaX.Layer:
        alpha 1
        ease 1 zoom 1.5 xpos 500 yoffset 50
        pause .5
        ease .5 zoom 1 xpos EmmaX.SpriteLoc yoffset 0
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
        alpha 1 zoom 1 offset (0,0) xpos EmmaX.SpriteLoc

    "[EmmaX.Name] отстраняется"
    return

# End Emma TJ Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Emma Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Emma BJ element ///////////////////////////////////////////////////////////////////////////                                     Core Emma BJ element
#Emma BJ Over Sprite Compositing


image Emma_BJ_Animation:#BJ_NewTest:                                                                #core BJ animation
    LiveComposite(
        (858,928),
        (-270,-160), ConditionSwitch( #-270,-160
            # Emma's hair backside
            "Speed == 0", At("Emma_BJ_HairBack", Emma_BJ_Head_0()),               #Static
            "Speed == 1", At("Emma_BJ_HairBack", Emma_BJ_Head_1()),               #Licking
            "Speed == 2", At("Emma_BJ_HairBack", Emma_BJ_Head_2()),               #Heading
            "Speed == 3", At("Emma_BJ_HairBack", Emma_BJ_Head_3()),               #Sucking
            "Speed == 4", At("Emma_BJ_HairBack", Emma_BJ_Head_4()),               #Deepthroat
            "Speed == 5", At("Emma_BJ_HairBack", Emma_BJ_Head_5()),               #Cumming High
            "Speed == 6", At("Emma_BJ_HairBack", Emma_BJ_Head_6()),               #Cumming Deep
            "True", Null(),
            ),
        (-20,270), ConditionSwitch(
            # Emma's body, everything below the chin
            "Speed == 0", At("Emma_BJ_Backdrop", Emma_BJ_Body_0()),           #Static
            "Speed == 1", At("Emma_BJ_Backdrop", Emma_BJ_Body_1()),           #Licking
            "Speed == 2", At("Emma_BJ_Backdrop", Emma_BJ_Body_2()),           #Heading
            "Speed == 3", At("Emma_BJ_Backdrop", Emma_BJ_Body_3()),           #Sucking
            "Speed == 4", At("Emma_BJ_Backdrop", Emma_BJ_Body_4()),           #Deepthroat
            "Speed == 5", At("Emma_BJ_Backdrop", Emma_BJ_Body_5()),           #Cumming High
            "Speed == 6", At("Emma_BJ_Backdrop", Emma_BJ_Body_6()),           #Cumming Deep
            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(
            # Emma's head Underlay
            "Speed == 0", At("Emma_BJ_Head", Emma_BJ_Head_0()),               #Static
            "Speed == 1", At("Emma_BJ_Head", Emma_BJ_Head_1()),               #Licking
            "Speed == 2", At("Emma_BJ_Head", Emma_BJ_Head_2()),               #Heading
            "Speed == 3", At("Emma_BJ_Head", Emma_BJ_Head_3()),               #Sucking
            "Speed == 4", At("Emma_BJ_Head", Emma_BJ_Head_4()),               #Deepthroat
            "Speed == 5", At("Emma_BJ_Head", Emma_BJ_Head_5()),               #Cumming High
            "Speed == 6", At("Emma_BJ_Head", Emma_BJ_Head_6()),               #Cumming Deep
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # Cock
            "Speed == 0", At("Blowcock", Emma_BJ_Cock_0()),                    #Static
            "Speed == 1", At("Blowcock", Emma_BJ_Cock_1()),                    #Licking
            "Speed >= 2", At("Blowcock", Emma_BJ_Cock_2()),                    #Heading+
#            "Speed == 2", At("Blowcock", Emma_BJ_Cock_2()),                    #Heading
#            "Speed == 3", At("Blowcock", Emma_BJ_Cock_2()),                    #Sucking
#            "Speed == 4", At("Blowcock", Emma_BJ_Cock_2()),                    #Deepthroat
            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(
            # the masked overlay for when her head overlaps the cock
#            "Speed < 3", Null(),
            "Speed == 2", At(AlphaMask("Emma_BJ_Head", "Emma_BJ_MaskHeadingComposite"), Emma_BJ_Head_2()), #Heading
            "Speed == 5", At(AlphaMask("Emma_BJ_Head", "Emma_BJ_MaskHeadingComposite"), Emma_BJ_Head_5()), #Cumming High
            "Speed == 3", At(AlphaMask("Emma_BJ_Head", "Emma_BJ_MouthSuckingMask"), Emma_BJ_Head_3()), #Sucking
            "Speed == 4", At(AlphaMask("Emma_BJ_Head", "Emma_BJ_MouthSuckingMask"), Emma_BJ_Head_4()), #Deepthroat
            "Speed == 6", At(AlphaMask("Emma_BJ_Head", "Emma_BJ_MouthSuckingMask"), Emma_BJ_Head_6()), #Cumming Deep
            "True", Null(),
            ),
        (325,490), ConditionSwitch(
            # the over part of spunk
#            "Speed < 3 or 'mouth' not in EmmaX.Spunk or not Player.Male", Null(),
            "Speed == 2", At("Emma_BJ_MaskHeadingSpunk", Emma_BJ_Head_2()), #Heading
            "Speed == 5", At("Emma_BJ_MaskHeadingSpunkC", Emma_BJ_Head_5()), #Heading
            "Speed == 3", At("EmmaSuckingSpunk", Emma_BJ_Head_3()), #Sucking
            "Speed == 4", At("EmmaSuckingSpunk", Emma_BJ_Head_4()), #Deepthroat
            "Speed == 6", At("EmmaSuckingSpunk", Emma_BJ_Head_6()), #Cumming Deep
            "True", Null(),
            ),
        )
    zoom .55
    anchor (.5,.5)

image Emma_BJ_HairBack:
    #Hair underlay
    ConditionSwitch(
            "EmmaX.Hair == 'short'", "images/EmmaBJFace/Emma_BJ_Hair_Short_Back.png",
            "EmmaX.Water or EmmaX.Hair == 'wet'", Null(), # or EmmaX.Hair == 'hat wet'
            "not Player.Male and 'facial' in EmmaX.Spunk",Null(),
            "True", Recolor("Emma", "Hair", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Hair_Wave_Back.png"),
            ),
    zoom 1.4
    anchor (0.5, 0.5)

image Emma_BJ_Backdrop:
    contains:
            #blanket
            ConditionSwitch(
                "'blanket' in EmmaX.RecentActions", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
                "True", Null(),
                ),
            zoom 2
            anchor (.5,.5)
            pos (350,600)
    contains:
            #body backdrop
            "Emma_Sex_Torso"
            zoom 2.5
            anchor (.5,.5)
            pos (160,750)
#    zoom 1.5
#    offset (-300,-200)

image Emma_BJ_Head:                                                                            #These are all the details of the face
    LiveComposite(
        (858,928),
         (0,0), ConditionSwitch(
            #Hair behind face above body
            "EmmaX.Hair == 'short'", Null(),
            "EmmaX.Water or EmmaX.Hair == 'wet'", Recolor("Emma", "Hair", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Hair_Wet_Mid.png"),  # or EmmaX.Hair == 'hat wet'
            "not Player.Male and 'facial' in EmmaX.Spunk",Recolor("Emma", "Hair", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Hair_Wet_Mid.png"),
            "True", Recolor("Emma", "Hair", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Hair_Wave_Mid.png"),
            ),
        (0,0), ConditionSwitch(
            # Basic Face layer
            "Speed <= 2 or Speed == 5 or not renpy.showing('Emma_BJ_Animation')", ConditionSwitch(
                    # If the animation isn't sucking, or if not in BJ pose
                    "EmmaX.Blush", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_FaceClosed_Blush.png",
                    "True", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_FaceClosed.png",
                    ),
            "EmmaX.Blush", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_FaceOpen_Blush.png",
            "True", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_FaceOpen.png"
            ),
        (0,0), ConditionSwitch(
            #Mouth
#            "(Speed == 2 or Speed == 5) and renpy.showing('Emma_BJ_Animation')", ConditionSwitch(
#                    # If the Heading animation is active
##                    "EmmaX.Blush", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_FaceClosed_Blush.png",
##                    "True", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_FaceClosed.png"
#                    ),
            "Speed and renpy.showing('Emma_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
                    "Speed == 1", Recolor("Emma", "Lips", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Mouth_Tongue.png"),  #licking
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", Recolor("Emma", "Lips", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Mouth_Sucking.png"), #sucking
                    "Speed == 4", Recolor("Emma", "Lips", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Mouth_Sucking.png"), #deepthroat
                    "Speed == 6", Recolor("Emma", "Lips", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Mouth_Sucking.png"), #cumming
                    ),
            "renpy.showing('Emma_CUN_Animation') and Speed", Recolor("Emma", "Lips", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Mouth_Tongue.png"),
            "Speed == 3 and renpy.showing('Emma_TJ_Animation')", Recolor("Emma", "Lips", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Mouth_Tongue.png"),
            "EmmaX.Mouth == 'normal'", Recolor("Emma", "Lips", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Mouth_Smile.png"),
            "EmmaX.Mouth == 'lipbite'", Recolor("Emma", "Lips", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Mouth_Lipbite.png"),
            "EmmaX.Mouth == 'sucking'", Recolor("Emma", "Lips", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Mouth_Sucking.png"),
            "EmmaX.Mouth == 'kiss'", Recolor("Emma", "Lips", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Mouth_Kiss.png"),
            "EmmaX.Mouth == 'sad'", Recolor("Emma", "Lips", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Mouth_Sad.png"),
            "EmmaX.Mouth == 'smile'", Recolor("Emma", "Lips", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Mouth_Smile.png"),
            "EmmaX.Mouth == 'smirk'", Recolor("Emma", "Lips", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Mouth_Smirk.png"),
            "EmmaX.Mouth == 'grimace'", Recolor("Emma", "Lips", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Mouth_Smile.png"),
            "EmmaX.Mouth == 'surprised'", Recolor("Emma", "Lips", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Mouth_Surprised.png"),
            "EmmaX.Mouth == 'tongue'", Recolor("Emma", "Lips", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Mouth_Tongue.png"),
            "True", Recolor("Emma", "Lips", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Mouth_Smile.png"),
            ),
        (428,605), ConditionSwitch(
            # Heading Mouth
#            "Speed == 2 and Trigger == 'blow'", At("Emma_BJ_MouthHeading", Emma_BJ_MouthAnim()),  #heading
            "not renpy.showing('Emma_BJ_Animation')", Null(),                       #heading
            "Speed == 2", At("Emma_BJ_MouthHeading", Emma_BJ_MouthAnim()),  #heading
            "Speed == 5", At("Emma_BJ_MouthHeading", Emma_BJ_MouthAnimC()), #cumming high
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Spunk layer
            "'mouth' not in EmmaX.Spunk or not Player.Male", Null(),
            "Speed and renpy.showing('Emma_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
                    "Speed == 1", "images/EmmaBJFace/Emma_BJ_Spunk_Tongue.png",  #licking
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", "images/EmmaBJFace/Emma_BJ_Spunk_SuckingUnder.png", #sucking
                    "Speed == 4", "images/EmmaBJFace/Emma_BJ_Spunk_SuckingUnder.png", #deepthroat
                    "Speed == 6", "images/EmmaBJFace/Emma_BJ_Spunk_SuckingUnder.png", #cumming
                    ),
            "EmmaX.Mouth == 'normal'", "images/EmmaBJFace/Emma_BJ_Spunk_Smile.png",
            "EmmaX.Mouth == 'lipbite'", "images/EmmaBJFace/Emma_BJ_Spunk_Lipbite.png",
            "EmmaX.Mouth == 'kiss'", "images/EmmaBJFace/Emma_BJ_Spunk_Kiss.png",
            "EmmaX.Mouth == 'sad'", "images/EmmaBJFace/Emma_BJ_Spunk_Sad.png",
            "EmmaX.Mouth == 'smile'", "images/EmmaBJFace/Emma_BJ_Spunk_Smile.png",
            "EmmaX.Mouth == 'smirk'", "images/EmmaBJFace/Emma_BJ_Spunk_Smirk.png",
            "EmmaX.Mouth == 'surprised'", "images/EmmaBJFace/Emma_BJ_Spunk_Surprised.png",
            "EmmaX.Mouth == 'tongue'", "images/EmmaBJFace/Emma_BJ_Spunk_Tongue.png",
            "EmmaX.Mouth == 'sucking'", "images/EmmaBJFace/Emma_BJ_Spunk_SuckingUnder.png",
            "True", "images/EmmaBJFace/Emma_BJ_Spunk_Smile.png",
            ),
        (0,0), ConditionSwitch(
            #wet face
            "Player.Male", Null(),
            "'mouth' not in EmmaX.Spunk and 'chin' not in EmmaX.Spunk", Null(),
            "renpy.showing('Emma_SexSprite')", "images/EmmaBJFace/Emma_BJ_Wet_Mouth.png",
            "'chin' not in EmmaX.Spunk and (EmmaX.Mouth == 'tongue' or Speed)", "images/EmmaBJFace/Emma_BJ_Wet_Tongue.png",
            "EmmaX.Mouth == 'tongue' or Speed", "images/EmmaBJFace/Emma_BJ_Wet_Tongue2.png",
            "'mouth' in EmmaX.Spunk or 'chin' in EmmaX.Spunk", "images/EmmaBJFace/Emma_BJ_Wet_Mouth.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Brows
            "EmmaX.Brows == 'normal'", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Brows_Normal.png",
            "EmmaX.Brows == 'angry'", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Brows_Angry.png",
            "EmmaX.Brows == 'sad'", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Brows_Sad.png",
            "EmmaX.Brows == 'surprised'", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Brows_Surprised.png",
            "EmmaX.Brows == 'confused'", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Brows_Confused.png",
            "True", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Brows_Normal.png",
            ),
        (0,0), "Emma BJ Blink",
            #Eyes
        (0,0), ConditionSwitch(
            #cum on the face
            "'facial' in EmmaX.Spunk and Player.Male", "images/EmmaBJFace/Emma_BJ_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hair overlay
            "EmmaX.Hair == 'short'", "images/EmmaBJFace/Emma_BJ_Hair_Short.png",
            "EmmaX.Water or EmmaX.Hair == 'wet'", Recolor("Emma", "Hair", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Hair_Wet_Top.png"), # or EmmaX.Hair == 'hat wet'
            "not Player.Male and 'facial' in EmmaX.Spunk",Recolor("Emma", "Hair", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Hair_Wet_Top.png"),
            "True", Recolor("Emma", "Hair", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Hair_Wave_Top.png"),
            ),
        # Modification mode
        (0,0), ConditionSwitch(
            "EmmaX.Mask == 'mask harem'", "images/EmmaBJFace/modification/Emma_bj_mask_harem.png",
            "True", Null(),
        ),
        # ----------------
        (-80,-95), ConditionSwitch(
            #Hats
            "EmmaX.Hat", "Emma_BJ_Hat",
            "True", Null(),
            ),
        )
    zoom 1.4
    anchor (0.5, 0.5)

image Emma BJ Blink:
        #eyeblinks
        ConditionSwitch(
            "EmmaX.Eyes == 'normal'", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Eyes_Sexy.png",
            "EmmaX.Eyes == 'sexy'", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Eyes_Sexy.png",
            "EmmaX.Eyes == 'closed'", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Eyes_Closed.png",
            "EmmaX.Eyes == 'surprised'", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Eyes_Surprised.png",
            "EmmaX.Eyes == 'side'", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Eyes_Side.png",
            "EmmaX.Eyes == 'stunned'", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Eyes_Surprised.png",
            "EmmaX.Eyes == 'down'", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Eyes_Down.png",
            "EmmaX.Eyes == 'manic'", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Eyes_Surprised.png",
            "EmmaX.Eyes == 'squint'", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Eyes_Squint.png",
            "True", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Eyes_Sexy.png",
            ),
        choice:
            3.5
        choice:
            3.25
        choice:
            3
        "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Eyes_Closed.png"
        .25
        repeat

image Emma_BJ_Hat:
    #the mouth used for the heading animations
#    contains:
        "images/EmmaSprite/EmmaSprite_Hat.png"
        zoom 1.3
        anchor (0.50,0.65)  #(0.50,0.65)

image Emma_BJ_MouthHeading:
    #the mouth used for the heading animations
    contains:
        Recolor("Emma", "Lips", "images/EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_BJ_Mouth_Sucking.png")
        zoom 1.4
        anchor (0.50,0.65)  #(0.50,0.65)

image Emma_BJ_MouthSuckingMask:
    #the mask used for sucking animations
    contains:
        "images/EmmaBJFace/Emma_BJ_Mouth_SuckingMask.png"
        zoom 1.4
#    contains: #see if this works, if not remove it
#        ConditionSwitch(
#            "'mouth' not in EmmaX.Spunk", Null(),
#            "Speed != 2 and Speed != 5", Null(),
#            "True", "images/EmmaBJFace/Emma_BJ_Spunk_SuckingOver.png",
#            )
#        zoom 1.4

image Emma_BJ_MaskHeading:
    #the mask used for the heading image
    contains:
        "images/EmmaBJFace/Emma_BJ_Mouth_SuckingMask.png"
        offset (-380,-595)

image Emma_BJ_MaskHeadingComposite:
    #The composite for the heading mask that goes over the face
    LiveComposite(
        (858,928),
        (300,462), ConditionSwitch(
            "Speed == 2", At("Emma_BJ_MaskHeading", Emma_BJ_MouthAnim()),
            "Speed == 5", At("Emma_BJ_MaskHeading", Emma_BJ_MouthAnimC()),
            "True", Null(),
            ),
        )
    zoom 1.8

image Emma_BJ_MaskHeadingSpunk:
    #The composite for the heading mask that goes over the face
    contains:
#            "EmmaSuckingSpunk"
            ConditionSwitch(
                "'mouth' not in EmmaX.Spunk or not Player.Male", Null(),
                "True", "images/EmmaBJFace/Emma_BJ_Spunk_SuckingOver.png",
                )
#            "images/EmmaBJFace/Emma_BJ_Spunk_SuckingOver.png"
            subpixel True
            anchor (0.5, 0.65)
            zoom 0.58 #0.58 = top of heading, 0.66 = crown, 0.60 = valley, 0.68 = base
            block: #total time 1.0 down, 1.5 back up 2.5 total
                pause .20
                easeout .15 zoom 0.66
                linear .15 zoom 0.60
                easein .25 zoom 0.68
                pause .25
                #1.0s to this point
                pause .40
                easeout .40 zoom 0.60
                linear .10 zoom 0.66
                easein .30 zoom 0.58
                pause .30
                #1.5s to this point
                repeat
    zoom 2.5 #1.8
    yoffset 210#130

image Emma_BJ_MaskHeadingSpunkC:
    #The composite for the heading mask that goes over the face
    contains:
#            "EmmaSuckingSpunk"
            ConditionSwitch(
                "'mouth' not in EmmaX.Spunk or not Player.Male", Null(),
                "True", "images/EmmaBJFace/Emma_BJ_Spunk_SuckingOver.png",
                )
#            "images/EmmaBJFace/Emma_BJ_Spunk_SuckingOver.png"
            subpixel True
            anchor (0.5, 0.65)
            zoom 0.7 #0.90
            block: #total time 10 down, 15 back up
                pause .20
                ease .50 zoom 0.65 #0.87
                pause .60
                ease .30 zoom 0.7#0.9
                pause .10
                ease .30 zoom 0.65#0.9
                pause .20
                ease .30 zoom 0.7#0.9
                repeat
    zoom 2.5 #1.8
    yoffset 210#130
image EmmaSuckingSpunk:
    contains:
        ConditionSwitch(
            "'mouth' not in EmmaX.Spunk or not Player.Male", Null(),
            "True", "images/EmmaBJFace/Emma_BJ_Spunk_SuckingOver.png",
            )
        zoom 1.4
        anchor (0.5, 0.5)


transform Emma_BJ_MouthAnim():
        #The animation for the heading mouth
        subpixel True
        zoom 0.58 #0.58 = top of heading, 0.66 = crown, 0.60 = valley, 0.68 = base
        block: #total time 1.0 down, 1.5 back up 2.5 total
            pause .20
            easeout .15 zoom 0.66
            linear .15 zoom 0.60
            easein .25 zoom 0.68
            pause .25
            #1.0s to this point
            pause .40
            easeout .40 zoom 0.60
            linear .10 zoom 0.66
            easein .30 zoom 0.58
            pause .30
            #1.5s to this point
            repeat

#        block: #total time 1.0 down, 1.5 back up 2.5 total
#            pause .20
#            easeout .15 zoom 0.66
#            linear .15 zoom 0.60
#            easein .25 zoom 0.68
#            pause .25
#            #1.0s to this point
#            pause .40
#            easeout .40 zoom 0.60
#            linear .10 zoom 0.66
#            easein .30 zoom 0.58
#            pause .30
#            #1.5s to this point
#            repeat

transform Emma_BJ_Head_2():
    #The heading animation for her face
    subpixel True
    offset (0,-40)     #top (0,-40), -20 is crown, 0 is mid
    block:
        ease 1 yoffset 40           #bottom
        ease 1.5 offset (0,-40)     #top
        repeat


transform Emma_BJ_MouthAnimC():
        #The animation for the heading mouth
        subpixel True
        zoom 0.7 #0.90
        block: #total time 10 down, 15 back up
            pause .20
            ease .50 zoom 0.65 #0.87
            pause .60
            ease .30 zoom 0.7#0.9
            pause .10
            ease .30 zoom 0.65#0.9
            pause .20
            ease .30 zoom 0.7#0.9
            repeat


#Cock Animations for Emma's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
transform Emma_BJ_Cock_0():
    #The angled static animation for the cock for starting
    anchor (.5,.5)
    rotate -10
transform Emma_BJ_Cock_1():
    #The licking animation for the cock
    subpixel True
    anchor (.5,.5)
    ease 0.5 rotate 0
    block:
        ease 2 rotate -5 #410
        pause .5
        ease 2.5 rotate 0
        repeat
transform Emma_BJ_Cock_2():
    #The vertical static animation for the cock used in most sucking
    anchor (.5,.5)
    rotate 0
    alpha 1
#End Cock Animations for Emma's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Head and Body Animations for Emma's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
transform Emma_BJ_Head_0():
    #The starting animation for her face
    subpixel True
    ease 1.5 offset (0,0)
transform Emma_BJ_Body_0():
    #The starting animation for her body
    subpixel True
    ease 1.5 offset (0,0)


transform Emma_BJ_Head_1():
    #The licking animation for her face
    subpixel True
    ease 0.5 offset (0,-35)  #top
    block:
        ease 2.5 offset (25,100) #bottom
        ease 2 offset (0,-35)  #top
        pause .5
        repeat
transform Emma_BJ_Body_1():
    #The licking animation for her body
    subpixel True
    ease 0.5 offset (0,-35)  #top
    block:
        ease 2.5 offset (30,90) #bottom 25,50
        ease 2 offset (0,-35)  #top
        pause .5
        repeat

#transform Emma_BJ_Head_2():
#    #The heading animation for her face
#    subpixel True
#    offset (0,-40)     #top
#    block:
#        ease 1 yoffset 35           #bottom
#        ease 1.5 offset (0,-40)     #top
#        repeat
##        ease 1 yoffset 35           #bottom
##        ease 1.5 offset (0,-40)     #top
##        repeat

transform Emma_BJ_Body_2():
    #The heading animation for her body
    subpixel True
    offset (0,-40)     #top
    block:
        ease 1 yoffset 15           #bottom
        ease 1.5 offset (0,-40)     #top
        repeat

transform Emma_BJ_Head_3():
    #The sucking animation for her face
    subpixel True
    ease 0.5 offset (0,50)
    block:
        ease 1 yoffset 120 #100
        ease 1.5 offset (0,50)
        repeat
transform Emma_BJ_Body_3():
    #The sucking animation for her body
    subpixel True
    ease 0.5 offset (0,50)
    block:
        ease 1 yoffset 100 #80      #bottom
        ease 1.5 offset (0,50) #top
        repeat

transform Emma_BJ_Head_4():
    #The deep animation for her face
    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1 yoffset 300
        pause .5
        ease 2 yoffset 100
        repeat
transform Emma_BJ_Body_4():
    #The deep animation for her body
    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1.2 yoffset 250
        pause .5
        ease 1.8 yoffset 100
        repeat

transform Emma_BJ_Head_5():
    #The heading cumming animation for her face
    subpixel True
    offset (0,-30)     #top
    block:
        ease 1 yoffset -20           #bottom
        ease 1.5 offset (0,-30)     #top
        repeat
transform Emma_BJ_Body_5():
    #The heading cumming animation for her body
    subpixel True
    offset (0,-30)     #top
    block:
        ease 1 yoffset -20           #bottom
        ease 1.5 offset (0,-30)     #top
        repeat

transform Emma_BJ_Head_6():
    #The deep cumming animation for her face
    ease .5 offset (0,230)
    block:
        subpixel True
        ease 1 yoffset 250
        pause .5
        ease 2 yoffset 230
        repeat
transform Emma_BJ_Body_6():
    #The deep cumming animation for her body
    ease .5 offset (0,190)
    block:
        subpixel True
        ease 1.2 yoffset 200
        pause .5
        ease 1.8 yoffset 190
        repeat


#transform Emma_BJ_Static():
#    #The static animation for her face
#    subpixel True
#    ease 1.5 offset (0,0)
#    repeat

#transform Emma_BJ_StaticBody():
#    #The static animation for her face
#    subpixel True
#    ease 1.5 offset (0,0)


#Head and Body Animations for Emma's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
                                                               #BJ Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Emma_BJ_Launch(Line = Trigger):    # The sequence to launch the Emma BJ animations
    if renpy.showing("Emma_BJ_Animation") and EmmaX.Pose != "69":
        return
    elif renpy.showing("Emma_69_Animation") and EmmaX.Pose == "69":
        return

    if not Player.Male:
        call Emma_CUN_Launch
        return

    call Girl_Hide(EmmaX)
    if Line == "L" or Line == "cum":
        show Emma_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1
            ease 1 zoom 2.5 offset (150,80)
        with dissolve
    else:
        show Emma_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1 zoom 2.5 offset (150,80)
        with dissolve

    $ Speed = 0
    hide Emma_Sprite

    if EmmaX.Pose == "69":
            show Emma_69_Animation zorder 150
    else:
            show Emma_BJ_Animation zorder 150:
                pos (645,510)

    if Taboo and Line == "L": # Emma gets started. . .
            if len(Present) >= 2:
                if Present[0] != EmmaX:
                        "[EmmaX.Name] оглядывается на [Present[0].Name_tvo], чтобы посмотреть, наблюдает ли она."
                elif Present[1] != EmmaX:
                        "[EmmaX.Name] оглядывается на [Present[1].Name_tvo], чтобы посмотреть, наблюдает ли она."
            else:
                        "[EmmaX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
            "Затем она наклоняется и берет ваш член в свой рот."
    elif Line == "L":
            "[EmmaX.Name] плавно наклоняется и прислоняет ваш член к своей щеке."


    if Line != "cum":
        $ Trigger = "blow"
#    show Emma_Sprite zorder EmmaX.Layer:
#        alpha 0
#    show Emma_BJ_Animation zorder 150:
#        pos (645,510)
    return

label Emma_BJ_Reset: # The sequence to the Emma animations from BJ to default
    if Player.Male != 1:
            call Emma_CUN_Reset
    if not renpy.showing("Emma_BJ_Animation") and not renpy.showing("Emma_69_Animation"):
            return
#    hide Emma_BJ_Animation
    call Girl_Hide(EmmaX)
    $ Speed = 0

    show Emma_Sprite at SpriteLoc(StageCenter) zorder 150:
        alpha 1 zoom 2.5 offset (150,80)
    with dissolve

    show Emma_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
        alpha 1 zoom 1 offset (0,0)
    return

# End Emma Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Start Emma Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Emma Handjob element //////////////////////////////////////////////////////////////////////                                         Core Emma HJ element

image Emma_HJ_Body:
    "Emma_Sprite"
    pos (680,-1250)#(350,-550)
    zoom 4.8#2.15


transform Emma_HJ_Body_1():
    subpixel True
#    pos (700,-1250)#(350,-550)
    block:
        ease .5 ypos -1220
        pause 0.25
        ease 1.0 ypos -1250
        pause 0.1
        repeat

transform Emma_HJ_Body_2():
    subpixel True
#    pos (350,-550)
    block:
        ease 0.2 ypos -1240
        pause 0.1
        ease 0.4 ypos -1250
        pause 0.1
        repeat

image Emma_Hand_Under:
    "images/EmmaSprite/[EmmaX.skin_image.skin_path]handemma2.png"
    anchor (0.5,0.5)
    pos (-10,0)


image Emma_Hand_Over:
    "images/EmmaSprite/[EmmaX.skin_image.skin_path]handemma1.png"
    anchor (0.5,0.5)
    pos (-10,0)

transform Emma_Hand_1():
    subpixel True
    pos (-20,-100)
    rotate 5
    block:
        ease .5 pos (0,150) rotate -5 #ypos 150 rotate 5 Bottom
        pause 0.25
        ease 1.0 pos (-20,-100) rotate 5 #250#-150 #rotate -10#  Top
        pause 0.1
        repeat

transform Emma_Hand_2():
    subpixel True
    pos (-15,-120)
    rotate 10
    block:
        ease 0.2 pos (-15,0) rotate 0
        pause 0.1
        ease 0.4 pos (-15,-120) rotate 10
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

transform Handcock_1E():
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

transform Handcock_2E():
    subpixel True
    rotate_pad False
    ypos 400
    rotate 0
    block:
        ease .2 ypos 430 rotate -3 #410
        ease .5 ypos 400 rotate 0
        pause 0.1
        repeat

image Emma_HJ_Animation:
    contains:
        ConditionSwitch(
            # backside of the hand
            "not Speed", Transform("Emma_HJ_Body"),
            "Speed == 1", At("Emma_HJ_Body", Emma_HJ_Body_1()),
            "Speed >= 2", At("Emma_HJ_Body", Emma_HJ_Body_2()),
            "Speed", Null(),
            )
    contains:
        ConditionSwitch(                                                # backside of the hand
            "not Speed", Transform("Emma_Hand_Under"),
            "Speed == 1", At("Emma_Hand_Under", Emma_Hand_1()),
            "Speed >= 2", At("Emma_Hand_Under", Emma_Hand_2()),
            "Speed", Null(),
            ),
    contains:
        ConditionSwitch(                                                # cock
            "not Speed", Transform("Zero_Handcock"),
            "Speed == 1", At("Zero_Handcock", Handcock_1E()),
            "Speed >= 2", At("Zero_Handcock", Handcock_2E()),
            "Speed", Null(),
            ),
        offset (0,0)
    contains:
        ConditionSwitch(                                                # fingers of the hand
            "not Speed", Transform("Emma_Hand_Over"),
            "Speed == 1", At("Emma_Hand_Over", Emma_Hand_1()),
            "Speed >= 2", At("Emma_Hand_Over", Emma_Hand_2()),
            "Speed", Null(),
            ),
    anchor (0.51, -1.3)
    zoom 0.4#0.6


label Emma_HJ_Launch(Line = Trigger):
    if renpy.showing("Emma_HJ_Animation"):
        $ Trigger = "hand"
        return
    if not Player.Male:
        call Emma_Finger_Launch
        return
    call Girl_Hide(EmmaX)
    if Line == "L":
        show Emma_Sprite at SpriteLoc(StageRight) zorder 150:
            alpha 1
            ease 1 zoom 1.7 offset (0,200)#(-50,200)
    else:
        show Emma_Sprite at SpriteLoc(StageRight) zorder 150:
            alpha 1
            ease 1 zoom 1.7 offset (0,200)#(-50,200)
        with dissolve

    if Line == "L": # Rogue gets started. . .
        if Taboo:
            if len(Present) >= 2:
                if Present[0] != EmmaX:
                        "[EmmaX.Name] оглядывается на [Present[0].Name_tvo], чтобы посмотреть, наблюдает ли она."
                elif Present[1] != EmmaX:
                        "[EmmaX.Name] оглядывается на [Present[1].Name_tvo], чтобы посмотреть, наблюдает ли она."
            else:
                        "[EmmaX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
            "Затем она наклоняется и хватает ваш член."
        else:
            "[EmmaX.Name] наклоняется и хватает ваш член."

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    else:
        $ Speed = 1
    pause .5
    $ EmmaX.ArmPose = 1
    show Emma_Sprite:
        alpha 0
    show Emma_HJ_Animation at SpriteLoc(StageCenter) zorder 150 with fade:
        #xoffset 150
        offset (100,250)#(100,250)
    return

label Emma_HJ_Reset: # The sequence to the Rogue animations from handjob to default
    if not renpy.showing("Emma_HJ_Animation"):
        return
    $ Speed = 0
    $ EmmaX.ArmPose = 1
    hide Emma_HJ_Animation with dissolve
    call Girl_Hide(EmmaX)
#    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
#        alpha 1
#        zoom 1.7 offset (-50,200)
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
        alpha 1 zoom 1 offset (0,0)
    return

# End Emma Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Start Emma Footjob animations  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_FJ_Chair:
    #footjob chair
    contains:
        ConditionSwitch(
            #Foot
            "not renpy.showing('Emma_FJ_Animation')", Null(),
            "True", "images/EmmaSprite/EmmaSprite_Chair.png"
            )
        anchor (0.5, 0.0)#(0.6, 0.05)
        zoom 0.80

image Emma_FJ_Mask:
    #core footjob animation
    contains:
        "images/EmmaSprite/EmmaSprite_FJMask.png"
#        Solid("#159457", xysize=(402,965))
        anchor (0.5, 0.0)#(0.6, 0.0)
        zoom 0.8 #0.75
        pos (160,0)#(200,0)

image Emma_FJ_Animation:
    #core footjob animation
    contains:
        #her basic dress back
        ConditionSwitch(
            #pants
            "EmmaX.Legs == 'dress'", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_Dress_Back_FJ.png"),
            "True", Null(),
            )
        zoom 0.80
    contains:
        ConditionSwitch(
            #Personal Wetness
            "not EmmaX.Wet", Null(),
            "EmmaX.Legs == 'pants' and not EmmaX.Upskirt", Null(),
            "EmmaX.Panties and not EmmaX.PantiesDown and EmmaX.Wet <= 1", Null(),
            "EmmaX.Wet == 1", AlphaMask("Wet_Drip","Emma_Drip_Mask"), #only plays if nothing is in the way
            "True", AlphaMask("Wet_Drip2","Emma_Drip_Mask"), #only plays if nothing is in the way
            )
        pos (160,400)
    contains:
        ConditionSwitch(
            #Spunk nethers
            "('in' not in EmmaX.Spunk and 'anal' not in EmmaX.Spunk) or not Player.Male", Null(),
            "EmmaX.Legs == 'pants' and not EmmaX.Upskirt", Null(),
            "True", ConditionSwitch( #Wet = 2+
                    "EmmaX.Panties and EmmaX.PantiesDown", AlphaMask("Spunk_Drip","Emma_Drip_MaskP"), #"Wet_Drip2",#
                    "EmmaX.Legs == 'pants'", AlphaMask("Spunk_Drip","Emma_Drip_MaskP"),
                    "True", AlphaMask("Spunk_Drip","Emma_Drip_Mask"), #only plays if nothing is in the way
                    ),
            )
        pos (160,400)
    contains:
        #her basic body, masked to hide the legs
#        "Emma_Sprite"
        AlphaMask("Emma_Sprite", "Emma_FJ_Mask")
#        zoom 1.1
    contains:
        #her basic legs rightside
        "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJRight.png"
        zoom 0.8

    contains:
        #panties up
        ConditionSwitch(
            "EmmaX.PantiesDown or not EmmaX.Panties", Null(),
#            "EmmaX.Panties == 'sports panties' and EmmaX.Wet", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties_Sports_Wet.png"),
            "EmmaX.Panties == 'sports panties'", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties_Sports.png"),
            "EmmaX.Panties == 'lace panties' and EmmaX.Wet", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties_Lace_Wet.png"),
            "EmmaX.Panties == 'lace panties'", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties_Lace.png"),
            "EmmaX.Panties == 'bikini bottoms'", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties_Bikini.png"),
#            "EmmaX.Wet", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties_Wet.png"), #readd when sprite works
            "True", Recolor("Emma", "Panties", "images/EmmaSprite/EmmaSprite_Panties.png"),
            )
        zoom 0.8
    contains:
        #Hose
        ConditionSwitch(
            "EmmaX.Hose == 'pantyhose' and not EmmaX.PantiesDown", Recolor("Emma", "Hose", "images/EmmaSprite/EmmaSprite_FJRight_Pantyhose.png"),
            "EmmaX.Hose == 'ripped pantyhose' and not EmmaX.PantiesDown", Recolor("Emma", "Hose", "images/EmmaSprite/EmmaSprite_FJRight_PantyhoseHoled.png"),
            "EmmaX.Hose == 'stockings' or EmmaX.Hose == 'stockings and garterbelt'", "images/EmmaSprite/EmmaSprite_FJRight_Stocking.png",
            "True", Null(),#Static
            )
        zoom 0.8
    contains:
        ConditionSwitch(
            #Personal Wetness
            "not EmmaX.Wet", Null(),
            "EmmaX.Legs and EmmaX.Wet <= 1", Null(),
            "EmmaX.Legs", "images/EmmaSprite/EmmaSprite_Wet.png",
            "EmmaX.Wet == 1", "images/EmmaSprite/EmmaSprite_Wet.png",
            "True", "images/EmmaSprite/EmmaSprite_Wet.png",       #EmmaX.Wet >1
            )
        zoom .8
    contains:
        #Garter
        ConditionSwitch(
            "EmmaX.Hose == 'garterbelt' or EmmaX.Hose == 'stockings and garterbelt'", Recolor("Emma", "Hose", "images/EmmaSprite/EmmaSprite_FJRight_Garter.png"),
            "True", Null(),#Static
            )
        zoom 0.8
    contains:
        #her basic pants rightside
        ConditionSwitch(
            #pants
            "not EmmaX.Legs", Null(),
            "EmmaX.Legs == 'dress' and EmmaX.ArmPose == 2", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_Dress_FJ2.png"),
            "EmmaX.Legs == 'dress'", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_Dress_FJ1.png"),
            "EmmaX.Upskirt", ConditionSwitch(
                        #if the skirt's up or pants down
                        "EmmaX.Legs == 'skirt'", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_SkirtUp.png"),
                        "True", Null(),
                        ),
            "True", ConditionSwitch(
                        "EmmaX.Legs == 'pants'", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_FJRight_Pants.png"),
                        "EmmaX.Legs == 'yoga pants'", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_FJRight_Yoga.png"),
                        "EmmaX.Legs == 'skirt'", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_FJRight_Skirt.png"),
                        "True", Null(),
                        ),
            )
        zoom 0.8#0.75
    contains:
        #boots
        ConditionSwitch(
            "EmmaX.Upskirt and EmmaX.Legs and EmmaX.Legs != 'skirt'", Null(),
            "EmmaX.Boots == 'thigh boots'", Recolor("Emma", "Boots", "images/EmmaSprite/EmmaSprite_FJRight_Boot.png"),
            "True", Null(),#Static
            )
        zoom 0.8

    contains:
        #dress overlap
        ConditionSwitch(
            "EmmaX.Legs == 'dress' and EmmaX.ArmPose == 2", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Dress_Over2.png"),         # one hand up
            "EmmaX.Legs == 'dress'", Recolor("Emma", "Over", "images/EmmaSprite/EmmaSprite_Dress_Over1.png"),         # one hand up
            "True", Null(),#Static
            )
        zoom 0.8
    contains:
        ConditionSwitch(
            # Emma's lower body
#            "Player.Cock != 'foot'", Null(),
            # If neither
            "Speed == 1", "Emma_FJ_Legs_1",#slow
            "Speed == 4", "Emma_FJ_Legs_4",#cumming
            "Speed >= 2", "Emma_FJ_Legs_2",#faster
            "True", "Emma_FJ_Legs_0",#Static
            )
        pos (410,-20) #(450,20)
        zoom 0.8
    contains:
        #dress overlap
        ConditionSwitch(
            "EmmaX.Hat", "images/EmmaSprite/EmmaSprite_Hat.png",
            "True", Null(),#Static
            )
        zoom 0.41
        pos (-10,-40) #(-17,-45) -x is left, -x is up
    anchor (0.6, 0.0)
    zoom .85
    subpixel True
    block:
        ease 1 yoffset -2
        ease 1 yoffset 0
        repeat
#End core Footjob animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



image Emma_FJ_Legs_0:
    #Footjob speed 0 static
    contains:
        #her basic legs left thigh
        ConditionSwitch(
            #pants
            "EmmaX.Legs == 'pants' and not EmmaX.Upskirt", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png"),
            "EmmaX.Legs == 'yoga pants' and not EmmaX.Upskirt", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png"),
            "EmmaX.Hose == 'pantyhose' and not EmmaX.PantiesDown", Recolor("Emma", "Hose", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJLeftThigh_Pantyhose.png"),
            "EmmaX.Hose == 'ripped pantyhose' and not EmmaX.PantiesDown", Recolor("Emma", "Hose", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJLeftThigh_PantyhoseHoled.png"),
            "EmmaX.Hose == 'stockings' or EmmaX.Hose == 'stockings and garterbelt'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJLeftThigh_Stocking.png",
            "True", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJLeftThigh.png",
            )
        subpixel True
        transform_anchor True
        anchor (.70,.63)
        pos (290,630)
        rotate 12
        parallel:
            ease 2.5 ypos 610
            ease 2.5 ypos 630
            repeat
        parallel:
            ease 2.5 rotate 10
            ease 2.5 rotate 12
            repeat
    contains:
        "Emma_FJ_Calf"
        subpixel True
        transform_anchor True
        pos (340,510) #(360,450)
        rotate 20
        parallel:
            ease 2.5 ypos 490
            ease 2.5 ypos 510
            repeat
        parallel:
            ease 2.5 rotate 15
            ease 2.5 rotate 20
            repeat
    contains:
        #her basic legs left foot
        ConditionSwitch(
            #Foot
            "EmmaX.Hose == 'ripped pantyhose' and not EmmaX.PantiesDown", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJFoot_StockingHoled.png",
            "(EmmaX.Hose == 'ripped pantyhose' or EmmaX.Hose == 'pantyhose') and EmmaX.PantiesDown", Null(),
            "EmmaX.Hose and EmmaX.Hose != 'garterbelt'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJFoot_Stocking.png",
            "True", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJFoot.png",
            )
        transform_anchor True
        anchor (.6,.8)
        pos (200,680)
        rotate 25
        parallel:
            easeout 2 rotate -5
            easein .5 rotate -10
            easeout 2 rotate 20
            easein .5 rotate 25
            repeat
    contains:
        #Cock
        "Zero_Emma_FootCock"
        transform_anchor True
        rotate 0
        block:
            pause .5
            easeout 1.5 rotate -5
            easein .5 rotate -7
            pause .5
            easeout 1 rotate -3
            easein 1 rotate 0
            repeat
    anchor (0.5, 0.0)
# End Emma Footjob Speed 0

image Emma_FJ_Legs_1:
    #Footjob speed 1 slow
    contains:
        #her basic legs left thigh
        ConditionSwitch(
            #pants
            "EmmaX.Legs == 'pants' and not EmmaX.Upskirt", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png"),
            "EmmaX.Legs == 'yoga pants' and not EmmaX.Upskirt", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png"),
            "EmmaX.Hose == 'pantyhose' and not EmmaX.PantiesDown", Recolor("Emma", "Hose", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJLeftThigh_Pantyhose.png"),
            "EmmaX.Hose == 'ripped pantyhose' and not EmmaX.PantiesDown", Recolor("Emma", "Hose", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJLeftThigh_PantyhoseHoled.png"),
            "EmmaX.Hose == 'stockings' or EmmaX.Hose == 'stockings and garterbelt'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJLeftThigh_Stocking.png",
            "True", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJLeftThigh.png",
            )
        transform_anchor True
        anchor (.70,.63)
        pos (280,615)
        rotate 10
        parallel:
            pause 1.3
            ease 2.2 ypos 630
            ease 1 ypos 615
            repeat
        parallel:
            easein .5 rotate 12
            pause 1
            ease 1.5 rotate 18
            pause .5
            easeout 1 rotate 14
            repeat
    contains:
        "Emma_FJ_Calf"
        transform_anchor True
        pos (350,475) #(360,450)
        rotate 15
        parallel:
            pause 1.5
            ease 2 ypos 515 #525
            ease 1 ypos 475
            repeat
        parallel:
            ease 1 rotate 8 #top 5-10-12-10
            ease 1 rotate 18
            ease 2 rotate 20
            ease .5 rotate 18
            repeat
    contains:
        #her basic legs left foot
        ConditionSwitch(
            #Foot
            "EmmaX.Hose == 'ripped pantyhose' and not EmmaX.PantiesDown", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJFoot_StockingHoled.png",
            "(EmmaX.Hose == 'ripped pantyhose' or EmmaX.Hose == 'pantyhose') and EmmaX.PantiesDown", Null(),
            "EmmaX.Hose and EmmaX.Hose != 'garterbelt'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJFoot_Stocking.png",
            "True", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJFoot.png",
            )
        transform_anchor True
        anchor (.6,.8)
        pos (200,680)
        rotate 25
        parallel:
            ease 1 xpos 240#(240,870)
            ease 1 xpos 200
            pause 2.5
            repeat
        parallel:
            pause 1.5
            ease 2 ypos 730
            ease 1 ypos 680#(240,870)
            repeat
        parallel:
            easein 1 rotate 0
            easeout 1 rotate 25
            easein 2 rotate 35
            easeout .5 rotate 25
            repeat
    contains:
        #Cock
        "Zero_Emma_FootCock"
        transform_anchor True
        block:
            easein 1 rotate 0
            ease 2.5 rotate -5
            easeout 1 rotate 2
            repeat
    anchor (0.5, 0.0)
# End Emma Footjob Speed 1

image Emma_FJ_Legs_2:
    #Footjob speed 1 Fast
    contains:
        #her basic legs left thigh
        ConditionSwitch(
            #pants
            "EmmaX.Legs == 'pants' and not EmmaX.Upskirt", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png"),
            "EmmaX.Legs == 'yoga pants' and not EmmaX.Upskirt", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png"),
            "EmmaX.Hose == 'pantyhose' and not EmmaX.PantiesDown", Recolor("Emma", "Hose", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJLeftThigh_Pantyhose.png"),
            "EmmaX.Hose == 'ripped pantyhose' and not EmmaX.PantiesDown", Recolor("Emma", "Hose", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJLeftThigh_PantyhoseHoled.png"),
            "EmmaX.Hose == 'stockings' or EmmaX.Hose == 'stockings and garterbelt'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJLeftThigh_Stocking.png",
            "True", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJLeftThigh.png",
            )
        transform_anchor True
        anchor (.70,.63)
        pos (290,610)
        rotate 10
        parallel:
            ease.5 ypos 630 #bottom high = bottom 480
            ease 1 ypos 610
            repeat
        parallel:
            ease .5 rotate 0
            ease 1 rotate 10
            repeat
    contains:
        "Emma_FJ_Calf"
        transform_anchor True
        pos (380,450) #360,460
        rotate 15
        parallel:
            ease .5 pos (320,500) #bottom high = bottom 480
            ease 1 pos (380,460)
            repeat
        parallel:
            ease .5 rotate -5
            ease 1 rotate 15
            repeat
    contains:
        #her basic legs left foot
        ConditionSwitch(
            #Foot
            "EmmaX.Hose == 'ripped pantyhose' and not EmmaX.PantiesDown", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJFoot_StockingHoled.png",
            "(EmmaX.Hose == 'ripped pantyhose' or EmmaX.Hose == 'pantyhose') and EmmaX.PantiesDown", Null(),
            "EmmaX.Hose and EmmaX.Hose != 'garterbelt'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJFoot_Stocking.png",
            "True", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJFoot.png",
            )
        transform_anchor True
        anchor (.6,.8)
        pos (240,670)
        rotate 30
        parallel:
            ease .5 pos (240,870)
            ease 1 pos (240,670)
            repeat
        parallel:
            ease .5 rotate 20
            ease 1 rotate 30
            repeat
    contains:
        #Cock
        "Zero_Emma_FootCock"
        transform_anchor True
        block:
            ease .5 rotate -8
            ease 1 rotate 0
            repeat
    anchor (0.5, 0.0)
# End Emma Footjob Speed 2


image Emma_FJ_Legs_4:
    #Footjob speed 4 Cumming
    contains:
        #her basic legs left thigh
        ConditionSwitch(
            #pants
            "EmmaX.Legs == 'pants' and not EmmaX.Upskirt", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png"),
            "EmmaX.Legs == 'yoga pants' and not EmmaX.Upskirt", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png"),
            "EmmaX.Hose == 'pantyhose' and not EmmaX.PantiesDown", Recolor("Emma", "Hose", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJLeftThigh_Pantyhose.png"),
            "EmmaX.Hose == 'ripped pantyhose' and not EmmaX.PantiesDown", Recolor("Emma", "Hose", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJLeftThigh_PantyhoseHoled.png"),
            "EmmaX.Hose == 'stockings' or EmmaX.Hose == 'stockings and garterbelt'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJLeftThigh_Stocking.png",
            "True", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJLeftThigh.png",
            )
        transform_anchor True
        anchor (.70,.63)
        pos (290,610)
        rotate 10
        parallel:
            ease 1 rotate 0
            ease 1.3 rotate 23
            pause.5
            repeat
    contains:
        "Emma_FJ_Calf"
        transform_anchor True
        pos (380,450) #360,460
        rotate 15
#        alpha 0.3
        parallel:
            ease 1 pos (320,480) #bottom high = bottom
            ease 1.3 pos (380,450)
            pause.5
            repeat
        parallel:
            ease 1 rotate 5
            ease 1.3 rotate 15
            pause.5
            repeat
    contains:
        #her basic legs left foot
        ConditionSwitch(
            #Foot
            "EmmaX.Hose == 'ripped pantyhose' and not EmmaX.PantiesDown", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJFoot_StockingHoled.png",
            "(EmmaX.Hose == 'ripped pantyhose' or EmmaX.Hose == 'pantyhose') and EmmaX.PantiesDown", Null(),
            "EmmaX.Hose and EmmaX.Hose != 'garterbelt'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJFoot_Stocking.png",
            "True", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJFoot.png",
            )
        transform_anchor True
        anchor (.6,.8)
        pos (240,670)
        rotate 40
        parallel:
            ease 1 pos (200,750) #(240,870)
            ease 1.3 pos (220,670)
            pause.5
            repeat
        parallel:
            ease 1 rotate 30
            ease 1.3 rotate 40
            pause.5
            repeat

    contains:
        #Cock
        "Zero_Emma_FootCock"
        transform_anchor True
        block:
            pause .1
            ease .9 rotate -8
            ease 1.3 rotate 0
            pause.5
            repeat
    anchor (0.5, 0.0)
# End Emma Footjob Speed 4


image Zero_Emma_FootCock:
    #cock used in Emma's FJ animation
    contains:
        ConditionSwitch(
                "Player.Sprite and AlphaCock", "Blowcock",
                "Player.Sprite", "Ghostcock",
                "True", Null(),
                )
    pos (200,1000)
    zoom .9
    anchor (-.4,0.7)

image Emma_FJ_Calf:
    #calf for footjob animation
    contains:
        ConditionSwitch(
            #calf
            "EmmaX.Hose == 'ripped pantyhose' and not EmmaX.PantiesDown", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJLeftCalf_StockingHoled.png",
            "(EmmaX.Hose == 'ripped pantyhose' or EmmaX.Hose == 'pantyhose') and EmmaX.PantiesDown", Null(),
            "EmmaX.Hose and EmmaX.Hose != 'garterbelt'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJLeftCalf_Stocking.png",
            "True", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJLeftCalf.png",
            )
    contains:
        #her basic legs left calf
        ConditionSwitch(
            #pants
            "not EmmaX.Legs or EmmaX.Upskirt", Null(),
            "EmmaX.Legs == 'pants'", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_FJLeftCalf_Pants.png"),
            "EmmaX.Legs == 'yoga pants'", Recolor("Emma", "Legs", "images/EmmaSprite/EmmaSprite_FJLeftCalf_Yoga.png"),
            "True", Null(),
            )
    anchor (.31,.63)#.3.6

#image Emma_FJ_Foot:
#    #calf for footjob animation
#    contains:
#        ConditionSwitch(
#            #Foot
#            "EmmaX.Hose == 'ripped pantyhose' and not EmmaX.PantiesDown", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJFoot_StockingHoled.png",
#            "(EmmaX.Hose == 'ripped pantyhose' or EmmaX.Hose == 'pantyhose') and EmmaX.PantiesDown", Null(),
#            "EmmaX.Hose and EmmaX.Hose != 'garterbelt'", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJFoot_Stocking.png",
#            "True", "images/EmmaSprite/[EmmaX.skin_image.skin_path]EmmaSprite_FJFoot.png",
#            )
#    contains:
#        #spunk
#        ConditionSwitch(
#            "'feet' in EmmaX.Spunk", "images/EmmaSprite/EmmaSprite_Spunk_Feet.png",
#            "True", Null(),
#            )
##    offset (400,100)
#    anchor (.31,.63)#.3.6
# End footjob animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Emma_FJ_Launch(Line = Trigger):    # The sequence to launch the Emma footjob animations
    $ Trigger = "foot"
    $ Player.Sprite = 1
    $ ShowFeet = 1
    if EmmaX.Pose == "doggy":
            call Emma_Sex_Launch("foot")
            return

    if renpy.showing("Emma_FJ_Animation"):
            return
    call Girl_Hide(EmmaX)
    $ Speed = 0
    show Emma_FJ_Chair zorder 10: #offscreen
        xpos 1580
        yoffset 140
        alpha 1
        ease .5 xpos 570
    show Emma_FJ_Animation zorder 150:  #show hidden
        alpha 0
        pos (950,200)
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer: #move emma's sprite into position
        alpha 1
        ease 1 zoom .8 xpos 580 yoffset 150
    pause 1

    show Emma_FJ_Chair zorder 10: #make sure chair is in place
        alpha 1
        xpos 570
    show Emma_Sprite zorder EmmaX.Layer: #hide emma's sprite
        alpha 0
    show Emma_FJ_Animation zorder 150:  # make FJ visible
        ease .5 alpha 1
    pause 0.5
    show Emma_FJ_Animation zorder 150: #make sure it's visible
        alpha 1
    return

label Emma_FJ_Reset: # The sequence to the Emma animations from Titfuck to default
    if renpy.showing("Emma_Doggy_Animation"):
        call Emma_Doggy_Reset
        return

    if not renpy.showing("Emma_FJ_Animation"):
        return
    call Girl_Hide(EmmaX)
    $ Player.Sprite = 0

    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
        zoom .8 xpos 580 yoffset 150 #offset (-100,50)
    show Emma_Sprite zorder EmmaX.Layer:
        alpha 1
        ease .5 zoom 1 xpos EmmaX.SpriteLoc yoffset 0 alpha 1
    pause .5

    hide Emma_FJ_Chair zorder 10
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
        alpha 1
        zoom 1 offset (0,0) xpos EmmaX.SpriteLoc

    "[EmmaX.Name] stands back up."
    return

# End Emma Footjob animations  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# Core Emma CUN element ///////////////////////////////////////////////////////////////////////////                                     Core Emma CUN element
#Emma CUN Over Sprite Compositing

image Emma_CUN_Animation: #core CUN animation
    LiveComposite(
        (787,913),
        (0,0), ConditionSwitch(                                                                 # back of the hair, which needs to go behind the body
            "Speed == 0",  "Emma_CUN_Anim_Static",
            "Speed == 1",  "Emma_CUN_Anim_Licking1",
            "Speed == 2",  "Emma_CUN_Anim_Licking2",
            "Speed >= 3",  "Emma_CUN_Anim_Licking3",
#            "Speed == 4",  "Emma_CUN_Anim_Licking1",
            "True", "Emma_CUN_Anim_Static",
            ),
        )
    zoom .55
    anchor (.5,.5)

image Emma_CUN_Anim_Static:
    #Animation for licking speed 1
    contains:
        #hair
        "Emma_BJ_HairBack"#"BJ_HairBack"
        subpixel True
        offset (40,0)#(-10,0)
        block:
            ease 2 yoffset 10
            ease 2 yoffset 0
            repeat
    contains:
        #body 2
        "Emma_BJ_Backdrop"
        pos (-440,-290)#(-330,-500)
        subpixel True
        offset (40,20)  #top(0,-35)
        block:
            ease 2 yoffset 30
            ease 2 yoffset 20
            repeat
    contains:
        #head
        "Emma_BJ_Head"#"BJ_Head"
        subpixel True
        offset (40,0)#(-10,0)
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


image Emma_CUN_Anim_Licking1:
    #Animation for licking speed 1
    contains:
        #hair
        "Emma_BJ_HairBack"#"BJ_HairBack"
        subpixel True
        offset (0,0)#490)
        block: #5s total
            ease 2.5 offset (0,75) #bottom (-60,100)
            easeout 1.5 offset (0,60)  #top (-70,50)
            ease .5 offset (0,0)  #top
            pause .5
            repeat
    contains:
        #body 2
        "Emma_BJ_Backdrop"#"Emma_Sprite"
#        zoom 1 #4.5
        pos (-440,-290)#(-330,-500)
        subpixel True
        offset (0,0)# -70,0
        block:
            ease 2.5 offset (0,75) #bottom (30,90)
            ease 2.3 offset (0,0)  #top
            pause .2
            repeat
    contains:
        #head
        "Emma_BJ_Head"#"BJ_Head"
        subpixel True
        offset (0,0)#490)
        block: #5s total
            ease 2.5 offset (0,75) #bottom (-60,100)
            easeout 1.5 offset (0,60)  #top (-70,50)
            ease .5 offset (0,0)  #top
            pause .5
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
#End Emma Licking 1

image Emma_CUN_Anim_Licking2:
    #Animation for licking speed 2
    contains:
        #hair
        "Emma_BJ_HairBack"#"BJ_HairBack"
        subpixel True
        offset (0,30)#490)
        block: #2s total
            ease 1 offset (0,100) #bottom
            easeout .65 offset (0,70)  #top -35)
            linear .35 offset (0,30)  #top -35)
#            pause .10
            repeat
    contains:
        #body 2
        "Emma_BJ_Backdrop"
        pos (-440,-290)#(-330,-500)
        subpixel True
        offset (0,0)#490)
        block:
            ease .75 offset (0,70) #bottom (30,90)
            ease .95 offset (0,30)  #top
            pause .30
            repeat

    contains:
        #head
        "Emma_BJ_Head"#"BJ_Head"
        subpixel True
        offset (0,30)#490)
        block: #2s total
            ease 1 offset (0,100) #bottom
            easeout .65 offset (0,70)  #top -35)
            linear .35 offset (0,30)  #top -35)
#            pause .10
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
            pause .2
            repeat
#End Emma Licking 2

image Emma_CUN_Anim_Licking3:
    #Animation for licking speed 3
    contains:
        #hair
        "Emma_BJ_HairBack"#"BJ_HairBack"
        subpixel True
        offset (0,90)#490)
        block: #2s total
            ease .5 offset (0,110) #bottom
            ease .5 offset (0,90)  #top -35)
            repeat
    contains:
        #body 2
        "Emma_BJ_Backdrop"
        pos (-440,-290)#(-330,-500)
        subpixel True
        offset (0,90)#490)
        block:
            ease .4 offset (0,80) #bottom (30,90)
            ease .4 offset (0,90)  #top
            pause .2
            repeat
    contains:
        #head
        "Emma_BJ_Head"#"BJ_Head"
        subpixel True
        offset (0,90)#490)
        block: #2s total
            ease .5 offset (0,110) #bottom
            ease .5 offset (0,90)  #top -35)
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
#End Emma Licking 3

#CUN Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Emma_CUN_Launch(Line = Trigger):
    # The sequence to launch the Emma CUN animations
    if renpy.showing("Emma_CUN_Animation") and EmmaX.Pose != "69":
        return
    elif renpy.showing("Emma_69_CUN") and EmmaX.Pose == "69":
        return

    if Player.Male == 1:
        call Emma_BJ_Launch
        return

    call Girl_Hide(EmmaX)
    if Line == "L" or Line == "cum":
        show Emma_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1
#            zoom 1 offset (0,0)
            ease 1 zoom 2.5 offset (70,240) #(-90,140) offset (150,80)
        with dissolve
    else:
        show Emma_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1 zoom 2.5 offset (70,240) #(-90,140)
        with dissolve

    if Taboo and Line == "L":
            # Emma gets started. . .
            if len(Present) >= 2:
                if Present[0] != EmmaX:
                        "[EmmaX.Name] оглядывается на [Present[0].Name_tvo], чтобы посмотреть, наблюдает ли она."
                elif Present[1] != EmmaX:
                        "[EmmaX.Name] оглядывается на [Present[1].Name_tvo], чтобы посмотреть, наблюдает ли она."
            else:
                        "[EmmaX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
    $ Speed = 1
    if Line == "L":
            if not EmmaX.Blow:
                "[EmmaX.Name] нерешительно стягивает с вас штаны и касается своим ртом вашей киски."
            else:
                "[EmmaX.Name] наклоняется и начинает лизать вашу киску."

    if Line != "cum":
        $ Trigger = "cun"

    show Emma_Sprite:
        alpha 0
    if EmmaX.Pose == "69":
            show Emma_69_CUN zorder 150
    else:
            show Emma_CUN_Animation zorder 150:
                pos (800,830)
    return

label Emma_CUN_Reset: # The sequence to the Emma animations from CUN to default
    if not renpy.showing("Emma_CUN_Animation") and not renpy.showing("Emma_69_CUN"):
        return
    hide Emma_CUN_Animation
    call Girl_Hide(EmmaX)
    $ Speed = 0

    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder 150:
        zoom 2 offset (70,140) alpha 1
        pause .5
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
        alpha 1 zoom 1 offset (0,0)
    $ EmmaX.FaceChange("sexy")
    return

#End Emma Cunnilingus Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

image Emma_Finger_Animation:
    # Core Animation for Fingering Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
        ConditionSwitch(                                                # backside of the hand
            "Speed == 1", "Emma_Finger_1",
            "Speed >= 2", "Emma_Finger_2",
            "True", "Emma_Finger_0",
            ),
    anchor (0.5,0.5)#anchor (0.51, -1.3)
    offset (400,945)#700,1190
    zoom 0.8
    # end Core Animation for Fingering Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <

image Emma_Finger_0:
    # Animation for Fingering Zero's pussy, static < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Emma_Sprite"
            pos (320,-550)
            zoom 2.15
    contains:
            ConditionSwitch(
                "Player.Wet", "EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_Fingering_Wet.png",
                "True", "EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_Fingering_Under.png",
                )
            anchor (0.5,0.6)
            pos (-10,0)

#            "Emma_Finger_Under"
    contains:
            "Zero_Pussy"
#    contains:
#            "EmmaBJFace/Emma_Fingering_Over.png"
#            anchor (0.5,0.6)
#            pos (20,40)
##            "Emma_Finger_Over"
    # end Animation for Fingering Zero's pussy, static < < < < < < < < < < < < < < < < < < < < < < < <

image Emma_Finger_1:
    # Animation for Fingering Zero's pussy, slow < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Emma_Sprite"
            pos (320,-550)
            zoom 2.15
            block:
                ease .5 ypos -540
                pause 0.25
                ease 1.0 ypos -550
                repeat
    contains:
            ConditionSwitch(
                "Player.Wet", "EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_Fingering_Wet.png",
                "True", "EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_Fingering_Under.png",
                )
            subpixel True
        #    xpos 10
            anchor (0.5,0.6)
            transform_anchor True
            pos (-10,0)
            block:
                ease .5 pos (-10,45) #(-30,50)   Bottom
                pause 0.25
                ease 1.0 pos (-10,0) #((20,-60) Top                 pause 0.1
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
#            "EmmaBJFace/Emma_Fingering_Over.png"
##            "Emma_Finger_Over"
#            subpixel True
#        #    xpos 10
#            anchor (0.5,0.6)
#            transform_anchor True
#            block:
#                ease .5 pos (10,85) rotate -15 #(-30,50)   Bottom
#                pause 0.25
#                ease 1.0 pos (10,40) rotate -5 #((20,-60) Top                 pause 0.1
#                repeat
    # end Animation for Fingering Zero's pussy, slow < < < < < < < < < < < < < < < < < < < < < < < <

image Emma_Finger_2:
    # Animation for Fingering Zero's pussy, fast < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Emma_Sprite"
            pos (320,-550)
            zoom 2.15
            block:
                ease 0.15 ypos -540 #rotate 3   100
                pause 0.1
                ease 0.45 ypos -550 #rotate -3  40
                pause 0.1
                repeat
    contains:
            ConditionSwitch(
                "Player.Wet", "EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_Fingering_Wet.png",
                "True", "EmmaBJFace/[EmmaX.skin_image.skin_path]Emma_Fingering_Under.png",
                )
            subpixel True
            anchor (0.5,0.6)
            transform_anchor True
#            rotate -15
            pos (-10,0)
            block:
                ease 0.15 ypos 45 #rotate 3   100
                pause 0.1
                ease 0.45 ypos 0 #rotate -3  40
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
#            "EmmaBJFace/Emma_Fingering_Over.png"
##            "Emma_Finger_Over"
#            anchor (0.5,0.6)
#            subpixel True
#            transform_anchor True
#            rotate -15
#            xpos 10
#            block:
#                ease 0.15 ypos 85 #rotate 3
#                pause 0.1
#                ease 0.45 ypos 40 #rotate -3 -50
#                pause 0.1
#                repeat
    # end Animation for Fingering Zero's pussy, fast < < < < < < < < < < < < < < < < < < < < < < < <

label Emma_Finger_Launch(Line = Trigger):
    if renpy.showing("Emma_Finger_Animation"):
        $ Trigger = "finger"
        return
    if Player.Male == 1:
        call Emma_HJ_Launch
        return

    call Girl_Hide(EmmaX)
    $ EmmaX.Arms = 0
    $ EmmaX.ArmPose = 1
    if not renpy.showing("Emma_Sprite"):
        show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder 150:
            alpha 1
            zoom 1.7 xpos 800 yoffset 200 #offset (-50,200)
        with dissolve
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 1.7 xpos 800 yoffset 200 #offset (-50,200)

    if Taboo and Line == "L":
        # Emma gets started. . .
        if len(Present) >= 2:
            if Present[0] != EmmaX:
                    "[EmmaX.Name] оглядывается на [Present[0].Name_tvo], чтобы посмотреть, наблюдает ли она."
            elif Present[1] != EmmaX:
                    "[EmmaX.Name] оглядывается на [Present[1].Name_tvo], чтобы посмотреть, наблюдает ли она."
        else:
                    "[EmmaX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
        if not EmmaX.Hand and EmmaX.Arms:
            "Когда вы стягиваете свои штаны, [EmmaX.Name] снимает перчатки и нерешительно тянется к вашей киске. Затем она начинает грубо ласкать ее."
        else:
            "Затем она наклоняется и хватает ваш член."
    elif Line == "L":
        if not EmmaX.Hand and EmmaX.Arms:
            "Когда вы стягиваете свои штаны, [EmmaX.Name] снимает перчатки и нерешительно тянется к вашей киске. Затем она начинает грубо ласкать ее."
        else:
            "[EmmaX.Name] наклоняется и кладет руку вам на киску."
    else:
            "[EmmaX.Name] наклоняется и кладет руку вам на киску."

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "finger"
    show Emma_Sprite:
        alpha 0
    show Emma_Finger_Animation at SpriteLoc(EmmaX.SpriteLoc) zorder 150 with fade
    return

label Emma_Finger_Reset: # The sequence to the Emma animations from handjob to default
    if not renpy.showing("Emma_Finger_Animation"):
        return
    $ Speed = 0
    hide Emma_Finger_Animation
    with dissolve
    call Girl_Hide(EmmaX)
    show Emma_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 yoffset 50
        pause .5
        ease .5 zoom 1 xpos EmmaX.SpriteLoc yoffset 0
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
        alpha 1 zoom 1 xpos EmmaX.SpriteLoc yoffset 0
    return

# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


# Start Emma 69 Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

image Emma_69_Animation:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
                #Shows different upper body motion depending on events
#                "True", "Emma_69_Anim1",
                "Speed == 2", "Emma_69_Anim2",
                "Speed == 3", "Emma_69_Anim3",
                "Speed == 4", "Emma_69_Anim4",
                "Speed == 5", "Emma_69_Anim5",
                "Speed == 6", "Emma_69_Anim6",
                "Speed", "Emma_69_Anim1",
                "True", "Emma_69_Static",
                ),
        )
    align (0.6,0.0)
    pos (475,-700)#(475,-700)
    zoom 1.8#1/3

#Start Animations for Emma's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Emma 69 Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_69_Body:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Emma_SexSprite
        (1120,840),

        (0,0), ConditionSwitch(
            #Base belly
            "True", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Body.png",
            ),
#        (0,0), ConditionSwitch(
#            #Wet look
#            "EmmaX.Water", "images/EmmaSex/Emma_69_Water_Body.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #bra layer
            "EmmaX.Uptop", ConditionSwitch(
                    #if top's up
#                    "EmmaX.Chest == 'bikini top'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_69_Chest_Bikini_Tits_Up.png"),
                    "EmmaX.Chest == 'corset'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_69_Chest_Corset_Body_Up.png"),
#                    "EmmaX.Chest == 'sports bra'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_69_Chest_Sports_Tits.png"),
#                    "EmmaX.Chest == 'lace bra'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_69_Chest_Lace_Tits.png"),
                    "True", Null(),
                    ),
            #if the top's down. . .
#            "EmmaX.Chest == 'bikini top'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_69_Chest_Bikini_Tits.png"),
            "EmmaX.Chest == 'corset'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_69_Chest_Corset_Body.png"),
            "EmmaX.Chest == 'sports bra'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_69_Chest_Sports_Body.png"),
            "EmmaX.Chest == 'lace bra'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_69_Chest_Lace_Body.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #shirt layer
            "(EmmaX.Over == 'dress' or EmmaX.Legs == 'dress') and EmmaX.Uptop", Recolor("Emma", "Over", "images/EmmaSex/Emma_69_Over_Dress_Body_Up.png"),
            "EmmaX.Over == 'nighty' and EmmaX.Uptop",  Recolor("Emma", "Over", "images/EmmaSex/Emma_69_Over_Dress_Body_Up.png"),
            "EmmaX.Uptop", Null(),
            "EmmaX.Over == 'dress' or EmmaX.Legs == 'dress'", Recolor("Emma", "Over", "images/EmmaSex/Emma_69_Over_Dress_Body.png"),
            "EmmaX.Over == 'jacket'", Recolor("Emma", "Over", "images/EmmaSex/Emma_69_Over_Jacket.png"),
            "EmmaX.Over == 'nighty'",  Recolor("Emma", "Over", "images/EmmaSex/Emma_69_Over_Dress_Body.png"),   #fix with nighty
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'belly' in EmmaX.Spunk and Player.Male", "images/EmmaSex/Emma_69_Spunk_Belly.png",
            "True", Null(),
            ),
#        (0,0), "images/EmmaSex/Emma_Sex_HeadRef.png",
        )
    offset (15,0)#(50,0)#(250,250)#(175,175)
#    yoffset -163
# End Emma 69 Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Emma 69 Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_69_Tits:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Emma_SexSprite
        (1120,840),

        (0,0), ConditionSwitch(
            #tops under
            "not EmmaX.Uptop", Null(),
            #if the top's down. . .
#            "EmmaX.Chest == 'bikini top'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_69_Chest_Bikini_Tits.png"),
#            "EmmaX.Chest == 'corset'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_69_Chest_Corset_Tits.png"),
            "EmmaX.Chest == 'sports bra'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_69_Chest_Lace_Tits.png"),
            "EmmaX.Chest == 'lace bra'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_69_Chest_Lace_Tits.png"),
            #shirt layer
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            # base tits
            "True", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Tits.png",
            ),
#        (0,0), ConditionSwitch(
#            #Wet look
#            "EmmaX.Water", "images/EmmaSex/Emma_69_Water_Body.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #bra layer
            "EmmaX.Uptop", ConditionSwitch(
                    #if top's up
                    "EmmaX.Chest == 'bikini top'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_69_Chest_Bikini_Tits_Up.png"),
#                    "EmmaX.Chest == 'corset'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_69_Chest_Corset_Tits.png"),
#                    "EmmaX.Chest == 'sports bra'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_69_Chest_Sports_Tits.png"),
#                    "EmmaX.Chest == 'lace bra'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_69_Chest_Lace_Tits.png"),
                    "True", Null(),
                    ),
            #if the top's down. . .
            "EmmaX.Chest == 'bikini top'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_69_Chest_Bikini_Tits.png"),
            "EmmaX.Chest == 'corset'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_69_Chest_Corset_Tits.png"),
            "EmmaX.Chest == 'sports bra'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_69_Chest_Sports_Tits.png"),
            "EmmaX.Chest == 'lace bra'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_69_Chest_Lace_Tits.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #shirt layer
            "(EmmaX.Over == 'dress' or EmmaX.Legs == 'dress') and EmmaX.Uptop", Null(),
            "EmmaX.Over == 'nighty' and EmmaX.Uptop", Null(),
            "EmmaX.Uptop", Null(),
            "EmmaX.Over == 'dress' or EmmaX.Legs == 'dress'", Recolor("Emma", "Over", "images/EmmaSex/Emma_69_Over_Dress_Tits.png"),
#            "EmmaX.Over == 'jacket'", Recolor("Emma", "Over", "images/EmmaSex/Emma_69_Over_Jacket.png"),
            "EmmaX.Over == 'nighty'", Recolor("Emma", "Chest", "images/EmmaSex/Emma_69_Chest_Lace_Tits.png"),   #fix with nighty
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #piercings
            "not EmmaX.Pierce", Null(),
            "EmmaX.Pierce == 'ring'", ConditionSwitch(
                    # ring pierce
                    "EmmaX.Uptop", "images/EmmaSex/Emma_69_Pierce_Tits_R.png",

                    "EmmaX.Over == 'dress' or EmmaX.Legs == 'dress'", "images/EmmaSex/Emma_69_Pierce_Tits_R_White.png",
                    "EmmaX.Chest == 'lace bra'", "images/EmmaSex/Emma_69_Pierce_Tits_R_Lace.png",
                    "EmmaX.Chest", "images/EmmaSex/Emma_69_Pierce_Tits_R_White.png",
                    "EmmaX.Over == 'nighty'", "images/EmmaSex/Emma_69_Pierce_Tits_R_Lace.png",

                    "True", "images/EmmaSex/Emma_69_Pierce_Tits_R.png",
                    ),
            "EmmaX.Uptop", "images/EmmaSex/Emma_69_Pierce_Tits_B.png",

            "EmmaX.Over == 'dress' or EmmaX.Legs == 'dress'", "images/EmmaSex/Emma_69_Pierce_Tits_B_Dress.png",
            "EmmaX.Chest == 'lace bra'", "images/EmmaSex/Emma_69_Pierce_Tits_B_Lace.png",
            "EmmaX.Chest", "images/EmmaSex/Emma_69_Pierce_Tits_B_White.png",
            "EmmaX.Over == 'nighty'", "images/EmmaSex/Emma_69_Pierce_Tits_B_Lace.png",

            "True", "images/EmmaSex/Emma_69_Pierce_Tits_B.png",
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'tits' in EmmaX.Spunk and Player.Male", "images/EmmaSex/Emma_69_Spunk_Tits.png",
            "True", Null(),
            ),
#        (0,0), "images/EmmaSex/Emma_Sex_HeadRef.png",
        )
    offset (15,0)#(250,250)#(175,175)
#    yoffset -163
# End Emma 69 Pose Tits / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Emma 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_69_Head:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Emma_SexSprite
        (1120,840),
        (0,0), ConditionSwitch(
            #tongue
            "renpy.showing('Emma_69_CUN') and Speed != 3", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Tongue.png",
            "Speed == 1", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Tongue.png",
            "True", Null(),
            ),
        (0,0), "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Head.png",
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'mouth' in EmmaX.Spunk and Player.Male", "images/EmmaSex/Emma_69_Spunk_Mouth.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #collar
#            "Speed == 1 and Player.Male", Null(),
#            "EmmaX.Chest == 'swimsuit' or EmmaX.Panties == 'swimsuit'", "images/EmmaSex/Emma_69_Collar.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #Hair over
            "Speed == 1 and Player.Male", Null(),
            "EmmaX.Hair == 'short'", "images/EmmaSex/Emma_69_Hair_Short.png",
            "EmmaX.Hair == 'wet' or EmmaX.Water", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Hair_Wet.png",
            "not Player.Male and 'facial' in EmmaX.Spunk","images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Hair_Wet.png",
            "True", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Hair_Long.png",
            ),
        )
    offset (15,0)#(175,175)#(180,100)
#    yoffset -163
# End Emma 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Emma 69 Pose Hair Over / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_69_HairOver:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Emma_SexSprite
        (1120,840),
        (0,0), ConditionSwitch(
            #Hair over
#            "renpy.showing('Emma_TJ_Animation')", Null(),
            "EmmaX.Hair == 'short'", "images/EmmaSex/Emma_69_Hair_Short.png",
            "EmmaX.Hair == 'wet' or EmmaX.Water", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Hair_Wet.png",
            "not Player.Male and 'facial' in EmmaX.Spunk","images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Hair_Wet.png",
            "True", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Hair_Long.png",
            ),
        )
    offset (15,0)#(180,100)
#    yoffset -163
# End Emma 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Emma 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_69_HairBack:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Emma_SexSprite
        (1120,840),
        (0,0), ConditionSwitch(
            #Hair over
            "EmmaX.Hair == 'short'", Null(),
            "True", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Hair_Long_Back.png",
            ),
#        (0,0), "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Hair_Long_Back.png",
        )
    offset (15,0)#(175,175)
#    yoffset -163
# End Emma 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Emma 69 Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_69_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Emma_SexSprite
        (1120,880),
#        (0,0), ConditionSwitch(
#            #scarf
#            "EmmaX.Acc", "images/EmmaSex/Emma_69_Scarf.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #back of skirt Layer
            "EmmaX.Over == 'dress' or EmmaX.Legs == 'dress'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_69_Legs_Dress_Under.png"),
            "EmmaX.Legs == 'skirt'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_69_Legs_Skirt_Under.png"),
            "EmmaX.Over == 'nighty'", Recolor("Emma", "Over", "images/EmmaSex/Emma_69_Legs_Nighty_Under.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs
#            "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/EmmaSex/Emma_Sex_FBase.png",
#            "Player.Sprite and Player.Cock == 'in' and Speed", "images/EmmaSex/Emma_Sex_FBase.png",
#            "Player.Sprite and Player.Cock == 'in' and Speed", "Emma_Sex_Heading_Pussy",
#            "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/EmmaSex/Emma_Sex_Ass.png",
#            "Trigger == 'lick pussy'", "images/EmmaSex/Emma_Sex_Ass.png",
            "True", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Ass.png",
            ),

        (0,0), ConditionSwitch(
            #ass red
            "EmmaX.Red", "images/EmmaSex/Emma_69_Red.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            "Player.Sprite and Player.Cock == 'anal'", "images/EmmaSex/Emma_Sex_Anus_Cover.png",
#            "True", Null(),
#            ),

#        (0,0), ConditionSwitch(
#            #Wet look
#            "not EmmaX.Water", Null(),
#            "True", "images/EmmaSex/Emma_69_Water_Legs.png",
#            ),

        (0,0), "Emma_69_Anus",
            #Anus Composite  (0,-10)

        (0,0), "Emma_69_Pussy",
            #Pussy Composite


        (0,0), ConditionSwitch(    #165,560
            #Personal Wetness
            "not EmmaX.Wet", Null(),
            "(EmmaX.Legs == 'yoga pants' or EmmaX.Legs == 'shorts') and not EmmaX.Upskirt", Null(),
            "EmmaX.Panties and not EmmaX.PantiesDown", Null(),
            "EmmaX.Wet == 1", AlphaMask("Wet_Drip_69","images/BetsySex/Betsy_69_Mask_Pussy.png"), #"Wet_Drip_69",
            "True", AlphaMask("Wet_Drip2_69","images/BetsySex/Betsy_69_Mask_Pussy.png"), #"Wet_Drip2_69",
            ),

        (-6,12), ConditionSwitch(    #-6,12
            #anal Spunk
            "'anal' not in EmmaX.Spunk or not Player.Male", Null(),
            "(EmmaX.Legs == 'yoga pants' or EmmaX.Legs == 'shorts') and not EmmaX.Upskirt", Null(),
#            "True", "Spunk_Drip2_69", #"Spunk_Drip_69",
            "True", AlphaMask("Spunk_Drip_69_Anal","images/BetsySex/Betsy_69_Mask_Ass.png"), #"Spunk_Drip_69",
            ),
        (0,0), ConditionSwitch(
            #anal Spunk
            "'anal' in EmmaX.Spunk", "images/EmmaSex/Emma_69_Spunk_Anus.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #hose layer
            "EmmaX.Hose == 'stockings and garterbelt'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_69_Hose_StockingsGarter.png"),
            "EmmaX.Hose == 'garterbelt'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_69_Hose_Garter.png"),
            "EmmaX.Hose == 'stockings'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_69_Hose_Stockings.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Panties if up
            "EmmaX.PantiesDown", ConditionSwitch(
                    #If she has panties down. . .
#                    "EmmaX.Panties == 'lace panties'", "images/EmmaSex/Emma_69_Panties_Lace_Down.png",
#                    "EmmaX.Panties == 'bikini bottoms'", "images/EmmaSex/Emma_69_Panties_Bikini_Down.png",
#                    "EmmaX.Panties and EmmaX.Wet", "images/EmmaSex/Emma_69_Panties_Tan_Down_Wet.png",
#                    "EmmaX.Panties", "images/EmmaSex/Emma_69_Panties_Tan_Down.png",
                    "True", Null(),
                    ),
            "EmmaX.Panties == 'lace panties'", Recolor("Emma", "Panties", "images/EmmaSex/Emma_69_Panties_Lace.png"),
            "EmmaX.Panties == 'bikini bottoms'", Recolor("Emma", "Panties", "images/EmmaSex/Emma_69_Panties_White.png"),
            "EmmaX.Panties == 'sports panties' and EmmaX.Wet", Recolor("Emma", "Panties", "images/EmmaSex/Emma_69_Panties_Sport_Wet.png"),
            "EmmaX.Panties == 'sports panties'", Recolor("Emma", "Panties", "images/EmmaSex/Emma_69_Panties_Sport.png"),
            "EmmaX.Panties and EmmaX.Wet", Recolor("Emma", "Panties", "images/EmmaSex/Emma_69_Panties_White_Wet.png"),
            "EmmaX.Panties", Recolor("Emma", "Panties", "images/EmmaSex/Emma_69_Panties_White.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pantyhose layer
            "EmmaX.Panties and EmmaX.PantiesDown", Null(),
            "EmmaX.Hose == 'pantyhose'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_69_Hose_Pantyhose.png"),
            "EmmaX.Hose == 'ripped pantyhose'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_69_Hose_Pantyhose_Holed.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #pants Layer
            "EmmaX.Upskirt", Null(),
            "EmmaX.Legs == 'pants' and EmmaX.Wet", Recolor("Emma", "Legs", "images/EmmaSex/Emma_69_Legs_Pants_Wet.png"),
            "EmmaX.Legs == 'pants'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_69_Legs_Pants.png"),
            "EmmaX.Legs == 'yoga pants' and EmmaX.Wet", Recolor("Emma", "Legs", "images/EmmaSex/Emma_69_Legs_Yoga_Wet.png"),
            "EmmaX.Legs == 'yoga pants'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_69_Legs_Yoga.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Piercings over pants and pantyhose
            "not EmmaX.Pierce", Null(),
            "EmmaX.Pierce == 'ring'",ConditionSwitch(
                    #If she has panties down. . .
                    "Player.Sprite and Player.Cock == 'in'", Null(),
                    "not EmmaX.Upskirt and (EmmaX.Legs == 'pants' or EmmaX.Legs == 'yoga pants')", "images/EmmaSex/Emma_69_Pierce_Pussy_R_White.png",
                    "not EmmaX.PantiesDown and EmmaX.Panties == 'lace panties'", "images/EmmaSex/Emma_69_Pierce_Pussy_R_Lace.png",
                    "not EmmaX.PantiesDown and EmmaX.Panties", "images/EmmaSex/Emma_69_Pierce_Pussy_R_White.png",
                    "not EmmaX.PantiesDown and EmmaX.Panties and EmmaX.Hose == 'pantyhose'", "images/EmmaSex/Emma_69_Pierce_Pussy_R_Lace.png",

                    "EmmaX.Pubes", "images/EmmaSex/Emma_69_Pierce_Pussy_R_Pubes.png",
                    "True", "images/EmmaSex/Emma_69_Pierce_Pussy_R.png",
                    ),
            #else, it's barbell
            "not EmmaX.Upskirt and (EmmaX.Legs == 'pants' or EmmaX.Legs == 'yoga pants')", "images/EmmaSex/Emma_69_Pierce_Pussy_B_White.png",
            "not EmmaX.PantiesDown and EmmaX.Panties == 'lace panties'", "images/EmmaSex/Emma_69_Pierce_Pussy_B_Lace.png",
            "not EmmaX.PantiesDown and EmmaX.Panties", "images/EmmaSex/Emma_69_Pierce_Pussy_B_White.png",
            "not EmmaX.PantiesDown and EmmaX.Panties and EmmaX.Hose == 'pantyhose'", "images/EmmaSex/Emma_69_Pierce_Pussy_B_Lace.png",

            "EmmaX.Pubes", "images/EmmaSex/Emma_69_Pierce_Pussy_B_Pubes.png",
            "True", "images/EmmaSex/Emma_69_Pierce_Pussy_B.png",
            ),

        (0,0), ConditionSwitch(
            #skirt Layer
            "EmmaX.Upskirt", ConditionSwitch(
                    #If she has pants down. . .
                    "EmmaX.Over == 'dress' or EmmaX.Legs == 'dress'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_69_Legs_Dress_Up.png"),
                    "EmmaX.Legs == 'skirt'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_69_Legs_Skirt_Up.png"),
                    "EmmaX.Over == 'nighty'", Recolor("Emma", "Over", "images/EmmaSex/Emma_69_Legs_Nighty_Up.png"),
                    "True", Null(),
                    ),
            "EmmaX.Over == 'dress' or EmmaX.Legs == 'dress'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_69_Legs_Dress.png"),
            "EmmaX.Legs == 'skirt'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_69_Legs_Skirt.png"),
            "EmmaX.Over == 'nighty'", Recolor("Emma", "Over", "images/EmmaSex/Emma_69_Legs_Nighty.png"),
            "True", Null(),
            ),

        (0,0),ConditionSwitch(
            #Outside Spunk
            "'back' in EmmaX.Spunk and Player.Male", "images/EmmaSex/Emma_69_Spunk_Ass.png",
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #pussy fondling animation
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Emma_Sex_Fondle_Pussy",
#            "True", "images/EmmaSex/Emma_Sex_Hand.png",
#            ),

#        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer
#            "not Player.Sprite or Player.Cock != 'out'", Null(),
#            "Speed >= 2", "Emma_Hotdog_Zero_Anim2",
#            "Speed", "Emma_Hotdog_Zero_Anim1",
#            "True", "Emma_Hotdog_Zero_Anim0",
#            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
#            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy' or Trigger2 == 'lick pussy'", "Emma_69_Lick_Pussy",
            "Trigger == 'lick ass' or Trigger2 == 'lick ass'", "Emma_69_Lick_Ass",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy fondling animation
            "EmmaX.Offhand == 'fondle pussy' and EmmaX.Lust > 60 and not (Player.Sprite)",  At("EmmaFingerHand", GirlFingerPussyX()), #"Emma_Sex_Mast2",
            "EmmaX.Offhand == 'fondle pussy'", At("EmmaMastHand", GirlGropePussyX()), #"Emma_Sex_Mast",
#            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Emma_Sex_Fondle_Pussy",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Footjob overlay
#            "Player.Cock == 'foot'", Null(),
#            "Player.Sprite and Player.Cock == 'anal'",AlphaMask("Emma_69_Feet", "images/EmmaSex/Emma_Sex_Feet_Mask.png"),
#            "renpy.showing('Anal_Plug_In_Sex') or renpy.showing('Anal_Plug_Out_Sex')",AlphaMask("Emma_69_Feet", "images/EmmaSex/Emma_Sex_Feet_Mask.png"),
#            "ShowFeet", "Emma_69_Feet",
##            "Player.Sprite", AlphaMask("Emma_Sex_Feet", "images/EmmaSex/Emma_Sex_Feet_Mask.png"),
##            "Trigger == 'lick pussy'", AlphaMask("Emma_Sex_Feet", "images/EmmaSex/Emma_Sex_Feet_Mask.png"),
##            "Trigger == 'lick ass'", AlphaMask("Emma_Sex_Feet", "images/EmmaSex/Emma_Sex_Feet_Mask.png"),
#            "True", AlphaMask("Emma_69_Feet", "images/EmmaSex/Emma_Sex_Feet_Mask.png"),
#            ),

        (0,0), "Emma_69_Feet_L",
        (0,0), ConditionSwitch(
            #Footjob overlay
            "Player.Cock == 'foot'", Null(),
            "True", "Emma_69_Feet_R",
#            "Player.Sprite and Player.Cock == 'anal'",AlphaMask("Emma_69_Feet", "images/EmmaSex/Emma_Sex_Feet_Mask.png"),
#            "renpy.showing('Anal_Plug_In_Sex') or renpy.showing('Anal_Plug_Out_Sex')",AlphaMask("Emma_69_Feet", "images/EmmaSex/Emma_Sex_Feet_Mask.png"),
#            "ShowFeet", "Emma_69_Feet",
##            "Player.Sprite", AlphaMask("Emma_Sex_Feet", "images/EmmaSex/Emma_Sex_Feet_Mask.png"),
##            "Trigger == 'lick pussy'", AlphaMask("Emma_Sex_Feet", "images/EmmaSex/Emma_Sex_Feet_Mask.png"),
##            "Trigger == 'lick ass'", AlphaMask("Emma_Sex_Feet", "images/EmmaSex/Emma_Sex_Feet_Mask.png"),
#            "True", AlphaMask("Emma_69_Feet", "images/EmmaSex/Emma_Sex_Feet_Mask.png"),
            ),
#        (0,0), "Emma_69_Tail",

#        (0,0), ConditionSwitch(                                                                                 #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
#            "not Speed", "Emma_Sex_Feet",
#            "Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Emma_Sex_Feet", "images/EmmaSex/Emma_Sex_FeetMask.png"),
#            "True", "Emma_Sex_Feet",
#            ),
        )
    offset (-15,0)#(175,175)
# End Emma 69 Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Emma_69_Feet_R:
    LiveComposite(
        #the lower legs used in the sex pose, referenced by Emma_Sex_Legs
        (1120,840),
        (0,0), ConditionSwitch(
            #feet layer
            "(EmmaX.Hose == 'pantyhose' or EmmaX.Hose == 'ripped pantyhose') and EmmaX.Panties and EmmaX.PantiesDown", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Feet_R.png",
            "EmmaX.Hose == 'ripped pantyhose'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_69_Feet_Holed_R.png"),
            "EmmaX.Hose and EmmaX.Hose != 'garterbelt'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_69_Feet_Hose_R.png"),
            "True", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Feet_R.png",   #Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Wet look
#            "not EmmaX.Water", Null(),
#            "True", "images/EmmaSex/Emma_69_Water_Feet_R.png",
#            ),
        (0,0), ConditionSwitch(
            #pants Layer
            "EmmaX.Upskirt", Null(),
            "EmmaX.Legs == 'pants'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_69_Feet_Pants_R.png"),
            "EmmaX.Legs == 'yoga pants'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_69_Feet_Yoga_R.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk
            "'feet' in EmmaX.Spunk", "images/EmmaSex/Emma_69_Spunk_Feet_R.png",
            "True", Null(),
            ),
        )

image Emma_69_Feet_L:
    LiveComposite(
        #the lower legs used in the sex pose, referenced by Emma_Sex_Legs
        (1120,840),
        (0,0), ConditionSwitch(
            #feet layer
            "(EmmaX.Hose == 'pantyhose' or EmmaX.Hose == 'ripped pantyhose') and EmmaX.Panties and EmmaX.PantiesDown", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Feet_L.png",
            "EmmaX.Hose == 'ripped pantyhose'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_69_Feet_Holed_L.png"),
            "EmmaX.Hose and EmmaX.Hose != 'garterbelt'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_69_Feet_Hose_L.png"),
            "True", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Feet_L.png",   #Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Wet look
#            "not EmmaX.Water", Null(),
#            "True", "images/EmmaSex/Emma_69_Water_Feet_L.png",
#            ),
        (0,0), ConditionSwitch(
            #pants Layer
            "EmmaX.Upskirt", Null(),
            "EmmaX.Legs == 'pants'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_69_Feet_Pants_L.png"),
            "EmmaX.Legs == 'yoga pants'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_69_Feet_Yoga_L.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk
            "'feet' in EmmaX.Spunk", "images/EmmaSex/Emma_69_Spunk_Feet_L.png",
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




# Start Emma 69 Pose Pussy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_69_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).

    contains:
            # The background plate of her pussy
            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/EmmaSex/Emma_Sex_Pussy_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed", "Emma_Sex_Heading_Pussy",
#                "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/EmmaSex/Emma_Sex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Pussy_Open.png",
                "EmmaX.Offhand == 'fondle pussy' and EmmaX.Lust > 60", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Pussy_Open.png",
                "True", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Pussy_Closed.png",
                )
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "not EmmaX.Wet", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/JubesSex/Jubes_Sex_WetPussy_F.png",
                "True", "images/BetsySex/Betsy_69_Water_Pussy.png",
                )
    contains:
            # pubes
            ConditionSwitch(
                "not EmmaX.Pubes", Null(),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Pubes_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and Speed >= 1", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Pubes_Fucking.png",
                "Player.Sprite and Player.Cock == 'in'", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Pubes_Fucking.png",
#                "Player.Sprite and Player.Cock == 'out'", "images/EmmaSex/Emma_Sex_Pubes_Open.png",
                "Trigger == 'lick pussy'", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Pubes_Open.png",
                "EmmaX.Offhand == 'fondle pussy' and EmmaX.Lust > 60", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Pubes_Open.png",
                "True", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Pubes_Closed.png",
                )
    contains:
            #Spunk
            ConditionSwitch(
                "'in' not in EmmaX.Spunk or not Player.Male", Null(),
                "(EmmaX.Legs == 'yoga pants' or EmmaX.Legs == 'shorts') and not EmmaX.Upskirt", Null(),
                "EmmaX.Panties and not EmmaX.PantiesDown", Null(),
#                "True", "Spunk_Drip_69",
                "True", AlphaMask("Spunk_Drip_69","images/BetsySex/Betsy_69_Mask_Pussy.png"),
                )
            offset (0,-50)

#    contains:
#            ConditionSwitch(
#                #Outside Spunk
##                "'in' in EmmaX.Spunk and Player.Sprite and Player.Cock == 'in' and Speed and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_PussyF.png",
#                "'in' in EmmaX.Spunk and Player.Male", "images/BetsySex/Betsy_69_Spunk_Pussy.png",
#                "True", Null(),
#                )
##            offset (0,10)
    contains:
            #Spunk under penis
            ConditionSwitch(
                "'in' in EmmaX.Spunk", "images/EmmaSex/Emma_69_Spunk_Pussy.png",
                "True", Null(),
                )
#    contains:
#            #hose layer
#            ConditionSwitch(
#                "EmmaX.Panties and EmmaX.PantiesDown", Null(),
#                "EmmaX.Hose == 'ripped pantyhose' and ShowFeet", "images/EmmaSex/Emma_Sex_Hose_Pantyhose_Holed.png",
#                "EmmaX.Hose == 'ripped pantyhose'", "images/EmmaSex/Emma_Sex_Hose_Pantyhose_Holed.png",
#                "True", Null(),
#                ),
#    contains:
#            # The animation of Zero's moving penis, masked by her pussy shape
#            ConditionSwitch(
##                "not Player.Sprite", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 3", AlphaMask("Emma_Sex_Fucking_Zero_Anim3", "Emma_Sex_Fucking_Mask"),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", AlphaMask("Emma_Sex_Fucking_Zero_Anim2", "Emma_Sex_Fucking_Mask"),
#                "Player.Sprite and Player.Cock == 'in' and Speed == 1", AlphaMask("Emma_Sex_Fucking_Zero_Anim1", "Emma_Sex_Heading_Mask"),
#                "Player.Sprite and Player.Cock == 'in'", "Emma_Sex_Fucking_Zero_Anim0",
#                "True", Null(),
#                )
#    contains:
#            #Piercings
#            ConditionSwitch(
#                "EmmaX.Pierce == 'barbell' and Player.Sprite and Player.Cock == 'in' and Speed", "images/EmmaSex/Emma_Sex_Pierce_Pussy_BarbellF.png",
#                "EmmaX.Pierce == 'ring' and Player.Sprite and Player.Cock == 'in' and Speed", "images/EmmaSex/Emma_Sex_Pierce_Pussy_RingF.png",
#                "EmmaX.Pierce == 'barbell'", "images/EmmaSex/Emma_Sex_Pierce_Pussy_Barbell.png",
#                "EmmaX.Pierce == 'ring'", "images/EmmaSex/Emma_Sex_Pierce_Pussy_Ring.png",
#                "True", Null(),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed == 1", "Emma_Pussy_Spunk_Heading",
#                "True", Null(),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "Speed == 1", Null(),
#                "'in' not in EmmaX.Spunk or not Player.Sprite or Player.Cock != 'in' or not Speed or not Player.Male", Null(),
##                "Speed <= 1", Null(), #"Emma_Pussy_Spunk_Heading",
#                "True", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
#                )

    #End Emma Pussy composite


image Emma_69_Lick_Pussy:
        "Lick_AnimF"
        zoom 0.7
        rotate 180
        offset (510,500)#(535,500
image Emma_69_Lick_Ass:
        "Lick_AnimF"
        zoom 0.7
        rotate 180
        offset (535,580)#(535,550)

image Emma_Sex_Fondle_Pussy:
        "GropePussy_Emma"
        xzoom -1.3
        yzoom 1.3
#        rotate 180
        offset(-610,-250) #(-610,-300)
#        block:
#            ease 1 offset(-1000,0) #(535,500)
#            ease 1 offset(-1000,-1000) #(535,500)
#            ease 1 offset(0,-1000) #(535,500)
#            ease 1 offset(0,0) #(535,500)
#            repeat

image Emma_69_Fondle_Pussy:
        "GropePussy_Emma"
        xzoom -1.5
        yzoom 1.5
        offset(-710,-300) #(-890,-300)
#        block:
#            ease 1 offset(-1000,0) #(535,500)
#            ease 1 offset(-1000,-1000) #(535,500)
#            ease 1 offset(0,-1000) #(535,500)
#            ease 1 offset(0,0) #(535,500)
#            repeat

image Emma_69_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/JubesSex/Jubes_Sex_Anal.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/JubesSex/Jubes_Sex_Anal.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/EmmaSex/Emma_Sex_Anus.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/EmmaSex/Emma_Sex_Anus.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed", "Emma_Sex_Anal_Heading",
#            "Player.Sprite and Player.Cock == 'anal'", "Emma_Sex_Anal_Tip",
            "EmmaX.Plug", "images/PlugBase_Sex.png",
            "EmmaX.Loose > 2", "Emma_Gape_Anal_Sex",
#            "EmmaX.Loose", "images/EmmaSex/Emma_Sex_Anus_Loose.png",
            "True", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Anus.png",
            "True", Null(),
            )
#    contains:
#            #Spunk under penis
#            ConditionSwitch(
#                "'anal' not in EmmaX.Spunk or not Player.Male", Null(),
##                "Player.Sprite and Player.Cock != 'anal' and Speed >= 1", "images/EmmaSex/Emma_Sex_Spunk_Anal_Under.png",
##                "Player.Sprite and Player.Cock == 'anal' and Speed == 1", "Emma_Sex_Anal_Spunk_Heading_Under",
#                "True", "images/EmmaSex/Emma_69_Spunk_Anus.png",
#                )
#            offset (5,0)
#    contains:
#            # The animation of Zero's moving penis, masked by her anus shape
#            ConditionSwitch(
#                "not Player.Sprite or Player.Cock != 'anal'", Null(),
#                "Speed >= 3",  AlphaMask("Emma_Sex_Anal_Zero_Anim3", "Emma_Sex_Anal_MaskF"),
#                "Speed >= 2", AlphaMask("Emma_Sex_Anal_Zero_Anim2", "Emma_Sex_Anal_MaskF"),
#                "Speed", AlphaMask("Emma_Sex_Anal_Zero_Anim1", "Emma_Sex_Anal_Mask"),
#                "True", AlphaMask("Emma_Sex_Anal_Zero_Anim0", "Emma_Sex_Anal_Mask"),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "'anal' not in EmmaX.Spunk or not Player.Sprite or Player.Cock != 'anal' or not Speed or not Player.Male", Null(),
#                "Speed == 1", "Emma_Sex_Anal_Spunk_Heading_Over",
#                "True", "Emma_Sex_Anal_Spunk",
#                )

image Emma_Gape_Anal_Sex:
        #removing an anal plug
        contains:
            #Hole
            "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_69_Anus.png"
            transform_anchor True
            subpixel True
            anchor (560,620)#(0.52,0.69)
            offset (560,617)#(218,518)
            zoom 1 # tight
            block:
                ease 3 zoom 1.2 #in.87
                ease 3 zoom 1 #out
                repeat

#Start Animations for Emma's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_69_Static:
        #this is the animation for Emma's hairback during 69, Speed 0 (static)
        contains:
            subpixel True
            "Emma_69_HairBack"
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
            offset (680,900)#(675,900)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Emma's head during 69, Speed 0 (static)
        contains:
            subpixel True
            "Emma_69_Head"
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
        #this is the animation for Emma's upper body during 69, Speed 0 (static)
        contains:
            "Emma_69_Tits"
            subpixel True
            rotate 180
            anchor (560,400)#(560,330) + is right and down
            offset (700,715)#(-560,-330) + is right and down
            transform_anchor True
            yzoom 1
            pos (0,-15) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,-25) #top
                pause .25
                ease 1 pos (0,-15) #bottom
                repeat
            parallel:
                #Total time, 3 seconds
                pause .25
                easein 1.5 yzoom .9 #top
                pause .25
                ease 1 yzoom 1 #bottom
                repeat
        contains:
            "Emma_69_Body"
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
        #this is the animation for Emma's lower body during 69, Speed 0 (static)
        contains:
            "Emma_69_Legs"
            subpixel True
            rotate 180
            pos (0,-15) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,-10) #top
                pause .25
                ease 1 pos (0,-15) #bottom
                repeat

#Start Animations for Emma's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_69_Anim1:
        #this is the animation for Emma's hairback during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Emma_69_HairBack"
            rotate 190
#            zoom .75
            offset (10,0)
#            offset (180,50)#(180,100)
            pos (35,55) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (0,-55) #top(10,-25
                pause 1.50
                ease 2.25 pos (35,55) #bottom(30,60)
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 rotate 180
                pause 1.50
                ease 2.25 rotate 190#210
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
        #this is the animation for Emma's head during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Emma_69_Head"
            rotate 220
#            zoom .75
#            offset (180,50)#(180,100)
            pos (50,60) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (20,-50)#(20,-25) #top
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
        #this is the animation for Emma's upper body during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Emma_69_HairOver"
#            "images/EmmaSex/Emma_69_Hair.png"
            rotate 190
#            zoom .75
            offset (10,0)
#            offset (180,50)#(180,100)
            pos (35,55) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (0,-55) #top(10,-25
                pause 1.50
                ease 2.25 pos (35,55) #bottom(30,60)
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 rotate 180
                pause 1.50
                ease 2.25 rotate 190
                repeat
        contains:
            subpixel True
            "Emma_69_Tits"
            rotate 180
            anchor (560,400)#(560,330) + is right and down
            offset (700,715)#(-560,-330) + is right and down
            transform_anchor True
            yzoom 1
            pos (30,40) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (0,0) #top
                pause 1.5#1.25
                ease 2.25 pos (30,40) #bottom #2.5
                repeat
            parallel:
                #Total time, 5 seconds
                easein .2 yzoom 1.15#bottom
                ease .2 yzoom 1
                pause .1
                ease .75 yzoom 1.05 #top
                ease .25 yzoom .9
                ease .25 yzoom 1
                pause .75
                ease .5 yzoom .9 #heading down
                pause 1.4
                easeout .6 yzoom 1.1#bottom
                repeat
            parallel:
                #Total time, 5 seconds
                easein .5 rotate 180
                ease .75 rotate 178
                ease .5 rotate 180
                pause 1.0#1.25
                ease 1 rotate 185
                pause 1.0#             #bottom
                ease .25 rotate 178
                repeat
        contains:
            subpixel True
            "Emma_69_Body"
            rotate 180
#            zoom .65
            pos (30,40) #X less is left, Y less is up
            block:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (0,0) #top
                pause 1.25
                ease 2.5 pos (30,40) #bottom
                repeat
        #this is the animation for Emma's lower body during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Emma_69_Legs"
            rotate 185
            pos (30,10) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .25
                easein 1 pos (0,-5)#(0,-5)
                pause 1
                ease 2.75 pos (30,10)
                repeat
            parallel:
                #Total time, 5 seconds
                pause .25
                easein 1 rotate 180
                pause 1
                ease 2.75 rotate 185
                repeat

#Start Animations for Emma's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_69_Anim2:
        #this is the animation for Emma's hairback during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Emma_69_HairBack"
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
            offset (680,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Emma's head during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Emma_69_Head"
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
        #this is the animation for Emma's upper body during 69, Speed 2 (heading)
        contains:
            "Emma_69_Tits"
            subpixel True
            rotate 180
            anchor (560,400)#(560,330) + is right and down
            offset (700,715)#(-560,-330) + is right and down
            transform_anchor True
            yzoom 1.1
            pos (0,0) #X less is left, Y less is up
#            alpha .9
            parallel:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,-10) #top
                pause .25
                ease 1 pos (0,0) #bottom
                repeat
            parallel:
                #Total time, 3 seconds
                ease .2 yzoom 1
                ease .8 yzoom 1.2
                easein 1.0 yzoom 1
                ease .6 yzoom .9
                pause .2
                ease .2 yzoom 1.1
                repeat
        contains:
            "Emma_69_Body"
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
        #this is the animation for Emma's lower body during 69, Speed 2 (heading)
        contains:
            "Emma_69_Legs"
            subpixel True
            rotate 180
            pos (0,-5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,-10) #top
                pause .25
                ease 1 pos (0,-5) #bottom
                repeat

#Start Animations for Emma's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_69_Anim3:
        #this is the animation for Emma's hairback during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Emma_69_HairBack"
            rotate 180
#            zoom .75
            pos (0,30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-20) #top
#                pause .5
                ease 1.25 pos (0,30) #bottom
                repeat
        #this is the animation for Zero's cock during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (680,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Emma's head during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Emma_69_Head"
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
        #this is the animation for Emma's upper body during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Emma_69_Tits"
            rotate 180
            anchor (560,400)#(560,330) + is right and down
            offset (700,715)#(-560,-330) + is right and down
            transform_anchor True
            yzoom 1
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
        #this is the animation for Emma's lower body during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Emma_69_Body"
            rotate 180
#            zoom .65
            pos (0,30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-5) #top
#                pause .5
                ease 1.25 pos (0,30) #bottom
                repeat
        #this is the animation for Emma's lower body during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Emma_69_Legs"
            rotate 180
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,-5)
#                pause .5
                ease 1.25 pos (0,10)
                repeat

#Start Animations for Emma's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_69_Anim4:
        #this is the animation for Emma's hairback during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Emma_69_HairBack"
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
            offset (680,900)#(690,900)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Emma's head during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Emma_69_Head"
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
        #this is the animation for Emma's upper body during 69, Speed 4 (deep)
#        contains:
#            subpixel True
#            "Emma_69_Tits"
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
            "Emma_69_Tits"
            rotate 180
            anchor (560,400)#(560,330) + is right and down
            offset (700,715)#(-560,-330) + is right and down
            transform_anchor True
            yzoom 1
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
            "Emma_69_Body"
            rotate 180
#            zoom .65
            pos (0,40) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,5) #top
                pause .5
                ease 1.75 pos (0,40) #bottom
                repeat
        #this is the animation for Emma's lower body during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Emma_69_Legs"
            rotate 180
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,-5)
#                pause .5
                ease 2.25 pos (0,10)
                repeat

#Start Animations for Emma's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_69_Anim5:
        #this is the animation for Emma's hairback during 69, Speed 5 (cum high)
        contains:
            subpixel True
            "Emma_69_HairBack"
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
            offset (680,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Emma's head during 69, Speed 5 (cum high)
        contains:
            subpixel True
            "Emma_69_Head"
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
        #this is the animation for Emma's upper body during 69, Speed 5 (cum high)
        contains:
            "Emma_69_Tits"
            subpixel True
            rotate 180
            anchor (560,400)#(560,330) + is right and down
            offset (700,715)#(-560,-330) + is right and down
            transform_anchor True
            yzoom 1
            pos (0,-10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .5
                easein 1.75 pos (0,-20) #top
#                pause .5
                ease 1.25 pos (0,-10) #bottom
                repeat
        contains:
            "Emma_69_Body"
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
        #this is the animation for Emma's lower body during 69, Speed 5 (cum high)
        contains:
            "Emma_69_Legs"
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

#Start Animations for Emma's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_69_Anim6:
        #this is the animation for Emma's hairback during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Emma_69_HairBack"
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
            offset (680,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Emma's head during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Emma_69_Head"
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
        #this is the animation for Emma's upper body during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Emma_69_Tits"
            rotate 180
            anchor (560,400)#(560,330) + is right and down
            offset (700,715)#(-560,-330) + is right and down
            transform_anchor True
            yzoom 1
            pos (0,30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,35) #top
                pause .5
                ease 1.75 pos (0,30) #bottom
                repeat
        contains:
            subpixel True
            "Emma_69_Body"
            rotate 180
#            zoom .65
            pos (0,30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,35) #top
                pause .5
                ease 1.75 pos (0,30) #bottom
                repeat
        #this is the animation for Emma's lower body during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Emma_69_Legs"
            rotate 180
            pos (0,20) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,10)
#                pause .5
                ease 2.25 pos (0,20)
                repeat

#End Animations for Emma's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#Start Emma 69 Cunnilingus Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

#Start Animations for Emma's 69 Cunnalingus pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Emma_69_CUN:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
#                "True", "Emma_69_Anim1",
                "Speed == 2",   "Emma_69_Cun2",
                "Speed == 3",   "Emma_69_Cun3",
                "Speed",        "Emma_69_Cun1",
                "True",         "Emma_69_Cun0",
                ),
        )
    align (0.6,0.0)
    pos (475,-700)
    zoom 1.8#1/3

#Start Animations for Emma's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Animations for Emma's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_69_Cun0:
        #this is the animation for Emma's hairback during 69, Speed 0 (static)
        contains:
            subpixel True
            "Emma_69_HairBack"
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
        #this is the animation for Emma's head during 69, Speed 0 (static)
        contains:
            subpixel True
            "Emma_69_Head"
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
        #this is the animation for Emma's upper body during 69, Speed 0 (static)
        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (728,920)#(590,620)
        #this is the animation for Emma's lower body during 69, Speed 0 (static)
        contains:
            "Emma_69_Tits"
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
            "Emma_69_Body"
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
            "Emma_69_Legs"
            subpixel True
            rotate 180
            pos (10,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (10,0) #top
                pause .25
                ease 1 pos (10,5) #bottom
                repeat

#Start Animations for Emma's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_69_Cun1:
        #this is the animation for Emma's hairback during 69, Speed 1 (lick)
        contains:
            subpixel True
            "Emma_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (15,-10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                ease 1.0 pos (15,10) #top
                easeout .5 pos (15,-5) #top
                easein 1.0 pos (15,-10) #bottom
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
        #this is the animation for Emma's head during 69, Speed 1 (lick)
        contains:
            subpixel True
            "Emma_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (15,-10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                ease 1.0 pos (15,10) #top
                easeout .5 pos (15,-5) #top
                easein 1.0 pos (15,-10) #bottom
                pause .5
                repeat
        #this is the animation for Emma's upper body during 69, Speed 1 (lick)
        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (728,920)#(590,620)
        #this is the animation for Emma's lower body during 69, Speed 1 (lick)
        contains:
            "Emma_69_Tits"
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
            "Emma_69_Body"
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
            "Emma_69_Legs"
            subpixel True
            rotate 180
            pos (10,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (10,0) #top
                pause .25
                ease 1 pos (10,5) #bottom
                repeat


#Start Animations for Emma's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_69_Cun2:
        #this is the animation for Emma's hairback during 69, Speed 2 (clit)
        contains:
            subpixel True
            "Emma_69_HairBack"
            rotate 170
#            zoom .75
#            offset (180,50)#(180,100)
            pos (5,0) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                easein .9 pos (5,5) #top
                easein 1.1 pos (5,0) #bottom
                repeat
            parallel:
                #Total time, 3 seconds
                easein 1.0 rotate 175 #top
                easein 1.0 rotate 170 #bottom
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
        #this is the animation for Emma's head during 69, Speed 2 (clit)
        contains:
            subpixel True
            "Emma_69_Head"
            rotate 165
#            zoom .75
#            offset (180,50)#(180,100)
            pos (5,0) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                easein .9 pos (0,-5) #top
                easein 1.1 pos (0,-10) #bottom
                repeat
            parallel:
                #Total time, 3 seconds
                easein 1.0 rotate 170 #top
                easein 1.0 rotate 165 #bottom
                repeat
        #this is the animation for Emma's upper body during 69, Speed 2 (clit)
        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (728,920)#(590,620)
        #this is the animation for Emma's lower body during 69, Speed 2 (clit)
        contains:
            "Emma_69_Tits"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1 pos (0,-5) #top
                ease 1 pos (0,0) #bottom
                repeat
        contains:
            "Emma_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1 pos (0,-5) #top
                ease 1 pos (0,0) #bottom
                repeat
        contains:
            "Emma_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat

#Start Animations for Emma's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Emma_69_Cun3:
        #this is the animation for Emma's hairback during 69, Speed 3 (suck)
        contains:
            subpixel True
            "Emma_69_HairBack"
            rotate 170
#            zoom .75
#            offset (180,50)#(180,100)
            pos (5,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (5,10) #top
#                pause .5
                ease 1.25 pos (5,15) #bottom
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
        #this is the animation for Emma's head during 69, Speed 3 (suck)
        contains:
            subpixel True
            "Emma_69_Head"
            rotate 170
#            zoom .75
#            offset (180,50)#(180,100)
            pos (5,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (5,10) #top
#                pause .5
                ease 1.25 pos (5,15) #bottom
                repeat
        #this is the animation for Emma's upper body during 69, Speed 3 (suck)
        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (728,920)#(590,620)
        #this is the animation for Emma's lower body during 69, Speed 3 (suck)
        contains:
            "Emma_69_Tits"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .3
                easein 1.5 pos (0,-5) #top
                pause .3
                ease .9 pos (0,0) #bottom
                repeat
        contains:
            "Emma_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,-5) #top
                pause .25
                ease 1 pos (0,0) #bottom
                repeat
        contains:
            "Emma_69_Legs"
            subpixel True
            rotate 180
            pos (5,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (5,0) #top
                pause .25
                ease 1 pos (5,5) #bottom
                repeat
#End Animations for Emma's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#End Emma 69 Animations

# Start Emma Scissor Pose content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Emma_SC_Sprite:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
                #if the top's down. . .
                "Speed >= 2", "Emma_SC_Anim_2",
                "Speed", "Emma_SC_Anim_1",
                "True", "Emma_SC_Anim_0",
                ),
        )
    align (0.6,0.0)
    pos (650,300)#(650,200)(925,740)#(910,850)
    zoom 0.85#0.8

# End Emma Sex Pose Speed 2 Scissor / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#image Emma_Sex_Legs = LiveComposite(
image Emma_SC_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Kitty_SexSprite
        (1120,840),
        (0,0), ConditionSwitch(
            # back of dress
            "EmmaX.Legs == 'dress'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_Dress_S_Back.png"),
            "True", Null(),
            ),
        (0,0), "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Sex_Legs_Sex.png",
        #Legs Base
#        (0,0),ConditionSwitch(
#            #wet look
#            "EmmaX.Water", "images/EmmaSex/Emma_Sex_Wet_Legs.png",
#            "True", Null(),
#            ),
#        (0,0), "Emma_Sex_Anus",
#        #Anus Composite

#        (0,0), "Emma_SC_Pussy",
#        #Pussy Composite

        (0,0), ConditionSwitch(
            # stockings
            "EmmaX.Hose == 'stockings'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_Sex_Hose_Stockings_S.png"),
            "EmmaX.Hose == 'stockings and garterbelt'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_Sex_Hose_StockingsGarter_S.png"),
            "EmmaX.Hose == 'garterbelt'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_Sex_Hose_Garter_S.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # piercings
            "EmmaX.Pierce == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_S.png",
            "(EmmaX.Legs == 'pants' or EmmaX.Legs == 'yoga pants') and not EmmaX.Upskirt", Null(),
            "EmmaX.Panties and not EmmaX.PantiesDown", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S_C2.png",
            "EmmaX.Hose == 'pantyhose' and not EmmaX.PantiesDown", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S_C2.png",
            "EmmaX.Pierce == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # pubes
            "EmmaX.Pubes", Recolor("Emma", "Pubes", "images/EmmaSex/[EmmaX.skin_image.skin_path]Emma_Pubes_Sex.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # panties
            "EmmaX.PantiesDown", Null(),
            "EmmaX.Panties == 'sports panties' and EmmaX.Wet", Recolor("Emma", "Panties", "images/EmmaSex/Emma_Sex_Panties_Sport_SW.png"),
            "EmmaX.Panties == 'sports panties'", Recolor("Emma", "Panties", "images/EmmaSex/Emma_Sex_Panties_Sport_S.png"),
            "EmmaX.Panties == 'lace panties'", Recolor("Emma", "Panties", "images/EmmaSex/Emma_Sex_Panties_Lace_S.png"),
            "EmmaX.Panties == 'bikini bottoms'", Recolor("Emma", "Panties", "images/EmmaSex/Emma_Sex_Panties_Bikini_S.png"),
            "EmmaX.Panties and EmmaX.Wet", Recolor("Emma", "Panties", "images/EmmaSex/Emma_Sex_Panties_SW.png"),
            "EmmaX.Panties", Recolor("Emma", "Panties", "images/EmmaSex/Emma_Sex_Panties_S.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # pantyhose
            "(EmmaX.Panties and EmmaX.PantiesDown)", Null(),
            "EmmaX.Hose == 'ripped pantyhose'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_Sex_Hose_PantyhoseHoled_S.png"),
            "Player.Sprite and Player.Cock == 'in'", Null(),
            "EmmaX.Hose == 'pantyhose'", Recolor("Emma", "Hose", "images/EmmaSex/Emma_Sex_Hose_Pantyhose_S.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # piercings
            "(not EmmaX.Panties and EmmaX.Hose != 'pantyhose') or EmmaX.PantiesDown", Null(),
            "EmmaX.Hose == 'pantyhose' and EmmaX.PantiesDown", Null(),
            "EmmaX.Pierce == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_S_C.png",
            "EmmaX.Pierce == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S_C.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # legs
            "EmmaX.Legs == 'dress' and (EmmaX.Upskirt or Player.Sprite)", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_Dress_S_Up.png"),
            "EmmaX.Legs == 'dress'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_Dress_S.png"),
            "EmmaX.Legs == 'skirt'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_Skirt_Pussy.png"),
            "EmmaX.Upskirt", Null(),
            "EmmaX.Legs == 'pants' and EmmaX.Wet >= 2", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_Pants_SW.png"),
            "EmmaX.Legs == 'pants'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_Pants_S.png"),
            "EmmaX.Legs == 'yoga pants' and EmmaX.Wet >= 2", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_YogaPants_SW.png"),
            "EmmaX.Legs == 'yoga pants'", Recolor("Emma", "Legs", "images/EmmaSex/Emma_Sex_YogaPants_S.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # piercings over
            "(EmmaX.Legs != 'pants' and EmmaX.Legs != 'yoga pants') or EmmaX.Upskirt", Null(),
            "EmmaX.Pierce == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_S_C.png",
            "EmmaX.Pierce != 'ring'", Null(),
            "EmmaX.Panties and not EmmaX.PantiesDown", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S_C.png",
            "EmmaX.Hose == 'pantyhose' and not EmmaX.PantiesDown", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S_C.png",
            "True", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S_C.png",
            ),
        (0,0), ConditionSwitch(
            # boots
            "(EmmaX.Legs == 'pants' or EmmaX.Legs == 'yoga pants') and EmmaX.Upskirt", Null(),
            "EmmaX.Boots == 'thigh boots'", Recolor("Emma", "Boots", "images/EmmaSex/Emma_Sex_Boots_Pussy.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # Over
            "EmmaX.Over == 'nighty'", Recolor("Emma", "Over", "images/EmmaSex/Emma_Sex_Nighty_Pussy.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # spunk
            "'belly' in EmmaX.Spunk and Player.Male", "images/EmmaSex/Emma_Spunk_Belly.png",
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #Panties if up
#            "not EmmaX.Panties or EmmaX.PantiesDown", Null(),
#            "Player.Sprite and (Player.Cock == 'sex' or Player.Cock == 'anal')", Null(),  #hide if sexing
#            "EmmaX.Panties == 'lace panties'", "images/EmmaSex/Emma_Sex_Panties_Lace.png",
#            "EmmaX.Panties == 'green panties' and EmmaX.Wet", "images/EmmaSex/Emma_Sex_Panties_Green_Wet.png",
#            "EmmaX.Panties == 'green panties' or EmmaX.Panties == 'bikini bottoms'", "images/EmmaSex/Emma_Sex_Panties_Green.png",
#            "EmmaX.Panties == 'shorts' and EmmaX.Wet", "images/EmmaSex/Emma_Sex_Panties_Shorts_Wet.png",
#            "EmmaX.Panties == 'shorts'", "images/EmmaSex/Emma_Sex_Panties_Shorts.png",
#            "EmmaX.Wet", "images/EmmaSex/Emma_Sex_Panties_Black_Wet.png",
#            "True", "images/EmmaSex/Emma_Sex_Panties_Black.png",
#            ),

#        (0,0), ConditionSwitch(
#            #Hose layer (add panties up dependencies)
#            #"EmmaX.PantiesDown", Null(),
#            "EmmaX.Hose == 'ripped pantyhose'", "images/EmmaSex/Emma_Sex_Hose_Legs_Full_Hole.png",
#            "EmmaX.Hose == 'ripped tights'", "images/EmmaSex/Emma_Sex_Hose_Legs_Tights_Hole.png",
#            "EmmaX.Hose == 'stockings'", "images/EmmaSex/Emma_Sex_Hose_Legs_Stockings.png",
#            "EmmaX.Hose == 'stockings and garterbelt'", "images/EmmaSex/Emma_Sex_Hose_Legs_StockingGarter.png",
#            "EmmaX.Hose == 'garterbelt'", "images/EmmaSex/Emma_Sex_Hose_Legs_Garter.png",
#            "EmmaX.PantiesDown", Null(),
#            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),  #hide if sexing
#            "EmmaX.Hose == 'pantyhose'", "images/EmmaSex/Emma_Sex_Hose_Legs_Full.png",
#            "EmmaX.Hose == 'tights' and EmmaX.Wet", "images/EmmaSex/Emma_Sex_Hose_Legs_Tights_Wet.png",
#            "EmmaX.Hose == 'tights'", "images/EmmaSex/Emma_Sex_Hose_Legs_Tights.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #Legs Layer
#            "EmmaX.Legs == 'skirt'", "images/EmmaSex/Emma_Sex_Legs_Skirt.png",
#            "EmmaX.Upskirt", Null(),
#            "EmmaX.Legs == 'pants' and EmmaX.Wet > 1", "images/EmmaSex/Emma_Sex_Legs_Pants_Wet.png",
#            "EmmaX.Legs == 'pants'","images/EmmaSex/Emma_Sex_Legs_Pants.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #Sweater
#            "EmmaX.Acc == 'sweater'", "images/EmmaSex/Emma_Sex_Sweater.png",
#            "True", Null(),
#            ),
##        (0,0), ConditionSwitch(
##            #Over Layer
##            "EmmaX.Over == 'towel'", "images/KittySex/Kitty_Sex_Towel_Legs.png",
##            "True", Null(),
##            ),
#        (0,0),ConditionSwitch(
#            #Outside Spunk
#            "'belly' in EmmaX.Spunk and Player.Male", "images/KittySex/Kitty_Sex_Spunk_Pelvis.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #pussy licking animation
#            "Player.Sprite", Null(),
#            "Trigger == 'lick pussy'", "Emma_Sex_Lick_Pussy",
#            "Trigger == 'lick ass'", "Emma_Sex_Lick_Ass",
#            "EmmaX.Offhand == 'fondle pussy' and EmmaX.Lust > 60", At("EmmaFingerHand", GirlFingerPussyX()),
#            "EmmaX.Offhand == 'fondle pussy'", At("EmmaMastHand", GirlGropePussyX()),
#            "True", Null()
#            ),
#        (0,0), ConditionSwitch(
#            #Shows different lower body motion depending on events
#            "not Speed or Player.Cock == 'foot' or ShowFeet", "Emma_Sex_Feet",
#            #"Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Emma_Sex_Feet", "images/KittySex/Kitty_Sex_FeetMask.png"),
#            "True", AlphaMask("Emma_Sex_Feet","images/EmmaSex/Emma_Sex_FeetMask2.png")
#            ),
        )
# End Emma Scissor Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Emma_SC_Anim_0:
        #this is the animation for Emma's lower body during Scissoring, Speed 0 (static)
        contains:
            subpixel True
            "Emma_SC_Legs"#"Emma_SC_Legs"
            anchor (560,580)#(560,420)
            offset (710,390) #(560,580)
            transform_anchor True
            zoom 1.4
            rotate 15
            pos (18,-50) #X less is left, Y less is up
#            parallel:
#                pause .5
#                ease 2 rotate 30
#                pause .5
#                ease 2 rotate 35
#                repeat
            parallel:
                ease 2 pos (18,-60)
                pause .5
                ease 2 pos (18,-50)
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
        contains:
            subpixel True
            "Emma_Sex_Body"
            anchor (560,580)#(560,420)
            offset (710,380) #(560,580)
            transform_anchor True
            zoom 1.5
            rotate 0
            pos (0,0) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                ease 2 pos (0,10)
                pause .5
                ease 2 pos (0,0)
                pause .5
                repeat
#        contains:
#            subpixel True
##            "Emma_Sex_Feet"
#            ConditionSwitch(
#                #Shows different lower body motion depending on events
#                "ShowFeet", "Emma_Sex_Feet",
#                "True", AlphaMask("Emma_Sex_Feet","images/EmmaSex/Emma_Sex_FeetMask2.png")
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
        #end animation for Emma's lower body during Scissoring, Speed 0 (static) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Emma_SC_Anim_1:
        #this is the animation for Emma's lower body during Scissoring, Speed 1 (slow)
        contains:
            subpixel True
            "Emma_SC_Legs"#"Emma_SC_Legs"
            anchor (560,580)#(560,420)
            offset (710,390) #(560,580)
            transform_anchor True
            zoom 1.4
            rotate 15
            pos (12,-50) #X less is left, Y less is up
            parallel:
#                pause .5
                ease 1.5 rotate 10
#                pause .5
                ease 1.5 rotate 15
                repeat
            parallel:
                ease 1 pos (12,-60)
                pause .5
                ease 1 pos (12,-50)
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
            "Emma_Sex_Body"
            anchor (560,580)#(560,420)
            offset (710,380) #(560,580)
            transform_anchor True
            zoom 1.5
            rotate 0
            pos (0,0) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                ease 1 pos (0,10)
                pause .5
                ease 1 pos (0,0)
                pause .5
                repeat
#        contains:
#            subpixel True
##            "Emma_Sex_Feet"
#            ConditionSwitch(
#                #Shows different lower body motion depending on events
#                "ShowFeet", "Emma_Sex_Feet",
#                "True", AlphaMask("Emma_Sex_Feet","images/EmmaSex/Emma_Sex_FeetMask2.png")
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
        #End animation for Emma's lower body during Scissoring, Speed 1 (slow) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Emma_SC_Anim_2:
        #this is the animation for Emma's lower body during Scissoring, Speed 2 (fast)
        contains:
            subpixel True
            "Emma_SC_Legs"#"Emma_SC_Legs"
            anchor (560,580)#(560,420)
            offset (710,390) #(560,580)
            transform_anchor True
            zoom 1.4
            rotate 15
            pos (18,-50) #X less is left, Y less is up
            parallel:
                ease .5 rotate 12
                pause .1
                ease .5 rotate 15
                repeat
            parallel:
                ease .5 pos (18,-40)
                ease .5 pos (18,-50)
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
            "Emma_Sex_Body"
            anchor (560,580)#(560,420)
            offset (710,380) #(560,580)
            transform_anchor True
            zoom 1.5
            rotate 0
            pos (0,0) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                pause .1
                ease .5 pos (0,10)
                ease .5 pos (0,0)
                repeat
#        contains:
#            subpixel True
##            "Emma_Sex_Feet"
#            ConditionSwitch(
#                #Shows different lower body motion depending on events
#                "ShowFeet", "Emma_Sex_Feet",
#                "True", AlphaMask("Emma_Sex_Feet","images/EmmaSex/Emma_Sex_FeetMask2.png")
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
        #End animation for Emma's lower body during Scissoring, Speed 2 (fast) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     SC Launch/Reset
label Emma_SC_Launch(Line = Trigger):
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    return
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary

    $ Trigger = Line

    if renpy.showing("Emma_SC_Sprite"):
        return
    $ Speed = 0
    call Girl_Hide(EmmaX,1) #call Rogue_Hide
    show Emma_SC_Sprite zorder 150
    with dissolve
    return

label Emma_SC_Reset:
    if not renpy.showing("Emma_SC_Sprite"):
        return
    $ EmmaX.ArmPose = 2
    hide Emma_SC_Sprite
    call Girl_Hide(EmmaX) #call Rogue_Hide
#    call Set_The_Scene(Dress = 0)
    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
        alpha 1 zoom 1 offset (0,0) anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return
# End Emma Scissor Pose content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

# Emma Misc Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#image Test_Object:                 #this is the yellow rectangle
#    contains:
#        Solid("#d5f623", xysize=(1024, 678))
#    anchor (0,0)
#    alpha .8

#image Emma_At_DeskB:
#    contains:
#        subpixel True
#        "Emma_Sprite"
#        zoom 0.29
#        pos (450,190) #(500,200)
#    contains:
##        AlphaMask("Test_Object", "images/ClassroomFront.png")
#        AlphaMask("images/Classroom.jpg", "images/ClassroomFront.png")
#    contains:
#        ConditionSwitch(
#                "bg_current != 'bg classroom' or Current_Time == 'Evening' or Current_Time == 'Night' or Weekday >= 5", Null(),
#                "True", "images/ClassroomPupils.png",
#                )

#image Emma_At_PodiumB:
#    contains:
#        subpixel True
#        "Emma_Sprite"
#        zoom 0.29
#        pos (670,180) #(500,200)
#    contains:
##        AlphaMask("Test_Object", "images/ClassroomFront.png")
#        AlphaMask("images/Classroom.jpg", "images/ClassroomFront.png")
#    contains:
#        ConditionSwitch(
#                "bg_current != 'bg classroom' or Current_Time == 'Evening' or Current_Time == 'Night' or Weekday >= 5", Null(),
#                "True", "images/ClassroomPupils.png",
#                )

image Emma_At_Desk:
    contains:
        subpixel True
        "Emma_Sprite"
        zoom 0.29
        pos (450,190) #(500,200)

image Emma_At_Podium:
    contains:
        subpixel True
        "Emma_Sprite"
        zoom 0.29
        pos (670,180) #(500,200)


image Emma_Behind_Podium:
    contains:
        subpixel True
        "Emma_Sprite"
        zoom 0.29
        pos (640,180) #(500,200)
        block:
            subpixel True
            ease .5 ypos 183
            ease .5 ypos 180
            pause .5
            repeat



#label Emma_Kissing_Launch(T = Trigger,Set=1):
#    call Emma_Hide
#    $ Trigger = T
#    $ EmmaX.Pose = "kiss" if Set else EmmaX.Pose
#    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer
#    show Emma_Sprite at SpriteLoc(StageCenter) zorder EmmaX.Layer:
#        ease 0.5 offset (0,0) zoom 2 alpha 1
#    return

#label Emma_Kissing_Smooch:
#    $ EmmaX.FaceChange("kiss")
#    show Emma_Sprite at SpriteLoc(StageCenter) zorder EmmaX.Layer:
#        ease 0.5 xpos StageCenter offset (0,0) zoom 2 alpha 1
#        pause 1
#        ease 0.5 xpos EmmaX.SpriteLoc zoom 1
#    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
#        zoom 1
#    $ EmmaX.FaceChange("sexy")
#    return

#label Emma_Breasts_Launch(T = Trigger,Set=1):
#    call Emma_Hide
#    $ Trigger = T
#    $ EmmaX.Pose = "breasts" if Set else EmmaX.Pose
#    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
##        ease 0.5 offset (-100,-200) zoom 2
#        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
#    return

#label Emma_Middle_Launch(T = Trigger,Set=1):
#    call Emma_Hide
#    $ Trigger = T
#    $ EmmaX.Pose = "mid" if Set else EmmaX.Pose
#    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
##        ease 0.5 offset (-100,-200) zoom 2
#        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
#    return

#label Emma_Pussy_Launch(T = Trigger,Set=1):
#    call Emma_Hide
#    $ Trigger = T
#    $ EmmaX.Pose = "pussy" if Set else EmmaX.Pose
#    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
#        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
#    return

#label Emma_Pos_Reset(T = 0,Set=0):
#    if EmmaX.Loc != bg_current:
#            return
#    call Emma_Hide
#    show Emma_Sprite at SpriteLoc(EmmaX.SpriteLoc) zorder EmmaX.Layer:
#        ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
#    show Emma_Sprite zorder EmmaX.Layer:
#        offset (0,0)
#        anchor (0.5, 0.0)
#        zoom 1
#        xzoom 1
#        yzoom 1
#        alpha 1
#        pos (EmmaX.SpriteLoc,50)
#    $ EmmaX.Pose = "full" if Set else 0
#    $ Trigger = T
#    return

#label Emma_Hide(Sprite=0):
##        call Emma_Sex_Reset
#        hide Emma_SexSprite
#        hide Emma_Doggy_Animation
#        hide Emma_HJ_Animation
#        hide Emma_BJ_Animation
#        hide Emma_TJ_Animation
#        hide Emma_FJ_Animation
#        hide Emma_Finger_Animation
#        hide Emma_CUN_Animation
#        if Sprite:
#                hide Emma_Sprite
#        return



# Interface items //////////////////////////////////////////////////////////////////////////////

image GropeLeftBreast_Emma:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65#.7
        pos (215,400)#(215,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block:
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image GropeRightBreast_Emma:
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (110,400)#(120,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -90
        block:
            ease 1 rotate -60 #-30
            ease 1 rotate -90 #-60
            repeat

#image GropeBreast:
image LickRightBreast_Emma:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5
        xzoom -0.45
        pos (105,375)#(115,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (85,345)#(95,370)
            pause .5
            ease 1.5 rotate 30 pos (105,375)#(115,400)
            repeat

image LickLeftBreast_Emma:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5
        xzoom -0.45
        pos (205,370) #(200,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (190,350)#(190,380)
            pause .5
            ease 1.5 rotate 30 pos (205,370)#(200,410)
            repeat

image GropeThigh_Emma:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (180,670)#(200,720)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        block:
            pause .5
            ease 1 rotate 110 pos (150,750)
            ease 1 rotate 100 pos (180,670)
            repeat

image GropePussy_Emma:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (200,600)#(210,640) -20
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease .5 rotate 190 pos (200,585)
                ease .75 rotate 170 pos (200,600)
            choice:
                ease .5 rotate 190 pos (200,585)
                pause .25
                ease 1 rotate 170 pos (200,600)
            repeat

image FingerPussy_Emma:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.65
        pos (210,665)#(220,730)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (220,640)#(230,695)
                pause .5
                ease 1 rotate 50 pos (210,665)  #(220,730)
            choice:
                ease .5 rotate 40 pos (220,640)
                pause .5
                ease 1.75 rotate 50 pos (210,665)
            choice:
                ease 2 rotate 40 pos (220,640)
                pause .5
                ease 1 rotate 50 pos (210,665)
            choice:
                ease .25 rotate 40 pos (220,640)
                ease .25 rotate 50 pos (210,665)
                ease .25 rotate 40 pos (220,640)
                ease .25 rotate 50 pos (210,665)
            repeat

image Lickpussy_Emma:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (230,625)#(240,680)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout .5 rotate -50 pos (210,605) #(220,660)
            linear .5 rotate -60 pos (200,615) #(210,670)
            easein 1 rotate 10 pos (230,625) #(240,680)
            repeat

image VibratorRightBreast_Emma:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (150,380)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 370
            pause .25
            ease 1 rotate 55 ypos 380
            pause .25
            repeat

image VibratorLeftBreast_Emma:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (270,400)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 390
            pause .25
            ease 1 rotate 55 ypos 400
            pause .25
            repeat

image VibratorPussy_Emma:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,665)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 70
        block:
            ease 1 rotate 35 xpos 230 ypos 655
            pause .25
            ease 1 rotate 70 xpos 240 ypos 665
            pause .25
            repeat

image VibratorAnal_Emma:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (270,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 10
        block:
            ease 1 rotate 0 xpos 260 ypos 655
            pause .25
            ease 1 rotate 10 xpos 270 ypos 665
            pause .25
            repeat

image VibratorPussyInsert_Emma:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_Emma:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0



#Lesbian action animations.
image GirlGropeBothBreast_Emma:
    contains:
        "GirlGropeLeftBreast_Emma"
    contains:
        "GirlGropeRightBreast_Emma"

image GirlGropeLeftBreast_Emma:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (240,370)#(240,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -20
        block:
            ease 1 rotate -40 pos (230,360)#(280,390)
            ease 1 rotate -20 pos (240,370)
            repeat

image GirlGropeRightBreast_Emma:
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (90,380) #(110,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block:
            ease 1 rotate -30 pos (90,410)#(110,410)
            ease 1 rotate -10 pos (90,380)
            repeat

image GirlGropeThigh_Emma:
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

image GirlGropePussy_EmmaSelf:
    contains:
        "GirlGropePussy_Emma"
        anchor (0.5,0.5)
        rotate -40
#        yzoom -1
        pos (120,530)

image GirlGropePussy_Emma:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (200,575)#(210,625)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (205,590)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 pos (205,590)#-10+20
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (205,590)
                ease .75 rotate 200 pos (205,595)
                ease .5 rotate 205 pos (205,590)
                ease .75 rotate 200 pos (205,595)
            choice: #Fast stroke
                ease .3 rotate 205 pos (205,590)
                ease .3 rotate 200 pos (205,600)
                ease .3 rotate 205 pos (205,590)
                ease .3 rotate 200 pos (205,600)
            repeat

image GirlFingerPussy_Emma:
    contains:
        subpixel True
        "UI_GirlFinger"
        zoom .6
        pos (220,640)#(220,635)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (220,645)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 pos (220,645)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (220,655)
                ease .75 rotate 200 pos (220,660)
                ease .5 rotate 205 pos (220,655)
                ease .75 rotate 200 pos (220,660)
            choice: #Fast stroke
                ease .3 rotate 205 pos (220,655)
                ease .3 rotate 200 pos (220,665)
                ease .3 rotate 205 pos (220,655)
                ease .3 rotate 200 pos (220,665)
            repeat

image EmmaMastHand:
        "images/UI_GirlHand_Emma.png"
        zoom 0.95
        rotate 240
        offset (360,210)

image EmmaFingerHand:
        "images/UI_GirlFinger_Emma.png"
        zoom 0.95
        rotate 220
        offset (320,280)
