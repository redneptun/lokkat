rem  make the dist
call make_dist_windows.bat

rem  remove the archive
erase pak\windows\packages\net.redneptun.lokkat\data\lokkat.7z

rem  zip the dist
cd dist\windows\ 
..\..\tools\win\QtIFW-3.1.1\bin\archivegen.exe ^
..\..\pak\windows\packages\net.redneptun.lokkat\data\lokkat.7z *
cd ..\..

rem  build the installer
cd pak\windows\ 
..\..\tools\win\QtIFW-3.1.1\bin\binarycreator.exe -c config\config.xml ^
-p packages Lokkat-0.5-Installer.exe
cd ..\..
