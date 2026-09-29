## Section 9.3 — Switching Systems and Traffic Engineering (AEiE0903)

## 📖 1. Introduction
This section explores the core routing mechanisms of telecommunication networks. It covers how calls and data are switched, how network traffic is engineered to ensure acceptable quality, and the signaling protocols used to control network resources.

## 💡 2. Basic Concept
Switching allows a network to connect multiple devices without requiring point-to-point connections between every single pair. Traffic engineering applies mathematical models to dimension the network appropriately for expected user demand.

> [!NOTE] Definition
> **Switching**: The process of establishing a connection from an inlet to an outlet in a switching network.
> **Traffic Engineering**: The application of teletraffic theory to the design and dimensioning of telecommunication networks.

## 3. Digital and Analog Switching
- **Analog Switching**: Early telephone networks used electromechanical switches (Strowger, Crossbar) to physically connect two copper wires. The signal remained analog throughout the network. Space Division Switching was primarily used.
- **Digital Switching**: Voice is digitized (e.g., PCM at 64 kbps). Switching is performed using time slots. Uses Time Division Switching (Time Slot Interchange - TSI) and Space Division Switching, often combined as Time-Space-Time (TST) or Space-Time-Space (STS) switches.

## 4. Concept of Soft Switching
A **Softswitch** is a central device in a telecommunications network which connects telephone calls from one type of network to another entirely by means of software running on a general-purpose computer system, rather than using specialized hardware.
- Separates the call control (signaling) from the media gateway (transport).
- Enables the integration of legacy PSTN networks with modern IP networks (VoIP).

## 5. Teletraffic Parameters
Key concepts for sizing telecommunication networks.

- **Traffic Intensity (A)**: The measure of average occupancy of a server or resource. Measured in Erlangs. 1 Erlang = 1 resource occupied for 1 continuous hour.

$$ A = \lambda \times H $$
  Where $\lambda$ is the call arrival rate (calls/hour), and $H$ is the average holding time (hours/call).
- **Busy Hour**: The continuous 60-minute period for which the traffic volume or number of call attempts is greatest. Network capacity is always designed for the busy hour.
- **Grade of Service (GoS)**: The probability that a call is blocked or delayed. A GoS of 0.01 means 1% of calls are blocked during the busy hour. For a blocked-calls-cleared system, GoS is calculated using the Erlang B formula.
- **Service Level**: A broader term than GoS, often incorporating GoS, delay metrics, and reliability metrics.

## 6. Traffic Routing in Wireless Networks
Routing determines the path a call takes from source to destination.
- In cellular networks, the Mobile Switching Center (MSC) routes calls.
- Routing must account for user mobility (roaming and handover).
- **Home Location Register (HLR)** and **Visitor Location Register (VLR)** are queried to find the current location of a mobile subscriber before routing the call.

## 7. Common Channel Signaling (CCS)
Signaling is the exchange of information specifically concerned with the establishment and control of connections.
- **Channel Associated Signaling (CAS)**: Signaling is carried in the same channel as the voice (e.g., in-band). Slow and insecure.
- **Common Channel Signaling (CCS)**: A separate, dedicated data network is used solely for signaling. Highly efficient, fast, and secure. SS7 (Signaling System 7) is the dominant CCS protocol used in PSTN and 2G/3G networks.

## 8. ISDN and Packet vs Circuit Switching
### Integrated Services Digital Network (ISDN)
A set of communication standards for simultaneous digital transmission of voice, video, data, and other network services over the traditional circuits of the PSTN.
- Basic Rate Interface (BRI): 2B + D (two 64 kbps data channels, one 16 kbps signaling channel).
- Primary Rate Interface (PRI): 30B + D (in Europe/Nepal) or 23B + D (in US).

### Packet Switching vs Circuit Switching for PCN (Personal Communication Networks)
| Feature | Circuit Switching | Packet Switching |
|---|---|---|
| **Path** | Dedicated path established before data transfer | No dedicated path; packets routed independently |
| **Bandwidth** | Reserved, even if idle | Shared on demand |
| **Delay** | Low and constant | Variable (queuing delay, jitter) |
| **Billing** | Time-based | Volume-based |
| **Suitability** | Real-time voice | Burst data, VoIP |

## 9. Protocol for Network Access
Network access protocols define how a user equipment connects to the network.
- **CSMA/CD** (Carrier Sense Multiple Access with Collision Detection): Used in wired Ethernet.
- **CSMA/CA** (Carrier Sense Multiple Access with Collision Avoidance): Used in wireless LANs (Wi-Fi) since collision detection is difficult over radio.
- **ALOHA / Slotted ALOHA**: Early random access protocols used in satellite and cellular networks for initial access requests.

## 💡 Common Mistakes / Exam Tips

> [!WARNING]
> Traffic intensity ($A$) is dimensionless but is expressed in units of Erlangs. Ensure your units for call arrival rate and holding time match (e.g., both in minutes or both in hours) before multiplying.

> [!TIP]
> GoS (Grade of Service) and QoS (Quality of Service) are different. GoS is a specific metric related to network capacity (blocking probability), while QoS is an umbrella term covering GoS, delay, jitter, bandwidth, etc.

## 📝 Quick Reference / Formula Summary

> [!IMPORTANT]
> - Traffic in Erlangs: $A = \lambda \times H$ (or $A = \frac{C \times h}{60}$ if $C$ is calls/min and $h$ is holding time in min).
> - Total traffic: $A_T = \text{number of subscribers} \times \text{traffic per subscriber}$.
> - Erlang B Formula (Blocking probability): $P_B = \frac{A^N / N!}{\sum_{k=0}^{N} (A^k / k!)}$, where $N$ is number of channels.

## ✏️ Practice Problems
1. A telephone exchange observes 120 calls in a busy hour. The average duration of each call is 3 minutes. Calculate the traffic intensity in Erlangs.
   *Answer sketch: Call arrival rate $\lambda = 120$ calls/hour. Holding time $H = 3/60 = 0.05$ hours. Traffic $A = 120 \times 0.05 = 6$ Erlangs.*

2. What is the fundamental difference between CAS and CCS?
   *Answer sketch: In CAS, signaling and voice share the same physical channel. In CCS, a separate out-of-band packet-switched network is dedicated entirely to carrying signaling messages for multiple voice channels.*

3. Why is packet switching more efficient than circuit switching for bursty data traffic?
   *Answer sketch: Circuit switching reserves a dedicated channel for the entire session, wasting capacity during idle periods. Packet switching dynamically shares resources, utilizing the channel only when there is actual data to send, leading to statistical multiplexing gains.*
</Section 9.3: Switching Systems and Traffic Engineering (AEiE0903)>
