import sys

from log_parser.cli import parse_args
from log_parser.parser import parser
from log_parser.commands import StatsCommand
from log_parser.renderers import ErrorRenderer
from log_parser.exceptions import LogParserException


def main() -> None:
    args = parse_args(sys.argv[1:])

    try:
        command = StatsCommand(parser=parser)
        command.run(args=args)
    except LogParserException as exc:
        ErrorRenderer(exc.message, exc.details, args.verbose, exc.type).render()
    except Exception as exc:
        ErrorRenderer(
            error='An unknown error occurred while the program was running.',
            detail_error=exc,
            verbose=args.verbose,
            type='Exception'
        ).render()


if __name__ == '__main__':
    main()
