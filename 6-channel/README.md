## Zip

Hint is zip, so i tried to find url+filename+".zip" <br/>
We get a zipfile with tons of txt files inside it along with readme.txt

It says it starts at 90052 and I opened 950052.txt. We can found next file to be opened <br/>
I made a script to opened all things files like our prev solution linkedlist <br/>
The final file says collect comments

I had no idea about that and so confused about it <br/>
Then I found out that every zipfile has comment for each object side it. <br/>
We can get comment by using `archive.getinfo("firstobj.1").comment`

I appended collected comment to a list. <br/>
When I view at the list, I found overlapping characters and also `\n`s <br/>
I assume this as a string so print single character together to form a big string

I got next step finally ... yay

next lvl: hockey

## Reference Links
- https://stackoverflow.com/questions/51792923/python-reading-a-zip-file-comment
