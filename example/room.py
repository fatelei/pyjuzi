import argparse

from pyjuzi.room import RoomApi


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
    room_api = RoomApi(args.endpoint, args.token)
    print(room_api.list_rooms(0, 10))
