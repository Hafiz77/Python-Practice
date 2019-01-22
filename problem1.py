#Problem 1

a = {
"key1": 1,
"key2": {
    "key3": 1,
    "key4": {
        "key5": 4,
        "key6":{
            "key7":{
                "key8":5
                }
            }
        }
    }
}



def findDepth(dictionary, depth =1 ,d = {}):
    for key, value in dictionary.items():
        d[key] = depth;
        if type(value) is dict:
            findDepth(value, depth+1)
    return d;

def print_depth(data):
    d = findDepth(data)
    for key, value in sorted(d.iteritems(), key=lambda (k,v): (v,k)):
        print "%s: %s" % (key, value)
    
print_depth(a)
