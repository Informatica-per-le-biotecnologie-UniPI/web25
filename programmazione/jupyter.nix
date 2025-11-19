let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-25.05";
  pkgs = import nixpkgs { config = {}; overlays = []; };
in
pkgs.mkShellNoCC {

  packages = with pkgs; [
    # python
    python313
    python313Packages.ipython
    python313Packages.pip
    # python313Packages.jupyter
    nodejs
    python313Packages.jupyterlab
    python313Packages.ipykernel
    
    python313Packages.pandas
    python313Packages.tabulate
    python313Packages.scikit-learn
    python313Packages.seaborn
    python313Packages.openpyxl
  ];
}
