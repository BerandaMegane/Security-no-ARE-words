# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "セキュリティのアレまとめ"
copyright = "2023, BerandaMegane"
author = "BerandaMegane"

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = "%Y-%m-%dT%H:%M%z"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.githubpages",
    "sphinx_sitemap",
    "sphinxext.opengraph",
]

templates_path = ['_templates']
exclude_patterns = ['Thumbs.db']

language = 'ja'

# sphinx_sitemap 向け設定
html_baseurl = "https://are.bocchi-megane.dev/"
sitemap_locales = [None]
sitemap_url_scheme = "{link}"

# sphinxext.opengraph 向け設定
ogp_site_url = html_baseurl
ogp_image = "http://are.bocchi-megane.dev/ogp_image.png"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "セキュリティのアレまとめ"
html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_favicon = "_static/favicon.ico"
html_logo = "_static/html_logo.png"

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
    "CNAME",
]
