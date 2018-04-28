# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import users.storage
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='officehour',
            name='officer_username',
        ),
        migrations.AddField(
            model_name='officehour',
            name='officer',
            field=models.ForeignKey(default=None, to='users.OfficerProfile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='berkeleyclass',
            name='class_name',
            field=models.IntegerField(choices=[(10100, 'CS 10'), (10610, 'CS 61A'), (10611, 'CS 61AS'), (10612, 'CS 61B/L'), (10613, 'CS 61C'), (10700, 'CS 70'), (10981, 'CS 98-1'), (10982, 'CS 98-2'), (10983, 'CS 98-32'), (10984, 'CS 98-47'), (11490, 'CS 149'), (11500, 'CS 150'), (11600, 'CS 160'), (11610, 'CS 161'), (11620, 'CS 162'), (11640, 'CS 164'), (11690, 'CS 169'), (11700, 'CS 170'), (11720, 'CS 172'), (11740, 'CS 174'), (11760, 'CS 176'), (11840, 'CS 184'), (11860, 'CS 186'), (11880, 'CS 188'), (11890, 'CS 189'), (11945, 'CS 194-5'), (11948, 'CS 194-8'), (11950, 'CS 195'), (11981, 'CS 198-1'), (11982, 'CS 198-2'), (11983, 'CS 198-32'), (11984, 'CS 198-47'), (20200, 'EE 20'), (20400, 'EE 40'), (21050, 'EE 105'), (21170, 'EE 117'), (21180, 'EE 118'), (21200, 'EE 120'), (21210, 'EE 121'), (21220, 'EE 122'), (21230, 'EE 123'), (21250, 'EE 125'), (21260, 'EE 126'), (21270, 'EE 127'), (21280, 'EE 128'), (21300, 'EE 130'), (21340, 'EE 134'), (21370, 'EE 137A'), (21371, 'EE 137B'), (21400, 'EE 140'), (21410, 'EE 141'), (21420, 'EE 142'), (21430, 'EE 143'), (21440, 'EE 144'), (21451, 'EE 145B'), (21470, 'EE 147'), (21490, 'EE 149'), (21500, 'EE 150'), (21920, 'EE 192'), (30010, 'Math 1A'), (30011, 'Math 1B'), (30530, 'Math 53'), (30540, 'Math 54'), (31040, 'Math 104'), (31100, 'Math 110'), (31130, 'Math 113'), (31280, 'Math 128A'), (31850, 'Math 185')]),
        ),
        migrations.AlterField(
            model_name='interviewslot',
            name='day_of_week',
            field=models.IntegerField(default=1, choices=[(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')]),
        ),
        migrations.AlterField(
            model_name='interviewslot',
            name='hour',
            field=models.IntegerField(default=9, choices=[(9, '9am - 10am'), (10, '10am - 11am'), (11, '11am - 12pm'), (12, '12pm - 1pm'), (13, '1pm - 2pm'), (14, '2pm - 3pm'), (15, '3pm - 4pm'), (16, '4pm - 5pm')]),
        ),
        migrations.AlterField(
            model_name='officehour',
            name='day_of_week',
            field=models.IntegerField(default=1, choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday')]),
        ),
        migrations.AlterField(
            model_name='officehour',
            name='hour',
            field=models.IntegerField(default=11, choices=[(11, '11 AM'), (12, '12 PM'), (13, '1 PM'), (14, '2 PM'), (15, '3 PM'), (16, '4 PM'), (17, '5 PM')]),
        ),
        migrations.AlterField(
            model_name='officerprofile',
            name='position',
            field=models.IntegerField(default=1, choices=[(1, 'President'), (2, 'Vice President'), (3, 'Secretary'), (4, 'Treasurer'), (5, 'Professional Development'), (6, 'Industrial Relations'), (7, 'Social'), (8, 'Publicity'), (9, 'Outreach'), (10, 'Web Development'), (11, 'Facilities')]),
        ),
        migrations.AlterField(
            model_name='officerprofile',
            name='term',
            field=models.CharField(verbose_name='Officer term', max_length=5, default='S15', choices=[('F95', 'Fall 1995'), ('F96', 'Fall 1996'), ('F97', 'Fall 1997'), ('F98', 'Fall 1998'), ('F99', 'Fall 1999'), ('F00', 'Fall 2000'), ('F01', 'Fall 2001'), ('F02', 'Fall 2002'), ('F03', 'Fall 2003'), ('F04', 'Fall 2004'), ('F05', 'Fall 2005'), ('F06', 'Fall 2006'), ('F07', 'Fall 2007'), ('F08', 'Fall 2008'), ('F09', 'Fall 2009'), ('F10', 'Fall 2010'), ('F11', 'Fall 2011'), ('F12', 'Fall 2012'), ('F13', 'Fall 2013'), ('F14', 'Fall 2014'), ('F15', 'Fall 2015'), ('F16', 'Fall 2016'), ('F17', 'Fall 2017'), ('F18', 'Fall 2018'), ('S95', 'Spring 1995'), ('S96', 'Spring 1996'), ('S97', 'Spring 1997'), ('S98', 'Spring 1998'), ('S99', 'Spring 1999'), ('S00', 'Spring 2000'), ('S01', 'Spring 2001'), ('S02', 'Spring 2002'), ('S03', 'Spring 2003'), ('S04', 'Spring 2004'), ('S05', 'Spring 2005'), ('S06', 'Spring 2006'), ('S07', 'Spring 2007'), ('S08', 'Spring 2008'), ('S09', 'Spring 2009'), ('S10', 'Spring 2010'), ('S11', 'Spring 2011'), ('S12', 'Spring 2012'), ('S13', 'Spring 2013'), ('S14', 'Spring 2014'), ('S15', 'Spring 2015'), ('S16', 'Spring 2016'), ('S17', 'Spring 2017'), ('S18', 'Spring 2018')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='grad_year',
            field=models.CharField(verbose_name='When are you graduating | When did you graduate?', max_length=4, default='15', choices=[('95', '1995'), ('96', '1996'), ('97', '1997'), ('98', '1998'), ('99', '1999'), ('00', '2000'), ('01', '2001'), ('02', '2002'), ('03', '2003'), ('04', '2004'), ('05', '2005'), ('06', '2006'), ('07', '2007'), ('08', '2008'), ('09', '2009'), ('10', '2010'), ('11', '2011'), ('12', '2012'), ('13', '2013'), ('14', '2014'), ('15', '2015'), ('16', '2016'), ('17', '2017'), ('18', '2018'), ('19', '2019'), ('20', '2020'), ('21', '2021')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(default='/profile_images/spock.jpg', upload_to=users.models.profile_image_path, storage=users.storage.OverwriteStorage()),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.IntegerField(verbose_name='You are a(n)', default=1, choices=[(1, 'Candidate'), (2, 'Member'), (3, 'Officer'), (4, 'Alumnus')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='year_joined',
            field=models.CharField(verbose_name='When did you join UPE?', max_length=11, default='F14', choices=[('F95', 'Fall 1995'), ('F96', 'Fall 1996'), ('F97', 'Fall 1997'), ('F98', 'Fall 1998'), ('F99', 'Fall 1999'), ('F00', 'Fall 2000'), ('F01', 'Fall 2001'), ('F02', 'Fall 2002'), ('F03', 'Fall 2003'), ('F04', 'Fall 2004'), ('F05', 'Fall 2005'), ('F06', 'Fall 2006'), ('F07', 'Fall 2007'), ('F08', 'Fall 2008'), ('F09', 'Fall 2009'), ('F10', 'Fall 2010'), ('F11', 'Fall 2011'), ('F12', 'Fall 2012'), ('F13', 'Fall 2013'), ('F14', 'Fall 2014'), ('F15', 'Fall 2015'), ('F16', 'Fall 2016'), ('F17', 'Fall 2017'), ('F18', 'Fall 2018'), ('S95', 'Spring 1995'), ('S96', 'Spring 1996'), ('S97', 'Spring 1997'), ('S98', 'Spring 1998'), ('S99', 'Spring 1999'), ('S00', 'Spring 2000'), ('S01', 'Spring 2001'), ('S02', 'Spring 2002'), ('S03', 'Spring 2003'), ('S04', 'Spring 2004'), ('S05', 'Spring 2005'), ('S06', 'Spring 2006'), ('S07', 'Spring 2007'), ('S08', 'Spring 2008'), ('S09', 'Spring 2009'), ('S10', 'Spring 2010'), ('S11', 'Spring 2011'), ('S12', 'Spring 2012'), ('S13', 'Spring 2013'), ('S14', 'Spring 2014'), ('S15', 'Spring 2015'), ('S16', 'Spring 2016'), ('S17', 'Spring 2017'), ('S18', 'Spring 2018')]),
        ),
    ]
