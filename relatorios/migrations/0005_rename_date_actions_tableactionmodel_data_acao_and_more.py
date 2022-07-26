# Generated by Django 4.0.5 on 2022-07-20 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relatorios', '0004_tableactionmodel_municipio_atendido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tableactionmodel',
            old_name='date_actions',
            new_name='data_acao',
        ),
        migrations.RenameField(
            model_name='tableactionmodel',
            old_name='date_to_publication',
            new_name='data_publicacao',
        ),
        migrations.RenameField(
            model_name='tableactionmodel',
            old_name='description_action',
            new_name='descricao_acao',
        ),
        migrations.RenameField(
            model_name='tableactionmodel',
            old_name='numbers_employee',
            new_name='n_profissionais_atendidos',
        ),
        migrations.RenameField(
            model_name='tableeventmodel',
            old_name='date_final',
            new_name='data_final',
        ),
        migrations.RenameField(
            model_name='tableeventmodel',
            old_name='date_initial',
            new_name='data_inicial',
        ),
        migrations.RenameField(
            model_name='tableeventmodel',
            old_name='date_to_publication',
            new_name='data_publicacao',
        ),
        migrations.RenameField(
            model_name='tableeventmodel',
            old_name='event_feature',
            new_name='tipo_evento',
        ),
        migrations.RenameField(
            model_name='tableeventmodel',
            old_name='title_event',
            new_name='titulo_evento',
        ),
        migrations.AddField(
            model_name='tableeventmodel',
            name='descricao_evento',
            field=models.TextField(default='', max_length=150, verbose_name='Descrição do Evento'),
        ),
        migrations.AddField(
            model_name='tableeventmodel',
            name='instituiao_ofertante',
            field=models.CharField(default='', max_length=150, verbose_name='Instituição Ofertante'),
        ),
        migrations.AlterField(
            model_name='tableactionmodel',
            name='municipio_atendido',
            field=models.CharField(choices=[('Não se aplica', 'Não se aplica'), ('*Grupo de municípios', '*Grupo de municípios'), ('Acorizal', 'Acorizal'), ('Água Boa', 'Água Boa'), ('Alta Floresta', 'Alta Floresta'), ('Alto Araguaia', 'Alto Araguaia'), ('Alto Boa Vista', 'Alto Boa Vista'), ('Alto Garças', 'Alto Garças'), ('Alto Paraguai', 'Alto Paraguai'), ('Alto Taquari', 'Alto Taquari'), ('Apiacás', 'Apiacás'), ('Araguaiana', 'Araguaiana'), ('Araguainha', 'Araguainha'), ('Araputanga', 'Araputanga'), ('Arenápolis', 'Arenápolis'), ('Aripuanã', 'Aripuanã'), ('Barão de Melgaço', 'Barão de Melgaço'), ('Barra do Bugres', 'Barra do Bugres'), ('Barra do Garças', 'Barra do Garças'), ('Bom Jesus do Araguaia', 'Bom Jesus do Araguaia'), ('Brasnorte', 'Brasnorte'), ('Cáceres', 'Cáceres'), ('Campinápolis', 'Campinápolis'), ('Campo Novo do Parecis', 'Campo Novo do Parecis'), ('Campo Verde', 'Campo Verde'), ('Campos de Júlio', 'Campos de Júlio'), ('Canabrava do Norte', 'Canabrava do Norte'), ('Canarana', 'Canarana'), ('Carlinda', 'Carlinda'), ('Castanheira', 'Castanheira'), ('Chapada dos Guimarães', 'Chapada dos Guimarães'), ('Cláudia', 'Cláudia'), ('Cocalinho', 'Cocalinho'), ('Colíder', 'Colíder'), ('Colniza', 'Colniza'), ('Comodoro', 'Comodoro'), ('Confresa', 'Confresa'), ("Conquista D'Oeste", "Conquista D'Oeste"), ('Cotriguaçu', 'Cotriguaçu'), ('Cuiabá', 'Cuiabá'), ('Curvelândia', 'Curvelândia'), ('Denise', 'Denise'), ('Diamantino', 'Diamantino'), ('Dom Aquino', 'Dom Aquino'), ('Feliz Natal', 'Feliz Natal'), ("Figueirópolis D'Oeste", "Figueirópolis D'Oeste"), ('Gaúcha do Norte', 'Gaúcha do Norte'), ('General Carneiro', 'General Carneiro'), ("Glória D'Oeste", "Glória D'Oeste"), ('Guarantã do Norte', 'Guarantã do Norte'), ('Guiratinga', 'Guiratinga'), ('Indiavaí', 'Indiavaí'), ('Ipiranga do Norte', 'Ipiranga do Norte'), ('Itanhangá', 'Itanhangá'), ('Itaúba', 'Itaúba'), ('Itiquira', 'Itiquira'), ('Jaciara', 'Jaciara'), ('Jangada', 'Jangada'), ('Jauru', 'Jauru'), ('Juara', 'Juara'), ('Juína', 'Juína'), ('Juruena', 'Juruena'), ('Juscimeira', 'Juscimeira'), ("Lambari D'Oeste", "Lambari D'Oeste"), ('Lucas do Rio Verde', 'Lucas do Rio Verde'), ('Luciara', 'Luciara'), ('Marcelândia', 'Marcelândia'), ('Matupá', 'Matupá'), ("Mirassol D'Oeste", "Mirassol D'Oeste"), ('Nobres', 'Nobres'), ('Nortelândia', 'Nortelândia'), ('Nossa Senhora do Livramento', 'Nossa Senhora do Livramento'), ('Nova Bandeirantes', 'Nova Bandeirantes'), ('Nova Brasilândia', 'Nova Brasilândia'), ('Nova Canaã do Norte', 'Nova Canaã do Norte'), ('Nova Guarita', 'Nova Guarita'), ('Nova Lacerda', 'Nova Lacerda'), ('Nova Marilândia', 'Nova Marilândia'), ('Nova Maringá', 'Nova Maringá'), ('Nova Monte Verde', 'Nova Monte Verde'), ('Nova Mutum', 'Nova Mutum'), ('Nova Nazaré', 'Nova Nazaré'), ('Nova Olímpia', 'Nova Olímpia'), ('Nova Santa Helena', 'Nova Santa Helena'), ('Nova Ubiratã', 'Nova Ubiratã'), ('Nova Xavantina', 'Nova Xavantina'), ('Novo Horizonte do Norte', 'Novo Horizonte do Norte'), ('Novo Mundo', 'Novo Mundo'), ('Novo Santo Antônio', 'Novo Santo Antônio'), ('Novo São Joaquim', 'Novo São Joaquim'), ('Paranaíta', 'Paranaíta'), ('Paranatinga', 'Paranatinga'), ('Pedra Preta', 'Pedra Preta'), ('Peixoto de Azevedo', 'Peixoto de Azevedo'), ('Planalto da Serra', 'Planalto da Serra'), ('Poconé', 'Poconé'), ('Pontal do Araguaia', 'Pontal do Araguaia'), ('Ponte Branca', 'Ponte Branca'), ('Pontes e Lacerda', 'Pontes e Lacerda'), ('Porto Alegre do Norte', 'Porto Alegre do Norte'), ('Porto dos Gaúchos', 'Porto dos Gaúchos'), ('Porto Esperidião', 'Porto Esperidião'), ('Porto Estrela', 'Porto Estrela'), ('Poxoréu', 'Poxoréu'), ('Primavera do Leste', 'Primavera do Leste'), ('Querência', 'Querência'), ('Reserva do Cabaçal', 'Reserva do Cabaçal'), ('Ribeirão Cascalheira', 'Ribeirão Cascalheira'), ('Ribeirãozinho', 'Ribeirãozinho'), ('Rio Branco', 'Rio Branco'), ('Rondolândia', 'Rondolândia'), ('Rondonópolis', 'Rondonópolis'), ('Rosário Oeste', 'Rosário Oeste'), ('Salto do Céu', 'Salto do Céu'), ('Santa Carmem', 'Santa Carmem'), ('Santa Cruz do Xingu', 'Santa Cruz do Xingu'), ('Santa Rita do Trivelato', 'Santa Rita do Trivelato'), ('Santa Terezinha', 'Santa Terezinha'), ('Santo Afonso', 'Santo Afonso'), ('Santo Antônio do Leste', 'Santo Antônio do Leste'), ('Santo Antônio do Leverger', 'Santo Antônio do Leverger'), ('São Félix do Araguaia', 'São Félix do Araguaia'), ('São José do Povo', 'São José do Povo'), ('São José do Rio Claro', 'São José do Rio Claro'), ('São José do Xingu', 'São José do Xingu'), ('São José dos Quatro Marcos', 'São José dos Quatro Marcos'), ('São Pedro da Cipa', 'São Pedro da Cipa'), ('Sapezal', 'Sapezal'), ('Serra Nova Dourada', 'Serra Nova Dourada'), ('Sinop', 'Sinop'), ('Sorriso', 'Sorriso'), ('Tabaporã', 'Tabaporã'), ('Tangará da Serra', 'Tangará da Serra'), ('Tapurah', 'Tapurah'), ('Terra Nova do Norte', 'Terra Nova do Norte'), ('Tesouro', 'Tesouro'), ('Torixoréu', 'Torixoréu'), ('União do Sul', 'União do Sul'), ('Vale de São Domingos', 'Vale de São Domingos'), ('Várzea Grande', 'Várzea Grande'), ('Vera', 'Vera'), ('Vila Bela da Santíssima Trindade', 'Vila Bela da Santíssima Trindade'), ('Vila Rica', 'Vila Rica')], default='(Não se aplica)', max_length=100),
        ),
        migrations.AlterField(
            model_name='tableactionmodel',
            name='outras_acoes',
            field=models.CharField(choices=[('(Não se aplica)', '(Não se aplica)'), ('Apuração de denúncias', 'Apuração de denúncias'), ('Fiscalizações e auditorias', 'Fiscalizações e auditorias'), ('Plano de Providências', 'Plano de Providências'), ('Capacitação', 'Capacitação'), ('Supervisão Técnica', 'Supervisão Técnica'), ('Formação', 'Formação'), ('Manifestação Técnica', 'Manifestação Técnica'), ('Audiência Pública', 'Audiência Pública'), ('Outros', 'Outros')], default='(Não se aplica)', max_length=100),
        ),
        migrations.AlterField(
            model_name='tableactionmodel',
            name='tecnico_nao_presencial',
            field=models.CharField(choices=[('Centrais de relacionamento', 'Centrais de relacionamento'), ('E-mails, telefonemas e mensagens', 'E-mails, telefonemas e mensagens'), ('Normas, orientações técnicas e materiais informativos', 'Normas, orientações técnicas e materiais informativos'), ('Videoconferências e transmissões ao vivo', 'Videoconferências e transmissões ao vivo'), ('Instrumentos e ferramentas informacionais do SUAS', 'Instrumentos e ferramentas informacionais do SUAS'), ('Sítios eletrônicos e aplicativos', 'Sítios eletrônicos e aplicativos'), ('(Não se Aplica)', '(Não se Aplica)')], default='(Não se aplica)', max_length=100),
        ),
        migrations.AlterField(
            model_name='tableactionmodel',
            name='tecnico_presencial',
            field=models.CharField(choices=[('Encontros de apoio técnico', 'Encontros de apoio técnico'), ('Apoio técnico individualizado no município', 'Apoio técnico individualizado no município'), ('Apoio técnico individualizado na SAAS', 'Apoio técnico individualizado na SAAS'), ('Monitoramento com periodicidade mínima anual', 'Monitoramento com periodicidade mínima anual'), ('Seminários e/ou Oficinas', 'Seminários e/ou Oficinas'), ('Visitas técnicas', 'Visitas técnicas'), ('(Não se aplica)', '(Não se aplica)')], default='(Não se aplica)', max_length=100),
        ),
    ]
