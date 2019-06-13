from setuptools import setup, find_packages

setup(
    name='template-repo',
    version=0.0.1,
    packages=find_packages(),
    url='https://github.com/justusschock/template-repo',
    test_suite="unittest",
    long_description="",
    long_description_content_type='text/markdown',
    install_requires=[],
    tests_require=["coverage"],
    python_requires=">=3.5",
)
