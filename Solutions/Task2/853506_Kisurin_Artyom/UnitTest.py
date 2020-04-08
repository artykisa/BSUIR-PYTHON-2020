import unittest
import lab2Class
import decor
import MyJson
import random
import lab2

class Lab2Tests(unittest.TestCase):
    def test_lab2Class(self):
        vec = lab2Class.vector([1, 2, 3])
        vec2 = lab2Class.vector([0, 0, 0])
        vec3 = lab2Class.vector([1, 2, 3])
        vec4 = lab2Class.vector([1, 2, 3, 4])
        self.assertEqual(vec.Equal(vec2), False)
        self.assertEqual(vec.Equal(vec4), False)
        self.assertEqual(lab2Class.vector.add(vec, vec3), [2,4,6])
        self.assertEqual(lab2Class.vector.sub(vec, vec3), [0,0,0])
        self.assertEqual(vec2.lengh(),0)
        self.assertEqual(vec2.tostring(), "0,0,0")
        self.assertEqual(vec.getbyindex(2), 3)
        self.assertEqual(lab2Class.vector.scalar(vec, vec3), 14)
        self.assertRaises(Exception, vec.Equal(vec4))
        self.assertRaises(Exception, vec.getbyindex(10))
        self.assertRaises(Exception, lab2Class.vector.add(vec, vec4))
        self.assertRaises(Exception, lab2Class.vector.sub(vec, vec4))
        self.assertRaises(Exception, lab2Class.vector.scalar(vec, vec4))
        check=vec.vec
        vec.multconst(1)
        self.assertEqual(check, vec.vec)

    def test_decor(self):
        self.assertEqual(decor.decorator("Artyom"),"ARTYOM")
        self.assertEqual(decor.decorator("Artyom"),"ARTYOM")
        self.assertEqual(decor.decorator("Artur"),"ARTUR")
        self.assertEqual(decor.decorator("Artur"),"ARTUR")
        
    def test_json(self):
        s1="""{
"Name": "Geeks",
"1": 
[
\t1,
\t2,
\t3,
\t4
]
}"""
        s2="""{
"Hm": "Kl"
}"""
        s3="""{
"1": 
[
\t1.2,
\t2.2,
\t3.3,
\t4.4
]
}"""
        s4="""{
"list": 
[
\t"apple",
\t"banana",
\t"cherry"
]
}"""
        s5="""{
"Dict": 
[
\tFalse,
\tTrue,
\tnull
]
}"""
        s6="""{
"Dict": 
{
\t"Name": "Geeks"
}
}"""
        Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
        Dict2 = {'Hm': 'Kl'}
        Dict3= {1: [1.2, 2.2, 3.3, 4.4]}
        thislist = ["apple", "banana", "cherry"]
        Dict4 = {'list': thislist}
        thislist2 = [False, True, None]
        Dict5 = {'Dict': thislist2}
        InDict = {'Name': 'Geeks'}
        Dict6 = {'Dict': InDict}
        self.assertEqual(MyJson.to_json(Dict),s1)
        self.assertEqual(MyJson.to_json(Dict2),s2)
        self.assertEqual(MyJson.to_json(Dict3), s3)
        self.assertEqual(MyJson.to_json(Dict4), s4)
        self.assertEqual(MyJson.to_json(Dict5), s5)
        self.assertEqual(MyJson.to_json(Dict6), s6)

    def test_merge(self):
        with open('nums.txt', 'w') as f:
            f.writelines('{}\n'.format(random.randint(-100000, 100000)) for _ in range(50))
        lab2.merge("nums.txt")
        temp=100001
        tempbool=True
        with open('nums.txt', 'r') as f:
            for lines in f:
                if int(lines)<=int(temp):
                    temp=lines
                    continue
                else:
                    tempbool=False
                    break;
        self.assertFalse(tempbool)
if __name__ == '__main__':
    unittest.main()
