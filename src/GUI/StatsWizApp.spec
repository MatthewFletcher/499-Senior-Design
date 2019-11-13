# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['StatsWizApp.py'],
             pathex=['/home/x230m/Documents/FA19/499-Senior-Design/src/GUI',
             '/home/x230m/Documents/FA19/499-Senior-Design/src/Math'],
             binaries=[],
             datas=[],
             hiddenimports=['numpy.random.common', 'numpy.random.bounded_integers', 'numpy.random.entropy', 'statistics', 'Stats_Wizard'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

a.datas += [('StatsLogo1.png', '/home/x230m/Documents/FA19/499-Senior-Design/src/GUI/StatsLogo1.png', "DATA")]
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='StatsWizApp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='StatsWizApp')
