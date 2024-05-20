import requests
from bs4 import BeautifulSoup
import os


def save_wiki_content_as_text(page_url, directory, filename):
    # Send a GET request to the Wikipedia page
    response = requests.get(page_url)

    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract text from the <p> tags (paragraphs)
    text_content = '\n'.join(p.get_text() for p in soup.find_all('p'))

    # Save the extracted text to a file
    with open(os.path.join(directory, filename), 'w', encoding='utf-8') as file:
        file.write(text_content)
    print(f"Content saved to {filename}")


if __name__ == "__main__":
    counties = ["Alameda County", "Alpine County", "Amador County", "Butte County", "Calaveras County", "Colusa County",
                "Contra Costa County", "Del Norte County", "El Dorado County", "Fresno County", "Glenn County",
                "Humboldt County", "Imperial County", "Inyo County", "Kern County", "Kings County", "Lake County",
                "Lassen County", "Los Angeles County", "Madera County", "Marin County", "Mariposa County",
                "Mendocino County", "Merced County", "Modoc County", "Mono County", "Monterey County", "Napa County",
                "Nevada County", "Orange County", "Placer County", "Plumas County", "Riverside County",
                "Sacramento County", "San Benito County", "San Bernardino County", "San Diego County",
                "San Francisco County", "San Joaquin County", "San Luis Obispo County", "San Mateo County",
                "Santa Barbara County", "Santa Clara County", "Santa Cruz County", "Shasta County", "Sierra County",
                "Siskiyou County", "Solano County", "Sonoma County", "Stanislaus County", "Sutter County",
                "Tehama County", "Trinity County", "Tulare County", "Tuolumne County", "Ventura County", "Yolo County",
                "Yuba County"]

    dir_ = "/Users/laurenfernandes/Documents/PersonalProject/RAG_langchain/data_counties"

    for county in counties:
        county_modified = county.replace(" ", "_")
        page_link = f"https://en.wikipedia.org/wiki/{county_modified}/_California"
        save_wiki_content_as_text(page_link, dir_, county_modified + ".txt")
