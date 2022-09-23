from django.shortcuts import render, redirect

from family_budget.models import Budget




def index(request):
    if request.user.is_authenticated:
        # budgets = Budget.objects.filter(owner=request.user)
        budgets = Budget.objects.select_related("owner").all()
        return render(request, 'budget/index.html', {'budgets':budgets})
    else:
        return render(request, 'budget/index.html')


def budget(request, slug):
    if Budget.objects.filter(slug=slug).exists():
        budget = Budget.objects.get(slug=slug)
        return render(request, 'budget/budget.html', {'budget':budget})
    else:
        return redirect('family_budget:index')


# def category(request, category):
#     try:
#         category_obj = Category.objects.get(slug=category)
#     except:
#         return return_404(request)    
        
#     product_obj = Product.objects.filter(Q(category__name__in=list(category_obj.children.all())) | Q(category__name=category_obj.name))
    
#     paginator = Paginator(product_obj, 16)
#     if 'page' in request.GET:
#         page_num = request.GET['page']
#     else:
#         page_num = 1
#     page = paginator.get_page(page_num)
#     response = paginator.page(page_num)

#     products = get_product_zip_with_images(response, True, request)

#     product_category_parents = []
#     categ = category_obj
#     while categ.parent != None:
#         product_category_parents.append(categ.parent)
#         categ = categ.parent
#     product_category_parents.reverse()

#     context = {
#         'products':products,
#         'page':page,
#         'category':category_obj,
#         'product_category_parents': product_category_parents
#     }
#     return render(request, 'cosmetics/cosmetics_list.html', context)


# def product(request, product):
#     try:
#         product_obj = Product.objects.get(slug=product)
#     except:
#         return return_404(request)
#     images = Image.objects.filter(product=product_obj)
#     related_products = []

#     # ищем подобные этому продукты
#     related_by_name = Product.objects.filter(name__icontains = str(product_obj.name)[:int(len(product_obj.name))//2]).exclude(id=product_obj.id) # берём, скажем, первую половину названия
#     if related_by_name.count() != 0: 
#         for obj in related_by_name: related_products.append(obj)

#     related_by_category = Product.objects.filter(category = product_obj.category).exclude(id=product_obj.id).exclude(id__in=[_id.id for _id in related_products])
#     if related_by_category.count != 0 and len(related_products) <= 10:
#         for obj in related_by_category: 
#             if len(related_products) <= 10:
#                 related_products.append(obj)
#             else:
#                 break

#     related_by_manufacturer = Product.objects.filter(manufacturer = product_obj.manufacturer).exclude(id=product_obj.id).exclude(id__in=[_id.id for _id in related_products])
#     if related_by_manufacturer.count != 0 and len(related_products) <= 10:
#         for obj in related_by_manufacturer: 
#             if len(related_products) <= 10:
#                 related_products.append(obj)
#             else:
#                 break


#     if str(product_obj.vendor_code) not in request.session.get('carted_prod_vend_codes', '').split(';'):
#         product_in_cart = False
#     else:
#         product_in_cart = True
#     if str(product_obj.vendor_code) not in request.session.get('liked_prod_vend_codes', '').split(';'):
#         product_in_liked = False
#     else:
#         product_in_liked = True
            
#     context = {
#         'product':product_obj,
#         'images':images,
#         'related_products':related_products,
#         'product_in_cart':product_in_cart,
#         'product_in_liked':product_in_liked,
#     }
#     return render(request, 'cosmetics/product.html', context)

# @staff_member_required
# def my_admin(request):
#     orders = Order.objects.all()
#     return render(request, 'admin_fld/admin_index.html', {'orders':orders})

# @staff_member_required
# def add_new_product(request):

#     if request.is_ajax():
#         category_id = request.GET.get('category_id', None)
#         images = request.FILES.getlist('img')

#         if category_id:
#             if category_id == '':
#                 return JsonResponse(data={
#                     'subcategories': 'empty',
#                 })

#             category = Category.objects.get(id=int(category_id))

#             subcategories = {}
#             for subcat in category.children.all():
#                 subcategories[subcat.id] = subcat.name

#             return JsonResponse(data={
#                 'subcategories':subcategories,
#             })
#         elif images:
#             uploaded_images = {}
#             for val in images:
#                 uploaded_image = Image.objects.create(image=val)
#                 uploaded_images[uploaded_image.id] = str(uploaded_image.image.url)

#             return JsonResponse(data={
#                 'uploaded_images':uploaded_images,
#             })


