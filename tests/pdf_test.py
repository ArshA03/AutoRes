import rendercv.data.generator as generator
import rendercv.data.reader as reader

import rendercv.renderer.renderer as renderer
from pathlib import Path

# generator.create_a_sample_yaml_input_file(input_file_path=Path("sample_input2.yaml"))

model = reader.read_input_file(file_path_or_contents=Path("ash_resume.yaml"))

renderer.create_a_latex_file(rendercv_data_model=model, output_directory=Path("output"))

renderer.render_a_pdf_from_latex(latex_file_path=Path("output/Ash_Afshar_CV.tex"))