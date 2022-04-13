base_max_step = 16*90000 # batch_size 19 for 90 k
milestones_ratio = [2/3, 8/9]
batch_size = 8
max_iters = base_max_step // batch_size
milestones = [int(max_iters*m) for m in milestones_ratio]
interval = max_iters // 18

# optimizer
optimizer = dict(type='SGD', lr=0.01*batch_size/16, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)


# learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=0.001,
    by_epoch=False,
    step=milestones)
# runtime settings
runner = dict(type='IterBasedRunner', max_iters=max_iters)
checkpoint_config = dict(by_epoch=False, interval=interval)
evaluation = dict(interval=interval,)