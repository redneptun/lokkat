# Lokkat
Easy One-Time Pad encryption for everyone.

## Using Lokkat
If you want to use Lokkat you have two choices: either download and run a binary or download the source code run it that way. Lokkat does not have to compiled as it is written in Python.

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

### Recommendations

- IDE: As Lokkat is mostly written in Python, I suggest using an IDE suitable for the job. I used PyCharm in combination with various editors. I am not sure if I would exactly recommend it '^^ but you do you.

