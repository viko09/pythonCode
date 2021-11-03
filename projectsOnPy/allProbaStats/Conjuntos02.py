# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 14:55:49 2021

@author: luiso
"""

from matplotlib_venn import venn2 
from matplotlib import pyplot as plt

venn2(subsets = (5, 5, 1),set_labels = ('Group A', 'Group B'))
plt.title('$A \cup B$')
plt.savefig('Figure 1.png', dpi=300) # Modificame
plt.show()

venn2(subsets = (5, 5, 0),set_labels = ('Group A', 'Group B'))
plt.title('$A \cap B$')
plt.savefig('Figure 2.png', dpi=300) # Modificame
plt.show()