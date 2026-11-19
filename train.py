import yaml
p = yaml.safe_load(open("params.yaml"))
open("metrics.json", "w").write('{"score": %s}' % (p["lr"] * 10))


