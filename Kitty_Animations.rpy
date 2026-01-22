# Basic Kitty Sprites

image Kitty_Sprite:
    LiveComposite(
        (480,960),
        (0,0), "images/KittySprite/Kitty_Sprite_Shadow.png",
        (124,0), "Kitty_HairBack",
#        (124,0), ConditionSwitch(
#            "renpy.showing('Kitty_BJ_Animation')", Null(),
#            "True", "Kitty_HairBack",
#            ),
        (0,0), ConditionSwitch(
            #back of dress
            "KittyX.Legs == 'dress' and KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittySprite/Kitty_Sprite_Legs_Dress_Back.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Arms1
            "KittyX.ArmPose == 1", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Arms1.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #back of the shirt
            "KittyX.Over == 'pink top' and KittyX.ArmPose != 1", Recolor("Kitty", "Over", "images/KittySprite/Kitty_Sprite_Under_Pink2.png"),       #2
            "KittyX.Over == 'pink top'", Recolor("Kitty", "Over", "images/KittySprite/Kitty_Sprite_Under_Pink1.png"),                  #1
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #body
            "KittyX.ArmPose != 1 and KittyX.Pubes", Recolor("Kitty", "Pubes", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Body_Hair2.png"),
            "KittyX.ArmPose != 1", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Body_Bare2.png",
            "KittyX.Pubes", Recolor("Kitty", "Pubes", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Body_Hair1.png"),
            "True", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Body_Bare1.png",
            ),

#        (0,0), ConditionSwitch(
#            #wet look
#            "KittyX.Water and KittyX.ArmPose", "images/KittySprite/Kitty_Sprite_Water2.png",
#            "KittyX.Water", "images/KittySprite/Kitty_Sprite_Water1.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #piercings bottom
            "not KittyX.Pierce or (KittyX.Panties and not KittyX.PantiesDown)", Null(),
            "KittyX.Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingB.png",
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallB.png",
            ),

#        (0,0), ConditionSwitch(
#            #panties
#            "not KittyX.Panties or KittyX.PantiesDown", Null(),
#            "KittyX.Legs or KittyX.Upskirt", Null(), #If panties are down, and pants are either off or down, skip this

#            "not KittyX.Panties or not KittyX.PantiesDown", Null(), #If panties are not down or if  pants are on and up, skip this
#            "KittyX.Legs and KittyX.Legs != 'blue skirt' and not KittyX.Upskirt", Null(), #If panties are not down or if  pants are on and up, skip this

#            "KittyX.Wet and KittyX.Panties == 'green panties'", Recolor("Kitty", "Panties", "images/KittySprite/Kitty_Sprite_Panties_Green_Wet.png"),
#            "KittyX.Wet and KittyX.Panties == 'lace panties'", Recolor("Kitty", "Panties", "images/KittySprite/Kitty_Sprite_Panties_Lace_Wet.png"),
#            "KittyX.Wet and KittyX.Panties == 'bikini bottoms'", Recolor("Kitty", "Panties", "images/KittySprite/Kitty_Sprite_Panties_Bikini_Wet.png"),
#            "KittyX.Panties == 'green panties'", Recolor("Kitty", "Panties", "images/KittySprite/Kitty_Sprite_Panties_Green.png"),
#            "KittyX.Panties == 'lace panties'", Recolor("Kitty", "Panties", "images/KittySprite/Kitty_Sprite_Panties_Lace.png"),
#            "KittyX.Panties == 'bikini bottoms'", Recolor("Kitty", "Panties", "images/KittySprite/Kitty_Sprite_Panties_Bikini.png"),
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #panties down
#            "not KittyX.Panties or not KittyX.PantiesDown", Null(), #If panties are not down or if  pants are on and up, skip this
#            "KittyX.Legs and KittyX.Legs != 'blue skirt' and not KittyX.Upskirt", Null(), #If panties are not down or if  pants are on and up, skip this
#            "KittyX.Wet and KittyX.Panties == 'green panties'", Recolor("Kitty", "Panties", "images/KittySprite/Kitty_Sprite_Panties_Green_Down_Wet.png"),
#            "KittyX.Wet and KittyX.Panties == 'lace panties'", Recolor("Kitty", "Panties", "images/KittySprite/Kitty_Sprite_Panties_Lace_Down_Wet.png"),
#            "KittyX.Wet and KittyX.Panties == 'bikini bottoms'", Recolor("Kitty", "Panties", "images/KittySprite/Kitty_Sprite_Panties_Bikini_DownW.png"),
#            "KittyX.Panties == 'green panties'", Recolor("Kitty", "Panties", "images/KittySprite/Kitty_Sprite_Panties_Green_Down.png"),
#            "KittyX.Panties == 'lace panties'", Recolor("Kitty", "Panties", "images/KittySprite/Kitty_Sprite_Panties_Lace_Down.png"),
#            "KittyX.Panties == 'bikini bottoms'", Recolor("Kitty", "Panties", "images/KittySprite/Kitty_Sprite_Panties_Bikini_Down.png"),
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #under hose layer
            "KittyX.Hose == 'stockings and garterbelt'", Recolor("Kitty", "Hose", "images/KittySprite/Kitty_Sprite_Hose_StockingGarter.png"),
            "KittyX.Hose == 'garterbelt'", Recolor("Kitty", "Hose", "images/KittySprite/Kitty_Sprite_Hose_Garter.png"),
            "KittyX.Hose == 'stockings'", Recolor("Kitty", "Hose", "images/KittySprite/Kitty_Sprite_Hose_Stockings.png"),
            "KittyX.Hose == 'knee stockings'", Recolor("Kitty", "Hose", "images/KittySprite/Kitty_Sprite_Hose_Knee.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #panties layer
            "not KittyX.PantiesDown or (KittyX.Legs and KittyX.Legs != 'blue skirt' and not KittyX.Upskirt)", ConditionSwitch(
                    # if the panties aren't down. . .
                    # and she's not wearing pants that are up
                    "KittyX.Panties == 'lace panties'", Recolor("Kitty", "Panties", "images/KittySprite/Kitty_Sprite_Panties_Lace.png"),
                    "KittyX.Wet", ConditionSwitch(
                            # if they're up and wet. . .
                            "KittyX.Panties == 'green panties'", Recolor("Kitty", "Panties", "images/KittySprite/Kitty_Sprite_Panties_Green_Wet.png"),
                            "KittyX.Panties == 'bikini bottoms'", Recolor("Kitty", "Panties", "images/KittySprite/Kitty_Sprite_Panties_Bikini_Wet.png"),
                            # Modification mode
                            "KittyX.Panties == 'nighty panties'", "images/KittySprite/modification/Kitty_sprite_panties_nighty_wet.png",
                            # -----------------
                            "True", Null(),
                            ),
                    "True", ConditionSwitch(
                            #if they're just up. . .
                            "KittyX.Panties == 'green panties'", Recolor("Kitty", "Panties", "images/KittySprite/Kitty_Sprite_Panties_Green.png"),
                            "KittyX.Panties == 'bikini bottoms'", Recolor("Kitty", "Panties", "images/KittySprite/Kitty_Sprite_Panties_Bikini.png"),
                            # Modification mode
                            "KittyX.Panties == 'nighty panties'", "images/KittySprite/modification/Kitty_sprite_panties_nighty.png",
                            # -----------------
                            "True", Null(),
                            ),
                    ),
            "KittyX.Panties == 'lace panties'", Recolor("Kitty", "Panties", "images/KittySprite/Kitty_Sprite_Panties_Lace_Down.png"),
            "KittyX.Wet", ConditionSwitch(
                    #if wet and down. . .
#                    "KittyX.Legs and KittyX.Legs != 'blue skirt' and not KittyX.Upskirt", Null(), #If nor wearing a skirt, they would be invisible
                    "KittyX.Panties == 'green panties'", Recolor("Kitty", "Panties", "images/KittySprite/Kitty_Sprite_Panties_Green_Down_Wet.png"),
                    "KittyX.Panties == 'bikini bottoms'", Recolor("Kitty", "Panties", "images/KittySprite/Kitty_Sprite_Panties_Bikini_DownW.png"),
                    # Modification mode
                    "KittyX.Panties == 'nighty panties'", "images/KittySprite/modification/Kitty_sprite_panties_nighty_down_wet.png",
                    # -----------------
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                    # if not wet, but down
#                    "KittyX.Legs and KittyX.Legs != 'blue skirt' and not KittyX.Upskirt", Null(), #If nor wearing a skirt, they would be invisible
                    "KittyX.Panties == 'green panties'", Recolor("Kitty", "Panties", "images/KittySprite/Kitty_Sprite_Panties_Green_Down.png"),
                    "KittyX.Panties == 'bikini bottoms'", Recolor("Kitty", "Panties", "images/KittySprite/Kitty_Sprite_Panties_Bikini_Down.png"),
                    # Modification mode
                    "KittyX.Panties == 'nighty panties'", "images/KittySprite/modification/Kitty_sprite_panties_nighty_down.png",
                    # ----------------
                    "True", Null(),
                    ),
            ),


        (0,0), ConditionSwitch(
            #over hose layer
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "KittyX.Hose == 'pantyhose'", Recolor("Kitty", "Hose", "images/KittySprite/Kitty_Sprite_Hose_Pantyhose.png"),
            "KittyX.Hose == 'ripped pantyhose'", Recolor("Kitty", "Hose", "images/KittySprite/Kitty_Sprite_Hose_RippedPantyhose.png"),
            "True", Null(),
            ),
        (225,560), ConditionSwitch(
            #Personal Wetness
            "not KittyX.Wet", Null(),
            "KittyX.Legs and not KittyX.Upskirt", Null(),
            "KittyX.Panties and not KittyX.PantiesDown and KittyX.Wet <= 1", Null(),
            "KittyX.Wet == 1", ConditionSwitch( #Wet = 1
                    "KittyX.Panties and KittyX.PantiesDown", AlphaMask("Wet_Drip","Kitty_Drip_MaskP"),
                    "KittyX.Legs", AlphaMask("Wet_Drip","Kitty_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip","Kitty_Drip_Mask"), #only plays if nothing is in the way
                    ),
            "True", ConditionSwitch( #Wet = 2+
                    "KittyX.Panties and KittyX.PantiesDown", AlphaMask("Wet_Drip2","Kitty_Drip_MaskP"), #"Wet_Drip2",#
                    "KittyX.Legs", AlphaMask("Wet_Drip2","Kitty_Drip_MaskP"),
                    "KittyX.Panties", AlphaMask("Wet_Drip","Kitty_Drip_Mask"), #"Wet_Drip2",#
                    "True", AlphaMask("Wet_Drip2","Kitty_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (0,0), ConditionSwitch(
            #wetness
            "KittyX.Legs or not KittyX.Wet", Null(),
            "KittyX.Panties and not KittyX.PantiesDown and KittyX.Wet < 2", Null(),
            "KittyX.Panties and not KittyX.PantiesDown", "images/KittySprite/Kitty_Sprite_Wet1.png",
            "KittyX.Wet == 2", "images/KittySprite/Kitty_Sprite_Wet2.png",
            "True", "images/KittySprite/Kitty_Sprite_Wet1.png",
            ),
        (225,560), ConditionSwitch(
            #Spunk nethers
            "('in' not in KittyX.Spunk and 'anal' not in KittyX.Spunk) or not Player.Male", Null(),
            "KittyX.Legs and not KittyX.Upskirt", Null(),
            "True", ConditionSwitch( #Wet = 2+
                    "KittyX.Panties and KittyX.PantiesDown", AlphaMask("Spunk_Drip2","Kitty_Drip_MaskP"), #"Wet_Drip2",#
                    "KittyX.Legs", AlphaMask("Spunk_Drip2","Kitty_Drip_MaskP"),
                    "True", AlphaMask("Spunk_Drip2","Kitty_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (0,0), ConditionSwitch(
            #pants
            "KittyX.Legs == 'blue skirt' and KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittySprite/Kitty_Sprite_Skirt_Up.png"),
            "KittyX.Legs == 'blue skirt'", Recolor("Kitty", "Legs", "images/KittySprite/Kitty_Sprite_Skirt.png"),
            "KittyX.Legs == 'dress' and KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittySprite/Kitty_Sprite_Legs_Dress_Up.png"),
            "KittyX.Legs == 'dress'", Recolor("Kitty", "Legs", "images/KittySprite/Kitty_Sprite_Legs_Dress.png"),
            "not KittyX.Legs or KittyX.Upskirt", Null(),
            "KittyX.Legs == 'capris'", Recolor("Kitty", "Legs", "images/KittySprite/Kitty_Sprite_Pants_Blue.png"),
            "KittyX.Legs == 'black jeans'", Recolor("Kitty", "Legs", "images/KittySprite/Kitty_Sprite_Pants_Black.png"),
            "KittyX.Wet and KittyX.Legs == 'yoga pants'", Recolor("Kitty", "Legs", "images/KittySprite/Kitty_Sprite_Pants_Yoga_Wet.png"),
            "KittyX.Legs == 'yoga pants'", Recolor("Kitty", "Legs", "images/KittySprite/Kitty_Sprite_Pants_Yoga.png"),
            "KittyX.Wet and KittyX.Legs == 'shorts'", Recolor("Kitty", "Legs", "images/KittySprite/Kitty_Sprite_Shorts_Wet.png"),
            "KittyX.Legs == 'shorts'", Recolor("Kitty", "Legs", "images/KittySprite/Kitty_Sprite_Shorts.png"),
            # Modification mode
            "KittyX.Legs == 'bottom harem' and KittyX.Upskirt", "images/KittySprite/modification/Kitty_sprite_skirt_harem_up.png",
            "KittyX.Legs == 'bottom harem'", "images/KittySprite/modification/Kitty_sprite_skirt_harem.png",
            # ----------------
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #boots layer
            "KittyX.Boots", "images/KittySprite/Kitty_Sprite_Boots_Sandals.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Arms2
            "KittyX.ArmPose != 1", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Arms2.png",
            "True", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Chest_Bare.png",
            ),
#        (0,0), "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Chest_Bare.png",


        (0,0), ConditionSwitch(
            #piercings top
            "not KittyX.Pierce", Null(),
            "KittyX.Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingT.png",
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallT.png",
            ),
#        (0,0), ConditionSwitch(
#            #Bra
#            "not KittyX.Chest", Null(),
#            "KittyX.ArmPose and KittyX.Chest == 'cami'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Cami2.png"),
#            "KittyX.ArmPose and KittyX.Chest == 'bikini top'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bikini2.png"),
#            "KittyX.Chest == 'bikini top'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bikini1.png"),
#            "KittyX.Chest == 'lace bra'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bra_Lace.png"),
#            "KittyX.Chest == 'sports bra'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bra_Sport.png"),
#            "KittyX.Chest == 'bra'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bra_Basic.png"),
#            "KittyX.Chest == 'cami'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Cami1.png"),
#            "KittyX.Chest == 0 and KittyX.Over == 'pink top'", Null(),   #use for when bra and top clash
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #necklace
            "KittyX.Neck == 'gold necklace'", "images/KittySprite/Kitty_Sprite_Necklace1.png",
            "KittyX.Neck == 'star necklace'", "images/KittySprite/Kitty_Sprite_Necklace2.png",
            "KittyX.Neck == 'flower necklace'", "images/KittySprite/Kitty_Sprite_Necklace3.png",
            # Modification mode
            "KittyX.Neck == 'nighty collar'", "images/KittySprite/modification/Kitty_sprite_neck_nighty_collar.png",
            # -----------------
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #bra layer
            "not KittyX.Chest", Null(),
            "not KittyX.Uptop", ConditionSwitch(
                    #if the top's down. . .
                    "KittyX.ArmPose != 1 and KittyX.Chest == 'cami'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Cami2.png"),
                    "KittyX.ArmPose != 1 and KittyX.Chest == 'bikini top'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bikini2.png"),
                    "KittyX.ArmPose != 1 and KittyX.Chest == 'dress'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bra_Dress2.png"),
                    "KittyX.Chest == 'bikini top'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bikini1.png"),
                    "KittyX.Chest == 'lace bra'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bra_Lace.png"),
                    "KittyX.Chest == 'sports bra'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bra_Sport.png"),
                    "KittyX.Chest == 'bra'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bra_Basic.png"),
                    "KittyX.Chest == 'cami'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Cami1.png"),
                    "KittyX.Chest == 'dress'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bra_Dress1.png"),
                    "True", Null(),
                    ),
            "KittyX.Over and KittyX.Over != 'towel'", ConditionSwitch(
                    # If she's wearing a shirt over the bra
#                    "KittyX.ArmPose and KittyX.Chest == 'cami'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Cami1_UpS.png"),
#                    "KittyX.ArmPose and KittyX.Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini2_UpS.png",
                    "KittyX.Chest == 'bikini top'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bikini1_Up.png"),
                    "KittyX.Chest == 'lace bra'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bra_Lace1_UpS.png"),
                    "KittyX.Chest == 'sports bra'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bra_Sport1_UpS.png"),
                    "KittyX.Chest == 'bra'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bra_Basic1_Up.png"),
                    "KittyX.Chest == 'cami'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Cami1_UpS.png"),
                    "KittyX.Chest == 'dress'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bra_Dress_UpS.png"),
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                    # if she's not wearing a shirt
                    "KittyX.ArmPose != 1", ConditionSwitch(
                            # if Arms 2
                            "KittyX.Chest == 'bikini top'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bikini2_Up.png"),
                            "KittyX.Chest == 'lace bra'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bra_Lace2_Up.png"),
                            "KittyX.Chest == 'sports bra'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bra_Sport2_Up.png"),
                            "KittyX.Chest == 'bra'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bra_Basic2_Up.png"),
                            "KittyX.Chest == 'cami'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Cami2_Up.png"),
                            "KittyX.Chest == 'dress'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bra_Dress_Up.png"),
                            "True", Null(),
                            ),
                    "True", ConditionSwitch(
                            # if Arms 1
                            "KittyX.Chest == 'bikini top'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bikini1_Up.png"),
                            "KittyX.Chest == 'lace bra'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bra_Lace1_Up.png"),
                            "KittyX.Chest == 'sports bra'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bra_Sport1_Up.png"),
                            "KittyX.Chest == 'bra'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bra_Basic1_Up.png"),
                            "KittyX.Chest == 'cami'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Cami1_Up.png"),
                            "KittyX.Chest == 'dress'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bra_Dress_Up.png"),
                            "True", Null(),
                            ),
                    "True", Null(),
                    ),
            ),

        (0,0), ConditionSwitch(
            #piercings over clothes
            "not KittyX.Pierce or not KittyX.Chest or KittyX.Uptop", Null(),
            "KittyX.Pierce == 'ring' and KittyX.Legs", "images/KittySprite/Kitty_Sprite_Piercing_RingOverTop.png",
            "KittyX.Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingOver.png",
            "KittyX.Legs", "images/KittySprite/Kitty_Sprite_Piercing_BallOverTop.png",
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallOver.png",
            ),
        (0,0), ConditionSwitch(
            #wet look
            "KittyX.Water and KittyX.ArmPose != 1", "images/KittySprite/Kitty_Sprite_Water2.png",
            "KittyX.Water", "images/KittySprite/Kitty_Sprite_Water1.png",
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #shirt
#            "not KittyX.Over", Null(),
#            "KittyX.ArmPose and KittyX.Over == 'pink top'", Recolor("Kitty", "Over", "images/KittySprite/Kitty_Sprite_Over_Pink2.png"),
#            "KittyX.ArmPose and KittyX.Over == 'red shirt'", Recolor("Kitty", "Over", "images/KittySprite/Kitty_Sprite_Over_Crew2.png"),
#            "KittyX.ArmPose and KittyX.Over == 'towel'", Recolor("Kitty", "Over", "images/KittySprite/Kitty_Sprite_Over_Towel2.png"),
#            "KittyX.Over == 'pink top'", Recolor("Kitty", "Over", "images/KittySprite/Kitty_Sprite_Over_Pink1.png"),
#            "KittyX.Over == 'red shirt'", Recolor("Kitty", "Over", "images/KittySprite/Kitty_Sprite_Over_Crew1.png"),
#            "KittyX.Over == 'towel'", Recolor("Kitty", "Over", "images/KittySprite/Kitty_Sprite_Over_Towel1.png"),
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #shirt layer
            "not KittyX.Over", Null(),
            "not KittyX.Uptop", ConditionSwitch(
                    #if the top's down. . .
                    "KittyX.ArmPose != 1 and KittyX.Over == 'pink top'", Recolor("Kitty", "Over", "images/KittySprite/Kitty_Sprite_Over_Pink2.png"),
                    "KittyX.ArmPose != 1 and KittyX.Over == 'red shirt'", Recolor("Kitty", "Over", "images/KittySprite/Kitty_Sprite_Over_Crew2.png"),
                    "KittyX.ArmPose != 1 and KittyX.Over == 'towel'", Recolor("Kitty", "Over", "images/KittySprite/Kitty_Sprite_Over_Towel2.png"),
                    "KittyX.ArmPose != 1 and KittyX.Over == 'jacket'", Recolor("Kitty", "Over", "images/KittySprite/Kitty_Sprite_Over_Jacket2.png"),
                    "KittyX.Over == 'pink top'", Recolor("Kitty", "Over", "images/KittySprite/Kitty_Sprite_Over_Pink1.png"),
                    "KittyX.Over == 'red shirt'", Recolor("Kitty", "Over", "images/KittySprite/Kitty_Sprite_Over_Crew1.png"),
                    "KittyX.Over == 'towel'", Recolor("Kitty", "Over", "images/KittySprite/Kitty_Sprite_Over_Towel1.png"),
                    "KittyX.Over == 'jacket'", Recolor("Kitty", "Over", "images/KittySprite/Kitty_Sprite_Over_Jacket1.png"),
                    # Modification mode
                    "KittyX.Over == 'nighty' and KittyX.ArmPose != 1", "images/KittySprite/modification/Kitty_sprite_over_nighty2.png",
                    "KittyX.Over == 'nighty'", "images/KittySprite/modification/Kitty_sprite_over_nighty1.png",
                    "KittyX.Over == 'top harem'", "images/KittySprite/modification/Kitty_sprite_over_harem_top.png",
                    # -----------------
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                    # if she's not wearing a shirt
                    "KittyX.ArmPose != 1 and KittyX.Over == 'pink top'", Recolor("Kitty", "Over", "images/KittySprite/Kitty_Sprite_Over_Pink2_Up.png"),
                    "KittyX.ArmPose != 1 and KittyX.Over == 'red shirt'", Recolor("Kitty", "Over", "images/KittySprite/Kitty_Sprite_Over_Crew2_Up.png"),
                    "KittyX.ArmPose != 1 and KittyX.Over == 'jacket'", Recolor("Kitty", "Over", "images/KittySprite/Kitty_Sprite_Over_Jacket2_Up.png"),
                    "KittyX.Over == 'pink top'", Recolor("Kitty", "Over", "images/KittySprite/Kitty_Sprite_Over_Pink1_Up.png"),
                    "KittyX.Over == 'red shirt'", Recolor("Kitty", "Over", "images/KittySprite/Kitty_Sprite_Over_Crew1_Up.png"),
                    "KittyX.Over == 'jacket'", Recolor("Kitty", "Over", "images/KittySprite/Kitty_Sprite_Over_Jacket1_Up.png"),
                    # Modification mode
                    "KittyX.Over == 'nighty' and KittyX.ArmPose != 1", "images/KittySprite/modification/Kitty_sprite_over_nighty2_up.png",
                    "KittyX.Over == 'nighty'", "images/KittySprite/modification/Kitty_sprite_over_nighty1_up.png",
                    "KittyX.Over == 'top harem'", "images/KittySprite/modification/Kitty_sprite_over_harem_top_up.png",
                    # -----------------
                    "True", Null(),
                    ),
            ),

        (0,0), ConditionSwitch(
            #bra over shirt layer
            "not KittyX.Over or not KittyX.Chest or not KittyX.Uptop", Null(),
            "KittyX.Chest == 'cami'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Cami_Over.png"),
            "KittyX.Chest == 'lace bra'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bra_Lace_Over.png"),
            "KittyX.Chest == 'sports bra'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bra_Sport_Over.png"),
            "KittyX.Chest == 'bra'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bra_Basic_Over.png"),
            "KittyX.Chest == 'bikini top'", Recolor("Kitty", "Chest", "images/KittySprite/Kitty_Sprite_Bikini_Over.png"),
            "True", Null(),
            ),

        (124,0), "Kitty_Head",
#        (124,0), ConditionSwitch(
#            "renpy.showing('Kitty_BJ_Animation')", Null(),
#            "True", "Kitty_Head",
#            ),

        (0,0), ConditionSwitch(
            #anal spunk
            "KittyX.Legs and not KittyX.Upskirt", Null(),
            "KittyX.Panties and not KittyX.PantiesDown", Null(),
            "'anal' in KittyX.Spunk and Player.Male", "images/KittySprite/Kitty_Sprite_Spunk_Anal.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy spunk
            "KittyX.Legs and not KittyX.Upskirt", Null(),
            "KittyX.Panties and not KittyX.PantiesDown", Null(),
            "'in' in KittyX.Spunk and Player.Male", "images/KittySprite/Kitty_Sprite_Spunk_Pussy.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #belly spunk
            "'belly' in KittyX.Spunk and Player.Male", "images/KittySprite/Kitty_Sprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #tits spunk
            "'tits' in KittyX.Spunk and Player.Male", "images/KittySprite/Kitty_Sprite_Spunk_Tits.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #UI tool for When Kitty is masturbating using KittyX.Offhand actions while lead
            "Trigger == 'lesbian' or not KittyX.Offhand",Null(),# or Ch_Focus is not KittyX", Null(),
            "KittyX.Offhand == 'fondle pussy' and Trigger != 'sex' and KittyX.Lust >= 70", "GirlFingerPussy_Kitty",
            "KittyX.Offhand == 'fondle pussy'", "GirlGropePussy_Kitty",
            "KittyX.Offhand == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Kitty",    #When zero is working the right breast, fondle left
            "KittyX.Offhand == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Kitty", #When zero is working the left breast, fondle right
            "KittyX.Offhand == 'fondle breasts'", "GirlGropeRightBreast_Kitty",
            "KittyX.Offhand == 'vibrator breasts'", "VibratorRightBreast_Kitty",
            "KittyX.Offhand == 'vibrator pussy'", "VibratorPussy_Kitty",
            "KittyX.Offhand == 'vibrator pussy insert'", "VibratorPussy_Kitty",
            "KittyX.Offhand == 'vibrator anal'", "VibratorAnal_Kitty",
            "KittyX.Offhand == 'vibrator anal insert'", "VibratorPussy_Kitty",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for KittyX.Offhand(lesbian) actions (ie Kitty's hand on her when Kitty is secondary)
            "not Partner or Partner is KittyX or KittyX in Nearby", Null(),
            "Partner.Offhand == 'fondle girl pussy' and Trigger != 'sex' and KittyX.Lust >= 70", "GirlFingerPussy_Kitty",
            "Partner.Offhand == 'fondle girl pussy'", "GirlGropePussy_Kitty",
            "Partner.Offhand == 'lick girl pussy'", "Lickpussy_Kitty",
            "Partner.Offhand == 'suck girl breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Kitty",
            "Partner.Offhand == 'suck girl breasts'", "LickRightBreast_Kitty",
            "Partner.Offhand == 'fondle girl breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Kitty",    #When zero is working the right breast, fondle left
            "Partner.Offhand == 'fondle girl breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Kitty", #When zero is working the left breast, fondle right
            "Partner.Offhand == 'fondle girl breasts'", "GirlGropeRightBreast_Kitty",
            "Partner.Offhand == 'vibrator girl breasts'", "VibratorRightBreast_Kitty",
            "Partner.Offhand == 'vibrator girl pussy'", "VibratorPussy_Kitty",
            "Partner.Offhand == 'vibrator girl pussy insert'", "VibratorPussy_Kitty",
            "Partner.Offhand == 'vibrator girl anal'", "VibratorAnal_Kitty",
            "Partner.Offhand == 'vibrator girl anal insert'", "VibratorPussy_Kitty",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for when RogueX is the partner in the scene, and the lead is working on her
            "not Partner or Partner is not KittyX", Null(),
            "Ch_Focus.Offhand == 'fondle girl pussy' and Trigger != 'sex' and KittyX.Lust >= 70", "GirlFingerPussy_Kitty",
            "Ch_Focus.Offhand == 'fondle girl pussy'", "GirlGropePussy_Kitty",
            "Ch_Focus.Offhand == 'lick girl pussy'", "Lickpussy_Kitty",
            "Ch_Focus.Offhand == 'suck girl breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Kitty",
            "Ch_Focus.Offhand == 'suck girl breasts'", "LickRightBreast",
            "Ch_Focus.Offhand == 'fondle girl breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Kitty",    #When zero is working the right breast, fondle left
            "Ch_Focus.Offhand == 'fondle girl breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Kitty", #When zero is working the left breast, fondle right
            "Ch_Focus.Offhand == 'fondle girl breasts'", "GirlGropeRightBreast_Kitty",
            "Ch_Focus.Offhand == 'vibrator girl breasts'", "VibratorRightBreast_Kitty",
            "Ch_Focus.Offhand == 'vibrator girl pussy'", "VibratorPussy_Kitty",
            "Ch_Focus.Offhand == 'vibrator girl pussy insert'", "VibratorPussy_Kitty",
            "Ch_Focus.Offhand == 'vibrator girl anal'", "VibratorAnal_Kitty",
            "Ch_Focus.Offhand == 'vibrator girl anal insert'", "VibratorPussy_Kitty",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger1(primary) actions
            #Kitty is primary and a sex trigger is active
            "not Trigger or Ch_Focus is not KittyX", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast_Kitty",
            "Trigger == 'fondle thighs'", "GropeThigh_Kitty",
            "Trigger == 'fondle breasts'", "GropeLeftBreast_Kitty",
            "Trigger == 'suck breasts'", "LickRightBreast_Kitty",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_Kitty",
            "Trigger == 'fondle pussy'", "GropePussy_Kitty",
            "Trigger == 'lick pussy'", "Lickpussy_Kitty",
            "Trigger == 'vibrator pussy'", "VibratorPussy_Kitty",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy_Kitty",
            "Trigger == 'vibrator anal'", "VibratorAnal_Kitty",
            "Trigger == 'vibrator anal insert'", "VibratorPussy_Kitty",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus is not KittyX", Null(),
#            "Trigger == 'fondle breasts' and not KittyX.Offhand", "GropeRightBreast_Kitty",  #"Trigger == 'fondle breasts' and not KittyX.Offhand",
            #When doing nothing offhand, use both hands on breasts.
            "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast_Kitty",
            #When sucking right breast, fondle left
            "Trigger2 == 'fondle breasts'", "GropeLeftBreast_Kitty",
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast_Kitty",
            #When sucking right breast, vibrator left
            "Trigger2 == Trigger", Null(),
            #When both triggers are the same, do nothing
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast_Kitty",
            "Trigger2 == 'suck breasts'", "LickLeftBreast_Kitty",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy_Kitty",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy_Kitty",
            "Trigger2 == 'vibrator anal'", "VibratorAnal_Kitty",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy_Kitty",
            "Trigger2 == 'fondle pussy'", "GropePussy_Kitty",
            "Trigger2 == 'lick pussy'", "Lickpussy_Kitty",
            "Trigger2 == 'fondle thighs'", "GropeThigh_Kitty",
            "True", Null(),
            ),
        )
    anchor (0.5, 0.0)
    zoom .74   #.76
    offset (30,0)
#    pos (500,100) #fix remove diagnostic


