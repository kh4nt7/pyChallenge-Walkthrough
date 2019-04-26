## Hint

> Follow the chain

## Suspicious 
> `<a href="linkedlist.php?nothing=12345"><img src="chainsaw.jpg" border="0"/></a>`

When we look at the source-code, we found

> `<!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never <br/>
  end. 400 times is more than enough. -->`
  
I tried to send a get request with parameter nothing=400, this response happens
> and the next nothing is 57589

Mom, I think I just found the chain LOL
