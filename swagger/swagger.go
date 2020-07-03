// Code generated by go-bindata. (@generated) DO NOT EDIT.

// Package swagger generated by go-bindata.// sources:
// v1alpha/tracker/tracker.swagger.json
// v1alpha/extractor/extractor.swagger.json
// v1alpha/schema/schema.swagger.json
// v1alpha/deps/deps.swagger.json
// v1alpha/store/store.swagger.json
package swagger

import (
	"bytes"
	"compress/gzip"
	"fmt"
	"net/http"
	"io"
	"io/ioutil"
	"os"
	"path/filepath"
	"strings"
	"time"
)

func bindataRead(data []byte, name string) ([]byte, error) {
	gz, err := gzip.NewReader(bytes.NewBuffer(data))
	if err != nil {
		return nil, fmt.Errorf("read %q: %v", name, err)
	}

	var buf bytes.Buffer
	_, err = io.Copy(&buf, gz)
	clErr := gz.Close()

	if err != nil {
		return nil, fmt.Errorf("read %q: %v", name, err)
	}
	if clErr != nil {
		return nil, err
	}

	return buf.Bytes(), nil
}

type asset struct {
	bytes []byte
	info  os.FileInfo
}

type bindataFileInfo struct {
	name    string
	size    int64
	mode    os.FileMode
	modTime time.Time
}

// Name return file name
func (fi bindataFileInfo) Name() string {
	return fi.name
}

// Size return file size
func (fi bindataFileInfo) Size() int64 {
	return fi.size
}

// Mode return file mode
func (fi bindataFileInfo) Mode() os.FileMode {
	return fi.mode
}

// ModTime return file modify time
func (fi bindataFileInfo) ModTime() time.Time {
	return fi.modTime
}

// IsDir return file whether a directory
func (fi bindataFileInfo) IsDir() bool {
	return fi.mode&os.ModeDir != 0
}

// Sys return file is sys mode
func (fi bindataFileInfo) Sys() interface{} {
	return nil
}


type assetFile struct {
	*bytes.Reader
	name            string
	childInfos      []os.FileInfo
	childInfoOffset int
}

type assetOperator struct{}

// Open implement http.FileSystem interface
func (f *assetOperator) Open(name string) (http.File, error) {
	var err error
	if len(name) > 0 && name[0] == '/' {
		name = name[1:]
	}
	content, err := Asset(name)
	if err == nil {
		return &assetFile{name: name, Reader: bytes.NewReader(content)}, nil
	}
	children, err := AssetDir(name)
	if err == nil {
		childInfos := make([]os.FileInfo, 0, len(children))
		for _, child := range children {
			childPath := filepath.Join(name, child)
			info, errInfo := AssetInfo(filepath.Join(name, child))
			if errInfo == nil {
				childInfos = append(childInfos, info)
			} else {
				childInfos = append(childInfos, newDirFileInfo(childPath))
			}
		}
		return &assetFile{name: name, childInfos: childInfos}, nil
	} else {
		// If the error is not found, return an error that will
		// result in a 404 error. Otherwise the server returns
		// a 500 error for files not found.
		if strings.Contains(err.Error(), "not found") {
			return nil, os.ErrNotExist
		}
		return nil, err
	}
}

// Close no need do anything
func (f *assetFile) Close() error {
	return nil
}

// Readdir read dir's children file info
func (f *assetFile) Readdir(count int) ([]os.FileInfo, error) {
	if len(f.childInfos) == 0 {
		return nil, os.ErrNotExist
	}
	if count <= 0 {
		return f.childInfos, nil
	}
	if f.childInfoOffset+count > len(f.childInfos) {
		count = len(f.childInfos) - f.childInfoOffset
	}
	offset := f.childInfoOffset
	f.childInfoOffset += count
	return f.childInfos[offset : offset+count], nil
}

// Stat read file info from asset item
func (f *assetFile) Stat() (os.FileInfo, error) {
	if len(f.childInfos) != 0 {
		return newDirFileInfo(f.name), nil
	}
	return AssetInfo(f.name)
}

// newDirFileInfo return default dir file info
func newDirFileInfo(name string) os.FileInfo {
	return &bindataFileInfo{
		name:    name,
		size:    0,
		mode:    os.FileMode(2147484068), // equal os.FileMode(0644)|os.ModeDir
		modTime: time.Time{}}
}

