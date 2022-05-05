from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    address = forms.CharField(max_length=15)
    email = forms.EmailField()
    password1 = forms.DecimalField(max_digits=9)
    phone_number = forms.IntegerField(max_value=11)

    def clean(self): 
        val1 = self.cleaned_data.get("password1")
        val2 = self.cleaned_data.get("password2")
        if val1 == val2:
            return self.cleaned_data
        else:
            raise forms.ValidationError("Please confirm whether the passwords are consistent.")
