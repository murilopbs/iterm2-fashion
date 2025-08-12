import os

class PhotoUtil:
    def __init__(self):
        pwd = os.getcwd()
        self.dir = pwd + '/photos'

    def list_all_photo_dir(self):
        photos = os.listdir(self.dir)

    def list_all_photos(self):
        photos = self.list_all_dir()
        image_photo = []
        for photo in photos:
            if photo.endswith(('.jpg', '.png')):
                image_photo.append(self.absolute_path(photo))
        return image_photo
    
    def absolute_path(self, file_name):
        full_path = self.dir + '/' + file_name
        return full_path

    def get_first_image(self):
        photos = self.list_all_photo_dir()
        if not photos:
            return None
        return self.absolute_path(photo[0])

