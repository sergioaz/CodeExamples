"""
 **Standardizes field names**:
   - Accepts `"userId"`, `"user_id"`, or `"userid"` ➝ `user_id`
   - Accepts `"timestamp"`, `"time"`, or `"access_time"` ➝ `timestamp`
   - Accepts `"activity"`, `"action"`, or `"event"` ➝ `activity`

2. ✅ **Cleans and validates data**:
   - Converts `timestamp` to ISO 8601 format: `'YYYY-MM-DDTHH:MM:SSZ'`
     - Supports UNIX timestamps (int), or strings like `"2023-09-05 14:00"` or `"09/05/2023 14:00"`
     - If timestamp can't be parsed, set it to `"unknown"`
   - Ensures `user_id` is a string; if missing or null, set to `"unknown"`
   - Ensures `activity` is a lowercase string; if missing, set to `"unknown"`

3. ✅ **Adds metadata**:
   - Adds `"source_system"` field with the provided `source_system` value

4. ✅ **Removes corrupted records**:
   - Drop any record where **both** `user_id` and `timestamp` are `"unknown"`

"""
from datetime import datetime, timezone
from typing import List, Dict

def transform_logs(records: List[Dict], source_system: str) -> List[Dict]:
    res_list = []
    result = {}
    for record in records:
        if "userId" in record:
            result["user_id"] = record["userId"]
        elif "user_id" in record:
            result["user_id"] = record["user_id"]
        elif "userid" in record:
            result["user_id"] = record["userid"]
        else:
            result["user_id"] = "unknown"

        result["user_id"] = str(result["user_id"])

        if "activity" in record:
            result["activity"] = record["activity"].lower()
        elif "action" in record:
            result["activity"] = record["action"].lower()
        elif "event" in record:
            result["activity"] = record["event"].lower()
        else:
            result["activity"] = "unknown"

        if "timestamp" in record:
            result["timestamp"] = convert_timestamp(record["timestamp"])
        elif "time" in record:
            result["timestamp"] = convert_timestamp(record["time"])
        elif "access_time" in record:
            result["timestamp"] = convert_timestamp(record["access_time"])
        else:
            result["timestamp"] = "unknown"

        if result["user_id"] == "unknown" and result["timestamp"] == "unknown":
            continue

        result["source_system"] = source_system

        result_to_append = result.copy()

        res_list.append(result_to_append)
    
    return res_list


