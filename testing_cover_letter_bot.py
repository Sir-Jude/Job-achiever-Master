import openai
from unittest import mock
from cover_letter_bot import generate_cover_letter, save_cover_letter_as_txt, save_cover_letter_as_pdf

openai.api_key = "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"

def test_generate_cover_letter():
    mock_response = {
        'choices': [{'message': {'content': 'Sample cover letter'}, 'finish_reason': 'stop', 'index': 0}],
    }

    with mock.patch('openai.ChatCompletion.create') as mock_create:
        mock_create.return_value = mock_response

        cover_letter = generate_cover_letter("John Doe", "ABC Company", "Jane Smith", "25", "Software Engineer", "5 years of experience", "English")

    assert cover_letter == "Sample cover letter"

def test_save_cover_letter_as_txt(tmpdir):
    cover_letter = "Sample cover letter"
    filename = str(tmpdir.join("cover_letter.txt"))
    save_cover_letter_as_txt(cover_letter, filename)

    with open(filename, 'r') as f:
        saved_content = f.read()

    assert saved_content == cover_letter

def test_save_cover_letter_as_pdf(tmpdir):
    cover_letter = "Sample cover letter"
    filename = str(tmpdir.join("cover_letter.pdf"))
    save_cover_letter_as_pdf(cover_letter, filename)

    assert tmpdir.join("cover_letter.pdf").exists()