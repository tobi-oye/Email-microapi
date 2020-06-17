Welcome to development branch
To get started:

Make sure you are on a desktop or laptop

Step 1: Click on Fork at the top right corner

Step 2: Click on clone or download, copy the url you see after clicking on it

Step 3: Head to your local machine and create a folder, (this step is not necessary but to keep your work organized on your local machine, you can create folder called ‘github repo’ on your desktop).

Step 4: Open your preferred terminal

Here you have arrays of choice, you could use git bash (you have to download it to use it. Download it here -> [GitHub]https://git-scm.com/downloads)), powershell or your default window terminal.

If you want to use git bash:

4.1 Open the ‘github repo’ folder, remember you saved it on your desktop.

Right-click anywhere in the folder and choose ‘git bash here’, automatically git bash will open.

*If you want to use the terminal

4.2 press Window + R on your keyboard

Step 5:git clone pasteTheUrlOfTheLinkYouCopiedInStep2

It should look like this

git clone https://github.com/{yourGithubUsername}/Email-microapi.git

Step 6: To start your work, work the directory that contains the project files.

cd Email-microapi

Step 7: git remote add upstream https://github.com/microapidev/Email-microapi.git

Step 8: git pull upstream development

Note: you will be on the Master branch automatically.

You need to move out of the Master branch to another branch to start your work.

To move to another branch

Run: git checkout -b <nameOfBranch>
  
You can use any name for your branch.

But for consistency and orderliness, use your slack username

IE: <nameOfBranch> should be replaced with your slack username, use hypen where you will normally use space. That is if you have space in your username. I don’t think anybody does. If you do though, use hypen(-)
  
For example,

git checkout -b sylver-codez :white_check_mark:

git checkout -b sylver codez :x:

Once you are done writing the script and you have tested that everything is working perfectly fine (I.e your code has passed). (Optional: If you could make a screenshot of it and attach your pull request)

Run: git add .


Run: git commit -m "chore: create script"

git push origin username

In my case, it would be

git push origin sylver-codez - (Notice how it ends with the branch you created earlier).

Creating Pull requests

PR === Pull request

Go to github.com, locate the repository you forked in step 1

As soon as you get there, you are going to see a green ‘compare and create a pull request’

Click on it, and type your message, click on create pull request. I will merge as soon as possible

