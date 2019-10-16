# Twitter-Datos

Para extraer datos de usuarios de la red social Twitter se requiere : 

# Recursos 
  Tweepy : Dependecia de Python utilizada para accedera la API de Twitter
     Nota : Instalar Tweepy
  
  Estrutura 
  
    Import Tweety 
    
    Autenticación: 
     --- credenciales 
    
    api = tweepy.API (auth) se llama al metodo pasandole como parametro la autenticación previa realizada, 
    para asi empezar a obtener la informacion de los usurios.     
# Pasos: 

 1. Autenticación: Twitter utiliza el protocolo Oauth 2.0 por motivos de seguridad , por tanto  para obtener la autenticación es 
 necesaria la creación de una Aplicación de Twitter ( apps.twitter.com) , dado que esta nos permitira usar la API de twitter para asi 
 obtener los datos de los usuarios . ahora al crear la aplicacion se va a proporcionar cuatro credenciales ( Consumer Key , Consumer 
 Secret , Access Token , Access Token Secret) las cuales sirven basicamente para realizar este paso. 
 
 2. Utilizar a la API de twitter por medio de requerimientos, esto se hace a través de un HTTP request en el cual se definira lo que 
 se desea obtener esto reflejado en los parametros del body del requerimiento.
 
 3. Se estable la ruta ('/') y la manera en que el usuario interactua y visualiza la app
 
 4. Utiliza el metodo GET , el cual sirve para obtener la información del ususrio sumistrado. 
