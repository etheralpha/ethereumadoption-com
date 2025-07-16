---
layout: default
---


<!-- Header -->
<header class="py-3 my-2">
  <div class="container text-center">
    <h1 class="display-5 fw-bold text-capitalize mt-2 mt-sm-4 mt-md-5">Ethereum: The Global Economic Layer</h1>
    <div class="col-lg-7 mx-auto">
      <p class="lead mb-4">Build on the most secure, liquid, and programmable blockchain ecosystem</p>
      <div class="d-flex justify-content-center gap-3 flex-wrap">
        <a href="#build-l1" class="btn btn-primary pop">Build on L1</a>
        <a href="#build-l2" class="btn btn-light pop">Build on L2</a>
        <a href="/built-on-ethereum" class="btn btn-outline-light pop">Dashboard</a>
      </div>
      <div class="row g-4 my-4 text-center" data-sal="slide-up">
        <div class="col-sm-6 col-md-4 col-lg-6 col-xl-4">
          <div class="card pop h-100">
            <div class="card-body">
              <h3 class="card-title">$<span id="overviewRWA">{{site.data.overview.rwas.amount}}</span>{{site.data.overview.rwas.unit}}+</h3>
              <p class="card-text">RWAs</p>
            </div>
          </div>
        </div>
        <div class="col-sm-6 col-md-4 col-lg-6 col-xl-4">
          <div class="card pop h-100">
            <div class="card-body">
              <h3 class="card-title">$<span id="overviewStablecoins">{{site.data.overview.stablecoins.amount}}</span>{{site.data.overview.stablecoins.unit}}+</h3>
              <p class="card-text">Stablecoins</p>
            </div>
          </div>
        </div>
        <div class="col-sm-12 col-md-4 col-lg-6 col-xl-4">
          <div class="card pop h-100">
            <div class="card-body">
              <h3 class="card-title">$<span id="overviewTVL">{{site.data.overview.tvl.amount}}</span>{{site.data.overview.tvl.unit}}+</h3>
              <p class="card-text">Total Value Locked</p>
            </div>
          </div>
        </div>
        <div class="col-sm-12 col-md-6 col-lg-6 col-xl-6">
          <div class="card pop h-100">
            <div class="card-body">
              <h3 class="card-title">Ξ<span id="overviewExported">{{site.data.overview.exported.amount}}</span>{{site.data.overview.exported.unit}}+</h3>
              <p class="card-text">ETH Exported to L2s</p>
            </div>
          </div>
        </div>
        <div class="col-sm-12 col-md-6 col-lg-12 col-xl-6">
          <div class="card pop h-100">
            <div class="card-body">
              <h3 class="card-title">Ξ<span id="overviewReserves">{{site.data.overview.reserves.amount}}</span>{{site.data.overview.reserves.unit}}+</h3>
              <p class="card-text">Strategic Reserves Held in ETH</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</header>



