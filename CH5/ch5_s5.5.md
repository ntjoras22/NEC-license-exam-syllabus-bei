## 🔧 Section Application Layer (ACtE0505)

## 📖 1. Introduction
The Application Layer is the topmost layer of both the OSI and TCP/IP models. It provides the interface between the applications we use to communicate and the underlying network over which our messages are transmitted. For the NEC exam, understanding how different application protocols function and the architectures they rely on is critical.

## 💡 2. Basic Concept
The application layer contains the protocols and services that applications use to exchange data over a network. It does not refer to the application programs themselves (like a web browser), but rather to the protocols they use (like HTTP).

> [!NOTE] Definition
> **Application Layer**: The layer that provides services directly to the user application. It establishes communication partners, determines resource availability, and synchronizes communication.

## 🔧 3. Application Architectures

### 3.1 Client-Server Model
*   **Server**: Always-on host, permanent IP address, typically in data centers for scaling.
*   **Client**: Communicates with server, may be intermittently connected, dynamic IP address, do not communicate directly with each other.
*   *Examples*: Web (HTTP), Email (SMTP/IMAP), File Transfer (FTP).

### 3.2 Peer-to-Peer (P2P) Model
*   No always-on server.
*   Arbitrary end systems (peers) directly communicate.
*   Peers request service from other peers, provide service in return to other peers.
*   Highly scalable but complex to manage.
*   *Examples*: BitTorrent, Skype.

## 4. DNS (Domain Name System)
DNS translates human-readable domain names (like www.google.com) into IP addresses (like 142.250.190.4).
*   **Protocol**: UDP (typically) on port 53.
*   **Hierarchy**: Root name servers -> Top-Level Domain (TLD) servers (.com, .org, .edu) -> Authoritative name servers.
*   **Resolution Methods**:
    1.  **Iterative**: The contacted server replies with the name of the server to contact next. "I don't know this name, but ask this server."
    2.  **Recursive**: Puts the burden of name resolution on the contacted name server.

## 5. Electronic Mail (SMTP, POP3, IMAP)
Email involves user agents (mail readers), mail servers, and protocols.

*   **SMTP (Simple Mail Transfer Protocol)**: Push protocol used to send mail from the sender's user agent to the sender's mail server, and from the sender's mail server to the receiver's mail server. Uses TCP port 25.
*   **POP3 (Post Office Protocol version 3)**: Pull protocol used by the receiver's user agent to download mail from the mail server. Usually "download and delete" mode. TCP port 110.
*   **IMAP (Internet Message Access Protocol)**: Pull protocol, more complex than POP3. Keeps all messages on the server, allowing user to organize messages in folders. State is maintained across sessions. TCP port 143.

## 6. File Transfer Protocol (FTP)
FTP is used to transfer files between computers. It is unique because it uses **two out-of-band TCP connections**.
1.  **Control Connection (Port 21)**: Used for sending commands and replies (authentication, directory listing). Remains open during the entire session.
2.  **Data Connection (Port 20)**: Used for the actual file transfer. A new data connection is opened for each file transferred and closed when the transfer is complete.

## 7. HTTP and WWW
The World Wide Web (WWW) is a repository of information distributed globally. HTTP (Hypertext Transfer Protocol) is the protocol used for web communication.
*   **Protocol**: TCP port 80.
*   **Characteristics**: Stateless (server maintains no information about past client requests).

### 7.1 HTTP Connections
*   **Non-Persistent HTTP**: At most one object sent over TCP connection. Connection closed. Downloading multiple objects requires multiple connections.
*   **Persistent HTTP**: Multiple objects can be sent over a single TCP connection between client and server. Standard in HTTP/1.1.

### 7.2 HTTP Messages
*   **Request Methods**: `GET` (request document), `POST` (send data to server), `HEAD` (request headers only), `PUT` (upload file).
*   **Response Codes**:
    *   2xx: Success (e.g., 200 OK)
    *   3xx: Redirection (e.g., 301 Moved Permanently)
    *   4xx: Client Error (e.g., 404 Not Found)
    *   5xx: Server Error (e.g., 500 Internal Server Error)

## 8. SNMP (Simple Network Management Protocol)
SNMP is an application-layer protocol used to manage and monitor network devices.
*   **Components**: Managed devices (contain SNMP agents), Management Information Base (MIB, a database of variables), and Network Management System (NMS, the manager).
*   **Protocol**: UDP ports 161 (Agent) and 162 (Manager/Traps).
*   **Operations**: Get, GetNext, Set (Manager to Agent), and Trap (Agent sends unsolicited alert to Manager).

## 💡 Common Mistakes / Exam Tips

> [!WARNING]
> Do not confuse the roles of SMTP and POP3/IMAP. SMTP is *only* for sending/pushing emails. POP3/IMAP are for receiving/pulling emails.

> [!TIP]
> Remember the port numbers: FTP (20, 21), SSH (22), Telnet (23), SMTP (25), DNS (53), HTTP (80), POP3 (110), IMAP (143), SNMP (161/162), HTTPS (443).
> FTP is "out-of-band" because control and data are on separate ports. HTTP is "in-band".

## 📝 Quick Reference / Formula Summary

> [!IMPORTANT]
> | Protocol | Transport | Port | Function |
| :--- | :--- | :--- | :--- |
| DNS | UDP | 53 | Hostname to IP translation |
| HTTP | TCP | 80 | Web document transfer |
| SMTP | TCP | 25 | Email transfer (push) |
| POP3/IMAP | TCP | 110/143 | Email retrieval (pull) |
| FTP | TCP | 20, 21 | File transfer (data, control) |

## ✏️ Practice Problems

1.  **If a web page consists of a base HTML file and 5 JPEG images, how many TCP connections are required to download the page using non-persistent HTTP? How many for persistent HTTP?**
    *Answer:* Non-persistent: 1 + 5 = 6 separate TCP connections. Persistent: 1 TCP connection.

2.  **Describe the difference between an iterative and recursive DNS query.**
    *Answer:* In a recursive query, the contacted DNS server does the work of querying other servers on behalf of the client until it gets the IP address. In an iterative query, the contacted server simply returns the address of the next DNS server to ask, and the client (or local DNS server) must make the next query itself.

3.  **Why does FTP use two separate ports?**
    *Answer:* FTP uses out-of-band control. Port 21 is used for control commands (login, cd, ls) which require low bandwidth but continuous connection. Port 20 is used for actual bulk data transfer, establishing and tearing down connections as needed without dropping the control session.
</Section 5.5: Application Layer (ACtE0505)>
