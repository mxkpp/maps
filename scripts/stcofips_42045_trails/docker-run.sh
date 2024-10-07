#!/bin/bash

# Run from repo root: ./scripts/stcofips_42045_trails/docker-run.sh

set -euo pipefail

docker build -t maps .

run_module () {
    module=$1
    log_file=$2
    cmd="python3 -m ${module}"
    docker run --rm \
        -v $PWD:/app \
        -t maps \
        $cmd \
        |& tee "${log_file}"
}

set -x

run_module "scripts.stcofips_42045_trails.prep_data" "logs/prep_data.log"
