# Contributing

In the spirit of [free software](http://www.fsf.org/licensing/essays/free-sw.html), I encourage **everyone** to help improve this project.
Here are some ways _you_ can contribute:

- Report bugs.
- Suggest new features.
- Write or edit documentation.
- Write specifications.
- Write code (**no patch is too small**: fix typos, add comments, clean up inconsistent whitespace).
- Refactor code.
- Fix [issues](https://github.com/ArielMAJ/Python_API_Challenge/issues).
- Review patches.

## Submitting an issue

This project uses the [GitHub issue tracker](https://github.com/ArielMAJ/Python_API_Challenge/issues) to track bugs and features.
Before submitting a bug report or feature request, check to make sure no one else has already submitted the same bug report.

When submitting a bug report, please include any details that may be necessary to reproduce the bug, including the version of the
API, Python version, and operating system.

## Writing code

Install the development dependencies with `pip install -r requirements-dev.txt` and always run `black` and `isort` before
committing and making PRs. If you’re adding new functionality, you should provide tests to cover it.

## Submitting a pull request

1. Fork the repository.
2. Create a topic branch.
3. Add tests for your unimplemented feature or bug fix.
4. Run `python -m unittest`. If your tests pass, return to step 3 until there are enough tests.
5. Implement your feature or bug fix.
6. If your changes are not fully covered by your tests, return to step 3.
7. Add documentation for your feature or bug fix.
8. Commit and push your changes.
9. Submit a pull request.

## License

By contributing, you agree that your contributions will be licensed under its [MIT](./LICENSE) license.
