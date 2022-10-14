# -*- coding=utf-8 -*-
# @Time    : 2022/10/08 21:26
# @Author  : ╰☆H.俠ゞ
# =============================================================
import importlib
import inspect


def run(self):
    for key, value in self._step.items():
        class_method = str(key).split(".")
        if len(class_method) >= 2:
            self._package_name = '.'.join(class_method[0:-2])
            self._object_name = class_method[-2]
            self._object_name = class_method[-1]
        elif len(class_method) == 1:
            self._method_name = class_method[0]
        self._params = value
    class_object = self.object_get()
    method_object = self.method_get(class_object)
    return self.method_run(method_object)


def method_run(self, method_object):
    param_dict = self.get_param_dict()
    params_new = self.updata_params(self._params, param_dict)
    return method_object(*params_new)


def object_get(self):
    if self._object_name in [[], '']:
        return self
    else:
        param_dict = self.get_param_dict()
        if self._object_name in param_dict and self._package_name == '':
            return param_dict[self._object_name]
        else:
            if self._package_name == '':
                # random.random()
                self._package_name = self._object_name
            else:
                self._package_name = '.'.join([self._package_name, self._object_name])
            self._object_name = ''
            # 动态导入某个包
            name_list = self._package_name.split('.')

            def find(index):
                package_name = '.'.join(name_list[0:index + 1])
                package_target = importlib.import_module(package_name)
                importlib.invalidate_caches()
                globals()[package_name] = package_target
                if len(name_list) == index + 1:
                    return package_target
                else:
                    object_name = name_list[index + 1]
                    if hasattr(package_target, object_name):
                        object_target = getattr(package_target, object_name)
                        if inspect.ismodule(object_target):
                            return find(index + 1)
                        else:
                            return object_target
                    else:
                        return find(index + 1)

            package_target = find(0)
            return package_target

