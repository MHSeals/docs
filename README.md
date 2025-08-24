# Documentation
This repository hosts all the documentation regarding computer science.

## How to contribute
First, clone the repository:
````bash
git clone https://github.com/MHSeals/docs.git
```
Now install recursively install (through `requirements.txt`) MkDocs along with the "Material" theme and plugins:
```bash
pip install -r requirements.txt
```
Finally, launch the live server that will update automatically as you make/save changes:
````bash
mkdocs serve
```
Once you're done editing, build the website and push it onto the gh-pages branch.
````bash
mkdocs build
mkdocs gh-deploy
```
