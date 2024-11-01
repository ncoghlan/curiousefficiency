
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time

##############################################
# Configuration, please edit
##############################################


# Data about this site
BLOG_AUTHOR = "Alyssa Coghlan"
BLOG_TITLE = "Curious Efficiency"
# This is the main URL for your site. It will be used
# in a prominent link
SITE_URL = "https://www.curiousefficiency.org"
# This is the URL where nikola's output will be deployed.
# If not set, defaults to SITE_URL
BASE_URL = SITE_URL + "/"
BLOG_EMAIL = "ncoghlan@gmail.com"
BLOG_DESCRIPTION = """\
Efficiency (a virtue) is the child of laziness and greed (both vices), while
much of our economic activity is devoted to preventing boredom in the idle
time created by increases in efficiency. To be human is to be a strange
creature indeed :)
"""

# Nikola is multilingual!
#
# Currently supported languages are:
#   English -> en
#   Greek -> gr
#   German -> de
#   French -> fr
#   Polish -> pl
#   Russian -> ru
#   Spanish -> es
#   Italian -> it
#   Simplified Chinese -> zh-cn
#
# If you want to use Nikola with a non-supported language you have to provide
# a module containing the necessary translations
# (p.e. look at the modules at: ./nikola/data/themes/default/messages/fr.py).
# If a specific post is not translated to a language, then the version
# in the default language will be shown instead.

# What is the default language?
DEFAULT_LANG = "en"

# What other languages do you have?
# The format is {"translationcode" : "path/to/translation" }
# the path will be used as a prefix for the generated pages location
TRANSLATIONS = {
    DEFAULT_LANG: "",
    # Example for another language:
    # "es": "./es",
}

# Links for the sidebar / navigation bar.
# You should provide a key-value pair for each used language.
NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ('/pages/about/', 'About'),
        ('/archive.html', 'Archives'),
        ('/categories/', 'Tags'),
        ('/rss.xml', 'RSS'),
        ('https://python-notes.curiousefficiency.org', 'Python Notes')
    ),
}
WRITE_TAG_CLOUD = True



##############################################
# Below this point, everything is optional
##############################################


# POSTS and PAGES contains (wildcard, destination, template) tuples.
#
# The wildcard is used to generate a list of reSt source files
# (whatever/thing.txt).
#
# That fragment could have an associated metadata file (whatever/thing.meta),
# and optionally translated files (example for spanish, with code "es"):
#     whatever/thing.txt.es and whatever/thing.meta.es
#
# From those files, a set of HTML fragment files will be generated:
# cache/whatever/thing.html (and maybe cache/whatever/thing.html.es)
#
# These files are combinated with the template to produce rendered
# pages, which will be placed at
# output / TRANSLATIONS[lang] / destination / pagename.html
#
# where "pagename" is the "slug" specified in the metadata file.
#
# The difference between POSTS and PAGES is that POSTS are added
# to feeds and are considered part of a blog, while PAGES are
# just independent HTML pages.
#

POSTS = (
    ("posts/*.txt", "posts", "post.tmpl"),
    ("posts/*.rst", "posts", "post.tmpl"),
    ("posts/*.md", "posts", "post.tmpl"),
    ("posts/*.html", "posts", "post.tmpl"),
)
PAGES = (
    ("pages/*.txt", "pages", "story.tmpl"),
    ("pages/*.rst", "pages", "story.tmpl"),
)
# One or more folders containing files to be copied as-is into the output.
# The format is a dictionary of "source" "relative destination".
# Default is:
# FILES_FOLDERS = {'files': '' }
# Which means copy 'files' into 'output'
FILES_FOLDERS = {'files': 'files' }

# A mapping of languages to file-extensions that represent that language.
# Feel free to add or delete extensions to any list, but don't add any new
# compilers unless you write the interface for it yourself.
#
# 'rest' is reStructuredText
# 'markdown' is MarkDown
# 'html' assumes the file is html and just copies it
COMPILERS = {
        "rest": ('.txt', '.rst'),
        "markdown": ('.md', '.mdown', '.markdown', '.wp'),
        "html": ('.html', '.htm')
        }

MARKDOWN_EXTENSIONS = [
    "fenced_code",
    "codehilite",
    "extra",
    "markdown.extensions.meta"
]
METADATA_FORMAT = "Pelican"

# Create by default posts in one file format?
# Set to False for two-file posts, with separate metadata.
# ONE_FILE_POSTS = True

# Use date-based path when creating posts?
# Can be enabled on a per-post basis with `nikola new_post -d`.
# The setting is ignored when creating pages.
NEW_POST_DATE_PATH = True

# What format to use when creating posts with date paths?
# Default is '%Y/%m/%d', other possibilities include '%Y' or '%Y/%m'.
NEW_POST_DATE_PATH_FORMAT = '%Y/%m'


# If this is set to True, then posts that are not translated to a language
# LANG will not be visible at all in the pages in that language.
# If set to False, the DEFAULT_LANG version will be displayed for
# untranslated posts.
# HIDE_UNTRANSLATED_POSTS = False

# Paths for different autogenerated bits. These are combined with the
# translation paths.

# Final locations are:
# output / TRANSLATION[lang] / TAG_PATH / index.html (list of tags)
# output / TRANSLATION[lang] / TAG_PATH / tag.html (list of posts for a tag)
# output / TRANSLATION[lang] / TAG_PATH / tag.xml (RSS feed for a tag)
# TAG_PATH = "categories"

