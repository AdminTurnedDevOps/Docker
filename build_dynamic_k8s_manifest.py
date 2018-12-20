import json
import os
import sys


def k8s_manifest(*kwargs):
    template = """apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: {name}
    spec:
      selector:
        matchLabels:
          app: nginx
      replicas: 2
      template:
        metadata:
          labels:
            app: nginx
        spec:
          containers:
          - name: {name}
            image: {image}
            ports:
            - containerPort: 80
    """

    K8s_manifest = template.format(name=name, image=image)
    print(K8s_manifest)

    yaml_file = os.path.isfile("{}/manifest.yaml").format(file_path)

    if yaml_file:
        os.system("rm -rf {}/manifest.yaml").format(file_path)
        os.system("touch {}/manifest.yaml").format(file_path)

        with open("{}/manifest.yaml", "w").format(file_path) as f:
            f.write(K8s_manifest)
    else:
        os.system("touch {}/manifest.yaml").format(file_path)

        with open("{}/manifest.yaml", "w").format(file_path) as f:
            f.write(K8s_manifest)


name = sys.argv[1]
image = sys.argv[2]
file_path = sys.argv[3]

if __name__ == '__main__'
    k8s_manifest(name, image, file_path)
