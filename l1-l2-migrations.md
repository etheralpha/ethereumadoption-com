---
layout: default
---


{%- include partials/header.html title="L1 > L2 Migrations" tagline="A list of L1s that migrated to Ethereum L2s" -%}


<!-- Content -->
<section id="migrations" class="pb-5">
  <div class="container">
    <div class="table-responsive mx-auto" style="max-width: 40rem;">
      <table id="migrationsTable" class="table">
        <thead>
          <tr>
            <th scope="col">Date</th>
            <th scope="col">Migration</th>
            <th scope="col">Source</th>
          </tr>
        </thead>
        <tbody>
          {%- assign migrations = site.data.pivots-chains -%}
          {%- for migration in migrations -%}
            <tr>
              <td>{{migration.date  | date: "%b %d, %Y"}}</td>
              <td>{{migration.title}}</td>
              <td><a href="{{migration.link}}" target="_blank">{{site.data.icons.document}}</a></td>
            </tr>
          {%- endfor -%}
        </tbody>
      </table>
    </div>
  </div>
</section>
