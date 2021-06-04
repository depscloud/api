FROM golang:1.16-buster

RUN apt-get update && apt-get install -y unzip

ENV PROTOC_VERSION=3.9.1

RUN curl -sSL -o protoc.zip https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOC_VERSION}/protoc-${PROTOC_VERSION}-linux-x86_64.zip && \
    unzip -d /usr/local/protoc protoc.zip && \
    rm -rf protoc.zip

ENV PATH="${PATH}:/usr/local/protoc/bin"

RUN GOBIN=/usr/local/bin go get \
    github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway@v1.16.0 \
    github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger@v1.16.0 \
    google.golang.org/protobuf/cmd/protoc-gen-go@v1.26.0 \
    google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.1.0 \
    github.com/go-bindata/go-bindata/...
