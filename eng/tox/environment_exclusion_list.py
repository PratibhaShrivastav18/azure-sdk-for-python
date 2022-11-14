#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import logging
logging.getLogger().setLevel(logging.INFO)


PYLINT_ACCEPTABLE_FAILURES = [
    "azure-applicationinsights",
    "azure-batch",
    "azure-cognitiveservices-anomalydetector",
    "azure-cognitiveservices-formrecognizer",
    "azure-cognitiveservices-knowledge-nspkg",
    "azure-cognitiveservices-knowledge-qnamaker",
    "azure-cognitiveservices-language-luis",
    "azure-cognitiveservices-language-nspkg",
    "azure-cognitiveservices-language-spellcheck",
    "azure-cognitiveservices-language-textanalytics",
    "azure-cognitiveservices-nspkg",
    "azure-cognitiveservices-personalizer",
    "azure-cognitiveservices-search-autosuggest",
    "azure-cognitiveservices-search-customimagesearch",
    "azure-cognitiveservices-search-customsearch",
    "azure-cognitiveservices-search-entitysearch",
    "azure-cognitiveservices-search-imagesearch",
    "azure-cognitiveservices-search-newssearch",
    "azure-cognitiveservices-search-nspkg",
    "azure-cognitiveservices-search-videosearch",
    "azure-cognitiveservices-search-visualsearch",
    "azure-cognitiveservices-search-websearch",
    "azure-cognitiveservices-vision-computervision",
    "azure-cognitiveservices-vision-contentmoderator",
    "azure-cognitiveservices-vision-customvision",
    "azure-cognitiveservices-vision-face",
    "azure-cognitiveservices-vision-nspkg",
    "azure-common",
    "azure-nspkg",
    "azure-servicemanagement-legacy",
    "azure-graphrbac",
    "azure-loganalytics",
    "azure-servicefabric",
    "azure-template",
    "azure-keyvault",
    "azure-synapse",
    "azure-synapse-artifacts",
    "azure-synapse-spark",
    "azure-synapse-accesscontrol",
    "azure-synapse-monitoring",
    "azure-synapse-managedprivateendpoints",
    "azure-synapse-nspkg",
    "azure-ai-anomalydetector",
    "azure-security-attestation",
    "azure-iot-deviceupdate",
    "azure-purview-nspkg",
    "azure-purview-scanning",
    "azure-purview-catalog",
    "azure-purview-account",
    "azure-purview-administration",
    "azure-messaging-nspkg",
    "azure-agrifood-farming",
    "azure-developer-loadtesting",
    "azure-developer-devcenter"
]

# omit package from running mypy checks
MYPY_OPT_OUT = [
  "azure-agrifood-farming",
  "azure-ai-anomalydetector",
  "azure-appconfiguration-provider",
  "azure-security-attestation",
  "azure-batch",
  "azure-communication-chat",
  "azure-communication-email",
  "azure-communication-identity",
  "azure-communication-jobrouter",
  "azure-communication-networktraversal",
  "azure-communication-phonenumbers",
  "azure-communication-rooms",
  "azure-communication-sms",
  "azure-confidentialledger",
  "azure-containerregistry",
  "azure-mgmt-core",
  "azure-core-experimental",
  "azure-core-tracing-opencensus",
  "azure-core-tracing-opentelemetry",
  "azure-iot-deviceupdate",
  "azure-digitaltwins-core",
  "azure-eventhub-checkpointstoreblob",
  "azure-eventhub-checkpointstoreblob-aio",
  "azure-eventhub-checkpointstoretable",
  "azure-developer-loadtesting",
  "azure-maps-geolocation",
  "azure-maps-render",
  "azure-maps-route",
  "azure-maps-search",
  "azure-mixedreality-authentication",
  "azure-ai-ml",
  "azure-iot-modelsrepository",
  "azure-monitor-ingestion",
  "azure-monitor-opentelemetry-exporter",
  "azure-monitor-query",
  "azure-purview-administration",
  "azure-purview-catalog",
  "azure-purview-scanning",
  "azure-schemaregistry",
  "azure-schemaregistry-avroencoder",
  "azure-search-documents",
  "azure-storage-blob",
  "azure-storage-blob-changefeed",
  "azure-storage-file-datalake",
  "azure-storage-file-share",
  "azure-storage-queue",
  "azure-synapse-accesscontrol",
  "azure-synapse-artifacts",
  "azure-synapse-managedprivateendpoints",
  "azure-synapse-monitoring",
  "azure-synapse-spark",
  "azure-messaging-webpubsubservice",
]

