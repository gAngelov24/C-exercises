#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;

class Animals{
public:
    int size;
    string color;
    Animals(){
        size = 0;
        color = "N/A";
    }
    Animals(int size, string color){
        this->size = size;
        this->color = color;
    }
    void sound(){
        cout << "Animals make many sounds: " << endl;
    }
    void attributes(){
        cout << "This is an animal with size " << size << " and color " << color << endl;
    }
};
class Cow : public Animals{
public:
    Cow(int size , string color){
        this->size = size;
        this->color = color;
    }
    void sound(){
        cout << "A cow goes mooooo" << endl;
    }
    void attributes(){
        cout << "This animal is a Cow with size " << size << " and color " << color << endl;
    }
};

//Class bird dirived from Animals
class Bird : public Animals{
    public:
    int wingspan;
    int weight;
    void attributes();
    void sound();
    Bird(){
        wingspan = 0;
        weight = 0;
    }
    Bird(int wingS, double weight);
};
Bird::Bird(int wingS, double weight){
    wingspan = wingS;
    this->weight = weight;
}
void Bird::attributes(){
    cout << "This animal is a bird with wingspan " << wingspan << " and weight " << weight << endl;
}
void Bird::sound(){
    cout << "A bird goes KAKAWW" << endl;
}

class Eagle : public Bird{
    int height;
    string type;
    public:
    void attributes();
    Eagle(int hgt, string type){
        height = hgt;
        this->type = type;
    }
    Eagle(const Eagle& eag){
        height = eag.height;
        type = eag.type;
    }
    int getHeight(){
        return height;
    }
    string getType(){
        return type;
    }
};
void Eagle::attributes(){
    if(type == "bald eagle"){
        cout << "RAWWWWW MERICA BABY!!!!!" << endl;
    } else {
        cout << "This is a " << type << " eagle with a height of " << height << endl;
    }
}

int main()
{
    cout << "Hello World!" << endl;
    Eagle baldE(10, "bald eagle");
    baldE.attributes();
    cout << "This eagle has height " << baldE.getHeight() << endl;
    Eagle eagle(5, "Stupid");
    eagle.attributes();
    Eagle copy(baldE);
    copy.attributes();
    cout << "This copy has height " << copy.getHeight() << endl;

    /*Animals animal;
    animal.attributes();
    animal.sound();
    Animals animal2(5, "pink");
    animal2.attributes();
    animal2.sound();
    Cow cow1(100, "Black and white");
    cow1.attributes();
    cow1.sound();
    Cow cow2(300, "black and white");
    cow2.attributes();
    cow2.sound();
    Bird bird;
    bird.attributes();
    bird.sound();
    Bird bird2(10, 0.5);
    bird2.attributes();
    bird2.sound(); */
    
    return 0;
}