# If TAG_PAGES_ARE_INDEXES is set to True, each tag's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# TAG_PAGES_ARE_INDEXES = True

# Final location is output / TRANSLATION[lang] / INDEX_PATH / index-*.html
# INDEX_PATH = ""

# Create per-month archives instead of per-year
# CREATE_MONTHLY_ARCHIVE = False
# Final locations for the archives are:
# output / TRANSLATION[lang] / ARCHIVE_PATH / ARCHIVE_FILENAME
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / index.html
# ARCHIVE_PATH = ""
# ARCHIVE_FILENAME = "archive.html"

# Final locations are:
# output / TRANSLATION[lang] / RSS_PATH / rss.xml
# RSS_PATH = ""

# Slug the Tag URL easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_TAG_PATH = True

# A list of redirection tuples, [("foo/from.html", "/bar/to.html")].
#
# A HTML file will be created in output/foo/from.html that redirects
# to the "/bar/to.html" URL. notice that the "from" side MUST be a
# relative URL.
#
# If you don't need any of these, just set to []
REDIRECTIONS = [
# Redirect old Boredom & Laziness paths
('2004/11/firing-it-up.html', '/posts/2004/11/firing-it-up/'),
('2004/11/mt-st-helens.html', '/posts/2004/11/mt-st-helens/'),
('2004/11/python-quirk.html', '/posts/2004/11/python-quirk/'),
('2004/12/brain-dead-software-1-yast-online.html', '/posts/2004/12/brain-dead-software-1-yast-online/'),
('2004/12/email-blogging.html', '/posts/2004/12/email-blogging/'),
('2004/12/google-footprint.html', '/posts/2004/12/google-footprint/'),
('2004/12/type-checking-in-python.html', '/posts/2004/12/type-checking-in-python/'),
('2005/02/because-james-doesnt-remember-it.html', '/posts/2005/02/because-james-doesnt-remember-it/'),
('2005/04/self-defeating-advertisements.html', '/posts/2005/04/self-defeating-advertisements/'),
('2005/07/grand-column.html', '/posts/2005/07/grand-column/'),
('2005/07/lance-hannah.html', '/posts/2005/07/lance-hannah/'),
('2006/04/ego-surfing.html', '/posts/2006/04/ego-surfing/'),
('2007/06/what-he-said.html', '/posts/2007/06/what-he-said/'),
('2010/01/justifying-python-language-changes.html', '/posts/2010/01/justifying-python-language-changes/'),
('2010/01/kubuntu-dev-packages-to-build-python.html', '/posts/2010/01/kubuntu-dev-packages-to-build-python/'),
('2010/01/status-quo-wins-stalemate.html', '/posts/2010/01/status-quo-wins-stalemate/'),
('2010/12/ethos.html', '/posts/2010/12/ethos/'),
('2010/12/joining-modern-era-of-blogging.html', '/posts/2010/12/joining-modern-era-of-blogging/'),
('2010/12/musings-on-lotr-movie-adaptations.html', '/posts/2010/12/musings-on-lotr-movie-adaptations/'),
('2011/01/comments-update-and-site-to-do-list.html', '/posts/2011/01/comments-update-and-site-to-do-list/'),
('2011/01/some-goals-for-python-33.html', '/posts/2011/01/some-goals-for-python-33/'),
('2011/01/which-matters-more-to-you-being-right.html', '/posts/2011/01/which-matters-more-to-you-being-right/'),
('2011/02/bye-bye-blogilo.html', '/posts/2011/02/bye-bye-blogilo/'),
('2011/02/justifying-python-language-changes.html', '/posts/2011/02/justifying-python-language-changes/'),
('2011/02/linking-sites-in-blog-posts.html', '/posts/2011/02/linking-sites-in-blog-posts/'),
('2011/02/posting-code-and-syntax-highlighting.html', '/posts/2011/02/posting-code-and-syntax-highlighting/'),
('2011/02/status-quo-wins-stalemate.html', '/posts/2011/02/status-quo-wins-stalemate/'),
('2011/02/to-pycon-and-beyond_8775.html', '/posts/2011/02/to-pycon-and-beyond_8775/'),
('2011/03/climate-change-skepticism-text-book.html', '/posts/2011/03/climate-change-skepticism-text-book/'),
('2011/03/python-language-summit-highlights.html', '/posts/2011/03/python-language-summit-highlights/'),
('2011/03/python-language-summit-rough-notes.html', '/posts/2011/03/python-language-summit-rough-notes/'),
('2011/03/python-vm-summit-rough-notes.html', '/posts/2011/03/python-vm-summit-rough-notes/'),
('2011/03/python-vm-summit-somewhat-coherent.html', '/posts/2011/03/python-vm-summit-somewhat-coherent/'),
('2011/03/queenslands-unelected-leader-of.html', '/posts/2011/03/queenslands-unelected-leader-of/'),
('2011/03/thoughts-and-impressions-following.html', '/posts/2011/03/thoughts-and-impressions-following/'),
('2011/03/what-is-python-script.html', '/posts/2011/03/what-is-python-script/'),
('2011/04/benefits-and-limitations-of-pyc-only.html', '/posts/2011/04/benefits-and-limitations-of-pyc-only/'),
('2011/04/musings-on-culture-of-python-dev.html', '/posts/2011/04/musings-on-culture-of-python-dev/'),
('2011/06/fixing-grub2-update-issues-with-kubuntu.html', '/posts/2011/06/fixing-grub2-update-issues-with-kubuntu/'),
('2011/06/switching-to-android.html', '/posts/2011/06/switching-to-android/'),
('2011/06/updated-to-do-list-for-python-33.html', '/posts/2011/06/updated-to-do-list-for-python-33/'),
('2011/07/effective-communication-brain-hacking.html', '/posts/2011/07/effective-communication-brain-hacking/'),
('2011/07/sharing-vs-broadcasting.html', '/posts/2011/07/sharing-vs-broadcasting/'),
('2011/07/sure-its-surprising-but-whats.html', '/posts/2011/07/sure-its-surprising-but-whats/'),
('2011/08/of-python-and-road-maps-or-lack-thereof.html', '/posts/2011/08/of-python-and-road-maps-or-lack-thereof/'),
('2011/08/open-source-windows-and-teaching-python.html', '/posts/2011/08/open-source-windows-and-teaching-python/'),
('2011/08/scripting-languages-and-suitable.html', '/posts/2011/08/scripting-languages-and-suitable/'),
('2011/09/mirror-all-things.html', '/posts/2011/09/mirror-all-things/'),
('2011/09/spinning-up-pulpdist-project.html', '/posts/2011/09/spinning-up-pulpdist-project/'),
('2011/10/correcting-ignorance-learning-bit-about.html', '/posts/2011/10/correcting-ignorance-learning-bit-about/'),
('2011/12/help-improve-python-33-standard-library.html', '/posts/2011/12/help-improve-python-33-standard-library/'),
('2011/12/new-year-python-meme-december-2011.html', '/posts/2011/12/new-year-python-meme-december-2011/'),
('2012/01/using-sopa-protests-to-highlight.html', '/posts/2012/01/using-sopa-protests-to-highlight/'),
('2012/01/walkdir-03-released-for-more-python.html', '/posts/2012/01/walkdir-03-released-for-more-python/'),
('2012/05/contextlib2-04-now-with-exitstack.html', '/posts/2012/05/contextlib2-04-now-with-exitstack/'),
('2012/05/djangos-cbvs-are-not-mistake-but.html', '/posts/2012/05/djangos-cbvs-are-not-mistake-but/'),
('2012/05/embarrassment-of-riches.html', '/posts/2012/05/embarrassment-of-riches/'),
('2012/06/some-thoughts-on-else-clauses-in.html', '/posts/2012/06/some-thoughts-on-else-clauses-in/'),
('2012/07/the-title-of-this-blog.html', '/posts/2012/07/the-title-of-this-blog/'),
('2012/07/volunteer-supported-free-threaded-cross.html', '/posts/2012/07/volunteer-supported-free-threaded-cross/'),
('2012/10/pythons-future-global-perspective.html', '/posts/2012/10/pythons-future-global-perspective/'),
('2012/11/pycon-india-2012.html', '/posts/2012/11/pycon-india-2012/'),
('2013/02/a-sliding-scale-of-freedom.html', '/posts/2013/02/a-sliding-scale-of-freedom/'),
('2013/03/change-future-one-small-slice-of-pycon.html', '/posts/2013/03/change-future-one-small-slice-of-pycon/'),
('2013/03/python-language-summit-pycon-us-2013.html', '/posts/2013/03/python-language-summit-pycon-us-2013/'),
# Redirect original Curious Efficiency paths
('posts/200411firing-it-up.html', '/posts/2004/11/firing-it-up/'),
('posts/200411mt-st-helens.html', '/posts/2004/11/mt-st-helens/'),
('posts/200411python-quirk.html', '/posts/2004/11/python-quirk/'),
('posts/200412brain-dead-software-1-yast-online.html', '/posts/2004/12/brain-dead-software-1-yast-online/'),
('posts/200412email-blogging.html', '/posts/2004/12/email-blogging/'),
('posts/200412google-footprint.html', '/posts/2004/12/google-footprint/'),
('posts/200412type-checking-in-python.html', '/posts/2004/12/type-checking-in-python/'),
('posts/200502because-james-doesnt-remember-it.html', '/posts/2005/02/because-james-doesnt-remember-it/'),
('posts/200504self-defeating-advertisements.html', '/posts/2005/04/self-defeating-advertisements/'),
('posts/200507grand-column.html', '/posts/2005/07/grand-column/'),
('posts/200507lance-hannah.html', '/posts/2005/07/lance-hannah/'),
('posts/200604ego-surfing.html', '/posts/2006/04/ego-surfing/'),
('posts/200706what-he-said.html', '/posts/2007/06/what-he-said/'),
('posts/201001justifying-python-language-changes.html', '/posts/2010/01/justifying-python-language-changes/'),
('posts/201001kubuntu-dev-packages-to-build-python.html', '/posts/2010/01/kubuntu-dev-packages-to-build-python/'),
('posts/201001status-quo-wins-stalemate.html', '/posts/2010/01/status-quo-wins-stalemate/'),
('posts/201012ethos.html', '/posts/2010/12/ethos/'),
('posts/201012joining-modern-era-of-blogging.html', '/posts/2010/12/joining-modern-era-of-blogging/'),
('posts/201012musings-on-lotr-movie-adaptations.html', '/posts/2010/12/musings-on-lotr-movie-adaptations/'),
('posts/201101comments-update-and-site-to-do-list.html', '/posts/2011/01/comments-update-and-site-to-do-list/'),
('posts/201101some-goals-for-python-33.html', '/posts/2011/01/some-goals-for-python-33/'),
('posts/201101which-matters-more-to-you-being-right.html', '/posts/2011/01/which-matters-more-to-you-being-right/'),
('posts/201102bye-bye-blogilo.html', '/posts/2011/02/bye-bye-blogilo/'),
('posts/201102justifying-python-language-changes.html', '/posts/2011/02/justifying-python-language-changes/'),
('posts/201102linking-sites-in-blog-posts.html', '/posts/2011/02/linking-sites-in-blog-posts/'),
('posts/201102posting-code-and-syntax-highlighting.html', '/posts/2011/02/posting-code-and-syntax-highlighting/'),
('posts/201102status-quo-wins-stalemate.html', '/posts/2011/02/status-quo-wins-stalemate/'),
('posts/201102to-pycon-and-beyond_8775.html', '/posts/2011/02/to-pycon-and-beyond_8775/'),
('posts/201103climate-change-skepticism-text-book.html', '/posts/2011/03/climate-change-skepticism-text-book/'),
('posts/201103python-language-summit-highlights.html', '/posts/2011/03/python-language-summit-highlights/'),
('posts/201103python-language-summit-rough-notes.html', '/posts/2011/03/python-language-summit-rough-notes/'),
('posts/201103python-vm-summit-rough-notes.html', '/posts/2011/03/python-vm-summit-rough-notes/'),
('posts/201103python-vm-summit-somewhat-coherent.html', '/posts/2011/03/python-vm-summit-somewhat-coherent/'),
('posts/201103queenslands-unelected-leader-of.html', '/posts/2011/03/queenslands-unelected-leader-of/'),
('posts/201103thoughts-and-impressions-following.html', '/posts/2011/03/thoughts-and-impressions-following/'),
('posts/201103what-is-python-script.html', '/posts/2011/03/what-is-python-script/'),
('posts/201104benefits-and-limitations-of-pyc-only.html', '/posts/2011/04/benefits-and-limitations-of-pyc-only/'),
('posts/201104musings-on-culture-of-python-dev.html', '/posts/2011/04/musings-on-culture-of-python-dev/'),
('posts/201106fixing-grub2-update-issues-with-kubuntu.html', '/posts/2011/06/fixing-grub2-update-issues-with-kubuntu/'),
('posts/201106switching-to-android.html', '/posts/2011/06/switching-to-android/'),
('posts/201106updated-to-do-list-for-python-33.html', '/posts/2011/06/updated-to-do-list-for-python-33/'),
('posts/201107effective-communication-brain-hacking.html', '/posts/2011/07/effective-communication-brain-hacking/'),
('posts/201107sharing-vs-broadcasting.html', '/posts/2011/07/sharing-vs-broadcasting/'),
('posts/201107sure-its-surprising-but-whats.html', '/posts/2011/07/sure-its-surprising-but-whats/'),
('posts/201108of-python-and-road-maps-or-lack-thereof.html', '/posts/2011/08/of-python-and-road-maps-or-lack-thereof/'),
('posts/201108open-source-windows-and-teaching-python.html', '/posts/2011/08/open-source-windows-and-teaching-python/'),
('posts/201108scripting-languages-and-suitable.html', '/posts/2011/08/scripting-languages-and-suitable/'),
('posts/201109mirror-all-things.html', '/posts/2011/09/mirror-all-things/'),
('posts/201109spinning-up-pulpdist-project.html', '/posts/2011/09/spinning-up-pulpdist-project/'),
('posts/201110correcting-ignorance-learning-bit-about.html', '/posts/2011/10/correcting-ignorance-learning-bit-about/'),
('posts/201112help-improve-python-33-standard-library.html', '/posts/2011/12/help-improve-python-33-standard-library/'),
('posts/201112new-year-python-meme-december-2011.html', '/posts/2011/12/new-year-python-meme-december-2011/'),
('posts/201201using-sopa-protests-to-highlight.html', '/posts/2012/01/using-sopa-protests-to-highlight/'),
('posts/201201walkdir-03-released-for-more-python.html', '/posts/2012/01/walkdir-03-released-for-more-python/'),
('posts/201205contextlib2-04-now-with-exitstack.html', '/posts/2012/05/contextlib2-04-now-with-exitstack/'),
('posts/201205djangos-cbvs-are-not-mistake-but.html', '/posts/2012/05/djangos-cbvs-are-not-mistake-but/'),
('posts/201205embarrassment-of-riches.html', '/posts/2012/05/embarrassment-of-riches/'),
('posts/201206some-thoughts-on-else-clauses-in.html', '/posts/2012/06/some-thoughts-on-else-clauses-in/'),
('posts/201207the-title-of-this-blog.html', '/posts/2012/07/the-title-of-this-blog/'),
('posts/201207volunteer-supported-free-threaded-cross.html', '/posts/2012/07/volunteer-supported-free-threaded-cross/'),
('posts/201210pythons-future-global-perspective.html', '/posts/2012/10/pythons-future-global-perspective/'),
('posts/201211pycon-india-2012.html', '/posts/2012/11/pycon-india-2012/'),
('posts/201302a-sliding-scale-of-freedom.html', '/posts/2013/02/a-sliding-scale-of-freedom/'),
('posts/201303change-future-one-small-slice-of-pycon.html', '/posts/2013/03/change-future-one-small-slice-of-pycon/'),
('posts/201303python-language-summit-pycon-us-2013.html', '/posts/2013/03/python-language-summit-pycon-us-2013/'),
# Adjust for Nikola layout change to use folder-per-post rather than file-per-post
# $ find posts -mindepth 2 -name '*.html' '!' -name 'index*' -printf "('%p', '/%p/'),\n" | sed 's,.html/,/,' | sort
('posts/2004/11/firing-it-up.html', '/posts/2004/11/firing-it-up/'),
('posts/2004/11/mt-st-helens.html', '/posts/2004/11/mt-st-helens/'),
('posts/2004/11/python-quirk.html', '/posts/2004/11/python-quirk/'),
('posts/2004/12/brain-dead-software-1-yast-online.html', '/posts/2004/12/brain-dead-software-1-yast-online/'),
('posts/2004/12/email-blogging.html', '/posts/2004/12/email-blogging/'),
('posts/2004/12/google-footprint.html', '/posts/2004/12/google-footprint/'),
('posts/2004/12/type-checking-in-python.html', '/posts/2004/12/type-checking-in-python/'),
('posts/2005/02/because-james-doesnt-remember-it.html', '/posts/2005/02/because-james-doesnt-remember-it/'),
('posts/2005/04/self-defeating-advertisements.html', '/posts/2005/04/self-defeating-advertisements/'),
('posts/2005/07/grand-column.html', '/posts/2005/07/grand-column/'),
('posts/2005/07/lance-hannah.html', '/posts/2005/07/lance-hannah/'),
('posts/2006/04/ego-surfing.html', '/posts/2006/04/ego-surfing/'),
('posts/2007/06/what-he-said.html', '/posts/2007/06/what-he-said/'),
('posts/2010/01/justifying-python-language-changes.html', '/posts/2010/01/justifying-python-language-changes/'),
('posts/2010/01/kubuntu-dev-packages-to-build-python.html', '/posts/2010/01/kubuntu-dev-packages-to-build-python/'),
('posts/2010/01/status-quo-wins-stalemate.html', '/posts/2010/01/status-quo-wins-stalemate/'),
('posts/2010/12/ethos.html', '/posts/2010/12/ethos/'),
('posts/2010/12/joining-modern-era-of-blogging.html', '/posts/2010/12/joining-modern-era-of-blogging/'),
('posts/2010/12/musings-on-lotr-movie-adaptations.html', '/posts/2010/12/musings-on-lotr-movie-adaptations/'),
('posts/2011/01/comments-update-and-site-to-do-list.html', '/posts/2011/01/comments-update-and-site-to-do-list/'),
('posts/2011/01/some-goals-for-python-33.html', '/posts/2011/01/some-goals-for-python-33/'),
('posts/2011/01/which-matters-more-to-you-being-right.html', '/posts/2011/01/which-matters-more-to-you-being-right/'),
('posts/2011/02/bye-bye-blogilo.html', '/posts/2011/02/bye-bye-blogilo/'),
('posts/2011/02/justifying-python-language-changes.html', '/posts/2011/02/justifying-python-language-changes/'),
('posts/2011/02/linking-sites-in-blog-posts.html', '/posts/2011/02/linking-sites-in-blog-posts/'),
('posts/2011/02/posting-code-and-syntax-highlighting.html', '/posts/2011/02/posting-code-and-syntax-highlighting/'),
('posts/2011/02/status-quo-wins-stalemate.html', '/posts/2011/02/status-quo-wins-stalemate/'),
('posts/2011/02/to-pycon-and-beyond_8775.html', '/posts/2011/02/to-pycon-and-beyond_8775/'),
('posts/2011/03/climate-change-skepticism-text-book.html', '/posts/2011/03/climate-change-skepticism-text-book/'),
('posts/2011/03/python-language-summit-highlights.html', '/posts/2011/03/python-language-summit-highlights/'),
('posts/2011/03/python-language-summit-rough-notes.html', '/posts/2011/03/python-language-summit-rough-notes/'),
('posts/2011/03/python-vm-summit-rough-notes.html', '/posts/2011/03/python-vm-summit-rough-notes/'),
('posts/2011/03/python-vm-summit-somewhat-coherent.html', '/posts/2011/03/python-vm-summit-somewhat-coherent/'),
('posts/2011/03/queenslands-unelected-leader-of.html', '/posts/2011/03/queenslands-unelected-leader-of/'),
('posts/2011/03/thoughts-and-impressions-following.html', '/posts/2011/03/thoughts-and-impressions-following/'),
('posts/2011/03/what-is-python-script.html', '/posts/2011/03/what-is-python-script/'),
('posts/2011/04/benefits-and-limitations-of-pyc-only.html', '/posts/2011/04/benefits-and-limitations-of-pyc-only/'),
('posts/2011/04/musings-on-culture-of-python-dev.html', '/posts/2011/04/musings-on-culture-of-python-dev/'),
('posts/2011/06/fixing-grub2-update-issues-with-kubuntu.html', '/posts/2011/06/fixing-grub2-update-issues-with-kubuntu/'),
('posts/2011/06/switching-to-android.html', '/posts/2011/06/switching-to-android/'),
('posts/2011/06/updated-to-do-list-for-python-33.html', '/posts/2011/06/updated-to-do-list-for-python-33/'),
('posts/2011/07/effective-communication-brain-hacking.html', '/posts/2011/07/effective-communication-brain-hacking/'),
('posts/2011/07/sharing-vs-broadcasting.html', '/posts/2011/07/sharing-vs-broadcasting/'),
('posts/2011/07/sure-its-surprising-but-whats.html', '/posts/2011/07/sure-its-surprising-but-whats/'),
('posts/2011/08/of-python-and-road-maps-or-lack-thereof.html', '/posts/2011/08/of-python-and-road-maps-or-lack-thereof/'),
('posts/2011/08/open-source-windows-and-teaching-python.html', '/posts/2011/08/open-source-windows-and-teaching-python/'),
('posts/2011/08/scripting-languages-and-suitable.html', '/posts/2011/08/scripting-languages-and-suitable/'),
('posts/2011/09/mirror-all-things.html', '/posts/2011/09/mirror-all-things/'),
('posts/2011/09/spinning-up-pulpdist-project.html', '/posts/2011/09/spinning-up-pulpdist-project/'),
('posts/2011/10/correcting-ignorance-learning-bit-about.html', '/posts/2011/10/correcting-ignorance-learning-bit-about/'),
('posts/2011/12/help-improve-python-33-standard-library.html', '/posts/2011/12/help-improve-python-33-standard-library/'),
('posts/2011/12/new-year-python-meme-december-2011.html', '/posts/2011/12/new-year-python-meme-december-2011/'),
('posts/2012/01/using-sopa-protests-to-highlight.html', '/posts/2012/01/using-sopa-protests-to-highlight/'),
('posts/2012/01/walkdir-03-released-for-more-python.html', '/posts/2012/01/walkdir-03-released-for-more-python/'),
('posts/2012/05/contextlib2-04-now-with-exitstack.html', '/posts/2012/05/contextlib2-04-now-with-exitstack/'),
('posts/2012/05/djangos-cbvs-are-not-mistake-but.html', '/posts/2012/05/djangos-cbvs-are-not-mistake-but/'),
('posts/2012/05/embarrassment-of-riches.html', '/posts/2012/05/embarrassment-of-riches/'),
('posts/2012/06/some-thoughts-on-else-clauses-in.html', '/posts/2012/06/some-thoughts-on-else-clauses-in/'),
('posts/2012/07/the-title-of-this-blog.html', '/posts/2012/07/the-title-of-this-blog/'),
('posts/2012/07/volunteer-supported-free-threaded-cross.html', '/posts/2012/07/volunteer-supported-free-threaded-cross/'),
('posts/2012/10/pythons-future-global-perspective.html', '/posts/2012/10/pythons-future-global-perspective/'),
('posts/2012/11/pycon-india-2012.html', '/posts/2012/11/pycon-india-2012/'),
('posts/2013/02/a-sliding-scale-of-freedom.html', '/posts/2013/02/a-sliding-scale-of-freedom/'),
('posts/2013/03/change-future-one-small-slice-of-pycon.html', '/posts/2013/03/change-future-one-small-slice-of-pycon/'),
('posts/2013/03/python-language-summit-pycon-us-2013.html', '/posts/2013/03/python-language-summit-pycon-us-2013/'),
('posts/2014/03/on-wielding-power.html', '/posts/2014/03/on-wielding-power/'),
('posts/2014/08/multilingual-programming.html', '/posts/2014/08/multilingual-programming/'),
('posts/2014/08/python-4000.html', '/posts/2014/08/python-4000/'),
('posts/2014/08/python-teaching-suggestions.html', '/posts/2014/08/python-teaching-suggestions/'),
('posts/2014/09/seven-billion-seconds-per-second.html', '/posts/2014/09/seven-billion-seconds-per-second/'),
('posts/2014/12/kallithea-on-openshift.html', '/posts/2014/12/kallithea-on-openshift/'),
('posts/2015/01/abuse-is-not-ok.html', '/posts/2015/01/abuse-is-not-ok/'),
('posts/2015/01/dtca-public-consultation.html', '/posts/2015/01/dtca-public-consultation/'),
('posts/2015/04/fedora-encrypted-volumes.html', '/posts/2015/04/fedora-encrypted-volumes/'),
('posts/2015/04/pycon-australia-education-miniconf.html', '/posts/2015/04/pycon-australia-education-miniconf/'),
('posts/2015/04/stop-supporting-python26.html', '/posts/2015/04/stop-supporting-python26/'),
('posts/2015/07/asyncio-background-calls.html', '/posts/2015/07/asyncio-background-calls/'),
('posts/2015/07/asyncio-tcp-echo-server.html', '/posts/2015/07/asyncio-tcp-echo-server/'),
('posts/2015/10/27-languages-to-improve-your-python.html', '/posts/2015/10/27-languages-to-improve-your-python/'),
('posts/2015/10/languages-to-improve-your-python.html', '/posts/2015/10/languages-to-improve-your-python/'),
('posts/2016/05/pycon-australia-education-cfp-2016.html', '/posts/2016/05/pycon-australia-education-cfp-2016/'),
('posts/2016/08/what-problem-does-it-solve.html', '/posts/2016/08/what-problem-does-it-solve/'),
('posts/2016/09/python-packaging-ecosystem.html', '/posts/2016/09/python-packaging-ecosystem/'),
('posts/2017/10/considering-pythons-target-audience.html', '/posts/2017/10/considering-pythons-target-audience/'),
('posts/2017/10/software-adoption-cycles.html', '/posts/2017/10/software-adoption-cycles/'),
('posts/2019/03/what-does-x-equals-a-plus-b-mean.html', '/posts/2019/03/what-does-x-equals-a-plus-b-mean/'),
# Fix up old navigation links
('/pages/about.html', '/pages/about/'),
('/categories.html', '/categories/'),
]

