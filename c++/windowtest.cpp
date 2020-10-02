#include <SFML/Window.hpp>
#include <SFML/Window/ContextSettings.hpp>
#include <SFML/Window/Event.hpp>
#include <SFML/Window/VideoMode.hpp>

int main() {
    sf::ContextSettings settings;
    settings.depthBits = 24;
    settings.stencilBits = 8;
    settings.majorVersion = 4;
    settings.minorVersion = 6;
    settings.attributeFlags = sf::ContextSettings::Core;

    sf::Window window(sf::VideoMode(800, 600), "OpenGL IsThisTheTitle?", sf::Style::Close, settings);

    // Event loop
    bool running = true;

    while (running){
        sf::Event windowEvent;
        while (window.pollEvent(windowEvent)){
            switch (windowEvent.type){
            case sf::Event::Closed:
                running = false;
                break;
            }
        }
    }


    return 0;
}
