// MathJax loader — deferred so it also re-typesets content rendered by
// instant navigation (Material's "navigation.instant" style page swaps).
(function () {
  function load() {
    if (window.mathjaxLoaderDone) return;
    window.mathjaxLoaderDone = true;
    var script = document.createElement("script");
    script.src = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg-full.js";
    script.async = true;
    document.head.appendChild(script);
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", load);
  } else {
    load();
  }
})();
