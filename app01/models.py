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
        ('VANTAGEM','VANTAGEM'),
        ('DESCONTO','DESCONTO'),
    ]

    ID_MUNICIPIOS_CHOICES = [
        (150,'Abaiara'),
        (129,'Acarape'),
        (24,'Acara??'),
        (33,'Acopiara'),
        (117,'Aiuaba'),
        (151,'Alc??ntaras'),
        (173,'Altaneira'),
        (125,'Alto Santo'),
        (41,'Amontada'),
        (175,'Antonina do Norte'),
        (131,'Apuiar??s'),
        (13,'Aquiraz'),
        (17,'Aracati'),
        (73,'Aracoiaba'),
        (160,'Ararend??'),
        (93,'Araripe'),
        (152,'Aratuba'),
        (169,'Arneiroz'),
        (84,'Assar??'),
        (82,'Aurora'),
        (179,'Baixio'),
        (110,'Banabui??'),
        (26,'Barbalha'),
        (89,'Barreira'),
        (87,'Barro'),
        (130,'Barroquinha'),
        (53,'Baturit??'),
        (35,'Beberibe'),
        (60,'Bela Cruz'),
        (34,'Boa Viagem'),
        (37,'Brejo Santo'),
        (23,'Camocim'),
        (69,'Campos Sales'),
        (15,'Canind??'),
        (114,'Capistrano'),
        (86,'Caridade'),
        (108,'Carir??'),
        (72,'Cariria??u'),
        (106,'Cari??s'),
        (115,'Carnaubal'),
        (20,'Cascavel'),
        (96,'Catarina'),
        (161,'Catunda'),
        (2,'Caucaia'),
        (143,'Chaval'),
        (139,'Chor??'),
        (100,'Chorozinho'),
        (85,'Corea??'),
        (18,'Crate??s'),
        (6,'Crato'),
        (112,'Croat??'),
        (79,'Cruz'),
        (176,'Erer??'),
        (32,'Eus??bio'),
        (81,'Forquilha'),
        (1,'Fortaleza'),
        (120,'Fortim'),
        (136,'Frecheirinha'),
        (170,'General Sampaio'),
        (134,'Gra??a'),
        (31,'Granja'),
        (181,'Granjeiro'),
        (156,'Groa??ras'),
        (74,'Guai??ba'),
        (48,'Guaraciaba do Norte'),
        (180,'Guaramiranga'),
        (102,'Hidrol??ndia'),
        (21,'Horizonte'),
        (141,'Ibaretama'),
        (78,'Ibiapina'),
        (145,'Ibicuitinga'),
        (101,'Icapu??'),
        (22,'Ic??'),
        (9,'Iguatu'),
        (76,'Independ??ncia'),
        (153,'Ipaporanga'),
        (146,'Ipaumirim'),
        (46,'Ipu'),
        (51,'Ipueiras'),
        (135,'Iracema'),
        (162,'Irapuan Pinheiro'),
        (83,'Irau??uba'),
        (168,'Itai??aba'),
        (50,'Itaitinga'),
        (36,'Itapaj??'),
        (7,'Itapipoca'),
        (98,'Itapi??na'),
        (45,'Itarema'),
        (92,'Itatira'),
        (113,'Jaguaretama'),
        (154,'Jaguaribara'),
        (57,'Jaguaribe'),
        (58,'Jaguaruana'),
        (71,'Jardim'),
        (167,'Jati'),
        (99,'Jericoacoara'),
        (3,'Juazeiro do Norte'),
        (80,'Juc??s'),
        (28,'Limoeiro do Norte'),
        (103,'Madalena'),
        (64,'Mangabeira'),
        (4,'Maracana??'),
        (8,'Maranguape'),
        (68,'Marco'),
        (155,'Martin??pole'),
        (49,'Massap??.jpg Massap??'),
        (39,'Mauriti'),
        (128,'Meruoca'),
        (70,'Milagres'),
        (142,'Milh??'),
        (138,'Mira??ma'),
        (54,'Miss??o Velha'),
        (42,'Momba??a'),
        (27,'Morada Nova'),
        (165,'Mora??jo'),
        (88,'Morrinhos'),
        (133,'Mucambo'),
        (158,'Mulungu'),
        (126,'Nova Olinda'),
        (62,'Nova Russas'),
        (67,'Novo Oriente'),
        (94,'Or??s'),
        (19,'Pacajus'),
        (11,'Pacatuba'),
        (148,'Pacoti'),
        (177,'Pacuj??'),
        (163,'Palhano'),
        (140,'Palm??cia'),
        (55,'Paracuru'),
        (59,'Paraipaba'),
        (65,'Parambu'),
        (149,'Paramoti'),
        (44,'Pedra Branca'),
        (164,'Penaforte'),
        (52,'Pentecoste'),
        (123,'Pereiro'),
        (97,'Pindoretama'),
        (119,'Piquet Caneiro'),
        (159,'Pires Ferreira'),
        (147,'Poranga'),
        (132,'Porteiras'),
        (157,'Potengi'),
        (178,'Potiretama'),
        (95,'Quiterian??polis'),
        (10,'Quixad??'),
        (124,'Quixel??'),
        (12,'Quixeramobim'),
        (90,'Quixer??'),
        (66,'Reden????o'),
        (111,'Reriutaba'),
        (14,'Russas'),
        (127,'Saboeiro'),
        (121,'Salitre'),
        (61,'Santana do Acara??'),
        (116,'Santana do Cariri'),
        (43,'Santa Quit??ria'),
        (40,'S??o Benedito'),
        (38,'S??o Gon??alo do Amarante'),
        (174,'S??o Jo??o do Jaguaribe'),
        (144,'S??o Lu??s do Curu'),
        (77,'Senador Pompeu'),
        (171,'Senador S??'),
        (5,'Sobral'),
        (109,'Solon??pole'),
        (118,'Tabosa'),
        (63,'Tabuleiro do Norte'),
        (75,'Tamboril'),
        (166,'Tarrafas'),
        (29,'Tau??'),
        (105,'Teju??uoca'),
        (16,'Tiangu??'),
        (30,'Trairi'),
        (122,'Tururu'),
        (56,'Ubajara'),
        (172,'Umari'),
        (104,'Umirim'),
        (91,'Uruburetama'),
        (137,'Uruoca'),
        (107,'Varjota'),
        (47,'V??rzea Alegre'),
        (25,'Vi??osa do Cear??'),
    ]

    id_provdesc = models.AutoField(primary_key=True)
    id_municipio = models.IntegerField(choices=ID_MUNICIPIOS_CHOICES,default='')
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
