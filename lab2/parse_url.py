#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


class URLParser(object):

    def __init__(self):
        self.text = ''  #вставьте текст
        self.links = URLParser.search_for_URL(self.text)

    def search_for_URL(text):
        links = re.findall(r'(?:https?://)?(?:www\.)?[\w\-\._]+\.[a-z]+' +
                           '[\w_\-/]*(?:\.[a-z]+)?', text)
        return links

a = URLParser()