// AssetFile return a http.FileSystem instance that data backend by asset
func AssetFile() http.FileSystem {
	return &assetOperator{}
}

var _v1alphaTrackerTrackerSwaggerJson = []byte("\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\xff\xe4\x58\x4d\x8f\x9b\x30\x10\xbd\xe7\x57\x58\x6e\x8f\xab\x4d\xbb\xbd\xed\xad\xea\xb6\xa7\xf6\xd2\x8f\x53\x55\x45\x8e\x99\x10\xef\x82\x6d\xd9\x43\x2a\xba\xca\x7f\xaf\x8c\x49\x03\xec\x42\x82\x4d\x12\xad\x7a\x88\x88\xf0\x8c\x99\x37\x6f\xfc\x66\xe0\x71\x46\x08\xb5\xbf\x59\x9a\x82\xa1\xb7\x84\xde\x5c\xbf\xa1\x57\xee\x9e\x90\x2b\x45\x6f\x89\x5b\x27\x84\xa2\xc0\x0c\xdc\x7a\x02\xda\xf2\x4c\x15\xc9\x82\x69\x31\xdf\xbc\x65\x99\x5e\xb3\x39\x1a\xc6\x1f\xc0\xec\xae\xd7\xda\x28\x54\xd5\x3e\x84\xd0\x0d\x18\x2b\x94\x74\xde\xf5\x5f\x22\x15\x12\x0b\x48\x67\x84\x6c\xab\xa7\x71\x25\x6d\x91\x83\xa5\xb7\xe4\xa7\xf7\x62\x5a\x67\x82\x33\x14\x4a\xce\xef\xad\x92\xce\xf6\x57\x65\xab\x8d\x4a\x0a\x7e\xa4\x2d\xc3\xb5\x33\x7c\xf4\x8f\x49\x60\x25\xa4\x70\x76\x76\x8f\xcd\x41\xba\x03\x0d\x32\x01\xc9\xcb\x2f\x4c\xb2\x14\x72\x90\xf8\x49\x54\x90\xbd\x95\xcb\x41\xa9\xab\x14\xa8\xe5\x3d\x70\xac\xd1\xf9\x78\x34\x18\x14\x60\x1b\xd6\x84\xd0\x8c\xc9\xb4\x60\x29\xb4\xee\x36\xf6\xb1\x68\x84\x4c\xe9\xbf\xa5\xed\xd5\xde\xd7\x96\x16\x21\x0f\xf2\x54\x85\xe1\xf0\xc3\x64\x21\xce\xca\xa4\x4c\x8a\x3f\x55\x26\x43\xfc\x73\x95\x14\x59\x10\xe0\x7d\x91\x8c\x76\x4d\x76\xdc\x75\x19\x68\xf8\x33\x63\x58\x49\xaf\x9a\x4b\x02\x21\xef\xda\x13\x42\x5f\x1b\x58\x39\x8f\x57\xf3\x46\xb1\xec\x0a\xbd\x5d\x2a\xb4\xe1\xb9\x9d\x75\xff\xf9\x6b\x1d\x28\xad\x4e\xc4\xb2\x58\xbd\x97\x65\x4c\x4d\x39\xfb\x45\x11\x46\xee\x86\x65\xc5\x21\x6e\x5a\x19\x5a\x29\x93\x33\x74\xab\xcb\x12\x81\x1e\x40\x68\x0a\x89\x22\x87\x8f\xc6\x28\x13\x03\x11\x3a\x1b\x1c\x8d\x8f\xab\xa4\x17\x9e\x90\x08\x4e\xe1\x7a\xf0\x09\x89\xef\x6e\x7a\x4a\x1a\xac\x0d\x3c\xc4\x09\x20\x13\xd9\xc9\x6a\xb2\x59\x52\x23\x2a\xd1\xf2\x35\xe4\xcc\x57\xb1\xbd\x94\xbe\xd5\xc7\x7d\xe1\x74\x1f\x0d\x13\x12\x83\xb4\x8e\x2b\x3d\xc5\x99\xef\x7b\x56\x2b\x99\x8d\xe7\x7a\x3a\x8e\x0b\x77\x80\x03\xdf\x6a\x2e\xc6\x41\x78\x8f\x19\x2b\xd6\x43\x39\xe8\x76\x8c\xb3\xa6\xe0\xcc\xfd\x6e\x20\x0f\xdf\xaa\xb6\x1d\x93\x87\xc0\xae\x30\xa6\x96\x1b\x6e\x0f\x42\x26\x71\xb8\xeb\x59\xf1\xb3\xb0\x78\xd7\xe8\xe0\x5f\xc1\x6a\x25\x6d\x54\x2a\xce\x38\x11\xd4\x28\xc2\x86\x82\x67\x52\x80\x93\x26\x00\x5f\x0a\x7c\x2f\x85\xc9\x14\xd8\xfd\x99\x3c\x19\xf0\x3a\xe8\x3a\xe0\x5a\xbe\x02\x41\x57\xce\x53\x60\xd6\x03\xfa\x17\x3e\xfa\x70\x55\xf4\xf7\xe5\x88\x89\xea\xb4\x04\xb5\xfa\x4a\x18\x31\x5e\x8c\xff\x3b\x62\xfc\xab\xe3\x89\x89\xa9\x1b\x5d\x0c\x31\x93\x48\xe4\x89\xc1\xb6\x65\x22\x18\x74\x5b\x66\x62\x54\xf1\xc9\xac\x79\x90\xa9\xdd\x78\x3a\x62\xf2\x19\x73\x22\x8f\xc1\x1d\x3f\x15\xd9\xee\x0e\x07\xe3\xec\x72\xd5\x42\x3d\x45\x16\x87\x70\x7f\x77\x97\x29\xca\xbb\xda\xcf\x4d\x61\x3d\xf5\xbd\x54\x2a\x03\x26\x7b\x5f\xf8\xeb\xe5\x03\x51\x3f\xff\x59\x24\x22\xec\x8b\x7f\x80\xfa\xf0\x72\x5e\x48\x87\x18\x79\x3a\x97\x45\x4f\x93\xa3\xaa\x7e\xf7\x79\xe1\x3c\xda\x31\x73\xbf\xed\xec\x6f\x00\x00\x00\xff\xff\x5e\xb1\x3b\x87\xcc\x16\x00\x00")

