# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AirRack(models.Model):
    id = models.BigAutoField(primary_key=True)
    air_code = models.CharField(max_length=32, blank=True, null=True)
    rack_code = models.CharField(max_length=32, blank=True, null=True)


class Airconditioning(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    company = models.CharField(max_length=64, blank=True, null=True)
    format = models.CharField(max_length=100, blank=True, null=True)
    power = models.CharField(max_length=10, blank=True, null=True)
    voltage = models.CharField(max_length=10, blank=True, null=True)
    engineroom_id = models.CharField(max_length=32, blank=True, null=True)
    mode = models.CharField(max_length=2, blank=True, null=True)
    type = models.CharField(max_length=2, blank=True, null=True)
    plot = models.CharField(max_length=2, blank=True, null=True)
    supplymode = models.CharField(db_column='supplyMode', max_length=2, blank=True, null=True)  # Field name made lowercase.
    conditioner = models.CharField(max_length=32, blank=True, null=True)
    cop = models.CharField(max_length=2, blank=True, null=True)
    air_code = models.CharField(max_length=32, blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    start_time = models.CharField(max_length=20, blank=True, null=True)
    loop_air_flow = models.CharField(max_length=32, blank=True, null=True)
    compressor_model = models.CharField(max_length=32, blank=True, null=True)
    cryogen = models.CharField(max_length=64, blank=True, null=True)
    set_temp = models.CharField(max_length=32, blank=True, null=True)
    in_wind = models.CharField(max_length=32, blank=True, null=True)
    in_wind_fool_range = models.CharField(max_length=32, blank=True, null=True)
    out_wind_fool_range = models.CharField(max_length=32, blank=True, null=True)
    in_wind_height = models.CharField(max_length=32, blank=True, null=True)
    in_wind_size = models.CharField(max_length=100, blank=True, null=True)
    out_wide_size = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'airconditioning'


class AllotItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    allot_count = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=32, blank=True, null=True)
    demand_id = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    engineroom_count = models.IntegerField(blank=True, null=True)
    project_code = models.CharField(max_length=32, blank=True, null=True)
    project_bewrite = models.CharField(max_length=200, blank=True, null=True)
    project_state = models.CharField(max_length=2, blank=True, null=True)
    surplus_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'allot_item'


class MaintainLog(models.Model):
    #host = models.ForeignKey(Host)
    maintain_type = models.CharField(max_length=32)
    hard_type = models.CharField(max_length=16)
    time = models.DateTimeField()
    operator = models.CharField(max_length=16)
    note = models.TextField()

    def __str__(self):
        return '%s maintain-log [%s] %s %s' % (self.host.name, self.time.strftime('%Y-%m-%d %H:%M:%S'),
                                               self.maintain_type, self.hard_type)

    class Meta:
        verbose_name = u"Maintain Log"
        verbose_name_plural = verbose_name


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BaData(models.Model):
    seq_id = models.BigAutoField(primary_key=True)
    gateway_id = models.CharField(max_length=20, blank=True, null=True)
    mobile_no = models.CharField(max_length=20, blank=True, null=True)
    gateway_no = models.IntegerField(blank=True, null=True)
    package_id = models.CharField(max_length=60, blank=True, null=True)
    protocol_version = models.CharField(max_length=4, blank=True, null=True)
    fun_code = models.CharField(max_length=4, blank=True, null=True)
    terminator_no = models.CharField(max_length=20, blank=True, null=True)
    sensor_no = models.CharField(max_length=20, blank=True, null=True)
    sensor_data = models.FloatField(blank=True, null=True)
    alert_type = models.CharField(max_length=4, blank=True, null=True)
    collect_time = models.CharField(max_length=30, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ba_data'


class Battery(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    battery_code = models.CharField(max_length=32, blank=True, null=True)
    capacity = models.CharField(max_length=64, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    feature = models.CharField(max_length=64, blank=True, null=True)
    range_of_use = models.CharField(max_length=100, blank=True, null=True)
    rate = models.CharField(max_length=20, blank=True, null=True)
    time = models.CharField(max_length=20, blank=True, null=True)
    size = models.CharField(max_length=32, blank=True, null=True)
    weight = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    ups_code = models.CharField(max_length=32, blank=True, null=True)
    rectifier_code = models.CharField(max_length=32, blank=True, null=True)
    voltage = models.CharField(max_length=20, blank=True, null=True)
    temp = models.CharField(max_length=10, blank=True, null=True)
    start_time = models.CharField(max_length=20, blank=True, null=True)
    engineroom_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'battery'


class BladeAttach(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    creater = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blade_attach'


class BladeDept(models.Model):
    num = models.IntegerField(blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    simplename = models.CharField(max_length=45, blank=True, null=True)
    fullname = models.CharField(max_length=255, blank=True, null=True)
    tips = models.CharField(max_length=255, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blade_dept'


class BladeDict(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    tips = models.CharField(max_length=255, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blade_dict'


class BladeGenerate(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    realpath = models.CharField(max_length=255, blank=True, null=True)
    packagename = models.CharField(max_length=255, blank=True, null=True)
    modelname = models.CharField(max_length=255, blank=True, null=True)
    tablename = models.CharField(max_length=255, blank=True, null=True)
    pkname = models.CharField(max_length=255, blank=True, null=True)
    tips = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blade_generate'


class BladeLoginLog(models.Model):
    logname = models.CharField(max_length=255, blank=True, null=True)
    userid = models.CharField(max_length=255, blank=True, null=True)
    classname = models.CharField(max_length=255, blank=True, null=True)
    method = models.TextField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    succeed = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blade_login_log'


class BladeMenu(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    pcode = models.CharField(max_length=255, blank=True, null=True)
    alias = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    levels = models.IntegerField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    tips = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    isopen = models.CharField(max_length=255, blank=True, null=True)
    istemplate = models.CharField(max_length=255, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blade_menu'


class BladeNotice(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    publishtime = models.DateTimeField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    creater = models.IntegerField(blank=True, null=True)
    pic = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blade_notice'


class BladeOperationLog(models.Model):
    logname = models.CharField(max_length=255, blank=True, null=True)
    userid = models.CharField(max_length=255, blank=True, null=True)
    classname = models.CharField(max_length=255, blank=True, null=True)
    method = models.TextField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    succeed = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blade_operation_log'


class BladeParameter(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    para = models.TextField(blank=True, null=True)
    tips = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blade_parameter'


class BladeRelation(models.Model):
    menuid = models.IntegerField(blank=True, null=True)
    roleid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blade_relation'


class BladeRole(models.Model):
    num = models.IntegerField(blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    deptid = models.IntegerField(blank=True, null=True)
    tips = models.CharField(max_length=255, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blade_role'


class BladeRoleExt(models.Model):
    userid = models.CharField(max_length=255, blank=True, null=True)
    rolein = models.TextField(blank=True, null=True)
    roleout = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blade_role_ext'


class BladeUser(models.Model):
    account = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    salt = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    roleid = models.CharField(max_length=255, blank=True, null=True)
    deptid = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blade_user'


class BxData(models.Model):
    seq_id = models.BigAutoField(primary_key=True)
    gateway_id = models.CharField(max_length=20, blank=True, null=True)
    mobile_no = models.CharField(max_length=20, blank=True, null=True)
    gateway_no = models.IntegerField(blank=True, null=True)
    package_id = models.CharField(max_length=60, blank=True, null=True)
    protocol_version = models.CharField(max_length=4, blank=True, null=True)
    fun_code = models.CharField(max_length=4, blank=True, null=True)
    terminator_no = models.CharField(max_length=20, blank=True, null=True)
    sensor_no = models.CharField(max_length=20, blank=True, null=True)
    sensor_data = models.FloatField(blank=True, null=True)
    collect_time = models.CharField(max_length=30, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bx_data'


class Colheadcabinet(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    col_code = models.CharField(max_length=32, blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=2, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    engineroom_id = models.CharField(max_length=32, blank=True, null=True)
    distributors_code = models.CharField(max_length=32, blank=True, null=True)
    acdc = models.CharField(max_length=2, blank=True, null=True)
    start_time = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colheadcabinet'


class CollectDesinfo(models.Model):
    seq_id = models.CharField(primary_key=True, max_length=32)
    collect_time = models.CharField(max_length=24, blank=True, null=True)
    package_id = models.CharField(max_length=60, blank=True, null=True)
    gateway_id = models.CharField(max_length=32, blank=True, null=True)
    data_length = models.IntegerField(blank=True, null=True)
    data_count = models.IntegerField(blank=True, null=True)
    data_status = models.CharField(max_length=3, blank=True, null=True)
    insert_time = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collect_desinfo'


class CoolRedRowCol(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    engineroom_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cool_red_row_col'


class CurrentSensors(models.Model):
    id = models.BigAutoField(primary_key=True)
    sensors_code = models.CharField(max_length=64, blank=True, null=True)
    sensors_name = models.CharField(max_length=64, blank=True, null=True)
    device_id = models.CharField(max_length=32, blank=True, null=True)
    place = models.CharField(max_length=32, blank=True, null=True)
    engineroom_id = models.CharField(max_length=32, blank=True, null=True)
    gateway_id = models.CharField(max_length=32, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    device_code = models.CharField(max_length=32, blank=True, null=True)
    unit = models.CharField(max_length=5, blank=True, null=True)
    acquisition = models.IntegerField(blank=True, null=True)
    plot_id = models.CharField(max_length=32, blank=True, null=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    terminal_code = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'current_sensors'


class Customer(models.Model):
    id = models.BigAutoField(primary_key=True,verbose_name = u'序号')
    name = models.CharField(max_length=100, blank=True, null=True,verbose_name = u'名称')
    code = models.CharField(max_length=32, blank=True, null=True,verbose_name = u'业务编号')
    nature = models.CharField(max_length=64, blank=True, null=True,verbose_name = u'客户性质')
    cust_code = models.CharField(max_length=32, blank=True, null=True,verbose_name = u'客户编号')
    pid = models.IntegerField(blank=True, null=True,verbose_name = u'上级编号')
    num = models.IntegerField(blank=True, null=True,verbose_name = u'序号')
    grade = models.IntegerField(blank=True, null=True,verbose_name = u'级别')

    class Meta:
        managed = False
        db_table = 'customer'
        verbose_name = '客户管理'
        verbose_name_plural = '客户管理'


class Demand(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    customer_code = models.CharField(max_length=32, blank=True, null=True)
    status = models.CharField(max_length=2, blank=True, null=True)
    demand_bewrite = models.CharField(max_length=200, blank=True, null=True)
    engineroom_count = models.IntegerField(blank=True, null=True)
    demand_code = models.CharField(max_length=32, blank=True, null=True)
    allot_count = models.IntegerField(blank=True, null=True)
    surplus_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demand'


class Deploy(models.Model):
    id = models.BigAutoField(primary_key=True)
    laber_number = models.CharField(max_length=32, blank=True, null=True)
    place = models.CharField(max_length=64, blank=True, null=True)
    range_of_use = models.CharField(max_length=64, blank=True, null=True)
    return_number = models.CharField(max_length=20, blank=True, null=True)
    mac_col_code = models.CharField(max_length=32, blank=True, null=True)
    rack_code = models.CharField(max_length=32, blank=True, null=True)
    terminal_code = models.CharField(max_length=32, blank=True, null=True)
    gateway_code = models.CharField(max_length=32, blank=True, null=True)
    line_model = models.CharField(max_length=32, blank=True, null=True)
    engineroom_id = models.CharField(max_length=32, blank=True, null=True)
    device_id = models.CharField(max_length=2, blank=True, null=True)
    cool_hot = models.CharField(max_length=2, blank=True, null=True)
    sensor_type = models.CharField(max_length=2, blank=True, null=True)
    collect_type = models.CharField(max_length=2, blank=True, null=True)
    line_code = models.IntegerField(blank=True, null=True)
    air_type = models.CharField(max_length=2, blank=True, null=True)
    engineroom_type = models.CharField(max_length=2, blank=True, null=True)
    group_code = models.CharField(max_length=2, blank=True, null=True)
    seat = models.CharField(max_length=10, blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deploy'


class Distributors(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    engineroom_id = models.CharField(max_length=32, blank=True, null=True)
    company = models.CharField(max_length=128, blank=True, null=True)
    model = models.CharField(max_length=64, blank=True, null=True)
    size = models.CharField(max_length=32, blank=True, null=True)
    dis_code = models.CharField(max_length=32, blank=True, null=True)
    power_distribution = models.CharField(max_length=10, blank=True, null=True)
    function = models.CharField(max_length=2, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    current_quota = models.FloatField(blank=True, null=True)
    already_use_current_count = models.FloatField(blank=True, null=True)
    not_used_current_count = models.FloatField(blank=True, null=True)
    acdc = models.CharField(max_length=2, blank=True, null=True)
    start_time = models.CharField(max_length=20, blank=True, null=True)
    aocn_count = models.IntegerField(blank=True, null=True)
    already_use_aocn_count = models.IntegerField(blank=True, null=True)
    not_use_aocn_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'distributors'


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


class EnghotmanagerAccessrecord(models.Model):
    date = models.DateField()
    user_count = models.IntegerField()
    view_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'enghotmanager_accessrecord'


class EnghotmanagerHost(models.Model):
    name = models.CharField(max_length=64)
    nagios_name = models.CharField(max_length=64, blank=True, null=True)
    ip = models.CharField(max_length=39, blank=True, null=True)
    internal_ip = models.CharField(max_length=39, blank=True, null=True)
    user = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    ssh_port = models.IntegerField(blank=True, null=True)
    status = models.SmallIntegerField()
    brand = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    cpu = models.CharField(max_length=64)
    core_num = models.SmallIntegerField()
    hard_disk = models.IntegerField()
    memory = models.IntegerField()
    system = models.CharField(max_length=32)
    system_version = models.CharField(max_length=32)
    system_arch = models.CharField(max_length=32)
    create_time = models.DateField()
    guarantee_date = models.DateField()
    service_type = models.CharField(max_length=32)
    description = models.TextField()
    administrator = models.ForeignKey(AuthUser, models.DO_NOTHING)
    idc = models.ForeignKey('EnghotmanagerIdc', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'enghotmanager_host'


class EnghotmanagerHostgroup(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'enghotmanager_hostgroup'


class EnghotmanagerHostgroupHosts(models.Model):
    hostgroup = models.ForeignKey(EnghotmanagerHostgroup, models.DO_NOTHING)
    host = models.ForeignKey(EnghotmanagerHost, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'enghotmanager_hostgroup_hosts'
        unique_together = (('hostgroup', 'host'),)


class EnghotmanagerIdc(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    contact = models.CharField(max_length=32)
    telphone = models.CharField(max_length=32)
    address = models.CharField(max_length=128)
    customer_id = models.CharField(max_length=128)
    create_time = models.DateField()

    class Meta:
        managed = False
        db_table = 'enghotmanager_idc'


class EnghotmanagerIdcGroups(models.Model):
    idc = models.ForeignKey(EnghotmanagerIdc, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'enghotmanager_idc_groups'
        unique_together = (('idc', 'group'),)


class EnghotmanagerMaintainlog(models.Model):
    maintain_type = models.CharField(max_length=32)
    hard_type = models.CharField(max_length=16)
    time = models.DateTimeField()
    operator = models.CharField(max_length=16)
    note = models.TextField()
    host = models.ForeignKey(EnghotmanagerHost, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'enghotmanager_maintainlog'


class Engineroom(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120, blank=True, null=True)
    code = models.CharField(max_length=60, blank=True, null=True)
    geos_id = models.CharField(max_length=32, blank=True, null=True)
    customer_id = models.CharField(max_length=32, blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    rows = models.IntegerField(blank=True, null=True)
    cols = models.IntegerField(blank=True, null=True)
    cools = models.IntegerField(blank=True, null=True)
    hots = models.IntegerField(blank=True, null=True)
    mac_build_num = models.IntegerField(blank=True, null=True)
    room_code = models.CharField(max_length=10, blank=True, null=True)
    prov_id = models.CharField(max_length=32, blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    floorheight = models.FloatField(blank=True, null=True)
    rackplot = models.CharField(db_column='rackPlot', max_length=2, blank=True, null=True)  # Field name made lowercase.
    engroom_code = models.CharField(max_length=32, blank=True, null=True)
    start_time = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=32, blank=True, null=True)
    dimension = models.CharField(max_length=32, blank=True, null=True)
    exterior_walls_orientations = models.CharField(max_length=32, blank=True, null=True)
    exterior_walls_count = models.IntegerField(blank=True, null=True)
    building_structure = models.CharField(max_length=2, blank=True, null=True)
    chamfer = models.CharField(max_length=2, blank=True, null=True)
    floor_type = models.CharField(max_length=2, blank=True, null=True)
    floor_format = models.CharField(max_length=4, blank=True, null=True)
    plenum_height = models.CharField(max_length=32, blank=True, null=True)
    big_type = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engineroom'


class EngineroomRowCol(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    engineroom_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engineroom_row_col'


class EngineroomType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    room_type_code = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engineroom_type'


class Facility(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    rack_id = models.CharField(max_length=32, blank=True, null=True)
    device_plot = models.CharField(max_length=32, blank=True, null=True)
    device_u = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    inoutsort = models.CharField(max_length=2, blank=True, null=True)
    layingsort = models.CharField(max_length=2, blank=True, null=True)
    fac_code = models.CharField(max_length=32, blank=True, null=True)
    engineroom_id = models.CharField(max_length=32, blank=True, null=True)
    start_time = models.CharField(max_length=20, blank=True, null=True)
    direction_of_air_supply = models.CharField(max_length=2, blank=True, null=True)
    wiring_circuit_count = models.IntegerField(blank=True, null=True)
    wiring_circuit_count_bewrite = models.CharField(max_length=100, blank=True, null=True)
    seat = models.CharField(max_length=10, blank=True, null=True)
    group = models.CharField(max_length=2, blank=True, null=True)
    mac_col_code = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility'


class FacilityPlot(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    power = models.CharField(max_length=32, blank=True, null=True)
    fan_power = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    device_u = models.CharField(max_length=2, blank=True, null=True)
    plot_code = models.CharField(max_length=32, blank=True, null=True)
    size = models.CharField(max_length=32, blank=True, null=True)
    type = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility_plot'


class FacilityType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    fac_type_code = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility_type'


class Gateway(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    code = models.CharField(max_length=64, blank=True, null=True)
    engineroom_id = models.CharField(max_length=32, blank=True, null=True)
    gateway_code = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gateway'


class GatewayState(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.CharField(max_length=10, blank=True, null=True)
    ip = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gateway_state'


class Geospatial(models.Model):
    id = models.BigAutoField(primary_key=True)
    mac_build_name = models.CharField(max_length=120, blank=True, null=True)
    mac_build_address = models.CharField(max_length=200, blank=True, null=True)
    abbreviated = models.CharField(max_length=100, blank=True, null=True)
    prov_id = models.CharField(max_length=32, blank=True, null=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    mac_build_code = models.CharField(max_length=32, blank=True, null=True)
    mac_build_floor = models.IntegerField(blank=True, null=True)
    customer_id = models.CharField(max_length=32, blank=True, null=True)
    longitude = models.CharField(max_length=32, blank=True, null=True)
    dimension = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geospatial'


class HumiditytSensors(models.Model):
    id = models.BigAutoField(primary_key=True)
    sensors_code = models.CharField(max_length=64, blank=True, null=True)
    sensors_name = models.CharField(max_length=64, blank=True, null=True)
    device_id = models.CharField(max_length=32, blank=True, null=True)
    place = models.CharField(max_length=32, blank=True, null=True)
    engineroom_id = models.CharField(max_length=32, blank=True, null=True)
    gateway_id = models.CharField(max_length=32, blank=True, null=True)
    unit = models.CharField(max_length=5, blank=True, null=True)
    acquisition = models.IntegerField(blank=True, null=True)
    plot_id = models.CharField(max_length=32, blank=True, null=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    terminal_code = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'humidityt_sensors'


class MachineColumn(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    engineroom_id = models.CharField(max_length=32, blank=True, null=True)
    column_code = models.IntegerField(blank=True, null=True)
    adjacent = models.CharField(max_length=64, blank=True, null=True)
    coolpass = models.FloatField(db_column='coolPass', blank=True, null=True)  # Field name made lowercase.
    hotpass = models.FloatField(db_column='hotPass', blank=True, null=True)  # Field name made lowercase.
    mac_col_code = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machine_column'


class Manager(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    engineroom_id = models.CharField(max_length=32, blank=True, null=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    manager_code = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manager'


class OutdoorsMachine(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    outdoors_mac_code = models.CharField(max_length=32, blank=True, null=True)
    radiating = models.CharField(max_length=20, blank=True, null=True)
    brand = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    start_time = models.CharField(max_length=20, blank=True, null=True)
    size = models.CharField(max_length=32, blank=True, null=True)
    weight = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    air_code = models.CharField(max_length=32, blank=True, null=True)
    west_facing = models.CharField(max_length=2, blank=True, null=True)
    air_smooth = models.CharField(max_length=2, blank=True, null=True)
    shelter = models.CharField(max_length=2, blank=True, null=True)
    betwrite = models.CharField(max_length=200, blank=True, null=True)
    out_wind = models.CharField(max_length=32, blank=True, null=True)
    out_diameter = models.CharField(max_length=32, blank=True, null=True)
    engineroom_id = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'outdoors_machine'


class PassManager(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    engineroom_id = models.CharField(max_length=32, blank=True, null=True)
    pass_type = models.CharField(max_length=2, blank=True, null=True)
    pass_distance = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pass_manager'


class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    engineroom_count = models.IntegerField(blank=True, null=True)
    project_bewrite = models.CharField(max_length=200, blank=True, null=True)
    project_code = models.CharField(max_length=32, blank=True, null=True)
    project_state = models.CharField(max_length=2, blank=True, null=True)
    allot_count = models.IntegerField(blank=True, null=True)
    project_manager = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'


class ProjectTask(models.Model):
    id = models.BigAutoField(primary_key=True)
    task_code = models.CharField(max_length=32, blank=True, null=True)
    task_state = models.CharField(max_length=2, blank=True, null=True)
    prospecting = models.CharField(max_length=32, blank=True, null=True)
    plan = models.CharField(max_length=32, blank=True, null=True)
    construction = models.CharField(max_length=32, blank=True, null=True)
    test = models.CharField(max_length=32, blank=True, null=True)
    project_code = models.CharField(max_length=32, blank=True, null=True)
    task_bewrite = models.CharField(max_length=200, blank=True, null=True)
    engineroom_id = models.CharField(max_length=32, blank=True, null=True)
    engineroom_name = models.CharField(max_length=64, blank=True, null=True)
    engineroom_address = models.CharField(max_length=200, blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    engineroom_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_task'


class Province(models.Model):
    id = models.BigAutoField(primary_key=True)
    parentid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    orderid = models.CharField(max_length=20, blank=True, null=True)
    postcode = models.CharField(max_length=10, blank=True, null=True)
    shortname = models.CharField(db_column='shortName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    citycode = models.CharField(db_column='cityCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    mergername = models.CharField(db_column='mergerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lng = models.CharField(max_length=15, blank=True, null=True)
    lat = models.CharField(max_length=15, blank=True, null=True)
    pinyin = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'province'


class Rack(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    mac_col_id = models.CharField(max_length=32, blank=True, null=True)
    rows_code = models.CharField(max_length=3, blank=True, null=True)
    adjacent = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    engineroom_id = models.CharField(max_length=32, blank=True, null=True)
    col_code = models.CharField(max_length=32, blank=True, null=True)
    hot_code = models.CharField(max_length=32, blank=True, null=True)
    rack_code = models.CharField(max_length=32, blank=True, null=True)
    inairsort = models.CharField(db_column='inAirSort', max_length=2, blank=True, null=True)  # Field name made lowercase.
    outairsort = models.CharField(db_column='outAirSort', max_length=2, blank=True, null=True)  # Field name made lowercase.
    publicpass = models.CharField(db_column='publicPass', max_length=2, blank=True, null=True)  # Field name made lowercase.
    air_code = models.CharField(max_length=32, blank=True, null=True)
    rack_u_count = models.IntegerField(blank=True, null=True)
    colheadcabinet_code = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rack'


class RackType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    rack_type_code = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rack_type'


class RacktempCsv(models.Model):
    seq_id = models.IntegerField(blank=True, null=True)
    data_time = models.CharField(max_length=255, blank=True, null=True)
    device_pos1_rc = models.CharField(max_length=255, blank=True, null=True)
    device_pos2_no = models.IntegerField(blank=True, null=True)
    data_date_fmt = models.DateTimeField(blank=True, null=True)
    device_no = models.CharField(max_length=255, blank=True, null=True)
    temp_hu = models.FloatField(blank=True, null=True)
    temp_hm = models.FloatField(blank=True, null=True)
    temp_hd = models.FloatField(blank=True, null=True)
    temp_cu = models.FloatField(blank=True, null=True)
    temp_cm = models.FloatField(blank=True, null=True)
    temp_cd = models.FloatField(blank=True, null=True)
    data_datetime_fmt = models.CharField(max_length=255, blank=True, null=True)
    data_time_fmt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'racktemp_csv'


class Rectifier(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    rectifier_code = models.CharField(max_length=32, blank=True, null=True)
    capacity = models.CharField(max_length=64, blank=True, null=True)
    distributors_code = models.CharField(max_length=32, blank=True, null=True)
    start_time = models.CharField(max_length=20, blank=True, null=True)
    photo = models.CharField(max_length=100, blank=True, null=True)
    engineroom_id = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rectifier'


class ReportAvadataChannel(models.Model):
    seq_id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    data_date_fmt = models.CharField(max_length=64, blank=True, null=True)
    device_id = models.CharField(max_length=64, blank=True, null=True)
    province = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    device_no = models.CharField(max_length=64, blank=True, null=True)
    device_pos3_ch = models.CharField(max_length=64, blank=True, null=True)
    device_pos4_ud = models.CharField(max_length=64, blank=True, null=True)
    sensor_desc = models.CharField(max_length=64, blank=True, null=True)
    count_no = models.BigIntegerField(blank=True, null=True)
    sum_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    ava_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_avadata_channel'


class ReportAvadataDevice(models.Model):
    seq_id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    data_date_fmt = models.CharField(max_length=64, blank=True, null=True)
    device_id = models.CharField(max_length=64, blank=True, null=True)
    province = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    device_no = models.CharField(max_length=64, blank=True, null=True)
    device_pos3_ch = models.CharField(max_length=64, blank=True, null=True)
    device_pos4_ud = models.CharField(max_length=64, blank=True, null=True)
    sensor_desc = models.CharField(max_length=64, blank=True, null=True)
    count_no = models.BigIntegerField(blank=True, null=True)
    sum_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    ava_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_avadata_device'


class ReportAvadataGrid(models.Model):
    seq_id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    data_date_fmt = models.CharField(max_length=64, blank=True, null=True)
    device_id = models.CharField(max_length=64, blank=True, null=True)
    province = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    hu_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    hm_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    hd_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    cu_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    cm_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    cd_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    cool_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    hot_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    device_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    max_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    min_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    device_no = models.CharField(max_length=64, blank=True, null=True)
    status_grade = models.CharField(max_length=64, blank=True, null=True)
    status_desc = models.CharField(max_length=64, blank=True, null=True)
    status_note = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_avadata_grid'


class ReportAvadataReport(models.Model):
    seq_id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    data_date_fmt = models.CharField(max_length=64, blank=True, null=True)
    province = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    status_grade = models.CharField(max_length=64, blank=True, null=True)
    status_desc = models.CharField(max_length=64, blank=True, null=True)
    status_note = models.CharField(max_length=64, blank=True, null=True)
    count_all = models.IntegerField(blank=True, null=True)
    count_num = models.IntegerField(blank=True, null=True)
    grade_ratio = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_avadata_report'


class ReportAvadataSensor(models.Model):
    seq_id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    data_date_fmt = models.CharField(max_length=64, blank=True, null=True)
    device_id = models.CharField(max_length=64, blank=True, null=True)
    province = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    device_no = models.CharField(max_length=64, blank=True, null=True)
    device_pos3_ch = models.CharField(max_length=64, blank=True, null=True)
    device_pos4_ud = models.CharField(max_length=64, blank=True, null=True)
    sensor_desc = models.CharField(max_length=64, blank=True, null=True)
    count_no = models.BigIntegerField(blank=True, null=True)
    sum_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    ava_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    count_b25 = models.BigIntegerField(blank=True, null=True)
    ratio_b25 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    count_g25b28 = models.BigIntegerField(blank=True, null=True)
    ratio_g25b28 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    count_g28b30 = models.BigIntegerField(blank=True, null=True)
    ratio_g28b30 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    count_g30b32 = models.BigIntegerField(blank=True, null=True)
    ratio_g30b32 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    count_g32b35 = models.BigIntegerField(blank=True, null=True)
    ratio_g32b35 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    count_g35 = models.BigIntegerField(blank=True, null=True)
    ratio_g35 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_avadata_sensor'


class ReportCoolrtiReport(models.Model):
    data_date_fmt = models.CharField(max_length=64, blank=True, null=True)
    province = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    device_no = models.CharField(max_length=64, blank=True, null=True)
    device_id = models.CharField(max_length=64, blank=True, null=True)
    device_pos4_ud = models.CharField(max_length=64, blank=True, null=True)
    device_pos1_rc = models.CharField(max_length=64, blank=True, null=True)
    cool_device_id = models.CharField(max_length=64, blank=True, null=True)
    cool_device_no = models.CharField(max_length=64, blank=True, null=True)
    seq_id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    max_rti_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    device_pos1_rc_2 = models.CharField(max_length=45, blank=True, null=True)
    min_rti_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    ava_rti_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    top30_rti_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_coolrti_report'


class ReportCoolvalueGrid(models.Model):
    seq_id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    data_date_fmt = models.CharField(max_length=64, blank=True, null=True)
    data_datetime_fmt = models.CharField(max_length=64, blank=True, null=True)
    data_time_fmt = models.CharField(max_length=64, blank=True, null=True)
    data_year = models.IntegerField(blank=True, null=True)
    data_month = models.IntegerField(blank=True, null=True)
    data_day = models.IntegerField(blank=True, null=True)
    data_hour = models.IntegerField(blank=True, null=True)
    data_minute = models.IntegerField(blank=True, null=True)
    data_second = models.IntegerField(blank=True, null=True)
    province = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    device_id = models.CharField(max_length=64, blank=True, null=True)
    device_no = models.CharField(max_length=64, blank=True, null=True)
    device_pos1_rc = models.CharField(max_length=64, blank=True, null=True)
    temp_out = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    temp_in = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    work_cur = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    wet_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    h_out = models.CharField(max_length=45, blank=True, null=True)
    h_in = models.CharField(max_length=45, blank=True, null=True)
    wind_f = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    wind_v = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    wind_q = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    air_p = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    air_cp = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    coolvalue1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    coolvalue2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    volt_v = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cur_a = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    power_factor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    device_power = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    device_cop = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_coolvalue_grid'


class ReportImportData(models.Model):
    seq_id_key = models.BigAutoField(primary_key=True)
    import_time = models.DateTimeField()
    sensor_name = models.CharField(max_length=128)
    data_time = models.CharField(max_length=64, blank=True, null=True)
    sensor_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    device_type = models.CharField(max_length=64, blank=True, null=True)
    device_pos1_rc = models.CharField(max_length=64, blank=True, null=True)
    device_pos2_no = models.CharField(max_length=64, blank=True, null=True)
    device_pos3_ch = models.CharField(max_length=64, blank=True, null=True)
    device_pos4_ud = models.CharField(max_length=64, blank=True, null=True)
    device_pos5_xx = models.CharField(max_length=64, blank=True, null=True)
    data_year = models.IntegerField(blank=True, null=True)
    sensor_type = models.CharField(max_length=64, blank=True, null=True)
    data_month = models.IntegerField(blank=True, null=True)
    data_day = models.IntegerField(blank=True, null=True)
    data_hour = models.IntegerField(blank=True, null=True)
    data_minute = models.IntegerField(blank=True, null=True)
    data_date_fmt = models.CharField(max_length=64, blank=True, null=True)
    data_time_fmt = models.CharField(max_length=64, blank=True, null=True)
    data_datetime_fmt = models.CharField(max_length=64, blank=True, null=True)
    device_no = models.CharField(max_length=64, blank=True, null=True)
    sensor_desc = models.CharField(max_length=64, blank=True, null=True)
    data_second = models.IntegerField(blank=True, null=True)
    province = models.CharField(max_length=64, blank=True, null=True)
    groups = models.CharField(max_length=128, blank=True, null=True)
    dataunitl = models.CharField(max_length=64, blank=True, null=True)
    isalarm = models.IntegerField(blank=True, null=True)
    sensor_state = models.CharField(max_length=64, blank=True, null=True)
    toplimit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    downlimit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    enviewgroup = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_import_data'


class ReportImportDataHistory(models.Model):
    seq_id_key = models.BigAutoField(primary_key=True)
    import_time = models.DateTimeField()
    sensor_name = models.CharField(max_length=128)
    data_time = models.CharField(max_length=64, blank=True, null=True)
    sensor_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    device_type = models.CharField(max_length=64, blank=True, null=True)
    device_pos1_rc = models.CharField(max_length=64, blank=True, null=True)
    device_pos2_no = models.CharField(max_length=64, blank=True, null=True)
    device_pos3_ch = models.CharField(max_length=64, blank=True, null=True)
    device_pos4_ud = models.CharField(max_length=64, blank=True, null=True)
    device_pos5_xx = models.CharField(max_length=64, blank=True, null=True)
    data_year = models.IntegerField(blank=True, null=True)
    sensor_type = models.CharField(max_length=64, blank=True, null=True)
    data_month = models.IntegerField(blank=True, null=True)
    data_day = models.IntegerField(blank=True, null=True)
    data_hour = models.IntegerField(blank=True, null=True)
    data_minute = models.IntegerField(blank=True, null=True)
    data_date_fmt = models.CharField(max_length=64, blank=True, null=True)
    data_time_fmt = models.CharField(max_length=64, blank=True, null=True)
    data_datetime_fmt = models.CharField(max_length=64, blank=True, null=True)
    device_no = models.CharField(max_length=64, blank=True, null=True)
    sensor_desc = models.CharField(max_length=64, blank=True, null=True)
    data_second = models.IntegerField(blank=True, null=True)
    province = models.CharField(max_length=64, blank=True, null=True)
    groups = models.CharField(max_length=128, blank=True, null=True)
    dataunitl = models.CharField(max_length=64, blank=True, null=True)
    isalarm = models.IntegerField(blank=True, null=True)
    sensor_state = models.CharField(max_length=64, blank=True, null=True)
    toplimit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    downlimit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    enviewgroup = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    device_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_import_data_history'


class ReportImportDatelist(models.Model):
    seq_id = models.AutoField(primary_key=True)
    import_time = models.DateTimeField(blank=True, null=True)
    imported_data_date = models.CharField(max_length=64, blank=True, null=True)
    trans_grid_over = models.IntegerField(blank=True, null=True)
    trans_grid_time = models.CharField(max_length=64, blank=True, null=True)
    calcu_range_over = models.IntegerField(blank=True, null=True)
    calcu_range_time = models.CharField(max_length=64, blank=True, null=True)
    calcu_topn_over = models.IntegerField(blank=True, null=True)
    calcu_topn_time = models.CharField(max_length=64, blank=True, null=True)
    calcu_pcc_over = models.IntegerField(blank=True, null=True)
    calcu_pcc_time = models.CharField(max_length=64, blank=True, null=True)
    imported_device_no = models.CharField(max_length=64, blank=True, null=True)
    province = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    device_id = models.CharField(max_length=64, blank=True, null=True)
    calcu_rangeratio_over = models.IntegerField(blank=True, null=True)
    calcu_rangeratio_time = models.CharField(max_length=45, blank=True, null=True)
    calcu_avavalue_over = models.IntegerField(blank=True, null=True)
    calcu_avavalue_time = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_import_datelist'


class ReportImportDevicelist(models.Model):
    seq_id = models.BigAutoField(primary_key=True)
    province = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    device_no = models.CharField(max_length=64, blank=True, null=True)
    device_id = models.CharField(max_length=64, blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    device_type = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_import_devicelist'


class ReportPccgridData(models.Model):
    data_date_fmt = models.CharField(max_length=16, blank=True, null=True)
    device_no = models.CharField(max_length=32, blank=True, null=True)
    sensor1 = models.CharField(max_length=64, blank=True, null=True)
    device_pos1_rc = models.CharField(max_length=64, blank=True, null=True)
    device_pos2_no = models.CharField(max_length=64, blank=True, null=True)
    device_pos3_ch_1 = models.CharField(max_length=64, blank=True, null=True)
    device_pos4_ud_1 = models.CharField(max_length=64, blank=True, null=True)
    pcc_hu = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    pcc_hm = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    pcc_hd = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    pcc_cu = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    pcc_cm = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    pcc_cd = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    seq_id = models.BigAutoField(primary_key=True)
    import_time = models.DateTimeField()
    province = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    device_id = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_pccgrid_data'


class ReportRacktempData(models.Model):
    seq_id = models.BigAutoField(primary_key=True)
    data_time = models.CharField(max_length=64, blank=True, null=True)
    device_pos1_rc = models.CharField(max_length=64, blank=True, null=True)
    device_pos2_no = models.CharField(max_length=64, blank=True, null=True)
    data_date_fmt = models.CharField(max_length=64, blank=True, null=True)
    device_no = models.CharField(max_length=64, blank=True, null=True)
    temp_hu = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    temp_hm = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    temp_hd = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    temp_cu = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    temp_cm = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    temp_cd = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    data_datetime_fmt = models.CharField(max_length=64, blank=True, null=True)
    data_time_fmt = models.CharField(max_length=64, blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    province = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    device_id = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_racktemp_data'


class ReportRangeratioData(models.Model):
    seq_id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    data_date_fmt = models.CharField(max_length=64, blank=True, null=True)
    data_hour = models.IntegerField(blank=True, null=True)
    province = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    device_no = models.CharField(max_length=64, blank=True, null=True)
    device_id = models.CharField(max_length=64, blank=True, null=True)
    device_type = models.CharField(max_length=64, blank=True, null=True)
    sensor_type = models.CharField(max_length=64, blank=True, null=True)
    device_pos1_rc = models.CharField(max_length=64, blank=True, null=True)
    device_pos2_no = models.CharField(max_length=64, blank=True, null=True)
    device_pos3_ch = models.CharField(max_length=64, blank=True, null=True)
    device_pos4_ud = models.CharField(max_length=64, blank=True, null=True)
    data_year = models.IntegerField(blank=True, null=True)
    data_month = models.IntegerField(blank=True, null=True)
    data_day = models.IntegerField(blank=True, null=True)
    max_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    min_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    data_count_all = models.BigIntegerField(blank=True, null=True)
    temp_down = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    temp_up = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    data_count_range = models.BigIntegerField(blank=True, null=True)
    range_ratio = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    status_desc = models.CharField(max_length=64, blank=True, null=True)
    sensor_desc = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_rangeratio_data'


class ReportRangeratioGrid(models.Model):
    seq_id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    data_date_fmt = models.CharField(max_length=64, blank=True, null=True)
    data_hour = models.IntegerField(blank=True, null=True)
    province = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    device_no = models.CharField(max_length=64, blank=True, null=True)
    device_id = models.CharField(max_length=64, blank=True, null=True)
    device_type = models.CharField(max_length=64, blank=True, null=True)
    sensor_type = models.CharField(max_length=64, blank=True, null=True)
    device_pos1_rc = models.CharField(max_length=64, blank=True, null=True)
    device_pos2_no = models.CharField(max_length=64, blank=True, null=True)
    device_pos3_ch = models.CharField(max_length=64, blank=True, null=True)
    device_pos4_ud = models.CharField(max_length=64, blank=True, null=True)
    data_year = models.IntegerField(blank=True, null=True)
    data_month = models.IntegerField(blank=True, null=True)
    data_day = models.IntegerField(blank=True, null=True)
    range_ratio_b25 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    range_ratio_g28b30 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    range_ratio_g32b35 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    range_ratio_g35 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    status_desc = models.CharField(max_length=64, blank=True, null=True)
    sensor_desc = models.CharField(max_length=45, blank=True, null=True)
    range_ratio_g25b28 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    range_ratio_g30b32 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_rangeratio_grid'


class ReportSourceData(models.Model):
    groups = models.CharField(max_length=128, blank=True, null=True)
    data = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    time = models.CharField(max_length=64, blank=True, null=True)
    type = models.CharField(max_length=64, blank=True, null=True)
    dataunit = models.CharField(max_length=64, blank=True, null=True)
    alarm = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=64, blank=True, null=True)
    toplimit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    downlimit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    identifying = models.CharField(max_length=128, blank=True, null=True)
    enviewgroup = models.CharField(max_length=64, blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_source_data'


class ReportSourceDataHistory(models.Model):
    groups = models.CharField(max_length=128, blank=True, null=True)
    data = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    time = models.CharField(max_length=64, blank=True, null=True)
    type = models.CharField(max_length=64, blank=True, null=True)
    dataunit = models.CharField(max_length=64, blank=True, null=True)
    alarm = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=64, blank=True, null=True)
    toplimit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    downlimit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    identifying = models.CharField(max_length=128, blank=True, null=True)
    enviewgroup = models.CharField(max_length=64, blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_source_data_history'


class ReportTempdifffreqGrid(models.Model):
    seq_id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    data_date_fmt = models.CharField(max_length=64, blank=True, null=True)
    province = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    device_no = models.CharField(max_length=64, blank=True, null=True)
    device_id = models.CharField(max_length=64, blank=True, null=True)
    temp_up = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    temp_down = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    up_count = models.BigIntegerField(blank=True, null=True)
    mid_count = models.BigIntegerField(blank=True, null=True)
    down_count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_tempdifffreq_grid'


class ReportTemppccData(models.Model):
    data_date_fmt = models.CharField(max_length=16, blank=True, null=True)
    device_no = models.CharField(max_length=32, blank=True, null=True)
    sensor1 = models.CharField(max_length=64, blank=True, null=True)
    sensor2 = models.CharField(max_length=64, blank=True, null=True)
    pcc_value = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    count_no = models.BigIntegerField()
    seq_id = models.BigAutoField(primary_key=True)
    device_pos1_rc = models.CharField(max_length=64, blank=True, null=True)
    device_pos2_no = models.CharField(max_length=64, blank=True, null=True)
    device_pos3_ch_1 = models.CharField(max_length=64, blank=True, null=True)
    device_pos4_ud_1 = models.CharField(max_length=64, blank=True, null=True)
    device_pos3_ch_2 = models.CharField(max_length=64, blank=True, null=True)
    device_pos4_ud_2 = models.CharField(max_length=64, blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    province = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    device_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_temppcc_data'


class ReportTemprangeCfg(models.Model):
    seq_id = models.BigAutoField(primary_key=True)
    temp_down = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    temp_up = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status_desc = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_temprange_cfg'


class ReportTemprangefreqData(models.Model):
    seq_id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    start_date = models.CharField(max_length=64, blank=True, null=True)
    end_date = models.CharField(max_length=64, blank=True, null=True)
    device_no = models.CharField(max_length=64, blank=True, null=True)
    temp_low = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    temp_high = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sensor_hu = models.IntegerField(blank=True, null=True)
    sensor_hm = models.IntegerField(blank=True, null=True)
    sensor_hd = models.IntegerField(blank=True, null=True)
    sensor_cu = models.IntegerField(blank=True, null=True)
    sensor_cm = models.IntegerField(blank=True, null=True)
    sensor_cd = models.IntegerField(blank=True, null=True)
    province = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    device_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_temprangefreq_data'


class ReportTemptopnData(models.Model):
    seq_id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField()
    start_date = models.CharField(max_length=64)
    end_date = models.CharField(max_length=64)
    device_no = models.CharField(max_length=64)
    device_pos3_ch = models.CharField(max_length=64, blank=True, null=True)
    device_pos4_ud = models.CharField(max_length=64, blank=True, null=True)
    most_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ava_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ava_lowrat = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    most_lowrat = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    top10p_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    top20p_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    top40p_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    max_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    min_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    max_amp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    province = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    device_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_temptopn_data'


class ReportWarnData(models.Model):
    groups = models.CharField(max_length=128, blank=True, null=True)
    data = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    time = models.CharField(max_length=64, blank=True, null=True)
    type = models.CharField(max_length=64, blank=True, null=True)
    dataunit = models.CharField(max_length=64, blank=True, null=True)
    alarm = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=64, blank=True, null=True)
    toplimit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    downlimit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    identifying = models.CharField(max_length=128, blank=True, null=True)
    enviewgroup = models.CharField(max_length=64, blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_warn_data'


class ReversionRevision(models.Model):
    date_created = models.DateTimeField()
    comment = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reversion_revision'


class ReversionVersion(models.Model):
    object_id = models.CharField(max_length=191)
    format = models.CharField(max_length=255)
    serialized_data = models.TextField()
    object_repr = models.TextField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    revision = models.ForeignKey(ReversionRevision, models.DO_NOTHING)
    db = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'reversion_version'
        unique_together = (('db', 'content_type', 'object_id', 'revision'),)


class SensorsPlot(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    range = models.CharField(max_length=10, blank=True, null=True)
    precise = models.CharField(max_length=10, blank=True, null=True)
    plot_code = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensors_plot'


class Sim(models.Model):
    id = models.BigAutoField(primary_key=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    gateway = models.CharField(max_length=32, blank=True, null=True)
    scw = models.CharField(max_length=64, blank=True, null=True)
    dataplan = models.CharField(max_length=64, blank=True, null=True)
    sim_code = models.CharField(max_length=32, blank=True, null=True)
    code = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sim'


class TempSensors(models.Model):
    id = models.BigAutoField(primary_key=True)
    sensors_code = models.CharField(max_length=64, blank=True, null=True)
    sensors_name = models.CharField(max_length=64, blank=True, null=True)
    rack_id = models.CharField(max_length=32, blank=True, null=True)
    cool_hot = models.CharField(max_length=4, blank=True, null=True)
    hmd = models.CharField(max_length=4, blank=True, null=True)
    mac_col_id = models.CharField(max_length=32, blank=True, null=True)
    engineroom_id = models.CharField(max_length=32, blank=True, null=True)
    gateway_id = models.CharField(max_length=32, blank=True, null=True)
    device_id = models.CharField(max_length=32, blank=True, null=True)
    unit = models.CharField(max_length=5, blank=True, null=True)
    acquisition = models.IntegerField(blank=True, null=True)
    plot_id = models.CharField(max_length=32, blank=True, null=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)
    terminal_code = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_sensors'


class Terminal(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    terminal_code = models.CharField(max_length=32, blank=True, null=True)
    gateway_code = models.CharField(max_length=32, blank=True, null=True)
    engineroom_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'terminal'


class UploadCad(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    creater = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    task_code = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upload_cad'


class Ups(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    ups_code = models.CharField(max_length=32, blank=True, null=True)
    capacity = models.CharField(max_length=64, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    entry_range = models.CharField(max_length=100, blank=True, null=True)
    voltage = models.CharField(max_length=20, blank=True, null=True)
    rate = models.CharField(max_length=20, blank=True, null=True)
    battery_time = models.CharField(max_length=20, blank=True, null=True)
    size = models.CharField(max_length=32, blank=True, null=True)
    weight = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    distributors_code = models.CharField(max_length=32, blank=True, null=True)
    start_time = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    engineroom_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ups'


class VoltageSensors(models.Model):
    id = models.BigAutoField(primary_key=True)
    sensors_code = models.CharField(max_length=64, blank=True, null=True)
    sensors_name = models.CharField(max_length=64, blank=True, null=True)
    device_id = models.CharField(max_length=32, blank=True, null=True)
    place = models.CharField(max_length=32, blank=True, null=True)
    engineroom_id = models.CharField(max_length=32, blank=True, null=True)
    gateway_id = models.CharField(max_length=32, blank=True, null=True)
    device_code = models.CharField(max_length=32, blank=True, null=True)
    unit = models.CharField(max_length=5, blank=True, null=True)
    acquisition = models.IntegerField(blank=True, null=True)
    plot_id = models.CharField(max_length=32, blank=True, null=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    terminal_code = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voltage_sensors'


class XadminBookmark(models.Model):
    title = models.CharField(max_length=128)
    url_name = models.CharField(max_length=64)
    query = models.CharField(max_length=1000)
    is_share = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xadmin_bookmark'


class XadminLog(models.Model):
    action_time = models.DateTimeField()
    ip_addr = models.CharField(max_length=39, blank=True, null=True)
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.CharField(max_length=32)
    message = models.TextField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'xadmin_log'


class XadminUsersettings(models.Model):
    key = models.CharField(max_length=256)
    value = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'xadmin_usersettings'


class XadminUserwidget(models.Model):
    page_id = models.CharField(max_length=256)
    widget_type = models.CharField(max_length=50)
    value = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'xadmin_userwidget'
