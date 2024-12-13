from rdy2cpl.grids.base.reduced_gaussian import ReducedGaussianGrid


class N80(ReducedGaussianGrid):
    def __init__(self):
        super().__init__(_lats, _nlons)


_lats = (
    89.1415194264611, 88.0294288679515, 86.910770814124, 85.7906288836365, 84.6699240844466,
    83.5489469125421, 82.4278175240078, 81.3065945226689, 80.1853098724772, 79.0639824814086,
    77.9426242466729, 76.8212430271002, 75.6998442220113, 74.5784316632959, 73.4570081455833,
    72.3355757549091, 71.214136079887, 70.0926903516245, 68.9712395389358, 67.8497844146698,
    66.7283256028822, 65.6068636130103, 64.4853988650433, 63.3639317083405, 62.2424624358907,
    61.1209912952521, 59.9995184970404, 58.8780442215827, 57.7565686241836, 56.6350918393302,
    55.5136139840772, 54.3921351607921, 53.2706554593984, 52.1491749592204, 51.0276937305087,
    49.906211835711, 48.784729330535, 47.6632462648426, 46.5417626834057, 45.4202786265483,
    44.298794130694, 43.1773092288349, 42.0558239509352, 40.9343383242788, 39.8128523737712,
    38.6913661222016, 37.5698795904715, 36.4483927977945, 35.3269057618723, 34.2054184990488,
    33.0839310244466, 31.962443352088, 30.8409554950018, 29.7194674653187, 28.5979792743565,
    27.4764909326964, 26.3550024502506, 25.2335138363243, 24.1120250996709, 22.9905362485413,
    21.8690472907301, 20.747558233616, 19.6260690841993, 18.5045798491365, 17.3830905347709,
    16.2616011471617, 15.1401116921107, 14.018622175186, 12.8971326017452, 11.7756429769564,
    10.6541533058176, 9.53266359317569, 8.41117384374318, 7.28968406211511, 6.16819425278443,
    5.04670442015713, 3.92521456856645, 2.80372470228675, 1.68223482554707, 0.560744942544222,
    -0.560744942544222, -1.68223482554707, -2.80372470228675, -3.92521456856645, -5.04670442015713,
    -6.16819425278443, -7.28968406211511, -8.41117384374318, -9.53266359317569, -10.6541533058176,
    -11.7756429769564, -12.8971326017452, -14.018622175186, -15.1401116921107, -16.2616011471617,
    -17.3830905347709, -18.5045798491365, -19.6260690841993, -20.747558233616, -21.8690472907301,
    -22.9905362485413, -24.1120250996709, -25.2335138363243, -26.3550024502506, -27.4764909326964,
    -28.5979792743565, -29.7194674653187, -30.8409554950018, -31.962443352088, -33.0839310244466,
    -34.2054184990488, -35.3269057618723, -36.4483927977945, -37.5698795904715, -38.6913661222016,
    -39.8128523737712, -40.9343383242788, -42.0558239509352, -43.1773092288349, -44.298794130694,
    -45.4202786265483, -46.5417626834057, -47.6632462648426, -48.784729330535, -49.906211835711,
    -51.0276937305087, -52.1491749592204, -53.2706554593984, -54.3921351607921, -55.5136139840772,
    -56.6350918393302, -57.7565686241836, -58.8780442215827, -59.9995184970404, -61.1209912952521,
    -62.2424624358907, -63.3639317083405, -64.4853988650433, -65.6068636130103, -66.7283256028822,
    -67.8497844146698, -68.9712395389358, -70.0926903516245, -71.214136079887, -72.3355757549091,
    -73.4570081455833, -74.5784316632959, -75.6998442220113, -76.8212430271002, -77.9426242466729,
    -79.0639824814086, -80.1853098724772, -81.3065945226689, -82.4278175240078, -83.5489469125421,
    -84.6699240844466, -85.7906288836365, -86.910770814124, -88.0294288679515, -89.1415194264611,
)

_nlons = (
    18, 25, 36, 40, 45, 54, 60, 64, 72, 72,
    80, 90, 96, 100, 108, 120, 120, 128, 135, 144,
    144, 150, 160, 160, 180, 180, 180, 192, 192, 200,
    200, 216, 216, 216, 225, 225, 240, 240, 240, 256,
    256, 256, 256, 288, 288, 288, 288, 288, 288, 288,
    288, 288, 300, 300, 300, 300, 320, 320, 320, 320,
    320, 320, 320, 320, 320, 320, 320, 320, 320, 320,
    320, 320, 320, 320, 320, 320, 320, 320, 320, 320,
    320, 320, 320, 320, 320, 320, 320, 320, 320, 320,
    320, 320, 320, 320, 320, 320, 320, 320, 320, 320,
    320, 320, 320, 320, 300, 300, 300, 300, 288, 288,
    288, 288, 288, 288, 288, 288, 288, 256, 256, 256,
    256, 240, 240, 240, 225, 225, 216, 216, 216, 200,
    200, 192, 192, 180, 180, 180, 160, 160, 150, 144,
    144, 135, 128, 120, 120, 108, 100, 96, 90, 80,
    72, 72, 64, 60, 54, 45, 40, 36, 25, 18,
)