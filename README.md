# Temporal-ASL

<img width="1494" height="491" alt="Screenshot 2026-08-03 094422" src="https://github.com/user-attachments/assets/98dd6879-fe68-48a5-be42-4cff09048e80" />


Data collection repository for the **Temporal-ASL** dataset as described in the paper *"Challenging the Spatiotemporal Processing of Neuromorphic Models through a Temporally-Rich Event-Based Dataset"* (ICONS 2026).

> ### 📄 Abstract
> While neuromorphic systems offer a promising path for processing dynamic, event-based data, current benchmarks often fail to isolate the specific impact of temporal integration on model performance. To address this, our research rigorously investigates how neuromorphic architectures encode and integrate temporal information by conducting a comprehensive ablation study using a hybrid network. We systematically transition from a fully spatial Convolutional Neural Network (CNN) to a fully Spiking Neural Network (SNN) by progressively replacing ReLU activations with spiking neurons across nine distinct model configurations. 
> 
> To challenge these architectures, we introduce the **Temporal-ASL Dataset**, a neuromorphic benchmark specifically curated with signs that exhibit high spatial isomorphism but distinct temporal signatures. This approach allows us to decouple spatial features from motion dynamics and quantify the marginal contribution of spiking membrane dynamics in resolving ambiguities that remain invisible to frame-isolated models. Our analysis reveals a performance hierarchy that peaks at **72.5%** with a hybrid SNN configuration, representing a **6.25% improvement** over the spatial CNN baseline. Logit trajectory analysis confirms this boost stems from the spiking layers' ability to disambiguate spatially similar signs. However, accuracy declines steadily in deeper hierarchies, falling to **23.75%** for the fully spiking SNN. Ultimately, these findings demonstrate that shallow neuromorphic integration effectively maximizes the gains from temporal integration while mitigating the information loss inherent in binary spike quantization.

## Dataset Classes & Lexicon

The dataset features **10 distinct dynamic ASL vocabulary signs**, indexed from `0` to `9`:

| Label (Index) | Class Name / Gloss |
| :---: | :--- |
| **0** | Tuesday |
| **1** | Bathroom |
| **2** | Name |
| **3** | Weight |
| **4** | Brown |
| **5** | Beer |
| **6** | Favorite |
| **7** | Colors |
| **8** | Hamburger |
| **9** | Marriage |

## Event Generation & Preprocessing

### Custom Event Simulation
The event data is generated directly from consecutive RGB video frames using temporal differencing and polarity thresholding:

1. **Consecutive Frame Differencing:** For each pixel location $(x, y)$, the intensity difference between two consecutive frames at times $t$ and $t-1$ is computed:
   $$\Delta I(x, y, t) = I(x, y, t) - I(x, y, t-1)$$
2. **Polarity Thresholding:** A spike is generated whenever the magnitude of change exceeds a defined threshold $\theta$:
   * **ON Spike ($\text{Polarity} = 1$ / Channel 0):** Generated when $\Delta I(x, y, t) > \theta$ (Brightness increase)
   * **OFF Spike ($\text{Polarity} = 0$ / Channel 1):** Generated when $\Delta I(x, y, t) < -\theta$ (Brightness decrease)

### 3D Max Pooling Reduction
To lighten computational load we opted to reduce the dimensions of the event data using **3D Max Pooling**. The max pooling layers are applied across the spatial and temporal axes.
* **Spatial Pooling ($H \times W$):** Downsamples the spatial resolution by a factor of 2 ($480 \times 640 \rightarrow 240 \times 320$).
* **Temporal Pooling ($T$):** Downsamples the sequence length by a factor of 2 ($90 \rightarrow 45$ bins), preserving the strongest spike activations across consecutive time intervals while maintaining event sparsity.



## Dataset Structure & Splits

The dataset is partitioned by subject to evaluate cross-signer generalization. To ensure rigorous evaluation and prevent data leakage, the dataset uses a **subject-independent (cross-signer)** train/test split.

* **Training Subjects:** `blake` and `james`
  * Used for model training, feature learning, and cross-validation/hyperparameter tuning.
* **Validation Subject:** `peyton`
  * Exclusively reserved for benchmark evaluation.
  * Contains gesture sequences from a signer completely unseen during training.
  * **Evaluation Goal:** Assesses the model's true **zero-shot cross-subject generalization**—measuring how effectively an architecture learns generalized gesture dynamics rather than memorizing signer-specific features or backgrounds.

## Visualizing Data with `plot.py`

A lightweight visualization script (`plot.py`) is provided to inspect both raw RGB recordings and simulated DVS event sequences.
It loads the sample and uses OpenCV to display the frames sequentially at 30 FPS.

To run the visualizer:
```python plot.py -f <path_to_file>```

### Directory Structure
```text
TemporalASL/
├── original/
│   ├── rgb/
│   │   ├── blake/
│   │   ├── james/
│   │   └── peyton/
│   └── dvs/
│       ├── blake/
│       ├── james/
│       └── peyton/
└── reduced/
    ├── rgb/
    │   └── ...
    └── dvs/
        └── ...

