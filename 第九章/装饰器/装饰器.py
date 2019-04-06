def demo_decorater(fun):
    def new_fun(*args,**kwargs):
        pass
        fun(*args,**kwargs)
        pass
    return new_fun

