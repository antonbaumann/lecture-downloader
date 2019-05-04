### installation:
1. install `ffmpeg` if not already installed
2. clone repository: `git clone https://github.com/antonbaumann/lecture-downloader.git`
3. `cd lecture-downloader`
4. run `pip3 install -r requirements.txt`

### usage:
```bash
python3 lecture_downloader.py [-h] -u URL -o OUT_FILE

Download lectures

optional arguments:
  -h, --help   show this help message and exit
  -u URL       stream playlist url
  -o OUT_FILE  output file name
```
