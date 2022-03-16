class null(object):
  def __init__(self):
    self.version = "0.1b"
    self.language = [
      "python",
      "node.js",
      "HTML, CSS",
      "batch"
    ]
    
  def __str__(self) -> NoneType:
    return None
  
  @property
  def v(self):
    return self.v
  
  @property
  def lang(self):
    return self.language
  
  def call(script):
    if callable(script):
      script.__call__(None)
      
# null.py made by AWeirdScratcher lol
