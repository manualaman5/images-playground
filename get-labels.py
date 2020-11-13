import os

def detect_labels(path):
    """Detects labels in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)
        
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    
    return labels

def save_metadata(img_name, directory, labels):
    img_name_f = img_name.split('.')[0]
    print(img_name_f)
    path2txt = os.path.join(directory, f'{img_name_f}.txt')
    print(path2txt)
    with open(path2txt, 'w') as f:
        f.write('Source image name:{}\n'.format(img_name))
        f.write('Directory:{}\n'.format(directory)) 
        f.write('Labels:\n')
        for l in labels:
            f.write(f'{l.description}\n')

    return 

if __name__ == '__main__':
    my_input_dir = '/home/alaman/codes/pic-converter/resources/source_images' 
    my_output_dir = '/home/alaman/codes/pic-converter/resources/outs' 
    my_img_name = 'cat.jpeg'

    path2img = os.path.join(my_input_dir, my_img_name)
    
    labels = detect_labels(path2img)
    save_metadata(my_img_name, my_output_dir, labels)