func v1alphaTrackerTrackerSwaggerJsonBytes() ([]byte, error) {
	return bindataRead(
		_v1alphaTrackerTrackerSwaggerJson,
		"v1alpha/tracker/tracker.swagger.json",
	)
}

func v1alphaTrackerTrackerSwaggerJson() (*asset, error) {
	bytes, err := v1alphaTrackerTrackerSwaggerJsonBytes()
	if err != nil {
		return nil, err
	}

	info := bindataFileInfo{name: "v1alpha/tracker/tracker.swagger.json", size: 5836, mode: os.FileMode(420), modTime: time.Unix(1593753409, 0)}
	a := &asset{bytes: bytes, info: info}
	return a, nil
}

var _v1alphaExtractorExtractorSwaggerJson = []byte("\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\xff\xc4\x56\x4d\x6f\x13\x31\x10\xbd\xe7\x57\x58\x86\x63\xd5\x40\xb9\xe5\x86\xa0\xdc\x2a\x21\x24\x4e\x08\x55\x13\x7b\xb2\x71\xb5\x3b\x63\x8d\xc7\x81\x50\xe5\xbf\x23\xef\xa6\xc9\x66\x45\x20\xd9\x00\x3d\x65\xb4\xf3\xde\xd8\x6f\xbe\xe2\xc7\x89\x31\x36\x7d\x83\xaa\x42\xb1\x33\x63\x6f\xae\x5f\xd9\xab\xf2\x2d\xd0\x82\xed\xcc\x14\xbf\x31\x56\x83\xd6\x58\xfc\x1e\x63\x72\x35\x67\x7f\x0f\x31\x4c\x57\xaf\xa1\x8e\x4b\x98\xe2\x77\x15\x70\xca\xb2\xb7\xae\xa3\xb0\x72\x1b\xcb\x18\xbb\x42\x49\x81\xa9\x44\xd8\x9a\x86\x58\x4d\x42\xb5\x13\x63\x36\xed\x89\x8e\x29\xe5\x06\x93\x9d\x99\x2f\x1d\x0b\x62\xac\x83\x03\x0d\x4c\xd3\x87\xc4\x54\xb0\x5f\x5b\x6c\x14\xf6\xd9\x9d\x88\x05\x5d\x16\xe0\x63\x77\x8c\xc7\x45\xa0\x50\x70\x69\xaf\xaf\xc8\x7a\x8f\x11\xc9\x23\xb9\xf5\xee\x7b\x51\xbe\x8e\xad\x70\x9e\x3f\xa0\xd3\xad\x9e\xee\x06\x11\x45\x03\xa6\x1e\xda\x18\xcb\x52\x01\x85\x1f\xed\x45\x0e\x3c\xbd\x58\x49\x25\x50\x65\x77\xae\xcd\xd5\x9e\xdf\xb0\xcf\x6d\xaa\xcf\x66\x6e\x13\xfb\x8e\x29\xa9\x40\x20\x1d\x13\x24\x39\x8e\x03\x49\x3d\x26\x88\xc0\xda\x5e\xf5\x5d\x41\xb1\x19\xe2\x7f\x73\x96\x31\x9b\xc9\xd0\xea\x7e\xb7\xb7\x18\x94\xe2\x0e\x08\x2a\x6c\x90\xf4\x43\x38\x48\xcb\xd9\x85\xa9\x81\xaa\x0c\xd5\xa8\xd4\xa6\x75\x52\x6c\x46\x31\x39\x8b\xc3\xcf\x52\x8f\x21\x3f\x7b\x2f\x8d\xa1\xfa\xa7\xda\x0d\x2b\x30\xaa\x8f\x5e\x0a\x2e\x0a\xe3\xc5\xb4\x37\xb7\xd3\xc1\xb8\x9e\xd1\x5d\xbb\xfd\x74\xdb\x19\x9f\x30\x45\xa6\x74\x51\x67\x35\x07\x3d\xfa\x9f\x44\x0f\x06\x63\x4c\x0a\xee\x40\xdd\xf2\xef\x24\x40\xdd\x12\xfd\xc7\xa7\x45\xfb\x5c\xab\xa3\xfd\xcb\x99\xe7\xc5\x5b\xba\x68\x85\x17\xfc\x7d\x1e\x37\xb2\x2b\xa8\xf3\x9f\x26\xee\x20\x09\x0b\x96\x06\xca\xaa\xb6\xf3\xb5\xf6\xea\xf8\x6b\x85\x92\x49\x43\x83\xb7\x22\x2c\x97\x48\xc4\x41\x80\x93\xf5\x39\xf6\x47\xe5\x05\x52\x2c\xcf\x88\x23\xfa\x02\xe9\x9b\x9b\x23\x8b\x0a\x53\x1a\xb9\x9a\x3d\x2a\x84\xfa\x9f\x0d\x5d\xbf\xa5\x4e\xe9\xc4\xf2\x9a\x99\x6c\x26\x3f\x03\x00\x00\xff\xff\x87\xac\x86\x2c\x57\x09\x00\x00")

