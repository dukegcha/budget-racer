import cx_Freeze

executables = [cx_Freeze.Executable("budgetRacer.py")]

cx_Freeze.setup(
    name = "Budget Racer",
    options = {"build_exe" : {"packages" : ["pygame"],
                              "include_files" : ["racecar.png"]}},
    executables = executables

)