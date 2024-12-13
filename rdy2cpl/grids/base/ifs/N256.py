from rdy2cpl.grids.base.reduced_gaussian import ReducedGaussianGrid


class N256(ReducedGaussianGrid):
    def __init__(self):
        super().__init__(_lats, _nlons)


_lats = (
    89.7311486184145, 89.3828738963346, 89.0325424237903, 88.6817462435912, 88.3307737888073,
    87.979716034326, 87.6286106094843, 87.2774758672239, 86.9263218176459, 86.5751543820948,
    86.2239772863455, 85.8727929914671, 85.5216031882812, 85.1704090767342, 84.8192115319314,
    84.4680112070663, 84.116808599553, 83.7656040948441, 83.4143979962481, 83.0631905457019,
    82.7119819385429, 82.3607723342125, 82.0095618641375, 81.6583506376243, 81.3071387463237,
    80.9559262676574, 80.6047132674759, 80.2534998021422, 79.9022859201808, 79.5510716635948,
    79.1998570689256, 78.8486421681124, 78.4974269891952, 78.1462115568916, 77.794995893075,
    77.4437800171722, 77.0925639464961, 76.7413476965258, 76.3901312811428, 76.0389147128324,
    75.6876980028543, 75.3364811613902, 74.985264197669, 74.6340471200762, 74.282829936248,
    73.9316126531531, 73.5803952771642, 73.2291778141202, 72.877960269381, 72.526742647876,
    72.1755249541459, 71.8243071923805, 71.4730893664524, 71.1218714799457, 70.770653536183,
    70.4194355382484, 70.0682174890089, 69.7169993911329, 69.3657812471072, 69.0145630592523,
    68.6633448297359, 68.3121265605854, 67.9609082536991, 67.609689910856, 67.2584715337256,
    66.9072531238758, 66.5560346827804, 66.2048162118267, 65.8535977123208, 65.5023791854945,
    65.1511606325096, 64.7999420544634, 64.448723452393, 64.0975048272792, 63.7462861800502,
    63.3950675115857, 63.0438488227191, 62.6926301142415, 62.3414113869034, 61.990192641418,
    61.6389738784631, 61.2877550986836, 60.936536302693, 60.5853174910758, 60.2340986643887,
    59.8828798231628, 59.5316609679046, 59.1804420990975, 58.8292232172034, 58.4780043226634,
    58.1267854158993, 57.7755664973148, 57.4243475672959, 57.0731286262123, 56.7219096744183,
    56.3706907122534, 56.0194717400428, 55.6682527580989, 55.3170337667213, 54.9658147661975,
    54.614595756804, 54.2633767388061, 53.9121577124591, 53.5609386780083, 53.2097196356898,
    52.858500585731, 52.5072815283504, 52.1560624637589, 51.8048433921593, 51.4536243137474,
    51.1024052287118, 50.7511861372345, 50.3999670394908, 50.0487479356504, 49.6975288258768,
    49.3463097103278, 48.9950905891562, 48.6438714625095, 48.2926523305301, 47.941433193356,
    47.5902140511205, 47.2389949039526, 46.8877757519773, 46.5365565953153, 46.1853374340839,
    45.8341182683963, 45.4828990983625, 45.131679924089, 44.780460745679, 44.4292415632326,
    44.078022376847, 43.7268031866163, 43.3755839926321, 43.024364794983, 42.6731455937553,
    42.3219263890326, 41.9707071808963, 41.6194879694254, 41.2682687546966, 40.9170495367847,
    40.5658303157622, 40.2146110916997, 39.8633918646658, 39.5121726347275, 39.1609534019498,
    38.8097341663959, 38.4585149281275, 38.1072956872047, 37.756076443686, 37.4048571976283,
    37.0536379490872, 36.7024186981169, 36.35119944477, 35.9999801890982, 35.6487609311515,
    35.297541670979, 34.9463224086285, 34.5951031441466, 34.2438838775788, 33.8926646089697,
    33.5414453383626, 33.1902260658, 32.8390067913233, 32.487787514973, 32.1365682367886,
    31.785348956809, 31.4341296750718, 31.0829103916141, 30.7316911064722, 30.3804718196813,
    30.0292525312763, 29.6780332412909, 29.3268139497584, 28.9755946567113, 28.6243753621814,
    28.2731560662, 27.9219367687976, 27.5707174700042, 27.219498169849, 26.8682788683609,
    26.5170595655681, 26.1658402614983, 25.8146209561786, 25.4634016496356, 25.1121823418955,
    24.7609630329839, 24.4097437229261, 24.0585244117467, 23.7073050994701, 23.3560857861201,
    23.0048664717201, 22.6536471562932, 22.3024278398621, 21.951208522449, 21.5999892040758,
    21.248769884764, 20.897550564535, 20.5463312434094, 20.1951119214078, 19.8438925985505,
    19.4926732748573, 19.1414539503479, 18.7902346250414, 18.4390152989571, 18.0877959721135,
    17.7365766445292, 17.3853573162224, 17.0341379872112, 16.6829186575131, 16.3316993271457,
    15.9804799961263, 15.6292606644719, 15.2780413321993, 14.9268219993252, 14.575602665866,
    14.224383331838, 13.873163997257, 13.5219446621391, 13.1707253264999, 12.8195059903548,
    12.4682866537193, 12.1170673166086, 11.7658479790376, 11.4146286410212, 11.0634093025743,
    10.7121899637113, 10.3609706244468, 10.0097512847951, 9.65853194477046, 9.30731260438692,
    8.95609326365854, 8.60487392259918, 8.25365458122262, 7.90243523954255, 7.55121589757256,
    7.19999655532612, 6.84877721281669, 6.49755787005758, 6.14633852706203, 5.79511918384326,
    5.44389984041437, 5.09268049678841, 4.74146115297837, 4.3902418089972, 4.03902246485776,
    3.6878031205729, 3.3365837761554, 2.98536443161805, 2.63414508697352, 2.28292574223451,
    1.93170639741369, 1.58048705252365, 1.22926770757706, 0.878048362586456, 0.52682901756445,
    0.175609672523576, -0.175609672523576, -0.52682901756445, -0.878048362586456, -1.22926770757706,
    -1.58048705252365, -1.93170639741369, -2.28292574223451, -2.63414508697352, -2.98536443161805,
    -3.3365837761554, -3.6878031205729, -4.03902246485776, -4.3902418089972, -4.74146115297837,
    -5.09268049678841, -5.44389984041437, -5.79511918384326, -6.14633852706203, -6.49755787005758,
    -6.84877721281669, -7.19999655532612, -7.55121589757256, -7.90243523954255, -8.25365458122262,
    -8.60487392259918, -8.95609326365854, -9.30731260438692, -9.65853194477046, -10.0097512847951,
    -10.3609706244468, -10.7121899637113, -11.0634093025743, -11.4146286410212, -11.7658479790376,
    -12.1170673166086, -12.4682866537193, -12.8195059903548, -13.1707253264999, -13.5219446621391,
    -13.873163997257, -14.224383331838, -14.575602665866, -14.9268219993252, -15.2780413321993,
    -15.6292606644719, -15.9804799961263, -16.3316993271457, -16.6829186575131, -17.0341379872112,
    -17.3853573162224, -17.7365766445292, -18.0877959721135, -18.4390152989571, -18.7902346250414,
    -19.1414539503479, -19.4926732748573, -19.8438925985505, -20.1951119214078, -20.5463312434094,
    -20.897550564535, -21.248769884764, -21.5999892040758, -21.951208522449, -22.3024278398621,
    -22.6536471562932, -23.0048664717201, -23.3560857861201, -23.7073050994701, -24.0585244117467,
    -24.4097437229261, -24.7609630329839, -25.1121823418955, -25.4634016496356, -25.8146209561786,
    -26.1658402614983, -26.5170595655681, -26.8682788683609, -27.219498169849, -27.5707174700042,
    -27.9219367687976, -28.2731560662, -28.6243753621814, -28.9755946567113, -29.3268139497584,
    -29.6780332412909, -30.0292525312763, -30.3804718196813, -30.7316911064722, -31.0829103916141,
    -31.4341296750718, -31.785348956809, -32.1365682367886, -32.487787514973, -32.8390067913233,
    -33.1902260658, -33.5414453383626, -33.8926646089697, -34.2438838775788, -34.5951031441466,
    -34.9463224086285, -35.297541670979, -35.6487609311515, -35.9999801890982, -36.35119944477,
    -36.7024186981169, -37.0536379490872, -37.4048571976283, -37.756076443686, -38.1072956872047,
    -38.4585149281275, -38.8097341663959, -39.1609534019498, -39.5121726347275, -39.8633918646658,
    -40.2146110916997, -40.5658303157622, -40.9170495367847, -41.2682687546966, -41.6194879694254,
    -41.9707071808963, -42.3219263890326, -42.6731455937553, -43.024364794983, -43.3755839926321,
    -43.7268031866163, -44.078022376847, -44.4292415632326, -44.780460745679, -45.131679924089,
    -45.4828990983625, -45.8341182683963, -46.1853374340839, -46.5365565953153, -46.8877757519773,
    -47.2389949039526, -47.5902140511205, -47.941433193356, -48.2926523305301, -48.6438714625095,
    -48.9950905891562, -49.3463097103278, -49.6975288258768, -50.0487479356504, -50.3999670394908,
    -50.7511861372345, -51.1024052287118, -51.4536243137474, -51.8048433921593, -52.1560624637589,
    -52.5072815283504, -52.858500585731, -53.2097196356898, -53.5609386780083, -53.9121577124591,
    -54.2633767388061, -54.614595756804, -54.9658147661975, -55.3170337667213, -55.6682527580989,
    -56.0194717400428, -56.3706907122534, -56.7219096744183, -57.0731286262123, -57.4243475672959,
    -57.7755664973148, -58.1267854158993, -58.4780043226634, -58.8292232172034, -59.1804420990975,
    -59.5316609679046, -59.8828798231628, -60.2340986643887, -60.5853174910758, -60.936536302693,
    -61.2877550986836, -61.6389738784631, -61.990192641418, -62.3414113869034, -62.6926301142415,
    -63.0438488227191, -63.3950675115857, -63.7462861800502, -64.0975048272792, -64.448723452393,
    -64.7999420544634, -65.1511606325096, -65.5023791854945, -65.8535977123208, -66.2048162118267,
    -66.5560346827804, -66.9072531238758, -67.2584715337256, -67.609689910856, -67.9609082536991,
    -68.3121265605854, -68.6633448297359, -69.0145630592523, -69.3657812471072, -69.7169993911329,
    -70.0682174890089, -70.4194355382484, -70.770653536183, -71.1218714799457, -71.4730893664524,
    -71.8243071923805, -72.1755249541459, -72.526742647876, -72.877960269381, -73.2291778141202,
    -73.5803952771642, -73.9316126531531, -74.282829936248, -74.6340471200762, -74.985264197669,
    -75.3364811613902, -75.6876980028543, -76.0389147128324, -76.3901312811428, -76.7413476965258,
    -77.0925639464961, -77.4437800171722, -77.794995893075, -78.1462115568916, -78.4974269891952,
    -78.8486421681124, -79.1998570689256, -79.5510716635948, -79.9022859201808, -80.2534998021422,
    -80.6047132674759, -80.9559262676574, -81.3071387463237, -81.6583506376243, -82.0095618641375,
    -82.3607723342125, -82.7119819385429, -83.0631905457019, -83.4143979962481, -83.7656040948441,
    -84.116808599553, -84.4680112070663, -84.8192115319314, -85.1704090767342, -85.5216031882812,
    -85.8727929914671, -86.2239772863455, -86.5751543820948, -86.9263218176459, -87.2774758672239,
    -87.6286106094843, -87.979716034326, -88.3307737888073, -88.6817462435912, -89.0325424237903,
    -89.3828738963346, -89.7311486184145,
)
_nlons = (
    18, 25, 32, 40, 45, 50, 60, 64, 72, 72,
    75, 81, 90, 96, 100, 108, 120, 120, 125, 135,
    144, 150, 160, 160, 180, 180, 180, 192, 192, 200,
    216, 216, 216, 225, 240, 240, 243, 250, 256, 270,
    270, 288, 288, 288, 300, 300, 320, 320, 320, 324,
    360, 360, 360, 360, 360, 360, 375, 375, 384, 384,
    400, 400, 400, 432, 432, 432, 432, 432, 450, 450,
    450, 480, 480, 480, 480, 480, 486, 500, 500, 500,
    512, 512, 540, 540, 540, 540, 540, 576, 576, 576,
    576, 576, 576, 600, 600, 600, 600, 600, 640, 640,
    640, 640, 640, 640, 640, 640, 648, 675, 675, 675,
    675, 675, 675, 720, 720, 720, 720, 720, 720, 720,
    720, 720, 729, 729, 750, 750, 750, 750, 750, 768,
    768, 768, 768, 800, 800, 800, 800, 800, 800, 800,
    800, 810, 810, 864, 864, 864, 864, 864, 864, 864,
    864, 864, 864, 864, 864, 864, 864, 900, 900, 900,
    900, 900, 900, 900, 900, 900, 900, 900, 960, 960,
    960, 960, 960, 960, 960, 960, 960, 960, 960, 960,
    960, 960, 960, 960, 960, 960, 960, 960, 960, 960,
    972, 972, 972, 972, 972, 1000, 1000, 1000, 1000, 1000,
    1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
    1000, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024,
    1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024,
    1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024,
    1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024,
    1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024,
    1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024,
    1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024,
    1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024,
    1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024, 1024,
    1024, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
    1000, 1000, 1000, 1000, 1000, 1000, 1000, 972, 972, 972,
    972, 972, 960, 960, 960, 960, 960, 960, 960, 960,
    960, 960, 960, 960, 960, 960, 960, 960, 960, 960,
    960, 960, 960, 960, 900, 900, 900, 900, 900, 900,
    900, 900, 900, 900, 900, 864, 864, 864, 864, 864,
    864, 864, 864, 864, 864, 864, 864, 864, 864, 810,
    810, 800, 800, 800, 800, 800, 800, 800, 800, 768,
    768, 768, 768, 750, 750, 750, 750, 750, 729, 729,
    720, 720, 720, 720, 720, 720, 720, 720, 720, 675,
    675, 675, 675, 675, 675, 648, 640, 640, 640, 640,
    640, 640, 640, 640, 600, 600, 600, 600, 600, 576,
    576, 576, 576, 576, 576, 540, 540, 540, 540, 540,
    512, 512, 500, 500, 500, 486, 480, 480, 480, 480,
    480, 450, 450, 450, 432, 432, 432, 432, 432, 400,
    400, 400, 384, 384, 375, 375, 360, 360, 360, 360,
    360, 360, 324, 320, 320, 320, 300, 300, 288, 288,
    288, 270, 270, 256, 250, 243, 240, 240, 225, 216,
    216, 216, 200, 192, 192, 180, 180, 180, 160, 160,
    150, 144, 135, 125, 120, 120, 108, 100, 96, 90,
    81, 75, 72, 72, 64, 60, 50, 45, 40, 32,
    25, 18,
)