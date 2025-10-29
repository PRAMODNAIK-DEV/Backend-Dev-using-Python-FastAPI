interface Father{
    public int mobile = 1234567890;
    void show();
}

interface Mother{
    public int mobile = 1234567890;
    void show();
}

class Animal implements Father, Mother{
    Animal(){
        System.out.println("Animal Constructor");
    }

    void show(){
        System.out.println("Mobile Number: " + mobile);
    }
}

class Dog extends Animal{
    super();
}

