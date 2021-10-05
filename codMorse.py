#Mensagem em código Morse
#Para que o código funcione a posição das letras da lista morse devem corresponder a posição das letras da lista Alfabeto! 
morse = [".- ","-... ","-,-, ","-.. ",". ","..-. ","--. ",".... ",".. ",".--- ","-.- ",\
    ".-.. ","-- ","-. ","--- ",".--. ","--.- ",".-. ","... ","- ","..- ","...- ",".-- ","-..- ","-.-- ","--.. ","  "]
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

palavra_morse = ''
palavra = input("Digite uma palavra ou frase para ser traduzida para código morse: ").lower()
palavra_separada = list(palavra)

tamanho = len(palavra_separada)                 #Acha quantas letras tem na frase, contando a partir do 0
tamanho = tamanho - 1                           #Começa a contar a partir do zero.
x = 0

while(x <= tamanho):                            #percorre todas as letras da palavra de entrada e encontrando a posição de cada uma na lista "alfabeto"
    posicao = alfabeto.index(palavra_separada[x])
    #print(posicao)                             #Mostra a posição da letra na lista alfabeto
    
    letra_morse = morse[posicao]                #Letra em morse com a mesma posição da letra em alfabeto. 
    palavra_morse = palavra_morse + letra_morse #A cada loop uma letra da palavra é adicionada
    x = x + 1                                   # Faz com que x percorra todas as letras da palavra/frase
print(palavra_morse)