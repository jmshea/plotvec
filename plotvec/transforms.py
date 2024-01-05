import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from .plotvec import plotvec

def transform_unit_vecs(matrix, num_vectors=16, colormap='plasma', show_input_vecs=True):
  ''' Plot the outputs of a linear transform on radial unit vectors

  Generates unit vectors that are uniformly spaced in angle around the
  origin, applies the linear transform to the vectors, and plots the
  input vectors and output vectors

  Parameters
  ----------
  matrix : ndarray
    2D matrix that specifies the linear transform

  num_vectors: int
    number of vectors 

  colormap: string
    Matplotlib colormap

  show_input_vecs: boolean
    Whether to include a subplot with the points before the transformation
  '''

  assert matrix.shape == (2,2), "matrix argument must be a 2x2 array"
  unit_vectors = np.zeros((num_vectors,2))


  cmap = mpl.colormaps[colormap]

  if show_input_vecs:
    fig, axs = plt.subplots(1, 2, figsize=(8,4) )
  else: 
    fig, ax = plt.subplots(1, 1)
    axs = [ax]

  # Calculate and plot unit vectors
  plt.sca(axs[0])
  for i in range(num_vectors):
    unit_vectors[i] = [np.cos(2*np.pi*i/num_vectors), np.sin(2*np.pi*i/num_vectors)  ]
    rgba=cmap(i/num_vectors)
    if show_input_vecs:
      plotvec(unit_vectors[i], colors=[rgba], newfig=False)

  if show_input_vecs:
    plt. xlim(-1.1, 1.1)
    plt. ylim(-1.1, 1.1);
    plt.title('16 unit vectors evenly spaced\naround the unit circle')

  # Calculate and plot transformed vectors
  plt.sca(axs[-1])
  for i, vector in enumerate(unit_vectors):
    rgba=cmap(i/num_vectors)
    plotvec(matrix @ vector, colors=[rgba], newfig=False)

  plt.xlim(-4,4)
  plt.ylim(-4,4);
  plt.hlines(0,-4,4, 'k', linewidth=0.5)
  if show_input_vecs:
    plt.title('vectors Output when unit vectors\nare left-multiplied by matrix')

  plt.tight_layout()




def transform_field (matrix=np.eye(2), field_width=3, point_spacing=0.5,
                     preserve_axes=True, colormap='plasma', show_input_vecs=True):

  ''' Plot the outputs of a linear transform on a square field of points

  Generates a uniformly spaced field of points in a 2-D square,
  applies the linear transform to the points, and plots the
  field of output points

  Parameters
  ----------
  matrix : ndarray
    2D matrix that specifies the linear transform

  field_width: number
    size of input point field in each dimension

  point_spacing: number
    spacing between field points in each dimension

  preserve_axes: boolean
    keep limits of output axes same as input space

  colormap: string
    Matplotlib colormap

  show_input_vecs: boolean
    Whether to include a subplot with the points before the transformation
  '''

  assert matrix.shape == (2,2), "matrix argument must be a 2x2 array"

  # No need to output 2 graphs of same thing
  if np.all( matrix == np.eye(2) ):
    show_input_vecs=False

  cmap = mpl.colormaps[colormap]

  xs = np.arange(-field_width, field_width + point_spacing,
                 point_spacing)
  ys = xs

  if show_input_vecs:
    fig, axs = plt.subplots(1, 2, figsize=(8, 4))
  else:
    fig, ax = plt.subplots(1, 1)
    axs = [ax]

  for x in xs:
    for y in ys:
      angle = np.arctan2(y, x) 
      if angle < 0:
        angle += 2*np.pi
      rgba = cmap(angle / (2 * np.pi)   ) 
      if show_input_vecs:
        axs[0].scatter(x,y, 2, color=rgba)
      out = matrix @ np.array([x, y])
      axs[-1].scatter(out[0], out[1], 2, color=rgba)
      plt.scatter(out[0], out[1], 2, color=rgba)

  axs[0].axis('equal')
  axs[-1].axis('equal')
  if preserve_axes:
    plt.xlim(-field_width, field_width)
    plt.ylim(-field_width, field_width)

  if show_input_vecs:
    axs[0].set_title('Square grid of input points')
    axs[1].set_title('Points tranformed by left-multiplication by matrix')
    plt.tight_layout()
