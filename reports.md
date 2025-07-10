---
layout: default
---


{%- include partials/header.html title="ETH Reports" tagline="A list of ETH investment reports" -%}


<!-- Content -->
<section class="d-none pb-5">
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-12 mb-4">
        <div class="card rounded-3 mx-auto bg-blue text-gray" style="max-width: 40rem;">
          <div class="card-body my-3 mx-0 mx-sm-2 mx-md-3">
            <ul>
            {%- assign reports = site.data.reports -%}
            {%- for report in reports -%}
              {%- if report.link -%}
                <li class="entry">
                  {{report.author}} - <a href="{{report.link}}" target="_blank">{{report.title}}</a>
                </li>
              {%- endif -%}
            {%- endfor -%}
          </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>





<!-- Content -->
<section id="reports" class="pb-5 dd-none">
  <div class="container">
    <div class="table-responsive mx-auto" style="max-width: 40rem;">
      <table id="reportsTable" class="table">
        <thead>
          <tr>
            <th scope="col">Author</th>
            <th scope="col">Report</th>
          </tr>
        </thead>
        <tbody>
          {%- assign reports = site.data.reports -%}
          {%- for report in reports -%}
            <tr>
              <td>{{report.author}}</td>
              <td><a href="{{report.link}}" target="_blank">{{report.title}}</a></td>
            </tr>
          {%- endfor -%}
        </tbody>
      </table>
    </div>
  </div>
</section>
