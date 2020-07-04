# club-dev-ultimate-

This repo is private. That doesn't mean you can't clone it. It just won't be visible to you with any other github account.
So use the music club github account to clone the repo and commit changes.

The database has been changed from local sqlite3 to online postgresql on elephantsql which is why the queries maybe a bit slow. The connections have been made already. 
Although if you wish to change it back to sqlite3 for testing purposes you can just un-comment the lines in settings.py. Don't forget to revert it back before commiting.

Song recommendation functionality has been implemented already. All others are not.

# Intructions on Development
1) The original club-dev has become obsolete. So clone this repo straight away before doing any further development.
2) If you have done work on that just copy paste the new files that you made. Don't modify any of these files blindly.
3) There are some naming patterns. Eg: Django apps are to be named with 'app' as their prefix, etc.
4) Don't push directly to the master branch. Make a new branch. I'll analyse the code then push it myself.
5) As the data extraction from database maybe a bit slow so try to modify the code. (Eg: Calling an API beforehand and modifing the data as per user needs)
