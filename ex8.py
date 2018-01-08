#-*- coding: utf-8 -*-
formatter = "%s %s %s %s"
#formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ('Mon', 'Tue', 'Wed', 'Thu')
print formatter % (u"Пон", u"Вт", u"Ср", u"Чет");
