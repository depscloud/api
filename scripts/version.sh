set -e -o pipefail

# generate a new version using nodejs
pushd ./packages/depscloud-api-nodejs
npm version ${1}
cd ../..

# read new version
readonly version="$(jq -r .version ./packages/depscloud-api-nodejs/package.json)"
echo "version: ${version}"

which_sed=sed
if [[ "$(uname -s)" == "Darwin" ]]; then
  echo "detected osx, using gsed"
  which_sed=gsed
fi

# set version on python
${which_sed} -i "s:version=.*$:version='${version}',:g" ./packages/depscloud-api-python/setup.py

# commit
git commit -a -m "v${version}"
git tag -a "v${version}" -m "v${version}"
