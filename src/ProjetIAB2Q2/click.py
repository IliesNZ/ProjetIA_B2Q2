import pyautogui

def click_on_answer(coordonees):

    x1, y1, x2, y2 = coordonees
    
    centre_x = (x1 + x2) // 2
    centre_y = (y1 + y2) // 2
    
    print(f"Déplacement de la souris vers ({centre_x}, {centre_y})...")
    pyautogui.moveTo(centre_x, centre_y, duration=0.5)
    pyautogui.click()