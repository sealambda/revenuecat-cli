# Contributing

Hey there! Thanks for thinking about contributing to the revcat CLI for RevenueCat!
We appreciate all kinds of help, whether it's fixing bugs, adding new features, or improving our documentation.

This guide will help you get started.

## Reporting Issues

Found a bug? Please let us know by [submitting an issue](https://github.com/sealambda/revenuecat-cli/issues/new). Your
feedback helps us improve!

### Setting up your development environment

1. Fork the repository and clone your fork.
2. Make sure you follow our blog post on [how to install uv](https://sealambda.com/blog/hygienic-python-in-2025).
3. Run the CLI:
   ```sh
   uv run revcat --help
   ```

### Submitting a Pull Request

1. Create a new branch from `main` for your feature or bugfix.
2. Make your changes.
3. Commit your changes with a descriptive commit message.
4. Push your branch to your fork.
5. Open a pull request against the `main` branch of the original repository.
6. Clearly describe the problem and solution in your pull request. Include the issue number if applicable.
7. Wait for a review and address any feedback.

## Release Process

_for maintainers_

1. Run `cz bump --no-verify` to bump the version.
   We have to wait for https://github.com/commitizen-tools/commitizen/issues/1349 to solve the issue with `--no-verify`.
2. Run `uv lock` to update the lock file - then amend the commit with `git commit --all --no-edit --amend`.
3. Push the changes to the repository.
