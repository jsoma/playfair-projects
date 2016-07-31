require 'front_matter_parser'
require 'kramdown'
require 'nokogiri'
require 'yaml'

RSpec.describe do

  def filenames_from(path, matcher = '*')
    files = Dir.glob(File.join(path, matcher)).select{ |f| File.file?(f) }
    filenames = files.map{ |f| File.basename(f) }
  end

  user_paths = Dir.glob(File.join(File.dirname(__FILE__), '..', 'projects', '*')).select{ |f| File.directory?(f) }

  user_paths.each do |user_path|

    context "#{File.basename(user_path)}'s" do

      context "submitter directory" do
        it "should contain a BIO.yml" do
          files = Dir.glob(File.join(user_path, '*')).select{ |f| File.file?(f) }
          filenames = files.map{ |f| File.basename(f) }
          expect(filenames).to include("BIO.yml")
        end

        it "should ONLY contain a BIO.yml" do
          files = Dir.glob(File.join(user_path, '*')).select{ |f| File.file?(f) }
          filenames = files.map{ |f| File.basename(f) }
          expect(filenames - ["BIO.yml"]).to be_empty
        end

        context "BIO.yml" do
          it "includes a name" do
            contents = YAML.load_file(File.join(user_path, "BIO.yml"))
            expect(contents['name']).to be_truthy
          end

          it "includes an email address" do
            contents = YAML.load_file(File.join(user_path, "BIO.yml"))
            expect(contents['email']).to be_truthy
          end

        end
      end

      project_dirs = Dir.glob(File.join(user_path, '*')).select{ |f| File.directory?(f) }
      
      project_dirs.each do |project_dir|

        context "project #{File.basename(project_dir)}" do

          included = %w(STORY.md DIARY.md README.md)
          included.each do |required_file|
            it "should include a #{required_file}" do
              filenames = filenames_from(project_dir)
              expect(filenames).to include(required_file)
            end
          end

          it "should include a .png image" do
              filenames = filenames_from(project_dir, "*.png")
              expect(filenames.length).to be > 0
          end

          context "STORY.md" do
            story_md = File.join(project_dir, "STORY.md")

            context "front matter" do
              it "is correctly formatted" do
                parsed = FrontMatterParser.parse_file(story_md)
                expect(parsed.front_matter).not_to be_empty
              end

              it "includes a title" do
                parsed = FrontMatterParser.parse_file(story_md)
                expect(parsed.front_matter['title']).not_to be_empty
              end

              it "includes a summary" do
                parsed = FrontMatterParser.parse_file(story_md)
                expect(parsed.front_matter['title']).not_to be_empty
              end
            end

            context "markdown" do

              context "image" do
                it "is included in the markdown" do
                  parsed = FrontMatterParser.parse_file(story_md)
                  html = Kramdown::Document.new(parsed.content).to_html
                  html_doc = Nokogiri::HTML(html)
                  image = html_doc.css("img").first

                  expect(image).not_to be_nil
                end

                it "actually exists in the directory" do
                  parsed = FrontMatterParser.parse_file(story_md)
                  html = Kramdown::Document.new(parsed.content).to_html
                  html_doc = Nokogiri::HTML(html)
                  image = html_doc.css("img").first

                  filename = File.join(project_dir, image['src'])
                  expect(File.exists?(filename)).to be true
                end
              end
            end
          end
        end

      end

    end
  end
end