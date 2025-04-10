---
---


window.onload = load();

function load() {
  // if params detected, set active view
  let params = getQueryParameters();
  if ("view" in params) {
    setView(params.view)
  }
  updateLinkTargets();
  enableTooltips();
}

window.onload = updateLinkTargets();





// update the url parameters (does not trigger page refresh)
function setQueryParameters(params=false) {
  // pass params as string; "x=i&y=j&z=k"
  params = params ? params : "";
  if (params != "") {
    params = "?" + params;
  }
  let viewSelection = document.querySelector('input[name="view"]:checked').value;
  let anchor = window.location.href.split("#")[1];
  if (anchor != undefined) {
    if (anchor.includes("year-") && viewSelection != "dateGroup") {
      anchor = "";
    }
    if (anchor.includes("entity-") && viewSelection != "entityGroup") {
      anchor = "";
    }
    if (anchor.includes("network-") && viewSelection != "networkGroup") {
      anchor = "";
    }
  }
  anchor = (anchor == "" || anchor == undefined) ? "" : `#${anchor}`;
  let url = `{{site.url}}/built-on-ethereum${params}${anchor}`;
  url = url.replace("localhost", "127.0.0.1");
  window.history.replaceState(null, "", url);
}
// gets the url parameters
function getQueryParameters() {
  try {
    let queryString = location.search.slice(1), params = {};
    queryString.replace(/([^=]*)=([^&]*)&*/g, (_, key, value) => {
      params[key] = value;
    });
    return params;
  } catch {
    return null;
  }
}
function setView(viewId) {
  try {
    viewSelected = document.querySelector(`#${viewId}`)
    viewSelected.checked = true;
    applyView(viewSelected);
  }
  catch {
    console.log(`view id does not exist: ${viewId}`);
  }
}
function applyView(view) {
  let dateGroup = document.getElementById("dateGroup");
  let entityGroup = document.getElementById("entityGroup");
  let networkGroup = document.getElementById("networkGroup");
  dateGroup.classList.add("d-none");
  entityGroup.classList.add("d-none");
  networkGroup.classList.add("d-none");
  document.querySelector(`#${view.value}`).classList.remove("d-none");
  setQueryParameters(`view=${view.id}`);
}







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
function enableTooltips() {
  let tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  let tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
  })
}

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





