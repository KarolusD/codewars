def get_product_id(url):
    product_data = url[url.rindex('p')+2:]
    return product_data[:product_data.index('-')]


print('Example Tests')

print(get_product_id("http://www.exampleshop.com/fancy-coffee-cup-p-90764-12052019.html"), "90764")
print(get_product_id("http://www.exampleshop.com/dry-water-just-add-water-to-get-water-p-147-24122017.html"), "147")
print(get_product_id("http://www.exampleshop.com/public-toilet-proximity-radar-p-9423127", '9423127')
print(get_product_id("http://www.exampleshop.com/c-3-p-0-p-654-11112011.html"), "654")