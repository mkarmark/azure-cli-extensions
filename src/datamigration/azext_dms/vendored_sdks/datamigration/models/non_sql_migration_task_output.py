# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NonSqlMigrationTaskOutput(Model):
    """Base class for non sql migration task output.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Result identifier
    :vartype id: str
    :ivar started_on: Migration start time
    :vartype started_on: datetime
    :ivar ended_on: Migration end time
    :vartype ended_on: datetime
    :ivar status: Current state of migration. Possible values include:
     'Default', 'Connecting', 'SourceAndTargetSelected', 'SelectLogins',
     'Configured', 'Running', 'Error', 'Stopped', 'Completed',
     'CompletedWithWarnings'
    :vartype status: str or ~azure.mgmt.datamigration.models.MigrationStatus
    :ivar data_migration_table_results: Results of the migration. The key
     contains the table name and the value the table result object
    :vartype data_migration_table_results: dict[str,
     ~azure.mgmt.datamigration.models.NonSqlDataMigrationTableResult]
    :ivar progress_message: Message about the progress of the migration
    :vartype progress_message: str
    :ivar source_server_name: Name of source server
    :vartype source_server_name: str
    :ivar target_server_name: Name of target server
    :vartype target_server_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'started_on': {'readonly': True},
        'ended_on': {'readonly': True},
        'status': {'readonly': True},
        'data_migration_table_results': {'readonly': True},
        'progress_message': {'readonly': True},
        'source_server_name': {'readonly': True},
        'target_server_name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'started_on': {'key': 'startedOn', 'type': 'iso-8601'},
        'ended_on': {'key': 'endedOn', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'str'},
        'data_migration_table_results': {'key': 'dataMigrationTableResults', 'type': '{NonSqlDataMigrationTableResult}'},
        'progress_message': {'key': 'progressMessage', 'type': 'str'},
        'source_server_name': {'key': 'sourceServerName', 'type': 'str'},
        'target_server_name': {'key': 'targetServerName', 'type': 'str'},
    }

    def __init__(self):
        super(NonSqlMigrationTaskOutput, self).__init__()
        self.id = None
        self.started_on = None
        self.ended_on = None
        self.status = None
        self.data_migration_table_results = None
        self.progress_message = None
        self.source_server_name = None
        self.target_server_name = None
