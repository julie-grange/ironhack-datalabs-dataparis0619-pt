#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

>>>np.__version__
'1.16.2'

>>> np.show_config()
mkl_info:
    libraries = ['mkl_rt', 'pthread']
    library_dirs = ['/Users/julieG/anaconda3/lib']
    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]
    include_dirs = ['/Users/julieG/anaconda3/include']
blas_mkl_info:
    libraries = ['mkl_rt', 'pthread']
    library_dirs = ['/Users/julieG/anaconda3/lib']
    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]
    include_dirs = ['/Users/julieG/anaconda3/include']
blas_opt_info:
    libraries = ['mkl_rt', 'pthread']
    library_dirs = ['/Users/julieG/anaconda3/lib']
    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]
    include_dirs = ['/Users/julieG/anaconda3/include']
lapack_mkl_info:
    libraries = ['mkl_rt', 'pthread']
    library_dirs = ['/Users/julieG/anaconda3/lib']
    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]
    include_dirs = ['/Users/julieG/anaconda3/include']
lapack_opt_info:
    libraries = ['mkl_rt', 'pthread']
    library_dirs = ['/Users/julieG/anaconda3/lib']
    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]
    include_dirs = ['/Users/julieG/anaconda3/include']

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a=np.random.rand(2,3,5)


#4. Print a.

print a


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b=np.ones((5,2,3))


#6. Print b.

print b

#7. Do a and b have the same size? How do you prove that in Python code?


print(a.size)
#30
print(b.size)
#30

#8. Are you able to add a and b? Why or why not?

np.concatenate((a,b))

'''Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: all the input array dimensions except for the concatenation axis must match exactly'''


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
   
c=b.reshape(2,3,5)

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d=np.concatenate((a,c))

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print a

'''a
array([[[0.83752352, 0.92503075, 0.63706233, 0.70404514, 0.9805229 ],
        [0.8667858 , 0.96704892, 0.89851982, 0.24639608, 0.91412845],
        [0.26884669, 0.14857921, 0.13840237, 0.97524027, 0.11651294]],

       [[0.60331656, 0.95556117, 0.42789388, 0.19129437, 0.91093515],
        [0.89833991, 0.03125095, 0.54773063, 0.38287536, 0.59893667],
        [0.47085157, 0.1404829 , 0.87061593, 0.95485128, 0.54483375]]])'''


print d

'''d
array([[[0.83752352, 0.92503075, 0.63706233, 0.70404514, 0.9805229 ],
        [0.8667858 , 0.96704892, 0.89851982, 0.24639608, 0.91412845],
        [0.26884669, 0.14857921, 0.13840237, 0.97524027, 0.11651294]],

       [[0.60331656, 0.95556117, 0.42789388, 0.19129437, 0.91093515],
        [0.89833991, 0.03125095, 0.54773063, 0.38287536, 0.59893667],
        [0.47085157, 0.1404829 , 0.87061593, 0.95485128, 0.54483375]],

       [[1.        , 1.        , 1.        , 1.        , 1.        ],
        [1.        , 1.        , 1.        , 1.        , 1.        ],
        [1.        , 1.        , 1.        , 1.        , 1.        ]],

       [[1.        , 1.        , 1.        , 1.        , 1.        ],
        [1.        , 1.        , 1.        , 1.        , 1.        ],
        [1.        , 1.        , 1.        , 1.        , 1.        ]]])'''

#12. Multiply a and c. Assign the result to e.

e=a*c

#13. Does e equal to a? Why or why not?

Oui, toutes les valeurs de c sont égales à 1 donc quand on les multiplient avec les valeurs de a pour obtenir e ça ne change pas les valeurs (x*1 = x)


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_min=np.min(d)
d_max=np.max(d)
d_mean=np.mean(d)

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f=np.empty(2*3*5)



#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.

for x in f:
    for y in d:
        if y>d_min and y<d_mean:
            x=25
        elif y>d_mean and y<d_max:
            x=75
        elif y==d_mean:
            x=50
print(f)


"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""


"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""