# Generated by Django 4.1 on 2023-05-04 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0007_ad_as_bs_ch_ee_en_ep_fs_hc_hrc_hs_iac_jl_mac_l_mac_m_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='floor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='as',
            name='floor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='bs',
            name='floor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='ch',
            name='floor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='direcrions_post',
            name='floor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='ee',
            name='floor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='en',
            name='floor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='ep',
            name='floor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='fs',
            name='floor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='hc',
            name='floor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='hrc',
            name='floor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='hs',
            name='floor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='iac',
            name='floor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='jl',
            name='floor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='mac_l',
            name='floor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='mac_m',
            name='floor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='mm',
            name='floor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='om',
            name='floor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='sh',
            name='floor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='tfd',
            name='floor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='tsd',
            name='floor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='tta',
            name='floor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='ttd',
            name='floor',
            field=models.CharField(default='', max_length=100),
        ),
    ]