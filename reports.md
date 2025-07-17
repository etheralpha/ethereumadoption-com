---
layout: default
---


{%- include partials/header.html title="ETH Reports" tagline="A list of ETH investment reports" -%}


<!-- Content -->
<section id="reports" class="pb-5">
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
