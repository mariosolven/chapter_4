## Learn Python the Hard Way - Exercise 26.

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words): # added a colon at the end.
    """Prints the first word after popping it off."""
    word = words.pop(0) # changed '.poop' to '.pop'
    print (word) # added parenthesis to 'word'.

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) # the parenthesis wasn't closed at the end.
    print (word) # added parenthesis to 'word'.

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# added parenthesis in order to print in both lines 40 & 41.
print ("Let's practice everything.")
print ('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""

# added parenthesis in order to print in lines 53, 54 & 55.
print ("--------------")
print (poem)
print ("--------------")

five = 10 - 2 + 3 - 6 # changed the 5 for 6 because the ecuation didn't equals 5.
print ("This should be five: %s" % five) # added parenthesis in order to print.

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000 # changed the '\' for the correct one: '/' to divide.
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
# changed 'beans' for 'jelly_beans'.
# changed the '==' to '=' and the '-' to '_'.
jelly_beans, jars, crates = secret_formula(start_point)

# added parenthesis in order to print in both lines 73 & 75.
print ("With a starting point of: %d" % start_point)
print ("We'd have %d beans, %d jars, and %d crates." % (jelly_beans, jars, crates)) # changed 'jeans' for 'jelly_beans'.

start_point = start_point / 10

# added parenthesis in order to print in both lines 79 & 80.
print ("We can also do that this way:") 
print ("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)) #the 'crabapples' was changed for 'crates' and the '(start_pont' for '(start_point)'.

# changed 'god' for 'good', 'weight' for 'wait'.
# the '\t' was deleted.
sentence = "All good things come to those who wait."

# deleted the 'ex25.' in both lines 80 & 81.
words = break_words(sentence)
sorted_words = sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words) # deleted de '.'.
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence) # deleted the 'ex25.'
# changed 'prin' for 'print'.
# added parenthesis in order to print.
print (sorted_words)

print_first_and_last(sentence) # changed 'irst' for 'first'.

# removed the white space.
# changed 'a' for 'and' and 'senence' for 'sentence'.
print_first_and_last_sorted(sentence)
