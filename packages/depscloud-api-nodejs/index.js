const path = require('path');
const protoLoader = require('@grpc/proto-loader');
const grpc = require('@grpc/grpc-js');

const filenames = [];

filenames.push(path.join(__dirname, "depscloud", "api", "v1beta", "core.proto"));
filenames.push(path.join(__dirname, "depscloud", "api", "v1beta", "manifest.proto"));
filenames.push(path.join(__dirname, "depscloud", "api", "v1beta", "rpc.proto"));
filenames.push(path.join(__dirname, "depscloud_api", "v1alpha", "deps", "deps.proto"));
filenames.push(path.join(__dirname, "depscloud_api", "v1alpha", "extractor", "extractor.proto"));
filenames.push(path.join(__dirname, "depscloud_api", "v1alpha", "schema", "schema.proto"));
filenames.push(path.join(__dirname, "depscloud_api", "v1alpha", "store", "store.proto"));
filenames.push(path.join(__dirname, "depscloud_api", "v1alpha", "tracker", "tracker.proto"));
filenames.push(path.join(__dirname, "graphstore", "api", "v1beta", "graphstore.proto"));

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
