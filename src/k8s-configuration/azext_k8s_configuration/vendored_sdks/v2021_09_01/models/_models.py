# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class ErrorAdditionalInfo(msrest.serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: any
    """

    _validation = {
        'type': {'readonly': True},
        'info': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'info': {'key': 'info', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorAdditionalInfo, self).__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorDetail(msrest.serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ErrorAdditionalInfo]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'additional_info': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDetail]'},
        'additional_info': {'key': 'additionalInfo', 'type': '[ErrorAdditionalInfo]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorDetail, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ErrorResponse(msrest.serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.).

    :param error: The error object.
    :type error: ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ErrorDetail
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDetail'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class Resource(msrest.serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class ProxyResource(Resource):
    """The resource model definition for a Azure Resource Manager proxy resource. It will not have tags and a location.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ProxyResource, self).__init__(**kwargs)


class Extension(ProxyResource):
    """The Extension object.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :param identity: Identity of the Extension resource.
    :type identity: ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.Identity
    :ivar system_data: Top level metadata
     https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/common-api-contracts.md#system-metadata-for-all-azure-resources.
    :vartype system_data: ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.SystemData
    :param extension_type: Type of the Extension, of which this resource is an instance of.  It
     must be one of the Extension Types registered with Microsoft.KubernetesConfiguration by the
     Extension publisher.
    :type extension_type: str
    :param auto_upgrade_minor_version: Flag to note if this extension participates in auto upgrade
     of minor version, or not.
    :type auto_upgrade_minor_version: bool
    :param release_train: ReleaseTrain this extension participates in for auto-upgrade (e.g.
     Stable, Preview, etc.) - only if autoUpgradeMinorVersion is 'true'.
    :type release_train: str
    :param version: Version of the extension for this extension, if it is 'pinned' to a specific
     version. autoUpgradeMinorVersion must be 'false'.
    :type version: str
    :param scope: Scope at which the extension is installed.
    :type scope: ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.Scope
    :param configuration_settings: Configuration settings, as name-value pairs for configuring this
     extension.
    :type configuration_settings: dict[str, str]
    :param configuration_protected_settings: Configuration settings that are sensitive, as
     name-value pairs for configuring this extension.
    :type configuration_protected_settings: dict[str, str]
    :ivar provisioning_state: The provisioning state of the extension resource. Possible values
     include: "Succeeded", "Failed", "Canceled", "Creating", "Updating", "Deleting".
    :vartype provisioning_state: str or
     ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ProvisioningState
    :param statuses: Status from this extension.
    :type statuses: list[~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ExtensionStatus]
    :param error_info: The error detail.
    :type error_info: ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ErrorDetail
    :ivar custom_location_settings: Custom Location settings properties.
    :vartype custom_location_settings: dict[str, str]
    :ivar package_uri: Uri of the Helm package.
    :vartype package_uri: str
    :param aks_assigned_identity: Identity of the Extension resource in an AKS cluster.
    :type aks_assigned_identity:
     ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ExtensionPropertiesAksAssignedIdentity
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'custom_location_settings': {'readonly': True},
        'package_uri': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'Identity'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'extension_type': {'key': 'properties.extensionType', 'type': 'str'},
        'auto_upgrade_minor_version': {'key': 'properties.autoUpgradeMinorVersion', 'type': 'bool'},
        'release_train': {'key': 'properties.releaseTrain', 'type': 'str'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'scope': {'key': 'properties.scope', 'type': 'Scope'},
        'configuration_settings': {'key': 'properties.configurationSettings', 'type': '{str}'},
        'configuration_protected_settings': {'key': 'properties.configurationProtectedSettings', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'statuses': {'key': 'properties.statuses', 'type': '[ExtensionStatus]'},
        'error_info': {'key': 'properties.errorInfo', 'type': 'ErrorDetail'},
        'custom_location_settings': {'key': 'properties.customLocationSettings', 'type': '{str}'},
        'package_uri': {'key': 'properties.packageUri', 'type': 'str'},
        'aks_assigned_identity': {'key': 'properties.aksAssignedIdentity', 'type': 'ExtensionPropertiesAksAssignedIdentity'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Extension, self).__init__(**kwargs)
        self.identity = kwargs.get('identity', None)
        self.system_data = None
        self.extension_type = kwargs.get('extension_type', None)
        self.auto_upgrade_minor_version = kwargs.get('auto_upgrade_minor_version', True)
        self.release_train = kwargs.get('release_train', "Stable")
        self.version = kwargs.get('version', None)
        self.scope = kwargs.get('scope', None)
        self.configuration_settings = kwargs.get('configuration_settings', None)
        self.configuration_protected_settings = kwargs.get('configuration_protected_settings', None)
        self.provisioning_state = None
        self.statuses = kwargs.get('statuses', None)
        self.error_info = kwargs.get('error_info', None)
        self.custom_location_settings = None
        self.package_uri = None
        self.aks_assigned_identity = kwargs.get('aks_assigned_identity', None)


class ExtensionPropertiesAksAssignedIdentity(msrest.serialization.Model):
    """Identity of the Extension resource in an AKS cluster.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar principal_id: The principal ID of resource identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of resource.
    :vartype tenant_id: str
    :param type: The identity type. The only acceptable values to pass in are None and
     "SystemAssigned". The default value is None.
    :type type: str
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ExtensionPropertiesAksAssignedIdentity, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = kwargs.get('type', None)


