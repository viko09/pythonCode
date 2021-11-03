# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 14:55:49 2021

@author: luiso
"""

from matplotlib_venn import venn2, venn2_circles
from matplotlib import pyplot as plt

# Ejemplo 1
A = set([1,2,3,4]) 
B = set([4,5,6,7]) 


v = venn2([A, B],('A', 'B')) 
c = venn2_circles([A, B], linestyle='solid')

plt.savefig('Figure 1.png', dpi=300) # Modificame
plt.title('Figura 1')
plt.show()

# Ejemplo 2
# {A,B,AB}
v = venn2({'10': 1, '01': 1, '11': 1}, ('A', 'B')) 
c = venn2_circles((1, 1, 1), linestyle='solid')

v.get_patch_by_id('10').set_alpha(0.1)
v.get_patch_by_id('10').set_color('b')
v.get_patch_by_id('01').set_color('white')
v.get_patch_by_id('11').set_color('g')

#v.get_label_by_id('10').set_text('')
#v.get_label_by_id('01').set_text('')
#v.get_label_by_id('11').set_text('')

plt.title('Figura 2')
plt.savefig('Figure 2.png', dpi=300) # Modificame
plt.show()


# Ejemplo 3
v = venn2({'10': 1, '01': 1, '11': 1}, ('A', 'B')) 
c = venn2_circles((1, 1, 1), linestyle='solid')

v.get_patch_by_id('10').set_color('white')
v.get_patch_by_id('01').set_color('white')
v.get_patch_by_id('11').set_color('g')

v.get_label_by_id('10').set_text('')
v.get_label_by_id('01').set_text('')
v.get_label_by_id('11').set_text('')

plt.title('Figura 3')
plt.savefig('Figure 3.png', dpi=300) # Modificame
plt.show()


# Ejemplo 4
v = venn2({'10': 1, '01': 0, '11': 1}, ('A', 'B')) 
c = venn2_circles((1, 0, 1), linestyle='solid')

v.get_patch_by_id('10').set_color('b')
v.get_patch_by_id('11').set_color('g')

v.get_label_by_id('10').set_text('')
v.get_label_by_id('01').set_text('')
v.get_label_by_id('11').set_text('')

plt.title('Figura 4')
plt.savefig('Figure 4.png', dpi=300) # Modificame
plt.show()
