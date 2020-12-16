workspace(
    name = "nexus_proxy_test",
    managed_directories = {"@npm": ["js/node_modules"]},
)

##########

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "build_bazel_rules_nodejs",
    sha256 = "121f17d8b421ce72f3376431c3461cd66bfe14de49059edc7bb008d5aebd16be",
    urls = ["https://github.com/bazelbuild/rules_nodejs/releases/download/2.3.1/rules_nodejs-2.3.1.tar.gz"],
)

load("@build_bazel_rules_nodejs//:index.bzl", "node_repositories", "yarn_install")
# load("@build_bazel_rules_nodejs//:index.bzl", "yarn_install")

# # NOTE: this rule installs nodejs, npm, and yarn, but does NOT install
# # your npm dependencies into your node_modules folder.
# # You must still run the package manager to do this.
node_repositories(package_json = [
    "//js:package.json",
    ]
)

yarn_install(
    name = "npm",
    package_json = "//js:package.json",
    yarn_lock = "//js:yarn.lock",
)

##########

http_archive(
    name = "rules_python",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.1.0/rules_python-0.1.0.tar.gz",
    sha256 = "b6d46438523a3ec0f3cead544190ee13223a52f6a6765a29eae7b7cc24cc83a0",
)

# load("@rules_python//python:pip.bzl", "pip_repositories")
# pip_repositories()

# load("@rules_python//python:pip.bzl", "pip_install")

# # Create a central repo that knows about the dependencies needed for
# # requirements.txt.
# pip_install(   # or pip3_import
#     name = "my_deps",
#     requirements = "//path/to:requirements.txt",
# )
