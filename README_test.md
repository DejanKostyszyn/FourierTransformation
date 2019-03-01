# FourierTransformation
A program to plot [fourier transformations](https://doi.org/10.1016/B978-044450871-3/50107-8) in python3 by Dejan Kostyszyn.
## Requirements
To run the program, the following requirements are necessary to be installed:
[Python3](https://www.python.org/Python3), [NumPy](http://www.numpy.org/), [Matplotlib](https://matplotlib.org/) and [Jupyter Notebook](https://jupyter.org/) 
## Run the program
1. Change into the folder, where you saved the ```FourierTransformation.ipynb``` and run ```jupyter-notebook```.
1. The Browser will show a menu, where you will find the file ```FourierTransformation.ipynb```. Click on it.
1. On the top menu click 'Cell -> Run All'
## Alter the program
If you want to calculate another function, simply alter line 13. The functions either have to be [NumPy](http://www.numpy.org/) functions, or you must include the according libraries. E.g. the [math](https://docs.python.org/3/library/math.html) module.

In case you want to alter f(x), make sure that f(x) fits Dirichlets conditions:

* ![](https://tex.s2cms.ru/svg/%24f%28x%29%20%3D%20f%28x%20%2B%202pi%29%24)
* ![](https://tex.s2cms.ru/svg/%24f%28x%29%24) is in ![](https://tex.s2cms.ru/svg/%24%28-pi%2C%20pi%29%24) in finitely many intervals static and monotone
* If f is not static in ![](https://tex.s2cms.ru/svg/%24x_0%24), then ![](https://tex.s2cms.ru/svg/%24f%28x_0%29%20%3D%20%28f%28x_0%20-%200%29%20%2B%20f%28x_0%20%2B%200%29%29/2%24)

### Alter f(x): Example 1
Change
```return x```
to
```return np.exp(-x)```
### Alter f(x): Example 2
Change ```return x``` to
```
if(x < 0):
        return 0
else:
        return x
```
### Alter n
If you want to alter the depth of the approximation, you can simply alter ```n``` in line 9. It is required that n is a numpy array, i.e. you can **not** simply write ```n = 100```. Instead you have to write ```n = np.array([v])```, if you want to use only one value ```v``` of datatype ```int16```.


If you find any mistakes, please feel free to contact me.