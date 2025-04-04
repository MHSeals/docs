# Documentation
this repository hosts all the documentation regarding computer science

## How to contribute
First, clone the repository:
```
git clone https://github.com/MHSeals/docs.git
```
Now install MkDocs along with the "Ivory" theme:
```
pip install mkdocs
pip install mkdocs-ivory
```
Finally, launch the live server that will update automatically as you make/save changes:
```
mkdocs serve
```
Once you're done editing, build the website and push it onto the gh-pages branch.
```
mkdocs build
cd site
mkdocs gh-deploy
```
