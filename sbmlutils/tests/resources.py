"""
Definition of data and files for the tests.
The files are located in the resources directory.
"""
import os
from os.path import join as pjoin

# get the directories of the tests & the test resources
test_dir = os.path.dirname(os.path.abspath(__file__))
resources_dir = os.path.abspath(pjoin(pjoin(test_dir, os.pardir), os.pardir))
resources_dir = pjoin(resources_dir, 'resources')


################################################################
# comp
################################################################
# ExternalModelDefinitions
DFBA_EMD_SBML = pjoin(resources_dir, 'dfba/diauxic_top.xml')

################################################################
# Data
################################################################
csv_filepath = pjoin(resources_dir, 'data', 'test.csv')


################################################################
# Models
################################################################
BASIC_SBML = pjoin(resources_dir, 'models/basic/basic_7.xml')

# demo -----------------------
DEMO_SBML = pjoin(resources_dir, 'models/demo/Koenig_demo_12.xml')
DEMO_SBML_NO_ANNOTATIONS = pjoin(resources_dir, 'models/demo/Koenig_demo_12_no_annotations.xml')
DEMO_ANNOTATIONS = pjoin(resources_dir, 'models/demo/demo_annotations.xlsx.csv')

# galactose ------------------
GALACTOSE_SINGLECELL_SBML = pjoin(resources_dir, 'models/galactose/galactose_30.xml')
GALACTOSE_SINGLECELL_SBML_NO_ANNOTATIONS = pjoin(resources_dir, 'models/galactose/galactose_30_no_annotations.xml')
GALACTOSE_TISSUE_SBML = pjoin(resources_dir, 'models/galactose/Galactose_v128_Nc20_dilution.xml')
GALACTOSE_ANNOTATIONS = pjoin(resources_dir, 'models/galactose/galactose_annotations.xlsx.csv')

# glucose ------------------
GLUCOSE_SBML = pjoin(resources_dir, 'models/glucose/Hepatic_glucose_3.xml')

# van_der_pol ---------------
VDP_SBML = pjoin(resources_dir, 'models/van_der_pol/van_der_pol.xml')