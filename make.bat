@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation
REM .\make.ps1 html  ... build only
REM .\make.ps1 preview  ... localhost:8000 preview

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=source
set BUILDDIR=docs

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.https://www.sphinx-doc.org/
	exit /b 1
)

if "%1" == "" goto help

if "%1" == "html" (
	rmdir /s /q %BUILDDIR%
	%SPHINXBUILD% -b html %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
	goto end
)

if "%1" == "clean" (
	rmdir /s /q %BUILDDIR%
	goto end
)

if "%1" == "preview" (
	start http://localhost:8000
	sphinx-autobuild -b html source %BUILDDIR%
	goto end
)

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
