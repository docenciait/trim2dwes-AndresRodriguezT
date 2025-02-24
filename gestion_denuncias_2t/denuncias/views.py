from django.shortcuts import render, redirect, get_object_or_404  
from django.contrib import messages  
from .models import Denuncia  
from .forms import DenunciaForm  
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required 
def lista_denuncias(request):
    denuncias = Denuncia.objects.all()  
    return render(request, 'denuncias/lista_denuncias.html', {'denuncias': denuncias}) 



@login_required  
def crear_denuncia(request):
  if request.method == 'POST':  
    form = DenunciaForm(request.POST) 
    if form.is_valid():  
      denuncia = form.save(commit=False)  
      denuncia.save()    
      return redirect('/denuncias/lista_denuncias')  
    else:
      messages.error(request, 'Ha habido un error creando la denuncia')  
  else:
    form = DenunciaForm()  
  return render(request, 'denuncias/crear_denuncia.html', {'form': form})  
  

@login_required  
def editar_denuncia(request, denuncia_id):
    denuncia = get_object_or_404(Denuncia, id=denuncia_id)  
    if request.method == 'POST':  
      form = DenunciaForm(request.POST, instance=denuncia)  
      if form.is_valid():  
        form.save()  
        messages.success(request, 'Denuncia actualizada.')  
        return redirect('/denuncias/lista_denuncias')  
      else:
        messages.error(request, 'Ha habido un error actualizando la denuncia') 
    else:
      form = DenunciaForm()  
      return render(request, 'denuncias/editar_denuncia.html', {'form': form})

  
@login_required  
def eliminar_denuncia(request, denuncia_id):
    denuncia = get_object_or_404(Denuncia, id=denuncia_id)  
    if request.method == 'POST':  
      denuncia.delete()    
      return redirect('/denuncias/lista_denuncias')  
    return render(request, 'denuncias/eliminar_denuncia.html', {'denuncia': denuncia})