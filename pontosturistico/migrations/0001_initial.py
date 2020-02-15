# Generated by Django 3.0.3 on 2020-02-15 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('comentario', '0001_initial'),
        ('atracoes', '0001_initial'),
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontoTuristico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('aprovado', models.BooleanField(default=False)),
                ('atracoes', models.ManyToManyField(to='atracoes.Atracao')),
                ('avaliacoes', models.ManyToManyField(to='avaliacoes.Avaliacao')),
                ('comentarios', models.ManyToManyField(to='comentario.Comentario')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enderecos.Endereco')),
            ],
        ),
    ]
