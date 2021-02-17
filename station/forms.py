from django import forms
from .models import Species, Genus, Family

class SpeciesForm(forms.ModelForm):
    class Meta: 
        model = Species
        fields = ('family', 'genus_name', 'species_name', 'name', 'author', 'remark')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['genus_name'].queryset = Genus.objects.none() # передаем пустой набор родовых названий
    
        # для пост-запроса с созданием нового вида передаются родовые названия в соответствии с выбранным семейством
        if 'family' in self.data:
            try:
                family_id = int(self.data.get('family'))
                self.fields['genus_name'].queryset = Genus.objects.filter(family_name_id=family_id).order_by('name')
                
            # ошибочный ввод игнорируется и передается пустой набор родовых названий
            except (ValueError, TypeError):
                pass
        # для запроса с изменением вида передаются родовые названия в соответствии с уже установленным семейством
        elif self.instance.pk:
           self.fields['genus_name'].queryset = self.instance.family.genus_name.order_by('name')

