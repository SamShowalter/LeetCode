#!/usr/bin/env bash
set -euo pipefail

dirs=(
  lc_1768 lc_1071 lc_1431 lc_0605 lc_0345 lc_0151 lc_0238 lc_0334 lc_0443 lc_0283
  lc_0392 lc_0011 lc_1679 lc_0643 lc_1456 lc_1004 lc_1493 lc_1732 lc_0724 lc_2215
  lc_1207 lc_1657 lc_2352 lc_2390 lc_0735 lc_0394 lc_0933 lc_0649 lc_2095 lc_0328
  lc_0206 lc_2130 lc_0104 lc_0872 lc_1448 lc_0437 lc_1372 lc_0236 lc_0199 lc_1161
  lc_0700 lc_0450 lc_0841 lc_0547 lc_1466 lc_0399 lc_1926 lc_0994 lc_0215 lc_2336
  lc_2542 lc_2462 lc_0374 lc_2300 lc_0162 lc_0875 lc_0017 lc_0216 lc_1137 lc_0746
  lc_0198 lc_0790 lc_0062 lc_1143 lc_0714 lc_0072 lc_0338 lc_0136 lc_1318 lc_0208
  lc_1268 lc_0435 lc_0452 lc_0739 lc_0901
)

for d in "${dirs[@]}"; do
  # ensure directory exists
  mkdir -p "$d"

  num=${d#lc_}           # the four-digit number (e.g., 0011, 0605, 1768)
  file="$d/lc_${num}.py"

  # write/overwrite the template (no escaping in triple-quoted strings)
  cat > "$file" <<EOF
import os
import sys
from typing import Dict, List

#######################################################################
# Problem # ${num}
#######################################################################
problem = """
"""

#######################################################################
# Notes
#######################################################################

notes = """

"""

#######################################################################
# Solution
#######################################################################

EOF

  printf 'wrote:     %s\n' "$file"
done
