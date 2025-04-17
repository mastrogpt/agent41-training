#!/bin/bash
cd "$(dirname $0)"
set -a
DH_IMAGE=sciabarracom/agent41-starter
TAG=$(grep "image: $DH_IMAGE" docker-compose.yml | awk -F: '{print $3}')
docker build -t $DH_IMAGE:$TAG . --load
