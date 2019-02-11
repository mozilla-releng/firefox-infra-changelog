class HandleArgs(object):
    """
    This class takes an input argument and calls the methods based on the
    choose argument.
    UseCase:
    # test_obj = HandleArgs()
    # try:
    #     test_obj.input_argument(sys.argv[1])
    # except IndexError:
    #     test_obj.input_argument("default")

    """
    def input_argument(self, argument):
        method_name = "method_" + str(argument).replace("-", "")
        print("Method name is: ", method_name)
        method = getattr(self, method_name, lambda: "Invalid argument!")
        return method()

    def method_default(self):
        print("No argument available!")
        return None

    def method_git(self):
        print("Runs in git only!")
        return ""

    def method_hg(self):
        print("Runs in HG only!")
        return ""

    def method_r(self):
        print("Runs in L only!")
        return ""


