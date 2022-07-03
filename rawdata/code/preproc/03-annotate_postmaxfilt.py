#!/usr/bin/env python
"""Manually mark bad segments after maxfilter for ICA"""
import logging
from os import getcwd

import hydra
from utils import (
    annotate_raw_manually,
    prepare_annotated_raw,
    write_annotations,
    write_bad_channels,
)

logger = logging.getLogger(__name__)


@hydra.main(config_path="../configs/", config_name="03-annotate_postmaxfilt")
def main(cfg):
    logger.info(f"Starting new session for {__file__}")
    logger.info(f"Current working directory is {getcwd()}")

    raw = prepare_annotated_raw(
        cfg.maxfiltered.maxfiltered_path, cfg.bad_channels_path, cfg.annotations_path
    )
    bads, annotations = annotate_raw_manually(raw)
    write_bad_channels(cfg.bad_channels_path, bads)
    write_annotations(cfg.annotations_path, annotations)

    logger.info(f"Channels marked as bad: {bads}")
    logger.info(f"Annotations: {annotations}")


if __name__ == "__main__":
    main()