<!-- Industry Leaders -->
<div id="industryLeaders" class="container py-0 py-md-3 py-lg-5">
  <h2 class="section-title text-center" data-sal="slide-up">Join Industry Leaders on Ethereum</h2>
  <div class="row d-flex justify-content-center" data-sal="slide-up">
    <div class="col-12 col-xl-10 quote text-center">
      <p>"There was no question the blockchain we would start our tokenization on would be Ethereum, and that's not just a BlackRock thing. That's the natural default answer. That's really important."
        <div>⏤ <a href="https://www.youtube.com/live/ZElYvaq0JTQ?t=7419s">Robbie Mitchnick, BlackRock Head of Digital Assets</a></div>
      </p>
    </div>
  </div>
  <div class="row text-center" data-sal="slide-up">
    <div class="col col-6 col-sm-4 col-lg-3 my-5">
      <a href="/built-on-ethereum?view=byEntity#entity-blackrock">
        <img class="p-1" src="/assets/img/builders/blackrock.png">
      </a>
    </div>
    <div class="col col-6 col-sm-4 col-lg-3 my-5">
      <a href="/built-on-ethereum?view=byEntity#entity-deutsche-bank">
        <img class="p-1" src="/assets/img/builders/deutsche-bank.png">
      </a>
    </div>
    <div class="col col-6 col-sm-4 col-lg-3 my-5">
      <a href="/built-on-ethereum?view=byEntity#entity-sony">
        <img class="p-1" src="/assets/img/builders/sony.png">
      </a>
    </div>
    <div class="col col-6 col-sm-4 col-lg-3 my-5">
      <a href="/built-on-ethereum?view=byEntity#entity-societe-generale">
        <img class="p-1" src="/assets/img/builders/societe-generale.png">
      </a>
    </div>
    <div class="col col-6 col-sm-4 col-lg-3 my-5">
      <a href="/built-on-ethereum?view=byEntity#entity-ubs">
        <img class="p-1" src="/assets/img/builders/ubs.png">
      </a>
    </div>
    <div class="col col-6 col-sm-4 col-lg-3 my-5">
      <a href="/built-on-ethereum?view=byEntity#entity-visa">
        <img class="p-1 py-2" src="/assets/img/builders/visa.webp">
      </a>
    </div>
    <div class="col col-6 col-sm-4 col-lg-3 my-5">
      <a href="/built-on-ethereum?view=byEntity#entity-fidelity">
        <img class="p-1" src="/assets/img/builders/fidelity.png">
      </a>
    </div>
    <div class="col col-6 col-sm-4 col-lg-3 my-5">
      <a href="/built-on-ethereum?view=byEntity#entity-ey">
        <img class="py-1" src="/assets/img/builders/ey.png">
      </a>
    </div>
  </div>
</div>



<!-- Ethereum Diagram -->
<div id="diagram" class="container py-0 py-md-3 py-lg-5">
  <h2 class="section-title text-center" data-sal="slide-up">What Is Ethereum L1 and L2?</h2>
  <div class="col-lg-10 col-xl-8 col-xxl-7 mx-auto">
    <p class="lead text-center mb-4">Ethereum is comprised of L1 and L2s. Ethereum Mainnet (L1) is the foundational base layer that apps L2s are built on top of. L2s are sovereign chains with custom environments built on Ethereum Mainnet.</p>
  </div>
  <div class="col-xl-10 col-xxl-9 mx-auto">
    <img class="w-100" src="/assets/img/diagrams/ethereum.png">
  </div>
</div>



<!-- L1 Benefits -->
<div id="build-l1" class="container py-0 py-md-3 py-lg-5">
  <h2 class="section-title text-center" data-sal="slide-up">Why Build on Ethereum L1?</h2>
  <div class="row g-4 d-flex justify-content-center" data-sal="slide-up">
    <div class="col-12 col-sm-6 col-xl-4">
      <div class="card pop h-100">
        <div class="card-body">
          <h5 class="card-title">Maximum Security</h5>
          <p class="card-text">Battle-tested and decentralized, Ethereum L1 secures the world’s largest onchain economy.</p>
        </div>
      </div>
    </div>
    <div class="col-12 col-sm-6 col-xl-4">
      <div class="card pop h-100">
        <div class="card-body">
          <h5 class="card-title">Maximum Liquidity</h5>
          <p class="card-text">Tap into trillions in stablecoins, ETH, and tokenized assets natively available.</p>
        </div>
      </div>
    </div>
    <div class="col-12 col-sm-6 col-xl-4">
      <div class="card pop h-100">
        <div class="card-body">
          <h5 class="card-title">Mature Tooling</h5>
          <p class="card-text">Leverage years of ecosystem development with rich libraries, dev tools, and infra.</p>
        </div>
      </div>
    </div>
    <div class="col-12 col-sm-6 col-xl-4">
      <div class="card pop h-100">
        <div class="card-body">
          <h5 class="card-title">Censorship Resistance</h5>
          <p class="card-text">Ethereum is globally distributed and leaderless, making it nearly impossible to censor or shut down.</p>
        </div>
      </div>
    </div>
    <div class="col-12 col-sm-6 col-xl-4">
      <div class="card pop h-100">
        <div class="card-body">
          <h5 class="card-title">Credibly Neutral</h5>
          <p class="card-text">Ethereum is public infrastructure that operates by protocol, not politics.</p>
        </div>
      </div>
    </div>
    <div class="col-12 col-sm-6 col-xl-4">
      <div class="card pop h-100">
        <div class="card-body">
          <h5 class="card-title">Developer Access</h5>
          <p class="card-text">Tap into the largest pool of blockchain developers for faster hiring and scalable growth.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- CTA to Build on L1 -->
  <div class="text-center mt-5 mb-4" data-sal="slide-up">
    <h4 class="fw-bold">Ready to start building on Ethereum L1?</h4>
    <p class="mb-3">Access world-class tooling, liquidity, and security today.</p>
    <a href="/build-on-ethereum#build-l1" class="btn btn-primary">Start Building on L1</a>
  </div>
