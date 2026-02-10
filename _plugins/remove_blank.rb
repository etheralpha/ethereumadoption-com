# This plugin will remove empty strings from array
# 
# Usage:
#   list = ["Banana", "apple", "", "Cherry", "date"]
#   {{ list | remove_blank }}
# 
# Output:
#   ["Banana", "apple", Cherry", "date"]

module Jekyll
  module RemoveBlank

    def remove_blank(input)
      input.reject(&:empty?)
    end

  end
end

Liquid::Template.register_filter(Jekyll::RemoveBlank)