#     if request.method =='POST':
#         form = ProductForm(data=request.POST)
#         if form.is_valid():
#             product = form.save(commit=False)
#             try:
#                 product.category = Category.objects.get(id=int(request.POST['subcategory']))
#             except:
#                 product.category = Category.objects.get(id=int(request.POST['category']))

#             trans_name = translate_str(product.name)
#             trans_description = translate_str(html2text.html2text(product.description).replace('[','').replace(']','').replace('*','').strip())
#             trans_country = translate_str(product.country)
#             trans_active_components = translate_str(product.active_components)
#             trans_purpose = translate_str(product.purpose)
#             trans_skin_type = translate_str(product.skin_type)
#             trans_how_to_use = translate_str(product.how_to_use)

#             product.name_uk = trans_name['uk']
#             product.name_ru = trans_name['ru']
#             if get_language() == 'uk':
#                 product.description_uk = product.description
#                 product.description_ru = trans_description['ru']
#             elif get_language() == 'ru':
#                 product.description_ru = product.description
#                 product.description_uk = trans_description['uk']
#             product.country_uk = trans_country['uk']
#             product.country_ru = trans_country['ru']
#             product.active_components_uk = trans_active_components['uk']
#             product.active_components_ru = trans_active_components['ru']
#             product.purpose_uk = trans_purpose['uk']
#             product.purpose_ru = trans_purpose['ru']
#             product.skin_type_uk = trans_skin_type['uk']
#             product.skin_type_ru = trans_skin_type['ru']
#             product.how_to_use_uk = trans_how_to_use['uk']
#             product.how_to_use_ru = trans_how_to_use['ru']
            
#             product.save()
            
#             uploaded_images_ids = request.POST['uploaded_images_ids'].split(';')
#             uploaded_images_ids = [int(i) for i in uploaded_images_ids if i!='']
#             counter = 1
#             for image in Image.objects.filter(id__in = uploaded_images_ids):
#                 image.product = product
#                 # меняем название фото на название продукта для seo
#                 old_name = str(image.image)
#                 new_name = '/'.join(old_name.split('/')[:-1]) + '/' +  slugify(product.name) + '-' + str(counter) + '.' + 'jpg' #+ str(image.image).split('/')[-1].split('.')[-1]
                
#                 if os.path.exists(new_name): new_name = '/'.join(old_name.split('/')[:-1]) + '/' +  slugify(product.name) + '-' + str(random.randint(5, 20)) + '.' + 'jpg'
                
#                 os.rename(old_name, new_name) # ставим тут, потому что, когда мы меняем название image.image = new_name, django-cleanup библиотека удаляет изображение
#                 image.image = new_name
#                 image.save()
#                 counter += 1

#             # return redirect('cosmetics:all_products_admin')
#             return redirect('admin:cosmetics_product_change', product.id)
#     else:
#         form = ProductForm()
#         categories = Category.objects.filter(parent=None)
#         return render(request, 'admin_fld/add_product.html', {'form':form, 'categories':categories})

# @staff_member_required
# def all_products_admin(request):
#     return render(request, 'admin_fld/all_products_admin.html')


# @csrf_exempt
# def cart(request):
#     if request.is_ajax():
#         prod_slug = request.POST.get('prod_slug', None)
#         product = Product.objects.get(slug=prod_slug)
#         status = ''
#         action = ''
#         button_htmlContent = ''
#         if get_language() == 'uk': goto_url = '/cart/'
#         elif get_language() == 'ru': goto_url = '/ru/cart/'

#         # если в сессии у нас ничего нет, заполним данными с аккаунта пользователя
#         if request.user.is_authenticated and request.session.get('carted_prod_vend_codes', '') == '':
#             request.session['carted_prod_vend_codes'] = ';'.join([str(cart_obj.vendor_code) for cart_obj in request.user.carted.all()])
   
#         carted_prod_vend_codes = request.session.get('carted_prod_vend_codes', '')
#         if carted_prod_vend_codes != '':
#             carted_prod_vend_codes = carted_prod_vend_codes.split(';')
#             if str(product.vendor_code) in carted_prod_vend_codes:
#                 carted_prod_vend_codes.remove(str(product.vendor_code))
#                 carted_prod_vend_codes = ';'.join(carted_prod_vend_codes)
#                 request.session['carted_prod_vend_codes'] = str(carted_prod_vend_codes)

