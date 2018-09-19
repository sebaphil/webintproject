import gzip
import json
import urllib

def retrieve_single_question():
    url = 'https://api.stackexchange.com/2.2/questions?tagged=postgres&filter=withbody&page=1&pagesize=1&order=asc&sort=creation&site=stackoverflow'
    filename, _ = urllib.urlretrieve(url)
    return json.loads(gzip.GzipFile(filename).read())
