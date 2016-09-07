dirs = Dir.glob(File.join(File.dirname(__FILE__), "..", "projects", "**", "**"))

dirs.sort_by{ |d| d.length }
	.reverse
	.select{ |d| 
		puts d
		File.directory?(d) 
	}.each do |dir|
		puts dir
		cleaned = File.basename(dir).downcase.gsub(/[^a-z0-9\-]/, "-")
		destination = File.join(File.dirname(dir), cleaned)
		if dir != destination
			File.rename(dir, destination)
		end
end