#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Demi Yu'

from kafka import KafkaConsumer

consumer = KafkaConsumer('sex')
for msg in consumer:
    print((msg.value).decode('utf8'))