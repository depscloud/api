set -e -o pipefail

if [[ $# -lt 1 ]]; then
  echo "expected at least one argument"
  exit 1
fi

readonly ROOT_DIR="$(dirname "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )" )"
readonly PYTHON_PACKAGE_DIR="${ROOT_DIR}/packages/depscloud-api-python"

python -m grpc_tools.protoc \
  -I=${ROOT_DIR}/proto/src \
  -I=${ROOT_DIR}/proto/lib \
  -I=${ROOT_DIR}/proto/lib/grpc-gateway/third_party/googleapis \
  --python_out=${PYTHON_PACKAGE_DIR} \
  --grpc_python_out=${PYTHON_PACKAGE_DIR} \
 ${1}
