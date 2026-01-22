# renpy_sprite_helpers.rpy
init python:
    """
    Helper utilities for sprite Animations files.

    Provides:
    - sprite_skin_prefix(ch): safely returns skin_image.skin_path or empty string
    - sprite_flags(ch): returns common computed flags (is_wet, hair_wet, etc.)

    Add this file to the project and then use in *Animations.rpy files:
      $ skin = sprite_skin_prefix(BetsyX)
      $ f = sprite_flags(BetsyX)

    This reduces repeated attribute lookups in ConditionSwitch expressions.
    """

    def sprite_skin_prefix(ch):
        """Return the skin_image.skin_path prefix for a given character-like object.
        Safe if the attribute is missing.
        """
        try:
            sp = ch.skin_image.skin_path
            if sp is None:
                return ""
            return sp
        except Exception:
            return ""

    def sprite_flags(ch):
        """Return a small dict of commonly-queried boolean/int flags derived from the
        character object. This centralizes attribute access and can be extended.
        Note: this function does not mutate the character, it just returns a dict.
        """
        get = getattr
        flags = {}
        # wetness: some scripts use Wet (int) and Water (bool). Normalize both.
        try:
            wet_val = get(ch, "Wet", 0)
        except Exception:
            wet_val = 0
        flags["is_wet"] = bool(wet_val) or bool(get(ch, "Water", False))
        # hair wet
        hair = get(ch, "Hair", "")
        flags["hair_wet"] = hair in ("wet", "wetlong") or flags["is_wet"]
        # panty related
        flags["panties_down"] = bool(get(ch, "PantiesDown", False))
        flags["has_panties"] = bool(get(ch, "Panties", False))
        # common pose flags
        flags["armpose_not1"] = (get(ch, "ArmPose", 0) != 1)
        flags["has_legs"] = bool(get(ch, "Legs", False))
        flags["upskirt"] = bool(get(ch, "Upskirt", False))
        return flags