# Commands to execute to deploy. Can be anything, for example,
# you may use rsync:
# "rsync -rav output/* joe@my.site:/srv/www/site"
# And then do a backup, or ping pingomatic.
# To do manual deployment, set it to []
DEPLOY_COMMANDS = {
    u'default': [u'rsync -rav output/* ~/devel/ncoghlan.github.io'],
    u'publish': [
        u"""pushd ~/devel/ncoghlan.github.io &&
            git add . &&
            git commit -m "Deployment from local site build" &&
            git push &&
            popd
        """,
    ],
    u'publish-ci': [
        u"""rsync -rav output/* ../deployed &&
            pushd ../deployed &&
            git add . &&
            git commit -m "Automatic deployment from CI" &&
            git push
            popd
        """,
    ],
}

# Where the output site should be located
# If you don't use an absolute path, it will be considered as relative
# to the location of conf.py
# OUTPUT_FOLDER = 'output'

# where the "cache" of partial generated content should be located
# default: 'cache'
# CACHE_FOLDER = 'cache'

# Filters to apply to the output.
# A directory where the keys are either: a file extensions, or
# a tuple of file extensions.
#
# And the value is a list of commands to be applied in order.
#
# Each command must be either:
#
# A string containing a '%s' which will
# be replaced with a filename. The command *must* produce output
# in place.
#
# Or:
#
# A python callable, which will be called with the filename as
# argument.
#
# By default, there are no filters.
# FILTERS = {
#    ".jpg": ["jpegoptim --strip-all -m75 -v %s"],
# }

