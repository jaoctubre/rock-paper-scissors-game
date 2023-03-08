# A Simple Rock, Paper, Scissors Game

For this python project, we have a classic game of rock, paper, and scissor which asks for the number of games to be played against the computer. The user can stop the game at any point before it has reached the number of trials set in the beginning of the game. After every turn, the program will print the computer's choice as well as the current score for both the user and the computer.

The program also check for valid choices as well the number of trials. Giving an invalid trials nummber will return an error message and start the program again.

**The flow of the the program goes like this:**
```
1. Program asks player for the number of games to be played in a row.
2. The player inputs his choice for the round: rock, paper, or scissors
3. For every turn, the program outputs the computer's choice for the round, gives the result and updates the scores for each.
4. The user can stop the game by choosing 'stop' as choice when asked.
5. This goes on until the number of games is reached or either one gets more than half of the total points.
6. At the end, the program asks if the player wants to play more rounds of the game.
```

**Two Winning Conditions**
- If either player gets more than half of the total points, the game will automatically stop and declare that player as the winner of the game.
- Whoever gets the most points at the end of the game is declared the winner even if they do not get more than half of the total points. This is possible since the program counts ties into the number of games.