func v1alphaExtractorExtractorSwaggerJsonBytes() ([]byte, error) {
	return bindataRead(
		_v1alphaExtractorExtractorSwaggerJson,
		"v1alpha/extractor/extractor.swagger.json",
	)
}

func v1alphaExtractorExtractorSwaggerJson() (*asset, error) {
	bytes, err := v1alphaExtractorExtractorSwaggerJsonBytes()
	if err != nil {
		return nil, err
	}

	info := bindataFileInfo{name: "v1alpha/extractor/extractor.swagger.json", size: 2391, mode: os.FileMode(420), modTime: time.Unix(1593753409, 0)}
	a := &asset{bytes: bytes, info: info}
	return a, nil
}

var _v1alphaSchemaSchemaSwaggerJson = []byte("\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\xff\xa4\x93\xc1\x6e\xfa\x30\x0c\xc6\xef\x7d\x0a\x2b\xff\xff\x11\xd1\x8d\xdd\xb8\xed\xb0\xa7\x98\x26\x14\x5a\xb7\x18\xb5\x49\x64\xbb\x4c\x15\xea\xbb\x4f\x29\x1d\x04\x44\x05\xd2\x4e\xa9\xec\xdf\xf7\x39\x5f\xeb\x1e\x33\x00\x23\xdf\xb6\xae\x91\xcd\x1a\xcc\x6a\xf9\x62\x16\xb1\x46\xae\xf2\x66\x0d\xb1\x0f\x60\x94\xb4\xc1\xd8\x2f\x31\x48\xd1\xf8\xae\xdc\xd8\x40\xf9\xe1\xd5\x36\x61\x67\x73\x29\x76\xd8\xfe\x1e\xcb\xc0\x5e\xfd\xe8\x02\x60\x0e\xc8\x42\xde\x45\xed\xf4\x08\xce\x2b\x08\xaa\xc9\x00\x86\x71\x56\xe1\x9d\x74\x2d\x8a\x59\xc3\xe7\x49\x65\x43\x68\xa8\xb0\x4a\xde\xe5\x7b\xf1\x2e\xb2\x5f\x23\x1b\xd8\x97\x5d\xf1\x24\x6b\x75\x17\xc1\xe3\x69\x4c\x89\x15\x39\x8a\x9c\x5c\x92\x8d\x97\xdd\x76\xd5\xbb\xeb\xcf\xc5\x18\xb8\x0f\x63\x5e\xbf\xdd\x63\xa1\x53\x98\x13\x1e\x90\x95\x50\x12\x7a\xe2\x37\x1d\x37\x57\xd5\xc4\x47\x94\xc9\xd5\xe6\xdc\x1a\x16\x17\xed\xc1\x36\x1d\x3e\x10\x2e\xd2\x5e\xe5\xb9\xb5\x1a\xbb\xdb\x5e\x31\x31\xcd\xd2\x73\x1a\x61\xb8\x73\x4a\x2d\x7e\x30\x7b\xfe\x4b\x44\xbc\x31\x78\x3a\x5f\xe1\xcb\xd9\x78\xe4\x14\xe3\xea\xcd\xe4\x23\xa7\x6f\xab\xfb\xae\x2d\x8a\xd8\xfa\xd1\x7b\xbb\x2b\x2d\x51\x2d\x35\x32\x27\xb5\xcc\xb6\xbf\xbe\x11\x29\xb6\xb7\x3c\x80\xf9\xcf\x58\x45\xc5\xbf\x3c\xd9\xad\x3c\x5d\xa9\x84\x1f\xe6\xbe\x53\xfc\x0f\xb2\x21\xfb\x09\x00\x00\xff\xff\x9b\xfc\xdd\x16\x8b\x03\x00\x00")

