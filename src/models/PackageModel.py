
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

class OptionFind(Config):
    name: Literal["optionFind"] = "optionFind"
    value: Literal["optionFind"] = "optionFind"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "find"


class OptionCount(Config):
    name: Literal["optionCount"] = "optionCount"
    value: Literal["optionCount"] = "optionCount"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "count"


class OptionLen(Config):
    name: Literal["optionLen"] = "optionLen"
    value: Literal["optionLen"] = "optionLen"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "length"


class Classes(Config):
    """
       .
    """
    name: Literal["classes"] = "classes"
    value: List[Union[OptionFind, OptionCount, OptionLen]]
    type: Literal["object"] = "object"
    field: Literal["selectBox"] = "selectBox"

    class Config:
        title = "Classes"
        json_schema_extra = {
            "shortDescription": "."
        }

class ClassesEnabled(Config):
    name: Literal["classesEnabled"] = "classesEnabled"
    value: Literal["classesEnabled"] = "classesEnabled"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    classes: Classes

    class Config:
        title = "Enabled"

class ClassesDisabled(Config):
    name: Literal["classesDisabled"] = "classesDisabled"
    value: Literal["classesDisabled"] = "classesDisabled"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Disabled"

class ConfigClasses(Config):
    """
        .
    """
    name: Literal["configClasses"] = "configClasses"
    value: Union[ClassesEnabled, ClassesDisabled]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Classes"
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
    configClasses: ConfigClasses
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
