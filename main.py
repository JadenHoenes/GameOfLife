#Imports
import random
import time

#Main function - instantiates Game and runs it
def main():
    gameOfLife = Game(50)
    gameOfLife.run()

#Cell Class - Main building block of a generation
#Includes logic to randomly populate the board with initial generation
#shouldLive holds a boolean to determine if it survives the current generation
#status holds the character to print
class Cell:
    def __init__(self):
        self.shouldLive = True
        randomNumber = random.random()
        if randomNumber > 0.33:
            self.status = " "
        else:
            self.status = "X"

#Generation - Main logic, handles rules and printing of game
class Generation:
    def __init__(self): #Initialize 22x22 list of Cells
        self.population = [[Cell() for x in range(0, 23)] for y in range(0, 23)]

    def print(self): #Prints 20x20 generation
        for i in range(len(self.population)):
            for j in range(len(self.population[i])):
                if i < 21 and i > 0 and j < 21 and j > 0:
                    print(self.population[i][j].status,end = " ")
            print()

    def determineNumNeighbors(self, row, col): #Checks all valid spots for living neighbors, counts them, returns result
        count = 0
        spot1 = self.population[row-1][col-1]
        spot2 = self.population[row-1][col]
        spot3 = self.population[row-1][col+1]
        spot4 = self.population[row][col-1]
        spot5 = self.population[row][col+1]
        spot6 = self.population[row+1][col-1]
        spot7 = self.population[row+1][col]
        spot8 = self.population[row+1][col+1]
        list1 = [spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8]
        for i in list1:
          if (row-1 > 0 and row+1<21 and col-1 > 0 and col+1 < 21) and i.status=="X":
            count+=1
        return count

    def newGenerationCreation(self): #Handles logic of creating the next generation, first determines if each cell should survive, then updates the display value
        for i in range(len(self.population)):
            for j in range(len(self.population[i])):
                if i < 21 and i > 0 and j < 21 and j > 0: #This handles the rules of survival, underpopulated, overpopulated, and reproduction
                    currentCell = self.population[i][j]
                    numNeighbors = self.determineNumNeighbors(i, j)
                    if numNeighbors < 2:
                        currentCell.shouldLive = False
                    if numNeighbors > 3:
                        currentCell.shouldLive = False
                    if (numNeighbors == 3 or numNeighbors == 2) and currentCell.status=="X":
                        currentCell.shouldLive = True
                    if numNeighbors == 3:
                        currentCell.shouldLive = True
        for i in range(len(self.population)): #This updates display values
            for j in range(len(self.population[i])):
                if i < 21 and i > 0 and j < 21 and j > 0:
                  currentCell = self.population[i][j]
                  if currentCell.shouldLive:
                    currentCell.status = "X"
                  else:
                    currentCell.status = " "
                  self.population[i][j] = currentCell
        
class Game: #Manages order of operations for game, generations = number of generations to play through
    def __init__(self, generations):
        self.generations = generations
    def run(self): #Make first generation, loop 'generations' amount of times, in each generation print board, update the generation, then wait .3 seconds
        currentGeneration = Generation()
        for i in range(self.generations):
            currentGeneration.print()
            print("   Generation: ", i+1)
            currentGeneration.newGenerationCreation()
            time.sleep(0.3)

main()
