# Template Repository

# 最初にやること

## uv 

### install
https://docs.astral.sh/uv/

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### sync

```bash
# pyproject.tomlの依存関係をインストール
uv sync 
```

```bash
# 新しい依存関係を追加
uv add <dependency> 

# devグループに追加
uv add <dependency> --dev

# 依存関係を削除
uv remove <dependency> 
```

### python

```bash
# .python-versionからインストール
uv python install 
```

```bash
# pythonスクリプトの実行
uv run <your_script.py>
```

```bash
# moduleの実行
uv run -m <module>
```

### packageの実行

```bash
# packageの実行
uv run <package> <args>
```

```bash
# 具体例
uv run mypy .
uv run pytest .
uv run deptry .
```


## pre-commit
### install