# Coverage E2E — Auth > Login with OTP

Sumber: `auth/login-otp/TestCases/tc-login-otp.md` (185 TC aktif). Suite: `specs/Auth/LoginOtp/`. Status seluruh spec: `draft`, belum ada script Playwright / TestSpectra.

**Verifikasi lint:** `npx spectra lint --strict specs/Auth/LoginOtp` → `✓ 27 specs and 1 suites verified. All spec schemas are valid. 0 lint errors found.`

**Aturan seleksi:** sesuai `docs/e2e-conventions.md` bagian 2, spec e2e merangkap fungsionalitas dan skenario FE. Seluruh 185 TC granular masuk ke dalam spec tanpa pengecualian. Skenario yang membutuhkan intercept kegagalan server, timeout jaringan, manipulasi response, threshold rate-limit IP, atau direct API harness ditandai `Mode: mock` di `## Prerequisites`. Hambatan teknis, ketergantungan mail-catcher, manipulasi waktu server, atau label manual dicatat di `## Prerequisites` sebagai sumber rujukan resmi implementasi otomasi bagi tim FE, bukan alasan mengeluarkan TC.

**Nomor folder:** Prefix `TC-AUTH-OTP-E2E-` berasal dari `ModulBesar = AUTH` dan `SubModul = OTP` sesuai registri resmi `foundation/tc-prefix-registry.md`. Nomor `001` sampai `027` adalah nomor urut spec dalam suite ini.

---

## TC granular → spec e2e

