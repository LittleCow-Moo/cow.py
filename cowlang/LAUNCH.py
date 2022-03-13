import os
import time
import json



class Color:
  warn = "\033[31m"
  end = "\033[0m"
  green = "\033[92m"
  cyan = "\033[96m"
  def warning(message):
    print(Color.warn + message + Color.end)

class ImportManager():
    def __init__(self):
        self.imports = []
        self.default = {
            "cow": {
                "version": "2.0.5",
                "description": "A simple, lightweight, and extensible text-based programming language.",
                "all": {
                    "exit": "[exit]",
                    "eat grass": "log 哞~ 草真好吃~",
                    "info": "process.info",
                    "moo": "moo!important 哞~"
                }
            },
            "process": {
                "version": "1.0",
                "description": "Process information",
                "all": {
                    "exit": "[exit]",
                    "time": "nowtime() int"
                }
            }
        }
    def add(self, module_name):
        module_name = module_name.replace("\n", "")
        if module_name in self.default:
            self.imports.append(module_name)
            PATH = self.default[module_name]
            print(f"Import: **Default\n~~ {module_name} v.{PATH['version']} ~~\n{PATH['description']}")
        else:
            module_name = module_name.replace("\n", "") + ".cl"
            if not module_name in os.listdir():
                Color.warning("Module not found (Skipped)")
            else:
                print("we're still running here..")
                lines = open(module_name, "r").readlines()
                if '[package]' in lines[0]:
                    lines.pop(0)
                    lines = '\n'.join(lines) # convert "lines" to str
                    PACKAGE = json.loads(lines)
                    self.add_key(PACKAGE)
                    print(PACKAGE)
                    self.imports.append(module_name)
                else:
                    Color.warning(f"WARNING: Filename '{module_name}' was not a package.\nIf you're trying to make one, make sure that the first line is '[pacakge]'")
                    
    def add_key(self, key):
        MUST = [
            "version",
            "description",
            "all"
        ]
        for i in MUST:
            try:
                key[0][i]
            except:
                Color.warning(f"Key not found ({i})")
                return
        if not isinstance(key[0]['all'], dict):
            Color.warning("Key was not a dictionary (all)")
            return
        print(Color.green + "Module added to 'default' ;)"+ Color.end)
        self.default.append(key)


        self.default.append(key)
    def run(self):
        pass
    def imported(self):
        return self.imports
    def commands(self):
        return self.default

def CowLang(lines) -> None:
    Manager = ImportManager()
    start_time = time.time()
    data = {}
    print(Color.green + "\n{Promise: fulfilled}\n" + Color.end)
    _quit_ = False
    try:
        lines[0]
    except:
        return Color.warning("The file is blank. Please edit it and restart the program.")
    if '[package]' in lines[0]:
        lines.pop(0)
        lines = '\n'.join(lines) # convert "lines" to str
        PACKAGE = json.loads(lines)
        _quit_ = True
    
    for line in lines:
        if _quit_:
            continue
        line = line.replace("\n", "")
        for i in Manager.imported():
                if line.startswith(f"{i}."):
                    if line == "process.time":
                        print(Color.cyan + str(time.time()) + Color.end)
                        break
                    try:
                        line = Manager.commands()[i]['all'][line.replace(f"{i}.", "", 1)]
                    except KeyError:
                        Color.warning(f"Module '{i}' has no feature: {line}")
        if line.startswith("#") or line.startswith("//"):
            continue # skip comments

        elif line.startswith("log "):
            print(line.replace("log ", "", 1))

        elif line.startswith("[import] "): # MAIN import manager
            Manager.add(line.replace("[import] ", "", 1))

        elif line == "[exit]":
            _quit_ = True

        elif line.startswith("wait "):
            if float(line.split(" ")[1]) == 0 or float(line.split(" ")[1]) > 10:
                Color.warning("Invalid Wait Time: skipping the command")
            time.sleep(float(line.split(" ")[1]))

        elif line.startswith("moo!important "):
            print("Important Comment: " + Color.cyan + line.replace("moo!important ", "", 1) + Color.end)

        elif line.startswith("var "):
            Color.warning("Warning:\nYou are using the var method.\nThis is deprecated and will be removed in the future.\nPlease use 'moo!data' add instead.")
        
        elif line.startswith("moo!data add "):
            read = line.replace("moo!data add ", "", 1)
            if line.count(",") != 1:
                Color.warning("Invalid Data: skipping the command")
                print(Color.green + "Usage: moo!data add KEY,VALUE\n" + Color.end)
                continue
            else:
                try:
                    data[read.split(",")[0]] = int(read.split(",")[1])
                except:
                    data[read.split(",")[0]] = read.split(",")[1]
                
                print(data)
        
        else:
            if line == "process.time" and "process" in Manager.imported():
                continue
            Color.warning("Invalid Command or Not Defined: " + line)
    end_time = time.time()
    grammar = ""
    if round(end_time - start_time) > 1:
        grammar = "s" 
    print(Color.green + "Execution Time: About " + str(round(end_time - start_time)) + f" second{grammar}" + Color.end)
    grammar2 = ""
    if end_time - start_time > 1:
        grammar2 = "s"
    print(Color.cyan + f"Accurate: {end_time - start_time} second{grammar2}" + Color.end)
    print("")

print(Color.end + "CowLangConfig - version 1.0a")
print("Running check..")



class Errors:
  class FileNotFound(Exception):
    pass
  class InvalidFormat(Exception):
      pass

def _check():
    text = input(Color.green + "Do you want me to edit the file for you? (y/n) " + Color.end)
    if text.lower() == "y":
        file = input(Color.cyan + "Enter the file you want to run> " + Color.end)
        if not file in os.listdir():
            raise Errors.FileNotFound('The file you entered does not exist :(')
        open("CONFIG.clcon", "w").writelines(f"run={file}")
        print(Color.green + "Done! :)" + Color.end)
        return
    else:
        print("Ok, I won't do anything.")

if not "CONFIG.clcon" in os.listdir():
  Color.warning("Check: Cannot Find Config File 'CONFIG.clcon', do you want to create one?")
  text = input(Color.green + "Proceed? (Y/N)> " + Color.end)
  if text.lower() != "y":
    raise(Errors.FileNotFound("Cannot Find Config File 'CONFIG.clcon'"))
  else:
      print("Creating Config File 'CONFIG.clcon'")
      with open("CONFIG.clcon", "w+") as main:
        main.writelines("run=main.py") 
      print("Config File 'CONFIG.clcon' Created")
      _check()
      exit()
else:
    print("Check: Config File 'CONFIG.clcon' Found")

    with open("CONFIG.clcon", "r") as main:     # check if the file is blank (it will raise an error)
        try:
            thing = main.read()
            if thing == "":
                Color.warning("Config File 'CONFIG.clcon' is empty.")
                _check()
                exit()
        except:
            Color.warning("Config File 'CONFIG.clcon' is empty.")
            _check()
            exit()
        
    file = open("CONFIG.clcon", "r").readlines()

    for lines in file: # it means for items in file (aka this is a list)
        if lines.startswith("run="):
            value = lines.split("=")[1]
            break
        elif lines.startswith("#") or lines.startswith("//"):
            continue # ignore it since it's a comment
    if not value.endswith("cl"):
        Color.warning("The file extension was not '.cl', do you want to continue?")
        text = input(Color.green + "y/n> " + Color.end)
        if text.lower() != "y":
            raise(Errors.InvalidFormat("The file extension was not '.cl'"))
    print(Color.cyan + f"Running {value}..." + Color.end)
    CowLang(open(value, "r").readlines())
