def testQue(name,gender=True):
    """
    :param name:
    :param gender:
    :return:
    """
    gender_Txt="man"
    if not gender:
        gender_Txt="woman"

    print("name is-%s,gender-%s" % (name,gender_Txt) )

testQue("afu")
testQue("yi",gender=False)
def multValues(name,*args,**kv):
    print(name)
    print(args)
    print(kv)
multValues("yi",1,2,3,k="hah",a="bb")