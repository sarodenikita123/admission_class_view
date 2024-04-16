from django.shortcuts import render, redirect
from .forms import AdmissionForm
from .models import Admission
from django.views import View


class CreateView(View):
    template_name = "crud_app/create.html"
    form = AdmissionForm

    def get(self, request):
        form = self.form()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
        return render(request, self.template_name, {"form": form})


class ShowView(View):
    template_name = "crud_app/show.html"
    form = AdmissionForm

    def get(self, request):
        form = self.form()
        obj = Admission.objects.all()
        context = {"obj": obj, "form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
        return render(request, self.template_name, {"form": form})


class UpdateView(View):
    template_name = "crud_app/create.html"
    form = AdmissionForm

    def get(self, request, pk):
        obj = Admission.objects.get(id=pk)
        form = AdmissionForm(request.POST, instance=obj)
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        template_name = "crud_app/create.html"
        obj = Admission.objects.get(id=pk)
        form = AdmissionForm(request.POST, instance=obj)
        context = {"form": form}
        if form.is_valid():
            form.save()
            return redirect("show_url")
        return render(request, template_name, context)


class DeleteView(View):
    template_name = "crud_app/confirm.html"
    form = AdmissionForm

    def get(self, request, pk):
        obj = Admission.objects.get(id=pk)
        form = self.form(request.POST, instance=obj)
        context = {"obj": obj, "form": form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        obj = Admission.objects.get(id=pk)
        obj.delete()
        return redirect("show_url")





