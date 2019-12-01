from flask import Flask, json

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)

@api.route('/login', methods=['POST'])
def login():
  return json.dumps({"msg":"logged in"})

@api.route('/logout', methods=['POST'])
def logout():
  return json.dumps({"msg":"logged out"})

@api.route('/sampleGetApi', methods=['GET'])
def sample_get_api():
  return json.dumps({"msg":"hello from GET API"})

@api.route('/samplePostApi', methods=['POST'])
def sample_post_api():
  return json.dumps({"msg":"hello from POST API"})

if __name__ == '__main__':
    api.run()