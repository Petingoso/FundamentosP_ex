let
  pkgs = import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/d9d07251f12399413e6d33d5875a6f1994ef75a7.tar.gz") {};
in
  pkgs.mkShellNoCC {
    packages = [
      (
        pkgs.python3.withPackages (python-pkgs: [
          python-pkgs.debugpy
        ])
      )
    ];
  }
