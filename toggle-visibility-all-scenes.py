import obspython as obs

# GLOBAL VARIABLES #############################################################

is_active = False
visibility_handler = None

# GLOBAL FUNCTIONS #############################################################

def script_defaults(settings):
    obs.obs_data_set_default_bool(settings, "is_active", is_active)

def script_description():
    return ("When clicking the eye to toggle the visibility of a source that is "
        "present in multiple scenes, that change will be reflected in all the "
        "scenes.")

def script_update(settings):
    global is_active, visibility_handler
    is_active = obs.obs_data_get_bool(settings, "is_active")
    if is_active:
        scenes = obs.obs_frontend_get_scenes()
        for scene in scenes:
            visibility_handler = obs.obs_source_get_signal_handler(scene)
            obs.signal_handler_connect(
                    visibility_handler,
                    "item_visible",
                    on_visibility_toggle
                    )
        obs.source_list_release(scenes)
    else:
        obs.signal_handler_disconnect(
                visibility_handler,
                "item_visible",
                on_visibility_toggle
                )
        visibility_handler = None

def script_properties():
    props = obs.obs_properties_create()
    is_active_prop = obs.obs_properties_add_bool(
            props,
            "is_active",
            "Active"
            )

    return props

################################################################################

def on_visibility_toggle(calldata):
    scenes_as_sources = obs.obs_frontend_get_scenes()
    sceneitem = obs.calldata_sceneitem(calldata, "item")
    visibility = obs.calldata_bool(calldata, "visible")
    name = obs.obs_source_get_name(obs.obs_sceneitem_get_source(sceneitem))
    for scene_as_source in scenes_as_sources:
        scene = obs.obs_scene_from_source(scene_as_source)
        match = obs.obs_scene_find_source(scene, name)
        if match:
            obs.obs_sceneitem_set_visible(match, visibility)
    obs.source_list_release(scenes_as_sources)
