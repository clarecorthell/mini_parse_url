import re
from tld import get_tld

MAX_URL_LEN = 1000

class URLParsed(object):
    """
    Returns parsed URL with attributes:
    
    subdomain
    suffix
    tld
    domain
    path
    local (bool)

    """
    def get_subdomain(self):
        try:
            sub = get_tld(self.url, as_object=True).subdomain
            if sub and len(sub):
                return sub
            return None
        except:
            return None

    def get_suffix(self):
        try:
            suffix = get_tld(self.url, as_object=True).suffix
            if suffix and len(suffix):
                return suffix
        except:
            return None

    def parse_tld(self):
        try:
            parsed = get_tld(self.url, as_object=True)
            if parsed.suffix and len(parsed.suffix):
                return parsed.tld
            return None
        except:
            return None

    def get_domain(self):
        if self.subdomain and len(self.subdomain):
            return self.subdomain + '.' + self.tld
        elif self.tld and len(self.tld):
            return self.tld
        return None

    def get_path(self):
        """
        Appends local '/' where doesn't exist

        """
        try:
            path = self.original.rsplit(self.domain,1)[1]
        except AttributeError:
            return None
        except:
            path = self.original.rsplit(self.domain,1)[0]

        if len(path):
            if path[:1] != '/':
                return '/' + path
            return path
        return None

    def get_local(self):
        return False if self.domain else True

    def sanitize_url(self, url=None):
        """
        Remove non-link '/' edge case urls
        add 'http://' for tld parsing trickery

        - javascript
        - urls longer than 1000 chars

        """
        if len(url) > MAX_URL_LEN or url[:10] == 'javascript':
            self.original = None # overwrite the egregious cases
            return None
        elif url[:4] != 'http':
            return 'http://' + url
        return url

    def __init__(self, url):
        self.original = url # store original url but process sanitized url
        self.url = self.sanitize_url(url)

        if not self.url or len(self.url) > 3:
            self.subdomain = None
            self.suffix = None
            self.tld = None
            self.domain = None
            self.path = None
            self.local = None
        else:
            self.subdomain = self.get_subdomain()
            self.suffix = self.get_suffix()
            self.tld = self.parse_tld()
            self.domain = self.get_domain()
            self.path = self.get_path()
            self.local = self.get_local()
