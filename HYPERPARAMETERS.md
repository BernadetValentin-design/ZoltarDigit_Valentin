# Hyperparameter Analysis

## Summary
This documents presents the differents configurations used for MLP and CNN.

## MLP (Multi-Layer Perceptron)

### Architecture
- **Input**: 784 neurons (28x28 pixels flattened)
- **Hidden Layer 1**: 512 neurons, SiLU activation
- **Hidden Layer 2**: 512 neurons, SiLU activation
- **Output**: 10 neurons (classes 0-9)

### MLP Configurations

| Config | STEPS | BATCH | LR | LR_DECAY | PATIENCE | Accuracy | Time |
|--------|-------|-------|-----|----------|----------|----------|------|
| 1 - Baseline | 100 | 512 | 0.02 | 0.9 | 50 | 94.50% | 34.7s |
| 2 - More training | 200 | 512 | 0.02 | 0.9 | 50 | 95.80% | 56.3s |
| 3 - High LR | 100 | 512 | 0.05 | 0.9 | 50 | 93.20% | 33.7s |
| 4 - Low LR | 100 | 512 | 0.01 | 0.9 | 50 | 94.10% | 35.6s |
| 5 - Small batch | 100 | 256 | 0.02 | 0.9 | 50 | 94.80% | 37.0s |
| 6 - Large batch | 100 | 1024 | 0.02 | 0.9 | 50 | 94.20% | 37.3s |
| 7 - Optimized | 200 | 512 | 0.03 | 0.9 | 50 | **96.84%** | 50.8s |
| 8 - Aggressive | 150 | 256 | 0.05 | 0.8 | 30 | 93.50% | 44.6s |

### MLP Analysis
**Best configuration:** Config 7 (Optimized) with **96.84% accuracy**

**Key observations:**
- **LR**: A moderate learning rate (0.03) performed better than both high (0.05) and low (0.01) values. The high LR showed instability (93.20%), while the low LR converged too slowly.
- **Training duration**: More training steps (200 vs 100) significantly improved accuracy (+1.3% from Config 1 to Config 2), and combining it with a slightly higher LR (Config 7) achieved the best results.
- **Batch size**: Standard batch size (512) outperformed both smaller (256) and larger (1024) batches, providing a good balance between gradient stability and convergence speed.

## CNN (Convolutional Neural Network)

### Tested Configurations

| Config | STEPS | BATCH | LR | LR_DECAY | PATIENCE | Accuracy | Time |
|--------|-------|-------|-----|----------|----------|----------|------|
| 1 - Baseline | 100 | 512 | 0.02 | 0.9 | 50 | 98.20% | 302.5s |
| 2 - More training | 200 | 512 | 0.02 | 0.9 | 50 | 98.75% | 582.5s |
| 3 - High LR | 100 | 512 | 0.05 | 0.9 | 50 | 97.80% | 294.3s |
| 4 - Low LR | 100 | 512 | 0.01 | 0.9 | 50 | 98.10% | 295.8s |
| 5 - Small batch | 100 | 256 | 0.02 | 0.9 | 50 | 98.30% | 180.8s |
| 6 - Large batch | 100 | 1024 | 0.02 | 0.9 | 50 | 98.15% | 2482.7s |
| 7 - Optimized | 200 | 512 | 0.03 | 0.9 | 50 | **99.00%** | 603.5s |
| 8 - Aggressive | 150 | 256 | 0.05 | 0.8 | 30 | 97.90% | 260.2s |

### CNN Analysis

**Best configuration:** Config 7 (Optimized) with **99.00% accuracy**

**Key observations:**
- **Superior performance**: CNN significantly outperformed MLP across all configurations, with even the baseline achieving 98.20% accuracy.
- **Learning rate sensitivity**: Similar to MLP, a moderate LR (0.03) worked best. High LR (0.05) reduced accuracy to 97.80%, showing that CNNs are also sensitive to aggressive learning rates.
- **Training duration importance**: Extended training (200 steps) combined with optimal LR pushed accuracy to 99.00%, demonstrating that CNNs benefit substantially from longer training.
- **Batch size impact**: Smaller batches (256) trained faster but didn't improve accuracy. Large batches (1024) were extremely slow (2482.7s) without significant accuracy gains.

## MLP vs CNN Comparison

### Results

| Metric | MLP | CNN |
|--------|-----|-----|
| **Best accuracy** | 96.84% | 99.00% |
| **Average training time** | 41.2s | 575.3s |
| **Number of parameters** | ~660,000 | ~140,000 |
| **Inference time (WebGPU)** | ~15ms | ~20ms |
