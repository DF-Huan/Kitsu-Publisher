from . import client as raw

from .sorting import sort_by_name
from .cache import cache
from .helpers import normalize_model_parameter
from .shot import get_sequence

default = raw.default_client


def new_scene(project, sequence, name, client=default):
***REMOVED***
    Create a scene for given sequence.
***REMOVED***
    project = normalize_model_parameter(project)
    sequence = normalize_model_parameter(sequence)
    shot = {"name": name, "sequence_id": sequence["id"]}
    return raw.post(
        "data/projects/%s/scenes" % project["id"],
        shot,
        client=client
    )


@cache
def all_scenes(project=None, client=default):
***REMOVED***
    Retrieve all scenes.
***REMOVED***
    project = normalize_model_parameter(project)
    if project is not None:
        scenes = raw.fetch_all(
            "projects/%s/scenes" % project["id"],
            client=client
***REMOVED***
***REMOVED***
        scenes = raw.fetch_all("scenes")
    return sort_by_name(scenes)


@cache
def all_scenes_for_project(project, client=default):
***REMOVED***
    Retrieve all scenes for given project.
***REMOVED***
    project = normalize_model_parameter(project)
    scenes = raw.fetch_all(
        "projects/%s/scenes" % project["id"],
        client=client
    )
    return sort_by_name(scenes)


@cache
def all_scenes_for_sequence(sequence, client=default):
***REMOVED***
    Retrieve all scenes which are children from given sequence.
***REMOVED***
    sequence = normalize_model_parameter(sequence)
    return sort_by_name(
        raw.fetch_all("sequences/%s/scenes" % sequence["id"], client=client),
    )


@cache
def get_scene(scene_id, client=default):
***REMOVED***
    Return scene corresponding to given scene ID.
***REMOVED***
    return raw.fetch_one("scenes", scene_id, client=client)


@cache
def get_scene_by_name(sequence, scene_name, client=default):
***REMOVED***
    Returns scene corresponding to given sequence and name.
***REMOVED***
    sequence = normalize_model_parameter(sequence)
***REMOVED*** = raw.fetch_all(
        "scenes/all",
        {"parent_id": sequence["id"], "name": scene_name},
        client=client
    )
    return next(iter(result or []), None)


def update_scene(scene, client=default):
***REMOVED***
    Save given scene data into the API.
***REMOVED***
    return raw.put("data/entities/%s" % scene["id"], scene, client=client)


def new_scene_asset_instance(scene, asset, description="", client=default):
***REMOVED***
    Creates a new asset instance on given scene. The instance number is
    automatically generated (increment highest number).
***REMOVED***
    scene = normalize_model_parameter(scene)
    asset = normalize_model_parameter(asset)
    data = {"asset_id": asset["id"], "description": description}
    return raw.post(
        "data/scenes/%s/asset-instances" % scene["id"],
        data,
        client=client
    )


@cache
def all_asset_instances_for_scene(scene, client=default):
***REMOVED***
    Return the list of asset instances listed in a scene.
***REMOVED***
    scene = normalize_model_parameter(scene)
    return raw.get(
        "data/scenes/%s/asset-instances" % scene["id"],
        client=client
    )


@cache
def get_asset_instance_by_name(scene, name, client=default):
***REMOVED***
    Returns the asset instance of the scene that has the given name.
***REMOVED***
    return raw.fetch_first(
        "asset-instances",
        {"name": name, "scene_id": scene["id"]},
        client=client
    )


@cache
def all_camera_instances_for_scene(scene, client=default):
***REMOVED***
    Return the list of camera instances listed in a scene.
***REMOVED***
    scene = normalize_model_parameter(scene)
    return raw.get(
        "data/scenes/%s/camera-instances" % scene["id"],
        client=client
    )


@cache
def all_shots_for_scene(scene, client=default):
***REMOVED***
    Return the list of shots issued from given scene.
***REMOVED***
    scene = normalize_model_parameter(scene)
    return raw.get(
        "data/scenes/%s/shots" % scene["id"],
        client=client
    )


def add_shot_to_scene(scene, shot, client=default):
***REMOVED***
    Link a shot to a scene to mark the fact it was generated out from that
    scene.
***REMOVED***
    scene = normalize_model_parameter(scene)
    shot = normalize_model_parameter(shot)
    data = {"shot_id": shot["id"]}
    return raw.post(
        "data/scenes/%s/shots" % scene["id"],
        data,
        client=client
    )


def remove_shot_from_scene(scene, shot, client=default):
***REMOVED***
    Remove link between a shot and a scene.
***REMOVED***
    scene = normalize_model_parameter(scene)
    shot = normalize_model_parameter(shot)
    return raw.delete(
        "data/scenes/%s/shots/%s" % (scene["id"], shot["id"]),
        client=client
    )


def update_asset_instance_name(asset_instance, name, client=default):
***REMOVED***
    Update the name of given asset instance.
***REMOVED***
    path = "/data/asset-instances/%s" % asset_instance["id"]
    return raw.put(path, {"name": name}, client=client)


def update_asset_instance_data(asset_instance, data, client=default):
***REMOVED***
    Update the extra data of given asset instance.
***REMOVED***
    asset_instance = normalize_model_parameter(asset_instance)
    path = "/data/asset-instances/%s" % asset_instance["id"]
    return raw.put(path, {"data": data}, client=client)


@cache
def get_sequence_from_scene(scene, client=default):
***REMOVED***
    Return sequence which is parent of given shot.
***REMOVED***
    scene = normalize_model_parameter(scene)
    return get_sequence(scene["parent_id"], client=client)