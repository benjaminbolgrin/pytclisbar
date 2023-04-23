# "pytclisbar" is a threaded command line interface status bar for Python.
# Author: Benjamin Bolgrin

# Usage:
# Import the StatusBar class from the pytclisbar module
# Initialize a StatusBar object by providing a headline and the total number of your loop's iterations
# Start the status bar by calling the 'start()' method
# Update the status by calling the 'setCurrentIteration()' method

# Modify the bar length by calling the 'setStatusBarLength()' method.
# Modify the spinner speed by calling the 'setSpinnerSpeed()' method.
# Modify the status bar prefix by calling the 'setStatusBarPrefix()' method.
# Modify the status bar suffix by calling the 'setStatusBarSuffix()' method.
# Modify the 'current iteration' char by calling the 'setCurrentIterationChar()' method.
# Modify the 'iterations left' char by calling the 'setIterationsLeftChar()' method.

# It's recommended to call the 'join()' method, to synchronize threads before proceeding with your program.

from threading import Thread
import time


class StatusBar(Thread):

    def __init__(self, statusHeadline: str = "", totalIterations: int = 0) -> None:

        super().__init__()

        self.animationStepOne: str = '|'
        self.animationStepTwo: str = '/'
        self.animationStepThree: str = '-'
        self.animationStepFour: str = '\\'
        self.animationStepFive: str = '/'
        self.animationStepSix: str = '-'
        self.animationStepSeven: str = '\\'

        self.statusHeadline: str = statusHeadline
        self.totalIterations: int = totalIterations

        self.barLength: int = 20
        self.currentIterationChar: str = '|'
        self.iterationLeftChar: str = '.'
        self.currentIterationString: str = ''
        self.statusBarPrefix: str = '['
        self.statusBarSuffix: str = ']'
        self.currentIteration: int = 0
        self.percentageDone: float = 0.00
        self.spinnerSpeed: float = 0.25
        self.updateCalculatedValues()

    def run(self) -> None:

        print('\n{}'.format(self.statusHeadline))

        i: int = 1
        while self.currentIteration < self.totalIterations:

            time.sleep(self.spinnerSpeed)

            if i == 1:
                animationStep: str = self.animationStepOne
            elif i == 2:
                animationStep: str = self.animationStepTwo
            elif i == 3:
                animationStep: str = self.animationStepThree
            elif i == 4:
                animationStep: str = self.animationStepFour
            elif i == 5:
                animationStep: str = self.animationStepFive
            elif i == 6:
                animationStep: str = self.animationStepSix
            elif i == 7:
                animationStep: str = self.animationStepSeven
                i -= 7

            print('\r{}{}{}{}{} {:6.2f}%'.format(self.statusBarPrefix, self.currentIterationString,
                                                 animationStep,
                                                 self.iterationsLeftString[1:], self.statusBarSuffix,
                                                 self.percentageDone), end=" ")
            i += 1

        if self.currentIteration == self.totalIterations:

            print('\r{}{}{} {:6.2f}%'.format(self.statusBarPrefix,
                                               self.currentIterationString,
                                               self.statusBarSuffix, self.percentageDone), end=" ")
            print()
            return

    def setCurrentIteration(self, currentIteration: int) -> None:
        self.currentIteration: int = currentIteration
        self.updateValues()

    def updatePercentageDone(self) -> None:
        self.percentageDone: float = self.currentIteration / self.totalIterations * 100

    def updateCurrentIterationString(self) -> None:
        if self.currentIteration == self.totalIterations:
            self.currentIterationString: str = self.barLength * self.currentIterationChar
        else:
            self.currentIterationString: str = int(self.percentageDone // self.barPieces) * self.currentIterationChar

    def updateIterationsLeftString(self) -> None:
        currentIterStringLength = len(self.currentIterationString)
        iterLeftStringLength = self.barLength - currentIterStringLength
        self.iterationsLeftString: str = iterLeftStringLength * self.iterationLeftChar

    def updateValues(self) -> None:
        self.updatePercentageDone()
        self.updateCurrentIterationString()
        self.updateIterationsLeftString()

    def setStatusBarPrefix(self, char: chr) -> None:
        self.statusBarPrefix: chr = char

    def setStatusBarSuffix(self, char: chr) -> None:
        self.statusBarSuffix: chr = char

    def setCurrentIterationChar(self, char: chr) -> None:
        self.currentIterationChar: chr = char

    def setIterationsLeftChar(self, char: chr) -> None:
        self.iterationLeftChar: chr = char

    def setSpinnerSpeed(self, speed: float) -> None:
        self.spinnerSpeed: float = speed

    def setStatusBarLength(self, length: int) -> None:
        self.barLength: int = length
        self.updateCalculatedValues()

    def updateCalculatedValues(self) -> None:
        self.barPieces: float = 100 / self.barLength
        self.iterationsLeftString: str = self.barLength * self.iterationLeftChar
