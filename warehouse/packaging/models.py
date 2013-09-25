# Copyright 2013 Donald Stufft
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

from sqlalchemy import Table, Column, CheckConstraint
from sqlalchemy import Boolean, UnicodeText
from sqlalchemy import sql

from warehouse.application import Warehouse


packages = Table("packages", Warehouse.metadata,
    Column("name", UnicodeText(), primary_key=True, nullable=False),
    Column("stable_version", UnicodeText()),
    Column("normalized_name", UnicodeText()),
    Column("autohide", Boolean(), server_default=sql.true()),
    Column("comments", Boolean(), server_default=sql.true()),
    Column("bugtrack_url", UnicodeText()),
    Column(
        "hosting_mode",
        UnicodeText(),
        nullable=False,
        server_default="pypi-explicit",
    ),

    # Validate that packages begin and end with an alpha numeric and contain
    #   only alpha numeric, ., _, and -.
    CheckConstraint(
        "name ~* '^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$'",
        name="packages_valid_name",
    ),
)