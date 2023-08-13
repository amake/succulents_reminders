import sys
from random import choice
from enum import Enum, StrEnum, auto
from typing import NamedTuple
from datetime import date, datetime


class Hemisphere(Enum):
    """Hemisphere."""

    Northern = auto()
    Southern = auto()

# All data assumes Northern Hemisphere


class GrowingType(Enum):
    """Succulent growing type."""

    SpringAutumn = auto()
    Summer = auto()
    Winter = auto()


class TipType(Enum):
    """Tip type."""

    Location = auto()
    Watering = auto()
    Fertilizing = auto()
    Maintenance = auto()


class Tip(NamedTuple):
    """A hint for succulent care."""

    month: int
    day: int
    succulent_type: GrowingType
    tip_type: TipType
    title: str
    description: str


tips = [
    # Spring/Autumn
    Tip(6, 10, GrowingType.SpringAutumn, TipType.Location,
        '🔥☀️ Protect from the sun ☀️🔥',
        'Consider moving your spring/autumn succulents to a well-ventilated '
        'area with partial shade to protect them from the sun.'),
    Tip(9, 13, GrowingType.SpringAutumn, TipType.Location,
        '🌞🌱 Move into the sun 🌱🌞',
        'Consider moving your spring/autumn succulents to a well-ventilated '
        'place where they will get plenty of sun.'),
    Tip(3, 1, GrowingType.SpringAutumn, TipType.Watering,
        '💧 Slowly increase watering 💧',
        'You can start watering your spring/autumn succulents a bit more '
        'frequently now.'),
    Tip(4, 1, GrowingType.SpringAutumn, TipType.Watering,
        '💦 Water freely 💦',
        'Your spring/autumn succulents are ready to be watered thoroughly as '
        'soon as their soil is dry.'),
    Tip(6, 11, GrowingType.SpringAutumn, TipType.Watering,
        '💧 Reduce watering 💧',
        'Reduce the amount and frequency of watering for your spring/autumn '
        'succulents as we approach the hot summer months.'),
    Tip(7, 1, GrowingType.SpringAutumn, TipType.Watering,
        '💧 Reduce watering 💧',
        'Now that summer is here, you’ll want to cut watering of your '
        'spring/autumn succulents to once per 10 days, depending on your '
        'environment.'),
    Tip(9, 5, GrowingType.SpringAutumn, TipType.Watering,
        '💦 Water freely 💦',
        'Now that the summer heat has died down, feel free to water your '
        'spring/autumn succulents thoroughly as soon as their soil is dry.'),
    Tip(11, 15, GrowingType.SpringAutumn, TipType.Watering,
        '💧 Reduce watering 💧',
        'As we approach winter, reduce watering of your spring/autumn '
        'succulents to once or twice per month.'),
    Tip(3, 2, GrowingType.SpringAutumn, TipType.Fertilizing,
        '🌱📈 Fertilize! 📈🌱',
        'Consider giving your spring/autumn succulents a bit of slow-release '
        'fertilizer.'),
    Tip(5, 1, GrowingType.SpringAutumn, TipType.Fertilizing,
        '🌱📈 Fertilize! 📈🌱',
        'Consider giving your spring/autumn succulents a bit of slow-release '
        'fertilizer.'),
    Tip(9, 14, GrowingType.SpringAutumn, TipType.Fertilizing,
        '🌱📈 Fertilize! 📈🌱',
        'Consider giving your spring/autumn succulents a bit of slow-release '
        'fertilizer. But hold off if you prefer them to change color over '
        'winter!'),
    Tip(3, 3, GrowingType.SpringAutumn, TipType.Maintenance,
        '🛠️ Spring maintenance 🛠️',
        'Now is a great time to start doing maintenance on your spring/autumn '
        'succulents such as: repotting, splitting offsets, and propagating.'),
    Tip(9, 15, GrowingType.SpringAutumn, TipType.Maintenance,
        '🛠️ Autumn maintenance 🛠️',
        'Now is a great time to start doing maintenance on your spring/autumn '
        'succulents such as repotting and splitting offsets.'),
    # Summer
    Tip(4, 2, GrowingType.Summer, TipType.Location,
        '🌞🌱 Move outside 🌱🌞',
        'Now that it’s warmer out, you can start moving your summer '
        'succulents outside so they can get more light.'),
    Tip(5, 2, GrowingType.Summer, TipType.Location,
        '🌞🌱 Move into the sun 🌱🌞',
        'Consider moving your summer succulents to a place where they '
        'will get plenty of sun.'),
    Tip(11, 1, GrowingType.Summer, TipType.Location,
        'Move inside',
        'Before it gets colder than 5℃ (40°F), start moving your summer '
        'succulents indoors, but make sure they still get plenty of light.'),
    Tip(4, 3, GrowingType.Summer, TipType.Watering,
        '💧 Slowly increase watering 💧',
        'You can start watering your summer succulents a bit.'),
    Tip(5, 3, GrowingType.Summer, TipType.Watering,
        '💦 Water freely 💦',
        'Your summer succulents are ready to be watered thoroughly as '
        'soon as their soil is completely dry.'),
    Tip(9, 16, GrowingType.Summer, TipType.Watering,
        '💧 Reduce watering 💧',
        'Reduce the amount and frequency of watering for your summer '
        'succulents as it gets cooler.'),
    Tip(11, 2, GrowingType.Summer, TipType.Watering,
        '🛑 Stop watering 🛑',
        'As we approach winter, your summer succulents don’t need any more '
        'water. Give them a break until next spring!'),
    Tip(5, 4, GrowingType.Summer, TipType.Fertilizing,
        '🌱📈 Fertilize! 📈🌱',
        'Consider giving your summer succulents a bit of slow-release '
        'fertilizer.'),
    Tip(7, 2, GrowingType.Summer, TipType.Fertilizing,
        '🌱📈 Fertilize! 📈🌱',
        'Consider giving your summer succulents a bit of slow-release '
        'fertilizer.'),
    Tip(5, 5, GrowingType.Summer, TipType.Maintenance,
        '🛠️ Summer maintenance 🛠️',
        'Now is a great time to start doing maintenance on your summer '
        'succulents such as: repotting, splitting offsets, and propagating.'),
    # Winter
    Tip(3, 15, GrowingType.Winter, TipType.Location,
        '🌞🌱 Move outside 🌱🌞',
        'Now that it’s warmer out, you can start moving your winter '
        'succulents outside so they can get more light.'),
    Tip(6, 12, GrowingType.Winter, TipType.Location,
        '😎 Move into the shade 😎',
        'Consider moving your winter succulents to a well-ventilated '
        'area with partial shade to protect them from the sun.'),
    Tip(9, 17, GrowingType.Winter, TipType.Location,
        '🌞🌱 Move into the sun 🌱🌞',
        'If you’ve been protecting your winter succulents from the summer '
        'sun, consider moving them back to a well-ventilated place '
        'where they will get plenty of light as we approach winter.'),
    Tip(3, 4, GrowingType.Winter, TipType.Watering,
        '💦 Water freely 💦',
        'Your winter succulents are ready to be watered thoroughly as '
        'soon as their soil is dry.'),
    Tip(6, 13, GrowingType.Winter, TipType.Watering,
        '💧 Reduce watering 💧',
        'Reduce the amount and frequency of watering for your winter '
        'succulents as we approach the hot summer months.'),
    Tip(7, 3, GrowingType.Winter, TipType.Watering,
        '💧 Water sparingly 💧',
        'Now that summer is here, you’ll want to cut watering of your '
        'winter succulents to twice per month, just enough to wet the surface '
        'of the soil.'),
    Tip(9, 18, GrowingType.Winter, TipType.Watering,
        '💧 Slowly increase watering 💧',
        'You can start watering your winter succulents a bit more.'),
    Tip(10, 1, GrowingType.Winter, TipType.Watering,
        '💦 Water freely 💦',
        'Now that the summer heat has died down, feel free to water your '
        'winter succulents thoroughly as soon as their soil is dry.'),
    Tip(12, 1, GrowingType.Winter, TipType.Watering,
        '💧 Reduce watering 💧',
        'As we approach winter, reduce watering of your winter '
        'succulents to twice per month.'),
    Tip(3, 5, GrowingType.Winter, TipType.Fertilizing,
        '🌱📈 Fertilize! 📈🌱',
        'Consider giving your winter succulents a bit of slow-release '
        'fertilizer.'),
    Tip(10, 2, GrowingType.Winter, TipType.Fertilizing,
        '🌱📈 Fertilize! 📈🌱',
        'Consider giving your winter succulents a bit of slow-release '
        'fertilizer.'),
    Tip(9, 1, GrowingType.Winter, TipType.Maintenance,
        '🛠️ Autumn maintenance 🛠️',
        'Now is a great time to start doing maintenance on your winter '
        'succulents such as: repotting, splitting offsets, and propagating.'),
]


