from django import forms
from django.conf import settings
from .models import File

import logging
logging.basicConfig(
    filename=settings.LOGFILE,
    level=logging.INFO,
    format=' %(asctime)s - %(levelname)s - %(message)s'
    )

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        readonly_fields = ['s3_key',]
        fields = ['parent', 'name', 'file', 's3_key']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        parent = self.cleaned_data.get('parent')
        logging.info('name {0}, parent {1}'.format(name, parent.name))

        # get the set of files with the same parent
        siblings = File.objects.filter(parent=parent)
        for sibling in siblings:
            if self.instance != sibling and name == sibling.name:
                raise forms.ValidationError('A File entry with that name already exists')
        return self.cleaned_data['name']
