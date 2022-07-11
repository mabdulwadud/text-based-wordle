# Text-Based Wordle

This basic Python application is, - as the title of this markdown implies -a simple, text-based 'Wordle' application. The idea is simple: you have six(6) tries to guess a randomly generated word. Because this is a text-based version of the game, there are no color codes (yet...*wink, wink*). The rules are outlined in the next section of this document.

# News
**There are some known issues with this mini project. For one, it does not work entirely. It is still very broken. If you treat it well enough,
it might work for you.** 

Known Issues:
- There isn't a specific way to ensure the user doesn't guess a forbidden word; this rule is upheld due to the word list only consisting of five-letter words. A failsafe should be implemented for this. 
- Once you guess a word, guesses are subtracted regardless of word validity.
> For example, if you guess a word that is not in the word list, the number of guesses should not be subtracted.
- There is some bad code that needs to be filtered out.

# Rules

If you aren't familiar with the rules of the game, here are the official rules (as outlined by tomsguide.com):

- You have to guess the Worlde in six goes or less
- Every word you enter must be in the world list.
- A correct letter turns green.
- A correct letter in the wrong place turns yellow.
- An incorrect letter turns gray
- Letters can be used more than once
- Answers are never plurals

Obvously, all of these rules are not applied in this version. Here, the following rules apply:

- You have to guess in six guesses or less.
- The word guessed must be in the list.
- A correct letter is indicated by a tick (check) mark.
- A correct letter in the incorrect position is indicated by an asterisk (\*)
- An incorrect letter is indicated by an X
- Letters can be used more than once
- Answers *can* be plurals as of now

# Future Plans

I'm working on this section right now. More here.


