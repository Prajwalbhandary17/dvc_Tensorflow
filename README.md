# DVC -DL MLOPS

## commands

### create new env

```bash
conda create --prefix python=3.7 -y
```

### init initialize
```bash
git init
dvc init
```

### create empty files

```bash
mkdir -p src/utils config
touch src/__init__.py src/utils/__init__.py param.yaml dvc.yaml config/config.yaml src/stage_01_load_save.py src/utils/all_utils.py setup.py .gitignore

```

### install src
```bash
pip install -e .
```
