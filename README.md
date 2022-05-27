# APCSFinal_CastroValadezSandra

Clock App: 

At the very beginning of the code I imported tkinter, which was already on the raspberry pi. Then, I named the window as Clock App. Afterwards, I defined the clock and created the hour, minute, and second variables that would be used for the clock. The “%I” allows the clock to display a 12 hour time, not military.  The label2.config and label.after tell the clock to update after a certain amount of time. The function update changes the text on the screen, which are the numbers and the semicolon that makeup the clock, to update. Then, label2 and label2.pack pick the font, size, background, and foreground color. Lastly, the function is called. When the code is run, a clock with blue text and a 12 hour time period is displayed. 

Password Generator App:

First random is imported. Then using print, the user is told “Hi! Let's generate a password” so they know what the purpose of the app is. Then, a list of characters is created that will be used to generate the password later. Using passwordLenght, the user is asked how many characters they want and using this input, the program now understands how long the user wants the password to be. Afterwards, newpassword is used to append a random character to the password string. Then the finalpassword is used to join the list back into a string.  At the end of the code, the user is told their newpassword. 
