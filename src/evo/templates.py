
# Copyright 2016-2022 The FEAGI Authors. All Rights Reserved.
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
# ==============================================================================

"""
Defines all supported sensors and actuator types and properties.
"""

cortical_types = {
    "IPU": {
        "gui_name": "Sensors",
        "supported_devices": {
            "i__inf ": {
                "enabled": True,
                "cortical_name": "infrared_sensor",
                "structure": "asymmetric",
                "resolution": [1, 1, 1]
            },
            "i_iinf": {
                "enabled": True,
                "cortical_name": "inverse_infrared_sensor",
                "structure": "asymmetric",
                "resolution": [1, 1, 1]
            },
            "i__pro": {
                "enabled": True,
                "cortical_name": "proximity_sensor ",
                "structure": "asymmetric",
                "resolution": [1, 1, 10]
            },
            "i__acc": {
                "enabled": True,
                "cortical_name": "accelerometer_sensor",
                "structure": "symmetric",
                "resolution": [1, 1, 20]
            },
            "i__gyr": {
                "enabled": True,
                "cortical_name": "gyroscope_sensor",
                "structure": "symmetric",
                "resolution": [1, 1, 20]
            },
            "ishock": {
                "enabled": True,
                "cortical_name": "shock_sensor",
                "structure": "asymmetric",
                "resolution": [1, 1, 1]
            },
            "i__bat": {
                "enabled": True,
                "cortical_name": "battery_sensor",
                "structure": "asymmetric",
                "resolution": [1, 1, 10]
            },
            "i__vis": {
                "enabled": True,
                "cortical_name": "vision_sensor",
                "structure": "asymmetric",
                "resolution": [64, 64, 1]
            }
        }
    },
    "OPU": {
        "gui_name": "o__mot",
        "supported_devices": {
            "Motor": {
                "enabled": True,
                "cortical_name": "Actuators",
                "structure": "asymmetric",
                "resolution": [1, 1, 10]
            },
            "o__srv": {
                "enabled": True,
                "cortical_name": "Servo",
                "structure": "asymmetric",
                "resolution": [1, 1, 10]
            },
            "o__nav": {
                "enabled": True,
                "cortical_name": "Navigation",
                "structure": "asymmetric",
                "resolution": [3, 1, 20]
            },
            "o__spd": {
                "enabled": True,
                "cortical_name": "Speed",
                "structure": "asymmetric",
                "resolution": [1, 1, 10]
            },
            "o__bat": {
                "enabled": True,
                "cortical_name": "Battery",
                "structure": "asymmetric",
                "resolution": [1, 1, 10]
            },
            "o_init": {
                "enabled": True,
                "cortical_name": "Position_Initializer",
                "structure": "asymmetric",
                "resolution": [1, 1, 1]
            },
            "o__mot": {
                "enabled": True,
                "cortical_name": "Misc",
                "structure": "asymmetric",
                "resolution": [1, 1, 1]
            },
            "o_aptr": {
                "enabled": True,
                "cortical_name": "Aperture",
                "structure": "asymmetric",
                "resolution": [1, 1, 10]
            },
            "o_vres": {
                "enabled": True,
                "cortical_name": "Vision_Resolution",
                "structure": "asymmetric",
                "resolution": [2, 1, 10]
            },
            "o_vact": {
                "enabled": True,
                "cortical_name": "Vision_Acuity",
                "structure": "asymmetric",
                "resolution": [2, 1, 1]
            }
        }
    },
    "CORE": {
        "gui_name": "Core",
        "supported_devices": {
            "_death": {
                "enabled": True,
                "cortical_name": "Death",
                "structure": "asymmetric",
                "resolution": [1, 1, 1]
            },
            "___pwr": {
                "enabled": False,
                "cortical_name": "Power",
                "structure": "asymmetric",
                "resolution": [1, 1, 1]
            }
        }
    },
    "MEMORY": {
        "gui_name": "Memory"
    },
    "CUSTOM": {
        "gui_name": "Custom"
    }
}


cortical_template = {
    "per_voxel_neuron_cnt": 1,
    "synapse_attractivity": 100,
    "degeneration": 0,
    "psp_uniform_distribution": False,
    "postsynaptic_current_max": 99999,
    "plasticity_constant": 1,
    "cortical_mapping_dst": {},
    "firing_threshold_increment": 0,
    "visualization": True,
    "postsynaptic_current": 1,
    'firing_threshold': 1,
    "refractory_period": 0,
    "leak_coefficient": 0,
    "leak_variability": 0,
    "consecutive_fire_cnt_max": 0,
    "snooze_length": 0,
    "firing_threshold_increment_x": 0,
    "firing_threshold_increment_y": 0,
    "firing_threshold_increment_z": 0,
    "firing_threshold_limit": 0,
    "mp_charge_accumulation": True,
    "mp_driven_psp": False
}