image Kitty_Head:
    LiveComposite(
        (416,610),
#        (0,0), ConditionSwitch(
#            "KittyX.Water", Recolor("Kitty", "Hair", "images/KittySprite/Kitty_Sprite_Hair_Wet_Back.png"),
#            "KittyX.Hair == 'long'", Recolor("Kitty", "Hair", "images/KittySprite/Kitty_Sprite_Hair_Long_Back.png"),
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Base head
            "KittyX.Water and KittyX.Blush == 1", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Head_Wet_Blush1.png",
            "KittyX.Water and KittyX.Blush == 2", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Head_Wet_Blush2.png",
            "KittyX.Water", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Head_Wet_Base.png",
            "KittyX.Blush == 1", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Head_Evo_Blush1.png",
            "KittyX.Blush == 2", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Head_Evo_Blush2.png",
            "True", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Head_Evo_Base.png",
            ),
        (0,0), ConditionSwitch(
            #Brows
            "KittyX.Brows == 'normal'", "images/KittySprite/Kitty_Sprite_Brows_Normal.png",
            "KittyX.Brows == 'angry'", "images/KittySprite/Kitty_Sprite_Brows_Angry.png",
            "KittyX.Brows == 'sad'", "images/KittySprite/Kitty_Sprite_Brows_Sad.png",
            "KittyX.Brows == 'surprised'", "images/KittySprite/Kitty_Sprite_Brows_Surprised.png",
            "KittyX.Brows == 'confused'", "images/KittySprite/Kitty_Sprite_Brows_Confused.png",
            "True", "images/KittySprite/Kitty_Sprite_Brows_Normal.png",
            ),
        (0,0), ConditionSwitch(
            #Mouth
            "KittyX.Mouth == 'normal'", Recolor("Kitty", "Lips", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Mouth_Normal.png"),
            "KittyX.Mouth == 'lipbite'", Recolor("Kitty", "Lips", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Mouth_Lipbite.png"),
            "KittyX.Mouth == 'kiss'", Recolor("Kitty", "Lips", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Mouth_Kiss.png"),
            "KittyX.Mouth == 'sad'", Recolor("Kitty", "Lips", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Mouth_Sad.png"),
            "KittyX.Mouth == 'smile'", Recolor("Kitty", "Lips", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Mouth_Smile.png"),
            "KittyX.Mouth == 'surprised' or KittyX.Mouth == 'open'", Recolor("Kitty", "Lips", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Mouth_Surprised.png"),
            "KittyX.Mouth == 'tongue'", Recolor("Kitty", "Lips", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Mouth_Tongue.png"),
            "KittyX.Mouth == 'sucking'", Recolor("Kitty", "Lips", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Mouth_Tongue.png"), #fix add
            "True", Recolor("Kitty", "Lips", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Mouth_Normal.png"),
            ),
        (0,0), ConditionSwitch(
            #wet face
            "Player.Male", Null(),
            "('mouth' in KittyX.Spunk or 'chin' in KittyX.Spunk) and KittyX.Mouth == 'tongue'", "images/KittySprite/Kitty_Sprite_Wet_Tongue2.png",
            "'mouth' in KittyX.Spunk and KittyX.Mouth == 'tongue'", "images/KittySprite/Kitty_Sprite_Wet_Tongue.png",
            "'chin' in KittyX.Spunk", "images/KittySprite/Kitty_Sprite_Wet_Mouth.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #chin Spunk
            "'chin' not in KittyX.Spunk or not Player.Male", Null(),
            "True", "images/KittySprite/Kitty_Sprite_Spunk_Chin.png",
            ),
        (0,0), ConditionSwitch(
            #Mouth Spunk
            "'mouth' not in KittyX.Spunk or not Player.Male", Null(),
            "KittyX.Mouth == 'normal'", "images/KittySprite/Kitty_Sprite_Spunk_Normal.png",
            "KittyX.Mouth == 'lipbite'", "images/KittySprite/Kitty_Sprite_Spunk_Normal.png",
            "KittyX.Mouth == 'kiss'", "images/KittySprite/Kitty_Sprite_Spunk_Kiss.png",
            "KittyX.Mouth == 'sad'", "images/KittySprite/Kitty_Sprite_Spunk_Sad.png",
            "KittyX.Mouth == 'smile'", "images/KittySprite/Kitty_Sprite_Spunk_Smile.png",
            "KittyX.Mouth == 'surprised' or KittyX.Mouth == 'open'", "images/KittySprite/Kitty_Sprite_Spunk_Surprised.png",
            "KittyX.Mouth == 'tongue'", "images/KittySprite/Kitty_Sprite_Spunk_Tongue.png",
            "KittyX.Mouth == 'sucking'", "images/KittySprite/Kitty_Sprite_Spunk_Sucking.png", #fix add
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Facial
            "'facial' in KittyX.Spunk and Player.Male", "images/KittySprite/Kitty_Sprite_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), "Kitty Blink",
        (0,0), ConditionSwitch(
            #Hair
            "KittyX.Water or KittyX.Hair == 'wet'", Recolor("Kitty", "Hair", "images/KittySprite/Kitty_Sprite_Hair_Wet.png"),
            "not Player.Male and ('hair' in KittyX.Spunk or 'facial' in KittyX.Spunk)",Recolor("Kitty", "Hair", "images/KittySprite/Kitty_Sprite_Hair_Wet.png"),
            "KittyX.Hair == 'evo'", Recolor("Kitty", "Hair", "images/KittySprite/Kitty_Sprite_Hair_Evo.png"),
            "KittyX.Hair == 'long'", Recolor("Kitty", "Hair", "images/KittySprite/Kitty_Sprite_Hair_Long.png"),
            "True", Recolor("Kitty", "Hair", "images/KittySprite/Kitty_Sprite_Hair_Evo.png"),
            ),
        (0,0), ConditionSwitch(
            #hair water
            "KittyX.Water", "images/KittySprite/Kitty_Sprite_Wet_Head.png",
            "not Player.Male and 'facial' in KittyX.Spunk","images/KittySprite/Kitty_Sprite_Wet_Head.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hair spunk
            "KittyX.Hair == 'evo' and 'hair' in KittyX.Spunk and Player.Male", "images/KittySprite/Kitty_Sprite_Spunk_Evohair.png",
            "KittyX.Hair == 'long' and 'hair' in KittyX.Spunk and Player.Male", "images/KittySprite/Kitty_Sprite_Spunk_Evohair.png",
#            "KittyX.Hair == 'evo' and 'hair' in KittyX.Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Evohair.png",
            "True", Null(),
            ),
        # Modification mode
        (0,0), ConditionSwitch(
            "KittyX.Mask == 'mask harem'", "images/KittySprite/modification/Kitty_sprite_mask_harem.png",
            "True", Null(),
        ),
        # -----------------
        )
#    anchor (0.6, 0.0)
    zoom .5

image Kitty_HairBack:
    LiveComposite(
        (416,610),
        (0,0), ConditionSwitch(
            "KittyX.Water or KittyX.Hair == 'wet'", Recolor("Kitty", "Hair", "images/KittySprite/Kitty_Sprite_Hair_Wet_Back.png"),
            "not Player.Male and 'facial' in KittyX.Spunk",Recolor("Kitty", "Hair", "images/KittySprite/Kitty_Sprite_Hair_Wet_Back.png"),
            "KittyX.Hair == 'long'", Recolor("Kitty", "Hair", "images/KittySprite/Kitty_Sprite_Hair_Long_Back.png"),
            "True", Null(),
            ),
        )
#    anchor (0.6, 0.0)
    zoom .5

image Kitty Blink:
    ConditionSwitch(
    "KittyX.Eyes == 'sexy'", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Eyes_Sexy.png",
    "KittyX.Eyes == 'side'", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Eyes_Side.png",
    "KittyX.Eyes == 'surprised'", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Eyes_Surprised.png",
    "KittyX.Eyes == 'manic'", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Eyes_Surprised.png",
    "KittyX.Eyes == 'normal'", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Eyes_Normal.png",
    "KittyX.Eyes == 'down'", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Eyes_Down.png",
    "KittyX.Eyes == 'stunned'", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Eyes_Down.png",
    "KittyX.Eyes == 'squint'", "Kitty_Squint",
    "KittyX.Eyes == 'leftside'", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Eyes_SideLeft.png",
    "KittyX.Eyes == 'closed'", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Eyes_Closed.png",
    "True", "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Eyes_Normal.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    # This randomizes the time between blinking.
    "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Eyes_Closed.png"
    .25
    repeat

image Kitty_Squint:
    "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Eyes_Sexy.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/KittySprite/[KittyX.skin_image.skin_path]Kitty_Sprite_Eyes_Squint.png"
    .25
    repeat


image Kitty_Drip_Mask:
    #This is the mask for her drip pattern
    contains:
        "images/KittySprite/Kitty_Sprite_WetMask.png"
        offset (-225,-560)

image Kitty_Drip_MaskP:
    #This is the mask for her drip pattern in panties down mode
    contains:
        "images/KittySprite/Kitty_Sprite_WetMaskP.png"
        offset (-225,-560)

# End Kitty Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Kitty Doggy Compositing ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#image Kitty_Doggy_Base = LiveComposite(
image Kitty_Doggy_Animation: #nee Kitty_Doggy
    LiveComposite(
        #Base body
        (420,750),
        (0,0), ConditionSwitch(
            #Shows different upper body motion depending on events
            "not Player.Sprite", "Kitty_Doggy_Body",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Kitty_Doggy_Fuck2_Top",
                    "Speed > 1", "Kitty_Doggy_Fuck_Top",
                    "Speed", "Kitty_Doggy_Anal_Head_Top",
                    "True", "Kitty_Doggy_Body",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Kitty_Doggy_Fuck2_Top",
                    "Speed > 1", "Kitty_Doggy_Fuck_Top",
                    "True", "Kitty_Doggy_Body",
                    ),
            "True", "Kitty_Doggy_Body",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events
            "not Player.Sprite", "Kitty_Doggy_Ass",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Kitty_Doggy_Fuck2_Ass",
                    "Speed > 1", "Kitty_Doggy_Fuck_Ass",
                    "Speed", "Kitty_Doggy_Anal_Head_Ass",
                    "True", "Kitty_Doggy_Ass",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Kitty_Doggy_Fuck2_Ass",
                    "Speed > 1", "Kitty_Doggy_Fuck_Ass",
                    "True", "Kitty_Doggy_Ass",
                    ),
            "True", "Kitty_Doggy_Ass",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events
            "Player.Sprite and Player.Cock == 'foot'", ConditionSwitch(
                    "Speed > 1", "Kitty_Doggy_Feet2",
                    "Speed", "Kitty_Doggy_Feet1",
                    "True", "Kitty_Doggy_Feet0",
                    ),
            "ShowFeet", "Kitty_Doggy_Shins0",
            "True", Null(),
            ),
        )
    align (0.6,0.0)
#    yoffset 0
# End Base / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Kitty_Doggy_Body:
    LiveComposite(
        #Upper body
        (420,750),
#        (165,0),"Kitty_Doggy_Hair_Under", #back of the hair
#        (10,115), "Kitty_Doggy_Head",               #Head(0,105)
        (10,115), ConditionSwitch(
            #Head
            "KittyX.Facing", "Kitty_Doggy_Head_Fore",
            "True", "Kitty_Doggy_Head",
            ),
        #(0,0), "images/JeanDoggy/Jean_Doggy_Breast.png", #Body base
#        (0,0), "images/KittyDoggy/Kitty_Doggy_HeadRef.png", # reference head
        (0,0), "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Body.png", #Body base
        (0,0), ConditionSwitch(
            #bra
            "not KittyX.Chest", Null(),
            "KittyX.Uptop", ConditionSwitch(
                    "KittyX.Over and KittyX.Over != 'towel' and KittyX.Over != 'jacket'", Null(),
                    "KittyX.Chest == 'dress' and KittyX.Over and KittyX.Over != 'towel'", Recolor("Kitty", "Chest", "images/KittyDoggy/Kitty_Doggy_Bra_Dress_UpC.png"),
                    "KittyX.Chest == 'dress'", Recolor("Kitty", "Chest", "images/KittyDoggy/Kitty_Doggy_Bra_Dress_Up.png"),
                    "KittyX.Chest == 'cami'", Recolor("Kitty", "Chest", "images/KittyDoggy/Kitty_Doggy_Bra_Cami_Up.png"),
                    "KittyX.Chest == 'lace bra'", Recolor("Kitty", "Chest", "images/KittyDoggy/Kitty_Doggy_Bra_Lace.png"),
                    "KittyX.Chest == 'sports bra'", Recolor("Kitty", "Chest", "images/KittyDoggy/Kitty_Doggy_Bra_Sports_Up.png"),
                    "KittyX.Chest == 'bikini top'", Recolor("Kitty", "Chest", "images/KittyDoggy/Kitty_Doggy_Bra_Bikini_Up.png"),
                    "True", Recolor("Kitty", "Chest", "images/KittyDoggy/Kitty_Doggy_Bra.png"),
                    ),
            "KittyX.Chest == 'dress'", Recolor("Kitty", "Chest", "images/KittyDoggy/Kitty_Doggy_Bra_Dress.png"),
            "KittyX.Chest == 'cami'", Recolor("Kitty", "Chest", "images/KittyDoggy/Kitty_Doggy_Bra_Cami.png"),
            "KittyX.Chest == 'lace bra'", Recolor("Kitty", "Chest", "images/KittyDoggy/Kitty_Doggy_Bra_Lace.png"),
            "KittyX.Chest == 'sports bra'", Recolor("Kitty", "Chest", "images/KittyDoggy/Kitty_Doggy_Bra_Sports.png"),
            "KittyX.Chest == 'bikini top'", Recolor("Kitty", "Chest", "images/KittyDoggy/Kitty_Doggy_Bra_Bikini.png"),
            "True", Recolor("Kitty", "Chest", "images/KittyDoggy/Kitty_Doggy_Bra.png"),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "KittyX.Water", "images/KittyDoggy/Kitty_Doggy_Body_Wet.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Overshirt
            "not KittyX.Over", Null(),
            "KittyX.Over == 'jacket'", Recolor("Kitty", "Over", "images/KittyDoggy/Kitty_Doggy_Over_Jacket.png"),
            "KittyX.Over == 'red shirt'", Recolor("Kitty", "Over", "images/KittyDoggy/Kitty_Doggy_Over_Red.png"),
            "KittyX.Over == 'pink top'", Recolor("Kitty", "Over", "images/KittyDoggy/Kitty_Doggy_Over_Pink.png"),
            "KittyX.Over == 'towel' and not KittyX.Uptop", Recolor("Kitty", "Over", "images/KittyDoggy/Kitty_Doggy_Over_Towel.png"),
            # Modification mode
            "KittyX.Over == 'nighty'and KittyX.Uptop", "images/KittyDoggy/modification/Kitty_doggy_over_nighty_top_up.png",
            "KittyX.Over == 'top harem'", "images/KittyDoggy/modification/Kitty_doggy_over_harem_top.png",
            # -----------------
            "True", Null(),
            ),
        # Modification mode
        (0,0), ConditionSwitch(
            #neck
            "KittyX.Neck == 'nighty collar'", "images/KittyDoggy/modification/Kitty_doggy_neck_nighty_collar.png",
            "True", Null(),
            ),
        # ----------------
        (0,0), ConditionSwitch(
            #spunk back Layer
            "'back' in KittyX.Spunk and Player.Male", "images/KittyDoggy/Kitty_Doggy_Spunk_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast fondling animation
            "Trigger == 'fondle breasts' or Trigger2 == 'fondle breasts'", "Kitty_Doggy_GropeBreast",
            "True", Null()
            ),
        (10,115), ConditionSwitch(
            #Head
            "KittyX.Facing", "Kitty_Doggy_Hair_Fore",
            "True", Null(),
            ),
        #(161,-1), "Jean_Doggy_Head",               #Head
#        (165,0),"Jean_Doggy_Hair_Over", #front of the hair
        )
#    transform_anchor True
#    anchor (225,1400)
    offset (-30,0)#(-190,-40)
    zoom 0.95
#    rotate 20
# End Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Kitty_Doggy_Head:
    LiveComposite(
        #Head
        (420,750),
        #(0,0), "images/JeanDoggy/Jean_Doggy_Head.png", #Body base
        #(0,0), "images/JeanDoggy/Jean_Doggy_TestArm.png",#Eyes
        (0,0), ConditionSwitch(
            #Head
#            "KittyX.Blush > 1", "images/KittyDoggy/Kitty_Doggy_Head_Blush2.png",
            "KittyX.Blush", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Head_Blush.png",
            "True", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Head.png",
            ),
        (0,0), ConditionSwitch(
            #Mouth
            "KittyX.Mouth == 'normal'", Recolor("Kitty", "Lips", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Mouth_Normal.png"),
            "KittyX.Mouth == 'lipbite'", Recolor("Kitty", "Lips", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Mouth_Smile.png"),
            "KittyX.Mouth == 'sucking'", Recolor("Kitty", "Lips", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Mouth_Tongue.png"),
            "KittyX.Mouth == 'kiss'", Recolor("Kitty", "Lips", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Mouth_Kiss.png"),
            "KittyX.Mouth == 'sad'", Recolor("Kitty", "Lips", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Mouth_Sad.png"),
            "KittyX.Mouth == 'smile'", Recolor("Kitty", "Lips", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Mouth_Smile.png"),
            "KittyX.Mouth == 'grimace'", Recolor("Kitty", "Lips", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Mouth_Smile.png"),
            "KittyX.Mouth == 'surprised'", Recolor("Kitty", "Lips", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Mouth_Kiss.png"),
            "KittyX.Mouth == 'tongue'", Recolor("Kitty", "Lips", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Mouth_Tongue.png"),
            "True", Recolor("Kitty", "Lips", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Mouth_Normal.png"),
            ),
#        (0,0), ConditionSwitch(
#            #chin spunk
#            "'chin' in KittyX.Spunk", "images/JeanDoggy/Jean_Doggy_Spunk_Chin.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Mouth spunk
            "'mouth' not in KittyX.Spunk or Player.Male", Null(),
            #"KittyX.Mouth == 'normal'", "images/KittyDoggy/Kitty_Doggy_Spunk_Normal.png",
            #"KittyX.Mouth == 'sad'", "images/KittyDoggy/Kitty_Doggy_Spunk_Normal.png",
            "KittyX.Mouth == 'lipbite'", "images/KittyDoggy/Kitty_Doggy_Spunk_Smile.png",
            "KittyX.Mouth == 'smile'", "images/KittyDoggy/Kitty_Doggy_Spunk_Smile.png",
            "KittyX.Mouth == 'grimace'", "images/KittyDoggy/Kitty_Doggy_Spunk_Smile.png",
            "KittyX.Mouth == 'sucking'", "images/KittyDoggy/Kitty_Doggy_Spunk_Tongue.png",
            #"KittyX.Mouth == 'kiss'", "images/KittyDoggy/Kitty_Doggy_Spunk_Open.png",
#            "KittyX.Mouth == 'surprised'", "images/KittyDoggy/Kitty_Doggy_Spunk_Normal.png",
            "KittyX.Mouth == 'tongue'", "images/KittyDoggy/Kitty_Doggy_Spunk_Tongue.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Spunk_Normal.png",
            ),
        (0,0), ConditionSwitch(
            #Brows
            #"KittyX.Brows == 'normal'", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Brows_Normal.png",
            "KittyX.Brows == 'angry'", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Brows_Angry.png",
            "KittyX.Brows == 'sad'", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Brows_Sad.png",
            "KittyX.Brows == 'surprised'", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Brows_Surprised.png",
            #"KittyX.Brows == 'confused'", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Brows_Normal.png",
            "True", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Brows_Normal.png",
            ),
        (0,0), "Kitty Doggy Blink",#Eyes
#        (0,0), ConditionSwitch(
#            #wet hair strand
#            "KittyX.Water or KittyX.Hair == 'wet'", "images/JeanDoggy/Jean_Doggy_Hair_Wet_Under.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #face spunk
            "'facial' in KittyX.Spunk and Player.Male", "images/KittyDoggy/Kitty_Doggy_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hair
            "KittyX.Water or KittyX.Hair == 'wet'", Recolor("Kitty", "Hair", "images/KittyDoggy/Kitty_Doggy_Hair_Wet.png"),
            "not Player.Male and 'facial' in KittyX.Spunk",Recolor("Kitty", "Hair", "images/KittyDoggy/Kitty_Doggy_Hair_Wet.png"),
            "KittyX.Hair == 'long'", Recolor("Kitty", "Hair", "images/KittyDoggy/Kitty_Doggy_Hair_Long.png"),
            "True", Recolor("Kitty", "Hair", "images/KittyDoggy/Kitty_Doggy_Hair_Evo.png"),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "KittyX.Water", "images/KittyDoggy/Kitty_Doggy_Head_Wet.png",
            "not Player.Male and 'facial' in KittyX.Spunk","images/KittyDoggy/Kitty_Doggy_Head_Wet.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #face spunk
            "'hair' in KittyX.Spunk and Player.Male", "images/KittyDoggy/Kitty_Doggy_Spunk_Hair.png",
            "True", Null(),
            ),
        # Modification mode
        (0,0), ConditionSwitch(
            "KittyX.Mask == 'mask harem'", "images/KittyDoggy/modification/Kitty_doggy_headband_harem_mask.png",
            "True", Null(),
        )
        # -----------------
        )
    zoom 0.75 #.8
    #alpha 0.9
# End Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Kitty_Doggy_Head_Fore:
    LiveComposite(
        #Head
        (420,750),
        (0,0), ConditionSwitch(
            #Hair
            "KittyX.Water or KittyX.Hair == 'wet'", Recolor("Kitty", "Hair", "images/KittyDoggy/Kitty_Doggy_Hair_Wet_Fore_Under.png"),
            "not Player.Male and 'facial' in KittyX.Spunk",Recolor("Kitty", "Hair", "images/KittyDoggy/Kitty_Doggy_Hair_Wet_Fore_Under.png"),
            "KittyX.Hair == 'long'", Recolor("Kitty", "Hair", "images/KittyDoggy/Kitty_Doggy_Hair_Long_Fore_Under.png"),
            "True", Recolor("Kitty", "Hair", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Hair_Evo_Fore_Under.png"),
            ),
        )
    zoom 0.75 #.8
    #alpha 0.9
# End Head Fore / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Kitty_Doggy_Hair_Fore:
    LiveComposite(
        #Head
        (420,750),
        (0,0), ConditionSwitch(
            #Hair
            "KittyX.Water or KittyX.Hair == 'wet'", Recolor("Kitty", "Hair", "images/KittyDoggy/Kitty_Doggy_Hair_Wet_Fore_Over.png"),
            "not Player.Male and 'facial' in KittyX.Spunk",Recolor("Kitty", "Hair", "images/KittyDoggy/Kitty_Doggy_Hair_Wet_Fore_Over.png"),
            "KittyX.Hair == 'long'", Recolor("Kitty", "Hair", "images/KittyDoggy/Kitty_Doggy_Hair_Long_Fore_Over.png"),
            "True", Recolor("Kitty", "Hair", "images/KittyDoggy/Kitty_Doggy_Hair_Evo_Fore_Over.png"),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "KittyX.Water", "images/KittyDoggy/Kitty_Doggy_Head_Wet.png",
            "not Player.Male and 'facial' in KittyX.Spunk","images/KittyDoggy/Kitty_Doggy_Head_Wet.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #face spunk
            "'hair' in KittyX.Spunk and Player.Male", "images/KittyDoggy/Kitty_Doggy_Spunk_Hair.png",
            "True", Null(),
            ),
        )
    zoom 0.75 #.8
    #alpha 0.9
# End Head Fore / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Kitty Doggy Blink:
        #Eyes
        ConditionSwitch(
        "KittyX.Eyes == 'sexy'", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Eyes_Sexy.png",
        "KittyX.Eyes == 'side'", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Eyes_Side.png",
#        "KittyX.Eyes == 'normal'", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Eyes_Normal.png",
        "KittyX.Eyes == 'closed'", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Eyes_Closed.png",
#        "KittyX.Eyes == 'manic'", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Eyes_Normal.png",
        "KittyX.Eyes == 'down'", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Eyes_Down.png",
        "KittyX.Eyes == 'stunned'", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Eyes_Stunned.png",
#        "KittyX.Eyes == 'surprised'", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Eyes_Normal.png",
        "KittyX.Eyes == 'squint'", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Eyes_Sexy.png",
        "True", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Eyes_Normal.png",
        ),
    #    choice:
    #        3.5
    #    choice:
    #        3.25
    #    choice:
    #        3
        3
        # This randomizes the time between blinking.
        "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Eyes_Closed.png"
        .25
        repeat

image Kitty_Doggy_Ass:
    LiveComposite(
        #Lower body
        (420,750),
        (0,0), ConditionSwitch(
            #Legs backside
            "not KittyX.Upskirt", Null(),
            "KittyX.Legs == 'dress'", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Dress_Back.png"),
            "KittyX.Legs == 'shorts' and KittyX.Wet", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts_BackW.png"),
            "KittyX.Legs == 'shorts'", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts_Back.png"),
            "KittyX.Legs == 'yoga pants'", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga_Back.png"),
            # Modification mode
            "KittyX.Legs == 'bottom harem'", "images/KittyDoggy/modification/Kitty_doggy_skirt_harem_back.png",
            # -----------------
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Panties back
            "not KittyX.PantiesDown or (KittyX.Legs and KittyX.Legs != 'blue skirt' and not KittyX.Upskirt)", Null(),
            "KittyX.Panties == 'green panties' and KittyX.Wet", Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Green_BackW.png"),
            "KittyX.Panties == 'green panties'", Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Green_Back.png"),
            "KittyX.Panties == 'bikini bottoms' and KittyX.Wet",Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Bikini_BackW.png"),
            "KittyX.Panties == 'bikini bottoms'",Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Bikini_Back.png"),
            "KittyX.Panties == 'lace panties'",Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Lace_Back.png"),
            "True", Null(),
            ),
#        (0,0), "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Ass.png", #Ass Base


        (0,0), ConditionSwitch(
            #Pussy base
            "Trigger == 'lick pussy'", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Ass_Open.png",
            "KittyX.Legs and not KittyX.Upskirt", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Ass_Closed.png",
            "KittyX.Panties and not KittyX.PantiesDown", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Ass_Closed.png",
            "Player.Sprite and Player.Cock == 'in'", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Ass_Fucking.png",
            "'dildo pussy' in (Trigger,Trigger2,KittyX.Offhand)", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Ass_Fucking.png",
            "'fondle pussy' in (Trigger,Trigger2,KittyX.Offhand)", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Ass_Fucking.png",
            "Trigger == 'insert pussy'", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Ass_Fucking.png",
            "True", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Ass_Closed.png",
            ),

        (0,0), ConditionSwitch(
            #Anus Composite
            "Player.Sprite and Player.Cock == 'anal'", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Anal_FullBase.png",
            "'insert ass' in (Trigger,Trigger2,KittyX.Offhand)", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Anal_FullBase.png",
            "'dildo anal' in (Trigger,Trigger2,KittyX.Offhand)", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Anal_FullBase.png",
            "KittyX.Loose > 2", "Jean_Gape_Anal",
            "KittyX.Loose", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
            "True", "images/JeanDoggy/Jean_Doggy_Asshole_Tight.png",
            ),

        (0,0), ConditionSwitch(
            #ass red
            "KittyX.Red", "images/KittyDoggy/Kitty_Doggy_Red.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Wet look
            "KittyX.Water", "images/KittyDoggy/Kitty_Doggy_Ass_Wet.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #Hose
            "KittyX.Hose == 'stockings'", Recolor("Kitty", "Hose", "images/KittyDoggy/Kitty_Doggy_Hose_Stockings.png"),
            "KittyX.Hose == 'garterbelt'", Recolor("Kitty", "Hose", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png"),
            "KittyX.Hose == 'stockings and garterbelt'", Recolor("Kitty", "Hose", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png"),
#            "KittyX.Panties and KittyX.PantiesDown", Null(),
#            "(KittyX.Legs and KittyX.Legs != 'blue skirt') and not KittyX.Upskirt", Null(),
#            "KittyX.Hose == 'pantyhose'", Recolor("Kitty", "Hose", "images/KittyDoggy/Kitty_Doggy_Hose_Pantyhose.png"),
#            "KittyX.Hose == 'ripped pantyhose'", Recolor("Kitty", "Hose", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Panties if Down
            "not KittyX.PantiesDown or (KittyX.Legs and KittyX.Legs != 'blue skirt' and not KittyX.Upskirt)", Null(),
            "KittyX.Panties == 'green panties' and KittyX.Wet", Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Green_DownW.png"),
            "KittyX.Panties == 'green panties'", Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Green_Down.png"),
            "KittyX.Panties == 'bikini bottoms' and KittyX.Wet", Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Bikini_DownW.png"),
            "KittyX.Panties == 'bikini bottoms'", Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Bikini_Down.png"),
            "KittyX.Panties == 'lace panties'",Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Lace_Down.png"),
            # Modification mode
            "KittyX.Panties == 'nighty panties'", "images/KittyDoggy/modification/Kitty_doggy_panties_nighty_down.png",
            # -----------------
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs Layer if down
            "KittyX.Hose and KittyX.Hose != 'garterbelt'", Null(),
            "KittyX.Legs == 'capris' and KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Blue_Down.png"),
            "KittyX.Legs == 'black jeans' and KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Black_Down.png"),
            "KittyX.Legs == 'yoga pants' and KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga_Down.png"),
            "KittyX.Legs == 'shorts' and KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts_Down.png"),
            # Modification mode
            "KittyX.Legs == 'bottom harem' and KittyX.Upskirt", "images/KittyDoggy/modification/Kitty_doggy_skirt_harem_up.png",
            # -----------------
            "True", Null(),
            ),


        (0,0), ConditionSwitch(
            #spunkpussy Layer
            "'in' in KittyX.Spunk and Player.Cock == 'in' and Player.Male",Null(),# "images/JeanDoggy/Jean_Doggy_SpunkPussyOpen.png",  #fix for KittyX.Spunk is used later
            "'in' in KittyX.Spunk and Player.Male ", "images/JeanDoggy/Jean_Doggy_SpunkPussyClosed.png",
            "KittyX.Wet and Player.Cock == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "KittyX.Wet", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pubes
            "not KittyX.Pubes", Null(),
            "Player.Sprite and Player.Cock == 'in'", Null(), # Recolor("Kitty", "Pubes", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Pubes_Fucked.png"),
            "'dildo pussy' in (Trigger,Trigger2,KittyX.Offhand)", Null(),
            "'fondle pussy' in (Trigger,Trigger2,KittyX.Offhand)", Null(),
            "Trigger == 'insert pussy'", Null(),
            "(KittyX.Legs and KittyX.Legs != 'blue skirt') and not KittyX.Upskirt", Null(),
            "KittyX.PantiesDown and Trigger == 'lick pussy'", Recolor("Kitty", "Pubes", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Pubes_Open.png"),
            "KittyX.Panties and KittyX.PantiesDown", Recolor("Kitty", "Pubes", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Pubes.png"),
            "KittyX.Panties", Recolor("Kitty", "Pubes", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_PubesC.png"),
            "KittyX.Hose == 'pantyhose' and Trigger == 'lick pussy'", Recolor("Kitty", "Pubes", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Pubes_OpenC.png"),
            "KittyX.Hose == 'pantyhose'", Recolor("Kitty", "Pubes", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_PubesC.png"),
            "Trigger == 'lick pussy'", Recolor("Kitty", "Pubes", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Pubes_Open.png"),
            "True", Recolor("Kitty", "Pubes", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Pubes.png"),
            ),
        (0,0), ConditionSwitch(
            #Pussy Piercings
            "Player.Sprite", Null(),
            "'dildo pussy' in (Trigger,Trigger2,KittyX.Offhand)", Null(),
            "'fondle pussy' in (Trigger,Trigger2,KittyX.Offhand)",Null(),
            "Trigger == 'insert pussy'", Null(),
            "KittyX.Pierce == 'barbell'", "images/KittyDoggy/Kitty_Doggy_Pierce_Barbell.png",
            "KittyX.Pierce == 'ring' and KittyX.Panties and not KittyX.PantiesDown", "images/KittyDoggy/Kitty_Doggy_Pierce_RingC.png",
            "KittyX.Pierce == 'ring' and KittyX.Hose == 'pantyhose' and not (KittyX.Panties and KittyX.PantiesDown)", "images/KittyDoggy/Kitty_Doggy_Pierce_RingC.png",
            "KittyX.Pierce == 'ring' and KittyX.Legs and KittyX.Legs != 'blue skirt' and not KittyX.Upskirt", "images/KittyDoggy/Kitty_Doggy_Pierce_RingC.png",
            "KittyX.Pierce == 'ring'", "images/KittyDoggy/Kitty_Doggy_Pierce_Ring.png",
            "True", Null(),
            ),

        (2,-8), ConditionSwitch(
            #spunkanal Layer
            "'anal' not in KittyX.Spunk or Player.Sprite or not Player.Male", Null(),
            "Player.Cock == 'anal'", "images/RogueDoggy/Rogue_Doggy_SpunkAnalOpen.png",
            "KittyX.Loose", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png",
            "True", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png",
            ),
        (0,0), ConditionSwitch(
            #Panties if up
            "KittyX.PantiesDown or not KittyX.Panties", Null(),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),
            "KittyX.Panties == 'green panties' and KittyX.Wet", Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_GreenW.png"),
            "KittyX.Panties == 'green panties'", Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Green.png"),
            "KittyX.Panties == 'lace panties'", Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Lace.png"),
            "KittyX.Panties == 'bikini bottoms' and KittyX.Wet", Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_BikiniW.png"),
            "KittyX.Panties == 'bikini bottoms'", Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Bikini.png"),
            # Modification mode
            "KittyX.Panties == 'nighty panties'", "images/KittyDoggy/modification/Kitty_doggy_panties_nighty.png",
            # -----------------
            "True", Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Green.png"),
            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #full hose/tights
#            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),
#            "KittyX.Panties and KittyX.PantiesDown and KittyX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "KittyX.Panties and KittyX.PantiesDown", Null(),
#            "(KittyX.Legs or KittyX.Legs == 'blue skirt') or not KittyX.Upskirt", Null(),   #maybe?
            "KittyX.Hose == 'pantyhose'", Recolor("Kitty", "Hose", "images/KittyDoggy/Kitty_Doggy_Hose_Pantyhose.png"),
            "KittyX.Hose == 'ripped pantyhose'", Recolor("Kitty", "Hose", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Legs Layer
            "KittyX.Legs == 'dress'", ConditionSwitch(
                    "KittyX.Upskirt and Player.Sprite and Player.Cock == 'anal' and Speed" , Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Dress_Up.png"),
                    "KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Dress_Up.png"),
                    "True", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Dress.png"),
                    ),
            "KittyX.Legs == 'blue skirt'", ConditionSwitch(
                    "KittyX.Upskirt and Player.Sprite and Player.Cock == 'anal' and Speed" , Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_BlueSkirt_Up.png"),   #Rogue_Doggy_Legs_Skirt_UpAnal.png",
                    "KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_BlueSkirt_Up.png"),
                    "True", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_BlueSkirt.png"),
                    ),

            "KittyX.Upskirt", Null(),
            "KittyX.Legs == 'capris'", ConditionSwitch(
#                    "KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Blue_Down.png"),
                    "KittyX.Wet > 1", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_BlueW.png"),
                    "True", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Blue.png"),
                    ),
            "KittyX.Legs == 'black jeans'", ConditionSwitch(
#                    "KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Black_Down.png"),
                    "KittyX.Wet > 1", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_BlackW.png"),
                    "True", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Black.png"),
                    ),
            "KittyX.Legs == 'yoga pants'", ConditionSwitch(
#                    "KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga_Down.png"),
                    "KittyX.Wet > 1", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_YogaW.png"),
                    "True", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga.png"),
                    ),
            "KittyX.Legs == 'shorts'", ConditionSwitch(
#                    "KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts_Down.png"),
                    "KittyX.Wet > 1", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_ShortsW.png"),
                    "True", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts.png"),
                    ),
#            "KittyX.Legs == 'skirt'", ConditionSwitch(
#                    "KittyX.Upskirt and Player.Sprite and Player.Cock == 'anal' and Speed" , "images/KittyDoggy/Kitty_Doggy_Legs_Skirt_Up.png",   #Rogue_Doggy_Legs_Skirt_UpAnal.png",
#                    "KittyX.Upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Skirt_Up.png",
#                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_Skirt.png",
#                    ),
            # Modification mode
            "KittyX.Legs == 'bottom harem'", "images/KittyDoggy/modification/Kitty_doggy_skirt_harem.png",
            # ----------------
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over Layer
            "KittyX.Legs == 'blue skirt' and KittyX.Upskirt", Null(),
            "KittyX.Legs == 'dress' and KittyX.Upskirt", Null(),
            "KittyX.Over == 'pink top'", Recolor("Kitty", "Over", "images/KittyDoggy/Kitty_Doggy_Over_Pink_Tail.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over Layer
            "KittyX.Legs == 'dress' and KittyX.Upskirt", Null(),
            "KittyX.Over == 'towel' and KittyX.Uptop", Null(),
            "KittyX.Over == 'towel' and KittyX.Upskirt", Recolor("Kitty", "Over", "images/KittyDoggy/Kitty_Doggy_Legs_Towel_Up.png"),
            "KittyX.Over == 'towel'", Recolor("Kitty", "Over", "images/KittyDoggy/Kitty_Doggy_Legs_Towel.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Pussy Composite
            "KittyX.Legs and not KittyX.Upskirt",Null(),
            "KittyX.Panties and not KittyX.PantiesDown", Null(),
            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Kitty_Pussy_Fucking3",#Speed 3
                    "Speed > 1", "Kitty_Pussy_Fucking2",#Speed 2
                    "Speed", "Kitty_Pussy_Heading",      #Speed 1
                    "True", "Kitty_Pussy_Static",              #Speed 0
                    ),
            "'dildo pussy' in (Trigger,Trigger2,KittyX.Offhand)", "Kitty_Pussy_Fucking2",
            "'fondle pussy' in (Trigger,Trigger2,KittyX.Offhand)", "Kitty_Pussy_Fingering",
            "Trigger == 'insert pussy'", "Kitty_Pussy_Fingering",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Anus Composite
            "KittyX.Legs and not KittyX.Upskirt",Null(),
            "KittyX.Panties and not KittyX.PantiesDown", Null(),
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Kitty_Anal_Fucking2", #Speed 3
                    "Speed > 1", "Kitty_Anal_Fucking",  #Speed 2
                    "Speed", "Kitty_Anal_Heading",      #Speed 1
                    "True", "Kitty_Anal",               #Speed 0
                    ),
            "'insert ass' in (Trigger,Trigger2,KittyX.Offhand)", "Kitty_Anal_Fingering",
            "'dildo anal' in (Trigger,Trigger2,KittyX.Offhand)", "Kitty_Anal_Fucking",
            "KittyX.Plug", "images/PlugIn.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk back Layer
            "'back' in KittyX.Spunk and Player.Male", "images/KittyDoggy/Kitty_Doggy_Spunk_Ass.png",
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


image Kitty_Doggy_Feet:         #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
    contains:
            AlphaMask("Kitty_Doggy_Shins", "images/KittyDoggy/Kitty_Doggy_Feet_Mask.png")

image Kitty_Doggy_Shins:             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
    #Kitty's footjob shins
#    contains:
#            "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Feet_Legs.png"
    contains:
            #hose legs
        ConditionSwitch(
            "KittyX.Hose == 'ripped pantyhose'", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Feet_Legs_Hole.png",
            "KittyX.Hose and KittyX.Hose != 'garterbelt'", Recolor("Kitty", "Hose", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Hose.png"),
            "True", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Feet_Legs.png"
            )
    contains:
        #pants
        ConditionSwitch(
            "KittyX.Legs == 'capris'", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Blue.png"),
            "KittyX.Legs == 'black jeans'", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Black.png"),
            "KittyX.Legs == 'yoga pants'", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Yoga.png"),
            "True", Null(),
            )
#    contains:
#        "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Feet.png"
    contains:
            #hose toes
        ConditionSwitch(
            "not Player.Sprite or Player.Cock == 'foot'", ConditionSwitch(
                    "KittyX.Hose == 'ripped pantyhose'", Recolor("Kitty", "Hose", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Feet_Hose_HoleF.png"),
                    "KittyX.Hose and KittyX.Hose != 'garterbelt'", Recolor("Kitty", "Hose", "images/KittyDoggy/Kitty_Doggy_Feet_HoseF.png"),
                    "True", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_FeetF.png"  #If you're doing the footjob
                    ),
            "KittyX.Hose == 'ripped pantyhose'", Recolor("Kitty", "Hose", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Feet_Hose_Hole.png"),
            "KittyX.Hose and KittyX.Hose != 'garterbelt'", Recolor("Kitty", "Hose", "images/KittyDoggy/Kitty_Doggy_Feet_Hose.png"),
            "True", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Feet.png"
            )
    contains:
        #spunk
        ConditionSwitch(
            "'feet' in KittyX.Spunk", "images/KittyDoggy/Kitty_Doggy_Spunk_Feet.png",
            "True", Null(),
            )
#    pos (0,0)

image Kitty_Doggy_Shins_Ghost:
        "Kitty_Doggy_Shins"
        alpha 0.5

image Kitty_Doggy_Shins0:
    #static animation
#    contains:
    "Kitty_Doggy_Shins"
    pos (0, 15) #(0,0) top

image Kitty_Doggy_GropeBreast:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        xzoom -.55
        yzoom .55
        offset (110,420)#(150,340)
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
        block:
            ease 1 rotate 10#60
            ease 1 rotate 0#90
            repeat

image Kitty_Gape_Anal:
        #animation for her asshole growing and shrinking a bit when over 2 Looseness
        contains:
            subpixel True
            "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Anal_GapeBase.png"
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

image Zero_Kitty_Hotdog_Static:
    # The unmoving version of the hotdog cock
    # called in Doggy Ass LC
    contains:
        "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Kitty_Hotdog_Moving:
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

image Kitty_Pussy_Mask:
    #AlphaMask used to prevent the cock from moving past the pussy
    #Called in "Jean_Pussy_Moving"
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

image Kitty_Pussy_Mask_Static:
    #AlphaMask used to prevent the cock from moving past the pussy in static pose
    #Called in "Jean_Pussy_Moving"
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


image Kitty_Pussy_Static:
    #Full Animation for speed 0
    subpixel True
    contains:
        #moving hole
        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
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
            "KittyX.Pubes", Recolor("Kitty", "Pubes", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Pubes_Heading.png"),
            "True", Null(),
            )
        subpixel True
        anchor (0.51,0.69)
        pos (213,518) #(213,518)
        xzoom .75
        block:
            ease 1 xzoom .9
            pause 1
            ease 3 xzoom .77
            repeat
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "KittyX.Pierce == 'barbell'", "images/KittyDoggy/Kitty_Doggy_Pierce_Barbell.png",
            "KittyX.Pierce == 'ring'", "images/KittyDoggy/Kitty_Doggy_Pierce_Ring.png",
            "True", Null(),
            )
        offset (-1,6)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in KittyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
        subpixel True
        anchor (0.52,0.69)
        pos (218,516) #(221,516)
        xzoom .7
        block:
            ease 1 xzoom .9
            pause 1
            ease 3 xzoom .7
            repeat

    contains:
        #Cock
        AlphaMask("Zero_Kitty_Doggy_Static", "Kitty_Pussy_Mask_Static")
    contains:
        # expanding pussy flap
        AlphaMask("Kitty_PussyHole_Static", "Kitty_Pussy_Hole_Mask_Static")


image Zero_Kitty_Doggy_Static:
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

image Kitty_Pussy_Hole_Mask_Static:
    # This is the alpha used for the little flap in the heading animation "Kitty_Pussy_Moving"
    contains:
        #Base
        AlphaMask("images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat

image Kitty_PussyHole_Static:
    #This is the image impacted by the mask for the pussy flap in "Jean_Pussy_Moving"
    contains:
        #Mask
        "images/JeanDoggy/Jean_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 512
            pause 1
            ease 3 ypos 515
            repeat


image Kitty_Pussy_Heading:
    #Full Animation for speed 1
    subpixel True
    contains:
        #moving hole
        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.515,0.69)#(0.51,0.69)
#        anchor (0.53,0.69)
        pos (215,518) #(213,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat

    contains:
        #pubes
        ConditionSwitch(
            "KittyX.Pubes", Recolor("Kitty", "Pubes", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Pubes_Heading.png"),
            "True", Null(),
            )
        subpixel True
        anchor (0.51,0.69)
        pos (213,518) #(213,518)
        xzoom .95#.75
        block:
            ease 1 xzoom 1.2
            pause 1
            ease 3 xzoom .95
            repeat
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "KittyX.Pierce == 'barbell'", "images/KittyDoggy/Kitty_Doggy_Pierce_Barbell.png",
            "KittyX.Pierce == 'ring'", "images/KittyDoggy/Kitty_Doggy_Pierce_Ring.png",
            "True", Null(),
            )
        offset (-1,6)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in KittyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
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
        AlphaMask("Zero_Kitty_Doggy_Heading", "Kitty_Pussy_Mask")

    contains:
        # expanding pussy flap
        AlphaMask("Kitty_Pussy_Heading_Flap", "Kitty_Pussy_Hole_Mask")
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in KittyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
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

image Zero_Kitty_Doggy_Heading:
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

image Kitty_Pussy_Hole_Mask:
    # This is the alpha used for the little flap in the heading animation "Jean_Pussy_Heading"
    contains:
        #Base
        AlphaMask("images/JeanDoggy/Jean_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat

image Kitty_Pussy_Heading_Flap:
    #This is the image impacted by the mask for the pussy flap in "Jean_Pussy_Heading"
    contains:
        #Mask
        "images/JeanDoggy/Jean_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 505
            pause 1
            ease 3 ypos 515
            repeat


image Kitty_Pussy_Fingering:
    #Full Animation for speed 1
    subpixel True
    contains:
        #moving hole
        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
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
            "KittyX.Pubes", Recolor("Kitty", "Pubes", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Pubes_Fucked.png"),
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
            "KittyX.Pierce == 'barbell'", "images/KittyDoggy/Kitty_Doggy_Pierce_Barbell.png",
            "KittyX.Pierce == 'ring'", "images/KittyDoggy/Kitty_Doggy_Pierce_Ring.png",
            "True", Null(),
            )
        offset (-3,8)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in KittyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
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
        AlphaMask("Zero_Pussy_Finger", "Rogue_Pussy_Mask")
    contains:
        # expanding pussy flap
        AlphaMask("Kitty_Pussy_Heading_Flap", "Kitty_Pussy_Hole_Mask")
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in KittyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
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



# > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

image Kitty_Pussy_Fucking2:
    #Full Animation for speed 2
    contains:
        #Base
        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
    contains:
        #pubes
        ConditionSwitch(
            "KittyX.Pubes", Recolor("Kitty", "Pubes", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Pubes_Fucked.png"),
            "True", Null(),
            )
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "KittyX.Pierce == 'barbell'", "images/KittyDoggy/Kitty_Doggy_Pierce_Barbell.png",
            "KittyX.Pierce == 'ring'", "images/KittyDoggy/Kitty_Doggy_Pierce_Ring.png",
            "True", Null(),
            )
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in KittyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            "'dildo pussy' in (Trigger,Trigger2,KittyX.Offhand)", AlphaMask("Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "True",AlphaMask("Zero_Kitty_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            )
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in KittyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )


image Zero_Kitty_Doggy_Fucking2:
    # Sex Speed 2 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat


image Kitty_Pussy_Fucking3:
    #Full Animation for speed 3
    contains:
        #Base
        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
    contains:
        #pubes
        ConditionSwitch(
            "KittyX.Pubes", Recolor("Kitty", "Pubes", "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Pubes_Fucked.png"),
            "True", Null(),
            )
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "KittyX.Pierce == 'barbell'", "images/KittyDoggy/Kitty_Doggy_Pierce_Barbell.png",
            "KittyX.Pierce == 'ring'", "images/KittyDoggy/Kitty_Doggy_Pierce_Ring.png",
            "True", Null(),
            )
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in KittyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Kitty_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in KittyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )



image Zero_Kitty_Doggy_Fucking3:
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

image Kitty_Anal:
    #Anal static Loose
    contains:
        #Base
        "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png"
        anchor (0.50,0.69)
        pos (205,515)#(208,500)
        zoom 1.25
        alpha .7
    contains:
        #spunk under cock
        ConditionSwitch(
            "'anal' in KittyX.Spunk and Player.Male", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png",
            "True", Null(),
            )
        yoffset -15
    contains:
        #Cock
        "Zero_Doggy_Insert"
        pos (172,500)

image Kitty_Anal_Fingering:
    #Animation for speed 1
    contains:
        #Hole
        "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Anal_FullHole.png"
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
            "'anal' in KittyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
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
        AlphaMask("Zero_Kitty_Doggy_Anal_Finger", "Kitty_Doggy_Anal_Fingering_Mask")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in KittyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
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

image Zero_Kitty_Doggy_Anal_Finger:
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
image Kitty_Doggy_Anal_Fingering_Mask:
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
image Kitty_Anal_Heading:
    #Animation for speed 1
    contains:
        #Hole
        "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Anal_FullHole.png"
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
            "'anal' in KittyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
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
        AlphaMask("Zero_Kitty_Doggy_Anal_Heading", "Kitty_Doggy_Anal_Heading_Mask")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in KittyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
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

image Zero_Kitty_Doggy_Anal_Heading:
        #the cock anal heading animation
    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500#505
            repeat

image Zero_Kitty_Doggy_Anal_HeadingJunk:
    #this is a mask to correct an annoying glitch in the core mask
    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease .5 ypos 550
            pause .25
            ease 1.75 ypos 600#505
            repeat

image Kitty_Doggy_Anal_Heading_Mask:
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

image Kitty_Doggy_Anal_Head_Top:
#animation for anal fucking top half
    contains:
        subpixel True
        "Kitty_Doggy_Body"
        ypos 0
        block:
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat

image Kitty_Doggy_Anal_Head_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Kitty_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -10
            easeout .1 ypos -7
            easein .9 ypos 0
            pause .9
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Kitty_Doggy_Anal1:
    #Animation for speed 2 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat

image Kitty_Anal_Fucking:
    #Animation for speed 2 Ass
    contains:
        #Hole
        "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Anal_FullHole.png"
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
            "'anal' in KittyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            #full hose/tights
            "'dildo anal' in (Trigger,Trigger2,KittyX.Offhand)", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", AlphaMask("Zero_Kitty_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            ),
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in KittyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )

image Kitty_Doggy_Fuck_Top:
    #animation for anal fucking top half
    contains:
        subpixel True
        "Kitty_Doggy_Body"
        ypos 0#15
        pause .4
        block:
            ease .2 ypos -10#5
            pause .3
            ease 2 ypos 0#15
            repeat

image Kitty_Doggy_Fuck_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Kitty_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15#-25
            ease .1 ypos -5#-15
            pause .2
            ease 1.6 ypos 0
            repeat


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Kitty_Doggy_Anal2:
    #Animation for speed 3 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat

image Kitty_Anal_Fucking2:
    #Animation for speed 3 Ass
    contains:
        #Hole
        "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Anal_FullHole.png"
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
            "'anal' in KittyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Kitty_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in KittyX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )

image Kitty_Doggy_Fuck2_Top:
    #animation for anal fucking2 top half
    contains:
        subpixel True
        "Kitty_Doggy_Body"
        ypos 0#20
        block:
            pause .15
            ease .1 ypos -20#0
            pause .1
            easein .5 ypos 0#20
            pause .05
            repeat

image Kitty_Doggy_Fuck2_Ass:
    #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Kitty_Doggy_Ass"
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

image Kitty_Doggy_Feet0:
    #static animation
    contains:
        "Kitty_Doggy_Shins"
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
        "Kitty_Doggy_Feet"
        pos (0, -20) #(0,0) top
        block:
            subpixel True
            pause .5
            ease 2 ypos 0#20
            pause .5
            ease 2 ypos -20#0
            repeat

image Kitty_Doggy_Feet1:
    #slow animation
    contains:
        "Kitty_Doggy_Shins"
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
        "Kitty_Doggy_Feet"
        pos (0, -20) #(0,0) top
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos -20
            repeat

image Kitty_Doggy_Feet2:
    #fast animation
    contains:
        "Kitty_Doggy_Shins"
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
        "Kitty_Doggy_Feet"
        pos (0, -20) #(0,0) top
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos -20
            repeat
# Footjob animations end > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Doggy Launch/Reset
label Kitty_Doggy_Launch(Line = Trigger):
    if renpy.showing("Kitty_Doggy_Animation"):
        return
    $ Speed = 0
    call Girl_Hide(KittyX,1)
    show Kitty_Doggy_Animation at SpriteLoc(StageCenter+50) zorder 150
    with dissolve
    return

label Kitty_Doggy_Reset:
    if not renpy.showing("Kitty_Doggy_Animation"):
        return
#    $ Trigger = 0               #fix, not sure this is a good idea
    $ KittyX.ArmPose = 2
    $ KittyX.SpriteVer = 0
    hide Kitty_Doggy_Animation
    call Girl_Hide(KittyX)
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
            alpha 1 zoom 1 offset (0,0) anchor (0.6, 0.0)
    with dissolve
    $ Speed = 0
    return

# End Kitty Doggy Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Kitty Sex Sprite ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


image Kitty_SexSprite:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
                #Shows different upper body motion depending on events
                "not Player.Sprite", "Kitty_Sex_Body_Static",
                "Player.Cock == 'anal'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Kitty_Sex_Body_Anim3",
                        "Speed >= 2", "Kitty_Sex_Body_Anim2",
                        "Speed", "Kitty_Sex_Body_Anim1",
                        "True", "Kitty_Sex_Body_Static",
                        ),
                "Player.Cock == 'in'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Kitty_Sex_Body_Anim3",
                        "Speed >= 2", "Kitty_Sex_Body_Anim2",
                        "Speed", "Kitty_Sex_Body_Anim1",
                        "True", "Kitty_Sex_Body_Static",
                        ),
                "Player.Cock == 'foot'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 2", "Kitty_Sex_Body_FootAnim2",
                        "Speed", "Kitty_Sex_Body_FootAnim1",
                        "True", "Kitty_Sex_Body_FootAnimStatic",
                        ),
                "Player.Cock == 'out' and Speed >= 2","Kitty_Hotdog_Body_Anim2",
                "True", "Kitty_Sex_Body_Static",
                ),
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
                "not Player.Sprite", "Kitty_Sex_Legs_Static",
                "Player.Cock == 'anal'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Kitty_Sex_Legs_Anim3",
                        "Speed >= 2", "Kitty_Sex_Legs_Anim2",
                        "Speed", "Kitty_Sex_Legs_Anim1",
                        "True", "Kitty_Sex_Legs_Static",
                        ),
                "Player.Cock == 'in'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Kitty_Sex_Legs_Anim3",
                        "Speed >= 2", "Kitty_Sex_Legs_Anim2",
                        "Speed", "Kitty_Sex_Legs_Anim1",
                        "True", "Kitty_Sex_Legs_Static",
                        ),
                "Player.Cock == 'foot'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 2", "Kitty_Sex_Legs_FootAnim2",
                        "Speed", "Kitty_Sex_Legs_FootAnim1",
                        "True", "Kitty_Sex_Legs_FootAnimStatic",
                        ),
                "Player.Cock == 'out' and Speed >= 2","Kitty_Hotdog_Legs_Anim2",
                "True", "Kitty_Sex_Legs_Static",
                ),
        )
    align (0.6,0.0)
    pos (650,230)#(750,230)
    zoom 0.7

image Kitty_Sex_Body_Static:
    contains:
            "Kitty_Sex_Body"
    pos (650,230)

image Kitty_Sex_Legs_Static:
    contains:
            "Kitty_Sex_Legs"
    pos (650,230)

image Kitty_Sex_Body:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Kitty_SexSprite
        (1120,840),
        (260,-350), "Kitty_HairBack_Sex",
            #Hair underlayer
        (0,0), ConditionSwitch(
            #Body Base
            "KittyX.Pierce == 'barbell'", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Body_Barbell.png",
            "KittyX.Pierce == 'ring'", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Body_Ring.png",
            "True", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Body.png",
            ),
        # Modification mode
        (0,0), ConditionSwitch(
            #neck top harem
            "KittyX.Over == 'top harem'", "images/KittySex/modification/Kitty_sex_over_harem_top_neck.png",
            "True", Null(),
            ),
        # -----------------
        (260,-350), "Kitty_Head_Sex",  #check positioning (400,-300)
        #Eyes
        (0,0), ConditionSwitch(
            #necklace
            "KittyX.Neck == 'gold necklace'", "images/KittySex/Kitty_Sex_Neck_Gold.png",
            "KittyX.Neck == 'star necklace'", "images/KittySex/Kitty_Sex_Neck_Star.png",
            "KittyX.Neck == 'flower necklace'", "images/KittySex/Kitty_Sex_Neck_Flower.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #dress base
            "KittyX.Legs == 'dress'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Legs_Dress_Waist.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #bra layer
            "not KittyX.Chest", Null(),
            "not KittyX.Uptop", ConditionSwitch(
                    #if the top's down. . .
                    "KittyX.Chest == 'dress'", Recolor("Kitty", "Chest", "images/KittySex/Kitty_Sex_Under_Dress.png"),
                    "KittyX.Chest == 'cami'", Recolor("Kitty", "Chest", "images/KittySex/Kitty_Sex_Under_Cami.png"),
                    "KittyX.Chest == 'sports bra'", Recolor("Kitty", "Chest", "images/KittySex/Kitty_Sex_Under_SportsBra.png"),
                    "KittyX.Chest == 'bra'", Recolor("Kitty", "Chest", "images/KittySex/Kitty_Sex_Under_Bra.png"),
                    "KittyX.Chest == 'bikini top'", Recolor("Kitty", "Chest", "images/KittySex/Kitty_Sex_Under_Bikini.png"),
                    "KittyX.Chest == 'lace bra'", Recolor("Kitty", "Chest", "images/KittySex/Kitty_Sex_Under_LaceBra.png"),
                    "True", Null(),
                    ),
            "KittyX.Over", ConditionSwitch(
                    # If she's wearing a shirt over the bra
                    "KittyX.Chest == 'dress'", Recolor("Kitty", "Chest", "images/KittySex/Kitty_Sex_Under_Dress_UpS.png"),
                    "KittyX.Chest == 'cami'", Recolor("Kitty", "Chest", "images/KittySex/Kitty_Sex_Under_Cami_UpS.png"),
                    "KittyX.Chest == 'bikini top'", Recolor("Kitty", "Chest", "images/KittySex/Kitty_Sex_Under_Bikini_Up.png"),
                    "KittyX.Chest == 'sports bra' and KittyX.Over == 'red shirt'", Recolor("Kitty", "Chest", "images/KittySex/Kitty_Sex_Under_SportsBra_UpS.png"),
                    "KittyX.Chest == 'sports bra'", Recolor("Kitty", "Chest", "images/KittySex/Kitty_Sex_Under_SportsBra_Up.png"),
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                    # if she's not wearing a shirt
                    "KittyX.Chest == 'dress'", Recolor("Kitty", "Chest", "images/KittySex/Kitty_Sex_Under_Dress_Up.png"),
                    "KittyX.Chest == 'cami'", Recolor("Kitty", "Chest", "images/KittySex/Kitty_Sex_Under_Cami_Up.png"),
                    "KittyX.Chest == 'sports bra'", Recolor("Kitty", "Chest", "images/KittySex/Kitty_Sex_Under_SportsBra_Up.png"),
                    "KittyX.Chest == 'bra'", Recolor("Kitty", "Chest", "images/KittySex/Kitty_Sex_Under_Bra_Up.png"),
                    "KittyX.Chest == 'bikini top'", Recolor("Kitty", "Chest", "images/KittySex/Kitty_Sex_Under_Bikini_Up.png"),
                    "KittyX.Chest == 'lace bra'", Recolor("Kitty", "Chest", "images/KittySex/Kitty_Sex_Under_LaceBra_Up.png"),
                    "True", Null(),
                    ),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "KittyX.Water", "images/KittySex/Kitty_Sex_Water_Body.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #shirt layer
            "not KittyX.Over", Null(),
            "not KittyX.Uptop", ConditionSwitch(
                    #if the top's down. . .
                    "KittyX.Over == 'jacket'", Recolor("Kitty", "Over", "images/KittySex/Kitty_Sex_Over_Jacket.png"),
                    "KittyX.Over == 'pink top'", Recolor("Kitty", "Over", "images/KittySex/Kitty_Sex_Over_PinkShirt.png"),
                    "KittyX.Over == 'red shirt'", Recolor("Kitty", "Over", "images/KittySex/Kitty_Sex_Over_RedShirt.png"),
                    "KittyX.Over == 'towel'", Recolor("Kitty", "Over", "images/KittySex/Kitty_Sex_Over_Towel.png"),
                    # Modification mode
                    "KittyX.Over == 'nighty'", "images/KittySex/modification/Kitty_sex_over_nighty.png",
                    "KittyX.Over == 'top harem'", "images/KittySex/modification/Kitty_sex_over_harem_top.png",
                    # -----------------
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                    # if she's not wearing a shirt
                    "KittyX.Over == 'jacket'", Recolor("Kitty", "Over", "images/KittySex/Kitty_Sex_Over_Jacket_Up.png"),
                    "KittyX.Over == 'pink top' and KittyX.Chest == 'sports bra'", Recolor("Kitty", "Over", "images/KittySex/Kitty_Sex_Over_PinkShirt_UpS.png"),
                    "KittyX.Over == 'pink top'", Recolor("Kitty", "Over", "images/KittySex/Kitty_Sex_Over_PinkShirt_Up.png"),
                    "KittyX.Over == 'red shirt'", Recolor("Kitty", "Over", "images/KittySex/Kitty_Sex_Over_RedShirt_Up.png"),
#                    "KittyX.Over == 'towel'", Recolor("Kitty", "Over", "images/KittySex/Kitty_Sex_Over_Towel.png"),
                    # Modification mode
                    "KittyX.Over == 'nighty'", "images/KittySex/modification/Kitty_sex_over_nighty.png",
                    "KittyX.Over == 'top harem'", "images/KittySex/modification/Kitty_sex_over_harem_top_up.png",
                    # ----------------
                    "True", Null(),
                    ),
            ),
        (0,0), ConditionSwitch(
            #bra layer over the shirt
            "not KittyX.Chest or not KittyX.Over or not KittyX.Uptop", Null(),
            # if she's not wearing a shirt
            "KittyX.Chest == 'dress'", Recolor("Kitty", "Chest", "images/KittySex/Kitty_Sex_Under_Dress_Up.png"),
            "KittyX.Chest == 'bra'", Recolor("Kitty", "Chest", "images/KittySex/Kitty_Sex_Under_Bra_Up.png"),
            "KittyX.Chest == 'lace bra'", Recolor("Kitty", "Chest", "images/KittySex/Kitty_Sex_Under_LaceBra_UpS.png"),
            "True", Null(),
            ),
        # Modification mode
        (0,0), ConditionSwitch(
            # neck
            "KittyX.Neck == 'nighty collar'", "images/KittySex/modification/Kitty_sex_neck_nighty_collar.png",
            "True", Null(),
        ),
        # -----------------
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'belly' in KittyX.Spunk and Player.Male", "images/KittySex/Kitty_Sex_Spunk_Body.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'tits' in KittyX.Spunk and Player.Male", "images/KittySex/Kitty_Sex_Spunk_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast licking animation
            "Trigger == 'suck breasts' or Trigger2 == 'suck breasts'", "Kitty_Sex_Lick_Breasts",
            "True", Null()
            ),
        (0,0), ConditionSwitch(
            #breast fondling animation
            "Trigger == 'fondle breasts' or Trigger2 == 'fondle breasts'", "Kitty_Sex_Fondle_Breasts",
            "True", Null()
            ),
        )

image Kitty_Sex_Lick_Breasts:
        "Lick_Anim"
        zoom 0.6
        offset (450,210)#270)

image Kitty_Sex_Fondle_Breasts:
        "GropeLeftBreast"
        zoom 1.1
        offset (320,-180)#-130)

image Kitty_Head_Sex:
    # The head used for the sex pose, referenced by Kitty_Sex_Body
    "Kitty_Head"
    zoom 1.5
    anchor (0.5,0.5)
    rotate -10

image Kitty_HairBack_Sex:
    # The hair behind the head for the sex pose, referenced by Kitty_Sex_Body
    "Kitty_HairBack"
    zoom 1.5
    anchor (0.5,0.5)
    rotate -10

#image Kitty_Sex_Legs = LiveComposite(
image Kitty_Sex_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Kitty_SexSprite
        (1120,840),
        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            "KittyX.Legs == 'dress' and KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Legs_Dress_Back_Up.png"),
            "KittyX.Legs == 'dress'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Legs_Dress_Back.png"),
            "KittyX.Legs == 'blue skirt'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Skirt_Back.png"),
            "True", Null(),
            ),
        (0,0), "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Legs.png",                                                         #Legs Base
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "KittyX.Water", "images/KittySex/Kitty_Sex_Water_Legs.png",
            "True", Null(),
            ),

        (0,0), "Kitty_Sex_Anus",                                                                          #Anus Composite

        (0,0), "Kitty_Sex_Pussy",                                                                         #Pussy Composite

        (0,0), ConditionSwitch(                                                                                 #Panties if up
            "KittyX.PantiesDown", Null(),
            "KittyX.Panties == 'green panties' and KittyX.Wet", Recolor("Kitty", "Panties", "images/KittySex/Kitty_Sex_Panties_Green_Wet.png"),
            "KittyX.Panties == 'green panties'", Recolor("Kitty", "Panties", "images/KittySex/Kitty_Sex_Panties_Green.png"),
            "KittyX.Panties == 'lace panties' and KittyX.Wet", Recolor("Kitty", "Panties", "images/KittySex/Kitty_Sex_Panties_Lace_Wet.png"),
            "KittyX.Panties == 'lace panties'", Recolor("Kitty", "Panties", "images/KittySex/Kitty_Sex_Panties_Lace.png"),
            "KittyX.Panties == 'bikini bottoms' and KittyX.Wet", Recolor("Kitty", "Panties", "images/KittySex/Kitty_Sex_Panties_Bikini_Wet.png"),
            "KittyX.Panties == 'bikini bottoms'", Recolor("Kitty", "Panties", "images/KittySex/Kitty_Sex_Panties_Bikini.png"),
            # Modification mode
            "KittyX.Panties == 'nighty panties' and KittyX.Wet", "images/KittySex/modification/Kitty_sex_panties_nighty_wet.png",
            "KittyX.Panties == 'nighty panties'", "images/KittySex/modification/Kitty_sex_panties_nighty.png",
            # -----------------
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #hose layer
            "KittyX.Hose == 'stockings and garterbelt'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_StockingGarter_Legs.png"),
            "KittyX.Hose == 'garterbelt'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_Garter_Legs.png"),
            "KittyX.Hose == 'stockings'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_Stockings_Legs.png"),
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "KittyX.Hose == 'pantyhose'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_Pantyhose_Legs.png"),
#            "KittyX.Hose == 'ripped pantyhose'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_RippedPantyhose_Legs.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            "KittyX.Legs == 'dress' and KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Legs_Dress_Up.png"),
            "KittyX.Legs == 'dress'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Legs_Dress.png"),
            "KittyX.Legs == 'blue skirt'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Skirt.png"),
            "KittyX.Upskirt", Null(),
            "KittyX.Legs == 'capris' and KittyX.Wet > 1", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Pants_Blue_Wet.png"),
            "KittyX.Legs == 'capris'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Pants_Blue.png"),
            "KittyX.Legs == 'black jeans' and KittyX.Wet > 1", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Pants_Black_Wet.png"),
            "KittyX.Legs == 'black jeans'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Pants_Black.png"),
            "KittyX.Legs == 'shorts' and KittyX.Wet > 1", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Shorts_Wet.png"),
            "KittyX.Legs == 'shorts'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Shorts.png"),
            "KittyX.Legs == 'yoga pants' and KittyX.Wet > 1", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Pants_Yoga_Wet.png"),
            "KittyX.Legs == 'yoga pants'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Pants_Yoga.png"),
            # Modification mode
            "KittyX.Legs == 'bottom harem' and KittyX.Upskirt", "images/KittySex/modification/Kitty_sex_skirt_harem_up.png",
            "KittyX.Legs == 'bottom harem'", "images/KittySex/modification/Kitty_sex_skirt_harem.png",
            # ----------------
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #Over Layer
            "KittyX.Over == 'towel' and not KittyX.Uptop", Recolor("Kitty", "Over", "images/KittySex/Kitty_Sex_Towel_Legs.png"),
            "True", Null(),
            ),
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in KittyX.Spunk and Player.Male", "images/KittySex/Kitty_Sex_Spunk_Pelvis.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer
            "not Player.Sprite or Player.Cock != 'out'", Null(),
            "Speed >= 2", "Kitty_Hotdog_Zero_Anim2",
            "Speed", "Kitty_Hotdog_Zero_Anim1",
            "True", "Kitty_Hotdog_Zero_Anim0",
            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite", Null(),
            "Trigger == 'lick pussy'", "Kitty_Sex_Lick_Pussy",
            "Trigger == 'lick ass'", "Kitty_Sex_Lick_Ass",
            "KittyX.Offhand == 'fondle pussy' and KittyX.Lust > 60", At("KittyFingerHand", GirlFingerPussyX()),
            "KittyX.Offhand == 'fondle pussy'", At("KittyMastHand", GirlGropePussyX()),
            "True", Null()
            ),
        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer
            "not Player.Sprite or Player.Cock != 'foot'", Null(),
            "Speed >= 2", "Kitty_Footcock_Zero_Anim2",
            "Speed", "Kitty_Footcock_Zero_Anim1",
            "True", "Kitty_Footcock_Static",
            ),
