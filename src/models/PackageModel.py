
from pydantic import Field, validator
from typing import List, Optional, Union, Literal, Dict
from sdks.novavision.src.base.model import Package, Image, Inputs, Configs, Outputs, Response, Request, Output, Input, Config, Detection

class InputData(Input):
    name: Literal["inputData"] = "inputData"
    value: Union[List[Image], Image, List[Detection], Detection, Dict, List]
    type: str = "object"


class OutputData(Output):
    name: Literal["outputData"] = "outputData"
    value: Union[List[Image], Image, List[Detection], Detection, Dict, List]
    type: str = "object"

    class Config:
        title = "Output Data"

class ConfigSelectedKey(Config):
    """
        .
    """
    name: Literal["configSelectedKey"] = "configSelectedKey"
    value: str = Field(min_length=0)
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Selected Key"
        json_schema_extra = {
            "shortDescription": "."
        }

class TargetValue(Config):
    """
        .
    """
    name: Literal["targetValue"] = "targetValue"
    value: str
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Target Value"
        json_schema_extra = {
            "shortDescription": "."
        }

class ReplaceValue(Config):
    """
        .
    """
    name: Literal["replaceValue"] = "replaceValue"
    value: str
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Replace Value"
        json_schema_extra = {
            "shortDescription": "."
        }


class ReplaceEnabled(Config):
    name: Literal["replaceEnabled"] = "replaceEnabled"
    value: Literal["replaceEnabled"] = "replaceEnabled"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    targetValue: TargetValue
    replaceValue: ReplaceValue

    class Config:
        title = "Enabled"


class ReplaceDisabled(Config):
    name: Literal["replaceDisabled"] = "replaceDisabled"
    value: Literal["replaceDisabled"] = "replaceDisabled"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Disabled"


class ConfigReplace(Config):
    """
        .
    """
    name: Literal["configReplace"] = "configReplace"
    value: Union[ReplaceEnabled, ReplaceDisabled]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Replace"
        json_schema_extra = {
            "shortDescription": "."
        }

class LengthEnabled(Config):
    name: Literal["lengthEnabled"] = "lengthEnabled"
    value: Literal["lengthEnabled"] = "lengthEnabled"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    targetValue: TargetValue
    replaceValue: ReplaceValue

    class Config:
        title = "Enabled"


class LengthDisabled(Config):
    name: Literal["lengthDisabled"] = "lengthDisabled"
    value: Literal["lengthDisabled"] = "lengthDisabled"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Disabled"


class ConfigLength(Config):
    """
        .
    """
    name: Literal["configLength"] = "configLength"
    value: Union[LengthEnabled, LengthDisabled]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Length"
        json_schema_extra = {
            "shortDescription": "."
        }

class CountValue(Config):
    """
        .
    """
    name: Literal["countValue"] = "countValue"
    value: str
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Count Value"
        json_schema_extra = {
            "shortDescription": "."
        }

class CountEnabled(Config):
    name: Literal["countEnabled"] = "countEnabled"
    value: Literal["countEnabled"] = "countEnabled"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    countValue: CountValue

    class Config:
        title = "Enabled"


class CountDisabled(Config):
    name: Literal["countDisabled"] = "countDisabled"
    value: Literal["countDisabled"] = "countDisabled"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Disabled"


class ConfigCount(Config):
    """
        .
    """
    name: Literal["configCount"] = "configCount"
    value: Union[CountEnabled, CountDisabled]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Count"
        json_schema_extra = {
            "shortDescription": "."
        }

class FindValue(Config):
    """
        .
    """
    name: Literal["findValue"] = "findValue"
    value: str
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Count Value"
        json_schema_extra = {
            "shortDescription": "."
        }

class FindEnabled(Config):
    name: Literal["findEnabled"] = "findEnabled"
    value: Literal["findEnabled"] = "findEnabled"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    findValue: FindValue

    class Config:
        title = "Enabled"


class FindDisabled(Config):
    name: Literal["findDisabled"] = "findDisabled"
    value: Literal["findDisabled"] = "findDisabled"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Disabled"


class ConfigFind(Config):
    """
        .
    """
    name: Literal["configFind"] = "configFind"
    value: Union[FindEnabled, FindDisabled]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Find"
        json_schema_extra = {
            "shortDescription": "."
        }

class Swapcase(Config):
    name: Literal["swapcase"] = "swapcase"
    value: Literal["swapcase"] = "swapcase"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Swapcase"

class Title(Config):
    name: Literal["title"] = "title"
    value: Literal["title"] = "title"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Title"

