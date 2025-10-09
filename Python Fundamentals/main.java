interface Pramod{
    public int mobile = 1234567890;
    void show();
}

interface Prajwal{
    public int mobile = 1234567890;
    void show();
}

class Animal implements Pramod, Prajwal{
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