# Create a gzipped copy of each generated file. Cheap server-side optimization.
# GZIP_FILES = False
# File extensions that will be compressed
# GZIP_EXTENSIONS = ('.txt', '.htm', '.html', '.css', '.js', '.json')

# #############################################################################
# Image Gallery Options
# #############################################################################

# Galleries are folders in galleries/
# Final location of galleries will be output / GALLERY_PATH / gallery_name
# GALLERY_PATH = "galleries"
# THUMBNAIL_SIZE = 180
# MAX_IMAGE_SIZE = 1280
# USE_FILENAME_AS_TITLE = True

# #############################################################################
# HTML fragments and diverse things that are used by the templates
# #############################################################################

# Data about post-per-page indexes
# INDEXES_TITLE = ""  # If this is empty, the default is BLOG_TITLE
# INDEXES_PAGES = ""  # If this is empty, the default is 'old posts page %d' translated

# Name of the theme to use.
# THEME = 'bootstrap'

# Color scheme to be used for code blocks. If your theme provide "assets/css/code.css" this
# is ignored.
# Can be any of autumn borland bw colorful default emacs friendly fruity manni monokai
# murphy native pastie perldoc rrt tango trac vim vs
# CODE_COLOR_SCHEME = default

# If you use 'site-reveal' theme you can select several subthemes
# THEME_REVEAL_CONGIF_SUBTHEME = 'sky' # You can also use: beige/serif/simple/night/default

