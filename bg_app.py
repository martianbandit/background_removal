import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(layout="wide", page_title="Supprime Arriere-plan")

st.write("## Cet outils supprime l'arrière plan d'une image que vous telecharger")
st.write(
    """:dog: Essayez de telecharger une image pour voir l’arriere-plan supprimer comme par magie. Des images en pleine qualite peuvent être téléchargees 
    à partir de la barre laterale. remerciments a la [bibliotheque rembg ](https://github.com/danielgatis/rembg) :grin:"""
)
st.sidebar.write("## Upload et download :gear:")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write(" Image Original :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Image sans arrière plan :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("telecharger votre image sans arriere plan", convert_image(fixed), "fixed.png", "image/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("telecharger une image depuis votre ordinateur:", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("Le fichier telecharger est trop volumineux. Veuillez telecharger une image inferieure à 5 Mo.")
    else:
        fix_image(upload=my_upload)
else:
    fix_image("./LE CATS MALIN.png"