#        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer
#            "not Player.Sprite or Player.Cock != 'foot'", Null(),
#            "Speed >= 2", At("Kitty_Footcock", Kitty_Footcock_Zero_Anim2A()),
#            "Speed", At("Kitty_Footcock", Kitty_Footcock_Zero_Anim1A()),
#            "True", At("Kitty_Footcock", Kitty_Footcock_StaticA()),
#            ),
#        (0,0), ConditionSwitch(                                                                                 #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "renpy.showing('Anal_Plug_In_Sex') or renpy.showing('Anal_Plug_Out_Sex')", AlphaMask("Kitty_Sex_Feet", "images/KittySex/Kitty_Sex_FeetMask.png"),
            "not Speed", "Kitty_Sex_Feet",
            "Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Kitty_Sex_Feet", "images/KittySex/Kitty_Sex_FeetMask.png"),
            "True", "Kitty_Sex_Feet",
            ),
        )

image Kitty_Sex_Feet:
    LiveComposite(
        #the lower legs used in the sex pose, referenced by Kitty_Sex_Legs
        (1120,840),
        (0,0), "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Feet.png",                                                         #Legs Base
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "KittyX.Water", "images/KittySex/Kitty_Sex_Water_Feet.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #hose layer
            "KittyX.Legs and not KittyX.Upskirt and KittyX.Legs != 'blue skirt' and KittyX.Legs != 'shorts'",ConditionSwitch(
                    #If she has pants on, I need alternate kneesocks to not clip through knees
                    "KittyX.Hose == 'stockings and garterbelt'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png"),
                    "KittyX.Hose == 'stockings'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png"),
                    "KittyX.Hose == 'knee stockings'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png"),
                    "KittyX.Panties and KittyX.PantiesDown", Null(),
                    "KittyX.Hose == 'pantyhose'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png"),
                    "KittyX.Hose == 'ripped pantyhose'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_RippedPantyhose_FeetP.png"),
                    "True", Null(),
                    ),
