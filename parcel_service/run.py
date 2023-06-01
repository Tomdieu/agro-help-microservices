from parcel_app import app

import uvicorn

if __name__ == '__main__':
    uvicorn.run('run:app',port=8003,reload=True,app_dir='./')