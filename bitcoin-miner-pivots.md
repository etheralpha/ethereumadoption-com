---
layout: default
---


{%- include partials/header.html title="Bitcoin Miner Pivots" tagline="A list of miners divesting from BTC to ETH" -%}


<!-- Content -->
<section id="bitcoinPivots" class="pb-5">
  <div class="container">
    <div class="table-responsive mx-auto" style="max-width: 40rem;">
      <table id="bitcoinPivotsTable" class="table">
        <thead>
          <tr>
            <th scope="col">Date</th>
            <th scope="col">Company</th>
            <th scope="col">ETH Holdings</th>
            <th scope="col">Source</th>
          </tr>
        </thead>
        <tbody>
          {%- assign pivots = site.data.pivots-miners -%}
          {%- for pivot in pivots -%}
            <tr>
              <td>{{pivot.date  | date: "%b %d, %Y"}}</td>
              <td>{{pivot.company}}</td>
              <td>{{pivot.holdings}}</td>
              <td><a href="{{pivot.link}}" target="_blank">{{site.data.icons.document}}</a></td>
            </tr>
          {%- endfor -%}
        </tbody>
      </table>
    </div>
  </div>
</section>
