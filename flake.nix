{
  description = "Python development environment";

  inputs = {
    # Bring in the stable nixpkgs release (25.05).
    # This gives us a large, well-tested set of packages (Linux + macOS).
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.05";

    # flake-utils helps us write flakes that work on multiple systems
    # (Linux/macOS, Intel/ARM) without repeating code.
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
  }:
  # eachDefaultSystem generates outputs for the main supported systems:
  # - "x86_64-linux"    (Linux on Intel/AMD)
  # - "aarch64-linux"   (Linux on ARM, e.g. Raspberry Pi, AWS Graviton)
  # - "x86_64-darwin"   (macOS on Intel)
  # - "aarch64-darwin"  (macOS on Apple Silicon M1/M2/M3)
  # So this flake should work on Linux and MacOS
    flake-utils.lib.eachDefaultSystem (system: let
      # Import nixpkgs for the current system
      pkgs = import nixpkgs {inherit system;};
    in {
      # Define the development shell (what you get with `nix develop`)
      devShells.default = pkgs.mkShell {
        # Tools we want available inside the shell
        buildInputs = with pkgs; [
          # Pick the Python version from stable nixpkgs
          # (You can switch to pkgs.python312 or pkgs.python311 if needed)
          python313
          uv # Fast Python package/dependency manager
          git-cliff # Generate changelogs from git history
          mask # Markdown-based replacement for Make
        ];

        # Commands that run every time you enter the shell
        shellHook = ''
          uv venv
          source .venv/bin/activate
          uv pip install -r pyproject.toml --all-extras
          pre-commit install --hook-type pre-commit --hook-type commit-msg --hook-type pre-push
          clear
          echo "Welcome!"
        '';
      };
    });
}
