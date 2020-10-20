#!/usr/bin/env bash

readonly ROOT_DIR="$(dirname "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )" )"

function index_js() {
cat <<EOF
const parent = require("../");

module.exports = parent.${1};
EOF
}

function index_test_ts() {
cat <<EOF
describe("${1}", () => {
    test("require", () => {
        const schema = require("./index");

        expect(Object.keys(schema)).toMatchSnapshot();
    });
});
EOF
}

## TODO: EVENTUALLY REMOVE THESE

function root_js() {
  filenames=""
  for file in "$@"; do
    filenames="${filenames}"$'\n'"filenames.push(path.join(__dirname, ${file//\//\", \"}));"
  done

cat <<EOF
const path = require('path');
const protoLoader = require('@grpc/proto-loader');
const grpc = require('@grpc/grpc-js');

const filenames = [];
${filenames}

const packageDefinition = protoLoader.loadSync(
    filenames,
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true,
        includeDirs: [
            __dirname,
        ]
    }
);

const descriptor = grpc.loadPackageDefinition(packageDefinition);

module.exports = {
    v1alpha: descriptor.cloud.deps.api.v1alpha,
    v1beta: descriptor.depscloud.api.v1beta,
};
EOF
}

function translate_dir() {
  pushd "${ROOT_DIR}/${1}"
  for file in $(find . -name *.proto | cut -c 3-); do
    directory="${ROOT_DIR}/$(dirname "${file}")"
    base="$(basename "${directory}")"
    file_base="$(basename "${file}" .proto)"

    mkdir -p "${directory}"

    if [[ ! -f "${directory}/index.d.ts" ]]; then
      touch "${directory}/index.d.ts"
    fi

    index_js "${base}"      > "${directory}/index.js"
    index_test_ts "${base}" > "${directory}/index_test.ts"
  done
  popd
}

## MAIN EXECUTION
translate_dir depscloud_api
translate_dir depscloud/api

root_js $(find . -name *.proto | grep -v node_modules | sort | uniq | cut -c 3- | xargs -I {} echo '"{}"') > index.js
index_test_ts "api" > index_test.ts
