# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

SIGNAL_FUNCTIONS = ["cos","cot","tan","cot","sin","csc"]

class Signal:
    #when this class initializes, it will split apart a given string into it's different components. takes a signal string.
    def __init__(self, signal):
        #This is the main string that saves the raw inputted data
        self.rawSignal = signal
        self.type = "ERROR"
        self.steps = ""
        self.functions = []
        self.split_into_fund(signal)



    #Takes the raw signal string and splits it into values needed by the program
    def split_into_fund(self,rawsignal):
        functions = []
        c = 0

        if "[n]" in rawsignal:
            self.type = "D"
            self.steps += " This signal is discrete since there are n values on the interval \n"
            rawsignal.replace("(t)", "")
        elif "(t)" in rawsignal:
            self.type = "C"
            self.steps += " This signal is continous since values are on an infinite (time) interval \n"
            rawsignal = rawsignal.replace("(t)", "")

        for sig in SIGNAL_FUNCTIONS:
            if sig in rawsignal:
                print("THis is rawsignal = " + rawsignal)
                temp = rawsignal[rawsignal.find(sig):rawsignal.find("}")+1]
                print("This is the temp str " + temp)
                fStart = temp.find("{")
                fEnd = temp.find("}")
                if fEnd == fStart:
                    print("yes")
                else:
                    print("FOUND AT POS " + str(fStart) + "-" + str(fEnd))
                    f = temp[1+fStart:fEnd]
                    self.functions.append([sig,f])
                    print("Length of signal " + str(len(rawsignal)))
                    rawsignal = rawsignal[fEnd:len(rawsignal) + 1]
                    print("This is the next function " + rawsignal)
                    self.steps += str(self.functions) + " Trig function found in the typed signal"








# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    signal = "x(t) = cos{2t} + sin{(1/3)t}"
    sig = Signal(signal)
    print(sig.steps)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
