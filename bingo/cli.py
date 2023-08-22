import os
import platform
import random as rand
import requests
import typer
import ctypes
# import json

# from datetime import datetime
# from typing import Optional

from bingo import __app_name__, __version__

# ANSI colors
class Colors(object):
    def __init__(self) -> None:
        self.HEADER = '\033[95m'
        self.OKBLUE = '\033[94m'
        self.OKCYAN = '\033[96m'
        self.OKGREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'

class Market(object):
    def __init__(self) -> None:
        self.US = "en-US",
        self.CN = "zh-CN",
        self.JP = "ja-JP",
        self.IN = "en-IN",
        self.BR = "pt-BR",
        self.FR = "fr-FR",
        self.DE = "de-DE",
        self.CA = "en-CA",
        self.GB = "en-GB",
        self.IT = "it-IT",
        self.ES = "es-ES",


#"en-US": English (United States)
#"zh-CN": Chinese (China)
#"ja-JP": Japanese (Japan)
#"en-IN": English (India)
#"pt-BR": Portuguese (Brazil)
#"fr-FR": French (France)
#"de-DE": German (Germany)
#"en-CA": English (Canada)
#"en-GB": English (United Kingdom)
#"it-IT": Italian (Italy)
#"es-ES": Spanish (Spain)
#"fr-CA": French (Canada)

colors = Colors()
market = Market()

app = typer.Typer()

BING_API_URL = "https://www.bing.com/HPImageArchive.aspx"
BIND_CDN_URL = "https://cn.bing.com"

def download_wallpaper(day: int = 0,
                       path: str = os.path.expanduser("~/Desktop"),
                       uhd: int = 1, # by default UHD
                       market: str = "en-US",
                       uhdwidth: int = 3840, #4k
                       uhdheight: int = 2160
                       ):
    params = {
        "format": "js",
        "idx": day,
        "n": 1,
        "mkt": market,
        "uhd": uhd,
        "uhdwidth": uhdwidth,
        "uhdheight": uhdheight
    }

    
    response = requests.get(BING_API_URL, params=params)
    data = response.json()

    if "images" in data and data["images"]:
        image_data = data["images"][0]
        image_url = "https://www.bing.com" + image_data["url"]
        start_date = image_data["startdate"]
        
        image_title = image_data["title"]
        image_copyright = image_data["copyright"]

        image_response = requests.get(image_url)
        image_extension = os.path.splitext(image_url)[1].split('&')[0]
        image_filename = f"{start_date}-{image_title}{image_extension}"
        image_path = os.path.join(path, image_filename)
        
        with open(image_path, "wb") as image_file:
            image_file.write(image_response.content)
        
        print("{}{}OK: Wallpaper downloaded and saved as \"{}\"!{}\nTitle: {} \nCopyright: {}".format(
            colors.OKGREEN,
            colors.BOLD,
            image_path,
            colors.ENDC,
            image_title,
            image_copyright
        ))
        return image_path
        
    else:
        print("{}{}ERROR: Something went wrong downloading the wallaper!{}".format(
            colors.FAIL,
            colors.BOLD,
            colors.ENDC
        ))
    



def set_wallpaper_windows(image_path):
    SPI_SETDESKWALLPAPER = 20
    try:
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
        print("{}{}OK: Wallpaper set!".format(
            colors.OKGREEN,
            colors.BOLD,
            colors.ENDC
        ))
        exit(0)
    except:
        print("{}{}ERROR: Something went wrong setting wallpaper!{}".format(
            colors.FAIL,
            colors.BOLD,
            colors.ENDC
        ))
        exit(1)

def set_wallpaper_linux(image_path):
    desktop_env = os.environ.get("XDG_CURRENT_DESKTOP")
    
    if desktop_env and "GNOME" in desktop_env:
        try:
            os.system(f"gsettings set org.gnome.desktop.background picture-uri file://{image_path}")
            print("{}{}OK: Wallpaper set on gnome environment!".format(
            colors.OKGREEN,
            colors.BOLD,
            colors.ENDC
            ))
            exit(0)
        except:
            print("{}{}ERROR: Something went wrong setting wallpaper!{}".format(
                colors.FAIL,
                colors.BOLD,
                colors.ENDC
            ))
            exit(1)
            
    elif os.path.isfile("/usr/bin/feh"):
        os.system(f"feh --bg-fill {image_path}")
    elif os.path.isfile("/usr/bin/nitrogen"):
        os.system(f"nitrogen --set-auto {image_path}")
    else:
        print("{}{}ERROR: Unsupported desktop environment or wallpaper setting tool!{]}".format(
            colors.FAIL,
            colors.BOLD,
            colors.ENDC
        ))
        exit(1)


@app.command()
def main(day: int = typer.Option(0, help="Day ranging from 0-6. 0 is today, 6 is a week ago."),
        today: bool = typer.Option(False, help="Download todays's wallpaper."),
        yesterday: bool = typer.Option(False, help="Download yesterday's wallpaper"),
        random: bool = typer.Option(False, help="Download a random wallpaper."),
        uhd: bool = typer.Option(True, help="Download images in ulta HD (4k) resolutions"),
        country: str = typer.Option("US", help="Bing service country"),
        path: str = typer.Option(os.path.expanduser("~/Desktop"), help="Path to save the wallpaper"),
        set: bool = typer.Option(False, help="Set the image as wallpaper."),
        version: bool = typer.Option(False, help="Show app version and exit.")
        ):
    """
    Download Bing wallpapers and save them as images on the user's desktop folder by default.
    """
    _day = day
    _path = path
    _uhd = uhd
    _market = country

    if version:
        # Show version and exit

        print("{}{}{}! ({}): A bing wallpaper downloader utility.{}\nHomepage: https://github.com/deep5050/bingo\n{}{}Use of the images are restricted to wallpapers only.{}".format(
            colors.OKBLUE,
            colors.BOLD,
            __app_name__,
            __version__,
            colors.ENDC,
            colors.WARNING,
            colors.BOLD,
            colors.ENDC
        ))
        exit(0)

    if not os.path.isdir(path):
        print("{}{}ERROR: Directory '{}' does not exist!{}".format(
            colors.BOLD,
            colors.FAIL,
            path,
            colors.ENDC
        ))
        exit(1)
    

    if today:
        _day = 0
    
    if yesterday:
        _day = 1
    
    if random:
        _day = rand.randint(0,6)
    
    if uhd == False:
        _uhd = 0
    else:
        _uhd = 1
    

    if _day > 6:
        print("{}{}ERROR: You can download wallpaper not older than a week!{}".format(
            colors.BOLD,
            colors.FAIL,
            colors.ENDC
        ))
        exit(1)

    if market:

        _market = getattr(market, _market, None)
        # print(_market)
        if _market == None:
            print("{}{}ERROR: country not found! see documentation {}".format(
                colors.FAIL,
                colors.BOLD,
                colors.ENDC
            ))
            exit(1)

    image_path = download_wallpaper(day=_day,
                       path=_path,
                       uhd=_uhd,
                       market=_market
                       )
    if set:
        # Set wallpaper based on the platform
        if platform.system() == "Windows":
            set_wallpaper_windows(image_path)
        elif platform.system() == "Linux":
            set_wallpaper_linux(image_path)
        else:
            print("{}{}Unsupported operating system!{}".format(
                colors.FAIL,
                colors.BOLD,
                colors.ENDC
            ))
            exit(1)

if __name__ == "__main__":
    app()