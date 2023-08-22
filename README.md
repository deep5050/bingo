<p align=center>
<img src="logo.svg" align=center>
<h2 align=center> BINGO! </h2>
<p align=center> A Bing wallpaper downloader utility </p>

 <p align=center>
<img width="500px" alt="UPI" src="https://user-images.githubusercontent.com/27947066/235618869-8c9d9bce-096d-469e-8f61-c29cc01eacc3.png">
</p>

</p>

# Install
```bash
pip3 install bingo-cli --user
```

# Usage

```
deep@deep$ bingo --help

 Usage: bingo [OPTIONS]

 Download Bing wallpapers and save them as images on the user's desktop folder by default.

╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────╮
│ --day                                     INTEGER                        Day ranging from 0-6. 0 is     │
│                                                                          today, 6 is a week ago.        │
│                                                                          [default: 0]                   │
│ --today                 --no-today                                       Download todays's wallpaper.   │
│                                                                          [default: no-today]            │
│ --yesterday             --no-yesterday                                   Download yesterday's wallpaper │
│                                                                          [default: no-yesterday]        │
│ --random                --no-random                                      Download a random wallpaper.   │
│                                                                          [default: no-random]           │
│ --uhd                   --no-uhd                                         Download images in ulta HD     │
│                                                                          (4k) resolutions               │
│                                                                          [default: uhd]                 │
│ --country                                 TEXT                           Bing service country           │
│                                                                          [default: US]                  │
│ --path                                    TEXT                           Path to save the wallpaper     │
│                                                                          [default: /home/deep/Desktop]  │
│ --set                   --no-set                                         Set the image as wallpaper.    │
│                                                                          [default: no-set]              │
│ --version               --no-version                                     Show app version and exit.     │
│                                                                          [default: no-version]          │
│ --install-completion                      [bash|zsh|fish|powershell|pws  Install completion for the     │
│                                           h]                             specified shell.               │
│                                                                          [default: None]                │
│ --show-completion                         [bash|zsh|fish|powershell|pws  Show completion for the        │
│                                           h]                             specified shell, to copy it or │
│                                                                          customize the installation.    │
│                                                                          [default: None]                │
│ --help                                                                   Show this message and exit.    │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Supported countries

- US --> "en-US": English (United States)
- CN --> "zh-CN": Chinese (China)
- JP --> "ja-JP": Japanese (Japan)
- IN --> "en-IN": English (India)
- BR --> "pt-BR": Portuguese (Brazil)
- FR --> "fr-FR": French (France)
- DE --> "de-DE": German (Germany)
- CA --> "en-CA": English (Canada)
- GB --> "en-GB": English (United Kingdom)
- IT --> "it-IT": Italian (Italy)
- ES --> "es-ES": Spanish (Spain)
- CA --> "fr-CA": French (Canada)

Example:

```bash
deep@deep$ bingo --country IN --random
```