import os
from mongoengine import *
from flask import *
import random
import mlab
mlab.connect()

app = Flask(__name__)

app.config["IMG_PATH"] = os.path.join(app.root_path, "images")

class Foody(Document):
    title = StringField()
    name = StringField()
    image = StringField()
    address = StringField()
    location1 = StringField()
    rating = FloatField()
    price = StringField()

sunsetsoda = Foody("sunsetsoda", "Sunset soda", "http://www.thenibble.com/reviews/main/cocktails/images/tequila-sunset-250.jpg","245/4 Nguyễn Trãi, Quận 1, Hồ Chí Minh", "https://www.google.com/maps/place/245%2F4+Nguy%E1%BB%85n+Tr%C3%A3i,+Nguy%E1%BB%85n+C%C6%B0+Trinh,+Qu%E1%BA%ADn+1,+H%E1%BB%93+Ch%C3%AD+Minh,+Vi%E1%BB%87t+Nam/@10.764489,106.6856232,17z/data=!3m1!4b1!4m5!3m4!1s0x31752f19d9a1c407:0xa15ba58fdc46f25d!8m2!3d10.764489!4d106.687811", 9.5, "$10")
sodatao = Foody("sodatao", "Soda Táo", "http://static1.bestie.vn/Mlog/ImageContent/201607/bestie-giam-tao-20160713105856.jpg", "331 Trần Bình Trọng, 4, Quận 5, Hồ Chí Minh", "https://www.google.com/maps/place/331+Tr%E1%BA%A7n+B%C3%ACnh+Tr%E1%BB%8Dng,+ph%C6%B0%E1%BB%9Dng+4,+Qu%E1%BA%ADn+5,+H%E1%BB%93+Ch%C3%AD+Minh,+Vi%E1%BB%87t+Nam/@10.763149,106.6766786,17z/data=!3m1!4b1!4m8!1m2!2m1!1zMzMxIFRy4bqnbiBCw6xuaCBUcuG7jW5nLCA0LCBRdeG6rW4gNSwgSOG7kyBDaMOtIE1pbmg!3m4!1s0x31752f1dd602e723:0xb841a8dd2a6bc1e4!8m2!3d10.7631437!4d106.6788673", 8.0, "$15")
trasuaphomaituoi = Foody("trasuaphomaituoi", "Trà sữa phô mai tươi", "https://tea-2.lozi.vn/v1/images/resized/tra-sua-pho-mai-tuoi-1467392556-336636-1467977242?w=320&type=s", "113 Phan Xích Long, phường 1, Quận Phú Nhuận, Hồ Chí Minh", "https://www.google.com/maps/place/113+Phan+X%C3%ADch+Long,+ph%C6%B0%E1%BB%9Dng+1,+Ph%C3%BA+Nhu%E1%BA%ADn,+H%E1%BB%93+Ch%C3%AD+Minh,+Vi%E1%BB%87t+Nam/@10.7990867,106.6842004,17z/data=!3m1!4b1!4m5!3m4!1s0x317528d046d7cd0d:0x3f3fc9431e041412!8m2!3d10.7990814!4d106.6863891", 7.0, "$15")
pizzahaisan = Foody("pizzahaisan", "Pizza hải sản", "http://img2.news.zing.vn/2012/05/22/combo.jpg", "151/2B Nguyễn Ảnh Thủ, Huyện Hóc Môn, Hồ Chí Minh", "https://www.google.com/maps/place/151%2F2B+Nguy%E1%BB%85n+%E1%BA%A2nh+Th%E1%BB%A7,+Trung+Ch%C3%A1nh,+T%C3%A2n+Xu%C3%A2n,+H%C3%B3c+M%C3%B4n,+H%E1%BB%93+Ch%C3%AD+Minh,+Vi%E1%BB%87t+Nam/@10.8579483,106.6065413,17z/data=!3m1!4b1!4m5!3m4!1s0x31752a3e4b99ff9b:0x1c2fb1e5953ff668!8m2!3d10.857943!4d106.60873", 8.0, "$10")
fruitteablueberry = Foody("fruitteablueberry", "Fruit Tea Blueberry", "https://d25dbtkkim974w.cloudfront.net/media/gallery/images/b/l/blueberry05124.jpg", "47/5F đường Song Hành, Huyện Hóc Môn, Hồ Chí Minh", "https://www.google.com/maps/place/47%2F5D+%C4%90%C6%B0%E1%BB%9Dng+Song+H%C3%A0nh+QL+22,+Trung+Ch%C3%A1nh,+T%C3%A2n+Xu%C3%A2n,+H%C3%B3c+M%C3%B4n,+H%E1%BB%93+Ch%C3%AD+Minh,+Vi%E1%BB%87t+Nam/@10.8603054,106.6041619,17z/data=!3m1!4b1!4m5!3m4!1s0x31752a1550bf79a1:0xc5ff85924db5ad7a!8m2!3d10.8603001!4d106.6063506", 8.5, "$15")
hongtrasuibot = Foody("hongtrasuibot", "Hồng trà sủi bọt", "http://store.bobapop.com.vn/resource/uploads/2016/09/03-hong-tra-sb-600x600.jpg", "485 Sư Vạn Hạnh, phường 9, Quận 10, Hồ Chí Minh", "https://www.google.com/maps/place/485+S%C6%B0+V%E1%BA%A1n+H%E1%BA%A1nh,+ph%C6%B0%E1%BB%9Dng+9,+Qu%E1%BA%ADn+10,+H%E1%BB%93+Ch%C3%AD+Minh,+Vi%E1%BB%87t+Nam/@10.7688842,106.6687002,17z/data=!3m1!4b1!4m5!3m4!1s0x31752ede1cbfe961:0x55bfe8ab97303d83!8m2!3d10.7688789!4d106.6708889", 7.5, "$20")
trasua = Foody("trasua", "Trà sữa", "https://s-media-cache-ak0.pinimg.com/originals/f2/d1/96/f2d196363da420e1212d74e2553a71f3.jpg", "98-126 Nguyễn Tri Phương, Phường 7, Quận 5, Hồ Chí Minh", "https://www.google.com/maps/place/98-%3E126+Nguy%E1%BB%85n+Tri+Ph%C6%B0%C6%A1ng,+Ph%C6%B0%E1%BB%9Dng+7,+Qu%E1%BA%ADn+5,+H%E1%BB%93+Ch%C3%AD+Minh,+Vi%E1%BB%87t+Nam/@10.7540384,106.6675623,17z/data=!3m1!4b1!4m5!3m4!1s0x31752efbf2b7d7b9:0x4474da772512a3f1!8m2!3d10.7540331!4d106.669751", 7.5, "$15")
laukem = Foody("laukem", "Lẩu kem", "http://muare1.vcmedia.vn/images/2013/07/06/mr_330695_85b505ad0d7abd7c.png", "6A Trần Hưng Đạo, Phạm Ngũ Lão, Quận 1, Hồ Chí Minh", "https://www.google.com/maps/place/6A+Tr%E1%BA%A7n+H%C6%B0ng+%C4%90%E1%BA%A1o,+Ph%E1%BA%A1m+Ng%C5%A9+L%C3%A3o,+Qu%E1%BA%ADn+1,+H%E1%BB%93+Ch%C3%AD+Minh,+Vi%E1%BB%87t+Nam/@10.7693412,106.6940223,17z/data=!3m1!4b1!4m5!3m4!1s0x31752f3e4f599229:0xfa8397214daa9999!8m2!3d10.7693359!4d106.696211", 8, "$20")
#
sunsetsoda.save()
sodatao.save()
trasuaphomaituoi.save()
pizzahaisan.save()
fruitteablueberry.save()
hongtrasuibot.save()
trasua.save()
laukem.save()

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/product', methods=["GET", "POST"])
# def product():
#     productuser=[]
#     if request.method == "GET":
#         productrandom = []
#         while len(productrandom) <= 2:
#             item = random.choice(Foody.objects)
#             if item not in productrandom:
#                 productrandom.append(item)
#                 productuser.append(item)
#             return render_template("product.html", foodys = productrandom)
#         # if request.method == "POST":
        #     productrandom = []
        #     while len(productrandom) <= 2:
        #         item = random.choice(Foody.objects)
        #         if item not in productuser:
        #             if item not in productrandom:
        #                 productrandom.append(item)
        #                 productuser.append(item)
        #         if len(productuser) <= len(Foody.objects):
        #             for i in productuser:
        #                 productuser.remove(i)
        #                 continue
        #     return render_template("product.html", foodys = productrandom)


@app.route('/product')
def product():
    productused = []
    productrandom = []
    while len(productrandom) <= 7:
        item = random.choice(Foody.objects)
        if item not in productrandom:
            productrandom.append(item)
            productused.append(item)

    # return render_template("product.html", foodys=Foody.objects())
    return render_template("product.html", foodys=productrandom)
    # return render_template("product.html", foody = Foody.objects().with_index[product_index])

@app.route('/productdetail/<int:product_item>')
def productdetail(product_item):
    return render_template("productdetail.html", foody=Foody.objects()[product_item])


if __name__ == '__main__':
    app.run()
