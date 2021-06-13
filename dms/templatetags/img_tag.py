from django import template
register = template.Library()


def modify_url(img_url):
    img_url = str(img_url)
    return img_url.split("/")[-1]


def checkifimage(string):
    if "dms/images/" in str(string):
        return str(string).split("/")[-1]
    else:
        return string


def combine_list(l):
    # print(l[0])
    return ",".join(l)


register.filter("modify_url", modify_url)
register.filter("checkifimage", checkifimage)
register.filter("combine_list", combine_list)
