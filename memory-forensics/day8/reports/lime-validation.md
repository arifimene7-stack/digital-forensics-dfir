# LiME Acquisition Tool Validation

## Environment
- OS: Ubuntu
- Kernel: 7.0.0-31-generic
- Secure Boot: Enabled
- Kernel headers: Available

## Installation
- Package: lime-forensics-dkms
- Version: 1.11.0
- DKMS build: Successful

## Module
- Name: lime
- Path: /lib/modules/7.0.0-31-generic/updates/dkms/lime.ko.zst
- Kernel compatibility: Matching vermagic
- Signature: PKCS#7
- Signer: Local Secure Boot Module Signature key (hostname redacted)
- Hash algorithm: SHA-512

## Signing Configuration
DKMS configuration references:
- /var/lib/shim-signed/mok/MOK.priv
- /var/lib/shim-signed/mok/MOK.der

The certificate is not enrolled in MOK.

## Limitations
- The module has not been loaded.
- No RAM image has been acquired.
- No Volatility memory-image analysis has been performed.
- Secure Boot configuration was not modified.

## Conclusion
LiME was successfully built and signed for the running kernel.
However, its loading has not been validated under the current Secure Boot
trust configuration. Memory acquisition remains incomplete.
