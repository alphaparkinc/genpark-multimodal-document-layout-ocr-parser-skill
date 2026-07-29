class MultimodalDocumentLayoutOcrParserClient:
    def parse_document_layout(self, document_url: str, dpi: int = 300) -> dict:
        md = "# Parsed Document\n\nExtracted content from invoice\n\n| Column A | Column B |\n| --- | --- |\n| Val 1 | Val 2 |"
        return {
            "parsed_markdown": md,
            "extracted_tables_count": 1
        }
