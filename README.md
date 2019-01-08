RENJU build 2.3 RELEASE NOTES
=====
*Author: Pranshu Gupta*
---------------------

![renju.png](renju.png)

LIST OF CHANGES MADE IN BUILD 2.3

1. Removed the dependency on wxPython. The application can now run 
   with only Pygame installed along with Python.

2. User can now choose the color of his/her coin.

3. There was a bug in previous builds due to which the coins placed
   placed on the board used to dissappear if the application window
   was minimized. This bug has been removed.

4. The user can save an unfinished game and resume it later.

5. Added support to undo the last move during the game. This feature
   is disabled by default. The user can always enable it before the 
   game starts.

6. The notifications now appear in the game window only.
   Pop-up windows have been deprecated. A side pane has been added to
   the board for this purpose.

7. The user can restart the game any time.

8. The code for placing the coin has been improved.

9. Two player mode has been removed.

10. Added notifications telling whose turn is it.