func v1alphaSchemaSchemaSwaggerJsonBytes() ([]byte, error) {
	return bindataRead(
		_v1alphaSchemaSchemaSwaggerJson,
		"v1alpha/schema/schema.swagger.json",
	)
}

func v1alphaSchemaSchemaSwaggerJson() (*asset, error) {
	bytes, err := v1alphaSchemaSchemaSwaggerJsonBytes()
	if err != nil {
		return nil, err
	}

	info := bindataFileInfo{name: "v1alpha/schema/schema.swagger.json", size: 907, mode: os.FileMode(420), modTime: time.Unix(1593753409, 0)}
	a := &asset{bytes: bytes, info: info}
	return a, nil
}

var _v1alphaDepsDepsSwaggerJson = []byte("\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\xff\xa4\x93\xc1\x6e\x82\x40\x10\x86\xef\x3c\xc5\x64\xdb\xa3\x91\xd6\xde\xbc\xf5\xd0\xa7\x68\x1a\xb3\xc2\x80\x63\x60\x67\x33\x3b\xd8\x10\xc3\xbb\x37\x8b\x44\x57\x23\xd1\xa4\x17\x20\x33\xdf\xff\xcf\xfe\x30\x1c\x33\x00\x13\x7e\x6d\x5d\xa3\x98\x35\x98\xd5\xf2\xcd\x2c\x62\x8d\x5c\xc5\x66\x0d\xb1\x0f\x60\x94\xb4\xc1\xd8\x2f\xd1\x87\xa2\xe1\xae\xdc\x58\x4f\xf9\xe1\xdd\x36\x7e\x67\xf3\x58\x1d\x2f\x4b\x2f\xac\x3c\x3a\x00\x98\x03\x4a\x20\x76\x51\x37\x3d\x82\x63\x85\x80\x6a\x32\x80\x61\x9c\x53\xb0\x0b\x5d\x8b\xc1\xac\xe1\xfb\xa4\xb2\xde\x37\x54\x58\x25\x76\xf9\x3e\xb0\x8b\xec\xcf\xc8\x7a\xe1\xb2\x2b\x9e\x64\xad\xee\x22\x78\x3c\x8d\x29\xb1\x22\x47\x91\x0b\x97\x54\xe3\x61\xb7\x5d\xf5\xe9\xfa\x73\x31\x86\xed\xfd\x98\x95\xb7\x7b\x2c\x74\x0a\x73\xc2\x3d\x8a\x12\x86\x84\x9e\xf8\x4d\x27\xcd\x55\x35\xf1\x09\x2a\xe4\x6a\x73\x6e\x0d\x8b\x8b\xf6\x60\x9b\x0e\x1f\x08\x17\x69\xaf\x62\x69\xad\xc6\xee\xb6\x57\x4c\x4c\xb3\xf4\x3e\x8d\x30\xd2\x39\xa5\x16\xbf\x44\x58\xfe\x13\x11\x6f\x0c\x9e\xce\x57\x70\x39\x1b\x8f\x9c\x62\x5c\xbb\x99\x7c\xe4\xf4\x63\x75\xdf\xb5\xc5\x10\x6c\xfd\xe8\xbd\xdd\x95\x96\xa8\x96\x9a\x30\x27\xb5\x22\xb6\xbf\x3e\x11\x29\xb6\xb7\x3c\x80\x79\x15\xac\xa2\xe2\x25\x4f\x76\x2b\x4f\x57\x2a\xe1\x87\xb9\xef\x14\xff\x83\x6c\xc8\xfe\x02\x00\x00\xff\xff\xa6\xcd\x5e\xf0\x87\x03\x00\x00")

