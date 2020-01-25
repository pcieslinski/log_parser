from log_parser.cli import parser


def main():
    args = parser.parse_args()

    file = args.file
    since = args.since
    until = args.until

    print(f'Values: path - {file.name}, since - {since}, until - {until}')


if __name__ == '__main__':
    main()
