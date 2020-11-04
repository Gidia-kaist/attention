from pathlib import Path

from . import (
    utils,
    network,
    models,
    analysis,
    preprocessing,
    datasets,
    encoding,
    pipeline,
    learning,
    evaluation,
    environment,
    conversion,
    shared_preference,
)

ROOT_DIR = Path(__file__).parents[0].parents[0]
