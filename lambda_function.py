def lambda_handler(event, context):
    text = event.get('text', '')
    word_count = len(text.split())
    upper_text = text.upper()
    return { 'word_count': word_count, 'upper_text': upper_text }