func v1alphaDepsDepsSwaggerJsonBytes() ([]byte, error) {
	return bindataRead(
		_v1alphaDepsDepsSwaggerJson,
		"v1alpha/deps/deps.swagger.json",
	)
}

func v1alphaDepsDepsSwaggerJson() (*asset, error) {
	bytes, err := v1alphaDepsDepsSwaggerJsonBytes()
	if err != nil {
		return nil, err
	}

	info := bindataFileInfo{name: "v1alpha/deps/deps.swagger.json", size: 903, mode: os.FileMode(420), modTime: time.Unix(1593753410, 0)}
	a := &asset{bytes: bytes, info: info}
	return a, nil
}

var _v1alphaStoreStoreSwaggerJson = []byte("\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\xff\xb4\x55\x41\x6f\xdb\x3c\x0c\xbd\xfb\x57\x08\xfa\xbe\x63\xd0\xac\xe9\x2d\xb7\x02\xed\x86\x0d\xc3\x56\x74\x03\x76\x18\x8a\x42\xb1\x68\x47\x9d\x2d\x09\x14\x95\x21\x28\xfc\xdf\x07\xc9\x89\xab\xa6\x76\xe3\x20\xc9\x25\x09\xc4\xf7\x1e\xf9\x44\x8a\x79\xce\x18\xe3\xee\xaf\x28\x4b\x40\x3e\x67\x7c\x76\xf1\x81\x4f\xc2\x99\xd2\x85\xe1\x73\x16\xe2\x8c\x71\x52\x54\x41\x88\x4b\xb0\x2e\xaf\x8c\x97\x8f\xc2\xaa\xe9\xea\x52\x54\x76\x29\xa6\x8e\x0c\x42\xfb\x79\x61\xd1\x90\x89\x1a\x8c\xf1\x15\xa0\x53\x46\x07\xe6\xe6\x27\xd3\x86\x98\x03\xe2\x19\x63\x4d\xcc\x94\x1b\xed\x7c\x0d\x8e\xcf\xd9\xef\x96\x25\xac\xad\x54\x2e\x48\x19\x3d\x7d\x72\x46\x07\xec\x43\xc4\x5a\x34\xd2\xe7\x23\xb1\x82\x96\x01\xf8\xdc\xa6\x91\x50\x28\xad\x02\xce\xbd\xf8\x8a\xc5\x2e\x7c\x71\xad\xd7\xdd\x61\xb0\xbb\xb6\xd1\xad\x59\x3c\x41\x4e\x1b\x33\x2d\xdc\x02\x92\x02\x97\xa0\x37\xf8\x47\x8f\xd5\xab\xd3\x44\xc7\x11\x2a\x5d\xf2\x2e\xd4\x4c\x5e\xb8\x2b\x51\x79\xd8\x43\x9c\xa4\xb1\xc2\x60\x2d\x28\x44\x17\x6b\x82\x44\x34\x4b\xbf\x37\x29\x38\x7a\x4d\xaa\x86\x5b\x44\x83\xc7\x58\x84\x1d\x81\xd1\xfe\x72\x23\x07\xed\x29\x4d\x10\x06\x6f\xc0\x9f\xd2\x74\x35\xeb\x57\xad\xc1\x39\x51\xee\xbb\xb7\x5e\xaa\x04\x12\xaa\x72\x43\x54\x81\x28\xd6\xaf\x2b\x52\x04\xf5\x2e\x9e\x31\xfe\x3f\x42\x11\x18\xff\x4d\x93\xd9\x9a\xa6\x23\x95\xe0\x9b\x3d\x7d\x8a\x8f\xe7\x06\x2a\x20\xb8\x07\x67\x8d\x76\xf0\x4e\xbb\xde\x52\x3f\x2a\x2d\x47\x10\xf7\xf6\xd9\x0a\x85\x67\xbb\x9b\x58\xe9\x27\x14\x76\xf9\x99\xa0\xbe\x13\x0a\x0f\xbe\xa2\x8e\x7d\x8c\xc9\x72\x2b\xf2\xb3\x25\x1e\x3c\x43\x7f\x2e\x4f\xf2\x62\x53\xc5\xd9\xc9\x15\xaf\x4e\xad\x08\x3a\x37\x32\x30\x77\x74\xc7\x34\xfb\x76\xcb\xed\x55\xee\x1a\x72\x23\x48\x9c\x6f\x19\x0e\x94\xd4\x33\x49\x3b\xb9\x38\x68\x5f\x77\x7f\x3a\xf1\xe4\xfe\xfa\x57\x52\x0a\xff\xf2\xe3\xfb\xb7\x6d\xfa\x87\x8e\x26\xa1\x10\xbe\x8a\xf5\x05\xfc\x3b\xc5\xc4\xc7\x70\xcc\x7e\x96\x6f\xb7\xe1\x98\xbe\xf4\xf7\x43\xf7\x2c\xed\x03\xd5\x86\x1b\xf0\x55\x39\x3a\xc5\xaa\xea\x5b\x3d\x67\x5a\x55\x07\xaf\xa9\x3b\x3f\xc6\x62\xb6\x65\x37\x59\x93\xfd\x0b\x00\x00\xff\xff\x74\x37\xef\xc2\x8b\x09\x00\x00")

