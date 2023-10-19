import turtle, random, math

#I implemented logic to avoid instant collisions, and I made it so that the walls loop. I also
#adjusted the color of the background for visibility purposes, but it isn't particularly fancy.

#I also tested the game with a timer of 16ms rather than 30ms, as I preferred the look of 60fps,
#so feel free to change the turtle.ontimer call in gameloop() to be 16ms if you want an extra challenge!
class Game:
    '''
    Purpose: A Game object represents the main code responsible for running the game, handling the events and gameloop logic.
    Instance variables:
        player - A SpaceCraft object with randomly generated initial position and velocity. This serves as the player-controlled
            object in the game.
        obstacle_list - A list of Obstacle objects created according to the default Obstacle initializer.
    Methods:
        __init__ - Initializes the player and the Obstacles, sets the boundaries of the turtle window, and makes the first call to
            gameloop(). Handles the keypress events used to control the player SpaceCraft.
        gameloop - moves the player, then tries to animate each of the Obstacles in obstacle_list. After this, if the player is
            within 20 units of the bottom of the turtle window, gameloop makes a call to player.check_win to check if the win-condition
            has been met. If there is no collision or win-check, gameloop calls itself again after a 30ms delay. If an error is raised
            during this process, it is handled according to the specified exceptions within the try-except block, displaying either a 
            win message or a collision message to the turtle window.
    '''
    def __init__(self):
        #Bottom left corner of screen is (0, 0)
        #Top right corner is (500, 500)
        turtle.setworldcoordinates(0, 0, 500, 500)
        turtle.bgcolor('black')
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.delay(0)
        
        #Creating the ship
        init_values = (random.uniform(100,400),random.uniform(250,450),random.uniform(-4,4),random.uniform(-2,0))
        self.player = SpaceCraft(init_values[0],init_values[1],init_values[2],init_values[3])
        
        #Creating 20 obstacles and starting their animation loops
        self.obstacle_list = []
        for num_obs in range(20):
            self.obstacle_list.append(Obstacles(self.player))
        
        #Starting the player's gameloop
        self.gameloop()
        #Defining the inputs for the SpaceCraft controls
        turtle.onkeypress(self.player.thrust, 'Up')
        turtle.onkeypress(self.player.left_turn, 'Left')
        turtle.onkeypress(self.player.right_turn, 'Right')
        #These two lines must always be at the BOTTOM of __init__
        turtle.listen()
        turtle.mainloop()

    def gameloop(self):
        self.player.move()
        try:
            for obst in self.obstacle_list:
                obst.animate(self.player)
            if self.player.y_pos <=20:
                self.player.check_win()
            else:
                turtle.ontimer(self.gameloop,30)
        except Collision_Error:
            self.player.write("You crashed!")
        except Good_Landing_Error:
            self.player.write("Successful Landing!")

