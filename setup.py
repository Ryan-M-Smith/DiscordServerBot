#
# FILENAME: setup.py | DiscordServerBot
# DESCRIPTION: The setup script for DiscordServerBot
# CREATED: 2021-06-12 @ 11:55 PM
# COPYRIGHT: Copyright (c) 2021 by Ryan Smith <rysmith2113@gmail.com>
#

import setuptools, subprocess, os, sys

# Get the software's `pip` requirements
with open("README.md", "r") as ld, open("requirements.txt", "r") as req:
	long_description = ld.read()
	requirements = req.read().split("\n")
	

with open("version.txt", "r") as v:
	version = list(v.read().split("\n"))[0][9:] # Read the version line (first line) only

AUTHOR, EMAIL = "Ryan Smith", "rysmith2113@gmail.com"

setuptools.setup(
	name="DiscordServerBot",
	version=version,
	author=AUTHOR,
	author_email=EMAIL,
	maintainer=AUTHOR,
	maintainer_email=EMAIL,
	description="A voice assistant",
	long_description=long_description, # The README
	long_description_content_type="text/markdown",
	url="https://www.github.com/Ryan-M-Smith/DiscordServerBot",
	
	# This web address directly downloads a zip archive of the project's master branch from GitHub.
	# If you want more download options or wish to clone the repository, see the `url` parameter
	# above or use `python3.9 setup.py --url`.
	download_url="https://www.github.com/Ryan-M-Smith/DiscordServerBot/archive/master.zip",
	
	packages=setuptools.find_packages(),
	license='GNU GPLv3+',
	platforms=["MacOS", "Linux", "Windows"],
	classifiers=[
		"Development Status :: 4 - Beta",
		"Intended Audience :: End Users/Desktop",
		"License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
		"Topic :: Communications",
		"Programming language :: Python :: 3 :: Only",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Operating System :: MacOS :: MacOS X",
		"Operating System :: POSTIX :: Linux",
		"Operating System :: Microsoft :: Windows",
		"Environment :: Console"
	],
	install_requires=requirements,
	python_requires=">=3.6",
	include_package_data=True,
	entry_points={"console_scripts": ["serverbot=src.bot:run"]}
)