class Variety(StrEnum):
    """Succulent variety."""

    # Spring/autumn
    Cotyledon = auto()
    Crassula = auto()
    Echeveria = auto()
    Graptopetalum = auto()
    Haworthia = auto()
    Pachyphytum = auto()
    Sedum = auto()
    Sempervivum = auto()
    Senecio = auto()

    # Summer
    Agave = auto()
    Aloe = auto()
    Cactus = auto()
    Euphorbia = auto()
    Gasteria = auto()
    Huernia = auto()
    Kalanchoe = auto()
    Pachypodium = auto()

    # Winter
    Aeonium = auto()
    Conophytum = auto()
    Lithops = auto()
    Othonna = auto()
    Pleiospilos = auto()


exemplar_succulents = {
    GrowingType.SpringAutumn: [
        Variety.Cotyledon, Variety.Crassula, Variety.Echeveria,
        Variety.Graptopetalum, Variety.Haworthia, Variety.Pachyphytum,
        Variety.Sedum, Variety.Sempervivum, Variety.Senecio
    ],
    GrowingType.Summer: [
        Variety.Agave, Variety.Aloe, Variety.Cactus, Variety.Euphorbia,
        Variety.Gasteria, Variety.Huernia, Variety.Kalanchoe,
        Variety.Pachypodium
    ],
    GrowingType.Winter: [
        Variety.Aeonium, Variety.Conophytum, Variety.Lithops, Variety.Othonna,
        Variety.Pleiospilos,
    ]
}

