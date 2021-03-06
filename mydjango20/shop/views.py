from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse

from shop.forms import ShopForm
from shop.models import Shop


def shop_list(request: HttpRequest) -> HttpResponse:
    qs = Shop.objects.all().order_by("-id")

    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(name__incontains=query)

    return render(request, "shop/shop_list.html", {
        "shop_list": qs,
    })


def shop_detail(request:HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, "shop/shop_detail.html", {
        "shop": shop,
    })


# /shop/new/
def shop_new(request: HttpRequest) -> HttpResponse:
    #raise NotImplementedError("곧 구현 예정")

    if request.method == "POST":
        form = ShopForm(request,POST, request.FIELS)
        if form.is_valid():
            saved_post = form.save()
            return redirect("shop:shop_detail", saved_post.pk)
    else:
        form = ShopForm()


    return render(request, "shop/shop_form.html", {
        "form": form,
    })