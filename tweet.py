import random
#need three elements 
    # opener: top 10, must have, 
    # thing: patio, summer gadgets
    # purpose: for relaxing, for your home

opener = ['top 10 ', 
        'Must have ', 
        '10 must have ',
        'AD editors select 8 ',
        'Our favorite ']

thing = ['dazzling patio furnishings ',
        'elegant entertaining accessories ',
        'stunning casual dinning pieces ',
        'chic beach towels ',
        'striking designer chaise-longues ']

purpose = ['to impress!',
            'for absolute summer indulgence',
            'for summer adventures',
            'for perfect indoor-outdoor living ',
            'for chic alfresco entertaining ']

print random.choice(opener) + random.choice(thing) + random.choice(purpose)