| Spec | Isi | TC sumber | Platform |
|---|---|---|---|
| TC-AUTH-OTP-E2E-001 | Screening halaman Request OTP (web), prefill email dari Login with Password, buka langsung, akses publik Read Only, dan sanitasi input | 01, 03, 04, 05, 10, 101, 157 | web |
| TC-AUTH-OTP-E2E-002 | Screening halaman Request OTP di mobile (tanpa reCAPTCHA), keypad numerik & autofokus kotak digit, Google Play Integrity token attestation valid & invalid (EC-51, EC-52), dan Verify tanpa attestation/reCAPTCHA (EC-53) | 02, 08, 180, 185 | **mobile** |
| TC-AUTH-OTP-E2E-003 | Validasi field Email: kosong, format regex tanpa @ / tanpa domain, TLD 2 karakter (.co), batas 120 karakter real-time, trim spasi luar, dan hirarki evaluasi | 11, 12, 13, 14, 15, 16, 17, 18, 167, 168 | web |
| TC-AUTH-OTP-E2E-004 | Proteksi reCAPTCHA gate web: blokir submit tanpa centang, hilangnya caption saat dicentang, urutan evaluasi Email sebelum reCAPTCHA, reCAPTCHA sebelum status akun, dan token sekali pakai | 22, 23, 24, 25, 26, 27 | web |
| TC-AUTH-OTP-E2E-005 | Evaluasi status akun pra-request: email belum terdaftar (tanpa log), akun belum aktivasi (Note `Account not activated`), dan akun inactive (Note `Account is inactive`) | 19, 20, 21 | web |
| TC-AUTH-OTP-E2E-006 | Request OTP berhasil, transisi Verify OTP, state loading disabled, idempotensi double-click, integritas subject/konten template email, dan SLA delivery < 2 menit | 28, 29, 30, 37, 38, 39 | web |
| TC-AUTH-OTP-E2E-007 | Penanganan kegagalan server 5xx dan network timeout pada Request OTP, toast error, form interaktif, dan reset widget reCAPTCHA | 31, 32 | web (`Mode: mock`) |
| TC-AUTH-OTP-E2E-008 | Batasan IP rate limit pada Request OTP, Resend, dan Verify OTP: status 429, agnostik pergantian email, preservasi input digit (NC-10), dan pencatatan log | 33, 34, 63, 85, 135 | web (`Mode: mock`) |
| TC-AUTH-OTP-E2E-009 | Navigasi pra-autentikasi: tautan Use password instead dan Back membawa email; auto-redirect pengguna yang sudah login ke Portal Product Hub | 06, 35, 36, 75, 76 | web |
| TC-AUTH-OTP-E2E-010 | Screening halaman Verify OTP, auto-advance kursor 1-5, digit ke-6 auto-submit & freeze form, backspace mundur, paste 6 digit, paste spasi/strip, paste > 6 digit, paste tengah, dan pembersihan error saat ketik ulang (NC-10) | 07, 40, 41, 42, 43, 44, 45, 46, 47, 69 | web |
| TC-AUTH-OTP-E2E-011 | Verifikasi OTP sukses happy path profil BASE ke Product Hub tanpa gate perantara, masa berlaku aktif < 5 menit, dan pencatatan simetris 1:1 di Activity Log Session & User Log | 48, 51, 100, 127, 136, 137 | web |
| TC-AUTH-OTP-E2E-012 | Validasi kode salah (NC-10), kedaluwarsa > 5 menit (NC-10), kode usang pasca-ganti, penonaktifan user di GS saat Verify (NC-04, NC-10), akun belum aktivasi saat Verify ditolak `Account is not activated` (EC-49), penghapusan user di GS saat Verify (NC-04, NC-10), dan independensi lock terhadap login password | 49, 50, 55, 61, 62, 68, 120, 123, 124, 133, 184 | web |
| TC-AUTH-OTP-E2E-013 | Fallback tombol [Verify] saat auto-submit gagal 5xx atau timeout: digit dipertahankan (NC-10), validasi OTP must not be empty, recovery saat server pulih, dan reset visual tombol | 56, 57, 58, 59, 60, 119, 131, 177 | web (`Mode: mock`) |
| TC-AUTH-OTP-E2E-014 | Invalidasi permanen kode OTP setelah 5x verifikasi salah pada kode yang sama (NC-05), batas toleransi 4x salah, dan reset counter kesalahan saat Resend menerbitkan kode baru | 65, 66, 67, 122 | web |
| TC-AUTH-OTP-E2E-015 | Siklus Resend: State A countdown 60s (MM:SS), State B aktif, reset timer, kuota 5x resend, cooldown 10 menit, transisi ke State Exhausted, kegagalan 5xx tidak memotong kuota, penolakan direct API, dan timer berbasis server | 77, 78, 79, 80, 81, 82, 83, 84, 130, 181, 183 | web |
| TC-AUTH-OTP-E2E-016 | Invarian tepat satu kode aktif per user: invalidasi kode lama pasca-Resend, invalidasi kode lama pasca-Edit email, penolakan kode lintas email/user, dan pencatatan log | 52, 53, 54, 64, 121, 125, 141 | web |
| TC-AUTH-OTP-E2E-017 | Alur Edit email dari Verify OTP: navigasi keyboard, form Request OTP terisi email, reCAPTCHA unchecked (NC-09), edit ke email baru, reset kuota saat exhausted via edit email (NC-03), dan Use password instead | 86, 87, 88, 89, 94, 95, 96 | web |
| TC-AUTH-OTP-E2E-018 | Penolakan Request OTP sesi sama selama cooldown 10m atau kuota habis (alert inline `Too many requests`), navigasi bolak-balik tidak mereset sesi, pembersihan storage lokal tidak membobol cooldown, dan penerimaan pasca-cooldown (NC-03) | 90, 91, 92, 93, 134, 166, 169, 170, 182 | web |
| TC-AUTH-OTP-E2E-019 | Preservasi state Verify OTP: reload F5 tetap di Verify (NC-08), tombol Back kembali ke Request OTP tanpa invalidasi kode (NC-08), dan akses URL langsung diarahkan ke Request OTP | 70, 71, 73, 179 | web |
| TC-AUTH-OTP-E2E-020 | Agreement Gate: screening Confirm to Continue, pemicu login pertama (profil FIRST), pemicu idle > 30 hari (profil IDLE), pemicu kebijakan privasi baru (profil POLICY), tautan modal tanpa memutus sesi, dan paritas dengan login password | 09, 97, 98, 99, 104, 142 | web |
| TC-AUTH-OTP-E2E-021 | Agreement Gate: submit tanpa centang diblokir ("You need to agree to the Privacy Policy to continue"), submit sah ke Product Hub, F5 saat token valid (NC-08), akses langsung tanpa token, token TTL 10m expired / abandoned (tidak dicatat, PRD §9.8), dan tampering | 72, 74, 102, 103, 105, 106, 107, 108, 109, 110, 111, 126, 128, 132 | web |
| TC-AUTH-OTP-E2E-022 | Handoff MFA Authenticator (TOTP) pasca-OTP: setup first login, prompt TOTP pada idle & perangkat baru (NEWDEV), pengiriman Login Alert email, dan alur gabungan Agreement + MFA (POLNEW) | 112, 113, 114, 115, 129, 174 | web |
| TC-AUTH-OTP-E2E-023 | Sinkronisasi status user Global Settings: pemulihan instan saat re-activated, akun baru diaktivasi langsung bisa OTP, perubahan email user di GS, Session Management concurrent session, dialog Duplicate Login Attempt (tampil & Cancel tidak dicatat, Confirm 1 entri Success per EC-50), dan terminasi sesi real-time saat dinonaktifkan admin | 138, 139, 140, 143, 175, 176 | web |
| TC-AUTH-OTP-E2E-024 | Plan Gating platform parity: akses OTP universal untuk Starter, Growth, Professional, Enterprise, Distributor, Partner, Principal; dan penolakan status tenant Client Suspended/Expired | 144, 145, 146, 147, 148, 149, 150, 151, 152 | web |
| TC-AUTH-OTP-E2E-025 | Pencatatan multi-surface log kegagalan pra-request: submit tanpa reCAPTCHA tidak dicatat di log, submit akun belum aktivasi dicatat `Account not activated`, dan akun inactive dicatat `Account is inactive` | 116, 117, 118 | web |
| TC-AUTH-OTP-E2E-026 | Security & Defense-in-Depth: direct API request tanpa/invalid reCAPTCHA token, direct verify tanpa/invalid session, direct verify sebelum request, bypass MFA/Agreement, cross-user agreement token, SQL/NoSQL injection kotak digit, token replay, dan penerimaan atribut entry=edit_email informatif tanpa verifikasi riwayat (EC-54) | 153, 154, 155, 156, 158, 159, 160, 161, 162, 163, 171, 172, 178 | web (`Mode: mock`) |
| TC-AUTH-OTP-E2E-027 | Konkurensi multi-tab: verifikasi paralel atomik (hanya 1 yang sukses), resend di Tab A meng-invalidate input Tab B, dan request OTP paralel dari dua tab untuk email yang sama | 164, 165, 173 | web (`Mode: mock`) |

**Total:** 185 dari 185 TC granular aktif tercakup penuh tanpa celah dan tanpa duplikasi. 26 spec web, 1 spec mobile.

---

## Verifikasi Integritas dan Kepatuhan

- **Duplikasi:** `0` (tidak ada satu pun ID `TC-AUTH-OTP-NN` yang muncul di lebih dari 1 spec).
- **Cakupan:** `100%` (seluruh 185 TC dari `TC-AUTH-OTP-01` sampai `TC-AUTH-OTP-185` terpetakan).
- **Lint Spectra:** `npx spectra lint --strict specs/Auth/LoginOtp` lulus dengan `0` lint error.
- **Konvensi Tombol & Pesan UI:** Mengikuti `prd-conventions.md` §24.1, PRD mutakhir (GAP-409–420, commit `8b9d5eb`), dan konsensus NC-01 sampai NC-19.
