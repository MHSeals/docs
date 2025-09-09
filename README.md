# Documentation
This repository hosts all the documentation regarding computer science.

## How to contribute
First, clone the repository:
````bash
git clone https://github.com/MHSeals/docs.git
```
Install all dependencies through `requirements.txt` (MkDocs, "Material" theme, and plugins):
```bash
pip install -r requirements.txt
```
> [!TIP]
> If you don't have issues installing Python packages system-wide, install Conda:
> ```bash
> wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh # Fetch the installer
> bash Miniconda3-latest-Linux-x86_64.sh # Run the installer
> rm Miniconda3-latest-Linux-x86_64.sh # Clean up installer
> source ~/.bashrc # Replace with .zshrc or config.fish depending on your shell
> ```
>
> Then, start a virtual environment and run the installation command
> ```bash
> conda create -n "docs"
> conda activate docs
> conda install pip
> pip install -r requirements.txt
> ```

Finally, launch the live server that will update automatically as you make/save changes:
````bash
mkdocs serve
```

Once you're done editing, build the website and push it onto the gh-pages branch.
````bash
mkdocs build
mkdocs gh-deploy
```
