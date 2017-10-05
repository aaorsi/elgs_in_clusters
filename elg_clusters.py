import os

jplus_dir         =  '/home/CEFCA/aaorsi/work/j-plus/'
elg_analysis_dir  = '/home/CEFCA/aaorsi/work/elg_jplus/'
elgdata           = '%s/out/elgs.dat' % elg_analysis_dir
redmapper_dir     = '/home/CEFCA/aaorsi/work/redmapper/'
redmapperdata     = redmapper_dir + 'redmapper_dr8_public_v6.3_catalog.fits'
tilesdata         = '%s/tiles/tiles_data.tsv' % elg_analysis_dir


cwd = os.getcwd()

import sys

sys.path.append(jplus_dir)
sys.path.append(elg_analysis_dir)

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from astropy.io import fits

import jplus
import elg_analysis as elg
import elgtools as tools_elg
import learn_elgs as learn_elg
import pickle


def load_catalogues(elgfile = elgdata, centralobj = redmapperdata, centralobjtype = 'fits', xmatchtiles=True):
# Function to load elgs and redmapper catalogues
  
  elgs = pickle.load(open(elgfile))
  print 'ELG catalogue loaded'

  if centralobjtype == 'fits':
    raw_central = fits.open(centralobj)
    central     = raw_central[1].data
  
  print 'central objects loaded'

  if xmatchtiles:
  # Select only those central objects 
  # near a J-PLUS tile
  
    t_info = np.loadtxt(tilesdata)
    print 'tiles info read'
    
    elgtiles = np.unique(elgs['tile_id'])
    ntiles = len(elgtiles)
    print 'ELG sample is contained in %d tiles' % ntiles

    for i in range(ntiles):
      idt = np.where(elgtiles[i] == t_info[:,0])
      rat = t_info[idt,1]
      dect = t_info[idt,2]
      tile_scale = 1.40
      
      idcen = []
      
      # Loop to determine which central objects are in the footprint of J-PLUS ELGs (TODO)
      for j in range()




  
