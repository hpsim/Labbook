# Commands

This file describes ideas how the labbook works and which commands are available. At the center of the labbook commands is a configuration file defining pipelines and dependencies




labbook init campaign
labook execute <pipeline>
labbook commit -m <message>

File / Folder Structure
  
labbook init project [template]
  
 base results .gitignore .archive .config 
  
labbook init campaign parameter_foo 
  
 base  parameter_foo results .gitignore .archive .config 
  
labbook init new_base [parameter_foo/1] -m "Use parameter 1 for new base case"
  
 base results .archive/old_base_id

