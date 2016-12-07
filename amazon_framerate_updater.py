#!/usr/bin/python
# -*- coding: utf-8 -*-

# Amazon Framerate Updater
#
# Author: Simon Lachaîne


import os
import sys
import time

import lxml.etree as etree
from PyQt4 import QtCore, QtGui

import framerate_updater_ui as main_frame


original_files = []
mmc_lst = []
destination_path = ""
directory = ""


class UpdateXml(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        nsmap = {
            "manifest": "http://www.movielabs.com/schema/manifest/v1.5/manifest",
            "md": "http://www.movielabs.com/schema/md/v2.4/md",
        }

        for mmc in mmc_lst:
            mmc_xml = etree.parse(mmc)
            mmc_root = mmc_xml.getroot()

            for sub in mmc_root.findall(path=".//md:FrameRate", namespaces=nsmap):
                if sub.get("multiplier") == "999/1000":
                    sub.set("multiplier", "1000/1001")

                if sub.get("timecode") == "NDF":
                    sub.set("timecode", "NonDrop")

            tree = etree.ElementTree(mmc_root)
            os.chdir(destination_path)
            tree.write(os.path.basename(mmc),
                       xml_declaration=True,
                       encoding="UTF-8",
                       pretty_print=True)


class FramerateApp(QtGui.QMainWindow, main_frame.Ui_AmazonFramerateApp):
    def __init__(self, parent=None):
        super(FramerateApp, self).__init__(parent)

        self.update_xml_thread = UpdateXml()

        self.setupUi(self)

        self.original_btn.clicked.connect(self.original_dlg)
        self.clear_btn.clicked.connect(self.clear_mmcs)
        self.destination_btn.clicked.connect(self.destination_dlg)
        self.process_btn.clicked.connect(self.process)

        self.show()

    def original_dlg(self):
        global original_files
        global directory
        global mmc_lst

        original_files = \
            QtGui.QFileDialog.getOpenFileNames(
                parent=self,
                caption="Locate MMC file(s)",
                directory=directory,
                filter="Xml files (*.xml)")

        for mmc in [str(f) for f in original_files]:
            mmc_lst.append(mmc)
            self.original_text.appendPlainText(mmc)

        if original_files:
            directory = os.path.dirname(mmc_lst[0])

    def clear_mmcs(self):
        global original_files
        global mmc_lst

        while original_files:
            original_files.pop()

        while mmc_lst:
            mmc_lst.pop()
        self.original_text.clear()

    def destination_dlg(self):
        global destination_path
        global directory

        destination_path = \
            str(QtGui.QFileDialog.getExistingDirectory(
                parent=self,
                caption="Select destination for the updated files",
                directory=directory))

        self.destination_line.setText(destination_path)

        if destination_path:
            directory = destination_path

    def process(self):
        if not original_files:
            files_msg = QtGui.QMessageBox()
            files_msg.setIcon(QtGui.QMessageBox.Information)
            files_msg.setText("Please select at least one MMC to process.")
            files_msg.setWindowTitle("Input needed")
            files_msg.setStandardButtons(QtGui.QMessageBox.Ok)
            files_msg.exec_()
            return

        if not destination_path:
            dest_msg = QtGui.QMessageBox()
            dest_msg.setIcon(QtGui.QMessageBox.Information)
            dest_msg.setText("Please select the destination for the updated file(s).")
            dest_msg.setWindowTitle("Input needed")
            dest_msg.setStandardButtons(QtGui.QMessageBox.Ok)
            dest_msg.exec_()
            return

        self.connect(self.update_xml_thread, QtCore.SIGNAL("finished()"), self.update_xml_done)
        self.update_xml_thread.start()

    def update_xml_done(self):
        results = "Process completed at %s." % time.strftime("%X")
        self.process_line.setText(results)


def main():
    app = QtGui.QApplication(sys.argv)
    gui = FramerateApp()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
