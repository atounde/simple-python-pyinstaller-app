FROM odoo:12

USER root
# # Copy entrypoint script and Odoo configuration file
RUN pip3 install num2words xlwt xlrd
COPY ./btp/docker/entrypoint.sh /
COPY ./btp/docker/odoo.conf /etc/odoo/
RUN chown odoo /etc/odoo/odoo.conf

# # Mount /var/lib/odoo to allow restoring filestore and /mnt/extra-addons for users addons
RUN mkdir -p /mnt/extra-addons \
        && chown -R odoo /mnt/extra-addons
RUN mkdir -p /mnt/btools \
        && chown -R odoo /mnt/btools
RUN mkdir -p /mnt/btp \
        && chown -R odoo /mnt/btp
VOLUME ["/var/lib/odoo", "/mnt/extra-addons", "/mnt/btools", "/mnt/btp"]

COPY ./btools/ /mnt/btools
COPY ./btp/addons /mnt/btp

USER odoo

# ENTRYPOINT ["/entrypoint.sh"]
CMD ["odoo"]
