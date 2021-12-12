from my_blueprint import bp
from sanic import Sanic
from sanic.exceptions import ServerError, abort
from sanic.response import json, text

app = Sanic(__name__)
app.blueprint(bp)


# @app.route("/")
# async def test(request):
#     return json({'hello': 'world'})


@app.route("/killme")
def i_am_ready_to_die(request):
    raise ServerError("Something bad happening", status_code=500)


@app.route("/youshallnotpass")
def no_no(request):
    abort(401)
    # this won't happen
    text("OK")


@app.websocket("/feed")
async def feed(request, ws):
    while True:
        data = "hello"
        print(f"Sending: {data}")
        await ws.send(data)
        data = await ws.recv()
        print(f"Received: {data}")


@app.middleware("request")
async def print_on_request(request):
    print("I print when a request is received by the server")


@app.middleware("response")
async def print_on_response(request, response):
    print("I print when a response is returned by the server")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
