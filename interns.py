#!/usr/bin/env python3
#
# SCRIPT: interns
# AUTHOR: Vidushi Bansal
# DATE:   03/03/2020
# REV:    1.1.A (Valid are A, B, D, T and P)
#          (For Alpha, Beta, Dev, Test and Production)
#
#
# PLATFORM: UBUNTU
#
# PURPOSE: Use of jinja template and passing the dictionary to it.
# REV LIST:
#    DATE        : Date of revision
#    BY          : AUTHOR OF MODIFICATION
#    MODIFICATION: Describe the chages made. What do they enhance.
#
# set -n   # Uncomment to check script syntax, without execution.
#          # NOTE: Do forget comment it back as it won't allow the
#          # the script to execute.
#
# set +x   # Uncomment this for debugging this shell script.
#
#
################################################################
#          Define Files and Variables here                     #
from jinja2 import Template
intern1 = {'Name':'vidushi', 'Department':'Btech', 'Year':2020}
intern2 = {'Name':'Himanshu', 'Department':'Btech', 'Year':2020}
intern3 = {'Name': 'Pratik', 'Department':'Btech', 'Year':2020}
intern4 = {'Name': 'Vaibhav', 'Department':'Btech', 'Year':2020}

interns = {'Intern1':intern1, 'Intern2':intern2, 'Intern3':intern3, 'Intern4':intern4}
################################################################
################################################################
#          Define Functions here                               #
#def jinjafun():
 #   for i in interns:
  #      for j in Intern1:
   #         name=i.Name
    #        dept=i.Department
     #       year=i.Year
      #      tm = Template("Name of the Intern is {{name}}. Department of the intern is {{dept}}. Year of graduation of the intern is {{year}}")

   # msg = tm.render(interns=interns)
   # print(msg)
#
#
#
#
#
#
def jinjafun():
    for i in interns:

         tm = Template("Name of the Intern is {{i['Name']}}. Department of the intern is {{i['Department']}}. Year of graduation of the intern is {{i['Year']}}")
         msg = tm.render(i=interns[i])
         print(msg)

################################################################
################################################################
#          Beginning of Main                                   #
jinjafun()
################################################################
# End of script                                               #

