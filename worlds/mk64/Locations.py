from enum import IntFlag, auto

from BaseClasses import Location


ID_BASE = 4660000


class MK64Location(Location):
    game: str = "Mario Kart 64"


class Group(IntFlag):
    base = auto()
    hazard = auto()
    secret = auto()
    blue_shell_item_spot = auto()
    omit = auto()


# Mappings of each Region to dictionary of location data
# 4660000 - 4660584

#   Region: { Location:                    (location id, Group) }
course_locations = {
    "Luigi Raceway": {
        "Luigi Raceway Take the Lead":      (466000_0, Group.base),
        "Luigi Raceway Qualify":            (466000_1, Group.base),
        "Luigi Raceway 1st":                (466000_2, Group.base),
        "Luigi Raceway Balloon":            (46600_97, Group.blue_shell_item_spot),
    },
    "Moo Moo Farm": {
        "Moo Moo Farm Take the Lead":       (466000_3, Group.base),
        "Moo Moo Farm Qualify":             (466000_4, Group.base),
        "Moo Moo Farm 1st":                 (466000_5, Group.base),
        "Defeat Chubby":                    (46600_85, Group.hazard),
    },
    "Koopa Troopa Beach": {
        "Koopa Troopa Beach Take the Lead": (466000_6, Group.base),
        "Koopa Troopa Beach Qualify":       (466000_7, Group.base),
        "Koopa Troopa Beach 1st":           (466000_8, Group.base),
        "Koopa Troopa Beach Secret":        (4660_437, Group.secret),
        "Koopa Troopa Beach Rock":          (46600_98, Group.blue_shell_item_spot),  # Needs Yellow & Blue Switch, or Red & Green, (should just feather be in logic too?)
    },
    "Kalimari Desert": {
        "Kalimari Desert Take the Lead":    (466000_9, Group.base),
        "Kalimari Desert Qualify":          (46600_10, Group.base),
        "Kalimari Desert 1st":              (46600_11, Group.base),
        "Destroy Cactus":                   (46600_86, Group.hazard),
        "Kalimari Desert Secret":           (4660_438, Group.secret),  # Needs Yellow, Red, or Blue Switch, or Feather
    },
    "Toad's Turnpike": {
        "Toad's Turnpike Take the Lead":    (46600_12, Group.base),
        "Toad's Turnpike Qualify":          (46600_13, Group.base),
        "Toad's Turnpike 1st":              (46600_14, Group.base),
        "Toad's Turnpike Secret":           (4660_439, Group.secret),
    },
    "Frappe Snowland": {
        "Frappe Snowland Take the Lead":    (46600_15, Group.base),
        "Frappe Snowland Qualify":          (46600_16, Group.base),
        "Frappe Snowland 1st":              (46600_17, Group.base),
        "Defeat Snowman Bomb":              (46600_87, Group.hazard),
        "Snow Yoshi's Secret":              (4660_440, Group.secret),
    },
    "Choco Mountain": {
        "Choco Mountain Take the Lead":     (46600_18, Group.base),
        "Choco Mountain Qualify":           (46600_19, Group.base),
        "Choco Mountain 1st":               (46600_20, Group.base),
        "Deflect Boulder":                  (46600_88, Group.hazard),
    },
    "Mario Raceway": {
        "Mario Raceway Take the Lead":      (46600_21, Group.base),
        "Mario Raceway Qualify":            (46600_22, Group.base),
        "Mario Raceway 1st":                (46600_23, Group.base),
        "Destroy Mario Sign":               (46600_90, Group.hazard),
    },
    "Wario Stadium": {
        "Wario Stadium Take the Lead":      (46600_24, Group.base),
        "Wario Stadium Qualify":            (46600_25, Group.base),
        "Wario Stadium 1st":                (46600_26, Group.base),
    },
    "Sherbet Land": {
        "Sherbet Land Take the Lead":       (46600_27, Group.base),
        "Sherbet Land Qualify":             (46600_28, Group.base),
        "Sherbet Land 1st":                 (46600_29, Group.base),
        "Spin Baby Penguin":                (46600_91, Group.hazard),
        "Spin Adult Penguin":               (46600_92, Group.hazard),
        "Giant Penguin's Secret":           (4660_441, Group.omit),  # Not in the game yet
    },
    "Royal Raceway": {
        "Royal Raceway Take the Lead":      (46600_30, Group.base),
        "Royal Raceway Qualify":            (46600_31, Group.base),
        "Royal Raceway 1st":                (46600_32, Group.base),
        "Peach's Castle Secret":            (4660_442, Group.secret),
        "Peach's Castle Trail Secret":      (4660_443, Group.secret),
        "Peach's Castle Moat Ramp Secret":  (4660_444, Group.secret),
    },
    "Bowser's Castle": {
        "Bowser's Castle Take the Lead":    (46600_33, Group.base),
        "Bowser's Castle Qualify":          (46600_34, Group.base),
        "Bowser's Castle 1st":              (46600_35, Group.base),
        "Destroy Bush":                     (46600_93, Group.hazard),
        "Destroy Thwomp":                   (46600_94, Group.hazard),
        "Marty's Secret":                   (4660_445, Group.secret),  # Needs Green Switch or Feather
    },
    "D.K.'s Jungle Parkway": {
        "D.K.'s Jungle Parkway Take the Lead": (46600_36, Group.base),
        "D.K.'s Jungle Parkway Qualify":    (46600_37, Group.base),
        "D.K.'s Jungle Parkway 1st":        (46600_38, Group.base),
        "Deflect Kiwano Fruit":             (46600_95, Group.hazard),
        "D.K.'s Jungle Parkway Secret":     (4660_446, Group.secret),
    },
    "Yoshi Valley": {
        "Yoshi Valley Take the Lead":       (46600_39, Group.base),
        "Yoshi Valley Qualify":             (46600_40, Group.base),
        "Yoshi Valley 1st":                 (46600_41, Group.base),
        "Defeat Giant Yoshi Egg":           (46600_96, Group.hazard),
    },
    "Banshee Boardwalk": {
        "Banshee Boardwalk Take the Lead":  (46600_42, Group.base),
        "Banshee Boardwalk Qualify":        (46600_43, Group.base),
        "Banshee Boardwalk 1st":            (46600_44, Group.base),
        "Banshee Boardwalk Secret":         (4660_447, Group.secret),
    },
    "Rainbow Road": {
        "Rainbow Road Take the Lead":       (46600_45, Group.base),
        "Rainbow Road Qualify":             (46600_46, Group.base),
        "Rainbow Road 1st":                 (46600_47, Group.base),
    },
}

