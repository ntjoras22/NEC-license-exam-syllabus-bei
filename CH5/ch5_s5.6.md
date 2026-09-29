## Section Network Security (ACtE0506)

## 📖 1. Introduction
Network security encompasses the policies and practices adopted to prevent and monitor unauthorized access, misuse, modification, or denial of a computer network and network-accessible resources. In the NEC exam, you are expected to understand the cryptographic primitives and how they are applied across different network layers.

## 💡 2. Basic Concept & Security Goals
The foundational concepts of information security are often modeled as the CIA triad.

> [!NOTE] Definition
> **Security Goals (CIA Triad)**:
> 1. **Confidentiality**: Ensuring data is accessible only to authorized entities (preventing eavesdropping).
> 2. **Integrity**: Ensuring data is not altered in transit or at rest.
> 3. **Availability**: Ensuring systems and data are available to authorized users when needed (preventing DoS).
> Additional goals include **Authentication** (verifying identity) and **Non-repudiation** (preventing a sender from denying they sent a message).

## 3. Cryptography Basics
Cryptography is the mathematical foundation for achieving security goals.
*   **Plaintext**: Original message.
*   **Ciphertext**: Encrypted message.
*   **Encryption / Decryption**: $C = E_K(P)$ and $P = D_K(C)$

### 3.1 Symmetric-Key Algorithms
Both the sender and receiver use the *same* secret key. Fast and efficient for bulk encryption.
*   **DES (Data Encryption Standard)**: 64-bit block size, 56-bit key. Now considered insecure due to short key length.
*   **AES (Advanced Encryption Standard)**: 128-bit block size, 128/192/256-bit keys. The current global standard. Highly secure.

### 3.2 Asymmetric-Key Algorithms (Public-Key)
Uses a *pair* of keys: a Public Key (known to all) and a Private Key (kept secret by the owner).
*   **Encryption**: Sender encrypts with receiver's Public Key. Receiver decrypts with their Private Key.
*   **RSA (Rivest-Shamir-Adleman)**: Based on the mathematical difficulty of factoring the product of two large prime numbers.
    *   Key generation: Choose primes $p, q$. Compute $n=pq$. Compute $\phi(n) = (p-1)(q-1)$. Choose $e$ such that $1 < e < \phi(n)$ and $gcd(e, \phi(n)) = 1$. Compute $d \equiv e^{-1} \pmod{\phi(n)}$.
    *   Public key: $(e, n)$. Private key: $(d, n)$.
    *   Encryption: $C = P^e \pmod n$. Decryption: $P = C^d \pmod n$.

### Symmetric vs. Asymmetric

| Feature | Symmetric-Key | Asymmetric-Key |
| :--- | :--- | :--- |
| **Keys** | One shared secret key | Pair: Public and Private |
| **Speed** | Very fast | Slow (computationally heavy) |
| **Key Distribution** | Difficult (requires secure channel) | Easy (public keys are public) |
| **Use Case** | Bulk data encryption | Key exchange, digital signatures |

## 4. Message Integrity and Authentication

### 4.1 Hash Algorithms
A hash function maps an arbitrary length message to a fixed-length digest.
*   Properties: One-way (cannot reverse), Collision-resistant (hard to find two messages with same hash).
*   Examples: MD5 (128-bit, broken), SHA-1 (160-bit, broken), SHA-256 (secure).

### 4.2 Message Authentication Code (MAC)
Provides both integrity and authentication. It is a hash function keyed with a shared symmetric key. If the MAC matches, the receiver knows the message hasn't been altered AND it came from someone holding the secret key.

### 4.3 Digital Signatures
Provides integrity, authentication, and non-repudiation.
*   The sender hashes the message, then encrypts the hash with their **Private Key**. This encrypted hash is the signature.
*   The receiver decrypts the signature using the sender's **Public Key** and compares it to a locally calculated hash of the message.

