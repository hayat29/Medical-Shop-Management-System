from django.db import models
from django import forms
from django.core.exceptions import ValidationError

# Validator to ensure positive values
def validate_positive(value):
    if value <= 0:
        raise ValidationError(f"{value} is not a positive number")

# Validator to ensure non-negative values
def validate_non_negative(value):
    if value < 0:
        raise ValidationError(f"{value} is a negative number")

# Model to represent the company providing medicines
class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

# Model to represent individual medicines
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='medicines')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(validators=[validate_positive])

    def __str__(self):
        return f"{self.name} ({self.company.name})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not hasattr(self, 'inventory'):
            Inventory.objects.create(medicine=self, stock_quantity=self.quantity)

# Model to manage the stock of medicines
class Stock(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='stocks')
    quantity_added = models.IntegerField(validators=[validate_positive])
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Stock: {self.medicine.name} - {self.quantity_added}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.medicine.quantity += self.quantity_added
        self.medicine.save()
        self.medicine.inventory.stock_quantity = self.medicine.quantity
        self.medicine.inventory.save()

# Model to manage sales
class Sell(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='sales')
    quantity_sold = models.IntegerField(validators=[validate_positive])
    date_sold = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Sold: {self.medicine.name} - {self.quantity_sold}"

    def clean(self):
        if self.quantity_sold > self.medicine.quantity:
            raise ValidationError(f"Not enough stock to sell {self.quantity_sold} units of {self.medicine.name}")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
        self.medicine.quantity -= self.quantity_sold
        self.medicine.save()
        self.medicine.inventory.stock_quantity = self.medicine.quantity
        self.medicine.inventory.save()

# Inventory model to manage overall inventory
class Inventory(models.Model):
    medicine = models.OneToOneField(Medicine, on_delete=models.CASCADE, related_name='inventory')
    stock_quantity = models.IntegerField(validators=[validate_non_negative])

    def __str__(self):
        return f"Inventory: {self.medicine.name} - {self.stock_quantity}"

# Form for Medicine
class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'company', 'price', 'quantity']

        # Optional: Customizing widgets for better UI
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter medicine name'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter price'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Enter quantity'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if Medicine.objects.filter(name=name).exists():
            raise forms.ValidationError(f"Medicine {name} already exists")