# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 23:05:01 2019

@author: RobertWinslow

This takes the spiral code and makes pretty pictures with it.
"""

from PIL import Image
from colorsys import hsv_to_rgb
import numpy as np


def spiral_value(x,y,w,h):
    d = min(x,y,w-1-x,h-1-y)
    spiralStart = 2*d*(w+h-2*d)
    edgeValue = 0
    if (y-d == 0 or x-w+1+d == 0):
        edgeValue = x-d + y-d
    else:
        edgeValue = 2*(w-2*d)+2*(h-2*d)-4-(x-d)-(y-d)#(w-2*d)+(h-2*d)-2 + (w-2*d-1-x+d) + (h-2*d-1-y+d)   #(w-1-d) + (w-2*d-1-x) + (h-2*d-1-y)#2*(w+h)-4-10*d-x-y
    return spiralStart+edgeValue


def display_spiral(w,h):
    for y in range(h):
        for x in range(w):
            中=spiral_value(x,y,w,h)
            print('{:<3d}'.format(中), end='')
        print('')
        
        
def simple_gradient(x,y,w,h):
    return (0,x,y)

def color_spiral(x,y,w,h):
    hue = (spiral_value(x,y,w,h) % 360) / 360
    return tuple(round(i*255) for i in hsv_to_rgb(hue, 1, 1))

def bright_spiral(x,y,w,h):
    p = 50 #period of oscillation in pixels.
    value = abs(spiral_value(x,y,w,h) % p - p/2) / (p/2)
    return tuple(round(i*255) for i in hsv_to_rgb(1, 0, value))

def get_radius(x,y,w,h):
    return ((x-w/2)**2+(y-h/2)**2)**0.5

def get_angle_from_center(x,y,w,h):
    return (np.arctan2(h/2-y,x-w/2) / (2*np.pi) * 360) %360
    
def circle_spiral0(x,y,w,h):
    "This one makes weird fractal stuff."
    a = get_angle_from_center(x,y,w,h)
    r = get_radius(x,y,w,h)
    hue = a/4 + r / 360
    return tuple(int(round(i*255)) for i in hsv_to_rgb(hue, 1, 1))

def circle_spiral(x,y,w,h):
    #how to get next layer to start at same point as previous layer?
    a = get_angle_from_center(x,y,w,h)
    r = get_radius(x,y,w,h)
    #if r < 100 or (r > 150 and r<250) or (r>300):
    #    return tuple(int(round(i*255)) for i in hsv_to_rgb(1, 0, 0))
    hue = (a*(r/100)) / 360
    return tuple(int(round(i*255)) for i in hsv_to_rgb(hue, 1, 1))

def simple_spiral(x,y,w,h):
    a = get_angle_from_center(x,y,w,h)
    r = get_radius(x,y,w,h)
    hue = (a+r) / 360
    return tuple(int(round(i*255)) for i in hsv_to_rgb(hue, 1, 1))

def circle_gradient(x,y,w,h):
    #a = get_angle_from_center(x,y,w,h)
    r = get_radius(x,y,w,h)
    hue = r / 20
    return tuple(int(round(i*255)) for i in hsv_to_rgb(hue, 1, 1))

def square_gradient(x,y,w,h):
    d = min(x,y,w-1-x,h-1-y)
    hue = d / 360
    return tuple(int(round(i*255)) for i in hsv_to_rgb(hue, 1, 1))

def square_stripes(x,y,w,h):
    d = min(x,y,w-1-x,h-1-y)
    hue = round(d / 60) /6
    return tuple(int(round(i*255)) for i in hsv_to_rgb(hue, 1, 1))

def circle_spiral2(x,y,w,h):
    a = get_angle_from_center(x,y,w,h)
    r = get_radius(x,y,w,h)
    baseline = 500
    hue = (a*(r/baseline))/360 + 2*np.pi*(r)
    return tuple(int(round(i*255)) for i in hsv_to_rgb(hue, 1, 1))

def triangle_wave(x, period, amplitude):
    if 0<=x<0.25*period: 
        return x*4*amplitude/period
    elif 0.25*period <= x < 0.75*period:
        return amplitude - (x-0.25*period)*(4*amplitude/period)
    else: 
        return - amplitude + (x-0.75*period)*(4*amplitude/period)

def circle_ripple(x,y,w,h):
    a = get_angle_from_center(x,y,w,h)
    r = get_radius(x,y,w,h)
    ripple = 10
    #if r<baseline or r>2*baseline: return tuple(int(round(i*255)) for i in hsv_to_rgb(0, 0, 0))
    #hue = a/360 + (np.sin(r/ripple)+1)/2
    hue = a/360
    #value = ((np.cos(r/ripple)*np.sin(a/360*2*np.pi))+2)/3
    value = ((np.cos(r/ripple)*(-1)*triangle_wave(a/360,1,1))+2)/3
    return tuple(int(round(i*255)) for i in hsv_to_rgb(hue, 1, value))
    
def circle_to_square_projection(x,y):
    """Take a point at distance r from the 0,0 and 
    project it out to a centered square with side-length 2r 
    
    Currently has bug with upper left
    """
    r = (x**2+y**2)**0.5
    if x == 0 and y == 0 :
        return 0,0
    elif x > 0 and -1<=(y/x)<=1:
        return r, r*y/x
    elif x < 0 and -1<=(y/x)<=1:
        return -r, -r*y/x
    elif y > 0 and -1<=(x/y)<=1:
        return r*x/y, r
    elif y < 0 and -1<=(x/y)<=1:
        return -r*x/y, -r
    
    
    
def circle_to_ngon(x,y,n):
    """Take a point at distance r from the 0,0 and 
    project it out to a centered ngon with outer radius r
    
    angle remains the same but radius may change
    """
    r = (x**2+y**2)**0.5
    a = np.arctan2(y,x) % (2*np.pi) 
    newr = r * np.cos(np.pi/n)/np.cos(a%(2*np.pi/n) - (np.pi/n))
    newx = newr*np.sin(a)
    newy = newr*np.cos(a)
    return newx,newy
    
def square_test(x,y,w,h):
    newx, newy = circle_to_square_projection(x-(w-1)/2,y-(h-1)/2)
    newx += (w-1)/2
    newy += (h-1)/2
    #print(round(newx),round(newy))
    return color_spiral(round(newx/2),round(newy/2),w/2,h/2)

def convoluted_gradient(x,y,w,h):
    #newx, newy = circle_to_square_projection2(x,y,w,h)
    newx, newy = circle_to_square_projection(x-(w-1)/2,y-(h-1)/2)
    newx += (w-1)/2
    newy += (h-1)/2
    return square_stripes(newx,newy,w,h)
    
def create_image(w,h,name,color_function):
    img = Image.new('RGB', size=(w, h))
    pix = img.load()
    for x in range(w):
        for y in range(h):
            #print(color_function(x,y,w,h))
            pix[x,y] = color_function(x,y,w,h)
    img.save(name)
    
    
def attempted_pentagon(x,y,w,h):
    newx, newy = circle_to_ngon(x-(w-1)/2,y-(h-1)/2,7)
    newx += (w-1)/2
    newy += (h-1)/2
    return circle_gradient(newx,newy,w,h)

def gradient80(x,y,w,h):
    return tuple(round(i*255) for i in hsv_to_rgb(x/80, 1, 1))
    
display_spiral(5,5)
create_image(1000,1000,'skellytest.png',circle_ripple)

