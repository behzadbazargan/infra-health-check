#!/usr/bin/env python3

import argparse
import socket
import sys
from datetime import datetime


def check_port(host, port, timeout):
    """Check whether a TCP port is reachable."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, socket.error):
        return False


def parse_ports(value):
    """Parse comma-separated ports."""
    ports = []

    for item in value.split(","):
        item = item.strip()

        try:
            port = int(item)
        except ValueError:
            raise argparse.ArgumentTypeError(
                f"Invalid port: {item}"
            )

        if not 1 <= port <= 65535:
            raise argparse.ArgumentTypeError(
                f"Port must be between 1 and 65535: {port}"
            )

        ports.append(port)

    return ports


def main():
    parser = argparse.ArgumentParser(
        description="Lightweight TCP infrastructure health checker."
    )

    parser.add_argument(
        "host",
        help="Target hostname or IP address"
    )

    parser.add_argument(
        "ports",
        type=parse_ports,
        help="TCP ports separated by commas (example: 22,80,443)"
    )

    parser.add_argument(
        "-t",
        "--timeout",
        type=float,
        default=2.0,
        help="Connection timeout in seconds (default: 2)"
    )

    args = parser.parse_args()

    print("=" * 45)
    print("        Infra Health Check")
    print("=" * 45)
    print()
    print(f"Target : {args.host}")
    print(f"Time   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    success = 0
    failed = 0

    for port in args.ports:
        if check_port(args.host, port, args.timeout):
            print(f"[OK]   TCP/{port:<5} : reachable")
            success += 1
        else:
            print(f"[FAIL] TCP/{port:<5} : unreachable")
            failed += 1

    print()
    print("-" * 45)
    print(f"Result : {success} OK / {failed} FAILED")
    print("-" * 45)

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
