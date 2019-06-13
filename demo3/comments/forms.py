from .models import Comment
from django import forms

# class CCCForm(forms.Form):
#     name= forms.CharField()
#     url = forms.URLField()
#     email=forms.EmailField()
#     content = forms.Textarea()

# 继承forms.ModelForm
class CommentForm(forms.ModelForm):
    # 关联模型
    class Meta():
        model = Comment
        # 重写模型中的部分字段
        fields = ["author", "content", "email", "url"]
        widget={'content':forms.Textarea}



# req.POST.get()
#
#
# cf = CCCForm(req.POST)
# cf.cleaned_data["user"]
#
#
# cf= CommentForm()
# c = cf.save(commit=False)
# c.save()