class Upper(Config):
    name: Literal["upper"] = "upper"
    value: Literal["upper"] = "upper"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Upper"


class Lower(Config):
    name: Literal["lower"] = "lower"
    value: Literal["lower"] = "lower"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Lower"


class Capitalize(Config):
    name: Literal["capitalize"] = "capitalize"
    value: Literal["capitalize"] = "capitalize"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Capitalize"

class CaseConversionsDisabled(Config):
    name: Literal["caseConversionsDisabled"] = "caseConversionsDisabled"
    value: Literal["caseConversionsDisabled"] = "caseConversionsDisabled"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Disabled"

class ConfigCaseConversions(Config):
    """
        .
    """
    name: Literal["configCaseConversions"] = "configCaseConversions"
    value: Union[CaseConversionsDisabled, Capitalize, Lower, Upper, Title, Swapcase]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Case Conversions"
        json_schema_extra = {
            "shortDescription": "."
        }


class RStripValue(Config):
    """
        .
    """
    name: Literal["rStripValue"] = "rStripValue"
    value: str
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "R Strip Value"
        json_schema_extra = {
            "shortDescription": "."
        }

class RStrip(Config):
    name: Literal["rStrip"] = "rStrip"
    value: Literal["rStrip"] = "rStrip"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    rStripValue: RStripValue

    class Config:
        title = "R Strip"

class LStripValue(Config):
    """
        .
    """
    name: Literal["lStripValue"] = "lStripValue"
    value: str
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "L Strip Value"
        json_schema_extra = {
            "shortDescription": "."
        }

class LStrip(Config):
    name: Literal["lStrip"] = "lStrip"
    value: Literal["lStrip"] = "lStrip"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    lStripValue: LStripValue

    class Config:
        title = "L Strip"

class StripValue(Config):
    """
        .
    """
    name: Literal["stripValue"] = "stripValue"
    value: str
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Strip Value"
        json_schema_extra = {
            "shortDescription": "."
        }

class Strip(Config):
    name: Literal["strip"] = "strip"
    value: Literal["strip"] = "strip"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    stripValue: StripValue

    class Config:
        title = "Strip"

class PrefixValue(Config):
    """
        .
    """
    name: Literal["prefixValue"] = "prefixValue"
    value: str
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Prefix Value"
        json_schema_extra = {
            "shortDescription": "."
        }

class RemovePrefix(Config):
    name: Literal["removePrefix"] = "removePrefix"
    value: Literal["removePrefix"] = "removePrefix"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    prefixValue: PrefixValue

    class Config:
        title = "Remove Prefix"

class SuffixValue(Config):
    """
        .
    """
    name: Literal["suffixValue"] = "suffixValue"
    value: str
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Suffix Value"
        json_schema_extra = {
            "shortDescription": "."
        }

class RemoveSuffix(Config):
    name: Literal["removeSuffix"] = "removeSuffix"
    value: Literal["removeSuffix"] = "removeSuffix"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    suffixValue: SuffixValue

    class Config:
        title = "Remove Suffix"


class EdgeTrimmingDisabled(Config):
    name: Literal["edgeTrimmingDisabled"] = "edgeTrimmingDisabled"
    value: Literal["edgeTrimmingDisabled"] = "edgeTrimmingDisabled"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Disabled"

class ConfigEdgeTrimming(Config):
    """
        .
    """
    name: Literal["configEdgeTrimming"] = "configEdgeTrimming"
    value: Union[EdgeTrimmingDisabled,RemoveSuffix,RemovePrefix,Strip,LStrip,RStrip]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Edge Trimming"
        json_schema_extra = {
            "shortDescription": "."
        }


class StringInputs(Inputs):
    inputData: InputData


class StringConfigs(Configs):
    configSelectedKey: ConfigSelectedKey
    configReplace: ConfigReplace
    configLength: ConfigLength
    configCount: ConfigCount
    configFind: ConfigFind
    configCaseConversions: ConfigCaseConversions
    configEdgeTrimming: ConfigEdgeTrimming


class StringOutputs(Outputs):
    outputData: OutputData


class StringRequest(Request):
    inputs: Optional[StringInputs]
    configs: StringConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class StringResponse(Response):
    outputs: StringOutputs


class StringExecutor(Config):
    name: Literal["String"] = "String"
    value: Union[StringRequest, StringResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "String"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }


class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: Union[StringExecutor]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Task"
        json_schema_extra = {
            "target": "value"
        }


class PackageConfigs(Configs):
    executor: ConfigExecutor


class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["String"] = "String"