# Again, if you use 'site-reveal' theme you can select several transitions between the slides
# THEME_REVEAL_CONGIF_TRANSITION = 'cube' # You can also use: page/concave/linear/none/default

# date format used to display post dates. (str used by datetime.datetime.strftime)
# DATE_FORMAT = '%Y-%m-%d %H:%M'

# FAVICONS contains (name, file, size) tuples.
# Used for create favicon link like this:
# <link rel="name" href="file" sizes="size"/>
# about favicons, see: http://www.netmagazine.com/features/create-perfect-favicon
# FAVICONS = {
#     ("icon", "/favicon.ico", "16x16"),
#     ("icon", "/icon_128x128.png", "128x128"),
# }

# Show only teasers in the index pages? Defaults to False.
# INDEX_TEASERS = False

# A HTML fragment describing the license, for the sidebar. Default is "".
# I recommend using the Creative Commons' wizard:
# http://creativecommons.org/choose/
# LICENSE = """
# <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/2.5/ar/">
# <img alt="Creative Commons License BY-NC-SA"
# style="border-width:0; margin-bottom:12px;"
# src="http://i.creativecommons.org/l/by-nc-sa/2.5/ar/88x31.png"></a>"""

# A small copyright notice for the page footer (in HTML).
# Default is ''
COPYRIGHT_NOTICE = 'Contents &copy; {date} <a href="mailto:{email}">{author}</a>'
COPYRIGHT_NOTICE = COPYRIGHT_NOTICE.format(email=BLOG_EMAIL,
                                           author=BLOG_AUTHOR,
                                           date=time.gmtime().tm_year)
