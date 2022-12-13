from setuptools import setup, find_packages


setup(
    name="mlflow-iap-auth-plugin",
    version="0.0.1",
    description="IAP AUth plugin for MLflow",
    packages=find_packages(),
    install_requires=["mlflow", "google-cloud-iam"],
    entry_points={
        # Define a RequestHeaderProvider plugin. The entry point name for request header providers
        # is not used, and so is set to the string "unused" here
        "mlflow.request_header_provider": "unused=mlflow_test_plugin.request_header_provider:PluginRequestHeaderProvider",  # pylint: disable=line-too-long
    },
)
