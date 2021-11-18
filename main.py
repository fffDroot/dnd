import random

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from random import choice
import pymorphy2
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown

t = ''
set = ''


class MyApp(App):
    def up1(self, tx):
        self.lbl2.text = tx

    def up2(self, tx):
        self.lbl2.text = tx

    def up3(self, tx):
        self.lbl2.text = tx

    def s1(self, instance):
        global set
        set = 'Ваш сеттинг: Средневековье'
        self.up1(set)

    def s2(self, instance):
        global set
        set = 'Ваш сеттинг: Современность'
        self.up2(set)

    def s3(self, instance):
        global set
        set = 'Ваш сеттинг: Будущее'
        self.up3(set)

    def update(self):
        global t
        self.lbl.text = t

    def btn_press(self, instance):
        global t
        self.person = self.npc.text
        self.it = self.item.text
        morph = pymorphy2.MorphAnalyzer()
        p = morph.parse(self.it)[0]
        if p.tag.gender == 'masc':
            self.predm = f' Вам известно, что в этой комнате спрятан {self.it}'
        elif p.tag.gender == 'femn':
            self.predm = f' Вам известно, что в этой комнате спрятана {self.it}'
        elif p.tag.gender == 'neut':
            self.predm = f' Вам известно, что в этой комнате спрятано {self.it}'
        else:
            self.predm = f' Вам известно, что в этой комнате спрятан {self.it}'

        per = morph.parse(self.person)[0]

        if self.lbl2.text == '' or self.textinput.text == '' or self.item.text == '' or self.npc.text == '':
            self.lbl.text = 'Введены не все данные'
        elif self.lbl2.text == 'Ваш сеттинг: Средневековье':
            f1 = open(r'old\additional items\items.txt', 'r', encoding='utf-8')
            f2 = open(r'old\Exits from the room\exits.txt', 'r', encoding='utf-8')
            f3 = open(r'old\Furniture and what other items may be on\Furniture.txt', 'r', encoding='utf-8')
            f4 = open(r'old\lighting items\lighting items .txt', 'r', encoding='utf-8')
            f5 = open(r'old\room lighting\lighting.txt', 'r', encoding='utf-8')
            f6 = open(r'old\room type\type.txt', 'r', encoding='utf-8')
            f7 = open(r'old\size room\Size.txt', 'r', encoding='utf-8')
            f8 = open(r'old\Walls\Walls.txt', 'r', encoding='utf-8')
            f9 = open(r'old\Where objects can be located\located.txt', 'r', encoding='utf-8')
            f11 = open(r'old\nps\cloth.txt', 'r', encoding='utf-8')
            f12 = open(r'old\nps\color.txt', 'r', encoding='utf-8')
            f13 = open(r'old\nps\hair.txt', 'r', encoding='utf-8')
            f14 = open(r'old\nps\osobt.txt', 'r', encoding='utf-8')
            f17 = open(r'coord\position.txt', 'r')
            f18 = open(r'coord\destv.txt', 'r')
            r11 = f11.readline()
            sp11 = r11.split(' : ')
            r12 = f12.readline()
            sp12 = r12.split(' : ')
            r13 = f13.readline()
            sp13 = r13.split(' : ')
            r14 = f14.readline()
            sp14 = r14.split(' : ')
            r17 = f17.readline()
            sp17 = r17.split(' : ')
            r18 = f18.readline()
            sp18 = r18.split(' : ')

            r1 = f1.readline()
            sp1 = r1.split(' : ')
            r2 = f2.readline()
            sp2 = r2.split(' : ')
            r3 = f3.readline()
            sp3 = r3.split(' : ')
            r4 = f4.readline()
            sp4 = r4.split(' : ')
            r5 = f5.readline()
            sp5 = r5.split(' : ')
            r6 = f6.readline()
            sp6 = r6.split(' : ')
            r7 = f7.readline()
            sp7 = r7.split(' : ')
            r8 = f8.readline()
            sp8 = r8.split(' : ')
            r9 = f9.readline()
            sp9 = r9.split(' : ')
            f1.close()
            f2.close()
            f3.close()
            f4.close()
            f5.close()
            f6.close()
            f7.close()
            f8.close()
            f9.close()
            cl = choice(sp11)
            loctcl = morph.parse(cl)[0]
            cloth = loctcl.inflect({'accs'}).word
            if per.tag.gender == 'masc':
                pers = f' {choice(sp17)} комнаты {choice(sp18)} {self.person}. \n Он казался {choice(sp14)}, \nу него {choice(sp13)}, глаза его были {choice(sp12)} цвета. \nОн одет в {cloth}.'
            elif per.tag.gender == 'femn':
                pers = f' {choice(sp17)} комнаты {choice(sp18)} {self.person}. \n Она казалась {choice(sp14)}, \nу неё {choice(sp13)}, глаза её были {choice(sp12)} цвета. \nОна одета в {cloth}.'
            else:
                pers = f' {choice(sp17)} комнаты {choice(sp18)} {self.person}. \n Он казался {choice(sp14)}, \nу него {choice(sp13)}, глаза его были {choice(sp12)} цвета. \nОн одет в {cloth}.'
            furn1 = choice(sp3)
            loct1 = morph.parse(furn1)[0]
            sl = loct1.inflect({'loct'}).word
            furn2 = choice(sp3)
            furn3 = choice(sp3)
            if self.textinput.text == '':
                lock = choice(sp6).capitalize()
            else:
                lock = self.textinput.text
            t = f'{lock.capitalize()}: комната была {choice(sp7)}, {choice(sp5)}.\n Комната освещалась {choice(sp4)}. Стены комнаты {choice(sp8)}.\n В комнате также был выход, представленный в виде {choice(sp2)}.\n В комнате рапспологались: {furn1}, {furn2}, {furn3}. \nНа {sl} {choice(sp1)}.' + pers + self.predm
            self.update()
        elif self.lbl2.text == 'Ваш сеттинг: Современность':
            f1 = open(r'now\additional items\items(n).txt', 'r', encoding='utf-8')
            f2 = open(r'now\Exits from the room\Exits(n).txt', 'r', encoding='utf-8')
            f3 = open(r'now\Furniture and what other items may be on\Furniture(n).txt', 'r', encoding='utf-8')
            f4 = open(r'now\lighting items\ilghting items(n).txt', 'r', encoding='utf-8')
            f5 = open(r'now\room lighting\room lighting(n).txt', 'r', encoding='utf-8')
            f6 = open(r'now\room type\room type(n).txt', 'r', encoding='utf-8')
            f7 = open(r'now\size room\size room(n).txt', 'r', encoding='utf-8')
            f8 = open(r'now\Walls\Walls(n).txt', 'r', encoding='utf-8')
            f9 = open(r'now\Where objects can be located\location(n).txt', 'r', encoding='utf-8')
            f11 = open(r'now\nps\cloth.txt', 'r', encoding='utf-8')
            f12 = open(r'now\nps\color.txt', 'r', encoding='utf-8')
            f13 = open(r'now\nps\hair.txt', 'r', encoding='utf-8')
            f14 = open(r'now\nps\osobt.txt', 'r', encoding='utf-8')
            f17 = open(r'coord\position.txt', 'r')
            f18 = open(r'coord\destv.txt', 'r')
            r11 = f11.readline()
            sp11 = r11.split(' : ')
            r12 = f12.readline()
            sp12 = r12.split(' : ')
            r13 = f13.readline()
            sp13 = r13.split(' : ')
            r14 = f14.readline()
            sp14 = r14.split(' : ')
            r17 = f17.readline()
            sp17 = r17.split(' : ')
            r18 = f18.readline()
            sp18 = r18.split(' : ')

            r1 = f1.readline()
            sp1 = r1.split(' : ')
            r2 = f2.readline()
            sp2 = r2.split(' : ')
            r3 = f3.readline()
            sp3 = r3.split(' : ')
            r4 = f4.readline()
            sp4 = r4.split(' : ')
            r5 = f5.readline()
            sp5 = r5.split(' : ')
            r6 = f6.readline()
            sp6 = r6.split(' : ')
            r7 = f7.readline()
            sp7 = r7.split(' : ')
            r8 = f8.readline()
            sp8 = r8.split(' : ')
            r9 = f9.readline()
            sp9 = r9.split(' : ')
            f1.close()
            f2.close()
            f3.close()
            f4.close()
            f5.close()
            f6.close()
            f7.close()
            f8.close()
            f9.close()
            cl = choice(sp11)
            loctcl = morph.parse(cl)[0]
            cloth = loctcl.inflect({'accs'}).word
            if per.tag.gender == 'masc':
                pers = f' {choice(sp17)} комнаты {choice(sp18)} {self.person}. \n Он казался {choice(sp14)}, \nу него {choice(sp13)}, глаза его были {choice(sp12)} цвета. \nОн одет в {cloth}.'
            elif per.tag.gender == 'femn':
                pers = f' {choice(sp17)} комнаты {choice(sp18)} {self.person}. \n Она казалась {choice(sp14)}, \nу неё {choice(sp13)}, глаза её были {choice(sp12)} цвета. \nОна одета в {cloth}.'
            else:
                pers = f' {choice(sp17)} комнаты {choice(sp18)} {self.person}. \n Он казался {choice(sp14)}, \nу него {choice(sp13)}, глаза его были {choice(sp12)} цвета. \nОн одет в {cloth}.'
            furn1 = choice(sp3)
            loct1 = morph.parse(furn1)[0]
            sl = loct1.inflect({'loct'}).word
            furn2 = choice(sp3)
            furn3 = choice(sp3)
            if self.textinput.text == '':
                lock = choice(sp6).capitalize()
            else:
                lock = self.textinput.text
            t = f'{lock.capitalize()}: комната была {choice(sp7)}, {choice(sp5)}.\nКомната освещалась {choice(sp4)}. Стены комнаты {choice(sp8)}.\n В комнате также был выход, представленный в виде {choice(sp2)}.\nВ комнате рапспологались: {furn1}, {furn2}, {furn3}. \nНа {sl} {choice(sp1)}.' + pers + self.predm
            self.update()
        elif self.lbl2.text == 'Ваш сеттинг: Будущее':
            f1 = open(r'fut\additional items\Items(F).txt', 'r', encoding='utf-8')
            f2 = open(r'fut\Exits from the room\Exits(F).txt', 'r', encoding='utf-8')
            f3 = open(r'fut\Furniture and what other items may be on\Furniture(F).txt', 'r', encoding='utf-8')
            f4 = open(r'fut\lighting items\lighting items(F).txt', 'r', encoding='utf-8')
            f5 = open(r'fut\room lighting\room ligting(F).txt', 'r', encoding='utf-8')
            f6 = open(r'fut\room type\room type.txt', 'r', encoding='utf-8')
            f7 = open(r'fut\size room\size room(F).txt', 'r', encoding='utf-8')
            f8 = open(r'fut\Walls\Walls(F).txt', 'r', encoding='utf-8')
            f9 = open(r'fut\Where objects can be located\location(F).txt', 'r', encoding='utf-8')
            f11 = open(r'fut\nps\cloth.txt', 'r', encoding='utf-8')
            f12 = open(r'fut\nps\color.txt', 'r', encoding='utf-8')
            f13 = open(r'fut\nps\hair.txt', 'r', encoding='utf-8')
            f14 = open(r'fut\nps\osobt.txt', 'r', encoding='utf-8')
            f17 = open(r'coord\position.txt', 'r')
            f18 = open(r'coord\destv.txt', 'r')
            r11 = f11.readline()
            sp11 = r11.split(' : ')
            r12 = f12.readline()
            sp12 = r12.split(' : ')
            r13 = f13.readline()
            sp13 = r13.split(' : ')
            r14 = f14.readline()
            sp14 = r14.split(' : ')
            r17 = f17.readline()
            sp17 = r17.split(' : ')
            r18 = f18.readline()
            sp18 = r18.split(' : ')
            cl = choice(sp11)
            loctcl = morph.parse(cl)[0]
            cloth = loctcl.inflect({'accs'}).word
            if per.tag.gender == 'masc':
                pers = f' {choice(sp17)} комнаты {choice(sp18)} {self.person}. \n Он казался {choice(sp14)}, \nу него {choice(sp13)}, глаза его были {choice(sp12)} цвета. \nОн одет в {cloth}.'
            elif per.tag.gender == 'femn':
                pers = f' {choice(sp17)} комнаты {choice(sp18)} {self.person}. \n Она казалась {choice(sp14)}, \nу неё {choice(sp13)}, глаза её были {choice(sp12)} цвета. \nОна одета в {cloth}.'
            else:
                pers = f' {choice(sp17)} комнаты {choice(sp18)} {self.person}. \n Он казался {choice(sp14)}, \nу него {choice(sp13)}, глаза его были {choice(sp12)} цвета. \nОн одет в {cloth}.'
            r1 = f1.readline()
            sp1 = r1.split(' : ')
            r2 = f2.readline()
            sp2 = r2.split(' : ')
            r3 = f3.readline()
            sp3 = r3.split(' : ')
            r4 = f4.readline()
            sp4 = r4.split(' : ')
            r5 = f5.readline()
            sp5 = r5.split(' : ')
            r6 = f6.readline()
            sp6 = r6.split(' : ')
            r7 = f7.readline()
            sp7 = r7.split(' : ')
            r8 = f8.readline()
            sp8 = r8.split(' : ')
            r9 = f9.readline()
            sp9 = r9.split(' : ')
            f1.close()
            f2.close()
            f3.close()
            f4.close()
            f5.close()
            f6.close()
            f7.close()
            f8.close()
            f9.close()
            furn1 = choice(sp3)
            loct1 = morph.parse(furn1)[0]
            sl = loct1.inflect({'loct'}).word
            furn2 = choice(sp3)
            furn3 = choice(sp3)
            if self.textinput.text == '':
                lock = choice(sp6).capitalize()
            else:
                lock = self.textinput.text
            t = f'{lock.capitalize()}: комната была {choice(sp7)}, {choice(sp5)}.\n Комната освещалась {choice(sp4)}. Стены комнаты {choice(sp8)}.\n В комнате также был выход, представленный в виде {choice(sp2)}.\n В комнате рапспологались: {furn1}, {furn2}, {furn3}. \nНа {sl} {choice(sp1)}.' + pers + self.predm
            self.update()

    def build(self):
        global t
        global set
        n1 = random.randint(1, 4)
        n2 = random.randint(1, 4)
        n3 = random.randint(1, 4)
        a1 = AnchorLayout(anchor_x='center', anchor_y='bottom')
        a2 = AnchorLayout(anchor_x='center', anchor_y='center')
        a3 = AnchorLayout(anchor_x='left', anchor_y='top')
        a4 = AnchorLayout(anchor_x='center', anchor_y='top')
        a5 = AnchorLayout(anchor_x='right', anchor_y='top')
        fl = FloatLayout(size=(300, 200))
        a1.add_widget(Button(text='Сгенерировать Историю',
                             font_size=15,
                             on_press=self.btn_press,
                             background_color=[.80, .10, .30, 1],
                             background_normal='',
                             size_hint=(.50, .10)))

        self.lbl = Label(text='',
                         font_size=12,
                         valign='center',
                         halign='center',
                         pos=(-100, 0))
        self.lbl2 = Label(text=set, font_size=12, pos=(-318, 115))
        a2.add_widget(self.lbl)

        a3.add_widget(Button(text='Средневековье',
                             font_size=15,
                             on_press=self.s1,
                             # background_color=[.80, .10, .30, 1],
                             background_normal=(f'old\photo\{n1}o.jpeg'),
                             size_hint=(.33, .30),
                             valign='top',
                             halign='left'

                             ))
        a4.add_widget(Button(text='Современность',
                             font_size=15,
                             on_press=self.s2,
                             # background_color=[.80, .10, .30, 1],
                             background_normal=(f'now\photo\{n2}n.jpeg'),
                             size_hint=(.33, .30),
                             valign='top',
                             halign='center'
                             ))
        a5.add_widget(Button(text='Будущее',
                             font_size=15,
                             on_press=self.s3,
                             # background_color=[.80, .10, .30, 1],
                             background_normal=(f'fut\photo\{n3}f.jpeg'),
                             size_hint=(.33, .30),
                             valign='top',
                             halign='right'
                             ))
        self.textinput = TextInput(text='', pos=(670, 300), size_hint=(.15, .10))
        self.item = TextInput(text='', pos=(670, 200), size_hint=(.15, .10))
        self.npc = TextInput(text='', pos=(670, 100), size_hint=(.15, .10))
        self.lbl3 = Label(text='Введите локацию', font_size=9, pos=(330, 90))
        self.lblitem = Label(text='Введите особый предмет', font_size=9, pos=(330, -20))
        self.lblnpc = Label(text='Введите ключевого персонажа', font_size=9, pos=(330, -130))
        fl.add_widget(a1)
        fl.add_widget(a2)
        fl.add_widget(a3)
        fl.add_widget(a4)
        fl.add_widget(a5)
        fl.add_widget(self.lbl2)
        fl.add_widget(self.lbl3)
        fl.add_widget(self.lblitem)
        fl.add_widget(self.lblnpc)
        fl.add_widget(self.textinput)
        fl.add_widget(self.item)
        fl.add_widget(self.npc)
        return fl


if __name__ == '__main__':
    app = MyApp()
    app.run()