#                 status = 'remove'
#                 action = _('Удалено с корзины')
#                 button_htmlContent = '<div>'+_('Добавить в корзину') + '</div> <span>(' + _('и смотреть дальше')+')</span></a>'
#             else:
#                 carted_prod_vend_codes.append(str(product.vendor_code))
#                 carted_prod_vend_codes = ';'.join(carted_prod_vend_codes)
#                 request.session['carted_prod_vend_codes'] = str(carted_prod_vend_codes)

#                 status = 'add'
#                 action = _('Добавлено в корзину')
#                 button_htmlContent = _('Добавлено в корзину') + '!✅'
#         else:
#             request.session['carted_prod_vend_codes'] = str(product.vendor_code)

#             status = 'add'
#             action = _('Добавлено в корзину')
#             button_htmlContent = _('Добавлено в корзину') + '!✅'


#         if request.user.is_authenticated:
#             if request.user.carted.filter(id=product.id).exists():
#                 request.user.carted.remove(product)
#             else:
#                 request.user.carted.add(product)


#         return JsonResponse(data={
#             'status': status,
#             'action': action,
#             'button_htmlContent':button_htmlContent,
#             'goto_url':goto_url,
#         })
#     else:
#         vendor_codes = []
#         for v_c in request.session.get('carted_prod_vend_codes', '').split(';'):
#             try:
#                 v_c = int(v_c)
#                 vendor_codes.append(v_c)
#             except: pass

#         products = Product.objects.filter(vendor_code__in = vendor_codes )
#         all_products = get_product_zip_with_images(products)

#         total_price = 0
#         for prod in products: total_price+=prod.price
        
#         return render(request, 'cosmetics/cart.html',{'all_products':all_products, 'total_price':total_price})

# @csrf_exempt
# def liked(request):
#     if request.is_ajax():
#         prod_slug = request.POST.get('prod_slug', None)
#         product = Product.objects.get(slug=prod_slug)
#         status = ''
#         action = ''
#         button_htmlContent = ''
#         if get_language() == 'uk': goto_url = '/liked/'
#         elif get_language() == 'ru': goto_url = '/ru/liked/'

#         # если в сессии у нас ничего нет, заполним данными с аккаунта пользователя
#         if request.user.is_authenticated and request.session.get('liked_prod_vend_codes', '') == '':
#             request.session['liked_prod_vend_codes'] = ';'.join([str(cart_obj.vendor_code) for cart_obj in request.user.liked.all()])
   
#         liked_prod_vend_codes = request.session.get('liked_prod_vend_codes', '')
#         if liked_prod_vend_codes != '':
#             liked_prod_vend_codes = liked_prod_vend_codes.split(';')
#             if str(product.vendor_code) in liked_prod_vend_codes:
#                 liked_prod_vend_codes.remove(str(product.vendor_code))
#                 liked_prod_vend_codes = ';'.join(liked_prod_vend_codes)
#                 request.session['liked_prod_vend_codes'] = str(liked_prod_vend_codes)

#                 status = 'remove'
#                 action = _('Удалено с') + ' ❤️'
#                 button_htmlContent = '<div>'+_('Добавить в') + ' ❤️' + '</div> <span>(' + _('и смотреть дальше')+')</span></a>'
#             else:
#                 liked_prod_vend_codes.append(str(product.vendor_code))
#                 liked_prod_vend_codes = ';'.join(liked_prod_vend_codes)
#                 request.session['liked_prod_vend_codes'] = str(liked_prod_vend_codes)

#                 status = 'add'
#                 action = _('Добавлено в') + ' ❤️'
#                 button_htmlContent = _('Добавлено в') + ' ❤️' + '!✅'
#         else:
#             request.session['liked_prod_vend_codes'] = str(product.vendor_code)

#             status = 'add'
#             action = _('Добавлено в') + ' ❤️'
#             button_htmlContent = _('Добавлено в') + ' ❤️' + '!✅'


#         if request.user.is_authenticated:
#             if request.user.liked.filter(id=product.id).exists():
#                 request.user.liked.remove(product)
#             else:
#                 request.user.liked.add(product)


#         return JsonResponse(data={
#             'status': status,
#             'action': action,
#             'button_htmlContent':button_htmlContent,
#             'goto_url':goto_url,
#         })
#     else:
#         vendor_codes = []
#         for v_c in request.session.get('liked_prod_vend_codes', '').split(';'):
#             try:
#                 v_c = int(v_c)
#                 vendor_codes.append(v_c)
#             except Exception as e: print(e)

#         products = Product.objects.filter(vendor_code__in = vendor_codes )
#         all_products = get_product_zip_with_images(products, True, request)
        
