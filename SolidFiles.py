#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''


Script Info :

Author : Xonshiz
Github : https://github.com/Xonshiz
Website : http://www.xonshiz.psychoticelites.com
Email ID: xonshiz@psychoticelites.com

'''

import requests
import re
import json
from tqdm import tqdm
from sys import exit


class SolidFiles(object):
    def __init__(self):

        try:
            downloadUrl = str(raw_input("Enter the url : ")).strip()  # <-- Python 2.7
        except :
            downloadUrl = str(input("Enter the url : ")).strip()  # <-- Python 3

        streamUrl, splashUrl, downloadUrl, embedUrl, ticket, nodeId, nodeName, filetype, shareUrl, subtitles = self.webPageDownloader(downloadUrl)
        self.File_Downloader(downloadUrl, str(nodeName).replace(".001", ""))


    def webPageDownloader(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'
        }
        pageSource = requests.get(url, headers = headers).text

        if 'Page not found | Solidfiles' in pageSource: # What do when 404? THIS!
            print("Seems like the file is not present.")
            print("Check the URL again manually please.")

            exit(0)

        else:
            mainOptions = str(re.search(r'viewerOptions\'\,\ (.*?)\)\;', pageSource).group(1))

            jsonString = json.loads(mainOptions, encoding="utf-8")

            splashUrl = jsonString["streamUrl"]
            downloadUrl = jsonString["downloadUrl"]
            embedUrl = jsonString["embedUrl"]
            ticket = jsonString["ticket"]
            nodeName = jsonString["nodeName"]
            filetype = jsonString["filetype"]
            shareUrl = jsonString["shareUrl"]
            nodeId = jsonString["nodeId"]
            subtitles = jsonString["subtitles"]
            streamUrl = jsonString["streamUrl"]

            return (
            streamUrl, splashUrl, downloadUrl, embedUrl, ticket, nodeId, nodeName, filetype, shareUrl, subtitles)

    def File_Downloader(self, ddl, fileName):
        dlr = requests.get(ddl, stream=True)  # Downloading the content using python.
        with open(fileName, "wb") as handle:
            for data in tqdm(dlr.iter_content(chunk_size=1024)):  # Added chunk size to speed up the downloads
                handle.write(data)
        print("Download has been completed.")  # Viola


if __name__ == '__main__':
    SolidFiles()