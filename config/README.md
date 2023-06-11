```
conda create --name csf python=3.10
activate csf
python --version
pip --version
```

```
activate csf
mkdir csf-report
cd csf-report
git init
type nul > .gitignore
mkdir config
type nul > .\config\.gitkeep
type nul > .\config\README.md
conda env export > .\config\environment.yml
```

```
git config alias.czf "cz --name=cz_fogoprobr commit"
git config alias.l "log --oneline"
git config alias.s "status"
git config --local --list
```

```
pip install python-dotenv
```