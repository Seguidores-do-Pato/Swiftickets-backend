import uuid

def img_path(instance, filename):
    return "{0}_{1}".format(uuid.uuid4(), filename)