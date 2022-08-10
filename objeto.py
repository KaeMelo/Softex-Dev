class cadeira:
  pernas = 4
  tamanho = [40.0, 90.0]
  altura = 50.0 
  pesoSuportado = 140.0
  montada = False
  
  def montar(self):
    if self.montada:
      print("A cadeira já está montada. ")
    else:
      print("Montando cadeira. ")
      
    def mexer(self):
      print("Mexendo. ")
      
    def desmontar(self):
      print("Desmontando cadeira. ")
      
class televisão:
  tamanho = 120.0
  altura = 77.0 
  hz = 120
  
  def ligar(self):
    print("Ligando televisão. ")
    
  def desligar(self):
    print("Desligando televisão. ")
  
  def canal(self):
    print("Mudando canal. ")
    
class foto:
  tamanho = 330
  qualidade = 11.7
  megapixels = 36
  
  def tirarFoto(self):
    print("Foto tirada com sucesso.")
