with (import <nixpkgs> {});
let
  gems = bundlerEnv {
    name = "website";
    inherit ruby;
    gemdir = ./.;
  };
in stdenv.mkDerivation {
  name = "website";
  buildInputs = [gems ruby];
}
