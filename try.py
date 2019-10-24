"""
Created on Dday , Oct 32, 2109

Author: Dear

"""

import pandas as pd
import glob, os, os.path, ntpath, shutil
import numpy as np


UE = r"D:\Dropbox (UXO-India)\UN_Habitat_Project\Analysis data\output"
Lo = r"D:\Dropbox (UXO-India)\Atlas_of_Urbanization_updation_Oct_2017"
Ar = r"D:\Dropbox (UXO-India)\UN_Habitat_Project\#UXO_Arterial_Revesion\#CityWise_Arterial_shapefiles"


for folder in os.listdir(UE):
    print folder

    Out_f = r"G:\#WRI_Locale_arrangment\Test"

    arterial= r"%s\%s\%s_Arterial" %(Out_f, folder, folder)
    T0 = r"%s\%s\%s_T0" %(Out_f, folder, folder)
    T1_T3 = r"%s\%s\%s_T1_T3" %(Out_f, folder, folder)

    if not os.path.exists(arterial):
        os.makedirs(arterial)

    if not os.path.exists(T0):
        os.makedirs(T0)

    if not os.path.exists(T1_T3):
        os.makedirs(T1_T3)

    t0_files = glob.glob(r"%s\T0_locals_with_excel\%s\*.*" % (Lo,folder))
    t1_t3_files = glob.glob(r"%s\T1_T2_locals_with_excel\%s\*.*" % (Lo,folder))

    for t0_f in t0_files:
        print t0_f
        shutil.copy(t0_f,T0)

    for t1_t3_f in t1_t3_files:
        print t1_t3_f
        shutil.copy(t1_t3_f,T1_T3)
    try:
        ar_files = glob.glob(r"%s\%s_Arterial\SHP\%s_Master_AR_medians.*" % (Ar, folder,folder))
        for ar in ar_files:
            print ar
            shutil.copy(ar, arterial)
    except:
        pass
            
