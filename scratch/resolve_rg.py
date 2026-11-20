import urllib.request

url = 'https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnDeJtBgewcvmfWUs-NmTh2uOe0nuM2Jm9UNKI-clLz9gcy9T2wEu7L9f3YAelDPBuxN_4kSKgyy7kVs3lO7cRxdF6dxg6tCVGHwOt2ZHPOX66reoESkcxRXU8sP0_q6Igv2pCcogpwrjzVPlJP6SN4Z93pA7Lib4h5u8pPc2cT5wz64X7dkBQpDNumuWRv6rcxLtXR_REp9MQ5XVnlDubOl09eannY3acOkg-r6bepi3nWaq2Ls6DbQQABtdTuJcTt7CVceg47P1l0VVfZrwLGfYGWQtnVsu_f6CqiBxmyR5HiSVConctSUzkXuQ='
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        print("Final URL:", resp.geturl())
except Exception as e:
    print("Error:", e)