photos = {
    Variety.Cotyledon: [
        'IMG_3407.jpg', 'IMG_3551.jpg', 'IMG_3837.jpg', 'IMG_4307.jpg',
        'IMG_4654.jpg', 'IMG_4735.jpg',
    ],
    Variety.Crassula: [
        'IMG_3554.jpg', 'IMG_3863.jpg', 'IMG_4381.jpg', 'IMG_4465.jpg',
        'IMG_4466.jpg',
    ],
    Variety.Echeveria: [
        'IMG_4324.jpg', 'IMG_4647.jpg', 'IMG_4649.jpg', 'IMG_4678.jpg',
        'IMG_4742.jpg', 'IMG_4744.jpg',
    ],
    Variety.Graptopetalum: ['IMG_3630.jpg'],
    Variety.Haworthia: [
        'IMG_2778.jpg', 'IMG_3435.jpg', 'IMG_3577.jpg', 'IMG_4177.jpg',
        'IMG_4180.jpg', 'IMG_4183.jpg', 'IMG_4184.jpg', 'IMG_4291.jpg',
    ],
    Variety.Pachyphytum: ['IMG_4745.jpg'],
    Variety.Sedum: [
        'IMG_3005.jpg', 'IMG_3014.jpg', 'IMG_3553.jpg', 'IMG_4374.jpg',
        'IMG_4506.jpg',
    ],
    Variety.Sempervivum: [
        'IMG_3568.jpg', 'IMG_3569.jpg', 'IMG_3983.jpg',
    ],
    Variety.Senecio: [],  # TODO
    Variety.Agave: [
        'IMG_4299.jpg', 'IMG_4360.jpg', 'IMG_4377.jpg', 'IMG_4747.jpg',
    ],
    Variety.Aloe: ['IMG_3880.jpg', 'IMG_4679.jpg', 'IMG_4746.jpg'],
    Variety.Cactus: [
        'IMG_3566.jpg', 'IMG_3900.jpg', 'IMG_3957.jpg', 'IMG_3959.jpg',
    ],
    Variety.Euphorbia: [
        'IMG_2908.jpg', 'IMG_4364.jpg', 'IMG_4369.jpg', 'IMG_4609.jpg',
    ],
    Variety.Gasteria: ['IMG_3311.jpg'],
    Variety.Huernia: ['IMG_4368.jpg'],
    Variety.Kalanchoe: ['IMG_3827.jpg', 'IMG_4378.jpg', 'IMG_4653.jpg'],
    Variety.Pachypodium: [],
    Variety.Aeonium: [
        'IMG_3636.jpg', 'IMG_3787.jpg', 'IMG_3788.jpg', 'IMG_3789.jpg',
        'IMG_4155.jpg',
    ],
    Variety.Conophytum: ['IMG_1813.jpg'],
    Variety.Lithops: [
        'IMG_1538.jpg', 'IMG_1553.jpg'
    ],
    Variety.Othonna: [],  # TODO
    Variety.Pleiospilos: [],  # TODO
}

