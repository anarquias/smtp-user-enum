#!/usr/bin/python3

import os
import sys
import socket
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument( '--username',  type=str,   help='put single username here' )
    parser.add_argument( '--usernames',             help='put file of usernames' )
    parser.add_argument( '--port',      type=int,   help='put the tcp port here' )
    parser.add_argument( '--hostname',  type=str,   help='put here the hostname of the smtp server' )
    parser.add_argument( '--num',       type=int,   help='put the number of usernames to check' )
    args = parser.parse_args()


if __name__ == "__main__":
            main()


