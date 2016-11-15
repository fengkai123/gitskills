#coding=utf-8
#随机发四种颜色的牌（除去大小王）
from pprint import pprint
from random import shuffle
values = range(1,11) + 'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['%s of %s' % (v,s) for v in values for s in suits]
shuffle(deck)
# pprint(deck[:12])
while deck:  #回车一次发一张
    raw_input(deck.pop())