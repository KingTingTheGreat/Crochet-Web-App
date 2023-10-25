import numpy as np
from Yarn import Yarn, YARN_COLORS

class ImageToColors:

    def _init_(self):
        self.colors:list[Yarn] = YARN_COLORS

    def color_distance(self, color1:str, color2:str) -> float:
        """ returns the euclidean distance between two hexcode colors """
        color1 = np.array([int(color1[i:i+2], 16) for i in range(1, 6, 2)])
        color2 = np.array([int(color2[i:i+2], 16) for i in range(1, 6, 2)])
        diff = color1 - color2
        return np.sqrt(np.dot(diff.T, diff))
    
    def find_yarn(self, color:str) -> Yarn:
        """ given a color, returns the yarn object corresponding to that color in the list """
        for yarn in self.colors:
            if yarn.hex == color: return yarn
        #yarn not found
        return None
    
    def find_closest_yarn (self, color2:str) -> Yarn:
        """ given a color, finds the closest Yarn match in the list of Yarns """
        ret_color = ''
        dist = 500
        for yarn in self.colors:
            temp_dist = self.color_distance(yarn.hex, color2)
            if temp_dist < dist:
                ret_color = yarn.hex
                dist = temp_dist
        return self.find_yarn(ret_color)
    
    
    

        
         
