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
import argparse


class SolidFiles(object):
    def __init__(self):
        parser = argparse.ArgumentParser(description='SolidFiles downloader downloads files from solidfiles.com')

        parser.add_argument('-b', '--batch', nargs=1, help='Indicates a file name in current directory.')

        args = parser.parse_args()

        if args.batch:
            file_name = args.batch[0]
            try:
                with open(file_name, "r") as link_file:
                    downloadUrl = link_file.readline().strip()
<<<<<<< HEAD
                lines = [line.rstrip('\n') for line in open(file_name)]

                for link in lines:
                    downloadUrl, nodeName, filetype = self.webPageDownloader(link)
=======

                    downloadUrl, nodeName, filetype = self.webPageDownloader(downloadUrl)
>>>>>>> 86a536ac30eaa42828f3d58cb6f74e249f5cad1d
                    self.File_Downloader(downloadUrl, str(nodeName).replace(".001", ""))
            except Exception as ex:
                print(ex)
                print("An error occurred. Check the file is present in the same directory.")
                pass
        if not args.batch:
            try:
                downloadUrl = str(raw_input("Enter the url : ")).strip()  # <-- Python 2.7
            except:
                downloadUrl = str(input("Enter the url : ")).strip()  # <-- Python 3

            downloadUrl, nodeName, filetype = self.webPageDownloader(downloadUrl)
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

            # splashUrl = jsonString["streamUrl"]
            downloadUrl = jsonString["downloadUrl"]
            # ticket = jsonString["ticket"]
            nodeName = jsonString["nodeName"]
            filetype = jsonString["filetype"]
            # shareUrl = jsonString["shareUrl"]
            # nodeId = jsonString["nodeId"]
            # subtitles = jsonString["subtitles"]
            # streamUrl = jsonString["streamUrl"]

            return (downloadUrl, nodeName, filetype)

    def File_Downloader(self, ddl, fileName):
        dlr = requests.get(ddl, stream=True)  # Downloading the content using python.
        with open(fileName, "wb") as handle:
            for data in tqdm(dlr.iter_content(chunk_size=1024)):  # Added chunk size to speed up the downloads
                handle.write(data)
        print("Download has been completed.")  # Viola


if __name__ == '__main__':
    SolidFiles()