## 5. Key Management and Public Key Infrastructure (PKI)
How do we know a public key really belongs to the person claiming it? We use **Digital Certificates**.
*   A Certificate Authority (CA) binds a public key to an entity's identity.
*   The CA digitally signs the certificate using the CA's private key.
*   X.509 is the standard format for digital certificates.

## 6. Security at Different Layers

### 6.1 Transport Layer Security (SSL/TLS)
Provides secure communication between two sockets (e.g., HTTPS).
*   Provides confidentiality (symmetric encryption), integrity (MAC), and authentication (certificates).
*   **Handshake**: Client and server negotiate cipher suites, authenticate the server (and optionally client), and securely exchange a shared master secret using RSA or Diffie-Hellman.

### 6.2 Network Layer Security (IPsec)
Secures IP packets between nodes. Can operate in two modes:
1.  **Transport Mode**: Encrypts only the IP payload (TCP/UDP segment). Used for host-to-host.
2.  **Tunnel Mode**: Encrypts the entire original IP packet and adds a new IP header. Used for VPNs (Gateway-to-Gateway).
*   **Protocols**: AH (Authentication Header - integrity only) and ESP (Encapsulating Security Payload - confidentiality and integrity).

### 6.3 Wireless LAN Security
*   **WEP (Wired Equivalent Privacy)**: Legacy. Highly flawed 24-bit initialization vector (IV) sent in plaintext. easily cracked.
*   **WPA / WPA2 / WPA3**: Modern standards. Use robust protocols like TKIP and CCMP (based on AES).

## 7. Firewalls
A network security system that monitors and controls incoming/outgoing traffic based on rules.
*   **Packet Filter**: Inspects IP/TCP/UDP headers. Fast but stateless.
*   **Stateful Firewall**: Tracks the state of active connections.
*   **Application Gateway (Proxy)**: Inspects application data (e.g., HTTP). Highly secure but slow.

## 💡 Common Mistakes / Exam Tips

> [!WARNING]
> Do not confuse the use of keys in encryption vs. digital signatures.
> **Encryption**: Sender uses Receiver's Public Key.
> **Signature**: Sender uses Sender's Private Key.

> [!TIP]
> IPsec operates at the Network Layer (Layer 3). SSL/TLS operates at the Transport Layer (Layer 4). Firewalls can operate at layers 3, 4, or 7.
> Remember the block sizes: DES=64-bit, AES=128-bit.

## 📝 Quick Reference / Formula Summary

> [!IMPORTANT]
> - RSA Modulus $n = p \times q$
> - Euler Totient $\phi(n) = (p-1) \times (q-1)$
> - RSA Encryption: $C = P^e \bmod n$
> - RSA Decryption: $P = C^d \bmod n$

## ✏️ Practice Problems

1.  **In an RSA algorithm, given primes $p=3$, $q=11$, and $e=7$. Find the decryption key $d$.**
    *Answer:*
    $n = p \times q = 33$
    $\phi(n) = (3-1)(11-1) = 2 \times 10 = 20$
    We need $d$ such that $(e \times d) \bmod \phi(n) = 1$.
    $(7 \times d) \bmod 20 = 1$.
    By testing values (or extended Euclidean algorithm), $7 \times 3 = 21 \equiv 1 \pmod{20}$.
    So, $d = 3$.

2.  **What is the primary difference between a MAC and a Digital Signature?**
    *Answer:* A MAC uses symmetric key cryptography, meaning it provides integrity and authentication but cannot provide non-repudiation (since both parties have the key, either could have generated the MAC). A digital signature uses asymmetric cryptography (sender's private key), providing integrity, authentication, AND non-repudiation.

3.  **Explain the difference between IPsec Tunnel Mode and Transport Mode.**
    *Answer:* Transport mode encrypts only the payload of the IP packet, leaving the original IP header intact. Tunnel mode encrypts the entire original IP packet and wraps it in a new outer IP header, making it suitable for Virtual Private Networks (VPNs) between routers over the public internet.
</Section 5.6: Network Security (ACtE0506)>
