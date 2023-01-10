import numpy as np
import matplotlib.pyplot as plt

def plotvec(*argv, chain=False, labels=False, newfig=True,
            legendloc='best', color_offset=0, width=None,
            square_aspect_ratio=True):
  """ plot a sequence of 2-d vectors

  Uses Matplotlib to plot 2-d vectors as directional arrows. Allows
  chaining sequence of vectors for effects like sums of vectors, and
  allows labeling and color shifting (to coordinate colors of multiple
  calls to plotvec).

  Parameters
  ----------
  *argv: lists or NumPy vectors
         One or more 2-d vectors

  chain: bool, default: False
         Whether to place tail of vector at head of previous vector

  labels: list, tuple, or bool, default: False
         Labels for each vector for use in legend, or False for no labels

  newfig: bool, default: True
         Whether to open a new figure for this plot (else plot on current fig)

  legendloc: string or int, default: 'best'
         Argument for legend location passed to Matplotlib

  color_offset: int, default: 0
         Shift color sequence by fixed value

  width: None or number
         Width of arrow shaft, also affects head size. Typically float around
         0.005 times the width of the plot.

  square_aspect_ratio: book, default: True
         If True (default), make plots square; otherwise, default aspect ratio

  Returns
  ----------
  None

  """

  xmin=0
  xmax=-1000000
  ymin=0
  ymax=-1000000
  origin=[0,0]
  if newfig:
    plt.figure()

  # Plot the vectors
  for i, head in enumerate(argv):
    if type(labels) == bool:
      plt.quiver(*origin, *head, width=width, 
                 angles='xy',scale_units='xy',scale=1,
                 color='C'+str(i+color_offset))
    else:
      plt.quiver(*origin, *head, width=width, 
                 angles='xy',scale_units='xy',scale=1,
                 color='C'+str(i+color_offset), label=labels[i])
    xmin=min(xmin,head[0])
    xmax=max(xmax,head[0])
    ymin=min(ymin,head[1])
    ymax=max(ymax,head[1])
    if chain:
      origin = head


  # Set limits based on vector dimensions and add axis lines
  plt.xlim(min(-1, xmin-1), max(1,xmax+1))
  plt.ylim(min(-1,ymin-1),max(1,ymax+1))
  plt.hlines(0, min(-1, xmin-1), max(1,xmax+1), 'k', linewidth=0.5, alpha=0.5)
  plt.vlines(0, min(-1,ymin-1),max(1,ymax+1), 'k', linewidth=0.5, alpha=0.5)

  # Set aspect ratio to square if requested
  if square_aspect_ratio:
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')

  # Add legend if user passed labels
  if type(labels) != bool:
    plt.legend(loc=legendloc);
