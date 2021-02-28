import obspython as obs
import subprocess

# GLOBAL VARIABLES #############################################################

active_monitor = 0
left_width = 1920
check_freq = 300
scene_names = ["", ""]
monitor_left_list = None
monitor_right_list = None
is_active = False

# GLOBAL SCRIPTS ###############################################################

def script_defaults(settings):
    obs.obs_data_set_default_bool(settings, "is_active", is_active)
    obs.obs_data_set_default_int(settings, "left_width", left_width)
    obs.obs_data_set_default_int(settings, "check_freq", check_freq)
    obs.obs_data_set_default_string(settings, "scene_for_left_mon", "")
    obs.obs_data_set_default_string(settings, "scene_for_right_mon", "")

def script_description():
    return ("Automatically switches between 2 scenes based on the monitor "
            "containing the active window in a Linux environment. Specific "
            "to installations with a dual-monitor setup."
            "\n\n Dependencies: xdotool")

def script_properties():
    global monitor_left_list, monitor_right_list
    props = obs.obs_properties_create()
    active = obs.obs_properties_add_bool(props, "is_active", "Active")
    refresh_lists = obs.obs_properties_add_button(
            props,
            "refresh_lists",
            "Refresh scene lists",
            refresh_lists_callback
            )

    monitor_left_list = obs.obs_properties_add_list(
            props,
            "scene_for_left_mon",
            "Scene for left monitor",
            obs.OBS_COMBO_TYPE_EDITABLE,
            obs.OBS_COMBO_FORMAT_STRING
            )

    monitor_right_list = obs.obs_properties_add_list(
            props,
            "scene_for_right_mon",
            "Scene for right monitor",
            obs.OBS_COMBO_TYPE_EDITABLE,
            obs.OBS_COMBO_FORMAT_STRING
            )

    check_freq_prop = obs.obs_properties_add_int(
            props,
            "check_freq",
            "Check for active monitor every (ms)",
            2,
            30000,
            50
            )

    left_width_prop = obs.obs_properties_add_int(
            props,
            "left_width",
            "Left monitor width (px)",
            144,
            3840,
            10
            )

    return props

def script_load(settings):
    obs.timer_add(switch_scenes, check_freq)

def script_update(settings):
    global is_active, scene_names, left_width, check_freq
    is_active = obs.obs_data_get_bool(settings, "is_active")
    scene_names[0] = obs.obs_data_get_string(settings, "scene_for_left_mon")
    scene_names[1] = obs.obs_data_get_string(settings, "scene_for_right_mon")
    left_width = obs.obs_data_get_int(settings, "left_width")
    check_freq = obs.obs_data_get_int(settings, "check_freq")
    obs.timer_remove(switch_scenes)
    if is_active:
        obs.timer_add(switch_scenes, check_freq)

#-------------------------------------------------------------------------------

def refresh_lists_callback(props, prop):
    if populate_scene_lists([monitor_left_list, monitor_right_list]):
        return True
    return True

def populate_scene_lists(lists):
    scene_names = obs.obs_frontend_get_scene_names()
    for l in lists:
        obs.obs_property_list_clear(l)
        obs.obs_property_list_add_string(l, "", "")
        for name in scene_names:
            obs.obs_property_list_add_string(l, name, name)

# SCENE SWITCHING ##############################################################

def get_active_monitor():
    global active_monitor
    bash_command = ("xdotool getactivewindow getwindowgeometry "
            "| grep -m 1 Position "
            "| grep -Eo [[:digit:]]+ "
            "| head -n 1")
    x = subprocess.run(
            bash_command,
            shell=True,
            capture_output=True,
            ).stdout.decode()
    if x == "":
        return active_monitor
    elif int(x) < left_width:
        active_monitor = 0
    else:
        active_monitor = 1
    return active_monitor

def should_switch_scenes():
    current = obs.obs_frontend_get_current_scene()
    name = obs.obs_source_get_name(current)
    obs.obs_source_release(current)
    if name in scene_names and name != scene_names[get_active_monitor()]:
        return True
    return False

def switch_scenes():
    if is_active and should_switch_scenes():
        sources = obs.obs_enum_sources()
        scenes = obs.obs_frontend_get_scenes(sources)
        obs.source_list_release(sources)
        current = obs.obs_frontend_get_current_scene()
        for s in scenes:
            if s != current and obs.obs_source_get_name(s) in scene_names:
                obs.obs_frontend_set_current_scene(s)
        obs.obs_source_release(current)
