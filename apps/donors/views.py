from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import DonorProfileForm


@login_required(login_url='login')
def create_donor_profile(request):
    form = DonorProfileForm()
    if request.method == 'POST':
        form = DonorProfileForm(request.POST,request.FILES)
        if form.is_valid():
            donor_profile = form.save(commit=False)
            donor_profile.user = request.user
            donor_profile.save()
            messages.success(request,'Donor profile created successfully')
            return redirect('dashboard')

    context = {'form': form}
    return render(request,'donors/create_profile.html',context)