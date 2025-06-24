def main():
    import argparse
    from smapp import smapp

    parser = argparse.ArgumentParser()

    parser.add_argument('-u',
                        '--url',
                        type=str,
                        dest='url',
                        default='https://httpbin.org/post',
                        help='Number of smapps to send.')

    parser.add_argument('-s',
                        '--smapps',
                        dest='smapps',
                        type=int,
                        default=10,
                        help='Number of smapps to send.')

    parser.add_argument('-i',
                        '--iterator-range',
                        dest='iterator_range',
                        type=int,
                        default=1,
                        help='Number of times to request a list of proxies.')

    parser.add_argument('-l',
                        '--list-limit',
                        dest='list_limit',
                        type=int,
                        default=10,
                        help='Number of proxies to return in each request.')

    cli_args = parser.parse_args()

    url = cli_args.url
    smapps = cli_args.smapps
    iterator_range = cli_args.iterator_range
    list_limit = cli_args.list_limit

    smapp.smapp_dat_ass(smapps, iterator_range, list_limit, url)

if __name__ == '__main__':
    main()