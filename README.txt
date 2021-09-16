	* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
	*       ______   ______     __     __   __     ______   ______     ______             *
	*      /\  == \ /\  == \   /\ \   /\ "-.\ \   /\__  _\ /\  ___\   /\  == \            *
	*      \ \  _-/ \ \  __<   \ \ \  \ \ \-.  \  \/_/\ \/ \ \  __\   \ \  __<            *
	*       \ \_\    \ \_\ \_\  \ \_\  \ \_\\"\_\    \ \_\  \ \_____\  \ \_\ \_\          *
	*        \/_/     \/_/ /_/   \/_/   \/_/ \/_/     \/_/   \/_____/   \/_/ /_/          *
	*  ______     ______     ______   ______     ______     ______   ______     ______    *
	* /\  == \   /\  ___\   /\  == \ /\  __ \   /\  == \   /\__  _\ /\  ___\   /\  == \   *
	* \ \  __<   \ \  __\   \ \  _-/ \ \ \/\ \  \ \  __<   \/_/\ \/ \ \  __\   \ \  __<   *
	*  \ \_\ \_\  \ \_____\  \ \_\    \ \_____\  \ \_\ \_\    \ \_\  \ \_____\  \ \_\ \_\ *
	*   \/_/ /_/   \/_____/   \/_/     \/_____/   \/_/ /_/     \/_/   \/_____/   \/_/ /_/ *
	*                                                                                     *
	* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

INTRODUCTION
------------

The Printer Reporter automates the task of reading and formatting the accounting reports produced

by the Collingwood and Barrie HP PageWide XL 5100ps and 4000ps printers. These reports were

previously completed manually, a task that took 15 - 20 min on average depending on the size of the 

reports.


REQUIREMENTS
------------

The original script has been compiled using pyinstaller so Python does not need to be installed. 


COMMON ISSUES
-------------

   1.	If you run the batch script and the prompt says 'UNC Path are not supported' and
	
	'main.exe is not a recognized command'

	ensure you are running the program from the mapped drive N:\ 

	and not the direct path \\col-nas\Shared\


   2.   If the script throws an error on line 46, double check the stored dates in src\dist\main\dates

	One of them likely has an extra space or extra line, make sure that only the date is there.

	If the problem persists, you may have downloaded the accounting spreadsheets in the wrong order

   
   3.   If the script throwns an error on line 11, The spreadsheets are not being moved to the 
	
	right place and the script can't access them or they aren't being renamed properly.
	
	Double check the batch script, they should moved from downloads to:

	N:\PrinterReporter\src\dist\main\reports and should be named bar and col.































