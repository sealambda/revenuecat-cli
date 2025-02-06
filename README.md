# RevenueCat CLI

Unofficial RevenueCat CLI for Python.

It allows you to interact with the RevenueCat API from the command line,
and automate more complex tasks such as granting entitlements to users.

## ⚙️ Installation

[We recommend](https://sealambda.com/blog/hygienic-python-in-2025) [uv](https://github.com/astral-sh/uv) to run the CLI.

```bash
# to run the CLI straight away
uvx revcat --help

# or if you prefer to install it
uv tool install revcat
```

You may of course also use `pip` to install the CLI - or `pipx` if you prefer to install it in an isolated environment.

```bash
pipx install revcat

# ...or if you like to live on the edge
pip install revcat
```

## 🔨 Usage

```bash
export REVENUECAT_API_KEY=<api-key>
revcat v1 entitlements grant --user-id <user-id> --entitlement-id <entitlement-id>
```

## 💻 Contributing

If you want to contribute to the project, please read the [CONTRIBUTING.md](./CONTRIBUTING.md) file.

It contains information on how to set up your development environment, submit issues, and create pull requests.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