#            "KittyX.Legs and (not KittyX.Upskirt and KittyX.Legs != 'blue skirt' and KittyX.Legs != 'shorts') and KittyX.Hose == 'stockings and garterbelt'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png"),
#            "KittyX.Legs and (not KittyX.Upskirt and KittyX.Legs != 'blue skirt' and KittyX.Legs != 'blue skirt') and KittyX.Hose == 'stockings'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png"),
#            "KittyX.Legs and (not KittyX.Upskirt and KittyX.Legs != 'blue skirt' and KittyX.Legs != 'blue skirt') and KittyX.Hose == 'knee stockings'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png"),
            "KittyX.Hose == 'stockings' or KittyX.Hose == 'stockings and garterbelt'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_Stockings_Feet.png"),
            "KittyX.Hose == 'knee stockings'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_Kneesocks_Feet.png"),
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "KittyX.Hose == 'pantyhose'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_Stockings_Feet.png"),
#            "KittyX.Legs and (not KittyX.Upskirt and KittyX.Legs != 'blue skirt' and KittyX.Legs != 'blue skirt') and KittyX.Hose == 'ripped pantyhose'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_RippedPantyhose_FeetP.png"),
            "KittyX.Hose == 'ripped pantyhose'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_RippedPantyhose_Feet.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            "KittyX.Upskirt", Null(),
            "KittyX.Legs == 'dress'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Legs_Dress_Feet.png"),
            "KittyX.Legs == 'capris'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Feet_Blue.png"),
            "KittyX.Legs == 'black jeans'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Feet_Black.png"),
            "KittyX.Legs == 'yoga pants'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Feet_Yoga.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk
            "'feet' in KittyX.Spunk", "images/KittySex/Kitty_Sex_Spunk_Feet.png",
            "True", Null(),
            ),
        )

image Kitty_Sex_Lick_Pussy:
        "Lick_Anim"
        zoom 0.7
        offset (530,510)

image Kitty_Sex_Lick_Ass:
        "Lick_Anim"
        zoom 0.7
        offset (535,590)

