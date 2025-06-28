""" python deps for this project """


install_requires: list[str] = [
    "redis",
    "pylogconf",
]
build_requires: list[str] = [
    "pydmt",
    "pymakehelper",
]
test_requires: list[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "mypy",
    # types
]
requires = install_requires + build_requires + test_requires
