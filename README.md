# Lokkat
Easy One-Time Pad encryption for everyone.

## Using Lokkat
If you want to use Lokkat you have two choices: either downloading and running a binary or downloading the source code running it that way. Lokkat does not have to compiled as it is written in Python.

If you would like to know how to **use** Lokkat, let me recommend the user manual: it can be found [here](http://htmlpreview.github.io/?https://github.com/redneptun/lokkat/blob/master/help/user_manual_en.html) in English and [here](http://htmlpreview.github.io/?https://github.com/redneptun/lokkat/blob/master/help/user_manual_de.html) in German. This user manual is also available from within the application by pressing **F1**.

### Run Lokkat using prepared binaries
You can download binaries for Lokkat [here](http://redneptun.net/lokkat/download_en.html).

There are an installer and a ZIP for MS Windows 7+ and a .deb package for any GNU/Linux distro that can handle those.

### Run Lokkat using the source code
You can clone this repository and run either:

- `run.sh` if you are on GNU/Linux
- `run.bat` if you are on Windows

## Developing Lokkat
Setting up a development environment for Lokkat is easy. Just follow these instructions.

### Requirements

- **GNU/Linux**: Lokkat was developed on a GNU/Linux machine. While Python as well as Qt and its tools are avaiable on Windows as well you are probably going to have a much easier time using a GNU/Linux machine as well.

- **Qt5 toolset**: Lokkat's GUI was built using Qt5. You can download it [here](https://doc.qt.io/qt-5/gettingstarted.html). You are specifically going to need these tools:
  - *Qt Creator/Designer*: Those were used to build the GUI. The files to use it with are `gui/*.ui`
  - *Qt Linguist*: This tool was used to create the translation from German to English. Should you want to add further language support or localize some new strings you put into the UI, I suggest you use this. It's pretty good! It was used for `res/l10n/*.ts`
  - *lupdate*: This command line tool is used to update the aforementioned `.ts` files by using it on the `gui/*.ui` files. It checks for any new strings in your UI and puts them into TS file to be localized using the Qt Linguist tool
  - *lrelease*: This command line is used to convert the prepared `.ts` files into `.qm` files which can then be packaged using Qt's resource system

- **Wine 4+**: If you want to build Lokkat distributables for Windows using GNU/Linux you are going to need this. You can get it [here](https://www.winehq.org/).

### Recommendations

- **IDE**: As Lokkat is mostly written in Python, I suggest using an IDE suitable for the job. I used PyCharm in combination with various editors. I can hardly say I endorse it but it works.

### Developer Documentation

This is not the only README of Lokkat. In its various subdirectories you are going to find more READMEs to provide you with more info on the specific contents and purpose of those subdirectories.

### Where to start?

I suggest these steps:

1. Clone the source code
2. Download and install the [requirements](https://github.com/redneptun/lokkat#requirements) you need for your platform
3. Read the this README in full
4. Choose an IDE
5. Open the project inside the IDE and try to get it to run
6. If it runs: get to work with whatever you were planning ;-P
7. If it doesn't: find the problem
  - See if somebody already had the same problem
  - Maybe opening a new [issue](https://github.com/redneptun/lokkat/issues) can get you some help
  - Find a solution and document it here ;-)

#### The project root

Here are is some general information about the project root and its structure:

- **config/**: contains the code for loading/saving the configuration file of Lokkat
- **crypt/**: contains the code for encrypting the data and retrieving random data from external sources
- **dist**: only exists after you first build of distributables (either for Windows or GNU/Linux); contains executables of Lokkat
- **etc/**: contains stuff that did not fit anywhere else
- **gui/**: contains the Qt GUI design files, their Python counterparts as well as all of the code of UI in general
- **help/**: contains the user manual and its images
- **pak/**: contains packages/installers and information to build packages for Windows and GNU/Linux
- **res/**: contains all kinds of resources
- **tools/**: contains development tools for building distributables for Windows and GNU/Linux
- **venv/**: contains a virtual Python 3.7 environment for development purposes
- *LICENSE*: is the GNU GPL v3 license
- *README.md*: is the file you are currently reading
- *TODO*: contains some planned features and known bugs
- *gnu_linux.spec*: this file specifies how [Pyinstaller](https://www.pyinstaller.org/) should build the distributable for GNU/Linux
- *lokkat.py*: **THIS IS THE MAIN ENTRY POINT OF THE APPLICATION**
- *make_dist_gnu_linux*: a shell script to build a distributable for GNU/Linux. Intended to be used on a GNU/Linux machine.
- *make_dist_windows*: a shell script to build a distributable `.EXE` for Windows. Intended to be used on a GNU/Linux machine. *Yes, you can build executable files for Windows on a GNU/Linux system using PyInstaller, but you are going to need [Wine](https://www.winehq.org/).*s
- *make_dist_windows.bat*: a batch script to build a distributable `.EXE` for Windows. Intended to be used on a Windows system.
- *make_pak_windows*: creates an installer for Windows using the Qt Installer Framework. Intended to be used on a GNU/Linux system utilizing Wine.
- *make_pak_windows.bat*: just the same as the shell script for GNU/Linux but intended to be used from a Windows system instead
- *qtedit*: a convencience shell script to be used during UI design.
  - Opens a .ui file in the Qt-Designer. After that, runs `lupdate` to update the `.ts` translations file and opens the `.ts` files for this UI files in Qt Linguist for you to provide localization for potential new strings. When you close the Linguist application afterwards the `.ts` files are automatically converted into `.qm` binary files to be used by the Qt resource system. After that the resources file is rebuilt.
  - As you can see this convenience script can save you a lot of time when patching UIs in Qt. If you are not familiar with all the tools involved, I recommend doing it all step by step manually first and taking a look with an editor at what the script is doing.
  - Usage example: `./qtedit gui/gui.ui`
- *run.bat*: runs Lokkat on Windows from source
- *run.sh*: runs Lokkat on GNU/Linux from source
- *windows.spec*: this file specifies how [Pyinstaller](https://www.pyinstaller.org/) should build the distributable for Windows

# Postface

Lokkat's initial development was guided by the ambition to give a free/libre software tool to the public to utilize the [One-time pad encryption](https://en.wikipedia.org/wiki/One-time_pad). Its main design goals were:

- Ease of use
- Security
- Education

Please keep this in mind when contributing. Thank you.