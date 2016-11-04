#! /usr/bin/env python
# -*- coding:utf-8 -*-

import time
import urllib2


class Crawler :

    prev_fetch_time = 0
    interval = 60

    @classmethod
    def fetch (cls, url) :
        try :
            sleep_time = cls.interval - (time.time() - cls.prev_fetch_time)
            if sleep_time > 0 :
                time.sleep(sleep_time)
            cls.prev_fetch_time = time.time()
            return urllib2.urlopen(url).read()
        except Exception as e :
            print 'Error@Crawler.fetch() :', e.message
            return ''
