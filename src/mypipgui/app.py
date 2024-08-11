import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from mylocale.TR import tr
import os
import sys
import locale


class MyPipGUI(toga.App):
    def startup(self):
        lang = locale.getlocale()[0]
        self.file = f"{self.paths.app.absolute()}/resources/localisation.csv"
        main_box = toga.Box()
        module_input = toga.TextInput(
            placeholder=tr(
                csv_file=self.file, target_key="SEARCHPACKAGE", langcode=lang
            )
        )
        searchbtn = toga.Button(
            text=tr(csv_file=self.file, target_key="SEARCHPACKAGE", langcode=lang)
        )
        installbtn = toga.Button(
            tr(csv_file=self.file, target_key="INSTALLPACKAGE", langcode=lang),
            enabled=False,
        )
        main_box.add(module_input)
        main_box.add(searchbtn)
        main_box.add(installbtn)
        main_box.style.direction = "column"
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def install(package, version=""):
    if package == "":
        return Exception()
    if version != "":
        os.system(f"{sys.executable} -m pip install {package}=={version}")
    else:
        os.system(f"{sys.executable} -m pip install {package}")


def main():
    return MyPipGUI()
