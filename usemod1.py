#!/usr/bin/env python
# import MODULE
# from pkg.pkg import module
from enmax.epc import utils

#  1.  utils.py in current folder
#  2.  for p in PYTHONPATH paths
#           p/utils.py in any folder in PYTHONPATH
#  3.  utils.py in python installation folders

utils.get_hbi_data()
utils.put_data_in_database()
print(utils.FOODS)
# utils._data_update()

