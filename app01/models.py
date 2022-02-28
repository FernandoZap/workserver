from __future__ import unicode_literals
from django.db import connection
from django.db import models
from . import choices



class Departamento(models.Model):  
    id_departamento = models.AutoField(primary_key=True)
    id_municipio = models.IntegerField()
    codigo = models.CharField(max_length=50,default='')  
    departamento = models.CharField(max_length=50)

    def __str__(self):
        return self.departamento

    class Meta:
            db_table = "departamento"  

    class Meta:
        db_table = 'departamento'
        constraints = [
            models.UniqueConstraint(fields=['departamento', 'id_municipio'], name='unique departamento departamento')
        ]

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE {}'.format(cls._meta.db_table))        



class Municipio(models.Model):  
    id_municipio = models.AutoField(primary_key=True)
    municipio = models.CharField(max_length=100)
    modelo = models.IntegerField(default=0)
    string_pesquisa = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.municipio

    class Meta:
            db_table = "municipio"        

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE {}'.format(cls._meta.db_table))        

class Setor(models.Model):  
    id_setor = models.AutoField(primary_key=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True)
    id_municipio = models.IntegerField(default=0)
    setor = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)

    def __str__(self):
        return self.setor

    class Meta:
            db_table = "setor"        

    class Meta:
        db_table = 'setor'
        constraints = [
            models.UniqueConstraint(fields=['id_municipio', 'departamento','codigo'], name='unique setor setor')
        ]

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE {}'.format(cls._meta.db_table))        


class Funcionario(models.Model):  
    id_funcionario = models.AutoField(primary_key=True)
    id_municipio = models.IntegerField()
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20)
    matricula = models.CharField(max_length=20,default='')
    data_admissao = models.DateField(null=True)
    carga_horaria = models.IntegerField(default=0)
    jornada = models.IntegerField(default=0)
    ativo = models.IntegerField(default=1)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'funcionario'
        constraints = [
            models.UniqueConstraint(fields=['id_municipio', 'codigo'], name='funcionario unique codigo')
        ]
        indexes = [
            models.Index(fields=['id_municipio'])
        ]

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE {}'.format(cls._meta.db_table))        



class Cargo(models.Model):  
    id_cargo = models.AutoField(primary_key=True)
    id_municipio = models.IntegerField()
    cargo = models.CharField(max_length=100)
    ativo = models.IntegerField(default=1)

    def __str__(self):
        return self.cargo

    class Meta:
        db_table = 'cargo'
        constraints = [
            models.UniqueConstraint(fields=['id_municipio', 'cargo'], name='unique cargo')
        ]


    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE {}'.format(cls._meta.db_table))        


class Vinculo(models.Model):  
    id_vinculo = models.AutoField(primary_key=True)
    id_municipio = models.IntegerField()
    vinculo = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, null=True)
    ativo = models.IntegerField(default=1)

    def __str__(self):
        return self.vinculo

    class Meta:
        db_table = 'vinculo'
        constraints = [
            models.UniqueConstraint(fields=['id_municipio', 'codigo'], name='unique_vinculo_codigo')
        ]


    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE {}'.format(cls._meta.db_table))        
    

class ProvDesc(models.Model):  
    PROVDESC_CHOICES = [
        ('',''),
        ('VANTAGEM','vANTAGEM'),
        ('DESCONTO','DESCONTO'),
    ]
    id_provdesc = models.AutoField(primary_key=True)
    id_municipio = models.IntegerField(choices=choices.MUNICIPIOS_CHOICES,default='')
    tipo = models.CharField(max_length=9,choices=PROVDESC_CHOICES,default='')
    codigo = models.CharField(max_length=5) 
    descricao = models.CharField(max_length=40)
    ordenacao1 = models.IntegerField(default=0)

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'provdesc'
        constraints = [
            models.UniqueConstraint(fields=['id_municipio', 'codigo'], name='provdesc unique codigo')
        ]


    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE {}'.format(cls._meta.db_table))        
    

class LogErro(models.Model):  
    id_logerro = models.AutoField(primary_key=True)
    id_municipio = models.IntegerField()
    codigo = models.CharField(max_length=100)
    observacao = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return self.codigo

    class Meta:
        db_table = 'logerro'


    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE {}'.format(cls._meta.db_table))        


class Funcao(models.Model):  
    id_funcao = models.AutoField(primary_key=True)
    id_municipio = models.IntegerField()
    funcao = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)

    def __str__(self):
        return self.funcao

    class Meta:
        db_table = 'funcao'
        constraints = [
            models.UniqueConstraint(fields=['id_municipio', 'codigo'], name='unique_funcao_codigo')
        ]

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE {}'.format(cls._meta.db_table))        


class Lotacao(models.Model):  
    id_lotacao = models.AutoField(primary_key=True)
    id_municipio = models.IntegerField()
    lotacao = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)

    def __str__(self):
        return self.lotacao

    class Meta:
        db_table = 'lotacao'
        constraints = [
            models.UniqueConstraint(fields=['id_municipio', 'codigo'], name='unique_lotacao_codigo')
        ]

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE {}'.format(cls._meta.db_table))        


class FolhaMes(models.Model):
    id_folha = models.AutoField(primary_key=True)
    id_municipio=models.IntegerField(null=True)
    anomes = models.IntegerField()
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE,null=True)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE, null=True)
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE, null=True)
    lotacao = models.ForeignKey(Lotacao, on_delete=models.CASCADE, null=True)
    vinculo = models.ForeignKey(Vinculo, on_delete=models.CASCADE, null=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'folhames'
        constraints = [
            models.UniqueConstraint(fields=['anomes', 'funcionario'], name='unique_folhames')
        ]

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE {}'.format(cls._meta.db_table))        



class ProventosMes(models.Model):
    id_provento = models.AutoField(primary_key=True)
    id_municipio = models.IntegerField(null=True)
    anomes = models.IntegerField()
    folhames = models.ForeignKey(FolhaMes, on_delete=models.CASCADE,null=True)
    provdesc = models.ForeignKey(ProvDesc, on_delete=models.CASCADE,null=True)
    valor = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'proventosmes'
        constraints = [
            models.UniqueConstraint(fields=['anomes', 'folhames', 'provdesc'], name='unique_proventosmes')
        ]

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE {}'.format(cls._meta.db_table))        
