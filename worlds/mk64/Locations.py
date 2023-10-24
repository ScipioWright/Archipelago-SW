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


# Mappings of each Region to dictionary of location data
# 4660000 - 4660583

#   Region: { Location:                    (location id, Group) }
course_locations = {
    "Luigi Raceway": {
        "Lead Luigi Raceway":              (466000_0, Group.base),
        "Qualify Luigi Raceway":           (466000_1, Group.base),
        "Win Luigi Raceway":               (466000_2, Group.base),
        "Luigi Raceway Balloon":           (4660_108, Group.blue_shell_item_spot),
    },
    "Moo Moo Farm": {
        "Lead Moo Moo Farm":               (466000_3, Group.base),
        "Qualify Moo Moo Farm":            (466000_4, Group.base),
        "Win Moo Moo Farm":                (466000_5, Group.base),
        "Defeat Chubby":                   (46600_97, Group.hazard),
    },
    "Koopa Troopa Beach": {
        "Lead Koopa Troopa Beach":         (466000_6, Group.base),
        "Qualify Koopa Troopa Beach":      (466000_7, Group.base),
        "Win Koopa Troopa Beach":          (466000_8, Group.base),
        "Koopa Troopa Beach Secret":       (4660_574, Group.secret),
        "Koopa Troopa Beach Rock":         (4660_109, Group.blue_shell_item_spot),
    },
    "Kalimari Desert": {
        "Lead Kalimari Desert":            (466000_9, Group.base),
        "Qualify Kalimari Desert":         (46600_10, Group.base),
        "Win Kalimari Desert":             (46600_11, Group.base),
        "Destroy Cactus":                  (46600_98, Group.hazard),
        "Kalimari Desert Secret":          (4660_575, Group.secret),
    },
    "Toad's Turnpike": {
        "Lead Toad's Turnpike":            (46600_12, Group.base),
        "Qualify Toad's Turnpike":         (46600_13, Group.base),
        "Win Toad's Turnpike":             (46600_14, Group.base),
        "Toads Turnpike Secret":           (4660_576, Group.secret),
    },
    "Frappe Snowland": {
        "Lead Frappe Snowland":            (46600_15, Group.base),
        "Qualify Frappe Snowland":         (46600_16, Group.base),
        "Win Frappe Snowland":             (46600_17, Group.base),
        "Defeat Snowman Bomb":             (46600_99, Group.hazard),
        "Snow Yoshi's Secret":             (4660_577, Group.secret),
    },
    "Choco Mountain": {
        "Lead Choco Mountain":             (46600_18, Group.base),
        "Qualify Choco Mountain":          (46600_19, Group.base),
        "Win Choco Mountain":              (46600_20, Group.base),
        # "Deflect Boulder":               (4660_100, Group.hazard),  omit because this hazard sucks (bad gameplay)
    },
    "Mario Raceway": {
        "Lead Mario Raceway":              (46600_21, Group.base),
        "Qualify Mario Raceway":           (46600_22, Group.base),
        "Win Mario Raceway":               (46600_23, Group.base),
        "Destroy Mario Sign":              (4660_102, Group.hazard),
    },
    "Wario Stadium": {
        "Lead Wario Stadium":              (46600_24, Group.base),
        "Qualify Wario Stadium":           (46600_25, Group.base),
        "Win Wario Stadium":               (46600_26, Group.base),
    },
    "Sherbet Land": {
        "Lead Sherbet Land":               (46600_27, Group.base),
        "Qualify Sherbet Land":            (46600_28, Group.base),
        "Win Sherbet Land":                (46600_29, Group.base),
        "Spin Baby Penguin":               (4660_103, Group.hazard),
        "Spin Adult Penguin":              (4660_104, Group.hazard),
    },
    "Royal Raceway": {
        "Lead Royal Raceway":              (46600_30, Group.base),
        "Qualify Royal Raceway":           (46600_31, Group.base),
        "Win Royal Raceway":               (46600_32, Group.base),
        "Peach's Castle Secret":           (4660_578, Group.secret),
        "Peach's Castle Trail Secret":     (4660_579, Group.secret),
        "Peach's Castle Moat Ramp Secret": (4660_580, Group.secret),
    },
    "Bowser's Castle": {
        "Lead Bowser's Castle":            (46600_33, Group.base),
        "Qualify Bowser's Castle":         (46600_34, Group.base),
        "Win Bowser's Castle":             (46600_35, Group.base),
        "Destroy Bush":                    (4660_105, Group.hazard),
        "Destroy Thwomp":                  (4660_106, Group.hazard),
        "Marty's Secret":                  (4660_581, Group.secret),
    },
    "D.K.'s Jungle Parkway": {
        "Lead D.K.'s Jungle Parkway":      (46600_36, Group.base),
        "Qualify D.K.'s Jungle Parkway":   (46600_37, Group.base),
        "Win D.K.'s Jungle Parkway":       (46600_38, Group.base),
        "D.K.'s Jungle Parkway Secret":    (4660_582, Group.secret),
    },
    "Yoshi Valley": {
        "Lead Yoshi Valley":               (46600_39, Group.base),
        "Qualify Yoshi Valley":            (46600_40, Group.base),
        "Win Yoshi Valley":                (46600_41, Group.base),
        "Defeat Giant Yoshi Egg":          (4660_107, Group.hazard),
    },
    "Banshee Boardwalk": {
        "Lead Banshee Boardwalk":          (46600_42, Group.base),
        "Qualify Banshee Boardwalk":       (46600_43, Group.base),
        "Win Banshee Boardwalk":           (46600_44, Group.base),
        "Banshee Boardwalk Secret":        (4660_583, Group.secret),
    },
    "Rainbow Road": {
        "Lead Rainbow Road":               (46600_45, Group.base),
        "Qualify Rainbow Road":            (46600_46, Group.base),
        "Win Rainbow Road":                (46600_47, Group.base),
    },
}

