# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import NamedTuple
import json

from google.cloud.pubsublite_v1.types.common import Cursor
from google.cloud.pubsublite.types.partition import Partition


class PublishMetadata(NamedTuple):
    partition: Partition
    cursor: Cursor

    def encode(self) -> str:
        return json.dumps(
            {"partition": self.partition.value, "offset": self.cursor.offset}
        )

    @staticmethod
    def decode(source: str) -> "PublishMetadata":
        loaded = json.loads(source)
        return PublishMetadata(
            partition=Partition(loaded["partition"]),
            cursor=Cursor(offset=loaded["offset"]),
        )
