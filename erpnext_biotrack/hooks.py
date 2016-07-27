# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "erpnext_biotrack"
app_title = "ERPNext BioTrack"
app_publisher = "Webonyx"
app_description = "BioTrack connector for ERPNext"
app_icon = "octicon octicon-globe"
app_color = "green"
app_email = "jared@webonyx.com"
app_license = "MIT"

fixtures = [
	{
		"doctype": "Custom Field",
		"filters": [
			["name", "in", (
				# Item Group
				"Item Group-external_id",
				"Item Group-can_be_collected",

				# Employee
				"Employee-external_id",
				"Employee-external_transaction_id",
				"Employee-wa_state_compliance_sync",


				"Warehouse-external_id",
				"Warehouse-external_transaction_id",
				"Warehouse-plant_room",
				"Warehouse-quarentine",
				"Warehouse-wa_state_compliance_sync",

				# Customer
				"Customer-wa_state_compliance_sync",
				"Customer-external_transaction_id",
				"Customer-ubi",
				"Customer-license_no",

				# Stock Entry
				"Stock Entry-external_id",
				"Stock Entry-is_plant",
				"Stock Entry-external_transaction_id",
				"Stock Entry-wa_state_compliance_sync",

				# Stock Entry Detail
				"Stock Entry Detail-strain"
			)]
		]
	},
	{
		"doctype": "Item Group",
		"filters": [
			{
				"parent_item_group": "WA State Classifications"
			}
		]
	},
	'Stock Status'
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_biotrack/css/erpnext_biotrack.css"
# app_include_js = "/assets/erpnext_biotrack/js/erpnext_biotrack.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_biotrack/css/erpnext_biotrack.css"
# web_include_js = "/assets/erpnext_biotrack/js/erpnext_biotrack.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erpnext_biotrack.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_biotrack.install.before_install"
after_install = "erpnext_biotrack.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_biotrack.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
	# 	"all": [
	# 		"erpnext_biotrack.tasks.all"
	# 	],
	"daily": [
		"erpnext_biotrack.tasks.daily"
	],
	"hourly": [
		"erpnext_biotrack.tasks.hourly"
	],
	"weekly": [
		"erpnext_biotrack.tasks.weekly"
	]
	# 	"monthly": [
	# 		"erpnext_biotrack.tasks.monthly"
	# 	]
}

# Testing
# -------

# before_tests = "erpnext_biotrack.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_biotrack.event.get_events"
# }
