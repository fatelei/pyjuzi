import argparse

from pyjuzi.contact import ContactApi


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--endpoint",
                        dest="endpoint",
                        default="ex-api.botorange.com",
                        type=str,
                        help="api endpoint")
    parser.add_argument(
        "--token", dest="token", required=True, help="api token")
    args = parser.parse_args()
    contact_api = ContactApi(args.endpoint, args.token)
    print(contact_api.list_contact(0, 10))