CC0_LICENSE = '<a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0</a>, republish as you wish.'
POWERED_BY_NIKOLA = 'Powered by <a href="https://getnikola.com/">Nikola</a>'
CONTENT_FOOTER = '{} - {} - {}'.format(COPYRIGHT_NOTICE,
                                       CC0_LICENSE,
                                       POWERED_BY_NIKOLA)

# To enable comments via Disqus, you need to create a forum at
# http://disqus.com, and set DISQUS_FORUM to the short name you selected.
# If you want to disable comments, set it to False.
# Default is "nikolademo", used by the demo sites
COMMENT_SYSTEM_ID = "boredomandlaziness"

# Create index.html for story folders?
# STORY_INDEX = False
# Enable comments on story pages?
# COMMENTS_IN_STORIES = False
# Enable comments on picture gallery pages?
# COMMENTS_IN_GALLERIES = False

# If a link ends in /index.html, drop the index.html part.
# http://mysite/foo/bar/index.html => http://mysite/foo/bar/
# Default = False
# STRIP_INDEX_HTML = False

# Do you want a add a Mathjax config file?
# MATHJAX_CONFIG = ""

# If you are using the compile-ipynb plugin, just add this one:
#MATHJAX_CONFIG = """
#<script type="text/x-mathjax-config">
#MathJax.Hub.Config({
#    tex2jax: {
#        inlineMath: [ ['$','$'], ["\\\(","\\\)"] ],
#        displayMath: [ ['$$','$$'], ["\\\[","\\\]"] ]
#    },
#    displayAlign: 'left', // Change this to 'center' to center equations.
#    "HTML-CSS": {
#        styles: {'.MathJax_Display': {"margin": 0}}
#    }
#});
#</script>
#"""

