# Flowformer for Time Series Classification

We test our proposed Flowformer on the [[UEA]](https://www.timeseriesclassification.com/) dataset, including 10 subsets.

<p align="center">
<img src="..\pic\TS_results.png" height = "300" alt="" align=center />
<br><br>
<b>Figure 1.</b> Results on UEA.
</p>


## Get Started

1. Install the packages by the following commands.

```shell
pip install -r requirements.txt
```

2. Download the dataset from [[Google Drive]](https://drive.google.com/drive/folders/13Cg1KYOlzM5C7K8gK8NfC-F3EYxkM3D2).

3. Train and evaluate the model with following commands. We use the "Best accuracy" as our metric for all baselines and experiments.

```shell
bash scripts/flowformer.sh
```

## Acknowledgement

We appreciate the following github repos a lot for their valuable code base:

https://github.com/gzerveas/mvts_transformer

https://github.com/thuml/Autoformer
