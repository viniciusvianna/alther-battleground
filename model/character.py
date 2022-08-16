from model.action import Action
from model.attribute import Attribute
from model.weapon import Weapon
from model.race import Race

# Esta é a classe base que representa o personagem, sendo assim deve conter:
# Info básica que não envolve métodos: nome, raça, origem, escola, aspiração, altura, peso, idade e idiomas (v)
# Info básica que envolve métodos: nível, xp, pd, pv, am, ap, moeda (v)
# Atributos: corpo, mente, foco, espírito, social e natureza (v)
# Ações do personagem: acerto, esquiva, defesa, resistência e artes (v)
# Equipamentos: mão direita, mão esquerda, tronco (v)
# Efeitos: mão direita, mão esquerda, tronco, cabeça, pés, acessório (v)
# Caminhos: ativos e não ativos, pc
# Habilidades: intrínseca, padrão (x4), suporte (x2), movimento, reação e perfeita
# Inventário e Anotações
# Companheiro Animal


class Character:

    def __init__(self, name: str,
                 race: Race,
                 origin: str,
                 school: str,
                 aspiration: str,
                 height: float,
                 weight: float,
                 age: int,
                 languages=None,
                 level=1,
                 total_xp=0,
                 current_xp=-1,
                 pd=0,
                 total_pv=0,
                 current_pv=-1,
                 am=1,
                 ap=1,
                 valors=0,
                 ruubis=0,
                 attributes=None,
                 actions=None,
                 effects=None):
        if languages is None:
            languages = ["Medio"]

        if actions is None:
            actions = {"hit": Action("Hit"),
                       "evade": Action("Evade"),
                       "defend": Action("Defend"),
                       "resist": Action("Resist"),
                       "arts": Action("Arts")}

        if attributes is None:
            attributes = {"body": Attribute("Body", 10),
                          "mind": Attribute("Mind", 5),
                          "focus": Attribute("Focus", 10),
                          "spirit": Attribute("Spirit", 5),
                          "social": Attribute("Social", 10),
                          "nature": Attribute("Nature", 5)}

        if effects is None:
            effects = {"Hand1": None,
                       "Hand2": None,
                       "Body": None,
                       "Head": None,
                       "Feet": None,
                       "Accessory": None}

        self.name = name
        self.race = race
        self.origin = origin
        self.school = school
        self.aspiration = aspiration
        self.height = height
        self.weight = weight
        self.age = age
        self.languages = languages
        self.level = level
        self.total_xp = total_xp

        if current_xp < 0:
            self.current_xp = total_xp
        else:
            self.current_xp = current_xp

        self.pd = pd
        self.total_pv = total_pv

        if current_pv < 0:
            self.current_pv = total_pv
        else:
            self.current_pv = current_pv

        self.am = am
        self.ap = ap
        self.valors = valors
        self.ruubis = ruubis
        self.attributes = attributes
        self.actions = actions
        self.effects = effects
        self.equips = {"Hand1": None, "Hand2": None, "Body": None}

    def __str__(self):
        return self.name

    def show_attributes(self):
        print("Attributes")
        for attribute in self.attributes.values():
            print(attribute)

    def show_actions(self):
        print("Actions")
        for action in self.actions.values():
            print(action)

    def equip_weapon(self, weapon: Weapon, slot: str):
        attr = weapon.damage.attr
        for attribute in self.attributes.keys():
            if attr.name.lower() == attribute:
                weapon.damage.attr = self.attributes[attribute]

        self.equips[slot] = weapon

    def attack(self, hand):
        if self.equips[hand] is None:
            result = self.attributes["body"].total_value / 4  # Ataque sem arma tem dano fixo de C4
        else:
            result = self.equips[hand].damage.roll_damage()

        return result