func v1alphaStoreStoreSwaggerJsonBytes() ([]byte, error) {
	return bindataRead(
		_v1alphaStoreStoreSwaggerJson,
		"v1alpha/store/store.swagger.json",
	)
}

func v1alphaStoreStoreSwaggerJson() (*asset, error) {
	bytes, err := v1alphaStoreStoreSwaggerJsonBytes()
	if err != nil {
		return nil, err
	}

	info := bindataFileInfo{name: "v1alpha/store/store.swagger.json", size: 2443, mode: os.FileMode(420), modTime: time.Unix(1593753410, 0)}
	a := &asset{bytes: bytes, info: info}
	return a, nil
}

// Asset loads and returns the asset for the given name.
// It returns an error if the asset could not be found or
// could not be loaded.
func Asset(name string) ([]byte, error) {
	canonicalName := strings.Replace(name, "\\", "/", -1)
	if f, ok := _bindata[canonicalName]; ok {
		a, err := f()
		if err != nil {
			return nil, fmt.Errorf("Asset %s can't read by error: %v", name, err)
		}
		return a.bytes, nil
	}
	return nil, fmt.Errorf("Asset %s not found", name)
}

// MustAsset is like Asset but panics when Asset would return an error.
// It simplifies safe initialization of global variables.
func MustAsset(name string) []byte {
	a, err := Asset(name)
	if err != nil {
		panic("asset: Asset(" + name + "): " + err.Error())
	}

	return a
}

// AssetInfo loads and returns the asset info for the given name.
// It returns an error if the asset could not be found or
// could not be loaded.
func AssetInfo(name string) (os.FileInfo, error) {
	canonicalName := strings.Replace(name, "\\", "/", -1)
	if f, ok := _bindata[canonicalName]; ok {
		a, err := f()
		if err != nil {
			return nil, fmt.Errorf("AssetInfo %s can't read by error: %v", name, err)
		}
		return a.info, nil
	}
	return nil, fmt.Errorf("AssetInfo %s not found", name)
}

