# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Party_with_Patty.py'],
             pathex=['.'],
             binaries=[],
             datas=[('resourses/backgrounds/fon.png', 'resourses/backgrounds'), ('resourses/backgrounds/icon.png', 'resourses/backgrounds'), ('resourses/backgrounds/substrate.png', 'resourses/backgrounds'), ('resourses/objects/castle0.png', 'resourses/objects'), ('resourses/objects/castle1.png', 'resourses/objects'), ('resourses/objects/cloud0.png', 'resourses/objects'), ('resourses/objects/cloud1.png', 'resourses/objects'), ('resourses/objects/crab0.png', 'resourses/objects'), ('resourses/objects/crab1.png', 'resourses/objects'), ('resourses/objects/heart.png', 'resourses/objects'), ('resourses/objects/snag0.png', 'resourses/objects'), ('resourses/objects/snag1.png', 'resourses/objects'), ('resourses/characters/marina0.png', 'resourses/characters'), ('resourses/characters/marina1.png', 'resourses/characters'), ('resourses/characters/marina1.png', 'resourses/characters'), ('resourses/characters/sonya0.png', 'resourses/characters'), ('resourses/characters/sonya1.png', 'resourses/characters'), ('resourses/characters/sonya_invert.png', 'resourses/characters'), ('resourses/sounds/click_button.wav', 'resourses/sounds'), ('resourses/sounds/crash.wav', 'resourses/sounds'), ('resourses/sounds/fall.wav', 'resourses/sounds'), ('resourses/sounds/hp.wav', 'resourses/sounds'), ('resourses/sounds/jump.wav', 'resourses/sounds'), ('resourses/sounds/loss.wav', 'resourses/sounds'), ('resourses/sounds/main.mp3', 'resourses/sounds'), ('resourses/sounds/menu.mp3', 'resourses/sounds'), ('resourses/sounds/pause.wav', 'resourses/sounds'), ('resourses/font/PingPong.ttf', 'resourses/font')],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Party with Patty',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False, icon='C:/Users/1/Desktop/Питон/pygame/Party_with_Patty/resourses/backgrounds/icon.ico')
