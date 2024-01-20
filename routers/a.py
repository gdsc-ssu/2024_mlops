from fastapi import APIRouter

a = APIRouter(prefix = '/a')

@a.get('/', tags=['a'])
async def start_a():
    return {'msg' : 'a'}

@a.get('/model', tags=['a'])
async def a_model():
    return {'msg' : 'a model'}
