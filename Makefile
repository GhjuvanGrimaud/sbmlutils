#################################################################
# Makefile
#################################################################

.PHONY: build help

help:
	@echo "=========================="
	@echo "matthiaskoenig/sbmlutils"
	@echo "=========================="
	@echo
	@grep -E '^[a-zA-Z0-9_%/-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build:
	docker build --no-cache --rm --force-rm -t matthiaskoenig/sbmlutils .

