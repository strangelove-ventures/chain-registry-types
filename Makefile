ASSETLIST_SCHEMA_URL := https://raw.githubusercontent.com/cosmos/chain-registry/master/assetlist.schema.json
CHAIN_SCHEMA_URL := https://raw.githubusercontent.com/cosmos/chain-registry/master/chain.schema.json
IBC_DATA_SCHEMA_URL := https://raw.githubusercontent.com/cosmos/chain-registry/master/ibc_data.schema.json

prepare:
	yarn install
	mkdir -p dist/{golang,python,rust,typescript}/

build:
	./node_modules/.bin/quicktype $(ASSETLIST_SCHEMA_URL) --alphabetize-properties --out dist/golang/assetlist.go & \
		./node_modules/.bin/quicktype $(ASSETLIST_SCHEMA_URL) --alphabetize-properties --out dist/python/assetlist.py & \
		./node_modules/.bin/quicktype $(ASSETLIST_SCHEMA_URL) --alphabetize-properties --out dist/rust/assetlist.rs & \
		./node_modules/.bin/quicktype $(ASSETLIST_SCHEMA_URL) --alphabetize-properties --out dist/typescript/assetlist.ts & \
		./node_modules/.bin/quicktype $(CHAIN_SCHEMA_URL) --alphabetize-properties --out dist/golang/chain.go & \
		./node_modules/.bin/quicktype $(CHAIN_SCHEMA_URL) --alphabetize-properties --out dist/python/chain.py & \
		./node_modules/.bin/quicktype $(CHAIN_SCHEMA_URL) --alphabetize-properties --out dist/rust/chain.rs & \
		./node_modules/.bin/quicktype $(CHAIN_SCHEMA_URL) --alphabetize-properties --out dist/typescript/chain.ts & \
		./node_modules/.bin/quicktype $(IBC_DATA_SCHEMA_URL) --alphabetize-properties --out dist/golang/ibc_data.go & \
		./node_modules/.bin/quicktype $(IBC_DATA_SCHEMA_URL) --alphabetize-properties --out dist/python/ibc_data.py & \
		./node_modules/.bin/quicktype $(IBC_DATA_SCHEMA_URL) --alphabetize-properties --out dist/rust/ibc_data.rs & \
		./node_modules/.bin/quicktype $(IBC_DATA_SCHEMA_URL) --alphabetize-properties --out dist/typescript/ibc_data.ts & \
		wait

clean:
	rm -rf dist/**/*
