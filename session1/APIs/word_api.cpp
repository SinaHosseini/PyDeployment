#include <iostream>
#include <curl/curl.h>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

size_t WriteCallback(void *contents, size_t size, size_t nmemb, std::string *buffer) {
    size_t totalSize = size * nmemb;
    buffer->append((char *)contents, totalSize);
    return totalSize;
}

int main() {
    std::string userText;
    std::cout << "Please enter your word: ";
    std::cin >> userText;

    std::string url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + userText;

    CURL *curl;
    CURLcode res;
    std::string response;

    curl = curl_easy_init();
    if (curl) {
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response);

        res = curl_easy_perform(curl);
        curl_easy_cleanup(curl);

        if (res != CURLE_OK) {
            std::cerr << "Failed to get data from the server: " << curl_easy_strerror(res) << std::endl;
            return 1;
        }
    }

    json data = json::parse(response);

    std::cout << data.dump(4) << std::endl;

    return 0;
}
