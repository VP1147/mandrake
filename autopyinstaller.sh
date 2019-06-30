#!/bin/sh
pyinstaller mandrake.spec
rm -r build/
chmod a+w+x dist/
echo '<<OK>>'
