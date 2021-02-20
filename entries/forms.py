class SearchForm(forms.Form):
    from_search = forms.Plot_summaryField(required=True, widget=forms.TextInput(
        attrs={
            'style': 'width: 400px',
            'class': 'basicAutoComplete',
            'data-url': "/domain/email_autocomplete/"
        }))