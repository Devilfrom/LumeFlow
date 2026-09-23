#
#  Copyright 2025 The InfiniFlow Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import os
from enum import Enum

from rag.utils.azure_sas_conn import LumeFlowAzureSasBlob
from rag.utils.azure_spn_conn import LumeFlowAzureSpnBlob
from rag.utils.minio_conn import LumeFlowMinio
from rag.utils.s3_conn import LumeFlowS3
from rag.utils.oss_conn import LumeFlowOSS


class Storage(Enum):
    MINIO = 1
    AZURE_SPN = 2
    AZURE_SAS = 3
    AWS_S3 = 4
    OSS = 5


class StorageFactory:
    storage_mapping = {
        Storage.MINIO: LumeFlowMinio,
        Storage.AZURE_SPN: LumeFlowAzureSpnBlob,
        Storage.AZURE_SAS: LumeFlowAzureSasBlob,
        Storage.AWS_S3: LumeFlowS3,
        Storage.OSS: LumeFlowOSS,
    }

    @classmethod
    def create(cls, storage: Storage):
        return cls.storage_mapping[storage]()


STORAGE_IMPL_TYPE = os.getenv('STORAGE_IMPL', 'MINIO')
STORAGE_IMPL = StorageFactory.create(Storage[STORAGE_IMPL_TYPE])
