from nose.tools import assert_equal
from parse import URLParsed

class TestLinkParser(object):

    def test_parse_domain(self):
        """
        Tests: URLParsed()

        """
        assert_equal(URLParsed('www.gartner.com/blog/pdfindex.jsp?g=connectloud_cmp_report').original, 'www.gartner.com/blog/pdfindex.jsp?g=connectloud_cmp_report')
        assert_equal(URLParsed('www.gartner.com/blog/pdfindex.jsp?g=connectloud_cmp_report').subdomain, 'www')
        assert_equal(URLParsed('www.gartner.com/blog/pdfindex.jsp?g=connectloud_cmp_report').domain, 'www.gartner.com')
        assert_equal(URLParsed('www.gartner.com/blog/pdfindex.jsp?g=connectloud_cmp_report').tld, 'gartner.com')
        assert_equal(URLParsed('www.gartner.com/blog/pdfindex.jsp?g=connectloud_cmp_report').path, '/blog/pdfindex.jsp?g=connectloud_cmp_report')
        assert_equal(URLParsed('www.gartner.com/blog/pdfindex.jsp?g=connectloud_cmp_report').local, False)
        assert_equal(URLParsed('www.gartner.com/blog/pdfindex.jsp?g=connectloud_cmp_report').query_string, 'g=connectloud_cmp_report')
        assert_equal(URLParsed('www.gartner.com/blog/pdfindex.jsp?g=connectloud_cmp_report').path_list, ['blog','pdfindex.jsp'])

        assert_equal(URLParsed('www.gartner.com/pdfindex.jsp?g=connectloud_cmp_report').original, 'www.gartner.com/pdfindex.jsp?g=connectloud_cmp_report')
        assert_equal(URLParsed('www.gartner.com/pdfindex.jsp?g=connectloud_cmp_report').subdomain, 'www')
        assert_equal(URLParsed('www.gartner.com/pdfindex.jsp?g=connectloud_cmp_report').domain, 'www.gartner.com')
        assert_equal(URLParsed('www.gartner.com/pdfindex.jsp?g=connectloud_cmp_report').tld, 'gartner.com')
        assert_equal(URLParsed('www.gartner.com/pdfindex.jsp?g=connectloud_cmp_report').path, '/pdfindex.jsp?g=connectloud_cmp_report')
        assert_equal(URLParsed('www.gartner.com/pdfindex.jsp?g=connectloud_cmp_report').local, False)
        assert_equal(URLParsed('www.gartner.com/pdfindex.jsp?g=connectloud_cmp_report').query_string, 'g=connectloud_cmp_report')
        assert_equal(URLParsed('www.gartner.com/pdfindex.jsp?g=connectloud_cmp_report').path_list, ['pdfindex.jsp'])

        assert_equal(URLParsed('http://www.twitter.com/knitcrate').original, 'http://www.twitter.com/knitcrate')
        assert_equal(URLParsed('http://www.twitter.com/knitcrate').subdomain, 'www')
        assert_equal(URLParsed('http://www.twitter.com/knitcrate').domain, 'www.twitter.com')
        assert_equal(URLParsed('http://www.twitter.com/knitcrate').tld, 'twitter.com')
        assert_equal(URLParsed('http://www.twitter.com/knitcrate').path, '/knitcrate')
        assert_equal(URLParsed('http://www.twitter.com/knitcrate').local, False)
        assert_equal(URLParsed('http://www.twitter.com/knitcrate').query_string, None)
        assert_equal(URLParsed('http://www.twitter.com/knitcrate').path_list, ['knitcrate'])

        assert_equal(URLParsed('www.twitter.com/knitcrate').original, 'www.twitter.com/knitcrate')
        assert_equal(URLParsed('www.twitter.com/knitcrate').subdomain, 'www')
        assert_equal(URLParsed('www.twitter.com/knitcrate').domain, 'www.twitter.com')
        assert_equal(URLParsed('www.twitter.com/knitcrate').tld, 'twitter.com')
        assert_equal(URLParsed('www.twitter.com/knitcrate').path, '/knitcrate')
        assert_equal(URLParsed('www.twitter.com/knitcrate').local, False)
        assert_equal(URLParsed('www.twitter.com/knitcrate').query_string, None)
        assert_equal(URLParsed('www.twitter.com/knitcrate').path_list, ['knitcrate'])

        assert_equal(URLParsed('www.twitter.com').original, 'www.twitter.com')
        assert_equal(URLParsed('www.twitter.com').subdomain, 'www')
        assert_equal(URLParsed('www.twitter.com').domain, 'www.twitter.com')
        assert_equal(URLParsed('www.twitter.com').tld, 'twitter.com')
        assert_equal(URLParsed('www.twitter.com').path, None)
        assert_equal(URLParsed('www.twitter.com').local, False)
        assert_equal(URLParsed('www.twitter.com').query_string, None)
        assert_equal(URLParsed('www.twitter.com').path_list, None)

        assert_equal(URLParsed('twitter.com').original, 'twitter.com')
        assert_equal(URLParsed('twitter.com').subdomain, None)
        assert_equal(URLParsed('twitter.com').domain, 'twitter.com')
        assert_equal(URLParsed('twitter.com').tld, 'twitter.com')
        assert_equal(URLParsed('twitter.com').path, None)
        assert_equal(URLParsed('twitter.com').local, False)
        assert_equal(URLParsed('twitter.com').query_string, None)
        assert_equal(URLParsed('twitter.com').path_list, None)

        assert_equal(URLParsed('twitter.com/knitcrate').original, 'twitter.com/knitcrate')
        assert_equal(URLParsed('twitter.com/knitcrate').subdomain, None)
        assert_equal(URLParsed('twitter.com/knitcrate').domain, 'twitter.com')
        assert_equal(URLParsed('twitter.com/knitcrate').tld, 'twitter.com')
        assert_equal(URLParsed('twitter.com/knitcrate').path, '/knitcrate')
        assert_equal(URLParsed('twitter.com/knitcrate').local, False)
        assert_equal(URLParsed('twitter.com/knitcrate').query_string, None)
        assert_equal(URLParsed('twitter.com/knitcrate').path_list, ['knitcrate'])

        assert_equal(URLParsed('brochure.html').original, 'brochure.html')
        assert_equal(URLParsed('brochure.html').subdomain, None)
        assert_equal(URLParsed('brochure.html').domain, None)
        assert_equal(URLParsed('brochure.html').tld, None)
        assert_equal(URLParsed('brochure.html').path, '/brochure.html')
        assert_equal(URLParsed('brochure.html').local, True)
        assert_equal(URLParsed('brochure.html').query_string, None)
        assert_equal(URLParsed('brochure.html').path_list, ['brochure.html'])

        assert_equal(URLParsed('knitcrate/brochure.html').original, 'knitcrate/brochure.html')
        assert_equal(URLParsed('knitcrate/brochure.html').subdomain, None)
        assert_equal(URLParsed('knitcrate/brochure.html').domain, None)
        assert_equal(URLParsed('knitcrate/brochure.html').tld, None)
        assert_equal(URLParsed('knitcrate/brochure.html').path, '/knitcrate/brochure.html')
        assert_equal(URLParsed('knitcrate/brochure.html').local, True)
        assert_equal(URLParsed('knitcrate/brochure.html').query_string, None)
        assert_equal(URLParsed('knitcrate/brochure.html').path_list, ['knitcrate','brochure.html'])

        assert_equal(URLParsed('/knitcrate').original, '/knitcrate')
        assert_equal(URLParsed('/knitcrate').domain, None)
        assert_equal(URLParsed('/knitcrate').subdomain, None)
        assert_equal(URLParsed('/knitcrate').tld, None)
        assert_equal(URLParsed('/knitcrate').path, '/knitcrate')
        assert_equal(URLParsed('/knitcrate').local, True)
        assert_equal(URLParsed('/knitcrate').query_string, None)
        assert_equal(URLParsed('/knitcrate').path_list, ['knitcrate'])

        assert_equal(URLParsed('knitcrate').original, 'knitcrate')
        assert_equal(URLParsed('knitcrate').domain, None)
        assert_equal(URLParsed('knitcrate').subdomain, None)
        assert_equal(URLParsed('knitcrate').tld, None)
        assert_equal(URLParsed('knitcrate').path, '/knitcrate') # appends /
        assert_equal(URLParsed('knitcrate').local, True)
        assert_equal(URLParsed('knitcrate').query_string, None)
        assert_equal(URLParsed('knitcrate').path_list, ['knitcrate'])

        assert_equal(URLParsed('javascript:void(0);').original, 'javascript:void(0);')
        assert_equal(URLParsed('javascript:void(0);').url, None)
        assert_equal(URLParsed('javascript:void(0);').domain, None)
        assert_equal(URLParsed('javascript:void(0);').subdomain, None)
        assert_equal(URLParsed('javascript:void(0);').tld, None)
        assert_equal(URLParsed('javascript:void(0);').path, None)
        assert_equal(URLParsed('javascript:void(0);').local, None)
        assert_equal(URLParsed('javascript:void(0);').query_string, None)
        assert_equal(URLParsed('javascript:void(0);').path_list, None)

        assert_equal(URLParsed('  ').original, '  ')
        assert_equal(URLParsed('  ').url, None)
        assert_equal(URLParsed('  ').domain, None)
        assert_equal(URLParsed('  ').subdomain, None)
        assert_equal(URLParsed('  ').tld, None)
        assert_equal(URLParsed('  ').path, None)
        assert_equal(URLParsed('  ').local, None)
        assert_equal(URLParsed('  ').query_string, None)
        assert_equal(URLParsed('  ').path_list, None)
