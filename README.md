<h1 align="center">revcat</h1>
<h3 align="center">Unofficial RevenueCat CLI for weird but necessary use cases</h2>

<p align="center">
    <a  href="https://pypi.org/project/revcat/">
        <img alt="CI" src="https://img.shields.io/pypi/v/revcat.svg?style=flat-round&logo=pypi&logoColor=white">
    </a>
</p>

**revcat** lets you interact with the RevenueCat API from the command line, but that’s not really the main reason it exists.

You could do that with curl or any other HTTP client—if you enjoy writing long, unreadable commands and questioning your life choices.

The real reason for revcat is to handle the weird but necessary use cases that RevenueCat doesn’t support out of the box. One of those?
Granting entitlements to a huge list of users via a CSV file.

In our case, we wanted to grant an early-adopter entitlement to users who signed up before we introduced the paywall. The idea was simple:
they had been using certain features for free, and even though some of those features later became PRO, we wanted to let them keep access
as a thank-you for being there from the start—and let’s be honest, also to prevent a huge spike in our churn rate 🙂.

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
