Simple Internet messenger

Setup:
	$ make setup & make
Usage:

Sending messages:
	 Send a HTTP/S GET request to http://example.url/msg?uname={your usernmae}&msg={your message}channel={channel name}

Reading messages:
	Send a HTTP/S request to http://example.url/channel/{channel name}

clean up:
	$ make clean
