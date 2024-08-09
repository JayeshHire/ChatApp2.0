# import
# adding the package to the path dynamically
import sys

sys.path.append(r"C:\Users\jayes\source\repos\python-projects\chatApp\chatApp\src\my_db_utils")

import db_data_types as db
import unittest


class TestDataTypes(unittest.TestCase):

    # check if the instance of classes inheriting DataType are callable or not
    def test_check_callable_instance(self):
        cls_objs = db.DbDataTypeMeta._instances
        for cls_obj_name, cls_obj in cls_objs.items():
            # print(cls_obj_name)
            self.assertEqual(True, callable(cls_obj()), \
                             f"Instance class {cls_obj_name} should be callable")

    # check if class with appropriate name is created or not
    def test_instance(self):
        cls_objs = db.DbDataTypeMeta._instances
        for cls_obj_name, cls_obj in cls_objs.items():
            inst = cls_obj()
            self.assertEqual(inst.__class__, cls_obj,
                             f"Name of class is not correct ")

    # check if the upon calling the instance of the class
    # it returns an instance of appropriate class or not
    def test_instance_return(self):
        cls_objs = db.DbDataTypeMeta._instances
        # print(cls_objs)
        for cls_obj_name, cls_obj in cls_objs.items():
            inst = cls_obj()
            if inst.__class__ == db.Boolean or \
                    inst.__class__ == db.UUID:
                self.assertEqual(inst(), inst.__class__.__name__.lower(),
                                 f"return value should be {inst.__class__.__name__} "
                                 f"for object of class {inst.__class__.__name__}")
            else:
                for dt, dt_cls in inst.db_types.items():
                    dtype = inst(dt)
                    self.assertIsInstance(dtype, dt_cls.__class__,
                                          f"an instance of {dt_cls.__class__.__name__} "
                                          f"should be returned."
                                          f"But instead an instance of {dtype.__class__} was returned")

    # checks if the instance of actual datatypes are callable
    # it also checks if they are returning appropriate values on calling or not
    def test_dtype_instances_callability(self):
        cls_objs = db.DbDataTypeMeta._instances
        for cls_obj_names, cls_obj in cls_objs.items():
            if cls_obj_names != 'Boolean' and cls_obj_names != 'UUID':
                inst = cls_obj()
                for dtype, dtype_cls in inst.db_types.items():
                    if dtype in ('char', 'varchar'):
                        dtype_inst = inst(dtype)
                        self.assertEqual(True, callable(dtype_inst),
                                         "instance of class object should be callable"
                                         )
                        self.assertEqual(f"{dtype}(5)", dtype_inst(n=5),
                                         f"upon calling the instance of '{dtype_inst.__class__.__name__}'"
                                         f", it should return '{dtype}(5)'")
                        continue
                    if dtype == 'numeric':
                        dtype_inst = inst(dtype)
                        self.assertEqual(True, callable(dtype_inst),
                                         "instance of class object should be callable"
                                         )
                        self.assertEqual(f"{dtype}(4, 3)", dtype_inst(d=4, p=3),
                                         f"upon calling the instance of '{dtype_inst.__class__.__name__}'"
                                         f", it should return '{dtype}(4,3)'")
                        continue
                    dtype_inst = inst(dtype)
                    self.assertEqual(True, callable(dtype_inst),
                                     "instance of class object should be callable"
                                     )
                    self.assertEqual(dtype, dtype_inst(),
                                     f"upon calling the instance of '{dtype_inst.__class__.__name__}'"
                                     f", it should return '{dtype}'")


if __name__ == "__main__":
    unittest.main()
