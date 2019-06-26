# -*- mode: python -*-

block_cipher = None

added_files = [
             ('settings.json','.'),
             ('design','design'),
             ('info.txt','.'),
             ('man.txt','.'),
             ('LICENSE','.')
]

a = Analysis(['mandrake.py'],
             pathex=['/home/vp1147/Documentos/GitHub/mandrake'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='mandrake',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='mandrake')
