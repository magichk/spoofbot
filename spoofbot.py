#!/usr/bin/env python
# -*- coding: ISO-8859-15 -*-
import sys
import urllib
import urllib.request
import urllib.error
#import urllib2 --> pytthon 2.X


def help():
    print (" ____                     __ ____        _   ")
    print ("/ ___| _ __   ___   ___  / _| __ )  ___ | |_ ")
    print ("\___ \| '_ \ / _ \ / _ \| |_|  _ \ / _ \| __|")
    print (" ___) | |_) | (_) | (_) |  _| |_) | (_) | |_ ")
    print ("|____/| .__/ \___/ \___/|_| |____/ \___/ \__|")
    print ("      |_|                                    ")

    print ("SpoofBot v0.1 Beta")
    print ("This tool simulates a bot of searchengines and tryies to read bots.txt")
    print (" ")
    print ("Usage: python.py spoofbot.py -u http://<url> -b <bot type>")
    print ("Example: python.py spoofbot.py -u http://github.com/robots.txt -b Google")
    print (" ")
    print ("Types of bots:")
    print ("Google")
    print ("Bing")
    print (" ")


def request_site(url, bot):
    
    if (bot == "Google"):
        #Python 2.X
        #req = urllib2.Request(url + '/robots.txt')
        #req.add_header('User-Agent', 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
        #codigo = urllib2.urlopen(req)

        #Python 3.X
        url = url + "/robots.txt"
        hdr = { 'User-Agent' : 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)' }

        req = urllib.request.Request(url, headers=hdr)
        codigo = urllib.request.urlopen(req)
        
        for line in codigo:
            print (line)

    elif (bot == "Bing"):
        print ("Buscar con bing..")

if (len(sys.argv) != 5):
    help()
else:
    request_site(sys.argv[2], sys.argv[4])