image GropeBack:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        zoom .7
        pos (300,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block:
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image TestingSolid:
        #this is a blank solid I use to test things.
        contains:
            Solid("#75d7ec", xysize=(1500,1500))
            alpha 0.2

#Start Animations for Kitty's Pussy during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_Sex_Pussy_Fucking0:
    # This is the visual for her pussy during the Speed 0 mode (static).
    contains:
            # The background plate of her pussy
            "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pussy_Open.png"
    contains:
            # pubes
            ConditionSwitch(
                "not KittyX.Pubes", Null(),
                "True", Recolor("Kitty", "Pubes", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pubes_Open.png"),
                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Sex_Zero_Anim0", "Kitty_Pussy_Open_Mask")

image Kitty_Sex_Pussy_Fucking1:
    # This is the visual for her pussy during the Speed 1 mode (heading).
    contains:
            # The background plate of her pussy
            "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pussy_Open.png"
    contains:
            # pubes
            ConditionSwitch(
                "not KittyX.Pubes", Null(),
                "True", Recolor("Kitty", "Pubes", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pubes_Open.png"),
                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Sex_Zero_Anim1", "Kitty_Pussy_Open_Mask")

image Kitty_Sex_Pussy_Fucking2:
    # This is the visual for her pussy during the Speed 2 mode (slow).
    contains:
            # The background plate of her pussy
            "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pussy_Fucking.png"
    contains:
            # pubes
            ConditionSwitch(
                "not KittyX.Pubes", Null(),
                "True", Recolor("Kitty", "Pubes", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pubes_Fucking.png"),
                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Sex_Zero_Anim2", "Kitty_Pussy_Fucking_Mask")
image Kitty_Sex_Pussy_Fucking3:  #rename this to 3
    # This is the visual for her pussy during the Speed 3 mode (fast).
    contains:
            # The background plate of her pussy
            "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pussy_Fucking.png"
    contains:
            # pubes
            ConditionSwitch(
                "not KittyX.Pubes", Null(),
                "True", Recolor("Kitty", "Pubes", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pubes_Fucking.png"),
                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Sex_Zero_Anim3", "Kitty_Pussy_Fucking_Mask")

image Kitty_Pussy_Fucking_Mask:
        #This is the mask image for Kitty's wide open pussy
        contains:
            "images/KittySex/Kitty_Sex_Pussy_Mask.png"

image Kitty_Pussy_Open_Mask:
        #This is the mask image for Kitty's wide open pussy
        contains:
            "images/KittySex/Kitty_Sex_Pussy_Mask.png"
            yoffset 3

#image TestMask:
#        #This involves a working, shrinking and growing mask for the pussy
#        contains:
#            "images/KittySex/Kitty_Sex_Pussy_Mask.png"
#            subpixel True
#            anchor (0.5,0.63)
#            pos (0.5,0.63)
#            zoom 1
#            block:
#                ease 1 zoom .5
#                pause 1
#                ease 3 zoom 1
#                repeat

image Kitty_Pussy_Spunk_Heading:
    "images/KittySex/Kitty_Sex_Spunk_Puss_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8

image Kitty_Sex_Pussy_Hole:
    "images/JubesDoggy/Jubes_Doggy_Pussy_HHole.png"
    transform_anchor True
    anchor (212,580)#(210,600)
    pos (558,580)#(400,-10)
    xzoom 0.8
    parallel:
        ease 1 yzoom 1.2
        pause 1
        ease 3 yzoom 1
        repeat
    parallel:
        ease 1 xzoom 1.2
        pause 2
        ease 2  xzoom 0.8
        repeat

image Kitty_Sex_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pussy_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and Speed", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pussy_Open.png",
                "Player.Sprite and Player.Cock == 'in'", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pussy_Closed.png",
                "Trigger == 'lick pussy'", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pussy_Open.png",
                "KittyX.Offhand == 'fondle pussy' and KittyX.Lust > 60", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pussy_Open.png",
                "True", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pussy_Closed.png",
                )
    contains:
            # growing pussy hole
            ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and Speed == 1", "Kitty_Sex_Pussy_Hole",#"images/RogueSex/Rogue_Sex_Pussy_Open.png",
                "True", Null(),
                )
    contains:
            # wet pussy
            ConditionSwitch(
                "not KittyX.Wet", Null(),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/KittySex/Kitty_Sex_WetPussy_F.png",
                "True", "images/KittySex/Kitty_Sex_WetPussy_C.png",
                )
    contains:
            #ring piercing
            ConditionSwitch(
                "KittyX.Pierce != 'ring'", Null(),
                "not Player.Sprite or Player.Cock != 'in' or Speed <= 1", "images/KittySex/Kitty_Sex_Pussy_Ring.png",
                "True", "images/KittySex/Kitty_Sex_Pussy_RingF.png",
                )
    contains:
            #barbell piercing
            ConditionSwitch(
                "KittyX.Pierce != 'barbell'", Null(),
                "not Player.Sprite or Player.Cock != 'in' or Speed <= 1", "images/KittySex/Kitty_Sex_Pussy_Barbell.png",
                "True", "images/KittySex/Kitty_Sex_Pussy_BarbellF.png",
                )
    contains:
            # pubes
            ConditionSwitch(
                "not KittyX.Pubes", Null(),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", Recolor("Kitty", "Pubes", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pubes_Fucking.png"),
                "Player.Sprite and Player.Cock == 'in' and Speed", Recolor("Kitty", "Pubes", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pubes_Open.png"),
                "Player.Sprite and Player.Cock == 'in'", Recolor("Kitty", "Pubes", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pubes_Closed.png"),
                "Trigger == 'lick pussy'", Recolor("Kitty", "Pubes", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pubes_Open.png"),
                "KittyX.Offhand == 'fondle pussy' and KittyX.Lust > 60", Recolor("Kitty", "Pubes", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pubes_Open.png"),
                "True", Recolor("Kitty", "Pubes", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pubes_Closed.png"),
                )
    contains:
            #Spunk under penis
            ConditionSwitch(
                "'in' in KittyX.Spunk and Player.Male", "images/KittySex/Kitty_Sex_Spunk_Puss_Under.png",
                "True", Null(),
                )
    contains:
            #hose layer
            ConditionSwitch(
                "KittyX.Panties and KittyX.PantiesDown", Null(),
                "KittyX.Hose == 'ripped pantyhose'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_RippedPantyhose_Legs.png"),
                "True", Null(),
                )
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            ConditionSwitch(
                "not Player.Sprite", Null(),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 3", AlphaMask("Kitty_Sex_Zero_Anim3", "Kitty_Pussy_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", AlphaMask("Kitty_Sex_Zero_Anim2", "Kitty_Pussy_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and Speed", AlphaMask("Kitty_Sex_Zero_Anim1", "Kitty_Pussy_Open_Mask"),
                "Player.Sprite and Player.Cock == 'in'", AlphaMask("Kitty_Sex_Zero_Anim0", "Kitty_Pussy_Open_Mask"),
                "True", Null(),
                )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "'in' not in KittyX.Spunk or not Player.Sprite or Player.Cock != 'in' or not Speed or not Player.Male", Null(),
                "Speed <= 1", "Kitty_Pussy_Spunk_Heading",
                "True", "images/KittySex/Kitty_Sex_Spunk_Puss_Over.png",
                )

    #End Kitty Pussy composite

#End Animations for Kitty's Pussy during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Zero's Cock during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_Sex_Zero_Anim0:
        #this is Kitty's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (498,530) #X less is left, Y less is up (498,520)
            zoom 1.4

image Kitty_Sex_Zero_Anim1:
        #this is Kitty's sex animation, Speed 1 (heading)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (498,525) #X less is left, Y less is up(498,520)
            zoom 1.4
            block:
                ease 1 pos (498,510) #(498,500)
                pause 1
                ease 3 pos (498,525)
                repeat

image Kitty_Sex_Zero_Anim2:
        #this is Kitty's sex animation, Speed 2 (slow)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,490) #X less is left, Y less is up
            zoom 1.4
            block:
                ease 1 pos (500,380) #(500,470)
                pause 1
                ease 3 pos (500,490)
                repeat

image Kitty_Sex_Zero_Anim3:
        #this is Kitty's sex animation, Speed 3 (fast)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,490) #X less is left, Y less is up
            zoom 1.4
            block:
                ease .25 pos (500,380) #(500,470)
                pause .25
                ease 1.5 pos (500,490)
                repeat
#End Animations for Zero's Cock during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Kitty's Legs during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_Sex_Legs_Anim1:
        #this is the animation for Kitty's lower body during sex, Speed 1 (heading)
        contains:
            subpixel True
            "Kitty_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .25
                easein 1 pos (0,-5)
                pause 1
                ease 2.75 pos (0,0)
                repeat

image Kitty_Sex_Legs_Anim2:
        #this is the animation for Kitty's lower body during sex, Speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .5 pos (0,-15)
                ease .25 pos (0,-10)
                pause 1
                ease 2.75 pos (0,0)
                repeat

image Kitty_Sex_Legs_Anim3:
        #this is the animation for Kitty's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Kitty_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .15
                easein .15 pos (0,-20)
                ease .10 pos (0,-15)
                pause .20
                ease 1.4 pos (0,0)
                repeat
#End Animations for Kitty's Legs during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Kitty's Body during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_Sex_Body_Anim1:
        #this is the animation for Kitty's upper body during sex, Speed 1 (heading)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 pos (0,-5)
                pause 1.25
                ease 2.5 pos (0,0)
                repeat

image Kitty_Sex_Body_Anim2:
        #this is the animation for Kitty's upper body during sex, Speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .6
                easein .4 pos (0,-10)
                ease .25 pos (0,-5)
                pause 1
                ease 2.75 pos (0,10)
                repeat

image Kitty_Sex_Body_Anim3:
        #this is the animation for Kitty's upper body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .17
                easein .13 pos (0,-20)
                ease .10 pos (0,-15)
                pause .20
                ease 1.4 pos (0,10)
                repeat
#End Animations for Kitty's Body during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





#Start Animations for Kitty's Ass during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Kitty_Sex_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/KittySex/Kitty_Sex_Hole_Open.png",
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/KittySex/Kitty_Sex_Hole_Open.png",
            "Player.Sprite and Player.Cock == 'anal' and Speed", "Kitty_Sex_Anal_Heading",
            "Player.Sprite and Player.Cock == 'anal'", "Kitty_Sex_Anal_Tip",
            "KittyX.Plug", "images/PlugBase_Sex.png",
            "KittyX.Loose > 2", "Kitty_Gape_Anal_Sex",
            "KittyX.Loose", "images/KittySex/Kitty_Sex_Hole_Loose.png",
            "True", "images/KittySex/Kitty_Sex_Hole_Tight.png",
            )
    contains:
            #Spunk under penis
            ConditionSwitch(
                "'anal' not in KittyX.Spunk or Player.Male", Null(),
                "Player.Sprite and Player.Cock != 'anal' and Speed >= 1", "images/KittySex/Kitty_Sex_Spunk_Anal_Under.png",
                "Player.Sprite and Player.Cock != 'anal' and Speed == 1", "Kitty_Sex_Anal_Spunk_Heading_Under",
                "True", "images/KittySex/Kitty_Sex_Spunk_Anal_Closed.png",
                )
    contains:
            # The animation of Zero's moving penis, masked by her anus shape
            ConditionSwitch(
            "not Player.Sprite or Player.Cock != 'anal'", Null(),
            "Speed >= 3",  AlphaMask("Kitty_Anal_Zero_Anim3", "Kitty_Sex_Anal_Fucking_Mask"),
            "Speed >= 2", AlphaMask("Kitty_Anal_Zero_Anim2", "Kitty_Sex_Anal_Fucking_Mask"),
            "Speed", AlphaMask("Kitty_Anal_Zero_Anim1", "Kitty_Sex_Anal_Fucking_Mask"),
            "True", AlphaMask("Kitty_Anal_Zero_Anim0", "Kitty_Sex_Anal_Fucking_Mask"),
            )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "'anal' not in KittyX.Spunk or not Player.Sprite or Player.Cock != 'anal' or not Speed or not Player.Male", Null(),
                "Speed == 1", "Kitty_Sex_Anal_Spunk_Heading_Over",
                "True", "images/KittySex/Kitty_Sex_Spunk_Anal_Over.png",
                )

image Kitty_Gape_Anal_Sex:
        #removing an anal plug
        contains:
            #Hole
            "images/KittySex/Kitty_Sex_Hole_Open.png"
            transform_anchor True
            subpixel True
            anchor (560,620)#(0.52,0.69)
            offset (560,615)#(218,518)
            zoom .40 # tight
            block:
                ease 3 zoom .50 #in.87
                ease 3 zoom .40 #out
                repeat

image Kitty_Sex_Anal_Fucking0:
    # This is the visual for her pussy during the Speed 0 mode (static).
    contains:
            # The background plate of her pussy
            "Kitty_Sex_Anal_Tip"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Anal_Zero_Anim0", "Kitty_Sex_Anal_Fucking_Mask")

image Kitty_Sex_Anal_Fucking1:
    # This is the visual for her pussy during the Speed 1 mode (heading).
    contains:
            # The background plate of her pussy
            "Kitty_Anal_Heading"
#            "images/KittySex/Kitty_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Anal_Zero_Anim1", "Kitty_Sex_Anal_Fucking_Mask")

image Kitty_Sex_Anal_Fucking2:
    # This is the visual for her pussy during the Speed 2 mode (slow).
    contains:
            # The background plate of her pussy
            "images/KittySex/Kitty_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Anal_Zero_Anim2", "Kitty_Sex_Anal_Fucking_Mask")

image Kitty_Sex_Anal_Fucking3:
    # This is the visual for her pussy during the Speed 3 mode (fast).
    contains:
            # The background plate of her pussy
            "images/KittySex/Kitty_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Anal_Zero_Anim3", "Kitty_Sex_Anal_Fucking_Mask")

image Kitty_Sex_Anal_Fucking_Mask:
        #This is the mask image for Kitty's wide open pussy
        contains:
            "images/KittySex/Kitty_Sex_Hole_Mask.png"

image Kitty_Sex_Anal_Open_Mask:
        #This is the mask image for Kitty's wide open pussy
        contains:
            "images/KittySex/Kitty_Sex_Hole_Mask.png"
            yoffset 3

image Kitty_Sex_Anal_Heading:
    "images/KittySex/Kitty_Sex_Hole_Open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
    block:
        #total 5 second
        ease .75 xzoom 1.0
        ease .25 xzoom 0.9
        pause 1.50
        ease .25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

image Kitty_Sex_Anal_Spunk_Heading_Over:
    "images/KittySex/Kitty_Sex_Spunk_Anal_Over.png"
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
image Kitty_Sex_Anal_Spunk_Heading_Under:
    "images/KittySex/Kitty_Sex_Spunk_Anal_Under.png"
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

image Kitty_Sex_Anal_Tip:
    "images/KittySex/Kitty_Sex_Hole_Open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6

#End Animations for Kitty's Pussy during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Zero's Cock during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_Anal_Zero_Anim0:
        #this is Kitty's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,600) #X less is left, Y less is up (498,520)
            zoom 1.4

image Kitty_Anal_Zero_Anim1:
        #this is Kitty's sex animation, Speed 1 (heading)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,600) #X less is left, Y less is up
            zoom 1.4
            block:
                ease 1 pos (500,570) #(500,470)
                pause 1
                ease 3 pos (500,600)
                repeat

image Kitty_Anal_Zero_Anim2:
        #this is Kitty's sex animation, Speed 2 (slow)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,570) #X less is left, Y less is up
            zoom 1.4
            block:
                ease 1 pos (500,450) #(500,470)
                pause 1
                ease 3 pos (500,570)
                repeat

image Kitty_Anal_Zero_Anim3:
        #this is Kitty's sex animation, Speed 3 (fast)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,570) #X less is left, Y less is up
            zoom 1.4
            block:
                ease .25 pos (500,450) #(500,470)
                pause .25
                ease 1.5 pos (500,570)
                repeat
#End Animations for Zero's Cock during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Zero's Cock during Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_Hotdog_Zero_Anim0:
        #this is Kitty's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (498,570) #X less is left, Y less is up
            zoom 1.4

image Kitty_Hotdog_Zero_Anim1:
        #this is Kitty's sex animation, Speed 1 (heading)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (498,500) #X less is left, Y less is up
            zoom 1.4
            block:
                ease 1 pos (498,560) #(500,500)
                pause .5
                ease 1.5 pos (498,500)
                repeat

image Kitty_Hotdog_Zero_Anim2:
        #this is Kitty's sex animation, Speed 3 (fast)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,510) #X less is left, Y less is up
            zoom 1.4
            block:
                ease .5 pos (500,400) #(500,470)
                pause .5
                ease 1 pos (500,510)
                repeat

image Kitty_Hotdog_Body_Anim2:
        #this is the animation for Kitty's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .30
                ease .50 pos (0,-10)
                pause .20
                ease 1 pos (0,0)
                repeat

image Kitty_Hotdog_Legs_Anim2:
        #this is the animation for Kitty's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Kitty_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .20
                ease .50 pos (0,-10)
                pause .20
                ease 1.1 pos (0,0)
                repeat

#End Animations for Zero's Cock during Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Kitty's Legs during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Kitty_Footcock:
    contains:
            subpixel True
#            "Blowcock"
            ConditionSwitch(
                "AlphaCock", "Blowcock",
                "True", "Ghostcock",
                )
            zoom 0.7
            anchor (0.5,0.5)
            offset (465,70)
            pos (0,0)
    pos (750,230)

image Kitty_Footcock_Static:
    contains:
            subpixel True
            "Kitty_Footcock"
            pos (392,295)
    pos (750,230)

image Kitty_Footcock_Zero_Anim1:
    contains:
            subpixel True
            "Kitty_Footcock"
            pos (392,295)
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 ypos 360#65
                ease .25 ypos 355#60
                pause 1
                ease 2.50 ypos 270#285
                repeat
    pos (750,230)

image Kitty_Footcock_Zero_Anim2:
    contains:
            subpixel True
            "Kitty_Footcock"
            pos (392,295)
            block:
                #Total time, 4 seconds
                pause .2
                easein .4 ypos 360
                ease .2 ypos 355
                pause .2
                ease 1.00 ypos 270
                repeat
    pos (750,230)

transform Kitty_Footcock_Zero_Anim1A():
            subpixel True
            offset (0,0)
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 yoffset 60#65
                ease .25 yoffset 55#60
                pause 1
                ease 1.50 yoffset -30#285
                repeat

transform Kitty_Footcock_Zero_Anim2A():
            subpixel True
            offset (0,0)
            block:
                #Total time, 2 seconds
                pause .2
                easein .4 yoffset 60
                ease .2 yoffset 55
                pause .2
                ease 1.00 yoffset -30
                pause .2
                easein .4 yoffset 60
                ease .2 yoffset 55
                pause .2
                ease 1.00 yoffset -30
                repeat

transform Kitty_Footcock_StaticA():
            subpixel True
            offset (0,-5)
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset 0
                pause 1
                ease 1.50 yoffset -5
                repeat

image Kitty_Sex_Legs_FootAnim1:
        #this is the animation for Kitty's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (0,-65)
                ease .25 pos (0,-60)
                pause 1
                ease 2.50 pos (0,25)#(0,10)
                repeat
        pos (750,230)

image Kitty_Sex_Legs_FootAnim2:
        #this is the animation for Kitty's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .2
                easein .4 pos (0,-65)
                ease .2 pos (0,-60)
                pause .2
                ease 1.0 pos (0,25)#(0,10)
                repeat
        pos (750,230)

image Kitty_Sex_Legs_FootAnimStatic:
        #this is the animation for Kitty's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
        pos (750,230)

transform Kitty_Sex_Legs_FootAnim1A():
        #this is the animation for Kitty's lower body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 yoffset -65
                ease .25 yoffset -60
                pause 1
                ease 1.50 yoffset 25
                repeat

transform Kitty_Sex_Legs_FootAnim2A():
        #this is the animation for Kitty's lower body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .2
                easein .4 yoffset -65
                ease .2 yoffset -60
                pause .2
                ease 1.0 yoffset 25
                pause .2
                easein .4 yoffset -65
                ease .2 yoffset -60
                pause .2
                ease 1.0 yoffset 25
                repeat

transform Kitty_Sex_Legs_FootAnimStaticA():
        #this is the animation for Kitty's lower body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset -5
                pause 1
                ease 1.50 yoffset 0
                repeat

#End Animations for Kitty's Legs during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Kitty's Body during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Kitty_Sex_Body_FootAnim1:
        #this is the animation for Kitty's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 pos (0,-25)#(0,-5)
                ease .25 pos (0,-15)#(0,0)
                pause 1
                ease 2.50 pos (0,15)#(0,5)
                repeat
        pos (750,230)

image Kitty_Sex_Body_FootAnim2:
        #this is the animation for Kitty's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .2
                easein .4 pos (0,-25)#(0,-5)
                ease .2 pos (0,-15)#(0,0)
                pause .2
                ease 1.0 pos (0,15)#(0,5)
                repeat
        pos (750,230)

image Kitty_Sex_Body_FootAnimStatic:
        #this is the animation for Kitty's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            pos (0,0) #X less is left, Y less is up
        pos (750,230)

transform Kitty_Sex_Body_FootAnim1A():
        #this is the animation for Kitty's upper body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 yoffset -25
                ease .25 yoffset -15
                pause 1
                ease 1.50 yoffset 15
                repeat

transform Kitty_Sex_Body_FootAnim2A():
        #this is the animation for Kitty's upper body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .2
                easein .4 yoffset -25
                ease .2 yoffset -15
                pause .2
                ease 1.0 yoffset 15
                pause .2
                easein .4 yoffset -25
                ease .2 yoffset -15
                pause .2
                ease 1.0 yoffset 15
                repeat

transform Kitty_Sex_Body_FootAnimStaticA():
        #this is the animation for Kitty's upper body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset -5
                pause 1
                ease 1.50 yoffset 0
                repeat
#End Animations for Kitty's Body during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     Sex Launch/Reset
label Kitty_Sex_Launch(Line = Trigger):
    $ KittyX.Offhand = 0 if KittyX.Offhand == "hand" else KittyX.Offhand

#    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    $ KittyX.Pose = 0
#    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary

    $ Line = "solo" if not Line else Line
    if Line == "sex":
        $ Player.Sprite = 1
        $ Player.Cock = "in"
        call Cock_Occupied(KittyX,"pussy")
        if Trigger2 in ("fondle pussy","dildo pussy","lick pussy"):
                $ Trigger2 = 0
    elif Line == "anal":
        $ Player.Sprite = 1
        $ Player.Cock = "anal"
        call Cock_Occupied(KittyX,"anal")
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
        call Zero_Strapped(KittyX) #puts strap-on on.
    $ Trigger = Line

    if KittyX.Pose == "doggy":
            call Kitty_Doggy_Launch(Line)
            return
    if renpy.showing("Kitty_SexSprite"):
        return
    $ Speed = 0
    call Girl_Hide(KittyX,1)
    show Kitty_SexSprite zorder 150
#    show Kitty_SexSprite zorder 150:
#        pos (750,230)

    with dissolve
    return

label Kitty_Sex_Reset:
    if renpy.showing("Kitty_Doggy_Animation"):
        call Kitty_Doggy_Reset
        return
    if not renpy.showing("Kitty_SexSprite"):
        return
    $ KittyX.ArmPose = 2
    hide Kitty_SexSprite
    call Girl_Hide(KittyX)
#    call Set_The_Scene(Dress = 0)
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
        alpha 1 zoom 1 offset (0,0) anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return

# End Kitty Sex pose Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Kitty Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Kitty BJ element ///////////////////////////////////////////////////////////////////////////                                     Core Kitty BJ element
#Kitty BJ Over Sprite Compositing


image Kitty_BJ_Animation:#                                                                #core BJ animation
    LiveComposite(
        (858,928),
        (0,0), ConditionSwitch(
            "Speed == 1", "Kitty_BJ_Anim1",               #Licking
            "Speed == 2", "Kitty_BJ_Anim2",               #Heading
            "Speed == 3", "Kitty_BJ_Anim3",               #Sucking
            "Speed == 4", "Kitty_BJ_Anim4",               #Deepthroat
            "Speed == 5", "Kitty_BJ_Anim5",               #Cumming High
            "Speed == 6", "Kitty_BJ_Anim6",               #Cumming Deep
            "Speed == 0", "Kitty_BJ_Anim0",               #Static
            ),
        )
    zoom .55
    transform_anchor True
    anchor (.5,.5)
    offset (300,0)

image Kitty_BJ_HairBack:
    #Hair underlay
    ConditionSwitch(
            "KittyX.Water and KittyX.Hair == 'evo'", Recolor("Kitty", "Hair", "images/KittyBJFace/Kitty_BJ_HairBackWet.png"),
            "not Player.Male and 'facial' in KittyX.Spunk",Recolor("Kitty", "Hair", "images/KittyBJFace/Kitty_BJ_HairBackWet.png"),
            "KittyX.Hair == 'long'", Recolor("Kitty", "Hair", "images/KittyBJFace/Kitty_BJ_HairBackWet.png"),
            "True", Null(),
            ),
    zoom 1.4
    anchor (0.5, 0.5)
    yoffset 50

image Kitty_BJ_Backdrop:
    #Her Body under the head
    LiveComposite(
        (858,928),
        (-375,350), ConditionSwitch(      #(-375,250)
            #blanket
            "'blanket' in KittyX.RecentActions", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
            "True", Null(),
            ),
        (120,-150),"Kitty_BJ_Ass",
        (0,0), ConditionSwitch(
            #red shirt under
            "KittyX.Over == 'red shirt'", "images/KittyBJFace/Kitty_BJ_Over_RedUnder.png",
#            "KittyX.Chest == 'dress'", "images/KittyBJFace/Kitty_BJ_Over_RedUnder.png",
            "True", Null(),
            ),
        (0,0),"images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Body.png",
            #body
        (0,0), ConditionSwitch(
            #necklace
            "KittyX.Neck == 'gold necklace'", "images/KittyBJFace/Kitty_BJ_Neck_Gold.png",
            "KittyX.Neck == 'star necklace'", "images/KittyBJFace/Kitty_BJ_Neck_Star.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # piercings
            "not KittyX.Pierce", Null(),
            "(KittyX.Over or KittyX.Chest) and not KittyX.Uptop", Null(),
            "KittyX.Pierce == 'ring'", "images/KittyBJFace/Kitty_BJ_PierceRing.png",
            "True", "images/KittyBJFace/Kitty_BJ_PierceBall.png",
            ),
        (0,0), ConditionSwitch(
            # wet body
            "not KittyX.Water", Null(),
            "True", "images/KittyBJFace/Kitty_BJ_Wet_Body.png",
            ),

        (0,0), ConditionSwitch(
            #Bra
            "KittyX.Uptop", Null(),
            "KittyX.Chest == 'lace bra'", Recolor("Kitty", "Chest", "images/KittyBJFace/Kitty_BJ_Bra_Lace.png"),
            "KittyX.Chest == 'sports bra'", Recolor("Kitty", "Chest", "images/KittyBJFace/Kitty_BJ_Bra_Sport.png"),
            "KittyX.Chest == 'bikini top'", Recolor("Kitty", "Chest", "images/KittyBJFace/Kitty_BJ_Bra_Bikini.png"),
            "KittyX.Chest == 'bra'", Recolor("Kitty", "Chest", "images/KittyBJFace/Kitty_BJ_Bra.png"),
            "KittyX.Chest == 'cami'", Recolor("Kitty", "Chest", "images/KittyBJFace/Kitty_BJ_Bra_Cami.png"),
            "KittyX.Chest == 'dress'", Recolor("Kitty", "Chest", "images/KittyBJFace/Kitty_BJ_Bra_Dress.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Shirt
            "KittyX.Uptop", Null(),
            "KittyX.Over == 'pink top'", Recolor("Kitty", "Over", "images/KittyBJFace/Kitty_BJ_Over_PinkShirt.png"),
            "KittyX.Over == 'red shirt'", Recolor("Kitty", "Over", "images/KittyBJFace/Kitty_BJ_Over_RedShirt.png"),
            "KittyX.Over == 'jacket'", Recolor("Kitty", "Over", "images/KittyBJFace/Kitty_BJ_Over_Jacket.png"),
            "KittyX.Over == 'towel'", Recolor("Kitty", "Over", "images/KittyBJFace/Kitty_BJ_Over_Towel.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Spunk
            "'tits' not in KittyX.Spunk or not Player.Male", Null(),
            "True", "images/KittyBJFace/Kitty_BJ_Spunk_Body.png",
            ),
        )
    zoom 1.5
    offset (-650,-750)
#end image Kitty_BJ_Backdrop:

image Kitty_BJ_Ass:
    LiveComposite(
        #Lower body
        (420,750),
        (0,0), ConditionSwitch(
            #Legs backside
            "not KittyX.Upskirt", Null(),
            "KittyX.Legs == 'dress'", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Dress_Back.png"),
#            "KittyX.Legs == 'shorts' and KittyX.Wet", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts_BackW.png"),
#            "KittyX.Legs == 'shorts'", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts_Back.png"),
#            "KittyX.Legs == 'yoga pants'", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga_Back.png"),
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Panties back
#            "not KittyX.PantiesDown or (KittyX.Legs and KittyX.Legs != 'blue skirt' and not KittyX.Upskirt)", Null(),
#            "KittyX.Panties == 'green panties' and KittyX.Wet", Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Green_BackW.png"),
#            "KittyX.Panties == 'green panties'", Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Green_Back.png"),
#            "KittyX.Panties == 'bikini bottoms' and KittyX.Wet",Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Bikini_BackW.png"),
#            "KittyX.Panties == 'bikini bottoms'",Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Bikini_Back.png"),
#            "KittyX.Panties == 'lace panties'",Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Lace_Back.png"),
#            "True", Null(),
#            ),
        (0,0),  "images/KittyDoggy/[KittyX.skin_image.skin_path]Kitty_Doggy_Ass_Closed.png",

        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #Hose
            "KittyX.Hose == 'stockings'", Recolor("Kitty", "Hose", "images/KittyDoggy/Kitty_Doggy_Hose_Stockings.png"),
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "(KittyX.Legs and KittyX.Legs != 'blue skirt') and not KittyX.Upskirt", Null(),
            "KittyX.Hose == 'pantyhose'", Recolor("Kitty", "Hose", "images/KittyDoggy/Kitty_Doggy_Hose_Pantyhose.png"),
            "KittyX.Hose == 'ripped pantyhose'", Recolor("Kitty", "Hose", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png"),
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #Panties if Down
#            "not KittyX.PantiesDown or (KittyX.Legs and KittyX.Legs != 'blue skirt' and not KittyX.Upskirt)", Null(),
#            "KittyX.Panties == 'green panties' and KittyX.Wet", Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Green_DownW.png"),
#            "KittyX.Panties == 'green panties'", Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Green_Down.png"),
#            "KittyX.Panties == 'bikini bottoms' and KittyX.Wet", Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Bikini_DownW.png"),
#            "KittyX.Panties == 'bikini bottoms'", Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Bikini_Down.png"),
#            "KittyX.Panties == 'lace panties'",Recolor("Kitty", "Panties", "images/KittyDoggy/Kitty_Doggy_Panties_Lace_Down.png"),
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #Legs Layer if down
#            "KittyX.Hose and KittyX.Hose != 'garterbelt'", Null(),
#            "KittyX.Legs == 'capris' and KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Blue_Down.png"),
#            "KittyX.Legs == 'black jeans' and KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Black_Down.png"),
#            "KittyX.Legs == 'yoga pants' and KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga_Down.png"),
#            "KittyX.Legs == 'shorts' and KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts_Down.png"),
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #full hose/tights
#            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),
#            "KittyX.Panties and KittyX.PantiesDown and KittyX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "KittyX.Hose == 'garterbelt'", Recolor("Kitty", "Hose", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png"),
            "KittyX.Hose == 'stockings and garterbelt'", Recolor("Kitty", "Hose", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png"),
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "(KittyX.Legs or KittyX.Legs == 'blue skirt') or not KittyX.Upskirt", Null(),   #maybe?
            "KittyX.Hose == 'pantyhose'", Recolor("Kitty", "Hose", "images/KittyDoggy/Kitty_Doggy_Hose_Pantyhose.png"),
            "KittyX.Hose == 'ripped pantyhose'", Recolor("Kitty", "Hose", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Legs Layer
            "KittyX.Legs == 'dress'", ConditionSwitch(
                    "KittyX.Upskirt and Player.Sprite and Player.Cock == 'anal' and Speed" , Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Dress_Up.png"),
                    "KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Dress_Up.png"),
                    "True", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Dress.png"),
                    ),
            "KittyX.Legs == 'blue skirt'", ConditionSwitch(
                    "KittyX.Upskirt and Player.Sprite and Player.Cock == 'anal' and Speed" , Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_BlueSkirt_Up.png"),   #Rogue_Doggy_Legs_Skirt_UpAnal.png",
                    "KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_BlueSkirt_Up.png"),
                    "True", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_BlueSkirt.png"),
                    ),

            "KittyX.Upskirt", Null(),
            "KittyX.Legs == 'capris'", ConditionSwitch(
#                    "KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Blue_Down.png"),
                    "KittyX.Wet > 1", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_BlueW.png"),
                    "True", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Blue.png"),
                    ),
            "KittyX.Legs == 'black jeans'", ConditionSwitch(
#                    "KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Black_Down.png"),
                    "KittyX.Wet > 1", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_BlackW.png"),
                    "True", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Black.png"),
                    ),
            "KittyX.Legs == 'yoga pants'", ConditionSwitch(
#                    "KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga_Down.png"),
                    "KittyX.Wet > 1", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_YogaW.png"),
                    "True", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga.png"),
                    ),
            "KittyX.Legs == 'shorts'", ConditionSwitch(
#                    "KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts_Down.png"),
                    "KittyX.Wet > 1", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_ShortsW.png"),
                    "True", Recolor("Kitty", "Legs", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts.png"),
                    ),
#            "KittyX.Legs == 'skirt'", ConditionSwitch(
#                    "KittyX.Upskirt and Player.Sprite and Player.Cock == 'anal' and Speed" , "images/KittyDoggy/Kitty_Doggy_Legs_Skirt_Up.png",   #Rogue_Doggy_Legs_Skirt_UpAnal.png",
#                    "KittyX.Upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Skirt_Up.png",
#                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_Skirt.png",
#                    ),
            "True", Null(),
            ),
        )
    zoom 1.5
# End Ass / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Kitty_BJ_Head:                                                                            #These are all the details of the face
    LiveComposite(
        (858,928),
        (0,0), ConditionSwitch(
            #Hair back
            "KittyX.Water or KittyX.Hair == 'wet'", Recolor("Kitty", "Hair", "images/KittyBJFace/Kitty_BJ_HairBackWet.png"), #AlphaMask(Recolor("Kitty", "Hair", "images/KittyBJFace/Kitty_BJ_HairBackWet.png"), "Kitty_BJ_Backdrop"),
            "not Player.Male and 'facial' in KittyX.Spunk",Recolor("Kitty", "Hair", "images/KittyBJFace/Kitty_BJ_HairBackWet.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # Basic Face layer
            "Speed <= 2 or Speed == 5 or not renpy.showing('Kitty_BJ_Animation')", ConditionSwitch(
                    # If the animation isn't sucking, or if not in BJ pose
                    "KittyX.Water", ConditionSwitch(
                            # If she's wet
                            "KittyX.Blush", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_FaceClosed_Wet_Blush.png",
                            "True", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_FaceClosed_Wet.png",
                            ),
                    "KittyX.Blush", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_FaceClosed_Blush.png",
                    "True", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_FaceClosed.png"
                    ),
            #if it is in the open, sucking position
            "KittyX.Water", ConditionSwitch(
                    # If she's wet
                    "KittyX.Blush", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_FaceOpen_Wet_Blush.png",
                    "True", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_FaceOpen_Wet.png",
                    ),
            "KittyX.Blush", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_FaceOpen_Blush.png",
            "True",  "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_FaceOpen.png"
            ),
        (0,0), ConditionSwitch(
            #chin spunk
            "Player.Male and 'chin'  in KittyX.Spunk", "images/KittyBJFace/Kitty_BJ_Spunk_Chin.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Mouth
            "Speed and renpy.showing('Kitty_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
                    "Speed == 1", Recolor("Kitty", "Lips", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Mouth_Tongue.png"),  #licking
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", Recolor("Kitty", "Lips", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Mouth_Sucking.png"), #sucking
                    "Speed == 4", Recolor("Kitty", "Lips", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Mouth_Sucking.png"), #deepthroat
                    "Speed == 6", Recolor("Kitty", "Lips", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Mouth_Sucking.png"), #cumming
                    "True", Recolor("Kitty", "Lips", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Mouth_Sucking.png"), #cumming
                    ),
            "renpy.showing('Kitty_CUN_Animation') and Speed", Recolor("Kitty", "Lips", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Mouth_Tongue.png"),
            "Speed == 3 and renpy.showing('Kitty_TJ_Animation')", Recolor("Kitty", "Lips", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Mouth_Tongue.png"),
            "Speed >= 5 and renpy.showing('Kitty_TJ_Animation')", Recolor("Kitty", "Lips", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Mouth_Kiss.png"),
            "KittyX.Mouth == 'normal'", Recolor("Kitty", "Lips", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Mouth_Smile.png"),
            "KittyX.Mouth == 'lipbite'", Recolor("Kitty", "Lips", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Mouth_Lipbite.png"),
            "KittyX.Mouth == 'sucking'", Recolor("Kitty", "Lips", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Mouth_Sucking.png"),
            "KittyX.Mouth == 'kiss'", Recolor("Kitty", "Lips", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Mouth_Kiss.png"),
            "KittyX.Mouth == 'sad'", Recolor("Kitty", "Lips", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Mouth_Sad.png"),
            "KittyX.Mouth == 'smile'", Recolor("Kitty", "Lips", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Mouth_Smile.png"),
            "KittyX.Mouth == 'grimace'", Recolor("Kitty", "Lips", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Mouth_Smile.png"),
            "KittyX.Mouth == 'surprised'", Recolor("Kitty", "Lips", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Mouth_Surprised.png"),
            "KittyX.Mouth == 'tongue'", Recolor("Kitty", "Lips", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Mouth_Tongue.png"),
            "True", Recolor("Kitty", "Lips", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Mouth_Smile.png"),
            ),
        (428,555), ConditionSwitch(  #(428,605)
            # Heading Mouth
            "not renpy.showing('Kitty_BJ_Animation')", Null(),
            "Speed == 2", "Kitty_BJ_MouthHeading",  #heading
            "Speed == 5", "Kitty_BJ_MouthHigh", #cumming high
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #wet face
            "Player.Male", Null(),
            "'mouth' not in KittyX.Spunk and 'chin' not in KittyX.Spunk", Null(),
            "'chin' not in KittyX.Spunk and (KittyX.Mouth == 'tongue' or Speed)", "images/KittyBJFace/Kitty_BJ_Wet_Tongue.png",
            "KittyX.Mouth == 'tongue' or Speed", "images/KittyBJFace/Kitty_BJ_Wet_Tongue2.png",
            "'mouth' in KittyX.Spunk or 'chin' in KittyX.Spunk", "images/KittyBJFace/Kitty_BJ_Wet_Mouth.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Spunk layer
            "'mouth' not in KittyX.Spunk or not Player.Male", Null(),
            "Speed and renpy.showing('Kitty_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
                    "Speed == 1", "images/KittyBJFace/Kitty_BJ_Spunk_Tongue.png",  #licking
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png", #sucking
                    "Speed == 4", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png", #deepthroat
                    "True", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png", #cumming
                    ),
            "Speed >= 5 and renpy.showing('Kitty_TJ_Animation')", "images/KittyBJFace/Kitty_BJ_Spunk_Kiss.png",
            "KittyX.Mouth == 'normal'", "images/KittyBJFace/Kitty_BJ_Spunk_Smile.png",
            "KittyX.Mouth == 'lipbite'", "images/KittyBJFace/Kitty_BJ_Spunk_Lipbite.png",
            "KittyX.Mouth == 'kiss'", "images/KittyBJFace/Kitty_BJ_Spunk_Kiss.png",
            "KittyX.Mouth == 'sad'", "images/KittyBJFace/Kitty_BJ_Spunk_Kiss.png",
            "KittyX.Mouth == 'smile'", "images/KittyBJFace/Kitty_BJ_Spunk_Smile.png",
            "KittyX.Mouth == 'surprised'", "images/KittyBJFace/Kitty_BJ_Spunk_Surprised.png",
            "KittyX.Mouth == 'tongue'", "images/KittyBJFace/Kitty_BJ_Spunk_Tongue.png",
            "KittyX.Mouth == 'sucking'", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png", #fix add
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Brows
            "KittyX.Brows == 'normal'", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Brows_Normal.png",
            "KittyX.Brows == 'angry'", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Brows_Angry.png",
            "KittyX.Brows == 'sad'", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Brows_Sad.png",
            "KittyX.Brows == 'surprised'", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Brows_Surprised.png",
            "KittyX.Brows == 'confused'", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Brows_Confused.png",
            "True", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Brows_Normal.png",
            ),
        (0,0), "Kitty BJ Blink",
            #Eyes
        (0,0), ConditionSwitch(
            #cum on the face
            "'facial' in KittyX.Spunk and Player.Male", "images/KittyBJFace/Kitty_BJ_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hair overlay
            "KittyX.Water or KittyX.Hair == 'wet'", Recolor("Kitty", "Hair", "images/KittyBJFace/Kitty_BJ_Hair_Wet.png"),
            "not Player.Male and 'facial' in KittyX.Spunk",Recolor("Kitty", "Hair", "images/KittyBJFace/Kitty_BJ_Hair_Wet.png"),
            "KittyX.Hair == 'long'", Recolor("Kitty", "Hair", "images/KittyBJFace/Kitty_BJ_Hair_Long.png"),
            "KittyX.Hair == 'evo'", Recolor("Kitty", "Hair", "images/KittyBJFace/Kitty_BJ_Hair_Evo.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hair water overlay
            "not KittyX.Water and not (not Player.Male and 'facial' in KittyX.Spunk)", Null(),
            "Speed > 2", "images/KittyBJFace/Kitty_BJ_Wet_HeadOpen.png",
            "True", "images/KittyBJFace/Kitty_BJ_Wet_HeadClosed.png",
            ),
        (0,0), ConditionSwitch(
            #cum on the hair
            "'hair' in KittyX.Spunk and Player.Male", "images/KittyBJFace/Kitty_BJ_Spunk_Hair.png",
            "True", Null(),
            ),
        )
    zoom 1.4
    anchor (0.5, 0.5)
#end image Kitty_BJ_Head:

image Kitty BJ Blink:
        #eyeblinks
        ConditionSwitch(
            "KittyX.Eyes == 'normal'", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Eyes_Normal.png",
            "KittyX.Eyes == 'sexy'", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Eyes_Sexy.png",
            "KittyX.Eyes == 'closed'", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Eyes_Closed.png",
            "KittyX.Eyes == 'surprised'", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Eyes_Surprised.png",
            "KittyX.Eyes == 'side'", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Eyes_Side.png",
            "KittyX.Eyes == 'stunned'", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Eyes_Surprised.png",
            "KittyX.Eyes == 'down'", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Eyes_Down.png",
            "KittyX.Eyes == 'manic'", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Eyes_Surprised.png",
            "KittyX.Eyes == 'squint'", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Eyes_Squint.png",
            "True", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Eyes_Normal.png",
            ),
        choice:
            3.5
        choice:
            3.25
        choice:
            3
        "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Eyes_Closed.png"
        .25
        repeat
#end image Kitty BJ Blink:

image Kitty_BJ_MouthHeading:
    #the mouth used for the heading animations
    contains:
        Recolor("Kitty", "Lips", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Mouth_Sucking.png")
        zoom 1.4
        anchor (0.50,0.6)#(0.50,0.65)  #(0.40,0.65)
    contains:
        ConditionSwitch(
            'mouth' in KittyX.Spunk, 'images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png',
            'True', Null(),
            )
        zoom 1.4
        anchor (0.50,0.6)#(0.50,0.65)  #(0.40,0.65)
    subpixel True
    zoom 0.45 #0.90
    block:
        ease .55 zoom 0.65      #crown

        ease .15 zoom 0.60
        ease .15 zoom 0.65
        pause .45               #bottom
        ease .15 zoom 0.60
        ease .15 zoom 0.65

        ease 0.9 zoom 0.45      #Top
        repeat
# end image Kitty_BJ_MouthHeading:

image Kitty_BJ_MouthHigh:
    #the mouth used for the cumming high animations
    contains:
        Recolor("Kitty", "Lips", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_BJ_Mouth_Sucking.png")
        zoom 1.4
        anchor (0.50,0.6)#(0.50,0.65)  #(0.40,0.65)
    contains:
        ConditionSwitch(
            "'mouth' in KittyX.Spunk", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png",
            "True", Null(),
            )
        zoom 1.4
        anchor (0.50,0.6)#(0.50,0.65)  #(0.40,0.65)
    subpixel True
    zoom 0.45 #0.90
    block:
        ease 1 zoom .50            #crown
        pause .5                    #bottom
        ease 1 zoom .45              #top
        repeat
# end image Kitty_BJ_MouthHigh:

image Kitty_BJ_MouthSuckingMask:
    #the mask used for sucking animations, Kitty_BJ_Anim3, Kitty_BJ_Anim4, Kitty_BJ_Anim6
    contains:
        "images/KittyBJFace/Kitty_BJ_Mouth_SuckingMask.png"
    contains:
        ConditionSwitch(
            "'mouth' not in KittyX.Spunk or not Player.Male", Null(),
            "Speed != 2 and Speed != 5", Null(),
            "True", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png",
            )
    zoom 1.4

image Kitty_BJ_SpunkSucking:
    #the mouth used for the heading animations
    contains:
        ConditionSwitch(
            "'mouth' in KittyX.Spunk", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingO.png",
            "True", Null(),
            )
        zoom 1.4
        offset (-170,-190)


#Head and Body Animations for Kitty's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
#Head and Body Animations for Kitty's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Kitty_BJ_Anim0:
    #Animation for Kitty BJ static (Speed 0)
    contains:
            # Kitty's body, everything below the chin (Speed 0)
            "Kitty_BJ_Backdrop"
            subpixel True
            offset (0,0)
    contains:
            # Kitty's head Underlay (Speed 0)
            "Kitty_BJ_Head"
            subpixel True
            offset (0,0)
    contains:
            # Cock (Speed 0)
            "Blowcock"
            anchor (.5,.5)
            offset (300,170)
            rotate -10
#end Kitty_BJ_Anim0 Static (Speed 0)


image Kitty_BJ_Anim1:
    #Animation for Kitty BJ Licking (Speed 1)
    contains:
            # Kitty's body, everything below the chin (Speed 1)
            "Kitty_BJ_Backdrop"
            subpixel True
            offset (0,-35)  #top
            block:
                ease 2.5 offset (30,90) #bottom 25,50
                ease 2 offset (0,-35)  #top
                pause .5
                repeat

    contains:
            # Kitty's head Underlay (Speed 1)
            "Kitty_BJ_Head"
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
            offset (300,170)
            rotate 0
            block:
                ease 2 rotate -5 #410
                pause .5
                ease 2.5 rotate 0
                repeat
#end Kitty_BJ_Anim1 Licking (Speed 1)


image Kitty_BJ_Anim2:
    #Animation for Kitty BJ Heading (Speed 2)
    contains:
            # Kitty's body, everything below the chin (Speed 2)
            "Kitty_BJ_Backdrop"
            subpixel True
            offset (0,-40)     #top
            block:
                ease 1 yoffset 15           #bottom
                ease 1.5 offset (0,-40)     #top
                repeat
    contains:
            # Kitty's head Underlay (Speed 2)
            "Kitty_BJ_Head"
            subpixel True
            offset (0,-40)     #top
            block:
                ease 1 yoffset 35           #bottom
                ease 1.5 offset (0,-40)     #top
                repeat
    contains:
            # Cock (Speed 2)
            "Blowcock"
            anchor (.5,.5)
            offset (300,170)
            rotate 0
#            alpha .9
    contains:
            # Her face overlay for the heading animation  (Speed 2)
            contains:
                AlphaMask("Kitty_BJ_HeadingHead", "Kitty_BJ_MaskHeadingMask")
            subpixel True
            offset (0,-40)     #top
            anchor (0.5, 0.5)
            block:
                ease 1 yoffset 35#35           #bottom
                ease 1.5 offset (0,-40)     #top
                repeat
    contains:
            # Her spunk for the heading animation (Speed 2)
            "Kitty_BJ_SpunkHeading"
            subpixel True
            offset (0,-40)     #top
            anchor (0.5, 0.5)
            block:
                ease 1 yoffset 35           #bottom
                ease 1.5 offset (0,-40)     #top
                repeat
#end Kitty_BJ_Anim2 Heading (Speed 2)

image Kitty_BJ_MaskHeadingMask:
    #the mask used for the heading image
    contains:
        "images/KittyBJFace/Kitty_BJ_Mouth_SuckingMask.png"
        subpixel True
        transform_anchor True
        anchor (429,570)#(429,464)
        offset (429,605)#(429,464)
        zoom 0.9 #0.70
        block:
            ease .5 zoom 1.2            #crown
            pause 1                    #bottom
            ease 1 zoom 0.9              #top
            repeat
#end image Kitty_BJ_MaskHeadingMask:

image Kitty_BJ_HeadingHead:
    #An alt copy of her head that is alphaed by Kitty_BJ_MaskHeadingMask
    #used in Kitty_BJ_Anim2
    contains:
        "Kitty_BJ_Head"
        anchor (429,464)#(0.5, 0.5)
        offset (257,279)#(0.5, 0.5)

image Kitty_BJ_SpunkHeading:
    #the mouth used for the heading animations
    contains:
        contains:
            ConditionSwitch(
                "'mouth' in KittyX.Spunk", "images/KittyBJFace/Kitty_BJ_Spunk_Heading.png",
                "True", Null(),
                )
            zoom 1.4
        transform_anchor True
        anchor (600,798)#(0.5, 0.5)
        offset (430,603)#(0.5, 0.5)
        zoom 0.45      #Top
        subpixel True
        block:
            ease .55 zoom 0.65      #crown

            ease .15 zoom 0.60
            ease .15 zoom 0.65
            pause .45               #bottom
            ease .15 zoom 0.60
            ease .15 zoom 0.65

            ease 0.9 zoom 0.45      #Top
            repeat
#end image Kitty_BJ_SpunkHeading:
#end Kitty_BJ_Anim2 Heading (Speed 2) Elements / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Kitty_BJ_Anim3:
    #Animation for Kitty BJ Sucking (Speed 3)
    contains:
            # Kitty's body, everything below the chin (Speed 3)
            "Kitty_BJ_Backdrop"
            subpixel True
            offset (0,-40)     #top
            block:
                ease 1 yoffset 15           #bottom
                ease 1.5 offset (0,-40)     #top
                repeat
    contains:
            # Kitty's head Underlay (Speed 3)
            "Kitty_BJ_Head"
            subpixel True
            offset (0,50)
            block:
                ease 1 yoffset 150 #100
                ease 1.5 offset (0,50)
                repeat
    contains:
            # Cock (Speed 3)
            "Blowcock"
            anchor (.5,.5)
            offset (300,170)
            rotate 0
    contains:
            # the masked overlay for when her head overlaps the cock (Speed 3)
            AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MouthSuckingMask")
            subpixel True
            anchor (0.5, 0.5)
            offset (0,50)
            block:
                ease 1 yoffset 150 #100
                ease 1.5 offset (0,50)
                repeat
    contains:
            # Her spunk for the heading animation (Speed 3)
            "Kitty_BJ_SpunkSucking"
            subpixel True
            anchor (0.5, 0.5)
            offset (0,50)
            block:
                ease 1 yoffset 150 #100
                ease 1.5 offset (0,50)
                repeat
#end Kitty_BJ_Anim3 Sucking (Speed 3)


image Kitty_BJ_Anim4:
    #Animation for Kitty BJ Deep (Speed 4)
    contains:
            # Kitty's body, everything below the chin (Speed 4)
            "Kitty_BJ_Backdrop"
            offset (0,100)
            block:
                subpixel True
                ease 1.2 yoffset 250
                pause .5
                ease 1.8 offset (0,100)
                repeat
    contains:
            # Kitty's head Underlay (Speed 4)
            "Kitty_BJ_Head"
            offset (0,100)
            block:
                subpixel True
                ease 1 yoffset 300
                pause .5
                ease 2 offset (0,100)
                repeat
    contains:
            # Cock (Speed 4)
            "Blowcock"
            anchor (.5,.5)
            offset (300,170)
            rotate 0
    contains:
            # the masked overlay for when her head overlaps the cock (Speed 4)
            AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MouthSuckingMask")
            anchor (0.5, 0.5)
            offset (0,100)
            block:
                subpixel True
                ease 1 yoffset 300
                pause .5
                ease 2 offset (0,100)
                repeat
    contains:
            # Her spunk for the heading animation (Speed 4)
            "Kitty_BJ_SpunkSucking"
            subpixel True
            anchor (0.5, 0.5)
            offset (0,100)
            block:
                subpixel True
                ease 1 yoffset 300
                pause .5
                ease 2 offset (0,100)
                repeat
#end Kitty_BJ_Anim4 Deep (Speed 4)


image Kitty_BJ_Anim5:
    #Animation for Kitty BJ cum high (Speed 5)
    contains:
            # Kitty's body, everything below the chin (Speed 5)
            "Kitty_BJ_Backdrop"
            subpixel True
            offset (0,-30)     #top
            block:
                ease 1 yoffset -20           #bottom
                ease 1.5 offset (0,-30)     #top
                repeat
    contains:
            # Kitty's head Underlay (Speed 5)
            "Kitty_BJ_Head"
            subpixel True
            offset (0,-30)     #top
            block:
                ease 1 yoffset -20           #bottom
                ease 1.5 offset (0,-30)     #top
                repeat
    contains:
            # Cock (Speed 5)
            "Blowcock"
            anchor (.5,.5)
            offset (300,170)
            rotate 0
#            alpha 0.8
    contains:
            # Her face overlay for the heading animation  (Speed 5)
            contains:
                AlphaMask("Kitty_BJ_CumHighHead", "Kitty_BJ_MaskCumHighMask")
            subpixel True
            offset (0,-30)     #top
            anchor (0.5, 0.5)
            block:
                ease 1 yoffset -20#35           #bottom
                ease 1.5 offset (0,-30)     #top
                repeat
    contains:
            # Her spunk for the heading animation (Speed 5)
            "Kitty_BJ_SpunkCumHigh"
            subpixel True
            offset (0,-30)     #top
            anchor (0.5, 0.5)
            block:
                ease 1 yoffset -20           #bottom
                ease 1.5 offset (0,-30)     #top
                repeat
            #redo animation process for this one.
#end Kitty_BJ_Anim5 Cum High (Speed 5)

image Kitty_BJ_MaskCumHighMask:
    #the mask used for the cumming high image
    contains:
        "images/KittyBJFace/Kitty_BJ_Mouth_SuckingMask.png"
        subpixel True
        transform_anchor True
        anchor (429,570)#(429,464)
        offset (429,605)#(429,464)
        zoom .9 #0.70
        block:
            ease .5 zoom 1.2            #crown
            pause 1                    #bottom
            ease 1 zoom .9              #top
            repeat
#end image Kitty_BJ_MaskCumHighMask:

image Kitty_BJ_CumHighHead:
    #An alt copy of her head that is alphaed by Kitty_BJ_MaskCumHighMask
    #used in Kitty_BJ_Anim5
    contains:
        "Kitty_BJ_Head"
        anchor (429,464)#(0.5, 0.5)
        offset (257,279)#(0.5, 0.5)

image Kitty_BJ_SpunkCumHigh:
    #the spunk used for the cumming high animations
    contains:
        contains:
            ConditionSwitch(
                "'mouth' in KittyX.Spunk", "images/KittyBJFace/Kitty_BJ_Spunk_Heading.png",
                "True", Null(),
                )
            zoom 1.4
        transform_anchor True
        anchor (600,798)#(600,798)
        offset (430,603)#(430,601)
        zoom .45              #top
        subpixel True
        block:
            ease 1 zoom .50            #crown
            pause .5                    #bottom
            ease 1 zoom .45              #top
            repeat
#end image Kitty_BJ_SpunkCumHigh:
#end Kitty_BJ_Anim5 Cum High (Speed 5) Elements / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Kitty_BJ_Anim6:
    #Animation for Kitty BJ cum deep (Speed 6)
    contains:
            # Kitty's body, everything below the chin (Speed 6)
            "Kitty_BJ_Backdrop"
            offset (0,190)
            block:
                subpixel True
                ease 1.2 yoffset 200
                pause .5
                ease 1.8 offset (0,190)
                repeat
    contains:
            # Kitty's head Underlay (Speed 6)
            "Kitty_BJ_Head"
            offset (0,230)
            block:
                subpixel True
                ease 1 yoffset 250
                pause .5
                ease 2 offset (0,230)
                repeat
    contains:
            # Cock (Speed 6)
            "Blowcock"
            anchor (.5,.5)
            offset (300,170)
            rotate 0
    contains:
            # the masked overlay for when her head overlaps the cock (Speed 6)
            AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MouthSuckingMask")
            anchor (0.5, 0.5)
            offset (0,230)
            block:
                subpixel True
                ease 1 yoffset 250
                pause .5
                ease 2 offset (0,230)
                repeat
    contains:
            # Her spunk for the heading animation (Speed 6)
            "Kitty_BJ_SpunkSucking"
            subpixel True
            anchor (0.5, 0.5)
            offset (0,230)
            block:
                subpixel True
                ease 1 yoffset 250
                pause .5
                ease 2 offset (0,230)
                repeat
#end Kitty_BJ_Anim6 cum deep (Speed 6)

#end Kitty_BJ_Anims / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
#BJ Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Kitty_BJ_Launch(Line = Trigger):    # The sequence to launch the Kitty BJ animations
    if renpy.showing("Kitty_BJ_Animation") and KittyX.Pose != "69":
        return
    elif renpy.showing("Kitty_69_Animation") and KittyX.Pose == "69":
        return

    if not Player.Male:
        call Kitty_CUN_Launch
        return

    call Girl_Hide(KittyX)
    if Line == "L" or Line == "cum":
        show Kitty_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1
            ease 1 zoom 2.5 offset (150,80)
        with dissolve
    else:
        show Kitty_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1
            zoom 2.5 offset (150,80)
        with dissolve

    $ Speed = 0
    $ Player.Sprite = 1

    if Line != "cum":
        $ Trigger = "blow"

    show Kitty_Sprite zorder KittyX.Layer:
        alpha 0

    if KittyX.Pose == "69":
            show Kitty_69_Animation zorder 150
    else:
            show Kitty_BJ_Animation zorder 150

    if Line == "L":
            if Taboo:
                if len(Present) >= 2:
                    if Present[0] != KittyX:
                            "[KittyX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                    elif Present[1] != KittyX:
                            "[KittyX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
                else:
                            "[KittyX.Name] небрежно оглядывается по сторонам, чтобы убедиться, что никто не наблюдает."
            if not KittyX.Blow:
                "[KittyX.Name] нерешительно опускается на колени и прикасается своим ртом к вашему члену."
            else:
                "[KittyX.Name] встает на колени и начинает сосать ваш член."
    return

label Kitty_BJ_Reset: # The sequence to the Kitty animations from BJ to default
    if Player.Male != 1:
            call Kitty_CUN_Reset
    if not renpy.showing("Kitty_BJ_Animation") and not renpy.showing("Kitty_69_Animation"):
            return
    call Girl_Hide(KittyX)
    $ Speed = 0

    show Kitty_Sprite at SpriteLoc(StageCenter) zorder 150:
        alpha 1
        zoom 2.5 offset (150,80)
    with dissolve

    show Kitty_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
        alpha 1
        zoom 1 offset (0,0)

    return

# End Kitty Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Start Kitty TJ Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Kitty TJ annimation element ///////////////////////////////////////////////////////////////////////////                                     Core Kitty BJ element

image Kitty_TJ_Animation:
    #core titjob animation
    contains:
        ConditionSwitch(
            # Kitty's upper body
            "Player.Sprite", ConditionSwitch(
                    # If during sex
                    "Speed == 1", "Kitty_TJ_Body_1",#slow
                    "Speed == 2", "Kitty_TJ_Body_2",#fast
                    "Speed == 3", "Kitty_TJ_Body_3",#licking
                    "Speed >= 5", "Kitty_TJ_Body_5",#cumming
                    "True",       "Kitty_TJ_Body_0",#Static
                    ),
            "True","Kitty_TJ_Body_0",#Static
            )
    zoom 1.35 #0.8
    anchor (.5,.5)
    pos (600,605) #(600,705)#height for bj


image Kitty_TJ_Torso:
    # Her torso for the sex, BJ, and TJ poses
    contains:
            #body
            "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_TJ_Body.png"
    contains:
            # necklaces
        ConditionSwitch(
            "KittyX.Neck == 'gold necklace'", "images/KittyBJFace/Kitty_TJ_Neck_Gold.png",   # KittyX.TitsUp = 1
            "KittyX.Neck == 'star necklace'", "images/KittyBJFace/Kitty_TJ_Neck_Star.png",   # KittyX.TitsUp = 1
            "KittyX.Neck == 'flower necklace'", "images/KittyBJFace/Kitty_TJ_Neck_Flower.png",   # KittyX.TitsUp = 1
            "True", Null(),
            )
    contains:
            # Over clothing layer
        ConditionSwitch(
            "KittyX.Over == 'jacket'", Recolor("Kitty", "Over", "images/KittyBJFace/Kitty_TJ_Over_Jacket.png"),   # KittyX.TitsUp = 1
            "KittyX.Over == 'red shirt'", Recolor("Kitty", "Over", "images/KittyBJFace/Kitty_TJ_Over_Red.png"),   # KittyX.TitsUp = 1
            "KittyX.Over == 'pink top'", Recolor("Kitty", "Over", "images/KittyBJFace/Kitty_TJ_Over_Pink.png"),   # KittyX.TitsUp = 1
            "True", Null(),
            )
    contains:
            # spunk on tits
            ConditionSwitch(
                "KittyX.Water", "images/KittyBJFace/Kitty_TJ_Wet_Body.png",
                "True", Null(),
                )
    contains:
            # spunk on belly
            ConditionSwitch(
                "'belly' in KittyX.Spunk and Player.Male", "images/KittyBJFace/Kitty_TJ_Spunk_Belly.png",
                "True", Null(),
                )
    contains:
            # spunk on tits
            ConditionSwitch(
                "'tits' in KittyX.Spunk and Player.Male", "images/KittyBJFace/Kitty_TJ_Spunk_Tits.png",
                "True", Null(),
                )

#image Kitty_TJ_Arms:
#    # Her arms for the TJ poses
#    contains:
#            #body
#            "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_TJ_Arms.png"

image Kitty_TJ_Tits:
    #core titjob breasts
    contains:
            #base layer
#            "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_TJ_Tits.png"
        ConditionSwitch(
#            "Player.Sprite and Speed", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_TJ_Tits_Smooshed.png",
            "KittyX.Pierce == 'barbell'", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_TJ_Tits_Barbell.png",
            "KittyX.Pierce == 'ring'",  "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_TJ_Tits_Ring.png",
            "True",                     "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_TJ_Tits.png",
            )
    contains:
            # spunk on tits
            ConditionSwitch(
                "KittyX.Water", "images/KittyBJFace/Kitty_TJ_Wet_Tits.png",
                "True", Null(),
                )
    contains:
            #shirt sleaves
        ConditionSwitch(
#            "Player.Sprite and Speed", "images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_TJ_Tits_Smooshed.png",
            "KittyX.Over == 'pink top'", Recolor("Kitty", "Over", "images/KittyBJFace/Kitty_TJ_Arms_Pink.png"),
            "True",                     Null(),
            )
    contains:
            #chest clothing layer
        ConditionSwitch(
            "KittyX.Chest == 'bra'", Recolor("Kitty", "Chest", "images/KittyBJFace/Kitty_TJ_Chest_Bra.png"),
            "KittyX.Chest == 'bikini top'", Recolor("Kitty", "Chest", "images/KittyBJFace/Kitty_TJ_Chest_Bikini.png"),
            "KittyX.Chest == 'dress'", Recolor("Kitty", "Chest", "images/KittyBJFace/Kitty_TJ_Chest_Dress.png"),
            "KittyX.Chest == 'cami' and KittyX.Over", Recolor("Kitty", "Chest", "images/KittyBJFace/Kitty_TJ_Chest_CamiC.png"),
            "KittyX.Chest == 'cami'", Recolor("Kitty", "Chest", "images/KittyBJFace/Kitty_TJ_Chest_Cami.png"),
            "KittyX.Chest == 'sports bra' and KittyX.Over", Recolor("Kitty", "Chest", "images/KittyBJFace/Kitty_TJ_Chest_SportsC.png"),
            "KittyX.Chest == 'sports bra'", Recolor("Kitty", "Chest", "images/KittyBJFace/Kitty_TJ_Chest_Sports.png"),
            "KittyX.Chest == 'lace bra' and KittyX.Over", "images/KittyBJFace/Kitty_TJ_Chest_LaceC.png",
            "KittyX.Chest == 'lace bra'", "images/KittyBJFace/Kitty_TJ_Chest_Lace.png",
            "True", Null(),   # KittyX.TitsUp = 0
            )

#    contains:
#            # spunk on tits
#        ConditionSwitch(
#                "'tits' in KittyX.Spunk", "images/KittySex/Kitty_Spunk_Titjob_Over.png",
#                "True", Null(),
#                )


#image Kitty_TJ_MaskA:
#    #Test mask for showing her moving chest
#    contains:
##        Solid("#159457", xysize=(750,750))
#        "images/KittyBJFace/Kitty_TJ_Mask.png"

image Kitty_Mega_Mask:
    # giant green brick for use in finding where a mask is
    contains:
        Solid("#159457", xysize=(1750,1750))
        alpha .5


#  TJ animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Kitty_TJ_Body_0:
        #Her Body in the TJ pose, idle
        contains:
                #Hair underlay
                "Kitty_BJ_HairBack"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (505,260) #bottom  #505
                subpixel True
                block:
                    ease 2.4 ypos 250 #top
                    ease 1.6 ypos 260 #bottom
                    repeat
        contains:
                #base body
                "Kitty_TJ_Torso"#"images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_TJ_Body.png"
                pos (545,330)#(500,360)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.4 ypos 325 #top
                    ease 1.6 ypos 330 #bottom
                    repeat
#        contains:
#                #arms
#                "Kitty_TJ_Arms"#"images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_TJ_Arms.png"
#                pos (545,330)#pos (0,0) #bottom
#                anchor (0.5, 0.5)
#                zoom 0.55           #temp
#                subpixel True
#                block:
#                    ease 2.4 ypos 325 #top
#                    ease 1.6 ypos 330 #bottom
#                    repeat
        contains:
                #tits underlayer
                "Kitty_TJ_Tits"
                pos (545,330)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.4 ypos 325 #top
                    ease 1.6 ypos 330 #bottom
                    repeat
        contains:
                #head
                "Kitty_BJ_Head"
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
#End TJ animation Speed 0


image Kitty_TJ_Mask_1:
        contains:
            #"images/KittyBJFace/Kitty_TJ_Mask.png"
            ConditionSwitch(
                "KittyX.Chest == 'dress'", "images/KittyBJFace/Kitty_TJ_Mask_Dress.png",
                "KittyX.Chest", "images/KittyBJFace/Kitty_TJ_Mask_Bra.png",
                "True", "images/KittyBJFace/Kitty_TJ_Mask.png",
                )
            pos (100,60) #bottom #pos (545,330)
            anchor (0.5, 0.5)
            zoom 1.4           #temp
            subpixel True
            block:
                ease 2.9 ypos -40 #top 280
                ease 1 ypos 60 #bottom 330
                pause .1
                repeat

image Kitty_TJ_Body_1:
        #Her Body in the TJ pose, slow 1
        contains:
                #Hair underlay
                "Kitty_BJ_HairBack"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (505,260) #bottom  #505
                subpixel True
                block:
                    ease 3 ypos 210 #top
                    ease 1 ypos 260 #bottom
                    repeat
        contains:
                #base body
                "Kitty_TJ_Torso"#"images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_TJ_Body.png"
                pos (545,330)#(500,360)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.8 ypos 280 #top
                    ease 1 ypos 330 #bottom
                    pause .2
                    repeat
#        contains:
#                #arms
#                "Kitty_TJ_Arms"#"images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_TJ_Arms.png"
#                pos (545,330)#pos (0,0) #bottom
#                anchor (0.5, 0.5)
#                zoom 0.55           #temp
#                subpixel True
#                block:
#                    ease 2.85 ypos 280 #top
#                    ease 1 ypos 330 #bottom
#                    pause .15
#                    repeat
        contains:
                #tits underlayer
                "Kitty_TJ_Tits"
                pos (545,330)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.9 ypos 280 #top
                    ease 1 ypos 330 #bottom
                    pause .1
                    repeat
        contains:
                #head
                "Kitty_BJ_Head"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (505,260) #bottom  #280
                subpixel True
                block:
                    ease 2.9 ypos 210 #top
                    ease 1 ypos 260 #bottom
                    pause .1
                    repeat
        contains:
                #zero's cock
                ConditionSwitch(
                    "Player.Sprite", AlphaMask("Blowcock", "Kitty_TJ_Mask_1"),
                    "True", Null(),
                    )
                subpixel True
                pos (665,500) #bottom #150
                anchor (0.5,0.5)
                zoom 0.4
                block:
                    ease 2.8 ypos 490 #top
                    ease .8 ypos 500 #bottom
                    pause .4
                    repeat
#End TJ animation Speed 1


image Kitty_TJ_Mask_2:
        contains:
            #"images/KittyBJFace/Kitty_TJ_Mask.png"
            ConditionSwitch(
                "KittyX.Chest == 'dress'", "images/KittyBJFace/Kitty_TJ_Mask_Dress.png",
                "KittyX.Chest", "images/KittyBJFace/Kitty_TJ_Mask_Bra.png",
                "True", "images/KittyBJFace/Kitty_TJ_Mask.png",
                )
            pos (100,60) #bottom #pos (545,330)
            anchor (0.5, 0.5)
            zoom 1.4           #temp
            subpixel True
            block:
                ease .71 ypos -15 #top 280
                ease .27 ypos 60 #bottom 330
                pause .02
                repeat

image Kitty_TJ_Body_2:
        #Her Body in the TJ pose, fast 2
        contains:
                #Hair underlay
                "Kitty_BJ_HairBack"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (505,260) #bottom  #505
                subpixel True
                block:
                    ease .7 ypos 215 #top
                    ease .25 ypos 260 #bottom
                    pause .05
                    repeat
        contains:
                #base body
                "Kitty_TJ_Torso"#"images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_TJ_Body.png"
                pos (545,330)#(500,360)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease .65 ypos 285 #top
                    ease .25 ypos 330 #bottom
                    pause .1
                    repeat
#        contains:
#                #arms
#                "Kitty_TJ_Arms"#"images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_TJ_Arms.png"
#                pos (545,330)#pos (0,0) #bottom
#                anchor (0.5, 0.5)
#                zoom 0.55           #temp
#                subpixel True
#                block:
#                    ease .68 ypos 285 #top
#                    ease .25 ypos 330 #bottom
#                    pause .07
#                    repeat
        contains:
                #tits underlayer
                "Kitty_TJ_Tits"
                pos (545,330)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease .71 ypos 290 #top
                    ease .27 ypos 330 #bottom
                    pause .02
                    repeat
        contains:
                #head
                "Kitty_BJ_Head"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (505,260) #bottom  #280
                subpixel True
                block:
                    ease .68 ypos 215 #top
                    ease .25 ypos 260 #bottom
                    pause .07
                    repeat
        contains:
                #zero's cock
                ConditionSwitch(
                    "Player.Sprite", AlphaMask("Blowcock", "Kitty_TJ_Mask_2"),
                    "True", Null(),
                    )
                subpixel True
                pos (665,500) #bottom #150
                anchor (0.5,0.5)
                zoom 0.4
                block:
                    ease .72 ypos 490 #top
                    ease .27 ypos 500 #bottom
                    pause .01
                    repeat
#End TJ animation Speed 2


image Kitty_TJ_Mask_3:
        contains:
            #"images/KittyBJFace/Kitty_TJ_Mask.png"
            ConditionSwitch(
                "KittyX.Chest == 'dress'", "images/KittyBJFace/Kitty_TJ_Mask_Dress.png",
                "KittyX.Chest", "images/KittyBJFace/Kitty_TJ_Mask_Bra.png",
                "True", "images/KittyBJFace/Kitty_TJ_Mask.png",
                )
            pos (100,140) #bottom #pos (545,330)
            anchor (0.5, 0.5)
            zoom 1.4           #temp
            subpixel True
            block:
                ease 2.2 ypos 90 #top 280
                ease .6 ypos 140 #bottom 330
                pause .2
                repeat

image Kitty_TJ_Body_3:
        #Her Body in the TJ pose, licking 3
        contains:
                #Hair underlay
                "Kitty_BJ_HairBack"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (500,260) #bottom  #505
                rotate 0
                subpixel True
                block:
                    #left tilted loop
                    ease 2.2 pos (500,290) #top
                    ease .8 pos (520,320) #bottom
                    ease 2.2 pos (510,290) #top
                    ease .8 pos (520,320) #bottom
                    repeat
        contains:
                #base body
                "Kitty_TJ_Torso"#"images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_TJ_Body.png"
                pos (545,360)#(500,360)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.2 ypos 340 #top
                    ease .6 ypos 360 #bottom
                    pause .2
                    repeat
#        contains:
#                #arms
#                "Kitty_TJ_Arms"#"images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_TJ_Arms.png"
#                pos (545,360)#pos (0,0) #bottom
#                anchor (0.5, 0.5)
#                zoom 0.55           #temp
#                subpixel True
#                block:
#                    ease 2.2 ypos 340 #top
#                    ease .6 ypos 360 #bottom
#                    pause .2
#                    repeat
        contains:
                #tits underlayer
                "Kitty_TJ_Tits"
                pos (545,360)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.2 ypos 340 #top
                    ease .6 ypos 360 #bottom
                    pause .2
                    repeat
        contains:
                #head
                "Kitty_BJ_Head"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (500,310) #bottom  #505
                subpixel True
                rotate 0
                block:
                    #left tilted loop
                    ease 2.2 pos (500,290) rotate 0 #top
                    ease .8 pos (520,320) rotate 10#bottom
                    ease 2.2 pos (510,290) rotate 0#top
                    ease .8 pos (520,320) rotate 5#bottom
                    repeat
        contains:
                #zero's cock
                ConditionSwitch(
                    "Player.Sprite", AlphaMask("Blowcock", "Kitty_TJ_Mask_3"),
                    "True", Null(),
                    )
                subpixel True
                pos (665,500) #bottom #150
                anchor (0.5,0.5)
                zoom 0.4
#End TJ animation Speed 3


image Kitty_TJ_Mask_5:
        contains:
            #"images/KittyBJFace/Kitty_TJ_Mask.png"
            ConditionSwitch(
                "KittyX.Chest == 'dress'", "images/KittyBJFace/Kitty_TJ_Mask_Dress.png",
                "KittyX.Chest", "images/KittyBJFace/Kitty_TJ_Mask_Bra.png",
                "True", "images/KittyBJFace/Kitty_TJ_Mask.png",
                )
            pos (100,140) #bottom #pos (545,330)
            anchor (0.5, 0.5)
            zoom 1.4           #temp
            subpixel True
            block:
                ease 2.2 ypos 120 #top 280 #90
                ease 1.6 ypos 140 #bottom 330
                pause .2
                repeat

image Kitty_TJ_Body_5:
        #Her Body in the TJ pose, cumming 5
        contains:
                #Hair underlay
                "Kitty_BJ_HairBack"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (500,260) #bottom  #505
                rotate 0
                subpixel True
                block:
                    #un tilted loop
                    ease 2 pos (500,304) #top 280
                    ease 1.6 pos (500,307) #bottom 315
                    pause .4
                    repeat
        contains:
                #base body
                "Kitty_TJ_Torso"#"images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_TJ_Body.png"
                pos (545,360)#(500,360)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.2 ypos 350 #top
                    ease 1.6 ypos 360 #bottom
                    pause .2
                    repeat
#        contains:
#                #arms
#                "Kitty_TJ_Arms"#"images/KittyBJFace/[KittyX.skin_image.skin_path]Kitty_TJ_Arms.png"
#                pos (545,360)#pos (0,0) #bottom
#                anchor (0.5, 0.5)
#                zoom 0.55           #temp
#                subpixel True
#                block:
#                    ease 2.2 ypos 350 #top
#                    ease 1.6 ypos 360 #bottom
#                    pause .2
#                    repeat
        contains:
                #tits underlayer
                "Kitty_TJ_Tits"
                pos (545,360)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.2 ypos 350 #top
                    ease 1.6 ypos 360 #bottom
                    pause .2
                    repeat
    #    contains:
    #            #tits underlayer
    #            "Kitty_TJ_MaskA"
    #            pos (545,360)#pos (0,0) #bottom
    #            anchor (0.5, 0.5)
    #            zoom 0.55           #temp
    #            subpixel True
    #            block:
    #                ease 2.2 ypos 350 #top
    #                ease 1.6 ypos 360 #bottom
    #                pause .2
    #                repeat
        contains:
                #head
                "Kitty_BJ_Head"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (500,307) #bottom  #505
                subpixel True
                rotate 0
                block:
                    #un tilted loop
                    ease 2 pos (500,304) #top 280
                    ease 1.6 pos (500,307) #bottom 315
                    pause .4
                    repeat
        contains:
                #zero's cock
                ConditionSwitch(
    #                "Player.Sprite", AlphaMask("Kitty_Mega_Mask", "Kitty_TJ_Mask_5"),
                    "Player.Sprite", AlphaMask("Blowcock", "Kitty_TJ_Mask_5"),
    #                "Player.Sprite", AlphaMask("Blowcock", "Kitty_Mega_Mask"),
                    "True", Null(),
                    )
                subpixel True
                pos (665,500) #bottom #150
                anchor (0.5,0.5)
                zoom 0.4

    #    contains:
    #            #zero's cock
    #            ConditionSwitch(
    #                "Player.Sprite", "Blowcock",
    #                "True", Null(),
    #                )
    #            subpixel True
    #            alpha 0.2
    #            pos (640,150) #bottom #150
    #            anchor (0.5,0.5)
    #            zoom 0.4
    #    contains:
    #            #tits
    #            "Kitty_Tits_Mask"
    #            pos (545,360)#pos (0,0) #bottom
    #            anchor (0.5, 0.5)
    #            zoom 0.55           #temp
    #            subpixel True
    #            block:
    #                ease 2.2 ypos 340 #top
    #                ease .6 ypos 360 #bottom
    #                pause .2
    #                repeat
#End TJ animation Speed 5 (cumming)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


label Kitty_TJ_Launch(Line = Trigger):    # The sequence to launch the Kitty Titfuck animations
    if renpy.showing("Kitty_TJ_Animation"):
        return
    call Girl_Hide(KittyX)
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 2 xpos 700 yoffset 50 #offset (-100,50)
    if Line == "L" and Taboo:
                if len(Present) >= 2:
                    if Present[0] != KittyX:
                            "[KittyX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                    elif Present[1] != KittyX:
                            "[KittyX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
                else:
                            "[KittyX.Name] небрежно оглядывается по сторонам, чтобы убедиться, что никто не наблюдает."
    if KittyX.Chest and KittyX.Over:
        "Она скидывает [get_clothing_name(KittyX.Over_key, vin)] и [get_clothing_name(KittyX.Chest_key, vin)]."
    elif KittyX.Over:
        "Она скидывает [get_clothing_name(KittyX.Over_key, vin)], обнажая свою грудь."
    elif KittyX.Chest:
        "Она снимает [get_clothing_name(KittyX.Chest_key, vin)] и отбрасывает в сторону."
#    $ KittyX.Over = 0
#    $ KittyX.Chest = 0
#    $ KittyX.ArmPose = 0
    $ KittyX.Uptop = 1
    call Girl_First_Topless(KittyX)      #restore if topless
    if Line == "L":
            if not KittyX.Tit:
                "Она нерешительно прижимает ваш член к своей груди."
            else:
                "Она сжимает свои груди вокруг вашего члена."


    show blackscreen onlayer black with dissolve
    show Kitty_Sprite zorder KittyX.Layer:
        alpha 0
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "titjob"
    show Kitty_TJ_Animation zorder 150
    $ Player.Sprite = 1
    hide blackscreen onlayer black with dissolve
    return

label Kitty_TJ_Reset: # The sequence to the Kitty animations from Titfuck to default
    if not renpy.showing("Kitty_TJ_Animation"):
            return
    call Girl_Hide(KittyX)
    $ Player.Sprite = 0

    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder 150:
            zoom 2 xpos 550 yoffset 50 alpha 1
            ease 1 zoom 1.5 xpos 700 yoffset 50
            pause .5
            ease .5 zoom 1 xpos KittyX.SpriteLoc yoffset 0
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
            alpha 1 zoom 1 offset (0,0) xpos KittyX.SpriteLoc
#    "Kitty pulls back"
    return

# End Kitty TJ Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /






# Start Kitty Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Kitty Handjob element //////////////////////////////////////////////////////////////////////                                         Core Kitty HJ element

image Kitty_HJ_Body:
    "Kitty_Sprite"
    pos (680,-1250)#(350,-550)
    zoom 4.8#2.15


transform Kitty_HJ_Body_1():
    subpixel True
#    pos (700,-1250)#(350,-550)
    block:
        ease .5 ypos -1220
        pause 0.25
        ease 1.0 ypos -1250
        pause 0.1
        repeat

transform Kitty_HJ_Body_2():
    subpixel True
#    pos (350,-550)
    block:
        ease 0.2 ypos -1240
        pause 0.1
        ease 0.4 ypos -1250
        pause 0.1
        repeat


image Kitty_Hand_Under:
    "images/KittySprite/[KittyX.skin_image.skin_path]handkitty2.png"
    anchor (0.5,0.5)
    pos (0,0)


image Kitty_Hand_Over:
    "images/KittySprite/[KittyX.skin_image.skin_path]handkitty1.png"
    anchor (0.5,0.5)
    pos (0,0)

#transform Handcock_1():
#    subpixel True
#    rotate_pad False
#    ease .5 ypos 450 rotate -2 #450
#    pause 0.25
#    ease 1.0 ypos 400 rotate 0 #400
#    pause 0.1
#    repeat

#transform Handcock_2():
#    subpixel True
#    rotate_pad False
#    ease .2 ypos 430 rotate -3 #410
#    ease .5 ypos 400 rotate 0
#    pause 0.1
#    repeat

transform Kitty_Hand_1():
    subpixel True
    ease .5 ypos 150 rotate 5 #500 #100 #rotate 10#   Bottom
    pause 0.25
    ease 1.0 ypos -100 rotate -5 #250#-150 #rotate -10#  Top
    pause 0.1
    repeat

transform Kitty_Hand_2():
    subpixel True
    ease 0.2 ypos 0 rotate 3
    pause 0.1
    ease 0.4 ypos -100 rotate -3
    pause 0.1
    repeat

image Kitty_HJ_Animation:
    contains:
        ConditionSwitch(
            # backside of the hand
            "not Speed", Transform("Kitty_HJ_Body"),
            "Speed == 1", At("Kitty_HJ_Body", Kitty_HJ_Body_1()),
            "Speed >= 2", At("Kitty_HJ_Body", Kitty_HJ_Body_2()),
            "Speed", Null(),
            )
    contains:
        ConditionSwitch(                                                # backside of the hand
            "not Speed", Transform("Kitty_Hand_Under"),
            "Speed == 1", At("Kitty_Hand_Under", Kitty_Hand_1()),
            "Speed >= 2", At("Kitty_Hand_Under", Kitty_Hand_2()),
            "Speed", Null(),
            ),
    contains:
        ConditionSwitch(                                                # cock
            "not Speed", Transform("Zero_Handcock"),
            "Speed == 1", At("Zero_Handcock", Handcock_1()),
            "Speed >= 2", At("Zero_Handcock", Handcock_2()),
            "Speed", Null(),
            ),
        offset (0,0)
    contains:
        ConditionSwitch(                                                # fingers of the hand
            "not Speed", Transform("Kitty_Hand_Over"),
            "Speed == 1", At("Kitty_Hand_Over", Kitty_Hand_1()),
            "Speed >= 2", At("Kitty_Hand_Over", Kitty_Hand_2()),
            "Speed", Null(),
            ),
    anchor (0.51, -1.3)
    zoom 0.4#0.6


label Kitty_HJ_Launch(Line = Trigger):
    if renpy.showing("Kitty_HJ_Animation"):
        $ Trigger = "hand"
        return
    if not Player.Male:
        call Kitty_Finger_Launch
        return
    call Girl_Hide(KittyX)
    if Line == "L":
        show Kitty_Sprite at SpriteLoc(StageRight) zorder 150:
            alpha 1
            ease 1 zoom 1.8 offset (0,200)#(150,0)#(-50,200)
    else:
        show Kitty_Sprite at SpriteLoc(StageRight) zorder 150:
            alpha 1
            ease 1 zoom 1.8 offset (0,200)#(150,0)#(-50,200)
        with dissolve

    if Line == "L":
            if Taboo:
                if len(Present) >= 2:
                    if Present[0] != KittyX:
                            "[KittyX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                    elif Present[1] != KittyX:
                            "[KittyX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
                else:
                            "[KittyX.Name] небрежно оглядывается по сторонам, чтобы убедиться, что никто не наблюдает."
            else:
                "[KittyX.Name] наклоняется и хватает ваш член."

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    else:
        $ Speed = 1
    pause .5
    show Kitty_Sprite:
        alpha 0
    show Kitty_HJ_Animation at SpriteLoc(StageCenter) zorder 150 with fade:
        #xoffset 150
        offset (100,250)#(75,250)
    return

label Kitty_HJ_Reset: # The sequence to the Rogue animations from handjob to default
    if not renpy.showing("Kitty_HJ_Animation"):
            return
    $ Speed = 0
    hide Kitty_HJ_Animation with dissolve
    call Girl_Hide(KittyX)
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder 150:
            alpha 1
            ease 1 zoom 1.5 offset (-150,50)
            pause .5
            ease .5 zoom 1 offset (0,0)
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
            alpha 1 zoom 1 offset (0,0)
    return


#label Kitty_Kissing_Launch(T = Trigger,Set=1):
#    call Girl_Hide(KittyX)
#    $ Trigger = T
#    $ KittyX.Pose = "kiss" if Set else KittyX.Pose
#    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer
#    show Kitty_Sprite at SpriteLoc(StageCenter):
#            ease 0.5 offset (0,0) zoom 2 alpha 1
#    return

#label Kitty_Kissing_Smooch:
#    $ KittyX.FaceChange("kiss")
#    show Kitty_Sprite at SpriteLoc(StageCenter) zorder KittyX.Layer:
#        ease 0.5 xpos StageCenter offset (0,0) zoom 2 alpha 1
#        pause 1
#        ease 0.5 xpos KittyX.SpriteLoc zoom 1
#    $ KittyX.FaceChange("sexy")
#    return

#label Kitty_Breasts_Launch(T = Trigger,Set=1):
#    call Kitty_Hide
#    $ Trigger = T
#    $ KittyX.Pose = "breasts" if Set else KittyX.Pose
#    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
#        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1 # pos (900,-50)
#    return

#label Kitty_Middle_Launch(T = Trigger,Set=1):
#    call Kitty_Hide
#    $ Trigger = T
#    $ KittyX.Pose = "mid" if Set else KittyX.Pose
#    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
##        ease 0.5 offset (-100,-200) zoom 2
#        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
#    return

#label Kitty_Pussy_Launch(T = Trigger,Set=1):
#    call Kitty_Hide
#    $ Trigger = T
#    $ KittyX.Pose = "pussy" if Set else KittyX.Pose
#    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
#        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
#    return

#label Kitty_Pos_Reset(T = 0,Set=0):
#    if KittyX.Loc != bg_current:
#            return
#    call Kitty_Hide
#    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
#        ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
#    show Kitty_Sprite zorder KittyX.Layer:
#        offset (0,0)
#        anchor (0.5, 0.0)
#        zoom 1
#        xzoom 1
#        yzoom 1
#        alpha 1
#        pos (KittyX.SpriteLoc,50)
#    $ KittyX.Pose = "full" if Set else 0
#    $ Trigger = T
#    return

#label Kitty_Hide(Sprite=0):
##        call Kitty_Sex_Reset
#        hide Kitty_SexSprite
#        hide Kitty_Doggy_Animation
#        hide Kitty_HJ_Animation
#        hide Kitty_BJ_Animation
#        hide Kitty_TJ_Animation
#        hide Kitty_Finger_Animation
#        hide Kitty_CUN_Animation
#        hide Kitty_69_Animation
#        hide Kitty_69_CUN
#        hide Kitty_Seated
#        if Sprite:
#                hide Kitty_Sprite
#        return



# End Kitty Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# Core Kitty CUN element ///////////////////////////////////////////////////////////////////////////                                     Core Kitty CUN element
#Kitty CUN Over Sprite Compositing

image Kitty_CUN_Animation: #core CUN animation
    LiveComposite(
        (787,913),
        (0,0), ConditionSwitch(                                                                 # back of the hair, which needs to go behind the body
            "Speed == 0",  "Kitty_CUN_Anim_Static",
            "Speed == 1",  "Kitty_CUN_Anim_Licking1",
            "Speed == 2",  "Kitty_CUN_Anim_Licking2",
            "Speed >= 3",  "Kitty_CUN_Anim_Licking3",
#            "Speed == 4",  "Kitty_CUN_Anim_Licking1",
            "True", "Kitty_CUN_Anim_Static",
            ),
        )
    zoom .55
    anchor (.5,.5)

image Kitty_CUN_Anim_Static:
    #Animation for licking speed 1
#    contains:
#        #hair
#        "Kitty_BJ_HairBack"#"BJ_HairBack"
#        subpixel True
#        offset (-10,0)
    contains:
        #body 2
        "Kitty_BJ_Backdrop"
        pos (0,0)#(-330,-500)#(175,-110)
        subpixel True
        offset (20,20)  #top(0,-35)
        block:
            ease 2 yoffset 30
            ease 2 yoffset 20
            repeat
    contains:
        #head
        "Kitty_BJ_Head"#"BJ_Head"
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


image Kitty_CUN_Anim_Licking1:
    #Animation for licking speed 1
#    contains:
#        #hair
#        "Kitty_BJ_HairBack"#"BJ_HairBack"
#        subpixel True
#        offset (-80,0)#490)
#        block: #5s total
#            ease 2.5 offset (-60,100) #bottom
#            easeout 1.5 offset (-70,50)  #top -35)
#            linear .5 offset (-80,0)  #top -35)
#            pause .5
#            repeat
    contains:
        #body 2
        "Kitty_BJ_Backdrop"#"Kitty_Sprite"
#        zoom 1 #4.5
        pos (0,0)#(-300,-200)#(200,-750)#(545,-300)
        subpixel True
        offset (0,0)# -70,0
        block:
            ease 2.5 offset (0,75) #bottom (30,90)
            ease 2.3 offset (0,0)  #top
            pause .2
            repeat
    contains:
        #head
        "Kitty_BJ_Head"#"BJ_Head"
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
#End Kitty Licking 1

image Kitty_CUN_Anim_Licking2:
    #Animation for licking speed 2
#    contains:
#        #hair
#        "Kitty_BJ_HairBack"#"BJ_HairBack"
#        subpixel True
#        offset (-80,30)#490)
#        block: #2s total
#            ease 1 offset (-60,100) #bottom
#            easeout .65 offset (-70,70)  #top -35)
#            linear .25 offset (-80,30)  #top -35)
#            pause .1
#            repeat
    contains:
        #body 2
        "Kitty_BJ_Backdrop"
        pos (0,0)#(175,-110)
        subpixel True
        offset (0,0)#490)
        block:
            ease .75 offset (0,70) #bottom (30,90)
            ease .95 offset (0,30)  #top
            pause .30
            repeat

    contains:
        #head
        "Kitty_BJ_Head"#"BJ_Head"
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
#End Kitty Licking 2

image Kitty_CUN_Anim_Licking3:
    #Animation for licking speed 3
#    contains:
#        #hair
#        "Kitty_BJ_HairBack"#"BJ_HairBack"
#        subpixel True
#        offset (-80,90)#490)
#        block: #2s total
#            ease .5 offset (-80,110) #bottom
#            ease .5 offset (-80,90)  #top -35)
#            repeat
    contains:
        #body 2
        "Kitty_BJ_Backdrop"
        pos (0,0)#(175,-110)
        subpixel True
        offset (0,0)#490)
        block:
            ease .4 offset (0,100) #bottom (30,90)
            ease .4 offset (0,90)  #top
            pause .2
            repeat
    contains:
        #head
        "Kitty_BJ_Head"#"BJ_Head"
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
#End Kitty Licking 3

#CUN Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Kitty_CUN_Launch(Line = Trigger):
    # The sequence to launch the Kitty CUN animations
    if renpy.showing("Kitty_CUN_Animation") and KittyX.Pose != "69":
        return
    elif renpy.showing("Kitty_69_CUN") and KittyX.Pose == "69":
        return

    if Player.Male == 1:
        call Kitty_BJ_Launch
        return

    call Girl_Hide(KittyX)
    if Line == "L" or Line == "cum":
        show Kitty_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1
            ease 1 zoom 2.5 offset (70,240) #(-90,140) offset (150,80)
        with dissolve
    else:
        show Kitty_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1 zoom 2.5 offset (70,240) #(-90,140)
        with dissolve

    if Taboo and Line == "L":
            # Kitty gets started. . .
            if len(Present) >= 2:
                if Present[0] != KittyX:
                        "[KittyX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                elif Present[1] != KittyX:
                        "[KittyX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
            else:
                        "[KittyX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
    $ Speed = 1
    if Line == "L":
            if not KittyX.Blow:
                "[KittyX.Name] нерешительно стягивает с вас штаны и касается своим ртом вашей киски."
            else:
                "[KittyX.Name] наклоняется и начинает лизать вашу киску."

    if Line != "cum":
        $ Trigger = "cun"

    show Kitty_Sprite:
        alpha 0
    if KittyX.Pose == "69":
            show Kitty_69_CUN zorder 150
    else:
            show Kitty_CUN_Animation zorder 150:
                pos (800,830)#(645,610)
    return

label Kitty_CUN_Reset: # The sequence to the Kitty animations from CUN to default
    if not renpy.showing("Kitty_CUN_Animation") and not renpy.showing("Kitty_69_CUN"):
        return
#    hide Kitty_CUN_Animation
    call Girl_Hide(KittyX)
    $ Speed = 0

    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder 150:
        zoom 2 offset (70,140) alpha 1
        pause .5
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
        alpha 1 zoom 1 offset (0,0)
    $ KittyX.FaceChange("sexy")
    return

#End Kitty Cunnilingus Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

image Kitty_Finger_Animation:
    # Core Animation for Fingering Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
        ConditionSwitch(                                                # backside of the hand
            "Speed == 1", "Kitty_Finger_1",
            "Speed >= 2", "Kitty_Finger_2",
            "True", "Kitty_Finger_0",
            ),
    anchor (0.5,0.5)#anchor (0.51, -1.3)
    offset (400,945)#700,1190
    zoom 0.8
    # end Core Animation for Fingering Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <

image Kitty_Finger_0:
    # Animation for Fingering Zero's pussy, static < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Kitty_Sprite"
            pos (390,-550)
            zoom 2.15
    contains:
            ConditionSwitch(
                "Player.Wet", "KittyBJFace/[KittyX.skin_image.skin_path]Kitty_Fingering_Wet.png",
                "True", "KittyBJFace/[KittyX.skin_image.skin_path]Kitty_Fingering_Under.png",
                )
            anchor (0.5,0.6)
            pos (20,40)

#            "Kitty_Finger_Under"
    contains:
            "Zero_Pussy"
    contains:
            "KittyBJFace/[KittyX.skin_image.skin_path]Kitty_Fingering_Over.png"
            anchor (0.5,0.6)
            pos (20,40)
#            "Kitty_Finger_Over"
    # end Animation for Fingering Zero's pussy, static < < < < < < < < < < < < < < < < < < < < < < < <

image Kitty_Finger_1:
    # Animation for Fingering Zero's pussy, slow < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Kitty_Sprite"
            pos (390,-550)
            zoom 2.15
            block:
                ease .5 ypos -540
                pause 0.25
                ease 1.0 ypos -550
                repeat
    contains:
            ConditionSwitch(
                "Player.Wet", "KittyBJFace/[KittyX.skin_image.skin_path]Kitty_Fingering_Wet.png",
                "True", "KittyBJFace/[KittyX.skin_image.skin_path]Kitty_Fingering_Under.png",
                )
            subpixel True
        #    xpos 10
            anchor (0.5,0.6)
            transform_anchor True
            pos (10,40)
            rotate -5
            block:
                ease .5 pos (10,85) rotate -15 #(-30,50)   Bottom
                pause 0.25
                ease 1.0 pos (10,40) rotate -5 #((20,-60) Top                 pause 0.1
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
            "KittyBJFace/[KittyX.skin_image.skin_path]Kitty_Fingering_Over.png"
#            "Kitty_Finger_Over"
            subpixel True
        #    xpos 10
            anchor (0.5,0.6)
            transform_anchor True
            pos (10,40)
            rotate -5
            block:
                ease .5 pos (10,85) rotate -15 #(-30,50)   Bottom
                pause 0.25
                ease 1.0 pos (10,40) rotate -5 #((20,-60) Top                 pause 0.1
                repeat
    # end Animation for Fingering Zero's pussy, slow < < < < < < < < < < < < < < < < < < < < < < < <

image Kitty_Finger_2:
    # Animation for Fingering Zero's pussy, fast < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Kitty_Sprite"
            pos (390,-550)
            zoom 2.15
            block:
                ease 0.15 ypos -540 #rotate 3   100
                pause 0.1
                ease 0.45 ypos -550 #rotate -3  40
                pause 0.1
                repeat
    contains:
            ConditionSwitch(
                "Player.Wet", "KittyBJFace/[KittyX.skin_image.skin_path]Kitty_Fingering_Wet.png",
                "True", "KittyBJFace/[KittyX.skin_image.skin_path]Kitty_Fingering_Under.png",
                )
            subpixel True
            anchor (0.5,0.6)
            transform_anchor True
            rotate -15
            pos (10,40)
            block:
                ease 0.15 ypos 85 #rotate 3   100
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
            "KittyBJFace/[KittyX.skin_image.skin_path]Kitty_Fingering_Over.png"
#            "Kitty_Finger_Over"
            anchor (0.5,0.6)
            subpixel True
            transform_anchor True
            rotate -15
            pos (10,40)
            block:
                ease 0.15 ypos 85 #rotate 3
                pause 0.1
                ease 0.45 ypos 40 #rotate -3 -50
                pause 0.1
                repeat
    # end Animation for Fingering Zero's pussy, fast < < < < < < < < < < < < < < < < < < < < < < < <

label Kitty_Finger_Launch(Line = Trigger):
    if renpy.showing("Kitty_Finger_Animation"):
        $ Trigger = "finger"
        return
    if Player.Male == 1:
        call Kitty_HJ_Launch
        return

    call Girl_Hide(KittyX)
    $ KittyX.Arms = 0
    $ KittyX.ArmPose = 1
    if not renpy.showing("Kitty_Sprite"):
        show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder 150:
            alpha 1 zoom 1.7 xpos 850 yoffset 200 #offset (-50,200)
        with dissolve
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 1.7 xpos 850 yoffset 200 #offset (-50,200)

    if Taboo and Line == "L":
        # Kitty gets started. . .
        if len(Present) >= 2:
            if Present[0] != KittyX:
                    "[KittyX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
            elif Present[1] != KittyX:
                    "[KittyX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
        else:
                    "[KittyX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
        if not KittyX.Hand and KittyX.Arms:
            "Когда вы стягиваете свои штаны, [KittyX.Name] снимает перчатки и нерешительно тянется к вашей киске. Затем она начинает грубо ласкать ее."
        else:
            "Затем она наклоняется и хватает ваш член."
    elif Line == "L":
        if not KittyX.Hand and KittyX.Arms:
            "Когда вы стягиваете свои штаны, [KittyX.Name] снимает перчатки и нерешительно тянется к вашей киске. Затем она начинает грубо ласкать ее."
        else:
            "[KittyX.Name] наклоняется и кладет руку вам на киску."
    else:
            "[KittyX.Name] наклоняется и кладет руку вам на киску."

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "finger"
    show Kitty_Sprite:
        alpha 0
    show Kitty_Finger_Animation at SpriteLoc(KittyX.SpriteLoc) zorder 150 with fade
    return

label Kitty_Finger_Reset: # The sequence to the Kitty animations from handjob to default
    if not renpy.showing("Kitty_Finger_Animation"):
        return
    $ Speed = 0
    hide Kitty_Finger_Animation
    with dissolve
    call Girl_Hide(KittyX)
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder 150:
        alpha 0 zoom 1.7  xpos 850 yoffset 200
    show Kitty_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 yoffset 50
        pause .5
        ease .5 zoom 1 xpos KittyX.SpriteLoc yoffset 0
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
        alpha 1 zoom 1 xpos KittyX.SpriteLoc yoffset 0
    return

# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////



# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

# Start Kitty 69 Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

image Kitty_69_Animation:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
                #Shows different upper body motion depending on events
#                "True", "Kitty_69_Anim1",
                "Speed == 2", "Kitty_69_Anim2",
                "Speed == 3", "Kitty_69_Anim3",
                "Speed == 4", "Kitty_69_Anim4",
                "Speed == 5", "Kitty_69_Anim5",
                "Speed == 6", "Kitty_69_Anim6",
                "Speed", "Kitty_69_Anim1",
                "True", "Kitty_69_Static",
                ),
        )
    align (0.6,0.0)
    pos (475,-800)#(475,-700)
    zoom 1.8#1/3

#Start Animations for Kitty's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Kitty 69 Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_69_Body:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Kitty_SexSprite
        (1120,840),

        (0,0), ConditionSwitch(
            #bra layer if up
            "not KittyX.Uptop", Null(),
            #if top's up
            "KittyX.Chest == 'bikini top'", "images/KittySex/Kitty_69_Chest_Bikini_Up.png",
            "KittyX.Chest == 'sports bra'", "images/KittySex/Kitty_69_Chest_Sports_Up.png",
            "KittyX.Chest == 'cami'", "images/KittySex/Kitty_69_Chest_Cami_Up.png",
            "KittyX.Chest == 'lace bra'", "images/KittySex/Kitty_69_Chest_Bra_Up.png",
            "KittyX.Chest == 'bra'", "images/KittySex/Kitty_69_Chest_Bra_Up.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #body
#            "KittyX.Arms", "images/KittySex/Kitty_69_BodyG.png",
            "True", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_69_Body.png",
            ),
#        (0,0), ConditionSwitch(
#            #Wet look
#            "KittyX.Water", "images/KittySex/Kitty_69_Water_Body.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #bra layer
            "KittyX.Uptop and KittyX.Chest == 'dress'", "images/KittySex/Kitty_69_Chest_Dress_Up.png",
            "KittyX.Uptop", Null(),
            #if top's up
            "KittyX.Chest == 'bikini top'", "images/KittySex/Kitty_69_Chest_Bikini.png",
            "KittyX.Chest == 'sports bra'", "images/KittySex/Kitty_69_Chest_Sports.png",
            "KittyX.Chest == 'cami'", "images/KittySex/Kitty_69_Chest_Cami.png",
            "KittyX.Chest == 'lace bra'", "images/KittySex/Kitty_69_Chest_Lace.png",
            "KittyX.Chest == 'bra'", "images/KittySex/Kitty_69_Chest_Bra.png",
            "KittyX.Chest == 'dress'", "images/KittySex/Kitty_69_Chest_Dress.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #shirt layer
#            "KittyX.Over == 'pink top' and KittyX.Uptop", "images/KittySex/Kitty_69_Over_Pink_Up.png",
            "KittyX.Over == 'jacket'", "images/KittySex/Kitty_69_Over_Jacket.png",
            "KittyX.Uptop", ConditionSwitch(
                    # ring pierce
                    "KittyX.Over == 'towel'", Null(),
                    "KittyX.Over == 'red shirt'", "images/KittySex/Kitty_69_Over_Red_Up.png",
                    "KittyX.Over == 'pink top'", "images/KittySex/Kitty_69_Over_Pink_Up.png",
                    "True", Null(),
                    ),
            "KittyX.Over == 'towel'", "images/KittySex/Kitty_69_Over_Towel.png",
            "KittyX.Over == 'red shirt'", "images/KittySex/Kitty_69_Over_Red.png",
            "KittyX.Over == 'pink top'", "images/KittySex/Kitty_69_Over_Pink.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #piercings
            "not KittyX.Pierce", Null(),
            "KittyX.Pierce == 'ring'", ConditionSwitch(
                    # ring pierce
                    "KittyX.Uptop", "images/KittySex/Kitty_69_Pierce_Tits_R.png",

                    "KittyX.Over == 'pink top'", "images/KittySex/Kitty_69_Pierce_Tits_R_Pink.png",
                    "KittyX.Over == 'red shirt'", "images/KittySex/Kitty_69_Pierce_Tits_R_Red.png",
                    "KittyX.Over == 'towel'", "images/KittySex/Kitty_69_Pierce_Tits_R_Towel.png",

                    "KittyX.Chest == 'sports bra'", "images/KittySex/Kitty_69_Pierce_Tits_R_Sports.png",
                    "KittyX.Chest == 'bikini top'", "images/KittySex/Kitty_69_Pierce_Tits_R_Bikini.png",
                    "KittyX.Chest == 'cami'", "images/KittySex/Kitty_69_Pierce_Tits_R_Cami.png",
                    "KittyX.Chest == 'dress'", "images/KittySex/Kitty_69_Pierce_Tits_R_Pink.png",
                    "KittyX.Chest == 'lace bra'", "images/KittySex/Kitty_69_Pierce_Tits_R_Lace.png",
                    "KittyX.Chest", "images/KittySex/Kitty_69_Pierce_Tits_R_Bra.png",

                    "True", "images/KittySex/Kitty_69_Pierce_Tits_R.png",
                    ),
            "KittyX.Uptop", "images/KittySex/Kitty_69_Pierce_Tits_B.png",

            "KittyX.Over == 'pink top'", "images/KittySex/Kitty_69_Pierce_Tits_B_Pink.png",
            "KittyX.Over == 'red shirt'", "images/KittySex/Kitty_69_Pierce_Tits_B_Red.png",
            "KittyX.Over == 'towel'", "images/KittySex/Kitty_69_Pierce_Tits_B_Towel.png",

            "KittyX.Chest == 'sports bra'", "images/KittySex/Kitty_69_Pierce_Tits_B_Sports.png",
            "KittyX.Chest == 'bikini top'", "images/KittySex/Kitty_69_Pierce_Tits_B_Bikini.png",
            "KittyX.Chest == 'cami'", "images/KittySex/Kitty_69_Pierce_Tits_B_Cami.png",
            "KittyX.Chest == 'dress'", "images/KittySex/Kitty_69_Pierce_Tits_B_Pink.png",
#            "KittyX.Chest == 'lace bra'", "images/KittySex/Kitty_69_Pierce_Tits_B_Bra.png",
            "KittyX.Chest", "images/KittySex/Kitty_69_Pierce_Tits_B_Bra.png",

            "True", "images/KittySex/Kitty_69_Pierce_Tits_B.png",
            ),
#        (0,0), ConditionSwitch(
#            #piercings
#            "not KittyX.Pierce", Null(),
#            "KittyX.Uptop", Null(),
#            "KittyX.Pierce == 'ring'", ConditionSwitch(
#                    # ring pierce
#                    "KittyX.Over == 'mesh top'", "images/KittySex/Kitty_69_Pierce_Tits_R_Mesh.png",
#                    "KittyX.Over == 'nighty'", "images/KittySex/Kitty_69_Pierce_Tits_R_Nighty.png",
#                    "True", Null(),
#                    ),
#            "KittyX.Over == 'mesh top'", "images/KittySex/Kitty_69_Pierce_Tits_B_Mesh.png",
#            "KittyX.Over == 'nighty'", "images/KittySex/Kitty_69_Pierce_Tits_B_Nighty.png",
#            "True", Null(),
#            ),

        (0,0),ConditionSwitch(
            #Outside Spunk
            "'tits' in KittyX.Spunk and Player.Male", "images/KittySex/Kitty_69_Spunk_Tits.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'belly' in KittyX.Spunk and Player.Male", "images/KittySex/Kitty_69_Spunk_Belly.png",
            "True", Null(),
            ),
#        (0,0), "images/KittySex/Kitty_Sex_HeadRef.png",
        )
    zoom .9#.8
    offset (70,80)#(145,150)#(250,210)#(175,175)
#    yoffset -163
# End Kitty 69 Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Kitty 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_69_Head:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Kitty_SexSprite
        (1120,840),
        (0,0), ConditionSwitch(
            #tongue
            "renpy.showing('Kitty_69_CUN') and Speed != 3", "images/KittySex/Kitty_69_Tongue.png",
            "Speed == 1", "images/KittySex/Kitty_69_Tongue.png",
            "True", Null(),
            ),
        (0,0), "images/KittySex/[KittyX.skin_image.skin_path]Kitty_69_Head.png",
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'mouth' in KittyX.Spunk and Player.Male", "images/KittySex/Kitty_69_Spunk_Mouth.png",
            "('mouth' in KittyX.Spunk or 'chin' in KittyX.Spunk) and not Player.Male", "images/KittySex/Kitty_69_WetFace.png",
            "True", Null(),
            ),

        (0,0),ConditionSwitch(
            #Outside Spunk
            "'chin' in KittyX.Spunk and Player.Male", "images/KittySex/Kitty_69_Spunk_Chin.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Hair over
#            "Speed == 1 and Player.Male", Null(),
#            "Speed == 4 and Player.Male", Null(),
#            "Speed == 6 and Player.Male", Null(),
#            "KittyX.Water or KittyX.Hair == 'wet'", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_69_Hair_Wet.png",
#            "not Player.Male and ('hair' in KittyX.Spunk or 'facial' in KittyX.Spunk)",Recolor("Kitty", "Hair", "images/KittySex/Kitty_69_Hair_Pony.png"),

##            "KittyX.Hair == 'long'", "images/KittySex/Kitty_69_Hair_Long_Over.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #Hair over
            "KittyX.Hair == 'evo' and not KittyX.Water",Recolor("Kitty", "Hair", "images/KittySex/Kitty_69_Hair_Pony.png"),
            "Speed == 1 and Player.Male", Null(),
            "Speed == 4 and Player.Male", Null(),
            "Speed == 6 and Player.Male", Null(),
            "KittyX.Water or KittyX.Hair == 'wet'", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_69_Hair_Wet.png",
            "not Player.Male and ('hair' in KittyX.Spunk or 'facial' in KittyX.Spunk)","images/KittySex/[KittyX.skin_image.skin_path]Kitty_69_Hair_Wet.png",

            "KittyX.Hair == 'long'", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_69_Hair_Long.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Pontytail
            "Speed == 1 and Player.Male", Null(),
            "KittyX.Hair == 'evo' and not KittyX.Water",Recolor("Kitty", "Hair", "images/KittySex/Kitty_69_Hair_Pony_Tail.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #neck over
            "(Speed == 0 or Speed == 2 or Speed == 3 or Speed == 5) and Player.Male", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_69_Neck.png",
            "not Player.Male", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_69_Neck.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #collar
#            "KittyX.Neck", "images/KittySex/Kitty_69_Collar.png",
#            "True", Null(),
#            ),
        )
    zoom .8
    offset (145,150)
#    offset (0,0)#(175,135)#(175,175)
#    yoffset -163
# End Kitty 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Kitty 69 Pose Hair Over / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_69_HairOver:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Kitty_SexSprite
        (1120,840),
        (0,0), "images/KittySex/[KittyX.skin_image.skin_path]Kitty_69_Neck.png",
        (0,0), ConditionSwitch(
            #Hair over
            "KittyX.Water or KittyX.Hair == 'wet'", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_69_Hair_Wet.png",
            "not Player.Male and ('hair' in KittyX.Spunk or 'facial' in KittyX.Spunk)","images/KittySex/[KittyX.skin_image.skin_path]Kitty_69_Hair_Wet.png",

            "KittyX.Hair == 'long'", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_69_Hair_Long.png",
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #Hair over
##            "renpy.showing('Kitty_TJ_Animation')", Null(),
##            "KittyX.Hair == 'blonde'", "images/KittySex/Kitty_69_Hair_Blonde_Lick.png",
##            "KittyX.Hair == 'long' or KittyX.Hair == 'wetlong'", "images/KittySex/Kitty_69_Hair_Long_Lick.png",
#            "True", "images/KittySex/Kitty_69_Hair_Over.png",
#            ),
#        (0,0), ConditionSwitch(
#            #collar
#            "KittyX.Neck", "images/KittySex/Kitty_69_Collar.png",     # == 'spiked collar'
#            "True", Null(),
#            ),
        )
    zoom .8
    offset (145,150)
#    offset (0,0)#(175,135)#(180,100)
#    yoffset -163
# End Kitty 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Kitty 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_69_HairBack:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Kitty_SexSprite
        (1120,840),
#        (0,0), "images/KittySex/[KittyX.skin_image.skin_path]Kitty_69_Head.png",
        (0,0), ConditionSwitch(
            #Hair over
            "KittyX.Hair == 'evo' and not KittyX.Water",Recolor("Kitty", "Hair", "images/KittySex/Kitty_69_Hair_Pony_Under.png"),
#            "Speed == 1 and Player.Male", Null(),
#            "Speed == 4 and Player.Male", Null(),
#            "Speed == 6 and Player.Male", Null(),
            "KittyX.Water or KittyX.Hair == 'wet'", Recolor("Kitty", "Hair", "images/KittySex/Kitty_69_Hair_Wet_Under.png"),
            "not Player.Male and ('hair' in KittyX.Spunk or 'facial' in KittyX.Spunk)",Recolor("Kitty", "Hair", "images/KittySex/Kitty_69_Hair_Wet_Under.png"),

            "KittyX.Hair == 'long'", Recolor("Kitty", "Hair", "images/KittySex/Kitty_69_Hair_Long_Under.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hair over
#            "renpy.showing('Kitty_TJ_Animation')", Null(),
#            "KittyX.Hair == 'blonde'", "images/KittySex/Kitty_69_Hair_Blonde_Under.png",
#            "KittyX.Hair == 'long' or KittyX.Hair == 'wetlong'", Recolor("Kitty", "Hair", "images/KittySex/Kitty_69_Hair_Long_Under.png"),
#            "KittyX.Hair == 'wet' or KittyX.Hair == 'wetlong' or KittyX.Water", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_69_Hair_Long.png",
#            "not Player.Male and 'facial' in KittyX.Spunk","images/KittySex/Kitty_Sprite_Hair_Wet.png",
            "True", Null(),#"images/KittySex/Kitty_69_Hair_Under.png",
            ),
        )
    zoom .8
    offset (145,150)#(175,135)#(175,175)
#    yoffset -163
# End Kitty 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#image Kitty_Sex_Legs = LiveComposite(
image Kitty_69_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Kitty_SexSprite
        (1120,840),
#        (0,0), "images/KittySex/[KittyX.skin_image.skin_path]Kitty_69_Hips.png",
#        (0,0), ConditionSwitch(                                                                                 #Legs Layer
#            "KittyX.Legs == 'dress' and KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Legs_Dress_Back_Up.png"),
#            "KittyX.Legs == 'dress'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Legs_Dress_Back.png"),
#            "KittyX.Legs == 'blue skirt'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Skirt_Back.png"),
#            "True", Null(),
#            ),
        (0,0), "images/KittySex/[KittyX.skin_image.skin_path]Kitty_69_Legs.png",                                                         #Legs Base
#        (0,0), ConditionSwitch(                                                                                 #Wet look
#            "KittyX.Water", "images/KittySex/Kitty_Sex_Water_Legs.png",
#            "True", Null(),
#            ),

        (0,0), "Kitty_69_Anus",                                                                          #Anus Composite

        (0,0), "Kitty_69_Pussy",                                                                         #Pussy Composite

        (0,0), ConditionSwitch(                                                                                 #Panties if up
            "KittyX.PantiesDown", Null(),
            "KittyX.Panties == 'green panties' and KittyX.Wet", "images/KittySex/Kitty_69_Panties_Green_Wet.png",
            "KittyX.Panties == 'green panties'", "images/KittySex/Kitty_69_Panties_Green.png",
#            "KittyX.Panties == 'lace panties' and KittyX.Wet", "images/KittySex/Kitty_69_Panties_Lace_Wet.png",
            "KittyX.Panties == 'lace panties'", "images/KittySex/Kitty_69_Panties_Lace.png",
#            "KittyX.Panties == 'bikini bottoms' and KittyX.Wet", "images/KittySex/Kitty_69_Panties_Bikini_Wet.png",
            "KittyX.Panties == 'bikini bottoms'", "images/KittySex/Kitty_69_Panties_Bikini.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #hose layer
            "KittyX.Hose == 'stockings and garterbelt'", "images/KittySex/Kitty_69_Hose_StockingsGarter.png",
            "KittyX.Hose == 'garterbelt'", "images/KittySex/Kitty_69_Hose_Garter.png",
            "KittyX.Hose == 'stockings'", "images/KittySex/Kitty_69_Hose_Stockings.png",
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "KittyX.Hose == 'pantyhose'", "images/KittySex/Kitty_69_Hose_Pantyhose.png",
            "KittyX.Hose == 'ripped pantyhose'", "images/KittySex/Kitty_69_Hose_Pantyhose_Holed.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(                                                                                 #Over Layer
            "KittyX.Over == 'towel' and not KittyX.Uptop", "images/KittySex/Kitty_69_Legs_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #Legs Layer
#            "KittyX.Legs == 'dress' and KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Legs_Dress_Up.png"),
            "KittyX.Legs == 'dress'", "images/KittySex/Kitty_69_Legs_Dress.png",
#            "KittyX.Legs == 'blue skirt'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Skirt.png"),
            "KittyX.Upskirt", Null(),
            "KittyX.Legs == 'capris' and KittyX.Wet > 1", "images/KittySex/Kitty_69_Legs_Blue_Wet.png",
            "KittyX.Legs == 'capris'", "images/KittySex/Kitty_69_Legs_Blue.png",
            "KittyX.Legs == 'black jeans' and KittyX.Wet > 1", "images/KittySex/Kitty_69_Legs_Black_Wet.png",
            "KittyX.Legs == 'black jeans'", "images/KittySex/Kitty_69_Legs_Black.png",
            "KittyX.Legs == 'shorts' and KittyX.Wet > 1", "images/KittySex/Kitty_69_Legs_Shorts_Wet.png",
            "KittyX.Legs == 'shorts'", "images/KittySex/Kitty_69_Legs_Shorts.png",
            "KittyX.Legs == 'yoga pants' and KittyX.Wet > 1", "images/KittySex/Kitty_69_Legs_Yoga_Wet.png",
            "KittyX.Legs == 'yoga pants'", "images/KittySex/Kitty_69_Legs_Yoga.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Piercings over pants and pantyhose
            "not KittyX.Pierce", Null(),
            "KittyX.Pierce == 'ring'",ConditionSwitch(
                    #If she has panties down. . .
#                    "Player.Sprite and Player.Cock == 'in'", "images/KittySex/Kitty_Sex_Pussy_RingF.png",

                    "KittyX.Legs and KittyX.Legs != 'dress' and not KittyX.Upskirt", "images/KittySex/Kitty_69_Pierce_Pussy_R_Clothed.png",

                    "KittyX.PantiesDown", "images/KittySex/Kitty_Sex_Pussy_Ring.png",
                    "KittyX.Panties == 'lace panties'", "images/KittySex/Kitty_69_Pierce_Pussy_R_Lace.png",
                    "KittyX.Panties", "images/KittySex/Kitty_69_Pierce_Pussy_R_Clothed.png",

                    "KittyX.Hose == 'pantyhose' and not (KittyX.Panties and KittyX.PantiesDown)", "images/KittySex/Kitty_69_Pierce_Pussy_R_Lace.png",

                    "True", "images/KittySex/Kitty_Sex_Pussy_Ring.png",
                    ),
            #else, it's barbell
#            "Player.Sprite and Player.Cock == 'in'", "images/KittySex/Kitty_Sex_Pussy_BarbellF.png",

            "KittyX.Legs and KittyX.Legs != 'dress' and not KittyX.Upskirt", "images/KittySex/Kitty_69_Pierce_Pussy_B_Clothed.png",

            "KittyX.PantiesDown", "images/KittySex/Kitty_Sex_Pussy_Barbell.png",
            "KittyX.Panties == 'lace panties'", "images/KittySex/Kitty_69_Pierce_Pussy_B_Lace.png",
            "KittyX.Panties", "images/KittySex/Kitty_69_Pierce_Pussy_B_Clothed.png",

            "KittyX.Hose == 'pantyhose' and not (KittyX.Panties and KittyX.PantiesDown)", "images/KittySex/Kitty_69_Pierce_Pussy_B_Lace.png",

            "True", "images/KittySex/Kitty_Sex_Pussy_Barbell.png",
            ),

#        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
#            "'belly' in KittyX.Spunk and Player.Male", "images/KittySex/Kitty_Sex_Spunk_Pelvis.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer
#            "not Player.Sprite or Player.Cock != 'out'", Null(),
#            "Speed >= 2", "Kitty_Hotdog_Zero_Anim2",
#            "Speed", "Kitty_Hotdog_Zero_Anim1",
#            "True", "Kitty_Hotdog_Zero_Anim0",
#            ),

        (0,0), ConditionSwitch(
            #pussy licking animation
#            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy' or Trigger2 == 'lick pussy'", "Kitty_69_Lick_Pussy",
            "Trigger == 'lick ass'", "Kitty_69_Lick_Ass",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy fondling animation
            "KittyX.Offhand == 'fondle pussy' and KittyX.Lust > 60 and not (Player.Sprite)",  At("KittyFingerHand", GirlFingerPussyX()), #"Betsy_Sex_Mast2",
            "KittyX.Offhand == 'fondle pussy' or Trigger2 == 'lick ass'", At("KittyMastHand", GirlGropePussyX()), #"Betsy_Sex_Mast",
#            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Kitty_Sex_Fondle_Pussy",
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #pussy licking animation
##            "Player.Sprite", Null(),
#            "Trigger == 'lick pussy'", "Kitty_Sex_Lick_Pussy",
#            "Trigger == 'lick ass'", "Kitty_Sex_Lick_Ass",
#            "KittyX.Offhand == 'fondle pussy' and KittyX.Lust > 60", At("KittyFingerHand", GirlFingerPussyX()),
#            "KittyX.Offhand == 'fondle pussy'", At("KittyMastHand", GirlGropePussyX()),
#            "True", Null()
#            ),
#        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer
#            "not Player.Sprite or Player.Cock != 'foot'", Null(),
#            "Speed >= 2", "Kitty_Footcock_Zero_Anim2",
#            "Speed", "Kitty_Footcock_Zero_Anim1",
#            "True", "Kitty_Footcock_Static",
#            ),
#        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer
#            "not Player.Sprite or Player.Cock != 'foot'", Null(),
#            "Speed >= 2", At("Kitty_Footcock", Kitty_Footcock_Zero_Anim2A()),
#            "Speed", At("Kitty_Footcock", Kitty_Footcock_Zero_Anim1A()),
#            "True", At("Kitty_Footcock", Kitty_Footcock_StaticA()),
#            ),
#        (0,0), ConditionSwitch(                                                                                 #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "renpy.showing('Anal_Plug_In_Sex') or renpy.showing('Anal_Plug_Out_Sex')", AlphaMask("Kitty_69_Feet", "images/KittySex/Kitty_69_FeetMask.png"),
            "not Speed", "Kitty_69_Feet",
            "Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Kitty_69_Feet", "images/KittySex/Kitty_69_FeetMask.png"),
            "True", "Kitty_69_Feet",
            ),
        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            "KittyX.Upskirt", Null(),
            "KittyX.Legs == 'dress'", "images/KittySex/Kitty_69_Feet_Dress.png",
            "True", Null(),
            ),
        )

image Kitty_69_Feet = LiveComposite(
        #the lower legs used in the sex pose, referenced by Kitty_Sex_Legs
        (1120,840),
#        (0,0), "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Feet.png",                                                         #Legs Base
#        (0,0), ConditionSwitch(                                                                                 #Wet look
#            "KittyX.Water", "images/KittySex/Kitty_Sex_Water_Feet.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #hose layer
            "KittyX.Legs and not KittyX.Upskirt and KittyX.Legs != 'blue skirt' and KittyX.Legs != 'shorts'",ConditionSwitch(
                    #If she has pants on, I need alternate kneesocks to not clip through knees
                    "KittyX.Hose == 'stockings and garterbelt'", "images/KittySex/Kitty_69_Feet_Stockings.png",
                    "KittyX.Hose == 'stockings'", "images/KittySex/Kitty_69_Feet_Stockings.png",
                    "KittyX.Hose == 'knee stockings'", "images/KittySex/Kitty_69_Feet_Kneesocks.png",
                    "KittyX.Panties and KittyX.PantiesDown", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_69_Feet.png",
                    "KittyX.Hose == 'pantyhose'", "images/KittySex/Kitty_69_Feet_Stockings.png",
                    "KittyX.Hose == 'ripped pantyhose'", "images/KittySex/Kitty_69_Feet_Stockings_Holed.png",
                    "True", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_69_Feet.png",
                    ),
#            "KittyX.Legs and (not KittyX.Upskirt and KittyX.Legs != 'blue skirt' and KittyX.Legs != 'shorts') and KittyX.Hose == 'stockings and garterbelt'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png"),
#            "KittyX.Legs and (not KittyX.Upskirt and KittyX.Legs != 'blue skirt' and KittyX.Legs != 'blue skirt') and KittyX.Hose == 'stockings'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png"),
#            "KittyX.Legs and (not KittyX.Upskirt and KittyX.Legs != 'blue skirt' and KittyX.Legs != 'blue skirt') and KittyX.Hose == 'knee stockings'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png"),
            "KittyX.Hose == 'stockings' or KittyX.Hose == 'stockings and garterbelt'", "images/KittySex/Kitty_69_Feet_Stockings.png",
            "KittyX.Hose == 'knee stockings'", "images/KittySex/Kitty_69_Feet_Kneesocks.png",
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "KittyX.Hose == 'pantyhose'", "images/KittySex/Kitty_69_Feet_Stockings.png",
#            "KittyX.Legs and (not KittyX.Upskirt and KittyX.Legs != 'blue skirt' and KittyX.Legs != 'blue skirt') and KittyX.Hose == 'ripped pantyhose'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_RippedPantyhose_FeetP.png"),
            "KittyX.Hose == 'ripped pantyhose'", "images/KittySex/Kitty_69_Feet_Stockings_Holed.png",
            "True", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_69_Feet.png",
            ),

        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            "KittyX.Upskirt", Null(),
            "KittyX.Legs == 'dress'", "images/KittySex/Kitty_69_Feet_Dress.png",
            "KittyX.Legs == 'capris'", "images/KittySex/Kitty_69_Feet_Blue.png",
            "KittyX.Legs == 'black jeans'", "images/KittySex/Kitty_69_Feet_Black.png",
            "KittyX.Legs == 'yoga pants'", "images/KittySex/Kitty_69_Feet_Yoga.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk
            "'feet' in KittyX.Spunk", "images/KittySex/Kitty_Sex_Spunk_Feet.png",
            "True", Null(),
            ),
        )


# Start Kitty 69 Pose Pussy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_69_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).

    contains:
            # The background plate of her pussy
            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pussy_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed", "Kitty_Sex_Heading_Pussy",
#                "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/KittySex/Kitty_69_Pussy_Open.png",
                "KittyX.Offhand == 'fondle pussy' and KittyX.Lust > 60", "images/KittySex/Kitty_69_Pussy_Open.png",
                "True", "images/KittySex/Kitty_69_Pussy.png",
                )
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "not KittyX.Wet", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/JubesSex/Jubes_Sex_WetPussy_F.png",
                "True", "images/BetsySex/Betsy_69_Water_Pussy.png",
                )
    contains:
            # pubes
            ConditionSwitch(
                "not KittyX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", Recolor("Kitty", "Pubes", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pubes_Fucking.png"),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 1", Recolor("Kitty", "Pubes", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pubes_Fucking.png"),
#                "Player.Sprite and Player.Cock == 'in'", Recolor("Kitty", "Pubes", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pubes_Open.png"),
#                "Player.Sprite and Player.Cock == 'out'", Recolor("Kitty", "Pubes", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pubes_Open.png"),
                "Trigger == 'lick pussy'", Recolor("Kitty", "Pubes", "images/KittySex/Kitty_69_Pubes_Open.png"),
                "KittyX.Offhand == 'fondle pussy' and KittyX.Lust > 60", Recolor("Kitty", "Pubes", "images/KittySex/Kitty_69_Pubes_Open.png"),
                "True", Recolor("Kitty", "Pubes", "images/KittySex/Kitty_69_Pubes.png"),
                )
    contains:
            #Wet
            ConditionSwitch(
                "not KittyX.Wet", Null(),
                "(KittyX.Legs == 'yoga pants' or KittyX.Legs == 'shorts') and not KittyX.Upskirt", Null(),
                "KittyX.Panties and not KittyX.PantiesDown", Null(),
#                "True", "Spunk_Drip_69",
                "True", AlphaMask("Wet_Drip_69","images/KittySex/Kitty_69_Mask_Pussy.png"),
                )
            offset (10,0)
    contains:
            #Spunk
            ConditionSwitch(
                "'in' not in KittyX.Spunk or not Player.Male", Null(),
                "(KittyX.Legs == 'yoga pants' or KittyX.Legs == 'shorts') and not KittyX.Upskirt", Null(),
                "KittyX.Panties and not KittyX.PantiesDown", Null(),
#                "True", "Spunk_Drip_69",
                "True", AlphaMask("Spunk_Drip_69","images/KittySex/Kitty_69_Mask_Pussy.png"),
                )
            offset (10,0)

    contains:
            ConditionSwitch(
                #Outside Spunk
#                "'in' in KittyX.Spunk and Player.Sprite and Player.Cock == 'in' and Speed and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_PussyF.png",
                "'in' in KittyX.Spunk and Player.Male", "images/BetsySex/Betsy_69_Spunk_Pussy.png",
                "True", Null(),
                )
#            offset (0,-15)
#    contains:
#            #Spunk under penis
#            ConditionSwitch(
#                "'in' in KittyX.Spunk", "images/KittySex/Kitty_Sex_Spunk_Puss_Under.png",
#                "True", Null(),
#                )
#    contains:
#            #hose layer
#            ConditionSwitch(
#                "KittyX.Panties and KittyX.PantiesDown", Null(),
#                "KittyX.Hose == 'ripped pantyhose' and ShowFeet", "images/KittySex/Kitty_Sex_Hose_Pantyhose_Holed.png",
#                "KittyX.Hose == 'ripped pantyhose'", "images/KittySex/Kitty_Sex_Hose_Pantyhose_Holed.png",
#                "True", Null(),
#                ),
#    contains:
#            # The animation of Zero's moving penis, masked by her pussy shape
#            ConditionSwitch(
##                "not Player.Sprite", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 3", AlphaMask("Kitty_Sex_Fucking_Zero_Anim3", "Kitty_Sex_Fucking_Mask"),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", AlphaMask("Kitty_Sex_Fucking_Zero_Anim2", "Kitty_Sex_Fucking_Mask"),
#                "Player.Sprite and Player.Cock == 'in' and Speed == 1", AlphaMask("Kitty_Sex_Fucking_Zero_Anim1", "Kitty_Sex_Heading_Mask"),
#                "Player.Sprite and Player.Cock == 'in'", "Kitty_Sex_Fucking_Zero_Anim0",
#                "True", Null(),
#                )
#    contains:
#            #Piercings
#            ConditionSwitch(
#                "KittyX.Pierce == 'barbell' and Player.Sprite and Player.Cock == 'in' and Speed", "images/KittySex/Kitty_Sex_Pierce_Pussy_BarbellF.png",
#                "KittyX.Pierce == 'ring' and Player.Sprite and Player.Cock == 'in' and Speed", "images/KittySex/Kitty_Sex_Pierce_Pussy_RingF.png",
#                "KittyX.Pierce == 'barbell'", "images/KittySex/Kitty_Sex_Pierce_Pussy_Barbell.png",
#                "KittyX.Pierce == 'ring'", "images/KittySex/Kitty_Sex_Pierce_Pussy_Ring.png",
#                "True", Null(),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed == 1", "Kitty_Pussy_Spunk_Heading",
#                "True", Null(),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "Speed == 1", Null(),
#                "'in' not in KittyX.Spunk or not Player.Sprite or Player.Cock != 'in' or not Speed or not Player.Male", Null(),
##                "Speed <= 1", Null(), #"Kitty_Pussy_Spunk_Heading",
#                "True", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
#                )

    #End Kitty Pussy composite


image Kitty_69_Lick_Pussy:
        "Lick_AnimF"
        zoom 0.6
        rotate 180
        offset (515,520)#(535,500
image Kitty_69_Lick_Ass:
        "Lick_AnimF"
        zoom 0.6
        rotate 180
        offset (515,580)#(535,580)

image Kitty_Sex_Fondle_Pussy:
        "GropePussy_Kitty"
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

image Kitty_69_Fondle_Pussy:
        "GropePussy_Kitty"
        xzoom -1.5
        yzoom 1.5
        offset(-710,-300) #(-890,-300)
#        block:
#            ease 1 offset(-1000,0) #(535,500)
#            ease 1 offset(-1000,-1000) #(535,500)
#            ease 1 offset(0,-1000) #(535,500)
#            ease 1 offset(0,0) #(535,500)
#            repeat

image Kitty_69_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/JubesSex/Jubes_Sex_Anal.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/JubesSex/Jubes_Sex_Anal.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/KittySex/Kitty_Sex_Anus.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/KittySex/Kitty_Sex_Anus.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed", "Kitty_Sex_Anal_Heading",
#            "Player.Sprite and Player.Cock == 'anal'", "Kitty_Sex_Anal_Tip",
            "KittyX.Plug", "images/PlugBase_Sex.png",
            "KittyX.Loose > 2", "Kitty_Gape_Anal_Sex",
#            "KittyX.Loose", "images/KittySex/Kitty_Sex_Hole_Loose.png",
#            "True", "images/KittySex/Kitty_Sex_Hole_Tight.png",
            "True", Null(),
            )
    contains:
            #Spunk under penis
            ConditionSwitch(
                "'anal' not in KittyX.Spunk or not Player.Male", Null(),
#                "Player.Sprite and Player.Cock != 'anal' and Speed >= 1", "images/KittySex/Kitty_Sex_Spunk_Anal_Under.png",
#                "Player.Sprite and Player.Cock == 'anal' and Speed == 1", "Kitty_Sex_Anal_Spunk_Heading_Under",
                "True", "images/BetsySex/Betsy_69_Spunk_Ass.png",
                )
            offset (-8,-5)
#    contains:
#            # The animation of Zero's moving penis, masked by her anus shape
#            ConditionSwitch(
#                "not Player.Sprite or Player.Cock != 'anal'", Null(),
#                "Speed >= 3",  AlphaMask("Kitty_Sex_Anal_Zero_Anim3", "Kitty_Sex_Anal_MaskF"),
#                "Speed >= 2", AlphaMask("Kitty_Sex_Anal_Zero_Anim2", "Kitty_Sex_Anal_MaskF"),
#                "Speed", AlphaMask("Kitty_Sex_Anal_Zero_Anim1", "Kitty_Sex_Anal_Mask"),
#                "True", AlphaMask("Kitty_Sex_Anal_Zero_Anim0", "Kitty_Sex_Anal_Mask"),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "'anal' not in KittyX.Spunk or not Player.Sprite or Player.Cock != 'anal' or not Speed or not Player.Male", Null(),
#                "Speed == 1", "Kitty_Sex_Anal_Spunk_Heading_Over",
#                "True", "Kitty_Sex_Anal_Spunk",
#                )


#Start Animations for Kitty's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_69_Static:
        #this is the animation for Kitty's hairback during 69, Speed 0 (static)
        contains:
            subpixel True
            "Kitty_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-125) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-130) #top -70
#                pause .5
                ease 1.25 pos (0,-125) #bottom -65
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
        #this is the animation for Kitty's head during 69, Speed 0 (static)
        contains:
            subpixel True
            "Kitty_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-125) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-130) #top -70
#                pause .5
                ease 1.25 pos (0,-125) #bottom -65
                repeat
        #this is the animation for Kitty's upper body during 69, Speed 0 (static)
#        contains:
#            "Kitty_69_Tits"
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
            "Kitty_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,-70) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,-80) #top -20
                pause .25
                ease 1 pos (0,-70) #bottom -10
                repeat
        #this is the animation for Kitty's lower body during 69, Speed 0 (static)
        contains:
            "Kitty_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat

#Start Animations for Kitty's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_69_Anim1:
        #this is the animation for Kitty's hairback during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Kitty_69_HairBack"
            rotate 190
            pos (70,-30) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 ypos -120 #top (10,-60)
                pause .7#.75
                ease 2.6 ypos -30 #bottom (50,40)
                pause .45# 0
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 rotate 180
                pause .5#1.50
                ease 2 rotate 190 #2.25
                pause 1.25#1.50
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 xpos 10 #top (10,-60)
                pause .5#.75
                ease 2.4 xpos 70 #bottom (50,40)
                pause .85# 0
                repeat

#            zoom .75
#            offset (180,50)#(180,100)
#            pos (50,45) #X less is left, Y less is up
#            parallel:
#                #Total time, 5 seconds
#                pause .5
#                easein .75 pos (20,-60) #top(10,-30)
#                pause .75#1.50
#                ease 2.5 pos (70,35) #bottom(45,55)
#                pause .5# 0
#                repeat
#            parallel:
#                #Total time, 5 seconds
#                pause .5
#                easein .75 rotate 180
#                pause 1.50
#                ease 2.25 rotate 210
#                repeat
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
        #this is the animation for Kitty's head during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Kitty_69_Head"
            rotate 220
#            zoom .75
#            offset (180,50)#(180,100)
            pos (125,-10) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 ypos -105 #top (35,-65)
                pause .75#1.25
                ease 2.5 ypos -10 #bottom (85,50)
                pause .5#1.25
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .50 rotate 200
                pause 1.5
                ease 1.25 rotate 220
                pause 1.25
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 xpos 55 #top (35,-65)
                pause .75#1.25
                ease 2.0 xpos 125 #bottom (85,50)
                pause 1 #1.25
                repeat
        #this is the animation for Kitty's upper body during 69, Speed 1 (licking)
        contains:
            #ponytail
            subpixel True
            ConditionSwitch(
                "KittyX.Hair == 'evo' and not KittyX.Water",Recolor("Kitty", "Hair", "images/KittySex/Kitty_69_Hair_Pony_Tail.png"),
                "True", Null(),
                )
            rotate 180
#            zoom .75
#            offset (10,0)
#            offset (180,50)#(180,100)
            pos (70,-30) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .55
                easein .75 ypos -120 #top (10,-60)
                pause .65#.75
                ease 2.6 ypos -50 #bottom (50,40)
                pause .45# 0
                repeat
#            parallel:
#                #Total time, 5 seconds
#                pause .5
#                easein .75 rotate 180
#                pause .5#1.50
#                ease 2 rotate 180 #2.25
#                pause 1.25#1.50
#                repeat
            parallel:
                #Total time, 5 seconds
                pause 1.75#4.15#.75
                ease .3 rotate 182 #2.25

                pause 2.0#4.15#.75

                ease .35 rotate 180 #2.25
                ease .3 rotate 181 #2.25
                ease .3 rotate 180 #2.25
#                pause .1#1.50
                repeat
            parallel:
                #Total time, 5 seconds
                pause .55
                easein .75 xpos -10 #top (10,-60)
                pause .25#.75
                ease 2.6 xpos 25 #bottom (70,40)
                pause .85# 0
                repeat

        contains:
            subpixel True
            "Kitty_69_HairOver"
            rotate 180
#            zoom .75
#            offset (10,0)
#            offset (180,50)#(180,100)
            pos (70,-30) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .55
                easein .75 ypos -100 #top (10,-60)
                pause .65#.75
                ease 2.6 ypos -30 #bottom (50,40)
                pause .45# 0
                repeat
#            parallel:
#                #Total time, 5 seconds
#                pause .5
#                easein .75 rotate 180
#                pause .5#1.50
#                ease 2 rotate 180 #2.25
#                pause 1.25#1.50
#                repeat
            parallel:
                #Total time, 5 seconds
                pause .55
                easein .75 xpos 10 #top (10,-60)
                pause .25#.75
                ease 2.6 xpos 45 #bottom (70,40)
                pause .85# 0
                repeat
#        contains:
#            subpixel True
#            "Kitty_69_Tits"
#            rotate 180
##            zoom .65
#            pos (30,40) #X less is left, Y less is up
#            block:
#                #Total time, 5 seconds
#                pause .5
#                easein .75 pos (10,-10) #top
#                pause 1.25
#                ease 2.5 pos (30,40) #bottom
#                repeat
        contains:
            subpixel True
            "Kitty_69_Body"
            rotate 180
#            zoom .65
#            alpha 0.5
            pos (30,-10) #X less is left, Y less is up
            block:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (10,-70) #top (10,-20)
                pause .8
                ease 2.7 pos (30,-10) #bottom (30,50)
                pause .25
                repeat
        #this is the animation for Kitty's lower body during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Kitty_69_Legs"
            rotate 185
            pos (0,25) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein 1.0 pos (0,-5)
                pause .75
                ease 2.75 pos (30,25)
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein 1.0 rotate 180
                pause .75
                ease 2.75 rotate 185
                repeat

#Start Animations for Kitty's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_69_Anim2:
        #this is the animation for Kitty's hairback during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Kitty_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-80) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-110) #top -60
#                pause .5
                ease 1.25 pos (0,-80) #bottom -30
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
        #this is the animation for Kitty's head during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Kitty_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-80) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-110) #top -60
#                pause .5
                ease 1.25 pos (0,-80) #bottom -30
                repeat
        #this is the animation for Kitty's upper body during 69, Speed 2 (heading)
#        contains:
#            "Kitty_69_Tits"
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
            "Kitty_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,-60) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,-70) #top -10
                pause .25
                ease 1 pos (0,-60) #bottom 0
                repeat
        #this is the animation for Kitty's lower body during 69, Speed 2 (heading)
        contains:
            "Kitty_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat

#Start Animations for Kitty's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_69_Anim3:
        #this is the animation for Kitty's hairback during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Kitty_69_HairBack"
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
        #this is the animation for Kitty's head during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Kitty_69_Head"
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
        #this is the animation for Kitty's upper body during 69, Speed 3 (sucking)
#        contains:
#            subpixel True
#            "Kitty_69_Tits"
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
        #this is the animation for Kitty's lower body during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Kitty_69_Body"
            rotate 180
#            zoom .65
            pos (0,-20) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-60) #top 0
#                pause .5
                ease 1.25 pos (0,-20) #bottom 40
                repeat
        #this is the animation for Kitty's lower body during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Kitty_69_Legs"
            rotate 180
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,-5)
#                pause .5
                ease 1.25 pos (0,10)
                repeat

#Start Animations for Kitty's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_69_Anim4:
        #this is the animation for Kitty's hairback during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Kitty_69_HairBack"
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
        #this is the animation for Kitty's head during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Kitty_69_Head"
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
            "Kitty_69_HairOver"
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
        #this is the animation for Kitty's upper body during 69, Speed 4 (deep)
#        contains:
#            subpixel True
#            "Kitty_69_Tits"
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
#            "Kitty_69_Tits"
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
            "Kitty_69_Body"
            rotate 180
#            zoom .65
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-25) #top 35
                pause .5
                ease 1.75 pos (0,10) #bottom 70
                repeat
        #this is the animation for Kitty's lower body during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Kitty_69_Legs"
            rotate 180
            pos (0,30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,25)
#                pause .5
                ease 2.25 pos (0,30)
                repeat

#Start Animations for Kitty's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_69_Anim5:
        #this is the animation for Kitty's hairback during 69, Speed 5 (cum high)
        contains:
            subpixel True
            "Kitty_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-80) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-90) #top
#                pause .5
                ease 1.25 pos (0,-80) #bottom
                repeat
        #this is the animation for Zero's cock during 69, Speed 5 (cum high)
        contains:
            subpixel True
            "Zero_Blowcock"
            align (0.5,0.6)
            transform_anchor True
            rotate 0
            zoom .3
            offset (695,950)#((675,900)#(180,100)
            pos (0,0) #X less is left, Y less is up
        #this is the animation for Kitty's head during 69, Speed 5 (cum high)
        contains:
            subpixel True
            "Kitty_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-80) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-90) #top
#                pause .5
                ease 1.25 pos (0,-80) #bottom
                repeat
        #this is the animation for Kitty's upper body during 69, Speed 5 (cum high)
#        contains:
#            "Kitty_69_Tits"
#            subpixel True
#            rotate 180
##            zoom .65
#            pos (0,-10) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                pause .5
#                easein 1.75 pos (0,-20) #top
##                pause .5
#                ease 1.25 pos (0,-10) #bottom
#                repeat
        contains:
            "Kitty_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,-30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .5
                easein 1.75 pos (0,-50) #top
#                pause .5
                ease 1.25 pos (0,-30) #bottom
                repeat
        #this is the animation for Kitty's lower body during 69, Speed 5 (cum high)
        contains:
            "Kitty_69_Legs"
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

#Start Animations for Kitty's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_69_Anim6:
        #this is the animation for Kitty's hairback during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Kitty_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-10) #top 30
                pause .5
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
        #this is the animation for Kitty's head during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Kitty_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-10) #top 30
                pause .5
                ease 1.75 pos (0,10) #bottom 70
                repeat
        contains:
            subpixel True
            "Kitty_69_HairOver"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-15) #top 25
                pause .5
                ease 1.75 pos (0,0) #bottom 60
                repeat
        #this is the animation for Kitty's upper body during 69, Speed 6 (cum deep)
#        contains:
#            subpixel True
#            "Kitty_69_Tits"
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
            "Kitty_69_Body"
            rotate 180
#            zoom .65
            pos (0,5) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,0) #top 35
                pause .5
                ease 1.75 pos (0,5) #bottom 70
                repeat
        #this is the animation for Kitty's lower body during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Kitty_69_Legs"
            rotate 180
            pos (0,30) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,25)
#                pause .5
                ease 2.25 pos (0,30)
                repeat

#End Animations for Kitty's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#Start Kitty 69 Cunnilingus Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

#Start Animations for Kitty's 69 Cunnalingus pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Kitty_69_CUN:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
#                "True", "Kitty_69_Anim1",
                "Speed == 2",   "Kitty_69_Cun2",
                "Speed == 3",   "Kitty_69_Cun3",
                "Speed",        "Kitty_69_Cun1",
                "True",         "Kitty_69_Cun0",
                ),
        )
    align (0.6,0.0)
    pos (475,-700)
    zoom 1.8#1/3

#Start Animations for Kitty's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Animations for Kitty's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_69_Cun0:
        #this is the animation for Kitty's hairback during 69, Speed 0 (static)
        contains:
            subpixel True
            "Kitty_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (10,-120) #(15,-20)X less is left, Y less is up
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
        #this is the animation for Kitty's head during 69, Speed 0 (static)
        contains:
            subpixel True
            "Kitty_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (10,-120) #(15,-20)X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (10,-115) #top
#                pause .5
                ease 1.25 pos (10,-120) #bottom
                repeat
        #this is the animation for Kitty's upper body during 69, Speed 0 (static)
#        contains:
#            "Kitty_69_Tits"
#            subpixel True
#            rotate 180
##            zoom .65
#            pos (10,-20) #X less is left, Y less is up
#            block:
#                #Total time, 3 seconds
#                pause .25
#                easein 1.5 pos (10,-25) #top
#                pause .25
#                ease 1 pos (10,-20) #bottom
#                repeat
        contains:
            "Kitty_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (5,-80) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (5,-85) #top 35
                pause .5
                ease 1.75 pos (5,-80) #bottom 70
                repeat

        #this is the animation for Kitty's lower body during 69, Speed 0 (static)
        contains:
            "Kitty_69_Legs"
            subpixel True
            rotate 180
            pos (0,-30) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,-25) #top
                pause .25
                ease 1 pos (0,-30) #bottom
                repeat

#Start Animations for Kitty's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_69_Cun1:
        #this is the animation for Kitty's hairback during 69, Speed 1 (lick)
        contains:
            subpixel True
            "Kitty_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-110) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                ease 1.0 ypos -95 #top
                easeout .5 ypos -105 #top
                easein 1.0 ypos -110 #bottom
                pause .5
                repeat
            parallel:
                #Total time, 3 seconds
                pause .5
                easein .5 rotate 175 #top
                pause .25
                easein 1.25 rotate 180 #bottom
                pause .5
                repeat
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
        #this is the animation for Kitty's head during 69, Speed 1 (lick)
        contains:
            subpixel True
            "Kitty_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-110) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                ease 1.0 ypos -95 #top
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
        #this is the animation for Kitty's upper body during 69, Speed 1 (lick)
#        contains:
#            "Kitty_69_Tits"
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
            "Kitty_69_Body"
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
        #this is the animation for Kitty's lower body during 69, Speed 1 (lick)
        contains:
            "Kitty_69_Legs"
            subpixel True
            rotate 180
            pos (0,-30) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,-25) #top
                pause .25
                ease 1 pos (0,-30) #bottom
                repeat


#Start Animations for Kitty's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_69_Cun2:
        #this is the animation for Kitty's hairback during 69, Speed 2 (clit)
        contains:
            subpixel True
            "Kitty_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-100) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                easein .9 ypos -95 #top
                easein 1.1 ypos -100 #bottom
                repeat
            parallel:
                #Total time, 3 seconds
                pause 0.3
                easein .9 rotate 185 #top
                easein 0.8 rotate 175 #bottom
                repeat
        #this is the animation for Zero's cock during 69, Speed 2 (clit)
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
        #this is the animation for Kitty's head during 69, Speed 2 (clit)
        contains:
            subpixel True
            "Kitty_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-100) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                easein .9 ypos -95 #top
                easein 1.1 ypos -100 #bottom
                repeat
            parallel:
                #Total time, 3 seconds
                pause 0.2
                easein .8 rotate 185 #top
                easein 1.0 rotate 175 #bottom
                repeat
        #this is the animation for Kitty's upper body during 69, Speed 2 (clit)
#        contains:
#            "Kitty_69_Tits"
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
            "Kitty_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (10,-70) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1 pos (10,-75) #top
                ease 1 pos (10,-70) #bottom
                repeat
        #this is the animation for Kitty's lower body during 69, Speed 2 (clit)
        contains:
            "Kitty_69_Legs"
            subpixel True
            rotate 180
            pos (0,-25) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,-30) #top
                pause .25
                ease 1 pos (0,-25) #bottom
                repeat

#Start Animations for Kitty's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_69_Cun3:
        #this is the animation for Kitty's hairback during 69, Speed 3 (suck)
        contains:
            subpixel True
            "Kitty_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-90) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 ypos -95 #top
#                pause .5
                ease 1.25 ypos -90 #bottom
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
        #this is the animation for Kitty's head during 69, Speed 3 (suck)
        contains:
            subpixel True
            "Kitty_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-90) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 ypos -95 #top
#                pause .5
                ease 1.25 ypos -90 #bottom
                repeat
        #this is the animation for Kitty's upper body during 69, Speed 3 (suck)
#        contains:
#            "Kitty_69_Tits"
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
            "Kitty_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (10,-70) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (10,-75) #top
                pause .25
                ease 1 pos (10,-70) #bottom
                repeat
        #this is the animation for Kitty's lower body during 69, Speed 3 (suck)
        contains:
            "Kitty_69_Legs"
            subpixel True
            rotate 180
            pos (0,-25) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,-30) #top
                pause .25
                ease 1 pos (0,-20) #bottom
                repeat
#End Animations for Kitty's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#End Kitty 69 Animations

# Start Kitty Scissor Pose content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Kitty_SC_Sprite:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
                #if the top's down. . .
                "Speed >= 2", "Kitty_SC_Anim_2",
                "Speed", "Kitty_SC_Anim_1",
                "True", "Kitty_SC_Anim_0",
                ),
        )
    align (0.6,0.0)
    pos (650,300)#(650,200)(925,740)#(910,850)
    zoom 0.85#0.8

# End Kitty Sex Pose Speed 2 Scissor / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Kitty_SC_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Kitty_SexSprite
        (1120,840),
        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            "KittyX.Legs == 'dress' and KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Legs_Dress_Back_Up.png"),
            "KittyX.Legs == 'dress'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Legs_Dress_Back.png"),
            "KittyX.Legs == 'blue skirt'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Skirt_Back.png"),
            "True", Null(),
            ),
        (0,0), "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Legs.png",                                                         #Legs Base
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "KittyX.Water", "images/KittySex/Kitty_Sex_Water_Legs.png",
            "True", Null(),
            ),