class SpaceCraft(turtle.Turtle):
    '''
    Purpose: An SpaceCraft object represents the player-controllable object within the game.
    Instance variables: 
        x_pos - The x-position of the SpaceCraft in the turtle window
        y_pos - The y-position of the SpaceCraft in the turtle window
        x_vel - The x-velocity of the SpaceCraft in the turtle window
        y_vel - The y-velocity of the SpaceCraft in the turtle window
        fuel - The integer value of fuel left. When this becomes zero, the player can no longer control the ship.
    Methods:
        __init__ - initializes a SpaceCraft object, setting its initial heading to be upwards and moving it to its initial position
        move - updates the x and y positions of the SpaceCraft based on the x and y velocities, as well as consistently decreasing 
            the y velocity in order to simulate a constant acceleration effect. If the new position would be outside the left or right
            bounds of the turtle window, the position is set to the opposite side of the turtle window to simulate a "wraparound" 
            effect by using the absolute value function and modulus operator to keep the positions between 0-500.
        thrust - if the fuel remaining is >0, increases the velocity of the SpaceCraft by a magnitude of 1 in the direction it's 
            currently oriented, decrementing then printing out the remaining fuel. If there is no fuel, simply prints 'Out of fuel'.
        left_turn - if the fuel remaining is >0, changes the orientation of the SpaceCraft by 15 degrees counter-clockwise, 
            decrementing then printing out the remaining fuel. If there is no fuel, simply prints 'Out of fuel'.
        right_turn - if the fuel remaining is >0, changes the orientation of the SpaceCraft by 15 degrees clockwise, 
            decrementing then printing out the remaining fuel. If there is no fuel, simply prints 'Out of fuel'.
        check_win - checks if the magnitude of the x and y velocity are both below 3, raising a Good_Landing_Error if both of
            these conditions are satisfied, otherwise raises a Collision_Error.
    '''
    def __init__(self, x_pos, y_pos, x_vel, y_vel):
        turtle.Turtle.__init__(self)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.fuel = 40
        self.left(90)
        self.penup()
        self.speed(0)
        self.color("red")
        self.goto(self.x_pos, self.y_pos)

    def move(self):
        self.y_vel -= 0.0486
        self.x_pos = abs((self.xcor() + self.x_vel) % 500)
        self.y_pos = self.ycor() + self.y_vel
        self.goto(self.x_pos,self.y_pos)
    
    def thrust(self):
        if self.fuel > 0:
            self.fuel-=1
            angle = math.radians(self.heading())
            self.x_vel += math.cos(angle)
            self.y_vel += math.sin(angle)
            print(f'{self.fuel} fuel units remaining.')
        else:
            print('Out of fuel')
    
    def left_turn(self):
        if self.fuel > 0:
            self.fuel-=1
            self.left(15)
            print(f'{self.fuel} fuel units remaining.')
        else:
            print('Out of fuel')
            
    def right_turn(self):
        if self.fuel > 0:
            self.fuel-=1
            self.right(15)
            print(f'{self.fuel} fuel units remaining.')
        else:
            print('Out of fuel')

    def check_win(self):
        y_condition = abs(self.y_vel) < 3
        x_condition = abs(self.x_vel) < 3
        if y_condition and x_condition:
            raise Good_Landing_Error
        else:
            raise Collision_Error

