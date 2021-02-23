# OBS Studio scripts
My scripts for the recording and streaming software [OBS
Studio](https://github.com/obsproject/obs-studio), for the rare times when I
fail to find a plugin or script that already does what I want on Linux.

## [auto-monitor-switch.py](./auto-monitor-switch.py)
### Why not just use Automatic/Advanced Scene Switchers?
I need my scene switching trigger to be the active window's position on the
screen, and I can't have that with these.

### Prerequisites
- You need Linux, OBS Studio, Python 3.6 or later, and xdotool.  Try this in a terminal:
```bash
obs --version
python --version
xdotool --version
```
Output such as `obs: command not found` means you need to install something.
Get `obs-studio`, `python`, and `xdotool` from your distribution's package
manager, or their respective websites:
- https://obsproject.com
- https://www.python.org/downloads
- https://github.com/jordansissel/xdotool

### How to use

- Download [the script](./auto-monitor-switch.py)
- Start OBS Studio and go to Tools > Scripts
- Click the "+" sign at the bottom left, find the script you just downloaded
- Click "Refresh scene lists", then select the 2 scenes you'd like to alternate
  between
- Fill in the other parameters and tick the "Active" checkbox


## License

[MIT](./LICENSE)

