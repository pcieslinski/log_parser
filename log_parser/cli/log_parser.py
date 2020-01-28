import sys

from log_parser.parser import parser
from log_parser.commands import StatsCommand
from log_parser.renderers import ErrorRenderer
from log_parser.exceptions import LogParserException
from log_parser.cli.main_args_parser import main_parse_args
from log_parser.cli.stats_args_parser import stats_parse_args


class LogParser:
    def __init__(self) -> None:
        args = main_parse_args(sys.argv[1:2])

        if not hasattr(self, args.command):
            err_message = (f'The given command: {args.command} is not supported.'
                           ' To learn more about using the log-parser run `log-parser -h`')
            ErrorRenderer(
                error=err_message,
                detail_error=err_message,
                verbose=False,
                type='CommandNotFound'
            ).render()
            exit(1)

        getattr(self, args.command)()

    def stats(self) -> None:
        args = stats_parse_args(sys.argv[2:])

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
