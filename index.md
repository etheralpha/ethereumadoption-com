---
layout: default
---


{%- include partials/header.html -%}


<!-- Content -->
<section class="pb-5">
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-12 mb-4">
        <div class="card rounded-3 mx-auto bg-blue text-gray" style="max-width: 40rem;">
          <div class="card-body my-3 mx-0 mx-sm-2 mx-md-3">
            {% include partials/search.html %}
            {% include partials/view-controls.html %}
            <!-- Group by Date -->
            <div id="dateGroup" class="">
              {% include partials/grouped-by-date.html %}
            </div>
            <!-- Group by Entity -->
            <div id="entityGroup" class="d-none">
              {% include partials/grouped-by-entity.html %}
            </div>
            <!-- Group by Network -->
            <div id="networkGroup" class="d-none">
              {% include partials/grouped-by-network.html %}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