class Obstacles(SpaceCraft):
    '''
    Purpose: An object of this class represents an obstacle with collision and basic
    animation support. It serves as the obstacle for the spacecraft to avoid. It also
    inherits from SpaceCraft, mainly to use its constructor.
    Instance variables:
        Contains all of the instance variables from SpaceCraft class.
        self.safe_range - the integer range beyond which an Obstacle can be spawned. 
        self.collision_range - the integer range at which a SpaceCraft is deemed to collide with the Obstacle.
    Methods:
        __init__ - Uses the SpaceCraft constructor to instantiate the instance variables from there, then creates the
            remaining instance variables that are unique to Object. Sets the color and shape of the turtle cursor as well.
            Finally, moves the Obstacle to a new location by calling the relocate_obstacle method with the ship passed as a
            parameter.
        animate - This is the main method that is called within the gameloop. Moves the Obstacle by incrementing 
            the current position by the x and y velocity. Then, calls check_collision to see if the Obstacle collides
            with the SpaceCraft --passed in as ship--. Finally, checks if the Obstacle is still within the bounds of the 
            turtle window using check_on_screen, calling relocate_obstacle if it is off-screen.
        check_collision - uses self.collision_range and the generic Cartesian distance formula sqrt(x^2 + y^2) to determine
            whether the Obstacle and the ship object (though it is polymorphic!) are within collision range, raising
            a Collision_Error if they are.
        check_on_screen - evaluates whether the x and y coordinates of the Obstacle are within the turtle window bounds.
        get_safe_quadrants - Takes in the Obstacle and ship (either another Obstacle or SpaceCraft), and determines which quadrants
            are possibilities for the Obstacle to be moved into without violating the self.safe_range condition. The quadrants are
            defined in the method, and are relative to the ship's position. The method checks if there is a valid location both within 
            the bounds of the turtle window, and outside the safe_range of the ship, appending that quadrant to a returned list if it is valid.
        relocate_obstacle - Uses get_safe_quadrants to determine possible new areas for the Obstacle to be moved to, then selects one of the
            possible quadrants at random. Based on the selected quadrant, a new position is randomly generated within that quadrant, and the
            Obstacle's x and y positions are set to those new values. The Obstacle is assigned a new velocity as well, and moved to the new 
            location while hidden from view.  
    '''
    def __init__(self, ship):
        SpaceCraft.__init__(self, 0,0,0,0)
        self.shape("circle")
        self.color("gray")
        self.safe_range = 30
        self.collision_range = 6
        self.relocate_obstacle(ship)
        
    def animate(self, ship):
        self.x_pos = self.xcor() + self.x_vel
        self.y_pos = self.ycor() + self.y_vel
        self.goto(self.x_pos,self.y_pos)
        self.check_collision(ship)
        if not self.check_on_screen():
            self.relocate_obstacle(ship)

    def check_collision(self, ship):
        current_range = math.sqrt((self.x_pos - ship.x_pos)**2 + (self.y_pos - ship.y_pos)**2)
        if current_range < self.collision_range:
            raise Collision_Error
    
    def check_on_screen(self):
        y_condition = self.y_pos > 0 and self.y_pos < 500
        x_condition = self.x_pos > 0 and self.x_pos < 500
        if y_condition and x_condition:
            return True
        else:
            return False
        
    def get_safe_quadrants(self, ship):
        #Quadrant 1: top-left
        #Quadrant 2: top-right
        #Quadrant 3: bottom-left
        #Quadrant 4: bottom-right
        #All quadrants relative to the ship
        open_quadrants = []
        #This section is checking whether the ship is too close to the boundary of
        #the screen for an object to be safely spawned outside of a safe_range of
        #the ship, and appending each "open" quadrant to a list.
        if ship.y_pos < 500-self.safe_range:
            if ship.x_pos > self.safe_range:
                open_quadrants.append(1)
            if ship.x_pos < 500-self.safe_range:
                open_quadrants.append(2)
        if ship.y_pos > self.safe_range+75:
            if ship.x_pos > self.safe_range:
                open_quadrants.append(3)
            if ship.x_pos < 500-self.safe_range:
                open_quadrants.append(4)
        return open_quadrants

    def relocate_obstacle(self, ship):
        #Getting the open quadrants
        open_quads = self.get_safe_quadrants(ship)
        selected_quad = random.choice(open_quads)
        
        #Setting new positions for the obstacle based on open quadrants
        if selected_quad == 1:
            new_x = random.uniform(0, ship.x_pos - self.safe_range)
            new_y = random.uniform(ship.y_pos + self.safe_range, 500)
        elif selected_quad == 2:
            new_x = random.uniform(ship.x_pos + self.safe_range, 500)
            new_y = random.uniform(ship.y_pos + self.safe_range, 500)
        elif selected_quad == 3:
            new_x = random.uniform(0, ship.x_pos - self.safe_range)
            new_y = random.uniform(75, ship.y_pos - self.safe_range)
        elif selected_quad == 4:
            new_x = random.uniform(ship.x_pos + self.safe_range, 500)
            new_y = random.uniform(75, ship.y_pos - self.safe_range)

        #Giving the object a new velocity and setting to the new position
        self.hideturtle()
        self.x_pos = new_x
        self.y_pos = new_y
        self.x_vel = random.uniform(-3,3)
        self.y_vel = random.uniform(-3,3)
        self.goto(self.x_pos, self.y_pos)
        self.showturtle()
        
class Collision_Error(Exception):
    #This is a custom error type to raise if the ship collides with an obstacle or crash lands
    pass

class Good_Landing_Error(Exception):
    #This is a custom error type to raise if the ship lands successfully
    pass

if __name__ == '__main__':
    Game()
