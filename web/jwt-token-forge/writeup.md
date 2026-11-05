# Writeup: TokenForge (Web Exploitation)

- **Competition**: BSides Agra CTF
- **Category**: Web Security / Authentication
- **Points**: 350
- **Target**: `http://challenges.bsidesagra.ctf/api/admin-flag`

---

## 1. Vulnerability Analysis
During reconnaissance, the application authenticated users via standard JSON Web Tokens (JWT). Inspecting the token header revealed:
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

Testing the JWT verification endpoint showed that the backend library did not enforce a strict algorithm whitelist. Specifically, it permitted tokens where `alg` was modified to `none`.

---

## 2. Exploitation Steps
1. Decoded the payload and altered `role` from `"user"` to `"administrator"`, setting `"is_admin": true`.
2. Modified the header to `{"alg": "none", "typ": "JWT"}`.
3. Removed the cryptographic signature portion, ending the token with a trailing dot (`header.payload.`).
4. Submitted the forged token in the `Authorization: Bearer <token>` header to the restricted `/api/admin-flag` endpoint.

```bash
python3 exploit.py
```

### Result:
```text
flag{jwt_alg_confusion_bypass_2024}
```

---

## 3. Remediation & Defense
- Hardcode the expected signing algorithm: `jwt.verify(token, secret, algorithms=['HS256'])`.
- Never trust client-specified `alg` parameters without server-side policy enforcement.