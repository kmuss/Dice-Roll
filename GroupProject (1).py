import random
#start() function to prompt user for a positive integer n with error checking and meaningful error messages.
def start():
    done = False
    while not done:
        integer = input("Please enter a positive integer:\n")
        try:
            integer2=int(integer)
            if integer2 < 1:
                print(integer + " is not a positive integer!\n")
            else:
                done = True
        except ValueError:
            print(integer + " is not an integer!")
    return int(integer)
    ''' the start function asks the users to input a positive integer and given their input, if it is a positive integer, it will accept the 
    value. And if it's anything other than a positive integer, it will prompt the user to try again'''
#roll() function to roll dice of 1-to-6 n
def roll():
    dice = random.randint(1, 6)
    return dice
    '''This function is used to generaet a random number between 1 and 6, as if it was a dice. The return function calls back the number that's been rolled'''
#stat() to generate and report counts and percentage distribution in text
def stat():
    length = start()
    firstlist = []
    secondlist = [0]*6

    for counts in range(length):
        die = roll()
        firstlist.append(die)

    for tally in firstlist:
        secondlist[tally-1] += 1

    count = 1
    for output in secondlist:
        if count == 6:
            print(count, " was rolled ", output, ' times')
        else:
            print(count, " was rolled ", output, ' times, ', end='')
        count += 1

    index = 1
    for output in secondlist:
        if index == 6:
            print(index, " was rolled %.2f" % ((output/length)*100), '% ')
        else:
            print(index, " was rolled %.2f" % ((output/length)*100), '%, ', end='')
        index += 1
    '''this function first begins with setting a variable to equal the number inputted by the user. Then, it creates two
    lists. The length of the first list is determined by the amount the user entered. The second list is meant to keep only goes up
    to 6 positions. the first four loop populates the first list with randomly generated numbers from the roll function, and it will
    append the numbers onto the list. Second for loop runs through the first four loop and tallys up the different randomly generated numbers 
    that were appended into the first list. Finally, 
    Next, we initialized count to one and then ran a four loop to count the tallys and set an if condition to print out the desired result, 
    which in this case was to see how many times a certain number was rolled.
    Lastly, we initialized index to = 1 and then ran another for loop through the tally list (secondlist), and printed out the result that
    amount of roll and divided it by the users initial input to find the percentages'''
def main():
    stat()
    '''under the main function, we called back the stat function to run'''

if __name__ == "__main__":
    main()