# Enable social buttons?
# Defaults to true
SOCIAL_BUTTONS_CODE = ""

# Modify the number of Post per Index Page
# Defaults to 10
# INDEX_DISPLAY_POST_COUNT = 10

# RSS_LINK is a HTML fragment to link the RSS or Atom feeds. If set to None,
# the base.tmpl will use the feed Nikola generates. However, you may want to
# change it for a feedburner feed or something else.
# RSS_LINK = None

# Show only teasers in the RSS feed? Default to True
FEED_TEASERS = False


# A search form to search this site, for the sidebar. You can use a google
# custom search (http://www.google.com/cse/)
# Or a duckduckgo search: https://duckduckgo.com/search_box.html
# Default is no search form.
# SEARCH_FORM = ""
#
# This search form works for any site and looks good in the "site" theme where it
# appears on the navigation bar
#SEARCH_FORM = """
#<!-- Custom search -->
#<form method="get" id="search" action="http://duckduckgo.com/"
# class="navbar-form pull-left">
#<input type="hidden" name="sites" value="%s"/>
#<input type="hidden" name="k8" value="#444444"/>
#<input type="hidden" name="k9" value="#D51920"/>
#<input type="hidden" name="kt" value="h"/>
#<input type="text" name="q" maxlength="255"
# placeholder="Search&hellip;" class="span2" style="margin-top: 4px;"/>
#<input type="submit" value="DuckDuckGo Search" style="visibility: hidden;" />
#</form>
#<!-- End of custom search -->
#""" % BLOG_URL
#
# Also, there is a local search plugin you can use.

