/* Keep giscus in sync with Material's light/dark palette.
 *
 * Material renders data-md-color-scheme="default|slate" on <body> and updates
 * it when the sun/moon toggle is used — giscus cannot see that, so it would
 * otherwise keep following the OS preference and clash with the page. We post
 * a setConfig message to its iframe to make it follow the site instead.
 */
(function () {
  'use strict';

  function theme() {
    return document.body.getAttribute('data-md-color-scheme') === 'slate'
      ? 'dark'
      : 'light';
  }

  function apply() {
    var frame = document.querySelector('iframe.giscus-frame');
    if (!frame) return;
    frame.contentWindow.postMessage(
      { giscus: { setConfig: { theme: theme() } } },
      'https://giscus.app'
    );
  }

  // giscus announces itself once its iframe is ready — sync as soon as it does.
  window.addEventListener('message', function (e) {
    if (e.origin !== 'https://giscus.app' || !e.data || !e.data.giscus) return;
    apply();
  });

  new MutationObserver(apply).observe(document.body, {
    attributes: true,
    attributeFilter: ['data-md-color-scheme']
  });
})();
