from fastapi.responses import JSONResponse

NOT_FOUND_ERROR: dict = {"error": "Error 404 Not Found",
                         "error_description": "The requested URL was not found on this server."}


class ErrorResponses:
    @staticmethod
    def get_not_found_error() -> JSONResponse:
        return JSONResponse(
            status_code=404,
            content=NOT_FOUND_ERROR
        )
