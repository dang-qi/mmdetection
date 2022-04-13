# optimizer
optimizer = dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)


# learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=0.001,
    by_epoch=False,
    step=[60000, 80000])
# runtime settings
runner = dict(type='IterBasedRunner', max_iters=90000)
checkpoint_config = dict(by_epoch=False, interval=5000)