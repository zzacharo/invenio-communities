# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2021 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Community resources tests."""

import copy
from io import BytesIO

from invenio_communities.communities.records.api import Community


def test_community_disable(app, client):
    """Test a simple REST API flow."""
    app.config["COMMUNITIES_ENABLED"] = False
    # Create a community
    res = client.get('/communities')
    assert res.status_code == 404

    app.config["COMMUNITIES_ENABLED"] = True
