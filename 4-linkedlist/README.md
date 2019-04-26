## Hint

> Follow the chain

## Suspicious 
> `<a href="linkedlist.php?nothing=12345"><img src="chainsaw.jpg" border="0"/></a>`

When we look at the source-code, we found

> `<!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never <br/>
  end. 400 times is more than enough. -->`
  
I tried to send a get request with parameter nothing=400, this response happens
> and the next nothing is 57589

Mom, I think I just found the chain :) <br/>

My pseudocode is here 
* define original url
* define querystring(i.e, ?name=)
* assign first request (i.e, 400)
* add all of them and send request (url+querystring+request)
* loop :)

We extract the number in response using 
> `re.findall(r"[0-9]+", resp)`

## Reference Links
- https://www.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html
- https://regex101.com/
- https://www.twilio.com/blog/2016/12/http-requests-in-python-3.html


