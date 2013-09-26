from app import app
import argparse
import os
import routes


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                        description='Run the MightySpring backend server.')
    parser.add_argument('--debug', 
                        '-d', 
                        default=True)
    parser.add_argument('--port',
                        '-p',
                        nargs='?',
                        default=int(os.environ.get('PORT', 5000)),
                        type=int)
    parser.add_argument('--bind-address',
                        '-b',
                        nargs='?',
                        default=u'0.0.0.0',
                        type=unicode)

    args = parser.parse_args()
    debug = args.debug
    port = args.port
    bind_address = args.bind_address
    
    app.run(host=bind_address, port=port, debug=debug)