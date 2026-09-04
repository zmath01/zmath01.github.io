# MathJax configuration — must load BEFORE mathjax-loader.js.
# Works with pymdownx.arithmatex generic mode: $...$ / $$...$$ / \(...\) / \[...\]
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
    tags: "none",
  },
  options: {
    ignoreHtmlClass: ".*|tex2jax_ignore",
    processHtmlClass: "tex2jax_include",
  },
};
