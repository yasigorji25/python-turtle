
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10295674
#    Student name: yasaman gorjinejad
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked and will automatically be awarded a mark of 0.
#  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/). [81022PT]
#
#--------------------------------------------------------------------#



from turtle import *
from math import *

canvas_height = 700 # pixels
canvas_width = 1100 # pixels
grass_depth = 95 # vertical depth of the "grass", in pixels
half_width = canvas_width // 2 # maximum x coordinate in either direction
grid_font = ('Arial', 10, 'normal') # font for drawing the grid
grid_size = 50 # gradations for the x and y scales shown on the screen
offset = 5 # offset of the x-y coordinates from the screen's edge, in pixels
max_height = canvas_height - grass_depth # maximum positive y coordinate
max_building_height = 575 # city ordinance maximum building height
site_width = 240 # maximum width of a building site

# Define the locations of building sites approved by the
# city council (arranged from back to front)
sites = [['Site 1', [-225, 0]],
         ['Site 2', [25, 0]],
         ['Site 3', [275, 0]],
         ['Site 4', [-375, -25]],
         ['Site 5', [-125, -25]],
         ['Site 6', [125, -25]],
         ['Site 7', [375, -25]],
         ['Site 8', [-275, -50]],
         ['Site 9', [-25, -50]],
         ['Site 10', [225, -50]]]

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image.
# By default the drawing grid is displayed - call the function
# with False as the argument to prevent this.
def create_drawing_canvas(show_grid = True):

    # Set up the drawing canvas with coordinate (0, 0) in the
    # "grass" area
    setup(canvas_width, canvas_height)
    setworldcoordinates(-half_width, -grass_depth, half_width, max_height)

    # Draw as fast as possible
    tracer(False)

    # Make the sky blue
    bgcolor('sky blue')

    # Draw the "grass" as a big green rectangle (overlapping the
    # edge of the drawing canvas slightly)
    overlap = 25 # pixels
    penup()
    goto(-(half_width + overlap), -(grass_depth + overlap)) # bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(grass_depth + overlap * 2)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(grass_depth + overlap * 2)
    end_fill()

    # Draw a nice warm sun peeking into the image at the top left
    penup()
    goto(-canvas_width // 2, canvas_height - grass_depth)
    pencolor('yellow')
    dot(350)

    # Draw a big fluffy white cloud in the sky
    goto(canvas_width // 3, canvas_height - grass_depth - 100)
    pencolor('white')
    dot(200)
    setheading(200)
    forward(100)
    dot(180)
    setheading(0)
    forward(200)
    dot(160)

    # Optionally draw x coordinates along the bottom of the
    # screen (to aid debugging and marking)
    pencolor('black')
    if show_grid:
        for x_coord in range(-half_width + grid_size, half_width, grid_size):
            goto(x_coord, -grass_depth + offset)
            write('| ' + str(x_coord), font = grid_font)

    # Optionally draw y coordinates on the left-hand edge of
    # the screen (to aid debugging and marking)
    if show_grid:
        for y_coord in range(-grid_size, max_height, grid_size):
            goto(-half_width + offset, y_coord - offset)
            write(y_coord, font = grid_font)
        goto(-half_width + offset, max_building_height - 5)
        write('Maximum allowed building height', font = grid_font)

    # Optionally mark each of the building sites approved by
    # the city council
    if show_grid:
        for site_name, location in sites:
            goto(location)
            dot(5)
            goto(location[0] - (site_width // 2), location[1])
            setheading(0)
            pendown()
            forward(site_width)
            penup()
            goto(location[0] - 40, location[1] - 17)
            write(site_name + ': ' + str(location), font = grid_font)
     
    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas.
# By default the cursor (turtle) is hidden when the program
# ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(False) # ensure any drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the build_city function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_plan function appearing below.  Your
# program must work correctly for any data set generated by the
# random_plan function.
#
# Each of the data sets below is a list specifying a set of
# buildings to be erected.  Each specification consists of the
# following parts:
#
# a) The site on which to erect the building, from Site 1 to 10.
# b) The style of building to be erected, from style 'A' to 'D'.
# c) The number of floors to be constructed, from 1 to 10.

# Each of these data sets draws just one building in each of the
# four styles
fixed_plan_1 = [[1, 'A', 6]]
fixed_plan_2 = [[2, 'B', 7]]
fixed_plan_3 = [[3, 'C', 5]]
fixed_plan_4 = [[4, 'D', 4]]
fixed_plan_5 = [[1, 'A', 9]]
fixed_plan_6 = [[2, 'B', 2]]
fixed_plan_7 = [[3, 'C', 3]]
fixed_plan_8 = [[4, 'D', 6]]

# Each of the following data sets draws just one style of
# building but at three different sizes, including the maximum
# (so that you can check your building's maximum height against
# the height limit imposed by the city council)
fixed_plan_9 = [[1, 'A', 10], [2, 'A', 5], [3, 'A', 1]]
fixed_plan_10 = [[1, 'B', 10], [2, 'B', 5], [3, 'B', 1]]
fixed_plan_11 = [[1, 'C', 10], [2, 'C', 5], [3, 'C', 1]]
fixed_plan_12 = [[1, 'D', 10], [2, 'D', 5], [3, 'D', 1]]
fixed_plan_13 = [[1, 'A', 10], [2, 'A', 5], [3, 'A', 1]]
fixed_plan_14 = [[1, 'B', 10], [2, 'B', 5], [3, 'B', 1]]
fixed_plan_15 = [[1, 'C', 10], [2, 'C', 5], [3, 'C', 1]]
fixed_plan_16 = [[1, 'D', 10], [2, 'D', 5], [3, 'D', 1]]

# Each of the following data sets draws a complete cityscape
# involving each style of building at least once. There is
# no pattern to them, they are simply specific examples of the
# kind of data returned by the random_plan function which will be
# used to assess your solution. Your program must work for any value
# that can be returned by the random_plan function, not just these
# fixed data sets.
fixed_plan_17 = \
         [[1, 'D', 2],
          [2, 'B', 7],
          [5, 'C', 6],
          [6, 'A', 4]]
fixed_plan_18 = \
         [[1, 'D', 6],
          [3, 'C', 5],
          [4, 'B', 3],
          [9, 'A', 9],
          [10, 'D', 2]]
fixed_plan_19 = \
         [[5, 'C', 6],
          [6, 'B', 9],
          [7, 'A', 5],
          [8, 'A', 7],
          [9, 'D', 4]]
fixed_plan_20 = \
         [[1, 'A', 4],
          [2, 'B', 4],
          [3, 'A', 5],
          [4, 'D', 7],
          [10, 'B', 10]]
fixed_plan_21 = \
         [[1, 'B', 6],
          [3, 'A', 4],
          [4, 'C', 4],
          [6, 'A', 8],
          [8, 'C', 7],
          [9, 'B', 5],
          [10, 'D', 3]]
fixed_plan_22 = \
         [[1, 'A', 10],
          [2, 'A', 9],
          [3, 'C', 10],
          [4, 'B', 5],
          [5, 'B', 7],
          [6, 'B', 9],
          [7, 'C', 2],
          [8, 'C', 4],
          [9, 'A', 6],
          [10, 'D', 7]]
fixed_plan_23 = \
         [[3, 'A', 8],
          [4, 'C', 8],
          [5, 'B', 4],
          [6, 'D', 5],
          [7, 'C', 5],
          [8, 'A', 3],
          [9, 'D', 2]]
fixed_plan_24 = \
         [[2, 'C', 3],
          [3, 'B', 1],
          [4, 'C', 3],
          [5, 'C', 1],
          [6, 'D', 2],
          [7, 'B', 1],
          [8, 'D', 2],
          [9, 'C', 7],
          [10, 'A', 1]]
fixed_plan_25 = \
         [[1, 'B', 7],
          [3, 'C', 1],
          [6, 'D', 3],
          [7, 'A', 7],
          [8, 'D', 3],
          [9, 'C', 7],
          [10, 'C', 9]]
fixed_plan_26 = \
         [[1, 'A', 6],
          [2, 'A', 2],
          [3, 'A', 9],
          [4, 'D', 1],
          [5, 'C', 7],
          [6, 'D', 6],
          [7, 'B', 5],
          [8, 'A', 1],
          [9, 'D', 10],
          [10, 'A', 6]]
 
#
#--------------------------------------------------------------------#


# The function in this section will be used to mark your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a city
# to be built.  Your program must work for any data set returned by
# this function.  The results returned by calling this function will
# be used as the argument to your build_city function during marking.
# For convenience duri,ng code development and marking this function
# also prints the plan for the city to be built to the shell window.
#

def random_plan(print_plan = True):
    building_probability = 70 # percent
    from random import randint, choice
    # Create a random list of building instructions
    city_plan = []
    for site in range(1, len(sites) + 1): # consider each building site
        if randint(1, 100) <= building_probability: # decide whether to build here
            style = choice(['A', 'B', 'C', 'D']) # choose building style
            num_floors = randint(1, 10) # choose number of floors
            city_plan.append([site, style, num_floors])
    # Optionally print the result to the shell window
    if print_plan:
        print('\nBuildings to be constructed\n' +
              '(site, style, no. floors):\n\n',
              str(city_plan).replace('],', '],\n '))
    # Return the result to the student's build_city function
    return city_plan


def draw_triangle(x, y, pencolour, fillcolour, width):
    penup()
    pencolor(pencolour)
    goto(x, y)
    pendown()
    begin_fill()
    fillcolor(fillcolour)
    setheading(0)  # face east
    forward(width / 2)
    setheading(120)
    forward(width)
    setheading(240)
    forward(width)
    setheading(0)
    forward(width / 2)
    end_fill()
    penup()

    
             
def draw_rectangle( x , y, pencolour, fillcolour, width, height):
    penup()
    pencolor(pencolour)
    goto(x,y)
    pendown()
    begin_fill()
    fillcolor(fillcolour)
    setheading(0) #face east
    forward(width/2)
    left(90) #face north
    forward(height)
    left(90) # west
    forward(width)
    left(90) # south
    forward(height)
    goto(x,y)
    end_fill()
    penup()

        
def draw_floor(x_floor, y_floor, height, width , color, size_pen):
    
     
    goto(x_floor - (width//2), y_floor)
    pensize(size_pen)
    begin_fill()
    fillcolor(color)
    pendown()
    setheading(90)
    forward(height)
    setheading(0)
    forward(width)
    setheading(-90)
    forward(height)
    setheading(180)
    forward(width)
    end_fill()
    penup()
    y_floor = y_floor + height  # this would be the position to start drawing each floor

        
def draw_frame(x_floor, y_floor, height, width, size_pen, pencolour):
    
     
    goto(x_floor - (width//2), y_floor)
    pencolor(pencolour)
    pensize(size_pen)
    begin_fill()
    pendown()
    setheading(90)
    forward(height)
    setheading(0)
    forward(width)
    setheading(-90)
    forward(height)
    setheading(180)
    forward(width)
    penup()
    y_floor = y_floor + height

def draw_circle(x, y, radius, fillcolour, pencolour):
    goto(x,y)
    pendown()
    pencolor(pencolour)
    begin_fill()
    fillcolor(fillcolour)
    circle(radius)
    end_fill()
    pendown()

        
def draw_building_A(x, y, floors):

    floor_x = x 
    floor_y = y
    height = 40
    width =  240
    for floor in range(1,floors+1):
         draw_floor (floor_x, floor_y ,height, width, 'coral', 2)
         floor_y = floor_y + height

    # darw first floor of building A
    # draw the door

    first_floor_x = x
    first_floor_y = y
    first_floor_height = height
    first_floor_width = width
    penup()
    goto(first_floor_x + first_floor_width / 8, first_floor_y)
    setheading(90)
    pendown()
    begin_fill()
    fillcolor('yellow')
    circle(first_floor_height - first_floor_height / 4, extent = 180)
    end_fill()
    penup()
    goto(first_floor_x, first_floor_y )
    pendown()
    setheading(90)
    forward(first_floor_height - first_floor_height / 4)
    penup()
    goto(first_floor_x - first_floor_width /16,  first_floor_y +    first_floor_height / 3 )
    dot(7)
    goto(first_floor_x + first_floor_width /16,  first_floor_y +    first_floor_height / 3 )
    dot(7)

    

    # draw window for building A 

    window_x = x - width/3  # start x pont to draw a window
    
    window_y = y + height/4      # start y pont to draw a window
    
 
    for each in range(floors-1): # draw windows for each level of buildings 
        penup()
        window_y = window_y + height # increade the height to go to the upper level 
        window_x = x - site_width/3 # reassign the value of window_x to start drawing window from left of the each floor 
        for each in range(4): # draw 4 windows in one floor 
            pendown()
            draw_rectangle(window_x, window_y, 'red', 'yellow', width/8, height/2 )
            penup()
            window_x = window_x + 50  #distance between the windows (after draw a window x will be increase 50 to draw next window)


    #draw roof for building A
            
            
    roof_x = x
    roof_y = y
    roof_height = height
    roof_width = width

    pencolor('black')
    roof_x = x 
    roof_y = y + height * (floors)  # the y point above all the floors 
    penup()
    goto(roof_x -  roof_width/2 , roof_y)
    pendown()
    begin_fill()
    fillcolor('coral') # fill the half circle
    goto(roof_x + roof_width //2 ,  roof_y)
    setheading(90)
    circle(  roof_width //2 , extent = 180) # draw half circle on the roof 
    end_fill()
    penup()       
    setheading(0)
    pencolor('black')

    def draw_curve(heading, radius):  # define a flower in the half circle 
        pencolor('red')
        penup()
        begin_fill()
        fillcolor('yellow')
        goto(roof_x, roof_y + height)
        pendown()
        setheading(heading)
        circle(radius, extent = 70)
        goto(roof_x, roof_y + height)
        end_fill()
        

# use a define function for draw flower

    angle = 0
    for step in range(18):
        draw_curve(angle, site_width/5) 
        angle = angle + 20
    penup()       
    setheading(0)
    pencolor('black')
                
def draw_building_B(x, y, floors): # draw floors for building B 

    floor_x = x 
    floor_y = y
    height= 40
    width = 200

    for floor in range(1,floors+1):
      
        draw_floor (floor_x, floor_y ,height, width, 'snow',2)

        floor_y = floor_y + height  # each time add the y position 



    brick_width = width // 10   # width of each brick
    brick_x = x - width/2 + brick_width / 2  # position to start drawing brick 
    brick_y = y
    brick_height = height / 4

    for each in range(floors): 
        penup()
        #brick_y = brick_y + height # increase the height to go to the upper level 
        brick_x = x - width/2 + brick_width / 2 # reassign the value of window_x to start drawing window from left of the each floor
        for bricklayer in range(2):
            brick_x = x - width/2 + brick_width / 2
            brick_y = brick_y + height/2
            for each in range(10): 
                pendown()
                draw_rectangle(brick_x, brick_y - height/2, 'cornflowerblue', 'ivory', brick_width, brick_height )
                brick_x = brick_x + brick_width  # each time plus the building
    floor_x = x 
    floor_y = y
    height= 40
    width = 200

    # draw the farme of the building to level of floors be appear

    for floor in range(1,floors+1):

        draw_frame(floor_x, floor_y, height, width, 2, 'darkmagenta')
        floor_y = floor_y + height

# first floor of building B

    first_floor_x = x
    first_floor_y = y
    first_floor_height = height
    first_floor_width = width
    draw_floor(first_floor_x, first_floor_y, first_floor_height, first_floor_width ,'snow', 2)
    write('$$', align = 'left', font = ("wide latin", 30, "normal")) # write doller symbole at the bottom of the building
    penup()
    backward(first_floor_width - first_floor_width / 5)  # move to draw doller symbol at the bottom of the building
    write('$$', align = 'left', font = ("wide latin", 30, "normal"))
    draw_rectangle(first_floor_x, first_floor_y , 'darkmagenta', 'snow', first_floor_width / 2,  first_floor_height) # draw rectangle for entrance building
    draw_rectangle(first_floor_x, first_floor_y , 'darkmagenta', 'lavenderblush', first_floor_width / 4,  first_floor_height / 2)

    




    # draw roof for building B 
    roof_width = width 
    roof_height = height 
    roof_x = x 
    roof_y = y + height * (floors) # draw the roof top of the floors 
    draw_rectangle(roof_x, roof_y , 'darkmagenta', 'snow', roof_width - width / 4, roof_height - height / 4 )
    pencolor('black')
    write('Business Building', align = 'center', font = ("wide latin", 18, "italic")) # name of the building




         
def draw_building_C(x, y, floors):

    floor_x = x 
    floor_y = y
    height = 40
    width =  160
    pencolor('teal')
    for floor in range(1,floors+1):
         draw_floor (floor_x, floor_y ,height, width, 'aquamarine', 2)
         floor_y = floor_y + height  # each time y position will be increase 
           
         
    # draw window for building C
    

    window_x = x - width /4  # start x position to draw a window

    window_y = y + height / 4  # start x position to draw a window



    for each in range(floors - 1): # darw windows for each floor of building
        penup()
        window_x = x - width / 4  # reassign the value of window_x to start drawing window from left of the each floor 
        window_y = window_y + height  # increade the height to go to the upper level 
        for each in range(2): # draw two windows in each floor 
            draw_circle (window_x, window_y + height / 2, height / 3, 'olivedrab', 'palegreen')
            penup()
            goto(window_x, window_y - height / 4 - height/ 4)  # start position to draw cross after drawing each circle
            write('+', align = 'center', font = ("arial", 45, "normal"))
            penup()
            window_x = window_x + width /2 # each time the position of window_x will be increase to draw the windows 

    

            
          

     
    # draw roof

    roof_width = width 
    roof_height = height 
    roof_x = x 
    roof_y = y + height * (floors)  # the y position will be top of the all floors
    draw_triangle(roof_x, roof_y, 'teal', 'aquamarine', roof_width)  # draw a triangle top of the floors 
    draw_circle (roof_x, roof_y + height  /2, height / 2, 'honeydew', 'darkcyan')  # draw a clock on the roof
    # darw hour hand
    goto(roof_x, roof_y + height  /2) 
    pendown()
    setheading(90) # face north
    forward(height / 2)
    goto(roof_x, roof_y + height)
    setheading(0)
    forward(height / 2)
    

    
    

   # draw first floor

    first_floor_x = x
    first_floor_y = y
    first_floor_height = height
    first_floor_width = width

    # draw stairs 

    penup()
    draw_rectangle( first_floor_x , first_floor_y  , 'teal', 'mediumaquamarine', first_floor_width / 3 + first_floor_width /10 , first_floor_height / 10 )  # first stair 
    draw_rectangle( first_floor_x , first_floor_y + first_floor_height / 10   , 'teal', 'mediumaquamarine', first_floor_width / 3, first_floor_height / 10 ) # second stair
    draw_rectangle( first_floor_x , first_floor_y + first_floor_height * 2 /10 , 'teal', 'mediumaquamarine', first_floor_width / 4, first_floor_height / 10 )  # third stair
    draw_rectangle( first_floor_x , first_floor_y + first_floor_height * 3 /10 , 'teal', 'mediumaquamarine', first_floor_width / 5, first_floor_height / 10 )  # forth stair

    pencolor('black')


    

   
def draw_building_D(x, y, floors):

    floor_x = x 
    floor_y = y
    height = 30
    width =  180
    pencolor('teal')
    for floor in range(1,floors + 1):
         draw_floor (floor_x, floor_y ,height, width, 'darkgreen', 1)  
         floor_y = floor_y + height # increase the height each time in the loop floor 
           

            

    window_x = x - width /4  # start x position to draw a window

    window_y = y   # start x position to draw a window



    for each in range(floors - 1): # darw windows for each floor of building
        penup()
        window_x = x - width / 4  # reassign the value of window_x to start drawing window from left of the each floor 
        window_y = window_y + height  # increade the height to go to the upper level
        window_width = width
        for each in range(6): # draw two windows in each floor
             draw_triangle(window_x - window_width / 6 , window_y, 'yellow', 'darkred', window_width / 6)
             window_x = window_x +  window_width / 6  # each time will increase the window_x  position to draw the next window
             
           
          
     # draw the farme of the building to level of floors be appear

    floor_x = x 
    floor_y = y
    height = 30
    width =  180

    for floor in range(1,floors+1):

        draw_frame(floor_x, floor_y, height, width, 2, 'black')
        floor_y = floor_y + height
       


    # draw first floor

    brick_width = width / 10
    brick_x = x - width/2 + brick_width + 5
    brick_y = y
    brick_height = height / 3

    for bricklayer in range(3):
        brick_x = x - width / 2 + brick_width / 2
        brick_y = brick_y + height / 3
        for each in range(10): 
            pendown()
            draw_rectangle(brick_x , brick_y - height/3, 'black', 'saddlebrown', brick_width, brick_height )
            brick_x = brick_x + brick_width   # each time will increase the brick_x  position to draw the nex brick
            

# draw the entrance of the building

    first_floor_x = x
    first_floor_y = y
    first_floor_height = height
    first_floor_width = width

    draw_rectangle(first_floor_x, first_floor_y , 'tan', 'wheat', first_floor_width / 3,  first_floor_height)

    penup()


    # draw roof

    
    roof_width = width 
    roof_height = height 
    roof_x = x 
    roof_y = y + height * (floors)  # the y position will be top of the all floors

    draw_circle (roof_x - roof_width / 2 + roof_width / 12 , roof_y + roof_width / 12, roof_width / 12, 'darkviolet', 'pink')
    penup()
    goto(roof_x - roof_width / 3, roof_y)  # move to the circle which is on the left hand 
    pendown()
    write('A', align = 'center', font = ("arial", 20, "normal"))
    penup()
    draw_circle (roof_x - roof_width / 2 + roof_width *5 / 12 , roof_y + roof_width / 12, roof_width / 12, 'darkviolet', 'pink')
    penup()
    goto(roof_x , roof_y)   # move to the circle which is on the middle 
    pendown()
    write('R', align = 'center', font = ("arial", 20, "normal"))
    penup()
    draw_circle (roof_x - roof_width / 2 + roof_width * 9 / 12 , roof_y + roof_width / 12, roof_width / 12, 'darkviolet', 'pink')
    penup()
    goto(roof_x + roof_width / 3, roof_y)  #  # move to the circle which is on the right hand 
    pendown()
    write('T', align = 'center', font = ("arial", 20, "normal"))
    penup()

    
    pencolor('black')
    

    
    
    

    


        
        

        
    

    

    




def build_city(plan):

    for building_info in plan:
        # location
        x = sites[building_info[0]-1] [1] [0]
        y = sites[building_info[0]-1] [1] [1]

        # style
        style = building_info[1]
        
        # floors
        floors = building_info[2]

        # draw building A
        if style == 'A':
            draw_building_A(x, y, floors)

        # draw building B
        if style == 'B':
            draw_building_B(x, y, floors)


         # draw building C
        if style == 'C':
            draw_building_C(x, y, floors)


         # draw building D
        if style == 'D':
            draw_building_D(x, y, floors)
           
        
    

#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# building your city.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the coordinates and building sites
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with your name and/or a description of
# ***** your city
title("Yasaman Gorjinejad")

### Call the student's function to build the city
### ***** While developing your program you can call the build_city
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_plan()" as the
### ***** argument to the build_city function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_plan function.
##build_city(fixed_plan_1) # <-- used for code development only, not marking
build_city(random_plan())
# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#