</div>



<!-- L2 Benefits -->
<div id="build-l2" class="container py-0 py-md-3 py-lg-5">
  <h2 class="section-title text-center" data-sal="slide-up">Scale with Ethereum L2</h2>
  <div class="row g-4" data-sal="slide-up">
    <div class="col-md-4">
      <div class="card pop h-100">
        <div class="card-body">
          <h5 class="card-title">Higher Throughput</h5>
          <p class="card-text">Scale your dapps with rollups offering faster and cheaper transactions.</p>
        </div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card pop h-100">
        <div class="card-body">
          <h5 class="card-title">Custom Environments</h5>
          <p class="card-text">Design chains tailored to your needs — privacy, gas models, data availability, and execution.</p>
        </div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card pop h-100">
        <div class="card-body">
          <h5 class="card-title">Sovereign Yet Secure</h5>
          <p class="card-text">Enjoy L1-grade security while maintaining your network's autonomy.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- Side-by-side callouts -->
  <div class="row mt-5 g-4 ttext-center" data-sal="slide-up">
    <div class="col-md-4 d-flex align-items-stretch">
      <div class="card pop h-100">
        <div class="card-body d-flex flex-column">
          <h4 class="card-title">Build on an L2</h4>
          <p class="card-text mb-auto">
            Deploy on popular L2s like 
            <strong>Arbitrum</strong>, 
            <strong>Optimism</strong>, 
            <strong>Base</strong>, or
            <strong>ZKsync</strong>.
            (<a href="https://l2beat.com" class="text-underline">See more</a>)
          </p>
          <a class="btn btn-light mt-2 w-100" href="/build-on-ethereum#build-l2">Start Building on L2</a>
        </div>
      </div>
    </div>
    <!-- Launch Your Own L2 -->
    <div class="col-md-4 d-flex align-items-stretch">
      <div class="card pop h-100">
        <div class="card-body d-flex flex-column">
          <h4 class="card-title">Launch Your Own L2</h4>
          <p class="card-text mb-auto">Join industry leaders building L2s on Ethereum:
            <a class="text-underline" href="https://www.coinbase.com/blog/introducing-base">Coinbase</a>, 
            <a class="text-underline" href="https://blog.kraken.com/news/announcing-ink">Kraken</a>, 
            <a class="text-underline" href="https://soneium.org/en/blog/introducing-soneium-by-sony-block-solutions-labs-for-the-future-of-web3/">Sony</a>
          </p>
          <a class="btn btn-light mt-2 w-100" href="/build-on-ethereum#create-l2">Create Your Own L2</a>
        </div>
      </div>
    </div>
    <!-- L1 to L2 Migrations -->
    <div class="col-md-4 d-flex align-items-stretch">
      <div class="card pop h-100">
        <div class="card-body d-flex flex-column">
          <h4 class="card-title">L1 to L2 Migrations</h4>
          <p class="card-text mb-auto">L1 ecosystems are evolving by migrating to Ethereum L2s to gain access to unmatched security, and soon deep liquidity and shared infrastructure.</p>
          <p class="card-text">
            <strong>Case Studies</strong>:
            <a class="text-underline" href="https://blog.celo.org/celo-l2-is-now-live-a-note-from-our-founders-c585bd57b5fa">Celo</a>,
            <a class="text-underline" href="https://polygon.technology/blog/canto-to-migrate-to-a-zk-l2-powered-by-polygon-chain-development-kit">Canto</a>,
            <a class="text-underline" href="https://lisk.com/blog/posts/lisk-user-mainnet-is-live/">Lisk</a>,
            <a class="text-underline" href="https://blog.cronos.org/p/cronos-zkevm-launches-its-alpha-mainnet">Cronos</a>
          </p>
        </div>
      </div>
    </div>
  </div>
