# Changelog

All notable changes to this project will be documented in this file.

## [6.0.2] - 2026-11-02

### 🐛 Bug Fixes

- Module imports for library


## [6.0.1] - 2026-11-02

### 🐛 Bug Fixes

- *(build)* Map src.core to libname for library


## [6.0.0] - 2026-11-02

### 🐛 Bug Fixes

- [**breaking**] Dependency groups
  - Moved api and cli dependencies to separate groups

## [5.3.0] - 2025-09-30

### 🚀 Features

- Update pyproject.toml to make calculator runnable


- More maskfile utils


- Multiple runnable CLIs
  - installing this project now gives you 2 runnable CLIs -- `greeter` and `calculator`.

### 📚 Documentation

- Update


## [5.2.1] - 2025-09-25

### 🐛 Bug Fixes

- *(flake)* ShellHook shows outputs then clears


## [5.2.0] - 2025-09-25

### 🚀 Features

- *(flake)* Simplify flake and use stable nixpkgs


## [5.1.0] - 2025-07-02

### 🚀 Features

- Added example env with pycache env var


### 🐛 Bug Fixes

- Pre-commit


- Pre-commit again
  - Manually specifying the stage for each hook

- Pre-commit again again
  - I do want mypy and ruff to run before push

- *(build)* Docs bump truncates project version to major.minor


### 📚 Documentation

- Switched readme and symlink


## [5.0.1] - 2025-06-02

### 🐛 Bug Fixes

- *(changelog)* Only show breaking description if it's different to the commit message


## [5.0.0] - 2025-06-02

### 🐛 Bug Fixes

