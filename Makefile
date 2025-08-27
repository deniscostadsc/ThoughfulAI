.PHONY: \
	__build-lint \
	__build-test \
	__build-typecheck \
	lint \
	lint-fix \
	test \
	typecheck

__build-lint:
	@docker build -q -f .docker/Dockerfile --target lint -t lint .

__build-test:
	@docker build -q -f .docker/Dockerfile --target test -t test .

__build-typecheck:
	@docker build -q -f .docker/Dockerfile --target typecheck -t typecheck .

lint: __build-lint
	@docker run --rm -v $$(pwd):/code -u "$$(id -u):$$(id -g)" lint

lint-fix: __build-lint
	@docker run --rm -v $$(pwd):/code -u "$$(id -u):$$(id -g)" lint sh -c "ruff check --fix --unsafe-fixes . && ruff format ."

test: __build-test
	@docker run --rm -v $$(pwd):/code -u "$$(id -u):$$(id -g)" test

typecheck: __build-typecheck
	@docker run --rm -v $$(pwd):/code -u "$$(id -u):$$(id -g)" typecheck
