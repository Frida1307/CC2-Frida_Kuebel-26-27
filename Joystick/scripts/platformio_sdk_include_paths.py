Import("env")

import os
import re


package_dir = env.PioPlatform().get_package_dir(
    "framework-arduinoespressif32-esp32-libs"
)
if not package_dir:
    raise RuntimeError("PlatformIO ESP32 SDK package was not found")

sdk_include_dir = os.path.join(package_dir, "include")
compiler_include_flags = os.path.join(package_dir, "flags", "includes")
if not os.path.isfile(compiler_include_flags):
    raise RuntimeError(
        "PlatformIO ESP32 SDK include flags were not found: "
        + compiler_include_flags
    )

with open(compiler_include_flags, encoding="utf-8") as flags_file:
    relative_include_dirs = re.findall(
        r"-iwithprefixbefore\s+([^\s]+)", flags_file.read()
    )

include_dirs = [sdk_include_dir]
include_dirs.extend(
    os.path.normpath(os.path.join(sdk_include_dir, relative_dir))
    for relative_dir in relative_include_dirs
)
include_dirs = [path for path in include_dirs if os.path.isdir(path)]
if not include_dirs:
    raise RuntimeError("No ESP32 SDK include directories were found")

env.Append(CPPPATH=include_dirs)
