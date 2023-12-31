import pandas as pd
import numpy as np
from django.shortcuts import render
from rest_framework import viewsets
import joblib
from rest_framework.response import Response
from .forms import ApprovalForm
from .models import Approvals
from .serializers import ApprovalsSerializers
import tensorflow as tf


# Create your views here.
def perform_prediction(validated_data):
    df = pd.DataFrame(validated_data, index=[0])
    loan_status = approve_or_reject(df)
    return loan_status


class ApprovalsView(viewsets.ModelViewSet):
    queryset = Approvals.objects.all()
    serializer_class = ApprovalsSerializers

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            prediction_result = perform_prediction(serializer.validated_data)
            response_data = {'status': prediction_result}
            headers = self.get_success_headers(serializer.data)
            return Response(response_data, status=201, headers=headers)

        except ValueError as e:
            error_message = str(e)
            return Response({'message': error_message}, status=400)


# Approve or reject loan
def approve_or_reject(df):
    try:
        # Hot encoding data
        mdl = tf.keras.models.load_model('MyAPI/loan_model')
        scaler = joblib.load('MyAPI/scaler.sav')
        ohe_columns = scaler.get_feature_names_out()
        df_processed = pd.get_dummies(df)
        newdict = {}
        for i in ohe_columns:
            if i in df_processed.columns:
                newdict[i] = df_processed[i].values
            else:
                newdict[i] = 0
        data = pd.DataFrame(newdict)
        # Scaling data
        scaled_data = scaler.transform(data)
        y_pred = mdl.predict(scaled_data) > 0.53
        return np.where(y_pred, 'Approved', 'Declined')

    except Exception:
        error_message = 'An error occurred during loan prediction.'
        raise ValueError(error_message)


def cxstatus(request):
    form = ApprovalForm(request.POST)
    if form.is_valid():
        dependants = form.cleaned_data['Dependents']
        applicantincome = form.cleaned_data['ApplicantIncome']
        coapplicantincome = form.cleaned_data['CoapplicantIncome']
        loanamt = form.cleaned_data['LoanAmount']
        loanterm = form.cleaned_data['Loan_Amount_Term']
        credithistory = form.cleaned_data['Credit_History']
        gender = form.cleaned_data['Gender']
        married = form.cleaned_data['Married']
        graduatededucation = form.cleaned_data['Education']
        selfemployed = form.cleaned_data['Self_Employed']
        area = form.cleaned_data['Property_Area']

        # Create a dictionary of form field values
        data = {
            'Dependents': dependants,
            'ApplicantIncome': applicantincome,
            'CoapplicantIncome': coapplicantincome,
            'LoanAmount': loanamt,
            'Loan_Amount_Term': loanterm,
            'Credit_History': credithistory,
            'Gender': gender,
            'Married': married,
            'Education': graduatededucation,
            'Self_Employed': selfemployed,
            'Property_Area': area
        }

        # Create a DataFrame from the dictionary
        df = pd.DataFrame(data, index=[0])
        loan_status = approve_or_reject(df)
        return render(request, 'myform/status.html', {'status': loan_status, 'data': data})
    return render(request, 'myform/status.html', {'data': 'cannot retrieve data!'})


def cxcontact(request):
    form = ApprovalForm()
    return render(request, 'myform/form.html', {'form': form})
