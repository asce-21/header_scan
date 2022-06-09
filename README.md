# header_scan
Learning Python automation from  [Hacking Simplified](https://www.youtube.com/c/HackingSimplifiedAS) video.

This script is the result of steps introduced in the video from the [Python automation series.](https://youtube.com/playlist?list=PLGJe0xGh7cH35HAafEp0JWAjxO0-7qrJi)

I will learn along and try to create the Web Scanner by following the steps from the series as progressed.

## First Step

Git clone the repo for linux or Download Zip file

`git clone https://github.com/asce-21/header_scan.git`

Run requirements.txt first to make sure all modules used in the script are installed

`pip install -r requirements.txt`

## Usage

`python header_scan.py https://www.example.com` 

It will check if following Basic Security Headers are present/missing in the application response:

X-Frame-Options

X-XSS-Protection

X-Content-Type-Options

Strict-Transport-Security

Content-Security-Policy
