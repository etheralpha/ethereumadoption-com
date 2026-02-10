# This plugin will sort alphabetically
# 
# Usage:
#   list = ["Banana", "apple", "Cherry", "date"]
#   {{ list | alphabetize }}
# 
# Output:
#   ["apple", "Banana", "Cherry", "date"]

module Jekyll
  module Alphabetize

    def alphabetize(input)
      input.sort_by(&:downcase)
    end

  end
end

Liquid::Template.register_filter(Jekyll::Alphabetize)