from typing import List
from pydantic import BaseModel
from common.json_parser import load_data_from_json_file
from common.data_files_handler import get_full_path_file_by_file_name

AF_COOKIE_DATA_FILE_PATH = get_full_path_file_by_file_name("af_cookie.json")

af_cookie_mapping = {
    'sample.filetype': ['2-03d85760-b1c2-4cf2-8a73-0467659b9354+0', 189, 421, '2020-12-20 13:02:54',
                        '2020-12-19 13:51:11'],
    'sample.threat_name': ['2-758ccd8b-0740-486b-952f-97f81d590aab+0', 189, 4810, '2020-12-20 13:05:55',
                           '2020-12-19 13:51:11'],
    'sample.md5': ['2-d6dddba0-a8b2-4d15-b403-b7f3e27b997b+0', 189, 4776, '2020-12-20 13:15:05', '2020-12-19 13:51:11'],
    'sample.malware': ['2-90229bea-8a86-47d7-9946-bd7ece3eb29f+0', 178, 4890, '2020-12-20 12:34:45',
                       '2020-12-19 13:51:11']
}


def create_af_cookie(sample_type: str) -> dict:
    if sample_type in af_cookie_mapping.keys():
        af_cookie = af_cookie_mapping[sample_type]
    else:
        return {"error_message": "Please enter a valid field name"}
    af_cookie_data = update_cookie_value(af_cookie)
    return af_cookie_data


def update_cookie_value(af_cookie) -> dict:
    af_cookie_data = load_data_from_json_file(AF_COOKIE_DATA_FILE_PATH)
    af_cookie_data['af_cookie'] = af_cookie[0]
    af_cookie_data['bucket_info']['minute_points_remaining'] = af_cookie[1]
    af_cookie_data['bucket_info']['daily_points_remaining'] = af_cookie[2]
    af_cookie_data['bucket_info']['minute_bucket_start'] = af_cookie[3]
    af_cookie_data['bucket_info']['daily_bucket_start'] = af_cookie[4]
    return af_cookie_data


class Children(BaseModel):
    field: str
    operator: str
    value: str


class Query(BaseModel):
    operator: str = None
    children: List[Children]


class RequestBody(BaseModel):
    apiKey: str
    query: Query
    size: int
    sort: dict = None
    scope: str


class AfCookie(BaseModel):
    af_cookie: int
    af_complete_percentage: int
    af_in_progress: bool
    af_first_result_af_took: int
    bucket_info: dict


class AnalysisQuery(BaseModel):
    apiKey: str
    coverage: bool
    sections: List[str]


class ArtifactRequest(BaseModel):
    apiKey: str