relevant_succulents_titles = {
    GrowingType.SpringAutumn: 'Spring/autumn succulents include:',
    GrowingType.Summer: 'Summer succulents include:',
    GrowingType.Winter: 'Winter succulents include:',
}


def get_tips(on_date: date, hemisphere: Hemisphere):
    """Return a list of tips for the given date."""
    match_month = (on_date.month if hemisphere == Hemisphere.Northern
                   else (on_date.month + 6) % 12)
    return [tip._replace(month=on_date.month) for tip in tips
            if tip.month == match_month and tip.day == on_date.day]


def choose(collection, n: int):
    """Choose a random sample of n items from the collection."""
    result = set()
    while len(result) < n:
        result.add(choice(collection))
    return result


def get_images(tip: Tip, count=4):
    """Get image URLs for the supplied tip."""
    varieties = choose(
        [variety for variety in exemplar_succulents[tip.succulent_type]
         if photos[variety]],
        count
    )
    return [choice(photos[variety]) for variety in varieties]


def describe_date(tip: Tip):
    """Return a string representation of the date."""
    today = date.today()
    tip_date = date(today.year, tip.month, tip.day)
    month_name = tip_date.strftime('%B')
    if tip.day < 10:
        return f'early {month_name}'
    elif tip.day < 20:
        return f'mid {month_name}'
    else:
        return f'late {month_name}'


def format_tip(tip: Tip):
    """Return a string representation of the tip."""
    date_str = describe_date(tip)
    example_list = '\n'.join([str(name).title() for name in
                              sorted(exemplar_succulents[tip.succulent_type])])
    return f'''Succulent tip for {date_str}: {tip.title}

{tip.description}

{relevant_succulents_titles[tip.succulent_type]}
{example_list}

#succulents #plants #gardening
'''


if __name__ == '__main__':
    on_date = (datetime.strptime(sys.argv[1], '%Y-%m-%d')
               if sys.argv[1:] else date.today())
    hemisphere = (Hemisphere[sys.argv[2]]
                  if len(sys.argv) > 2 else Hemisphere.Northern)
    print('Tips for', on_date, 'in the', hemisphere.name, 'hemisphere:')
    for n, tip in enumerate(get_tips(on_date, hemisphere)):
        print(f'{n+1}.', format_tip(tip))
        print
