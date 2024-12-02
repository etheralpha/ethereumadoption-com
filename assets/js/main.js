---
---

window.onload = updateLinkTargets();


// open external links and pdfs in new tab
function updateLinkTargets() {
  {%- assign site_url = site.url | split: "//" | last -%}
  document.querySelectorAll("a").forEach(link => {
    let href = link.href;
    // set all links to open in new tab
    if (/^(https?:)?\/\//.test(link.href)) {
      link.target = "_blank";
    }
    // if current domain, use same tab
    if (href != undefined && href.includes("{{site_url}}")) {
      link.target = "_self";
    }
    // if relative links, use new tab
    if (href != undefined && !href.includes("https")) {
      link.target = "_self";
    }
    // open all .pdf, .png, .jpg, .mp4 in new tab
    if (/(\.pdf$|\.png$|\.jpe*g$|\.mp4)/.test(href)) {
      link.target = "_blank";
    }
    // if new-tab class, use new tab
    if (link.classList.contains("new-tab")) {
      link.target = "_blank";
    }
  })
}

// enable tooltips
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

// copy link and show tooltip confirmation
function copyText(text, id) {
  navigator.clipboard.writeText(text).then(function() {
    let tooltipElement = document.getElementById(id);
    let tooltip = bootstrap.Tooltip.getInstance(tooltipElement);
    tooltip.show();
    setTimeout(() => { tooltip.hide(); }, 1000);
  }, function(err) {
    console.error('Could not copy text: ', err);
  });
}