class ExtensionsList(msrest.serialization.Model):
    """Result of the request to list Extensions.  It contains a list of Extension objects and a URL link to get the next set of results.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: List of Extensions within a Kubernetes cluster.
    :vartype value: list[~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.Extension]
    :ivar next_link: URL to get the next set of extension objects, if any.
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Extension]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ExtensionsList, self).__init__(**kwargs)
        self.value = None
        self.next_link = None


class ExtensionStatus(msrest.serialization.Model):
    """Status from the extension.

    :param code: Status code provided by the Extension.
    :type code: str
    :param display_status: Short description of status of the extension.
    :type display_status: str
    :param level: Level of the status. Possible values include: "Error", "Warning", "Information".
     Default value: "Information".
    :type level: str or ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.LevelType
    :param message: Detailed message of the status from the Extension.
    :type message: str
    :param time: DateLiteral (per ISO8601) noting the time of installation status.
    :type time: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'display_status': {'key': 'displayStatus', 'type': 'str'},
        'level': {'key': 'level', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'time': {'key': 'time', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ExtensionStatus, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.display_status = kwargs.get('display_status', None)
        self.level = kwargs.get('level', "Information")
        self.message = kwargs.get('message', None)
        self.time = kwargs.get('time', None)


class Identity(msrest.serialization.Model):
    """Identity for the resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar principal_id: The principal ID of resource identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of resource.
    :vartype tenant_id: str
    :param type: The identity type. The only acceptable values to pass in are None and
     "SystemAssigned". The default value is None.
    :type type: str
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Identity, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = kwargs.get('type', None)


class OperationStatusList(msrest.serialization.Model):
    """The async operations in progress, in the cluster.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: List of async operations in progress, in the cluster.
    :vartype value:
     list[~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.OperationStatusResult]
    :ivar next_link: URL to get the next set of Operation Result objects, if any.
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[OperationStatusResult]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationStatusList, self).__init__(**kwargs)
        self.value = None
        self.next_link = None


class OperationStatusResult(msrest.serialization.Model):
    """The current status of an async operation.

    All required parameters must be populated in order to send to Azure.

    :param id: Fully qualified ID for the async operation.
    :type id: str
    :param name: Name of the async operation.
    :type name: str
    :param status: Required. Operation status.
    :type status: str
    :param properties: Additional information, if available.
    :type properties: dict[str, str]
    :param error: The error detail.
    :type error: ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ErrorDetail
    """

    _validation = {
        'status': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'error': {'key': 'error', 'type': 'ErrorDetail'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationStatusResult, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.status = kwargs['status']
        self.properties = kwargs.get('properties', None)
        self.error = kwargs.get('error', None)


class PatchExtension(msrest.serialization.Model):
    """The Extension Patch Request object.

    :param auto_upgrade_minor_version: Flag to note if this extension participates in auto upgrade
     of minor version, or not.
    :type auto_upgrade_minor_version: bool
    :param release_train: ReleaseTrain this extension participates in for auto-upgrade (e.g.
     Stable, Preview, etc.) - only if autoUpgradeMinorVersion is 'true'.
    :type release_train: str
    :param version: Version of the extension for this extension, if it is 'pinned' to a specific
     version. autoUpgradeMinorVersion must be 'false'.
    :type version: str
    :param configuration_settings: Configuration settings, as name-value pairs for configuring this
     extension.
    :type configuration_settings: dict[str, str]
    :param configuration_protected_settings: Configuration settings that are sensitive, as
     name-value pairs for configuring this extension.
    :type configuration_protected_settings: dict[str, str]
    """

    _attribute_map = {
        'auto_upgrade_minor_version': {'key': 'properties.autoUpgradeMinorVersion', 'type': 'bool'},
        'release_train': {'key': 'properties.releaseTrain', 'type': 'str'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'configuration_settings': {'key': 'properties.configurationSettings', 'type': '{str}'},
        'configuration_protected_settings': {'key': 'properties.configurationProtectedSettings', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PatchExtension, self).__init__(**kwargs)
        self.auto_upgrade_minor_version = kwargs.get('auto_upgrade_minor_version', True)
        self.release_train = kwargs.get('release_train', "Stable")
        self.version = kwargs.get('version', None)
        self.configuration_settings = kwargs.get('configuration_settings', None)
        self.configuration_protected_settings = kwargs.get('configuration_protected_settings', None)


class ResourceProviderOperation(msrest.serialization.Model):
    """Supported operation of this resource provider.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param name: Operation name, in format of {provider}/{resource}/{operation}.
    :type name: str
    :param display: Display metadata associated with the operation.
    :type display:
     ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ResourceProviderOperationDisplay
    :ivar is_data_action: The flag that indicates whether the operation applies to data plane.
    :vartype is_data_action: bool
    :ivar origin: Origin of the operation.
    :vartype origin: str
    """

    _validation = {
        'is_data_action': {'readonly': True},
        'origin': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'ResourceProviderOperationDisplay'},
        'is_data_action': {'key': 'isDataAction', 'type': 'bool'},
        'origin': {'key': 'origin', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceProviderOperation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)
        self.is_data_action = None
        self.origin = None


class ResourceProviderOperationDisplay(msrest.serialization.Model):
    """Display metadata associated with the operation.

    :param provider: Resource provider: Microsoft KubernetesConfiguration.
    :type provider: str
    :param resource: Resource on which the operation is performed.
    :type resource: str
    :param operation: Type of operation: get, read, delete, etc.
    :type operation: str
    :param description: Description of this operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceProviderOperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class ResourceProviderOperationList(msrest.serialization.Model):
    """Result of the request to list operations.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param value: List of operations supported by this resource provider.
    :type value:
     list[~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ResourceProviderOperation]
    :ivar next_link: URL to the next set of results, if any.
    :vartype next_link: str
    """

    _validation = {
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ResourceProviderOperation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceProviderOperationList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = None


class Scope(msrest.serialization.Model):
    """Scope of the extension. It can be either Cluster or Namespace; but not both.

    :param cluster: Specifies that the scope of the extension is Cluster.
    :type cluster: ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ScopeCluster
    :param namespace: Specifies that the scope of the extension is Namespace.
    :type namespace: ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.ScopeNamespace
    """

    _attribute_map = {
        'cluster': {'key': 'cluster', 'type': 'ScopeCluster'},
        'namespace': {'key': 'namespace', 'type': 'ScopeNamespace'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Scope, self).__init__(**kwargs)
        self.cluster = kwargs.get('cluster', None)
        self.namespace = kwargs.get('namespace', None)


class ScopeCluster(msrest.serialization.Model):
    """Specifies that the scope of the extension is Cluster.

    :param release_namespace: Namespace where the extension Release must be placed, for a Cluster
     scoped extension.  If this namespace does not exist, it will be created.
    :type release_namespace: str
    """

    _attribute_map = {
        'release_namespace': {'key': 'releaseNamespace', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ScopeCluster, self).__init__(**kwargs)
        self.release_namespace = kwargs.get('release_namespace', None)


class ScopeNamespace(msrest.serialization.Model):
    """Specifies that the scope of the extension is Namespace.

    :param target_namespace: Namespace where the extension will be created for an Namespace scoped
     extension.  If this namespace does not exist, it will be created.
    :type target_namespace: str
    """

    _attribute_map = {
        'target_namespace': {'key': 'targetNamespace', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ScopeNamespace, self).__init__(**kwargs)
        self.target_namespace = kwargs.get('target_namespace', None)


class SystemData(msrest.serialization.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :param created_by: The identity that created the resource.
    :type created_by: str
    :param created_by_type: The type of identity that created the resource. Possible values
     include: "User", "Application", "ManagedIdentity", "Key".
    :type created_by_type: str or
     ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.CreatedByType
    :param created_at: The timestamp of resource creation (UTC).
    :type created_at: ~datetime.datetime
    :param last_modified_by: The identity that last modified the resource.
    :type last_modified_by: str
    :param last_modified_by_type: The type of identity that last modified the resource. Possible
     values include: "User", "Application", "ManagedIdentity", "Key".
    :type last_modified_by_type: str or
     ~azure.mgmt.kubernetesconfiguration.v2021_09_01.models.CreatedByType
    :param last_modified_at: The timestamp of resource last modification (UTC).
    :type last_modified_at: ~datetime.datetime
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_by_type': {'key': 'createdByType', 'type': 'str'},
        'created_at': {'key': 'createdAt', 'type': 'iso-8601'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'str'},
        'last_modified_by_type': {'key': 'lastModifiedByType', 'type': 'str'},
        'last_modified_at': {'key': 'lastModifiedAt', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SystemData, self).__init__(**kwargs)
        self.created_by = kwargs.get('created_by', None)
        self.created_by_type = kwargs.get('created_by_type', None)
        self.created_at = kwargs.get('created_at', None)
        self.last_modified_by = kwargs.get('last_modified_by', None)
        self.last_modified_by_type = kwargs.get('last_modified_by_type', None)
        self.last_modified_at = kwargs.get('last_modified_at', None)
