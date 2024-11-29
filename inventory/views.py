from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book, Author, Category
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def book_list(request):
    books = Book.objects.all()
    return render(request, 'inventory/book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'inventory/book_detail.html', {'book': book})


@login_required
def book_add(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('inventory:book_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BookForm()
    return render(request, 'inventory/book_form.html', {'form': form})


@login_required
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('inventory:book_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BookForm(instance=book)
    return render(request, 'inventory/book_form.html', {'form': form})


@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('inventory:book_list')
    return render(request, 'inventory/book_confirm_delete.html', {'book': book})