@ECHO OFF

ECHO Getting downloads...
ECHO.


IF EXIST  %USERPROFILE%\Downloads\accounting.xls (

	MOVE %USERPROFILE%\Downloads\accounting.xls %USERPROFILE%\PrinterReporter\reports

	RENAME %USERPROFILE%\PrinterReporter\src\\PrinterReporter\reports\accounting.xls office1.xls
	) ELSE (
	ECHO Please download the Office 1 report
	ECHO.
	PAUSE
	EXIT
	)


IF EXIST %USERPROFILE%\Downloads\"accounting (1)".xls (

	MOVE %USERPROFILE%\Downloads\"accounting (1)".xls %USERPROFILE%\PrinterReporter\reports

	RENAME %USERPROFILE%\PrinterReporter\reports\"accounting (1)".xls office2.xls	

	) ELSE (
	ECHO Please download the Office 2 report
	ECHO.
	PAUSE
	EXIT
	)

ECHO Generating printer reports...
ECHO.

CD %USERPROFILE%\PrinterReporter\src\

python main.py

CD %USERPROFILE%\PrinterReporter\

DEL reports\bar.xls reports\col.xls


ECHO.
ECHO Printer reports finished! find them in the reports folder
ECHO.

PAUSE