def convert_timestamp(ts) -> str:
    if isinstance(ts, int):
        return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    elif not isinstance(ts, str):
        return "unknown"
    elif not ts.strip():  # Handle empty strings
        return "unknown"
    else:
        # Split the timestamp string to get the time part
        try:
            parts = ts.split()
            if len(parts) < 2:
                return "unknown"
            time_part = parts[1]
            colon_count = time_part.count(":")
        except:
            return "unknown"
        
    if "-" in ts:
        # convert assuming yyyy-mm-dd hh:mm or yyyy-mm-dd hh:mm:ss
        if colon_count == 2:
            # we have seconds
            try:
                dt = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
                return dt.replace(tzinfo=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            except:
                return "unknown"
        elif colon_count == 1:
            try:
                dt = datetime.strptime(ts, "%Y-%m-%d %H:%M")
                return dt.replace(second=0, tzinfo=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            except Exception:
                return "unknown"
        else:
            # no colons, 
            return "unknown"
        
    elif "/" in ts:
        # convert assuming MM/DD/YYYY hh:mm
        if colon_count == 2:
            # we have seconds
            try:
                dt = datetime.strptime(ts, "%m/%d/%Y %H:%M:%S")
                return dt.replace(tzinfo=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            except Exception:
                return "unknown"
        elif colon_count == 1:
            try:
                dt = datetime.strptime(ts, "%m/%d/%Y %H:%M")
                return dt.replace(second=0, tzinfo=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            except Exception:
                return "unknown"
    return "unknown"

#import pytest

def test_convert_timestamp():
    # Valid ISO with seconds
    assert convert_timestamp("2023-09-05 14:00:32") == "2023-09-05T14:00:32Z"
    # Valid ISO without seconds
    assert convert_timestamp("2023-09-05 14:00") == "2023-09-05T14:00:00Z"
    # Valid US format with seconds
    assert convert_timestamp("09/05/2023 14:00:32") == "2023-09-05T14:00:32Z"
    # Valid US format without seconds
    assert convert_timestamp("09/05/2023 14:00") == "2023-09-05T14:00:00Z"
    # UNIX timestamp
    assert convert_timestamp(1693922432) == datetime.fromtimestamp(1693922432, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    # Invalid string
    assert convert_timestamp("not a date") == "unknown"
    # None
    assert convert_timestamp(None) == "unknown"
    # Empty string
    assert convert_timestamp("") == "unknown"


def test_transform_logs():
    # Test 1: Standard field mapping
    records = [
        {
            "userId": "user123",
            "activity": "LOGIN",
            "timestamp": "2023-09-05 14:00:32"
        }
    ]
    result = transform_logs(records, "web_app")
    expected = [
        {
            "user_id": "user123",
            "activity": "login",
            "timestamp": "2023-09-05T14:00:32Z",
            "source_system": "web_app"
        }
    ]
    assert result == expected

    # Test 2: Alternative field names
    records = [
        {
            "user_id": "user456",
            "action": "LOGOUT",
            "time": "2023-09-05 15:30"
        }
    ]
    result = transform_logs(records, "mobile_app")
    expected = [
        {
            "user_id": "user456",
            "activity": "logout",
            "timestamp": "2023-09-05T15:30:00Z",
            "source_system": "mobile_app"
        }
    ]
    assert result == expected

    # Test 3: Different field name variations
    records = [
        {
            "userid": "user789",
            "event": "PAGE_VIEW",
            "access_time": "09/05/2023 16:45:30"
        }
    ]
    result = transform_logs(records, "analytics")
    expected = [
        {
            "user_id": "user789",
            "activity": "page_view",
            "timestamp": "2023-09-05T16:45:30Z",
            "source_system": "analytics"
        }
    ]
    assert result == expected

    # Test 4: Missing fields - set to unknown
    records = [
        {
            "userId": "user101"
            # missing activity and timestamp
        }
    ]
    result = transform_logs(records, "test_system")
    expected = [
        {
            "user_id": "user101",
            "activity": "unknown",
            "timestamp": "unknown",
            "source_system": "test_system"
        }
    ]
    assert result == expected

    # Test 5: UNIX timestamp
    records = [
        {
            "userId": "user202",
            "activity": "PURCHASE",
            "timestamp": 1693922432
        }
    ]
    result = transform_logs(records, "ecommerce")
    expected_timestamp = datetime.fromtimestamp(1693922432, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    expected = [
        {
            "user_id": "user202",
            "activity": "purchase",
            "timestamp": expected_timestamp,
            "source_system": "ecommerce"
        }
    ]
    assert result == expected

    # Test 6: Invalid timestamp - should be set to unknown
    records = [
        {
            "userId": "user303",
            "activity": "ERROR",
            "timestamp": "not a valid date"
        }
    ]
    result = transform_logs(records, "error_system")
    expected = [
        {
            "user_id": "user303",
            "activity": "error",
            "timestamp": "unknown",
            "source_system": "error_system"
        }
    ]
    assert result == expected

    # Test 7: Corrupted record removal - both user_id and timestamp unknown
    records = [
        {
            "some_other_field": "value"
            # no userId, activity, or timestamp
        },
        {
            "userId": "valid_user",
            "activity": "VALID_ACTION",
            "timestamp": "2023-09-05 10:00"
        }
    ]
    result = transform_logs(records, "mixed_system")
    # First record should be dropped, only second record should remain
    expected = [
        {
            "user_id": "valid_user",
            "activity": "valid_action",
            "timestamp": "2023-09-05T10:00:00Z",
            "source_system": "mixed_system"
        }
    ]
    assert result == expected

    # Test 8: Multiple records with mixed scenarios
    records = [
        {
            "userId": "user001",
            "activity": "LOGIN",
            "timestamp": "2023-01-01 09:00:00"
        },
        {
            "user_id": "user002",
            "action": "CLICK",
            "time": "01/01/2023 10:30"
        },
        {
            "userid": "user003",
            "event": "SCROLL",
            "access_time": 1672574400  # Unix timestamp
        },
        {
            # corrupted record - should be removed
        }
    ]
    result = transform_logs(records, "comprehensive_test")
    expected = [
        {
            "user_id": "user001",
            "activity": "login",
            "timestamp": "2023-01-01T09:00:00Z",
            "source_system": "comprehensive_test"
        },
        {
            "user_id": "user002",
            "activity": "click",
            "timestamp": "2023-01-01T10:30:00Z",
            "source_system": "comprehensive_test"
        },
        {
            "user_id": "user003",
            "activity": "scroll",
            "timestamp": datetime.fromtimestamp(1672574400, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "source_system": "comprehensive_test"
        }
    ]
    assert result == expected

    # Test 9: Empty records list
    records = []
    result = transform_logs(records, "empty_system")
    assert result == []

    print("All transform_logs tests passed!")


test_convert_timestamp()
test_transform_logs()


