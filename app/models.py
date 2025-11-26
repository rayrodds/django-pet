from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=200, blank=True)
	# avatar image
	image = models.ImageField(upload_to='avatars/', null=True, blank=True)
	cpf_cnpj = models.CharField(max_length=50, blank=True)
	phone = models.CharField(max_length=30, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	gender = models.CharField(max_length=20, blank=True)

	cep = models.CharField(max_length=20, blank=True)
	city = models.CharField(max_length=100, blank=True)
	neighborhood = models.CharField(max_length=100, blank=True)
	street = models.CharField(max_length=200, blank=True)
	number = models.CharField(max_length=20, blank=True)

	def __str__(self):
		return f"Profile: {self.user.username}"

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


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
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Categoria(models.Model):
    idcategoria = models.AutoField(db_column='idCategoria', primary_key=True)

    class Meta:
        managed = False
        db_table = 'categoria'


class Consulta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    tipo_de_consulta = models.CharField(db_column='TIPO_DE_CONSULTA', max_length=45)
    retorno_agendado = models.DateField(db_column='RETORNO_AGENDADO')
    tratamento = models.CharField(db_column='TRATAMENTO', max_length=45)
    data_consulta = models.DateField(db_column='DATA_CONSULTA')
    horario_consulta = models.TimeField(db_column='HORARIO_CONSULTA')
    observacoes = models.CharField(db_column='OBSERVACOES', max_length=45)
    pet_idpet = models.ForeignKey('Pet', models.DO_NOTHING, db_column='PET_idPET')
    veterinario_idveterinario = models.ForeignKey('Veterinario', models.DO_NOTHING, db_column='VETERINARIO_idVETERINARIO')

    class Meta:
        managed = False
        db_table = 'consulta'


class Conta(models.Model):
    id_conta = models.IntegerField(db_column='ID_Conta', primary_key=True)
    usuario = models.CharField(db_column='Usuario', max_length=20)
    perfil_id_perfil = models.IntegerField(db_column='Perfil_ID_Perfil')

    class Meta:
        managed = False
        db_table = 'conta'
        constraints = []
        indexes = []


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

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


class EstoqueProduto(models.Model):
    id_estoque_produto = models.AutoField(db_column='ID_Estoque_Produto', primary_key=True)
    produto_id_produto = models.ForeignKey('Produto', models.DO_NOTHING, db_column='Produto_ID_Produto', db_constraint=False)
    funcionario_id_funcionario = models.IntegerField(db_column='Funcionario_ID_Funcionario')
    funcionario_perfil_id_perfil = models.IntegerField(db_column='Funcionario_Perfil_ID_Perfil')

    class Meta:
        managed = False
        db_table = 'estoque_produto'
        constraints = []
        indexes = []


class Feedback(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    feedback_app = models.CharField(db_column='FEEDBACK_APP', max_length=45)

    class Meta:
        managed = False
        db_table = 'feedback'


class FeedbackPet(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    feedback_pet = models.CharField(db_column='FEEDBACK_PET', max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback_pet'


class Funcionario(models.Model):
    id_funcionario = models.AutoField(db_column='ID_Funcionario', primary_key=True)
    nome = models.CharField(db_column='Nome', max_length=50)
    cpf = models.IntegerField(db_column='CPF')
    endereco = models.CharField(db_column='Endereco', max_length=60)
    perfil_id_perfil = models.IntegerField(db_column='Perfil_ID_Perfil')

    class Meta:
        managed = False
        db_table = 'funcionario'
        constraints = []
        indexes = []


class Perfil(models.Model):
    id_perfil = models.IntegerField(db_column='ID_Perfil', primary_key=True)
    nome_perfil = models.CharField(db_column='Nome_Perfil', max_length=30)

    class Meta:
        managed = False
        db_table = 'perfil'


class PessoaFisica(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    cpf = models.CharField(db_column='CPF', unique=True, max_length=11)
    data_nascimento = models.DateField(db_column='DATA_NASCIMENTO')
    genero = models.CharField(db_column='GENERO', max_length=45)

    class Meta:
        managed = False
        db_table = 'pessoa fisica'


class PessoaJuridica(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    cnpj = models.CharField(db_column='CNPJ', unique=True, max_length=14)
    nome_fantasia = models.CharField(db_column='NOME_FANTASIA', max_length=45)
    endereco = models.CharField(db_column='ENDERECO', max_length=45)
    data_criacao = models.DateField(db_column='DATA_CRIACAO')

    class Meta:
        managed = False
        db_table = 'pessoa juridica'


class Pet(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nome = models.CharField(db_column='NOME', max_length=45)
    data_nascimento = models.DateField(db_column='DATA_NASCIMENTO')
    especie = models.CharField(db_column='ESPECIE', max_length=45)
    raca = models.CharField(db_column='RAÇA', max_length=45)
    sexo = models.CharField(db_column='SEXO', max_length=5)
    pelagem = models.CharField(db_column='PELAGEM', max_length=45)
    castrado = models.CharField(db_column='CASTRADO', max_length=3)
    tutor_idtutor = models.ForeignKey('Tutor', models.DO_NOTHING, db_column='TUTOR_idTUTOR')
    registro_pet_idregistro_pet = models.ForeignKey('ProntuarioPet', models.DO_NOTHING, db_column='REGISTRO_PET_idREGISTRO_PET')

    class Meta:
        managed = False
        db_table = 'pet'


class Produto(models.Model):
    id_produto = models.AutoField(db_column='ID_Produto', primary_key=True)
    nome = models.CharField(db_column='Nome', max_length=45)
    validade = models.DateField(db_column='Validade')
    fabricacao = models.DateField(db_column='Fabricacao')
    categoria_idcategoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='Categoria_idCategoria')

    class Meta:
        managed = False
        db_table = 'produto'


class ProntuarioPet(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    historico_veterinario = models.CharField(db_column='HISTORICO_VETERINARIO', unique=True, max_length=150)
    motivo_consulta = models.CharField(db_column='MOTIVO_CONSULTA', max_length=60)
    avaliacao_geral = models.CharField(db_column='AVALIACAO_GERAL', max_length=150)
    procedimentos = models.CharField(db_column='PROCEDIMENTOS', max_length=150)
    diagnostico_conslusivo = models.CharField(db_column='DIAGNOSTICO_CONSLUSIVO', max_length=150)
    observacao = models.CharField(db_column='OBSERVACAO', max_length=150)

    class Meta:
        managed = False
        db_table = 'prontuario_pet'


class Registro(models.Model):
    funcionario_id_funcionario = models.IntegerField(db_column='Funcionario_ID_Funcionario', primary_key=True)
    funcionario_perfil_id_perfil = models.IntegerField(db_column='Funcionario_Perfil_ID_Perfil')
    conta_id_conta = models.IntegerField(db_column='Conta_ID_Conta')
    conta_perfil_id_perfil = models.IntegerField(db_column='Conta_Perfil_ID_Perfil')

    class Meta:
        managed = False
        db_table = 'registro'
        constraints = []
        indexes = []
        unique_together = (('funcionario_id_funcionario', 'funcionario_perfil_id_perfil', 'conta_id_conta', 'conta_perfil_id_perfil'),)


class Tutor(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nome_tutor = models.CharField(db_column='NOME_TUTOR', max_length=45)
    cpf = models.CharField(db_column='CPF', unique=True, max_length=11)
    email = models.CharField(db_column='EMAIL', max_length=45)
    endereco = models.CharField(db_column='ENDEREÇO', max_length=60)
    data_de_nascimento = models.DateField(db_column='DATA DE NASCIMENTO')
    id_feedback = models.ForeignKey(Feedback, models.DO_NOTHING, db_column='ID_FEEDBACK')
    feedback_pet_idfeedback_pet = models.ForeignKey(FeedbackPet, models.DO_NOTHING, db_column='FEEDBACK_PET_idFEEDBACK_PET')
    senha = models.CharField(max_length=130)

    class Meta:
        managed = False
        db_table = 'tutor'


class Venda(models.Model):
    id_venda = models.AutoField(db_column='ID_Venda', primary_key=True)
    dia = models.DateField(db_column='Dia')
    hora = models.TimeField(db_column='Hora')
    valor = models.FloatField(db_column='Valor')
    funcionario_id_funcionario = models.IntegerField(db_column='Funcionario_ID_Funcionario')

    class Meta:
        managed = False
        db_table = 'venda'


class VendaHasProduto(models.Model):
    venda_id_venda = models.ForeignKey(Venda, models.DO_NOTHING, db_column='Venda_ID_Venda', db_constraint=False)
    produto_id_produto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='Produto_ID_Produto', db_constraint=False)

    class Meta:
        managed = False
        db_table = 'venda_has_produto'
        constraints = []
        indexes = []
        unique_together = ('venda_id_venda', 'produto_id_produto')


class Veterinario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nome = models.CharField(db_column='NOME', max_length=45)
    email = models.CharField(db_column='EMAIL', max_length=45)
    crmv = models.IntegerField(db_column='CRMV', unique=True)
    uf_crmv = models.CharField(db_column='UF_CRMV', max_length=5)
    telefone = models.CharField(db_column='TELEFONE', max_length=11)
    pessoa_juridica_idpessoa_juridica = models.ForeignKey(PessoaJuridica, models.DO_NOTHING, db_column='PESSOA_JURIDICA_idPESSOA_JURIDICA', blank=True, null=True)
    pessoa_fisica_idpessoa_fisica = models.ForeignKey(PessoaFisica, models.DO_NOTHING, db_column='PESSOA_FISICA_idPESSOA_FISICA', blank=True, null=True)
    tipo_veterinario = models.CharField(db_column='TIPO_VETERINARIO', max_length=8)

    class Meta:
        managed = False
        db_table = 'veterinario'
