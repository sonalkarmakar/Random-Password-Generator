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
		"rndmz_btn_key": "rndmz_btn_uppercase",
		"rndmz_btn_tip": "Randomise number of uppercase characters.",
		"label": "Number of Uppercase characters [`A`, `B`, `C`, ... `Z`]",
	},
	"slider_lower_chars": {
		"min_val": 1,
		"max_val": 16,
		"rndmz_btn_key": "rndmz_btn_lowercase",
		"rndmz_btn_tip": "Randomise number of lowercase characters.",
		"label": "Number of Lowercase characters [`a`, `b`, `c`, ... `z`]",
	},
	"slider_spcl_chars": {
		"min_val": 1,
		"max_val": 16,
		"rndmz_btn_key": "rndmz_btn_special",
		"rndmz_btn_tip": "Randomise number of special characters.",
		"label": "Number of Special characters [`,`, `!`, `_`, etc.]",
	},
	"slider_digits": {
		"min_val": 1,
		"max_val": 16,
		"rndmz_btn_key": "rndmz_btn_digits",
		"rndmz_btn_tip": "Randomise number of digits.",
		"label": "Number of Digits [`0`, `1`, `2`, ... `9`]",
	},
}

# Icons for randomiser buttons
# UI Icons
icons = {
	"warning": "warning",
	"password": "password",
	"privacy_tip": "privacy_tip",
	"content_copy": "content_copy",
	"reset_settings": "reset_settings",
	"randomiser_icons": ["casino", "ifl"],
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
			"GitHub": "https://github.com/sonalkarmakar/Random-Password-Generator",
			"GitLab": "https://gitlab.com/sonalkarmakar/Random-Password-Generator",
		},
	},
}