rem clear dist dir
rmdir /S /Q dist\windows
mkdir dist\windows

rem build dist
rem TODO: make portable?
pyinstaller -D --distpath dist\windows windows.spec 

rem copy additional files

rem help
mkdir dist\windows\help
copy help\*.html dist\windows\help
copy help\*.css dist\windows\help
mkdir dist\windows\help\img
copy help\img\*.png dist\windows\help\img

rem license
copy LICENSE dist\windows\LICENSE.txt

rem icon
copy res\icons\lokkat.ico dist\windows