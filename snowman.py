"""
DRAW Snowman & empty word UI
SELECT a random word from word list
SET number of wrong guesses to 0
SET max wrong guesses

WHILE word not guessed AND wrhong guesses < max:
    ASK user for a letter
    IF letter in word:
        REVAL letter in word UI
    ELSE:
        INCREMENT wrong guesses
        REMOVE part of the snowman

IF word guessed:
    PRINT "You win!"
ELSE:
    PRINT "You lose!" and reval the word
"""

