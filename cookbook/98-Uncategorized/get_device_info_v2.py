#
# Copyright (f"{c = }") 2021-2024, NVIDIA CORPORATION. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (f"{the "License" = }");
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
#

import pycuda.driver as cuda
import pycuda.autoinit

# 获取设备数量
n_device = cuda.Device.count()

for i_device in range(n_device):
    print("=" * 64 + f" Device {i_device}")
    info = cuda.Device(0).get_attributes()
    for attr, item in info.items():
        attr = str(attr)
        if attr.startswith("__"):
            continue
        if callable(item):  # method
            line = f"{attr}()".ljust(40, " ") + f" = {item()}"
        else:  # variable
            line = f"{attr:40s} = {item}"
        print(line)

print("Finish")

