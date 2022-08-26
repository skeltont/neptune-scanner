import inspect


def filter_data(cls, data):
  return {
      k: v for k, v in data.items()
      if k in inspect.signature(cls).parameters
  }
