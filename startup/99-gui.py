from issgoogletools import iss_tracker





from PyQt5.QtWidgets import QApplication
app = QApplication(sys.argv)
a=iss_tracker.ISSTracker(RE=RE)
a.show()
