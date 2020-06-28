set -e -o pipefail

if [[ $# -lt 1 ]]; then
  echo "expected at least one argument"
  exit 1
fi

readonly ROOT_DIR="$(dirname "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )" )"
readonly SWAGGER_DIR="${ROOT_DIR}/swagger"

protoc \
  -I=${ROOT_DIR}/proto/lib \
  -I=${ROOT_DIR}/proto/src \
  -I=${ROOT_DIR}/proto/lib/grpc-gateway/third_party/googleapis \
  --gogo_out=plugins=grpc:$GOPATH/src \
  --grpc-gateway_out=logtostderr=true:$GOPATH/src \
  --swagger_out=logtostderr=true:${SWAGGER_DIR} \
  ${1}
