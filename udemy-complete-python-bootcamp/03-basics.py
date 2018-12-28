#!/usr/bin/env python3
import unittest

class TestBasics(unittest.TestCase):

    def test_numbers(self):
        self.assertEqual(2 + 1, 3)
        self.assertEqual(2 - 1, 1)
        self.assertEqual(2 * 2, 4)
        self.assertEqual(3 / 2 , 1.5)
        self.assertEqual(7 / 4, 1.75)
        self.assertEqual(7 % 4, 3)
        self.assertEqual(50 % 5, 0)
        self.assertEqual(23 % 2, 1)
        self.assertEqual(20 % 2, 0)
        self.assertEqual(2 ** 3, 8)
        self.assertEqual(2 + 10 * 10 + 3, 105)
        self.assertEqual((2 + 10) * (10 + 3), 156)

    def test_types(self):
        self.assertEqual(type(10), int)
        self.assertEqual(type(30.1), float)
        self.assertEqual(type('hello'), str)
        self.assertEqual(type({}), dict)
        self.assertEqual(type({ 'a': 1 }), dict)
        self.assertEqual(type([]), list)
        self.assertEqual(type([1, 2]), list)
        self.assertEqual(type(()), tuple)
        self.assertEqual(type((1, 2)), tuple)

    def test_strings(self):
        self.assertEqual('hello', "hello")
        self.assertEqual(len('hello'), 5)
        self.assertEqual('Hello World'[0], 'H')
        self.assertEqual('Hello World'[8], 'r')
        self.assertEqual('Hello World'[-2], 'l')
        self.assertEqual('Hello World'[-2], 'l')
        self.assertEqual(type('Hello World'[2]), str)
        self.assertEqual('abcdefghijk'[2:], 'cdefghijk')
        self.assertEqual('abcdefghijk'[:4], 'abcd')
        self.assertEqual('abcdefghijk'[2:4], 'cd')
        self.assertEqual('abcdefghijk'[::2], 'acegik')
        self.assertEqual('abcdefghijk'[::-1], 'kjihgfedcba')
        self.assertEqual('abcdefghijk'[2:8:2], 'ceg')
        self.assertEqual('abc' + 'def', 'abcdef')
        self.assertEqual('z' * 3, 'zzz')
        self.assertEqual('abc' * 3, 'abcabcabc')
        self.assertEqual('Hello'.upper(), 'HELLO')
        self.assertEqual('Hello'.lower(), 'hello')
        self.assertEqual('hello world'.split(), ['hello', 'world'])
        self.assertEqual('hello world'.split('o'), ['hell', ' w', 'rld'])
        self.assertEqual('Hello {}'.format('world'), 'Hello world')
        self.assertEqual('A {} {} {}'.format('D', 'C', 'B'), 'A D C B')
        self.assertEqual('A{2}{0}{1}{2}{0}'.format('D', 'C', 'B'), 'ABDCBD')
        self.assertEqual('A {b} {c} {d}'.format(d='D', c='C', b='B'), 'A B C D')
        self.assertEqual('{r}'.format(r=100/777), '0.1287001287001287')
        self.assertEqual('{r:.4}'.format(r=100/777), '0.1287')
        self.assertEqual('{r:8.4}'.format(r=100/777), '  0.1287')
        self.assertEqual('{r:8.4f}'.format(r=100), '100.0000')
        self.assertEqual(f'{33:8.4f}', ' 33.0000')

    def test_list(self):
        self.assertEqual(len(['a', 100, 23.2]), 3)
        self.assertEqual([1, 2, 3][0], 1)
        self.assertEqual([1, 2, 3][1:], [2, 3])
        self.assertEqual([1, 2, 3] + [4, 5], [1, 2, 3, 4, 5])
        a = [1, 2, 3]; self.assertEqual(2 * a, [1, 2, 3, 1, 2, 3])
        a = [1, 2, 3]; a[0] = 4; self.assertEqual(a, [4, 2, 3])
        a = [1, 2, 3]; self.assertEqual(a.pop(), 3); self.assertEqual(a, [1, 2])
        a = [1, 2, 3]; self.assertEqual(a.pop(1), 2); self.assertEqual(a, [1, 3])
        a = [5, 2, 7]; a.sort(); self.assertEqual(a, [2, 5, 7])
        a = [5, 2, 7]; a.reverse(); self.assertEqual(a, [7, 2, 5])

if __name__ == '__main__':
    unittest.main()

