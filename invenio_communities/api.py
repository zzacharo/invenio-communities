# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2019 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Records API."""

from __future__ import absolute_import, print_function

from flask import current_app
from invenio_records.api import Record

from .models import CommunityMetadata


class Community(Record):
    """Define API for community creation and manipulation."""

    # TODO: Communities model doesn't have versioninig, some methods from
    # "invenio_records.api.RecordBase" have to be overridden/removed
    model_cls = CommunityMetadata

    @property
    def schema(self):
        """JSON Schema for the community metadata."""
        return current_app.config.get(
            'COMMUNITY_SCHEMA', 'communities/communities-v1.0.0.json')

    def delete(self, force=True):  # NOTE: By default hard-deleted
        """Delete a community."""
        return super(Community, self).delete(force=force)
