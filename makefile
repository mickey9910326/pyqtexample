ui:
	pyuic5 pyqtapp\\mainwindow.ui -o pyqtapp\\ui_mainwindow.py

test_ui:
	python tests\\test_ui.py
