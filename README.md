# Rename filenames of movies etc.

Simple script to sort all your files using guessit lib (https://github.com/guessit-io/guessit)
![Example](http://i.imgur.com/YvnLA8G.gif)
<i>No movie was pirated, they are only names of some popular torrents files</i>

### Installation
`pip install guessit` <br />
`python rename.py`

### Usage
Just write path to your movie directory. Script will change also subdirectories
 with files.

### Output
New filename will contain title + season + episode (if they exist) + container in files (not in directiories) 

#### Example
`Dark.Net.S01E02.HDTV.x264-FUM[ettv]` <br />
to <br />
`Dark Net - season 1 episode 2`
