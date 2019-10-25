#!/usr/bin/env python
# coding: utf-8

# # Chapter 16 Examples

# In[38]:


# %load ../EXAMPLES/np_create_arrays.py
#!/usr/bin/env python
import numpy as np

a = np.array([[1, 2.1, 3], [4, 5, 6], [7, 8, 9], [20, 30, 40]])  # <1>
print(a)
print("# dims", a.ndim)  # <2>
print("shape", a.shape)  # <3>
print()

a_zeros = np.zeros((3, 5), dtype=np.uint32)  # <4>
print(a_zeros)
print()

a_ones = np.ones((2, 3, 4, 5))  # <5>
print(a_ones)
print()

# with uninitialized values
a_empty = np.empty((3, 8))  # <6>
print(a_empty)

print(a.dtype)  # <7>

nan_array = np.full((5, 10), np.NaN)  # <8>
print(nan_array)


# In[39]:


a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [20, 30, 40]]) 
a


# In[40]:


a[0], a[1], a[-1]


# In[41]:


print(a.ndim, a.shape)


# In[42]:


a_zeros = np.zeros((3, 5, 10), dtype=np.uint32)  # <4>
a_zeros


# In[43]:


print(a_zeros.shape)


# In[44]:


a_ones = np.ones((4, 4))


# In[45]:


a_ones


# In[46]:


a_un = np.empty((10, 2))
a_un


# In[47]:


nan_array = np.full((3,3,3), np.NaN)
nan_array


# In[48]:


np.arange(10)


# In[49]:


# np.arange(START, STOP, STEP)  np.arange(STOP) np.arange(START,STOP)
np.arange(1,11)


# In[50]:


np.arange(1,2.1, .1)


# In[51]:


np.linspace(1, 50, 5)


# In[52]:


np.linspace(1, 10, 200)


# In[53]:


# %load ../EXAMPLES/np_basic_array_ops.py
#!/usr/bin/env python
import numpy as np

a = np.array(
    [
        [5, 10, 15],
        [2, 4, 6],
        [3, 6, 9, ],
    ]
)  # <1>

b = np.array(
    [
        [10, 85, 92],
        [77, 16, 14],
        [19, 52, 23],
    ]
)  # <2>
print("a")
print(a)
print()
print("b")
print(b)
print()

print("a * 10")
print(a * 10)  # <3>
print()

print("a + b")
print(a + b)  # <4>
print()

print("b + 3")
print(b + 3)  # <5>
print()

s1 = a.sum()  # <6>
s2 = b.sum()  # <6>
print("sum of a is {0}; sum of b is {1}".format(s1, s2))
print()

a += 1000  # <7>
print(a)


# In[54]:


a


# In[55]:


b


# In[56]:


a + b


# In[57]:


a @ b


# In[58]:


a * b


# In[59]:


a + 1
a


# In[60]:


a += 1
a


# In[62]:


a


# In[63]:


a.sum()


# In[64]:


a[0].sum()


# In[65]:


a.shape


# In[66]:


b.shape


# In[67]:


x = np.ones((4, 10))


# In[68]:


x


# In[69]:


x.size


# In[70]:


x.ndim


# In[71]:


x.shape = 10, 4
x


# In[72]:


a


# In[73]:


a.transpose()


# In[74]:


a.ravel()


# In[75]:


np.linalg.inv(a)


# In[102]:


# %load ../EXAMPLES/np_indexing.py
#!/usr/bin/env python
import numpy as np

a = np.array(
    [[70, 31, 21, 76, 19, 5, 54, 66],
     [23, 29, 71, 12, 27, 74, 65, 73],
     [11, 84, 7, 10, 31, 50, 11, 98],
     [25, 13, 43, 1, 31, 52, 41, 90],
     [75, 37, 11, 62, 35, 76, 38, 4]]
)  # <1>

print(a)
print()

print('a[0] =>', a[0])  # <2>
print('a[0][0] =>', a[0][0])  # <3>
print('a[0,0] =>', a[0, 0])  # <4>
print('a[0,:3] =>', a[0, :3])  # <5>
print('a[0,::2] =>', a[0, ::2])  # <6>
print()
print('a[::2] =>', a[::2])  # <7>
print()
print('a[:3, -2:] =>', a[:3, -2:])  # <8>


# In[78]:


a


# In[79]:


a[0]


# In[80]:


a[0][0], a[0,0]


# In[81]:


a[-1,-1]


# In[82]:


a[0,:3]


# In[83]:


a


# In[84]:


a[a,:3]


# In[86]:


a[:,0]


# In[87]:


a[:,:2]


# In[90]:


big_array = np.ones((10000000,2))
big_array


# In[91]:


big_array.size


# In[92]:


a


# In[94]:


#  ARRAY[row-or-row-slize, col-or-col-slice]
a[:3,-3:]


# In[95]:


a


# In[96]:


a > 70


# In[97]:


a == 76


# In[98]:


a


# In[99]:


a[a > 70] *= 100
a


# In[100]:


i = a > 70
i


# In[101]:


a[i]


# In[103]:


a


# In[104]:


a[i]


# In[ ]:


# %load ../EXAMPLES/np_stacking.py
#!/usr/bin/env python
import numpy as np

a = np.array(
    [[70, 31, 21, 76, 19, 5, 54, 66],
     [23, 29, 71, 12, 27, 74, 65, 73]]
)  # <1>

b = np.array(
    [[11, 84, 7, 10, 31, 50, 11, 98],
     [25, 13, 43, 1, 31, 52, 41, 90]]
)  # <2>

print('a =>\n', a)
print()
print('b =>\n', b)
print()
print('vstack((a,b)) =>\n', np.vstack((a, b)))  # <3>
print()

print('vstack((a,a[0] + a[1])) =>\n', np.vstack((a, a[0] + a[1])))  # <4>
print()

print('hstack((a,b)) =>\n', np.hstack((a, b)))  # <5>


# In[106]:


a


# In[107]:


b


# In[108]:


a = np.array(
    [[70, 31, 21, 76, 19, 5, 54, 66],
     [23, 29, 71, 12, 27, 74, 65, 73]]
)  # <1>

b = np.array(
    [[11, 84, 7, 10, 31, 50, 11, 98],
     [25, 13, 43, 1, 31, 52, 41, 90]]
)  # <2


# In[109]:


a


# In[110]:


b


# In[113]:


np.vstack((a, b))


# In[114]:


np.hstack((a, b))


# In[117]:


for value in a.flat:  # or a.flatten()
    print(value)


# In[130]:


x = np.full((5, 3), 42.)
x


# In[131]:


print(x.size, x.ndim, x.shape, x.dtype)


# In[ ]:




