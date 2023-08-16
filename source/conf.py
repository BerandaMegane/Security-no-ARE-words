# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'セキュリティのアレまとめ'
copyright = '2023, BerandaMegane'
author = 'BerandaMegane'

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = "%Y-%m-%dT%H:%M%z"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.githubpages",
    "sphinx_sitemap"
]

templates_path = ['_templates']
exclude_patterns = ['Thumbs.db']

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_baseurl = "https://are.bocchi-megane.dev/"
html_title = "セキュリティのアレまとめ"
html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_favicon = "_static/favicon.ico"
html_logo = "_static/アイコン.png"

# ページヘッダー・フッター設定
html_theme_options = {
    "logo": {
        "text": project,
    },
    "github_url": "https://github.com/BerandaMegane/Security-no-ARE-words",
    "twitter_url": "https://twitter.com/BerandaMegane",
    "external_links": [
        {"name": "お問合せ", "url": "https://forms.gle/7adWctvUpwrNvZxD6"},
    ],
  "footer_start": ["copyright", "last-updated", "sphinx-version"],
}

# 出力先ディレクトリにコピーする追加ファイル
html_extra_path = [
    "CNAME"
]
