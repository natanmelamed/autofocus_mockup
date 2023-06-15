from autofocus_resources import *
from fastapi import APIRouter, Header
from common.content_types import ContentType
from fastapi.responses import PlainTextResponse
from common.response_data_handler import ResponseDataHandler

router: APIRouter = APIRouter()
_response_data_handler: ResponseDataHandler = ResponseDataHandler(mongo=True,
                                                                      collection_name="autofocus")


@router.post("/api/v1.0/samples/search")
async def get_af_cookie(af_cookie: RequestBody) -> dict:
    sample_type = af_cookie.query.children[0].field
    af_cookie = create_af_cookie(sample_type)
    return af_cookie


@router.post("/api/v1.0/sample/{sha256_value}/analysis")
async def get_sample_analysis_by_sha256(sha256_value: str, query: AnalysisQuery) -> dict:
    return _response_data_handler.get_response_data_by_source(
        get_sample_analysis_by_sha256.__name__.replace("_", "-"), sha256_value[:10],
        required_query=True)


@router.get("/api/v1.0/output/threatFeedResult/", response_class=PlainTextResponse)
async def get_threat_indicator_feed(apiKey: str = Header("default_api_key_value")) -> dict:
    return _response_data_handler.get_response_data_by_source(
        get_threat_indicator_feed.__name__.replace("_", "-"), content_type=ContentType.TEXT)


@router.post("/api/v1.0/samples/results/{af_cookie}")
async def get_artifact_by(artifact: ArtifactRequest, af_cookie: str) -> dict:
    return _response_data_handler.get_response_data_by_source(
        get_artifact_by.__name__.replace("_", "-"), af_cookie[:10], required_query=True)


@router.get("/result/api/v1.0/samples/results/{artifact_type}")
async def get_artifact_by_result(artifact_type: str) -> dict:
    return _response_data_handler.get_response_data_by_source(
        get_artifact_by_result.__name__.replace("_", "-"), artifact_type, required_query=True)


@router.get("/result/api/v1.0/sample/{hash_value}/analysis")
async def get_sample_analysis_result(hash_value: str) -> dict:
    return _response_data_handler.get_response_data_by_source(
        get_sample_analysis_result.__name__.replace("_", "-"), hash_value[:10], required_query=True)
