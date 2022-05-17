---
Name: Diego Pajares Herrera
----
# List of Commands
## date
### Description
* Displays the date
### Syntax
* $ date
### Example
* Showing current time
* $ date

## uname
### Description
* Prints basic information about the OS
### Syntax
* $ uname
### Example
* Showing all available information of Linux
* $ uname -a 

## du
### Description
* Allows a user to gain disk information quickly
### Syntax
* $ du + directory
### Example
* Showing a summary of a directory's usage
* $ du -sh /home/DOcuments/

## free
### Description
* Displays amount of space available and used
### Syntax
* $ free + option
### Example
* Checking memory 
* $ free

## echo
### Description
* Displays line of text that are passed as an argument
### Syntax
* $ echo + option + string
### Example
* Displaying a text
* $ echo "Hello there"

## apt
### Description
* Updates, installs, removes related LInux distribution
### Syntax
* $ sudo apt + whatever do you want
### Example
* Updating my OS
* $ sudo apt update

## pwd
### Description
* Displaying current working directory
### Syntax
* $ pwd 
### Example
* You write pwd and you will see the directory you are in.
* pwd 
/home/adrian

## cd
### Description
* Changes the working directory
### Syntax
* $ cd + destination 
### Example
* Change from book to cvs file
*  cd ../cvs

## ls
### Description
* Listing the content of a given directory
### Syntax
* $ ls 
### Example
* Shows all files inside pictures
*  $ ls -a ~/Pictures

## tree
### Description
* Produces an indented listing of files
### Syntax
* $ tree + option + directory 
### Example
* Displaying the tree hierarchy of a directory
* *$ tree -a ./GFG

## man
### Description
* Shows the manual of a command
### Syntax
* $ man + command
### Example
* Showing the manual of pwd
* $ man pwd

## mkdir
### Description
* Creating a single directory or multiple directories
### Syntax
* $ mkdir + name of the directory
### Example
* Making a directory called Diego in the present directory 
*  $ mkdir Diego

## touch
### Description
* Creating files
### Syntax
* $ touch + name of file
### Example
* Create a file called file.txt in the present directory
* $ touch file.txt

## rm
### Description
* Removes files and directories with -r
### Syntax
* $ rm + name of the file
### Example
* Removing list.txt
* $ rm list.txt

## cp
### Description
* Copies files/directories from a source to a destination
### Syntax
* $ cp + files to copy + destination
### Example
* Copying files.txt in documents to pictures
* $ cp Downloads/files.txt Pictures/

## mv
### Description
* Moves and removes directories
### Syntax
* $ mv + source + destination
* $ mv + file/directory to rename + new name
### Example
* Moving list.txt in documents to pictures
* $ mv ../Documents/list.txt ../Pictures/

## stat
### Description
* Displays all information about a file except the file name and its content
### Syntax
* $ stat file name
### Example
* Showing the content of dracula.txt
* $ stat dracula.txt

## Wildcards (*,?,[])
### Description
* They are used to specify a file name for searches.
### Syntax
* $ ls + characters 
### Example
* Looking for files with the .txt
* $ ls *.txt

## Brace expansion
### Description
* Generate arbitrary strings to use with commands
### Syntax
* $ mkdir + directoryname / (nameofiles)
### Example
* Creating a directory with two .txt files
* $ mkdir documents/{file1,file2}

## cat
### Description
* Displaying the content of a file
### Syntax
* $ cat + option + file(s) to display
### Example
* To display a file in the current directory
* $ cat dracula.txt
  
## head
### Description
* Display the first 10 lines
### Syntax
* $ head + option + file
### Example
* Displaying the first lines of Dracula.txt
* $ head Dracula.txt

## tail
### Description
* Display the last 10 lines
### Syntax
* $ tail + option + file
### Example
* Displaying the last lines of dracula.txt
* $ tail dracula.txt

## cut
### Description
* Extracts a specific section of each line of a file
### Syntax
* $ cut + option + file
### Example
* Displaying all users in the seven field
* $ cut - d ':' -f7 /etc/passwd

## tr
### Description
* Translates or deletes characters from standard output
### Syntax
* Standard output | tr + option + set + set
### Example
* Translates dots to commas in dracula.txt
* $ cat dracula.txt | tr '.' ','

## paste
### Description
* Joins files horizontally in columns
### Syntax
* $ paste + option + files
### Example
* Merging two files 
* $ paste text.txt dracula.txt

## wc
### Description
* Prints the number of lines, characters, and bytes in a file
### Syntax
* $ wc + option + file
### Example
*  Displaying the number of lines of dracula.txt
*  $ wc -l dracula.txt

## grep
### Description
* Searches text in a given file
### Syntax
* $ grep + option + search criteria + file
### Example
* Searching the word love in dracula.txt
* $ grep -w 'love' dracula.txt

## output redirection
### Description
* Redirects output of commands to and from files.
### Saving the output of a command
* command output + > + file
### Example
* Save the output of a command to a file
* $ ls -lA ~ > all-files-in-home.txt

## vim or nano
### Description
* It is a text editor 
### Syntax
* To install it use: $ sudo apt install vim
### Example
* Creating a file and open vim at the same time
* $ vim dracula.txt

## tar
### Description
* Creates archives by combining files and directories into a single file
### Syntax
* $ tar + options + file.tar + files to archive 
### Example
* To extract a specific file
* $ tar -xf example.tar file3

## gzip, bzip2, or xz
### Description
* They are used for compression
### Syntax
* $ gzip file name
### Example
* Compressing a dracula.txt
* $ gzip dracula.txt

## chmod
### Description
* Changes permissions on files and directories 
### Syntax
* $ chmod permissions file/directory
### Example
* Changing the file permission to 654
* $ chmod 654 file1
