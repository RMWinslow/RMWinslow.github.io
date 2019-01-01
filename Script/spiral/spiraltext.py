# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 16:32:19 2018 by Robert Winslow
            
            ─────────────────────────────┐
            ┌───────────────────────────┐│
            │┌─────────────────────────┐││
            ││┌───────────────────────┐│││
            │││┌─────────────────────┐││││
            ││││┌───────────────────┐│││││
            │││││┌─────────────────┐││││││
            ││││││┌───────────────┐│││││││
            │││││││┌─────────────┐││││││││
            ││││││││┌───────────┐│││││││││
            │││││││││┌─────────┐││││││││││
            ││││││││││┌───────┐│││││││││││
            │││││││││││┌─────┐││││││││││││
            ││││││││││││┌───┐│││││││││││││
            │││││││││││││┌─┐││││││││││││││
            ││││││││││││││└┘││││││││││││││
            │││││││││││││└──┘│││││││││││││
            ││││││││││││└────┘││││││││││││
            │││││││││││└──────┘│││││││││││
            ││││││││││└────────┘││││││││││
            │││││││││└──────────┘│││││││││
            ││││││││└────────────┘││││││││
            │││││││└──────────────┘│││││││
            ││││││└────────────────┘││││││
            │││││└──────────────────┘│││││
            ││││└────────────────────┘││││
            │││└──────────────────────┘│││
            ││└────────────────────────┘││
            │└──────────────────────────┘│
            └────────────────────────────┘

This contains the functions needed to calculate the value of
your spiral interview question as a closed-form function.
The agent-based approach is totes probs faster if you
want to generate the entire spiral, but this has the advantage
of being able to find a single cell's value without needing to
calculate the whole dang thing.

