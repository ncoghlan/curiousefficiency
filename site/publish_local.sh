#!/bin/bash

# See http://redsymbol.net/articles/unofficial-bash-strict-mode/ for benefit of these options
set -euo pipefail
IFS=$'\n\t'

# Note: `readlink -f` (long available in GNU coreutils) is available on macOS 12.3 and later
script_dir="$(cd -- "$(dirname -- "$(readlink -f "${BASH_SOURCE[0]}")")" &> /dev/null && pwd)"

pushd "$script_dir" || exit 1

alias nikola="pdm run nikola"
nikola build && nikola deploy && nikola deploy publish

popd || exit 1