# Use content distribution networks for jquery and twitter-bootstrap css and js
# If this is True, jquery is served from the Google CDN and twitter-bootstrap
# is served from the NetDNA CDN
# Set this to False if you want to host your site without requiring access to
# external resources.
# USE_CDN = False

# Extra things you want in the pages HEAD tag. This will be added right
# before </HEAD>
# EXTRA_HEAD_DATA = ""
# Google analytics or whatever else you use. Added to the bottom of <body>
# in the default template (base.tmpl).
# ANALYTICS = ""

# The possibility to extract metadata from the filename by using a
# regular expression.
# To make it work you need to name parts of your regular expression.
# The following names will be used to extract metadata:
# - title
# - slug
# - date
# - tags
# - link
# - description
#
# An example re is the following:
# '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)-(?P<title>.*)\.md'
# FILE_METADATA_REGEXP = None

# Nikola supports Twitter Card summaries / Open Graph.
# Twitter cards make it possible for you to attach media to Tweets
# that link to your content.
#
# IMPORTANT:
# Please note, that you need to opt-in for using Twitter Cards!
# To do this please visit https://dev.twitter.com/form/participate-twitter-cards
#
# Uncomment and modify to following lines to match your accounts.
# Specifying the id for either 'site' or 'creator' will be preferred
# over the cleartext username. Specifying an ID is not necessary.
# Displaying images is currently not supported.
# TWITTER_CARD = {
#     # 'use_twitter_cards': True,  # enable Twitter Cards / Open Graph
#     # 'site': '@website',  # twitter nick for the website
#     # 'site:id': 123456,  # Same as site, but the website's Twitter user ID instead.
#     # 'creator': '@username',  # Username for the content creator / author.
#     # 'creator:id': 654321,  # Same as creator, but the Twitter user's ID.
# }


# If you want to use formatted post time in W3C-DTF Format(ex. 2012-03-30T23:00:00+02:00),
# set timzone if you want a localized posted date.
#
# TIMEZONE = 'Europe/Zurich'

# If webassets is installed, bundle JS and CSS to make site loading faster
# USE_BUNDLES = True

# Plugins you don't want to use. Be careful :-)
# DISABLED_PLUGINS = ["robots"]

# Experimental plugins - use at your own risk.
# They probably need some manual adjustments - please see their respective readme.
# ENABLED_EXTRAS = [
#     'planetoid',
#     'ipynb',
#     'localsearch',
#     'mustache',
# ]

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.

GLOBAL_CONTEXT : dict[str, object] = {}
