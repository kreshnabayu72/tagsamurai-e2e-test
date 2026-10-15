# Coverage E2E — Auth > Login with OTP

Sumber: `auth/login-otp/TestCases/tc-login-otp.md` (194 TC, `TC-AUTH-OTP-01`–`194`). Suite: `specs/Auth/LoginOtp/` (50 spec, `suite.md` dengan `parallel: false`). Status semua spec: `draft`, belum ada script.

**Verifikasi lint:** `spectra lint --strict specs/Auth/LoginOtp` → `✓ 50 specs and 1 suites verified. All spec schemas are valid. 0 lint errors found.`

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 190 TC masuk spec, 4 TC hanya-BE. Setiap TC punya satu spec utama (tabel "Lapisan per TC"). Sisi absence pencatatan (kelas g, prinsip 13) dari TC fungsional dicatat tambahan di spec 040 dan 047 melalui `sourceTc`, dan dicatat di `## Notes` spec asal. Asersi absence yang bergantung pada state berat (flood rate limit, TTL token, Agreement, MFA, Geo-IP, attestation, fixture BE) tetap di spec asalnya sebagai pengecualian prinsip 13 (E2E-004, 027, 028, 030–035).

**Nomor spec:** prefix `TC-AUTH-OTP-E2E-` dari `AUTH` + `OTP` pada `foundation/tc-prefix-registry.md`. Nomor `001`–`050` adalah nomor urut spec dalam suite. Spec lama di `specs_dummy/Auth/LoginOtp/` (27 spec dari 189 TC) tidak dipakai lagi dan tidak diubah.

**Mode:** semua spec `FE+BE`. Kegagalan server dan timeout dipaksa lewat `Spectra.intercept()` di atas backend nyata (bagian 6 konvensi), sehingga tidak ada spec `Mode: mock`. Spec mobile (003, 004) memakai `coverage.mobile: automated`.

---

## TC granular → spec e2e

