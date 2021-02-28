# OBS Studio scripts
My scripts for the recording and streaming software [OBS
Studio](https://github.com/obsproject/obs-studio), for the rare times when I
fail to find a plugin or script that already does what I want on Linux.
None of these are tested rigorously, and they might cause your computer to gain
sentience and reclaim dominion over your household. Or crash OBS.

## [auto-monitor-switch.py](./auto-monitor-switch.py)
### What does it do?
It automatically alternates between 2 scenes of your choosing based on the
position of the active window (specifically its top-left corner) on your
dual-monitor setup. Concretely, I made it so I could have Firefox on a monitor
and a terminal in the other, with each window having a scene that focuses on it,
and have OBS naturally follow my workflow/Alt+Tabbing without having to think
about it.

### Why not just use Automatic/Advanced Scene Switchers?
- The automatic one uses window titles to keep track, but Firefox and my
  terminal change titles every time I change tabs, so it can't keep track.
- The advanced one uses mouse position to keep track, but I Alt+Tab a lot and
  can spend a lot of time working without moving the mouse. (The
Advanced Scene Switcher plugin has many switch triggers available and it's
entirely possible that I simply missed the "active window" option, or if not,
that such an option gets added in the future. In any case, that's more practice
for me.)

### Prerequisites
- You need Linux, OBS Studio, Python 3.6 or later, and xdotool. Try this in a
  terminal:
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

## [toggle-visibility-all-scenes.py](./toggle-visibility-all-scenes.py)
### What does it do?
If you have a source present in multiple scenes, toggling its visibility
(hiding/showing it by clicking the eye icon) in one scene will apply the change
in all the other scenes that contain that source as well.

### Prerequisites
OBS and Python, check the prerequisites section for the script above if you need help.

### How to use
Download [the script](./toggle-visibility-all-scenes.py), start OBS and go to
Tools > Scripts, "+" button to add the script, tick the box.

## License

[MIT](./LICENSE)

