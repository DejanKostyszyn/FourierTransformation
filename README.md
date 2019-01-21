# FourierTransformation
A program to plot fourier transformations in python3 by Dejan Kostyszyn.

## Requirements
To run the program, the following requirements are necessary to be installed:
[Python3]{https://www.python.org/}, [NumPy]{http://www.numpy.org/}, [Matplotlib]{https://matplotlib.org/} and [Jupyter Notebook]{https://jupyter.org/} 

## Run the program
1. Change into the folder, where you saved the <code>FourierTransformation.ipynb</code> and run <code>jupyter-notebook<code>.
2. The Browser will show a menu, where you will find the file <code>FourierTransformation.ipynb</code>. Click on it.
3. On the top menu click 'Cell -> Run All'

## Alter the program
If you want to calculate another function, simply alter line 13. The functions either have to be [NumPy]{http://www.numpy.org/} functions, or you must include the according libraries. E.g. the [math]{https://docs.python.org/3/library/math.html} module.

### Example 1
Change
<code>return x</code>
to
<code>return np.exp(-x)</code>

### Example 2
Change
<code>return x</code>
to
<code>if(x < 0):
        return 0
    else:
        return x</code>
