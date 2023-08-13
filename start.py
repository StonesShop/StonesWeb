import uvicorn


if __name__ == "__main__":
    config = uvicorn.Config("app.main:app", port=5000,
                            log_level="info", host='0.0.0.0', reload=True)
    server = uvicorn.Server(config)
    server.run()
