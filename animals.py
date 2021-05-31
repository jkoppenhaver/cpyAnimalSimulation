import random


###############################################################################
# Class Animal
# Description: This class describes the basic animal attributes and methods
###############################################################################
class Animal(object):
    ###############################################################################
    # __init__
    # Description: This function initializes a new animal object.
    # Arguments: this_color - The color this animal should be represented as
    #            blank_color - The background color that signifies a space is unoccupied
    #            dispBuff - The display buffer this object should use
    # Returns: Nothing
    ###############################################################################
    def __init__(self, this_color, blank_color, dispBuff):
        self.blank_color = blank_color
        self.color = this_color
        self.x = random.randint(0, len(dispBuff) - 1)
        self.y = random.randint(0, len(dispBuff[0]) - 1)
        while dispBuff[self.x][self.y] != self.blank_color:
            self.x = random.randint(0, len(dispBuff) - 1)
            self.y = random.randint(0, len(dispBuff[0]) - 1)
        dispBuff[self.x][self.y] = self.color
        return

    ###############################################################################
    # __decideDirection
    # Description: This function decides how the animal should move next.
    #             This function is private and should only be called from within the class
    # Arguments: dispBuff - The display buffer this object should use
    # Returns: The chosen direction.  This direction is guaranteed to be a valid move
    ###############################################################################
    def __decideDirection(self, dispBuff):
        direction = random.randint(0, 3)
        while not self.__isValidMove(direction, dispBuff):
            direction = random.randint(0, 3)
        return direction

    ###############################################################################
    # __isValidMove
    # Description: This function determines if a direction is safe to move in.
    #             The default animal can move into any space that is on the display and unoccupied
    # Arguments: direction - The direction to be checked
    #            dispBuff - The display buffer this object should use
    # Returns: Boolean representing if the move is valid or not
    ###############################################################################
    def __isValidMove(self, direction, dispBuff):
        valid = False
        if direction == 0:
            # Move down
            if (self.y + 1) < len(dispBuff[0]) and dispBuff[self.x][self.y + 1] == self.blank_color:
                valid = True
        elif direction == 1:
            # Move right
            if (self.x + 1) < len(dispBuff) and dispBuff[self.x + 1][self.y] == self.blank_color:
                valid = True
        elif direction == 2:
            # Move up
            if (self.y - 1) >= 0 and dispBuff[self.x][self.y - 1] == self.blank_color:
                valid = True
        elif direction == 3:
            # Move left
            if (self.x - 1) >= 0 and dispBuff[self.x - 1][self.y] == self.blank_color:
                valid = True
        return valid

    ###############################################################################
    # move
    # Description: This function moves the animal one space in the direction decided by __decideDirection
    #             It moves the animal and then updates the display buffer to render the new location.
    #             *Note* This function only updates the display buffer.  It will not change the actual display.
    # Arguments: dispBuff - The display buffer this object should use
    # Returns: Boolean representing if the move is valid or not
    ###############################################################################
    def move(self, dispBuff):
        direction = self.__decideDirection(dispBuff)
        dispBuff[self.x][self.y] = self.blank_color
        if direction == 0:
            self.y += 1
        elif direction == 1:
            self.x += 1
        elif direction == 2:
            self.y -= 1
        elif direction == 3:
            self.x -= 1
        dispBuff[self.x][self.y] = self.color
        return


###############################################################################
# Class Prey
# Parent: Animal
# Description: This class inherits from Animal and overloads the some of
#             the functions to provide prey specific behavior.  The only
#             difference from Animal is that prey have 4 'directions' they
#             can choose from.  They can move up, down, left , right, or hide.
#             When prey hide they do not move at all and continue to occupy
#             their current space.
###############################################################################
class Prey(Animal):
    def __decideDirection(self, dispBuff):
        direction = random.randint(0, 4)
        while (not self.__isValidMove(direction, dispBuff)) and direction != 4:
            direction = random.randint(0, 4)
        return direction