# omit package from running pyright checks
PYRIGHT_OPT_OUT = [
  "azure-agrifood-farming",
  "azure-ai-anomalydetector",
  "azure-appconfiguration",
  "azure-appconfiguration-provider",
  "azure-security-attestation",
  "azure-batch",
  "azure-ai-language-conversations",
  "azure-ai-language-questionanswering",
  "azure-communication-chat",
  "azure-communication-email",
  "azure-communication-identity",
  "azure-communication-jobrouter",
  "azure-communication-networktraversal",
  "azure-communication-phonenumbers",
  "azure-communication-rooms",
  "azure-communication-sms",
  "azure-confidentialledger",
  "azure-containerregistry",
  "azure-core",
  "azure-mgmt-core",
  "azure-core-experimental",
  "azure-core-tracing-opencensus",
  "azure-core-tracing-opentelemetry",
  "azure-cosmos",
  "azure-developer-devcenter",
  "azure-iot-deviceupdate",
  "azure-digitaltwins-core",
  "azure-eventgrid",
  "azure-eventhub",
  "azure-eventhub-checkpointstoreblob",
  "azure-eventhub-checkpointstoreblob-aio",
  "azure-eventhub-checkpointstoretable",
  "azure-ai-formrecognizer",
  "azure-identity",
  "azure-keyvault-administration",
  "azure-keyvault-certificates",
  "azure-keyvault-keys",
  "azure-keyvault-secrets",
  "azure-developer-loadtesting",
  "azure-maps-geolocation",
  "azure-maps-render",
  "azure-maps-route",
  "azure-maps-search",
  "azure-ai-metricsadvisor",
  "azure-mixedreality-authentication",
  "azure-ai-ml",
  "azure-iot-modelsrepository",
  "azure-monitor-ingestion",
  "azure-monitor-opentelemetry-exporter",
  "azure-monitor-query",
  "azure-ai-personalizer",
  "azure-purview-administration",
  "azure-purview-catalog",
  "azure-purview-scanning",
  "azure-mixedreality-remoterendering",
  "azure-schemaregistry",
  "azure-schemaregistry-avroencoder",
  "azure-search-documents",
  "azure-servicebus",
  "azure-storage-blob",
  "azure-storage-blob-changefeed",
  "azure-storage-file-datalake",
  "azure-storage-file-share",
  "azure-storage-queue",
  "azure-synapse-accesscontrol",
  "azure-synapse-artifacts",
  "azure-synapse-managedprivateendpoints",
  "azure-synapse-monitoring",
  "azure-synapse-spark",
  "azure-data-tables",
  "azure-ai-textanalytics",
  "azure-ai-translation-document",
  "azure-messaging-webpubsubservice",
]

# omit package from running verifytypes checks
VERIFYTYPES_OPT_OUT = [
  "azure-agrifood-farming",
  "azure-ai-anomalydetector",
  "azure-appconfiguration",
  "azure-appconfiguration-provider",
  "azure-security-attestation",
  "azure-batch",
  "azure-ai-language-conversations",
  "azure-ai-language-questionanswering",
  "azure-communication-chat",
  "azure-communication-email",
  "azure-communication-identity",
  "azure-communication-jobrouter",
  "azure-communication-networktraversal",
  "azure-communication-phonenumbers",
  "azure-communication-rooms",
  "azure-communication-sms",
  "azure-confidentialledger",
  "azure-containerregistry",
  "azure-core",
  "azure-mgmt-core",
  "azure-core-experimental",
  "azure-core-tracing-opencensus",
  "azure-core-tracing-opentelemetry",
  "azure-cosmos",
  "azure-developer-devcenter",
  "azure-iot-deviceupdate",
  "azure-digitaltwins-core",
  "azure-eventgrid",
  "azure-eventhub",
  "azure-eventhub-checkpointstoreblob",
  "azure-eventhub-checkpointstoreblob-aio",
  "azure-eventhub-checkpointstoretable",
  "azure-ai-formrecognizer",
  "azure-identity",
  "azure-keyvault-administration",
  "azure-keyvault-certificates",
  "azure-keyvault-keys",
  "azure-keyvault-secrets",
  "azure-developer-loadtesting",
  "azure-maps-geolocation",
  "azure-maps-render",
  "azure-maps-route",
  "azure-maps-search",
  "azure-ai-metricsadvisor",
  "azure-mixedreality-authentication",
  "azure-ai-ml",
  "azure-iot-modelsrepository",
  "azure-monitor-ingestion",
  "azure-monitor-opentelemetry-exporter",
  "azure-monitor-query",
  "azure-ai-personalizer",
  "azure-purview-administration",
  "azure-purview-catalog",
  "azure-purview-scanning",
  "azure-mixedreality-remoterendering",
  "azure-schemaregistry",
  "azure-schemaregistry-avroencoder",
  "azure-search-documents",
  "azure-servicebus",
  "azure-storage-blob",
  "azure-storage-blob-changefeed",
  "azure-storage-file-datalake",
  "azure-storage-file-share",
  "azure-storage-queue",
  "azure-synapse-accesscontrol",
  "azure-synapse-artifacts",
  "azure-synapse-managedprivateendpoints",
  "azure-synapse-monitoring",
  "azure-synapse-spark",
  "azure-ai-textanalytics",
  "azure-data-tables",
  "azure-messaging-webpubsubservice",

]

