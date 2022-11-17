#!/usr/bin/env python
# -*- coding: utf_8 -*- 

from faker import Faker


fake = Faker('en_US')

print(fake.company())