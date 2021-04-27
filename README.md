Problem: Given a balance scale and 9 gold bars of the same size and look. You don’t know the exact weight of each bar, but you know they are the same weight, except for only one fake bar. It weighs less than others. You need to find the fake gold bar by only bars and balance scales. You can only place gold bars on scale plates (bowls) and find which scale weighs more or less.  

### My solution:  
Since there are 9 gold bars, in the first iteration we can single out one of the gold bars and weigh the other 8 bars on the scale. If the scale says equals, then the bar that has been singled out is the fake gold bar. Otherwise, check which side weigh less and choose that side to measure. From now on, there are even numbers of bars so we can weigh until only one bar is left and that will be the fake gold bar.

### Files included:  
		findfake.py  
		README  

### Commands to run (Linux):   
		You might need give read permission.  
		`chmod 550 findfake.py`  
		`python3 findfake.py`  
### Commands to run (Windows):  
		Tested on Visual Studio Code  
		`CTRL + F5`  
		

