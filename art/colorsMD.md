---
title: ISCC-NBS Color Chart
description: A table showing the structure and html codes of the ISCC-NBS system.
---

TODO: copy over from the colors html

# ISCC-NBS Color Centroid Table

The following colors are based on the [ISCC-NBS color system](https://en.wikipedia.org/wiki/ISCC%E2%80%93NBS_system), 
a color naming system devised by the National Bureau of Standards
based on the [Munsell color system.](https://en.wikipedia.org/wiki/Munsell_color_system).

This color system actually defines "blocks" of colors, and these are the centroids.

For ease of reading, I call yellow-green 'chartreuse' to distinguish from yellowish-green.
Also, I combine the modifiers of 'light -ish gray' and 'pale'.



--

## Motivation and explanation

Colors are hard. 
Some colors we see can't be shown on a screen. 
Some colors on a screen can't be printed. 
RGB values don't cleanly map to human perception because our eyes are most sensitive to green light.

While looking up visualizations of [XKCD's color survey data](https://blog.xkcd.com/2010/05/03/color-survey-results/),
I found  [Aubrey Jaffer's site](http://people.csail.mit.edu/jaffer/Color/),
which contains comparisons of several color name dictionaries.

According to the author, most online color dictionaries don't evenly cover the range of human perception, and include a number of colors which can't be reproduced in print.
They provide several alternate color dictionaries limited to the print gamut, including a cleaned-up version of the ISCC-NBS system with html-style color codes.

I was intrigued by the system, but unsatisfied with it's presentation.
- [This Catalog](http://people.csail.mit.edu/jaffer/Color/nbs-iscc.pdf) organizes colors nicely, but in pdf form.
- [This](http://people.csail.mit.edu/jaffer/Color/NBS-ISCC-rgb.txt) and [this](http://people.csail.mit.edu/jaffer/Color/nbs-iscc.txt) text file clearly is easy to access and copy from, but doesn't preview the color.
- This [linked comparison table](https://web.archive.org/web/20121103030619/http://tx4.us/nbs-iscc.htm) presents all the info and colors I want, but puts this in a verbose list that requires lots of scrolling.
- [This list](https://www.december.com/html/spec/colorucl.html) has a similar problem.

In my table above, 
- I organize the blocks in a grid by category and modifier
- I only use one value for each block, based on the color centroids from [this source.](http://people.csail.mit.edu/jaffer/Color/Dictionaries#nbs-iscc) (Do note that each color name refers to a range of colors. [These all count as vivid blue](https://www.december.com/html/spec/colornames.html).)
- I include plaintext html codes for easy copypasting into Gimp or Inkscape.

More details about the history of ISCC NBS color can be found [here](https://www.sciencedirect.com/topics/engineering/colour-category).



## Changes from the linked color dictionary

- Having both yellowishgreen and yellowgreen is confusing. I've relabelled yellowgreen as chartreuse.
- merged all lightgrayish- labels into pale labels.
- Several of the entries were based on guesses by the author. I disagree with some of these guesses, and have tried to improve upon them by interpolating similarly named colors in LCh color space.
    - vivid blue
        - was 00A1C2
        - changed to 0072ff(interpolation) or maybe less chroma 3b74ea for print friendliness
        - changed to 6375ba
        - changed to 367cc7
    - deep greenish blue
        - Was 2E8495
        - Changed to 00444f or 004652
    - vivid purplishblue
        - was 30267a
        - now 736ad0, made brighter with same hue and relative chroma
- relabelled some nuetral colors to make names more consistent in terms of relative luminosity
    - light...ishgrays have a relative luminosity of approx 75%
    - pinkishgray -> lightpinkishgray
    - yellowishgray -> lightyellowishgray
    - brownishgray -> darkbrownishgray
    - lightbrownishgray -> brownishgray
    - olivegray -> darkolivegray
    - lightolivegray -> olivegray


---

License info for the color dictionary used:

<pre>
! Copyright © 2003 Voluntocracy.  Permission is granted to copy and
! distribute modified or unmodified versions of this color dictionary
! provided the copyright notice and this permission notice are preserved
! on all copies and the entire such work is distributed under the terms
! of a permission notice identical to this one.
</pre>








