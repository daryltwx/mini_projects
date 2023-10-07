# Day 22:

Recreate the game of Pong using turtle. 

7 October 2023:
1. Break down the problem.

---

Step 1. Create display screen
- 
- Configure the screen aspect ratio (16:9) convert this to pixels.
- Create a class to host, the following:
  - The line in the middle, splitting the screen into two parts. 
  - Score keeping for Player 1 / 2.

Step 2. Create the bars
-
- Create the bars that the users will control, using class
- Controls: Left player - "w, s", Right player - "Up, Down"
- Set bar length to 3-4 squares.
- Set movement to be up/down only.
  - Unlike the snake where the head is the only determinant of movement, 
  use the far ends of the bar to control movement. 

Step 3. Create the ball
-
- Using class
- (def) And figure out the movement. 
  - How to have the ball move in diagonals if strike at a particular part of the bar.


Step 4. Create boundaries
- 
- If the ball touches the top or bottom screen, it will bounce (movement of the opposite direction)
- If ball touches left or right side of the screen. Calculate the score, if ball goes left, right scores vice versa.


Step 5. Create End condition
- 
If a player's score reaches 10, declare the winner. 



-----

Sample Solution:
-
Step 1. Create the screen

Step 2. Create and move a paddle

Step 3. Create another paddle

Step 4. Create the ball and make it move

Step 5. Detect collision with wall and bounce

Step 6. Detect collision with paddle

Step 7. Detect when paddle misses

Step 8. Keep score

-----

I'm pretty close. I could be more succinct like the sample answer.
And breakdown in simple understandable sentences instead of just adding the technicalities. 