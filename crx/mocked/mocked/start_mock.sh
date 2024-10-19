#!/bin/bash
mitmdump -q \
    --map-local '|g.alicdn.com/|/root/mocked/g.alicdn.com/' \
    --map-local '|huodong.taobao.com/|/root/mocked/huodong.taobao.com/' \
    --map-local '|log.mmstat.com/|/root/mocked/log.mmstat.com/' \
    --map-local '|o.alicdn.com/|/root/mocked/o.alicdn.com/' \
    --set connection_strategy=lazy \
    --listen-host 127.0.0.1 --listen-port 8080 &
