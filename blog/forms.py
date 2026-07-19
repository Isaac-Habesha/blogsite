from django import forms

from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'isPublished']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'mt-1 w-full rounded-2xl border border-white/10 bg-slate-900 px-4 py-3 text-white outline-none transition placeholder:text-slate-500 focus:border-emerald-400',
                'placeholder': 'Enter a title',
            }),
            'content': forms.Textarea(attrs={
                'class': 'mt-1 w-full rounded-2xl border border-white/10 bg-slate-900 px-4 py-3 text-white outline-none transition placeholder:text-slate-500 focus:border-emerald-400',
                'rows': 8,
                'placeholder': 'Write your blog content here',
            }),
            'isPublished': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 rounded border-white/20 bg-slate-900 text-emerald-400 focus:ring-emerald-400',
            }),
        }
