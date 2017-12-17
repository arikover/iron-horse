# wagon ids are generic and are composed to specific vehicle ids elsewhere
# order is significant
buy_menu_sort_order_wagons = ['metro_car',
                              'passenger_car',
                              'luxury_passenger_car',
                              'mail_car',
                              'open_car',
                              'box_car',
                              'flat_car',
                              'hopper_car',
                              'dump_car',
                              'tank_car',
                              'covered_hopper_car',
                              'silo_car',
                              'livestock_car',
                              'edibles_tank_car',
                              'reefer_car',
                              'fruit_veg_car',
                              'intermodal_car',
                              'stake_car',
                              'supplies_car',
                              'vehicle_transporter_car',
                              'metal_car',
                              'caboose_car']


# shared lists of allowed classes, shared across multiple vehicle types
# these lists are similar but not identical across Iron Horse, Squid, Road Hog etc
base_refits_by_class = {'empty': [],
                        'all_freight': ['CC_BULK', 'CC_PIECE_GOODS', 'CC_EXPRESS', 'CC_LIQUID', 'CC_ARMOURED', 'CC_REFRIGERATED', 'CC_COVERED', 'CC_NON_POURABLE'],
                        'pax': ['CC_PASSENGERS'],
                        'mail': ['CC_MAIL'],
                        'liquids': ['CC_LIQUID'],
                        'packaged_freight': ['CC_PIECE_GOODS', 'CC_EXPRESS', 'CC_ARMOURED', 'CC_LIQUID'],
                        'flatcar_freight': ['CC_PIECE_GOODS'],
                        'hopper_freight': ['CC_BULK'],
                        'refrigerated_freight': ['CC_REFRIGERATED'],
                        'express_freight': ['CC_EXPRESS','CC_ARMOURED']}

# rather than using disallowed classes (can cause breakage), specific labels are disallowed
# this is done per vehicle type, or added to global_constants for ease of reuse and updating
# these lists are similar but not identical across Iron Horse, Squid, Road Hog etc
# notably, Sugar Beet and Cassava are farm cargos allowed to travel by hopper, most farm cargos cannot
disallowed_refits_by_label = {'non_hopper_freight': ['WOOD', 'SGCN', 'FICR', 'BDMT', 'WDPR', 'GRAI', 'WHEA', 'MAIZ', 'FRUT', 'BEAN'],
                              'edible_liquids': ['MILK', 'WATR', 'BEER', 'FOOD', 'EOIL'],
                              'non_edible_liquids': ['RFPR', 'OIL_', 'FMSP', 'PETR', 'RUBR', 'SULP'],
                              'non_flatcar_freight': ['FOOD', 'FISH', 'LVST', 'FRUT', 'BEER', 'MILK', 'JAVA', 'SUGR', 'NUTS', 'EOIL', 'BOOM', 'FERT'],
                              'non_freight_special_cases': ['TOUR']}

# occasionally label refits need to be shared across vehicle classes
allowed_refits_by_label = {'box_freight': ['MAIL', 'GRAI', 'WHEA', 'MAIZ', 'FRUT', 'BEAN', 'NITR']}

# capacity multipliers for user-configurable capacity parameter
capacity_multipliers = [0.67, 1, 1.33]
# identifier for user-configurable capacity parameter
param_adjust_vehicle_capacity = 1
# mailbags are < 1t, multiply capacity appropriately
mail_multiplier = 2

# used to construct the cargo table automatically
# ! order is significant ! - openttd will cascade through default cargos in the order specified by the cargo table
cargo_labels = ['PASS', # pax first
                'TOUR',
                # "the mail must get through"
                'MAIL',
                # all other cargos - append new ones to end, don't change order
                'COAL',
                'IORE',
                'GRVL',
                'SAND',
                'AORE',
                'CORE',
                'CLAY',
                'SCMT',
                'WOOD',
                'LIME',
                'GOOD',
                'FOOD',
                'STEL',
                'FMSP',
                'ENSP',
                'BEER',
                'BDMT',
                'MNSP',
                'PAPR',
                'WDPR',
                'VEHI',
                'COPR',
                'DYES',
                'OIL_',
                'RFPR',
                'PETR',
                'PLAS',
                'WATR',
                'FISH',
                'CERE',
                'FICR',
                'FRVG',
                'FRUT',
                'GRAI',
                'LVST',
                'MAIZ',
                'MILK',
                'RUBR',
                'SGBT',
                'SGCN',
                'WHEA',
                'WOOL',
                'OLSD',
                'SUGR',
                'JAVA',
                'BEAN',
                'NITR',
                'VEHI',
                'EOIL',
                'NUTS',
                'CASS',
                'MNO2',
                'PHOS',
                'POTA',
                'PORE',
                'IRON',
                'NICK',
                'SLAG',
                'QLME',
                'BOOM',
                'METL',
                'SULP',
                'SASH',
                'CMNT',
                'COKE',
                'KAOL',
                'FERT',
                'PIPE',
                'SALT',
                'CBLK',
                'CHLO',
                #
                'NULL']

grfid = r"CA\12\1F"

# chameleon templating goes faster if a cache dir is used; this specifies which dir is cache dir
chameleon_cache_dir = '.chameleon_cache'

# specify location for intermediate files generated during build (nml, graphics, lang etc)
generated_files_dir = 'generated'

# this is for nml or grfcodec, don't need to use python path module here
graphics_path = 'generated/graphics/'

# cargo aging constant - OTTD default is 185
CARGO_AGE_PERIOD = 185

# OpenTTD's max date
max_game_date = 5000001

# standard offsets for trains
default_spritesheet_offsets = {'3': [[-3, -25], [-3, -21], [-16, -12], [5, -17], [-3, -14], [-14, -17], [-16, -12], [-8, -23]],
                               '4': [[-3, -23], [-4, -20], [-16, -12], [3, -17], [-3, -14], [-14, -17], [-16, -12], [-8, -22]],
                               '5': [[-3, -22], [-6, -19], [-16, -12], [1, -16], [-3, -14], [-16, -16], [-16, -12], [-8, -21]],
                               '6': [[-3, -22], [-8, -18], [-16, -12], [-1, -15], [-3, -14], [-16, -15], [-16, -12], [-8, -19]],
                               '7': [[-3, -20], [-8, -18], [-16, -12], [-1, -15], [-3, -14], [-17, -15], [-16, -12], [-10, -19]],
                               '8': [[-3, -20], [-10, -17], [-16, -12], [-4, -15], [-3, -13], [-17, -14], [-16, -12], [-10, -18]]}

# spritesheet bounding boxes, each defined by a 3 tuple (left x, width, height);
# upper y is determined by spritesheet row position, so isn't defined as a constant
spritesheet_bounding_boxes = ((60, 8, 29), (76, 26, 24), (107, 40, 16), (156, 26, 24),
                              (188, 8, 29), (200, 26, 24), (235, 40, 16), (284, 26, 24))

buy_menu_sprite_width = 36 # 36 is correct, but some spritesheets might have wrong widths due to copy-pasteo etc
buy_menu_sprite_height = 16