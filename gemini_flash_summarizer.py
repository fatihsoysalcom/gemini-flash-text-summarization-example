import google.generativeai as genai
import os

# Configure the Generative AI client with your API key.
# It's recommended to set this as an environment variable.
# export GOOGLE_API_KEY='YOUR_API_KEY'

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

def summarize_text(long_text):
    """Summarizes a given long text using Gemini 3.5 Flash.

    Args:
        long_text: The input text to be summarized.

    Returns:
        A string containing the summarized text.
    """
    # Initialize the Gemini 3.5 Flash model.
    # 'gemini-3.5-flash' is chosen for its speed and efficiency.
    model = genai.GenerativeModel('gemini-3.5-flash')

    # Define the prompt for summarization.
    # This prompt instructs the model to provide a concise summary.
    prompt = f"Aşağıdaki metni özetle:\n\n{long_text}"

    try:
        # Generate content using the model.
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Example long text to be summarized.
    # This text is a placeholder and should be replaced with actual content.
    example_text = (
        "Yapay zeka modellerinin hızla geliştiği bu dönemde, geliştiricilerin en güncel ve güçlü araçlara hakim olması kritik önem taşıyor. "
        "Google'ın sunduğu Gemini 3.5 Flash, özellikle hız ve verimlilik odaklı uygulamalar geliştirmek isteyenler için dikkat çekici bir seçenek olarak öne çıkıyor. "
        "Peki, Gemini 3.5 Flash tam olarak nedir ve geliştiriciler bu yenilikçi modeli projelerinde nasıl etkili bir şekilde kullanabilir? "
        "Bu rehberde, Gemini 3.5 Flash'ın temel özelliklerinden başlayarak, pratik uygulama örneklerine ve ileri düzey optimizasyon tekniklerine kadar her şeyi adım adım inceleyeceğiz. "
        "Amacımız, bu güçlü yapay zeka modelini kullanarak daha akıllı, daha hızlı ve daha kullanıcı dostu uygulamalar geliştirmenize yardımcı olmak."
    )

    print("Orijinal Metin:")
    print(example_text)
    print("\n--------------------\n")

    # Call the summarize_text function and print the result.
    summary = summarize_text(example_text)
    print("Özetlenmiş Metin:")
    print(summary)
