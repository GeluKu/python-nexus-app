import httpx

def get_catfacts():
    r = httpx.get('https://httpbin.org/get')
    print (f'Response: {r.status_code}')
    print(f'Content: {r.content}')

if __name__ == '__main__':
    get_catfacts()