#   Region/Location:          (location id, entrances from course region indices) }
shared_hazard_locations = {
    "Destroy Tree":           (46600_96, (0, 2, 5, 7, 10, 12, 13)),
    "Destroy Piranha Plant":  (4660_101, (7, 10)),
}

# Region ( Item Cluster {         Location: location id } )
item_cluster_locations = (
    (
        {
            "Luigi Raceway Items 1 Spot 1": 4660_110,
            "Luigi Raceway Items 1 Spot 2": 4660_111,
            "Luigi Raceway Items 1 Spot 3": 4660_112,
            "Luigi Raceway Items 1 Spot 4": 4660_113,
            "Luigi Raceway Items 1 Spot 5": 4660_114,
            "Luigi Raceway Items 1 Spot 6": 4660_115,
        }, {
            "Luigi Raceway Items 2 Spot 1": 4660_116,
            "Luigi Raceway Items 2 Spot 2": 4660_117,
            "Luigi Raceway Items 2 Spot 3": 4660_118,
            "Luigi Raceway Items 2 Spot 4": 4660_119,
            "Luigi Raceway Items 2 Spot 5": 4660_120,
            "Luigi Raceway Items 2 Spot 6": 4660_121,
        }, {
            "Luigi Raceway Items 3 Spot 1": 4660_122,
            "Luigi Raceway Items 3 Spot 2": 4660_123,
            "Luigi Raceway Items 3 Spot 3": 4660_124,
            "Luigi Raceway Items 3 Spot 4": 4660_125,
            "Luigi Raceway Items 3 Spot 5": 4660_126,
            "Luigi Raceway Items 3 Spot 6": 4660_127,
        },
    ), (
        {
            "Moo Moo Farm Items 1 Spot 1": 4660_128,
            "Moo Moo Farm Items 1 Spot 2": 4660_129,
            "Moo Moo Farm Items 1 Spot 3": 4660_130,
            "Moo Moo Farm Items 1 Spot 4": 4660_131,
            "Moo Moo Farm Items 1 Spot 5": 4660_132,
            "Moo Moo Farm Items 1 Spot 6": 4660_133,
        }, {
            "Moo Moo Farm Items 2 Spot 1": 4660_134,
            "Moo Moo Farm Items 2 Spot 2": 4660_135,
            "Moo Moo Farm Items 2 Spot 3": 4660_136,
            "Moo Moo Farm Items 2 Spot 4": 4660_137,
            "Moo Moo Farm Items 2 Spot 5": 4660_138,
            "Moo Moo Farm Items 2 Spot 6": 4660_139,
        }, {
            "Moo Moo Farm Items 3 Spot 1": 4660_140,
            "Moo Moo Farm Items 3 Spot 2": 4660_141,
            "Moo Moo Farm Items 3 Spot 3": 4660_142,
            "Moo Moo Farm Items 3 Spot 4": 4660_143,
            "Moo Moo Farm Items 3 Spot 5": 4660_144,
            "Moo Moo Farm Items 3 Spot 6": 4660_145,
            "Moo Moo Farm Items 3 Spot 7": 4660_146,
        }, {
            "Moo Moo Farm Items 4 Spot 1": 4660_147,
            "Moo Moo Farm Items 4 Spot 2": 4660_148,
            "Moo Moo Farm Items 4 Spot 3": 4660_149,
            "Moo Moo Farm Items 4 Spot 4": 4660_150,
            "Moo Moo Farm Items 4 Spot 5": 4660_151,
            "Moo Moo Farm Items 4 Spot 6": 4660_152,
            "Moo Moo Farm Items 4 Spot 7": 4660_153,
        },
    ), (
        {
            "Koopa Troopa Beach Items 1 Spot 1": 4660_154,
            "Koopa Troopa Beach Items 1 Spot 2": 4660_155,
            "Koopa Troopa Beach Items 1 Spot 3": 4660_156,
            "Koopa Troopa Beach Items 1 Spot 4": 4660_157,
            "Koopa Troopa Beach Items 1 Spot 5": 4660_158,
            "Koopa Troopa Beach Items 1 Spot 6": 4660_159,
        }, {
            "Koopa Troopa Beach Items 2 Spot 1": 4660_160,
            "Koopa Troopa Beach Items 2 Spot 2": 4660_161,
            "Koopa Troopa Beach Items 2 Spot 3": 4660_162,
            "Koopa Troopa Beach Items 2 Spot 4": 4660_163,
            "Koopa Troopa Beach Items 2 Spot 5": 4660_164,
            "Koopa Troopa Beach Items 2 Spot 6": 4660_165,
        }, {
            "Koopa Troopa Beach Items 3 Spot 1": 4660_166,
            "Koopa Troopa Beach Items 3 Spot 2": 4660_167,
            "Koopa Troopa Beach Items 3 Spot 3": 4660_168,
        }, {
            "Koopa Troopa Beach Items 4 Spot 1": 4660_169,
            "Koopa Troopa Beach Items 4 Spot 2": 4660_170,
            "Koopa Troopa Beach Items 4 Spot 3": 4660_171,
            "Koopa Troopa Beach Items 4 Spot 4": 4660_172,
            "Koopa Troopa Beach Items 4 Spot 5": 4660_173,
            "Koopa Troopa Beach Items 4 Spot 6": 4660_174,
        }, {
            "Koopa Troopa Beach Items 5 Spot 1": 4660_175,
            "Koopa Troopa Beach Items 5 Spot 2": 4660_176,
            "Koopa Troopa Beach Items 5 Spot 3": 4660_177,
            "Koopa Troopa Beach Items 5 Spot 4": 4660_178,
            "Koopa Troopa Beach Items 5 Spot 5": 4660_179,
            "Koopa Troopa Beach Items 5 Spot 6": 4660_180,
        }, {
            "Koopa Troopa Beach Items 6 Spot 1": 4660_181,
            "Koopa Troopa Beach Items 6 Spot 2": 4660_182,
            "Koopa Troopa Beach Items 6 Spot 3": 4660_183,
        },
    ), (
        {
            "Kalimari Desert Items 1 Spot 1": 4660_184,
            "Kalimari Desert Items 1 Spot 2": 4660_185,
            "Kalimari Desert Items 1 Spot 3": 4660_186,
            "Kalimari Desert Items 1 Spot 4": 4660_187,
            "Kalimari Desert Items 1 Spot 5": 4660_188,
        }, {
            "Kalimari Desert Items 2 Spot 1": 4660_189,
            "Kalimari Desert Items 2 Spot 2": 4660_190,
            "Kalimari Desert Items 2 Spot 3": 4660_191,
            "Kalimari Desert Items 2 Spot 4": 4660_192,
            "Kalimari Desert Items 2 Spot 5": 4660_193,
        }, {
            "Kalimari Desert Items 3 Spot 1": 4660_194,
            "Kalimari Desert Items 3 Spot 2": 4660_195,
            "Kalimari Desert Items 3 Spot 3": 4660_196,
            "Kalimari Desert Items 3 Spot 4": 4660_197,
            "Kalimari Desert Items 3 Spot 5": 4660_198,
        },
    ), (
        {
            "Toad's Turnpike Items 1 Spot 1": 4660_199,
            "Toad's Turnpike Items 1 Spot 2": 4660_200,
            "Toad's Turnpike Items 1 Spot 3": 4660_201,
            "Toad's Turnpike Items 1 Spot 4": 4660_202,
        }, {
            "Toad's Turnpike Items 2 Spot 1": 4660_203,
            "Toad's Turnpike Items 2 Spot 2": 4660_204,
            "Toad's Turnpike Items 2 Spot 3": 4660_205,
            "Toad's Turnpike Items 2 Spot 4": 4660_206,
        }, {
            "Toad's Turnpike Items 3 Spot 1": 4660_207,
            "Toad's Turnpike Items 3 Spot 2": 4660_208,
            "Toad's Turnpike Items 3 Spot 3": 4660_209,
            "Toad's Turnpike Items 3 Spot 4": 4660_210,
        }, {
            "Toad's Turnpike Items 4 Spot 1": 4660_211,
            "Toad's Turnpike Items 4 Spot 2": 4660_212,
            "Toad's Turnpike Items 4 Spot 3": 4660_213,
            "Toad's Turnpike Items 4 Spot 4": 4660_214,
        },
    ), (
        {
            "Frappe Snowland Items 1 Spot 1": 4660_215,
            "Frappe Snowland Items 1 Spot 2": 4660_216,
            "Frappe Snowland Items 1 Spot 3": 4660_217,
            "Frappe Snowland Items 1 Spot 4": 4660_218,
            "Frappe Snowland Items 1 Spot 5": 4660_219,
        }, {
            "Frappe Snowland Items 2 Spot 1": 4660_220,
            "Frappe Snowland Items 2 Spot 2": 4660_221,
            "Frappe Snowland Items 2 Spot 3": 4660_222,
            "Frappe Snowland Items 2 Spot 4": 4660_223,
            "Frappe Snowland Items 2 Spot 5": 4660_224,
        }, {
            "Frappe Snowland Items 3 Spot 1": 4660_225,
            "Frappe Snowland Items 3 Spot 2": 4660_226,
            "Frappe Snowland Items 3 Spot 3": 4660_227,
            "Frappe Snowland Items 3 Spot 4": 4660_228,
            "Frappe Snowland Items 3 Spot 5": 4660_229,
        },
    ), (
        {
            "Choco Mountain Items 1 Spot 1": 4660_230,
            "Choco Mountain Items 1 Spot 2": 4660_231,
            "Choco Mountain Items 1 Spot 3": 4660_232,
            "Choco Mountain Items 1 Spot 4": 4660_233,
            "Choco Mountain Items 1 Spot 5": 4660_234,
        }, {
            "Choco Mountain Items 2 Spot 1": 4660_235,
            "Choco Mountain Items 2 Spot 2": 4660_236,
            "Choco Mountain Items 2 Spot 3": 4660_237,
            "Choco Mountain Items 2 Spot 4": 4660_238,
            "Choco Mountain Items 2 Spot 5": 4660_239,
        }, {
            "Choco Mountain Items 3 Spot 1": 4660_240,
            "Choco Mountain Items 3 Spot 2": 4660_241,
            "Choco Mountain Items 3 Spot 3": 4660_242,
            "Choco Mountain Items 3 Spot 4": 4660_243,
            "Choco Mountain Items 3 Spot 5": 4660_244,
        },
    ), (
        {
            "Mario Raceway Items 1 Spot 1": 4660_245,
            "Mario Raceway Items 1 Spot 2": 4660_246,
            "Mario Raceway Items 1 Spot 3": 4660_247,
            "Mario Raceway Items 1 Spot 4": 4660_248,
            "Mario Raceway Items 1 Spot 5": 4660_249,
        }, {
            "Mario Raceway Items 2 Spot 1": 4660_250,
            "Mario Raceway Items 2 Spot 2": 4660_251,
            "Mario Raceway Items 2 Spot 3": 4660_252,
            "Mario Raceway Items 2 Spot 4": 4660_253,
            "Mario Raceway Items 2 Spot 5": 4660_254,
        }, {
            "Mario Raceway Items 3 Spot 1": 4660_255,
            "Mario Raceway Items 3 Spot 2": 4660_256,
            "Mario Raceway Items 3 Spot 3": 4660_257,
            "Mario Raceway Items 3 Spot 4": 4660_258,
            "Mario Raceway Items 3 Spot 5": 4660_259,
        },
    ), (
        {
            "Wario Stadium Items 1 Spot 1": 4660_260,
            "Wario Stadium Items 1 Spot 2": 4660_261,
            "Wario Stadium Items 1 Spot 3": 4660_262,
            "Wario Stadium Items 1 Spot 4": 4660_263,
            "Wario Stadium Items 1 Spot 5": 4660_264,
        }, {
            "Wario Stadium Items 2 Spot 1": 4660_265,
            "Wario Stadium Items 2 Spot 2": 4660_266,
            "Wario Stadium Items 2 Spot 3": 4660_267,
            "Wario Stadium Items 2 Spot 4": 4660_268,
            "Wario Stadium Items 2 Spot 5": 4660_269,
        }, {
            "Wario Stadium Items 3 Spot 1": 4660_270,
            "Wario Stadium Items 3 Spot 2": 4660_271,
            "Wario Stadium Items 3 Spot 3": 4660_272,
            "Wario Stadium Items 3 Spot 4": 4660_273,
            "Wario Stadium Items 3 Spot 5": 4660_274,
        }, {
            "Wario Stadium Items 4 Spot 1": 4660_275,
            "Wario Stadium Items 4 Spot 2": 4660_276,
            "Wario Stadium Items 4 Spot 3": 4660_277,
            "Wario Stadium Items 4 Spot 4": 4660_278,
            "Wario Stadium Items 4 Spot 5": 4660_279,
        }, {
            "Wario Stadium Items 5 Spot 1": 4660_280,
            "Wario Stadium Items 5 Spot 2": 4660_281,
            "Wario Stadium Items 5 Spot 3": 4660_282,
            "Wario Stadium Items 5 Spot 4": 4660_283,
            "Wario Stadium Items 5 Spot 5": 4660_284,
        }, {
            "Wario Stadium Items 6 Spot 1": 4660_285,
            "Wario Stadium Items 6 Spot 2": 4660_286,
            "Wario Stadium Items 6 Spot 3": 4660_287,
            "Wario Stadium Items 6 Spot 4": 4660_288,
            "Wario Stadium Items 6 Spot 5": 4660_289,
        },
    ), (
        {
            "Sherbet Land First Items Spot 1": 4660_290,
            "Sherbet Land First Items Spot 2": 4660_291,
            "Sherbet Land First Items Spot 3": 4660_292,
            "Sherbet Land First Items Spot 4": 4660_293,
            "Sherbet Land First Items Spot 5": 4660_294,
        }, {
            "Sherbet Land Left of Rock Items Spot 1": 4660_295,
            "Sherbet Land Left of Rock Items Spot 2": 4660_296,
            "Sherbet Land Left of Rock Items Spot 3": 4660_297,
            "Sherbet Land Left of Rock Items Spot 4": 4660_298,
        }, {
            "Sherbet Land Right of Rock Item Spot": 4660_299,
        }, {
            "Sherbet Land Cave Items Spot 1": 4660_300,
            "Sherbet Land Cave Items Spot 2": 4660_301,
            "Sherbet Land Cave Items Spot 3": 4660_302,
            "Sherbet Land Cave Items Spot 4": 4660_303,
            "Sherbet Land Cave Items Spot 5": 4660_304,
        }, {
            "Sherbet Land Last Items Spot 1": 4660_305,
            "Sherbet Land Last Items Spot 2": 4660_306,
            "Sherbet Land Last Items Spot 3": 4660_307,
            "Sherbet Land Last Items Spot 4": 4660_308,
        },
    ), (
        {
            "Royal Raceway Items 1 Spot 1": 4660_309,
            "Royal Raceway Items 1 Spot 2": 4660_310,
            "Royal Raceway Items 1 Spot 3": 4660_311,
            "Royal Raceway Items 1 Spot 4": 4660_312,
            "Royal Raceway Items 1 Spot 5": 4660_313,
        }, {
            "Royal Raceway Items 2 Spot 1": 4660_314,
            "Royal Raceway Items 2 Spot 2": 4660_315,
            "Royal Raceway Items 2 Spot 3": 4660_316,
            "Royal Raceway Items 2 Spot 4": 4660_317,
            "Royal Raceway Items 2 Spot 5": 4660_318,
        }, {
            "Royal Raceway Items 3 Spot 1": 4660_319,
            "Royal Raceway Items 3 Spot 2": 4660_320,
            "Royal Raceway Items 3 Spot 3": 4660_321,
            "Royal Raceway Items 3 Spot 4": 4660_322,
            "Royal Raceway Items 3 Spot 5": 4660_323,
        }, {
            "Royal Raceway Items 4 Spot 1": 4660_324,
            "Royal Raceway Items 4 Spot 2": 4660_325,
            "Royal Raceway Items 4 Spot 3": 4660_326,
            "Royal Raceway Items 4 Spot 4": 4660_327,
            "Royal Raceway Items 4 Spot 5": 4660_328,
        },
    ), (
        {
            "Bowser's Castle Items 1 Spot 1": 4660_329,
            "Bowser's Castle Items 1 Spot 2": 4660_330,
            "Bowser's Castle Items 1 Spot 3": 4660_331,
            "Bowser's Castle Items 1 Spot 4": 4660_332,
        }, {
            "Bowser's Castle Items 2 Spot 1": 4660_333,
            "Bowser's Castle Items 2 Spot 2": 4660_334,
            "Bowser's Castle Items 2 Spot 3": 4660_335,
            "Bowser's Castle Items 2 Spot 4": 4660_336,
        }, {
            "Bowser's Castle Items 3 Spot 1": 4660_337,
            "Bowser's Castle Items 3 Spot 2": 4660_338,
            "Bowser's Castle Items 3 Spot 3": 4660_339,
            "Bowser's Castle Items 3 Spot 4": 4660_340,
        },
    ), (
        {
            "D.K.'s Jungle Parkway Items 1 Spot 1": 4660_341,
            "D.K.'s Jungle Parkway Items 1 Spot 2": 4660_342,
            "D.K.'s Jungle Parkway Items 1 Spot 3": 4660_343,
            "D.K.'s Jungle Parkway Items 1 Spot 4": 4660_344,
            "D.K.'s Jungle Parkway Items 1 Spot 5": 4660_345,
        }, {
            "D.K.'s Jungle Parkway Items 2 Spot 1": 4660_346,
            "D.K.'s Jungle Parkway Items 2 Spot 2": 4660_347,
            "D.K.'s Jungle Parkway Items 2 Spot 3": 4660_348,
            "D.K.'s Jungle Parkway Items 2 Spot 4": 4660_349,
        }, {
            "D.K.'s Jungle Parkway Items 3 Spot 1": 4660_350,
            "D.K.'s Jungle Parkway Items 3 Spot 2": 4660_351,
            "D.K.'s Jungle Parkway Items 3 Spot 3": 4660_352,
            "D.K.'s Jungle Parkway Items 3 Spot 4": 4660_353,
        }, {
            "D.K.'s Jungle Parkway Items 4 Spot 1": 4660_354,
            "D.K.'s Jungle Parkway Items 4 Spot 2": 4660_355,
            "D.K.'s Jungle Parkway Items 4 Spot 3": 4660_356,
            "D.K.'s Jungle Parkway Items 4 Spot 4": 4660_357,
        }, {
            "D.K.'s Jungle Parkway Items 5 Spot 1": 4660_358,
            "D.K.'s Jungle Parkway Items 5 Spot 2": 4660_359,
            "D.K.'s Jungle Parkway Items 5 Spot 3": 4660_360,
            "D.K.'s Jungle Parkway Items 5 Spot 4": 4660_361,
            "D.K.'s Jungle Parkway Items 5 Spot 5": 4660_362,
        },
    ), (
        {
            "Yoshi Valley Field Items Spot 1": 4660_363,
            "Yoshi Valley Field Items Spot 2": 4660_364,
            "Yoshi Valley Field Items Spot 3": 4660_365,
            "Yoshi Valley Field Items Spot 4": 4660_366,
        }, {
            "Yoshi Valley Maze Entry Right Items Spot 1": 4660_367,
            "Yoshi Valley Maze Entry Right Items Spot 2": 4660_368,
            "Yoshi Valley Maze Entry Right Items Spot 3": 4660_369,
            "Yoshi Valley Maze Entry Right Items Spot 4": 4660_370,
        }, {
            "Yoshi Valley Maze Bridge Items Spot 1": 4660_371,
            "Yoshi Valley Maze Bridge Items Spot 2": 4660_372,
            "Yoshi Valley Maze Bridge Items Spot 3": 4660_373,
            "Yoshi Valley Maze Bridge Items Spot 4": 4660_374,
            "Yoshi Valley Maze Bridge Items Spot 5": 4660_375,
        }, {
            "Yoshi Valley Rightmost Items Spot 1": 4660_376,
            "Yoshi Valley Rightmost Items Spot 2": 4660_377,
            "Yoshi Valley Rightmost Items Spot 3": 4660_378,
            "Yoshi Valley Rightmost Items Spot 4": 4660_379,
            "Yoshi Valley Rightmost Items Spot 5": 4660_380,
            "Yoshi Valley Rightmost Items Spot 6": 4660_381,
        }, {
            "Yoshi Valley Leftmost Fork Items Spot 1": 4660_382,
            "Yoshi Valley Leftmost Fork Items Spot 2": 4660_383,
            "Yoshi Valley Leftmost Fork Items Spot 3": 4660_384,
            "Yoshi Valley Leftmost Fork Items Spot 4": 4660_385,
        }, {
            "Yoshi Valley Leftmost Ledge Items Spot 1": 4660_386,
            "Yoshi Valley Leftmost Ledge Items Spot 2": 4660_387,
            "Yoshi Valley Leftmost Ledge Items Spot 3": 4660_388,
            "Yoshi Valley Leftmost Ledge Items Spot 4": 4660_389,
        }, {
            "Yoshi Valley Hairpin Turn Items Spot 1": 4660_390,
            "Yoshi Valley Hairpin Turn Items Spot 2": 4660_391,
            "Yoshi Valley Hairpin Turn Items Spot 3": 4660_392,
            "Yoshi Valley Hairpin Turn Items Spot 4": 4660_393,
        }, {
            "Yoshi Valley Giant Egg Items Spot 1": 4660_394,
            "Yoshi Valley Giant Egg Items Spot 2": 4660_395,
            "Yoshi Valley Giant Egg Items Spot 3": 4660_396,
            "Yoshi Valley Giant Egg Items Spot 4": 4660_397,
            "Yoshi Valley Giant Egg Items Spot 5": 4660_398,
            "Yoshi Valley Giant Egg Items Spot 6": 4660_399,
        },
    ), (
        {
            "Banshee Boardwalk Items 1 Spot 1": 4660_400,
            "Banshee Boardwalk Items 1 Spot 2": 4660_401,
            "Banshee Boardwalk Items 1 Spot 3": 4660_402,
            "Banshee Boardwalk Items 1 Spot 4": 4660_403,
        }, {
            "Banshee Boardwalk Items 2 Spot 1": 4660_404,
            "Banshee Boardwalk Items 2 Spot 2": 4660_405,
            "Banshee Boardwalk Items 2 Spot 3": 4660_406,
            "Banshee Boardwalk Items 2 Spot 4": 4660_407,
        }, {
            "Banshee Boardwalk Items 3 Spot 1": 4660_408,
            "Banshee Boardwalk Items 3 Spot 2": 4660_409,
            "Banshee Boardwalk Items 3 Spot 3": 4660_410,
            "Banshee Boardwalk Items 3 Spot 4": 4660_411,
        }, {
            "Banshee Boardwalk Items 4 Spot 1": 4660_412,
            "Banshee Boardwalk Items 4 Spot 2": 4660_413,
            "Banshee Boardwalk Items 4 Spot 3": 4660_414,
            "Banshee Boardwalk Items 4 Spot 4": 4660_415,
        },
    ), (
        {
            "Rainbow Road Items 1 Spot 1": 4660_416,
            "Rainbow Road Items 1 Spot 2": 4660_417,
            "Rainbow Road Items 1 Spot 3": 4660_418,
            "Rainbow Road Items 1 Spot 4": 4660_419,
        }, {
            "Rainbow Road Items 2 Spot 1": 4660_420,
            "Rainbow Road Items 2 Spot 2": 4660_421,
            "Rainbow Road Items 2 Spot 3": 4660_422,
            "Rainbow Road Items 2 Spot 4": 4660_423,
        }, {
            "Rainbow Road Items 3 Spot 1": 4660_424,
            "Rainbow Road Items 3 Spot 2": 4660_425,
            "Rainbow Road Items 3 Spot 3": 4660_426,
            "Rainbow Road Items 3 Spot 4": 4660_427,
        }, {
            "Rainbow Road Items 4 Spot 1": 4660_428,
            "Rainbow Road Items 4 Spot 2": 4660_429,
            "Rainbow Road Items 4 Spot 3": 4660_430,
            "Rainbow Road Items 4 Spot 4": 4660_431,
        }, {
            "Rainbow Road Items 5 Spot 1": 4660_432,
            "Rainbow Road Items 5 Spot 2": 4660_433,
            "Rainbow Road Items 5 Spot 3": 4660_434,
            "Rainbow Road Items 5 Spot 4": 4660_435,
        }, {
            "Rainbow Road Items 6 Spot 1": 4660_436,
            "Rainbow Road Items 6 Spot 2": 4660_437,
            "Rainbow Road Items 6 Spot 3": 4660_438,
            "Rainbow Road Items 6 Spot 4": 4660_439,
        }, {
            "Rainbow Road Items 7 Spot 1": 4660_440,
            "Rainbow Road Items 7 Spot 2": 4660_441,
            "Rainbow Road Items 7 Spot 3": 4660_442,
            "Rainbow Road Items 7 Spot 4": 4660_443,
        }, {
            "Rainbow Road Items 8 Spot 1": 4660_444,
            "Rainbow Road Items 8 Spot 2": 4660_445,
            "Rainbow Road Items 8 Spot 3": 4660_446,
            "Rainbow Road Items 8 Spot 4": 4660_447,
        },
    ),
)