#   Region/Location:          (location id, entrances from course region indices) }
shared_hazard_locations = {
    "Destroy Tree":           (46600_84, (0, 2, 5, 7, 10, 12, 13)),
    "Destroy Piranha Plant":  (46600_89, (7, 10)),
}


class SpotData:
    def __init__(self, name, code, access=None):
        self.name = name
        self.code = code
        self.access = access


# Region ( Item Cluster {         (Location, location id, [items logically used to reach]) } )
item_cluster_locations = [
    [
        [
            SpotData("Luigi Raceway Items 1 Spot 1", 46600_99),
            SpotData("Luigi Raceway Items 1 Spot 2", 4660_100),
            SpotData("Luigi Raceway Items 1 Spot 3", 4660_101),
            SpotData("Luigi Raceway Items 1 Spot 4", 4660_102),
            SpotData("Luigi Raceway Items 1 Spot 5", 4660_103),
            SpotData("Luigi Raceway Items 1 Spot 6", 4660_104),
        ], [
            SpotData("Luigi Raceway Items 2 Spot 1", 4660_105),
            SpotData("Luigi Raceway Items 2 Spot 2", 4660_106),
            SpotData("Luigi Raceway Items 2 Spot 3", 4660_107),
            SpotData("Luigi Raceway Items 2 Spot 4", 4660_108),
            SpotData("Luigi Raceway Items 2 Spot 5", 4660_109, ["Green Switch", "Feather Power", "P2 Feather Power"]),
            SpotData("Luigi Raceway Items 2 Spot 6", 4660_110, ["Green Switch", "Feather Power", "P2 Feather Power"]),
        ], [
            SpotData("Luigi Raceway Items 3 Spot 1", 4660_111, ["Blue Switch", "Feather Power", "P2 Feather Power"]),
            SpotData("Luigi Raceway Items 3 Spot 2", 4660_112),
            SpotData("Luigi Raceway Items 3 Spot 3", 4660_113),
            SpotData("Luigi Raceway Items 3 Spot 4", 4660_114),
            SpotData("Luigi Raceway Items 3 Spot 5", 4660_115),
            SpotData("Luigi Raceway Items 3 Spot 6", 4660_116),
        ],
    ], [
        [
           SpotData("Moo Moo Farm Items 1 Spot 1", 4660_117),
           SpotData("Moo Moo Farm Items 1 Spot 2", 4660_118),
           SpotData("Moo Moo Farm Items 1 Spot 3", 4660_119),
           SpotData("Moo Moo Farm Items 1 Spot 4", 4660_120),
           SpotData("Moo Moo Farm Items 1 Spot 5", 4660_121),
           SpotData("Moo Moo Farm Items 1 Spot 6", 4660_122),
        ], [
           SpotData("Moo Moo Farm Items 2 Spot 1", 4660_123),
           SpotData("Moo Moo Farm Items 2 Spot 2", 4660_124),
           SpotData("Moo Moo Farm Items 2 Spot 3", 4660_125),
           SpotData("Moo Moo Farm Items 2 Spot 4", 4660_126, ["Red Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Moo Moo Farm Items 2 Spot 5", 4660_127, ["Red Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Moo Moo Farm Items 2 Spot 6", 4660_128, ["Red Switch", "Feather Power", "P2 Feather Power"]),
        ], [
           SpotData("Moo Moo Farm Items 3 Spot 1", 4660_129),
           SpotData("Moo Moo Farm Items 3 Spot 2", 4660_130),
           SpotData("Moo Moo Farm Items 3 Spot 3", 4660_131),
           SpotData("Moo Moo Farm Items 3 Spot 4", 4660_132, ["Yellow Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Moo Moo Farm Items 3 Spot 5", 4660_133),
           SpotData("Moo Moo Farm Items 3 Spot 6", 4660_134),
           SpotData("Moo Moo Farm Items 3 Spot 7", 4660_135),
        ], [
           SpotData("Moo Moo Farm Items 4 Spot 1", 4660_136),
           SpotData("Moo Moo Farm Items 4 Spot 2", 4660_137),
           SpotData("Moo Moo Farm Items 4 Spot 3", 4660_138),
           SpotData("Moo Moo Farm Items 4 Spot 4", 4660_139),
           SpotData("Moo Moo Farm Items 4 Spot 5", 4660_140),
           SpotData("Moo Moo Farm Items 4 Spot 6", 4660_141),
           SpotData("Moo Moo Farm Items 4 Spot 7", 4660_142),
        ],
    ], [
        [
           SpotData("Koopa Troopa Beach Items 1 Spot 1", 4660_143),
           SpotData("Koopa Troopa Beach Items 1 Spot 2", 4660_144),
           SpotData("Koopa Troopa Beach Items 1 Spot 3", 4660_145),
           SpotData("Koopa Troopa Beach Items 1 Spot 4", 4660_146),
           SpotData("Koopa Troopa Beach Items 1 Spot 5", 4660_147),
           SpotData("Koopa Troopa Beach Items 1 Spot 6", 4660_148),
        ], [
           SpotData("Koopa Troopa Beach Items 2 Spot 1", 4660_149),
           SpotData("Koopa Troopa Beach Items 2 Spot 2", 4660_150),
           SpotData("Koopa Troopa Beach Items 2 Spot 3", 4660_151),
           SpotData("Koopa Troopa Beach Items 2 Spot 4", 4660_152),
           SpotData("Koopa Troopa Beach Items 2 Spot 5", 4660_153),
           SpotData("Koopa Troopa Beach Items 2 Spot 6", 4660_154),
        ], [
           SpotData("Koopa Troopa Beach Items 3 Spot 1", 4660_155, ["Green Switch", "Feather Power", "P2 Feather Power", "Fake Item Box Power", "P2 Fake Item Box Power"]),
           SpotData("Koopa Troopa Beach Items 3 Spot 2", 4660_156, ["Green Switch", "Blue Switch", "Feather Power", "P2 Feather Power", "Fake Item Box Power", "P2 Fake Item Box Power"]),
           SpotData("Koopa Troopa Beach Items 3 Spot 3", 4660_157, ["Green Switch", "Blue Switch", "Feather Power", "P2 Feather Power", "Fake Item Box Power", "P2 Fake Item Box Power"]),
        ], [
           SpotData("Koopa Troopa Beach Items 4 Spot 1", 4660_158),
           SpotData("Koopa Troopa Beach Items 4 Spot 2", 4660_159),
           SpotData("Koopa Troopa Beach Items 4 Spot 3", 4660_160),
           SpotData("Koopa Troopa Beach Items 4 Spot 4", 4660_161),
           SpotData("Koopa Troopa Beach Items 4 Spot 5", 4660_162),
           SpotData("Koopa Troopa Beach Items 4 Spot 6", 4660_163),
        ], [
           SpotData("Koopa Troopa Beach Items 5 Spot 1", 4660_164),
           SpotData("Koopa Troopa Beach Items 5 Spot 2", 4660_165),
           SpotData("Koopa Troopa Beach Items 5 Spot 3", 4660_166),
           SpotData("Koopa Troopa Beach Items 5 Spot 4", 4660_167),
           SpotData("Koopa Troopa Beach Items 5 Spot 5", 4660_168),
           SpotData("Koopa Troopa Beach Items 5 Spot 6", 4660_169),
        ], [
           SpotData("Koopa Troopa Beach Items 6 Spot 1", 4660_170, ["Yellow Switch", "Red Switch", "Green Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Koopa Troopa Beach Items 6 Spot 2", 4660_171, ["Yellow Switch", "Red Switch", "Green Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Koopa Troopa Beach Items 6 Spot 3", 4660_172, ["Yellow Switch", "Red Switch", "Green Switch", "Feather Power", "P2 Feather Power"]),
        ],
    ], [
        [
           SpotData("Kalimari Desert Items 1 Spot 1", 4660_173),
           SpotData("Kalimari Desert Items 1 Spot 2", 4660_174),
           SpotData("Kalimari Desert Items 1 Spot 3", 4660_175),
           SpotData("Kalimari Desert Items 1 Spot 4", 4660_176),
           SpotData("Kalimari Desert Items 1 Spot 5", 4660_177),
        ], [
           SpotData("Kalimari Desert Items 2 Spot 1", 4660_178, ["Yellow Switch", "Red Switch", "Blue Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Kalimari Desert Items 2 Spot 2", 4660_179, ["Yellow Switch", "Red Switch", "Blue Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Kalimari Desert Items 2 Spot 3", 4660_180, ["Yellow Switch", "Red Switch", "Blue Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Kalimari Desert Items 2 Spot 4", 4660_181, ["Yellow Switch", "Red Switch", "Blue Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Kalimari Desert Items 2 Spot 5", 4660_182, ["Yellow Switch", "Red Switch", "Blue Switch", "Feather Power", "P2 Feather Power"]),
        ], [
           SpotData("Kalimari Desert Items 3 Spot 1", 4660_183, ["Blue Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Kalimari Desert Items 3 Spot 2", 4660_184, ["Blue Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Kalimari Desert Items 3 Spot 3", 4660_185),
           SpotData("Kalimari Desert Items 3 Spot 4", 4660_186),
           SpotData("Kalimari Desert Items 3 Spot 5", 4660_187, ["Red Switch", "Green Switch", "Feather Power", "P2 Feather Power"]),
        ],
    ], [
        [
           SpotData("Toad's Turnpike Items 1 Spot 1", 4660_188),
           SpotData("Toad's Turnpike Items 1 Spot 2", 4660_189),
           SpotData("Toad's Turnpike Items 1 Spot 3", 4660_190),
           SpotData("Toad's Turnpike Items 1 Spot 4", 4660_191),
        ], [
           SpotData("Toad's Turnpike Items 2 Spot 1", 4660_192, ["Blue Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Toad's Turnpike Items 2 Spot 2", 4660_193, ["Blue Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Toad's Turnpike Items 2 Spot 3", 4660_194, ["Blue Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Toad's Turnpike Items 2 Spot 4", 4660_195, ["Blue Switch", "Feather Power", "P2 Feather Power"]),
        ], [
           SpotData("Toad's Turnpike Items 3 Spot 1", 4660_196),
           SpotData("Toad's Turnpike Items 3 Spot 2", 4660_197),
           SpotData("Toad's Turnpike Items 3 Spot 3", 4660_198),
           SpotData("Toad's Turnpike Items 3 Spot 4", 4660_199),
        ], [
           SpotData("Toad's Turnpike Items 4 Spot 1", 4660_200, ["Red Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Toad's Turnpike Items 4 Spot 2", 4660_201, ["Red Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Toad's Turnpike Items 4 Spot 3", 4660_202, ["Red Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Toad's Turnpike Items 4 Spot 4", 4660_203, ["Red Switch", "Feather Power", "P2 Feather Power"]),
        ],
    ], [
        [
           SpotData("Frappe Snowland Items 1 Spot 1", 4660_204),
           SpotData("Frappe Snowland Items 1 Spot 2", 4660_205),
           SpotData("Frappe Snowland Items 1 Spot 3", 4660_206),
           SpotData("Frappe Snowland Items 1 Spot 4", 4660_207),
           SpotData("Frappe Snowland Items 1 Spot 5", 4660_208),
        ], [
           SpotData("Frappe Snowland Items 2 Spot 1", 4660_209),
           SpotData("Frappe Snowland Items 2 Spot 2", 4660_210),
           SpotData("Frappe Snowland Items 2 Spot 3", 4660_211),
           SpotData("Frappe Snowland Items 2 Spot 4", 4660_212),
           SpotData("Frappe Snowland Items 2 Spot 5", 4660_213),
        ], [
           SpotData("Frappe Snowland Items 3 Spot 1", 4660_214),
           SpotData("Frappe Snowland Items 3 Spot 2", 4660_215),
           SpotData("Frappe Snowland Items 3 Spot 3", 4660_216),
           SpotData("Frappe Snowland Items 3 Spot 4", 4660_217),
           SpotData("Frappe Snowland Items 3 Spot 5", 4660_218),
        ],
    ], [
        [
           SpotData("Choco Mountain Items 1 Spot 1", 4660_219),
           SpotData("Choco Mountain Items 1 Spot 2", 4660_220),
           SpotData("Choco Mountain Items 1 Spot 3", 4660_221),
           SpotData("Choco Mountain Items 1 Spot 4", 4660_222),
           SpotData("Choco Mountain Items 1 Spot 5", 4660_223),
        ], [
           SpotData("Choco Mountain Items 2 Spot 1", 4660_224),
           SpotData("Choco Mountain Items 2 Spot 2", 4660_225),
           SpotData("Choco Mountain Items 2 Spot 3", 4660_226),
           SpotData("Choco Mountain Items 2 Spot 4", 4660_227),
           SpotData("Choco Mountain Items 2 Spot 5", 4660_228),
        ], [
           SpotData("Choco Mountain Items 3 Spot 1", 4660_229),
           SpotData("Choco Mountain Items 3 Spot 2", 4660_230),
           SpotData("Choco Mountain Items 3 Spot 3", 4660_231),
           SpotData("Choco Mountain Items 3 Spot 4", 4660_232),
           SpotData("Choco Mountain Items 3 Spot 5", 4660_233),
        ],
    ], [
        [
           SpotData("Mario Raceway Items 1 Spot 1", 4660_234),
           SpotData("Mario Raceway Items 1 Spot 2", 4660_235),
           SpotData("Mario Raceway Items 1 Spot 3", 4660_236),
           SpotData("Mario Raceway Items 1 Spot 4", 4660_237),
           SpotData("Mario Raceway Items 1 Spot 5", 4660_238),
        ], [
           SpotData("Mario Raceway Items 2 Spot 1", 4660_239),
           SpotData("Mario Raceway Items 2 Spot 2", 4660_240),
           SpotData("Mario Raceway Items 2 Spot 3", 4660_241),
           SpotData("Mario Raceway Items 2 Spot 4", 4660_242),
           SpotData("Mario Raceway Items 2 Spot 5", 4660_243),
        ], [
           SpotData("Mario Raceway Items 3 Spot 1", 4660_244),
           SpotData("Mario Raceway Items 3 Spot 2", 4660_245),
           SpotData("Mario Raceway Items 3 Spot 3", 4660_246),
           SpotData("Mario Raceway Items 3 Spot 4", 4660_247),
           SpotData("Mario Raceway Items 3 Spot 5", 4660_248),
        ],
    ], [
        [
           SpotData("Wario Stadium Items 1 Spot 1", 4660_249),
           SpotData("Wario Stadium Items 1 Spot 2", 4660_250),
           SpotData("Wario Stadium Items 1 Spot 3", 4660_251),
           SpotData("Wario Stadium Items 1 Spot 4", 4660_252),
           SpotData("Wario Stadium Items 1 Spot 5", 4660_253),
        ], [
           SpotData("Wario Stadium Items 2 Spot 1", 4660_254, ["Blue Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Wario Stadium Items 2 Spot 2", 4660_255, ["Blue Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Wario Stadium Items 2 Spot 3", 4660_256, ["Blue Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Wario Stadium Items 2 Spot 4", 4660_257, ["Blue Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Wario Stadium Items 2 Spot 5", 4660_258),
        ], [
           SpotData("Wario Stadium Items 3 Spot 1", 4660_259),
           SpotData("Wario Stadium Items 3 Spot 2", 4660_260),
           SpotData("Wario Stadium Items 3 Spot 3", 4660_261),
           SpotData("Wario Stadium Items 3 Spot 4", 4660_262),
           SpotData("Wario Stadium Items 3 Spot 5", 4660_263),
        ], [
           SpotData("Wario Stadium Items 4 Spot 1", 4660_264),
           SpotData("Wario Stadium Items 4 Spot 2", 4660_265),
           SpotData("Wario Stadium Items 4 Spot 3", 4660_266, ["Yellow Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Wario Stadium Items 4 Spot 4", 4660_267),
           SpotData("Wario Stadium Items 4 Spot 5", 4660_268),
        ], [
           SpotData("Wario Stadium Items 5 Spot 1", 4660_269),
           SpotData("Wario Stadium Items 5 Spot 2", 4660_270),
           SpotData("Wario Stadium Items 5 Spot 3", 4660_271),
           SpotData("Wario Stadium Items 5 Spot 4", 4660_272),
           SpotData("Wario Stadium Items 5 Spot 5", 4660_273),
        ], [
           SpotData("Wario Stadium Items 6 Spot 1", 4660_274),
           SpotData("Wario Stadium Items 6 Spot 2", 4660_275),
           SpotData("Wario Stadium Items 6 Spot 3", 4660_276),
           SpotData("Wario Stadium Items 6 Spot 4", 4660_277),
           SpotData("Wario Stadium Items 6 Spot 5", 4660_278),
        ],
    ], [
        [
           SpotData("Sherbet Land Items 1 Spot 1", 4660_279),
           SpotData("Sherbet Land Items 1 Spot 2", 4660_280, ["Green Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Sherbet Land Items 1 Spot 3", 4660_281, ["Green Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Sherbet Land Items 1 Spot 4", 4660_282, ["Green Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Sherbet Land Items 1 Spot 5", 4660_283, ["Green Switch", "Feather Power", "P2 Feather Power"]),
        ], [
           SpotData("Sherbet Land Items 2 Spot 1", 4660_284, ["Red Switch", "Blue Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Sherbet Land Items 2 Spot 2", 4660_285, ["Red Switch", "Blue Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Sherbet Land Items 2 Spot 3", 4660_286, ["Red Switch", "Blue Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Sherbet Land Items 2 Spot 4", 4660_287, ["Red Switch", "Blue Switch", "Feather Power", "P2 Feather Power"]),
        ], [
           SpotData("Sherbet Land Bypass Spot", 4660_288),
        ], [
           SpotData("Sherbet Land Items 3 Spot 1", 4660_289),
           SpotData("Sherbet Land Items 3 Spot 2", 4660_290),
           SpotData("Sherbet Land Items 3 Spot 3", 4660_291),
           SpotData("Sherbet Land Items 3 Spot 4", 4660_292),
           SpotData("Sherbet Land Items 3 Spot 5", 4660_293),
        ], [
           SpotData("Sherbet Land Items 4 Spot 1", 4660_294),
           SpotData("Sherbet Land Items 4 Spot 2", 4660_295),
           SpotData("Sherbet Land Items 4 Spot 3", 4660_296),
           SpotData("Sherbet Land Items 4 Spot 4", 4660_297),
        ],
    ], [
        [
           SpotData("Royal Raceway Items 1 Spot 1", 4660_298),
           SpotData("Royal Raceway Items 1 Spot 2", 4660_299),
           SpotData("Royal Raceway Items 1 Spot 3", 4660_300),
           SpotData("Royal Raceway Items 1 Spot 4", 4660_301),
           SpotData("Royal Raceway Items 1 Spot 5", 4660_302),
        ], [
           SpotData("Royal Raceway Items 2 Spot 1", 4660_303),
           SpotData("Royal Raceway Items 2 Spot 2", 4660_304),
           SpotData("Royal Raceway Items 2 Spot 3", 4660_305, ["Red Switch"]),
           SpotData("Royal Raceway Items 2 Spot 4", 4660_306),
           SpotData("Royal Raceway Items 2 Spot 5", 4660_307),
        ], [
           SpotData("Royal Raceway Items 3 Spot 1", 4660_308),
           SpotData("Royal Raceway Items 3 Spot 2", 4660_309),
           SpotData("Royal Raceway Items 3 Spot 3", 4660_310),
           SpotData("Royal Raceway Items 3 Spot 4", 4660_311),
           SpotData("Royal Raceway Items 3 Spot 5", 4660_312),
        ], [
           SpotData("Royal Raceway Items 4 Spot 1", 4660_313),
           SpotData("Royal Raceway Items 4 Spot 2", 4660_314),
           SpotData("Royal Raceway Items 4 Spot 3", 4660_315),
           SpotData("Royal Raceway Items 4 Spot 4", 4660_316),
           SpotData("Royal Raceway Items 4 Spot 5", 4660_317),
        ],
    ], [
        [
           SpotData("Bowser's Castle Items 1 Spot 1", 4660_318),
           SpotData("Bowser's Castle Items 1 Spot 2", 4660_319),
           SpotData("Bowser's Castle Items 1 Spot 3", 4660_320),
           SpotData("Bowser's Castle Items 1 Spot 4", 4660_321),
        ], [
           SpotData("Bowser's Castle Items 2 Spot 1", 4660_322),
           SpotData("Bowser's Castle Items 2 Spot 2", 4660_323),
           SpotData("Bowser's Castle Items 2 Spot 3", 4660_324),
           SpotData("Bowser's Castle Items 2 Spot 4", 4660_325),
        ], [
           SpotData("Bowser's Castle Items 3 Spot 1", 4660_326, ["Red Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Bowser's Castle Items 3 Spot 2", 4660_327),
           SpotData("Bowser's Castle Items 3 Spot 3", 4660_328, ["Red Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Bowser's Castle Items 3 Spot 4", 4660_329, ["Yellow Switch", "Feather Power", "P2 Feather Power"]),
        ],
    ], [
        [
           SpotData("D.K.'s Jungle Parkway Items 1 Spot 1", 4660_330),
           SpotData("D.K.'s Jungle Parkway Items 1 Spot 2", 4660_331, ["Green Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("D.K.'s Jungle Parkway Items 1 Spot 3", 4660_332, ["Green Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("D.K.'s Jungle Parkway Items 1 Spot 4", 4660_333, ["Green Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("D.K.'s Jungle Parkway Items 1 Spot 5", 4660_334, ["Green Switch", "Feather Power", "P2 Feather Power"]),
        ], [
           SpotData("D.K.'s Jungle Parkway Items 2 Spot 1", 4660_335),
           SpotData("D.K.'s Jungle Parkway Items 2 Spot 2", 4660_336),
           SpotData("D.K.'s Jungle Parkway Items 2 Spot 3", 4660_337),
           SpotData("D.K.'s Jungle Parkway Items 2 Spot 4", 4660_338),
        ], [
           SpotData("D.K.'s Jungle Parkway Items 3 Spot 1", 4660_339),
           SpotData("D.K.'s Jungle Parkway Items 3 Spot 2", 4660_340, ["Red Switch", "Feather Power", "P2 Feather Power"]),  # Can reach with skilled use of fruit bonk
           SpotData("D.K.'s Jungle Parkway Items 3 Spot 3", 4660_341, ["Red Switch", "Feather Power", "P2 Feather Power"]),  # Can reach with skilled use of fruit bonk
           SpotData("D.K.'s Jungle Parkway Items 3 Spot 4", 4660_342),
        ], [
           SpotData("D.K.'s Jungle Parkway Items 4 Spot 1", 4660_343),
           SpotData("D.K.'s Jungle Parkway Items 4 Spot 2", 4660_344),
           SpotData("D.K.'s Jungle Parkway Items 4 Spot 3", 4660_345),
           SpotData("D.K.'s Jungle Parkway Items 4 Spot 4", 4660_346),
        ], [
           SpotData("D.K.'s Jungle Parkway Items 5 Spot 1", 4660_347),
           SpotData("D.K.'s Jungle Parkway Items 5 Spot 2", 4660_348),
           SpotData("D.K.'s Jungle Parkway Items 5 Spot 3", 4660_349),
           SpotData("D.K.'s Jungle Parkway Items 5 Spot 4", 4660_350),
           SpotData("D.K.'s Jungle Parkway Items 5 Spot 5", 4660_351),
        ],
    ], [
        [
           SpotData("Yoshi Valley Field Items Spot 1", 4660_352),
           SpotData("Yoshi Valley Field Items Spot 2", 4660_353),
           SpotData("Yoshi Valley Field Items Spot 3", 4660_354),
           SpotData("Yoshi Valley Field Items Spot 4", 4660_355),
        ], [
           SpotData("Yoshi Valley Maze Entry Items Spot 1", 4660_356),
           SpotData("Yoshi Valley Maze Entry Items Spot 2", 4660_357),
           SpotData("Yoshi Valley Maze Entry Items Spot 3", 4660_358),
           SpotData("Yoshi Valley Maze Entry Items Spot 4", 4660_359),
        ], [
           SpotData("Yoshi Valley Maze Bridge Items Spot 1", 4660_360, ["Green Switch", "Blue Switch", "Feather Power", "P2 Feather Power"]),  # Can reach with skilled use of Mushroom, etc if the Maze Railing is still down
           SpotData("Yoshi Valley Maze Bridge Items Spot 2", 4660_361, ["Green Switch", "Blue Switch", "Feather Power", "P2 Feather Power"]),  # Can reach with skilled use of Mushroom, etc if the Maze Railing is still down
           SpotData("Yoshi Valley Maze Bridge Items Spot 3", 4660_362, ["Green Switch", "Blue Switch", "Feather Power", "P2 Feather Power"]),  # Can reach with skilled use of Mushroom, etc if the Maze Railing is still down
           SpotData("Yoshi Valley Maze Bridge Items Spot 4", 4660_363, ["Green Switch", "Blue Switch", "Feather Power", "P2 Feather Power"]),  # Can reach with skilled use of Mushroom, etc if the Maze Railing is still down
           SpotData("Yoshi Valley Maze Bridge Items Spot 5", 4660_364, ["Green Switch", "Blue Switch", "Feather Power", "P2 Feather Power"]),  # Can reach with skilled use of Mushroom, etc if the Maze Railing is still down
        ], [
           SpotData("Yoshi Valley Rightmost Items Spot 1", 4660_365, ["Yellow Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Yoshi Valley Rightmost Items Spot 2", 4660_366, ["Yellow Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Yoshi Valley Rightmost Items Spot 3", 4660_367, ["Yellow Switch", "Blue Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Yoshi Valley Rightmost Items Spot 4", 4660_368, ["Yellow Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Yoshi Valley Rightmost Items Spot 5", 4660_369, ["Blue Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Yoshi Valley Rightmost Items Spot 6", 4660_370, ["Blue Switch", "Feather Power", "P2 Feather Power"]),
        ], [
           SpotData("Yoshi Valley Left Fork Items Spot 1", 4660_371),
           SpotData("Yoshi Valley Left Fork Items Spot 2", 4660_372),
           SpotData("Yoshi Valley Left Fork Items Spot 3", 4660_373),
           SpotData("Yoshi Valley Left Fork Items Spot 4", 4660_374),
        ], [
           SpotData("Yoshi Valley Left Ledge Items Spot 1", 4660_375),
           SpotData("Yoshi Valley Left Ledge Items Spot 2", 4660_376),
           SpotData("Yoshi Valley Left Ledge Items Spot 3", 4660_377),
           SpotData("Yoshi Valley Left Ledge Items Spot 4", 4660_378),
        ], [
           SpotData("Yoshi Valley Hairpin Turn Items Spot 1", 4660_379),
           SpotData("Yoshi Valley Hairpin Turn Items Spot 2", 4660_380),
           SpotData("Yoshi Valley Hairpin Turn Items Spot 3", 4660_381),
           SpotData("Yoshi Valley Hairpin Turn Items Spot 4", 4660_382),
        ], [
           SpotData("Yoshi Valley Giant Egg Items Spot 1", 4660_383),
           SpotData("Yoshi Valley Giant Egg Items Spot 2", 4660_384),
           SpotData("Yoshi Valley Giant Egg Items Spot 3", 4660_385, ["Green Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Yoshi Valley Giant Egg Items Spot 4", 4660_386, ["Green Switch", "Feather Power", "P2 Feather Power"]),
           SpotData("Yoshi Valley Giant Egg Items Spot 5", 4660_387),
           SpotData("Yoshi Valley Giant Egg Items Spot 6", 4660_388),
        ],
    ], [
        [
           SpotData("Banshee Boardwalk Items 1 Spot 1", 4660_389),
           SpotData("Banshee Boardwalk Items 1 Spot 2", 4660_390),
           SpotData("Banshee Boardwalk Items 1 Spot 3", 4660_391),
           SpotData("Banshee Boardwalk Items 1 Spot 4", 4660_392),
        ], [
           SpotData("Banshee Boardwalk Items 2 Spot 1", 4660_393),
           SpotData("Banshee Boardwalk Items 2 Spot 2", 4660_394),
           SpotData("Banshee Boardwalk Items 2 Spot 3", 4660_395),
           SpotData("Banshee Boardwalk Items 2 Spot 4", 4660_396),
        ], [
           SpotData("Banshee Boardwalk Items 3 Spot 1", 4660_397),
           SpotData("Banshee Boardwalk Items 3 Spot 2", 4660_398),
           SpotData("Banshee Boardwalk Items 3 Spot 3", 4660_399),
           SpotData("Banshee Boardwalk Items 3 Spot 4", 4660_400),
        ], [
           SpotData("Banshee Boardwalk Items 4 Spot 1", 4660_401),
           SpotData("Banshee Boardwalk Items 4 Spot 2", 4660_402),
           SpotData("Banshee Boardwalk Items 4 Spot 3", 4660_403),
           SpotData("Banshee Boardwalk Items 4 Spot 4", 4660_404),
        ],
    ], [
        [
           SpotData("Rainbow Road Items 1 Spot 1", 4660_405),
           SpotData("Rainbow Road Items 1 Spot 2", 4660_406),
           SpotData("Rainbow Road Items 1 Spot 3", 4660_407),
           SpotData("Rainbow Road Items 1 Spot 4", 4660_408),
        ], [
           SpotData("Rainbow Road Items 2 Spot 1", 4660_409),
           SpotData("Rainbow Road Items 2 Spot 2", 4660_410),
           SpotData("Rainbow Road Items 2 Spot 3", 4660_411),
           SpotData("Rainbow Road Items 2 Spot 4", 4660_412),
        ], [
           SpotData("Rainbow Road Items 3 Spot 1", 4660_413),
           SpotData("Rainbow Road Items 3 Spot 2", 4660_414),
           SpotData("Rainbow Road Items 3 Spot 3", 4660_415),
           SpotData("Rainbow Road Items 3 Spot 4", 4660_416),
        ], [
           SpotData("Rainbow Road Items 4 Spot 1", 4660_417),
           SpotData("Rainbow Road Items 4 Spot 2", 4660_418),
           SpotData("Rainbow Road Items 4 Spot 3", 4660_419),
           SpotData("Rainbow Road Items 4 Spot 4", 4660_420),
        ], [
           SpotData("Rainbow Road Items 5 Spot 1", 4660_421),
           SpotData("Rainbow Road Items 5 Spot 2", 4660_422),
           SpotData("Rainbow Road Items 5 Spot 3", 4660_423),
           SpotData("Rainbow Road Items 5 Spot 4", 4660_424),
        ], [
           SpotData("Rainbow Road Items 6 Spot 1", 4660_425),
           SpotData("Rainbow Road Items 6 Spot 2", 4660_426),
           SpotData("Rainbow Road Items 6 Spot 3", 4660_427),
           SpotData("Rainbow Road Items 6 Spot 4", 4660_428),
        ], [
           SpotData("Rainbow Road Items 7 Spot 1", 4660_429),
           SpotData("Rainbow Road Items 7 Spot 2", 4660_430),
           SpotData("Rainbow Road Items 7 Spot 3", 4660_431),
           SpotData("Rainbow Road Items 7 Spot 4", 4660_432),
        ], [
           SpotData("Rainbow Road Items 8 Spot 1", 4660_433),
           SpotData("Rainbow Road Items 8 Spot 2", 4660_434),
           SpotData("Rainbow Road Items 8 Spot 3", 4660_435),
           SpotData("Rainbow Road Items 8 Spot 4", 4660_436),
        ],
    ],
]

#   Region: (Location,             location id, option filter)
cup_locations = {
    "Mushroom Cup Trophy Ceremony": [
        ("Mushroom Cup Bronze",       46600_48, 0b0011),
        ("Mushroom Cup Silver",       46600_49, 0b0001),
        ("Mushroom Cup Gold",         46600_50, 0b0001),
        ("Mushroom Cup 100cc Bronze", 46600_51, 0b1000),
        ("Mushroom Cup 100cc Silver", 46600_52, 0b0010),
        ("Mushroom Cup 100cc Gold",   46600_53, 0b0100),
        ("Mushroom Cup 150cc Bronze", 46600_54, 0b1000),
        ("Mushroom Cup 150cc Silver", 46600_55, 0b1000),
        ("Mushroom Cup 150cc Gold",   46600_56, 0b0110),
    ],
    "Flower Cup Trophy Ceremony": [
        ("Flower Cup Bronze",       46600_57, 0b0011),
        ("Flower Cup Silver",       46600_58, 0b0001),
        ("Flower Cup Gold",         46600_59, 0b0001),
        ("Flower Cup 100cc Bronze", 46600_60, 0b1000),
        ("Flower Cup 100cc Silver", 46600_61, 0b0010),
        ("Flower Cup 100cc Gold",   46600_62, 0b0100),
        ("Flower Cup 150cc Bronze", 46600_63, 0b1000),
        ("Flower Cup 150cc Silver", 46600_64, 0b1000),
        ("Flower Cup 150cc Gold",   46600_65, 0b0110),
    ],
    "Star Cup Trophy Ceremony": [
        ("Star Cup Bronze",       46600_66, 0b0011),
        ("Star Cup Silver",       46600_67, 0b0001),
        ("Star Cup Gold",         46600_68, 0b0001),
        ("Star Cup 100cc Bronze", 46600_69, 0b1000),
        ("Star Cup 100cc Silver", 46600_70, 0b0010),
        ("Star Cup 100cc Gold",   46600_71, 0b0100),
        ("Star Cup 150cc Bronze", 46600_72, 0b1000),
        ("Star Cup 150cc Silver", 46600_73, 0b1000),
        ("Star Cup 150cc Gold",   46600_74, 0b0110),
    ],
    "Special Cup Trophy Ceremony": [
        ("Special Cup Bronze",       46600_75, 0b0011),
        ("Special Cup Silver",       46600_76, 0b0001),
        ("Special Cup Gold",         46600_77, 0b0001),
        ("Special Cup 100cc Bronze", 46600_78, 0b1000),
        ("Special Cup 100cc Silver", 46600_79, 0b0010),
        ("Special Cup 100cc Gold",   46600_80, 0b0100),
        ("Special Cup 150cc Bronze", 46600_81, 0b1000),
        ("Special Cup 150cc Silver", 46600_82, 0b1000),
        ("Special Cup 150cc Gold",   46600_83, 0b0110),
    ]
}

location_name_to_id = (
    {name: code for r in course_locations.values() for name, (code, _) in r.items()} |
    {name: code for name, (code, _) in shared_hazard_locations.items()} |
    {spot.name: spot.code for r in item_cluster_locations for c in r for spot in c} |
    {name: code for r in cup_locations.values() for name, code, _ in r}
)
