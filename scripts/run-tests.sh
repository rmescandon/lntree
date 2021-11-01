#!/bin/sh -eu
#
# Copyright (C) 2021 Telefónica S.A. All Rights Reserved
#

main_folder=$(pwd)
workdir="$(mktemp -d)"

cleanup() {
  cd "${main_folder}"
  rm -rf "$workdir"
  echo "Deleted working folder: ${workdir}"
  docker rmi lntree:latest || true
  echo "Removed docker image aus-unit-tests:latest"
}
trap cleanup EXIT INT

cp -rf . "$workdir"
cd "$workdir"

cat << EOF > Dockerfile
FROM python:3.8
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN pip install flake8

COPY . .

CMD ["flake8", "./lntree/lntree.py"]
EOF

docker build -f Dockerfile -t lntree .
docker run --rm lntree
