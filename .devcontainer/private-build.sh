#!/bin/bash
cd "$(dirname $0)"
set -a
IMG=mastrogpt/agent41-starter
TAG=$(grep "$IMG" docker-compose.yml | awk -F: '{print $3}')
docker build -t ghcr.io/$IMG:$TAG . --load