###############################################################################
# Class Predator
# Parent: Animal
# Description: This class inherits from Animal and overloads the some of
#             the functions to provide predator specific behavior.  This
#             includes chasing prey instead of moving randomly.
###############################################################################
class Predator(Animal):
    ###############################################################################
    # __init__
    # Description: This function initializes a new predator object.  It is
    #             the same as the Animal initializer except that it takes an
    #             extra argument that represents what color it should search
    #             for and chase.
    # Arguments: this_color - The color this animal should be represented as
    #            blank_color - The background color that signifies a space is unoccupied
    #            prey_color - The prey color that this predator should chase
    #            dispBuff - The display buffer this object should use
    # Returns: Nothing
    ###############################################################################
    def __init__(self, this_color, blank_color, prey_color, dispBuff):
        super().__init__(this_color, blank_color, dispBuff)
        self.blank_color = blank_color
        self.color = this_color
        self.prey = prey_color
        self.x = random.randint(0, len(dispBuff) - 1)
        self.y = random.randint(0, len(dispBuff[0]) - 1)
        while dispBuff[self.x][self.y] != self.blank_color:
            self.x = random.randint(0, len(dispBuff) - 1)
            self.y = random.randint(0, len(dispBuff[0]) - 1)
        dispBuff[self.x][self.y] = self.color
        return

    ###############################################################################
    # __isValidMove
    # Description: This function determines if a direction is safe to move in.
    #             The predator can move into any open space or a space occupied by prey
    # Arguments: direction - The direction to be checked
    #            dispBuff - The display buffer this object should use
    # Returns: Boolean representing if the move is valid or not
    ###############################################################################
    def __isValidMove(self, direction, dispBuff):
        valid = False
        if direction == 0:
            # Move down
            if ((self.y + 1) < len(dispBuff[0]) and (
                    dispBuff[self.x][self.y + 1] == self.blank_color or dispBuff[self.x][self.y + 1] == self.prey)):
                valid = True
        elif direction == 1:
            # Move right
            if ((self.x + 1) < len(dispBuff) and (
                    dispBuff[self.x + 1][self.y] == self.blank_color or dispBuff[self.x + 1][self.y] == self.prey)):
                valid = True
        elif direction == 2:
            # Move up
            if ((self.y - 1) >= 0 and (
                    dispBuff[self.x][self.y - 1] == self.blank_color or dispBuff[self.x][self.y - 1] == self.prey)):
                valid = True
        elif direction == 3:
            # Move left
            if ((self.x - 1) >= 0 and (
                    dispBuff[self.x - 1][self.y] == self.blank_color or dispBuff[self.x - 1][self.y] == self.prey)):
                valid = True
        return valid

    ###############################################################################
    # __decideDirection
    # Description: This function decides how the animal should move next.
    #             This function is private and should only be called from within the class
    #             For the predator, it searches for prey and moves towards the closest one.
    #             It also differs from the default __decideDirection method in that it does
    #             not matter if the space is occupied.
    # Arguments: dispBuff - The display buffer this object should use
    # Returns: The chosen direction.  This direction is guaranteed to be a valid move
    ###############################################################################
    def __decideDirection(self, dispBuff):
        direction = 0
        prey_locations = []
        # Look for prey and add all found locations to the prey_locations list
        for i in range(len(dispBuff)):
            for j in range(len(dispBuff[i])):
                if dispBuff[i][j] == self.prey:
                    prey_locations.append((i, j))
        if len(prey_locations) == 0:
            # No prey found so just move randomly
            direction = random.randint(0, 3)
            while not self.__isValidMove(direction, dispBuff):
                direction = random.randint(0, 3)
        else:
            # Determine the closest prey
            smallest_diff = 20
            smallest_index = 0
            for i in range(len(prey_locations)):
                diff = abs(prey_locations[i][0] - self.x) + abs(prey_locations[i][1] - self.y)
                if diff < smallest_diff:
                    smallest_diff = diff
                    smallest_index = i
            xdiff = prey_locations[smallest_index][0] - self.x
            ydiff = prey_locations[smallest_index][1] - self.y
            # Because the predators can not move diagonally, pick the axis with the largest
            # difference and move in that direction towards the prey.
            # The predator attempts to move towards the prey,
            # if that doesn't work, it tries to go around the block by moving perpendicular,
            # if that doesn't work, it tries to go around the block by moving away from the prey,
            # as a last resort, it will just wait until the bock moves.
            if abs(xdiff) > abs(ydiff):
                if xdiff > 0:
                    if self.__isValidMove(1, dispBuff):
                        direction = 1
                    elif self.__isValidMove(0, dispBuff):
                        direction = 0
                    elif self.__isValidMove(2, dispBuff):
                        direction = 2
                    elif self.__isValidMove(3, dispBuff):
                        direction = 3
                    else:
                        direction = 4
                else:
                    if self.__isValidMove(3, dispBuff):
                        direction = 3
                    elif self.__isValidMove(0, dispBuff):
                        direction = 0
                    elif self.__isValidMove(2, dispBuff):
                        direction = 2
                    elif self.__isValidMove(1, dispBuff):
                        direction = 1
                    else:
                        direction = 4
            else:
                if ydiff > 0:
                    if self.__isValidMove(0, dispBuff):
                        direction = 0
                    elif self.__isValidMove(1, dispBuff):
                        direction = 1
                    elif self.__isValidMove(3, dispBuff):
                        direction = 3
                    elif self.__isValidMove(2, dispBuff):
                        direction = 2
                    else:
                        direction = 4
                else:
                    if self.__isValidMove(2, dispBuff):
                        direction = 2
                    elif self.__isValidMove(1, dispBuff):
                        direction = 1
                    elif self.__isValidMove(3, dispBuff):
                        direction = 3
                    elif self.__isValidMove(4, dispBuff):
                        direction = 4
                    else:
                        direction = 4
        return direction
