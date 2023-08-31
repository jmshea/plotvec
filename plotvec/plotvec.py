import numpy as np
import matplotlib.pyplot as plt

def plotvec(*argv, tail=[0,0], chain=False, labels=None, newfig=True,
            legendloc='best', colors= None, color_offset=0, alpha=1,
            width=None, square_aspect_ratio=True, plotsum=False):
  """ plot a sequence of 2-d vectors

  Uses Matplotlib to plot 2-d vectors as directional arrows. Allows
  chaining sequence of vectors for effects like sums of vectors, and
  allows labeling and color shifting (to coordinate colors of multiple
  calls to plotvec).

  Parameters
  ----------
  *argv: lists or NumPy vectors
         One or more 2-d vectors

  tail: list or NumPy vector, default: [0,0]
        location of tail of (first) vector

  chain: bool, default: False
         Whether to place tail of vector at head of previous vector

  labels: list, tuple, or bool, default: False
         Labels for each vector for use in legend, or False for no labels

  newfig: bool, default: True
         Whether to open a new figure for this plot (else plot on current fig)

  legendloc: string or int, default: 'best'
         Argument for legend location passed to Matplotlib

  colors: list or tuple
         A list or tuple of colors acceptable to Matplotlib. Must be of same
         size as number of vectors to plot

  color_offset: int, default: 0
         Shift color sequence by fixed value

  alpha: numeric or list or tuple of numeric
         Transparency alpha(s), should be between 0 (fully transparent) and 1 (solid).
         If numeric, then same value is applied to all vectors. Otherwise, alpha for
         each vector must be specified

  width: None or number
         Width of arrow shaft, also affects head size. Typically float around
         0.005 times the width of the plot.

  square_aspect_ratio: book, default: True
         If True (default), make plots square; otherwise, default aspect ratio

  plotsum: bool, default: False
           If True, plot a vector from the initial tail to the final head, representing
           the sum of the vectors

  Returns
  ----------
  None

  """

  xmin = 1e6
  xmax = -1e6
  ymin = 1e6
  ymax = -1e6
  if newfig:
    plt.figure()
  else:
    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()

    # Adjust to compensate for extra space left around vectors
    xmin += 1
    xmax -= 1
    ymin += 1
    ymax -= 1

  xmin=min(xmin, tail[0])
  xmax=max(xmax, tail[0])
  ymin=min(ymin, tail[1])
  ymax=max(ymax, tail[1])

  

  if not colors:
    colors = ['C'+ str(i+color_offset) for i in range(len(argv)+1)]

  original_tail = tail

  # Plot the vectors
  if labels:
    my_labels=labels
  else:
    my_labels = [None]*len(argv)

  if type(alpha) == int or type(alpha) == float:
    alphas = [alpha] * (len(argv)+1)
  else:
    alphas = alpha

  for i, head in enumerate(argv):
    if labels:
      label=labels[i]
    plt.quiver(*tail, *head, width=width, 
               angles='xy',scale_units='xy',scale=1,
               color=colors[i], alpha=alphas[i],
               label=my_labels[i])
    if chain:
      tail += head
      xmin=min(xmin, tail[0])
      xmax=max(xmax, tail[0])
      ymin=min(ymin, tail[1])
      ymax=max(ymax, tail[1])
    else:
      xmin=min(xmin, head[0])
      xmax=max(xmax, head[0])
      ymin=min(ymin, head[1])
      ymax=max(ymax, head[1])


  # Set limits based on vector dimensions and add axis lines
  plt.xlim(min(-1, xmin-1), max(1,xmax+1))
  plt.ylim(min(-1,ymin-1),max(1,ymax+1))
  plt.hlines(0, min(-1, xmin-1), max(1,xmax+1), 'k', linewidth=0.5, alpha=0.5)
  plt.vlines(0, min(-1,ymin-1),max(1,ymax+1), 'k', linewidth=0.5, alpha=0.5)

  # Set aspect ratio to square if requested
  if square_aspect_ratio:
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')

  # Plot vector sum if requested


  if plotsum:
    plt.plot([original_tail[0], 0.1*original_tail[0]+0.9*tail[0]],
             [original_tail[1], 0.1*original_tail[1]+0.9*tail[1]],
                  linewidth=3, ls='--',
             color='C'+str(len(argv)) )
    plt.quiver(*[0.1*original_tail[0]+0.9*tail[0],0.1*original_tail[1]+0.9*tail[1]],
               *(0.08*(np.array(tail)-np.array(original_tail))),
               angles='xy',scale_units='xy',
               scale=1, linewidth=1, color='C'+str(len(argv)) )

  # Add legend if user passed labels
  if labels:
    plt.legend(loc=legendloc);

def plotvecR(*argv, tail=[0,0], chain=False, labels=None, newfig=True,
            legendloc='best', colors= None, color_offset=0, alpha=1,
            width=None,  plotsum=False):
  """ plot a sequence of 2-d vectors using plotvec with rectangular aspect ratio

  Shortcut for calling plotvec() with square_aspect_ratio=False

  See plotvec() help for other information

  """

  plotvec(*argv, tail=tail, chain=chain, labels=labels, newfig=newfig,
          legendloc=legendloc, colors=colors, color_offset=color_offset, alpha=alpha,
          width=width, square_aspect_ratio=False, plotsum=plotsum)

