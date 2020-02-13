#!/dls_sw/tools/bin/python2.4

import sys, os, re
from motorhome import *

# find the plc number and name from the filename
filename = sys.argv[1]
result = re.search(r"PLC(\d+)_([^_]*)_HM\.pmc", filename)
if result is not None:
    num, name = result.groups()
else:
    sys.stderr.write("***Error: Incorrectly formed homing plc filename: %s\n" % filename)
    sys.exit(1)

################# BL04I-MO-PMAC-01 ###################

if name == "QBPM1":
    plc = PLC(int(num), post = -400,ctype=PMAC)
    plc.add_motor(11, group=2, htype = RLIM, jdist = 0)
elif name == "HFM":
    plc = PLC(int(num), post = None,ctype=PMAC)
    for axis in (17,18,19): # All 3 jacks grouped together
        plc.add_motor(axis, group=2, htype = HSW_HLIM, jdist=-5000)
    for axis in (29,30): # Both translations grouped together
        plc.add_motor(axis, group=3, htype = HSW_HLIM, jdist=-5000)
elif name == "VFM":
    plc = PLC(int(num), post = None,ctype=PMAC)
    for axis in (25,26,27): # All 3 jacks grouped together
        plc.add_motor(axis, group=2, htype = HSW_HLIM, jdist=-5000)
    for axis in (31,32): # Both translations grouped together
        plc.add_motor(axis, group=3, htype = HSW_HLIM, jdist=-5000)
elif name == "QBPM2":
    plc = PLC(int(num), post = None,ctype=PMAC)
    plc.add_motor(16, group=2, htype = RLIM, jdist = 0)

################# BL04I-MO-PMAC-02 ###################

elif name == "DET":
    plc = PLC(int(num), post = None,ctype=PMAC)
    for axis in (1,2): # Both translations grouped together
        plc.add_motor(axis, group=2, htype=HSW_HLIM, jdist=1000)
    plc.add_motor(21, group=3, htype=HSW_HLIM, jdist=1000)
    plc.add_motor(22, group=4, htype=HSW_HLIM, jdist=1000)
elif name == "TABLE":
    plc = PLC(int(num), post = None,ctype=PMAC)
    for axis in (6,7,8): # All 3 jacks grouped together
        plc.add_motor(axis, group=3, htype = HSW_HLIM, jdist = 5000)
    for axis in (17,18): # Both translations grouped together
        plc.add_motor(axis, group=2, htype = HSW_HLIM, jdist = 1000)
elif name == "GONP":
    plc = PLC(int(num), post = None,ctype=PMAC)
    plc.add_motor(3, group=2, htype = HSW, jdist = 10000)
    plc.add_motor(4, group=3, htype = HSW, jdist = -10000)
    plc.add_motor(5, group=4, htype = HSW, jdist = 10000)
elif name == "OMEGA":
    plc = PLC(int(num), post = None,ctype=PMAC)
    plc.add_motor(31, group=2, htype = HOME, jdist = 0)

################# BL04I-MO-STEP-01 ###################

elif name == "BSX":
    plc = PLC(int(num), post = None,ctype=GEOBRICK)
    plc.add_motor(1, group=2, htype=HOME, jdist=0)
elif name == "MAPTXZ":
    plc = PLC(int(num), post = None,ctype=GEOBRICK)
    plc.add_motor(2, group=2, htype=HOME, jdist=0)
    plc.add_motor(3, group=3, htype=HOME, jdist=0)
elif name == "SCAT":
    plc = PLC(int(num), post = None,ctype=GEOBRICK)
    plc.add_motor(4, group=2, htype=HOME, jdist=0)
    plc.add_motor(5, group=3, htype=HOME, jdist=0)
elif name == "PLATE":
    plc = PLC(int(num), post = None,ctype=GEOBRICK)
    plc.add_motor(7, group=2, htype=HOME, jdist=0)
    plc.add_motor(8, group=3, htype=HOME, jdist=0)

################# BL04I-MO-STEP-02 ###################

elif name == "SCIN":
    plc = PLC(int(num), post = None,ctype=GEOBRICK)
    plc.add_motor(1, group=2, htype=RLIM, jdist=0)
    plc.add_motor(2, group=3, htype=RLIM, jdist=0)
elif name == "S4":
    plc = PLC(int(num), post = None,ctype=GEOBRICK)
    plc.add_motor(3, group=3, htype=RLIM, jdist=0)
    plc.add_motor(4, group=2, htype=RLIM, jdist=0)
    plc.add_motor(5, group=5, htype=RLIM, jdist=0)
    plc.add_motor(6, group=4, htype=RLIM, jdist=0)
elif name == "MAPTY":
    plc = PLC(int(num), post = None,ctype=GEOBRICK)
    plc.add_motor(7, group=2, htype=HSW, jdist=1000)

################# BL04I-MO-STEP-03 ###################

elif name == "BSYZ":
    plc = PLC(int(num), post = None,ctype=GEOBRICK)
    plc.add_motor(1, group=2, htype=HSW, jdist=1000)
    plc.add_motor(2, group=3, htype=HSW, jdist=1000)
elif name == "SAMP":
    plc = PLC(int(num), post = None,ctype=GEOBRICK)
    plc.add_motor(3, group=2, htype=RLIM, jdist=0)
    plc.add_motor(4, group=3, htype=RLIM, jdist=0)
elif name == "MINIKAPPA":
    plc = PLC(int(num), post = None,ctype=GEOBRICK)
    plc.add_motor(6, group=2, htype=RLIM, jdist=0)

################# BL04I-MO-STEP-04 ###################

elif name == "CRL":
    plc = PLC(int(num), post = None,ctype=GEOBRICK)
    plc.add_motor(1, group=2, htype=HSW, jdist=1000)
    plc.add_motor(2, group=3, htype=HSW, jdist=2000)
    plc.add_motor(3, group=4, htype=HSW, jdist=1000)
    plc.add_motor(4, group=5, htype=HSW, jdist=-1000)
    plc.add_motor(5, group=6, htype=HSW, jdist=-1000)
elif name == "FSWT":
    plc = PLC(int(num), post = None,ctype=GEOBRICK)
    for axis in (1,2): # Both X axes grouped together
        plc.add_motor(axis, group=2, htype=RLIM, jdist=0)
    for axis in (3,4): # Both Y axes grouped together
        plc.add_motor(axis, group=3, htype=RLIM, jdist=0)

################# BL04I-MO-STEP-06 ###################

elif name == "DCM":
    plc = PLC(int(num), post = None,ctype=GEOBRICK)
    plc.add_motor(1, group=2, htype=HSW_HLIM, jdist=-100000)
    plc.add_motor(5, group=3, htype=HSW_HLIM, jdist=-1000)
    plc.add_motor(3, group=4, htype=HSW_HLIM, jdist=20000)
    plc.add_motor(4, group=5, htype=HSW_HLIM, jdist=-1000)

######################################################

else:
    sys.stderr.write("***Error: Can't make homing PLC %d for %s\n" % (num, name))
    sys.exit(1)

# write out the plc
plc.write(filename)

