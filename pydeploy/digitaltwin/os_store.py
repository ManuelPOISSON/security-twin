import os

from dotenv import load_dotenv
from digitaltwin.utils.config import resolve_env_path

load_dotenv(override=True)

# Resolve paths to absolute paths
images_location = resolve_env_path("IMAGES_LOCATION", "/opt/images")
virtio_location = resolve_env_path("VIRTIO_LOCATION", "/opt/images")

os_store = {
    "linux": {
        "debian": {
            "20250210-2019": {
                "path": images_location + "/debian-12-genericcloud-amd64-20250210-2019.qcow2"
            },
            "20250811-2201": {
                "path": images_location + "/debian-13-genericcloud-amd64-20250811-2201.qcow2"
            }

        }
    },
    "windows": {
        "windows10": {
            "21H2": {
                "path": images_location + "/en-us_windows_10_enterprise_ltsc_2021_x64_dvd_d289cf96.iso"
            },
            "22H2": {
                "path": images_location + "/Win10_22H2_EnglishInternational_x64v1.iso"
            },
        },
        "server22": {
            "20348.3207": {
                "path": images_location + "/en-us_windows_server_version_2022_updated_sep_2021_x64_dvd_f4ba9ac1.iso"
            }
        },
        "server19": {
            "17763.737": {
                "path": images_location + "/17763.737.190906-2324.rs5_release_svc_refresh_SERVER_EVAL_x64FRE_en-us_1.iso"
            }
        },
    },
    "virtio": {
        "path": virtio_location + "/virtio-win-0.1.266.iso"
    },
}
