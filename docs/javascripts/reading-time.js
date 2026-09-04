/* Estimated reading time, injected right under each page's h1.
 *
 * Chinese chars count ~400/min, English words ~200/min.
 * Works with Material's instant navigation via document$ subscription.
 */
(function () {
  function readingTime() {
    var content = document.querySelector(".md-content__inner");
    if (!content) return;
    if (content.querySelector(".reading-time")) return;

    var h1 = content.querySelector("h1");
    if (!h1) return;

    var text = content.textContent || "";
    var cjk = (text.match(/[\u4e00-\u9fff]/g) || []).length;
    var words = (text.replace(/[\u4e00-\u9fff]/g, " ").match(/[A-Za-z0-9_']+/g) || []).length;
    var minutes = Math.max(1, Math.round(cjk / 400 + words / 200));

    var isEn = window.location.pathname.indexOf("/en/") === 0;
    var label = isEn ? "~" + minutes + " min read" : "约 " + minutes + " 分钟读完";

    var span = document.createElement("span");
    span.className = "reading-time";
    span.textContent = label;
    h1.insertAdjacentElement("afterend", span);
  }

  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(readingTime);
  } else {
    document.addEventListener("DOMContentLoaded", readingTime);
  }
})();
