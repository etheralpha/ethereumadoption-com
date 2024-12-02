---
layout: default
---


{%- include partials/header.html title="Ethereum Usecases" tagline="A list of non-speculative usecases with examples" -%}


<!-- Content -->
<section class="pb-5">
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-12 mb-4">
        <div class="card rounded-3 mx-auto bg-blue text-gray" style="max-width: 40rem;">
          <div class="card-body my-3 mx-0 mx-sm-2 mx-md-3">
            {%- assign usecases = site.data.usecases | sort: "category" -%}
              {%- for item in usecases -%}
                {%- assign cat_id = item.category | downcase | replace: " ", "-" -%}
                <div id="{{cat_id}}" class="group-header">{{item.category}}</div>
                {%- for example in item.examples -%}
                  <div class="entry">
                    {%- if example.link -%}
                      <a href="{{example.link}}" target="_blank">{{example.title}}</a>
                    {%- else -%}
                      <span class="">{{example.title}}</span>
                    {%- endif -%}
                  </div>
                {%- endfor -%}
              {%- endfor -%}
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
