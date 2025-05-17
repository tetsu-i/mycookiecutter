# {{cookiecutter.project_name}}

# Getting started

## Git
```
git init
git add .
git commit -m "first commit"
```

## uv 

### install
https://docs.astral.sh/uv/

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```bash
uv sync
```

## pre-commit

```bash
uv pre-commit install
```

# Usage

## uv

```bash
# install dependencies
uv sync 
```

```bash
uv add <dependency> 

uv add <dependency> --dev

uv remove <dependency> 
```

```bash
# install python 
uv python install 

uv run <your_script.py>

uv run -m <module>
```

## run package

```bash
# run package
uv run <package> <args>

# examples
uv run mypy .
uv run pytest .
uv run deptry .
```