# omit package from running type checkers on samples
# note: if removed from this list, you must enable one or both of mypy or pyright checks.
TYPE_CHECK_SAMPLES_OPT_OUT = [
  "azure-agrifood-farming",
  "azure-ai-anomalydetector",
  "azure-appconfiguration",
  "azure-appconfiguration-provider",
  "azure-security-attestation",
  "azure-batch",
  "azure-ai-language-conversations",
  "azure-ai-language-questionanswering",
  "azure-communication-chat",
  "azure-communication-email",
  "azure-communication-identity",
  "azure-communication-jobrouter",
  "azure-communication-networktraversal",
  "azure-communication-phonenumbers",
  "azure-communication-rooms",
  "azure-communication-sms",
  "azure-confidentialledger",
  "azure-containerregistry",
  "azure-core",
  "azure-mgmt-core",
  "azure-core-experimental",
  "azure-core-tracing-opencensus",
  "azure-core-tracing-opentelemetry",
  "azure-cosmos",
  "azure-developer-devcenter",
  "azure-iot-deviceupdate",
  "azure-digitaltwins-core",
  "azure-eventgrid",
  "azure-eventhub",
  "azure-eventhub-checkpointstoreblob",
  "azure-eventhub-checkpointstoreblob-aio",
  "azure-eventhub-checkpointstoretable",
  "azure-ai-formrecognizer",
  "azure-keyvault-administration",
  "azure-keyvault-certificates",
  "azure-keyvault-keys",
  "azure-keyvault-secrets",
  "azure-developer-loadtesting",
  "azure-maps-geolocation",
  "azure-maps-render",
  "azure-maps-route",
  "azure-maps-search",
  "azure-mixedreality-authentication",
  "azure-ai-ml",
  "azure-iot-modelsrepository",
  "azure-monitor-ingestion",
  "azure-monitor-opentelemetry-exporter",
  "azure-monitor-query",
  "azure-purview-administration",
  "azure-purview-catalog",
  "azure-purview-scanning",
  "azure-mixedreality-remoterendering",
  "azure-schemaregistry",
  "azure-schemaregistry-avroencoder",
  "azure-search-documents",
  "azure-servicebus",
  "azure-storage-blob",
  "azure-storage-blob-changefeed",
  "azure-storage-file-datalake",
  "azure-storage-file-share",
  "azure-storage-queue",
  "azure-synapse-accesscontrol",
  "azure-synapse-artifacts",
  "azure-synapse-managedprivateendpoints",
  "azure-synapse-monitoring",
  "azure-synapse-spark",
  "azure-ai-translation-document",
  "azure-messaging-webpubsubservice",
]


# --------------------------------------------------------------------------------------------------------------------
# DO NOT add packages to the below lists. They are used to omit packages that will never run type checking.

IGNORE_FILTER = ["nspkg", "mgmt", "cognitiveservices"]
FILTER_EXCLUSIONS = ["azure-mgmt-core"]
IGNORE_PACKAGES = [
  "azure-applicationinsights",
  "azure-servicemanagement-legacy",
  "azure",
  "azure-storage",
  "azure-monitor",
  "azure-servicefabric",
  "azure-keyvault",
  "azure-synapse",
  "azure-common",
  "conda-recipe",
  "azure-graphrbac",
  "azure-loganalytics",
  "azure-media-analytics-edge",
  "azure-media-videoanalyzer-edge",
  "azure-template",
]


def is_ignored_package(package_name):
    if package_name in IGNORE_PACKAGES:
        return True
    if package_name not in FILTER_EXCLUSIONS and any([identifier in package_name for identifier in IGNORE_FILTER]):
        return True
    return False
