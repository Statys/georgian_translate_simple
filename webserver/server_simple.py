from aiohttp import web
#from requests import Response
import ge_transliteration as tr

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    print(text)
    return web.Response(text=text)

async def api_translate(request):
    params = request.rel_url.query
    msg = params["msg_text"]
    lang = params["lang"]
    msg_translated = tr.translit_to_ge(msg, lang)
    resp = {"text": msg_translated}
    return web.json_response(resp)

async def api_translate_test():
    tr.test_translit_to_ge()
    return web.Response(text='Test passed!')

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/api/translate', api_translate),
                web.get('/api/translate_test', api_translate_test)
                ])

if __name__ == '__main__':
    web.run_app(app)