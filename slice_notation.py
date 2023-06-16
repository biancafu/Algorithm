# [a:b:c]
#counting from a inclusive to b exclusive with c as increment
# In [1]: string = "Howdy doody"

# In [2]: string[::]
# Out[2]: 'Howdy doody'

# In [3]: string[::-1]
# Out[3]: 'ydood ydwoH'

# In [4]: string[0:]    
# Out[4]: 'Howdy doody'

# In [5]: string[0::-1]
# Out[5]: 'H'      is one character, it says "count backwards from index 0 as far as you can". 
#As far as it can is the start of the string

# In [6]: string[:len(string)]
# Out[6]: 'Howdy doody'

#string[0:len(string):-1] or string[0:anything:-1]
#'' since The designated end of the slice cannot be reached from the start. You can think of this as the slice having ended "before" it began (hence is empty), 
#or you can think of the end point being automatically adjusted to be equal to the start point (hence the slice is empty).

# In [7]: string[:len(string):-1]
# Out[7]: ''     # count backwards from the end up to but not including index len(string)". 
#That index can't be reached, so the slice is empty.

# In [8]: string[0:len(string)]
# Out[8]: 'Howdy doody'

# In [9]: string[0:len(string):-1]  or [:0:-1]
# Out[9]: ''     count backwards from the end up to but not including index len(string)". That index can't be reached, so the slice is empty.

# string[:0:-1]/string[0:len(string)-1]
# count backwards from the end up to but not including index 0. So that's all except the first character, reversed.

#string[::-1]/[:]
#everything reversed

#string[-1::-1]
#same as string[::-1] because -1 means the last character of the string.