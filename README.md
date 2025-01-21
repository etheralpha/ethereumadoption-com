# ethereumadoption-com

This is the source code for <https://ethereumadoption.com>, a list of high profile entities building on Ethereum. This site focuses on non-crypto native entities.



## Local Development

1. Clone the repo (or fork the repo to your account)
1. Install dependencies: `bundle install`
1. Create a feature branch off of the `dev` branch
1. Start the local server: `bundle exec jekyll serve`
1. Go to <http://localhost:4400/> to view changes

To build the site use `bundle exec jekyll build`.

Resources:

- [Jekyll Docs](https://jekyllrb.com/docs/)
- [Liquid Syntax](https://shopify.github.io/liquid/basics/introduction/)


## Integrate Data

To use this data, simply query one of the following endpoints:
- `https://ethereumadoption.com/adoption.json`
- `https://ethereumadoption.com/adoption.yml`

Please do not abuse these endpoints, checking once or twice a day would be sufficient given the update frequency.

To get new additions you can use `https://ethereumadoption.com/adoption-new-entries.json`. This is updated every hour, roughly at the start of the hour. Each entry has an `is_recent` attribute. If `is_recent: true` then it's a recent event. If `is_recent: false` then it's a stale event that was previously missed. As time goes on there should be less stale/backdated events being added.


## Contributing

To add a new entry, add it to `_data/adoption.yml` using the template provided.

