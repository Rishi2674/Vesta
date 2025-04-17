import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from app.utils.groq_client_3 import groq_chat
from serpapi import GoogleSearch
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("SERP_API_KEY")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

    


def extract_google_links(query, num_links=3):
    params = {
        "engine": "google",
        "q": query,
        "api_key": API_KEY,  # Replace with env variable in prod
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    links = []
    if "organic_results" in results:
        for result in results["organic_results"]:
            link = result.get("link")
            if link:
                links.append(link)
            if len(links) >= num_links:
                break
    return links

def fetch_and_clean_text(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        page = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(page.text, "html.parser")
        # Remove scripts and styles
        for tag in soup(["script", "style", "noscript"]): tag.decompose()
        text = " ".join(chunk.strip() for chunk in soup.stripped_strings)
        return text[:3000]  # Limit to avoid prompt overflow
    except Exception as e:
        return ""

def web_search_summarizer_tool(user_input):
    # STEP 1: Use Groq to extract search query
    query_prompt = f"You are a helpful assistant. Given this user query: '{user_input}', convert it into a simple, concise Google search query.Just give the query."
    search_query = groq_chat(query_prompt).strip()
    print("Search Query",search_query)
    # STEP 2: Get top 2-3 URLs from Google
    urls = extract_google_links(search_query)
    print("Urls extracted",urls)
    if not urls:
        return "Couldn't find relevant results from web."

    # STEP 3: Fetch and clean content from each URL
    contents = [fetch_and_clean_text(url) for url in urls]
    combined_content = "\n\n".join(contents)
    # print("combined content",combined_content)

    # STEP 4: Summarise with Groq (include URLs in system prompt)
    source_text = "\n\n".join(f"Source: {url}" for url in urls)
    summarise_prompt = (
        f"You are a helpful assistant. Based on the following web content, provide a clear and concise answer "
        f"to this question: '{user_input}'. Also include the source URLs at the end for reference.\n\n"
        f"{combined_content}\n\n{source_text}"
    )
    final_summary = groq_chat(summarise_prompt).strip()
    return final_summary


# summary = web_search_summarizer_tool("State some tenancy laws in india.")
# print(summary)