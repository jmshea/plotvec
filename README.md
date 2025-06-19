# Making Attractive 2-D Vector Diagrams in Python with PlotVec

*How do I make attractive vector diagrams in Python?* PlotVec makes plotting vectors easier.  PlotVec was created to enable interactive quizzes for readers of my book [*Foundations of Data Science with Python*](https://amzn.to/48cYila) [Affilate Link]

(Note that the figures below use my matplotlibrc file, which is included in the GitHub repository for plotvec.)

Let's start by loading the `plotvec()` function and plotting a single vector:


$$
\mathbf{a} = [2,3]^T
$$



```python
import numpy as np
from plotvec import plotvec

a = np.array([2, 3])

plotvec(a)
```


    
![plotvec() output showing a graph of a single vector \[2, 3\]](figs/output_2_0.png)
    


We can add multiple vectors to the diagram easily. Let's add these vectors:

$$
\mathbf{b} =[1,-2]^T 
$$

$$
\mathbf{c} =[-1,-1]^T
$$


```python
a = np.array([2, 3])
b = np.array([1, -2])
c = np.array([-2, -1])

plotvec(a, b, c)
```


    
![plotvec() output showing a graph of three vectors that point in different directions](figs/output_4_0.png)
    


Note that by default `plotvec()` uses an equal aspect ratio -- this is important in many vector diagrams, for instance to tell whether two vectors are orthogonal. For instance, in the diagram above, vectors `b` and `c` are at 90 degree angles because they are orthogonal.

If an equal aspect ratio is not needed, `plotvecR()` can be used to plot vectors but orthogonal vectors will not necessarily be at 90 degree angles:


```python
from plotvec import plotvecR

plotvecR(a, b, c)
```


    
![plotvec() output showing a graph of three vectors without an equal aspect ratio](figs/output_6_0.png)
    


A legend can be added by specifying labels:


```python
import numpy as np
from plotvec import plotvec, plotvecR

a = np.array([2, 3])
b = np.array([1, -2])

plotvecR(a, b,
        labels = ['$\mathbf{a} = [ 2,3]^T$',
                  '$\mathbf{b} = [ 1, -2]^T$'],
        legendloc='upper left')
```


    
![plotvec() output showing a graph of two vectors with captions](figs/output_8_0.png)
    


By default, vectors will be plotted with their tails at the origin (0,0).  We can specify a different tail using the `tail` keyword argument:


```python
plotvec(c, tail=[2,1])
```


    
![plotvec() output showing a graph of a vector with the tail not at the origin](figs/output_10_0.png)
    


When plotting a sequence of vectors, we can have the tail of each vector be positioned at the head of the previous vector by settin `chain=True`:


```python
plotvec(a, b, c, chain=True)
```


    
![plotvec() output showing a graph of three "chained" vectors with each subsequent vector's tail at the previous vector's head](figs/output_12_0.png)
    


When plotting with `chain=True`, the head of the last vector is at the position of the sum of the vectors. We can ask `plotvec()` to show this sum as a vector using `plotsum=True`:


```python
plotvec(a, b, c, chain=True, plotsum=True)
```


    
![plotvec() showing a graph of three chained vectors and the vector sum](figs/output_14_0.png)
    


You can combine plot the result of multiple `plotvec()` commands on the same axes by specifying `newfig=False`. When using this option, it is good to either specify the colors of the vectors or else use the `color_offset` keyword parameter to tell later calls where to start in the color cycle. The example below also shows how to use `plot.annotate()` to label vectors:


```python
import matplotlib.pyplot as plt

plotvec([3,0], [0,4], chain=True);
plotvec([3,4], newfig=False, color_offset=2)
plt.annotate('3', (1.6, 0.1) );
plt.annotate('4', (3.1, 1.8) );
plt.annotate('5', (1.1, 1.9) );
```


    
![Example of multiple calls of plotvec() using a single output figure](figs/output_16_0.png)
    

## Illustrating the Effects of Two-dimensional Linear Transforms

When an $n$-vector is left-multiplied by a $m \times n$ matrix, the output is an $m$-vector. Since we can do this for every possible $n$-vector, and the outputs will fill some subspace of all $m$-vectors, we consider the matrix to define a linear transformation from the real $n$-vectors to the real $m$-vectors.

This is most easily visualized for linear transformations from $2$-vectors to other $2$-vectors, which is defined by a $2 \times 2$ matrix. 

PlotVec has two functions to help visualize such transformations.

A linear transformation of a 2-vector to another 2-vector can be considered to consist of a rotation and a scaling of the original vector. Because the transformation is linear, the amount of rotation and scaling only depends on the *direction* of the input vector and not the length of that vector. Thus, one way to visualize the effect of a linear transformation is to show how it rotates and scales all of the unit vectors. This is the purpose of the `transform_unit_vecs()` function. Its call signature is

`transform_unit_vecs(matrix, num_vectors=16, colormap='plasma', show_input_vecs=True)`

The most important argument is the only required one: the `matrix`. Let's illustrate the output for the following matrix:


```python
M = np.array([[0.5, -4],
              [-2,  3]])
```


```python
from plotvec import transform_unit_vecs

transform_unit_vecs(M)
```


    
![Output of call to transform_unit_vecs(): left graph is 16 unit vectors evenly spaced in phase; right graph is transformed output vectors, with nonuniform angles and lengths ](figs/output_21_0.png)
    


The left graph shows 16 unit vectors that are color-coded and uniformly spaced in phase. The right graph shows the 16-output vectors from left-multiplying the input vectors by the given matrix. The colors of the output vectors match the colors of the corresponding input vectors. By inspecting the input and output vectors, you can see that different input vectors are scaled and rotated by different amounts. 

Another way to think about a linear transformation is think about it as stretching, rotating, and flipping space. We can visualize this by creating a field of points and then showing the location of those points after the transformation. PlotVec has a `transform_field()` function to do this. Again, it uses colors to indicate corresponding input and output points. 

The code below use `transform_field()` to generate a uniformly spaced, rectangular set of input points and to show both these input points and the output points after the linear transformation using the `M` matrix in the example above. It sets the `preserve_axes` argument to `False` to allow the axes to expand to fit the output points, which occupy much more space then the input points.



```python
from plotvec import transform_field

transform_field(M, preserve_axes=False)
```


    
![Output of transform_field(): left graphs shows rectangular field of points; right graph is output field of points, which is in shape of parallelogram](figs/output_24_0.png)
    


The graphs show that the rectangular field of input points (on the left) is transformed into a parallelogram of points at the output (on the right).


**As an Amazon Associate I earn from qualifying purchases.**