#   Region: { Location:                location id }
cup_locations = {
    "Mushroom Cup Trophy Ceremony": {
        "Mushroom Cup Bronze":         46600_48,
        "Mushroom Cup Silver":         46600_49,
        "Mushroom Cup Gold":           46600_50,
        # "Mushroom Cup 50cc Bronze":  46600_51,  Might do more cup difficulty unlock options later on
        # "Mushroom Cup 50cc Silver":  46600_52,
        # "Mushroom Cup 50cc Gold":    46600_53,
        # "Mushroom Cup 100cc Bronze": 46600_54,
        # "Mushroom Cup 100cc Silver": 46600_55,
        "Mushroom Cup 100cc Gold":     46600_56,
        # "Mushroom Cup 150cc Bronze": 46600_57,
        # "Mushroom Cup 150cc Silver": 46600_58,
        "Mushroom Cup 150cc Gold":     46600_59,
    },
    "Flower Cup Trophy Ceremony": {
        "Flower Cup Bronze":         46600_60,
        "Flower Cup Silver":         46600_61,
        "Flower Cup Gold":           46600_62,
        # "Flower Cup 50cc Bronze":  46600_63,
        # "Flower Cup 50cc Silver":  46600_64,
        # "Flower Cup 50cc Gold":    46600_65,
        # "Flower Cup 100cc Bronze": 46600_66,
        # "Flower Cup 100cc Silver": 46600_67,
        "Flower Cup 100cc Gold":     46600_68,
        # "Flower Cup 150cc Bronze": 46600_69,
        # "Flower Cup 150cc Silver": 46600_70,
        "Flower Cup 150cc Gold":     46600_71,
    },
    "Star Cup Trophy Ceremony": {
        "Star Cup Bronze":         46600_72,
        "Star Cup Silver":         46600_73,
        "Star Cup Gold":           46600_74,
        # "Star Cup 50cc Bronze":  46600_75,
        # "Star Cup 50cc Silver":  46600_76,
        # "Star Cup 50cc Gold":    46600_77,
        # "Star Cup 100cc Bronze": 46600_78,
        # "Star Cup 100cc Silver": 46600_79,
        "Star Cup 100cc Gold":     46600_80,
        # "Star Cup 150cc Bronze": 46600_81,
        # "Star Cup 150cc Silver": 46600_82,
        "Star Cup 150cc Gold":     46600_83,
    },
    "Special Cup Trophy Ceremony": {
        "Special Cup Bronze":         46600_84,
        "Special Cup Silver":         46600_85,
        "Special Cup Gold":           46600_86,
        # "Special Cup 50cc Bronze":  46600_87,
        # "Special Cup 50cc Silver":  46600_88,
        # "Special Cup 50cc Gold":    46600_89,
        # "Special Cup 100cc Bronze": 46600_90,
        # "Special Cup 100cc Silver": 46600_91,
        "Special Cup 100cc Gold":     46600_92,
        # "Special Cup 150cc Bronze": 46600_93,
        # "Special Cup 150cc Silver": 46600_94,
        "Special Cup 150cc Gold":     46600_95,
    }
}

location_name_to_id = (
    {name: code for r in course_locations.values() for name, (code, _) in r.items()} |
    {name: code for name, (code, _) in shared_hazard_locations.items()} |
    {name: code for r in item_cluster_locations for c in r for name, code in c.items()} |
    {name: code for r in cup_locations.values() for name, code in r.items()}
)
