# coding: utf-8
import cs1graphics as cg
paper = cg.Canvas()
paper.setBackgroundColor('skyBlue')
paper.setWidth(800)
paper.setHeight(600)
paper.setTitle('My World')
paper.
dir(paper)
paper.getBackgroundColor()
paper.getWith()
paper.getWidth()
sun = cg.Circle()
paper.add(sun)
sun.setFillColor('yellow')
sun.setRadius(50)
sun.moveTo(700,100)
sunCenter = cg.Point(700, 100)
sun2 = cg.Circle(50, sunCenter)
sun2.setFillColor('lightYellow')
paper.add(sun2)
facade = cg.Square(200, cg.Point(400, 350))
facade.setFillColor('white')
paper.add(facade)
chimney = cg.Rectangle(50, 70, cg.Point(450, 215))
chimney.setFillColor('red')
paper.add(chimney)
tree = cg.Polygon(cg.Point(150, 220),
                  cg.Point(120, 380),
                  cg.Point(180, 380))
tree.setFillColor('darkGreen')
paper.add(tree)
sunraySW = cg.Path(cg.Point(660, 140), cg.Point(635,165))
sunraySW.setBorderColor('yellow')
sunraySW.setBorderWidth(6)
paper.add(sunraySW)
sunraySE = cg.Path(cg.Point(740, 140), cg.Point(765,165))
sunraySE.setBorderColor('yellow')
sunraySE.setBorderWidth(6)
paper.add(sunraySE)
sunrayNE = cg.Path(cg.Point(740, 60), cg.Point(765,35))
sunrayNE.setBorderColor('yellow')
sunrayNE.setBorderWidth(6)
paper.add(sunrayNE)
sunrayNW = cg.Path(cg.Point(660, 60), cg.Point(635,35))
sunrayNW.setBorderColor('yellow')
sunrayNW.setBorderWidth(6)
paper.add(sunrayNW)
chimney.getDepth()
grass = cg.Rectangle(800, 300, cg.Point(400, 450))
grass.setFillColor('green')
grass.setBorderColor('green')
grass.setDepth(75)
paper.add(grass)
grass.setDepth(20)
grass.setDepth(75)
door = cg.Rectangle(100, cg.Point(400, 450))
help(Rectangle)
help(cg.Rectangle)
help(cg.Rectangle)
door = cg.Rectangle(50,100, cg.Point(400, 450))
door.setFillColor('brown')
paper.add(door)
door = cg.Rectangle(50,100, cg.Point(400, 400))
paper.add(door)
door.setFillColor('brown')
door = cg.Rectangle(50,50, cg.Point(400, 400))
door.setFillColor('brown')
paper.add(door)
del door = cg.Rectangle(50,50, cg.Point(400, 400))
del door
paper.add(door)
paper.add(door)
door = cg.Rectangle(50,50, cg.Point(400, 400))
paper.remove(door)
paper.clear(door)
door.remove()
paper.remove(door)
door = cg.Rectangle(50,50, cg.Point(400, 400))
door.setFillColor('brown')
paper.add(door)
dir(door)
get_ipython().magic(u'man (door)')
help(door)
paper.remove(door)
door.getReferencePoint()
door.moveTo(400, 450)
paper.add(door)
help(door)
help(paper)
paper.refresh()
door.refresh()
help(paper)
remove(door)
paper.remove(door)
paper.remove(door)
window = cg.Square(50, cg.Point(350, 300))
window.setFillColor('blue')
paper.add(window)
window.move(10, 0)
window.move(-10, 0)
star = cg.Polygon(cg.Point(50, 10), cg.Point(55, 25), cg.Point(75, 20), cg.Point(60, 45), cg.Point(70, 60), cg.Point(50, 50), cg.Point(30, 60), cg.Point(40, 45), cg.Point(25, 20), cg.Point(45, 25))
star.setFillColor('lightpurple')
star.setFillColor('purple')
paper.add(star)
star.move(350, 500)
star.move(350, -100)
star.setFillColor('pink')
get_ipython().magic(u'save current_session ~0/')
