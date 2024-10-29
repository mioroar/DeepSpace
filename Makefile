PYTHON=python3
PYINSTALLER=pyinstaller
FILE_NAME=deepspace.py
WINDOWS_SOURCE=.\deepspace.py
LINUX_SOURCE=`pwd`/deepspace.py
PLAN9_SOURCE=/sys/src/cmd/python/deepspace.py
WINDOWS_OUTPUT=.\output\windows
LINUX_OUTPUT=`pwd`/output/linux
PLAN9_OUTPUT=/usr/local/bin/
WINDOWS_OPTIONS=--onefile --console
LINUX_OPTIONS=--onefile --console
CLEANING_FILE=clear.py
all: windows linux web

windows:
	pip install -r requirements.txt
	@echo "Building for Windows..."
	$(PYINSTALLER) $(WINDOWS_OPTIONS) $(WINDOWS_SOURCE) --distpath $(WINDOWS_OUTPUT)
	$(WINDOWS_OUTPUT)\deepspace.exe

web:
	@echo "Building for web..."
	pip install flask
	python source/web/app.py

linux:
	@echo "Building for Linux..."
	@echo
	@echo "Installing python, pip, PyInstaller...\n"
	@apt install -y python3 python3-pip make
	@pip install --break-system-packages -r requirements.txt
	@echo "Done\n"
	@echo "Building Binary file..."
	@$(PYINSTALLER) $(LINUX_OPTIONS) $(LINUX_SOURCE) --distpath $(LINUX_OUTPUT)
	@echo "Done\n"
	@echo
	@echo "Built file located in $(LINUX_OUTPUT)"
	@echo


clean:
	@echo "Cleaning..."
	python $(CLEANING_FILE)

.PHONY: all windows linux web clean