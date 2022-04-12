# Copyright (c) OpenMMLab. All rights reserved.
from .builder import DATASETS
from .coco import CocoDataset


@DATASETS.register_module()
class FashionpediaDataset(CocoDataset):

    CLASSES = ('shirt, blouse', 'top, t-shirt, sweatshirt', 'sweater', 'cardigan', 'jacket', 'vest', 'pants', 'shorts', 'skirt', 'coat', 'dress', 'jumpsuit', 'cape', 'glasses', 'hat', 'headband, head covering, hair accessory', 'tie', 'glove', 'watch', 'belt', 'leg warmer', 'tights, stockings', 'sock', 'shoe', 'bag, wallet', 'scarf', 'umbrella', 'hood', 'collar', 'lapel', 'epaulette', 'sleeve', 'pocket', 'neckline', 'buckle', 'zipper', 'applique', 'bead', 'bow', 'flower', 'fringe', 'ribbon', 'rivet', 'ruffle', 'sequin', 'tassel')

    PALETTE = [(255, 0, 0), (255, 33, 0), (255, 66, 0), (255, 99, 0), (255, 133, 0), (255, 166, 0), (255, 199, 0), (255, 232, 0), (243, 255, 0), (210, 255, 0), (177, 255, 0), (144, 255, 0), (110, 255, 0), (77, 255, 0), (44, 255, 0), (11, 255, 0), (0, 255, 22), (0, 255, 55), (0, 255, 88), (0, 255, 121), (0, 255, 155), (0, 255, 188), (0, 255, 221), (0, 255, 255), (0, 221, 255), (0, 188, 255), (0, 155, 255), (0, 121, 255), (0, 88, 255), (0, 55, 255), (0, 22, 255), (11, 0, 255), (44, 0, 255), (77, 0, 255), (110, 0, 255), (144, 0, 255), (177, 0, 255), (210, 0, 255), (243, 0, 255), (255, 0, 232), (255, 0, 199), (255, 0, 166), (255, 0, 133), (255, 0, 99), (255, 0, 66), (255, 0, 33)]
