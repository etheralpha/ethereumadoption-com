---
layout: default
---


{%- include partials/header.html -%}

<div class="container">
  <div class="alert bg-blue mx-auto" role="alert" style="max-width: 40rem;">
    <a href="https://t.me/ethereumadoption">
      {{site.data.icons.megaphone}}
      Get notified of new additions on Telegram!
    </a>
  </div>
</div>


<!-- Content -->
<section class="container">
  <div class="pb-5">
    <div class="row justify-content-center">
      <div class="col-12 mb-4">
        <div class="card rounded-3 mx-auto bg-blue text-gray" style="max-width: 40rem;">
          <div class="card-body my-3 mx-0 mx-sm-2 mx-md-3">
            {% include partials/search.html %}
            {% include partials/view-controls.html %}
            <!-- Group by Date -->
            <div id="dateGroup" class="">
              {% include partials/grouped-by-date-chart.html %}
              {% include partials/grouped-by-date.html %}
            </div>
            <!-- Group by Entity -->
            <div id="entityGroup" class="d-none">
              {% include partials/grouped-by-entity.html %}
            </div>
            <!-- Group by Network -->
            <div id="networkGroup" class="d-none">
              {% include partials/grouped-by-network-chart.html %}
              {% include partials/grouped-by-network.html %}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
