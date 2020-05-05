
# PyBluesky
### Version : 1.0.2

A simple python game to navigate your jet and fight though a massive missiles attack based on pygame framework</br>
Based on https://realpython.com/blog/python/pygame-a-primer

Author : Lakhya Jyoti Nath (ljnath)<br>
Date : April 2020<br>
Email : ljnath@ljnath.com<br>
Website : https://www.ljnath.com


[![Download PyBluesky](https://sourceforge.net/sflogo.php?type=13&group_id=3215162)](https://sourceforge.net/p/ljnath/)  
[![Download PyBluesky](https://img.shields.io/sourceforge/dt/ljnath.svg)](https://sourceforge.net/projects/ljnath/files/latest/download)

## Change Log

### [1.0.3] - 2020-05-05 (in development)
- changed API key handling from network handler to main game file
- changes game asset names to lowercase for UNIX comaptibity and changed name to be more meaningful
- changes game asset path name for UNIX comaptibity
- fixed hint text in player name input screen
- removed unused game assets

### [1.0.2] - 2020-05-04
- added support for player name, games prompts to enter the name for the 1st time and saving to file
- added support for automatically loading exitsing player name from file
- added support for player name to be used for submitting game result
- added special hint in the input name menu
- added support to save game level data along with game score
- added support to boost enemy missle speed by 5% after each 10th level
- changed starting missile count from 4 to 2 
- changed missile increase factor per level  to half
- changed input mode selection message in gamemenu sprite
- changed jet speed from 8 to 7
- changes TitleScreen enum to Screen as it has all type of screen information
- changed bullet speed from 5 to 7, to avoid jet hitting its own bullet
- changed game icon, shortcut icon
- fixed leaderboard rendereing issue related to alignment
- fixed help message
- replace duplicate codes with list comprehension
- removed capturing of system username

### [1.0.1] - 2020-05-03
- added leaderboard functionality (requires internet)
- added game help menu
- added support to toggle between menu in game start and gameover screen
- added support to upload game score and current system user to remote api
- added support to check for game update at startup
- added support for clouds to notify user about new game update
- added support for dynamic menu spries creation instead for pre-created sprites
- changed main game music
- removed game sound for jet move up and move down (no more licenses)

### [1.0.0] - 2020-05-02
- renamed game to PyBluesky
- added background vegetation support
- added packaging support

### [0.12] - 2020-05-02
- updated sprite for bullet, jet
- added support for flashing powerup star, flash rate is configurable in the class
- added music which powerup is activated
- added sprite for deactivated missiles to distinguishing between activated ones

### [0.11] - 2020-05-01
- added powerup star which will mark all active missiles as bad
- added suport for collision detection between the jet and its bullet
- consuming powerup will increase game score by 100

### [0.10] - 2020-05-01
- added ammo limit, game starts with 100 ammo and 50 is added pn every level up (max ammo can be 999)
- added support for game to run in full screen by default
- added support to dynamically set game resolution as the monitor resolution
- channged score sprite color to dark grey
- change levelup time from 10s to 20s

### [0.9] - 2020-05-01
- added shoot functionality for the jet by clicking mouse of pressing spacebar
- updated score calculation, now destroying 1 missile gives 10 pts
- added game instruction in welcome screen
- added sound effects for shooting and destroying missiles

### [0.8] - 2020-04-27
- added methods to continously move text on either X or Y axis
- added author sprite in the game menu

### [0.7] - 2020-04-26
- added game title in the menu
- added support for level up in the game, missile count will increase every level
- added sound for level up
- removed redundant condition check in jet sprite
- renamed GameInputText to GameMenuText

### [0.6] - 2020-04-26
- refactored game code into modules based on sprite
- introduced game environment to maintain and share game environment data across different various modules

### [0.5] - 2020-04-26
- added support for continous jet movement towards cursor; even on fixed mouse position

### [0.4] - 2020-04-26
- added suport for mouse movement as game input
- added input mode screen on game start
- fixed replay text sprite rendering

### [0.3] - 2020-04-25
- added support for game replay

### [0.2] - 2020-04-24
- refactored code and added comments
- changed jet image and collision sound
- changed cloud image and added support for random cloud design

### [0.1] - 2020-04-23
- first version with default game play
- added gameover message during collision
- added game scoring and playtime


## Demo

![](gameplay.gif)