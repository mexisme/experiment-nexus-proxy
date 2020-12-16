load("@build_bazel_rules_nodejs//:index.bzl", "nodejs_binary")

nodejs_binary(
    name = "nexus_proxy_pull",
    data = [
        "@npm//lodash",
        "@npm//winston",
    ],
    entry_point = "main.js",
)