#         return render(request, 'cosmetics/liked.html',{'all_products':all_products})


# def order(request):
#     if request.user.is_authenticated:
#         if request.user.first_name == '' or request.user.first_name == None:
#             form = OrderForm(initial={
#                 'author_name': request.session.get('author_name', ''), 
#                 'author_surname': request.session.get('author_surname', ''), 
#                 'author_phone': request.session.get('author_phone', ''), 
#                 'author_email': request.session.get('author_email', ''), 
#             })
#         else:
#             form = OrderForm(initial={
#                 'author_name': request.user.first_name, 
#                 'author_surname': request.user.last_name, 
#                 'author_phone': request.user.phone_number, 
#                 'author_email': request.user.email, 
#             })
#     else:
#         form = OrderForm(initial={
#             'author_name': request.session.get('author_name', ''), 
#             'author_surname': request.session.get('author_surname', ''), 
#             'author_phone': request.session.get('author_phone', ''), 
#             'author_email': request.session.get('author_email', ''), 
#         })

#     packaging_materials_for_np = {
#         _('Стандартная упаковка'): 7,
#     }
#     packaging_materials_for_pickup = {
#         _('Пакет-банан'): 0,
#     }

#     # если есть в запросе id товара, то оформим только его 
#     if request.GET != {}:
#         vendor_code = request.GET['vendor_code']
#         if not Product.objects.filter(vendor_code=vendor_code).exists():
#             return render(request, 'cosmetics/order.html', {'error':_('К сожалению, такого товара мы не нашли') + ' 😞'})
        
#         product = Product.objects.get(vendor_code=vendor_code)
#         image = Image.objects.filter(product=product).first()
#         product_quantity = ['1']
#         my_product = list(zip([product],[image],product_quantity))
        
#         request.session['order_vendor_codes'] = vendor_code
#         request.session['order_product_quantity'] = ';'.join(product_quantity)

#         total_price = int(product.price)
#         total_price += 7 # потому что у нас по дефолту стоит Новая почта

#         context = {
#             'packaging_materials_for_np': packaging_materials_for_np,
#             'packaging_materials_for_pickup': packaging_materials_for_pickup,
#             'products': my_product, 
#             'total_price': total_price,
#             'form':form
#         }
#         return render(request, 'cosmetics/order.html', context)
#     # если post - перешли с корзины
#     elif request.method == 'POST':
#         carted_prod_vend_codes = request.session.get('carted_prod_vend_codes', '')
#         products = Product.objects.filter(vendor_code__in = [int(prod_vc) for prod_vc in carted_prod_vend_codes.split(';')])
#         total_price = 0

#         product_quantity = request.POST.getlist('product_quantity')
#         vendor_codes = []
#         images = []
#         for i, prod in enumerate(products):
#             vendor_codes.append(str(prod.vendor_code))
#             total_price += int(prod.price) * int(product_quantity[i]) 
#             images.append(Image.objects.filter(product= prod).first())
#         my_product = list(zip(products, images, product_quantity))
#         total_price += 7 # потому что у нас по дефолту стоит Новая почта

#         request.session['order_vendor_codes'] = ';'.join(vendor_codes)
#         request.session['order_product_quantity'] = ';'.join(product_quantity)


#         context = {
#             'packaging_materials_for_np': packaging_materials_for_np,
#             'packaging_materials_for_pickup': packaging_materials_for_pickup,
#             'products': my_product, 
#             'total_price': total_price,
#             'form':form
#         }
#         return render(request, 'cosmetics/order.html', context)
#     # если ничего нет, то перейдём в корзину
#     else:
#         return redirect('cosmetics:cart')


# def order_success(request):
#     if request.method == 'POST':
#         form = OrderForm(data=request.POST)
#         if form.is_valid():
#             order = form.save(commit=False)
#             # request.session['author_name']
            
#             order.delivery_company = request.POST.get('delivery_checkbox', 'np')
#             order.delivery_way = request.POST.get('delivery_way_checkbox', '')
#             order.delivery_city = request.POST.get('city_input', '')
#             order.delivery_point = request.POST.get('delivery_point_input', '')
#             request.session['author_name'] = order.author_name
#             request.session['author_surname'] = order.author_surname
#             request.session['author_phone'] = order.author_phone
#             request.session['author_email'] = order.author_email
#             order.save()            
            
