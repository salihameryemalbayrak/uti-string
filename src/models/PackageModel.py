
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
        title = "Config Classes"
        json_schema_extra = {
            "shortDescription": "."
        }

class StringInputs(Inputs):
    inputData: InputData


class StringConfigs(Configs):
    configReplace: ConfigReplace
    configClasses: ConfigClasses
    configCaseConversions: ConfigCaseConversions


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
