import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from mylocale.TR import tr
import os
import sys
import locale
from mypypisearch import search
results = search("toga")
for result in results:
    print(result.name)


class MyPipGUI(toga.App):
    def startup(self):
        lang = locale.getlocale()[0]
        self.file = f"{self.paths.app.absolute()}/resources/localisation.csv"
        main_box = toga.Box()
        self.module_input = toga.TextInput(
            placeholder=tr(
                csv_file=self.file, target_key="SEARCHPACKAGE", langcode=lang
            ),
            on_change=self.change_module_input,
            style=Pack(padding=10, flex=1),
        )
        self.searchbtn = toga.Button(
            text=tr(csv_file=self.file, target_key="SEARCHPACKAGE", langcode=lang),
            enabled=False,
            style=Pack(padding=10, flex=1),
        )
        self.installbtn = toga.Button(
            tr(csv_file=self.file, target_key="INSTALLPACKAGE", langcode=lang),
            enabled=False,
            style=Pack(padding=10, flex=1),
        )
        main_box.add(self.module_input)
        main_box.add(self.searchbtn)
        main_box.add(self.installbtn)
        main_box.style.direction = "column"
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def change_module_input(self, widget):
        if self.module_input.value != "":
            self.searchbtn.enabled = True
        else:
            self.searchbtn.enabled = False


def install(package, version=""):
    if package == "":
        return Exception()
    if version != "":
        os.system(f"{sys.executable} -m pip install {package}=={version}")
    else:
        os.system(f"{sys.executable} -m pip install {package}")


def main():
    return MyPipGUI()
