# Week Report 6

## Wildcards
* It is based on the use of letters and characters to specify a file name for searches.
* Them main wildcard is the asterisk(*), and it can go with any characters or can be alone. For example, if you want to search a all .docx files, we use ls *.docx.
* ? is a wildcard that is used to a match a character. Also, to see hidden files, we use the command ./.*. Therefore, if we want to search a hidden file with two characters, we use the command ./.??*.
* The [] wildcard is extensive, so a chart is necessary:

| Command| Meaning|
|--------|---------------------|
|ls f[aeiou]*| Match all file that have a vowel after f|
|ls f[!aeiou]*| Match all file that does not have a vowel after f|
|ls f[a-z]*| Match all file that have a range of letters after f|
|ls *[0-9]*| Match all file that have at least one number|
|ls *[!0-9]*| Match all file that does not have a number|
|ls [a-psc]*| Match all file that have a letter from a to p or start with letters s or c|
|ls [a-fp-z]*]| Match all file that have a letter from a to f or p to z|
|ls [0-9][0-9][0-9]$USER| Match all file that begin with any three combination of numbers|

## Brace expansion 
* This feature generates file inside another files. For example, to create a music with two file named jazz and rock, we use the command mkdir -p music/{jazz,rock}ds. In the same, to create files with extensions, we use touch website{1..5}.html