// Code generated by protoc-gen-dts. DO NOT EDIT.
// source: depscloud_api/v1alpha/extractor/extractor.proto

import {
  ChannelCredentials, 
  Client, 
  ClientUnaryCall,
  ClientReadableStream,
  ClientWritableStream,
  ClientDuplexStream,
  Metadata,
  ServerUnaryCall,
  ServerReadableStream,
  ServerWritableStream,
  ServerDuplexStream,
  ServiceDefinition,
} from "@grpc/grpc-js";

import {
  DependencyManagementFile,
} from "../deps/deps";

export interface ExtractRequest {
  separator: string;
  fileContents: ExtractRequest_FileContentsEntry;
  url: string;
}

export type ExtractRequest_FileContentsEntry = { [key: string]: string }

export interface ExtractResponse {
  managementFiles: Array<DependencyManagementFile>;
}

export interface MatchRequest {
  separator: string;
  paths: Array<string>;
}

export interface MatchResponse {
  matchedPaths: Array<string>;
}

export interface IDependencyExtractor { 
  match(call: ServerUnaryCall<MatchRequest, MatchResponse>, callback: (error: Error, response: MatchResponse) => void): void; 
  extract(call: ServerUnaryCall<ExtractRequest, ExtractResponse>, callback: (error: Error, response: ExtractResponse) => void): void;
}

export class DependencyExtractor extends Client {
  public static service: ServiceDefinition<IDependencyExtractor>;

  constructor(address: string, credentials: ChannelCredentials, options?: object); 
  public match(request: MatchRequest, callback: (error: Error, response: MatchResponse) => void): void;
  public match(request: MatchRequest, metadata: Metadata, callback: (error: Error, response: MatchResponse) => void): void; 
  public extract(request: ExtractRequest, callback: (error: Error, response: ExtractResponse) => void): void;
  public extract(request: ExtractRequest, metadata: Metadata, callback: (error: Error, response: ExtractResponse) => void): void;
}

