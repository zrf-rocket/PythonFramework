# @author:SteveRocket 
# @Date:2023/4/25
# @File:forms
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/

from django import forms
class ContactForm(forms.Form):
    title = forms.CharField(max_length=50)
    body = forms.CharField(max_length=255)


class ArticleCreateForm(forms.Form):
    pass

class ArticleUpdateForm(forms.Form):
    pass