#             total_price = 0
#             products_codes = request.session.get('order_vendor_codes', '')
#             order_product_quantity = request.session.get('order_product_quantity', '').split(';')
#             products = Product.objects.filter(vendor_code__in=products_codes.split(';'))
#             for i, prod in enumerate(products): 
#                 OrderItem.objects.create(product=prod, order=order, quantity=int(order_product_quantity[i]))
#                 total_price += int(prod.price) * int(order_product_quantity[i])
#             if order.delivery_company == 'np': total_price += 7
#             order.total_price = total_price
#             if order.delivery_company == 'pickup': order.delivery_way = ''

#             order.save()  

#             # отправляем сообщения о товаре
#             created_order_func(order)
#             send_order_email_func(order)

#             # очищаем товары в корзине: в сессии и в аккаунте
#             if request.session.get('carted_prod_vend_codes', None): del request.session['carted_prod_vend_codes']
#             if request.user.is_authenticated: request.user.carted.clear()

#             return render(request, 'cosmetics/order_success.html', {'order_num':order.order_num})
#         else:
#             return render(request, 'cosmetics/order_success.html', {'error':True})
#     else:
#         return redirect('cosmetics:cart')



# import html2text
# from .models import WhySkinBlog
# def blog(request):
#     blog_obj = WhySkinBlog.objects.filter(status = 'published')
#     paginator = Paginator(blog_obj, 20)

#     page = request.GET.get('page')
#     try:
#         response = paginator.page(page)
#     except PageNotAnInteger:
#         response = paginator.page(1)
#     except EmptyPage:
#         response = paginator.page(paginator.num_pages)
    
#     yesterday_date = str(datetime.today().date().day-1).zfill(2) + '.' + str(datetime.today().date().month).zfill(2) + '.' + str(datetime.today().date().year).zfill(2) # для того, чтобы вместо дня 1 марта превратить в 01 марта

#     context={
#         'blog_obj':response, 
#         'yesterday_date': yesterday_date,
#     }

#     return render(request, 'others/blog.html', context)

# from django.db.models import F
# def blog_post(request, slug):
#     if WhySkinBlog.objects.filter(slug=slug).exists:
#         blog_obj = WhySkinBlog.objects.get(slug=slug)
#         WhySkinBlog.objects.filter(slug=slug).update(views=F('views')+1)
#         return render(request, 'others/blog_post.html', {'blog_obj':blog_obj, 'current_lang':get_language()})
#     else:
#         return redirect('account:blog')


# @staff_member_required
# def add_blog_post(request):
#     if request.method =='POST':
#         form = WhySkinBlogForm(data=request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.status = 'published'
#             trans_title = translate_str(post.title)
#             trans_content = translate_str(post.content)
#             post.title_uk = trans_title['uk']
#             post.title_ru = trans_title['ru']
#             post.content_uk = trans_content['uk']
#             post.content_ru = trans_content['ru']

#             post.save()

#             return redirect('cosmetics:blog')
#         else:
#             return redirect('cosmetics:add_blog_post')
#     else:
#         form = WhySkinBlogForm()
#         context={
#             'form':form,
#         }       
#         return render(request, 'others/blog_post_add.html', context) 




# def handler400_error(request, *args, **argv):
#     return render(request, "others/400.html")
# def handler403_error(request, *args, **argv):
#     return render(request, "others/403.html")
# def handler404_error(request, *args, **argv):
#     return render(request, "others/404.html", status=404)
# def handler500_error(request, *args, **argv):
#     return render(request, "others/500.html")

# def privacy_policy(request):
#     return render(request, "others/privacy_policy.html")
# def contract_offer(request):
#     return render(request, "others/contract_offer.html")
# def exchange_and_return(request):
#     return render(request, "others/exchange_and_return.html")
# @csrf_exempt
# def contacts(request):
#     if request.is_ajax():
#         name = request.POST.get('name', None)
#         email = request.POST.get('email', None)
#         text = request.POST.get('text', None)
        
#         text = f'Вопрос от посетителя: \n\n<strong>Имя</strong> - {name}\n<strong>Email/Номер телефона</strong> - {email}\n<strong>Вопрос</strong> - {text}' 
#         requests.get(f"https://api.telegram.org/bot{settings.TOKEN}/sendMessage?chat_id={settings.ADMIN_GROUP_TELEGRAM}&text={text}&parse_mode=HTML")

#         return JsonResponse(data={
#             'response': _('Отправлено!'),
#         })
#     else:
#         return render(request, "others/contacts.html")
# def delivery_and_payment(request):
#     return render(request, "others/delivery_and_payment.html")


# def error(request):
#     1/0
#     # return render(request, "others/exchange_and_return.html")