import os
from .common import mirex_melody_dataset_generator, load_melody_dataset

def generator(dataset_root):
    dataset_audio_path = os.path.join(dataset_root, "audio", "mono")
    dataset_annot_path = os.path.join(dataset_root, "GT")

    return mirex_melody_dataset_generator(dataset_audio_path, dataset_annot_path, annot_extension=".mel")

def dataset(dataset_root):
    return load_melody_dataset("orchset", generator(dataset_root))
