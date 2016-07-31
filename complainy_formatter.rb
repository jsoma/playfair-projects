RSpec::Support.require_rspec_core "formatters/base_text_formatter"

class ComplainyFormatter < RSpec::Core::Formatters::BaseTextFormatter
  RSpec::Core::Formatters.register self, :example_group_started, :example_group_finished,
                            :example_passed, :example_pending, :example_failed, :message

  def initialize(output)
    super
    @group_level = 0
  end

  def message(notification)
    # output.puts notification.message
  end

  def dump_failures(notification)
    # return if notification.failure_notifications.empty?
    # output.puts notification.fully_formatted_failed_examples
  end

  def dump_pending(notification)
  #   return if notification.pending_examples.empty?
  #   output.puts notification.fully_formatted_pending_examples
  end

  def dump_summary(summary)

    err_count = summary.examples.select{ |e| e.execution_result.status == :failed }.length

    output.puts ""
    output.puts RSpec::Core::Formatters::ConsoleCodes.wrap("Automatic testing says: #{err_count} things to fix", :magenta)
    output.puts ""

    summary.examples.each do |example|
      color = case example.execution_result.status 
      when :passed 
        #output.puts passed_output(example)
      when :failed
        output.puts failure_output(example)
      when :pending
        output.puts pending_output(example)
      end
    end
    # output.puts summary.fully_formatted
    # output.puts summary.inspect
  end

  def example_group_started(notification)
    # output.puts if @group_level == 0
    # output.puts "#{current_indentation}#{notification.group.description.strip}"

    # @group_level += 1
  end

  def example_group_finished(_notification)
    # @group_level -= 1
  end

  def example_passed(passed)
    # output.puts passed_output(passed.example)
  end

  def example_pending(pending)
    # output.puts pending_output(pending.example,
    #                            pending.example.execution_result.pending_message)
  end

  def example_failed(failure)
    # output.puts failure_output(failure.example,
    #                            failure.example.execution_result.exception)
  end

  private

  def passed_output(example)
    RSpec::Core::Formatters::ConsoleCodes.wrap("PASSED: #{example.full_description.strip}", :success)
  end

  def pending_output(example)
    RSpec::Core::Formatters::ConsoleCodes.wrap("PENDING: #{example.full_description.strip} ", :pending)
  end

  def failure_output(example)
    #RSpec::Core::Formatters::ConsoleCodes.wrap(example.full_description.strip, :failure)
    RSpec::Core::Formatters::ConsoleCodes.wrap("👿  #{example.full_description.strip}", :failure)
  end

  def next_failure_index
    @next_failure_index ||= 0
    @next_failure_index += 1
  end

  def current_indentation
    '  ' * @group_level
  end

end