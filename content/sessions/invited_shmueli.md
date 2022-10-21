---
title: "Invited: Semi-quantum Unclonable Cryptography (Chair: Kai-Min Chung)"
speakers:
  - shmueli
videoId: B1YoiZkwjo0
presentation: null
draft: false
---
Abstract: Quantum token schemes are executed in a system of quantum computers, and allow a quantum sender to sample a quantum state which is unclonable to everyone in the system, but also publicly verifiable.
Such schemes imply powerful primitives like public-key quantum money, and are at the heart of quantum cryptography.
While quantum token schemes allow to realize high-end tasks, their main drawback is that they require a strong computational model to be implemented - quantum computation and a quantum communication infrastructure.

A central open question in the field was whether we can have a stronger primitive, called a Semi-quantum Token scheme, that achieves the same functionality, only having a classical sender. Such primitive is known to imply quantum token schemes relying only on local quantum computation and classical communication. The question of the existence of such schemes (first defined as Semi-quantum Money) was first posed by Radian and Sattath (AFT 2019), and since, no construction was known under any computational assumption.

In this talk we explain how to construct a semi-quantum token scheme, assuming quantum-secure Indistinguishability Obfuscation for classical circuits, and the quantum sub-exponential hardness of the Learning with Errors problem. The technical centerpiece of the construction is a 3-message protocol where a classical computer can delegate to a (possibly malicious) quantum computer the generation of a quantum state which is unclonable and publicly verifiable.


<!-- fields to use above: -->
<!-- videoId: "Vfl9pPh6ipI" -->
<!-- presentation: "/slides/invited-MargaridaPereira.pdf" -->
