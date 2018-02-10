import docker

from flask import Flask, render_template

app = Flask(__name__)

image_list=[]

@app.route("/")
def docker_client():
    client = docker.from_env()

    for image in client.images.list():
        if image not in image_list:
            image1=str(image)
            image_list.append(image1.split(":")[1].split("\'")[1])


    return render_template('template.html',
    image_list=image_list
    )


if __name__ == "__main__":
    app.run(port=7000)
