require 'front_matter_parser'

story_md_files = Dir.glob(File.join(__dir__, "..", "projects", "**", "STORY.md"))
failures = []
successes = []
story_md_files.each do |story_path|
  yaml_path = File.join(File.dirname(story_path), "STORY.yml")

  begin
    md_contents = File.read(story_path).gsub("\r","")
    parsed = FrontMatterParser.parse(md_contents)
    if parsed.front_matter.empty?
      failures.push story_path unless File.exists?(yaml_path)
    else
      # puts "Working on #{story_path}"
      # Store the front matter in story.yml
      File.open(yaml_path, 'w') { |f| f.write(parsed.front_matter.to_yaml.gsub(/-{3,}/,'').strip) }
      # Rewrite the .md file to NOT have front matter
      File.open(story_path, 'w') { |f| f.write(parsed.content) }
      successes.push story_path
    end
  rescue
    failures.push story_path
  end
end

puts "\n# Successes"
successes.each do |f|
  puts f 
end

puts "\n# Failures"
failures.each do |f|
  puts f 
end

puts "\nProcessed #{successes.length}, #{failures.length} failures"