
from sdks.novavision.src.helper.package import PackageHelper
from components.String.src.models.PackageModel import PackageModel, PackageConfigs, ConfigExecutor, StringOutputs, StringResponse, StringExecutor, OutputData


def build_response_string(context):
    outputData = OutputData(value=context.outputData)
    stringOutputs = StringOutputs(outputData=outputData)
    stringResponse = StringResponse(outputs=stringOutputs)
    stringExecutor = StringExecutor(value=stringResponse)
    executor = ConfigExecutor(value=stringExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel