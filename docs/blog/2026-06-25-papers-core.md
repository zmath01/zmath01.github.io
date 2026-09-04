# Papers Core

Adam: A Method for Stochastic Optimization
Authors: Diederik P. Kingma, Jimmy Ba
First Author: Diederik P. Kingma
Year: 2014
Citations: 180,000
arXiv: 1412.6980
https://arxiv.org/abs/1412.6980

<!--more-->

## 1. Core Mathematical Formulas in "Adam: A Method for Stochastic Optimization"

The paper **"Adam: A Method for Stochastic Optimization"** by Diederik P. Kingma and Jimmy Ba (arXiv:1412.6980) introduces an algorithm that combines the advantages of **AdaGrad** and **RMSProp**. The mathematics focuses on estimating the first and second moments of the gradients to adaptively adjust learning rates for each parameter.

### 1. Gradient Computation
At each time step $t$, the algorithm computes the gradient of the stochastic objective function:

$$g_t = \nabla_\theta f_t(\theta_{t-1})$$

*   **$g_t$**: The gradient vector at time step $t$. It contains the partial derivatives of the loss function with respect to the parameters $\theta$.
*   **$\nabla_\theta$**: The gradient operator with respect to the parameter vector $\theta$.
*   **$f_t(\theta)$**: The stochastic objective function (loss) at time step $t$. This is typically the loss computed on a mini-batch of data.
*   **$\theta_{t-1}$**: The vector of model parameters at the previous time step $t-1$.
*   **$t$**: The current time step (iteration number), starting from $1$.

### 2. Biased First Moment Estimate (Momentum)
Adam maintains an exponentially decaying average of past gradients, similar to momentum:

$$m_t = \beta_1 m_{t-1} + (1 - \beta_1) g_t$$

*   **$m_t$**: The biased first moment estimate (mean of gradients) at time $t$.
*   **$m_{t-1}$**: The first moment estimate from the previous time step.
*   **$\beta_1$**: The exponential decay rate for the first moment. The paper suggests a default value of **0.9**. It controls how much weight is given to past gradients versus the current gradient.
*   **$g_t$**: The current gradient.
*   **$(1 - \beta_1)$**: The weight assigned to the current gradient.

This equation effectively smooths the gradient signal, reducing variance and helping the optimizer move consistently in the right direction.

### 3. Biased Second Raw Moment Estimate (Uncentered Variance)
Adam also maintains an exponentially decaying average of past *squared* gradients, similar to RMSProp:

$$v_t = \beta_2 v_{t-1} + (1 - \beta_2) g_t^2$$

*   **$v_t$**: The biased second raw moment estimate (uncentered variance of gradients) at time $t$.
*   **$v_{t-1}$**: The second moment estimate from the previous time step.
*   **$\beta_2$**: The exponential decay rate for the second moment. The paper suggests a default value of **0.999**.
*   **$g_t^2$**: The element-wise square of the current gradient ($g_t \odot g_t$). Squaring ensures all values are positive and emphasizes large gradients.
*   **$(1 - \beta_2)$**: The weight assigned to the current squared gradient.

This term adapts the learning rate: parameters with large, volatile gradients get smaller updates, while those with small, consistent gradients get larger updates.

### 4. Bias Correction
Since $m_t$ and $v_t$ are initialized as vectors of zeros, they are biased towards zero, especially during the initial time steps (when $t$ is small). Adam corrects this bias:

$$\hat{m}_t = \frac{m_t}{1 - \beta_1^t}$$

$$\hat{v}_t = \frac{v_t}{1 - \beta_2^t}$$

*   **$\hat{m}_t$**: The bias-corrected first moment estimate.
*   **$\hat{v}_t$**: The bias-corrected second raw moment estimate.
*   **$1 - \beta_1^t$**: The bias correction term for the first moment. As $t$ increases, $\beta_1^t$ approaches 0, and the denominator approaches 1, making the correction negligible in later stages.
*   **$1 - \beta_2^t$**: The bias correction term for the second moment.
*   **$t$**: The current time step.

Without this correction, the initial updates would be very small because $m_t$ and $v_t$ start near zero.

### 5. Parameter Update Rule
The final step updates the parameters using the corrected moments:

$$\theta_t = \theta_{t-1} - \alpha \cdot \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}$$

*   **$\theta_t$**: The updated parameter vector at time $t$.
*   **$\theta_{t-1}$**: The parameter vector from the previous time step.
*   **$\alpha$**: The **learning rate** (step size). The paper suggests a default of **0.001**. It scales the overall magnitude of the update.
*   **$\hat{m}_t$**: The bias-corrected first moment (direction).
*   **$\sqrt{\hat{v}_t}$**: The square root of the bias-corrected second moment (scale). This term normalizes the update by the magnitude of recent gradients.
*   **$\epsilon$**: A small constant added for numerical stability to prevent division by zero. The paper suggests **$10^{-8}$**.
*   **$\frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}$**: The adaptive update term. This effectively divides the learning rate for each parameter individually based on the history of its gradients.

### Summary of Hyperparameters
The paper recommends the following default values, which work well for most deep learning problems:

*   **$\alpha = 0.001$**: Learning rate.
*   **$\beta_1 = 0.9$**: Decay rate for the first moment.
*   **$\beta_2 = 0.999$**: Decay rate for the second moment.
*   **$\epsilon = 10^{-8}$**: Numerical stability constant.

These values require little tuning, making Adam a robust "out-of-the-box" optimizer.

---

Deep Residual Learning for Image Recognition
Authors: Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun
First Author: Kaiming He
Year: 2015
Citations: 130,000
arXiv: 1512.03385
https://arxiv.org/abs/1512.03385

## 2. Core Mathematical Formulas in "Deep Residual Learning for Image Recognition"

The paper **"Deep Residual Learning for Image Recognition"** by Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun (arXiv:1512.03385) introduces the Residual Network (ResNet) architecture. The mathematics centers on reformulating the layers to learn residual functions rather than direct mappings.

### 1. The Fundamental Residual Formula
The primary equation defining the residual block is:

$$\mathbf{y} = \mathcal{F}(\mathbf{x}, \{W_i\}) + \mathbf{x}$$

*   **$\mathbf{y}$**: The output vector of the residual block (before the final activation function).
*   **$\mathbf{x}$**: The input vector to the residual block. This represents the feature maps entering the block.
*   **$\mathcal{F}(\mathbf{x}, \{W_i\})$**: The **residual mapping** to be learned. This is the function represented by the stacked layers (the "shortcut" path).
    *   **$\mathcal{F}$**: The residual function itself. In the basic 2-layer block, $\mathcal{F} = W_2 \sigma(W_1 \mathbf{x})$.
    *   **$\{W_i\}$**: The set of weight matrices (and biases, though often omitted in notation for brevity) for the layers within the block. For a 2-layer block, this includes $W_1$ and $W_2$.
*   **$+$**: Element-wise addition. This operation adds the original input $\mathbf{x}$ directly to the output of the stacked layers. This requires $\mathbf{x}$ and $\mathcal{F}(\mathbf{x})$ to have the same dimensions.

The paper posits that instead of approximating a desired underlying mapping $\mathcal{H}(\mathbf{x})$ directly, the network approximates the residual $\mathcal{F}(\mathbf{x}) = \mathcal{H}(\mathbf{x}) - \mathbf{x}$. Thus, the original mapping becomes $\mathcal{H}(\mathbf{x}) = \mathcal{F}(\mathbf{x}) + \mathbf{x}$.

### 2. The Two-Layer Residual Block Expansion
For the specific case of a block with two layers (the most common configuration in the paper), the residual function $\mathcal{F}$ is expanded as:

$$\mathcal{F}(\mathbf{x}) = W_2 \sigma(W_1 \mathbf{x})$$

Substituting this into the main equation:

$$\mathbf{y} = W_2 \sigma(W_1 \mathbf{x}) + \mathbf{x}$$

*   **$W_1$**: The weight matrix (or convolutional kernel set) of the first layer in the block.
*   **$W_2$**: The weight matrix (or convolutional kernel set) of the second layer in the block.
*   **$\sigma$**: The **ReLU** (Rectified Linear Unit) activation function, defined as $\sigma(z) = \max(0, z)$. The paper notes that biases are omitted in this notation for simplicity but are present in implementation.
*   **$\mathbf{x}$**: The input to the first layer.

The final output of the block, after the element-wise addition, is passed through another ReLU activation: $\text{output} = \sigma(\mathbf{y}) = \sigma(\mathcal{F}(\mathbf{x}) + \mathbf{x})$.

### 3. Dimension Matching (Projection Shortcut)
When the dimensions of the input $\mathbf{x}$ and the residual output $\mathcal{F}(\mathbf{x})$ do not match (e.g., when changing the number of feature maps or downsampling spatial resolution), a linear projection $W_s$ is introduced:

$$\mathbf{y} = \mathcal{F}(\mathbf{x}, \{W_i\}) + W_s \mathbf{x}$$

*   **$W_s$**: A learnable weight matrix (implemented as a **$1 \times 1$ convolution**) that projects $\mathbf{x}$ to the correct dimensions to match $\mathcal{F}(\mathbf{x})$.
*   **$W_s \mathbf{x}$**: The projected input. This replaces the simple identity mapping $\mathbf{x}$ used when dimensions match.

The paper compares this "Option B" against "Option A" (zero-padding extra channels), finding that $W_s$ provides a slight accuracy improvement at the cost of additional parameters.

### 4. Generalization to Deep Stacks
For a network composed of $L$ such residual units, the output of the $l$-th layer $x_l$ can be expressed recursively. If $h(x_l) = x_l$ (identity shortcut) and $f$ is the post-addition activation (ReLU):

$$x_{l+1} = f(x_l + \mathcal{F}(x_l, W_l))$$

*   **$x_l$**: Input to the $l$-th residual unit.
*   **$x_{l+1}$**: Output of the $l$-th residual unit (and input to the next).
*   **$W_l$**: Weights specific to the $l$-th unit.
*   **$f$**: The ReLU activation function applied after the addition.

This recursive addition allows gradients to flow directly through the shortcut connections ($\frac{\partial \mathbf{y}}{\partial \mathbf{x}} = \frac{\partial \mathcal{F}}{\partial \mathbf{x}} + 1$), mitigating the vanishing gradient problem in very deep networks.


---

Why Does Deep and Cheap Learning Work So Well?
Authors: Henry W. Lin, Max Tegmark
First Author: Henry W. Lin
Year: 2016
Citations: 1,000
https://arxiv.org/abs/1608.08225

## 3. Why Does Deep and Cheap Learning Work So Well? -- Clarification on the Paper Title

(published in *Journal of Statistical Physics*, 2017)

The core argument is that deep learning succeeds because the physical laws governing our universe generate data with specific mathematical properties (symmetry, locality, compositionality) that neural networks are uniquely efficient at approximating.

## Explanation of Key Mathematical Symbols and Formulas

The paper relies on concepts from statistical physics and information theory to map probability distributions onto neural network architectures. Below are the primary formulas and the definitions of their symbols.

### 1. The Boltzmann Form of Probability
The authors recast Bayes' theorem into a form resembling the Boltzmann distribution from statistical mechanics to analyze the probability of a class $x$ given data $y$.

$$p(x|y) = \frac{1}{Z(y)} e^{-[H_x(y) + \mu_x]}$$

*   **$p(x|y)$**: The conditional probability that the class is $x$ given the observed data $y$.
*   **$Z(y)$**: The partition function (normalization constant), defined as $Z(y) = \sum_x e^{-[H_x(y) + \mu_x]}$. It ensures the probabilities sum to 1.
*   **$e$**: Euler's number, the base of the natural logarithm.
*   **$H_x(y)$**: The "Hamiltonian" or energy function, defined as $H_x(y) = -\ln p(y|x)$. In physics, this represents energy; in information theory, it is the self-information or negative log-likelihood of the data given the class.
*   **$\mu_x$**: The prior term, defined as $\mu_x = -\ln p(x)$. This represents the negative log-probability of the class $x$ occurring before seeing any data.
*   **$\ln$**: The natural logarithm.

### 2. Polynomial Expansion of the Hamiltonian
To demonstrate that neural networks can efficiently compute these probabilities, the authors expand the Hamiltonian $H_x(y)$ as a power series (polynomial).

$$H_x(y) = h + \sum_i h_i y_i + \sum_{i \le j} h_{ij} y_i y_j + \sum_{i \le j \le k} h_{ijk} y_i y_j y_k + \dots$$

*   **$h$**: A constant bias term (zeroth-order coefficient).
*   **$y_i, y_j, y_k$**: Components of the input data vector $y$ (e.g., pixel values or spin states).
*   **$h_i, h_{ij}, h_{ijk}$**: Coefficients of the polynomial expansion. These represent the interaction strengths between input variables (e.g., $h_{ij}$ captures pairwise correlations).
*   **$\sum$**: The summation symbol, indicating the sum over all specified indices.
*   **$i \le j$**: A constraint on the summation indices to avoid double-counting symmetric interaction terms (since $y_i y_j = y_j y_i$).

The paper argues that physical laws typically involve only low-order terms (usually up to degree 2, 3, or 4), making this series converge rapidly and allowing simple networks to approximate it.

### 3. Neural Network Approximation of Multiplication
A key mathematical hurdle is showing that neurons can perform multiplication (required for the $y_i y_j$ terms) using only addition and non-linear activation. The authors derive an approximation for multiplication $m(u, v) \approx uv$ using a smooth activation function $\sigma$ (like sigmoid or softplus).

$$m(u, v) = \frac{\sigma(u+v) + \sigma(-u-v) - \sigma(u-v) - \sigma(-u+v)}{8\sigma_2}$$

*   **$m(u, v)$**: The constructed function that approximates the product $uv$.
*   **$\sigma(\cdot)$**: The non-linear activation function of the neuron.
*   **$u, v$**: Scaled input variables.
*   **$\sigma_2$**: The second-order coefficient in the Taylor expansion of $\sigma(x) \approx \sigma_0 + \sigma_1 x + \sigma_2 x^2 + \dots$. This term must be non-zero for the approximation to work.
*   **$8\sigma_2$**: A normalization factor derived from the Taylor series algebra to isolate the $uv$ term.

This formula proves that a network with just a few hidden units can simulate multiplication, and by extension, any polynomial.

### 4. Vector Notation for Softmax
When dealing with discrete classes, the probability distribution is often written in vector notation, equating the Boltzmann form to the softmax function used in deep learning.

$$\mathbf{p}(\mathbf{x}) = \boldsymbol{\sigma}[-\mathbf{H}(\mathbf{x}) - \boldsymbol{\mu}]$$

*   **$\mathbf{p}(\mathbf{x})$**: A vector where each element is the probability $p(x|y)$ for a specific class $x$.
*   **$\boldsymbol{\sigma}$**: The softmax function applied to a vector, defined as $\sigma(\mathbf{z})_i = \frac{e^{z_i}}{\sum_j e^{z_j}}$.
*   **$\mathbf{H}(\mathbf{x})$**: A vector of Hamiltonians for each class.
*   **$\boldsymbol{\mu}$**: A vector of prior terms for each class.
*   **$-\mathbf{H}(\mathbf{x}) - \boldsymbol{\mu}$**: The input logit vector to the softmax layer, representing the negative energy of each state.

### 5. Hierarchical Composition
The paper describes deep networks as a composition of functions, reflecting the hierarchical structure of physical data.

$$f(\mathbf{v}) = \sigma_L A_L \dots \sigma_2 A_2 \sigma_1 A_1 \mathbf{v}$$

*   **$f(\mathbf{v})$**: The final output function of the network.
*   **$\mathbf{v}$**: The input vector.
*   **$A_k$**: Affine transformation matrices at layer $k$ (representing weights and biases: $A_k \mathbf{v} = W_k \mathbf{v} + b_k$).
*   **$\sigma_k$**: Element-wise non-linear activation functions at layer $k$.
*   **$L$**: The total number of layers in the network.

This structure allows the network to compute complex polynomials efficiently by reusing intermediate results (multiplications) across layers, a property known as **compositionality**.

---

Attention Is All You Need
Authors: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin
First Author: Ashish Vaswani
Year: 2017
Citations: 150,000
arXiv: 1706.03762
https://arxiv.org/abs/1706.03762

# 4. Core Mathematical Formulas in "Attention Is All You Need"

The paper **"Attention Is All You Need"** by Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, and Illia Polosukhin (arXiv:1706.03762) introduces the Transformer architecture. The mathematics defines how the model processes sequences using attention mechanisms rather than recurrence.

### 1. Scaled Dot-Product Attention
This is the fundamental operation of the Transformer, replacing recurrent layers.

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

*   **$\text{Attention}(Q, K, V)$**: The output matrix of the attention mechanism.
*   **$Q$**: The **Query** matrix. Each row represents a query vector for a specific position in the sequence.
*   **$K$**: The **Key** matrix. Each row represents a key vector for a specific position.
*   **$V$**: The **Value** matrix. Each row represents the value vector (the actual content) for a specific position.
*   **$K^T$**: The transpose of the Key matrix. This allows the dot product between queries (rows of $Q$) and keys (columns of $K^T$).
*   **$QK^T$**: The matrix of dot products between all queries and all keys. High values indicate strong similarity or relevance between a query and a key.
*   **$d_k$**: The dimension of the key (and query) vectors.
*   **$\sqrt{d_k}$**: The scaling factor. Dividing by the square root of the dimension prevents the dot products from becoming too large in magnitude, which would push the softmax function into regions with extremely small gradients (vanishing gradients).
*   **$\text{softmax}(\dots)$**: The softmax function applied row-wise. It normalizes the scaled scores into a probability distribution (values between 0 and 1 that sum to 1). These are the **attention weights**.
*   **$\dots V$**: The multiplication of the attention weights by the Value matrix. This computes a weighted sum of the values, where relevant values (high attention weight) contribute more to the output.

### 2. Multi-Head Attention
This mechanism allows the model to jointly attend to information from different representation subspaces at different positions.

$$\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \dots, \text{head}_h)W^O$$

where each head is computed as:

$$\text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$$

*   **$\text{MultiHead}(Q, K, V)$**: The final output of the multi-head attention layer.
*   **$\text{Concat}(\dots)$**: The concatenation operation. It joins the output matrices of all $h$ heads along the feature dimension.
*   **$\text{head}_i$**: The output of the $i$-th attention head.
*   **$h$**: The total number of attention heads (e.g., 8 in the base model).
*   **$W^O$**: The learnable weight matrix for the final linear projection. It maps the concatenated output back to the model dimension $d_{\text{model}}$.
*   **$W_i^Q$**: The learnable weight matrix projecting $Q$ for the $i$-th head. Dimensions: $d_{\text{model}} \times d_k$.
*   **$W_i^K$**: The learnable weight matrix projecting $K$ for the $i$-th head. Dimensions: $d_{\text{model}} \times d_k$.
*   **$W_i^V$**: The learnable weight matrix projecting $V$ for the $i$-th head. Dimensions: $d_{\text{model}} \times d_v$.
*   **$QW_i^Q, KW_i^K, VW_i^V$**: The projected Query, Key, and Value matrices specific to head $i$. Each head operates in a lower-dimensional subspace ($d_k = d_v = d_{\text{model}}/h$).

### 3. Positional Encodings
Since the Transformer contains no recurrence or convolution, it requires explicit injection of position information using sine and cosine functions.

$$PE_{(\text{pos}, 2i)} = \sin\left(\frac{\text{pos}}{10000^{2i/d_{\text{model}}}}\right)$$

$$PE_{(\text{pos}, 2i+1)} = \cos\left(\frac{\text{pos}}{10000^{2i/d_{\text{model}}}}\right)$$

*   **$PE_{(\text{pos}, \dots)}$**: The positional encoding vector element.
*   **$\text{pos}$**: The position of the token in the sequence (e.g., 0, 1, 2, ...).
*   **$i$**: The dimension index within the embedding vector, ranging from $0$ to $d_{\text{model}}/2 - 1$.
*   **$2i$**: Even indices of the embedding vector. These are assigned the sine function.
*   **$2i+1$**: Odd indices of the embedding vector. These are assigned the cosine function.
*   **$d_{\text{model}}$**: The dimension of the model's embedding space (e.g., 512).
*   **$10000$**: A scaling constant chosen to create a geometric progression of wavelengths.
*   **$10000^{2i/d_{\text{model}}}$**: The denominator determining the wavelength for dimension $i$. It forms a geometric progression from $2\pi$ to $10000 \cdot 2\pi$.
*   **$\sin, \cos$**: The sine and cosine trigonometric functions.

The final input to the encoder/decoder is the sum of the token embedding $E_{\text{token}}$ and the positional encoding: $x = E_{\text{token}} + PE$. This design allows the model to easily learn to attend to relative positions because $PE_{\text{pos}+k}$ can be represented as a linear function of $PE_{\text{pos}}$ for any fixed offset $k$.

### 4. Feed-Forward Network (Position-wise)
Each position in the encoder and decoder stacks contains a fully connected feed-forward network applied independently to each position.

$$\text{FFN}(x) = \max(0, xW_1 + b_1)W_2 + b_2$$

*   **$\text{FFN}(x)$**: The output of the feed-forward network for input $x$.
*   **$x$**: The input vector at a specific position (output of the attention layer).
*   **$W_1$**: The weight matrix of the first linear layer. Dimensions: $d_{\text{model}} \times d_{ff}$ (where $d_{ff} = 2048$ in the base model).
*   **$b_1$**: The bias vector of the first linear layer.
*   **$xW_1 + b_1$**: The affine transformation of the first layer.
*   **$\max(0, \dots)$**: The **ReLU** (Rectified Linear Unit) activation function. It introduces non-linearity by zeroing out negative values.
*   **$W_2$**: The weight matrix of the second linear layer. Dimensions: $d_{ff} \times d_{\text{model}}$.
*   **$b_2$**: The bias vector of the second linear layer.
*   **$\dots W_2 + b_2$**: The final linear projection back to the model dimension $d_{\text{model}}$.
