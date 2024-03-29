transformers_pretrained_token_dir = 'bert-base-chinese'

# dataset settings
dataset_type = 'RMDataset'

train_pipeline = [
]

test_pipeline = [
]

collate = dict(
    type='RMCollate',
    tokenizer=dict(
        type='AutoTokenizer',
        pretrained=transformers_pretrained_token_dir,
        do_lower_case=True,
    ),
)

train_dataloader = dict(
    batch_size=16,
    num_workers=2,
    dataset=dict(
        type=dataset_type,
        ann_file='./data.txt',
        test_mode=False,
        pipeline=train_pipeline,
    ),
    sampler=dict(type='DefaultSampler', shuffle=True),
    collate=collate
)

val_dataloader = dict(
    batch_size=16,
    num_workers=2,
    dataset=dict(
        type=dataset_type,
        ann_file='./data.txt',
        test_mode=True,
        pipeline=test_pipeline,
    ),
    sampler=dict(type='DefaultSampler', shuffle=False),
    collate=collate
)
val_evaluator = dict(type='RMMetrics')

test_dataloader = val_dataloader
test_evaluator = val_evaluator
