require 'optparse'

def load(filename, folder = "images/")
    path = folder + filename + ".svg"
    return File.read(path)
end

def save(filename, file_data, folder = "output/")
    path = folder + filename + ".svg"
    File.write(path, file_data, mode: "w")
end

def create(name, color, power)
    build = '<svg xmlns="http://www.w3.org/2000/svg" width="512" height="768">'
    build += load(name)
    build += '<rect width="492" height="100" fill="#101010a0" x="10" y="10" rx="50" ry="50"/>'
    build += '<text font-size="44" fill="'+color+'" x="100" y="74">'+name+'</text>'
    build += '<circle r="30" cx="60" cy="60" fill="'+color+'"/>'
    build += '<text font-size="44" fill="#101010f0" x="47" y="74">'+power+'</text>'
    build += '</svg>'

    save(name, build)
end

options = {}
OptionParser.new do |opts|
  opts.banner = "Usage: main.rb [options]"
  opts.on("--name NAME", "Name of the card") do |n|
    options[:name] = n
  end
  opts.on("--color COLOR", "Color of the card") do |c|
    options[:color] = c
  end
  opts.on("--power POWER", "Power of the card") do |p|
    options[:power] = p
  end
  opts.on("-h", "--help", "Prints this help") do
    puts opts
    exit
  end
end.parse!

create(options[:name], options[:color], options[:power])