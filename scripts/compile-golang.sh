set -e -o pipefail

if [[ $# -lt 1 ]]; then
  echo "expected at least one argument"
  exit 1
fi

api_configuration_file="$(dirname "${1}")/$(basename "${1}" .proto).yaml"
api_configuration=""
if [[ -f "${api_configuration_file}" ]]; then
  api_configuration=",grpc_api_configuration=${api_configuration_file}"
fi

readonly ROOT_DIR="$(dirname "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )" )"
readonly SWAGGER_DIR="${ROOT_DIR}/swagger"

protoc \
  -I=${ROOT_DIR}/proto/src \
  --go_out=$GOPATH/src \
  --go-grpc_out=$GOPATH/src \
  --grpc-gateway_out=allow_delete_body=true,logtostderr=true${api_configuration}:$GOPATH/src \
  --swagger_out=allow_delete_body=true,logtostderr=true${api_configuration}:${SWAGGER_DIR} \
  ${1}
