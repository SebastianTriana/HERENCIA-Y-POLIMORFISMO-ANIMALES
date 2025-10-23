#  Ejercicio de Herencia y Polimorfismo en Python

**Autor:** Sebastian Triana  

Este proyecto es un ejemplo práctico de **herencia y polimorfismo** en Python, utilizando una jerarquía de clases que representan diferentes tipos de animales.  
A través de este ejercicio se demuestra cómo las subclases pueden heredar atributos y métodos de una clase base, además de redefinir su comportamiento mediante el polimorfismo.

---

##  Descripción del código

El programa define una clase base llamada `Animal` y dos subclases: `raton` y `panda`.  
Cada subclase hereda los atributos y métodos de `Animal`, pero sobrescribe algunos comportamientos para representar acciones y características propias de cada especie.

---

##  Clases y métodos

### **Clase `Animal`**
Representa la clase base.  
**Atributos:**
- `especie`: tipo de animal.  
- `edad`: edad del animal.  
- `nombre`: nombre del animal.  

**Métodos:**
- `hablar()`: método genérico (vacío en la clase base).  
- `moverse()`: método genérico (vacío en la clase base).  
- `describir()`: imprime el tipo de clase del animal.

---

### **Clase `raton` (hereda de `Animal`)**
Representa un ratón (por ejemplo, Mickey Mouse).  
**Métodos sobrescritos:**
- `hablar()`: imprime un mensaje característico del ratón.  
- `moverse()`: describe cómo se desplaza el ratón.

---

### **Clase `panda` (hereda de `Animal`)**
Representa un panda (por ejemplo, Po de *Kung Fu Panda*).  
**Atributos adicionales:**
- `guerrero_dragon`: indica si el panda es el Guerrero Dragón o no.  

**Métodos sobrescritos y nuevos:**
- `hablar()`: imprime una frase propia del personaje.  
- `moverse()`: describe cómo se mueve el panda.  
- `guerrero()`: indica si el panda es el Guerrero Dragón.

---

##  Conceptos aplicados

- **Herencia:** Las clases `raton` y `panda` heredan de la clase `Animal`.  
- **Polimorfismo:** Cada clase redefine los métodos `hablar()` y `moverse()` para comportarse de manera diferente.  
- **Encapsulación:** Los atributos se definen dentro del constructor `__init__`.  
- **Reutilización de código:** Se usa `super()` para reutilizar la inicialización de la clase base.

---

##  Ejecución del programa

<img width="328" height="155" alt="image" src="https://github.com/user-attachments/assets/1d49eada-98ff-497b-9dae-768ad3b826cc" />
<img width="264" height="172" alt="image" src="https://github.com/user-attachments/assets/d1f8e26f-1787-4246-ad73-cd8c4e3a3d04" />
