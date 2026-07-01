__all__ = ['default_values', 'param_sliders', 'icons', 'content_paths']

# Define Default Values
default_values = {
	"min_passwd_len": 8,
	"max_passwd_len": 128,
	"safe_passwd_len": 64,
	"disable_reset_btn": True,
}

# Define Parameter Slider values
param_sliders = {
	"slider_upper_chars": {
		"min_val": 1,
		"max_val": 16,
	},
	"slider_lower_chars": {
		"min_val": 1,
		"max_val": 16,
	},
	"slider_spcl_chars": {
		"min_val": 1,
		"max_val": 16,
	},
	"slider_digits": {
		"min_val": 1,
		"max_val": 16,
	},
}

# Icons for randomiser buttons
# UI Icons
icons = {
	"warning": ":material/warning:",
	"password": ":material/password:",
	"privacy_tip": ":material/privacy_tip",
	"content_copy": ":material/content_copy",
	"reset_settings": ":material/reset_settings",
	"randomiser_icons": [":material/casino:", ":material/ifl:"],
}

# Content Paths
content_paths = {
	"create_passwd": "content/CreatingSecurePassword.md",
	"maintain_passwd": "content/MaintainingPasswordSecurity.md",
}

# App Author Details
author_details = {
	"name": "Sonal Karmakar",
	"email": "",
	"links": {
		"websites": {
			"GitHub": "https://github.com/sonalkarmakar",
			"GitLab": "https://gitlab.com/sonalkarmakar",
		},
		"repository": {
			"GitHub": "https://github.com/sonalkarmakar/<repository-name>",
			"GitLab": "https://gitlab.com/sonalkarmakar/<repository-name>",
		},
	},
}