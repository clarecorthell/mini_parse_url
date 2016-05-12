# mini_parse_url
parse_url utility

### Dependencies

`pip install tld`

### Import

`from mini_parse_url.parse import URLParsed`

### Use: Eat normal links, Get structure back.
```
ps = URLParsed('www.knitcrate.com/brochure.html')

ps.subdomain
>>> 'www'

ps.domain
>>> 'www.knitcrate.com'

ps.tld
>>> 'knitcrate.com'

ps.path
>>> '/knitcrate/brochure.html'

ps.local
>>> False

ps.original
>>> 'www.knitcrate.com/brochure.html'
```
And relative links, too:
```
ps = URLParsed('brochure.html')

ps.subdomain
ps.domain
ps.tld
>>> None

ps.path
>>> '/brochure.html'

ps.local
>>> True

ps.original
>>> 'brochure.html'
```

Basically, if you're consuming a webpage and structuring the `href`, this makes it easier to reconstruct full urls. Enjoy!

### Tests

Run `nosetests` at root of the repo.
