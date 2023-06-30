from django.forms import ModelForm
from .models import Approvals


class ApprovalForm(ModelForm):
    class Meta:
        model = Approvals
        fields = '__all__'

