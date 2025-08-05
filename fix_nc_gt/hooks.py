app_name = "fix_nc_gt"
app_title = "Fix Nc Gt"
app_publisher = "Jorux"
app_description = "Fix para deducir las notas de credito del outstanding amount en las sales invoices en erpnext."
app_email = "rodrishishi@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "fix_nc_gt",
# 		"logo": "/assets/fix_nc_gt/logo.png",
# 		"title": "Fix Nc Gt",
# 		"route": "/fix_nc_gt",
# 		"has_permission": "fix_nc_gt.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/fix_nc_gt/css/fix_nc_gt.css"
# app_include_js = "/assets/fix_nc_gt/js/fix_nc_gt.js"

# include js, css files in header of web template
# web_include_css = "/assets/fix_nc_gt/css/fix_nc_gt.css"
# web_include_js = "/assets/fix_nc_gt/js/fix_nc_gt.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "fix_nc_gt/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "fix_nc_gt/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "fix_nc_gt.utils.jinja_methods",
# 	"filters": "fix_nc_gt.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "fix_nc_gt.install.before_install"
# after_install = "fix_nc_gt.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "fix_nc_gt.uninstall.before_uninstall"
# after_uninstall = "fix_nc_gt.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "fix_nc_gt.utils.before_app_install"
# after_app_install = "fix_nc_gt.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "fix_nc_gt.utils.before_app_uninstall"
# after_app_uninstall = "fix_nc_gt.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "fix_nc_gt.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events
doc_events = {
    "Sales Invoice": {
        "on_submit": ["fix_nc_gt.api.pos_calculations"],
		"on_cancel": ["fix_nc_gt.api.pos_calculations"]
    }
# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"fix_nc_gt.tasks.all"
# 	],
# 	"daily": [
# 		"fix_nc_gt.tasks.daily"
# 	],
# 	"hourly": [
# 		"fix_nc_gt.tasks.hourly"
# 	],
# 	"weekly": [
# 		"fix_nc_gt.tasks.weekly"
# 	],
# 	"monthly": [
# 		"fix_nc_gt.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "fix_nc_gt.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "fix_nc_gt.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "fix_nc_gt.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["fix_nc_gt.utils.before_request"]
# after_request = ["fix_nc_gt.utils.after_request"]

# Job Events
# ----------
# before_job = ["fix_nc_gt.utils.before_job"]
# after_job = ["fix_nc_gt.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"fix_nc_gt.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