cell_value(x,y,w,h) gets a single number. Iterate through 
x and y to get the whole spiral.
"""
from math import ceil


def spiral_depth(x,y,w,h):
    """This returns the distance of (x,y) from the 
    edge of a (w by h) box. This is useful because
    each full rotation of the spiral returns us to
    an easy-to-calculate position.
    
    00000
    01110
    01210
    01110
    00000
    """
    return min(x,y,w-1-x,h-1-y)



def perimeter(w,h):
    """To get the perimeter of a rectangle of cells,
    add up all the edges and then subtract 4 because
    each corner is part of two different edges.
    
    ┼──w──┼
    │     │
    h     h
    │     │
    ┼──w──┼
    """
    return 2*w+2*h-4



def spiral_start(d,w,h):
    """This is the starting value of spiral number
    d in a (w by h) box. It's simply the number 
    of cells that must be traversed in the spiral
    path before completing d full rotations.
    ├────┐  
    ┌├──┐│  
    │┌X ││  
    ││  ││  
    │└──┘│  
    └────┘  
    
    Each spiral inwards reduces the width and height
    by 2 each.   
    ┼──7──┼
    │┼─5─┼│
    53   35
    │┼─5─┼│
    ┼──7──┼
    """
    return sum([perimeter(w-2*i,h-2*i) for i in range(d)])
    

def edge_value(x,y,w,h):
    """Assigns numbers to the perimeter of a (w by h)
    rectangle, with the top left cell being 0, and values
    incrementing clockwise.
    
    (This function returns nonsense for interior cells.)
    
    Along the top and right edges, the cell's value 
    increases as x and y increase.
    
    012345 
    ┌───┐6  
    │┌─┐│7 
    ││└┘│8
    │└──┘9
    └────┘
    
    Otherwise, the value increases as x and y decrease.
    
    ─────┐  
    9───┐│  
    8┌─┐││  
    7│└┘││  
    6└──┘│  
    543210 
    """
    if (y == 0 or x == w-1):
        return x+y
    else:
        return (w-1)+(h-1)+(w-1-x)+(h-1-y)
    #return x+y+2*((w-1)+(h-1)-x-y)*(1)



def cell_value(x,y,w,h):
    """Gets the value assigned to the cell in row y and 
    column x, given a spiralling pattern which starts
    in the top left and spirals clockwise around 
    a rectangle with width w and height h, increasing
    by one for each cell.
    
    For example, tile_value(3,2,5,5) will return 19.
    
    0   1   2   3   4   
    15  16  17  18  5   
    14  23  24 [19] 6   
    13  22  21  20  7   
    12  11  10  9   8   
    
    It looks like a bit of a mess, but all it's doing
    is treating the target cell like its on the outside 
    of the spiral and then adding to its value the cells
    from the actual outside spirals.
    
    An example with the values above:
        
    First, d is determined to be 1 because there is one 
    full spiral that wraps around the layer of the target
    cell. This single spiral contains 16 cells.
    *   *   *   *   *   
    *   ?   ?   ?   *   
    *   ?   ?  [?]  *   
    *   ?   ?   ?   *   
    *   *   *   *   *   
    
    Next, the box is stripped of the outside layer.
    
    The cells are moved up and to the left a number of 
    times equal to d, and then 2d is subtracted from both
    the width and height of the box.
    
    ?   ?   ?   ↖️
    ?   ?  [?]  
    ?   ?   ?  
    ↖️           ↖️
    
    Then the value of the cell in this simplified box is
    calculated. Here, we can see that our target cell is
    numbered three without the outside layers:
    0  1  2  
    7    [3]  
    6  5  4  
    
    Adding 3 to 16 yields 19, which is the actual value
    in the context of the full spiral.
    
    (If you need some other spiral, start with this one
    and use your linear algebra skills to do a rotation
    or whatevs.)"""
    d = spiral_depth(x,y,w,h)
    return edge_value(x-d,y-d,w-2*d,h-2*d)+spiral_start(d,w,h)


def display_spiral(w,h):
    for y in range(h):
        for x in range(w):
            中=cell_value(x,y,w,h)
            print('{:<3d}'.format(中), end='')
        print('')

    
display_spiral(5,7)


#%% BONUS FUNCTIONS

def סבל(x,y,w,h):
    """Don't worry about it."""
    #return sum([2*w+2*h-8*i-4 for i in range(min(x,y,w-1-x,h-1-y))])
    return (x-min(x,y,w-1-x,h-1-y))+(y-min(x,y,w-1-x,h-1-y))+2*((w-1-2*min(x,y,w-1-x,h-1-y))+(h-1-2*min(x,y,w-1-x,h-1-y))-(x-min(x,y,w-1-x,h-1-y))-(y-min(x,y,w-1-x,h-1-y)))*ceil(min(y-min(x,y,w-1-x,h-1-y),w-1-2*min(x,y,w-1-x,h-1-y)-(x-min(x,y,w-1-x,h-1-y)))/(w-2*min(x,y,w-1-x,h-1-y)+h-2*min(x,y,w-1-x,h-1-y)))+sum([2*w+2*h-8*i-4 for i in range(min(x,y,w-1-x,h-1-y))])

def display_spiral_2(w,h):
    for y in range(h):
        for x in range(w):
            中=סבל(x,y,w,h)
            print('{:<3d}'.format(中), end='')
        print('')
        
print('')
display_spiral_2(5,7)



def box_drawing_characters_are_fun(w,h):
    for y in range(h):
        for x in range(w):
            print(recursion_is_magic(x,y,w,h), end='')
        print('')
        
def recursion_is_magic(x,y,w,h):
    d = spiral_depth(x,y,w,h)
    if d == 0:
        if y==0 and x==w-1: return '┐'
        elif x==w-1 and y==h-1: return '┘'
        elif y==h-1 and x==0: return '└'
        elif x==0 and y==1: return '┌'
        elif y==0 or y==h-1: return '─'
        elif x==0 or x==w-1: return '│'
        else: return '🤔'
    else:
        return recursion_is_magic(x-d,y-d,w-2*d,h-2*d)
    
#box_drawing_characters_are_fun(30,30)
            