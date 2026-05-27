
(() => {
  const input = document.getElementById("search");
  const results = document.getElementById("search-results");
  if (!input || !results) return;
  const root = document.querySelector("script[src$='site.js']").getAttribute("src").replace(/assets\/site\.js$/, "");
  let index = [];
  fetch(root + "assets/search.json").then(r => r.json()).then(data => { index = data; });
  input.addEventListener("input", () => {
    const q = input.value.trim().toLowerCase();
    if (!q) {
      results.style.display = "none";
      results.innerHTML = "";
      return;
    }
    const hits = index
      .map(page => {
        const haystack = `${page.title} ${page.type} ${page.tags.join(" ")} ${page.excerpt}`.toLowerCase();
        return { page, score: haystack.includes(q) ? (page.title.toLowerCase().includes(q) ? 2 : 1) : 0 };
      })
      .filter(hit => hit.score)
      .sort((a, b) => b.score - a.score || a.page.title.localeCompare(b.page.title))
      .slice(0, 12);
    results.innerHTML = hits.map(({ page }) => `<a href="${root}${page.url}">${page.title}<small>${page.type}</small></a>`).join("");
    results.style.display = hits.length ? "block" : "none";
  });
  document.addEventListener("click", event => {
    if (!results.contains(event.target) && event.target !== input) results.style.display = "none";
  });
})();
