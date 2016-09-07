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
          it "should include a name" do
            contents = YAML.load_file(File.join(user_path, "BIO.yml"))
            expect(contents['name']).to be_truthy
          end

          it "should include an email address" do
            contents = YAML.load_file(File.join(user_path, "BIO.yml"))
            expect(contents['email']).to be_truthy
          end

        end
      end

      project_dirs = Dir.glob(File.join(user_path, '*')).select{ |f| File.directory?(f) }
      
      project_dirs.each do |project_dir|

        context "project #{File.basename(project_dir)}" do

          included = %w(STORY.md DIARY.md README.md STORY.yml)
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

          context "STORY.yml" do
            story_yml = File.join(project_dir, "STORY.yml")

            it "should be correctly formatted" do
              parsed = YAML.load_file(story_yml)
              expect(parsed).not_to be_empty
            end

            it "should contain a title" do
              parsed = YAML.load_file(story_yml)
              expect(parsed['title']).not_to be_empty
            end

            it "should contain a summary" do
              parsed = YAML.load_file(story_yml)
              expect(parsed['summary']).not_to be_empty
            end
          end

          context "STORY.md" do
            story_md = File.join(project_dir, "STORY.md")

            context "markdown" do

              context "image" do
                it "should be included in the markdown" do
                  content = File.read(story_md)
                  html = Kramdown::Document.new(content).to_html
                  html_doc = Nokogiri::HTML(html)
                  image = html_doc.css("img").first

                  expect(image).not_to be_nil
                end

                it "should actually exist in the directory" do
                  content = File.read(story_md)
                  html = Kramdown::Document.new(content).to_html
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