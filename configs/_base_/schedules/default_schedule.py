# optimizer
optim_wrapper = dict(
    optimizer=dict(type='AdamW', lr=5e-5, weight_decay=0),
    paramwise_cfg=dict(norm_decay_mult=0, bias_decay_mult=0),
    clip_grad=dict(max_norm=1),
)

# learning policy
param_scheduler = [
    # dict(type='LinearLR', start_factor=1e-10, end_factor=1, by_epoch=False, begin=0, end=50),
    dict(type='LinearLR', start_factor=1, end_factor=0, begin=0, by_epoch=False)
]

# train, val, test setting
train_cfg = dict(by_epoch=True, max_epochs=200, val_interval=1)
val_cfg = dict()
test_cfg = dict()

# NOTE: `auto_scale_lr` is for automatically scaling LR
# based on the actual training batch size.
auto_scale_lr = dict(base_batch_size=128)
