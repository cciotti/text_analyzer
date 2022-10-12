# coding=utf-8
__date__ = "29 September 2022"

import logging
import pathlib

from dynaconf import Dynaconf

logger = logging.getLogger(__name__)

_loc = pathlib.Path(__file__).parent

settings = Dynaconf(envvar_prefix="C_VAR", settings_files=[f"{_loc}/settings.toml"])
