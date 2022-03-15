# not a mathematically correct model
# more like a visual representation based on Math constants

import tkinter as tk

from random import randint, uniform, random
import math

#==================================================================================
#----------------INPUT PARAM HERE-----------------
#==================================================================================


# scale: radio bubble diameter in light years
SCALE = 225
# earth: 225

# number of advance civilizations from the Drake equation
NUM_CIVS = 15600000

#==================================================================================
#==================================================================================


# set up display canvas
root = tk.Tk()
root.title('Milky Way Galaxy')
c = tk.Canvas(root, width=1000, height=800, bg='black')
c.grid()
c.config(scrollregion=(-500, -400, 500, 400))

# actual milky way dimensions (light years)
DISC_RADIUS = 50000
DISC_HEIGHT = 1000
DISC_VOL = math.pi * DISC_RADIUS**2 * DISC_HEIGHT


def scale_galaxy():
    """
    Scale galaxy dimensions based on radio bubble size(scale)
    param: from GLOBAL
    return: scaled disc radius, scaled disc volume
    """
    disc_radius_scaled = round(DISC_RADIUS/SCALE)
    bubble_vol = 4/3 * math.pi * (SCALE/2)**3
    disc_vol_scaled = DISC_VOL/bubble_vol
    return disc_radius_scaled, disc_vol_scaled


def detect_prob(disc_vol_scaled):
    """
    calculate probability of galactic civilizations detecting each other
    use if condition to handle extreme points of regression
    """
    ratio = NUM_CIVS / disc_vol_scaled
    if ratio < 0.002:
        detection_prob = 0
    elif ratio >= 5:
        detection_prob = 1
    else:
        detection_prob = -0.004787*ratio**4 + 0.0671*ratio**3 - 0.3613*ratio**2 + \
                         0.9218*ratio + 0.00892
    return round(detection_prob, 3)


def random_polar_coordinates(disc_radius_scaled):
    """
    Generate uniform random (x,y) point within a disc for 2D display
    """
    r = random()
    theta = uniform(0, 2*math.pi)
    x = round(math.sqrt(r) * math.cos(theta) * disc_radius_scaled)
    y = round(math.sqrt(r) * math.sin(theta) * disc_radius_scaled)
    return x, y


def spirals(b, r, rotation_factor, fuzz_factor, arm):
    """
    build spiral arms using log spiral equation

    b: arbitrary constant in log spiral equation
    r: scaled galactic disc radius
    rotation_factor: rotation factor in rotating the spiral arm
    fuzz_arm: random shift in star positions
    arm: spiral arm ( 0 = main arm, 1 = trailing stars)

    """

    spiral_stars = []
    fuzz = int(0.030*abs(r))
    theta_max = 520
    for i in range(theta_max):
        theta = math.radians(i)
        x = r * math.exp(b * theta) * math.cos(theta + math.pi * rotation_factor) + randint(-fuzz, fuzz) * fuzz_factor
        y = r * math.exp(b * theta) * math.sin(theta + math.pi * rotation_factor) + randint(-fuzz, fuzz) * fuzz_factor
        spiral_stars.append((x, y))
    for x, y in spiral_stars:
        if arm == 0 and int(x % 2) == 0:
            c.create_oval(x-2, y-2, x+2, y+2, fill='white', outline='')
        elif arm == 0 and int(x % 2) != 0:
            c.create_oval(x-1, y-1, x+1, y+1, fill='white', outline='')
        elif arm == 1:
            c.create_oval(x, y, x, y, fill='white', outline='')


def star_haze(disc_radius_scaled, density):
    """
    randomly distribute faint tkinter stars in galactic disc

    disc_radius_scaled = galactic disc radius scaled to radio bubble diameter
    density = multiplier to vary number of stars posted
    """

    for i in range(0, int(disc_radius_scaled * density)):
        x, y = random_polar_coordinates(disc_radius_scaled)
        c.create_text(x, y, fill='white', font=('Helvetica', '7'), text='.')
        # create_oval was used. use create_text instead


def main():
    """
    calculate detection probability and post galaxy display and statistics
    """

    disc_radius_scaled, disc_vol_scaled = scale_galaxy()
    detection_probability = detect_prob(disc_vol_scaled)

    # build 4 main spiral arms and 4 trailing arms
    spirals(-0.3, disc_radius_scaled, 2, 1.5, 0)
    spirals(-0.3, disc_radius_scaled, 1.91, 1.5, 1)
    spirals(-0.3, -disc_radius_scaled, 2, 1.5, 0)
    spirals(-0.3, -disc_radius_scaled, -2.09, 1.5, 1)
    spirals(-0.3, -disc_radius_scaled, 0.5, 1.5, 0)
    spirals(-0.3, -disc_radius_scaled, 0.4, 1.5, 1)
    spirals(-0.3, -disc_radius_scaled, -0.5, 1.5, 0)
    spirals(-0.3, -disc_radius_scaled, -0.6, 1.5, 1)
    star_haze(disc_radius_scaled, density=20)

    # display legend
    c.create_text(-455, -360, fill='white', anchor='w', text='1 pixel = {} light year'.format(SCALE))
    c.create_text(-455, -330, fill='white', anchor='w', text='radio bubble diameter = {}'.format(SCALE))
    #c.create_text(-455, -300, fill='white', anchor='w', text='probability for detecting {} civilization = {}'.format(NUM_CIVS,
    # detection_probability))

    # annotate earth
    if SCALE == 225:
        c.create_rectangle(115, 75, 116, 76, fill='red', outline='')
        c.create_text(118, 72, fill='red', anchor='w', text="<--------Earth radio bubble")

    # run tkinter loop
    root.mainloop()


if __name__ == "__main__":
    main()




