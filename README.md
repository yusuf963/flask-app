# flask-app

# run the vertuall enviroment run the command
pipenv shell # to inter the vertual env and create a pipfile
 #### now you are in the vertual env sell
python # to enter IDE python on the terminal
import sys
sys.excutable # this will show you where you python is excuting right now - ofcourse its vertual
# you can quit() always
# pipenv lock -r # to list all the lib in you env
pipenv unstall -r ./reuirement.txt # bulk install for the listed  in the requirment file
pipenv check   # to check the safty of he packeges
pipenv graph    # list all the lib with their dependncies
pip freeze   # to ist all the lib in your project
pipenv show flask # to check the installation location of the module “flask”
