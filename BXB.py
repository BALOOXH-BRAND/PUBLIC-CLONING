import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