| Spec | Judul | Platform | TC sumber |
|---|---|---|---|
| TC-AUTH-OTP-E2E-001-screening-request-otp-dan-prefill | Screening Halaman Request OTP, Prefill Email dari Login with Password, dan Tautan Use Password Instead | web | 01, 03, 04, 05, 35 |
| TC-AUTH-OTP-E2E-002-screening-verify-otp-dan-confirm | Screening Halaman Verify OTP, Tautan Back to Login with Password, dan Layar Confirm to Continue | web | 07, 36, 09 |
| TC-AUTH-OTP-E2E-003-mobile-screening-request-dan-verify | Tampilan Mobile Halaman Request OTP Tanpa reCAPTCHA dan Keypad Numerik pada Halaman Verify OTP | mobile | 02, 08 |
| TC-AUTH-OTP-E2E-004-mobile-attestation-play-integrity | Token Attestation Play Integrity pada Request OTP dan Resend di Aplikasi Mobile | mobile | 185, 180 |
| TC-AUTH-OTP-E2E-005-akses-langsung-dan-redirect-sesi-aktif | Akses Langsung ke Layar Login with OTP tanpa Sesi dan Pengalihan bagi Pengguna yang Sudah Login | web | 73, 74, 06, 75, 76 |
| TC-AUTH-OTP-E2E-006-validasi-email-diblokir | Validasi Field Email pada Request OTP yang Diblokir: Kosong, Format, dan Batas 120 Karakter | web | 11, 12, 13, 167, 16, 168, 17 |
| TC-AUTH-OTP-E2E-007-email-valid-diterima-dan-normalisasi | Request OTP dengan Email Valid Diterima: TLD 2 Karakter, Tepat 120 Karakter, Trim Spasi, Plus-addressing, dan Kapitalisasi Campuran | web | 14, 15, 18, 186, 187 |
| TC-AUTH-OTP-E2E-008-status-akun-pra-request | Evaluasi Status Akun pada Request OTP: Email Belum Terdaftar, Belum Aktivasi, dan Inactive | web | 19, 20, 21 |
| TC-AUTH-OTP-E2E-009-recaptcha-gate-web | Proteksi reCAPTCHA Web pada Request OTP: Blokir Submit, Urutan Evaluasi, Reset Widget, dan Caption | web | 22, 23, 24, 25, 26, 27 |
| TC-AUTH-OTP-E2E-010-request-otp-sukses-loading-klik-ganda | Request OTP Berhasil, Indikator Loading, dan Klik Ganda pada Button Request OTP | web | 28, 29, 30 |
| TC-AUTH-OTP-E2E-011-email-otp-template-subject-sla | Isi, Subject, dan Waktu Penerimaan Email OTP | web | 37, 38, 39 |
| TC-AUTH-OTP-E2E-012-kotak-digit-input-ui | Perilaku Input Kotak 6 Digit OTP: Perpindahan Kursor, Filter Angka, Paste Parsial, dan Backspace | web | 40, 41, 46, 47 |
| TC-AUTH-OTP-E2E-013-paste-dan-auto-submit | Paste Kode OTP dan Verifikasi Otomatis pada Digit ke-6 | web | 42, 43, 44, 45 |
| TC-AUTH-OTP-E2E-014-verify-kode-salah-dan-fallback | Verify OTP dengan Kode Salah dan Button Verify Fallback | web | 49, 56, 60, 69, 177 |
| TC-AUTH-OTP-E2E-015-verify-percobaan-salah-5x | Batas 5 Kali Verify Salah pada Kode yang Sama dan Dampaknya terhadap Login with Password | web | 65, 66, 68 |
| TC-AUTH-OTP-E2E-016-verify-sukses-tanpa-gate | Verify OTP Berhasil Langsung ke Product Hub tanpa Agreement dan MFA | web | 10, 48, 100 |
| TC-AUTH-OTP-E2E-017-edit-email-dan-kode-email-lama | Edit Email dari Layar Verify OTP dan Penolakan Kode dari Request OTP Sebelumnya | web | 54, 64, 86, 88, 89 |
| TC-AUTH-OTP-E2E-018-state-halaman-f5-back-dan-sesi | State Layar Verify OTP dan Confirm to Continue terhadap F5, Tombol Back/Forward, dan Sesi Email-Request | web | 70, 71, 72, 179 |
| TC-AUTH-OTP-E2E-019-verify-setelah-perubahan-akun-oleh-admin | Verify OTP Setelah Akun Diubah di Global Settings: Belum Aktivasi, Email Diganti, Dihapus, dan Dinonaktifkan | web | 61, 62, 141, 184 |
| TC-AUTH-OTP-E2E-020-request-setelah-perubahan-status-akun | Request OTP Setelah Akun Dinonaktifkan, Dihapus, atau Diaktifkan Kembali di Global Settings | web | 138, 139, 140, 166 |
| TC-AUTH-OTP-E2E-021-resend-countdown-dan-invalidasi-kode | Countdown Resend 60 Detik, Resend Menerbitkan Kode Baru, dan Invalidasi Kode Lama | web | 77, 78, 52, 53, 67 |
| TC-AUTH-OTP-E2E-022-resend-kuota-habis-dan-cooldown-10-menit | Resend Sampai Kuota Habis, Cooldown 10 Menit, dan State Exhausted | web | 79, 80, 181, 82, 81 |
| TC-AUTH-OTP-E2E-023-request-ulang-setelah-kuota-habis-dan-ttl-sesi | Request OTP Ulang Setelah Kuota Resend Habis: Ditolak, Edit Email, Email Berbeda, dan Batas 24 Jam | web | 92, 94, 96, 87 |
| TC-AUTH-OTP-E2E-024-sesi-email-request-cooldown-60-detik | Sesi Email-Request: Penolakan Request OTP Saat Cooldown 60 Detik dan Sesi Baru Setelah Verifikasi Sukses | web | 169, 90, 189, 95 |
| TC-AUTH-OTP-E2E-025-sesi-email-request-menghitung-resend | Sesi Email-Request: Request OTP Setelah Cooldown Dihitung sebagai Resend dan Penolakan Tidak Menambah Hitungan | web | 91, 182 |
| TC-AUTH-OTP-E2E-026-ttl-kode-otp-5-menit | Masa Berlaku Kode OTP 5 Menit: Expired, Batas 4:59 dan 5:00, dan Kode yang Sudah Diganti | web | 50, 123, 194, 55, 51, 193 |
| TC-AUTH-OTP-E2E-027-ttl-token-pra-autentikasi-10-menit | Masa Berlaku Token Pra-Autentikasi 10 Menit pada Layar Confirm to Continue | web | 107, 111, 108 |
| TC-AUTH-OTP-E2E-028-rate-limit-ip-429 | Penolakan IP Rate Limit pada Request OTP, Verify OTP, dan Resend | web | 33, 135, 63, 85, 34 |
| TC-AUTH-OTP-E2E-029-resilience-request-dan-resend | Ketahanan Request OTP dan Resend terhadap Error Server dan Timeout | web | 31, 32, 83, 93, 183 |
| TC-AUTH-OTP-E2E-030-resilience-verify-dan-agreement | Ketahanan Verify OTP dan Konfirmasi Agreement terhadap Error Server dan Timeout | web | 57, 58, 59, 105, 106, 188 |
| TC-AUTH-OTP-E2E-031-agreement-gate-first-login | Layar Confirm to Continue: Pemicu Login Pertama, Checkbox, Tautan Privacy Policy, dan Konfirmasi | web | 97, 101, 102, 104, 109 |
| TC-AUTH-OTP-E2E-032-agreement-gate-policy-baru-dan-konfirmasi-sukses | Layar Confirm to Continue: Pemicu Versi Privacy Policy Baru dan Konfirmasi Sukses | web | 99, 103, 142 |
| TC-AUTH-OTP-E2E-033-handoff-mfa-first-login-dan-final | Handoff ke MFA Authenticator setelah Agreement dan Pencatatan Success di Titik Final | web | 112, 115, 129 |
| TC-AUTH-OTP-E2E-034-handoff-mfa-idle-device-baru-dan-alert | Handoff ke MFA untuk Idle 30 Hari, Device Baru, dan Email Alert Login Tak Biasa | web | 98, 113, 114, 174 |
| TC-AUTH-OTP-E2E-035-handoff-mfa-geo-ip | Handoff ke MFA berdasarkan Jarak dan Negara Login | web | 190, 191 |
| TC-AUTH-OTP-E2E-036-pencatatan-failed-request-otp | Pencatatan Failed pada Request OTP: Captcha not completed, Account is not activated, Account is inactive | web | 116, 117, 118 |
| TC-AUTH-OTP-E2E-037-pencatatan-failed-verify-otp | Pencatatan Failed pada Verify OTP: Empty OTP dan Incorrect OTP | web | 119, 120, 121, 122 |
| TC-AUTH-OTP-E2E-038-pencatatan-failed-consent-dan-email-changed | Pencatatan Failed: Account is inactive saat Verify, OTP invalid — email changed, dan Consent not given | web | 124, 125, 126 |
| TC-AUTH-OTP-E2E-039-pencatatan-success-dan-struktur-log | Pencatatan Success Login with OTP dan Struktur Kolom Surface Log | web | 127, 128, 136, 137 |
| TC-AUTH-OTP-E2E-040-tidak-dicatat-absence | Kondisi yang Tidak Dicatat di Surface Log: Penolakan Pra-Lookup, Kegagalan Server, Cooldown, dan Akun Terhapus | web | 130, 131, 132, 133, 134, 128, 11, 12, 13, 16, 19, 23, 24, 28, 89, 167, 168 |
| TC-AUTH-OTP-E2E-041-duplicate-login-attempt | Login with OTP saat Sesi Web Lain Aktif: Duplicate Login Attempt Dikonfirmasi atau Dibatalkan | web | 143, 175, 176 |
| TC-AUTH-OTP-E2E-042-entitas-plan-dan-status-client | Login with OTP Identik untuk Berbagai Plan dan Entitas | web | 144, 145, 146, 147, 148, 149, 150 |
| TC-AUTH-OTP-E2E-043-defense-in-depth-request-dan-verify | Defense-in-Depth: Payload Script, Klaim Mobile Tanpa Bukti, Resend Sebelum Cooldown, Token Diubah, dan Kode Terpakai | web | 157, 154, 84, 161, 155 |
| TC-AUTH-OTP-E2E-044-defense-in-depth-kuota-resend | Defense-in-Depth setelah Kuota Resend Habis: Resend Langsung, Request Tanpa Entry, Hapus Data Browser, dan Entry edit_email | web | 163, 171, 162, 178 |
| TC-AUTH-OTP-E2E-045-sesi-penuh-tidak-terbentuk-sebelum-gate | Sesi Penuh Tidak Terbentuk sebelum Agreement Dikonfirmasi dan sebelum MFA Selesai | web | 158, 159 |
| TC-AUTH-OTP-E2E-046-multi-tab-race | Multi-Tab dan Multi-Browser: Cooldown Lintas Konteks, Resend, Request, dan Verify Bersamaan | web | 170, 165, 173, 164 |
| TC-AUTH-OTP-E2E-047-tidak-dicatat-absence-penolakan-navigasi-dan-kegagalan | Tidak Ada Pencatatan di Surface Log untuk Navigasi, Edit Email, Penolakan Cooldown, Akun Terhapus, Kegagalan Server, dan Resend | web | 35, 36, 86, 30, 90, 140, 62, 157, 31, 32, 78, 68 |
| TC-AUTH-OTP-E2E-048-status-client-suspended-dan-expired | Login with OTP untuk User dari Client Berstatus Suspended dan Expired | web | 151, 152 |
| TC-AUTH-OTP-E2E-049-duplikasi-tab-konfirmasi-token-sekali-pakai | Duplikasi Tab pada Layar Confirm to Continue: Konfirmasi Kedua dengan Token yang Sama Ditolak | web | 110 |
| TC-AUTH-OTP-E2E-050-geo-ip-service-tidak-tersedia | Geo-IP Service Tidak Tersedia: Trigger Jarak dan Negara Dilewati, Verify OTP Lanjut ke Portal tanpa MFA | web | 192 |

