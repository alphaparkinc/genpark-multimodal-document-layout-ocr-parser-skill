from client import MultimodalDocumentLayoutOcrParserClient

def main():
    client = MultimodalDocumentLayoutOcrParserClient()
    res = client.parse_document_layout("https://example.com/invoice.pdf", 300)
    print(f"Extracted Tables: {res['extracted_tables_count']}")
    print("Parsed Markdown:")
    print(res["parsed_markdown"])

if __name__ == "__main__":
    main()
