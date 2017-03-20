# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > This cheat sheet summarizes the codeacademy.org lesson on command line  
1. `pwd` prints working directory  
2. `cd` changes directory  
3. `mkdir` makes new directory  
4. `rm` removes files (add -r to remove folders)  
5. `ls` lists files in current directory (add -a to see hidden files)  
6. `cp` copies files and directories  
7. `touch` creates an empty new file; specify filename  
8. `mv` moves a file from one location to another, or renames file  
9. `echo` accepts a standard input and returns a standard output (e.g. `echo "Hello" > outfile.txt` to create or overwrite, `echo "Hello" >> outfile.txt` to append file)  
10. `cat` displays the contents of a text file  
11. `|` pipes: use with other commands to direct ouput to another command  
12. `grep` global regular expression print; search for a text pattern and output matches (-i to make case insensitive)  
13. `sed` stream editor; accepts standard input and modifies it based on an expression, then displays output (useful for replacing text patterns en masse; use /g for global replacement)  
14. Others reviewed: uniq, sort, source, alias, env  
15. Environment settings: edit ~/.bash_profile to load new commands when a session starts... eg. `alias ll ls -al`, `export USER='Jane Doe'`  
16. Environment Variables reviewed: USER, HOME, PS1, PATH

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  lists files and directories in cwd (non-hidden)  
`ls -a`  lists all files and directories in cwd (including hidden)  
`ls -l`  lists contents in long format  
`ls -lh`  lists contents in long format, with human readable filesizes  
`ls -lah` lists all contents in long format, with human readable filesizes  
`ls -t`  order files and directories by the time they were modified  
`ls -Glp`  lists files in long format, appends indicator (such as / for folders), inhibits display of group information  

> > See above

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> >`ls -1` displays each entry on a line  
`ls -R` displays subdirectories as well  
`ls -m` display files as comma separated list  
`ls -u` display by file access time  
`ls -o` long format but exclude group name  

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs accepts a standard input and executes commands on it.  For example, here I used it to copy all the files containing the word "file" into a subdirectory:  
`mkdir copytest`  
`grep -il "file" *.md | xargs -I{} cp {} ./copytest`
