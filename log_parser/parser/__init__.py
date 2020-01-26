from log_parser.parser.parser import Parser
from log_parser.parser.pattern_builder import Director, GunicornPatternBuilder


pattern_builder = Director(builder=GunicornPatternBuilder())
pattern_builder.build_pattern()
pattern = pattern_builder.get_pattern()

parser = Parser(pattern=pattern)
