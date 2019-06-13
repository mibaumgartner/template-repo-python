# Python Template Repository

This repository contains a fully-functionable package structure including (empty) tests.

## Customize it!

To customize this repo, you need to have a look at the following chapters.

### Directory-Name
You might want to customize your package-name.

To do this, you simply have to rename the `template-repo` directory to whatever you want.
 > Make sure, to also change it in [line 37 of your setup.py](setup.py#L37), or you won't be able to install your package anymore!

### Python Package Metadata

To customize your python package, you just have to change your `setup.py`.

Currently the important part looks like 
```python
setup(
    name='template_package',
    version=_version,
    packages=find_packages(),
    url='https://github.com/justusschock/template-repo-python',
    test_suite="unittest",
    long_description=readme,
    long_description_content_type='text/markdown',
    install_requires=requirements,
    tests_require=["coverage"],
    python_requires=">=3.5",
    author="Justus Schock",
    author_email="justus.schock@rwth-aachen.de",
    license=license,
)
```
This includes the default information for me and must be adjusted to your needs:

* `name` provides the package-name you can later import
* `version` provides the package-version (which will currently be extracted from your package#s `__init__.py`, but be also set manually)
* `packages` is a list defining all packages (and their sub-packages and the sub-packages of their sub-packages and so on...), that should be installed. This is automatically extracted by `find_packages`, which also accepts some sub-packages to ignore (besides some other arguments).
`url` specifies the packages homepage (in this case the current GitHub repo); You might want to change it to your repos homepage.
* `test_suite` defines the test-suite to use for your unittests. In this repo template, we'll python's built-in framework `unittest`, but you can change this too; *Just make sure to also change this, when we get to CI/CD.*
* `long_description` does what it sayes: It provides a long description of your package. Currently this is parsed from your `README.md`
* `long_description_content_type` defines your description type; I set it to markdown in most cases
* `install_requires` is a list containing all your package requirements. They are automatically parsed from a `requirements.txt` file
* `tests_require` does the same thing for your unittests.
* `python_requires` specifies the python version, your package can be installed to (here it's been set to python 3.5 or above, since this is what I usually use). *Depending on the version you specify here, you might not be able to use all of python's latest features*
* `author` and `author_email` specify who you are.
* `license` specifies the license you want to release your code with. This is parsed from a `LICENSE` file.

There are still many other options to include here, but these are the most basic ones.
