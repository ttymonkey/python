from PIL import Image
from PIL import ImageChops

import datetime

def matchTemplate(searchImage, templateImage):
	minScore = -1000
	matching_xs = 0
	matching_ys = 0
	searchImage = searchImage.convert(mode="L")
	templateImage = templateImage.convert(mode="L")
	searchWidth, searchHeight = searchImage.size
	templateWidth, templateHeight = templateImage.size
	templateMask = Image.new(mode="L", size=templateImage.size, color=1)
	for xs in range(searchWidth-templateWidth+1):
		for ys in range(searchHeight-templateHeight+1):
			score = templateWidth*templateHeight
			searchCrop = searchImage.crop((xs,ys,xs+templateWidth,ys+templateHeight))
			diff = ImageChops.difference(templateImage, searchCrop)
			notequal = ImageChops.darker(diff,templateMask)
			countnotequal = sum(notequal.getdata())
			score -= countnotequal
			if minScore < score:
				minScore = score
				matching_xs = xs
				matching_ys = ys
	im1 = Image.new('RGB', (searchWidth, searchHeight), (80, 147, 0))
	im1.paste(templateImage, ((matching_xs), (matching_ys)))
	im1.save('search_image.png')

searchImage = Image.open("image.png")
templateImage = Image.open("search.png")
matchTemplate(searchImage, templateImage)