// AssetNames returns the names of the assets.
func AssetNames() []string {
	names := make([]string, 0, len(_bindata))
	for name := range _bindata {
		names = append(names, name)
	}
	return names
}

// _bindata is a table, holding each asset generator, mapped to its name.
var _bindata = map[string]func() (*asset, error){
	"v1alpha/tracker/tracker.swagger.json":     v1alphaTrackerTrackerSwaggerJson,
	"v1alpha/extractor/extractor.swagger.json": v1alphaExtractorExtractorSwaggerJson,
	"v1alpha/schema/schema.swagger.json":       v1alphaSchemaSchemaSwaggerJson,
	"v1alpha/deps/deps.swagger.json":           v1alphaDepsDepsSwaggerJson,
	"v1alpha/store/store.swagger.json":         v1alphaStoreStoreSwaggerJson,
}

// AssetDir returns the file names below a certain
// directory embedded in the file by go-bindata.
// For example if you run go-bindata on data/... and data contains the
// following hierarchy:
//     data/
//       foo.txt
//       img/
//         a.png
//         b.png
// then AssetDir("data") would return []string{"foo.txt", "img"}
// AssetDir("data/img") would return []string{"a.png", "b.png"}
// AssetDir("foo.txt") and AssetDir("nonexistent") would return an error
// AssetDir("") will return []string{"data"}.
func AssetDir(name string) ([]string, error) {
	node := _bintree
	if len(name) != 0 {
		canonicalName := strings.Replace(name, "\\", "/", -1)
		pathList := strings.Split(canonicalName, "/")
		for _, p := range pathList {
			node = node.Children[p]
			if node == nil {
				return nil, fmt.Errorf("Asset %s not found", name)
			}
		}
	}
	if node.Func != nil {
		return nil, fmt.Errorf("Asset %s not found", name)
	}
	rv := make([]string, 0, len(node.Children))
	for childName := range node.Children {
		rv = append(rv, childName)
	}
	return rv, nil
}

type bintree struct {
	Func     func() (*asset, error)
	Children map[string]*bintree
}

var _bintree = &bintree{nil, map[string]*bintree{
	"v1alpha": &bintree{nil, map[string]*bintree{
		"deps": &bintree{nil, map[string]*bintree{
			"deps.swagger.json": &bintree{v1alphaDepsDepsSwaggerJson, map[string]*bintree{}},
		}},
		"extractor": &bintree{nil, map[string]*bintree{
			"extractor.swagger.json": &bintree{v1alphaExtractorExtractorSwaggerJson, map[string]*bintree{}},
		}},
		"schema": &bintree{nil, map[string]*bintree{
			"schema.swagger.json": &bintree{v1alphaSchemaSchemaSwaggerJson, map[string]*bintree{}},
		}},
		"store": &bintree{nil, map[string]*bintree{
			"store.swagger.json": &bintree{v1alphaStoreStoreSwaggerJson, map[string]*bintree{}},
		}},
		"tracker": &bintree{nil, map[string]*bintree{
			"tracker.swagger.json": &bintree{v1alphaTrackerTrackerSwaggerJson, map[string]*bintree{}},
		}},
	}},
}}

// RestoreAsset restores an asset under the given directory
func RestoreAsset(dir, name string) error {
	data, err := Asset(name)
	if err != nil {
		return err
	}
	info, err := AssetInfo(name)
	if err != nil {
		return err
	}
	err = os.MkdirAll(_filePath(dir, filepath.Dir(name)), os.FileMode(0755))
	if err != nil {
		return err
	}
	err = ioutil.WriteFile(_filePath(dir, name), data, info.Mode())
	if err != nil {
		return err
	}
	err = os.Chtimes(_filePath(dir, name), info.ModTime(), info.ModTime())
	if err != nil {
		return err
	}
	return nil
}

// RestoreAssets restores an asset under the given directory recursively
func RestoreAssets(dir, name string) error {
	children, err := AssetDir(name)
	// File
	if err != nil {
		return RestoreAsset(dir, name)
	}
	// Dir
	for _, child := range children {
		err = RestoreAssets(dir, filepath.Join(name, child))
		if err != nil {
			return err
		}
	}
	return nil
}

func _filePath(dir, name string) string {
	canonicalName := strings.Replace(name, "\\", "/", -1)
	return filepath.Join(append([]string{dir}, strings.Split(canonicalName, "/")...)...)
}