- [**breaking**] Added space (#7)
  - * fix: added the space
  - **BREAKING CHANGE:** the space is back  * style: formatting 
## [4.0.0] - 2025-06-02

### 🚀 Features

- [**breaking**] Removed a space (#6)


## [3.0.0] - 2025-06-02

### 🚀 Features

- [**breaking**] Commit message
  - foo bar bar
  - **BREAKING CHANGE:** description of the breaking change 
- [**breaking**] Only commit message


- [**breaking**] Commit message without bang

  - **BREAKING CHANGE:** only breaking description 
### 🐛 Bug Fixes

- *(changelog)* Trying again


- *(changelog)* Again


## [2.0.1] - 2025-06-02

### 🐛 Bug Fixes

- *(changelog)* Only display breaking change description if it exists


## [2.0.0] - 2025-06-02

### 🚀 Features

- *(github)* Github action to check PR title (#2)
  - * feat(github): github action to check PR title  * fix(github): fiddling

- Pr template (#3)
  - * feat: added pull request template  * fix: pr template

- [**breaking**] Added breaking change to pr template (#5)


### 🐛 Bug Fixes

- *(github)* Remove double pr lint trigger (#4)


## [1.3.1] - 2025-06-02

### 🐛 Bug Fixes

- Build script (#1)
  - * fix: build script  * fix: build script again

## [1.3.0] - 2025-06-02

### 🚀 Features

- *(docs)* Linked to online docs


## [1.2.2] - 2025-06-02

### 🐛 Bug Fixes

- *(build)* Always remove the dist folder


## [1.2.1] - 2025-06-02

### 🐛 Bug Fixes

- *(build)* Release script


## [1.2.0] - 2025-06-01

### 🚀 Features

- *(docs)* Added maskfile to docs


## [1.1.2] - 2025-06-01

### 🐛 Bug Fixes

- *(build)* Fixed docs bump command
  - This should work even on a clean project with no "latest" version alias

## [1.1.1] - 2025-06-01

### 🐛 Bug Fixes

- *(changelog)* Wrap breaking changes lines


- *(build)* Tweak extensions and git hooks


- *(build)* Ruff config


### 🎨 Styling

- Comment


## [1.1.0] - 2025-05-31

### 🚀 Features

- *(docs)* Added a comment
  - I only added a comment but I want a really long commit body with multiple lines to see how that will look in the changelog. This is the third line now. They should be joined in the changelog.

### 🐛 Bug Fixes

- *(changelog)* Add more detail in git cliff template


- *(changelog)* Wrap multi-line commit body


## [1.0.0] - 2025-05-31

### 🚀 Features

- *(maskfile)* [**breaking**] Removed a space
  - foo bar basadiofj asodijf asodifj asdoifj asdofi asdoif jasdoifjaso idjfaos difja sdfoaisdjfa osdifjasdoifj
  - **BREAKING CHANGE:** Not really a breaking change but I just want to test how this will look in the changelog 
## [0.9.3] - 2025-05-31

### 🐛 Bug Fixes

- *(build)* Commitizen should no longer build changelog
  - Hopefully this works now

- *(build)* Maskfile
  - I was pointing git-cliff to the wrong file...

## [0.9.2] - 2025-05-31

### 🐛 Bug Fixes

- *(build)* Removed nonexistent commitizen settings...


- *(build)* Update mask bump command


- *(build)* Update bump command again
  - I've put git-cliff --bump before commitizen. Hopefully the changelog will be included...

## [0.9.1] - 2025-05-31

### 🐛 Bug Fixes

- Formatting in maskfile


### ⚙️ Miscellaneous Tasks

- Fix changelog format


## [0.9.0] - 2025-05-31

### 🚀 Features

- *(build)* Added more examples to maskfile


- *(build)* More maskfile entries


## [0.8.1] - 2025-05-31

### 🐛 Bug Fixes

- *(build)* Commitizen should use git-cliff for changelogs


## [0.8.0] - 2025-05-31

### 🚀 Features

- Parallelised test suite


- *(build)* Added git-cliff for changelog generation


- *(build)* Added maskfile


### 📚 Documentation

- Removed project structure page


- Calculator module docstring


- Added github link


- Change font and logo


- Change logo to python


- Moved explanation up


- Manual/nix sections in Getting Started


- Better link to getting started page


### ⚙️ Miscellaneous Tasks

- Remove demo


## [0.7.0] - 2025-05-22

### 🚀 Features

- *(api)* Brand new feature!!


### 🐛 Bug Fixes

- *(api)* Fix bug


### 📚 Documentation

- Readme


- How to build docs


- Version provider in mkdocs material


- Comment


### 🎨 Styling

- Format


## [0.6.0] - 2025-05-22

### 🚀 Features

- Moved calculator endpoints to separate file and updated docs


## [0.5.0] - 2025-05-22

### 🚀 Features

- Added web API


### 📚 Documentation

- More features


- Remove prerequisites from getting started


- Web api reference


### 🧪 Testing

- Api and cli


## [0.4.0] - 2025-05-19

### 🚀 Features

- Moved cli and core into src folder


### 📚 Documentation

- Bump version


- Mike build docs


- Update


- Configuration


### 🎨 Styling

- Format


## [0.3.2] - 2025-05-18

### 🐛 Bug Fixes

- *(cli)* Added docstring
  - asoi dfjsaoi fjsado fiasdjfo iasdjf asodifj asdoif jasdoifj asdofi ajsdfia sjdfoias djfoiasd jfoasid fjasoid jasodi fjasodif jasdif jasodif jasdoif jasodifj asdfjioasdfjoasdifjaosdifjaso dfa.

## [0.3.1] - 2025-05-18

### 🐛 Bug Fixes

- Remove custom changelog


## [0.3.0] - 2025-05-18

### 🚀 Features

- Custom changelog template


### 📚 Documentation

- Bump version


### ⚙️ Miscellaneous Tasks

- Manually bump core version because toml configured wrong


## [0.2.0] - 2025-05-18

### 🚀 Features

- Added version command


### 📚 Documentation

- Update getting started


<!-- generated by git-cliff -->