#        (0,0), "Kitty_Sex_Anus",                                                                          #Anus Composite

        (0,0), "Kitty_SC_Pussy",                                                                         #Pussy Composite

        (0,0), ConditionSwitch(                                                                                 #Panties if up
            "KittyX.PantiesDown", Null(),
            "KittyX.Panties == 'green panties' and KittyX.Wet", Recolor("Kitty", "Panties", "images/KittySex/Kitty_Sex_Panties_Green_Wet.png"),
            "KittyX.Panties == 'green panties'", Recolor("Kitty", "Panties", "images/KittySex/Kitty_Sex_Panties_Green.png"),
            "KittyX.Panties == 'lace panties' and KittyX.Wet", Recolor("Kitty", "Panties", "images/KittySex/Kitty_Sex_Panties_Lace_Wet.png"),
            "KittyX.Panties == 'lace panties'", Recolor("Kitty", "Panties", "images/KittySex/Kitty_Sex_Panties_Lace.png"),
            "KittyX.Panties == 'bikini bottoms' and KittyX.Wet", Recolor("Kitty", "Panties", "images/KittySex/Kitty_Sex_Panties_Bikini_Wet.png"),
            "KittyX.Panties == 'bikini bottoms'", Recolor("Kitty", "Panties", "images/KittySex/Kitty_Sex_Panties_Bikini.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #hose layer
            "KittyX.Hose == 'stockings and garterbelt'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_StockingGarter_Legs.png"),
            "KittyX.Hose == 'garterbelt'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_Garter_Legs.png"),
            "KittyX.Hose == 'stockings'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_Stockings_Legs.png"),
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "KittyX.Hose == 'pantyhose'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_Pantyhose_Legs.png"),
#            "KittyX.Hose == 'ripped pantyhose'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_RippedPantyhose_Legs.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            "KittyX.Legs == 'dress' and KittyX.Upskirt", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Legs_Dress_Up.png"),
            "KittyX.Legs == 'dress'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Legs_Dress.png"),
            "KittyX.Legs == 'blue skirt'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Skirt.png"),
            "KittyX.Upskirt", Null(),
            "KittyX.Legs == 'capris' and KittyX.Wet > 1", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Pants_Blue_Wet.png"),
            "KittyX.Legs == 'capris'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Pants_Blue.png"),
            "KittyX.Legs == 'black jeans' and KittyX.Wet > 1", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Pants_Black_Wet.png"),
            "KittyX.Legs == 'black jeans'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Pants_Black.png"),
            "KittyX.Legs == 'shorts' and KittyX.Wet > 1", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Shorts_Wet.png"),
            "KittyX.Legs == 'shorts'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Shorts.png"),
            "KittyX.Legs == 'yoga pants' and KittyX.Wet > 1", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Pants_Yoga_Wet.png"),
            "KittyX.Legs == 'yoga pants'", Recolor("Kitty", "Legs", "images/KittySex/Kitty_Sex_Pants_Yoga.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #Over Layer
            "KittyX.Over == 'towel' and not KittyX.Uptop", Recolor("Kitty", "Over", "images/KittySex/Kitty_Sex_Towel_Legs.png"),
            "True", Null(),
            ),
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in KittyX.Spunk and Player.Male", "images/KittySex/Kitty_Sex_Spunk_Pelvis.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite", Null(),
            "Trigger == 'lick pussy'", "Kitty_Sex_Lick_Pussy",
            "Trigger == 'lick ass'", "Kitty_Sex_Lick_Ass",
            "KittyX.Offhand == 'fondle pussy' and KittyX.Lust > 60", At("KittyFingerHand", GirlFingerPussyX()),
            "KittyX.Offhand == 'fondle pussy'", At("KittyMastHand", GirlGropePussyX()),
            "True", Null()
            ),
