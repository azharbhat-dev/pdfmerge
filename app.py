import os
from flask import Flask, request, render_template, send_file
import fitz

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def resize_and_merge_pdfs(pdf_list, output_path, target_size=(595, 842)):
    merged_pdf = fitz.open()
    for pdf_path in pdf_list:
        try:
            pdf = fitz.open(pdf_path)
            for page in pdf:
                original_rect = page.rect
                new_page = merged_pdf.new_page(width=target_size[0],
                                               height=target_size[1])
                scale = min(target_size[0] / original_rect.width,
                            target_size[1] / original_rect.height)
                new_width = original_rect.width * scale
                new_height = original_rect.height * scale
                x_offset = (target_size[0] - new_width) / 2
                y_offset = (target_size[1] - new_height) / 2
                target_rect = fitz.Rect(x_offset, y_offset,
                                        x_offset + new_width,
                                        y_offset + new_height)
                new_page.show_pdf_page(target_rect, pdf, page.number)
        except Exception as e:
            print(f"Error processing {pdf_path}: {e}")
    merged_pdf.save(output_path)

@app.route('/', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        files = request.files.getlist('pdf_files')
        if not files:
            return "No files selected", 400
        uploaded_pdf_paths = []
        for file in files:
            if file.filename.endswith('.pdf'):
                file_path = os.path.join(app.config['UPLOAD_FOLDER'],
                                         file.filename)
                file.save(file_path)
                uploaded_pdf_paths.append(file_path)
        output_pdf_path = os.path.join(app.config['UPLOAD_FOLDER'],
                                       'merged_output.pdf')
        resize_and_merge_pdfs(uploaded_pdf_paths, output_pdf_path)
        return send_file(output_pdf_path,
                         as_attachment=True,
                         download_name='merged_output.pdf')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
