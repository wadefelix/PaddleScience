# Copyright (c) 2021 PaddlePaddle Authors. All Rights Reserved.
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

import paddlescience as psci
import numpy as np

geo = psci.geometry.Rectangular(
    space_origin=(0.0, 0.0, 0.0), space_extent=(1.0, 1.0, 1.0))

geo_disc = geo.discretize(space_nsteps=(3, 6, 4))

data = np.ones(4 * 7 * 5, dtype="float32")
psci.visu.save_vtk(geo_disc, data, 'test3d')
