# 1. gene filtering, cryptography, math modeling, weather projections, data analysis for health predictions
# 2.Climate Data Online Search(find a pattern in the data to forecast weather) , WHO data set (dataset has information for each patient's personal information and medical data, whether or not they have had heart disease before. This will help me find trends and analyze the data) Khan Academy or YouTube vidoes(to learn how to do this)
# 3. Data analysis lists/dictionaries, github, condiotonals, making functions 
# 4. Make a script that filters genes from a NASA OSD dataset about mice and make a call that retrieves information to the user
# Realistic, Download a heart disease dataset using the python skills listed to list summary of the trends to predict 

# 1. Git is a version control tool, where GitHub is a website that holds the repositories 
# 2. Terminal is part of your computer system that you can type command lines in. The command line is the part where you type it
# 3. Local is your files stored in your computer, remote is where it's online for everyone
# 4. Version colntrol tracks changes to files or code
# 5 staging area is where you can complete modifications before commit to repo history 
# 6. Git add, moves the files into staging area for a commit
# 7. Git commit  saves everything in the stagin area to local pro
# 8. Push is whee you upload the local commits to a remote repo where everyone can see
# 9. Status tracks the changes in files 
# 10 pull- keeps the recent changes from repo to your computer
# 11, pwd- tells you the path of the folder you are in regarding terminal 
# 12. Ls- lists everything inside your directory like files 
# 13. Cd- change directory
# 14. Nano text editor 
# 15. Touch0 creates new files
# 16. Mv- move a file somewhere 
# 17, rm- remove 
# 19. Cat = shows the contents of your folders 
# ---------3.2-----------
# 1. Pwd
# 2.ls
# 3. cd python_decal/brianna_repo, , then git pull
# 4. mv /python_decal/brianna_repo/homework.py ~/python_decal/judy_decal/homework
# 5. Use cd
# 6. Use cat homework,py
# 7. Stage with git add hw.py, then save with git commit -m "updated", push to GitHub,
# 8.comands: git pull, then git push. The error means that Judy didnt pull latest changes. She needed to always git pull before pushing so its up to date.
# 9. I think use cd recents/ 

# 4.1
# My function will look like this 

# def check_data_type(value):
# 	if type(value). == int
# 		return 'int'
# 	elif type(value). == float
# 		return 'float'
# -------4.2----------
def enenOrOdd (n):
	if n / 2 ==int(n/2):
		return 'Even'
	else: 
		return 'odd'
print(enenOrOdd(4))
# ------5---------
# Takes list of int, returns sum using loop
# def sumWithLoop(numbers):
# Total =0
# For n in numbers:
# Total = total +n
# Return total
# -----6-------
# 6.1
# def duplicateList(lst):
# For iten in lst:
# new_list=append(item)
# Return new_list

# 6,2
# You need a : after the first line

# ----7--

# #favorite function is   

def check_data_type(value):
    if type(value) == int:
        return "The data type is: int"
    elif type(value) == float:
        return "The data type is: float"
    else:
          return "The data type is: unknown"
print(check_data_type(3.))
