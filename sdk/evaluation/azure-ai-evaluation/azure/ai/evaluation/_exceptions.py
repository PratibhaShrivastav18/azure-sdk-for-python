# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""This includes enums and classes for exceptions for use in azure-ai-evaluation."""

from enum import Enum

from azure.core.exceptions import AzureError


class ErrorCategory(Enum):
    """Error category to be specified when using EvaluationException class.

    When using EvaluationException, specify the type that best describes the nature of the error being captured.

    * INVALID_VALUE -> One or more inputs are invalid (e.g. incorrect type or format)
    * UNKNOWN_FIELD -> A least one unrecognized parameter is specified
    * MISSING_FIELD -> At least one required parameter is missing
    * FILE_OR_FOLDER_NOT_FOUND -> One or more files or folder paths do not exist
    * RESOURCE_NOT_FOUND -> Resource could not be found
    * FAILED_EXECUTION -> Execution failed
    * SERVICE_UNAVAILABLE -> Service is unavailable
    * UNKNOWN -> Undefined placeholder. Avoid using.
    """

    INVALID_VALUE = "INVALID VALUE"
    UNKNOWN_FIELD = "UNKNOWN FIELD"
    MISSING_FIELD = "MISSING FIELD"
    FILE_OR_FOLDER_NOT_FOUND = "FILE OR FOLDER NOT FOUND"
    RESOURCE_NOT_FOUND = "RESOURCE NOT FOUND"
    FAILED_EXECUTION = "FAILED_EXECUTION"
    SERVICE_UNAVAILABLE = "SERVICE UNAVAILABLE"
    UNKNOWN = "UNKNOWN"


class ErrorBlame(Enum):
    """Source of blame to be specified when using EvaluationException class.

    When using EvaluationException, specify whether the error is due to user actions or the system.
    """

    USER_ERROR = "UserError"
    SYSTEM_ERROR = "SystemError"
    UNKNOWN = "Unknown"


class ErrorTarget(Enum):
    """Error target to be specified when using EvaluationException class.

    When using EvaluationException, specify the code area that was being targeted when the
    exception was triggered.
    """

    EVAL_RUN = "EvalRun"
    CODE_CLIENT = "CodeClient"
    RAI_CLIENT = "RAIClient"
    CHAT_EVALUATOR = "ChatEvaluator"
    COHERENCE_EVALUATOR = "CoherenceEvaluator"
    CONTENT_SAFETY_CHAT_EVALUATOR = "ContentSafetyEvaluator"
    ECI_EVALUATOR = "ECIEvaluator"
    F1_EVALUATOR = "F1Evaluator"
    GROUNDEDNESS_EVALUATOR = "GroundednessEvaluator"
    PROTECTED_MATERIAL_EVALUATOR = "ProtectedMaterialEvaluator"
    RELEVANCE_EVALUATOR = "RelevanceEvaluator"
    SIMILARITY_EVALUATOR = "SimilarityEvaluator"
    INDIRECT_ATTACK_EVALUATOR = "IndirectAttackEvaluator"
    INDIRECT_ATTACK_SIMULATOR = "IndirectAttackSimulator"
    ADVERSARIAL_SIMULATOR = "AdversarialSimulator"
    DIRECT_ATTACK_SIMULATOR = "DirectAttackSimulator"
    EVALUATE = "Evaluate"
    CALLBACK_CONVERSATION_BOT = "CallbackConversationBot"
    MODELS = "Models"
    UNKNOWN = "Unknown"
    CONVERSATION = "Conversation"


class EvaluationException(AzureError):
    """The base class for all exceptions raised in pazure-ai-evaluation. If there is a need to define a custom
    exception type, that custom exception type should extend from this class.

    :param message: A message describing the error. This is the error message the user will see.
    :type message: str
    :param internal_message: The error message without any personal data. This will be pushed to telemetry logs.
    :type internal_message: str
    :param target: The name of the element that caused the exception to be thrown.
    :type target: ~azure.ai.evaluation._exceptions.ErrorTarget
    :param error_category: The error category, defaults to Unknown.
    :type error_category: ~azure.ai.evaluation._exceptionsErrorCategory
    :param error: The original exception if any.
    :type error: Exception
    """

    def __init__(
        self,
        message: str,
        internal_message: str,
        *args,
        target: ErrorTarget = ErrorTarget.UNKNOWN,
        category: ErrorCategory = ErrorCategory.UNKNOWN,
        blame: ErrorBlame = ErrorBlame.UNKNOWN,
        **kwargs,
    ) -> None:
        self.category = category
        self.target = target
        self.blame = blame
        self.internal_message = internal_message
        super().__init__(message, *args, **kwargs)
