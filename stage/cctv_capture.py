import cv2

# Adresse IP de la caméra IP
url = 'rtsp://adresse-ip-de-la-camera'

# Capture du flux vidéo
cap = cv2.VideoCapture(url)

# Boucle de lecture du flux vidéo
while(cap.isOpened()):
    # Lecture d'une image du flux vidéo
    ret, frame = cap.read()
    
    # Si la lecture est réussie
    if ret:
        # Affichage de l'image capturée
        cv2.imshow('RTSP Stream', frame)
        
        # Attendre 1 milliseconde pour vérifier si l'utilisateur appuie sur la touche 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Libération des ressources
cap.release()
cv2.destroyAllWindows()