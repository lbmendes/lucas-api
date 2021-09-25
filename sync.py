import asyncio
sleep = asyncio.sleep


async def fazer_burguer(senha, n):
    print(f'Fazendo burguer {n} para cliente {senha}')
    await sleep(2)
    return b"[|O]"

async def app(scope, receive, send):
    await send({'type': 'http.response.start', 'status': 200})    
    
    senha = scope.get('path')
    burguer1 = await fazer_burguer(senha, 1)
    burguer2 = await fazer_burguer(senha, 2)
    burguer3 = await fazer_burguer(senha, 3)
    bandeija = burguer1 + burguer2 + burguer3
    
    await send({'type': 'http.response.body', 'body': bandeija})    