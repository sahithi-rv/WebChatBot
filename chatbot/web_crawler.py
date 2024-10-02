import requests
from bs4 import BeautifulSoup
import html2text


def get_data_from_website(url):
    """
    Retrieve text content and metadata from a given URL.

    Args:
        url (str): The URL to fetch content from.

    Returns:
        tuple: A tuple containing the text content (str) and metadata (dict).
    """
    # Get response from the server
    response = requests.get(url)
    if response.status_code == 500:
        print("Server error")
        return
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Removing js and css code
    for script in soup(["script", "style"]):
        script.extract()

    # Extract text in markdown format
    html = str(soup)
    html2text_instance = html2text.HTML2Text()
    html2text_instance.images_to_alt = True
    html2text_instance.body_width = 0
    html2text_instance.single_line_break = True
    text = html2text_instance.handle(html)

    # Extract page metadata
    print(url)
    try:
        page_title = soup.title.string.strip()
    except:
        page_title = url.path[1:].replace("/", "-")
    meta_description = soup.find("meta", attrs={"name": "description"})
    meta_keywords = soup.find("meta", attrs={"name": "keywords"})
    if meta_description:
        description = meta_description.get("content")
    else:
        description = page_title
    if meta_keywords:
        meta_keywords = meta_description.get("content")
    else:
        meta_keywords = ""

    metadata = {'title': page_title,
                'url': url,
                'description': description,
                'keywords': meta_keywords}

    return text, metadata

import requests
from bs4 import BeautifulSoup

def get_urls_from_website(head_url):
    """
    Extracts blog category, URL, and title from a website's HTML.

    Args:
        head_url (str): The URL of the website containing the blog list.

    Returns:
        list: A list of dictionaries, where each dictionary represents a blog
              with keys 'category', 'url', and 'title'.
    """

    response = requests.get(head_url)
    soup = BeautifulSoup(response.content, 'html.parser')  # Use 'html.parser' for best compatibility

    blogs = []
    for blog_item in soup.find_all('div', class_='JMCi2v blog-post-homepage-link-hashtag-hover-color so9KdE lyd6fK I5nSmk'):
        blog = {}

        # Extract category
        #category_link = blog_item.find_previous_sibling('div', class_='CS4xCt JGhsWK')
        #if category_link:
        #    category_anchor = category_link.find('a')
        #    blog['category'] = category_anchor.text.strip() if category_anchor else None

        # Extract URL
        url_anchor = blog_item.find('a', class_='O16KGI pu51Xe lyd6fK mqysW5 has-custom-focus i6wKmL')
        if url_anchor:
            blog['url'] = url_anchor['href']

        # Extract title
        title_element = blog_item.find('div', class_='FbwBsX blog-post-title-font lyd6fK mqysW5 HhgCcE')
        if title_element:
            title_p = title_element.find('p', class_='bD0vt9 KNiaIk')
            blog['title'] = title_p.text.strip() if title_p else None

        blogs.append(blog)

    return blogs

head_url = 'https://www.anaadi.org/blog/page/6'  
blogs = get_urls_from_website(head_url)

for blog in blogs:
    #print(f"Category: {blog.get('category')}")
    print(f"URL: {blog.get('url')}")
    print(f"Title: {blog.get('title')}")
    print("---")