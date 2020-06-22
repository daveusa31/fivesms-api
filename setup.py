import os
import setuptools

import fivesms_api

packages = ["fivesms_api"] # Название плагина




if "requirements.txt" in os.listdir("."):
    with open("requirements.txt", encoding="utf-8") as r:
        requires = [i.strip() for i in r] # Зависимости
else:
    requires = []



setuptools.setup(
    name=fivesms_api.name,
    version=fivesms_api.__version__,
    author=fivesms_api.__author__,
    author_email="strelok.127@yandex.ru",
    packages=packages,
    include_package_data=True,
    python_requires=">=3.5",
    install_requires=requires,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: Russian",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    project_urls={"Source": fivesms_api.__source__},
)
