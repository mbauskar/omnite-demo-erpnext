from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		"Accounts": {
			"color": "#333333",
			"icon": "octicon octicon-repo",
			"type": "module"
		},
		"Buying": {
			"color": "#333333",
			"icon": "icon-shopping-cart",
			"icon": "octicon octicon-briefcase",
			"type": "module"
		},
		"HR": {
			"color": "#333333",
			"icon": "icon-group",
			"icon": "octicon octicon-organization",
			"label": _("Human Resources"),
			"type": "module"
		},
		"Manufacturing": {
			"color": "#333333",
			"icon": "icon-cogs",
			"icon": "octicon octicon-tools",
			"type": "module"
		},
		"POS": {
			"color": "#333333",
			"icon": "icon-th",
			"icon": "octicon octicon-credit-card",
			"type": "page",
			"link": "pos"
		},
		"Projects": {
			"color": "#333333",
			"icon": "icon-puzzle-piece",
			"icon": "octicon octicon-rocket",
			"type": "module"
		},
		"Selling": {
			"color": "#333333",
			"icon": "icon-tag",
			"icon": "octicon octicon-tag",
			"type": "module"
		},
		"CRM": {
			"color": "#333333",
			"icon": "octicon octicon-broadcast",
			"type": "module"
		},
		"Stock": {
			"color": "#333333",
			"icon": "icon-truck",
			"icon": "octicon octicon-package",
			"type": "module"
		},
		"Support": {
			"color": "#333333",
			"icon": "icon-phone",
			"icon": "octicon octicon-issue-opened",
			"type": "module"
		},
		"Learn": {
			"color": "#333333",
			"force_show": True,
			"icon": "icon-facetime-video",
			"type": "module",
			"is_help": True
		}
	}
