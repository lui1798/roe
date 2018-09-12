#!/usr/bin/env python
# _#_ coding:utf-8 _*_
from django.conf.urls import url
from api.views import user_api
from django.conf.urls import url
from api.views import (wiki_api, assets_api, deploy_api, cron_api,
                       logs_api, ansible_api, db_api, users_api,
                       orders_api, files_api, task_api)

urlpatterns = [

    url(r'^assets/(?P<id>[0-9]+)/$', assets_api.asset_detail,name='api_asset'),
    url(r'^assets/info/(?P<id>[0-9]+)/$', assets_api.asset_info,name='api_asset_info'),
    url(r'^service/$', assets_api.service_list,name='api_service'), #应用服务
    url(r'^service/(?P<id>[0-9]+)/$', assets_api.service_detail,name='api_service_detail'), #应用服务管理
    url(r'^project/$', assets_api.project_list,name='api_project'),#产品线项目
    url(r'^project/(?P<id>[0-9]+)/$', assets_api.project_detail,name='api_project_detail'),
    url(r'^group/$', assets_api.group_list,name='api_asset_group'),
    url(r'^group/(?P<id>[0-9]+)/$', assets_api.group_detail,name='api_asset_group_detail'),
    url(r'^user/$', users_api.user_list,name='api_user_list'),
    url(r'^user/(?P<id>[0-9]+)/$', users_api.user_detail,name='api_user_detail'),
    url(r'^zone/$', assets_api.zone_list),
    url(r'^zone/(?P<id>[0-9]+)/$', assets_api.zone_detail),
    url(r'^line/$', assets_api.line_list ,name='api_asset_line'),
    url(r'^line/(?P<id>[0-9]+)/$', assets_api.line_detail,name='api_asset_line_detail'),
    url(r'^raid/$', assets_api.raid_list,name='api_asset_raid'),
    url(r'^raid/(?P<id>[0-9]+)/$', assets_api.raid_detail,name='api_asset_raid_detail'),
    url(r'^server/$', assets_api.asset_server_list,name='api_machine'),
    url(r'^server/(?P<id>[0-9]+)/$', assets_api.asset_server_detail,name='api_machine_detail'),

    url(r'^cron/$', cron_api.cron_list,name='api_crontab'),
    url(r'^cron/(?P<id>[0-9]+)/$', cron_api.cron_detail,name='api_crontab_detail'),
    url(r'^playbook/$', ansible_api.playbook_list),
    url(r'^playbook/(?P<id>[0-9]+)/$', ansible_api.playbook_detail),
    url(r'^inventory/(?P<id>[0-9]+)/$', ansible_api.inventory_detail),
    url(r'^host/vars/(?P<id>[0-9]+)/$', ansible_api.ansible_host_vars),
    url(r'^deploy/$', deploy_api.deploy_list),
    url(r'^deploy/(?P<id>[0-9]+)/$', deploy_api.deploy_detail),
    url(r'^inc/config/$', db_api.inc_list),
    url(r'^inc/config/(?P<id>[0-9]+)/$', db_api.inc_detail),
    url(r'^db/config/$', db_api.db_list),
    url(r'^db/config/(?P<id>[0-9]+)/$', db_api.db_detail),
    url(r'^db/status/(?P<id>[0-9]+)/$', db_api.db_status),
    url(r'^db/org/(?P<id>[0-9]+)/$', db_api.db_org),
    url(r'^orders/(?P<id>[0-9]+)/$', orders_api.order_detail),
    url(r'^sql/custom/$', db_api.sql_custom_list),
    url(r'^sql/custom/(?P<id>[0-9]+)/$', db_api.sql_custom_detail),
    url(r'^wiki/tag/$', wiki_api.tag_list),
    url(r'^wiki/tag/(?P<id>[0-9]+)/$', wiki_api.tag_detail),
    url(r'^wiki/category/$', wiki_api.category_list),
    url(r'^wiki/category/(?P<id>[0-9]+)/$', wiki_api.category_detail),
    url(r'^wiki/archive/(?P<id>[0-9]+)/$', wiki_api.archive_detail),
    url(r'^file/upload/$', files_api.upload_file_list),
    url(r'^file/upload/(?P<id>[0-9]+)/$', files_api.upload_file_detail),
    url(r'^file/download/$', files_api.download_file_list),
    url(r'^file/download/(?P<id>[0-9]+)/$', files_api.download_file_detail),
    url(r'^task/crontab/$', task_api.task_crontab_list),
    url(r'^task/crontab/(?P<id>[0-9]+)/$', task_api.task_crontab_detail),
    url(r'^task/intervals/$', task_api.task_intervals_list),
    url(r'^task/intervals/(?P<id>[0-9]+)/$', task_api.task_intervals_detail),
    url(r'^logs/assets/(?P<id>[0-9]+)/$', assets_api.assetsLog_detail),
    url(r'^logs/cron/(?P<id>[0-9]+)/$', cron_api.cronLogsdetail),
    url(r'^logs/ansible/model/(?P<id>[0-9]+)/$', ansible_api.modelLogsdetail),
    url(r'^logs/ansible/playbook/(?P<id>[0-9]+)/$', ansible_api.playbookLogsdetail),
    url(r'^logs/deploy/(?P<id>[0-9]+)/$', deploy_api.deployLogs_detail),
    url(r'^logs/search/model/$', logs_api.AnsibleModelLogsList),
    url(r'^logs/search/playbook/$', logs_api.AnsiblePlayBookLogsList),
    url(r'^logs/sql/(?P<id>[0-9]+)/$', db_api.sql_exec_logs),
    url(r'^user/$', user_api.user_list),
    url(r'^user/(?P<id>[0-9]+)/$', user_api.user_detail),
]
