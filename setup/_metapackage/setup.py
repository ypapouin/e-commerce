import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-e-commerce",
    description="Meta package for oca-e-commerce Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-product_template_multi_link',
        'odoo14-addon-website_sale_attribute_filter_price',
        'odoo14-addon-website_sale_delivery_group',
        'odoo14-addon-website_sale_product_attribute_filter_category',
        'odoo14-addon-website_sale_product_description',
        'odoo14-addon-website_sale_product_detail_attribute_image',
        'odoo14-addon-website_sale_stock_available',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
