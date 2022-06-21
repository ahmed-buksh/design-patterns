from pydantic import BaseSettings


class SingletonExampleClass(BaseSettings, object):
    api_key: str = None

    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


if __name__ == '__main__':
    object1 = SingletonExampleClass()
    object2 = SingletonExampleClass()
    print(object2 == object1)
