import importlib.resources
path = importlib.resources.files("bmsgui.tools").joinpath("quickbms_4gb_files.exe")
print(path)