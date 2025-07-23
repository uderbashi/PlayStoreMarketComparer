# PlayStoreMarketComparer
A small script to compare the price of apps across differnt markets in the PlayStore. 

I wrote this becuse I wanted to buy an app on the PlayStore which on the website of the developer was stated to be cheaper than it was in my PlayStore. It was difficult comparing prices directly as I did not find something like SteamDB for the PlayStore. So I found the library called `google_play_scraper`, and it was easy from there.

## How to run it
First you need `google_play_scraper`. Install it with pip:
```bash
pip install google_play_scraper
```

Afterwards just run the script:
```bash
python Compare.py
```

It will ask you for a package name. You find this in the play store link. For example the link to GTA:SA is `https://play.google.com/store/apps/details?id=com.rockstargames.gtasa` and the part after `?id=` is the package name (in this case `com.rockstargames.gtasa`). Be careful as in links it could have other queries starting with `?`. Take only the package name which is usually in the form of `com.companyname.appname` it can be a bit shorter or longer, but that is the general form of the pakcage name.

After you give the program the package name it will try to get all the regions, and outut a CSV file with the results.
