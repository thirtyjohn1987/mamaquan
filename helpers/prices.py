#coding:utf-8
from helpers.crawls import getUrl
import urllib,json,re
from helpers.utils import getMarketFromUrl
from b2c import factory,Item


def getRuyiHtml(url):
    ruyi_host = "http://ruyi.etao.com/ext/productLinkSearch?"
    params = urllib.urlencode({"link":url})
    resp = getUrl(ruyi_host+params)
    html = resp.read() if resp else None
    return html

comp_price = re.compile(u"([0-9.]+)")
def getCpdata(html):
    cplist = list()
    data = json.loads(html)
    if not data.has_key("Items"):
        return None
    for d in data["Items"]:
        item = Item()
        item.market = getMarketFromUrl(d["DetailPageURL"])
        m = comp_price.search(d["Price"])
        item.price = float(m.group(1)) if m else None
        item.currency = 1 if d["Price"].find(u"￥") > -1 else None
        item.url = d["DetailPageURL"]
        cplist.append(item)
    return cplist


def getRuyiSearch(txt):
    url = "http://ruyi.taobao.com/ext/etaoSearch?q="+urllib.quote(txt.encode("utf8"))+"&application=&pid=rf002&page=1"
    html = getUrl(url).read()
    data = json.loads(html)
    cplist = list()
    if not data.has_key("Items"):
        return None
    for d in data["Items"]:
        item = Item()
        item.market = getMarketFromUrl(d["DetailPageURL"])
        m = comp_price.search(d["Price"])
        item.price = float(m.group(1)) if m else None
        item.currency = 1 if d["Price"].find(u"￥") > -1 else None
        item.url = d["DetailPageURL"]
        cplist.append(item)

    return cplist


def getCpdataFromSearch(name,marketlist):
    cplist = list()
    print marketlist
    for market in marketlist:
        print market + " searching...."
        b2c_list = factory(market)
        html = b2c_list.getSearchHtml(name)
        b2c_list.listhtml = html
        if b2c_list.noRightResult():
            print "no result"
            continue
        datalist = b2c_list.getlist()
        print len(datalist)

        if len(datalist)>0:
            d = datalist[0]
            b2c_item = factory(market)
            b2c_item.itemid = d.itemid
            if not d.price:
                d.price = b2c_item.getprize()
            d.currency = 1
            d.url = b2c_list.getSearchUrl(name)
            cplist.append(d)

    return cplist



