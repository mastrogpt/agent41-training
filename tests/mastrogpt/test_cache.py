import sys
sys.path.append("packages/mastrogpt/cache")
import os, cache as m

def test_cache():
    pref = os.getenv("REDIS_PREFIX")

    args = {}
    result = m.cache(args)
    assert result.get("output") == "Please provide a redis command."

    args = {"input": "PING"}
    result = m.cache(args)
    assert result.get("output")

    args = {"input": f"SET {pref}hello world"}
    result = m.cache(args)
    assert result.get("output") == 'True'

    args = {"input": f"GET {pref}hello"}
    result = m.cache(args)
    assert result.get("output") == "world"
    
    args = {"input": f"DEL {pref}hello"}
    result = m.cache(args)
    assert result.get("output") == "1"

    args = {"input": f"GET {pref}hello"}
    result = m.cache(args)
    assert result.get("output") == "None"
