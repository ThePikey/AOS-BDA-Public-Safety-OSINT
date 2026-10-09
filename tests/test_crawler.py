import unittest
from src.bda_crawler_public import init_db, search_fcc_and_ahj, ingest_records, generate_llm_compliance_prompt

class TestBDAPublicCrawler(unittest.TestCase):
    def test_search_and_prompt(self):
        init_db("test_bda.db")
        records = search_fcc_and_ahj("Roseburg", "OR")
        self.assertGreater(len(records), 0)
        ingest_records(records, "test_bda.db")
        
        prompt = generate_llm_compliance_prompt(records[0])
        self.assertIn("PUBLIC SAFETY BDA AUDIT PROMPT", prompt)
        self.assertIn("Roseburg", prompt)

if __name__ == "__main__":
    unittest.main()
