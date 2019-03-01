# https://github.com/thomasnilsson/github_markdown
# Thank you very much for this nice piece of code!
import github_markdown as gm

i = 'README_no_latex.md'
o = 'README.md'

gm.markdown_texify(i,o)