</div>



<!-- Roadmap -->
<div id="upcoming" class="container py-0 py-md-3 py-lg-5">
  <h2 class="section-title text-center" data-sal="slide-up">What’s Coming for Ethereum?</h2>
  <div class="row g-4" data-sal="slide-up">
    <div class="col-md-3 d-flex">
      <div class="card pop h-100">
        <div class="card-body d-flex flex-column">
          <h5 class="card-title pb-2 mb-auto">Shared Liquidity</h5>
          <p class="card-text">Aggregated, instant access to liquidity across L1 and L2s.</p>
        </div>
      </div>
    </div>
    <div class="col-md-3 d-flex">
      <div class="card pop h-100">
        <div class="card-body d-flex flex-column">
          <h5 class="card-title pb-2 mb-auto">Synchronous Composability</h5>
          <p class="card-text">Instant cross-rollup interactions like never before.</p>
        </div>
      </div>
    </div>
    <div class="col-md-3 d-flex">
      <div class="card pop h-100">
        <div class="card-body d-flex flex-column">
          <h5 class="card-title pb-2 mb-auto">Based Rollups</h5>
          <p class="card-text">Low overhead, minimal trust assumptions, max alignment.</p>
        </div>
      </div>
    </div>
    <div class="col-md-3 d-flex">
      <div class="card pop h-100">
        <div class="card-body d-flex flex-column">
          <h5 class="card-title pb-2 mb-auto">Native Rollups</h5>
          <p class="card-text">Rollups that feel like L1, powered directly by Ethereum.</p>
        </div>
      </div>
    </div>
    <div class="col-12 mt-4 text-center">
      <a href="https://ethroadmap.com/" class="btn btn-outline-light">View Roadmap</a>
    </div>
  </div>
</div>



<script>
  window.addEventListener('load', function(event) {
    startCountUp();
  });

  function startCountUp() {
    const options1 = {
      decimalPlaces: 0
    };
    const options2 = {
      decimalPlaces: 1
    };
    const overviewRWA = new countUp.CountUp("overviewRWA", {{site.data.overview.rwas.amount}}, options1);
    const overviewStablecoins = new countUp.CountUp("overviewStablecoins", {{site.data.overview.stablecoins.amount}}, options1);
    const overviewTVL = new countUp.CountUp("overviewTVL", {{site.data.overview.tvl.amount}}, options1);
    const overviewExported = new countUp.CountUp("overviewExported", {{site.data.overview.exported.amount}}, options2);
    const overviewReserves = new countUp.CountUp("overviewReserves", {{site.data.overview.reserves.amount}}, options2);
    overviewRWA.start();
    overviewStablecoins.start();
    overviewTVL.start();
    overviewExported.start();
    overviewReserves.start();
  }
</script>