#        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer
#            "not Player.Sprite or Player.Cock != 'foot'", Null(),
#            "Speed >= 2", At("Kitty_Footcock", Kitty_Footcock_Zero_Anim2A()),
#            "Speed", At("Kitty_Footcock", Kitty_Footcock_Zero_Anim1A()),
#            "True", At("Kitty_Footcock", Kitty_Footcock_StaticA()),
#            ),
#        (0,0), ConditionSwitch(                                                                                 #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
        (0,0),  "Kitty_Sex_Feet",
#        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
#            "renpy.showing('Anal_Plug_In_Sex') or renpy.showing('Anal_Plug_Out_Sex')", AlphaMask("Kitty_Sex_Feet", "images/KittySex/Kitty_Sex_FeetMask.png"),
#            "not Speed", "Kitty_Sex_Feet",
#            "Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Kitty_Sex_Feet", "images/KittySex/Kitty_Sex_FeetMask.png"),
#            "True", "Kitty_Sex_Feet",
#            ),
        )
# End Kitty Scissor Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Kitty_SC_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).
    contains:
            # The background plate of her pussy
            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pussy_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pussy_Open.png",
#                "Player.Sprite and Player.Cock == 'in'", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pussy_Closed.png",
                "Trigger == 'lick pussy'", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pussy_Open.png",
                "KittyX.Offhand == 'fondle pussy' and KittyX.Lust > 60", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pussy_Open.png",
                "True", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pussy_Closed.png",
                )
    contains:
            # wet pussy
            ConditionSwitch(
                "not KittyX.Wet", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/KittySex/Kitty_Sex_WetPussy_F.png",
                "True", "images/KittySex/Kitty_Sex_WetPussy_C.png",
                )
    contains:
            #ring piercing
            ConditionSwitch(
                "KittyX.Pierce == 'ring'", "images/KittySex/Kitty_Sex_Pussy_Ring.png",
                "KittyX.Pierce == 'barbell'", "images/KittySex/Kitty_Sex_Pussy_Barbell.png",
                "True", Null(),
                )
    contains:
            # pubes
            ConditionSwitch(
                "not KittyX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", Recolor("Kitty", "Pubes", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pubes_Fucking.png"),
#                "Player.Sprite and Player.Cock == 'in' and Speed", Recolor("Kitty", "Pubes", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pubes_Open.png"),
#                "Player.Sprite and Player.Cock == 'in'", Recolor("Kitty", "Pubes", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pubes_Closed.png"),
                "Trigger == 'lick pussy'", Recolor("Kitty", "Pubes", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pubes_Open.png"),
                "KittyX.Offhand == 'fondle pussy' and KittyX.Lust > 60", Recolor("Kitty", "Pubes", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pubes_Open.png"),
                "True", Recolor("Kitty", "Pubes", "images/KittySex/[KittyX.skin_image.skin_path]Kitty_Sex_Pubes_Closed.png"),
                )
    contains:
            #hose layer
            ConditionSwitch(
                "KittyX.Panties and KittyX.PantiesDown", Null(),
                "KittyX.Hose == 'ripped pantyhose'", Recolor("Kitty", "Hose", "images/KittySex/Kitty_Sex_Hose_RippedPantyhose_Legs.png"),
                "True", Null(),
                )

    #End Kitty Pussy composite

image Kitty_SC_Anim_0:
        #this is the animation for Kitty's lower body during Scissoring, Speed 0 (static)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.1
            rotate 10
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
            "Kitty_SC_Legs"
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
##            "Kitty_Sex_Feet"
#            ConditionSwitch(
#                #Shows different lower body motion depending on events
#                "ShowFeet", "Kitty_Sex_Feet",
#                "True", AlphaMask("Kitty_Sex_Feet", "images/KittySex/Kitty_Sex_FeetMask.png")
#                )
#            anchor (560,580)#(560,420)
#            offset (560,580) #(845,340)    #(840,390)
#            transform_anchor True
#            zoom 1.2
#            rotate 35
#            alpha .8
#            pos (0,0) #X less is left, Y less is up
#            parallel:
#                pause .5
#                ease 2 rotate 30
#                pause .5
#                ease 2 rotate 35
#                repeat
        #end animation for Kitty's lower body during Scissoring, Speed 0 (static) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Kitty_SC_Anim_1:
        #this is the animation for Kitty's lower body during Scissoring, Speed 1 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.1
            rotate 10
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
            "Kitty_SC_Legs"
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
#        contains:
#            subpixel True
##            "Kitty_Sex_Feet"
#            ConditionSwitch(
#                #Shows different lower body motion depending on events
#                "ShowFeet", "Kitty_Sex_Feet",
#                "True", AlphaMask("Kitty_Sex_Feet", "images/KittySex/Kitty_Sex_FeetMask.png")
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
        #End animation for Kitty's lower body during Scissoring, Speed 1 (slow) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Kitty_SC_Anim_2:
        #this is the animation for Kitty's lower body during Scissoring, Speed 2 (fast)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            anchor (560,580)#(560,420)
            offset (560,580) #(845,340)    #(840,390)
            transform_anchor True
            zoom 1.1
            rotate 10
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
            "Kitty_SC_Legs"
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
#        contains:
#            subpixel True
##            "Kitty_Sex_Feet"
#            ConditionSwitch(
#                #Shows different lower body motion depending on events
#                "ShowFeet", "Kitty_Sex_Feet",
#                "True", AlphaMask("Kitty_Sex_Feet", "images/KittySex/Kitty_Sex_FeetMask.png")
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
        #End animation for Kitty's lower body during Scissoring, Speed 2 (fast) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     SC Launch/Reset
label Kitty_SC_Launch(Line = Trigger):
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    return
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary

    $ Trigger = Line

    if renpy.showing("Kitty_SC_Sprite"):
        return
    $ Speed = 0
    call Girl_Hide(KittyX,1) #call Rogue_Hide
    show Kitty_SC_Sprite zorder 150
    with dissolve
    return

label Kitty_SC_Reset:
    if not renpy.showing("Kitty_SC_Sprite"):
        return
    $ KittyX.ArmPose = 2
    hide Kitty_SC_Sprite
    call Girl_Hide(KittyX) #call Rogue_Hide
#    call Set_The_Scene(Dress = 0)
    show Kitty_Sprite at SpriteLoc(KittyX.SpriteLoc) zorder KittyX.Layer:
        alpha 1 zoom 1 offset (0,0) anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return
# End Kitty Scissor Pose content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////




# Start Kitty Fondling Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Interface items //////////////////////////////////////////////////////////////////////////////

image GropeLeftBreast_Kitty:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65#.7
        pos (215,420)#(300,420)230
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block:
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image GropeRightBreast_Kitty:
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (120,410)#(180,410) 150
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block:
            ease 1 rotate -30
            ease 1 rotate -60
            repeat

#image GropeBreast:
image LickRightBreast_Kitty:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5
        xzoom -0.45
        pos (115,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (95,370)
            pause .5
            ease 1.5 rotate 30 pos (115,400)
            repeat

image LickLeftBreast_Kitty:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5
        xzoom -0.45
        pos (200,410) #(115,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (190,380)#(95,370)
            pause .5
            ease 1.5 rotate 30 pos (200,410)#(115,400)
            repeat

image GropeThigh_Kitty:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (200,720)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        parallel:
            pause .5
            ease 1 ypos 780
            ease 1 ypos 720
            repeat
        parallel:
            pause .5
            ease 1 rotate 110 xpos 180
            ease 1 rotate 100 xpos 200
            repeat

image GropePussy_Kitty:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (210,640)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease .5 rotate 190 pos (210,625)
                ease .75 rotate 170 pos (210,640)
            choice:
                ease .5 rotate 190 pos (210,625)
                pause .25
                ease 1 rotate 170 pos (210,640)
            repeat

image FingerPussy_Kitty:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.65
        pos (220,730)#(230,720)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (230,695)#(240,685)
                pause .5
                ease 1 rotate 50 pos (220,730)  #(230,720)
            choice:
                ease .5 rotate 40 pos (230,695)
                pause .5
                ease 1.75 rotate 50 pos (220,730)
            choice:
                ease 2 rotate 40 pos (230,695)
                pause .5
                ease 1 rotate 50 pos (220,730)
            choice:
                ease .25 rotate 40 pos (230,695)
                ease .25 rotate 50 pos (220,730)
                ease .25 rotate 40 pos (230,695)
                ease .25 rotate 50 pos (220,730)
            repeat

image Lickpussy_Kitty:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (240,680)#(250,670)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout .5 rotate -50 pos (220,660) #(230,650)
            linear .5 rotate -60 pos (210,670) #(220,660)
            easein 1 rotate 10 pos (240,680) #(250,670)
            repeat

image VibratorRightBreast_Kitty:
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

image VibratorLeftBreast_Kitty:
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

image VibratorPussy_Kitty:
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

image VibratorAnal_Kitty:
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

image VibratorPussyInsert_Kitty:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_Kitty:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0



#Lesbian action animations.
image GirlGropeLeftBreast_Kitty:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (240,400)#(300,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -20
        block:
            ease 1 rotate -40 pos (230,390)#(280,390)
            ease 1 rotate -20 pos (240,400)
            repeat

image GirlGropeRightBreast_Kitty:
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (110,380) #(160,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block:
            ease 1 rotate -30 pos (110,410)#(160,410)
            ease 1 rotate -10 pos (110,380)
            repeat

image GirlGropeThigh_Kitty:
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

image GirlGropePussy_Kitty:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (210,625)#(230,615)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (215,640)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 pos (215,640)#-10+20
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
#                ease .5 rotate 205 pos (225,620)
#                ease .75 rotate 200 pos (225,625)
                ease .5 rotate 205 pos (215,640)
                ease .75 rotate 200 pos (215,645)
                ease .5 rotate 205 pos (215,640)
                ease .75 rotate 200 pos (215,645)
            choice: #Fast stroke
                ease .3 rotate 205 pos (215,640)
                ease .3 rotate 200 pos (215,650)
                ease .3 rotate 205 pos (215,640)
                ease .3 rotate 200 pos (215,650)
            repeat

image GirlFingerPussy_Kitty:
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

image KittyMastHand:
        "images/UI_GirlHand_Kitty.png"
        zoom 0.95
        rotate 240
        offset (360,210)

image KittyFingerHand:
        "images/UI_GirlFinger_Kitty.png"
        zoom 0.95
        rotate 220
        offset (320,280)
