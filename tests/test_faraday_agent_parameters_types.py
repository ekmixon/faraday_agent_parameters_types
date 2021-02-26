#!/usr/bin/env python

"""Tests for `faraday_agent_parameters_types` package."""

import os
import pytest
from tests.config.agent_manifests import (
    generate_manifests,
    generate_env
)

from faraday_agent_parameters_types.custom_types.faraday_integer import FaradayInteger

all_json_manifests = generate_manifests()

@pytest.mark.parametrize("manifests", all_json_manifests, ids=lambda elem: elem["id_str"])
def test_new_config(manifests):
    config_executor = generate_env(manifests)
    for data in config_executor:
        if len(data) > 1:
            assert "type" in data.keys()
        else:
            assert "type" not in data.keys()


@pytest.mark.parametrize("manifests", all_json_manifests, ids=lambda elem: elem["id_str"])
def test_is_number(manifests):
    config_executor = generate_env(manifests)
    for data in config_executor:
        if len(data) > 1:
            value = os.getenv(data['name'])
            if data['type'] == 'string':
                pass
            elif data['type'] == 'integer':
                assert FaradayInteger(value)








