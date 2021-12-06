# mbti-tweet-analysis

## LIVE APP
https://mbti-app.azurefd.net

Projekt czteroosobowy realizowany w semestrze 2021Z w ramach przedmiotu Wprowadzenie do aplikacji i rozwiązań opartych o Sztuczną Inteligencję i Microsoft Azure.  

Celem projektu było stworzenie modelu klasyfikującego typ osobowości MBTI na podstawie krótkich wypowiedzi z serwisów społecznościowych oraz utworzenie prostej aplikacji webowej umożliwiającej korzystanie z modelu użytkownikowi.

## Diagram rozwiązania
![Diagram](https://raw.githubusercontent.com/gubapatryk/mbti-tweet-analysis/master/diagram.png)

## Film z demo działania rozwiązania

[![Film](https://img.youtube.com/vi/yuXHhs27Xmw/0.jpg)](https://www.youtube.com/watch?v=yuXHhs27Xmw)  

## Zespół
[Patryk Guba](https://github.com/gubapatryk)  
[Joanna Koła](https://github.com/Jannixen)   
[Maxymilian Kowalski](https://github.com/maxxx958)  
[Monika Kusiak](https://github.com/KitsunesWrath)

## Opis funkcjonalności

Po wprowadzeniu krótkiej wypowiedzi tekstowej do aplikacji webowej, użytkownik dostaje informację o najbardziej pasującym typie osobowości MBTI do wprowadzonej wiadomości.

## Schemat działania

Po wprowadzeniu wiadomości, tekst jest przekazywany do modelu, który dokonuje wektoryzacji wiadomości, a następnie klasyfikacji na podstawie modelu utworzonego z wykorzystaniem tf-df oraz xgboost na podstawie danych - postów pochodzących z serwisu Twitter z przypisanymi osobowościami MBTI. Następnie użytkownikowi zwracany jest przyporządkowany typ MBTI w interfejsie aplikacji webowej.

## Stos technologiczny

 - Azure Machine Learning - tworzenie modelu klasyfikującego 
 - Azure Web App - aplikacja webowa
 - Azure Front Door - zabezpieczenie aplikacji webowej przed atakami czy nadużyciami
 - Azure Container Instances - środowisko uruchomieniowe modelu w pierwotnej wersji
 - Linux App Service - środowisko uruchomieniowe modelu oraz aplikacji webowej (zastąpiło podejście z Azure Container Instances w finalnej wersji)
 - xgboost - biblioteka open source oparta na gradientowym podbijaniu (ang. gradient boosting) drzew klasyfikujących
