#bafomet
import base64, codecs
magic = 'I0RldmVsb3BlciBieSBCYWZvbWV0CiMgLSotIGNvZGluZzogdXRmLTggLSotCicnJwrQoNC10LTQsNC60YLQuNGA0L7QstCw0Lsg0LrQvtC0IGwzZTg2CicnJwppbXBvcnQgb3MKaW1wb3J0IHJlcXVlc3RzCmltcG9ydCBqc29uCmltcG9ydCB0aW1lCmltcG9ydCBnZXRwYXNzCmltcG9ydCBzdWJwcm9jZXNzCldIU0wgPSAnXDAzM1sxOzMybScKRU5ETCA9ICdcMDMzWzBtJwpSRURMID0gJ1wwMzNbMDszMW0nCkdOU0wgPSAnXDAzM1sxOzM0bScKCmNsYXNzIFpvb21FeWUob2JqZWN0KToKICAgIGRlZiBfX2luaXRfXyhzZWxmLCB1c2VybmFtZT1Ob25lLCBwYXNzd29yZD1Ob25lKToKICAgICAgICBzZWxmLnVzZXJuYW1lID0gdXNlcm5hbWUKICAgICAgICBzZWxmLnBhc3N3b3JkID0gcGFzc3dvcmQKCiAgICAgICAgc2VsZi5hY2Nlc3NfdG9rZW4gPSAnJwogICAgICAgICMgc2VsZi56b29tZXllX2xvZ2luX2FwaSA9ICJodHRwczovL2FwaS56b29tZXllLm9yZy91c2VyL2xvZ2luIgogICAgICAgICMgc2VsZi56b29tZXllX2RvcmtfYXBpID0gImh0dHBzOi8vYXBpLnpvb21leWUub3JnL3t9L3NlYXJjaCIKCiAgICAgICAgc2VsZi5pcF9wb3J0X2xpc3QgPSBbXQoKICAgICAgICBzZWxmLmxvYWRfYWNjZXNzX3Rva2VuKCkKCiAgICBkZWYgbG9hZF9hY2Nlc3NfdG9rZW4oc2VsZik6CiAgICAgICAgaWYgbm90IG9zLnBhdGguaXNmaWxlKCdhY2Nlc3NfdG9rZW4udHh0Jyk6CiAgICAgICAgICAgIHByaW50KFdIU0wgKyfQlNCw0LLQsNC5INGJ0LDRgSDQstC+0LnQtNC10Lwg0LIg0YLQstC+0Lkg0LDQutC60LDRg9C90YIsINC00LvRjyDQvtGB0YPRidC10YHRgtCy0LvQtdC90LjRjyDQv9C+0LjRgdC60LAuLi4nKQogICAgICAgICAgICBzZWxmLmxvZ2luKCkKICAgICAgICBlbHNlOgogICAgICAgICAgICB3aXRoIG9wZW4oJ2FjY2Vzc190b2tlbi50eHQnLCAncicpIGFzIGZyOgogICAgICAgICAgICAgICAgc2VsZi5hY2Nlc3NfdG9rZW4gPSBmci5yZWFkKCkKCiAgICBkZWYgc2F2ZV9hY2Nlc3NfdG9rZW4oc2VsZik6CiAgICAgICAgd2l0aCBvcGVuKCdhY2Nlc3NfdG9rZW4udHh0JywgJ3cnKSBhcyBmdzoKICAgICAgICAgICAgZncud3JpdGUoc2VsZi5hY2Nlc3NfdG9rZW4pCgogICAgZGVmIGxvZ2luKHNlbGYpOgogICAgICAgICIiIgogICAgICAgINCf0YDQtdC00LvQsNCz0LDRjiDQstCy0LXRgdGC0Lgg0LjQvNGPINGD0YfQtdGC0L3QvtC5INC30LDQv9C40YHQuCDQuCDQv9Cw0YDQvtC70YwKICAgICAgICA6cmV0dXJuOiBOb25lCiAgICAgICAgIiIiCiAgICAgICAgdHJ5OgogICAgICAgICAgICBzZWxmLnVzZXJuYW1lID0gaW5wdXQoR05TTCsgJ1sgKyBdICB1c2VybmFtZSA6Jykuc3RyaXAoKQogICAgICAgICAgICAjbDNlODY6INC00L7QsdCw0LLQuNC7INGE0LjRh9GDINGB0LrRgNGL0YLQvtCz0L4g0LLQstC+0LTQsCDQv9Cw0YDQvtC70Y8gICAgICAgICAgIAogICAgICAgICAgICBzZWxmLnBhc3N3b3JkID0gZ2V0cGFzcy5nZXRwYXNzKEdOU0wrICdbICsgXSAgcGFzc3dvcmQgOicpLnN0cmlwKCkKICAgICAgICAgICAgCiAgICAgICAgI2wzZTg2OiDQutC70LDRgdGB0LjQutCwLCDQtdGB0LvQuCDQvdCw0LbQuNC80LDQtdC8IDAg0YLQviDQuNC00LXQvCDQsiDRj9C00YDQviwg0LXQvdGC0YAgCiAgICAgICAgZXhjZXB0IEtleWJvYXJkSW50ZXJydXB0OgogICAgICAgICAgICBjaG9pc2VfZXhpdCA9IGlucHV0KCdcbls/XSDQtdGB0LvQuCDQvdGD0LbQvdC+INCy0YvQudGC0Lgg0LIg0LPQu9Cw0LLQvdC+0LUg0LzQtdC90Y4g0L3QsNC20LzQuNGC0LUgOTkg0LjQu9C4IEVudGVyLCDRh9GC0L7QsdGLINC/0YDQvtC00L7Qu9C20LjRgtGMINGA0LDQsdC+0YLQsNGC0Ywg0YEg0LzQvtC00YPQu9C10Lw6JykKICAgICAgICAgICAgaWYgY2hvaXNlX2V4aXQgPT0gJzAnOgogICAgICAgICAgICAgICAgI2wzZTg2OiDQv9C10YDQtdGF0L7QtCDQuiDRj9C00YDRgyDQstC+INCy0YHQtdGFINC00YDRg9Cz0LjRhSDRgdC70YPRh9Cw0Y/RhSDQstC+0LfQstGA0LDRgiDQuiDQuNC00LXQvdGC0LjRhNC40LrQsNGG0LjQuAogICAgICAgICAgICAgICAgc3VicHJvY2Vzcy5jYWxsKCdweXRob24'
love = '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'
god = 'FuCiAgICAgICAgd2hpbGUgVHJ1ZToKICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgIyDQodGC0YDQvtC60LAg0LTQu9GPINC/0L7QuNGB0LrQsCAgcXVlcnkgPSAncG9ydDo4MCB3ZWJsb2dpYyBjb3VudHJ5OkNoaW5hJwogICAgICAgICAgICAgICAgcXVlcnkgPSBpbnB1dChSRURMICsgIuKUlOKUgOKUgD4gIisgV0hTTCArIiDQktCy0L7QtNC4INC/0L7QuNGB0LrQvtCy0L7QuSDQt9Cw0L/RgNC+0YEgIitHTlNMKyIoIitSRURMICsgIm1haW5fbWVudSIgKyBHTlNMICsgIikiK0VOREwgKyAiPiAiKQoKICAgICAgICAgICAgICAgICMg0KPRgdGC0LDQvdC+0LLQuNGC0LUg0L3QsNGH0LDQu9GM0L3Rg9GOINGB0YLRgNCw0L3QuNGG0YMg0LTQu9GPINC/0L7Qu9GD0YfQtdC90LjRjyDRgNC10LfRg9C70YzRgtCw0YLQvtCyLCDRh9GC0L4g0LHQvtC70LXQtSDQv9C+0LvQtdC30L3Qviwg0LrQvtCz0LTQsCDRgdGD0LzQvNCwINC+0YLQvdC+0YHQuNGC0LXQu9GM0L3QviDQstC10LvQuNC60LAKICAgICAgICAgICAgICAgIHBhZ2UgPSBpbnQoaW5wdXQoUkVETCArICLilJTilIDilIA+IisgV0hTTCArIiDQoSDQutCw0LrQvtC5INGB0YLRgNCw0L3QuNGG0Ysg0L3QsNGH0LDRgtGMID8g0LLQstC10LTQuCDQvdC+0LzQtdGAICIrR05TTCsiKCIrUkVETCArICJtYWluX21lbnUiICsgR05TTCArICIpIitFTkRMICsgIj4gIikpCgogICAgICAgICAgICAgICAgIyDQo9GB0YLQsNC90L7QstC40YLQtSDQutC+0LvQuNGH0LXRgdGC0LLQviDRgdGC0YDQsNC90LjRhiDRgNC10LfRg9C70YzRgtCw0YLQvtCyCiAgICAgICAgICAgICAgICBudW0gPSBpbnQoaW5wdXQoUkVETCArICLilJTilIDilIA+ICIrIFdIU0wgKyIg0JLQstC10LTQuNGC0LUg0LrQvtC70LjRh9C10YHRgtCy0L4g0YHRgtGA0LDQvdC40YYsINC60L7RgtC+0YDRi9C1INCy0Ysg0YXQvtGC0LjRgtC1INC/0L7Qu9GD0YfQuNGC0YwgIitHTlNMKyIoIitSRURMICsgIm1haW5fbWVudSIgKyBHTlNMICsgIikiK0VOREwgKyAiPiAiKSkKCiAgICAgICAgICAgICAgICBpbmRleCA9IDAKICAgICAgICAgICAgICAgIHdoaWxlIFRydWU6CiAgICAgICAgICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgICAgICAgICAjINCe0LHRitC10LTQuNC90LjRgtC1INGB0YLRgNC+0LrRgyDQt9Cw0L/RgNC+0YHQsCDQuCDQvdC+0LzQtdGAINGB0YLRgNCw0L3QuNGG0Ysg0LTQu9GPINGB0L7Qt9C00LDQvdC40Y8gVVJMCiAgICAgICAgICAgICAgICAgICAgICAgIGlmIGluZGV4ID09IG51bToKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGJyZWFrCiAgICAgICAgICAgICAgICAgICAgICAgIG1zZyA9IEdOU0wgKydbe30ve31dINCf0L7Qu9GD0YfQsNGOINGB0YLRgNCw0L3QuNGG0YM6IHt9Jy5mb3JtYXQoaW5kZXgrMSwgbnVtLCBwYWdlKQogICAgICAgICAgICAgICAgICAgICAgICBwcmludChtc2cpCgogICAgICAgICAgICAgICAgICAgICAgICBhcGkgPSAnaHR0cHM6Ly9hcGkuem9vbWV5ZS5vcmcvaG9zdC9zZWFyY2gnCiAgICAgICAgICAgICAgICAgICAgICAgICMgc2VhcmNodXJsID0gJ3t9e30mcGFnZT17fScuZm9ybWF0KGFwaSwgcXVlcnksIHBhZ2UpCiAgICAgICAgICAgICAgICAgICAgICAgIHByaW50KFdIU0wgKyfQktGL0LLQvtC20YMg0LfQsNC/0YDQvtGBIDonLCBxdWVyeSkKCiAgICAgICAgICAgICAgICAgICAgICAgICMg0JjRgdC/0L7Qu9GM0LfRg9C10YLRgdGPINC00LvRjyDQv9C+0LvRg9GH0LXQvdC40Y8g0YDQtdC30YPQu9GM0YLQsNGC0L7QsiDQvdCwINGB0LvQtdC00YPRjtGJ0LXQuSDRgdGC0YDQsNC90LjRhtC1CiAgICAgICAgICAgICAgICAgICAgICAgIHBhZ2UgKz0gMQogICAgICAgICAgICAgICAgICAgICAgICBpbmRleCArPSAxCgogICAgICAgICAgICAgICAgICAgICAgICByZXNwID0gcmVxdWVzdHMuZ2V0KGFwaSwgaGVhZGVycz1oZWFkZXJzLCBwYXJhbXM9eyJxdWVyeSI6IHF1ZXJ5LCAicGFnZSI6IHBhZ2V9KQogICAgICAgICAgICAgICAgICAgICAgICByX2RlY29kZWQgPSBqc29uLmxvYWRzKHJlc3AudGV4dCkKICAgICAgICAgICAgICAgICAgICAgICAgZm9yIHggaW4gcl9kZWNvZGVkWydtY'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))