import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def plot_field (matrix=np.eye(2), field_width=3, point_spacing=0.5,
                preserve_axes=True, colormap='plasma'):

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
  '''

  assert matrix.shape == (2,2), "matrix argument must be a 2x2 array"

  cmap = mpl.colormaps[colormap]

  xs = np.arange(-field_width, field_width + point_spacing,
                 point_spacing)
  ys = xs

  for x in xs:
    for y in ys:
      angle = np.arctan2(y, x) 
      if angle < 0:
        angle += 2*np.pi
      rgba = cmap(angle / (2 * np.pi)   ) 
      out = matrix @ np.array([x, y])
      plt.scatter(out[0], out[1], 2, color=rgba)

  ax = plt.gca()
  ax.axis('equal')
  if preserve_axes:
    plt.xlim(-field_width, field_width)
    plt.ylim(-field_width, field_width)
