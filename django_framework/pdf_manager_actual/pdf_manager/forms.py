from django import forms

class PdfUploadForm(forms.Form):
    file = forms.FileField(label="上传PDF文件")
    md5 = forms.CharField(max_length=100, min_length=10)
    page = forms.IntegerField(min_value=1, label='输入抓取页码')