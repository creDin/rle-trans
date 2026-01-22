# Basic character Sprites

image Laura_Sprite:
    LiveComposite(
        (402,965),
        (0,0), "images/LauraSprite/Laura_Sprite_Shadow.png",
        (0,0), "Laura_Sprite_HairBack",
        (0,0), ConditionSwitch(
            #panties down back
            "not LauraX.Panties or not LauraX.PantiesDown or (LauraX.Legs and LauraX.Legs != 'skirt' and not LauraX.Upskirt)", Null(),
            "LauraX.Panties == 'wolvie panties'", Recolor("Laura", "Panties", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Back.png"),
            "LauraX.Panties == 'bikini bottoms'", Recolor("Laura", "Panties", "images/LauraSprite/Laura_Sprite_Panties_Bikini_Back.png"),
            "True", Recolor("Laura", "Panties", "images/LauraSprite/Laura_Sprite_Panties_Lace_Back.png"),
            ),
        (0,0), ConditionSwitch(
            #backside of arms
            "LauraX.Arms == 'gloves' and LauraX.ArmPose == 2", Recolor("Laura", "Arms", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Glove_Back2.png"),
            "LauraX.Arms == 'gloves'", Recolor("Laura", "Arms", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Glove_Back1.png"), #if LauraX.Arms == 1
            "LauraX.ArmPose == 2", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Arm_Back2.png",
            "True", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Arm_Back1.png", #if LauraX.Arms == 1
            ),
#        (0,0), ConditionSwitch(
#            #arms wristband
#            "LauraX.Arms == 'wrists'", Recolor("Laura", "Arms", "images/LauraSprite/Laura_Sprite_Wrist_Right.png"), # one hand up
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #L Over under
            "LauraX.Uptop and LauraX.Over == 'jacket'", Recolor("Laura", "Over", "images/LauraSprite/Laura_Sprite_Jacket_Back_Up.png"), # one hand up
            "LauraX.Over == 'jacket'", Recolor("Laura", "Over", "images/LauraSprite/Laura_Sprite_Jacket_Back.png"), # one hand up
            "True", Null(),
            ),
        #body
        (0,0), "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Body.png",

        #shifted here
        (0,0), ConditionSwitch(
            #arms midlayer
            "LauraX.Arms == 'gloves' and LauraX.ArmPose == 2", Recolor("Laura", "Arms", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Glove_Mid2.png"),
            "LauraX.Arms == 'gloves'", Recolor("Laura", "Arms", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Glove_Mid1.png"), #if LauraX.Arms == 1
            "LauraX.ArmPose == 2", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Arm_Mid2.png",         # one hand up
            "True", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Arm_Mid1.png", #if LauraX.Arms == 1   # Crossed
            ),
        # tits
        (0,0), "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Tits.png",
        (0,0), ConditionSwitch(
            #Water effect
            "LauraX.Water and LauraX.ArmPose == 1", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Water1.png",
            "LauraX.Water", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Water2.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #arms wristband
            "LauraX.Arms == 'wrists' and LauraX.ArmPose == 2", Recolor("Laura", "Arms", "images/LauraSprite/Laura_Sprite_Wrist2.png"), # one hand up
            "LauraX.Arms == 'wrists'", Recolor("Laura", "Arms", "images/LauraSprite/Laura_Sprite_Wrist1.png"), # one hand up
            # Modification mode
            "LauraX.Arms == 'arms gloves long mesh' and LauraX.ArmPose == 2", "images/LauraSprite/modification/Laura_sprite_arm2_gloves_long_mesh.png", # one hand up
            "LauraX.Arms == 'arms gloves long mesh'", "images/LauraSprite/modification/Laura_sprite_arm1_gloves_long_mesh.png", # one hand up
            # -----------------
            "True", Null(),
            ),
        #shifted here

        (145,560), ConditionSwitch(    #(225,560)
            #Personal Wetness
            "not LauraX.Wet", Null(),
            "LauraX.Legs and LauraX.Legs != 'skirt' and LauraX.Legs != 'other skirt' and not LauraX.Upskirt", Null(),
            "LauraX.Panties and not LauraX.PantiesDown and LauraX.Wet <= 1", Null(),
            "LauraX.Wet == 1", ConditionSwitch( #Wet = 1
                    "LauraX.Panties and LauraX.PantiesDown", AlphaMask("Wet_Drip","Laura_Drip_MaskP"),
                    "LauraX.Legs and LauraX.Legs != 'skirt' and LauraX.Legs != 'other skirt' ", AlphaMask("Wet_Drip","Laura_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip","Laura_Drip_Mask"), #only plays if nothing is in the way
                    ),
            "True", ConditionSwitch( #Wet = 2+
                    "LauraX.Panties and LauraX.PantiesDown", AlphaMask("Wet_Drip2","Laura_Drip_MaskP"),
                    "LauraX.Legs and LauraX.Legs != 'skirt' and LauraX.Legs != 'other skirt'", AlphaMask("Wet_Drip2","Laura_Drip_MaskP"),
                    "LauraX.Panties", AlphaMask("Wet_Drip","Laura_Drip_Mask"), #"Wet_Drip2",#
                    "True", AlphaMask("Wet_Drip2","Laura_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (145,560), ConditionSwitch(    #(225,560)
            #dripping spunk
            "('in' not in LauraX.Spunk and 'anal' not in LauraX.Spunk) or not Player.Male", Null(),
            "LauraX.Legs and LauraX.Legs != 'skirt' and not LauraX.Upskirt", Null(),
            "LauraX.Legs and LauraX.Legs != 'other skirt' and not LauraX.Upskirt", Null(),
            "LauraX.Panties and not LauraX.PantiesDown and LauraX.Wet <= 1", Null(),
            "True", ConditionSwitch( #Wet = 2+
                    "LauraX.Panties and LauraX.PantiesDown", AlphaMask("Spunk_Drip2","Laura_Drip_MaskP"),
#                    "LauraX.Legs and LauraX.Legs != 'skirt'", AlphaMask("Spunk_Drip2","Laura_Drip_MaskP"), #add if pantes have down art
                    "LauraX.Panties", AlphaMask("Spunk_Drip","Laura_Drip_Mask"), #"Wet_Drip2",#
                    "True", AlphaMask("Spunk_Drip2","Laura_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (0,0), ConditionSwitch(
            #pubes
            "LauraX.Pubes", Recolor("Laura", "Pubes", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Pubes.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #nude lower piercings
            "not LauraX.Pierce", Null(),
            "LauraX.Panties and not LauraX.PantiesDown", Null(),
            "LauraX.Legs != 'skirt' and LauraX.Legs and not LauraX.Upskirt", Null(), #skirt if wearing a skirt
            "LauraX.Legs != 'other skirt' and LauraX.Legs and not LauraX.Upskirt", Null(), #skirt if wearing a skirt
            "LauraX.Pierce == 'barbell'", "images/LauraSprite/Laura_Sprite_Barbell_Pussy.png",
            "LauraX.Pierce == 'ring'", "images/LauraSprite/Laura_Sprite_Ring_Pussy.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #stockings
            "LauraX.Hose == 'black stockings'", Recolor("Laura", "Hose", "images/LauraSprite/Laura_Sprite_BlackStockings.png"),
            "LauraX.Hose == 'stockings and garterbelt'", Recolor("Laura", "Hose", "images/LauraSprite/Laura_Sprite_StockingsGarter.png"),
            "LauraX.Hose == 'garterbelt'", Recolor("Laura", "Hose", "images/LauraSprite/Laura_Sprite_Garters.png"),
            "LauraX.Hose == 'stockings'", Recolor("Laura", "Hose", "images/LauraSprite/Laura_Sprite_Stockings.png"),
            # Modification mode
            "LauraX.Hose == 'stockings alice'", "images/LauraSprite/modification/Laura_sprite_hose_stockings_alice.png",
            "LauraX.Hose == 'stockings alice torn'", "images/LauraSprite/modification/Laura_sprite_hose_stockings_alice_torn.png",
            # ----------------
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #garterbelt
#            "LauraX.Hose == 'stockings and garterbelt' or LauraX.Hose == 'garterbelt'", Recolor("Laura", "Hose", "images/LauraSprite/Laura_Sprite_Garters.png"),
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #panties
            "not LauraX.Panties", Null(),
            "LauraX.PantiesDown", ConditionSwitch(
                    #if the panties are down
                    "not LauraX.Legs or LauraX.Upskirt or LauraX.Legs == 'skirt'", ConditionSwitch(
                            #if she's wearing a skirt or nothing else
                            "LauraX.Panties == 'wolvie panties' and LauraX.Wet", Recolor("Laura", "Panties", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Down_W.png"),
                            "LauraX.Panties == 'wolvie panties'", Recolor("Laura", "Panties", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Down.png"),
                            "LauraX.Panties == 'lace panties'", Recolor("Laura", "Panties", "images/LauraSprite/Laura_Sprite_Panties_Lace_Down.png"),
                            "LauraX.Panties == 'bikini bottoms'", Recolor("Laura", "Panties", "images/LauraSprite/Laura_Sprite_Panties_Bikini_Down.png"),
                            "True", Recolor("Laura", "Panties", "images/LauraSprite/Laura_Sprite_Panties_Leather_Down.png"),
                            ),
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                    #if she's got panties and they are not down
                    "LauraX.Wet", ConditionSwitch(
                        #if she's  wet
                        "LauraX.Panties == 'wolvie panties'", Recolor("Laura", "Panties", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_W.png"),
                        "LauraX.Panties == 'lace panties'", Recolor("Laura", "Panties", "images/LauraSprite/Laura_Sprite_Panties_Lace.png"),
                        "LauraX.Panties == 'bikini bottoms'", Recolor("Laura", "Panties", "images/LauraSprite/Laura_Sprite_Panties_Bikini.png"),
                        "True", Recolor("Laura", "Panties", "images/LauraSprite/Laura_Sprite_Panties_Leather.png"),
                        ),
                    "True", ConditionSwitch(
                        #if she's not wet
                        "LauraX.Panties == 'wolvie panties'", Recolor("Laura", "Panties", "images/LauraSprite/Laura_Sprite_Panties_Wolvie.png"),
                        "LauraX.Panties == 'lace panties'", Recolor("Laura", "Panties", "images/LauraSprite/Laura_Sprite_Panties_Lace.png"),
                        "LauraX.Panties == 'bikini bottoms'", Recolor("Laura", "Panties", "images/LauraSprite/Laura_Sprite_Panties_Bikini.png"),
                        "True", Recolor("Laura", "Panties", "images/LauraSprite/Laura_Sprite_Panties_Leather.png"),
                        ),
                    ),
            ),
        (0,0), ConditionSwitch(
            #pantyhose
            "LauraX.Hose == 'pantyhose'", Recolor("Laura", "Hose", "images/LauraSprite/Laura_Sprite_Hose_Pantyhose.png"),
            "LauraX.Hose == 'ripped pantyhose'", Recolor("Laura", "Hose", "images/LauraSprite/Laura_Sprite_Hose_Pantyhose_Holed.png"),
            # Modification mode
            "LauraX.Hose == 'pantyhose brown'", "images/LauraSprite/modification/Laura_sprite_hose_pantyhose_brown.png",
            "LauraX.Hose == 'pantyhose brown ripped'", "images/LauraSprite/modification/Laura_sprite_hose_pantyhose_brown_ripped.png",
            "LauraX.Hose == 'tights mesh torn'", "images/LauraSprite/modification/Laura_sprite_hose_tights_mesh_torn.png",
            # ----------------
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pants
            "not LauraX.Legs", Null(),
            "LauraX.Upskirt", ConditionSwitch(
                        #if the skirt's up or pants down
                        "LauraX.Legs == 'other skirt'", Recolor("Laura", "Legs", "images/LauraSprite/Laura_Sprite_SkirtCos_Up.png"),
                        "LauraX.Legs == 'skirt'", Recolor("Laura", "Legs", "images/LauraSprite/Laura_Sprite_Skirt_Up.png"),
                        "True", Null(),
                        ),
            "True", ConditionSwitch(
                    #if it's the ring pericings
                    "LauraX.Legs == 'other skirt'", Recolor("Laura", "Legs", "images/LauraSprite/Laura_Sprite_SkirtCos.png"),
                    "LauraX.Legs == 'skirt'", Recolor("Laura", "Legs", "images/LauraSprite/Laura_Sprite_Skirt.png"),
#                    "LauraX.Wet", ConditionSwitch(
#                        #if she's not wet
#                        "LauraX.Legs == 'leather pants'", Recolor("Laura", "Legs", "images/LauraSprite/Laura_Sprite_Pants_Leather.png"),
#                        "LauraX.Legs == 'mesh pants'", Recolor("Laura", "Legs", "images/LauraSprite/Laura_Sprite_Pants_Mesh.png"),
##                        "LauraX.Legs == 'yoga pants'", Recolor("Laura", "Legs", "images/LauraSprite/Laura_Sprite_Pants_YogaWet.png"),
#                        "True", Null(),
#                        ),
                    "True", ConditionSwitch(
                        #if she's wet
                        "LauraX.Legs == 'leather pants'", Recolor("Laura", "Legs", "images/LauraSprite/Laura_Sprite_Pants_Leather.png"),
                        "LauraX.Legs == 'mesh pants'", Recolor("Laura", "Legs", "images/LauraSprite/Laura_Sprite_Pants_Mesh.png"),
#                        "LauraX.Legs == 'yoga pants'", Recolor("Laura", "Legs", "images/LauraSprite/Laura_Sprite_Pants_Yoga.png"),
                        # Modification mode
                        "LauraX.Legs == 'leggings goth'", "images/LauraSprite/modification/Laura_sprite_legs_leggings_goth.png",
                        "LauraX.Legs == 'leggings goth torn'", "images/LauraSprite/modification/Laura_sprite_legs_leggings_goth_torn.png",
                        "LauraX.Legs == 'pants goth torn'", "images/LauraSprite/modification/Laura_sprite_legs_pants_goth_torn.png",
                        "LauraX.Legs == 'short skirt goth'", "images/LauraSprite/modification/Laura_sprite_legs_short_skirt_goth.png",
                        # ----------------
                        "True", Null(),
                        ),
                    ),
            ),
        (0,0), ConditionSwitch(
            #boots
            "LauraX.Boots", Recolor("Laura", "Boots", "images/LauraSprite/Laura_Sprite_Boots.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #clothed lower piercings
            "LauraX.Legs == 'skirt' or LauraX.Legs == 'other skirt'", Null(),
            "LauraX.Pierce == 'barbell'", ConditionSwitch(
                    #if it's the barbell pericings
                    "LauraX.Legs and not LauraX.Upskirt", "images/LauraSprite/Laura_Sprite_Barbell_PussyC.png",
                    "LauraX.Panties and not LauraX.PantiesDown", "images/LauraSprite/Laura_Sprite_Barbell_PussyC.png",
                    "True", Null(),
                    ),
            "LauraX.Pierce == 'ring'", ConditionSwitch(
                    #if it's the ring pericings
                    "LauraX.Legs and not LauraX.Upskirt", "images/LauraSprite/Laura_Sprite_Ring_PussyC.png",
                    "LauraX.Panties and not LauraX.PantiesDown", "images/LauraSprite/Laura_Sprite_Ring_PussyC.png",
                    "True", Null(),
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Personal Wetness
            "not LauraX.Wet", Null(),
            "LauraX.Legs and LauraX.Wet <= 1", Null(),
            "LauraX.Legs == 'other skirt'", Null(),
            "LauraX.Legs == 'skirt'", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Wetness.png",       #LauraX.Wet >1
            ),
        (0,0), ConditionSwitch(
            #pussy spunk
            "(LauraX.Legs and not LauraX.Upskirt) or not Player.Male", Null(),
            "'in' in LauraX.Spunk or 'anal' in LauraX.Spunk", "images/LauraSprite/Laura_Sprite_Spunk_Pussy.png",
            "True", Null(),
            ),
        #where arms and tits were before
        (0,0), ConditionSwitch(
            #nude peircings
            "not LauraX.Pierce", Null(),
            "LauraX.Pierce == 'barbell'", "images/LauraSprite/Laura_Sprite_Barbell_Tits.png",
            "LauraX.Pierce == 'ring'", "images/LauraSprite/Laura_Sprite_Ring_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #neck
            "LauraX.Neck == 'leash choker'", Recolor("Laura", "Neck", "images/LauraSprite/Laura_Sprite_Neck_Leash.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Chest layer
            "LauraX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "LauraX.Chest == 'white tank'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Bra_White_Up.png"),
                    "LauraX.Chest == 'leather bra'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Bra_Leather_Up.png"),
                    "LauraX.Chest == 'wolvie top'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Top_Wolvie_Up.png"),
                    "LauraX.Chest == 'bikini top'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Top_Bikini_Up.png"),
                    "LauraX.Chest == 'corset'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Top_Corset_Up.png"),
                    "LauraX.Chest == 'lace corset'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Top_Corset_Lace_Up.png"),
                    # Modification mode
                    "LauraX.Chest == 'goth top'", "images/LauraSprite/modification/Laura_sprite_chest_top_goth_up.png",
                    # -----------------
                    "True", Null(),
                    ),
            "LauraX.Chest == 'white tank'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Bra_White.png"),
            "LauraX.Chest == 'leather bra'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Bra_Leather.png"),
            "LauraX.Chest == 'wolvie top'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Top_Wolvie.png"),
            "LauraX.Chest == 'bikini top'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Top_Bikini.png"),
            "LauraX.Chest == 'corset'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Top_Corset.png"),
            "LauraX.Chest == 'lace corset'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Top_Corset_Lace.png"),
            # Modification mode
            "LauraX.Chest == 'goth top'", "images/LauraSprite/modification/Laura_sprite_chest_top_goth.png",
            # -----------------
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #suspenders
            "not LauraX.Legs", Null(), #hides when no skirt on
            "(LauraX.Legs == 'leather pants' or LauraX.Legs == 'mesh pants') and LauraX.Upskirt", Null(), #hides when no skirt on
#            "LauraX.Acc == 'suspenders' and not LauraX.Chest and not LauraX.Uptop", "images/LauraSprite/Laura_Sprite_Acc_Suspenders2.png", #over nips
            "LauraX.Acc == 'suspenders2'", "images/LauraSprite/Laura_Sprite_Acc_Suspenders2.png", #over nips
            "LauraX.Acc == 'suspenders'", "images/LauraSprite/Laura_Sprite_Acc_Suspenders1.png", #open
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #L Over
            "LauraX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "LauraX.Over == 'jacket' and LauraX.ArmPose == 2", Recolor("Laura", "Over", "images/LauraSprite/Laura_Sprite_Jacket_A2_Up.png"), # one hand up
                    "LauraX.Over == 'jacket'", Recolor("Laura", "Over", "images/LauraSprite/Laura_Sprite_Jacket_A1_Up.png"), # one hand up
#                    "LauraX.Over == 'towel'", Recolor("Laura", "Legs", "images/LauraSprite/Laura_Sprite_Towel.png"),
                    # Modification mode
                    "LauraX.Over == 'bunny'", "images/LauraSprite/modification/Laura_sprite_over_bunny_suit_up.png",
                    "LauraX.Over == 'apron alice'", "images/LauraSprite/modification/Laura_sprite_over_apron_alice_up.png",
                    # -----------------
                    "True", Null(),
                    ),
            "LauraX.Over == 'jacket' and LauraX.ArmPose == 2", Recolor("Laura", "Over", "images/LauraSprite/Laura_Sprite_Jacket_A2.png"), # one hand up
            "LauraX.Over == 'jacket'", Recolor("Laura", "Over", "images/LauraSprite/Laura_Sprite_Jacket_A1.png"), # one hand up
            "LauraX.Over == 'towel'", Recolor("Laura", "Legs", "images/LauraSprite/Laura_Sprite_Towel.png"),
            # Modification mode
            "LauraX.Over == 'top goth mesh' and LauraX.ArmPose == 2", "images/LauraSprite/modification/Laura_sprite_over_goth_mesh_A2.png", # one hand up
            "LauraX.Over == 'top goth mesh'", "images/LauraSprite/modification/Laura_sprite_over_goth_mesh_A1.png", # one hand up
            "LauraX.Over == 'bunny'", "images/LauraSprite/modification/Laura_sprite_over_bunny_suit.png",
            "LauraX.Over == 'apron alice'", "images/LauraSprite/modification/Laura_sprite_over_apron_alice.png",
            "LauraX.Over == 'dress alice'", "images/LauraSprite/modification/Laura_sprite_over_dress_alice.png",
            "LauraX.Over == 'dress alice torn'", "images/LauraSprite/modification/Laura_sprite_over_dress_alice_torn.png",
            # -----------------
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #clothed peircings
            "not LauraX.Pierce or (not LauraX.Over and not LauraX.Chest)", Null(),
            "LauraX.Over == 'jacket'", Null(),
            "LauraX.Pierce == 'barbell'",  "images/LauraSprite/Laura_Sprite_Barbell_TitsC.png",
            "LauraX.Pierce == 'ring'", "images/LauraSprite/Laura_Sprite_Ring_TitsC.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #belly spunk
            "'belly' in LauraX.Spunk and Player.Male", "images/LauraSprite/Laura_Sprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast spunk
            "'tits' in LauraX.Spunk and Player.Male", "images/LauraSprite/Laura_Sprite_Spunk_Tits.png",
            "True", Null(),
            ),
        #Head
#        (0,0), "Laura_Sprite_Head", #(55,0)
        (0,0), ConditionSwitch(
            # head
            "renpy.showing('Laura_BJ_Animation') or renpy.showing('Laura_CUN_Animation')", Null(),
            "True", "Laura_Sprite_Head",
            ),
        (0,0), ConditionSwitch(
            #arms toplayer
            "LauraX.Arms == 'gloves' and LauraX.ArmPose == 2", Recolor("Laura", "Arms", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Glove_Top2.png"),
            "LauraX.ArmPose == 2", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Arm_Left2.png", # one hand up
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Water effect
            "LauraX.Water and LauraX.ArmPose == 2", "images/LauraSprite/Laura_Sprite_Water2top.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #arms wristband
            "LauraX.ArmPose == 2 and LauraX.Arms == 'wrists'", Recolor("Laura", "Arms", "images/LauraSprite/Laura_Sprite_Wrist_Left2.png"), # one hand up
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #jacket arm toplayer
            "LauraX.Over == 'jacket' and LauraX.ArmPose == 2", Recolor("Laura", "Over", "images/LauraSprite/Laura_Sprite_Jacket_A2Top.png"), # one hand up
            # Modification mode
            "LauraX.Over == 'top goth mesh' and LauraX.ArmPose == 2", "images/LauraSprite/modification/Laura_sprite_over_goth_mesh_A2Top.png", # one hand up
            # -----------------
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #claws
            "LauraX.ArmPose == 2 and LauraX.Claws", "images/LauraSprite/Laura_Sprite_Claws2.png", # one hand up
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #hand spunk
            "LauraX.ArmPose == 2 or 'hand' not in LauraX.Spunk or not Player.Male", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Spunk_Hand.png",
            ),
#        (0,0), ConditionSwitch(                                                                         #Props
#            "not LauraX.Held or LauraX.ArmPose != 2", Null(),
#            "LauraX.ArmPose == 2 and LauraX.Held == 'phone'", "images/LauraSprite/Laura_held_phone.png",
#            "LauraX.ArmPose == 2 and LauraX.Held == 'dildo'", "images/LauraSprite/Laura_held_dildo.png",
#            "LauraX.ArmPose == 2 and LauraX.Held == 'vibrator'", "images/LauraSprite/Laura_held_vibrator.png",
#            "LauraX.ArmPose == 2 and LauraX.Held == 'panties'", "images/LauraSprite/Laura_held_panties.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #UI tool for When Laura is masturbating using LauraX.Offhand actions while lead
            "Trigger == 'lesbian' or not LauraX.Offhand",Null(),# or Ch_Focus is not LauraX", Null(),
            "LauraX.Offhand == 'fondle pussy' and Trigger != 'sex' and LauraX.Lust >= 70", "GirlFingerPussy_Laura",
            "LauraX.Offhand == 'fondle pussy'", "GirlGropePussy_Laura",
            "LauraX.Offhand == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Laura",    #When zero is working the right breast, fondle left
            "LauraX.Offhand == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Laura", #When zero is working the left breast, fondle right
            "LauraX.Offhand == 'fondle breasts'", "GirlGropeRightBreast_Laura",
            "LauraX.Offhand == 'vibrator breasts'", "VibratorRightBreast_Laura",
            "LauraX.Offhand == 'vibrator pussy'", "VibratorPussy_Laura",
            "LauraX.Offhand == 'vibrator pussy insert'", "VibratorPussy_Laura",
            "LauraX.Offhand == 'vibrator anal'", "VibratorAnal_Laura",
            "LauraX.Offhand == 'vibrator anal insert'", "VibratorPussy_Laura",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for LauraX.Offhand(lesbian) actions (ie Kitty's hand on her when Laura is secondary)
            "not Partner or Partner is LauraX or LauraX in Nearby", Null(),
            "Partner.Offhand == 'fondle girl pussy' and Trigger != 'sex' and LauraX.Lust >= 70", "GirlFingerPussy_Laura",
            "Partner.Offhand == 'fondle girl pussy'", "GirlGropePussy_Laura",
            "Partner.Offhand == 'lick girl pussy'", "Lickpussy_Laura",
            "Partner.Offhand == 'suck girl breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Laura",
            "Partner.Offhand == 'suck girl breasts'", "LickRightBreast_Laura",
            "Partner.Offhand == 'fondle girl breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Laura",    #When zero is working the right breast, fondle left
            "Partner.Offhand == 'fondle girl breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Laura", #When zero is working the left breast, fondle right
            "Partner.Offhand == 'fondle girl breasts'", "GirlGropeRightBreast_Laura",
            "Partner.Offhand == 'vibrator girl breasts'", "VibratorRightBreast_Laura",
            "Partner.Offhand == 'vibrator girl pussy'", "VibratorPussy_Laura",
            "Partner.Offhand == 'vibrator girl pussy insert'", "VibratorPussy_Laura",
            "Partner.Offhand == 'vibrator girl anal'", "VibratorAnal_Laura",
            "Partner.Offhand == 'vibrator girl anal insert'", "VibratorPussy_Laura",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for when RogueX is the partner in the scene, and the lead is working on her
            "not Partner or Partner is not LauraX", Null(),
            "Ch_Focus.Offhand == 'fondle girl pussy' and Trigger != 'sex' and LauraX.Lust >= 70", "GirlFingerPussy_Laura",
            "Ch_Focus.Offhand == 'fondle girl pussy'", "GirlGropePussy_Laura",
            "Ch_Focus.Offhand == 'lick girl pussy'", "Lickpussy_Laura",
            "Ch_Focus.Offhand == 'suck girl breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Laura",
            "Ch_Focus.Offhand == 'suck girl breasts'", "LickRightBreast",
            "Ch_Focus.Offhand == 'fondle girl breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast_Laura",    #When zero is working the right breast, fondle left
            "Ch_Focus.Offhand == 'fondle girl breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast_Laura", #When zero is working the left breast, fondle right
            "Ch_Focus.Offhand == 'fondle girl breasts'", "GirlGropeRightBreast_Laura",
            "Ch_Focus.Offhand == 'vibrator girl breasts'", "VibratorRightBreast_Laura",
            "Ch_Focus.Offhand == 'vibrator girl pussy'", "VibratorPussy_Laura",
            "Ch_Focus.Offhand == 'vibrator girl pussy insert'", "VibratorPussy_Laura",
            "Ch_Focus.Offhand == 'vibrator girl anal'", "VibratorAnal_Laura",
            "Ch_Focus.Offhand == 'vibrator girl anal insert'", "VibratorPussy_Laura",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger1(primary) actions
            #Laura is primary and a sex trigger is active
            "not Trigger or Ch_Focus is not LauraX", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast_Laura",
            "Trigger == 'fondle thighs'", "GropeThigh_Laura",
            "Trigger == 'fondle breasts'", "GropeLeftBreast_Laura",
            "Trigger == 'suck breasts'", "LickRightBreast_Laura",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_Laura",
            "Trigger == 'fondle pussy'", "GropePussy_Laura",
            "Trigger == 'lick pussy'", "Lickpussy_Laura",
            "Trigger == 'vibrator pussy'", "VibratorPussy_Laura",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy_Laura",
            "Trigger == 'vibrator anal'", "VibratorAnal_Laura",
            "Trigger == 'vibrator anal insert'", "VibratorPussy_Laura",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus is not LauraX", Null(),
#            "Trigger == 'fondle breasts' and not LauraX.Offhand", "GropeRightBreast_Laura",  #"Trigger == 'fondle breasts' and not LauraX.Offhand",
            #When doing nothing offhand, use both hands on breasts.
            "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast_Laura",
            #When sucking right breast, fondle left
            "Trigger2 == 'fondle breasts'", "GropeLeftBreast_Laura",
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast_Laura",
            #When sucking right breast, vibrator left
            "Trigger2 == Trigger", Null(),
            #When both triggers are the same, do nothing
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast_Laura",
            "Trigger2 == 'suck breasts'", "LickLeftBreast_Laura",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy_Laura",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy_Laura",
            "Trigger2 == 'vibrator anal'", "VibratorAnal_Laura",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy_Laura",
            "Trigger2 == 'fondle pussy'", "GropePussy_Laura",
            "Trigger2 == 'lick pussy'", "Lickpussy_Laura",
            "Trigger2 == 'fondle thighs'", "GropeThigh_Laura",
            "True", Null(),
            ),
        )
    anchor (0.5, 0.0)
    offset (35,0)
    zoom .78#.75

image Laura_Sprite_HairBack:
    ConditionSwitch(
            #hair back
            "not LauraX.Hair", Null(),
            "renpy.showing('Laura_BJ_Animation') or renpy.showing('Laura_CUN_Animation')", Null(),
#            "renpy.showing('Laura_SexSprite')", Recolor("Laura", "Hair", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Long_UnderSex.png"),
            "LauraX.Hair == 'wet' or LauraX.Water", Recolor("Laura", "Hair", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Wet_Under.png"),
            "not Player.Male and 'facial' in LauraX.Spunk",Recolor("Laura", "Hair", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Wet_Under.png"),
            "LauraX.Hair", Recolor("Laura", "Hair", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Long_Under.png"),
            "True", Null(),
            ),
#    Recolor("Laura", "Hair", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Long_Under.png")
    anchor (0.6, 0.0)
    zoom .5

image Laura_Sprite_HairMid:
    ConditionSwitch(
            #hair back
            "not LauraX.Hair", Null(),
            "renpy.showing('Laura_BJ_Animation') or renpy.showing('Laura_CUN_Animation')", Null(),
#            "renpy.showing('Laura_SexSprite')", Recolor("Laura", "Hair", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Long_UnderSex.png"),
            "LauraX.Hair == 'wet' or LauraX.Water", Null(),
            "not Player.Male and 'facial' in LauraX.Spunk",Null(),
            "LauraX.Hair", Recolor("Laura", "Hair", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Long_Mid.png"),
            "True", Null(),
            ),
    anchor (0.6, 0.0)
    zoom .5

image Laura_Sprite_HairTop:
    ConditionSwitch(
            #hair back
            "not LauraX.Hair", Null(),
            "renpy.showing('Laura_SexSprite')", Recolor("Laura", "Hair", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Long_OverSex.png"),
            "LauraX.Hair == 'wet' or LauraX.Water", Recolor("Laura", "Hair", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Wet_Over.png"),
            "not Player.Male and 'facial' in LauraX.Spunk",Recolor("Laura", "Hair", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Wet_Over.png"),
            "LauraX.Hair", Recolor("Laura", "Hair", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Long_Over.png"),
            "True", Null(),
            ),
#    Recolor("Laura", "Hair", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Long_Under.png")
    anchor (0.6, 0.0)
    zoom .5

image Laura_Sprite_Head:
    LiveComposite(
        (806,806),
        (0,0), ConditionSwitch(
                # hair behind face
                "renpy.showing('Laura_SexSprite')", Recolor("Laura", "Hair", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Long_UnderSex.png"),
                "True", Null(),
                ),
        (0,0), ConditionSwitch(
                # Face background plate
                "LauraX.Blush == 2", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Head_Blush2.png",
                "LauraX.Blush", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Head_Blush.png",
                "True", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Head.png",
                ),
        (0,0), ConditionSwitch(#chin spunk
            "'chin' in LauraX.Spunk and Player.Male", "images/LauraSprite/Laura_Sprite_Spunk_Chin.png",
#            "(renpy.showing('Laura_BJ_Animation') or renpy.showing('Laura_CUN_Animation'))and Speed >= 2", Null(),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(#Mouths
#            "renpy.showing('Laura_BJ_Animation') or renpy.showing('Laura_CUN_Animation')", Recolor("Laura", "Lips", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Mouth_SuckingBJ.png"), #and Speed >= 2
            "LauraX.Mouth == 'normal'", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png"),
            "LauraX.Mouth == 'lipbite'", Recolor("Laura", "Lips", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Mouth_Lipbite.png"),
            "LauraX.Mouth == 'sucking' or LauraX.Mouth == 'open'", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Sucking.png"),
            "LauraX.Mouth == 'kiss'", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Kiss.png"),
            "LauraX.Mouth == 'sad'", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Sad.png"),
            "LauraX.Mouth == 'smile'", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png"),
            "LauraX.Mouth == 'surprised'", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Surprised.png"),
            "LauraX.Mouth == 'tongue'", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Tongue.png"),
            "LauraX.Mouth == 'grimace'", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png"),
            "LauraX.Mouth == 'smirk'", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Smirk.png"),
#            "LauraX.Mouth == 'smirk'", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png"),
            "True", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png"),
            ),
        (0,0), ConditionSwitch(#Mouth spunk
            "'mouth' not in LauraX.Spunk or not Player.Male", Null(),
#            "renpy.showing('Laura_BJ_Animation') or renpy.showing('Laura_CUN_Animation')", "images/LauraSprite/Laura_Sprite_Spunk_MouthSuck.png", #and Speed >= 2
            "LauraX.Mouth == 'normal'", "images/LauraSprite/Laura_Sprite_Spunk_MouthNeutral.png",
            "LauraX.Mouth == 'lipbite'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmirk.png",
            "LauraX.Mouth == 'sucking' or LauraX.Mouth == 'open'", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",
            "LauraX.Mouth == 'kiss'", "images/LauraSprite/Laura_Sprite_Spunk_MouthKiss.png",
            "LauraX.Mouth == 'sad'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSad.png",
            "LauraX.Mouth == 'smile'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmile.png",
            "LauraX.Mouth == 'surprised'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSad.png",
            "LauraX.Mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",
            "LauraX.Mouth == 'grimace'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmile.png",
            "LauraX.Mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmirk.png",
            "True", "images/LauraSprite/Laura_Sprite_Spunk_MouthNeutral.png",
            ),

        (0,0), ConditionSwitch(
            #wet face
            "Player.Male", Null(),
            "'mouth' not in LauraX.Spunk and 'chin' not in LauraX.Spunk", Null(),
            "'chin' not in LauraX.Spunk and LauraX.Mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Head_Wet_Tongue.png",
            "LauraX.Mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Head_Wet_Tongue2.png",
            "'chin' in LauraX.Spunk", "images/LauraSprite/Laura_Sprite_Head_Wet_Mouth.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #brows
            "LauraX.Blush >= 2", ConditionSwitch(
                    "LauraX.Brows == 'normal'", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Normal_B.png",
                    "LauraX.Brows == 'angry'", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Angry_B.png",
                    "LauraX.Brows == 'sad'", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Sad_B.png",
                    "LauraX.Brows == 'surprised'", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Surprised_B.png",
                    "LauraX.Brows == 'confused'", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Confused_B.png",
                    "True", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Normal_B.png",
                    ),
            "True", ConditionSwitch(
                    "LauraX.Brows == 'normal'", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Normal.png",
                    "LauraX.Brows == 'angry'", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Angry.png",
                    "LauraX.Brows == 'sad'", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Sad.png",
                    "LauraX.Brows == 'surprised'", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Surprised.png",
                    "LauraX.Brows == 'confused'", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Confused.png",
                    "True", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Normal.png",
                    ),
            ),
        (0,0), "Laura Blink",     #Eyes
        (0,0), ConditionSwitch(
            #Hair mid
            "LauraX.Over == 'jacket'", Null(),
            "renpy.showing('Laura_TJ_Animation')", Null(),
            "renpy.showing('Laura_Sex_Animation')", Null(),
            "LauraX.Hair == 'wet' or LauraX.Water", Null(),
            "not Player.Male and 'facial' in LauraX.Spunk",Null(),
            "LauraX.Hair", Recolor("Laura", "Hair", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Long_Mid.png"),
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Face Water
#            "not LauraX.Water", Null(),
#            "True", "images/LauraSprite/Laura_Sprite_Wet_Head.png",
#            ),
        (0,0), ConditionSwitch(
            #Hair over
            "not LauraX.Hair", Null(),
            "renpy.showing('Laura_TJ_Animation')", Null(),
            "renpy.showing('Laura_SexSprite')", Recolor("Laura", "Hair", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Long_OverSex.png"),
            "LauraX.Hair == 'wet' or LauraX.Water", Recolor("Laura", "Hair", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Wet_Over.png"),
            "not Player.Male and 'facial' in LauraX.Spunk",Recolor("Laura", "Hair", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Wet_Over.png"),
            "LauraX.Hair", Recolor("Laura", "Hair", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Long_Over.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hair Water
            "not LauraX.Water and not (not Player.Male and 'facial' in LauraX.Spunk)", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Head_Wet.png",
#            "True", Recolor("Laura", "Hair", "images/LauraSprite/Laura_Sprite_Hair_Wet.png"),
            ),
        # Modification mode
        (0,0), ConditionSwitch(
            # hat
            "LauraX.Hat == 'bunny ears'", "images/LauraSprite/modification/Laura_sprite_hat_bunny_ears.png",
            "True", Null(),
        ),
        # -----------------
        (0,0), ConditionSwitch(
            #facial spunk
            "'hair' in LauraX.Spunk and Player.Male", "images/LauraSprite/Laura_Sprite_Spunk_Facial2.png",
            "'facial' in LauraX.Spunk and Player.Male", "images/LauraSprite/Laura_Sprite_Spunk_Facial1.png",
            "True", Null(),
            ),
        )
    anchor (0.6, 0.0)
    zoom .5

image Laura Blink:
    ConditionSwitch(
    "LauraX.Eyes == 'sexy'", "images/LauraSprite/Laura_Sprite_Eyes_Squint.png",
    "LauraX.Eyes == 'side'", "images/LauraSprite/Laura_Sprite_Eyes_Side.png",
    "LauraX.Eyes == 'surprised'", "images/LauraSprite/Laura_Sprite_Eyes_Surprised.png",
    "LauraX.Eyes == 'normal'", "images/LauraSprite/Laura_Sprite_Eyes_Normal.png",
    "LauraX.Eyes == 'stunned'", "images/LauraSprite/Laura_Sprite_Eyes_Stunned.png",
    "LauraX.Eyes == 'down'", "images/LauraSprite/Laura_Sprite_Eyes_Down.png",
    "LauraX.Eyes == 'closed'", "images/LauraSprite/Laura_Sprite_Eyes_Closed.png",
    "LauraX.Eyes == 'leftside'", "images/LauraSprite/Laura_Sprite_Eyes_Leftside.png",
    "LauraX.Eyes == 'manic'", "images/LauraSprite/Laura_Sprite_Eyes_Normal.png",
    "LauraX.Eyes == 'squint'", "Laura_Squint",
    "True", "images/LauraSprite/Laura_Sprite_Eyes_Normal.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/LauraSprite/Laura_Sprite_Eyes_Closed.png"
    .25
    repeat

image Laura_Squint:
    "images/LauraSprite/Laura_Sprite_Eyes_Normal.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/LauraSprite/Laura_Sprite_Eyes_Squint.png"
    .25
    repeat



image Laura_Drip_Mask:
    #This is the mask for her drip pattern
    contains:
        "images/LauraSprite/Laura_Sprite_WetMask.png"
        offset (-145,-560)#(-225,-560)

image Laura_Drip_MaskP:
    #This is the mask for her drip pattern in panties down mode
    contains:
        "images/LauraSprite/Laura_Sprite_WetMaskP.png"
        offset (-145,-560)#(-225,-560)

# End Laura Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#if there is a problem, remove Doggy form here and put it at the bottom.

# Laura Doggy Compositing ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#image Laura_Doggy_Base = LiveComposite(
image Laura_Doggy_Animation: #nee Laura_Doggy
    LiveComposite(
        #Base body
        (420,750),
        (0,0), ConditionSwitch(
            #Shows different upper body motion depending on events
            "not Player.Sprite", "Laura_Doggy_Body",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Laura_Doggy_Fuck2_Top",
                    "Speed > 1", "Laura_Doggy_Fuck_Top",
                    "Speed", "Laura_Doggy_Anal_Head_Top",
                    "True", "Laura_Doggy_Body",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Laura_Doggy_Fuck2_Top",
                    "Speed > 1", "Laura_Doggy_Fuck_Top",
                    "True", "Laura_Doggy_Body",
                    ),
            "Player.Cock == 'foot'", ConditionSwitch(
                    "Speed > 1", "Laura_Doggy_Foot2_Top",
                    "Speed", "Laura_Doggy_Foot1_Top",
                    "True", "Laura_Doggy_Foot0_Top",
                    ),
            "True", "Laura_Doggy_Body",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events
            "not Player.Sprite", "Laura_Doggy_Ass",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Laura_Doggy_Fuck2_Ass",
                    "Speed > 1", "Laura_Doggy_Fuck_Ass",
                    "Speed", "Laura_Doggy_Anal_Head_Ass",
                    "True", "Laura_Doggy_Ass",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Laura_Doggy_Fuck2_Ass",
                    "Speed > 1", "Laura_Doggy_Fuck_Ass",
                    "True", "Laura_Doggy_Ass",
                    ),
            "Player.Cock == 'foot'", ConditionSwitch(
                    "Speed > 1", "Laura_Doggy_Foot2_Ass",
                    "Speed", "Laura_Doggy_Foot1_Ass",
                    "True", "Laura_Doggy_Foot0_Ass",
                    ),
            "True", "Laura_Doggy_Ass",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
#            "not Player.Sprite", "Laura_Doggy_Shins0",
            "Player.Sprite and Player.Cock == 'foot'", ConditionSwitch(
                    "Speed > 1", "Laura_Doggy_Feet2",
                    "Speed", "Laura_Doggy_Feet1",
                    "True", "Laura_Doggy_Feet0",
                    ),
            "ShowFeet", "Laura_Doggy_Shins0",# "not Player.Sprite and ShowFeet", "Laura_Doggy_Shins",
            "True", Null(),
            ),
        )
    align (0.6,0.0)
    #yoffset 50
# End Base / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Laura_Doggy_Body:
    LiveComposite(
        #Upper body
        (610,750),
        #(165,0),"Laura_Doggy_Hair_Under", #back of the hair
#        (0,60), "Laura_Doggy_Head",               #Head

        (0,60), ConditionSwitch(
            #head
            "LauraX.Facing", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Hair_Long_Fore.png",
            "True", "Laura_Doggy_Head",
            ),
        #(0,0), "images/LauraDoggy/Laura_Doggy_HeadRef.png",               #Head

        (0,0), "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Body.png", #Body base
        (0,0), ConditionSwitch(
            #tanktop
            "not LauraX.Chest", Null(),
#            "LauraX.Uptop", ConditionSwitch(
#                    "LauraX.Chest == 'lace bra' and LauraX.Over", Recolor("Laura", "Chest", "images/LauraDoggy/Laura_Doggy_Chest_GreenBra_Up2.png"),
#                    "LauraX.Chest == 'lace bra'", Recolor("Laura", "Chest", "images/LauraDoggy/Laura_Doggy_Chest_GreenBra_Up.png"),
#                    "LauraX.Chest == 'corset'", Recolor("Laura", "Chest", "images/LauraDoggy/Laura_Doggy_Chest_Corset_Up.png"),
#                    "LauraX.Chest == 'sports bra'", Recolor("Laura", "Chest", "images/LauraDoggy/Laura_Doggy_Chest_SportsBra_Up.png"),
#                    "LauraX.Chest == 'bikini top'", Recolor("Laura", "Chest", "images/LauraDoggy/Laura_Doggy_Chest_Bikini_Up.png"),
#                    "LauraX.Over", Recolor("Laura", "Chest", "images/LauraDoggy/Laura_Doggy_Chest_GreenBra_Up2.png"),
#                    "True", Recolor("Laura", "Chest", "images/LauraDoggy/Laura_Doggy_Chest_GreenBra_Up.png"),
#                    ),
            "LauraX.Chest == 'white tank'", Recolor("Laura", "Chest", "images/LauraDoggy/Laura_Doggy_Chest_Costume.png"),
            "LauraX.Chest == 'lace corset'", Recolor("Laura", "Chest", "images/LauraDoggy/Laura_Doggy_Chest_Corset.png"),
            "LauraX.Chest == 'corset'", Recolor("Laura", "Chest", "images/LauraDoggy/Laura_Doggy_Chest_Corset.png"),
            "LauraX.Chest == 'wolvie top'", Recolor("Laura", "Chest", "images/LauraDoggy/Laura_Doggy_Chest_Wolvie.png"),
            "LauraX.Chest == 'bikini top'", Recolor("Laura", "Chest", "images/LauraDoggy/Laura_Doggy_Chest_Bikini.png"),
            # Modification mode
            "LauraX.Chest == 'goth top'", "images/LauraDoggy/modification/Laura_doggy_chest_top_goth.png",
            # ----------------
            "True", Recolor("Laura", "Chest", "images/LauraDoggy/Laura_Doggy_Chest_Tank.png"),
            ),
#        (0,0), ConditionSwitch(
#            #Wet look
#            "LauraX.Water", "images/RogueDoggy/Rogue_Doggy_WetTop.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #suspenders
            "not LauraX.Legs", Null(), #hides when no skirt on
            "LauraX.Acc == 'suspenders'", "images/LauraDoggy/Laura_Doggy_Suspenders.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #gloves
            "LauraX.Arms == 'gloves'", Recolor("Laura", "Arms", "images/LauraDoggy/Laura_Doggy_Gloves.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Overshirt
            "not LauraX.Over", Null(),
            "LauraX.Over == 'jacket'", Recolor("Laura", "Over", "images/LauraDoggy/Laura_Doggy_Over_Jacket.png"),
            # Modification mode
            "LauraX.Over == 'top goth mesh'", "images/LauraDoggy/modification/Laura_doggy_over_goth_mesh.png",
            # -----------------
            "LauraX.Over == 'towel' and not LauraX.Uptop", Recolor("Laura", "Over", "images/LauraDoggy/Laura_Doggy_Over_TowelTop.png"),
            # Modification mode
            "LauraX.Over == 'bunny' and not LauraX.Uptop", "images/LauraDoggy/modification/Laura_doggy_over_bunny_suit_top.png",
            # -----------------
            "True", Null(),
            ),
        (0,0), ConditionSwitch(             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #spunk back Layer
            "'back' in LauraX.Spunk and Player.Male", "images/LauraDoggy/Laura_Doggy_Spunk_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast fondling animation
            "Trigger == 'fondle breasts' or Trigger2 == 'fondle breasts'", "Laura_Doggy_GropeBreast",
            "True", Null()
            ),
        #(161,-1), "Laura_Doggy_Head",               #Head
        #(165,0),"Laura_Doggy_Hair_Over", #front of the hair
        )
#    transform_anchor True
#    anchor (225,1400)
    offset (-175,25)#(-200,0)
    zoom .95
#    offset (-350,-180)#(-190,-40)
#    rotate 20
# End Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Laura_Doggy_Head:
    LiveComposite(
        #Head
        (420,525),
        #(0,0), "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Head.png", #Body base
        #(0,0), "images/LauraDoggy/Laura_Doggy_TestArm.png",#Eyes
        (0,0), ConditionSwitch(
            #Hair
            "LauraX.Water or LauraX.Hair == 'wet'", Recolor("Laura", "Hair", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Hair_Wet_Back.png"),
            "not Player.Male and 'facial' in LauraX.Spunk",Recolor("Laura", "Hair", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Hair_Wet_Back.png"),
            "True", Recolor("Laura", "Hair", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Hair_Long_Back.png"),
            ),
        (0,0), ConditionSwitch(
            #Head
            #"LauraX.Blush > 1", "images/LauraDoggy/Laura_Doggy_Head_Blush2.png",
            "LauraX.Blush", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Head_Blush.png",
            "True", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Head.png",
            ),
        (0,0), ConditionSwitch(
            #Mouth
            "LauraX.Mouth == 'normal'", Recolor("Laura", "Lips", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Mouth_Smile.png"),
            "LauraX.Mouth == 'lipbite'", Recolor("Laura", "Lips", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Mouth_Smile.png"),
            "LauraX.Mouth == 'sucking'", Recolor("Laura", "Lips", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Mouth_Open.png"),
            "LauraX.Mouth == 'kiss'", Recolor("Laura", "Lips", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Mouth_Kiss.png"),
            "LauraX.Mouth == 'sad'", Recolor("Laura", "Lips", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Mouth_Sad.png"),
            "LauraX.Mouth == 'smile'", Recolor("Laura", "Lips", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Mouth_Smile.png"),
            "LauraX.Mouth == 'grimace'", Recolor("Laura", "Lips", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Mouth_Smile.png"),
            "LauraX.Mouth == 'surprised'", Recolor("Laura", "Lips", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Mouth_Open.png"),
            "LauraX.Mouth == 'tongue'", Recolor("Laura", "Lips", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Mouth_Tongue.png"),
            "True", Recolor("Laura", "Lips", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Mouth_Smile.png"),
            ),
#        (0,0), ConditionSwitch(
#            #chin spunk
#            "'chin' in LauraX.Spunk", "images/LauraDoggy/Laura_Doggy_Spunk_Chin.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #Mouth spunk
#            "'mouth' not in LauraX.Spunk", Null(),
#            #"LauraX.Mouth == 'normal'", "images/LauraDoggy/Laura_Doggy_Spunk_Normal.png",
#            #"LauraX.Mouth == 'sad'", "images/LauraDoggy/Laura_Doggy_Spunk_Normal.png",
#            "LauraX.Mouth == 'lipbite'", "images/LauraDoggy/Laura_Doggy_Spunk_Smile.png",
#            "LauraX.Mouth == 'smile'", "images/LauraDoggy/Laura_Doggy_Spunk_Smile.png",
#            "LauraX.Mouth == 'grimace'", "images/LauraDoggy/Laura_Doggy_Spunk_Smile.png",
#            "LauraX.Mouth == 'sucking'", "images/LauraDoggy/Laura_Doggy_Spunk_Open.png",
#            #"LauraX.Mouth == 'kiss'", "images/LauraDoggy/Laura_Doggy_Spunk_Open.png",
#            "LauraX.Mouth == 'surprised'", "images/LauraDoggy/Laura_Doggy_Spunk_Open.png",
#            "LauraX.Mouth == 'tongue'", "images/LauraDoggy/Laura_Doggy_Spunk_Open.png",
#            "True", "images/LauraDoggy/Laura_Doggy_Spunk_Normal.png",
#            ),
        (0,0), ConditionSwitch(
            #Brows
            #"LauraX.Brows == 'normal'", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Brows_Normal.png",
            "LauraX.Brows == 'angry'", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Brows_Angry.png",
            "LauraX.Brows == 'sad'", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Brows_Sad.png",
            "LauraX.Brows == 'surprised'", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Brows_Surprised.png",
            #"LauraX.Brows == 'confused'", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Brows_Normal.png",
            "True", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Brows_Normal.png",
            ),
        (0,0), "Laura Doggy Blink",#Eyes
#        (0,0), ConditionSwitch(
#            #Wet look
#            "LauraX.Water", "images/RogueDoggy/Rogue_Doggy_WetTop.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #face spunk
            "'facial' in LauraX.Spunk and Player.Male", "images/LauraDoggy/Laura_Doggy_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hair
            "LauraX.Water or LauraX.Hair == 'wet'", Recolor("Laura", "Hair", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Hair_Wet.png"),
            "not Player.Male and 'facial' in LauraX.Spunk",Recolor("Laura", "Hair", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Hair_Wet.png"),
            "True", Recolor("Laura", "Hair", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Hair_Long.png"),
            ),
        (0,0), ConditionSwitch(
            #face spunk
            "'hair' in LauraX.Spunk and Player.Male", "images/LauraDoggy/Laura_Doggy_Spunk_Hair.png",
            "True", Null(),
            ),
        # Modification mode
        (0,0), ConditionSwitch(
            "LauraX.Hat == 'bunny ears'", "images/LauraDoggy/modification/Laura_doggy_hat_bunny_ears.png",
            "True", Null(),
        ),
        # ----------------
        )
    #zoom 0.95
    #alpha 0.5
# End Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Laura Doggy Blink:
        #Eyes
        ConditionSwitch(
        "LauraX.Eyes == 'sexy'", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Eyes_Sexy.png",
        "LauraX.Eyes == 'side'", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Eyes_Side.png",
        "LauraX.Eyes == 'normal'", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Eyes_Sexy.png",
        "LauraX.Eyes == 'closed'", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Eyes_Closed.png",
        "LauraX.Eyes == 'manic'", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Eyes_Stunned.png",
        "LauraX.Eyes == 'down'", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Eyes_Sexy.png",
        "LauraX.Eyes == 'stunned'", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Eyes_Stunned.png",
        "LauraX.Eyes == 'surprised'", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Eyes_Surprised.png",
        "LauraX.Eyes == 'squint'", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Eyes_Sexy.png",
        "True", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Eyes_Normal.png",
        ),
    #    choice:
    #        3.5
    #    choice:
    #        3.25
    #    choice:
    #        3
        3
        # This randomizes the time between blinking.
        "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Eyes_Closed.png"
        .25
        repeat

image Laura_Doggy_Ass:
    LiveComposite(
        #Lower body
        (420,750),
#        (0,0), ConditionSwitch(
#            #Legs backside
#            "LauraX.Legs == 'skirt'",Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_Skirt_Back.png"),
#            "not LauraX.Upskirt", Null(),
#            "LauraX.Legs == 'pants'", Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_Pants_Back.png"),
#            "LauraX.Legs == 'yoga pants'", Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_Yoga_Back.png"),
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Panties back
            "not LauraX.PantiesDown or (LauraX.Legs == 'pants' and not LauraX.Upskirt)", Null(),
            "LauraX.Panties == 'wolvie panties'", Recolor("Laura", "Panties", "images/LauraDoggy/Laura_Doggy_Panties_Wolvie_Back.png"),
            "LauraX.Panties == 'lace panties'", Recolor("Laura", "Panties", "images/LauraDoggy/Laura_Doggy_Panties_Lace_Back.png"),
            "LauraX.Panties", Recolor("Laura", "Panties", "images/LauraDoggy/Laura_Doggy_Panties_Back.png"),
            "True", Null(),
            ),
#        (0,0), "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Ass.png", #Ass Base


        (0,0), ConditionSwitch(
            #Pussy base
            "LauraX.Legs and not LauraX.Upskirt", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Ass_Closed.png",
            "LauraX.Panties and not LauraX.PantiesDown", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Ass_Closed.png",
            "Player.Sprite and Player.Cock == 'in'", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Ass_Fucked.png",
            "Trigger == 'lick pussy'", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Ass_Open.png",
            "'dildo pussy' in (Trigger,Trigger2,LauraX.Offhand)", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Ass_Fucked.png",#Null(),
            "'fondle pussy' in (Trigger,Trigger2,LauraX.Offhand)", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Ass_Fucked.png",#Null(),
            "Trigger == 'insert pussy'", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Ass_Fucked.png",#Null(),
            "True", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Ass_Closed.png",
            ),
        (0,0), ConditionSwitch(
            #ass red
            "LauraX.Red", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Red.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Anus base
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    "Speed", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Anal_FullBase.png",      #Speed 1
                    "True", Null(),               #Speed 0
                    ),
            "'insert ass' in (Trigger,Trigger2,LauraX.Offhand)", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Anal_FullBase.png",
            "'dildo anal' in (Trigger,Trigger2,LauraX.Offhand)", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Anal_FullBase.png",
            "LauraX.Loose > 2", "Laura_Gape_Anal",    #intentional
            "True", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Asshole_Loose.png",
#            "True", "images/LauraDoggy/Laura_Doggy_Asshole_Tight.png",
            ),

#        (0,0), ConditionSwitch(
#            #Wet look
#            "LauraX.Water", "images/RogueDoggy/Rogue_Doggy_WetAss.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #Hose
            "LauraX.Hose == 'black stockings'", Recolor("Laura", "Hose", "images/LauraDoggy/Laura_Doggy_Stocking.png"),
            "LauraX.Hose == 'stockings'", Recolor("Laura", "Hose", "images/LauraDoggy/Laura_Doggy_Hose.png"),
#            "Player.Sprite and Player.Cock == 'in'", Null(),
#            "Player.Sprite and Player.Cock == 'anal'", Null(),
            "LauraX.Hose == 'stockings and garterbelt'", Recolor("Laura", "Hose", "images/LauraDoggy/Laura_Doggy_StockingsGarter.png"),
            "LauraX.Hose == 'garterbelt'", Recolor("Laura", "Hose", "images/LauraDoggy/Laura_Doggy_Garters.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Panties if Down
            "not LauraX.PantiesDown or (LauraX.Legs == 'pants' and not LauraX.Upskirt)", Null(),
            "LauraX.Panties == 'wolvie panties'", Recolor("Laura", "Panties", "images/LauraDoggy/Laura_Doggy_Panties_Wolvie_Down.png"),
            "LauraX.Panties == 'bikini bottoms'", Recolor("Laura", "Panties", "images/LauraDoggy/Laura_Doggy_Panties_Bikini_Down.png"),
            "LauraX.Panties", Recolor("Laura", "Panties", "images/LauraDoggy/Laura_Doggy_Panties_Black_Down.png"),
            "True", Null(),
            ),


        (0,0), ConditionSwitch(
            #spunkpussy Layer
            "'in' in LauraX.Spunk and Player.Cock == 'in' and Player.Male",Null(),# "images/LauraDoggy/Laura_Doggy_SpunkPussyOpen.png",  #fix for LauraX.Spunk is used later
            "'in' in LauraX.Spunk and Player.Male", "images/LauraDoggy/Laura_Doggy_SpunkPussyClosed.png",
            "LauraX.Wet and Player.Cock == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "LauraX.Wet", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pubes
            "not LauraX.Pubes", Null(),
            "Player.Sprite and Player.Cock == 'in'", Null(), # "images/LauraDoggy/Laura_Doggy_Pubes_Fucked.png",
            "'dildo pussy' in (Trigger,Trigger2,LauraX.Offhand)", Null(),
            "'fondle pussy' in (Trigger,Trigger2,LauraX.Offhand)", Null(),
            "Trigger == 'insert pussy'", Null(),
            "LauraX.Legs == 'pants' and not LauraX.Upskirt", Recolor("Laura", "Pubes", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Pubes_Panties.png"),
            "LauraX.Legs == 'mesh pants' and not LauraX.Upskirt", Recolor("Laura", "Pubes", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Pubes_Panties.png"),
            "LauraX.PantiesDown and Trigger == 'lick pussy'", Recolor("Laura", "Pubes", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Pubes_Open.png"),
            "LauraX.PantiesDown", Recolor("Laura", "Pubes", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Pubes.png"),
            "LauraX.Panties", Recolor("Laura", "Pubes", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Pubes_Panties.png"),
            "LauraX.Hose and LauraX.Hose == 'pantyhose'", Recolor("Laura", "Pubes", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Pubes_Panties.png"),
            "Trigger == 'lick pussy'", Recolor("Laura", "Pubes", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Pubes_Open.png"),
            "True", Recolor("Laura", "Pubes", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Pubes.png"),
            ),
        (0,0), ConditionSwitch(
            #Pussy Piercings
            "Player.Sprite", Null(),
            "LauraX.Pierce == 'ring'", "images/LauraDoggy/Laura_Doggy_Pierce_Ring.png",
            "LauraX.Pierce == 'barbell'", "images/LauraDoggy/Laura_Doggy_Pierce_Barbell.png",
            "True", Null(),
            ),


        (2,-8), ConditionSwitch(
            #spunkanal Layer
            "'anal' not in LauraX.Spunk or (Player.Sprite and Player.Cock == 'anal' and Speed >= 1) or not Player.Male", Null(),
#            "Player.Cock == 'anal'", "images/LauraDoggy/Laura_Doggy_SpunkAnalOpen.png",
            "LauraX.Loose", "images/LauraDoggy/Laura_Doggy_SpunkAnalLoose.png",
            "True", "images/LauraDoggy/Laura_Doggy_SpunkAnalLoose.png",
            ),
        (0,0), ConditionSwitch(
            #Panties if up
            "LauraX.PantiesDown or not LauraX.Panties", Null(),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),
            "LauraX.Panties == 'wolvie panties' and LauraX.Wet", Recolor("Laura", "Panties", "images/LauraDoggy/Laura_Doggy_Panties_Wolvie_Wet.png"),
            "LauraX.Panties == 'wolvie panties'", Recolor("Laura", "Panties", "images/LauraDoggy/Laura_Doggy_Panties_Wolvie.png"),
            "LauraX.Panties == 'lace panties'", Recolor("Laura", "Panties", "images/LauraDoggy/Laura_Doggy_Panties_Lace.png"),
            "LauraX.Panties == 'bikini bottoms'", Recolor("Laura", "Panties", "images/LauraDoggy/Laura_Doggy_Panties_Bikini.png"),
            "LauraX.Wet", Recolor("Laura", "Panties", "images/LauraDoggy/Laura_Doggy_Panties_Black_Wet.png"),
            "True", Recolor("Laura", "Panties", "images/LauraDoggy/Laura_Doggy_Panties_Black.png"),
            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #full hose/tights
            "LauraX.Panties and LauraX.PantiesDown", Null(),
            "LauraX.Hose == 'ripped pantyhose'", Recolor("Laura", "Hose", "images/LauraDoggy/Laura_Doggy_Hose_Pantyhose_Holed.png"),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
            "LauraX.Hose == 'pantyhose'", Recolor("Laura", "Hose", "images/LauraDoggy/Laura_Doggy_Hose_Pantyhose.png"),
            # Modification mode
            "LauraX.Hose == 'pantyhose brown'", "images/LauraDoggy/modification/Laura_doggy_hose_pantyhose_brown.png",
            "LauraX.Hose == 'pantyhose brown ripped'", "images/LauraDoggy/modification/Laura_doggy_hose_pantyhose_brown_ripped.png",
            "LauraX.Hose == 'tights mesh torn'", "images/LauraDoggy/modification/Laura_doggy_hose_tights_mesh_torn.png",
            # ----------------
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Legs Layer
            "LauraX.Legs == 'leather pants'", ConditionSwitch(
                    "LauraX.Upskirt or LauraX.PantiesDown", Null(), #Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_Pants_Down.png"),
                    #"LauraX.Wet > 1", Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_Pants_Wet.png"),
                    "True", Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_Pants.png"),
                    ),
            "LauraX.Legs == 'mesh pants'", ConditionSwitch(
                    "LauraX.Upskirt or LauraX.PantiesDown", Null(), #Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_Pants_Down.png"),
                    #"LauraX.Wet > 1", Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_Pants_Wet.png"),
                    "True", Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_MeshPants.png"),
                    ),
#            "LauraX.Legs == 'yoga pants'", ConditionSwitch(
#                    "LauraX.Upskirt", Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_Yoga_Down.png"),
#                    "LauraX.Wet > 1", Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_Yoga_Wet.png"),
#                    "True", Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_Yoga.png"),
#                    ),
            "LauraX.Legs == 'other skirt'", ConditionSwitch(
                    "LauraX.Upskirt and Player.Sprite and Player.Cock == 'anal' and Speed" , Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_SkirtCos_Up.png"),   #Rogue_Doggy_Legs_Skirt_UpAnal.png",
                    "LauraX.Upskirt", Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_SkirtCos_Up.png"),
                    "True", Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_SkirtCos.png"),
                    ),
            "LauraX.Legs == 'skirt'", ConditionSwitch(
                    "LauraX.Upskirt and Player.Sprite and Player.Cock == 'anal' and Speed" , Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_SkirtCos_Up.png"),   #Rogue_Doggy_Legs_Skirt_UpAnal.png",
                    "LauraX.Upskirt", Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_SkirtCos_Up.png"),
                    "True", Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_Skirt.png"),
                    ),
            # Modification mode
            "LauraX.Legs == 'leggings goth'", ConditionSwitch(
                "LauraX.Upskirt or LauraX.PantiesDown", Null(), #Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_Pants_Down.png"),
                #"LauraX.Wet > 1", Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_Pants_Wet.png"),
                "True", "images/LauraDoggy/modification/Laura_doggy_legs_leggings_goth.png",
            ),
            "LauraX.Legs == 'leggings goth torn'", ConditionSwitch(
                "LauraX.Upskirt or LauraX.PantiesDown", Null(), #Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_Pants_Down.png"),
                #"LauraX.Wet > 1", Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_Pants_Wet.png"),
                "True", "images/LauraDoggy/modification/Laura_doggy_legs_leggings_goth_torn.png",
            ),
            "LauraX.Legs == 'pants goth torn'", ConditionSwitch(
                "LauraX.Upskirt or LauraX.PantiesDown", Null(), #Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_Pants_Down.png"),
                #"LauraX.Wet > 1", Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_Pants_Wet.png"),
                "True", "images/LauraDoggy/modification/Laura_doggy_legs_pants_goth_torn.png",
            ),
            "LauraX.Legs == 'short skirt goth'", ConditionSwitch(
                "LauraX.Upskirt or LauraX.PantiesDown", Null(), #Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_Pants_Down.png"),
                #"LauraX.Wet > 1", Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Legs_Pants_Wet.png"),
                "True", "images/LauraDoggy/modification/Laura_doggy_legs_short_skirt_goth.png",
            ),
            # ------------------
            "True", Null(),
            ),
        (0,0), ConditionSwitch(             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #Over Layer
            "LauraX.Over == 'towel' and LauraX.Upskirt", Recolor("Laura", "Over", "images/LauraDoggy/Laura_Doggy_Over_TowelAss_Up.png"),
            "LauraX.Over == 'towel'", Recolor("Laura", "Over", "images/LauraDoggy/Laura_Doggy_Over_TowelAss.png"),
            # Modification mode
            "LauraX.Over == 'bunny'", "images/LauraDoggy/modification/Laura_doggy_over_bunny_suit_ass.png",
            # ----------------
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Pussy Piercings clothed
            "Player.Sprite", Null(),
            "LauraX.PantiesDown or (not LauraX.Panties and LauraX.Legs != 'leather pants')", Null(), #if not panties or legs, skip this
            "LauraX.Pierce == 'ring'", "images/LauraDoggy/Laura_Doggy_Pierce_RingC.png",
            "LauraX.Pierce == 'barbell'", "images/LauraDoggy/Laura_Doggy_Pierce_BarbellC.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Pussy Composite
            "LauraX.Legs and not LauraX.Upskirt",Null(),
            "LauraX.Panties and not LauraX.PantiesDown", Null(),
            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Laura_Pussy_Fucking3",#Speed 3
                    "Speed > 1", "Laura_Pussy_Fucking2",#Speed 2
                    "Speed", "Laura_Pussy_Heading",      #Speed 1
                    "True", "Laura_Pussy_Static",              #Speed 0
                    ),
            "'dildo pussy' in (Trigger,Trigger2,LauraX.Offhand)", "Laura_Pussy_Fucking2",
            "'fondle pussy' in (Trigger,Trigger2,LauraX.Offhand)", "Laura_Pussy_Fingering",
            "Trigger == 'insert pussy'", "Laura_Pussy_Fingering",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Anus Composite
            "LauraX.Legs and not LauraX.Upskirt",Null(),
            "LauraX.Panties and not LauraX.PantiesDown", Null(),
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Laura_Anal_Fucking2", #Speed 3
                    "Speed > 1", "Laura_Anal_Fucking",  #Speed 2
                    "Speed", "Laura_Anal_Heading",      #Speed 1
                    "True", "Laura_Anal",               #Speed 0
                    ),
            "'insert ass' in (Trigger,Trigger2,LauraX.Offhand)", "Laura_Anal_Fingering",
            "'dildo anal' in (Trigger,Trigger2,LauraX.Offhand)", "Laura_Anal_Fucking",
            "LauraX.Plug", "images/PlugIn.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk back Layer
            "'back' in LauraX.Spunk and Player.Male", "images/LauraDoggy/Laura_Doggy_Spunk_Ass.png",
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
            "LauraX.Over == 'towel'", Null(),
            "(LauraX.Legs == 'skirt' or LauraX.Legs == 'other skirt') and LauraX.Upskirt", Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Hotdog_Upskirt.png"),
            "True", "images/LauraDoggy/Laura_Doggy_HotdogBack.png",
            ),
        (0,0), ConditionSwitch(
            #Hotdogging Cock w/ alpha
            "not Player.Sprite or Player.Cock != 'out'", Null(),
            "(LauraX.Legs == 'skirt' or LauraX.Legs == 'other skirt') and LauraX.Upskirt and Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "(LauraX.Legs == 'skirt' or LauraX.Legs == 'other skirt') and LauraX.Upskirt", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
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


image Laura_Doggy_Feet:         #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
    contains:
            AlphaMask("Laura_Doggy_Shins", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Feet_Toes.png")

image Laura_Doggy_Shins:             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
    #Laura's footjob shins
    contains:
        "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Feet_Back.png"
#    contains:
#        "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Feet_Toes.png"
    contains:
            #hose legs
        ConditionSwitch(
            "not LauraX.Hose", Null(),
            "LauraX.Hose == 'stockings'", Recolor("Laura", "Hose", "images/LauraDoggy/Laura_Doggy_Feet_Hose_Back.png"),
            "LauraX.Hose == 'stockings and garterbelt'", Recolor("Laura", "Hose", "images/LauraDoggy/Laura_Doggy_Feet_Hose_Back.png"),
            "LauraX.Hose == 'black stockings'", Recolor("Laura", "Hose", "images/LauraDoggy/Laura_Doggy_Feet_Stockings_Back.png"),
            "LauraX.Hose == 'pantyhose'", Recolor("Laura", "Hose", "images/LauraDoggy/Laura_Doggy_Feet_Pantyhose.png"),
            "LauraX.Hose == 'ripped pantyhose'", Recolor("Laura", "Hose", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Feet_Pantyhose_Holed.png"),
            # Modification mode
            "LauraX.Hose == 'pantyhose brown'", "images/LauraDoggy/modification/Laura_doggy_hose_pantyhose_brown_feet.png",
            "LauraX.Hose == 'pantyhose brown ripped'", "images/LauraDoggy/modification/Laura_doggy_hose_pantyhose_brown_ripped_feet.png",
            # -----------------
            "True", Null(),
            )
    contains:
        #pants
        ConditionSwitch(
            "LauraX.Legs == 'leather pants'", Recolor("Laura", "Legs", "images/LauraDoggy/Laura_Doggy_Feet_Pants.png"),
            "True", Null(),
            )
    contains:
        #spunk
        ConditionSwitch(
            "'feet' in LauraX.Spunk and Player.Male", "images/LauraDoggy/Laura_Doggy_Spunk_Feet.png",
            "True", Null(),
            )
#    pos (0,0)

image Laura_Doggy_Shins0:
        #static animation
        "Laura_Doggy_Shins"
        offset (0, 150) #(0,0) top


image Laura_Doggy_GropeBreast:
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

image Laura_Gape_Anal:
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

image Zero_Laura_Hotdog_Static:
    # The unmoving version of the hotdog cock
    # called in Doggy Ass LC
    contains:
        "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Laura_Hotdog_Moving:
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


image Laura_Pussy_Mask:
    #AlphaMask used to prevent the cock from moving past the pussy
    #Called in "Laura_Pussy_Moving"
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

image Laura_Pussy_Mask_Static:
    #AlphaMask used to prevent the cock from moving past the pussy in static pose
    #Called in "Laura_Pussy_Moving"
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


image Laura_Pussy_Static:
    #Full Animation for speed 0
    subpixel True
    contains:
        #moving hole
        "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Pussy_FHole.png"
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
            "LauraX.Pubes", Recolor("Laura", "Pubes", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Pubes_Open.png"),
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
            "LauraX.Pierce == 'barbell'", "images/LauraDoggy/Laura_Doggy_Pierce_Barbell.png",
            "LauraX.Pierce == 'ring'", "images/LauraDoggy/Laura_Doggy_Pierce_Ring.png",
            "True", Null(),
            )
        offset (-3,8)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in LauraX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
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
        AlphaMask("Zero_Laura_Doggy_Static", "Laura_Pussy_Mask_Static")

    contains:
        # expanding pussy flap
        AlphaMask("Laura_PussyHole_Static", "Laura_Pussy_Hole_Mask_Static")

image Laura_Pussy_Hole_Mask_Static:
    # This is the alpha used for the little flap in the heading animation "Laura_Pussy_Moving"
    contains:
        #Base
        AlphaMask("images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat

image Laura_PussyHole_Static:
    #This is the image impacted by the mask for the pussy flap in "Laura_Pussy_Moving"
    contains:
        #Mask
        "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 512
            pause 1
            ease 3 ypos 515
            repeat


image Zero_Laura_Doggy_Static:
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

image Laura_Pussy_Heading:
    #Full Animation for speed 1
    subpixel True
    contains:
        #moving hole
        "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Pussy_FHole.png"
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
            "LauraX.Pubes", Recolor("Laura", "Pubes", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Pubes_F.png"),
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
            "LauraX.Pierce == 'barbell'", "images/LauraDoggy/Laura_Doggy_Pierce_Barbell.png",
            "LauraX.Pierce == 'ring'", "images/LauraDoggy/Laura_Doggy_Pierce_Ring.png",
            "True", Null(),
            )
        offset (-3,8)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in LauraX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
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
        AlphaMask("Zero_Laura_Doggy_Heading", "Laura_Pussy_Mask")

    contains:
        # expanding pussy flap
        AlphaMask("Laura_Pussy_Heading_Flap", "Laura_Pussy_Hole_Mask")
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in LauraX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
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


image Laura_Pussy_Hole_Mask:
    # This is the alpha used for the little flap in the heading animation "Laura_Pussy_Heading"
    contains:
        #Base
        AlphaMask("images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat

image Laura_Pussy_Heading_Flap:
    #This is the image impacted by the mask for the pussy flap in "Laura_Pussy_Heading"
    contains:
        #Mask
        "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 505
            pause 1
            ease 3 ypos 515
            repeat

image Laura_Pussy_Fingering:
    #Full Animation for speed 1
    subpixel True
    contains:
        #moving hole
        "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Pussy_FHole.png"
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
            "LauraX.Pubes", Recolor("Laura", "Pubes", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Pubes_Open.png"),
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
            "LauraX.Pierce == 'barbell'", "images/LauraDoggy/Laura_Doggy_Pierce_Barbell.png",
            "LauraX.Pierce == 'ring'", "images/LauraDoggy/Laura_Doggy_Pierce_Ring.png",
            "True", Null(),
            )
        offset (-3,8)

    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in LauraX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
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
    contains:
        # expanding pussy flap
        AlphaMask("Laura_Pussy_Heading_Flap", "Laura_Pussy_Hole_Mask")

    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in LauraX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
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


image Zero_Laura_Doggy_Heading:
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

image Laura_Pussy_Fucking2:
    #Full Animation for speed 2
    contains:
        #Base
        "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Pussy_FHole.png"
    contains:
        #pubes
        ConditionSwitch(
            "LauraX.Pubes", Recolor("Laura", "Pubes", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Pubes_F.png"),
            "True", Null(),
            )
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "LauraX.Pierce == 'barbell'", "images/LauraDoggy/Laura_Doggy_Pierce_Barbell.png",
            "LauraX.Pierce == 'ring'", "images/LauraDoggy/Laura_Doggy_Pierce_Ring.png",
            "True", Null(),
            )
        offset (-3,8)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in LauraX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            "'dildo pussy' in (Trigger,Trigger2,LauraX.Offhand)", AlphaMask("Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "True",AlphaMask("Zero_Laura_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            ),
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in LauraX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )


image Zero_Laura_Doggy_Fucking2:
    # Sex Speed 2 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat


image Laura_Pussy_Fucking3:
    #Full Animation for speed 3
    contains:
        #Base
        "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Pussy_FHole.png"
    contains:
        #pubes
        ConditionSwitch(
            "LauraX.Pubes", Recolor("Laura", "Pubes", "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Pubes_F.png"),
            "True", Null(),
            )
    contains:
        ConditionSwitch(
            #Pussy Piercings
            "LauraX.Pierce == 'barbell'", "images/LauraDoggy/Laura_Doggy_Pierce_Barbell.png",
            "LauraX.Pierce == 'ring'", "images/LauraDoggy/Laura_Doggy_Pierce_Ring.png",
            "True", Null(),
            )
        offset (-3,8)
    contains:
        #moving spunk under
        ConditionSwitch(
            "'in' in LauraX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Laura_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
    contains:
        #moving spunk
        ConditionSwitch(
            "'in' in LauraX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Pussy_Open.png",
            "True", Null(),
            )


image Zero_Laura_Doggy_Fucking3:
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

image Laura_Anal:
    #Anal static Loose
    contains:
        #Base
        "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Asshole_Loose.png"
        anchor (0.50,0.69)
        pos (208,500)
        zoom 1.25
    contains:
        #Cock
        "Zero_Doggy_Insert"
        pos (172,500)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Laura_Anal_Fingering:
    #Animation for speed 1
    contains:
        #Hole
        "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Anal_FullHole.png"
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
            "'anal' in LauraX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
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
        AlphaMask("Zero_Laura_Doggy_Anal_Finger", "Laura_Doggy_Anal_Fingering_Mask")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in LauraX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
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

image Zero_Laura_Doggy_Anal_Finger:
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
image Laura_Doggy_Anal_Fingering_Mask:
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
image Laura_Anal_Heading:
    #Animation for speed 1
    contains:
        #Hole
        "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Anal_FullHole.png"
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
            "'anal' in LauraX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
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
        AlphaMask("Zero_Laura_Doggy_Anal_Heading", "Laura_Doggy_Anal_Heading_Mask")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in LauraX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
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

image Zero_Laura_Doggy_Anal_Heading:
        #the cock anal heading animation
    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500#505
            repeat

image Zero_Laura_Doggy_Anal_HeadingJunk:
    #this is a mask to correct an annoying glitch in the core mask
    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease .5 ypos 550
            pause .25
            ease 1.75 ypos 600#505
            repeat

image Laura_Doggy_Anal_Heading_Mask:
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

image Laura_Doggy_Anal_Head_Top:
#animation for anal fucking top half
    contains:
        subpixel True
        "Laura_Doggy_Body"
        ypos 0
        block:
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat

image Laura_Doggy_Anal_Head_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Laura_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -10
            easeout .1 ypos -7
            easein .9 ypos 0
            pause .9
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Laura_Doggy_Anal1:
    #Animation for speed 2 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat

image Laura_Anal_Fucking:
    #Animation for speed 2 Ass
    contains:
        #Hole
        "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Anal_FullHole.png"
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in LauraX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            #full hose/tights
            "'dildo anal' in (Trigger,Trigger2,LauraX.Offhand)", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", AlphaMask("Zero_Laura_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            )
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in LauraX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )


image Laura_Doggy_Fuck_Top:
    #animation for anal fucking top half
    contains:
        subpixel True
        "Laura_Doggy_Body"
        ypos 15#28
        pause .4
        block:
            ease .2 ypos 5#10
            pause .3
            ease 2 ypos 15#28
            repeat

image Laura_Doggy_Fuck_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Laura_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15#-25
            ease .1 ypos -5#-15
            pause .2
            ease 1.6 ypos 0
            repeat


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Laura_Doggy_Anal2:
    #Animation for speed 3 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat

image Laura_Anal_Fucking2:
    #Animation for speed 3 Ass
    contains:
        #Hole
        "images/LauraDoggy/[LauraX.skin_image.skin_path]Laura_Doggy_Anal_FullHole.png"
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in LauraX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Fucking.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Laura_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")
    contains:
        #spunk over cock
        ConditionSwitch(
            "'anal' in LauraX.Spunk and Player.Male", "images/JubesDoggy/Jubes_Doggy_Spunk_Anal_Over.png",
            "True", Null(),
            )

image Laura_Doggy_Fuck2_Top:
    #animation for anal fucking2 top half
    contains:
        subpixel True
        "Laura_Doggy_Body"
        ypos 20
        block:
            pause .15
            ease .1 ypos 0
            pause .1
            easein .5 ypos 20
            pause .05
            repeat

image Laura_Doggy_Fuck2_Ass:
    #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Laura_Doggy_Ass"
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

image Laura_Doggy_Feet0:
    #static animation
    contains:
        "Laura_Doggy_Shins"
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
        "Laura_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            subpixel True
            pause .5
            ease 2 ypos 20
            pause .5
            ease 2 ypos 0
            repeat

image Laura_Doggy_Foot0_Top:
    #animation for footjob top half
    contains:
        subpixel True
        "Laura_Doggy_Body"
        ypos 10#28
        #pause .4
        block:
            pause .5
            ease 2 ypos 14
            pause .5
            ease 2 ypos 10
            repeat

image Laura_Doggy_Foot0_Ass:
    #animation for footjob ass half
    contains:
        subpixel True
        "Laura_Doggy_Ass"
        ypos 0
        block:     #total 3
            pause .1 #.5
            ease 2 ypos 10
            pause .5
            ease 2.4 ypos 0
            repeat


image Laura_Doggy_Feet1:
    #slow animation
    contains:
        "Laura_Doggy_Shins"
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
        "Laura_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat

image Laura_Doggy_Foot1_Top:
    #animation for footjob top half
    contains:
        subpixel True
        "Laura_Doggy_Body"
        ypos 70#28
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 70
            repeat

image Laura_Doggy_Foot1_Ass:
    #animation for footjob ass half
    contains:
        subpixel True
        "Laura_Doggy_Ass"
        ypos 0
        block: #total 3
            pause .3
            ease 2 ypos 80
            ease .7 ypos 0
            repeat


image Laura_Doggy_Feet2:
    #fast animation
    contains:
        "Laura_Doggy_Shins"
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
        "Laura_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat

image Laura_Doggy_Foot2_Top:
    #animation for footjob top half
    contains:
        subpixel True
        "Laura_Doggy_Body"
        ypos 70#28
        block:
            pause .05
            ease .6 ypos 90#90#110
            ease .3 ypos 70#70
            repeat

image Laura_Doggy_Foot2_Ass:
    #animation for footjob ass half
    contains:
        subpixel True
        "Laura_Doggy_Ass"
        ypos 70
        block: #total .95
            pause .15#.05
            ease .6 ypos 90#110
            ease .2 ypos 70
            repeat

# Footjob animations end > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Doggy Launch/Reset
label Laura_Doggy_Launch(Line = Trigger):
    if renpy.showing("Laura_Doggy_Animation"):
        return
    $ Speed = 0
    call Girl_Hide(LauraX,1)
    show Laura_Doggy_Animation at SpriteLoc(StageCenter+150) zorder 150
    with dissolve
    return

label Laura_Doggy_Reset:
    if not renpy.showing("Laura_Doggy_Animation"):
        return
#    $ Trigger = 0               #fix, not sure this is a good idea
    $ LauraX.ArmPose = 2
    $ LauraX.SpriteVer = 0
    hide Laura_Doggy_Animation
    call Girl_Hide(LauraX)
    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
            alpha 1 zoom 1 offset (0,0) anchor (0.6, 0.0)
    with dissolve
    $ Speed = 0
    return

# End Laura Doggy Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Start Laura Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Laura Sex element //////////////////////////////////////////////////////////////////////////// / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Laura_SexSprite:
    #core sex animation
    contains:
        ConditionSwitch(
            # Laura's upper body
            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                    # If during sex
                    "Speed == 1", "Laura_Sex_Body_S1",#heading
                    "Speed == 2", "Laura_Sex_Body_S2",#slow
                    "Speed == 3", "Laura_Sex_Body_S3",#fast
                    "Speed >= 4", "Laura_Sex_Body_S4",#cumming
                    "True",       "Laura_Sex_Body_S0",#Static
                    ),
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
#                    # If during Anal
                    "Speed == 1", "Laura_Sex_Body_A1",#heading
                    "Speed == 2", "Laura_Sex_Body_A2",#slow
                    "Speed == 3", "Laura_Sex_Body_A3",#fast
                    "Speed >= 4", "Laura_Sex_Body_A4",#cumming
                    "True",       "Laura_Sex_Body_A0",#Static
                    ),
            "Player.Cock == 'foot'", ConditionSwitch(
                    # If during Footjob
                    "not Player.Sprite","Laura_Sex_Body_F0",#Static
                    "Speed == 1", "Laura_Sex_Body_F1",#heading
                    "Speed >= 4", "Laura_Sex_Body_F0",#cumming
                    "Speed >= 2", "Laura_Sex_Body_F2",#slow
                    "True",       "Laura_Sex_Body_F0",#Static
                    ),

            "True", ConditionSwitch(
                    # If neither
                    "not Player.Sprite","Laura_Sex_Body_H0",#Static
                    "Speed == 1", "Laura_Sex_Body_H1",#slow
                    "Speed == 4", "Laura_Sex_Body_H0",#cumming
                    "Speed >= 2", "Laura_Sex_Body_H2",#fast
                    "True",       "Laura_Sex_Body_H0",#Static
                    ),
            )
    contains:
        ConditionSwitch(
            # Laura's lower body
            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                    # If during sex
                    "Speed == 1", "Laura_Sex_Legs_S1",#heading
                    "Speed == 2", "Laura_Sex_Legs_S2",#slow
                    "Speed == 3", "Laura_Sex_Legs_S3",#fast
                    "Speed >= 4", "Laura_Sex_Legs_S4",#cumming
                    "True", "Laura_Sex_Legs_S0",#Static
                    ),
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    # If during Anal
                    "Speed == 1", "Laura_Sex_Legs_A1",#heading
                    "Speed == 2", "Laura_Sex_Legs_A2",#slow
                    "Speed == 3", "Laura_Sex_Legs_A3",#fast
                    "Speed >= 4", "Laura_Sex_Legs_A4",#cumming
                    "True", "Laura_Sex_Legs_A0",#Static
                    ),
            "Player.Cock == 'foot'", ConditionSwitch(
                    # If during Footjob
                    "not Player.Sprite","Laura_Sex_Legs_F0",#Static
                    "Speed == 1", "Laura_Sex_Legs_F1",#heading
                    "Speed >= 4", "Laura_Sex_Legs_F0",#cumming
                    "Speed >= 2", "Laura_Sex_Legs_F2",#slow
                    "True",       "Laura_Sex_Legs_F0",#Static
                    ),
            "True", ConditionSwitch(
                    # If neither
                    "not Player.Sprite","Laura_Sex_Legs_H0",#Static
                    "Speed == 1", "Laura_Sex_Legs_H1",#heading
                    "Speed == 4", "Laura_Sex_Legs_H0",#cumming
                    "Speed >= 2", "Laura_Sex_Legs_H2",#slow
                    "True", "Laura_Sex_Legs_H0",#Static
                    ),
            )
    zoom .6 #0.6
    transform_anchor True
    anchor (.5,.5)
#    rotate -30

image Laura_Sex_HairBack:
    #Hair underlay
    "Laura_Sprite_HairBack"
    transform_anchor True
    zoom 1.8
    anchor (0.5, 0.5)
    rotate 10
    pos (800,100)

image Laura_Sex_Head:
    #Hair underlay
    "Laura_Sprite_Head"
    transform_anchor True
    zoom 1.8
    anchor (0.5, 0.5)
    rotate 10
    pos (800,100)



image Laura_Sex_Body:
    #Her torso for the sex pose
    contains:
            "Laura_Sex_HairBack"
    contains:
            # hand
#            "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Hand.png"

            ConditionSwitch(
                    "Player.Cock == 'foot'", Null(),
                    "LauraX.Arms == 'gloves'", Recolor("Laura", "Arms", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Hand_Gloved.png"),
                    "True", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Hand.png"
                    )
    contains:
            # Over under layer
        ConditionSwitch(
            "not LauraX.Over", Null(),
            "LauraX.Uptop", ConditionSwitch(
                    #if uptop
                    "LauraX.Over == 'jacket'", Recolor("Laura", "Over", "images/LauraSex/Laura_Sex_Jacket_Back_Up.png"),
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                    #if not uptop
                    "LauraX.Over == 'jacket'", Recolor("Laura", "Over", "images/LauraSex/Laura_Sex_Jacket_Back.png"),
                    "True", Null(),
                    ),
            )
    contains:
            # body
            "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Body.png"
    contains:
            # piercings tits
        ConditionSwitch(
            "not LauraX.Pierce", Null(),
            "LauraX.Pierce == 'barbell'", "images/LauraSex/Laura_Sex_Barbell_Tits.png",
            "LauraX.Pierce == 'ring'", "images/LauraSex/Laura_Sex_Ring_Tits.png",
            "True", Null(),
            )
    contains:
            # Chest clothing layer
        ConditionSwitch(
            "LauraX.Neck == 'leash choker'", Recolor("Laura", "Neck", "images/LauraSex/Laura_Sex_Leash.png"),
            "True", Null(),
            )
    contains:
            # garters
        ConditionSwitch(
            "LauraX.Hose == 'stockings and garterbelt' or LauraX.Hose == 'garterbelt'", Recolor("Laura", "Hose", "images/LauraSex/Laura_Sex_Garter.png"),
            "True", Null(),
            )
    contains:
            # Chest clothing layer
        ConditionSwitch(
            "not LauraX.Chest", Null(),
            "LauraX.Uptop",ConditionSwitch(
                    #if the top is up. . .
                    "not LauraX.Chest", Null(),
                    "LauraX.Chest == 'white tank'", Recolor("Laura", "Chest", "images/LauraSex/Laura_Sex_WhiteTank_Up.png"),
                    "LauraX.Chest == 'leather bra'", Recolor("Laura", "Chest", "images/LauraSex/Laura_Sex_Bra_Leather_Up.png"),
                    "LauraX.Chest == 'wolvie top'", Recolor("Laura", "Chest", "images/LauraSex/Laura_Sex_Top_Wolvie_Up.png"),
                    "LauraX.Chest == 'corset'", Recolor("Laura", "Chest", "images/LauraSex/Laura_Sex_Corset_Up.png"),
                    "LauraX.Chest == 'lace corset'", Recolor("Laura", "Chest", "images/LauraSex/Laura_Sex_Corset_Lace_Up.png"),
                    "LauraX.Chest == 'bikini top'", Recolor("Laura", "Chest", "images/LauraSex/Laura_Sex_Top_Bikini_Up.png"),
#                    "LauraX.Chest == 'sports bra'", Recolor("Laura", "Chest", "images/LauraSex/Laura_Sex_Bra_Sports_Up.png"),
#                    "LauraX.Chest == 'lace bra'", Recolor("Laura", "Chest", "images/LauraSex/Laura_Sex_Bra_Lace_Up.png"),
                    # Modification mode
                    "LauraX.Chest == 'goth top'", "images/LauraSex/modification/Laura_sex_chest_top_goth_up.png",
                    # -----------------
                    "True", Null(),
                    ),
            # else. . .
            "LauraX.Chest == 'white tank'", Recolor("Laura", "Chest", "images/LauraSex/Laura_Sex_WhiteTank.png"),
            "LauraX.Chest == 'leather bra'", Recolor("Laura", "Chest", "images/LauraSex/Laura_Sex_Bra_Leather.png"),
            "LauraX.Chest == 'wolvie top'", Recolor("Laura", "Chest", "images/LauraSex/Laura_Sex_Top_Wolvie.png"),
            "LauraX.Chest == 'corset'", Recolor("Laura", "Chest", "images/LauraSex/Laura_Sex_Corset.png"),
            "LauraX.Chest == 'lace corset'", Recolor("Laura", "Chest", "images/LauraSex/Laura_Sex_Corset_Lace.png"),
            "LauraX.Chest == 'bikini top'", Recolor("Laura", "Chest", "images/LauraSex/Laura_Sex_Top_Bikini.png"),
#            "LauraX.Chest == 'sports bra'", Recolor("Laura", "Chest", "images/LauraSex/Laura_Sex_Bra_Sports.png"),
#            "LauraX.Chest == 'lace bra'", Recolor("Laura", "Chest", "images/LauraSex/Laura_Sex_Bra_Lace.png"),
            # Modification mode
            "LauraX.Chest == 'goth top'", "images/LauraSex/modification/Laura_sex_chest_top_goth.png",
            # -----------------
            "True", Null(),
            )
    contains:
            # piercings tits over clothes
        ConditionSwitch(
            "not LauraX.Pierce or LauraX.Uptop", Null(),
            "LauraX.Pierce == 'barbell'", "images/LauraSex/Laura_Sex_Barbell_Tits_C.png",
            "LauraX.Pierce == 'ring'", "images/LauraSex/Laura_Sex_Ring_Tits_C.png",
            "True", Null(),
            )
    contains:
            # suspenders
        ConditionSwitch(
            "not LauraX.Legs", Null(), #hides when no skirt on
            "(LauraX.Legs == 'leather pants' or LauraX.Legs == 'mesh pants') and LauraX.Upskirt", Null(), #hides when no skirt on
#            "LauraX.Acc == 'suspenders' and not LauraX.Chest and not LauraX.Uptop", "images/LauraSex/Laura_Sex_Suspenders.png",
            "LauraX.Acc == 'suspenders2'", "images/LauraSex/Laura_Sex_Suspenders.png",
            "LauraX.Acc == 'suspenders'", "images/LauraSex/Laura_Sex_Suspenders_Up.png",
            "True", Null(),
            )
    contains:
            # Over clothing layer
        ConditionSwitch(
            "not LauraX.Over", Null(),
            "LauraX.Uptop", ConditionSwitch(
                    #if uptop
                    "LauraX.Over == 'jacket'", Recolor("Laura", "Over", "images/LauraSex/Laura_Sex_Jacket_Up.png"),
#                    "LauraX.Over == 'towel'", "images/LauraSex/Laura_Sex_Towel_Up.png",
                    # Modification mode
                    "LauraX.Over == 'bunny'", "images/LauraSex/modification/Laura_sex_over_bunny_suit_up.png",
                    # ----------------
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                    #if not uptop
                    "LauraX.Over == 'jacket'", Recolor("Laura", "Over", "images/LauraSex/Laura_Sex_Jacket.png"),
#                    "LauraX.Over == 'towel'", "images/LauraSex/Laura_Sex_Towel.png",
                    # Modification mode
                    "LauraX.Over == 'top goth mesh'", "images/LauraSex/modification/Laura_sex_over_goth_mesh.png",
                    "LauraX.Over == 'bunny'", "images/LauraSex/modification/Laura_sex_over_bunny_suit.png",
                    "LauraX.Over == 'apron alice'", "images/LauraSex/modification/Laura_sex_over_apron_alice.png",
                    "LauraX.Over == 'dress alice'", "images/LauraSex/modification/Laura_sex_over_dress_alice.png",
                    "LauraX.Over == 'dress alice torn'", "images/LauraSex/modification/Laura_sex_over_dress_alice_torn.png",
                    # ----------------
                    "True", Null(),
                    ),
            )
    contains:
            # spunk
        ConditionSwitch(
            "'belly' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_Sex_Spunk_Belly.png",
            "True", Null(),
            )
    contains:
            # spunk on tits
            ConditionSwitch(
                "'tits' not in LauraX.Spunk or not Player.Male", Null(),
                "True", "images/LauraSex/Laura_Sex_Spunk_Tits.png",
                )
    contains:
            ConditionSwitch(
                #breast licking animation
                "Trigger == 'suck breasts' or Trigger2 == 'suck breasts'", "Laura_Sex_Lick_Breasts",
                "True", Null()
                )
    contains:
            ConditionSwitch(
                #breast fondling animation
                "Trigger == 'fondle breasts' or Trigger2 == 'fondle breasts'", "Laura_Sex_Fondle_Breasts",
                "True", Null()
                )
    contains:
            "Laura_Sex_Head"
    transform_anchor True
    zoom .9 #1
    offset (55,55)
#    rotate 30
#end Laura Body base

image Laura_Sex_Lick_Breasts:
        "Lick_Anim"
        zoom 0.7
        offset (565,290)#(450,270)

image Laura_Sex_Fondle_Breasts:
        "GropeLeftBreast"
        zoom 1.5
        offset (360,-280)#(320,-130)

image Laura_Sex_Legs:
    #Her Legs during sex
    contains:
            # legs under
        ConditionSwitch(
            "LauraX.Legs == 'skirt'", Recolor("Laura", "Legs", "images/LauraSex/Laura_Sex_Skirt_Back.png"),
            "True", Null(),
            )
#    contains:
#            # spunk
#        ConditionSwitch(
#            "'anal' in LauraX.Spunk or 'in' in LauraX.Spunk", "images/LauraSex/Laura_Spunk_Sex.png",
#            "True", Null(),
#            )
    contains:
            # Legs base
        ConditionSwitch(
            "Player.Cock == 'foot'", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Legs_Foot.png",
            "True", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Legs_High.png",
            )
    contains:
            # anus
        ConditionSwitch(
            "Player.Cock == 'anal' and Speed > 1", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Anus_L.png", #and speed above heading?
#            "Player.Cock == 'anal' and Speed > 0", "images/LauraSex/Laura_Sex_Anus_M.png", #and speed above heading?
            "'anal' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_Sex_Anus_M.png", # If it's full. . .
            "LauraX.Plug", "Laura_Sex_Plug",
            "LauraX.Loose > 2", "Laura_Gape_Anal_Sex", # If it's full. . .
            "True", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Anus_S.png",
            )
    contains:
            # anal spunk
        ConditionSwitch(
            "'anal' not in LauraX.Spunk or not Player.Male", Null(),
            "Player.Cock == 'anal' and Speed > 1", "images/LauraSex/Laura_Sex_Spunk_Anal_U.png", #speed above heading?
            "True", "images/LauraSex/Laura_Sex_Spunk_Anal.png",
            )
    contains:
            # pussy
        ConditionSwitch(
            "Player.Cock == 'in' and Speed > 1", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pussy_Open.png", #and speed above heading?
            "Player.Cock == 'in' and Speed > 0", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pussy_Mid.png", #and speed heading?
            "Trigger == 'lick pussy'", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pussy_Mid.png", #pussy licking
            "LauraX.Offhand == 'fondle pussy' and LauraX.Lust > 60", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pussy_Mid.png",
            "True", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pussy_Closed.png",
            )
    contains:
            # pussy wetness
        ConditionSwitch(
            "not LauraX.Wet", Null(),
            "True", "images/LauraSex/Laura_Sex_Wet.png",
            )
    contains:
            # pussy spunk
        ConditionSwitch(
            "'in' not in LauraX.Spunk or not Player.Male", Null(),
            "Player.Cock == 'in' and Speed > 1", "images/LauraSex/Laura_Sex_Spunk_Pussy_Open.png", #and speed above heading?
            "True", "images/LauraSex/Laura_Sex_Spunk_Pussy.png",
            )
    contains:
            # pubes
        ConditionSwitch(
            "not LauraX.Pubes", Null(),
            "Player.Cock == 'in' and Speed > 1", Recolor("Laura", "Pubes", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pubes_Open.png"), #and speed above heading?
            "Player.Cock == 'in' and Speed > 0", Recolor("Laura", "Pubes", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pubes_Mid.png"), #and speed heading?
            "Trigger == 'lick pussy'", Recolor("Laura", "Pubes", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pubes_Mid.png"), #pussy licking
            "LauraX.Offhand == 'fondle pussy' and LauraX.Lust > 60", Recolor("Laura", "Pubes", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pubes_Mid.png"),
            "True", Recolor("Laura", "Pubes", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pubes_Closed.png"),
            )
    contains:
            # piercings
        ConditionSwitch(
            "LauraX.Pierce == 'barbell' and Player.Cock == 'in' and Speed > 1", "images/LauraSex/Laura_Sex_Barbell_Pussy_O.png", #and speed above heading?
            "LauraX.Pierce == 'barbell'", "images/LauraSex/Laura_Sex_Barbell_Pussy.png",
            "LauraX.Pierce == 'ring' and Player.Cock == 'in' and Speed > 1", "images/LauraSex/Laura_Sex_Ring_Pussy_O.png", #and speed above heading?
            "LauraX.Pierce == 'ring'", "images/LauraSex/Laura_Sex_Ring_Pussy.png",
            "True", Null(),
            )
    contains:
            # panties
        ConditionSwitch(
            "LauraX.PantiesDown", Null(),
#            "LauraX.Panties == 'wolvie panties' and LauraX.Wet", Recolor("Laura", "Panties", "images/LauraSex/Laura_Sex_Panties_Sport_SW.png"),
            "LauraX.Panties == 'bikini bottoms'", Recolor("Laura", "Panties", "images/LauraSex/Laura_Sex_Panties_Bikini.png"),
            "LauraX.Panties == 'wolvie panties'", Recolor("Laura", "Panties", "images/LauraSex/Laura_Sex_Panties_Wolvie.png"),
            "LauraX.Panties == 'lace panties'", Recolor("Laura", "Panties", "images/LauraSex/Laura_Sex_Panties_Lace.png"),
            "LauraX.Panties", Recolor("Laura", "Panties", "images/LauraSex/Laura_Sex_Panties_Black.png"),
            "True", Null(),
            )
    contains:
            # hose base layer
        ConditionSwitch(
            "Player.Cock == 'foot' and (LauraX.Hose == 'stockings and garterbelt' or LauraX.Hose == 'stockings')", Recolor("Laura", "Hose", "images/LauraSex/Laura_Sex_Stockings_Base_Foot.png"),
            "Player.Cock == 'foot' and LauraX.Hose == 'black stockings'", Recolor("Laura", "Hose", "images/LauraSex/Laura_Sex_BlackStockings_Base_Foot.png"),
            "Player.Cock == 'foot' and LauraX.Hose == 'pantyhose'", Recolor("Laura", "Hose", "images/LauraSex/Laura_Sex_Pantyhose_Base_Foot.png"),
            "Player.Cock == 'foot' and LauraX.Hose == 'ripped pantyhose'", Recolor("Laura", "Hose", "images/LauraSex/Laura_Sex_Pantyhose_Holed_Base_Foot.png"),
            "LauraX.Hose == 'pantyhose'", Recolor("Laura", "Hose", "images/LauraSex/Laura_Sex_Pantyhose_Base_Up.png"),
            "LauraX.Hose == 'ripped pantyhose'", Recolor("Laura", "Hose", "images/LauraSex/Laura_Sex_Pantyhose_Holed_Base_Up.png"),
            "LauraX.Hose == 'black stockings'", Recolor("Laura", "Hose", "images/LauraSex/Laura_Sex_BlackStockings_Base_Up.png"),
            "LauraX.Hose == 'stockings and garterbelt' or LauraX.Hose == 'stockings'", Recolor("Laura", "Hose", "images/LauraSex/Laura_Sex_Stockings_Base_Up.png"),
            # Modification mode
            "Player.Cock == 'foot' and LauraX.Hose == 'pantyhose brown'", "images/LauraSex/modification/Laura_sex_hose_pantyhose_brown_foot.png",
            "LauraX.Hose == 'pantyhose brown'", "images/LauraSex/modification/Laura_sex_hose_pantyhose_brown_foot_up.png",
            "Player.Cock == 'foot' and LauraX.Hose == 'pantyhose brown rippedhose'", "images/LauraSex/modification/Laura_sex_hose_pantyhose_brown_ripped_foot.png",
            "LauraX.Hose == 'pantyhose brown rippedhose'", "images/LauraSex/modification/Laura_sex_hose_pantyhose_brown_ripped_foot_up.png",
            "Player.Cock == 'foot' and LauraX.Hose == 'stockings alice'", "images/LauraSex/modification/Laura_sex_hose_stockings_alice_foot.png",
            "LauraX.Hose == 'stockings alice'", "images/LauraSex/modification/Laura_sex_hose_stockings_alice_foot_up.png",
            "Player.Cock == 'foot' and LauraX.Hose == 'stockings alice torn'", "images/LauraSex/modification/Laura_sex_hose_stockings_alice_torn_foot.png",
            "LauraX.Hose == 'stockings alice torn'", "images/LauraSex/modification/Laura_sex_hose_stockings_alice_torn_foot_up.png",
            "Player.Cock == 'foot' and LauraX.Hose == 'tights mesh torn'", "images/LauraSex/modification/Laura_sex_hose_tights_mesh_torn_foot.png",
            "LauraX.Hose == 'tights mesh torn'", "images/LauraSex/modification/Laura_sex_hose_tights_mesh_torn_foot_up.png",
            # ---------------
            "True", Null(),
            )
    contains:
            # legs
        ConditionSwitch(
            "LauraX.Legs == 'skirt' or LauraX.Legs == 'other skirt'", Recolor("Laura", "Legs", "images/LauraSex/Laura_Sex_Skirt.png"),
            "LauraX.Upskirt", Null(),
            "LauraX.Legs == 'leather pants' and Player.Cock == 'foot'", Recolor("Laura", "Legs", "images/LauraSex/Laura_Sex_Pants_Base_Foot.png"),
            "LauraX.Legs == 'leather pants'", Recolor("Laura", "Legs", "images/LauraSex/Laura_Sex_Pants_Base_Up.png"),
            "LauraX.Legs == 'mesh pants' and Player.Cock == 'foot'", Recolor("Laura", "Legs", "images/LauraSex/Laura_Sex_PantsMesh_Base_Foot.png"),
            "LauraX.Legs == 'mesh pants'", Recolor("Laura", "Legs", "images/LauraSex/Laura_Sex_PantsMesh_Base_Up.png"),
            # Modification mode
            "LauraX.Legs == 'leggings goth' and Player.Cock == 'foot'", "images/LauraSex/modification/Laura_sex_legs_leggings_goth_foot.png",
            "LauraX.Legs == 'leggings goth'", "images/LauraSex/modification/Laura_sex_legs_leggings_goth_foot_up.png",
            "LauraX.Legs == 'leggings goth torn' and Player.Cock == 'foot'", "images/LauraSex/modification/Laura_sex_legs_leggings_goth_torn_foot.png",
            "LauraX.Legs == 'leggings goth torn'", "images/LauraSex/modification/Laura_sex_legs_leggings_goth_torn_foot_up.png",
            "LauraX.Legs == 'pants goth torn' and Player.Cock == 'foot'", "images/LauraSex/modification/Laura_sex_legs_pants_goth_torn_foot.png",
            "LauraX.Legs == 'pants goth torn'", "images/LauraSex/modification/Laura_sex_legs_pants_goth_torn_foot_up.png",
            "LauraX.Legs == 'short skirt goth' and Player.Cock == 'foot'", "images/LauraSex/modification/Laura_sex_legs_short_skirt_goth_foot.png",
            "LauraX.Legs == 'short skirt goth'", "images/LauraSex/modification/Laura_sex_legs_short_skirt_goth_foot_up.png",
            # ----------------
            "True", Null(),
            )
    contains:
            # piercings
        ConditionSwitch(
#            "LauraX.Panties and LauraX.PantiesDown", Null(), #don't show if panties are down
#            "LauraX.Legs == 'skirt' or (LauraX.Legs and LauraX.Upskirt)", Null(), #don't show if pants are down
            "LauraX.Pierce == 'barbell'", "images/LauraSex/Laura_Sex_Barbell_Pussy_C.png",
            "LauraX.Pierce == 'ring'", "images/LauraSex/Laura_Sex_Ring_Pussy_C.png",
            "True", Null(),
            )
    contains:
        ConditionSwitch(
            #pussy licking animation
            "Player.Sprite", Null(),
            "Trigger == 'lick pussy'", "Laura_Sex_Lick_Pussy",
            "Trigger == 'lick ass'", "Laura_Sex_Lick_Ass",
            "LauraX.Offhand == 'fondle pussy' and LauraX.Lust > 60", At("LauraFingerHand", GirlFingerPussyX()),
            "LauraX.Offhand == 'fondle pussy'", At("LauraMastHand", GirlGropePussyX()),
            "True", Null()
            ),
#    contains:
#            # Over
#        ConditionSwitch(
#            "LauraX.Over == 'nighty'", "images/LauraSex/Laura_Sex_Nighty_Pussy.png",
#            "True", Null(),
#            )
    contains:
            # Feet
        ConditionSwitch(
            "Player.Cock == 'foot'", "Laura_Footjob_Foot",
            "True", "Laura_Sex_Foot",
            )
    contains:
            #spunk
        ConditionSwitch(
            "'feet' in LauraX.Spunk", "images/LauraSex/Laura_Sex_Spunk_Feet1.png",
            "True", Null(),
            )
    transform_anchor True
    zoom 1
#    rotate 30
#    offset (0,0)
# End Laura Legs base


image Laura_Sex_Lick_Pussy:
        "Lick_Anim"
        zoom 0.8
        offset (720,610)#(530,510)

image Laura_Sex_Lick_Ass:
        "Lick_Anim"
        zoom 0.8
        offset (730,700)#(535,590)

image Laura_Sex_Plug:
        "images/PlugBase_Sex.png"
        offset (-55,-145) #(200,100)(-110,-200)
        zoom 1.4

image Laura_Gape_Anal_Sex:
        #removing an anal plug
        contains:
            #Hole
            "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Anus_L.png"
            transform_anchor True
            subpixel True
            anchor (730,700)#(560,620)
            offset (730,700)#(560,617)
            zoom .30 # tight
            block:
                ease 3 zoom .40 #in.87
                ease 3 zoom .30 #out
                repeat

image Laura_Sex_Foot:
    #her vertical foot in the sex poses
#    contains:
#            # base
#            "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_FootHigh.png"
    contains:
            # hose/foot
        ConditionSwitch(
            "LauraX.Hose == 'stockings and garterbelt' or LauraX.Hose == 'stockings'", Recolor("Laura", "Hose", "images/LauraSex/Laura_Sex_Stockings_Up.png"),
            "LauraX.Hose == 'black stockings'", Recolor("Laura", "Hose", "images/LauraSex/Laura_Sex_BlackStockings_Up.png"),
            "LauraX.Hose == 'pantyhose'", Recolor("Laura", "Hose", "images/LauraSex/Laura_Sex_Pantyhose_Up.png"),
            "LauraX.Hose == 'ripped pantyhose'", Recolor("Laura", "Hose", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pantyhose_Holed_Up.png"),
            # Modification mode
            "LauraX.Hose == 'pantyhose brown'", "images/LauraSex/modification/Laura_sex_hose_pantyhose_brown_left_leg_up.png",
            "LauraX.Hose == 'pantyhose brown ripped'", "images/LauraSex/modification/Laura_sex_hose_pantyhose_brown_ripped_left_leg_up.png",
            "LauraX.Hose == 'stockings alice'", "images/LauraSex/modification/Laura_sex_hose_stockings_alice_left_leg_up.png",
            "LauraX.Hose == 'stockings alice torn'", "images/LauraSex/modification/Laura_sex_hose_stockings_alice_torn_left_leg_up.png",
            "LauraX.Hose == 'tights mesh torn'", "images/LauraSex/modification/Laura_sex_hose_tights_mesh_torn_foot_left_leg_up.png",
            # -----------------
            "True", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_FootHigh.png" #base
            )
    contains:
            # legs
        ConditionSwitch(
            "LauraX.Upskirt", Null(),
            "LauraX.Legs == 'leather pants'", Recolor("Laura", "Legs", "images/LauraSex/Laura_Sex_Pants_Up.png"),
            "LauraX.Legs == 'mesh pants'", Recolor("Laura", "Legs", "images/LauraSex/Laura_Sex_PantsMesh_Up.png"),
            # Modification mode
            "LauraX.Legs == 'leggings goth'", "images/LauraSprite/modification/Laura_sex_legs_leggings_goth_foot_left_leg_up.png",
            "LauraX.Legs == 'leggings goth torn'", "images/LauraSprite/modification/Laura_sex_legs_leggings_goth_torn_foot_left_leg_up.png",
            "LauraX.Legs == 'pants goth torn'", "images/LauraSprite/modification/Laura_sex_legs_pants_goth_torn_foot_left_leg_up.png",
            "LauraX.Legs == 'short skirt goth'", Null(),
            # ----------------
            "True", Null(),
            )
        xoffset  -2 #this shouldn't be needed, but otherwise there's a gap between the knee and leg.
    transform_anchor True
    zoom 1
#    alpha 0.2
    pos (988,-553)#(988,-553)

image Laura_Footjob_Foot:
    #her movable foot in the footjob poses
    contains:
            # hose/base
        ConditionSwitch(
            "LauraX.Hose == 'stockings and garterbelt' or LauraX.Hose == 'stockings'", Recolor("Laura", "Hose", "images/LauraSex/Laura_Sex_Stockings_Foot.png"),
            "LauraX.Hose == 'black stockings'", Recolor("Laura", "Hose", "images/LauraSex/Laura_Sex_BlackStockings_Foot.png"),
            "LauraX.Hose == 'pantyhose'", Recolor("Laura", "Hose", "images/LauraSex/Laura_Sex_Pantyhose_Foot.png"),
            "LauraX.Hose == 'ripped pantyhose'", Recolor("Laura", "Hose", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pantyhose_Holed_Foot.png"),
            # Modification mod
            "LauraX.Hose == 'pantyhose brown'", "images/LauraSex/modification/Laura_sex_hose_pantyhose_brown_left_leg_down.png",
            "LauraX.Hose == 'pantyhose brown ripped'", "images/LauraSex/modification/Laura_sex_hose_pantyhose_brown_ripped_left_leg_down.png",
            "LauraX.Hose == 'stockings alice'", "images/LauraSex/modification/Laura_sex_hose_stockings_alice_left_leg_down.png",
            "LauraX.Hose == 'stockings alice torn'", "images/LauraSex/modification/Laura_sex_hose_stockings_alice_torn_left_leg_down.png",
            "LauraX.Hose == 'tights mesh torn'", "images/LauraSex/modification/Laura_sex_hose_tights_mesh_torn_foot_left_leg_down.png",
            # ----------------
            "True", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Foot.png"
            )
    contains:
            # legs
        ConditionSwitch(
            "LauraX.Upskirt", Null(),
            "LauraX.Legs == 'leather pants'", Recolor("Laura", "Legs", "images/LauraSex/Laura_Sex_Pants_Foot.png"),
            "LauraX.Legs == 'mesh pants'", Recolor("Laura", "Legs", "images/LauraSex/Laura_Sex_PantsMesh_Foot.png"),
            # Modification mode
            "LauraX.Legs == 'leggings goth'", "images/LauraSprite/modification/Laura_sex_legs_leggings_goth_foot_left_leg_down.png",
            "LauraX.Legs == 'leggings goth torn'", "images/LauraSprite/modification/Laura_sex_legs_leggings_goth_torn_foot_left_leg_down.png",
            "LauraX.Legs == 'pants goth torn'", "images/LauraSprite/modification/Laura_sex_legs_pants_goth_torn_foot_left_leg_down.png",
            "LauraX.Legs == 'short skirt goth'", Null(),
            # ----------------
            "True", Null(),
            )
    contains:
        #spunk
        ConditionSwitch(
            "'feet' in LauraX.Spunk", "images/LauraSex/Laura_Sex_Spunk_Feet2.png",
            "True", Null(),
            )
    offset (1105,140) #
    zoom 1

image Laura_CockRef:
    "images/LauraSex/Laura_Sex_Cocktest.png"
    alpha 0.8


# Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Laura_SexMask:
    transform_anchor True
    contains:
        "images/LauraSex/Laura_Sex_MaskPussyX.png"
        pos (400,605)#(0,0)#(-300,-300) #303
        anchor (.5,.5)
    zoom 1
    anchor (0.5,0.5)

# Start S0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Sex_Body_S0:
    #Her Body in the sex pose, static
    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 0.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat

image Laura_Sex_Legs_S0:
    # Her Legs in the Sex pose, static
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2s
                pause 0.1
                ease 0.5 ypos -5 #in -25
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat
    contains:
            AlphaMask("Laura_Sex_Zero_Anim_S0", "Laura_SexMask")
            subpixel True
            pos (525,465)
            block:#total 2s
                pause 0.1
                ease 0.5 ypos 460 #in 470
                easeout 0.5 ypos 461 #471
                easein 0.9 ypos 465 #out 475
                repeat
    # End Legs Sex static

image Laura_Sex_Zero_Anim_S0:
    #this is the cock for Laura's sex animation, Speed0 (static)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        alpha 0.8
        pos (125,170)#125,75
        block: #total 4s
                ease 2 ypos 115#-50
                easeout .5 ypos 120#60
                easein 1.5 ypos 170
                repeat

    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True

# End S0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Start S1 (Heading) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Sex_Body_S1:
    #Her Body in the sex pose, heading
    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 0.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat

image Laura_Sex_Legs_S1:
    # Her Legs in the Sex pose, heading
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2s
                pause 0.1
                ease 0.5 ypos -5 #in -25
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat
    contains:
            "images/JubesDoggy/Jubes_Doggy_Pussy_HHole.png"
            transform_anchor True
            anchor (218,580)#(212,580)
            pos (728,650)#(558,580)
            xzoom 0.8
            alpha 0.5
            parallel:
                pause .1
                ease .5 yzoom 1.2
                pause .5
                ease .9 yzoom 1
                repeat
            parallel:
                pause .1
                ease .5 xzoom 1.2
                pause .5
                ease .9  xzoom 0.8
                repeat
    contains:
            AlphaMask("Laura_Sex_Zero_Anim_S1", "Laura_SexMask")
            subpixel True
            pos (525,485)
            block:#total 2s
                pause 0.1
                ease 0.5 ypos 480 #in 450
                easeout 0.5 ypos 481 #455
                easein 0.9 ypos 485 #out    #475
                repeat
    # End Legs Sex heading

image Laura_Sex_Pussy_Hole:
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

image Laura_Sex_Zero_Anim_S1:
    #this is the cock for Laura's sex animation, Speed1 (heading)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,115)#125,75
        block: #total 2s
                ease .5 ypos 90#-50
                easeout .5 ypos 100#60
                easein 1 ypos 115
                repeat

    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True

# End S1 (Heading) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Start S2 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Laura_Sex_Body_S2:
    #Her Body in the sex pose, slow
    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,10) #top (0,-10)
        block:
            pause 0.3
            ease 0.3 ypos -10 #in
            pause 0.20
            ease 1.70 ypos 10 #out
            repeat

image Laura_Sex_Legs_S2:
    # Her Legs in the Sex pose, slow
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:
                pause 0.25
                ease 0.3 ypos -25 #in
                easeout 0.45 ypos -20
                easein 1.5 ypos 0 #out
                repeat
    contains:
            AlphaMask("Laura_Sex_Zero_Anim_S2", "Laura_SexMask")
            subpixel True
            pos (525,478)
            block:
                pause 0.25
                ease 0.3 ypos 453 #in
                easeout 0.45 ypos 458
                easein 1.5 ypos 478 #out
                repeat
    contains:
            # spunk
            ConditionSwitch(
                "'in' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_Sex_Spunk_Anal_O.png",
                "True", Null(),
                )
            subpixel True
            pos (-15,-105) #top
            block:
                pause 0.25
                ease 0.3 ypos -130 #in
                easeout 0.45 ypos -125
                easein 1.5 ypos -105 #out
                repeat
    # End Legs Sex slow

image Laura_Sex_Zero_Anim_S2:
    #this is the cock for Laura's sex animation, Speed 1 (slow)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,75)#130,75
        block: #total 2.5s
                ease .5 ypos -50#-50
                easeout 1.5 ypos 60#100
                easein .5 ypos 75
                repeat

    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
# End S2 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


# Start S3 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Sex_Body_S3:
    #Her Body in the sex pose, fast
    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,10) #top (0,-10)
        block:#total 2.5s > 1.75 > 1.2
            pause 0.1
            ease 0.2 ypos -50 #in -10
            pause 0.2
            ease .7 ypos 10 #out
            repeat

image Laura_Sex_Legs_S3:
    # Her Legs in the Sex pose, slow
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -45 #in -25
                easeout 0.45 ypos -40 #-50
                easein .5 ypos 0 #out
                repeat
    contains:
            AlphaMask("Laura_Sex_Zero_Anim_S3", "Laura_SexMask")
            subpixel True
            pos (525,478) #(525,475)
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos 433 #in 450
                easeout 0.45 ypos 438 #455
                easein .5 ypos 478 #out
                repeat
#            block:#total 2.5s > 1.75 > 1.2
#                pause 0.05
#                ease 0.2 ypos 430 #in 450
#                easeout 0.45 ypos 435 #455
#                easein .5 ypos 475 #out
#                repeat
    contains:
            # spunk
            ConditionSwitch(
                "'in' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_Sex_Spunk_Anal_O.png",
                "True", Null(),
                )
            subpixel True
            pos (-15,-105) #top(-15,-105)
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -150 #in -45
                easeout 0.45 ypos -145 #-40
                easein .5 ypos -105 #out
                repeat
    # End Legs Sex fast

image Laura_Sex_Zero_Anim_S3:
    #this is the cock for Laura's sex animation, Speed3 (fast)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,75)#130,75
        block: #total 2.5s > 1.75 > 1.2
                ease .2 ypos -70#-50
                easeout .5 ypos 0#60
                easein .5 ypos 75
                repeat

    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
# End S3 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Start S4 (cumming) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Sex_Body_S4:
    #Her Body in the sex pose, cumming
    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,10) #top (0,10)
        block:#total 2.5s > 1.75 > 1.2
            pause 0.1
            ease 0.2 ypos 0 #in
            pause 0.2
            ease 1.7 ypos 10 #out
            repeat

image Laura_Sex_Legs_S4:
    # Her Legs in the Sex pose, slow
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -15 #in -25
                easeout 0.45 ypos -10 #-50
                easein 1.5 ypos 0 #out
                repeat
    contains:
            AlphaMask("Laura_Sex_Zero_Anim_S4", "Laura_SexMask")
            subpixel True
            pos (525,475)
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos 460 #in 450
                easeout 0.45 ypos 465 #455
                easein 1.5 ypos 475 #out
                repeat
    contains:
            # spunk
            ConditionSwitch(
                "'in' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_Sex_Spunk_Anal_O.png",
                "True", Null(),
                )
            subpixel True
            pos (-15,-105) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -120 #in -15
                easeout 0.45 ypos -115 #-10
                easein 1.5 ypos -105 #out
                repeat
    # End Legs Sex fast

image Laura_Sex_Zero_Anim_S4:
    #this is the cock for Laura's sex animation, Speed4 (cumming)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,-60)#130,75
        block: #total
                ease .2 ypos -70
                easeout .5 ypos -68
                easein 1.5 ypos -60
                repeat

    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True

# End S4 (cumming) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Anal Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start A0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Sex_Body_A0:
    #Her Body in the anal pose, static
    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 1.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat

image Laura_Sex_Legs_A0:
    # Her Legs in the anal pose, static
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2s
                pause 0.6
                easeout 0.8 ypos -2 #-50
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat
    contains:
            AlphaMask("Laura_Sex_Zero_Anim_A0", "Laura_AnalMask")
            subpixel True
            pos (533,587) #538,580
            block:#total 2.5s > 1.75 > 1.2
                pause 0.6
                easeout 0.8 ypos 585 #578
                easein 0.2 ypos 582 #out  575
                easeout 0.5 ypos 583 #576
                easein 0.9 ypos 587 #out  580
                repeat
    # End Legs anal static

image Laura_Sex_Zero_Anim_A0:
    #this is the cock for Laura's anal animation, Speed0 (static)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,115)#125,115
        block: #total 3s
                ease 1.5 ypos 110
                pause .5
                ease 1.0 ypos 115
                repeat
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True

# End A0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Start A1 (heading) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


image Laura_Sex_Body_A1:
    #Her Body in the anal pose, heading
    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 1.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat

image Laura_Sex_Legs_A1:
    # Her Legs in the anal pose, heading
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2s
                pause 0.6
                easeout 0.8 ypos -2 #-50
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat

    contains:
            #hole
            "images/LauraSex/Laura_Sex_Anus_M.png"
            subpixel True
            transform_anchor True
            anchor (740,685)#(212,580)
            pos (740,685)#(610,580)
            xzoom 0.8
            yzoom 1
            parallel:#total 2s
                pause 0.6
                easeout 0.8 ypos 683 #-50
                easein 0.2 ypos 680 #out
                easeout 0.5 ypos 681 #-50
                easein 0.9 ypos 685 #out
                repeat
            parallel:
                pause 0.6
                ease 1 yzoom 1.2
                pause .5
                ease .9 yzoom 1
                repeat
            parallel:
                pause 0.6
                ease 1 xzoom 1.2
                pause .5
                ease .9  xzoom 0.8
                repeat

    contains:
            #spunk
            ConditionSwitch(
                "'anal' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_Sex_Spunk_Anal.png",
                "True", Null(),
                )
            subpixel True
            transform_anchor True
            anchor (740,685)#(212,580)
            pos (740,685)#(610,580)
            xzoom 1
            yzoom 1
            parallel:#total 2s
                pause 0.6
                easeout 0.8 ypos 683 #-50
                easein 0.2 ypos 680 #out
                easeout 0.5 ypos 681 #-50
                easein 0.9 ypos 685 #out
                repeat
#            parallel:
#                pause 0.6
#                ease 1 yzoom 1.2
#                pause .5
#                ease .9 yzoom 1
#                repeat
            parallel:
                pause 0.6
                ease 1 xzoom 1.5
                pause .5
                ease .9  xzoom 1.1
                repeat

    contains:
            AlphaMask("Laura_Sex_Zero_Anim_A1", "Laura_AnalMask")
            subpixel True
            pos (538,583) #525,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.6
                easeout 0.8 ypos 581 #455
                easein 0.2 ypos 578 #out
                easeout 0.5 ypos 579 #455
                easein 0.9 ypos 583 #out
                repeat
    # End Legs anal heading

image Laura_Sex_Zero_Anim_A1:
    #this is the cock for Laura's anal animation, Speed1 (heading)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,115)#125,75
        block: #total 3s
                easeout 1.2 ypos 100
                easein .3 ypos 90
                easeout .5 ypos 100
                easein 1 ypos 115
                repeat
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True

# End A1 (heading) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
# Start A2 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Sex_Body_A2:
    #Her Body in the anal pose, slow
    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total 2.5s > 1.75 > 1.2
            pause 0.3
            ease 0.3 ypos -20 #in
            pause 0.20
            ease 1.70 ypos 20 #out
            repeat

image Laura_Sex_Legs_A2:
    # Her Legs in the anal pose, slow
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.25
                ease 0.3 ypos -35 #in
                easeout 0.45 ypos -30
                easein 1.5 ypos 0 #out
                repeat
    contains:
            AlphaMask("Laura_Sex_Zero_Anim_A2", "Laura_AnalMask")
            subpixel True
            pos (538,580) #525,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.25
                ease 0.3 ypos 545 #in 450
                easeout 0.45 ypos 550 #455
                easein 1.5 ypos 580 #out
                repeat
    contains:
            # spunk
            ConditionSwitch(
                "'anal' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_Sex_Spunk_Anal_O.png",
                "True", Null(),
                )
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.25
                ease 0.3 ypos -35 #in
                easeout 0.45 ypos -30
                easein 1.5 ypos 0 #out
                repeat
    # End Legs anal slow

image Laura_Sex_Zero_Anim_A2:
    #this is the cock for Laura's anal animation, Speed2 (slow)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,75)#130,75
        block: #total 2.5s > 1.75 > 1.2
                ease .5 ypos -50#-50
                easeout 1.5 ypos 60#60
                easein .5 ypos 75
                repeat
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True

# End A2 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
# Start A3 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Sex_Body_A3:
    #Her Body in the anal pose, fast
    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total 2.5s > 1.75 > 1.2
            pause 0.1
            ease 0.2 ypos -50 #in
            pause 0.2
            ease .7 ypos 00 #out
            repeat

image Laura_Sex_Legs_A3:
    # Her Legs in the anal pose, fast
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -55 #in -25
                easeout 0.45 ypos -40 #-50
                easein .5 ypos 0 #out
                repeat
    contains:
            AlphaMask("Laura_Sex_Zero_Anim_A3", "Laura_AnalMask")
            subpixel True
            pos (538,580) #525,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos 525 #in 450
                easeout 0.45 ypos 540 #455
                easein .5 ypos 580 #out
                repeat
    contains:
            # Spunk
            ConditionSwitch(
                "'anal' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_Sex_Spunk_Anal_O.png",
                "True", Null(),
                )
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -55 #in -25
                easeout 0.45 ypos -40 #-50
                easein .5 ypos 0 #out
                repeat
    # End Legs Anal fast

image Laura_Sex_Zero_Anim_A3:
    #this is the cock for Laura's anal animation, Speed3 (fast)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,75)#130,75
        block: #total 2.5s > 1.75 > 1.2
                ease .2 ypos -70#-50
                easeout .7 ypos 0#60
                easein .3 ypos 75
                repeat

    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True

# End A3 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
# Start A4 (cumming) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Sex_Body_A4:
    #Her Body in the anal pose, cumming
    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,20) #top (0,-10)
        block:#total 2.5s > 1.75 > 1.2
            pause 0.1
            ease 0.2 ypos 00 #in
            pause 0.2
            ease 1.7 ypos 20 #out
            repeat

image Laura_Sex_Legs_A4:
    # Her Legs in the anal pose, cumming
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -15 #in -25
                easeout 0.45 ypos -10 #-50
                easein 1.5 ypos 0 #out
                repeat
    contains:
            AlphaMask("Laura_Sex_Zero_Anim_A4", "Laura_AnalMask")
            subpixel True
            pos (538,583) #525,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos 568 #in 450
                easeout 0.45 ypos 573 #455
                easein 1.5 ypos 583 #out
                repeat
    contains:
            # spunk
            ConditionSwitch(
                "'anal' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_Sex_Spunk_Anal_O.png",
                "True", Null(),
                )
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -15 #in -25
                easeout 0.45 ypos -10 #-50
                easein 1.5 ypos 0 #out
                repeat
    # End Legs Anal cumming

image Laura_Sex_Zero_Anim_A4:
    #this is the cock for Laura's anal animation, Speed4 (cumming)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,-60)#130,75
        block: #total
                ease .2 ypos -70
                easeout .5 ypos -68
                easein 1.5 ypos -60
                repeat

    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
# End A4 (cumming) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


# Start H0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Sex_Body_H0:
    #Her Body in the hotdogging pose, static
    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 1.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat

image Laura_Sex_Legs_H0:
    # Her Legs in the hotdogging pose, static
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
#            block:#total 2s
#                pause 0.6
#                easeout 0.8 ypos -2 #-50
#                easein 0.2 ypos -5 #out
#                easeout 0.5 ypos -4 #-50
#                easein 0.9 ypos 0 #out
#                repeat
    contains:
            "Laura_Sex_Zero_Anim_H0"
#            AlphaMask("Laura_Sex_Zero_Anim_H0", "Laura_AnalMask")
            subpixel True
            pos (558,580) #538,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.6
                easeout 0.8 ypos 578 #455
                easein 0.2 ypos 575 #out
                easeout 0.5 ypos 576 #455
                easein 0.9 ypos 580 #out
                repeat
    # End Legs hotdogging static

image Laura_Sex_Zero_Anim_H0:
    #this is the cock for Laura's hotdogging animation, Speed0 (static)
    contains:
        subpixel True
        ConditionSwitch(
            "Player.Sprite", "Zero_Doggy_Insert",# Zero's cock, changes color and properties
            "True", Null(),
            )

#        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,115)#125,75
        alpha 0.8
        block: #total 3s
                ease 1.5 ypos 110
                pause .5
                ease 1.0 ypos 115
                repeat
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True

# End H0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Start H1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Sex_Body_H1:
    #Her Body in the hotdogging pose, slow
    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 1.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat

image Laura_Sex_Legs_H1:
    # Her Legs in the hotdogging pose, slow
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2s
                pause 0.6
                ease 1 ypos -10 #-50
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat
    contains:
            "Laura_Sex_Zero_Anim_H1"
#            AlphaMask("Laura_Sex_Zero_Anim_H0", "Laura_AnalMask")
            subpixel True
            pos (558,580) #538,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.6
                ease 1 ypos 570 #-50
                easeout 0.5 ypos 576 #455
                easein 0.9 ypos 580 #out
                repeat
    # End Legs hotdogging slow

image Laura_Sex_Zero_Anim_H1:
    #this is the cock for Laura's hotdogging animation, Speed1 (slow)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        alpha 0.8
        pos (125,250)#125,75
        block: #total 3s
                ease 1.5 ypos 90 #110
                pause .5
                ease 1.0 ypos 250
                repeat
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True

# End H1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Start H2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Sex_Body_H2:
    #Her Body in the hotdogging pose, fast
    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total .75s
            pause .3
            ease .5 ypos -5 #in
            pause 0.3
            ease .4 ypos 0 #out
            repeat

image Laura_Sex_Legs_H2:
    # Her Legs in the hotdogging pose, fast
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total .75s
                pause 0.1
                ease .25 ypos -20 #-50
                easeout 0.15 ypos -18 #-50
                easein 0.25 ypos 0 #out
                repeat
    contains:
            "Laura_Sex_Zero_Anim_H2"
#            AlphaMask("Laura_Sex_Zero_Anim_H0", "Laura_AnalMask")
            subpixel True
            pos (558,580) #538,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.1
                ease .25 ypos 560 #-50
                easeout 0.15 ypos 562 #455
                easein 0.25 ypos 580 #out
                repeat
    # End Legs anal fast

image Laura_Sex_Zero_Anim_H2:
    #this is the cock for Laura's hotdogging animation, Speed1 (fast)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        alpha 0.8
        pos (125,230)#125,75
        block: #total .75s
                ease .25 ypos 150 #110
                easeout 0.25 ypos 170
                easein 0.25 ypos 230
                repeat
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True

# End H2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


image Laura_AnalMask:
    transform_anchor True
    contains:
        "images/LauraSex/Laura_Sex_MaskAnalX.png"
        pos (400,670)#(0,0)#(-300,-300) #323 -70
        anchor (.5,.5)
    zoom 1
    anchor (0.5,0.5)



# Laura Footjob  Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Laura_Sex_Zero_Anim_F:
            #cock used in laura's sex pose
            ConditionSwitch(
                "Player.Sprite and AlphaCock", "Zero_Ghostcock",
                "Player.Sprite", "Zero_Blowcock",
                "True", Null(),
                )
            zoom .7
            anchor (0.5, 0.9)
            offset (270,650)#(220,350)
            rotate 0

# Start F1 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Sex_Body_F0:
    #Her Body in the hotdogging pose, static
    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 1.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat
    yoffset -100

image Laura_Sex_Legs_F0:
    # Her Legs in the hotdogging pose, static
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
#            block:#total 3s
#                pause 0.6
#                easeout 0.8 ypos -2 #-50
#                easein 0.2 ypos -5 #out
#                easeout 0.5 ypos -4 #-50
#                easein 0.9 ypos 0 #out
#                repeat
    contains:
            #Foot
#            ConditionSwitch(
#                "Player.Sprite", "Laura_Footjob_Foot",
#                "True", Null(),
#                )
            "Laura_Footjob_Foot",
            subpixel True
            anchor (1100,140)
            transform_anchor True
            pos (0,0) #top
            rotate 0
#            parallel:#total 3s
#                pause 0.6
#                easeout 0.8 ypos -2 #-2
#                easein 0.2 ypos -5 #out
#                easeout 0.5 ypos -4 #-4
#                easein 0.9 ypos 0 #out
#                repeat
            parallel:#total 3s
                ease 2 rotate 5 #20
                ease 2 rotate -5 #0
                pause .5
                repeat
    contains:
            "Laura_Sex_Zero_Anim_F"
            subpixel True
            transform_anchor True
            pos (558,580) #538,475
            rotate -5
#            parallel:#total 3s
#                pause 0.6
#                easeout 0.8 ypos 578 #578
#                easein 0.2 ypos 575 #out 575
#                easeout 0.5 ypos 576 #575
#                easein 0.9 ypos 580 #out  580
#                repeat
            parallel:#total 3s
                easeout 1 rotate -5 #-20
                easein 1 rotate -10 #-28
                pause .2
                easeout .8 rotate -5 #-20
                easein 1 rotate 0 #-5
                pause .5
                repeat

    yoffset -100
    # End Legs hotdogging static


# End F0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


# Start F1 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Sex_Body_F1:
    #Her Body in the hotdogging pose, static
    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 1.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat
    yoffset -100

image Laura_Sex_Legs_F1:
    # Her Legs in the hotdogging pose, static
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 3s
                pause 0.6
                easeout 0.8 ypos -2 #-50
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat
    contains:
            "Laura_Sex_Zero_Anim_F"
            subpixel True
            transform_anchor True
            pos (558,580) #538,475
            rotate -5
            parallel:#total 3s
                pause 0.6
                easeout 0.8 ypos 578 #455
                easein 0.2 ypos 575 #out
                easeout 0.5 ypos 576 #455
                easein 0.9 ypos 580 #out
                repeat
            parallel:#total 3s
                easeout 1 rotate -20 #-50
                easein 1 rotate -28 #-50
                pause .2
                easeout .8 rotate -20 #-50
                easein 1 rotate -5 #-50
                pause .5
                repeat
    contains:
            #Foot
            "Laura_Footjob_Foot"
            subpixel True
            anchor (1100,140)
            transform_anchor True
            pos (0,0) #top
            rotate 0
            parallel:#total 3s
                pause 0.6
                easeout 0.8 ypos -2 #-50
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat
            parallel:#total 3s
                ease 2 rotate 20 #-50
                ease 2 rotate 0 #-50
                pause .5
                repeat

    yoffset -100
    # End Legs hotdogging static

# End F1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


# Start F2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Sex_Body_F2:
    #Her Body in the hotdogging pose, fast
    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total 2s
            ease .7 ypos -10 #in
            ease .7 ypos 0 #out
            repeat
    rotate 15
    yoffset -250
    xoffset 500#400
    xzoom -1

image Laura_Sex_Legs_F2:
    # Her Legs in the hotdogging pose, fast
    contains:
            #Body
            "Laura_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 3
                ease 0.5 ypos -2 #-50
                ease 1 ypos -10 #-50
                pause .1
                repeat
    contains:
            "Laura_Sex_Zero_Anim_F"
            subpixel True
            transform_anchor True
            pos (808,380) #(558,580)
            rotate -55
            parallel:#total 3s
                easeout .25 rotate -58 #-20
                easein .25 rotate -60 #-28
                pause .1
                easeout .4 rotate -58 #-20
                easein .5 rotate -55 #-5
                pause .1#.25
                repeat
    contains:
            #Foot
            "Laura_Footjob_Foot"
            subpixel True
            anchor (1100,140)
            transform_anchor True
            pos (0,0) #top
            rotate 0
            parallel:#total 3s
                pause 0.15
                easeout 0.2 ypos -2 #-50
                easein 0.05 ypos -5 #out
                easeout 0.25 ypos -4 #-50
                easein 0.45 ypos 0 #out
                repeat
            parallel:#total 3s
                ease .5 rotate 20 #-50  top
                ease 1 rotate 0 #-50
                pause .1#.25
                repeat

    yoffset -400
    xoffset 300#200
    rotate 50
    # End Legs hotdogging fast


# End F2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

#End Footjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#End Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Laura_SexMaskX:
    transform_anchor True
    contains:
        "images/LauraSex/Laura_Sex_MaskPussyX.png"
        pos (200,303)#(0,0)#(-300,-300) #
        anchor (.5,.5)
    zoom 1
#    transform_anchor True
    anchor (0.5,0.5)
#    rotate 30

image Laura_Sex_Zero_AnimX:
        #this is the cock for Laura's sex animation, Speed 0 (static)
        contains:
            Solid("#159457", xysize=(401,606))#(1264,1061))
            alpha 0.9
        contains:
            subpixel True
#            anchor (0.5,0)
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
#            pos (498,530) #X less is left, Y less is up (498,520)
            zoom 1.6
            alpha 0.5
            pos (130,100)#(390,550)#(350,250) #466
#            rotate -30
            block:
                    ease 1.25 ypos -50#630
                    ease 1.25 ypos 100#480
                    repeat

        size (401,606)#(88,266)(1264,1061)#(1119,1186)
        anchor (0.1,0.5)
        transform_anchor True
#        rotate 30


image Laura_Mega_Mask2:
    # giant green brick for use in finding where a mask is
    contains:
        "images/LauraSex/Laura_Sex_PussyMaskTest2.png"
#        Solid("#159457", xysize=(500,500))
#        offset (-100,100)
#        anchor (0.5,0.5)
#        zoom 1.0
#        alpha .5
#        pos (200,0)#(26,350)#(-175,450)
#        block:
#                    ease .25 offset(0,-500)
#                    ease .25 offset(0,1000)
#                    ease .25 offset(200,-500)
#                    ease .25 offset(200,1000)
#                    ease .25 offset(400,-500)
#                    ease .25 offset(400,1000)
#                    ease .25 offset(600,-500)
#                    ease .25 offset(600,1000)
#                    ease 1.5 offset(-800,-1000)
#                    ease 1.5 offset(-200,-100)
#                    ease .25 offset(-400,-500)
#                    ease .25 offset(-400,1000)
#                    ease .25 offset(-200,-500)
#                    ease .25 offset(-200,1000)
#                    repeat
    transform_anchor True
    zoom 1
    rotate 30
#    block:
#                    ease 1 rotate 0
#                    ease 1 rotate 30
#                    repeat

#image Laura_Mega_Mask:
#    # giant green brick for use in finding where a mask is
#    contains:
#        "images/LauraSex/Laura_Sex_PussyMaskTestB.png"
#        Solid("#159457", xysize=(500,500))
#        offset (-100,100)
#        anchor (0.5,0.5)
#        zoom 1.0
#        alpha .5
#        pos (200,0)#(26,350)#(-175,450)
#        block:
#                    ease 1.5 offset(-800,-1200)
#                    ease 1.5 offset(-200,-100)
#                    ease 1.5 offset(-600,-1200)
#                    ease 1.5 offset(-600,-600)
#                    ease 1.5 offset(-200,-1200)
#                    ease 1.5 offset(-200,-600)
#                    repeat
#    transform_anchor True
#    zoom 1
#    rotate 30

# end Laura's Sex Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Laura_Sex_Launch(Line = Trigger):
        $ LauraX.Offhand = 0 if LauraX.Offhand == "hand" else LauraX.Offhand
        $ Line = "solo" if not Line else Line
        if Line == "sex":
            $ Player.Sprite = 1
            $ Player.Cock = "in"
            call Cock_Occupied(LauraX,"pussy")
            if Trigger2 in ("fondle pussy","dildo pussy","lick pussy"):
                    $ Trigger2 = 0
        elif Line == "anal":
            $ Player.Sprite = 1
            $ Player.Cock = "anal"
            call Cock_Occupied(LauraX,"anal")
            if Trigger2 in ("insert ass","dildo anal","lick ass"):
                    $ Trigger2 = 0
        elif Line == "solo":
            $ Player.Sprite = 1
            $ Player.Sprite = 0
            $ Player.Cock = "out"
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
            call Zero_Strapped(LauraX) #puts strap-on on.
        $ Trigger = Line

        if LauraX.Pose == "doggy":
                call Laura_Doggy_Launch(Line)
                return
        if renpy.showing("Laura_SexSprite"):
            return
        call Girl_Hide(LauraX,1)
        $ Speed = 0

        if Trigger == "in" or Trigger == "anal":
                if LauraX.Legs or LauraX.HoseNum() >= 5:
                    $ LauraX.Upskirt = 1
                if LauraX.Panties:
                    $ LauraX.PantiesDown = 1

        show Laura_SexSprite zorder 150:
            pos (450,500)
        with dissolve
        return

label Laura_Sex_Reset:
        if renpy.showing("Laura_Doggy_Animation"):
            call Laura_Doggy_Reset
            return
        if not renpy.showing("Laura_SexSprite"):
            return
        $ LauraX.ArmPose = 2
        hide Laura_SexSprite
        call Girl_Hide(LauraX)
        show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
            alpha 1 zoom 1 offset (0,0) anchor (0.5, 0.0)
        with dissolve
        $ Speed = 0
        return



# Laura's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Laura's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



image Laura_BJ_Animation:
    #core blowjob animation
    contains:
        ConditionSwitch(
            # Laura's upper body
#            "Player.Sprite", ConditionSwitch(
#                    # If during sex
            "Speed == 1", "Laura_BJ_Body_1",#Licking
            "Speed == 2", "Laura_BJ_Body_2",#Heading
            "Speed == 3", "Laura_BJ_Body_3",#Sucking
            "Speed == 4", "Laura_BJ_Body_4",#Deepthroat
            "Speed == 5", "Laura_BJ_Body_5",#Cumming high
            "Speed == 6", "Laura_BJ_Body_6",#Cumming deep
#                    "True",     "Laura_BJ_Body_0",#Static
#                    ),
            "True","Laura_BJ_Body_0",#Static
            )
    zoom 1.35
    anchor (.5,.5)
    pos (600,605)


#  BJ animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#image Laura_Sprite_BJ_SuckingMask:
#    contains:
#            "images/LauraSprite/Laura_Sprite_SuckingMask.png"
##            pos (200,50)
#    contains:
#            "images/LauraSprite/Laura_Sprite_SpunkSuckingO.png"
#    pos (100,150)
#    alpha .8

image Laura_BJ_Backdrop:
    LiveComposite(
        (402,965),
        (0,0), "Laura_Sprite_HairBack",
        (0,0), ConditionSwitch(
            #backside of arms
            "LauraX.Arms == 'gloves' and LauraX.ArmPose == 2", Recolor("Laura", "Arms", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Glove_Back2.png"),
            "LauraX.Arms == 'gloves'", Recolor("Laura", "Arms", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Glove_Back1.png"), #if LauraX.Arms == 1
            "LauraX.ArmPose == 2", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Arm_Back2.png",
            "True", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Arm_Back1.png", #if LauraX.Arms == 1
            ),
#        (0,0), ConditionSwitch(
#            #arms wristband
#            "LauraX.Arms == 'wrists'", Recolor("Laura", "Arms", "images/LauraSprite/Laura_Sprite_Wrist_Right.png"), # one hand up
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #L Over under
            "LauraX.Uptop and LauraX.Over == 'jacket'", Recolor("Laura", "Over", "images/LauraSprite/Laura_Sprite_Jacket_Back_Up.png"), # one hand up
            "LauraX.Over == 'jacket'", Recolor("Laura", "Over", "images/LauraSprite/Laura_Sprite_Jacket_Back.png"), # one hand up
            "True", Null(),
            ),
        #body
        (0,0), "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Body.png",

        #shifted here
        (0,0), ConditionSwitch(
            #arms midlayer
            "LauraX.Arms == 'gloves' and LauraX.ArmPose == 2", Recolor("Laura", "Arms", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Glove_Mid2.png"),
            "LauraX.Arms == 'gloves'", Recolor("Laura", "Arms", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Glove_Mid1.png"), #if LauraX.Arms == 1
            "LauraX.ArmPose == 2", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Arm_Mid2.png",         # one hand up
            "True", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Arm_Mid1.png", #if LauraX.Arms == 1   # Crossed
            ),
        # tits
        (0,0), "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Tits.png",
        (0,0), ConditionSwitch(
            #Water effect
            "LauraX.Water and LauraX.ArmPose == 1", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Water1.png",
            "LauraX.Water", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Water2.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #arms wristband
            "LauraX.Arms == 'wrists' and LauraX.ArmPose == 2", Recolor("Laura", "Arms", "images/LauraSprite/Laura_Sprite_Wrist2.png"), # one hand up
            "LauraX.Arms == 'wrists'", Recolor("Laura", "Arms", "images/LauraSprite/Laura_Sprite_Wrist1.png"), # one hand up
            "True", Null(),
            ),
        #shifted here
        #where arms and tits were before
        (0,0), ConditionSwitch(
            #nude peircings
            "not LauraX.Pierce", Null(),
            "LauraX.Pierce == 'barbell'", "images/LauraSprite/Laura_Sprite_Barbell_Tits.png",
            "LauraX.Pierce == 'ring'", "images/LauraSprite/Laura_Sprite_Ring_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #neck
            "LauraX.Neck == 'leash choker'", Recolor("Laura", "Neck", "images/LauraSprite/Laura_Sprite_Neck_Leash.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Chest layer
            "LauraX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "LauraX.Chest == 'white tank'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Bra_White_Up.png"),
                    "LauraX.Chest == 'leather bra'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Bra_Leather_Up.png"),
                    "LauraX.Chest == 'wolvie top'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Top_Wolvie_Up.png"),
                    "LauraX.Chest == 'bikini top'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Top_Bikini_Up.png"),
                    "LauraX.Chest == 'corset'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Top_Corset_Up.png"),
                    "LauraX.Chest == 'lace corset'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Top_Corset_Lace_Up.png"),
                    "True", Null(),
                    ),
            "LauraX.Chest == 'white tank'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Bra_White.png"),
            "LauraX.Chest == 'leather bra'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Bra_Leather.png"),
            "LauraX.Chest == 'wolvie top'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Top_Wolvie.png"),
            "LauraX.Chest == 'bikini top'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Top_Bikini.png"),
            "LauraX.Chest == 'corset'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Top_Corset.png"),
            "LauraX.Chest == 'lace corset'", Recolor("Laura", "Chest", "images/LauraSprite/Laura_Sprite_Top_Corset_Lace.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #suspenders
            "not LauraX.Legs", Null(), #hides when no skirt on
            "(LauraX.Legs == 'leather pants' or LauraX.Legs == 'mesh pants') and LauraX.Upskirt", Null(), #hides when no skirt on
#            "LauraX.Acc == 'suspenders' and not LauraX.Chest and not LauraX.Uptop", "images/LauraSprite/Laura_Sprite_Acc_Suspenders2.png", #over nips
            "LauraX.Acc == 'suspenders2'", "images/LauraSprite/Laura_Sprite_Acc_Suspenders2.png", #over nips
            "LauraX.Acc == 'suspenders'", "images/LauraSprite/Laura_Sprite_Acc_Suspenders1.png", #open
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #L Over
            "LauraX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "LauraX.Over == 'jacket' and LauraX.ArmPose == 2", Recolor("Laura", "Over", "images/LauraSprite/Laura_Sprite_Jacket_A2_Up.png"), # one hand up
                    "LauraX.Over == 'jacket'", Recolor("Laura", "Over", "images/LauraSprite/Laura_Sprite_Jacket_A1_Up.png"), # one hand up
#                    "LauraX.Over == 'towel'", Recolor("Laura", "Legs", "images/LauraSprite/Laura_Sprite_Towel.png"),
                    "True", Null(),
                    ),
            "LauraX.Over == 'jacket' and LauraX.ArmPose == 2", Recolor("Laura", "Over", "images/LauraSprite/Laura_Sprite_Jacket_A2.png"), # one hand up
            "LauraX.Over == 'jacket'", Recolor("Laura", "Over", "images/LauraSprite/Laura_Sprite_Jacket_A1.png"), # one hand up
            "LauraX.Over == 'towel'", Recolor("Laura", "Legs", "images/LauraSprite/Laura_Sprite_Towel.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #clothed peircings
            "not LauraX.Pierce or (not LauraX.Over and not LauraX.Chest)", Null(),
            "LauraX.Over == 'jacket'", Null(),
            "LauraX.Pierce == 'barbell'",  "images/LauraSprite/Laura_Sprite_Barbell_TitsC.png",
            "LauraX.Pierce == 'ring'", "images/LauraSprite/Laura_Sprite_Ring_TitsC.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #belly spunk
            "'belly' in LauraX.Spunk and Player.Male", "images/LauraSprite/Laura_Sprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast spunk
            "'tits' in LauraX.Spunk and Player.Male", "images/LauraSprite/Laura_Sprite_Spunk_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #arms toplayer
            "LauraX.Arms == 'gloves' and LauraX.ArmPose == 2", Recolor("Laura", "Arms", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Glove_Top2.png"),
            "LauraX.ArmPose == 2", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Arm_Left2.png", # one hand up
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Water effect
            "LauraX.Water and LauraX.ArmPose == 2", "images/LauraSprite/Laura_Sprite_Water2top.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #arms wristband
            "LauraX.ArmPose == 2 and LauraX.Arms == 'wrists'", Recolor("Laura", "Arms", "images/LauraSprite/Laura_Sprite_Wrist_Left2.png"), # one hand up
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #jacket arm toplayer
            "LauraX.Over == 'jacket' and LauraX.ArmPose == 2", Recolor("Laura", "Over", "images/LauraSprite/Laura_Sprite_Jacket_A2Top.png"), # one hand up
            "True", Null(),
            ),
        )
    anchor (0.5, 0.0)
    offset (35,0)#(35,0)
    zoom .78#.75

image Laura_BJ_Body:
    contains:
        "Laura_BJ_Backdrop"

image Laura_Sprite_BJ_HairBack:
    #This is the version of the hair back used in the BJ pose
#    Recolor("Laura", "Hair", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Long_Under.png")
    ConditionSwitch(
            #Hair over
            "not LauraX.Hair", Null(),
            "LauraX.Hair == 'wet' or LauraX.Water", Recolor("Laura", "Hair", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Wet_Under.png"),
            "not Player.Male and 'facial' in LauraX.Spunk",Recolor("Laura", "Hair", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Wet_Under.png"),
            "LauraX.Hair", Recolor("Laura", "Hair", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Long_Under.png"),
            "True", Null(),
            )

image Laura_Sprite_BJ_Head:
    #This is the version of the head used in the BJ pose
    LiveComposite(
        (806,806),
        (0,0), ConditionSwitch(
                # Face background plate
                "LauraX.Blush == 2", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Head_Blush2.png",
                "LauraX.Blush", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Head_Blush.png",
                "True", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Head.png",
                ),
        (0,0), ConditionSwitch(#chin spunk
            "'chin' not in LauraX.Spunk or not Player.Male", Null(),
            "Speed >= 2", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Spunk_Chin.png",
            ),
        (0,0), ConditionSwitch(#Mouths
            "renpy.showing('Laura_CUN_Animation') and Speed", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Tongue.png"),
            "Speed >= 2", Recolor("Laura", "Lips", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Mouth_SuckingBJ.png"),   #sucking
            "Speed == 1", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Tongue.png"),     #licking
            "LauraX.Mouth == 'normal'", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png"),
            "LauraX.Mouth == 'lipbite'", Recolor("Laura", "Lips", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Mouth_Lipbite.png"),
            "LauraX.Mouth == 'sucking'", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Sucking.png"),
            "LauraX.Mouth == 'kiss'", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Kiss.png"),
            "LauraX.Mouth == 'sad'", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Sad.png"),
            "LauraX.Mouth == 'smile'", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png"),
            "LauraX.Mouth == 'surprised'", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Surprised.png"),
            "LauraX.Mouth == 'tongue'", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Tongue.png"),
            "LauraX.Mouth == 'grimace'", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png"),
            "LauraX.Mouth == 'smirk'", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Smirk.png"),
#            "LauraX.Mouth == 'smirk'", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png"),
            "True", Recolor("Laura", "Lips", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png"),
            ),
        (0,0), ConditionSwitch(#Mouth spunk
            "'mouth' not in LauraX.Spunk or not Player.Male", Null(),
            "Speed >= 2", "images/LauraSprite/Laura_Sprite_Spunk_MouthSuck.png",   #sucking
            "Speed == 1", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",     #licking
            "LauraX.Mouth == 'normal'", "images/LauraSprite/Laura_Sprite_Spunk_MouthNeutral.png",
            "LauraX.Mouth == 'lipbite'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmirk.png",
            "LauraX.Mouth == 'sucking'", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",
            "LauraX.Mouth == 'kiss'", "images/LauraSprite/Laura_Sprite_Spunk_MouthKiss.png",
            "LauraX.Mouth == 'sad'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSad.png",
            "LauraX.Mouth == 'smile'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmile.png",
            "LauraX.Mouth == 'surprised'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSad.png",
            "LauraX.Mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",
            "LauraX.Mouth == 'grimace'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmile.png",
            "LauraX.Mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmirk.png",
            "True", "images/LauraSprite/Laura_Sprite_Spunk_MouthNeutral.png",
            ),
        (0,0), ConditionSwitch(#Mouth spunk over
            "Speed >= 2 and 'mouth' in LauraX.Spunk and Player.Male", "images/LauraSprite/Laura_Sprite_SpunkSuckingO.png",   #sucking
            "True", Null(),
            ),
        (0,0), ConditionSwitch(#wet tongue
            "Speed == 1", "images/LauraSprite/Laura_Sprite_Wet_Tongue.png",     #licking
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #wet face
            "Player.Male", Null(),
            "'mouth' not in LauraX.Spunk and 'chin' not in LauraX.Spunk", Null(),
            "'chin' not in LauraX.Spunk and (LauraX.Mouth == 'tongue' or Speed)", "images/LauraSprite/Laura_Sprite_Head_Wet_Tongue.png",
            "LauraX.Mouth == 'tongue' or Speed", "images/LauraSprite/Laura_Sprite_Head_Wet_Tongue2.png",
            "'mouth' in LauraX.Spunk or 'chin' in LauraX.Spunk", "images/LauraSprite/Laura_Sprite_Head_Wet_Mouth.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #brows
            "LauraX.Blush >= 2", ConditionSwitch(
                    "LauraX.Brows == 'normal'", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Normal_B.png",
                    "LauraX.Brows == 'angry'", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Angry_B.png",
                    "LauraX.Brows == 'sad'", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Sad_B.png",
                    "LauraX.Brows == 'surprised'", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Surprised_B.png",
                    "LauraX.Brows == 'confused'", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Confused_B.png",
                    "True", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Normal_B.png",
                    ),
            "True", ConditionSwitch(
                    "LauraX.Brows == 'normal'", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Normal.png",
                    "LauraX.Brows == 'angry'", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Angry.png",
                    "LauraX.Brows == 'sad'", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Sad.png",
                    "LauraX.Brows == 'surprised'", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Surprised.png",
                    "LauraX.Brows == 'confused'", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Confused.png",
                    "True", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Brows_Normal.png",
                    ),
            ),
        (0,0), "Laura Blink",     #Eyes
        (0,0), ConditionSwitch(
            #Hair mid
            "LauraX.Over == 'jacket'", Null(),
            "LauraX.Hair == 'wet' or LauraX.Water", Null(),
            "LauraX.Hair", Recolor("Laura", "Hair", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Long_Mid.png"),
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Face Water
#            "not LauraX.Water", Null(),
#            "True", "images/LauraSprite/Laura_Sprite_Wet_Head.png",
#            ),
        (0,0), ConditionSwitch(
            #Hair over
            "not LauraX.Hair", Null(),
            "LauraX.Hair == 'wet' or LauraX.Water", Recolor("Laura", "Hair", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Wet_Over.png"),
            "not Player.Male and 'facial' in LauraX.Spunk",Recolor("Laura", "Hair", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Wet_Over.png"),
            "LauraX.Hair", Recolor("Laura", "Hair", "images/LauraSprite/[LauraX.skin_image.skin_path]Laura_Sprite_Hair_Long_Over.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hair Water
            "not LauraX.Water and not (not Player.Male and 'facial' in LauraX.Spunk)", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Head_Wet.png",
#            "True", Recolor("Laura", "Hair", "images/LauraSprite/Laura_Sprite_Hair_Wet.png"),
            ),
        (0,0), ConditionSwitch(
            #facial spunk
            "'hair' in LauraX.Spunk and Player.Male", "images/LauraSprite/Laura_Sprite_Spunk_Facial2.png",
            "'facial' in LauraX.Spunk and Player.Male", "images/LauraSprite/Laura_Sprite_Spunk_Facial1.png",
            "True", Null(),
            ),
        )
#    anchor (0.6, 0.0)
#    zoom .5

image Laura_BlowCock_Mask:
    #This is a mask used by the blockcock during the Speed 3 sucking animation
    #it is a block moving in and out to prevent the cock sticking out the back.
    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,0)#(640,198)# top
#        block:
#                pause 0.1
#                ease 1.6 offset (0,300)# bottom
#                pause 0.1
#                ease 1.4 offset (0,0)# top
#                repeat


#image Laura_BlowCock_Mask_3:
#    This is a mask used by the blockcock during the Speed 4 deep throat animation
#    it is a block moving in and out to prevent the cock sticking out the back.
#    contains:
#        Solid("#159457", xysize=(190,950))
#        offset (0,0)#(640,198)# top
#        block:
#                pause 0.1
#                ease 1.6 offset (0,300)# bottom
#                pause 0.1
#                ease 1.4 offset (0,0)# top
#                repeat

image Laura_BJ_Body_0:
    #Her Body in the BJ pose, static
    contains:
            #Hair underlay
            "Laura_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (490,400) #(535,340) #top
            rotate 0 #-30
            parallel:
                ease 1.1 ypos 405 #bottom
                pause 0.2
                ease 1.1 ypos 400 #top
                pause 0.2
                repeat
#    contains:
#            #base body
#            "Laura_Sprite"
#            subpixel True
#            pos (650,800)#(673,740) #top
#            zoom 2.2 #.75
#            anchor (0.5, 0.5)
#            rotate -20
#            parallel:
#                pause 0.1
#                ease 1.1 ypos 810 #bottom
#                pause 0.2
#                ease 1 ypos 800 #top
#                pause 0.1
#                repeat
    contains:
            #base body
            "Laura_BJ_Body"
            anchor (100,180)#(0.6, 0.1)
            zoom 2.2 #.75
            pos (650,350)# #top     (650,350)(680,290) (145,50)
            transform_anchor True
            rotate -20
            subpixel True
#            alpha 0.8
            parallel:
                pause 0.1
                ease 1.1 ypos 360 #bottom
                pause 0.2
                ease 1.1 ypos 355 #top
                pause 0.1
                repeat
    contains:
            #base head under cock
            subpixel True
            "Laura_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (490,400) #(535,340) #top
            rotate 0 #-30
            parallel:
                ease 1.1 ypos 405 #bottom
                pause 0.2
                ease 1.1 ypos 400 #top
                pause 0.2
                repeat
    contains:
            #zero's cock
#            ConditionSwitch(
#                "Player.Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Laura_BlowCock_Mask"), #Null(),
#                )
            AlphaMask("Blowcock", "Laura_BlowCock_Mask")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4
            alpha 1
            rotate 10
            parallel:
                pause 0.1
#                easeout .1 rotate 1 #bottom .6
                ease .15 rotate -5 #bottom
                pause 0.4
                ease 1.95 rotate 10 #top
                repeat
            parallel:
                pause 0.1
#                easeout .1 pos (407,262) #bottom(637,168)
                ease .15 pos (405,255) #bottom(637,168)
                pause 0.4
                ease 1.95 pos (420,292) #top 412
                repeat
    #End BJ animation Speed 0


image Laura_BJ_Body_1:
    #Her Body in the BJ pose, licking
    contains:
            #Hair underlay
            "Laura_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (535,340) #(523,380) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.4 rotate -50 #bottom
                pause 0.3
                ease 1.4 rotate -30 #top
                repeat
            parallel:
                pause 0.1
                easeout 1.2 xpos 470 #bottom
                easein .2 xpos 460 #bottom 481
                pause 0.3
                easeout .75 xpos 500 #top
                easein .65 xpos 535 #top
                repeat
            parallel:
                pause 0.1
                ease 1.4 ypos 500 #bottom
                pause 0.3
                ease 1.4 ypos 340 #top
                repeat
#    contains:
#            #base body
#            "Laura_Sprite"
#            pos (673,740)#(680,755) #top
#            zoom 2.2 #.75
#            anchor (0.5, 0.5)
#            rotate -20
#            subpixel True
#            parallel:
#                pause 0.15
#                ease 1.25 rotate -40 #bottom
#                pause 0.45
#                ease 1.35 rotate -20 #top
#                repeat
#            parallel:
#                pause 0.15
#                easeout .9 xpos 740 #bottom
#                easein .35 xpos 740 #bottom 481
#                pause 0.5
#                easeout .65 xpos 710 #top
#                easein .65 xpos 673 #top
#                repeat
#            parallel:
#                pause 0.15
#                ease 1.25 ypos 830 #bottom
#                pause 0.45
#                ease 1.35 ypos 740 #top
#                repeat
    contains:
            #base body
            "Laura_BJ_Body"
            anchor (100,180)#(0.6, 0.1)
            zoom 2.2 #.75
            pos (680,290)#(673,740) #top
            transform_anchor True
            rotate -20
            subpixel True
#            alpha 0.8
            parallel:
                pause 0.15
                ease 1.25 rotate -40 #bottom
                pause 0.45
                ease 1.35 rotate -20 #top
                repeat

            parallel:
                pause 0.1
                easeout 1.2 xpos 605#470 #bottom
                easein .2 xpos 595#460 #bottom 481
                pause 0.3
                easeout .75 xpos 635#500 #top
                easein .65 xpos 680#680#535 #top
                repeat
            parallel:
                pause 0.1
                ease 1.4 ypos 420#450#500 #bottom
                pause 0.3
                ease 1.4 ypos 290#340 #top
                repeat
    contains:
            #base head under cock
            subpixel True
            "Laura_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (535,340) #(523,380) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.4 rotate -50 #bottom
                pause 0.3
                ease 1.4 rotate -30 #top
                repeat
            parallel:
                pause 0.1
                easeout 1.2 xpos 470 #bottom
                easein .2 xpos 460 #bottom 481
                pause 0.3
                easeout .75 xpos 500 #top
                easein .65 xpos 535 #top
                repeat
            parallel:
                pause 0.1
                ease 1.4 ypos 500 #bottom
                pause 0.3
                ease 1.4 ypos 340 #top
                repeat
    contains:
            #zero's cock
#            ConditionSwitch(
#                "Player.Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Laura_BlowCock_Mask"), #Null(),
#                )
            AlphaMask("Blowcock", "Laura_BlowCock_Mask")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4
#            alpha 0.8#1
            rotate 10
            parallel:
                pause 0.1
                easeout 1.2 rotate 1 #bottom
                easein .3 rotate -1 #bottom
                pause 0.4
                ease 1.2 rotate 10 #top
                repeat
            parallel:
                pause 0.1
                easeout 1.2 pos (407,262) #bottom(637,168)
                easein .3 pos (405,255) #bottom(637,168)
                pause 0.4
                ease 1.2 pos (412,292) #top
                repeat
    #End BJ animation Speed 1

image Laura_BJ_Body_2:
    #Her Body in the BJ pose, heading
    contains:
            #Hair underlay
            "Laura_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (530,355) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                easeout 1.2 rotate -40 #bottom
                ease .6 rotate -32 #bottom
                pause 0.1
                ease 1.2 rotate -30 #top
                repeat
            parallel:
                pause 0.1
                easeout 1.2 xpos 510 #bottom 510
                ease .7 xpos 520 #bottom
                pause 0.1
                ease 1.1 xpos 530 #top
                repeat
            parallel:
                pause 0.1
                ease 1.6 ypos 400 #bottom
                pause 0.1
                ease 1.4 ypos 355 #top
                repeat
#    contains:
#            #base body
#            "Laura_Sprite"
#            pos (680,755)#(680,755) #top
#            zoom 2.2 #.75
#            anchor (0.5, 0.5)
#            rotate -20
#            subpixel True
#            parallel:
#                pause 0.15
#                ease 1.55 rotate -30 #bottom
#                pause 0.15
#                ease 1.35 rotate -20 #top
#                repeat
#            parallel:
#                pause 0.15
#                ease 1.35 xpos 730 #bottom 760
#                pause 0.25
#                ease 1.45 xpos 680 #top
#                repeat
#            parallel:
#                pause 0.15
#                ease 1.55 ypos 780 #bottom
#                pause 0.15
#                ease 1.35 ypos 755 #top
#                repeat
    contains:
            #base body
            "Laura_BJ_Body"
            anchor (100,180)#(0.6, 0.1)
            zoom 2.2 #.75
            pos (670,300)#(673,740) #top
            transform_anchor True
            rotate -20
            subpixel True
#            alpha 0.8
            parallel:
                pause 0.15
                ease 1.55 rotate -30 #bottom
                pause 0.15
                ease 1.35 rotate -20 #top
                repeat
            parallel:
                pause 0.1
                easeout 1.2 xpos 650#510 #bottom 510
                ease .7 xpos 660#520 #bottom
                pause 0.1
                ease 1.1 xpos 670#530 #top
                repeat
            parallel:
                pause 0.1
                ease 1.6 ypos 335#400 #bottom
                pause 0.1
                ease 1.4 ypos 300#355 #top
                repeat
    contains:
            #base head under cock
            subpixel True
            "Laura_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (530,355) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                easeout 1.2 rotate -40 #bottom
                ease .6 rotate -32 #bottom
                pause 0.1
                ease 1.2 rotate -30 #top
                repeat
            parallel:
                pause 0.1
                easeout 1.2 xpos 510 #bottom 510
                ease .7 xpos 520 #bottom
                pause 0.1
                ease 1.1 xpos 530 #top
                repeat
            parallel:
                pause 0.1
                ease 1.6 ypos 400 #bottom
                pause 0.1
                ease 1.4 ypos 355 #top
                repeat
    contains:
            #zero's cock
#            ConditionSwitch(
#                "Player.Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Laura_BlowCock_Mask"), #Null(),
#                )
            AlphaMask("Blowcock", "Laura_BlowCock_Mask")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4
            alpha 1
            rotate 10
            parallel:
                pause 1.3
                ease .4 rotate 8 #bottom
                pause .2
                ease 1 rotate 10 #top
                pause .3
                repeat
            parallel:
                pause 1.3
                ease .4 pos (410,285) #bottom(407,262)
                pause .2
                ease 1 pos (412,292) #top
                pause .3
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Laura_Sprite_BJ_Head", "images/LauraSprite/Laura_Sprite_SuckingMask.png")
            zoom 0.81
            anchor (0.5, 0.5)
            pos (530,355) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                easeout 1.2 rotate -40 #bottom
                ease .6 rotate -32 #bottom
                pause 0.1
                ease 1.2 rotate -30 #top
                repeat
            parallel:
                pause 0.1
                easeout 1.2 xpos 510 #bottom 510
                ease .7 xpos 520 #bottom
                pause 0.1
                ease 1.1 xpos 530 #top
                repeat
            parallel:
                pause 0.1
                ease 1.6 ypos 400 #bottom
                pause 0.1
                ease 1.4 ypos 355 #top
                repeat
    #End BJ animation Speed 2



image Laura_BlowCock_Mask_3:
    #This is a mask used by the blockcock during the Speed 3 sucking animation
    #it is a block moving in and out to prevent the cock sticking out the back.
    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,100)#(640,198)# top
#        block:
#                pause 0.1
#                ease 1.6 offset (0,300)# bottom
#                pause 0.1
#                ease 1.4 offset (0,0)# top
#                repeat

image Laura_BJ_Body_3:
    #Her Body in the BJ pose, sucking
    contains:
            #Hair underlay
            "Laura_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
#                pause 0.2
                ease .7 rotate -50 #bottom
#                pause 0.1
                ease 1 rotate -30 #top
                repeat
            parallel:
#                pause 0.2
                easeout .3 xpos 500 #bottom .7
                easein .4 xpos 481 #bottom .9
#                pause 0.1
                easeout .55 xpos 500 #top .75
                easein .45 xpos 523 #top .65
                repeat
            parallel:
#                pause 0.2
                ease .7 ypos 450 #bottom
#                pause 0.1
                ease 1 ypos 380 #top
                repeat
#    contains:
#            #base body
#            "Laura_Sprite"
#            pos (673,780)#(680,755) #top
#            zoom 2.2 #.75
#            anchor (0.5, 0.5)
#            rotate -20
#            subpixel True
#            parallel:
##                pause 0.15
#                ease .7 rotate -40 #bottom
##                pause 0.15
#                ease 1.0 rotate -20 #top
#                repeat
#            parallel:
##                pause 0.15
#                easeout .3 xpos 710 #bottom
#                easein .4 xpos 760 #bottom
##                pause 0.15
#                easeout .55 xpos 710 #top
#                easein .45 xpos 673 #top
#                repeat
#            parallel:
##                pause 0.15
#                ease .7 ypos 780 #bottom 830
##                pause 0.15
#                ease 1.0 ypos 780 #top
#                repeat
    contains:
            #base body
            "Laura_BJ_Body"
            anchor (100,180)#(0.6, 0.1)
            zoom 2.2 #.75
            pos (660,320)#(673,740) #top
            transform_anchor True
            rotate -20
            subpixel True
#            alpha 0.8
            parallel:
#                pause 0.15
                ease .7 rotate -40 #bottom
#                pause 0.15
                ease 1.0 rotate -20 #top
                repeat

            parallel:
#                pause 0.2
                easeout .3 xpos 637#500 #bottom .7
                easein .4 xpos 616#481 #bottom .9
#                pause 0.1
                easeout .55 xpos 637#500 #top .75
                easein .45 xpos 660#523 #top .65
                repeat
            parallel:
#                pause 0.2
                ease .7 ypos 370#450 #bottom
#                pause 0.1
                ease 1 ypos 320#380 #top
                repeat
    contains:
            #base head under cock
            subpixel True
            "Laura_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
#                pause 0.2
                ease .7 rotate -50 #bottom
#                pause 0.1
                ease 1 rotate -30 #top
                repeat
            parallel:
#                pause 0.2
                easeout .3 xpos 500 #bottom .7
                easein .4 xpos 481 #bottom .9
#                pause 0.1
                easeout .55 xpos 500 #top .75
                easein .45 xpos 523 #top .65
                repeat
            parallel:
#                pause 0.2
                ease .7 ypos 450 #bottom
#                pause 0.1
                ease 1 ypos 380 #top
                repeat
    contains:
            #zero's cock
#            ConditionSwitch(
#                "Player.Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Laura_BlowCock_Mask"), #Null(),
#                )
            AlphaMask("Blowcock", "Laura_BlowCock_Mask_3")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4
            alpha 1
            rotate 10
            parallel:
#                pause 0.2
                ease .7 rotate 0 #bottom
#                pause 0.1
                ease 1 rotate 10 #top
                repeat
            parallel:
#                pause 0.2
                ease .7 pos (407,262) #bottom(637,168)
#                pause 0.1
                ease 1 pos (412,292) #top
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Laura_Sprite_BJ_Head", "images/LauraSprite/Laura_Sprite_SuckingMask.png")
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
#                pause 0.2
                ease .7 rotate -50 #bottom
#                pause 0.1
                ease 1 rotate -30 #top
                repeat
            parallel:
#                pause 0.2
                easeout .3 xpos 500 #bottom .7
                easein .4 xpos 481 #bottom .9
#                pause 0.1
                easeout .55 xpos 500 #top .75
                easein .45 xpos 523 #top .65
                repeat
            parallel:
#                pause 0.2
                ease .7 ypos 450 #bottom
#                pause 0.1
                ease 1 ypos 380 #top
                repeat
    #End BJ animation Speed 3


image Laura_BlowCock_Mask_4:
    #This is a mask used by the blockcock during the Speed 4 deep throat animation
    #it is a block moving in and out to prevent the cock sticking out the back.
    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,0)#(640,198)# top
        block:
                pause 0.1
                ease 1.6 offset (0,300)# bottom
                pause 0.1
                ease 1.4 offset (0,0)# top
                repeat

image Laura_BJ_Body_4:
    #Her Body in the BJ pose, deep throat
    contains:
            #Hair underlay
            "Laura_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.6 rotate -50 #bottom
                pause 0.1
                ease 1.4 rotate -30 #top
                repeat
            parallel:
                pause 0.1
                easeout .7 xpos 500 #bottom
                easein .9 xpos 481 #bottom
                pause 0.1
                easeout .75 xpos 500 #top
                easein .65 xpos 523 #top
                repeat
            parallel:
                pause 0.1
                ease 1.6 ypos 500 #bottom
                pause 0.1
                ease 1.4 ypos 380 #top
                repeat
#    contains:
#            #base body
#            "Laura_Sprite"
#            pos (673,780)#(680,755) #top
#            zoom 2.2 #.75
#            anchor (0.5, 0.5)
#            rotate -20
#            subpixel True
#            parallel:
#                pause 0.15
#                ease 1.55 rotate -40 #bottom
#                pause 0.15
#                ease 1.35 rotate -20 #top
#                repeat
#            parallel:
#                pause 0.15
#                easeout .65 xpos 710 #bottom
#                easein .9 xpos 760 #bottom
#                pause 0.15
#                easeout .70 xpos 710 #top
#                easein .65 xpos 673 #top
#                repeat
#            parallel:
#                pause 0.15
#                ease 1.55 ypos 830 #bottom
#                pause 0.15
#                ease 1.35 ypos 780 #top
#                repeat
    contains:
            #base body
            "Laura_BJ_Body"
            anchor (100,180)#(0.6, 0.1)
            zoom 2.2 #.75
            pos (660,320)#(673,740) #top
            transform_anchor True
            rotate -30
            subpixel True
#            alpha 0.8
            parallel:
                pause 0.15
                ease 1.25 rotate -40 #bottom
                pause 0.45
                ease 1.35 rotate -30 #top
                repeat

            parallel:
                pause 0.1
                easeout .7 xpos 637#500 #bottom
                easein .9 xpos 596#481 #bottom
                pause 0.1
                easeout .75 xpos 637#500 #top
                easein .65 xpos 660#523 #top
                repeat
            parallel:
                pause 0.1
                ease 1.6 ypos 410#500 #bottom
                pause 0.1
                ease 1.4 ypos 320#380 #top
                repeat
    contains:
            #base head under cock
            subpixel True
            "Laura_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.6 rotate -50 #bottom
                pause 0.1
                ease 1.4 rotate -30 #top
                repeat
            parallel:
                pause 0.1
                easeout .7 xpos 500 #bottom
                easein .9 xpos 481 #bottom
                pause 0.1
                easeout .75 xpos 500 #top
                easein .65 xpos 523 #top
                repeat
            parallel:
                pause 0.1
                ease 1.6 ypos 500 #bottom
                pause 0.1
                ease 1.4 ypos 380 #top
                repeat
    contains:
            #zero's cock
#            ConditionSwitch(
#                "Player.Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Laura_BlowCock_Mask"), #Null(),
#                )
            AlphaMask("Blowcock", "Laura_BlowCock_Mask_4")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4
            alpha 1
            rotate 10
            parallel:
                pause 0.1
                ease 1.6 rotate 0 #bottom
                pause 0.1
                ease 1.4 rotate 10 #top
                repeat
            parallel:
                pause 0.1
                ease 1.6 pos (407,262) #bottom(637,168)
                pause 0.1
                ease 1.4 pos (412,292) #top
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Laura_Sprite_BJ_Head", "images/LauraSprite/Laura_Sprite_SuckingMask.png")
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.6 rotate -50 #bottom
                pause 0.1
                ease 1.4 rotate -30 #top
                repeat
            parallel:
                pause 0.1
                easeout .7 xpos 500 #bottom
                easein .9 xpos 481 #bottom
                pause 0.1
                easeout .75 xpos 500 #top
                easein .65 xpos 523 #top
                repeat
            parallel:
                pause 0.1
                ease 1.6 ypos 500 #bottom
                pause 0.1
                ease 1.4 ypos 380 #top
                repeat
    #End BJ animation Speed 4


image Laura_BJ_Body_5:
    #Her Body in the BJ pose, high cumming
    contains:
            #Hair underlay
            "Laura_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (520,375) #(530,355) #bottom
            rotate -50 #-30
            parallel:
                pause 1
                ease .3 rotate -30 #top
                easeout .3 rotate -32 #bottom
                easein .5 rotate -35 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                easein .3 xpos 530 #top
                easeout .3 xpos 525 #bottom
                easein .5 xpos 520 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                ease .3 ypos 355 #top
                easeout .3 ypos 365 #bottom
                easein .5 ypos 375 #bottom
                pause .5
                repeat
#    contains:
#            #base body
#            "Laura_Sprite"
#            subpixel True
#            zoom 2.2 #.75
#            anchor (0.5, 0.5)
#            rotate -30
#            pos (730,760)#(680,755) #bottom
#            parallel:
#                pause 1
#                ease .3 rotate -26 #top
#                easeout .3 rotate -28 #bottom
#                easein .5 rotate -30 #bottom
#                pause .5
#                repeat
#            parallel:
#                pause 1
#                easein .3 xpos 710 #top 680
#                easeout .3 xpos 720 #bottom
#                easein .5 xpos 730 #bottom
#                pause .5
#                repeat
#            parallel:
#                pause 1
#                ease .3 ypos 750 #top 755
#                easeout .3 ypos 755 #bottom
#                easein .5 ypos 760 #bottom
#                pause .5
#                repeat
    contains:
            #base body
            "Laura_BJ_Body"
            anchor (100,180)#(0.6, 0.1)
            zoom 2.2 #.75
            pos (670,315)#(673,740) #top
            transform_anchor True
            rotate -30
            subpixel True
#            alpha 0.8
            parallel:
                pause 1
                ease .3 rotate -26 #top
                easeout .3 rotate -28 #bottom
                easein .5 rotate -30 #bottom
                pause .5
                repeat

            parallel:
                pause 1
                easein .3 xpos 680 #top
                easeout .3 xpos 675 #bottom
                easein .5 xpos 670 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                ease .3 ypos 295 #top
                easeout .3 ypos 305 #bottom
                easein .5 ypos 315 #bottom
                pause .5
                repeat
    contains:
            #base head under cock
            subpixel True
            "Laura_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (520,375) #(530,355) #bottom
            rotate -35 #-30
            parallel:
                pause 1
                ease .3 rotate -30 #top
                easeout .3 rotate -32 #bottom
                easein .5 rotate -35 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                easein .3 xpos 530 #top
                easeout .3 xpos 525 #bottom
                easein .5 xpos 520 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                ease .3 ypos 355 #top
                easeout .3 ypos 365 #bottom
                easein .5 ypos 375 #bottom
                pause .5
                repeat
    contains:
            #zero's cock
#            ConditionSwitch(
#                "Player.Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Laura_BlowCock_Mask"), #Null(),
#                )
            AlphaMask("Blowcock", "Laura_BlowCock_Mask")
            subpixel True
            pos (410,292) #bottom
            zoom 0.4
            alpha 1
            rotate 12
            parallel:
                pause 1
                ease .3 rotate 10 #top
                ease .3 rotate 12 #bottom
                pause 1
                repeat
            parallel:
                pause 1
                ease .3 pos (412,285) #top
                ease .3 pos (410,292) #bottom(637,168)
                pause 1
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Laura_Sprite_BJ_Head", "images/LauraSprite/Laura_Sprite_SuckingMask.png")
            zoom 0.81
            anchor (0.5, 0.5)
            pos (520,375) #(530,355) #bottom
            rotate -35 #-30
            parallel:
                pause 1
                ease .3 rotate -30 #top
                easeout .3 rotate -32 #bottom
                easein .5 rotate -35 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                easein .3 xpos 530 #top
                easeout .3 xpos 525 #bottom
                easein .5 xpos 520 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                ease .3 ypos 355 #top
                easeout .3 ypos 365 #bottom
                easein .5 ypos 375 #bottom
                pause .5
                repeat
    #End BJ animation Speed 5

image Laura_BlowCock_Mask_6:
    #This is a mask used by the blockcock during the Speed 4 deep throat animation
    #it is a block moving in and out to prevent the cock sticking out the back.
    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,300)#(640,198)# top
#        block:
#                pause 0.1
#                ease 1.6 offset (0,300)# bottom
#                pause 0.1
#                ease 1.4 offset (0,0)# top
#                repeat

image Laura_BJ_Body_6:
    #Her Body in the BJ pose, deep throat cumming
    contains:
            #Hair underlay
            "Laura_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (481,500) #(530,355) #bottom
            rotate -50 #-30
            parallel:
                pause 1
                ease .3 rotate -45 #top
                easeout .3 rotate -48 #bottom
                easein .5 rotate -50 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                easein .3 xpos 490 #top
                easeout .3 xpos 485 #bottom
                easein .5 xpos 481 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                ease .3 ypos 490 #top
                easeout .3 ypos 496 #bottom
                easein .5 ypos 500 #bottom
                pause .5
                repeat
#    contains:
#            #base body
#            "Laura_Sprite"
#            subpixel True
#            zoom 2.2 #.75
#            anchor (0.5, 0.5)
#            rotate -40
#            pos (760,830)#(680,755) #bottom
#            parallel:
#                pause 1
#                ease .3 rotate -38 #top
#                easeout .3 rotate -39 #bottom
#                easein .5 rotate -40 #bottom
#                pause .5
#                repeat
#            parallel:
#                pause 1
#                easein .3 xpos 750 #top
#                easeout .3 xpos 756 #bottom
#                easein .5 xpos 760 #bottom
#                pause .5
#                repeat
#            parallel:
#                pause 1
#                ease .3 ypos 835 #top
#                easeout .3 ypos 830 #bottom
#                easein .5 ypos 830 #bottom
#                pause .5
#                repeat
    contains:
            #base body
            "Laura_BJ_Body"
            anchor (100,180)#(0.6, 0.1)
            zoom 2.2 #.75
            pos (610,415)#(673,740) #top
            transform_anchor True
            rotate -40
            subpixel True
#            alpha 0.8
            parallel:
                pause 1
                ease .3 rotate -38 #top
                easeout .3 rotate -39 #bottom
                easein .5 rotate -40 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                easein .3 xpos 620 #top
                easeout .3 xpos 615 #bottom
                easein .5 xpos 610 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                ease .3 ypos 400 #top
                easeout .3 ypos 405 #bottom
                easein .5 ypos 415 #bottom
                pause .5
                repeat
    contains:
            #base head under cock
            subpixel True
            "Laura_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (481,500) #(530,355) #bottom
            rotate -50 #-30
            parallel:
                pause 1
                ease .3 rotate -45 #top
                easeout .3 rotate -48 #bottom
                easein .5 rotate -50 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                easein .3 xpos 490 #top
                easeout .3 xpos 485 #bottom
                easein .5 xpos 481 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                ease .3 ypos 490 #top
                easeout .3 ypos 496 #bottom
                easein .5 ypos 500 #bottom
                pause .5
                repeat
    contains:
            #zero's cock
#            ConditionSwitch(
#                "Player.Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Laura_BlowCock_Mask"), #Null(),
#                )
            AlphaMask("Blowcock", "Laura_BlowCock_Mask_6")
            subpixel True
            pos (407,262) #bottom
            zoom 0.4
            alpha 1
            rotate 0
            parallel:
                pause 1
                ease .3 rotate 2 #top
                ease .3 rotate 0 #bottom
                pause 1
                repeat
            parallel:
                pause 1
                ease .3 pos (409,268) #top
                ease .3 pos (407,262) #bottom(637,168)
                pause 1
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Laura_Sprite_BJ_Head", "images/LauraSprite/Laura_Sprite_SuckingMask.png")
            zoom 0.81
            anchor (0.5, 0.5)
            pos (481,500) #(530,355) #bottom
            rotate -50 #-30
            parallel:
                pause 1
                ease .3 rotate -45 #top
                easeout .3 rotate -48 #bottom
                easein .5 rotate -50 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                easein .3 xpos 490 #top
                easeout .3 xpos 485 #bottom
                easein .5 xpos 481 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                ease .3 ypos 490 #top
                easeout .3 ypos 496 #bottom
                easein .5 ypos 500 #bottom
                pause .5
                repeat
    #End BJ animation Speed 6
#Head and Body Animations for Laura's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
                                                               #BJ Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                               #BJ Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Laura_BJ_Launch(Line = Trigger):
    # The sequence to launch the Laura BJ animations
    $ LauraX.ArmPose = 1
    if renpy.showing("Laura_BJ_Animation") and LauraX.Pose != "69":
        return
    elif renpy.showing("Laura_69_Animation") and LauraX.Pose == "69":
        return

    if not Player.Male:
        call Laura_CUN_Launch
        return

    call Girl_Hide(LauraX)
    if Line == "L" or Line == "cum":
        show Laura_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1
            ease 1 zoom 2.5 offset (150,80)
        with dissolve
    else:
        show Laura_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1
            zoom 2.5 offset (150,80)
        with dissolve

    $ Speed = 0
    if Line == "L": # Laura gets started. . .
            if Taboo:
                if len(Present) >= 2:
                    if Present[0] != LauraX:
                            "[LauraX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                    elif Present[1] != LauraX:
                            "[LauraX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
                else:
                            "[LauraX.Name] небрежно оглядывается по сторонам, чтобы убедиться, что никто не наблюдает."
            "[LauraX.Name] плавно наклоняется и прислоняет ваш член к своей щеке."

    if Line != "cum":
        $ Trigger = "blow"

    hide Laura_Sprite

    if LauraX.Pose == "69":
            show Laura_69_Animation zorder 150
    else:
            show Laura_BJ_Animation zorder 150:
                pos (645,510)
    return

label Laura_BJ_Reset: # The sequence to the Laura animations from BJ to default
    if Player.Male != 1:
            call Laura_CUN_Reset
    if not renpy.showing("Laura_BJ_Animation") and not renpy.showing("Laura_69_Animation"):
        return
#    hide Laura_BJ_Animation
    call Girl_Hide(LauraX)
    $ Speed = 0

    show Laura_Sprite at SpriteLoc(StageCenter) zorder 150:
        alpha 1 zoom 2.5 offset (150,80)
    with dissolve

    show Laura_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
        alpha 1 zoom 1 offset (0,0)
    return

# End Laura Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Laura's TJ animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Animation components / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# start base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Laura_TJ_Animation:
            #core TJ animation
            contains:
                ConditionSwitch(
                    # Laura's upper body
                    "not Player.Sprite","Laura_TJ_0",#Static
                    "Speed == 1", "Laura_TJ_1",#slow
                    "Speed == 4", "Laura_TJ_4",#cumming high
                    "Speed == 5", "Laura_TJ_5",#cumming low
                    "Speed >= 2", "Laura_TJ_2",#fast
                    "True",       "Laura_TJ_0",#Static
                    )
            zoom .7 #0.6
            transform_anchor True
            anchor (.5,.5)
# end base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



image Laura_TJ_HairBack:
            #Hair underlay
            "Laura_Sprite_HairBack"
            transform_anchor True
            zoom 2.5
            anchor (0.5, 0.5)
            offset (320,100)
            rotate 0

image Laura_TJ_Head:
            #Hair underlay
            "Laura_Sprite_Head"
            transform_anchor True
            zoom 2.5
            anchor (0.5, 0.5)
            offset (320,100)
            rotate 0

image Laura_TJ_HairMid:
            #Hair midlayer
            "Laura_Sprite_HairMid"
            transform_anchor True
            zoom 2.5
            anchor (0.5, 0.5)
            rotate 20
            offset (320,100)
            rotate 0

image Laura_TJ_HairTop:
            #Hair overlay
            "Laura_Sprite_HairTop"
            transform_anchor True
            zoom 2.5 #2.1
            anchor (0.5, 0.5)
            offset (320,100) # (300,275)
            rotate 0

image Laura_TJ_ZeroCock:
            #cock used in laura's sex pose
            "Zero_Blowcock"
            transform_anchor True
            zoom .7
            anchor (0.5, 0.5)
            offset (220,670)#(300,750)
            rotate 0

image Laura_TJ_Body:
            #body underlay
            contains:
                "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_Body.png"
            contains:
                ConditionSwitch(
                        "not LauraX.Neck",Null(),
                        "True",       "images/LauraSex/Laura_Titjob_Neck_[LauraX.Neck].png",
                        )
            contains:
                ConditionSwitch(
                        "'tits' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_Titjob_Spunk_Chest.png",
                        "True", Null(),
                        )
            transform_anchor True
            zoom 1
            anchor (0.4, 1.0)
            offset (410,770) # (300,275)
            rotate 0


image Laura_TJ_LeftArm:
            #left arm
            contains:
                "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_LeftHand.png"
            contains:
                ConditionSwitch(
                        "not LauraX.Arms",Null(),
                        "LauraX.Arms == 'gloves'",       Recolor("Laura", "Arms", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_LeftGlove.png"),
                        "True",       Recolor("Laura", "Arms", "images/LauraSex/Laura_Titjob_wrists.png"),
                        )
            contains:
                # Left Piercings
                ConditionSwitch(
                        "not LauraX.Pierce",Null(),
                        "True",       "images/LauraSex/Laura_Titjob_Left_[LauraX.Pierce].png",
                        )

image Laura_TJ_RightArm:
            #left arm
            contains:
                "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_RightHand.png"
            contains:
                ConditionSwitch(
                        "LauraX.Arms == 'gloves'",       Recolor("Laura", "Arms", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_RightGlove.png"),
                        "True", Null(),
                        )
            contains:
                # Right Piercings
                ConditionSwitch(
                        "not LauraX.Pierce",Null(),
                        "True",       "images/LauraSex/Laura_Titjob_Right_[LauraX.Pierce].png",
                        )

image Laura_TJ_RightArmBack:
            #left arm
            contains:
                "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_RightHandBack.png"
            contains:
                ConditionSwitch(
                        "LauraX.Arms == 'gloves'",       Recolor("Laura", "Arms", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_RightGloveBack.png"),
                        "True", Null(),
                        )

# Animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start 0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Laura_TJ_0:
        #Her Body in the TJ pose, static
        contains:
                #hairback
                "Laura_TJ_HairBack"
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
                #base body test
                "Laura_TJ_Body"
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
                #right hand backside
                "Laura_TJ_RightArmBack" #"images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_RightHandBack.png"
                subpixel True
                pos (0,-15) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -5
                    pause .1
                    ease 2 ypos -15
                    pause .1
                    repeat
        contains:
                contains:
                    "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_RightTit.png"
                contains:
                    ConditionSwitch(
                            "'tits' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_Titjob_Spunk_Right.png",
                            "True", Null(),
                            )
                subpixel True
                pos (0,-15) #top (0,-10)
                transform_anchor True
                parallel:
                    pause .1
                    ease 2 ypos -5
                    pause .1
                    ease 2 ypos -15
                    repeat
        contains:
                #right hand
#                contains:
#                    "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_RightHand.png"
#                contains:
#                    # Right Piercings
#                    ConditionSwitch(
#                            "not LauraX.Pierce",Null(),
#                            "True",       "images/LauraSex/Laura_Titjob_Right_[LauraX.Pierce].png",
#                            )
                "Laura_TJ_RightArm"
                subpixel True
                pos (0,-15) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -5
                    pause .1
                    ease 2 ypos -15
                    pause .1
                    repeat
        contains:
                #head
                "Laura_TJ_Head"
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
                #zero cock
                subpixel True
                "Laura_TJ_ZeroCock"
                pos (0,30) #top (0,-10)
                transform_anchor True
                rotate -2
                parallel:
                    ease 2 rotate -2
                    pause .1
                    ease 2 rotate 3
                    pause .1
                    repeat
        contains:
                #left tit
                contains:
                    "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_LeftTit.png"
                contains:
                    ConditionSwitch(
                            "'tits' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_Titjob_Spunk_Left.png",
                            "True", Null(),
                            )
                subpixel True
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    pause .1
                    ease 2 ypos -40
                    pause .1
                    ease 2 ypos 0
                    repeat
        contains:
                #left hand
                "Laura_TJ_LeftArm"
#                contains:
#                    "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_LeftHand.png"
#                contains:
#                    # Left Piercings
#                    ConditionSwitch(
#                            "not LauraX.Pierce",Null(),
#                            "True",       "images/LauraSex/Laura_Titjob_Left_[LauraX.Pierce].png",
#                            )
                subpixel True
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -40
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat
        contains:
                #mid hair
                "Laura_TJ_HairMid"
                subpixel True
                pos (0,0) #top (0,+10)
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
                #head
                "Laura_TJ_HairTop"
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
# End Laura TJ Pose 0 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start 1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Laura_TJ_1:
        #Her Body in the TJ pose, slow
        contains:
                #hairback
                "Laura_TJ_HairBack"
                subpixel True
                pos (0,150) #top (0,-10)
                transform_anchor True
                rotate -5
                parallel:
                    ease 2 ypos 0
                    pause .2
                    ease 2 ypos 150
                    pause .5
                    repeat
                parallel:
                    ease 2 rotate 0
                    pause .2
                    ease 2 rotate -5
                    pause .5
                    repeat
        contains:
                #base body
                "Laura_TJ_Body"
                subpixel True
                pos (0,150) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos 0
                    pause .2
                    ease 2 ypos 150
                    pause .5
                    repeat
        contains:
                #right hand backside
                "Laura_TJ_RightArmBack"
                subpixel True
                pos (0,150) #top (0,-10)
                transform_anchor True
                block:
                    ease 2 ypos -20
                    pause .4
                    ease 1.8 ypos 150
                    pause .5
                    repeat
        contains:
                contains:
                    "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_RightTit.png"
                contains:
                    ConditionSwitch(
                            "'tits' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_Titjob_Spunk_Right.png",
                            "True", Null(),
                            )
                subpixel True
                pos (0,150) #top (0,-10)
                transform_anchor True
                block:
                    pause .1
                    ease 1.9 ypos -20
                    pause .4
                    ease 1.8 ypos 150
                    ease .5 ypos 140
                    repeat
        contains:
                #right hand
#                contains:
#                    "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_RightHand.png"
#                contains:
#                    # Right Piercings
#                    ConditionSwitch(
#                            "not LauraX.Pierce",Null(),
#                            "True",       "images/LauraSex/Laura_Titjob_Right_[LauraX.Pierce].png",
#                            )
                "Laura_TJ_RightArm"
                subpixel True
                pos (0,150) #top (0,-10)
                transform_anchor True
                block:
                    ease 2 ypos -20
                    pause .4
                    ease 1.8 ypos 150
                    pause .5
                    repeat
        contains:
                #head
                "Laura_TJ_Head"
                subpixel True
                pos (0,150) #top (0,-10)
                transform_anchor True
                rotate -5
                parallel:
                    ease 2 ypos 0
                    pause .2
                    ease 2 ypos 150
                    pause .5
                    repeat
                parallel:
                    ease 2 rotate 0
                    pause .2
                    ease 2 rotate -5
                    pause .5
                    repeat
        contains:
                #zero cock
                subpixel True
                "Laura_TJ_ZeroCock"
                pos (0,25) #top (0,-10)
                transform_anchor True
                rotate -5
                parallel:
                    ease 2 ypos 0
                    pause .4
                    ease 1.8 ypos 25
                    pause .5
                    repeat
                parallel:
                    ease 2 rotate 0
                    pause .2
                    ease 2 rotate -5
                    pause .5
                    repeat
        contains:
                #left tit
                contains:
                    "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_LeftTit.png"
                contains:
                    ConditionSwitch(
                            "'tits' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_Titjob_Spunk_Left.png",
                            "True", Null(),
                            )
                subpixel True
                pos (0,150) #top (0,-10)
                transform_anchor True
                block:
                    pause .1
                    ease 1.9 ypos -20
                    pause .4
                    ease 1.8 ypos 150
                    ease .5 ypos 140
                    repeat
        contains:
                #left hand
                "Laura_TJ_LeftArm"
                subpixel True
                pos (0,150) #top (0,-10)
                transform_anchor True
                block:
                    ease 2 ypos -20
                    pause .4
                    ease 1.8 ypos 150
                    pause .5
                    repeat
        contains:
                #mid hair
                "Laura_TJ_HairMid"
                subpixel True
                pos (0,160) #top (0,150)
                transform_anchor True
                rotate -5
                parallel:
                    ease 2 ypos -20#-20
                    pause .4
                    ease 1.8 ypos 160
                    pause .5
                    repeat
                parallel:
                    ease 2 rotate 0
                    pause .2
                    ease 2 rotate -5
                    pause .5
                    repeat
        contains:
                #head
                "Laura_TJ_HairTop"
                subpixel True
                pos (0,150) #top (0,-10)
                transform_anchor True
                rotate -5
                parallel:
                    ease 2 ypos 0
                    pause .2
                    ease 2 ypos 150
                    pause .5
                    repeat
                parallel:
                    ease 2 rotate 0
                    pause .2
                    ease 2 rotate -5
                    pause .5
                    repeat
# End Laura TJ Pose 1 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start 2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Laura_TJ_2:
        #Her Body in the TJ pose, fast
        contains:
                #hairback
                "Laura_TJ_HairBack"
                subpixel True
                pos (0,80) #top (0,-10)
                transform_anchor True
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
                #base body
                "Laura_TJ_Body"
                subpixel True
                pos (0,80) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 1 ypos -20
                    pause .1
                    ease .5 ypos 80
                    repeat
        contains:
                #right hand backside
                "Laura_TJ_RightArmBack"
                subpixel True
                pos (0,80) #top (0,-10)
                transform_anchor True
                block:
                    ease 1 ypos -40
                    pause .2
                    ease .4 ypos 80
                    repeat
        contains:
                contains:
                    "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_RightTit.png"
                contains:
                    ConditionSwitch(
                            "'tits' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_Titjob_Spunk_Right.png",
                            "True", Null(),
                            )
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
                #right hand
#                contains:
#                    "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_RightHand.png"
#                contains:
#                    # Right Piercings
#                    ConditionSwitch(
#                            "not LauraX.Pierce",Null(),
#                            "True",       "images/LauraSex/Laura_Titjob_Right_[LauraX.Pierce].png",
#                            )
                "Laura_TJ_RightArm"
                subpixel True
                pos (0,80) #top (0,-10)
                transform_anchor True
                block:
                    ease 1 ypos -40
                    pause .2
                    ease .4 ypos 80
                    repeat
        contains:
                #head
                "Laura_TJ_Head"
                subpixel True
                pos (0,80) #top (0,-10)
                transform_anchor True
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
                #zero cock
                subpixel True
                "Laura_TJ_ZeroCock"
                pos (0,30) #top (0,-10)
                transform_anchor True
                rotate -2
                parallel:
                    ease 1 ypos 0
                    pause .2
                    ease .4 ypos 30
                    repeat
                parallel:
                    ease 1 rotate 0
                    pause .1
                    ease .5 rotate -2
                    repeat
        contains:
                #left tit
                contains:
                    "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_LeftTit.png"
                contains:
                    ConditionSwitch(
                            "'tits' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_Titjob_Spunk_Left.png",
                            "True", Null(),
                            )
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
                #left hand
                "Laura_TJ_LeftArm"
                subpixel True
                pos (0,80) #top (0,-10)
                transform_anchor True
                block:
                    ease 1 ypos -40
                    pause .2
                    ease .4 ypos 80
                    repeat
        contains:
                #mid hair
                "Laura_TJ_HairMid"
                subpixel True
                pos (0,90) #top (0,+10)
                transform_anchor True
                rotate -5
                parallel:
                    ease 1 ypos -40#-20
                    pause .2
                    ease .4 ypos 90
                    repeat
                parallel:
                    ease 1 rotate 0
                    pause .2
                    ease .4 rotate -5
                    repeat
        contains:
                #head
                "Laura_TJ_HairTop"
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
# End Laura TJ Pose 2 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start 4 (cumming high) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Laura_TJ_4:
        #Her Body in the TJ pose, cumming
        contains:
                #hairback
                "Laura_TJ_HairBack"
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
                #base body
                "Laura_TJ_Body"
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
                #right hand backside
                "Laura_TJ_RightArmBack"
                subpixel True
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -30
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat
        contains:
                contains:
                    "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_RightTit.png"
                contains:
                    ConditionSwitch(
                            "'tits' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_Titjob_Spunk_Right.png",
                            "True", Null(),
                            )
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
                #right hand
#                contains:
#                    "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_RightHand.png"
#                contains:
#                    # Right Piercings
#                    ConditionSwitch(
#                            "not LauraX.Pierce",Null(),
#                            "True",       "images/LauraSex/Laura_Titjob_Right_[LauraX.Pierce].png",
#                            )
                "Laura_TJ_RightArm"
                subpixel True
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -30
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat
        contains:
                #head
                "Laura_TJ_Head"
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
                #zero cock
                subpixel True
                "Laura_TJ_ZeroCock"
                pos (0,20) #top (0,-10)
                transform_anchor True
                rotate 2
                parallel:
                    ease 2 ypos 0
                    pause .1
                    ease 2 ypos 20
                    pause .1
                    repeat
        contains:
                #left tit
                contains:
                    "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_LeftTit.png"
                contains:
                    ConditionSwitch(
                            "'tits' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_Titjob_Spunk_Left.png",
                            "True", Null(),
                            )
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
                #left hand
                "Laura_TJ_LeftArm"
                subpixel True
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -30
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat
        contains:
                #mid hair
                "Laura_TJ_HairMid"
                subpixel True
                pos (0,0) #top (0,+10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos -15
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
                #head
                "Laura_TJ_HairTop"
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
# End Laura TJ Pose 4 cumming / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start 5 (cumming low) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Laura_TJ_5:
        #Her Body in the TJ pose, cumming low
        contains:
                #hairback
                "Laura_TJ_HairBack"
                subpixel True
                pos (-30,155)
                transform_anchor True
                rotate -20
                parallel:
                    ease 2 ypos 140
                    pause .1
                    ease 2 ypos 155
                    pause .1
                    repeat
#        contains:
#                #base body
#                contains:
#                    "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_Body.png"
#                subpixel True
#                pos (-80,-200)
#                transform_anchor True
#                rotate -20
#                parallel:
#                    ease 2 ypos -220
#                    pause .1
#                    ease 2 ypos -200
#                    pause .1
#                    repeat
        contains:
                #base body
                "Laura_TJ_Body"
                subpixel True
                pos (185,70)
                transform_anchor True
                rotate -20
                parallel:
                    ease 2 ypos 50
                    pause .1
                    ease 2 ypos 70
                    pause .1
                    repeat
        contains:
                #right hand backside
                contains:
                    "Laura_TJ_RightArmBack"
                subpixel True
                pos (-80,-180)
                transform_anchor True
                rotate -10
                parallel:
                    ease 2 ypos -200
                    pause .1
                    ease 2 ypos -180
                    pause .1
                    repeat
        contains:
                #right tit
                contains:
                    "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_RightTit.png"
                contains:
                    ConditionSwitch(
                            "'tits' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_Titjob_Spunk_Right.png",
                            "True", Null(),
                            )
                subpixel True
                pos (-80,-160)
                transform_anchor True
                rotate -10
                parallel:
                    ease .4 ypos -170
                    ease 1.7 ypos -190
                    pause .1
                    ease 2 ypos -160
                    repeat
        contains:
                #right hand
#                contains:
#                    "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_RightHand.png"
#                contains:
#                    # Right Piercings
#                    ConditionSwitch(
#                            "not LauraX.Pierce",Null(),
#                            "True",       "images/LauraSex/Laura_Titjob_Right_[LauraX.Pierce].png",
#                            )
                "Laura_TJ_RightArm"
                subpixel True
                pos (-80,-180)
                transform_anchor True
                rotate -10
                parallel:
                    ease 2 ypos -200
                    pause .1
                    ease 2 ypos -180
                    pause .1
                    repeat
        contains:
                #head
                "Laura_TJ_Head"
                subpixel True
                pos (-30,155)
                transform_anchor True
                rotate -20
                parallel:
                    ease 2 ypos 140
                    pause .1
                    ease 2 ypos 155
                    pause .1
                    repeat
        contains:
                #zero cock
                subpixel True
                "Laura_TJ_ZeroCock"
                pos (0,20) #top (0,-10)
                transform_anchor True
                rotate 2
                parallel:
                    ease 2 ypos 0
                    pause .1
                    ease 2 ypos 20
                    pause .1
                    repeat
        contains:
                #left tit
                contains:
                    "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Titjob_LeftTit.png"
                contains:
                    ConditionSwitch(
                            "'tits' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_Titjob_Spunk_Left.png",
                            "True", Null(),
                            )
                subpixel True
                pos (-80,-160)
                transform_anchor True
                rotate -10
                parallel:
                    ease .4 ypos -170
                    ease 1.7 ypos -190
                    pause .1
                    ease 2 ypos -160
                    repeat
        contains:
                #left hand
                "Laura_TJ_LeftArm"
                subpixel True
                pos (-80,-180)
                transform_anchor True
                rotate -10
                parallel:
                    ease 2 ypos -200
                    pause .1
                    ease 2 ypos -180
                    pause .1
                    repeat
        contains:
                #mid hair
                "Laura_TJ_HairMid"
                subpixel True
                pos (-30,115)
                transform_anchor True
                rotate -10
                parallel:
                    ease 2 ypos 95
                    pause .1
                    ease 2 ypos 115
                    pause .1
                    repeat
        contains:
                #head
                "Laura_TJ_HairTop"
                subpixel True
                pos (-30,155)
                transform_anchor True
                rotate -20
                parallel:
                    ease 2 ypos 140
                    pause .1
                    ease 2 ypos 155
                    pause .1
                    repeat
# End Laura TJ Pose 5 cumming / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Laura's TJ animations end / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Laura_TJ_Launch(Line = Trigger):    # The sequence to launch the Laura Titfuck animations
    if renpy.showing("Laura_TJ_Animation"):
        return
    call Girl_Hide(LauraX)
    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 2.3 xpos 750 yoffset -100
    if Line == "L": # Laura gets started. . .
            if Taboo:
                if len(Present) >= 2:
                    if Present[0] != LauraX:
                            "[LauraX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                    elif Present[1] != LauraX:
                            "[LauraX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
                else:
                            "[LauraX.Name] небрежно оглядывается по сторонам, чтобы убедиться, что никто не наблюдает."
            "[LauraX.Name] наклоняется и помещает ваш член между своих грудей."

    if LauraX.Chest and LauraX.Over:
        "Она сбрасывает [get_clothing_name(LauraX.Over_key, vin)] и [get_clothing_name(LauraX.Chest_key, vin)]."
    elif LauraX.Over:
        "Она сбрасывает [get_clothing_name(LauraX.Over_key, vin)], обнажая свою грудь."
    elif LauraX.Chest:
        "Она стягивает [get_clothing_name(LauraX.Chest_key, vin)] и отбрасывает в сторону."
    $ LauraX.Over = 0
    $ LauraX.Chest = 0
    $ LauraX.ArmPose = 0

    call Girl_First_Topless(LauraX)

    show blackscreen onlayer black with dissolve
    show Laura_Sprite:
        alpha 0
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "titjob"
    show Laura_TJ_Animation zorder 150:
        pos (700,520) #700,420)
    $ Player.Sprite = 1
    hide blackscreen onlayer black with dissolve
    return

label Laura_TJ_Reset:
    # The sequence to the Laura animations from Titfuck to default
    if not renpy.showing("Laura_TJ_Animation"):
        return
#    hide Laura_TJ_Animation
    call Girl_Hide(LauraX)
    $ Player.Sprite = 0

    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder 150:
        zoom 2.3 xpos 750 yoffset -100
    show Laura_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 xpos 700 yoffset 50
        pause .5
        ease .5 zoom 1 xpos LauraX.SpriteLoc yoffset 0
    "[LauraX.Name] отстраняется"
    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
        alpha 1 zoom 1 offset (0,0) xpos LauraX.SpriteLoc
    return

# End Laura TJ Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Laura Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Laura Handjob element //////////////////////////////////////////////////////////////////////

image Laura_HJ_Body:
    "Laura_Sprite"
    pos (-180,-1250)#680,-1250
    zoom 4.8#2.15


transform Laura_HJ_Body_1():
    subpixel True
#    pos (700,-1250)#(350,-550)
    block:
        ease .5 ypos -1220
        pause 0.25
        ease 1.0 ypos -1250
        pause 0.1
        repeat

transform Laura_HJ_Body_2():
    subpixel True
#    pos (350,-550)
    block:
        ease 0.2 ypos -1240
        pause 0.1
        ease 0.4 ypos -1250
        pause 0.1
        repeat

image Laura_Hand_Under:
    "images/LauraSprite/[LauraX.skin_image.skin_path]handlaura2.png"
    anchor (0.5,0.5)
    pos (-10,0)


image Laura_Hand_Over:
    "images/LauraSprite/[LauraX.skin_image.skin_path]handlaura1.png"
    anchor (0.5,0.5)
    pos (-10,0)

transform Laura_Hand_1():
    subpixel True
    pos (-20,-100)
    rotate 5
    block:
        ease .5 pos (0,150) rotate -5 #ypos 150 rotate 5 Bottom
        pause 0.25
        ease 1.0 pos (-20,-100) rotate 5 #250#-150 #rotate -10#  Top
        pause 0.1
        repeat

transform Laura_Hand_2():
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

image Laura_HJ_Animation:
    contains:
        ConditionSwitch(
            # backside of the hand
            "not Speed", Transform("Laura_HJ_Body"),
            "Speed == 1", At("Laura_HJ_Body", Laura_HJ_Body_1()),
            "Speed >= 2", At("Laura_HJ_Body", Laura_HJ_Body_2()),
            "Speed", Null(),
            )
    contains:
        ConditionSwitch(
            # backside of the hand
            "not Speed", Transform("Laura_Hand_Under"),
            "Speed == 1", At("Laura_Hand_Under", Laura_Hand_1()),
            "Speed >= 2", At("Laura_Hand_Under", Laura_Hand_2()),
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
            "not Speed", Transform("Laura_Hand_Over"),
            "Speed == 1", At("Laura_Hand_Over", Laura_Hand_1()),
            "Speed >= 2", At("Laura_Hand_Over", Laura_Hand_2()),
            "Speed", Null(),
            ),
    anchor (0.51, -1.3)
    zoom 0.4#0.6


label Laura_HJ_Launch(Line = Trigger):
    if renpy.showing("Laura_HJ_Animation"):
        $ Trigger = "hand"
        return
    if not Player.Male:
        call Laura_Finger_Launch
        return
    call Girl_Hide(LauraX)
    if Line == "L":
        show Laura_Sprite at SpriteLoc(StageRight) zorder 150:
            alpha 1
            ease 1 zoom 1.7 offset (-150,200)#(0,200)
    else:
        show Laura_Sprite at SpriteLoc(StageRight) zorder 150:
            alpha 1
            ease 1 zoom 1.7 offset (-150,200)#(0,200)
        with dissolve

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    else:
        $ Speed = 1
    pause .5
    $ LauraX.ArmPose = 1
    show Laura_Sprite:
        alpha 0
    show Laura_HJ_Animation at SpriteLoc(StageCenter) zorder 150 with fade:
        #xoffset 150
        offset (250,250)#(100,250)
    return

label Laura_HJ_Reset: # The sequence to the Laura animations from handjob to default
    if not renpy.showing("Laura_HJ_Animation"):
        return
    $ Speed = 0
    $ LauraX.ArmPose = 1
    hide Laura_HJ_Animation with dissolve
    call Girl_Hide(LauraX)
    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
        alpha 1 zoom 1 offset (0,0)
    return

# End Laura Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# Core Laura CUN element ///////////////////////////////////////////////////////////////////////////                                     Core Laura CUN element
#Laura CUN Over Sprite Compositing

image Laura_CUN_Animation: #core CUN animation
    LiveComposite(
        (787,913),
        (0,0), ConditionSwitch(                                                                 # back of the hair, which needs to go behind the body
            "Speed == 0",  "Laura_CUN_Anim_Static",
            "Speed == 1",  "Laura_CUN_Anim_Licking1",
            "Speed == 2",  "Laura_CUN_Anim_Licking2",
            "Speed >= 3",  "Laura_CUN_Anim_Licking3",
#            "Speed == 4",  "Laura_CUN_Anim_Licking1",
            "True", "Laura_CUN_Anim_Static",
            ),
        )
    zoom .55
    anchor (.5,.5)

image Laura_CUN_Anim_Static:
    #Animation for licking speed 1
    contains:
        #hair
        "Laura_Sprite_BJ_HairBack"#"BJ_HairBack"
        zoom 1.7
        subpixel True
        offset (0,-50)#(-10,0)
        block:
            ease 2 yoffset -40
            ease 2 yoffset -50
            repeat
    contains:
        #body 2
        "Laura_Sprite"
        zoom 4.5
        pos (690,-10)#(825,-10)
        subpixel True
        offset (0,-50)  #top(0,-10)
        pause 0.05
        block:
            ease 2 yoffset -40
            ease 2 yoffset -50
            repeat
    contains:
        #head
        "Laura_Sprite_BJ_Head"#"BJ_Head"
        zoom 1.7
        subpixel True
        offset (0,-50)#(-10,0)
        block:
            ease 2 yoffset -40
            ease 2 yoffset -50
            repeat
    contains:
        #pussy
        "Zero_Pussy"
        anchor (.5,.5)
        zoom 1.7
        pos (850,1360)#(970,1360) (670,1260)
        offset (0,0)
        pause 0.1
        block:
            ease 2 yoffset 10
            ease 2 yoffset 0
            repeat


image Laura_CUN_Anim_Licking1:
    #Animation for licking speed 1
    contains:
        #hair
        "Laura_Sprite_BJ_HairBack"#"BJ_HairBack"
        zoom 1.7
        subpixel True
        offset (0,0)#490)
        block: #5s total
            ease 2.5 offset (0,50) #bottom
            easeout 1.5 offset (0,10)  #top -35)
            linear .5 offset (0,-30)  #top -35)
            pause .5
            repeat
    contains:
        #body 2
        "Laura_Sprite"
        zoom 4.5
        pos (690,-10)#(840,-50)
        subpixel True
        offset (0,0)#490)
        block:
            ease 2.5 offset (0,50) #bottom (30,90)
            ease 2 offset (0,-40)  #top
            pause .5
            repeat
    contains:
        #head
        "Laura_Sprite_BJ_Head"#"BJ_Head"
        zoom 1.7
        subpixel True
        offset (0,0)#490)
        block: #5s total
            ease 2.5 offset (0,50) #bottom
            easeout 1.5 offset (0,10)  #top -35)
            linear .5 offset (0,-30)  #top -35)
            pause .5
            repeat
    contains:
        #pussy
        "Zero_Pussy"
        subpixel True
        anchor (.5,.5)
        zoom 1.7
        pos (850,1360)#(970,1360) (670,1260)
        offset (0,5)#490)
        block:
            easein 1 yoffset 10 #510 bottom
            pause 1.5
            easeout 1 yoffset 0#490
            linear .3 yoffset -5#490
            easein .2 yoffset -3#490
            easeout 1 yoffset 5 #510 bottom
            repeat
#End Laura Licking 1

image Laura_CUN_Anim_Licking2:
    #Animation for licking speed 2
    contains:
        #hair
        "Laura_Sprite_BJ_HairBack"#"BJ_HairBack"
        zoom 1.7
        subpixel True
        offset (0,0)#490)
        block: #2s total
            ease 1 offset (0,70) #bottom
            easeout .65 offset (0,30)  #top -35)
            linear .25 offset (0,0)  #top -35)
            pause .10
            repeat
    contains:
        #body 2
        "Laura_Sprite"
        zoom 4.5
        pos (690,-10)#(840,-50)
        subpixel True
        offset (0,0)#490)
        block:
            ease .75 offset (0,30) #bottom (30,90)
            ease .95 offset (0,0)  #top
            pause .30
            repeat
    contains:
        #head
        "Laura_Sprite_BJ_Head"#"BJ_Head"
        zoom 1.7
        subpixel True
        offset (0,0)#490)
        block: #2s total
            ease 1 offset (0,70) #bottom
            easeout .65 offset (0,30)  #top -35)
            linear .25 offset (0,0)  #top -35)
            pause .10
            repeat
    contains:
        #pussy
        "Zero_Pussy"
        subpixel True
        anchor (.5,.5)
        zoom 1.7
        pos (850,1360)#(970,1360) (670,1260)
        offset (0,-3)#490)
        block:
            ease .5 yoffset 10 #510 bottom
            pause .5
            easeout .6 yoffset 0#490
            linear .1 yoffset -5#490
            easein .1 yoffset -3#490
            pause .2
            repeat
#End Laura Licking 2

image Laura_CUN_Anim_Licking3:
    #Animation for licking speed 3
    contains:
        #hair
        "Laura_Sprite_BJ_HairBack"#"BJ_HairBack"
        zoom 1.7
        subpixel True
        offset (20,50)#490)
        block: #2s total
            ease .5 offset (20,70) #bottom
            ease .5 offset (20,50)  #top -35)
            repeat
    contains:
        #body 2
        "Laura_Sprite"
        zoom 4.5
        pos (690,-10)#(840,-50)
        subpixel True
        offset (20,50)#490)
        block:
            ease .4 offset (20,60) #bottom (30,90)
            ease .4 offset (20,50)  #top
            pause .2
            repeat
    contains:
        #head
        "Laura_Sprite_BJ_Head"#"BJ_Head"
        zoom 1.7
        subpixel True
        offset (20,50)#490)
        block: #2s total
            ease .5 offset (20,70) #bottom
            ease .5 offset (20,50)  #top -35)
            repeat
    contains:
        #pussy
        "Zero_Pussy"
        subpixel True
        anchor (.5,.5)
        zoom 1.7
        pos (850,1360)#(970,1
#        pos (235,790)#(410,790)
        offset (0,5)#490)
        block:
            ease .25 yoffset 10 #510 bottom
            pause .25
            ease .25 yoffset 5#490
            ease .25 yoffset 6#490
            repeat
#End Laura Licking 3

#CUN Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Laura_CUN_Launch(Line = Trigger):
    # The sequence to launch the Laura CUN animations

    if renpy.showing("Laura_CUN_Animation") and LauraX.Pose != "69":
        return
    elif renpy.showing("Laura_69_CUN") and LauraX.Pose == "69":
        return

    if Player.Male == 1:
        call Laura_BJ_Launch
        return

    call Girl_Hide(LauraX)
    if Line == "L" or Line == "cum":
        show Laura_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1
            ease 1 zoom 2.5 offset (70,240) #(-90,140) offset (150,80)
        with dissolve
    else:
        show Laura_Sprite at SpriteLoc(StageCenter) zorder 150:
            alpha 1 zoom 2.5 offset (70,240) #(-90,140)
        with dissolve

    if Taboo and Line == "L":
            # Laura gets started. . .
            if len(Present) >= 2:
                if Present[0] != LauraX:
                        "[LauraX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
                elif Present[1] != LauraX:
                        "[LauraX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
            else:
                        "[LauraX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
    $ Speed = 1
    if Line == "L":
            if not LauraX.Blow:
                "[LauraX.Name] нерешительно стягивает с вас штаны и касается своим ртом вашей киски."
            else:
                "[LauraX.Name] наклоняется и начинает лизать вашу киску."

    if Line != "cum":
        $ Trigger = "cun"

    show Laura_Sprite:
        alpha 0
    if LauraX.Pose == "69":
            show Laura_69_CUN zorder 150
    else:
            show Laura_CUN_Animation zorder 150:
                pos (450,510) #(450,550)
    return

label Laura_CUN_Reset: # The sequence to the Laura animations from CUN to default
    if not renpy.showing("Laura_CUN_Animation") and not renpy.showing("Laura_69_CUN"):
        return
#    hide Laura_CUN_Animation
    call Girl_Hide(LauraX)
    $ Speed = 0

    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder 150:
        zoom 2 offset (70,140) alpha 1
        pause .5
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
        alpha 1 zoom 1 offset (0,0)
    $ LauraX.FaceChange("sexy")
    return

#End Laura Cunnilingus Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

image Laura_Finger_Animation:
    # Core Animation for Fingering Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
        ConditionSwitch(                                                # backside of the hand
            "Speed == 1", "Laura_Finger_1",
            "Speed >= 2", "Laura_Finger_2",
            "True", "Laura_Finger_0",
            ),
    anchor (0.5,0.5)#anchor (0.51, -1.3)
    offset (400,945)#(400,965)
    zoom 0.8
    # end Core Animation for Fingering Zero's pussy < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Finger_0:
    # Animation for Fingering Zero's pussy, static < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Laura_Sprite"
            pos (320,-550)
            zoom 2.15
    contains:
            ConditionSwitch(
                "Player.Wet", "LauraSprite/[LauraX.skin_image.skin_path]Laura_Fingering_Wet.png",
                "True", "LauraSprite/[LauraX.skin_image.skin_path]Laura_Fingering_Under.png",
                )
            anchor (0.5,0.6)
            pos (-20,40)

#            "Laura_Finger_Under"
    contains:
            "Zero_Pussy"
    contains:
            "LauraSprite/[LauraX.skin_image.skin_path]Laura_Fingering_Over.png"
            anchor (0.5,0.6)
            pos (-20,40)
#            "Laura_Finger_Over"
    # end Animation for Fingering Zero's pussy, static < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Finger_1:
    # Animation for Fingering Zero's pussy, slow < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Laura_Sprite"
            pos (320,-550)
            zoom 2.15
            block:
                ease 0.5 ypos -540 #rotate 3   100
                pause 0.25
                ease 1.0 ypos -550 #rotate -3  40
                repeat
    contains:
            ConditionSwitch(
                "Player.Wet", "LauraSprite/[LauraX.skin_image.skin_path]Laura_Fingering_Wet.png",
                "True", "LauraSprite/[LauraX.skin_image.skin_path]Laura_Fingering_Under.png",
                )
            subpixel True
        #    xpos 10
            anchor (0.5,0.6)
            transform_anchor True
            pos (-15,40)
            rotate -15
            block:
                ease .5 pos (-20,85) rotate 0 #(-30,50)   Bottom
                pause 0.25
                ease 1.0 pos (-15,40) rotate -15 #((20,-60) Top                 pause 0.1
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
            "LauraSprite/[LauraX.skin_image.skin_path]Laura_Fingering_Over.png"
#            "Laura_Finger_Over"
            subpixel True
        #    xpos 10
            anchor (0.5,0.6)
            transform_anchor True
            pos (-15,40)
            rotate -15
            block:
                ease .5 pos (-20,85) rotate 0 #(-30,50)   Bottom
                pause 0.25
                ease 1.0 pos (-15,40) rotate -15 #((20,-60) Top                 pause 0.1
                repeat
    # end Animation for Fingering Zero's pussy, slow < < < < < < < < < < < < < < < < < < < < < < < <

image Laura_Finger_2:
    # Animation for Fingering Zero's pussy, fast < < < < < < < < < < < < < < < < < < < < < < < <
    contains:
            "Laura_Sprite"
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
                "Player.Wet", "LauraSprite/[LauraX.skin_image.skin_path]Laura_Fingering_Wet.png",
                "True", "LauraSprite/[LauraX.skin_image.skin_path]Laura_Fingering_Under.png",
                )
            subpixel True
            anchor (0.5,0.6)
            transform_anchor True
            rotate 0
            pos (-20,40)
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
            "LauraSprite/[LauraX.skin_image.skin_path]Laura_Fingering_Over.png"
#            "Laura_Finger_Over"
            anchor (0.5,0.6)
            subpixel True
            transform_anchor True
            rotate 0
            pos (-20,40)
            block:
                ease 0.15 ypos 115 #rotate 3
                pause 0.1
                ease 0.45 ypos 40 #rotate -3 -50
                pause 0.1
                repeat
    # end Animation for Fingering Zero's pussy, fast < < < < < < < < < < < < < < < < < < < < < < < <

label Laura_Finger_Launch(Line = Trigger):
    if renpy.showing("Laura_Finger_Animation"):
        $ Trigger = "finger"
        return
    if Player.Male == 1:
        call Laura_HJ_Launch
        return

    call Girl_Hide(LauraX)
    $ LauraX.Arms = 0
    $ LauraX.ArmPose = 2
    if not renpy.showing("Laura_Sprite"):
        show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder 150:
            alpha 1 zoom 1.7 xpos 800 yoffset 200 #offset (-50,200)
        with dissolve
    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder 150:
        alpha 1
        ease 1 zoom 1.7 xpos 800 yoffset 200 #offset (-50,200)

    if Taboo and Line == "L":
        # Laura gets started. . .
        if len(Present) >= 2:
            if Present[0] != LauraX:
                    "[LauraX.Name] оглядывается на [Present[0].Name_vin], чтобы посмотреть, наблюдает ли она."
            elif Present[1] != LauraX:
                    "[LauraX.Name] оглядывается на [Present[1].Name_vin], чтобы посмотреть, наблюдает ли она."
        else:
                    "[LauraX.Name] оглядывается по сторонам, чтобы посмотреть, наблюдает ли кто-нибудь за ней."
        if not LauraX.Hand and LauraX.Arms:
            "Когда вы стягиваете свои штаны, [LauraX.Name] снимает перчатки и нерешительно тянется к вашей киске. Затем она начинает грубо ласкать ее."
        else:
            "Затем она наклоняется и хватает ваш член."
    elif Line == "L":
        if not LauraX.Hand and LauraX.Arms:
            "Когда вы стягиваете свои штаны, [LauraX.Name] снимает перчатки и нерешительно тянется к вашей киске. Затем она начинает грубо ласкать ее."
        else:
            "[LauraX.Name] наклоняется и кладет руку вам на киску."
    else:
            "[LauraX.Name] наклоняется и кладет руку вам на киску."

    show Laura_Sprite:
        alpha 0
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "finger"
    show Laura_Finger_Animation at SpriteLoc(LauraX.SpriteLoc) zorder 150 with fade
    return

label Laura_Finger_Reset: # The sequence to the Laura animations from handjob to default
    if not renpy.showing("Laura_Finger_Animation"):
        return
    $ Speed = 0
    hide Laura_Finger_Animation
    with dissolve
    call Girl_Hide(LauraX)
#    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
#        alpha 0
#        zoom 1.7  xpos 800 yoffset 200
    show Laura_Sprite zorder 150:
        alpha 1
        ease 1 zoom 1.5 yoffset 50
        pause .5
        ease .5 zoom 1 xpos LauraX.SpriteLoc yoffset 0
    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
        alpha 1 zoom 1 xpos LauraX.SpriteLoc yoffset 0

    $ LauraX.ArmPose = 1
    return

# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

# Start Laura 69 Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

image Laura_69_Animation:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
                #Shows different upper body motion depending on events
#                "True", "Laura_69_Anim1",
                "Speed == 2", "Laura_69_Anim2",
                "Speed == 3", "Laura_69_Anim3",
                "Speed == 4", "Laura_69_Anim4",
                "Speed == 5", "Laura_69_Anim5",
                "Speed == 6", "Laura_69_Anim6",
                "Speed", "Laura_69_Anim1",
                "True", "Laura_69_Static",
                ),
        )
    align (0.6,0.0)
    pos (475,-700)#(475,-800)
    zoom 1.6#1.8

#Start Animations for Laura's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Laura 69 Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Laura_69_Body:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Laura_SexSprite
        (1120,840),

        (0,0), ConditionSwitch(
            #bra layer if up
            "not LauraX.Uptop", Null(),
            #if top's up
            "LauraX.Chest == 'white tank'", Recolor("Laura", "Chest", "images/LauraSex/Laura_69_Chest_White.png"),
            "LauraX.Chest == 'wolvie top'", Recolor("Laura", "Chest", "images/LauraSex/Laura_69_Chest_Wolvie.png"),
            "LauraX.Chest == 'leather bra'", Recolor("Laura", "Chest", "images/LauraSex/Laura_69_Chest_Tank.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #body
#            "LauraX.Arms", "images/LauraSex/Laura_69_BodyG.png",
            "True", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_69_Body.png",
            ),

        (0,0), ConditionSwitch(
            #gloves layer
            "LauraX.Arms == 'gloves'", Recolor("Laura", "Arms", "images/LauraSex/Laura_69_Gloves.png"),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "LauraX.Water", "images/LauraSex/Laura_69_Water_Body.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #bra layer if up
            "LauraX.Uptop", ConditionSwitch(
                    "LauraX.Chest == 'bikini top'", Recolor("Laura", "Chest", "images/LauraSex/Laura_69_Chest_Bikini_Up.png"),
                    "LauraX.Chest == 'corset'", Recolor("Laura", "Chest", "images/LauraSex/Laura_69_Chest_Corset_Up.png"),
                    "LauraX.Chest == 'lace corset'", Recolor("Laura", "Chest", "images/LauraSex/Laura_69_Chest_Corset_Lace_Up.png"),
                    "True", Null(),
                    ),
            #if top's up
            "LauraX.Chest == 'leather bra'", Recolor("Laura", "Chest", "images/LauraSex/Laura_69_Chest_Tank.png"),
            "LauraX.Chest == 'bikini top'", Recolor("Laura", "Chest", "images/LauraSex/Laura_69_Chest_Bikini.png"),
            "LauraX.Chest == 'white tank'", Recolor("Laura", "Chest", "images/LauraSex/Laura_69_Chest_White.png"),
            "LauraX.Chest == 'wolvie top'", Recolor("Laura", "Chest", "images/LauraSex/Laura_69_Chest_Wolvie.png"),
            "LauraX.Chest == 'corset'", Recolor("Laura", "Chest", "images/LauraSex/Laura_69_Chest_Corset.png"),
            "LauraX.Chest == 'lace corset'", Recolor("Laura", "Chest", "images/LauraSex/Laura_69_Chest_Corset_Lace.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #shirt layer
            "LauraX.Over == 'jacket'", Recolor("Laura", "Over", "images/LauraSex/Laura_69_Over_Jacket_Both.png"),
            "LauraX.Over == 'towel' and not LauraX.Uptop", Recolor("Laura", "Over", "images/LauraSex/Laura_69_Over_Towel.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #piercings
            "not LauraX.Pierce", Null(),
            "LauraX.Pierce == 'ring'", ConditionSwitch(
                    # ring pierce
                    "LauraX.Uptop", "images/LauraSex/Laura_69_Pierce_Tits_R.png",

                    "LauraX.Over == 'towel'", "images/LauraSex/Laura_69_Pierce_Tits_R_Towel.png",

                    "LauraX.Chest == 'bikini top'", "images/LauraSex/Laura_69_Pierce_Tits_R_Black.png",
                    "LauraX.Chest == 'leather bra'", "images/LauraSex/Laura_69_Pierce_Tits_R_Black.png",
                    "LauraX.Chest == 'white tank'", "images/LauraSex/Laura_69_Pierce_Tits_R_White.png",
                    "LauraX.Chest == 'wolvie top'", "images/LauraSex/Laura_69_Pierce_Tits_R_Wolvie.png",
                    "LauraX.Chest == 'corset'", "images/LauraSex/Laura_69_Pierce_Tits_R_Red.png",
                    "LauraX.Chest == 'lace corset'", "images/LauraSex/Laura_69_Pierce_Tits_R_Red.png",

                    "True", "images/LauraSex/Laura_69_Pierce_Tits_R.png",
                    ),
            "LauraX.Uptop", "images/LauraSex/Laura_69_Pierce_Tits_B.png",

            "LauraX.Over == 'towel'", "images/LauraSex/Laura_69_Pierce_Tits_B_Towel.png",

            "LauraX.Chest == 'bikini top'", "images/LauraSex/Laura_69_Pierce_Tits_B_Black.png",
            "LauraX.Chest == 'leather bra'", "images/LauraSex/Laura_69_Pierce_Tits_B_Black.png",
            "LauraX.Chest == 'white tank'", "images/LauraSex/Laura_69_Pierce_Tits_B_White.png",
            "LauraX.Chest == 'wolvie top'", "images/LauraSex/Laura_69_Pierce_Tits_B_Wolvie.png",
            "LauraX.Chest == 'corset'", "images/LauraSex/Laura_69_Pierce_Tits_B_Red.png",
            "LauraX.Chest == 'lace corset'", "images/LauraSex/Laura_69_Pierce_Tits_B_Red.png",

            "True", "images/LauraSex/Laura_69_Pierce_Tits_B.png",
            ),
#        (0,0), ConditionSwitch(
#            #piercings
#            "not LauraX.Pierce", Null(),
#            "LauraX.Uptop", Null(),
#            "LauraX.Pierce == 'ring'", ConditionSwitch(
#                    # ring pierce
#                    "LauraX.Over == 'mesh top'", "images/LauraSex/Laura_69_Pierce_Tits_R_Mesh.png",
#                    "LauraX.Over == 'nighty'", "images/LauraSex/Laura_69_Pierce_Tits_R_Nighty.png",
#                    "True", Null(),
#                    ),
#            "LauraX.Over == 'mesh top'", "images/LauraSex/Laura_69_Pierce_Tits_B_Mesh.png",
#            "LauraX.Over == 'nighty'", "images/LauraSex/Laura_69_Pierce_Tits_B_Nighty.png",
#            "True", Null(),
#            ),

        (0,0),ConditionSwitch(
            #Outside Spunk
            "'tits' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_69_Spunk_Tits.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'belly' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_69_Spunk_Belly.png",
            "True", Null(),
            ),
#        (0,0), "images/LauraSex/Laura_Sex_HeadRef.png",
        )
    zoom .9#.8
    offset (75,30)#(70,80)
#    yoffset -163
# End Laura 69 Pose Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Laura 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Laura_69_Head:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Laura_SexSprite
        (1120,840),
        (0,0), ConditionSwitch(
            #tongue
            "renpy.showing('Laura_69_CUN') and Speed != 3", "images/LauraSex/Laura_69_Tongue.png",
            "Speed == 1", "images/LauraSex/Laura_69_Tongue.png",
            "True", Null(),
            ),
        (0,0), "images/LauraSex/[LauraX.skin_image.skin_path]Laura_69_Head.png",
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'mouth' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_69_Spunk_Mouth.png",
            "('mouth' in LauraX.Spunk or 'chin' in LauraX.Spunk) and not Player.Male", "images/LauraSex/Laura_69_Wet_Face.png",
            "True", Null(),
            ),

        (0,0),ConditionSwitch(
            #Outside Spunk
            "'chin' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_69_Spunk_Chin.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Hair over
#            "Speed == 1 and Player.Male", Null(),
#            "Speed == 4 and Player.Male", Null(),
#            "Speed == 6 and Player.Male", Null(),
#            "LauraX.Water or LauraX.Hair == 'wet'", "images/LauraSex/Laura_69_Hair_Wet.png",
#            "not Player.Male and ('hair' in LauraX.Spunk or 'facial' in LauraX.Spunk)","images/LauraSex/Laura_69_Hair_Pony.png",

##            "LauraX.Hair == 'long'", "images/LauraSex/Laura_69_Hair_Long_Over.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #Hair over
#            "LauraX.Hair == 'evo' and not LauraX.Water","images/LauraSex/Laura_69_Hair_Pony.png",
            "Speed == 1 and Player.Male", Null(),
            "Speed == 4 and Player.Male", Null(),
            "Speed == 6 and Player.Male", Null(),
#            "LauraX.Water or LauraX.Hair == 'wet'", "images/LauraSex/Laura_69_Hair_Wet.png",
#            "not Player.Male and ('hair' in LauraX.Spunk or 'facial' in LauraX.Spunk)","images/LauraSex/Laura_69_Hair_Wet.png",

            "True", Recolor("Laura", "Hair", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_69_Hair.png"),
#            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #neck over
            "(Speed == 0 or Speed == 2 or Speed == 3 or Speed == 5) and Player.Male", Recolor("Laura", "Hair", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_69_Hair.png"),
            "not Player.Male", Recolor("Laura", "Hair", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_69_Hair.png"),  #"images/LauraSex/Laura_69_Neck.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #neck
            "(Speed == 1 or Speed == 4 or Speed == 6) and Player.Male", Null(),
            "not Player.Male", Null(),
            "LauraX.Neck == 'leash choker'", Recolor("Laura", "Neck", "images/LauraSex/Laura_69_Neck_Leash.png"),
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #collar
#            "LauraX.Neck", "images/LauraSex/Laura_69_Collar.png",
#            "True", Null(),
#            ),
        )
    zoom .8
    offset (145,140)
#    offset (0,0)#(175,135)#(175,175)
#    yoffset -163
# End Laura 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Laura 69 Pose Hair Over / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Laura_69_HairOver:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Laura_SexSprite
        (1120,840),
#        (0,0), "images/LauraSex/Laura_69_Neck.png",
        (0,0), ConditionSwitch(
            #Hair over
#            "LauraX.Water or LauraX.Hair == 'wet'", "images/LauraSex/Laura_69_Hair_Wet.png",
#            "not Player.Male and ('hair' in LauraX.Spunk or 'facial' in LauraX.Spunk)","images/LauraSex/Laura_69_Hair_Wet.png",

            "True", Recolor("Laura", "Hair", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_69_Hair.png"),
#            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #Hair over
##            "renpy.showing('Laura_TJ_Animation')", Null(),
##            "LauraX.Hair == 'blonde'", "images/LauraSex/Laura_69_Hair_Blonde_Lick.png",
##            "LauraX.Hair == 'long' or LauraX.Hair == 'wetlong'", "images/LauraSex/Laura_69_Hair_Long_Lick.png",
#            "True", Recolor("Laura", "Hair", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_69_Hair_Over.png"),
#            ),
        (0,0), ConditionSwitch(
            #neck
            "LauraX.Neck == 'leash choker'", Recolor("Laura", "Neck", "images/LauraSex/Laura_69_Neck_Leash.png"),
            "True", Null(),
            ),
        )
    zoom .8
    offset (145,140)
#    offset (0,0)#(175,135)#(180,100)
#    yoffset -163
# End Laura 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Laura 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Laura_69_HairBack:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Laura_SexSprite
        (1120,840),
#        (0,0), "images/LauraSex/[LauraX.skin_image.skin_path]Laura_69_Head.png",
        (0,0), ConditionSwitch(
            #Hair over
#            "Speed == 1 and Player.Male", Null(),
#            "Speed == 4 and Player.Male", Null(),
#            "Speed == 6 and Player.Male", Null(),
#            "LauraX.Water or LauraX.Hair == 'wet'", "images/LauraSex/Laura_69_Hair_Wet_Under.png",
#            "not Player.Male and ('hair' in LauraX.Spunk or 'facial' in LauraX.Spunk)","images/LauraSex/Laura_69_Hair_Wet_Under.png",

            "True", Recolor("Laura", "Hair", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_69_Hair_Under.png"),
#            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hair over
#            "renpy.showing('Laura_TJ_Animation')", Null(),
#            "LauraX.Hair == 'blonde'", "images/LauraSex/Laura_69_Hair_Blonde_Under.png",
#            "LauraX.Hair == 'long' or LauraX.Hair == 'wetlong'", "images/LauraSex/Laura_69_Hair_Long_Under.png",
#            "LauraX.Hair == 'wet' or LauraX.Hair == 'wetlong' or LauraX.Water", "images/LauraSex/Laura_69_Hair_Long.png",
#            "not Player.Male and 'facial' in LauraX.Spunk","images/LauraSex/Laura_Sprite_Hair_Wet.png",
            "True", Null(),#Recolor("Laura", "Hair", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_69_Hair_Under.png"),
            ),
        )
    zoom .8
    offset (145,140)#(175,135)#(175,175)
#    yoffset -163
# End Laura 69 Pose Head / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#image Laura_Sex_Legs = LiveComposite(
image Laura_69_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Laura_SexSprite
        (1120,840),
        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            "LauraX.Legs == 'skirt' or LauraX.Legs == 'other skirt'", Recolor("Laura", "Legs", "images/LauraSex/Laura_69_Legs_Skirt_Under.png"),
            "LauraX.Over == 'towel'", Recolor("Laura", "Legs", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_69_Legs_Towel.png"),
            "LauraX.Hose == 'towel'", Recolor("Laura", "Legs", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_69_Legs_Towel.png"),
            "LauraX.Hose == 'stockings and garterbelt'", Recolor("Laura", "Hose", "images/LauraSex/Laura_69_Hose_Garter_Under.png"),
            "LauraX.Hose == 'garterbelt'", Recolor("Laura", "Hose", "images/LauraSex/Laura_69_Hose_Garter_Under.png"),
            "True", Null(),
            ),
        (0,0), "images/LauraSex/[LauraX.skin_image.skin_path]Laura_69_Legs.png",                                                         #Legs Base
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "LauraX.Water", "images/LauraSex/Laura_69_Water_Legs.png",
            "True", Null(),
            ),

        (0,0), "Laura_69_Anus",                                                                          #Anus Composite

        (0,0), "Laura_69_Pussy",                                                                         #Pussy Composite


        (0,0), ConditionSwitch(
            #hose layer
            "LauraX.Hose == 'stockings and garterbelt'", Recolor("Laura", "Hose", "images/LauraSex/Laura_69_Hose_StockingsGarter.png"),
            "LauraX.Hose == 'garterbelt'", Recolor("Laura", "Hose", "images/LauraSex/Laura_69_Hose_Garter.png"),
            "LauraX.Hose == 'stockings'", Recolor("Laura", "Hose", "images/LauraSex/Laura_69_Hose_Stockings.png"),
            "LauraX.Hose == 'black stockings'", Recolor("Laura", "Hose", "images/LauraSex/Laura_69_Hose_Socks.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(                                                                                 #Panties if up
            "LauraX.PantiesDown", Null(),
            "LauraX.Panties == 'wolvie panties' and LauraX.Wet", Recolor("Laura", "Panties", "images/LauraSex/Laura_69_Panties_Wolvie_Wet.png"),
            "LauraX.Panties == 'wolvie panties'", Recolor("Laura", "Panties", "images/LauraSex/Laura_69_Panties_Wolvie.png"),
            "LauraX.Panties == 'lace panties'", Recolor("Laura", "Panties", "images/LauraSex/Laura_69_Panties_Lace.png"),
            "LauraX.Panties == 'bikini bottoms'", Recolor("Laura", "Panties", "images/LauraSex/Laura_69_Panties_Bikini.png"),
            "LauraX.Panties", Recolor("Laura", "Panties", "images/LauraSex/Laura_69_Panties_Leather.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #hose layer
            "LauraX.Panties and LauraX.PantiesDown", Null(),
            "LauraX.Hose == 'pantyhose'", Recolor("Laura", "Hose", "images/LauraSex/Laura_69_Hose_Pantyhose.png"),
            "LauraX.Hose == 'ripped pantyhose'", Recolor("Laura", "Hose", "images/LauraSex/Laura_69_Hose_Pantyhose_Holed.png"),
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(                                                                                 #Over Layer
#            "LauraX.Over == 'towel' and not LauraX.Uptop", Recolor("Laura", "Legs", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_69_Legs_Towel.png"),
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            "LauraX.Legs == 'skirt' or LauraX.Legs == 'other skirt'", Recolor("Laura", "Legs", "images/LauraSex/Laura_69_Legs_Skirt.png"),
            "LauraX.Upskirt", Null(),
            "LauraX.Legs == 'mesh pants'", Recolor("Laura", "Legs", "images/LauraSex/Laura_69_Legs_MeshPants.png"),
            "LauraX.Legs == 'leather pants'", Recolor("Laura", "Legs", "images/LauraSex/Laura_69_Legs_Pants.png"),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Piercings over pants and pantyhose
            "not LauraX.Pierce", Null(),
            "LauraX.Pierce == 'ring'",ConditionSwitch(
                    #If she has panties down. . .
                    "LauraX.Legs == 'leather pants' and not LauraX.Upskirt", "images/LauraSex/Laura_69_Pierce_Pussy_R_Black.png",
                    "LauraX.Legs == 'mesh pants' and not LauraX.Upskirt and LauraX.Panties", "images/LauraSex/Laura_69_Pierce_Pussy_R_Black.png",
                    "LauraX.Legs == 'mesh pants' and not LauraX.Upskirt", "images/LauraSex/Laura_69_Pierce_Pussy_R_Mesh.png",

                    "LauraX.Panties and LauraX.PantiesDown", "images/LauraSex/Laura_69_Pierce_Pussy_R.png",

                    "LauraX.Hose == 'pantyhose'", "images/LauraSex/Laura_69_Pierce_Pussy_R_Black.png",

                    "LauraX.Panties == 'lace panties'", "images/LauraSex/Laura_69_Pierce_Pussy_R_Red.png",
                    "LauraX.Panties == 'wolvie panties'", "images/LauraSex/Laura_69_Pierce_Pussy_R_Wolvie.png",
                    "LauraX.Panties", "images/LauraSex/Laura_69_Pierce_Pussy_R_Black.png",

                    "True", "images/LauraSex/Laura_69_Pierce_Pussy_R.png",
                    ),
            #else, it's barbell
            "LauraX.Legs == 'leather pants' and not LauraX.Upskirt", "images/LauraSex/Laura_69_Pierce_Pussy_B_Black.png",
            "LauraX.Legs == 'mesh pants' and not LauraX.Upskirt and LauraX.Panties", "images/LauraSex/Laura_69_Pierce_Pussy_B_Black.png",
            "LauraX.Legs == 'mesh pants' and not LauraX.Upskirt", "images/LauraSex/Laura_69_Pierce_Pussy_B_Mesh.png",

            "LauraX.Panties and LauraX.PantiesDown", "images/LauraSex/Laura_69_Pierce_Pussy_B.png",

            "LauraX.Hose == 'pantyhose'", "images/LauraSex/Laura_69_Pierce_Pussy_B_Black.png",

            "LauraX.Panties == 'lace panties'", "images/LauraSex/Laura_69_Pierce_Pussy_B_Red.png",
            "LauraX.Panties == 'wolvie panties'", "images/LauraSex/Laura_69_Pierce_Pussy_B_Wolvie.png",
            "LauraX.Panties", "images/LauraSex/Laura_69_Pierce_Pussy_B_Black.png",

            "True", "images/LauraSex/Laura_69_Pierce_Pussy_B.png",
            ),

#        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
#            "'belly' in LauraX.Spunk and Player.Male", "images/LauraSex/Laura_Sex_Spunk_Pelvis.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer
#            "not Player.Sprite or Player.Cock != 'out'", Null(),
#            "Speed >= 2", "Laura_Hotdog_Zero_Anim2",
#            "Speed", "Laura_Hotdog_Zero_Anim1",
#            "True", "Laura_Hotdog_Zero_Anim0",
#            ),

        (0,0), ConditionSwitch(
            #pussy licking animation
#            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy' or Trigger2 == 'lick pussy'", "Laura_69_Lick_Pussy",
            "Trigger == 'lick ass' or Trigger2 == 'lick ass'", "Laura_69_Lick_Ass",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy fondling animation
            "LauraX.Offhand == 'fondle pussy' and LauraX.Lust > 60 and not (Player.Sprite)",  At("LauraFingerHand", GirlFingerPussyX()), #"Betsy_Sex_Mast2",
            "LauraX.Offhand == 'fondle pussy'", At("LauraMastHand", GirlGropePussyX()), #"Betsy_Sex_Mast",
#            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Laura_Sex_Fondle_Pussy",
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #pussy licking animation
##            "Player.Sprite", Null(),
#            "Trigger == 'lick pussy'", "Laura_Sex_Lick_Pussy",
#            "Trigger == 'lick ass'", "Laura_Sex_Lick_Ass",
#            "LauraX.Offhand == 'fondle pussy' and LauraX.Lust > 60", At("LauraFingerHand", GirlFingerPussyX()),
#            "LauraX.Offhand == 'fondle pussy'", At("LauraMastHand", GirlGropePussyX()),
#            "True", Null()
#            ),
#        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer
#            "not Player.Sprite or Player.Cock != 'foot'", Null(),
#            "Speed >= 2", "Laura_Footcock_Zero_Anim2",
#            "Speed", "Laura_Footcock_Zero_Anim1",
#            "True", "Laura_Footcock_Static",
#            ),
#        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer
#            "not Player.Sprite or Player.Cock != 'foot'", Null(),
#            "Speed >= 2", At("Laura_Footcock", Laura_Footcock_Zero_Anim2A()),
#            "Speed", At("Laura_Footcock", Laura_Footcock_Zero_Anim1A()),
#            "True", At("Laura_Footcock", Laura_Footcock_StaticA()),
#            ),
#        (0,0), ConditionSwitch(                                                                                 #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
#            "renpy.showing('Anal_Plug_In_Sex') or renpy.showing('Anal_Plug_Out_Sex')", AlphaMask("Laura_69_Feet", "images/LauraSex/Laura_69_FeetMask.png"),
#            "not Speed", "Laura_69_Feet",
#            "Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Laura_69_Feet", "images/LauraSex/Laura_69_FeetMask.png"),
#            "True", "Laura_69_Feet",
#            ),
#        (0,0), ConditionSwitch(                                                                                 #Legs Layer
#            "LauraX.Upskirt", Null(),
#            "LauraX.Legs == 'dress'", "images/LauraSex/Laura_69_Feet_Dress.png",
#            "True", Null(),
#            ),
        )
    offset (10,-80)#
# End Laura 69 Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#image Laura_69_Feet = LiveComposite(
#        #the lower legs used in the sex pose, referenced by Laura_Sex_Legs
#        (1120,840),
##        (0,0), "images/LauraSex/Laura_Sex_Feet.png",                                                         #Legs Base
##        (0,0), ConditionSwitch(                                                                                 #Wet look
##            "LauraX.Water", "images/LauraSex/Laura_Sex_Water_Feet.png",
##            "True", Null(),
##            ),

#        (0,0), ConditionSwitch(
#            #hose layer
#            "LauraX.Legs and not LauraX.Upskirt and LauraX.Legs != 'blue skirt' and LauraX.Legs != 'shorts'",ConditionSwitch(
#                    #If she has pants on, I need alternate kneesocks to not clip through knees
#                    "LauraX.Hose == 'stockings and garterbelt'", "images/LauraSex/Laura_69_Feet_Stockings.png",
#                    "LauraX.Hose == 'stockings'", "images/LauraSex/Laura_69_Feet_Stockings.png",
#                    "LauraX.Hose == 'knee stockings'", "images/LauraSex/Laura_69_Feet_Kneesocks.png",
#                    "LauraX.Panties and LauraX.PantiesDown", "images/LauraSex/Laura_69_Feet.png",
#                    "LauraX.Hose == 'pantyhose'", "images/LauraSex/Laura_69_Feet_Stockings.png",
#                    "LauraX.Hose == 'ripped pantyhose'", "images/LauraSex/Laura_69_Feet_Stockings_Holed.png",
#                    "True", "images/LauraSex/Laura_69_Feet.png",
#                    ),
##            "LauraX.Legs and (not LauraX.Upskirt and LauraX.Legs != 'blue skirt' and LauraX.Legs != 'shorts') and LauraX.Hose == 'stockings and garterbelt'", "images/LauraSex/Laura_Sex_Hose_Stockings_FeetP.png",
##            "LauraX.Legs and (not LauraX.Upskirt and LauraX.Legs != 'blue skirt' and LauraX.Legs != 'blue skirt') and LauraX.Hose == 'stockings'", "images/LauraSex/Laura_Sex_Hose_Stockings_FeetP.png",
##            "LauraX.Legs and (not LauraX.Upskirt and LauraX.Legs != 'blue skirt' and LauraX.Legs != 'blue skirt') and LauraX.Hose == 'knee stockings'", "images/LauraSex/Laura_Sex_Hose_Stockings_FeetP.png",
#            "LauraX.Hose == 'stockings' or LauraX.Hose == 'stockings and garterbelt'", "images/LauraSex/Laura_69_Feet_Stockings.png",
#            "LauraX.Hose == 'knee stockings'", "images/LauraSex/Laura_69_Feet_Kneesocks.png",
#            "LauraX.Panties and LauraX.PantiesDown", Null(),
#            "LauraX.Hose == 'pantyhose'", "images/LauraSex/Laura_69_Feet_Stockings.png",
##            "LauraX.Legs and (not LauraX.Upskirt and LauraX.Legs != 'blue skirt' and LauraX.Legs != 'blue skirt') and LauraX.Hose == 'ripped pantyhose'", "images/LauraSex/Laura_Sex_Hose_RippedPantyhose_FeetP.png",
#            "LauraX.Hose == 'ripped pantyhose'", "images/LauraSex/Laura_69_Feet_Stockings_Holed.png",
#            "True", "images/LauraSex/Laura_69_Feet.png",
#            ),

#        (0,0), ConditionSwitch(                                                                                 #Legs Layer
#            "LauraX.Upskirt", Null(),
#            "LauraX.Legs == 'dress'", "images/LauraSex/Laura_69_Feet_Dress.png",
#            "LauraX.Legs == 'capris'", "images/LauraSex/Laura_69_Feet_Blue.png",
#            "LauraX.Legs == 'black jeans'", "images/LauraSex/Laura_69_Feet_Black.png",
#            "LauraX.Legs == 'yoga pants'", "images/LauraSex/Laura_69_Feet_Yoga.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #spunk
#            "'feet' in LauraX.Spunk", "images/LauraSex/Laura_Sex_Spunk_Feet.png",
#            "True", Null(),
#            ),
#        )


# Start Laura 69 Pose Pussy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Laura_69_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).

    contains:
            # The background plate of her pussy
            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/LauraSex/Laura_Sex_Pussy_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed", "Laura_Sex_Heading_Pussy",
#                "Player.Sprite and Speed and (Player.Cock == 'in' or Player.Cock == 'out')", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pussy_Open.png",
                "Trigger == 'lick pussy'", "images/LauraSex/Laura_69_Pussy_Open.png",
                "LauraX.Offhand == 'fondle pussy' and LauraX.Lust > 60", "images/LauraSex/Laura_69_Pussy_Open.png",
                "True", "images/LauraSex/Laura_69_Pussy_Closed.png",
                )
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "not LauraX.Wet", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/JubesSex/Jubes_Sex_WetPussy_F.png",
                "True", "images/BetsySex/Betsy_69_Water_Pussy.png",
                )
            offset (-3,-120)
    contains:
            # pubes
            ConditionSwitch(
                "not LauraX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/LauraSex/Laura_Sex_Pubes_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 1", "images/LauraSex/Laura_Sex_Pubes_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in'", Recolor("Laura", "Pubes", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pubes_Open.png"),
#                "Player.Sprite and Player.Cock == 'out'", Recolor("Laura", "Pubes", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pubes_Open.png"),
#                "Trigger == 'lick pussy'", "images/LauraSex/Laura_69_Pubes_Open.png",
#                "LauraX.Offhand == 'fondle pussy' and LauraX.Lust > 60", "images/LauraSex/Laura_69_Pubes_Open.png",
                "True", Recolor("Laura", "Pubes", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_69_Pubes.png"),
                )
    contains:
            #Wet
            ConditionSwitch(
                "not LauraX.Wet", Null(),
                "(LauraX.Legs == 'yoga pants' or LauraX.Legs == 'shorts') and not LauraX.Upskirt", Null(),
                "LauraX.Panties and not LauraX.PantiesDown", Null(),
#                "True", "Spunk_Drip_69",
                "True", AlphaMask("Wet_Drip_69","images/BetsySex/Betsy_69_Mask_Pussy.png"),
                )
            offset (10,-150)#(10,0)
    contains:
            #Spunk
            ConditionSwitch(
                "'in' not in LauraX.Spunk or not Player.Male", Null(),
                "(LauraX.Legs == 'yoga pants' or LauraX.Legs == 'shorts') and not LauraX.Upskirt", Null(),
                "LauraX.Panties and not LauraX.PantiesDown", Null(),
#                "True", "Spunk_Drip_69",
                "True", AlphaMask("Spunk_Drip_69","images/BetsySex/Betsy_69_Mask_Pussy.png"),
                )
            offset (10,-150)

    contains:
            ConditionSwitch(
                #Outside Spunk
#                "'in' in LauraX.Spunk and Player.Sprite and Player.Cock == 'in' and Speed and Player.Male", "images/JubesSex/Jubes_Sex_Spunk_PussyF.png",
                "'in' in LauraX.Spunk and Player.Male", "images/BetsySex/Betsy_69_Spunk_Pussy.png",
                "True", Null(),
                )
            offset (0,-125)
#            offset (0,-15)
#    contains:
#            #Spunk under penis
#            ConditionSwitch(
#                "'in' in LauraX.Spunk", "images/LauraSex/Laura_Sex_Spunk_Puss_Under.png",
#                "True", Null(),
#                )
#    contains:
#            #hose layer
#            ConditionSwitch(
#                "LauraX.Panties and LauraX.PantiesDown", Null(),
#                "LauraX.Hose == 'ripped pantyhose' and ShowFeet", "images/LauraSex/Laura_Sex_Hose_Pantyhose_Holed.png",
#                "LauraX.Hose == 'ripped pantyhose'", "images/LauraSex/Laura_Sex_Hose_Pantyhose_Holed.png",
#                "True", Null(),
#                ),
#    contains:
#            # The animation of Zero's moving penis, masked by her pussy shape
#            ConditionSwitch(
##                "not Player.Sprite", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 3", AlphaMask("Laura_Sex_Fucking_Zero_Anim3", "Laura_Sex_Fucking_Mask"),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", AlphaMask("Laura_Sex_Fucking_Zero_Anim2", "Laura_Sex_Fucking_Mask"),
#                "Player.Sprite and Player.Cock == 'in' and Speed == 1", AlphaMask("Laura_Sex_Fucking_Zero_Anim1", "Laura_Sex_Heading_Mask"),
#                "Player.Sprite and Player.Cock == 'in'", "Laura_Sex_Fucking_Zero_Anim0",
#                "True", Null(),
#                )
#    contains:
#            #Piercings
#            ConditionSwitch(
#                "LauraX.Pierce == 'barbell' and Player.Sprite and Player.Cock == 'in' and Speed", "images/LauraSex/Laura_Sex_Pierce_Pussy_BarbellF.png",
#                "LauraX.Pierce == 'ring' and Player.Sprite and Player.Cock == 'in' and Speed", "images/LauraSex/Laura_Sex_Pierce_Pussy_RingF.png",
#                "LauraX.Pierce == 'barbell'", "images/LauraSex/Laura_Sex_Pierce_Pussy_Barbell.png",
#                "LauraX.Pierce == 'ring'", "images/LauraSex/Laura_Sex_Pierce_Pussy_Ring.png",
#                "True", Null(),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed == 1", "Laura_Pussy_Spunk_Heading",
#                "True", Null(),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "Speed == 1", Null(),
#                "'in' not in LauraX.Spunk or not Player.Sprite or Player.Cock != 'in' or not Speed or not Player.Male", Null(),
##                "Speed <= 1", Null(), #"Laura_Pussy_Spunk_Heading",
#                "True", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Over.png",
#                )

    #End Laura Pussy composite


image Laura_69_Lick_Pussy:
        "Lick_AnimF"
        zoom 0.6
        rotate 180
        offset (515,400)#(515,520
image Laura_69_Lick_Ass:
        "Lick_AnimF"
        zoom 0.6
        rotate 180
        offset (515,500)#(535,580)

image Laura_Sex_Fondle_Pussy:
        "GropePussy_Laura"
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

image Laura_69_Fondle_Pussy:
        "GropePussy_Laura"
        xzoom -1.5
        yzoom 1.5
        offset(-710,-300) #(-890,-300)
#        block:
#            ease 1 offset(-1000,0) #(535,500)
#            ease 1 offset(-1000,-1000) #(535,500)
#            ease 1 offset(0,-1000) #(535,500)
#            ease 1 offset(0,0) #(535,500)
#            repeat

image Laura_69_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/JubesSex/Jubes_Sex_Anal.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/JubesSex/Jubes_Sex_Anal.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/LauraSex/Laura_Sex_Anus.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/LauraSex/Laura_Sex_Anus.png",
#            "Player.Sprite and Player.Cock == 'anal' and Speed", "Laura_Sex_Anal_Heading",
#            "Player.Sprite and Player.Cock == 'anal'", "Laura_Sex_Anal_Tip",
            "LauraX.Plug", "Laura_Plug_69",
            "LauraX.Loose > 2", "Laura_Gape_Anal_69",
#            "LauraX.Loose", "images/LauraSex/Laura_Sex_Hole_Loose.png",
            "True", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_69_Anus.png",
            "True", Null(),
            )
    contains:
            #Spunk under penis
            ConditionSwitch(
                "'anal' not in LauraX.Spunk or not Player.Male", Null(),
#                "Player.Sprite and Player.Cock != 'anal' and Speed >= 1", "images/LauraSex/Laura_Sex_Spunk_Anal_Under.png",
#                "Player.Sprite and Player.Cock == 'anal' and Speed == 1", "Laura_Sex_Anal_Spunk_Heading_Under",
                "True", "images/BetsySex/Betsy_69_Spunk_Ass.png",
                )
#            offset (-8,-5)
            offset (-10,-105)
#    contains:
#            # The animation of Zero's moving penis, masked by her anus shape
#            ConditionSwitch(
#                "not Player.Sprite or Player.Cock != 'anal'", Null(),
#                "Speed >= 3",  AlphaMask("Laura_Sex_Anal_Zero_Anim3", "Laura_Sex_Anal_MaskF"),
#                "Speed >= 2", AlphaMask("Laura_Sex_Anal_Zero_Anim2", "Laura_Sex_Anal_MaskF"),
#                "Speed", AlphaMask("Laura_Sex_Anal_Zero_Anim1", "Laura_Sex_Anal_Mask"),
#                "True", AlphaMask("Laura_Sex_Anal_Zero_Anim0", "Laura_Sex_Anal_Mask"),
#                )
#    contains:
#            #Spunk over penis
#            ConditionSwitch(
#                "'anal' not in LauraX.Spunk or not Player.Sprite or Player.Cock != 'anal' or not Speed or not Player.Male", Null(),
#                "Speed == 1", "Laura_Sex_Anal_Spunk_Heading_Over",
#                "True", "Laura_Sex_Anal_Spunk",
#                )

image Laura_Gape_Anal_Sex2:
        #removing an anal plug
        contains:
            #Hole
            "images/LauraSex/[LauraX.skin_image.skin_path]Laura_69_Anus_Gape.png"
            transform_anchor True
            subpixel True
            anchor (550,545)#600,600(730,700)
            offset (730,700)#(730,700)
            zoom .20 # tight
            block:
                ease 3 zoom .25 #in.87
                ease 3 zoom .20 #out
                repeat

image Laura_Gape_Anal_69:
        "Laura_Gape_Anal"
#        xzoom -1.5
#        yzoom 1.5
        rotate 180
        offset(-485,-95) #(-175,-200)

#image Laura_Gape_Anal_69:
#        "Laura_Gape_Anal_Sex2"
##        xzoom -1.5
##        yzoom 1.5
#        offset(-173,-178) #(-175,-200)
image Laura_Plug_69:
        "images/PlugBase_Sex.png"
#        xzoom -1.5
#        yzoom 1.5
        offset(-5,-110) #(-175,-200)

#Start Animations for Laura's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Laura_69_Static:
        #this is the animation for Laura's hairback during 69, Speed 0 (static)
        contains:
            subpixel True
            "Laura_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-175) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-180) #top -130
#                pause .5
                ease 1.25 pos (0,-175) #bottom -125
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
        #this is the animation for Laura's head during 69, Speed 0 (static)
        contains:
            subpixel True
            "Laura_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-175) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-180) #top -130
#                pause .5
                ease 1.25 pos (0,-175) #bottom -125
                repeat
        #this is the animation for Laura's upper body during 69, Speed 0 (static)
        contains:
            "Laura_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,-100) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,-110) #top -80
                pause .25
                ease 1 pos (0,-100) #bottom -70
                repeat
        #this is the animation for Laura's lower body during 69, Speed 0 (static)
        contains:
            "Laura_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat

#Start Animations for Laura's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Laura_69_Anim1:
        #this is the animation for Laura's hairback during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Laura_69_HairBack"
            transform_anchor True
            anchor (450,180)#(450,220) (610,420)
            offset (625,700)#(645,700)
            rotate 190
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-10) #X less is left, Y less is up
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
                easein .75 xpos -50 #top 125(35,-65)
                pause .75#1.25
                ease 2.0 xpos 0 #bottom 175(85,50)
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
        #this is the animation for Laura's head during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Laura_69_Head"
            transform_anchor True
            anchor (450,180)#(450,220) (610,420)
            offset (645,700)#(470,550)
            rotate 240
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,0) #X less is left, Y less is up
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
                easein .75 xpos -50 #top 125(35,-65)
                pause .75#1.25
                ease 2.0 xpos 0 #bottom 175(85,50)
                pause 1 #1.25
                repeat
        contains:
            subpixel True
            "Laura_69_HairOver"
            transform_anchor True
            anchor (450,180)#(450,220) (610,420)
            offset (625,700)#(645,700)
            rotate 190
#            zoom .75
#            offset (180,50)#(180,100)
            pos (-5,-10) #X less is left, Y less is up
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
                easein .75 xpos -50 #top 125(35,-65)
                pause .75#1.25
                ease 2.0 xpos -5 #bottom 175(85,50)
                pause 1 #1.25
                repeat
        #this is the animation for Laura's upper body during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Laura_69_Body"
            rotate 180
#            zoom .65
#            alpha 0.5
            pos (60,-15) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 xpos 20 #top (10,-70)
                pause .8
                ease 1.4 xpos 50 #bottom(30,-10)
                ease 1.3 xpos 60 #bottom(30,-10)
#                pause 1.3
                pause .25
                repeat
            parallel:
                #Total time, 5 seconds
                pause .5
                easein .75 ypos -120 #top (10,-70)
                pause .8
#                ease 1.4 ypos -50 #bottom(30,-10)
                ease 2.7 ypos -15 #bottom(30,-10)
                pause .25
                repeat
#        #this is the animation for Laura's lower body during 69, Speed 1 (licking)
        contains:
            subpixel True
            "Laura_69_Legs"
            rotate 185
            pos (70,65) #X less is left, Y less is up
            parallel:
                #Total time, 5 seconds
                pause .5
                easein 1.0 pos (20,-15)#(0,-5)
                pause .5
                ease 2.5 pos (70,65)#(30,25)
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

#Start Animations for Laura's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Laura_69_Anim2:
        #this is the animation for Laura's hairback during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Laura_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-130) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-160) #top -110
#                pause .5
                ease 1.25 pos (0,-130) #bottom -80
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
        #this is the animation for Laura's head during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Laura_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-130) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (0,-160) #top -110
#                pause .5
                ease 1.25 pos (0,-130) #bottom -80
                repeat
        #this is the animation for Laura's upper body during 69, Speed 2 (heading)
        contains:
            "Laura_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,-90) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,-100) #top -10
                pause .25
                ease 1 pos (0,-90) #bottom 0
                repeat
        #this is the animation for Laura's lower body during 69, Speed 2 (heading)
        contains:
            "Laura_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat

#Start Animations for Laura's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Laura_69_Anim3:
        #this is the animation for Laura's hairback during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Laura_69_HairBack"
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
        #this is the animation for Laura's head during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Laura_69_Head"
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
        #this is the animation for Laura's upper body during 69, Speed 3 (sucking)
        #this is the animation for Laura's lower body during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Laura_69_Body"
            rotate 180
#            zoom .65
            pos (0,-20) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-60) #top 0
#                pause .5
                ease 1.25 pos (0,-20) #bottom 40
                repeat
        #this is the animation for Laura's lower body during 69, Speed 3 (sucking)
        contains:
            subpixel True
            "Laura_69_Legs"
            rotate 180
            pos (0,40) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,25) #-5
#                pause .5
                ease 1.25 pos (0,40) #10
                repeat

#Start Animations for Laura's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Laura_69_Anim4:
        #this is the animation for Laura's hairback during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Laura_69_HairBack"
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
        #this is the animation for Laura's head during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Laura_69_Head"
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
            "Laura_69_HairOver"
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
        #this is the animation for Laura's upper body during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Laura_69_Body"
            rotate 180
#            zoom .65
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,-25) #top 35
                pause .5
                ease 1.75 pos (0,10) #bottom 70
                repeat
        #this is the animation for Laura's lower body during 69, Speed 4 (deep)
        contains:
            subpixel True
            "Laura_69_Legs"
            rotate 180
            pos (0,60) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,55)
#                pause .5
                ease 2.25 pos (0,60)
                repeat

#Start Animations for Laura's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Laura_69_Anim5:
        #this is the animation for Laura's hairback during 69, Speed 5 (cum high)
        contains:
            subpixel True
            "Laura_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-145) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 0.25 pos (0,-150) #top -110
                pause .5
                ease 2.25 pos (0,-145) #bottom -80
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
        #this is the animation for Laura's head during 69, Speed 2 (heading)
        contains:
            subpixel True
            "Laura_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-145) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 0.25 pos (0,-150) #top -110
                pause .5
                ease 2.25 pos (0,-145) #bottom -80
                repeat
        #this is the animation for Laura's upper body during 69, Speed 2 (heading)
        contains:
            "Laura_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (0,-90) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (0,-100) #top -10
                pause .25
                ease 1 pos (0,-90) #bottom 0
                repeat
        #this is the animation for Laura's lower body during 69, Speed 2 (heading)
        contains:
            "Laura_69_Legs"
            subpixel True
            rotate 180
            pos (0,5) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (0,0) #top
                pause .25
                ease 1 pos (0,5) #bottom
                repeat

#Start Animations for Laura's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Laura_69_Anim6:
        #this is the animation for Laura's hairback during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Laura_69_HairBack"
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
        #this is the animation for Laura's head during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Laura_69_Head"
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
            "Laura_69_HairOver"
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
        #this is the animation for Laura's upper body during 69, Speed 6 (cum deep)
#        contains:
#            subpixel True
#            "Laura_69_Tits"
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
            "Laura_69_Body"
            rotate 180
#            zoom .65
            pos (0,10) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (0,5) #top 35
                pause .5
                ease 1.75 pos (0,10) #bottom 70
                repeat
        #this is the animation for Laura's lower body during 69, Speed 6 (cum deep)
        contains:
            subpixel True
            "Laura_69_Legs"
            rotate 180
            pos (0,60) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
#                pause .25
                easein .75 pos (0,55)
#                pause .5
                ease 2.25 pos (0,60)
                repeat

#End Animations for Laura's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#Start Laura 69 Cunnilingus Animations
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////

#Start Animations for Laura's 69 Cunnalingus pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Laura_69_CUN:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
#                "True", "Laura_69_Anim1",
                "Speed == 2",   "Laura_69_Cun2",
                "Speed == 3",   "Laura_69_Cun3",
                "Speed",        "Laura_69_Cun1",
                "True",         "Laura_69_Cun0",
                ),
        )
    align (0.6,0.0)
    pos (475,-700)
    zoom 1.8#1/3

#Start Animations for Laura's 69 pose / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Animations for Laura's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Laura_69_Cun0:
        #this is the animation for Laura's hairback during 69, Speed 0 (static)
        contains:
            subpixel True
            "Laura_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (10,-170) #(10,-120) X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (10,-165) #top
#                pause .5
                ease 1.25 pos (10,-170) #bottom
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
        #this is the animation for Laura's head during 69, Speed 0 (static)
        contains:
            subpixel True
            "Laura_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (10,-170) #(10,-120) X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1.75 pos (10,-165) #top
#                pause .5
                ease 1.25 pos (10,-170) #bottom
                repeat
        #this is the animation for Laura's upper body during 69, Speed 0 (static)
        contains:
            "Laura_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (5,-130) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .75 pos (5,-135) #top 35
                pause .5
                ease 1.75 pos (5,-130) #bottom 70
                repeat
        #this is the animation for Laura's lower body during 69, Speed 0 (static)
        contains:
            "Laura_69_Legs"
            subpixel True
            rotate 180
            pos (15,-30) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (15,-25) #top
                pause .25
                ease 1 pos (15,-30) #bottom
                repeat

#Start Animations for Laura's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Laura_69_Cun1:
        #this is the animation for Laura's hairback during 69, Speed 1 (lick)
        contains:
            subpixel True
            "Laura_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (0,-160) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                ease 1.0 ypos -165 #top
                easeout .5 ypos -155 #top
                easein 1.0 ypos -160 #bottom
                pause .5
                repeat
            parallel:
                #Total time, 3 seconds
                pause .5
                ease .5 xpos 32 #top
                pause .25
                easein 1.25 xpos 0 #bottom
                pause .5
                repeat
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
        #this is the animation for Laura's head during 69, Speed 1 (lick)
        contains:
            subpixel True
            "Laura_69_Head"
            rotate 185
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-160) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                ease 1.0 ypos -165 #top
                easeout .5 ypos -155 #top
                easein 1.0 ypos -160 #bottom
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
            "Laura_69_HairOver"
            rotate 185
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-160) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                ease 1.0 ypos -165 #top
                easeout .5 ypos -155 #top
                easein 1.0 ypos -160 #bottom
                pause .5
                repeat
            parallel:
                #Total time, 3 seconds
                pause .5
                ease .5 xpos 32 #top
                pause .25
                easein 1.25 xpos 12 #bottom
                pause .5
                repeat
            parallel:
                #Total time, 3 seconds
                pause .5
                easein .5 rotate 180 #top
                pause .25
                easein 1.25 rotate 185 #bottom
                pause .5
                repeat
        #this is the animation for Laura's upper body during 69, Speed 1 (lick)
        contains:
            "Laura_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (10,-120) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.25 pos (10,-125) #top
                pause .25
                ease 1.25 pos (10,-120) #bottom
                repeat
        #this is the animation for Laura's lower body during 69, Speed 1 (lick)
        contains:
            "Laura_69_Legs"
            subpixel True
            rotate 180
            pos (15,-30) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (15,-25) #top
                pause .25
                ease 1 pos (15,-30) #bottom
                repeat


#Start Animations for Laura's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Laura_69_Cun2:
        #this is the animation for Laura's hairback during 69, Speed 2 (clit)
        contains:
            subpixel True
            "Laura_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (32,-150) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                easein .9 ypos -145 #top
                easein 1.1 ypos -150 #bottom
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
        contains:
            #pussy
            "Zero_Legs"
            anchor (.5,.5)
            zoom .45
            pos (0,0)#(410,790)
            offset (745,921)#(728,920)
        #this is the animation for Laura's head during 69, Speed 2 (clit)
        contains:
            subpixel True
            "Laura_69_Head"
            rotate 178
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-150) #X less is left, Y less is up
            parallel:
                #Total time, 3 seconds
                easein .9 ypos -145 #top
                easein 1.1 ypos -150 #bottom
                repeat
            parallel:
                #Total time, 3 seconds
                pause 0.2
                easein .8 rotate 183 #top
                easein 1.0 rotate 178 #bottom
                repeat
        #this is the animation for Laura's upper body during 69, Speed 2 (clit)
        contains:
            "Laura_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (10,-120) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein 1 pos (10,-125) #top
                ease 1 pos (10,-120) #bottom
                repeat
        #this is the animation for Laura's lower body during 69, Speed 2 (clit)
        contains:
            "Laura_69_Legs"
            subpixel True
            rotate 180
            pos (15,-25) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (15,-30) #top
                pause .25
                ease 1 pos (15,-25) #bottom
                repeat

#Start Animations for Laura's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Laura_69_Cun3:
        #this is the animation for Laura's hairback during 69, Speed 3 (suck)
        contains:
            subpixel True
            "Laura_69_HairBack"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-145) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .5 ypos -150 #top
                pause 1.25
                ease 1.25 ypos -145 #bottom
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
        #this is the animation for Laura's head during 69, Speed 3 (suck)
        contains:
            subpixel True
            "Laura_69_Head"
            rotate 180
#            zoom .75
#            offset (180,50)#(180,100)
            pos (12,-145) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                easein .5 ypos -150 #top
                pause 1.25
                ease 1.25 ypos -145 #bottom
                repeat
        #this is the animation for Laura's upper body during 69, Speed 3 (suck)
        contains:
            "Laura_69_Body"
            subpixel True
            rotate 180
#            zoom .65
            pos (10,-120) #X less is left, Y less is up
            block:
                #Total time, 3 seconds
                pause .25
                easein 1.5 pos (10,-125) #top
                pause .25
                ease 1 pos (10,-120) #bottom
                repeat
        #this is the animation for Laura's lower body during 69, Speed 3 (suck)
        contains:
            "Laura_69_Legs"
            subpixel True
            rotate 180
            pos (15,-20) #X less is left, Y less is up
            block:
                pause .25
                easein 1.5 pos (15,-30) #top
                pause .25
                ease 1 pos (15,-20) #bottom
                repeat
#End Animations for Laura's Body during 69 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#End Laura 69 Animations

# Start Laura Scissor Pose content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Laura_SC_Sprite:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
                #if the top's down. . .
                "Speed >= 2", "Laura_SC_Anim_2",
                "Speed", "Laura_SC_Anim_1",
                "True", "Laura_SC_Anim_0",
                ),
        )
    align (0.6,0.0)
    pos (650,300)#(650,200)(925,740)#(910,850)
    zoom 0.85#0.8

# End Laura Sex Pose Speed 2 Scissor / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#image Laura_Sex_Legs = LiveComposite(
image Laura_SC_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Kitty_SexSprite
        (1120,840),
        (0,0), "images/LauraSex/Laura_Sex_Legs.png",
        #Legs Base
        (0,0),ConditionSwitch(
            #wet look
            "LauraX.Water", "images/LauraSex/Laura_Sex_Wet_Legs.png",
            "True", Null(),
            ),
#        (0,0), "Laura_Sex_Anus",
        #Anus Composite

        (0,0), "Laura_SC_Pussy",
        #Pussy Composite

        (0,0), ConditionSwitch(
            #Panties if up
            "not LauraX.Panties or LauraX.PantiesDown", Null(),
            "Player.Sprite and (Player.Cock == 'sex' or Player.Cock == 'anal')", Null(),  #hide if sexing
            "LauraX.Panties == 'lace panties'", Recolor("Laura", "Panties", "images/LauraSex/Laura_Sex_Panties_Lace.png"),
            "LauraX.Panties == 'green panties' and LauraX.Wet", "images/LauraSex/Laura_Sex_Panties_Green_Wet.png",
            "LauraX.Panties == 'green panties' or LauraX.Panties == 'bikini bottoms'", "images/LauraSex/Laura_Sex_Panties_Green.png",
            "LauraX.Panties == 'shorts' and LauraX.Wet", "images/LauraSex/Laura_Sex_Panties_Shorts_Wet.png",
            "LauraX.Panties == 'shorts'", "images/LauraSex/Laura_Sex_Panties_Shorts.png",
            "LauraX.Wet", "images/LauraSex/Laura_Sex_Panties_Black_Wet.png",
            "True", Recolor("Laura", "Panties", "images/LauraSex/Laura_Sex_Panties_Black.png"),
            ),

        (0,0), ConditionSwitch(
            #Hose layer (add panties up dependencies)
            #"LauraX.PantiesDown", Null(),
            "LauraX.Hose == 'ripped pantyhose'", "images/LauraSex/Laura_Sex_Hose_Legs_Full_Hole.png",
            "LauraX.Hose == 'ripped tights'", "images/LauraSex/Laura_Sex_Hose_Legs_Tights_Hole.png",
            "LauraX.Hose == 'stockings'", "images/LauraSex/Laura_Sex_Hose_Legs_Stockings.png",
            "LauraX.Hose == 'stockings and garterbelt'", "images/LauraSex/Laura_Sex_Hose_Legs_StockingGarter.png",
            "LauraX.Hose == 'garterbelt'", "images/LauraSex/Laura_Sex_Hose_Legs_Garter.png",
            "LauraX.PantiesDown", Null(),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),  #hide if sexing
            "LauraX.Hose == 'pantyhose'", "images/LauraSex/Laura_Sex_Hose_Legs_Full.png",
            "LauraX.Hose == 'tights' and LauraX.Wet", "images/LauraSex/Laura_Sex_Hose_Legs_Tights_Wet.png",
            "LauraX.Hose == 'tights'", "images/LauraSex/Laura_Sex_Hose_Legs_Tights.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Legs Layer
            "LauraX.Legs == 'skirt'", "images/LauraSex/Laura_Sex_Legs_Skirt.png",
            "LauraX.Upskirt", Null(),
            "LauraX.Legs == 'pants' and LauraX.Wet > 1", "images/LauraSex/Laura_Sex_Legs_Pants_Wet.png",
            "LauraX.Legs == 'pants'","images/LauraSex/Laura_Sex_Legs_Pants.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Sweater
            "LauraX.Acc == 'sweater'", "images/LauraSex/Laura_Sex_Sweater.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Over Layer
#            "LauraX.Over == 'towel'", "images/KittySex/Kitty_Sex_Towel_Legs.png",
#            "True", Null(),
#            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'belly' in LauraX.Spunk and Player.Male", "images/KittySex/Kitty_Sex_Spunk_Pelvis.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite", Null(),
            "Trigger == 'lick pussy'", "Laura_Sex_Lick_Pussy",
            "Trigger == 'lick ass'", "Laura_Sex_Lick_Ass",
            "LauraX.Offhand == 'fondle pussy' and LauraX.Lust > 60", At("LauraFingerHand", GirlFingerPussyX()),
            "LauraX.Offhand == 'fondle pussy'", At("LauraMastHand", GirlGropePussyX()),
            "True", Null()
            ),
#        (0,0), ConditionSwitch(
#            #Shows different lower body motion depending on events
#            "not Speed or Player.Cock == 'foot' or ShowFeet", "Laura_Sex_Feet",
#            #"Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Laura_Sex_Feet", "images/KittySex/Kitty_Sex_FeetMask.png"),
#            "True", AlphaMask("Laura_Sex_Feet","images/LauraSex/Laura_Sex_FeetMask2.png")
#            ),
        )


image Laura_SC_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).
    contains:
            # The background plate of her pussy
            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/LauraSex/Laura_Sex_Pussy_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pussy_Open.png",
#                "Player.Sprite and Player.Cock == 'in'", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pussy_Closed.png",
                "'dildo pussy' in (Trigger,Trigger2,LauraX.Offhand)", "images/LauraSex/Laura_Sex_Pussy_Fucking.png",
#                "Trigger == 'dildo pussy'", "images/LauraSex/Laura_Sex_Pussy_Fucking.png",
                "Trigger == 'lick pussy' or Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pussy_Open.png",
                "LauraX.Offhand == 'fondle pussy' and LauraX.Lust > 60", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pussy_Open.png",
                "True", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pussy_Closed.png",
                )
#    contains:
#            # growing pussy hole
#            ConditionSwitch(
#                "Player.Sprite and Player.Cock == 'in' and Speed == 1", "Laura_Sex_Pussy_Hole",#"images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pussy_Open.png",
#                "True", Null(),
#                )
    contains:
            # wet pussy
            ConditionSwitch(
                "not LauraX.Wet", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/KittySex/Kitty_Sex_WetPussy_F.png",
                "True", "images/KittySex/Kitty_Sex_WetPussy_C.png",
                )
    contains:
            #ring piercing
            ConditionSwitch(
                "LauraX.Pierce != 'ring'", Null(),
#                "not Player.Sprite or Player.Cock != 'in' or Speed <= 1", "images/LauraSex/Laura_Sex_Pussy_Ring.png",
                "True", "images/LauraSex/Laura_Sex_Pussy_RingF.png",
                )
    contains:
            #barbell piercing
            ConditionSwitch(
                "LauraX.Pierce != 'barbell'", Null(),
#                "not Player.Sprite or Player.Cock != 'in' or Speed <= 1", "images/LauraSex/Laura_Sex_Pussy_Barbell.png",
                "True", "images/LauraSex/Laura_Sex_Pussy_BarbellF.png",
                )
    contains:
            # pubes
            ConditionSwitch(
                "not LauraX.Pubes", Null(),
#                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/LauraSex/Laura_Sex_Pubes_Fucking.png",
#                "Player.Sprite and Player.Cock == 'in' and Speed", Recolor("Laura", "Pubes", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pubes_Open.png"),
#                "Player.Sprite and Player.Cock == 'in'", Recolor("Laura", "Pubes", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pubes_Closed.png"),
                "Trigger == 'lick pussy' or Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", Recolor("Laura", "Pubes", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pubes_Open.png"),
#                "'dildo pussy' in (Trigger,Trigger2,LauraX.Offhand)", "images/LauraSex/Laura_Sex_Pubes_Fucking.png",
                "LauraX.Offhand == 'fondle pussy' and LauraX.Lust > 60", Recolor("Laura", "Pubes", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pubes_Open.png"),
#                "Trigger == 'dildo pussy'", "images/LauraSex/Laura_Sex_Pubes_Fucking.png",
                "True", Recolor("Laura", "Pubes", "images/LauraSex/[LauraX.skin_image.skin_path]Laura_Sex_Pubes_Closed.png"),
                )

    #End Laura Pussy composite

#End Animations for Laura's Pussy during SC / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# End Laura Scissor Pose Legs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Laura_SC_Anim_0:
        #this is the animation for Laura's lower body during Scissoring, Speed 0 (static)
        contains:
            subpixel True
            "Laura_Sex_Body"
            anchor (720,600)#(560,580)
            offset (590,510) #(500,240) #(560,580)
            transform_anchor True
            zoom 1#1.2
            rotate -30
            pos (80,0) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                ease 2 pos (80,10)
                pause .5
                ease 2 pos (80,0)
                pause .5
                repeat
        contains:
            subpixel True
            "Laura_Sex_Legs"
            anchor (720,600)#(560,580)
            offset (590,510) #(500,240) #(560,580)
            transform_anchor True
            zoom 1.1#1.2
            rotate -45
            pos (0,0) #X less is left, Y less is up
            parallel:
                pause .5
                ease 2 rotate -35
                pause .5
                ease 2 rotate -45
                repeat
#            parallel:
#                pause .5
#                ease 2 rotate 30
#                pause .5
#                ease 2 rotate 35
#                repeat
        contains:
            #pussy
            "Zero_Pussy_Full"
            transform_anchor True
            anchor (.5,.5)
            zoom .7#.45
            pos (0,0)#(410,790)
            rotate 15
            offset (765,875)#(925,740)#(910,850)
#        contains:
#            subpixel True
##            "Laura_Sex_Feet"
#            ConditionSwitch(
#                #Shows different lower body motion depending on events
#                "ShowFeet", "Laura_Sex_Feet",
#                "True", AlphaMask("Laura_Sex_Feet","images/LauraSex/Laura_Sex_FeetMask2.png")
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
        #end animation for Laura's lower body during Scissoring, Speed 0 (static) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Laura_SC_Anim_1:
        #this is the animation for Laura's lower body during Scissoring, Speed 1 (slow)
        contains:
            subpixel True
            "Laura_Sex_Body"
            anchor (720,600)#(560,580)
            offset (590,510) #(500,240) #(560,580)
            transform_anchor True
            zoom 1
            rotate -20
            pos (50,10) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate 15
#                pause .5
#                ease 2 rotate 20
#                pause .5
#                repeat
            parallel:
                ease 1 pos (50,20)
                pause .5
                ease 1 pos (50,10)
                pause .5
                repeat
        contains:
            subpixel True
            "Laura_Sex_Legs"
            anchor (720,600)#(560,580)
            offset (590,510) #(500,240) #(560,580)
            transform_anchor True
            zoom 1.1
            rotate -25#35
            pos (0,-10) #X less is left, Y less is up
            parallel:
#                pause .5
                ease 1.5 rotate -20
#                pause .5
                ease 1.5 rotate -25
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
            rotate 15
            offset (765,875)#(925,740)#(910,850)
            parallel:
                pause .5
                ease 1 pos (0,-5)
                pause .5
                ease 1 pos (0,0)
                repeat
#        contains:
#            subpixel True
##            "Laura_Sex_Feet"
#            ConditionSwitch(
#                #Shows different lower body motion depending on events
#                "ShowFeet", "Laura_Sex_Feet",
#                "True", AlphaMask("Laura_Sex_Feet","images/LauraSex/Laura_Sex_FeetMask2.png")
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
        #End animation for Laura's lower body during Scissoring, Speed 1 (slow) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Laura_SC_Anim_2:
        #this is the animation for Laura's lower body during Scissoring, Speed 2 (fast)
        contains:
            subpixel True
            "Laura_Sex_Body"
            anchor (720,600)#(560,580)
            offset (590,510) #(500,240) #(560,580)
            transform_anchor True
            zoom 1
            rotate -20
            pos (50,10) #X less is left, Y less is up (0,0)
#            parallel:
#                ease 2 rotate -15
#                pause .5
#                ease 2 rotate -20
#                pause .5
#                repeat
            parallel:
                pause .1
                ease .5 pos (50,20)
                ease .5 pos (50,10)
                repeat
        contains:
            subpixel True
            "Laura_Sex_Legs"
            anchor (720,600)#(560,580)
            offset (590,510) #(500,240) #(560,580)
            transform_anchor True
            zoom 1.1
            rotate -25#35
            pos (0,-10) #X less is left, Y less is up
            parallel:
                ease .5 rotate -20
                pause .1
                ease .5 rotate -25
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
            rotate 15
            offset (765,875)#(925,740)
            parallel:
                ease .5 pos (0,-5)
                ease .5 pos (0,0)
                pause .1
                repeat
#        contains:
#            subpixel True
##            "Laura_Sex_Feet"
#            ConditionSwitch(
#                #Shows different lower body motion depending on events
#                "ShowFeet", "Laura_Sex_Feet",
#                "True", AlphaMask("Laura_Sex_Feet","images/LauraSex/Laura_Sex_FeetMask2.png")
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
        #End animation for Laura's lower body during Scissoring, Speed 2 (fast) / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     SC Launch/Reset
label Laura_SC_Launch(Line = Trigger):
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#    return
###    #temporary      #temporary      #temporary      #temporary      #temporary      #temporary

    $ Trigger = Line

    if renpy.showing("Laura_SC_Sprite"):
        return
    $ Speed = 0
    call Girl_Hide(LauraX,1) #call Rogue_Hide
    show Laura_SC_Sprite zorder 150
    with dissolve
    return

label Laura_SC_Reset:
    if not renpy.showing("Laura_SC_Sprite"):
        return
    $ LauraX.ArmPose = 2
    hide Laura_SC_Sprite
    call Girl_Hide(LauraX) #call Rogue_Hide
#    call Set_The_Scene(Dress = 0)
    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
        alpha 1 zoom 1 offset (0,0) anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return
# End Laura Scissor Pose content / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


# Laura Misc Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#label Laura_Kissing_Launch(T = Trigger,Set=1):
#    call Laura_Hide
#    $ Trigger = T
#    $ LauraX.Pose = "kiss" if Set else LauraX.Pose
#    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer
#    show Laura_Sprite at SpriteLoc(StageCenter) zorder LauraX.Layer:
#        ease 0.5 offset (0,0) zoom 2 alpha 1
#    return

#label Laura_Kissing_Smooch:
#    $ LauraX.FaceChange("kiss")
#    show Laura_Sprite at SpriteLoc(StageCenter) zorder LauraX.Layer:
#        ease 0.5 xpos StageCenter offset (0,0) zoom 2 alpha 1
#        pause 1
#        ease 0.5 xpos LauraX.SpriteLoc zoom 1
#    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
#        zoom 1
#    $ LauraX.FaceChange("sexy")
#    return

#label Laura_Breasts_Launch(T = Trigger,Set=1):
#    call Laura_Hide
#    $ Trigger = T
#    $ LauraX.Pose = "breasts" if Set else LauraX.Pose
#    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
##        ease 0.5 offset (-100,-200) zoom 2
#        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
#    return

#label Laura_Middle_Launch(T = Trigger,Set=1):
#    call Laura_Hide
#    $ Trigger = T
#    $ LauraX.Pose = "mid" if Set else LauraX.Pose
#    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
##        ease 0.5 offset (-100,-200) zoom 2
#        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
#    return

#label Laura_Pussy_Launch(T = Trigger,Set=1):
#    call Laura_Hide
#    $ Trigger = T
#    $ LauraX.Pose = "pussy" if Set else LauraX.Pose
#    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
#        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
#    return

#label Laura_Pos_Reset(T = 0,Set=0):
#    if LauraX.Loc != bg_current:
#            return
#    call Laura_Hide
#    show Laura_Sprite at SpriteLoc(LauraX.SpriteLoc) zorder LauraX.Layer:
#            ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
#    show Laura_Sprite zorder LauraX.Layer:
#            offset (0,0)
#            anchor (0.5, 0.0)
#            zoom 1
#            xzoom 1
#            yzoom 1
#            alpha 1
#            pos (LauraX.SpriteLoc,50)
#    $ LauraX.Pose = "full" if Set else 0
#    $ Trigger = T
#    return

#label Laura_Hide(Sprite=0):
##        call Laura_Sex_Reset
##        if renpy.showing("Laura_SexSprite"):
##            call Laura_Sex_Reset
##        if renpy.showing("Laura_Doggy_Animation"):
##            call Laura_Doggy_Reset
#        hide Laura_SexSprite
#        hide Laura_Doggy_Animation
#        hide Laura_HJ_Animation
#        hide Laura_BJ_Animation
#        hide Laura_TJ_Animation
#        hide Laura_Finger_Animation
#        hide Laura_CUN_Animation
#        hide Laura_Seated
#        if Sprite:
#                hide Laura_Sprite
#        return



# Interface items //////////////////////////////////////////////////////////////////////////////

image GropeLeftBreast_Laura:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65#.7
        pos (195,380)#(215,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 60
        block:
            ease 1 rotate 30
            ease 1 rotate 60
            repeat

image GropeRightBreast_Laura:
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (110,380)#(120,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block:
            ease 1 rotate -30 #-30
            ease 1 rotate -60 #-60
            repeat

#image GropeBreast:
image LickRightBreast_Laura:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5
        xzoom -0.45
        pos (95,355)#(105,375)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (75,330)#(85,345)  top
            pause .5
            ease 1.5 rotate 30 pos (95,355)#(105,375) bottom
            repeat

image LickLeftBreast_Laura:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5
        xzoom -0.45
        pos (195,360) #(200,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (190,340)#(190,380)
            pause .5
            ease 1.5 rotate 30 pos (195,360)#(200,410)
            repeat

image GropeThigh_Laura:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (115,690)#(180,670)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        block:
            pause .5
            ease 1 rotate 110 pos (105,780) #(150,750) bottom
            ease 1 rotate 100 pos (115,690)
            repeat

image GropePussy_Laura:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (120,620)#(200,600) -20
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease .5 rotate 190 pos (120,605) #(200,585)
                ease .75 rotate 170 pos (120,620)
            choice:
                ease .5 rotate 190 pos (120,605)
                pause .25
                ease 1 rotate 170 pos (120,620)
            repeat

image FingerPussy_Laura:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.65
        pos (140,700)#(210,665)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (150,665)#(220,640)
                pause .5
                ease 1 rotate 50 pos (140,700)  #(210,665)
            choice:
                ease .5 rotate 40 pos (150,665)
                pause .5
                ease 1.75 rotate 50 pos (140,700)
            choice:
                ease 2 rotate 40 pos (150,665)
                pause .5
                ease 1 rotate 50 pos (140,700)
            choice:
                ease .25 rotate 40 pos (150,665)
                ease .25 rotate 50 pos (140,700)
                ease .25 rotate 40 pos (150,665)
                ease .25 rotate 50 pos (140,700)
            repeat

image Lickpussy_Laura:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (155,650)#(230,625)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout .5 rotate -50 pos (145,630) #(210,605)
            linear .5 rotate -60 pos (135,640) #(200,615)
            easein 1 rotate 10 pos (155,650) #(230,625)
            repeat

image VibratorRightBreast_Laura:
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

image VibratorLeftBreast_Laura:
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

image VibratorPussy_Laura:
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

image VibratorAnal_Laura:
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

image VibratorPussyInsert_Laura:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_Laura:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0



#Lesbian action animations.
image GirlGropeBothBreast_Laura:
    contains:
        "GirlGropeLeftBreast_Laura"
    contains:
        "GirlGropeRightBreast_Laura"

image GirlGropeLeftBreast_Laura:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (220,370)#(240,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate 10 pos (220,380)#(280,390)
            ease 1 rotate -10 pos (220,370)
            repeat

image GirlGropeRightBreast_Laura:
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (90,370) #(90,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block:
            ease 1 rotate -40 pos (90,380)#(90,410)
            ease 1 rotate -10 pos (90,370)
            repeat

image GirlGropeThigh_Laura:
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

image GirlGropePussy_LauraSelf:
    contains:
        "GirlGropePussy_Laura"
        anchor (0.5,0.5)
        rotate -40
#        yzoom -1
        pos (100,500) #(120,530)

image GirlGropePussy_Laura:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (130,595) #(205,595)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (130,590)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 pos (130,590)#-10+20
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (130,590) #(205,590)
                ease .75 rotate 200 pos (130,595) #(205,595)
                ease .5 rotate 205 pos (130,590)
                ease .75 rotate 200 pos (130,595)
            choice: #Fast stroke
                ease .3 rotate 205 pos (130,590)
                ease .3 rotate 200 pos (130,600)
                ease .3 rotate 205 pos (130,590)
                ease .3 rotate 200 pos (130,600)
            repeat

image GirlFingerPussy_Laura:
    contains:
        subpixel True
        "UI_GirlFinger"
        zoom .6
        pos (140,605)#(220,640)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (140,610)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 pos (140,610)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 ypos 620
                ease .75 rotate 200 ypos 625
                ease .5 rotate 205 ypos 620
                ease .75 rotate 200 ypos 625
            choice: #Fast stroke
                ease .3 rotate 205 ypos 620
                ease .3 rotate 200 ypos 630
                ease .3 rotate 205 ypos 620
                ease .3 rotate 200 ypos 630
            repeat

image LauraMastHand:
        "images/UI_GirlHand_Emma.png"
        zoom 1.2
        rotate 220
        offset (800,590)

image LauraFingerHand:
        "images/UI_GirlFinger_Emma.png"
        zoom 1.2
        rotate 220
        offset (800,650)