## Lapisan per TC

| TC | Spec utama | Mode |
|---|---|---|
| TC-AUTH-OTP-01 | TC-AUTH-OTP-E2E-001-screening-request-otp-dan-prefill | FE+BE |
| TC-AUTH-OTP-02 | TC-AUTH-OTP-E2E-003-mobile-screening-request-dan-verify | FE+BE |
| TC-AUTH-OTP-03 | TC-AUTH-OTP-E2E-001-screening-request-otp-dan-prefill | FE+BE |
| TC-AUTH-OTP-04 | TC-AUTH-OTP-E2E-001-screening-request-otp-dan-prefill | FE+BE |
| TC-AUTH-OTP-05 | TC-AUTH-OTP-E2E-001-screening-request-otp-dan-prefill | FE+BE |
| TC-AUTH-OTP-06 | TC-AUTH-OTP-E2E-005-akses-langsung-dan-redirect-sesi-aktif | FE+BE |
| TC-AUTH-OTP-07 | TC-AUTH-OTP-E2E-002-screening-verify-otp-dan-confirm | FE+BE |
| TC-AUTH-OTP-08 | TC-AUTH-OTP-E2E-003-mobile-screening-request-dan-verify | FE+BE |
| TC-AUTH-OTP-09 | TC-AUTH-OTP-E2E-002-screening-verify-otp-dan-confirm | FE+BE |
| TC-AUTH-OTP-10 | TC-AUTH-OTP-E2E-016-verify-sukses-tanpa-gate | FE+BE |
| TC-AUTH-OTP-11 | TC-AUTH-OTP-E2E-006-validasi-email-diblokir | FE+BE |
| TC-AUTH-OTP-12 | TC-AUTH-OTP-E2E-006-validasi-email-diblokir | FE+BE |
| TC-AUTH-OTP-13 | TC-AUTH-OTP-E2E-006-validasi-email-diblokir | FE+BE |
| TC-AUTH-OTP-14 | TC-AUTH-OTP-E2E-007-email-valid-diterima-dan-normalisasi | FE+BE |
| TC-AUTH-OTP-15 | TC-AUTH-OTP-E2E-007-email-valid-diterima-dan-normalisasi | FE+BE |
| TC-AUTH-OTP-16 | TC-AUTH-OTP-E2E-006-validasi-email-diblokir | FE+BE |
| TC-AUTH-OTP-17 | TC-AUTH-OTP-E2E-006-validasi-email-diblokir | FE+BE |
| TC-AUTH-OTP-18 | TC-AUTH-OTP-E2E-007-email-valid-diterima-dan-normalisasi | FE+BE |
| TC-AUTH-OTP-19 | TC-AUTH-OTP-E2E-008-status-akun-pra-request | FE+BE |
| TC-AUTH-OTP-20 | TC-AUTH-OTP-E2E-008-status-akun-pra-request | FE+BE |
| TC-AUTH-OTP-21 | TC-AUTH-OTP-E2E-008-status-akun-pra-request | FE+BE |
| TC-AUTH-OTP-22 | TC-AUTH-OTP-E2E-009-recaptcha-gate-web | FE+BE |
| TC-AUTH-OTP-23 | TC-AUTH-OTP-E2E-009-recaptcha-gate-web | FE+BE |
| TC-AUTH-OTP-24 | TC-AUTH-OTP-E2E-009-recaptcha-gate-web | FE+BE |
| TC-AUTH-OTP-25 | TC-AUTH-OTP-E2E-009-recaptcha-gate-web | FE+BE |
| TC-AUTH-OTP-26 | TC-AUTH-OTP-E2E-009-recaptcha-gate-web | FE+BE |
| TC-AUTH-OTP-27 | TC-AUTH-OTP-E2E-009-recaptcha-gate-web | FE+BE |
| TC-AUTH-OTP-28 | TC-AUTH-OTP-E2E-010-request-otp-sukses-loading-klik-ganda | FE+BE |
| TC-AUTH-OTP-29 | TC-AUTH-OTP-E2E-010-request-otp-sukses-loading-klik-ganda | FE+BE |
| TC-AUTH-OTP-30 | TC-AUTH-OTP-E2E-010-request-otp-sukses-loading-klik-ganda | FE+BE |
| TC-AUTH-OTP-31 | TC-AUTH-OTP-E2E-029-resilience-request-dan-resend | FE+BE |
| TC-AUTH-OTP-32 | TC-AUTH-OTP-E2E-029-resilience-request-dan-resend | FE+BE |
| TC-AUTH-OTP-33 | TC-AUTH-OTP-E2E-028-rate-limit-ip-429 | FE+BE |
| TC-AUTH-OTP-34 | TC-AUTH-OTP-E2E-028-rate-limit-ip-429 | FE+BE |
| TC-AUTH-OTP-35 | TC-AUTH-OTP-E2E-001-screening-request-otp-dan-prefill | FE+BE |
| TC-AUTH-OTP-36 | TC-AUTH-OTP-E2E-002-screening-verify-otp-dan-confirm | FE+BE |
| TC-AUTH-OTP-37 | TC-AUTH-OTP-E2E-011-email-otp-template-subject-sla | FE+BE |
| TC-AUTH-OTP-38 | TC-AUTH-OTP-E2E-011-email-otp-template-subject-sla | FE+BE |
| TC-AUTH-OTP-39 | TC-AUTH-OTP-E2E-011-email-otp-template-subject-sla | FE+BE |
| TC-AUTH-OTP-40 | TC-AUTH-OTP-E2E-012-kotak-digit-input-ui | FE+BE |
| TC-AUTH-OTP-41 | TC-AUTH-OTP-E2E-012-kotak-digit-input-ui | FE+BE |
| TC-AUTH-OTP-42 | TC-AUTH-OTP-E2E-013-paste-dan-auto-submit | FE+BE |
| TC-AUTH-OTP-43 | TC-AUTH-OTP-E2E-013-paste-dan-auto-submit | FE+BE |
| TC-AUTH-OTP-44 | TC-AUTH-OTP-E2E-013-paste-dan-auto-submit | FE+BE |
| TC-AUTH-OTP-45 | TC-AUTH-OTP-E2E-013-paste-dan-auto-submit | FE+BE |
| TC-AUTH-OTP-46 | TC-AUTH-OTP-E2E-012-kotak-digit-input-ui | FE+BE |
| TC-AUTH-OTP-47 | TC-AUTH-OTP-E2E-012-kotak-digit-input-ui | FE+BE |
| TC-AUTH-OTP-48 | TC-AUTH-OTP-E2E-016-verify-sukses-tanpa-gate | FE+BE |
| TC-AUTH-OTP-49 | TC-AUTH-OTP-E2E-014-verify-kode-salah-dan-fallback | FE+BE |
| TC-AUTH-OTP-50 | TC-AUTH-OTP-E2E-026-ttl-kode-otp-5-menit | FE+BE |
| TC-AUTH-OTP-51 | TC-AUTH-OTP-E2E-026-ttl-kode-otp-5-menit | FE+BE |
| TC-AUTH-OTP-52 | TC-AUTH-OTP-E2E-021-resend-countdown-dan-invalidasi-kode | FE+BE |
| TC-AUTH-OTP-53 | TC-AUTH-OTP-E2E-021-resend-countdown-dan-invalidasi-kode | FE+BE |
| TC-AUTH-OTP-54 | TC-AUTH-OTP-E2E-017-edit-email-dan-kode-email-lama | FE+BE |
| TC-AUTH-OTP-55 | TC-AUTH-OTP-E2E-026-ttl-kode-otp-5-menit | FE+BE |
| TC-AUTH-OTP-56 | TC-AUTH-OTP-E2E-014-verify-kode-salah-dan-fallback | FE+BE |
| TC-AUTH-OTP-57 | TC-AUTH-OTP-E2E-030-resilience-verify-dan-agreement | FE+BE |
| TC-AUTH-OTP-58 | TC-AUTH-OTP-E2E-030-resilience-verify-dan-agreement | FE+BE |
| TC-AUTH-OTP-59 | TC-AUTH-OTP-E2E-030-resilience-verify-dan-agreement | FE+BE |
| TC-AUTH-OTP-60 | TC-AUTH-OTP-E2E-014-verify-kode-salah-dan-fallback | FE+BE |
| TC-AUTH-OTP-61 | TC-AUTH-OTP-E2E-019-verify-setelah-perubahan-akun-oleh-admin | FE+BE |
| TC-AUTH-OTP-62 | TC-AUTH-OTP-E2E-019-verify-setelah-perubahan-akun-oleh-admin | FE+BE |
| TC-AUTH-OTP-63 | TC-AUTH-OTP-E2E-028-rate-limit-ip-429 | FE+BE |
| TC-AUTH-OTP-64 | TC-AUTH-OTP-E2E-017-edit-email-dan-kode-email-lama | FE+BE |
| TC-AUTH-OTP-65 | TC-AUTH-OTP-E2E-015-verify-percobaan-salah-5x | FE+BE |
| TC-AUTH-OTP-66 | TC-AUTH-OTP-E2E-015-verify-percobaan-salah-5x | FE+BE |
| TC-AUTH-OTP-67 | TC-AUTH-OTP-E2E-021-resend-countdown-dan-invalidasi-kode | FE+BE |
| TC-AUTH-OTP-68 | TC-AUTH-OTP-E2E-015-verify-percobaan-salah-5x | FE+BE |
| TC-AUTH-OTP-69 | TC-AUTH-OTP-E2E-014-verify-kode-salah-dan-fallback | FE+BE |
| TC-AUTH-OTP-70 | TC-AUTH-OTP-E2E-018-state-halaman-f5-back-dan-sesi | FE+BE |
| TC-AUTH-OTP-71 | TC-AUTH-OTP-E2E-018-state-halaman-f5-back-dan-sesi | FE+BE |
| TC-AUTH-OTP-72 | TC-AUTH-OTP-E2E-018-state-halaman-f5-back-dan-sesi | FE+BE |
| TC-AUTH-OTP-73 | TC-AUTH-OTP-E2E-005-akses-langsung-dan-redirect-sesi-aktif | FE+BE |
| TC-AUTH-OTP-74 | TC-AUTH-OTP-E2E-005-akses-langsung-dan-redirect-sesi-aktif | FE+BE |
| TC-AUTH-OTP-75 | TC-AUTH-OTP-E2E-005-akses-langsung-dan-redirect-sesi-aktif | FE+BE |
| TC-AUTH-OTP-76 | TC-AUTH-OTP-E2E-005-akses-langsung-dan-redirect-sesi-aktif | FE+BE |
| TC-AUTH-OTP-77 | TC-AUTH-OTP-E2E-021-resend-countdown-dan-invalidasi-kode | FE+BE |
| TC-AUTH-OTP-78 | TC-AUTH-OTP-E2E-021-resend-countdown-dan-invalidasi-kode | FE+BE |
| TC-AUTH-OTP-79 | TC-AUTH-OTP-E2E-022-resend-kuota-habis-dan-cooldown-10-menit | FE+BE |
| TC-AUTH-OTP-80 | TC-AUTH-OTP-E2E-022-resend-kuota-habis-dan-cooldown-10-menit | FE+BE |
| TC-AUTH-OTP-81 | TC-AUTH-OTP-E2E-022-resend-kuota-habis-dan-cooldown-10-menit | FE+BE |
| TC-AUTH-OTP-82 | TC-AUTH-OTP-E2E-022-resend-kuota-habis-dan-cooldown-10-menit | FE+BE |
| TC-AUTH-OTP-83 | TC-AUTH-OTP-E2E-029-resilience-request-dan-resend | FE+BE |
| TC-AUTH-OTP-84 | TC-AUTH-OTP-E2E-043-defense-in-depth-request-dan-verify | FE+BE |
| TC-AUTH-OTP-85 | TC-AUTH-OTP-E2E-028-rate-limit-ip-429 | FE+BE |
| TC-AUTH-OTP-86 | TC-AUTH-OTP-E2E-017-edit-email-dan-kode-email-lama | FE+BE |
| TC-AUTH-OTP-87 | TC-AUTH-OTP-E2E-023-request-ulang-setelah-kuota-habis-dan-ttl-sesi | FE+BE |
| TC-AUTH-OTP-88 | TC-AUTH-OTP-E2E-017-edit-email-dan-kode-email-lama | FE+BE |
| TC-AUTH-OTP-89 | TC-AUTH-OTP-E2E-017-edit-email-dan-kode-email-lama | FE+BE |
| TC-AUTH-OTP-90 | TC-AUTH-OTP-E2E-024-sesi-email-request-cooldown-60-detik | FE+BE |
| TC-AUTH-OTP-91 | TC-AUTH-OTP-E2E-025-sesi-email-request-menghitung-resend | FE+BE |
| TC-AUTH-OTP-92 | TC-AUTH-OTP-E2E-023-request-ulang-setelah-kuota-habis-dan-ttl-sesi | FE+BE |
| TC-AUTH-OTP-93 | TC-AUTH-OTP-E2E-029-resilience-request-dan-resend | FE+BE |
| TC-AUTH-OTP-94 | TC-AUTH-OTP-E2E-023-request-ulang-setelah-kuota-habis-dan-ttl-sesi | FE+BE |
| TC-AUTH-OTP-95 | TC-AUTH-OTP-E2E-024-sesi-email-request-cooldown-60-detik | FE+BE |
| TC-AUTH-OTP-96 | TC-AUTH-OTP-E2E-023-request-ulang-setelah-kuota-habis-dan-ttl-sesi | FE+BE |
| TC-AUTH-OTP-97 | TC-AUTH-OTP-E2E-031-agreement-gate-first-login | FE+BE |
| TC-AUTH-OTP-98 | TC-AUTH-OTP-E2E-034-handoff-mfa-idle-device-baru-dan-alert | FE+BE |
| TC-AUTH-OTP-99 | TC-AUTH-OTP-E2E-032-agreement-gate-policy-baru-dan-konfirmasi-sukses | FE+BE |
| TC-AUTH-OTP-100 | TC-AUTH-OTP-E2E-016-verify-sukses-tanpa-gate | FE+BE |
| TC-AUTH-OTP-101 | TC-AUTH-OTP-E2E-031-agreement-gate-first-login | FE+BE |
| TC-AUTH-OTP-102 | TC-AUTH-OTP-E2E-031-agreement-gate-first-login | FE+BE |
| TC-AUTH-OTP-103 | TC-AUTH-OTP-E2E-032-agreement-gate-policy-baru-dan-konfirmasi-sukses | FE+BE |
| TC-AUTH-OTP-104 | TC-AUTH-OTP-E2E-031-agreement-gate-first-login | FE+BE |
| TC-AUTH-OTP-105 | TC-AUTH-OTP-E2E-030-resilience-verify-dan-agreement | FE+BE |
| TC-AUTH-OTP-106 | TC-AUTH-OTP-E2E-030-resilience-verify-dan-agreement | FE+BE |
| TC-AUTH-OTP-107 | TC-AUTH-OTP-E2E-027-ttl-token-pra-autentikasi-10-menit | FE+BE |
| TC-AUTH-OTP-108 | TC-AUTH-OTP-E2E-027-ttl-token-pra-autentikasi-10-menit | FE+BE |
| TC-AUTH-OTP-109 | TC-AUTH-OTP-E2E-031-agreement-gate-first-login | FE+BE |
| TC-AUTH-OTP-110 | TC-AUTH-OTP-E2E-049-duplikasi-tab-konfirmasi-token-sekali-pakai | FE+BE |
| TC-AUTH-OTP-111 | TC-AUTH-OTP-E2E-027-ttl-token-pra-autentikasi-10-menit | FE+BE |
| TC-AUTH-OTP-112 | TC-AUTH-OTP-E2E-033-handoff-mfa-first-login-dan-final | FE+BE |
| TC-AUTH-OTP-113 | TC-AUTH-OTP-E2E-034-handoff-mfa-idle-device-baru-dan-alert | FE+BE |
| TC-AUTH-OTP-114 | TC-AUTH-OTP-E2E-034-handoff-mfa-idle-device-baru-dan-alert | FE+BE |
| TC-AUTH-OTP-115 | TC-AUTH-OTP-E2E-033-handoff-mfa-first-login-dan-final | FE+BE |
| TC-AUTH-OTP-116 | TC-AUTH-OTP-E2E-036-pencatatan-failed-request-otp | FE+BE |
| TC-AUTH-OTP-117 | TC-AUTH-OTP-E2E-036-pencatatan-failed-request-otp | FE+BE |
| TC-AUTH-OTP-118 | TC-AUTH-OTP-E2E-036-pencatatan-failed-request-otp | FE+BE |
| TC-AUTH-OTP-119 | TC-AUTH-OTP-E2E-037-pencatatan-failed-verify-otp | FE+BE |
| TC-AUTH-OTP-120 | TC-AUTH-OTP-E2E-037-pencatatan-failed-verify-otp | FE+BE |
| TC-AUTH-OTP-121 | TC-AUTH-OTP-E2E-037-pencatatan-failed-verify-otp | FE+BE |
| TC-AUTH-OTP-122 | TC-AUTH-OTP-E2E-037-pencatatan-failed-verify-otp | FE+BE |
| TC-AUTH-OTP-123 | TC-AUTH-OTP-E2E-026-ttl-kode-otp-5-menit | FE+BE |
| TC-AUTH-OTP-124 | TC-AUTH-OTP-E2E-038-pencatatan-failed-consent-dan-email-changed | FE+BE |
| TC-AUTH-OTP-125 | TC-AUTH-OTP-E2E-038-pencatatan-failed-consent-dan-email-changed | FE+BE |
| TC-AUTH-OTP-126 | TC-AUTH-OTP-E2E-038-pencatatan-failed-consent-dan-email-changed | FE+BE |
| TC-AUTH-OTP-127 | TC-AUTH-OTP-E2E-039-pencatatan-success-dan-struktur-log | FE+BE |
| TC-AUTH-OTP-128 | TC-AUTH-OTP-E2E-039-pencatatan-success-dan-struktur-log | FE+BE |
| TC-AUTH-OTP-129 | TC-AUTH-OTP-E2E-033-handoff-mfa-first-login-dan-final | FE+BE |
| TC-AUTH-OTP-130 | TC-AUTH-OTP-E2E-040-tidak-dicatat-absence | FE+BE |
| TC-AUTH-OTP-131 | TC-AUTH-OTP-E2E-040-tidak-dicatat-absence | FE+BE |
| TC-AUTH-OTP-132 | TC-AUTH-OTP-E2E-040-tidak-dicatat-absence | FE+BE |
| TC-AUTH-OTP-133 | TC-AUTH-OTP-E2E-040-tidak-dicatat-absence | FE+BE |
| TC-AUTH-OTP-134 | TC-AUTH-OTP-E2E-040-tidak-dicatat-absence | FE+BE |
| TC-AUTH-OTP-135 | TC-AUTH-OTP-E2E-028-rate-limit-ip-429 | FE+BE |
| TC-AUTH-OTP-136 | TC-AUTH-OTP-E2E-039-pencatatan-success-dan-struktur-log | FE+BE |
| TC-AUTH-OTP-137 | TC-AUTH-OTP-E2E-039-pencatatan-success-dan-struktur-log | FE+BE |
| TC-AUTH-OTP-138 | TC-AUTH-OTP-E2E-020-request-setelah-perubahan-status-akun | FE+BE |
| TC-AUTH-OTP-139 | TC-AUTH-OTP-E2E-020-request-setelah-perubahan-status-akun | FE+BE |
| TC-AUTH-OTP-140 | TC-AUTH-OTP-E2E-020-request-setelah-perubahan-status-akun | FE+BE |
| TC-AUTH-OTP-141 | TC-AUTH-OTP-E2E-019-verify-setelah-perubahan-akun-oleh-admin | FE+BE |
| TC-AUTH-OTP-142 | TC-AUTH-OTP-E2E-032-agreement-gate-policy-baru-dan-konfirmasi-sukses | FE+BE |
| TC-AUTH-OTP-143 | TC-AUTH-OTP-E2E-041-duplicate-login-attempt | FE+BE |
| TC-AUTH-OTP-144 | TC-AUTH-OTP-E2E-042-entitas-plan-dan-status-client | FE+BE |
| TC-AUTH-OTP-145 | TC-AUTH-OTP-E2E-042-entitas-plan-dan-status-client | FE+BE |
| TC-AUTH-OTP-146 | TC-AUTH-OTP-E2E-042-entitas-plan-dan-status-client | FE+BE |
| TC-AUTH-OTP-147 | TC-AUTH-OTP-E2E-042-entitas-plan-dan-status-client | FE+BE |
| TC-AUTH-OTP-148 | TC-AUTH-OTP-E2E-042-entitas-plan-dan-status-client | FE+BE |
| TC-AUTH-OTP-149 | TC-AUTH-OTP-E2E-042-entitas-plan-dan-status-client | FE+BE |
| TC-AUTH-OTP-150 | TC-AUTH-OTP-E2E-042-entitas-plan-dan-status-client | FE+BE |
| TC-AUTH-OTP-151 | TC-AUTH-OTP-E2E-048-status-client-suspended-dan-expired | FE+BE |
| TC-AUTH-OTP-152 | TC-AUTH-OTP-E2E-048-status-client-suspended-dan-expired | FE+BE |
| TC-AUTH-OTP-154 | TC-AUTH-OTP-E2E-043-defense-in-depth-request-dan-verify | FE+BE |
| TC-AUTH-OTP-155 | TC-AUTH-OTP-E2E-043-defense-in-depth-request-dan-verify | FE+BE |
| TC-AUTH-OTP-157 | TC-AUTH-OTP-E2E-043-defense-in-depth-request-dan-verify | FE+BE |
| TC-AUTH-OTP-158 | TC-AUTH-OTP-E2E-045-sesi-penuh-tidak-terbentuk-sebelum-gate | FE+BE |
| TC-AUTH-OTP-159 | TC-AUTH-OTP-E2E-045-sesi-penuh-tidak-terbentuk-sebelum-gate | FE+BE |
| TC-AUTH-OTP-161 | TC-AUTH-OTP-E2E-043-defense-in-depth-request-dan-verify | FE+BE |
| TC-AUTH-OTP-162 | TC-AUTH-OTP-E2E-044-defense-in-depth-kuota-resend | FE+BE |
| TC-AUTH-OTP-163 | TC-AUTH-OTP-E2E-044-defense-in-depth-kuota-resend | FE+BE |
| TC-AUTH-OTP-164 | TC-AUTH-OTP-E2E-046-multi-tab-race | FE+BE |
| TC-AUTH-OTP-165 | TC-AUTH-OTP-E2E-046-multi-tab-race | FE+BE |
| TC-AUTH-OTP-166 | TC-AUTH-OTP-E2E-020-request-setelah-perubahan-status-akun | FE+BE |
| TC-AUTH-OTP-167 | TC-AUTH-OTP-E2E-006-validasi-email-diblokir | FE+BE |
| TC-AUTH-OTP-168 | TC-AUTH-OTP-E2E-006-validasi-email-diblokir | FE+BE |
| TC-AUTH-OTP-169 | TC-AUTH-OTP-E2E-024-sesi-email-request-cooldown-60-detik | FE+BE |
| TC-AUTH-OTP-170 | TC-AUTH-OTP-E2E-046-multi-tab-race | FE+BE |
| TC-AUTH-OTP-171 | TC-AUTH-OTP-E2E-044-defense-in-depth-kuota-resend | FE+BE |
| TC-AUTH-OTP-173 | TC-AUTH-OTP-E2E-046-multi-tab-race | FE+BE |
| TC-AUTH-OTP-174 | TC-AUTH-OTP-E2E-034-handoff-mfa-idle-device-baru-dan-alert | FE+BE |
| TC-AUTH-OTP-175 | TC-AUTH-OTP-E2E-041-duplicate-login-attempt | FE+BE |
| TC-AUTH-OTP-176 | TC-AUTH-OTP-E2E-041-duplicate-login-attempt | FE+BE |
| TC-AUTH-OTP-177 | TC-AUTH-OTP-E2E-014-verify-kode-salah-dan-fallback | FE+BE |
| TC-AUTH-OTP-178 | TC-AUTH-OTP-E2E-044-defense-in-depth-kuota-resend | FE+BE |
| TC-AUTH-OTP-179 | TC-AUTH-OTP-E2E-018-state-halaman-f5-back-dan-sesi | FE+BE |
| TC-AUTH-OTP-180 | TC-AUTH-OTP-E2E-004-mobile-attestation-play-integrity | FE+BE |
| TC-AUTH-OTP-181 | TC-AUTH-OTP-E2E-022-resend-kuota-habis-dan-cooldown-10-menit | FE+BE |
| TC-AUTH-OTP-182 | TC-AUTH-OTP-E2E-025-sesi-email-request-menghitung-resend | FE+BE |
| TC-AUTH-OTP-183 | TC-AUTH-OTP-E2E-029-resilience-request-dan-resend | FE+BE |
| TC-AUTH-OTP-184 | TC-AUTH-OTP-E2E-019-verify-setelah-perubahan-akun-oleh-admin | FE+BE |
| TC-AUTH-OTP-185 | TC-AUTH-OTP-E2E-004-mobile-attestation-play-integrity | FE+BE |
| TC-AUTH-OTP-186 | TC-AUTH-OTP-E2E-007-email-valid-diterima-dan-normalisasi | FE+BE |
| TC-AUTH-OTP-187 | TC-AUTH-OTP-E2E-007-email-valid-diterima-dan-normalisasi | FE+BE |
| TC-AUTH-OTP-188 | TC-AUTH-OTP-E2E-030-resilience-verify-dan-agreement | FE+BE |
| TC-AUTH-OTP-189 | TC-AUTH-OTP-E2E-024-sesi-email-request-cooldown-60-detik | FE+BE |
| TC-AUTH-OTP-190 | TC-AUTH-OTP-E2E-035-handoff-mfa-geo-ip | FE+BE |
| TC-AUTH-OTP-191 | TC-AUTH-OTP-E2E-035-handoff-mfa-geo-ip | FE+BE |
| TC-AUTH-OTP-192 | TC-AUTH-OTP-E2E-050-geo-ip-service-tidak-tersedia | FE+BE |
| TC-AUTH-OTP-193 | TC-AUTH-OTP-E2E-026-ttl-kode-otp-5-menit | FE+BE |
| TC-AUTH-OTP-194 | TC-AUTH-OTP-E2E-026-ttl-kode-otp-5-menit | FE+BE |

## TC hanya-BE (tidak masuk spec)

| TC | Alasan |
|---|---|
| TC-AUTH-OTP-153 | Request OTP langsung ke server dengan email kosong: request langsung ke server, asersinya kontrak validasi server; dicakup `tc-login-otp-backend.md`. |
| TC-AUTH-OTP-156 | Kode OTP non-numerik yang lolos filter input ditolak server: request langsung ke server, asersinya kontrak validasi server (non-numerik diperlakukan seperti kosong, NC-16); dicakup `tc-login-otp-backend.md` (`TC-AUTH-OTP-BE-076`). |
| TC-AUTH-OTP-160 | Konfirmasi Agreement yang dikirim langsung ke server tanpa persetujuan ditolak: request langsung ke server, asersinya kontrak validasi server; dicakup `tc-login-otp-backend.md`. |
| TC-AUTH-OTP-172 | Request OTP langsung ke server dengan email 121 karakter atau format salah ditolak: request langsung ke server, asersinya kontrak validasi server; dicakup `tc-login-otp-backend.md` (`TC-AUTH-OTP-BE-010`). |
