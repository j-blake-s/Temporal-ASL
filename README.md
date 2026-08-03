# Temporal-ASL

<img width="1494" height="491" alt="Screenshot 2026-08-03 094422" src="https://github.com/user-attachments/assets/98dd6879-fe68-48a5-be42-4cff09048e80" />


Data collection repository for the **Temporal-ASL** dataset as described in the paper *"Challenging the Spatiotemporal Processing of Neuromorphic Models through a Temporally-Rich Event-Based Dataset"* (ICONS 2026).

> ### 📄 Abstract
> While neuromorphic systems offer a promising path for processing dynamic, event-based data, current benchmarks often fail to isolate the specific impact of temporal integration on model performance. To address this, our research rigorously investigates how neuromorphic architectures encode and integrate temporal information by conducting a comprehensive ablation study using a hybrid network. We systematically transition from a fully spatial Convolutional Neural Network (CNN) to a fully Spiking Neural Network (SNN) by progressively replacing ReLU activations with spiking neurons across nine distinct model configurations. 
> 
> To challenge these architectures, we introduce the **Temporal-ASL Dataset**, a neuromorphic benchmark specifically curated with signs that exhibit high spatial isomorphism but distinct temporal signatures. This approach allows us to decouple spatial features from motion dynamics and quantify the marginal contribution of spiking membrane dynamics in resolving ambiguities that remain invisible to frame-isolated models. Our analysis reveals a performance hierarchy that peaks at **72.5%** with a hybrid SNN configuration, representing a **6.25% improvement** over the spatial CNN baseline. Logit trajectory analysis confirms this boost stems from the spiking layers' ability to disambiguate spatially similar signs. However, accuracy declines steadily in deeper hierarchies, falling to **23.75%** for the fully spiking SNN. Ultimately, these findings demonstrate that shallow neuromorphic integration effectively maximizes the gains from temporal integration while mitigating the information loss inherent in binary spike quantization.

