import os

from backend.services.json_loader import load_pda_from_json


SAMPLES_DIR = "backend/samples"


def list_samples():
    samples = []
    for file_name in os.listdir(SAMPLES_DIR):
        if file_name.endswith(".json"):
            samples.append(file_name)
    return samples


def load_sample(sample_name):
    file_path = os.path.join(SAMPLES_DIR, sample_name)
    return load_pda_from_json(file_path)