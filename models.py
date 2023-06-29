# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.IntegerField()
    primary = models.IntegerField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ColumnsPriv(models.Model):
    host = models.CharField(db_column='Host', primary_key=True, max_length=255, db_collation='ascii_general_ci')  # Field name made lowercase.
    db = models.CharField(db_column='Db', max_length=64)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=32)  # Field name made lowercase.
    table_name = models.CharField(db_column='Table_name', max_length=64)  # Field name made lowercase.
    column_name = models.CharField(db_column='Column_name', max_length=64)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.
    column_priv = models.CharField(db_column='Column_priv', max_length=31, db_collation='utf8mb3_general_ci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'columns_priv'
        unique_together = (('host', 'user', 'db', 'table_name', 'column_name'),)


class CompanyInfoCompanyList(models.Model):
    id = models.BigAutoField(primary_key=True)
    com_name = models.CharField(max_length=100)
    com_png = models.CharField(max_length=200)
    com_rank = models.CharField(max_length=7)
    com_in = models.TextField()

    class Meta:
        managed = False
        db_table = 'company_info_company_list'


class Component(models.Model):
    component_id = models.AutoField(primary_key=True)
    component_group_id = models.PositiveIntegerField()
    component_urn = models.TextField()

    class Meta:
        managed = False
        db_table = 'component'


class Db(models.Model):
    host = models.CharField(db_column='Host', primary_key=True, max_length=255, db_collation='ascii_general_ci')  # Field name made lowercase.
    db = models.CharField(db_column='Db', max_length=64)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=32)  # Field name made lowercase.
    select_priv = models.CharField(db_column='Select_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    insert_priv = models.CharField(db_column='Insert_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    update_priv = models.CharField(db_column='Update_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    delete_priv = models.CharField(db_column='Delete_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    create_priv = models.CharField(db_column='Create_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    drop_priv = models.CharField(db_column='Drop_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    grant_priv = models.CharField(db_column='Grant_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    references_priv = models.CharField(db_column='References_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    index_priv = models.CharField(db_column='Index_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    alter_priv = models.CharField(db_column='Alter_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    create_tmp_table_priv = models.CharField(db_column='Create_tmp_table_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    lock_tables_priv = models.CharField(db_column='Lock_tables_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    create_view_priv = models.CharField(db_column='Create_view_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    show_view_priv = models.CharField(db_column='Show_view_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    create_routine_priv = models.CharField(db_column='Create_routine_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    alter_routine_priv = models.CharField(db_column='Alter_routine_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    execute_priv = models.CharField(db_column='Execute_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    event_priv = models.CharField(db_column='Event_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    trigger_priv = models.CharField(db_column='Trigger_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'db'
        unique_together = (('host', 'user', 'db'),)


class DefaultRoles(models.Model):
    host = models.CharField(db_column='HOST', primary_key=True, max_length=255, db_collation='ascii_general_ci')  # Field name made lowercase.
    user = models.CharField(db_column='USER', max_length=32)  # Field name made lowercase.
    default_role_host = models.CharField(db_column='DEFAULT_ROLE_HOST', max_length=255, db_collation='ascii_general_ci')  # Field name made lowercase.
    default_role_user = models.CharField(db_column='DEFAULT_ROLE_USER', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'default_roles'
        unique_together = (('host', 'user', 'default_role_host', 'default_role_user'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class EngineCost(models.Model):
    engine_name = models.CharField(max_length=64)
    device_type = models.IntegerField()
    cost_name = models.CharField(primary_key=True, max_length=64)
    cost_value = models.FloatField(blank=True, null=True)
    last_update = models.DateTimeField()
    comment = models.CharField(max_length=1024, blank=True, null=True)
    default_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engine_cost'
        unique_together = (('cost_name', 'engine_name', 'device_type'),)


class Func(models.Model):
    name = models.CharField(primary_key=True, max_length=64)
    ret = models.IntegerField()
    dl = models.CharField(max_length=128)
    type = models.CharField(max_length=9, db_collation='utf8mb3_general_ci')

    class Meta:
        managed = False
        db_table = 'func'


class GeneralLog(models.Model):
    event_time = models.DateTimeField()
    user_host = models.TextField()
    thread_id = models.PositiveBigIntegerField()
    server_id = models.PositiveIntegerField()
    command_type = models.CharField(max_length=64)
    argument = models.TextField()

    class Meta:
        managed = False
        db_table = 'general_log'


class GlobalGrants(models.Model):
    user = models.CharField(db_column='USER', primary_key=True, max_length=32)  # Field name made lowercase.
    host = models.CharField(db_column='HOST', max_length=255, db_collation='ascii_general_ci')  # Field name made lowercase.
    priv = models.CharField(db_column='PRIV', max_length=32, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    with_grant_option = models.CharField(db_column='WITH_GRANT_OPTION', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'global_grants'
        unique_together = (('user', 'host', 'priv'),)


class GtidExecuted(models.Model):
    source_uuid = models.CharField(primary_key=True, max_length=36)
    interval_start = models.BigIntegerField()
    interval_end = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'gtid_executed'
        unique_together = (('source_uuid', 'interval_start'),)


class HelpCategory(models.Model):
    help_category_id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    parent_category_id = models.PositiveSmallIntegerField(blank=True, null=True)
    url = models.TextField()

    class Meta:
        managed = False
        db_table = 'help_category'


class HelpKeyword(models.Model):
    help_keyword_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'help_keyword'


class HelpRelation(models.Model):
    help_topic_id = models.PositiveIntegerField()
    help_keyword_id = models.PositiveIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'help_relation'
        unique_together = (('help_keyword_id', 'help_topic_id'),)


class HelpTopic(models.Model):
    help_topic_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    help_category_id = models.PositiveSmallIntegerField()
    description = models.TextField()
    example = models.TextField()
    url = models.TextField()

    class Meta:
        managed = False
        db_table = 'help_topic'


class InnodbIndexStats(models.Model):
    database_name = models.CharField(primary_key=True, max_length=64)
    table_name = models.CharField(max_length=199)
    index_name = models.CharField(max_length=64)
    last_update = models.DateTimeField()
    stat_name = models.CharField(max_length=64)
    stat_value = models.PositiveBigIntegerField()
    sample_size = models.PositiveBigIntegerField(blank=True, null=True)
    stat_description = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'innodb_index_stats'
        unique_together = (('database_name', 'table_name', 'index_name', 'stat_name'),)


class InnodbTableStats(models.Model):
    database_name = models.CharField(primary_key=True, max_length=64)
    table_name = models.CharField(max_length=199)
    last_update = models.DateTimeField()
    n_rows = models.PositiveBigIntegerField()
    clustered_index_size = models.PositiveBigIntegerField()
    sum_of_other_index_sizes = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'innodb_table_stats'
        unique_together = (('database_name', 'table_name'),)


class NdbBinlogIndex(models.Model):
    position = models.PositiveBigIntegerField(db_column='Position')  # Field name made lowercase.
    file = models.CharField(db_column='File', max_length=255)  # Field name made lowercase.
    epoch = models.PositiveBigIntegerField(primary_key=True)
    inserts = models.PositiveIntegerField()
    updates = models.PositiveIntegerField()
    deletes = models.PositiveIntegerField()
    schemaops = models.PositiveIntegerField()
    orig_server_id = models.PositiveIntegerField()
    orig_epoch = models.PositiveBigIntegerField()
    gci = models.PositiveIntegerField()
    next_position = models.PositiveBigIntegerField()
    next_file = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ndb_binlog_index'
        unique_together = (('epoch', 'orig_server_id', 'orig_epoch'),)


class PasswordHistory(models.Model):
    host = models.CharField(db_column='Host', primary_key=True, max_length=255, db_collation='ascii_general_ci')  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=32)  # Field name made lowercase.
    password_timestamp = models.DateTimeField(db_column='Password_timestamp')  # Field name made lowercase.
    password = models.TextField(db_column='Password', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'password_history'
        unique_together = (('host', 'user', 'password_timestamp'),)


class Plugin(models.Model):
    name = models.CharField(primary_key=True, max_length=64)
    dl = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'plugin'


class ProcsPriv(models.Model):
    host = models.CharField(db_column='Host', primary_key=True, max_length=255, db_collation='ascii_general_ci')  # Field name made lowercase.
    db = models.CharField(db_column='Db', max_length=64)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=32)  # Field name made lowercase.
    routine_name = models.CharField(db_column='Routine_name', max_length=64, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    routine_type = models.CharField(db_column='Routine_type', max_length=9)  # Field name made lowercase.
    grantor = models.CharField(db_column='Grantor', max_length=288)  # Field name made lowercase.
    proc_priv = models.CharField(db_column='Proc_priv', max_length=27, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'procs_priv'
        unique_together = (('host', 'user', 'db', 'routine_name', 'routine_type'),)


class ProxiesPriv(models.Model):
    host = models.CharField(db_column='Host', primary_key=True, max_length=255, db_collation='ascii_general_ci')  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=32)  # Field name made lowercase.
    proxied_host = models.CharField(db_column='Proxied_host', max_length=255, db_collation='ascii_general_ci')  # Field name made lowercase.
    proxied_user = models.CharField(db_column='Proxied_user', max_length=32)  # Field name made lowercase.
    with_grant = models.IntegerField(db_column='With_grant')  # Field name made lowercase.
    grantor = models.CharField(db_column='Grantor', max_length=288)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proxies_priv'
        unique_together = (('host', 'user', 'proxied_host', 'proxied_user'),)


class RecruitingRecruitingList(models.Model):
    id = models.BigAutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    company_intro = models.TextField()
    main_duties = models.TextField()
    requirments = models.TextField()
    stack = models.TextField()
    desirable_skills = models.TextField()
    employee_benefits = models.TextField()
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'recruiting_recruiting_list'


class ReplicationAsynchronousConnectionFailover(models.Model):
    channel_name = models.CharField(db_column='Channel_name', primary_key=True, max_length=64)  # Field name made lowercase.
    host = models.CharField(db_column='Host', max_length=255, db_collation='ascii_general_ci')  # Field name made lowercase.
    port = models.PositiveIntegerField(db_column='Port')  # Field name made lowercase.
    network_namespace = models.CharField(db_column='Network_namespace', max_length=64)  # Field name made lowercase.
    weight = models.PositiveIntegerField(db_column='Weight')  # Field name made lowercase.
    managed_name = models.CharField(db_column='Managed_name', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'replication_asynchronous_connection_failover'
        unique_together = (('channel_name', 'host', 'port', 'network_namespace', 'managed_name'),)


class ReplicationAsynchronousConnectionFailoverManaged(models.Model):
    channel_name = models.CharField(db_column='Channel_name', primary_key=True, max_length=64)  # Field name made lowercase.
    managed_name = models.CharField(db_column='Managed_name', max_length=64)  # Field name made lowercase.
    managed_type = models.CharField(db_column='Managed_type', max_length=64)  # Field name made lowercase.
    configuration = models.JSONField(db_column='Configuration', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'replication_asynchronous_connection_failover_managed'
        unique_together = (('channel_name', 'managed_name'),)


class ReplicationGroupConfigurationVersion(models.Model):
    name = models.CharField(primary_key=True, max_length=255, db_collation='ascii_general_ci')
    version = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'replication_group_configuration_version'


class ReplicationGroupMemberActions(models.Model):
    name = models.CharField(primary_key=True, max_length=255, db_collation='ascii_general_ci')
    event = models.CharField(max_length=64, db_collation='ascii_general_ci')
    enabled = models.IntegerField()
    type = models.CharField(max_length=64, db_collation='ascii_general_ci')
    priority = models.PositiveIntegerField()
    error_handling = models.CharField(max_length=64, db_collation='ascii_general_ci')

    class Meta:
        managed = False
        db_table = 'replication_group_member_actions'
        unique_together = (('name', 'event'),)


class RoleEdges(models.Model):
    from_host = models.CharField(db_column='FROM_HOST', primary_key=True, max_length=255, db_collation='ascii_general_ci')  # Field name made lowercase.
    from_user = models.CharField(db_column='FROM_USER', max_length=32)  # Field name made lowercase.
    to_host = models.CharField(db_column='TO_HOST', max_length=255, db_collation='ascii_general_ci')  # Field name made lowercase.
    to_user = models.CharField(db_column='TO_USER', max_length=32)  # Field name made lowercase.
    with_admin_option = models.CharField(db_column='WITH_ADMIN_OPTION', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'role_edges'
        unique_together = (('from_host', 'from_user', 'to_host', 'to_user'),)


class ServerCost(models.Model):
    cost_name = models.CharField(primary_key=True, max_length=64)
    cost_value = models.FloatField(blank=True, null=True)
    last_update = models.DateTimeField()
    comment = models.CharField(max_length=1024, blank=True, null=True)
    default_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'server_cost'


class Servers(models.Model):
    server_name = models.CharField(db_column='Server_name', primary_key=True, max_length=64)  # Field name made lowercase.
    host = models.CharField(db_column='Host', max_length=255, db_collation='ascii_general_ci')  # Field name made lowercase.
    db = models.CharField(db_column='Db', max_length=64)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=64)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=64)  # Field name made lowercase.
    port = models.IntegerField(db_column='Port')  # Field name made lowercase.
    socket = models.CharField(db_column='Socket', max_length=64)  # Field name made lowercase.
    wrapper = models.CharField(db_column='Wrapper', max_length=64)  # Field name made lowercase.
    owner = models.CharField(db_column='Owner', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servers'


class SlaveMasterInfo(models.Model):
    number_of_lines = models.PositiveIntegerField(db_column='Number_of_lines')  # Field name made lowercase.
    master_log_name = models.TextField(db_column='Master_log_name', db_collation='utf8mb3_bin')  # Field name made lowercase.
    master_log_pos = models.PositiveBigIntegerField(db_column='Master_log_pos')  # Field name made lowercase.
    host = models.CharField(db_column='Host', max_length=255, db_collation='ascii_general_ci', blank=True, null=True)  # Field name made lowercase.
    user_name = models.TextField(db_column='User_name', db_collation='utf8mb3_bin', blank=True, null=True)  # Field name made lowercase.
    user_password = models.TextField(db_column='User_password', db_collation='utf8mb3_bin', blank=True, null=True)  # Field name made lowercase.
    port = models.PositiveIntegerField(db_column='Port')  # Field name made lowercase.
    connect_retry = models.PositiveIntegerField(db_column='Connect_retry')  # Field name made lowercase.
    enabled_ssl = models.IntegerField(db_column='Enabled_ssl')  # Field name made lowercase.
    ssl_ca = models.TextField(db_column='Ssl_ca', db_collation='utf8mb3_bin', blank=True, null=True)  # Field name made lowercase.
    ssl_capath = models.TextField(db_column='Ssl_capath', db_collation='utf8mb3_bin', blank=True, null=True)  # Field name made lowercase.
    ssl_cert = models.TextField(db_column='Ssl_cert', db_collation='utf8mb3_bin', blank=True, null=True)  # Field name made lowercase.
    ssl_cipher = models.TextField(db_column='Ssl_cipher', db_collation='utf8mb3_bin', blank=True, null=True)  # Field name made lowercase.
    ssl_key = models.TextField(db_column='Ssl_key', db_collation='utf8mb3_bin', blank=True, null=True)  # Field name made lowercase.
    ssl_verify_server_cert = models.IntegerField(db_column='Ssl_verify_server_cert')  # Field name made lowercase.
    heartbeat = models.FloatField(db_column='Heartbeat')  # Field name made lowercase.
    bind = models.TextField(db_column='Bind', db_collation='utf8mb3_bin', blank=True, null=True)  # Field name made lowercase.
    ignored_server_ids = models.TextField(db_column='Ignored_server_ids', db_collation='utf8mb3_bin', blank=True, null=True)  # Field name made lowercase.
    uuid = models.TextField(db_column='Uuid', db_collation='utf8mb3_bin', blank=True, null=True)  # Field name made lowercase.
    retry_count = models.PositiveBigIntegerField(db_column='Retry_count')  # Field name made lowercase.
    ssl_crl = models.TextField(db_column='Ssl_crl', db_collation='utf8mb3_bin', blank=True, null=True)  # Field name made lowercase.
    ssl_crlpath = models.TextField(db_column='Ssl_crlpath', db_collation='utf8mb3_bin', blank=True, null=True)  # Field name made lowercase.
    enabled_auto_position = models.IntegerField(db_column='Enabled_auto_position')  # Field name made lowercase.
    channel_name = models.CharField(db_column='Channel_name', primary_key=True, max_length=64)  # Field name made lowercase.
    tls_version = models.TextField(db_column='Tls_version', db_collation='utf8mb3_bin', blank=True, null=True)  # Field name made lowercase.
    public_key_path = models.TextField(db_column='Public_key_path', db_collation='utf8mb3_bin', blank=True, null=True)  # Field name made lowercase.
    get_public_key = models.IntegerField(db_column='Get_public_key')  # Field name made lowercase.
    network_namespace = models.TextField(db_column='Network_namespace', db_collation='utf8mb3_bin', blank=True, null=True)  # Field name made lowercase.
    master_compression_algorithm = models.CharField(db_column='Master_compression_algorithm', max_length=64, db_collation='utf8mb3_bin')  # Field name made lowercase.
    master_zstd_compression_level = models.PositiveIntegerField(db_column='Master_zstd_compression_level')  # Field name made lowercase.
    tls_ciphersuites = models.TextField(db_column='Tls_ciphersuites', db_collation='utf8mb3_bin', blank=True, null=True)  # Field name made lowercase.
    source_connection_auto_failover = models.IntegerField(db_column='Source_connection_auto_failover')  # Field name made lowercase.
    gtid_only = models.IntegerField(db_column='Gtid_only')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'slave_master_info'


class SlaveRelayLogInfo(models.Model):
    number_of_lines = models.PositiveIntegerField(db_column='Number_of_lines')  # Field name made lowercase.
    relay_log_name = models.TextField(db_column='Relay_log_name', db_collation='utf8mb3_bin', blank=True, null=True)  # Field name made lowercase.
    relay_log_pos = models.PositiveBigIntegerField(db_column='Relay_log_pos', blank=True, null=True)  # Field name made lowercase.
    master_log_name = models.TextField(db_column='Master_log_name', db_collation='utf8mb3_bin', blank=True, null=True)  # Field name made lowercase.
    master_log_pos = models.PositiveBigIntegerField(db_column='Master_log_pos', blank=True, null=True)  # Field name made lowercase.
    sql_delay = models.IntegerField(db_column='Sql_delay', blank=True, null=True)  # Field name made lowercase.
    number_of_workers = models.PositiveIntegerField(db_column='Number_of_workers', blank=True, null=True)  # Field name made lowercase.
    id = models.PositiveIntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    channel_name = models.CharField(db_column='Channel_name', primary_key=True, max_length=64)  # Field name made lowercase.
    privilege_checks_username = models.CharField(db_column='Privilege_checks_username', max_length=32, db_collation='utf8mb3_bin', blank=True, null=True)  # Field name made lowercase.
    privilege_checks_hostname = models.CharField(db_column='Privilege_checks_hostname', max_length=255, db_collation='ascii_general_ci', blank=True, null=True)  # Field name made lowercase.
    require_row_format = models.IntegerField(db_column='Require_row_format')  # Field name made lowercase.
    require_table_primary_key_check = models.CharField(db_column='Require_table_primary_key_check', max_length=8)  # Field name made lowercase.
    assign_gtids_to_anonymous_transactions_type = models.CharField(db_column='Assign_gtids_to_anonymous_transactions_type', max_length=5)  # Field name made lowercase.
    assign_gtids_to_anonymous_transactions_value = models.TextField(db_column='Assign_gtids_to_anonymous_transactions_value', db_collation='utf8mb3_bin', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'slave_relay_log_info'


class SlaveWorkerInfo(models.Model):
    id = models.PositiveIntegerField(db_column='Id')  # Field name made lowercase.
    relay_log_name = models.TextField(db_column='Relay_log_name', db_collation='utf8mb3_bin')  # Field name made lowercase.
    relay_log_pos = models.PositiveBigIntegerField(db_column='Relay_log_pos')  # Field name made lowercase.
    master_log_name = models.TextField(db_column='Master_log_name', db_collation='utf8mb3_bin')  # Field name made lowercase.
    master_log_pos = models.PositiveBigIntegerField(db_column='Master_log_pos')  # Field name made lowercase.
    checkpoint_relay_log_name = models.TextField(db_column='Checkpoint_relay_log_name', db_collation='utf8mb3_bin')  # Field name made lowercase.
    checkpoint_relay_log_pos = models.PositiveBigIntegerField(db_column='Checkpoint_relay_log_pos')  # Field name made lowercase.
    checkpoint_master_log_name = models.TextField(db_column='Checkpoint_master_log_name', db_collation='utf8mb3_bin')  # Field name made lowercase.
    checkpoint_master_log_pos = models.PositiveBigIntegerField(db_column='Checkpoint_master_log_pos')  # Field name made lowercase.
    checkpoint_seqno = models.PositiveIntegerField(db_column='Checkpoint_seqno')  # Field name made lowercase.
    checkpoint_group_size = models.PositiveIntegerField(db_column='Checkpoint_group_size')  # Field name made lowercase.
    checkpoint_group_bitmap = models.TextField(db_column='Checkpoint_group_bitmap')  # Field name made lowercase.
    channel_name = models.CharField(db_column='Channel_name', primary_key=True, max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'slave_worker_info'
        unique_together = (('channel_name', 'id'),)


class SlowLog(models.Model):
    start_time = models.DateTimeField()
    user_host = models.TextField()
    query_time = models.TimeField()
    lock_time = models.TimeField()
    rows_sent = models.IntegerField()
    rows_examined = models.IntegerField()
    db = models.CharField(max_length=512)
    last_insert_id = models.IntegerField()
    insert_id = models.IntegerField()
    server_id = models.PositiveIntegerField()
    sql_text = models.TextField()
    thread_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'slow_log'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    id = models.BigAutoField(primary_key=True)
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class TablesPriv(models.Model):
    host = models.CharField(db_column='Host', primary_key=True, max_length=255, db_collation='ascii_general_ci')  # Field name made lowercase.
    db = models.CharField(db_column='Db', max_length=64)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=32)  # Field name made lowercase.
    table_name = models.CharField(db_column='Table_name', max_length=64)  # Field name made lowercase.
    grantor = models.CharField(db_column='Grantor', max_length=288)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.
    table_priv = models.CharField(db_column='Table_priv', max_length=98, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    column_priv = models.CharField(db_column='Column_priv', max_length=31, db_collation='utf8mb3_general_ci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tables_priv'
        unique_together = (('host', 'user', 'db', 'table_name'),)


class TimeZone(models.Model):
    time_zone_id = models.AutoField(db_column='Time_zone_id', primary_key=True)  # Field name made lowercase.
    use_leap_seconds = models.CharField(db_column='Use_leap_seconds', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'time_zone'


class TimeZoneLeapSecond(models.Model):
    transition_time = models.BigIntegerField(db_column='Transition_time', primary_key=True)  # Field name made lowercase.
    correction = models.IntegerField(db_column='Correction')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'time_zone_leap_second'


class TimeZoneName(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=64)  # Field name made lowercase.
    time_zone_id = models.PositiveIntegerField(db_column='Time_zone_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'time_zone_name'


class TimeZoneTransition(models.Model):
    time_zone_id = models.PositiveIntegerField(db_column='Time_zone_id', primary_key=True)  # Field name made lowercase.
    transition_time = models.BigIntegerField(db_column='Transition_time')  # Field name made lowercase.
    transition_type_id = models.PositiveIntegerField(db_column='Transition_type_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'time_zone_transition'
        unique_together = (('time_zone_id', 'transition_time'),)


class TimeZoneTransitionType(models.Model):
    time_zone_id = models.PositiveIntegerField(db_column='Time_zone_id', primary_key=True)  # Field name made lowercase.
    transition_type_id = models.PositiveIntegerField(db_column='Transition_type_id')  # Field name made lowercase.
    offset = models.IntegerField(db_column='Offset')  # Field name made lowercase.
    is_dst = models.PositiveIntegerField(db_column='Is_DST')  # Field name made lowercase.
    abbreviation = models.CharField(db_column='Abbreviation', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'time_zone_transition_type'
        unique_together = (('time_zone_id', 'transition_type_id'),)


class User(models.Model):
    host = models.CharField(db_column='Host', primary_key=True, max_length=255, db_collation='ascii_general_ci')  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=32)  # Field name made lowercase.
    select_priv = models.CharField(db_column='Select_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    insert_priv = models.CharField(db_column='Insert_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    update_priv = models.CharField(db_column='Update_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    delete_priv = models.CharField(db_column='Delete_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    create_priv = models.CharField(db_column='Create_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    drop_priv = models.CharField(db_column='Drop_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    reload_priv = models.CharField(db_column='Reload_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    shutdown_priv = models.CharField(db_column='Shutdown_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    process_priv = models.CharField(db_column='Process_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    file_priv = models.CharField(db_column='File_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    grant_priv = models.CharField(db_column='Grant_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    references_priv = models.CharField(db_column='References_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    index_priv = models.CharField(db_column='Index_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    alter_priv = models.CharField(db_column='Alter_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    show_db_priv = models.CharField(db_column='Show_db_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    super_priv = models.CharField(db_column='Super_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    create_tmp_table_priv = models.CharField(db_column='Create_tmp_table_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    lock_tables_priv = models.CharField(db_column='Lock_tables_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    execute_priv = models.CharField(db_column='Execute_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    repl_slave_priv = models.CharField(db_column='Repl_slave_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    repl_client_priv = models.CharField(db_column='Repl_client_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    create_view_priv = models.CharField(db_column='Create_view_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    show_view_priv = models.CharField(db_column='Show_view_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    create_routine_priv = models.CharField(db_column='Create_routine_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    alter_routine_priv = models.CharField(db_column='Alter_routine_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    create_user_priv = models.CharField(db_column='Create_user_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    event_priv = models.CharField(db_column='Event_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    trigger_priv = models.CharField(db_column='Trigger_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    create_tablespace_priv = models.CharField(db_column='Create_tablespace_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    ssl_type = models.CharField(max_length=9, db_collation='utf8mb3_general_ci')
    ssl_cipher = models.TextField()
    x509_issuer = models.TextField()
    x509_subject = models.TextField()
    max_questions = models.PositiveIntegerField()
    max_updates = models.PositiveIntegerField()
    max_connections = models.PositiveIntegerField()
    max_user_connections = models.PositiveIntegerField()
    plugin = models.CharField(max_length=64)
    authentication_string = models.TextField(blank=True, null=True)
    password_expired = models.CharField(max_length=1, db_collation='utf8mb3_general_ci')
    password_last_changed = models.DateTimeField(blank=True, null=True)
    password_lifetime = models.PositiveSmallIntegerField(blank=True, null=True)
    account_locked = models.CharField(max_length=1, db_collation='utf8mb3_general_ci')
    create_role_priv = models.CharField(db_column='Create_role_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    drop_role_priv = models.CharField(db_column='Drop_role_priv', max_length=1, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    password_reuse_history = models.PositiveSmallIntegerField(db_column='Password_reuse_history', blank=True, null=True)  # Field name made lowercase.
    password_reuse_time = models.PositiveSmallIntegerField(db_column='Password_reuse_time', blank=True, null=True)  # Field name made lowercase.
    password_require_current = models.CharField(db_column='Password_require_current', max_length=1, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    user_attributes = models.JSONField(db_column='User_attributes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
        unique_together = (('host', 'user'),)
