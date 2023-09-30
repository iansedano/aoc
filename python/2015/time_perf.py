from datetime import timedelta
from time import perf_counter_ns


def time_perf(func, arg):
    start = perf_counter_ns()
    result = func(arg)
    end = perf_counter_ns()
    return result, format_dynamic_timedelta(end - start)

def format_dynamic_timedelta(nanoseconds):
    if nanoseconds >= 60 * 1e9:  # Over a minute
        minutes, remainder = divmod(nanoseconds, 60 * 1e9)
        seconds = remainder // 1e9
        return f"{int(minutes)}m{int(seconds)}s"
    elif nanoseconds >= 1e9:  # Over a second
        seconds, remainder = divmod(nanoseconds, 1e9)
        return f"{int(seconds)}s"
    elif nanoseconds >= 1e6:  # Over a millisecond
        milliseconds = nanoseconds // 1e6
        return f"{int(milliseconds)}ms"
    elif nanoseconds >= 1e3:  # Over a microsecond
        microseconds = nanoseconds // 1e3
        return f"{int(microseconds)}µs"
    else:  # Less than a microsecond
        return "less than 1µs"
