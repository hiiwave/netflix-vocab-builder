# Netflix Vobaulary Building Tutorial

Wanna learn vocabulary before/after watching a Netflix series? Then this guide is for you.


## Tutorial

- Prepare subtitle files
  - Install [Netflix - subtitle downloader](https://greasyfork.org/zh-TW/scripts/26654-netflix-subtitle-downloader) from Tithen-Firion following this [guide](https://greasyfork.org/zh-TW)
  - Download the subtitles via subtitle menu ![image](https://greasyfork.org/system/screenshots/screenshots/000/013/616/original/menu.png?1546605608)
  - Uncompress the zip file to get the subtitles in *.vtt format

- Convert subtitles to text file
  - Download `vtt_convert.py` from [here](https://raw.githubusercontent.com/hiiwave/netflix-vocab-builder/master/vtt_convert.py)
  - Open your terminal and run
    `python vtt_convert.py path/to/your/*en*.vtt -o converted.txt`
  - It then converts the full text into `converted.txt`

- Create vocabulary list via Vocabulary.com

  - Copy the full text from `converted.txt` into [vocabgrabber](https://www.vocabulary.com/lists/vocabgrabber)
  - That's it, enjoy your personal vocabulary list on your favorite series!

## Contributing

Pull requests and issues are more than welcome.


## Disclaimer

This tutorial is for knowledge sharing purpose only. Please be responsible to your actions following your local laws, and ask for written permissions from the content owner (i.e. Netflix) when necessary.


## [Changelog](./CHANGELOG.md)
