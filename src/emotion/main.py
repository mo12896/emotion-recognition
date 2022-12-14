import app_controller as ctrl
from app_gui import parse_arguments


def main() -> None:
    args = parse_arguments()
    ctrl.controller(args)


if __name__ == "__main__":
    main()
