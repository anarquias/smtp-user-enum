#!/usr/bin/python3

import os
import sys
import socket
import argparse

def checkConnectionAndReturnSocket( Hostname, Port ):
    s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    connection = s.connect( (socket.gethostbyname( Hostname ), Port) )

    if connection == True:
        return s
    else:
        return False

def checkByUsernameFile( F, Hostname, Port, numLines ):
        s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        s.connect( (socket.gethostbyname( Hostname ), Port) )
        f = open( F, 'r' )
        if f:
            i = 0
            while i != numLines:
                user = f.readline().strip()
                s.send( 'VRFY '.encode() + user.encode() + ' \r\n'.encode() )
                usercheck = s.recv( 1024 )
                if '250'.encode() in usercheck:
                    print( '[*] {} exist on the mail server'.format( user ) )
                else:
                    print( '[-] {} doesn\'t exist on the mail server'.format( user ) )
                i = i + 1

def checkTheUser( user, Hostname, Port ):
        s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        s.connect( (socket.gethostbyname( Hostname ), Port) )
        s.send( 'VRFY '.encode() + user.encode() + ' \r\n'.encode() )
        usercheck = s.recv( 1024 )
        if '250'.encode() in usercheck:
            print( '[*] {} exist on the mail server'.format( user ) )
        else:
            print( '[-] {} doesn\'t exist on the mail server'.format( user ) )

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument( '--username',  type=str,   help='put single username here' )
    parser.add_argument( '--usernames',             help='put file of usernames' )
    parser.add_argument( '--port',      type=int,   help='put the tcp port here' )
    parser.add_argument( '--hostname',  type=str,   help='put here the hostname of the smtp server' )
    parser.add_argument( '--num',       type=int,   help='put the number of usernames to check' )
    args = parser.parse_args()

    if args.hostname:
        if args.port:
            checkConnectionAndReturnSocket( args.hostname, args.port )
            print( '[*] the server is alive and port 25 is open' )
    else:
        print( '[-] the server is not alive or the tcp port is not open' )
        sys.exit(1)
    if args.username:
        checkTheUser( args.username, args.hostname, args.port )
    elif args.usernames:
        if args.num is None:
            print( 'you have to specify the number of checks' )
    else:
        checkByUsernameFile( args.usernames, args.hostname, args.port, args.num )

if __name__ == "__main__":
            main()


