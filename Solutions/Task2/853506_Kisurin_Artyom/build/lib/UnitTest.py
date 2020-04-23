import unittest
import lab2Class
import decor
import MyJson
import random
import json
import lab2


class Lab2Tests(unittest.TestCase):
    def test_lab2Class(self):
        vec = lab2Class.vector([1, 2, 3])
        vec2 = lab2Class.vector([0, 0, 0])
        vec3 = lab2Class.vector([1, 2, 3])
        vec4 = lab2Class.vector([1, 2, 3, 4])
        self.assertEqual(vec == vec2, False)
        self.assertEqual(vec == vec4, False)
        self.assertEqual((vec + vec3).vec, [2, 4, 6])
        self.assertEqual((vec - vec3).vec, [0, 0, 0])
        self.assertEqual(vec2.len(), 0)
        self.assertEqual(str(vec2), "0,0,0")
        self.assertEqual(vec[2], 3)
        self.assertEqual(lab2Class.vector.scalar(vec, vec3), 14)
        self.assertEqual(False, vec == vec4)
        self.assertEqual(None, vec[10])
        self.assertEqual(None, vec + vec4)
        self.assertEqual(None, vec - vec4)
        self.assertEqual(None, lab2Class.vector.scalar(vec, vec4))
        self.assertEqual((vec3*1).vec, vec3.vec)

    def test_decor(self):
        self.assertEqual(decor.decorator("Artyom"), "ARTYOM")
        self.assertEqual(decor.decorator("Artyom"), "ARTYOM")
        self.assertEqual(decor.decorator("Artur"), "ARTUR")
        self.assertEqual(decor.decorator("Artur"), "ARTUR")

    def test_json(self):
        Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
        Dict2 = {'Hm': 'Kl'}
        Dict3 = {1: [1.2, 2.2, 3.3, 4.4]}
        this_list = ["apple", "banana", "cherry"]
        Dict4 = {'list': this_list}
        this_list2 = [False, True, None]
        Dict5 = {'Dict': this_list2}
        in_dict = {'Name': 'Geeks'}
        Dict6 = {'Dict': in_dict}
        self.assertEqual(MyJson.to_json(Dict), json.dumps(Dict))
        self.assertEqual(MyJson.to_json(Dict2), json.dumps(Dict2))
        self.assertEqual(MyJson.to_json(Dict3), json.dumps(Dict3))
        self.assertEqual(MyJson.to_json(Dict4), json.dumps(Dict4))
        self.assertEqual(MyJson.to_json(Dict5), json.dumps(Dict5))
        self.assertEqual(MyJson.to_json(Dict6), json.dumps(Dict6))

    def test_merge(self):
        with open('nums.txt', 'w') as f:
            f.writelines('{}\n'.format(random.randint(-100000, 100000)) for _ in range(50))
        lab2.merge("nums.txt")
        temp = 100001
        temp_bool = True
        with open('nums.txt', 'r') as f:
            for lines in f:
                if int(lines) <= int(temp):
                    temp = lines
                    continue
                else:
                    temp_bool = False
                    break;
        self.assertFalse(temp_bool)


