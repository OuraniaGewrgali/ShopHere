from django import forms

SORT_CHOICES = [
    ("-created_at", "Νεότερα"),
    ("price", "Τιμή ↑"),
    ("-price", "Τιμή ↓"),
    ("title", "Αλφαβητικά (Α-Ω)"),
    ("-title", "Αλφαβητικά (Ω-Α)"),
]

class BookFilterForm(forms.Form):
    q = forms.CharField(required=False, label="Αναζήτηση")
    category = forms.CharField(required=False, label="Κατηγορία")
    sort = forms.ChoiceField(choices=SORT_CHOICES, required=False, label="Ταξινόμηση")
    min_price = forms.DecimalField(required=False, min_value=0, label="Ελάχιστη τιμή")
    max_price = forms.DecimalField(required=False, min_value=0, label="Μέγιστη τιμή")
