import os
import shutil
from tqdm import tqdm
def move_image(start, end, report_folder, images_folder, resulting_folder, ignore_list):
    all_image_file_names = []
    for file_name in os.listdir(images_folder):
        if "CXR" in file_name and "1001.png" in file_name and int(file_name.split("_")[0][3:]) not in ignore_list:
            all_image_file_names.append((int(file_name.split("_")[0][3:]), file_name))
    all_image_file_names = sorted(all_image_file_names)

    for i, image_file_name in tqdm(all_image_file_names[start:end]):
        # moving reports
        current_xml_path = os.path.join(report_folder, f"{i}.xml")
        final_xml_path = os.path.join(resulting_folder, "reports", f"{i}.xml")
        shutil.copy(current_xml_path, final_xml_path)

        # moving images
        current_image_path = os.path.join(images_folder, image_file_name)
        final_image_path = os.path.join(resulting_folder, "images", f"{i}.png")
        shutil.copy(current_image_path, final_image_path)

if __name__ == "__main__":
    # place script on the same level as ecgen-radiology
    report_folder = "ecgen-radiology"
    images_folder = "images"
    resulting_folder = "data_subset"
    
    # These images are have ambiguous file paths and not frontal views 
    ignore_list =  [10, 17, 50, 62, 92, 98, 123, 124, 152, 154, 194, 195, 202, 227, 229, 237, 284, 285, 287, 340, 380, 386, 403, 412]
    if not os.path.exists(os.path.join(resulting_folder, "reports")):
        os.mkdir(os.path.join(resulting_folder, "reports"))
    if not os.path.exists(os.path.join(resulting_folder, "images")):
        os.mkdir(os.path.join(resulting_folder, "images"))
    move_image(2,302, report_folder, images_folder, resulting_folder, ignore_list)


