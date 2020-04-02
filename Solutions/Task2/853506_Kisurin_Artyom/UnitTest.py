import unittest
import lab2Class
import decor
import MyJson
#import lab2
class Lab2Tests(unittest.TestCase):
    def test_lab2Class(self):
        vec=lab2Class.vector([1,2,3])
        vec2=lab2Class.vector([0,0,0])
        vec3=lab2Class.vector([1,2,3])
        self.assertEqual(vec.Equal(vec2), False)
        self.assertEqual(lab2Class.vector.add(vec, vec3), [2,4,6])
        self.assertEqual(lab2Class.vector.sub(vec, vec3), [0,0,0])
        self.assertEqual(vec2.lengh(),0)
        self.assertEqual(vec2.tostring(), "0,0,0")
        self.assertEqual(vec.getbyindex(2),3)
        self.assertEqual(lab2Class.vector.scalar(vec, vec3), 14)
        
    def test_decor(self):
        self.assertEqual(decor.decorator("Artyom"),"ARTYOM")
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
       
        Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
        Dict2 = {'Hm': 'Kl'}
        self.assertEqual(MyJson.to_json(Dict),s1)
        self.assertEqual(MyJson.to_json(Dict2),s2)
       # self.assertEqual(calc.mul(2, 5), 10)
        
   # def test_div(self):
       # self.assertEqual(calc.div(8, 4), 2)

if __name__ == '__main__':
    unittest.main()