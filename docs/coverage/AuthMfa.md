# Coverage E2E — Auth > MFA

Sumber: `auth/mfa/TestCases/tc-mfa.md` (217 TC aktif, `TC-AUTH-MFA-01`–`217`). Suite: `specs/Auth/Mfa/`. Status seluruh spec: `draft`, belum ada script TestSpectra.

**Verifikasi lint:** `npx spectra lint --strict specs/Auth/Mfa` → `✓ 56 specs and 1 suites verified. All spec schemas are valid. 0 lint errors found.`

**Seleksi:** sesuai `docs/e2e-conventions.md` bagian 2, seluruh 217 TC masuk spec; tidak ada TC hanya-BE. Sembilan TC yang menembak endpoint secara langsung tanpa UI (TC-85, 86, 104, 124, 188, 189, 190, 193, 214) tetap masuk sebagai spec kelas a (defense-in-depth, client HTTP) di spec 041 dan 042; TC-204 dan 205 juga mengirim request klien HTTP langsung (20 request per menit per IP) di spec 049. Hambatan teknis dan label `Manual Only` di TC (jam server, jam authenticator, geo-IP, email service, rate limit, Android, mail-catcher, decode QR, proxy `X-Forwarded-For`) bukan alasan mengeluarkan TC; semua kebutuhan ditulis di `## Prerequisites` tiap spec.

**Mode:** semua spec `FE+BE`. Kegagalan 5xx dan timeout dipaksa lewat `Spectra.intercept()` di atas backend nyata atau dipicu di sisi server (geo-IP, email service), sehingga tidak ada spec `Mode: mock`. Spec mobile memakai `coverage.mobile: automated`.

**Nomor spec:** prefix `TC-AUTH-MFA-E2E-` dari `AUTH` + `MFA` pada `foundation/tc-prefix-registry.md`; `001`–`056` adalah nomor urut spec dalam suite. Spec lama `specs/Auth/Mfa/` (36 spec dari 210 TC) sudah dihapus dan digantikan seluruhnya.

**Pembagian TC lintas spec (prinsip 10):** dua TC terbelah dan dicatat di `sourceTc` kedua spec serta `## Notes`: TC-151 (butir a absence log di spec 035; butir b tepat satu entri Success di spec 031, utama); TC-48 (tampilan dan tanpa email di spec 027, utama; absence log langkah 8 di spec 035). TC-22 dan TC-23 seluruhnya di spec 019; Post Condition entri Success faktor-1 keduanya tidak punya Expected padanan atau langkah observasi di TC sehingga tidak diasersi (dicatat sebagai temuan QA). TC-AUTH-MFA-160 dan 161 (asersi log Failed) ditaruh di spec kondisi asalnya (008 dan 055), bukan di spec pencatatan 033, karena kondisinya memakai harness waktu dan akun aktor admin yang sama.

---

## TC granular → spec e2e

| Spec | Isi | TC sumber | Platform |
|---|---|---|---|
| TC-AUTH-MFA-E2E-001-screening-choose-verification-method | Screening Halaman Choose Verification Method | 01, 02, 03, 13, 61 | web |
| TC-AUTH-MFA-E2E-002-routing-metode-faktor-kedua | Routing Pemilihan Metode Faktor Kedua | 53, 55, 56, 57, 58, 60 | web |
| TC-AUTH-MFA-E2E-003-use-different-method-dan-recovery-otp | Use a Different Method dan Recovery OTP | 62, 63, 64 | web |
| TC-AUTH-MFA-E2E-004-screening-dan-input-otp-verification | Screening dan Input Kotak Digit OTP Verification | 04, 14, 67, 69, 87, 88, 89 | web |
| TC-AUTH-MFA-E2E-005-validasi-dan-sukses-verifikasi-otp | Validasi dan Sukses Verifikasi OTP Faktor Kedua | 70, 71, 72, 66, 68 | web |
| TC-AUTH-MFA-E2E-006-siklus-resend-otp-cooldown | Siklus Resend OTP dan Cooldown 60 Detik | 76, 77, 78, 80, 81 | web |
| TC-AUTH-MFA-E2E-007-kuota-resend-otp-5x | Kuota Resend OTP 5 Kali per Sesi Pre-Auth | 79, 82 | web |
| TC-AUTH-MFA-E2E-008-kedaluwarsa-kode-otp-5-menit | Kedaluwarsa Kode OTP Faktor Kedua 5 Menit | 73, 74, 211, 160 | web |
| TC-AUTH-MFA-E2E-009-screening-dan-input-authenticator-verification | Screening dan Input Halaman Authenticator Verification | 05, 06, 15, 08, 101, 102, 103 | web |
| TC-AUTH-MFA-E2E-010-validasi-kode-authenticator-dan-state-ui | Validasi Kode Authenticator dan State UI Halaman Authenticator Verification | 94, 95, 93, 09, 92 | web |
| TC-AUTH-MFA-E2E-011-verifikasi-authenticator-sukses | Verifikasi Authenticator Faktor Kedua Berhasil | 10, 90, 91 | web |
| TC-AUTH-MFA-E2E-012-drift-window-totp-dan-anti-replay | Drift Window TOTP dan Anti-Replay Kode Authenticator | 96, 97, 98, 99 | web |
| TC-AUTH-MFA-E2E-013-admin-reset-authenticator | Admin Reset Authenticator Saat Login MFA | 100, 105 | web |
| TC-AUTH-MFA-E2E-014-screening-dan-input-enrollment | Screening dan Input Kotak Digit Halaman Enrollment Authenticator | 07, 16, 113, 121, 122, 123 | web |
| TC-AUTH-MFA-E2E-015-validasi-dan-sukses-enrollment | Validasi Kode dan Keberhasilan Enrollment Authenticator | 110, 111, 112, 11, 106, 107, 108 | web |
| TC-AUTH-MFA-E2E-016-cancel-enrollment-dan-secret-per-sesi | Cancel Enrollment dan Secret Authenticator per Sesi Pre-auth | 114, 115, 116, 117, 118 | web |
| TC-AUTH-MFA-E2E-017-isi-qr-code-enrollment | Isi QR Code Enrollment Authenticator | 109 | web |
| TC-AUTH-MFA-E2E-018-akses-halaman-mfa-dan-navigasi-browser | Akses Halaman MFA dan Navigasi Browser | 19, 20, 21, 137 | web |
| TC-AUTH-MFA-E2E-019-evaluasi-single-step-tanpa-mfa | Evaluasi Single-Step Tanpa Pemicu MFA | 22, 23, 34, 148 | web |
| TC-AUTH-MFA-E2E-020-pemicu-mfa-login-pertama | Pemicu MFA pada Login Pertama | 24, 25, 149 | web |
| TC-AUTH-MFA-E2E-021-pemicu-mfa-idle-30-hari | Pemicu MFA Setelah Idle 30 Hari | 26, 27, 28, 59, 52 | web |
| TC-AUTH-MFA-E2E-022-deteksi-device-baru | Deteksi Device Baru | 30, 31, 50 | web |
| TC-AUTH-MFA-E2E-023-deteksi-lokasi-lebih-100-km | Deteksi Lokasi Lebih dari 100 km | 33, 38, 51, 208 | web |
| TC-AUTH-MFA-E2E-024-deteksi-beda-negara-dan-pasangan-trusted | Deteksi Beda Negara dan Pasangan Trusted | 35, 36, 37 | web |
| TC-AUTH-MFA-E2E-025-decay-dan-refresh-trust-pasangan-negara | Decay 180 Hari dan Refresh Trust Pasangan Negara | 41, 216, 42, 43, 44 | web |
| TC-AUTH-MFA-E2E-026-fail-open-geo-ip | Fail-Open Geo-IP | 45, 46, 209 | web |
| TC-AUTH-MFA-E2E-027-sekuensialitas-agreement-dan-mfa | Sekuensialitas Agreement dan MFA | 47, 48 | web |
| TC-AUTH-MFA-E2E-028-batas-5-percobaan-salah | Batas 5 Percobaan Salah Faktor-2 Meng-invalidate Sesi Pre-auth | 129, 130, 131, 133, 134, 135, 132 | web |
| TC-AUTH-MFA-E2E-029-ttl-sesi-pre-auth-10-menit | TTL Sesi Pre-auth MFA 10 Menit | 125, 126, 127, 128, 212, 213 | web |
| TC-AUTH-MFA-E2E-030-user-dinonaktifkan-atau-dihapus-saat-mfa | User Dinonaktifkan atau Dihapus Saat MFA Berlangsung | 138, 140, 141, 217, 142, 139 | web |
| TC-AUTH-MFA-E2E-031-trust-device-dan-pasca-login | Trust Device dan Pencatatan Pasca Login Final MFA | 143, 144, 145, 147, 150, 151 | web |
| TC-AUTH-MFA-E2E-032-email-alert-dan-template-email-mfa | Template Email OTP Faktor-2 dan Email Alert Login Tak Biasa | 65, 152, 153, 154, 155 | web |
| TC-AUTH-MFA-E2E-033-pencatatan-failed-faktor-kedua | Pencatatan Failed pada Verifikasi Faktor Kedua MFA | 158, 159, 162, 163, 164 | web |
| TC-AUTH-MFA-E2E-034-pencatatan-success-login-final | Pencatatan Success Login Final MFA dan Kolom Entri Log | 165, 166, 172, 173 | web |
| TC-AUTH-MFA-E2E-035-absence-pencatatan-log | Tidak Ada Pencatatan Log untuk Aksi Non-Autentikasi pada MFA | 168, 169, 170, 171, 207, 151, 48 | web |
| TC-AUTH-MFA-E2E-036-ip-address-x-forwarded-for | Kolom IP Address Entri Login Final Mengikuti X-Forwarded-For | 174 | web |
| TC-AUTH-MFA-E2E-037-integrasi-lintas-modul | Integrasi MFA dengan Reset Password dan Redirect Portal | 175, 176, 178 | web |
| TC-AUTH-MFA-E2E-038-client-suspended-dan-expired | MFA pada User dari Client Suspended dan Client Expired | 179, 180 | web |
| TC-AUTH-MFA-E2E-039-paritas-plan-subscription | Paritas MFA pada Plan Starter, Growth, Professional, dan Enterprise | 181, 182, 183, 184 | web |
| TC-AUTH-MFA-E2E-040-paritas-entitas | Paritas MFA untuk User Entitas Distributor, Partner, dan Principal | 185, 186, 187 | web |
| TC-AUTH-MFA-E2E-041-defense-token-dan-direct-api | Defense-in-Depth: Token Pre-auth dan Request Langsung ke Endpoint MFA | 188, 189, 190, 193 | web |
| TC-AUTH-MFA-E2E-042-defense-cooldown-resend-dan-non-numerik | Defense-in-Depth: Kode Non-Numerik dan Cooldown Resend OTP pada Request Langsung | 85, 214, 86, 104, 124 | web |
| TC-AUTH-MFA-E2E-043-defense-purpose-otp-dan-email-tujuan | Defense-in-Depth: Purpose OTP Lintas Login with OTP dan MFA serta Email Tujuan OTP | 191, 206, 210, 192 | web |
| TC-AUTH-MFA-E2E-044-konkurensi-multi-tab | Konkurensi Multi-Tab dan Multi-Sesi pada Sesi Pre-auth MFA | 136, 177, 197, 202, 203 | web |
| TC-AUTH-MFA-E2E-045-enrollment-dua-device-bersamaan | Enrollment Authenticator dari Dua Device Bersamaan (Web dan Android) | 119 | web + mobile |
| TC-AUTH-MFA-E2E-046-guard-double-submit | Guard Double-Submit pada OTP Verification, Authenticator Verification, dan Enrollment | 194, 195, 196 | web |
| TC-AUTH-MFA-E2E-047-resilience-otp-dan-toast-sticky | Resilience Kegagalan Server pada Login, OTP, dan Authenticator serta Toast Error Sticky | 83, 84, 198, 199, 200, 201 | web |
| TC-AUTH-MFA-E2E-048-resilience-enrollment-dan-email-alert | Resilience Kegagalan Verifikasi Enrollment dan Pengiriman Email Alert | 120, 156, 157 | web |
| TC-AUTH-MFA-E2E-049-rate-limit-ip-429 | Rate Limit IP (429) pada Verify Faktor-2 dan Kirim OTP | 204, 205 | web |
| TC-AUTH-MFA-E2E-050-mobile-layout-keypad-dan-qr | Layout Mobile Android: Keypad Numerik dan QR Enrollment | 17, 18 | mobile |
| TC-AUTH-MFA-E2E-051-mobile-biometric-relogin | Biometric Re-login sebagai Faktor-1 di Android | 54, 167 | web + mobile |
| TC-AUTH-MFA-E2E-052-platform-mobile-trust-idle-reinstall | Trust, Idle, dan Pasang Ulang Aplikasi per Platform | 29, 32, 49, 146 | web + mobile |
| TC-AUTH-MFA-E2E-053-siklus-trust-pasangan-negara-mfa-ketiga | Siklus Trust Pasangan Negara Setelah MFA Ketiga | 39 | web |
| TC-AUTH-MFA-E2E-054-window-90-hari-pasangan-negara | Window 90 Hari Pasangan Negara | 40, 215 | web |
| TC-AUTH-MFA-E2E-055-ganti-email-saat-otp-mfa | Ganti Email User Saat OTP Faktor Kedua MFA Berlangsung | 75, 161 | web |
| TC-AUTH-MFA-E2E-056-aksesibilitas-screen-reader-validasi-kode | Aksesibilitas Screen Reader pada Pesan Validasi Kode Authenticator | 12 | web |

**Total:** 217 dari 217 TC granular tercakup; 56 spec. TC-48 dan 151 muncul di dua spec (spec utama di tabel Lapisan per TC); selebihnya satu spec per TC.

---

## Lapisan per TC

| TC | Spec utama | Mode |
|---|---|---|
| TC-AUTH-MFA-01 | TC-AUTH-MFA-E2E-001-screening-choose-verification-method | FE+BE |
| TC-AUTH-MFA-02 | TC-AUTH-MFA-E2E-001-screening-choose-verification-method | FE+BE |
| TC-AUTH-MFA-03 | TC-AUTH-MFA-E2E-001-screening-choose-verification-method | FE+BE |
| TC-AUTH-MFA-04 | TC-AUTH-MFA-E2E-004-screening-dan-input-otp-verification | FE+BE |
| TC-AUTH-MFA-05 | TC-AUTH-MFA-E2E-009-screening-dan-input-authenticator-verification | FE+BE |
| TC-AUTH-MFA-06 | TC-AUTH-MFA-E2E-009-screening-dan-input-authenticator-verification | FE+BE |
| TC-AUTH-MFA-07 | TC-AUTH-MFA-E2E-014-screening-dan-input-enrollment | FE+BE |
| TC-AUTH-MFA-08 | TC-AUTH-MFA-E2E-009-screening-dan-input-authenticator-verification | FE+BE |
| TC-AUTH-MFA-09 | TC-AUTH-MFA-E2E-010-validasi-kode-authenticator-dan-state-ui | FE+BE |
| TC-AUTH-MFA-10 | TC-AUTH-MFA-E2E-011-verifikasi-authenticator-sukses | FE+BE |
| TC-AUTH-MFA-11 | TC-AUTH-MFA-E2E-015-validasi-dan-sukses-enrollment | FE+BE |
| TC-AUTH-MFA-12 | TC-AUTH-MFA-E2E-056-aksesibilitas-screen-reader-validasi-kode | FE+BE |
| TC-AUTH-MFA-13 | TC-AUTH-MFA-E2E-001-screening-choose-verification-method | FE+BE |
| TC-AUTH-MFA-14 | TC-AUTH-MFA-E2E-004-screening-dan-input-otp-verification | FE+BE |
| TC-AUTH-MFA-15 | TC-AUTH-MFA-E2E-009-screening-dan-input-authenticator-verification | FE+BE |
| TC-AUTH-MFA-16 | TC-AUTH-MFA-E2E-014-screening-dan-input-enrollment | FE+BE |
| TC-AUTH-MFA-17 | TC-AUTH-MFA-E2E-050-mobile-layout-keypad-dan-qr | FE+BE |
| TC-AUTH-MFA-18 | TC-AUTH-MFA-E2E-050-mobile-layout-keypad-dan-qr | FE+BE |
| TC-AUTH-MFA-19 | TC-AUTH-MFA-E2E-018-akses-halaman-mfa-dan-navigasi-browser | FE+BE |
| TC-AUTH-MFA-20 | TC-AUTH-MFA-E2E-018-akses-halaman-mfa-dan-navigasi-browser | FE+BE |
| TC-AUTH-MFA-21 | TC-AUTH-MFA-E2E-018-akses-halaman-mfa-dan-navigasi-browser | FE+BE |
| TC-AUTH-MFA-22 | TC-AUTH-MFA-E2E-019-evaluasi-single-step-tanpa-mfa | FE+BE |
| TC-AUTH-MFA-23 | TC-AUTH-MFA-E2E-019-evaluasi-single-step-tanpa-mfa | FE+BE |
| TC-AUTH-MFA-24 | TC-AUTH-MFA-E2E-020-pemicu-mfa-login-pertama | FE+BE |
| TC-AUTH-MFA-25 | TC-AUTH-MFA-E2E-020-pemicu-mfa-login-pertama | FE+BE |
| TC-AUTH-MFA-26 | TC-AUTH-MFA-E2E-021-pemicu-mfa-idle-30-hari | FE+BE |
| TC-AUTH-MFA-27 | TC-AUTH-MFA-E2E-021-pemicu-mfa-idle-30-hari | FE+BE |
| TC-AUTH-MFA-28 | TC-AUTH-MFA-E2E-021-pemicu-mfa-idle-30-hari | FE+BE |
| TC-AUTH-MFA-29 | TC-AUTH-MFA-E2E-052-platform-mobile-trust-idle-reinstall | FE+BE |
| TC-AUTH-MFA-30 | TC-AUTH-MFA-E2E-022-deteksi-device-baru | FE+BE |
| TC-AUTH-MFA-31 | TC-AUTH-MFA-E2E-022-deteksi-device-baru | FE+BE |
| TC-AUTH-MFA-32 | TC-AUTH-MFA-E2E-052-platform-mobile-trust-idle-reinstall | FE+BE |
| TC-AUTH-MFA-33 | TC-AUTH-MFA-E2E-023-deteksi-lokasi-lebih-100-km | FE+BE |
| TC-AUTH-MFA-34 | TC-AUTH-MFA-E2E-019-evaluasi-single-step-tanpa-mfa | FE+BE |
| TC-AUTH-MFA-35 | TC-AUTH-MFA-E2E-024-deteksi-beda-negara-dan-pasangan-trusted | FE+BE |
| TC-AUTH-MFA-36 | TC-AUTH-MFA-E2E-024-deteksi-beda-negara-dan-pasangan-trusted | FE+BE |
| TC-AUTH-MFA-37 | TC-AUTH-MFA-E2E-024-deteksi-beda-negara-dan-pasangan-trusted | FE+BE |
| TC-AUTH-MFA-38 | TC-AUTH-MFA-E2E-023-deteksi-lokasi-lebih-100-km | FE+BE |
| TC-AUTH-MFA-39 | TC-AUTH-MFA-E2E-053-siklus-trust-pasangan-negara-mfa-ketiga | FE+BE |
| TC-AUTH-MFA-40 | TC-AUTH-MFA-E2E-054-window-90-hari-pasangan-negara | FE+BE |
| TC-AUTH-MFA-41 | TC-AUTH-MFA-E2E-025-decay-dan-refresh-trust-pasangan-negara | FE+BE |
| TC-AUTH-MFA-42 | TC-AUTH-MFA-E2E-025-decay-dan-refresh-trust-pasangan-negara | FE+BE |
| TC-AUTH-MFA-43 | TC-AUTH-MFA-E2E-025-decay-dan-refresh-trust-pasangan-negara | FE+BE |
| TC-AUTH-MFA-44 | TC-AUTH-MFA-E2E-025-decay-dan-refresh-trust-pasangan-negara | FE+BE |
| TC-AUTH-MFA-45 | TC-AUTH-MFA-E2E-026-fail-open-geo-ip | FE+BE |
| TC-AUTH-MFA-46 | TC-AUTH-MFA-E2E-026-fail-open-geo-ip | FE+BE |
| TC-AUTH-MFA-47 | TC-AUTH-MFA-E2E-027-sekuensialitas-agreement-dan-mfa | FE+BE |
| TC-AUTH-MFA-48 | TC-AUTH-MFA-E2E-027-sekuensialitas-agreement-dan-mfa | FE+BE |
| TC-AUTH-MFA-49 | TC-AUTH-MFA-E2E-052-platform-mobile-trust-idle-reinstall | FE+BE |
| TC-AUTH-MFA-50 | TC-AUTH-MFA-E2E-022-deteksi-device-baru | FE+BE |
| TC-AUTH-MFA-51 | TC-AUTH-MFA-E2E-023-deteksi-lokasi-lebih-100-km | FE+BE |
| TC-AUTH-MFA-52 | TC-AUTH-MFA-E2E-021-pemicu-mfa-idle-30-hari | FE+BE |
| TC-AUTH-MFA-53 | TC-AUTH-MFA-E2E-002-routing-metode-faktor-kedua | FE+BE |
| TC-AUTH-MFA-54 | TC-AUTH-MFA-E2E-051-mobile-biometric-relogin | FE+BE |
| TC-AUTH-MFA-55 | TC-AUTH-MFA-E2E-002-routing-metode-faktor-kedua | FE+BE |
| TC-AUTH-MFA-56 | TC-AUTH-MFA-E2E-002-routing-metode-faktor-kedua | FE+BE |
| TC-AUTH-MFA-57 | TC-AUTH-MFA-E2E-002-routing-metode-faktor-kedua | FE+BE |
| TC-AUTH-MFA-58 | TC-AUTH-MFA-E2E-002-routing-metode-faktor-kedua | FE+BE |
| TC-AUTH-MFA-59 | TC-AUTH-MFA-E2E-021-pemicu-mfa-idle-30-hari | FE+BE |
| TC-AUTH-MFA-60 | TC-AUTH-MFA-E2E-002-routing-metode-faktor-kedua | FE+BE |
| TC-AUTH-MFA-61 | TC-AUTH-MFA-E2E-001-screening-choose-verification-method | FE+BE |
| TC-AUTH-MFA-62 | TC-AUTH-MFA-E2E-003-use-different-method-dan-recovery-otp | FE+BE |
| TC-AUTH-MFA-63 | TC-AUTH-MFA-E2E-003-use-different-method-dan-recovery-otp | FE+BE |
| TC-AUTH-MFA-64 | TC-AUTH-MFA-E2E-003-use-different-method-dan-recovery-otp | FE+BE |
| TC-AUTH-MFA-65 | TC-AUTH-MFA-E2E-032-email-alert-dan-template-email-mfa | FE+BE |
| TC-AUTH-MFA-66 | TC-AUTH-MFA-E2E-005-validasi-dan-sukses-verifikasi-otp | FE+BE |
| TC-AUTH-MFA-67 | TC-AUTH-MFA-E2E-004-screening-dan-input-otp-verification | FE+BE |
| TC-AUTH-MFA-68 | TC-AUTH-MFA-E2E-005-validasi-dan-sukses-verifikasi-otp | FE+BE |
| TC-AUTH-MFA-69 | TC-AUTH-MFA-E2E-004-screening-dan-input-otp-verification | FE+BE |
| TC-AUTH-MFA-70 | TC-AUTH-MFA-E2E-005-validasi-dan-sukses-verifikasi-otp | FE+BE |
| TC-AUTH-MFA-71 | TC-AUTH-MFA-E2E-005-validasi-dan-sukses-verifikasi-otp | FE+BE |
| TC-AUTH-MFA-72 | TC-AUTH-MFA-E2E-005-validasi-dan-sukses-verifikasi-otp | FE+BE |
| TC-AUTH-MFA-73 | TC-AUTH-MFA-E2E-008-kedaluwarsa-kode-otp-5-menit | FE+BE |
| TC-AUTH-MFA-74 | TC-AUTH-MFA-E2E-008-kedaluwarsa-kode-otp-5-menit | FE+BE |
| TC-AUTH-MFA-75 | TC-AUTH-MFA-E2E-055-ganti-email-saat-otp-mfa | FE+BE |
| TC-AUTH-MFA-76 | TC-AUTH-MFA-E2E-006-siklus-resend-otp-cooldown | FE+BE |
| TC-AUTH-MFA-77 | TC-AUTH-MFA-E2E-006-siklus-resend-otp-cooldown | FE+BE |
| TC-AUTH-MFA-78 | TC-AUTH-MFA-E2E-006-siklus-resend-otp-cooldown | FE+BE |
| TC-AUTH-MFA-79 | TC-AUTH-MFA-E2E-007-kuota-resend-otp-5x | FE+BE |
| TC-AUTH-MFA-80 | TC-AUTH-MFA-E2E-006-siklus-resend-otp-cooldown | FE+BE |
| TC-AUTH-MFA-81 | TC-AUTH-MFA-E2E-006-siklus-resend-otp-cooldown | FE+BE |
| TC-AUTH-MFA-82 | TC-AUTH-MFA-E2E-007-kuota-resend-otp-5x | FE+BE |
| TC-AUTH-MFA-83 | TC-AUTH-MFA-E2E-047-resilience-otp-dan-toast-sticky | FE+BE |
| TC-AUTH-MFA-84 | TC-AUTH-MFA-E2E-047-resilience-otp-dan-toast-sticky | FE+BE |
| TC-AUTH-MFA-85 | TC-AUTH-MFA-E2E-042-defense-cooldown-resend-dan-non-numerik | FE+BE |
| TC-AUTH-MFA-86 | TC-AUTH-MFA-E2E-042-defense-cooldown-resend-dan-non-numerik | FE+BE |
| TC-AUTH-MFA-87 | TC-AUTH-MFA-E2E-004-screening-dan-input-otp-verification | FE+BE |
| TC-AUTH-MFA-88 | TC-AUTH-MFA-E2E-004-screening-dan-input-otp-verification | FE+BE |
| TC-AUTH-MFA-89 | TC-AUTH-MFA-E2E-004-screening-dan-input-otp-verification | FE+BE |
| TC-AUTH-MFA-90 | TC-AUTH-MFA-E2E-011-verifikasi-authenticator-sukses | FE+BE |
| TC-AUTH-MFA-91 | TC-AUTH-MFA-E2E-011-verifikasi-authenticator-sukses | FE+BE |
| TC-AUTH-MFA-92 | TC-AUTH-MFA-E2E-010-validasi-kode-authenticator-dan-state-ui | FE+BE |
| TC-AUTH-MFA-93 | TC-AUTH-MFA-E2E-010-validasi-kode-authenticator-dan-state-ui | FE+BE |
| TC-AUTH-MFA-94 | TC-AUTH-MFA-E2E-010-validasi-kode-authenticator-dan-state-ui | FE+BE |
| TC-AUTH-MFA-95 | TC-AUTH-MFA-E2E-010-validasi-kode-authenticator-dan-state-ui | FE+BE |
| TC-AUTH-MFA-96 | TC-AUTH-MFA-E2E-012-drift-window-totp-dan-anti-replay | FE+BE |
| TC-AUTH-MFA-97 | TC-AUTH-MFA-E2E-012-drift-window-totp-dan-anti-replay | FE+BE |
| TC-AUTH-MFA-98 | TC-AUTH-MFA-E2E-012-drift-window-totp-dan-anti-replay | FE+BE |
| TC-AUTH-MFA-99 | TC-AUTH-MFA-E2E-012-drift-window-totp-dan-anti-replay | FE+BE |
| TC-AUTH-MFA-100 | TC-AUTH-MFA-E2E-013-admin-reset-authenticator | FE+BE |
| TC-AUTH-MFA-101 | TC-AUTH-MFA-E2E-009-screening-dan-input-authenticator-verification | FE+BE |
| TC-AUTH-MFA-102 | TC-AUTH-MFA-E2E-009-screening-dan-input-authenticator-verification | FE+BE |
| TC-AUTH-MFA-103 | TC-AUTH-MFA-E2E-009-screening-dan-input-authenticator-verification | FE+BE |
| TC-AUTH-MFA-104 | TC-AUTH-MFA-E2E-042-defense-cooldown-resend-dan-non-numerik | FE+BE |
| TC-AUTH-MFA-105 | TC-AUTH-MFA-E2E-013-admin-reset-authenticator | FE+BE |
| TC-AUTH-MFA-106 | TC-AUTH-MFA-E2E-015-validasi-dan-sukses-enrollment | FE+BE |
| TC-AUTH-MFA-107 | TC-AUTH-MFA-E2E-015-validasi-dan-sukses-enrollment | FE+BE |
| TC-AUTH-MFA-108 | TC-AUTH-MFA-E2E-015-validasi-dan-sukses-enrollment | FE+BE |
| TC-AUTH-MFA-109 | TC-AUTH-MFA-E2E-017-isi-qr-code-enrollment | FE+BE |
| TC-AUTH-MFA-110 | TC-AUTH-MFA-E2E-015-validasi-dan-sukses-enrollment | FE+BE |
| TC-AUTH-MFA-111 | TC-AUTH-MFA-E2E-015-validasi-dan-sukses-enrollment | FE+BE |
| TC-AUTH-MFA-112 | TC-AUTH-MFA-E2E-015-validasi-dan-sukses-enrollment | FE+BE |
| TC-AUTH-MFA-113 | TC-AUTH-MFA-E2E-014-screening-dan-input-enrollment | FE+BE |
| TC-AUTH-MFA-114 | TC-AUTH-MFA-E2E-016-cancel-enrollment-dan-secret-per-sesi | FE+BE |
| TC-AUTH-MFA-115 | TC-AUTH-MFA-E2E-016-cancel-enrollment-dan-secret-per-sesi | FE+BE |
| TC-AUTH-MFA-116 | TC-AUTH-MFA-E2E-016-cancel-enrollment-dan-secret-per-sesi | FE+BE |
| TC-AUTH-MFA-117 | TC-AUTH-MFA-E2E-016-cancel-enrollment-dan-secret-per-sesi | FE+BE |
| TC-AUTH-MFA-118 | TC-AUTH-MFA-E2E-016-cancel-enrollment-dan-secret-per-sesi | FE+BE |
| TC-AUTH-MFA-119 | TC-AUTH-MFA-E2E-045-enrollment-dua-device-bersamaan | FE+BE |
| TC-AUTH-MFA-120 | TC-AUTH-MFA-E2E-048-resilience-enrollment-dan-email-alert | FE+BE |
| TC-AUTH-MFA-121 | TC-AUTH-MFA-E2E-014-screening-dan-input-enrollment | FE+BE |
| TC-AUTH-MFA-122 | TC-AUTH-MFA-E2E-014-screening-dan-input-enrollment | FE+BE |
| TC-AUTH-MFA-123 | TC-AUTH-MFA-E2E-014-screening-dan-input-enrollment | FE+BE |
| TC-AUTH-MFA-124 | TC-AUTH-MFA-E2E-042-defense-cooldown-resend-dan-non-numerik | FE+BE |
| TC-AUTH-MFA-125 | TC-AUTH-MFA-E2E-029-ttl-sesi-pre-auth-10-menit | FE+BE |
| TC-AUTH-MFA-126 | TC-AUTH-MFA-E2E-029-ttl-sesi-pre-auth-10-menit | FE+BE |
| TC-AUTH-MFA-127 | TC-AUTH-MFA-E2E-029-ttl-sesi-pre-auth-10-menit | FE+BE |
| TC-AUTH-MFA-128 | TC-AUTH-MFA-E2E-029-ttl-sesi-pre-auth-10-menit | FE+BE |
| TC-AUTH-MFA-129 | TC-AUTH-MFA-E2E-028-batas-5-percobaan-salah | FE+BE |
| TC-AUTH-MFA-130 | TC-AUTH-MFA-E2E-028-batas-5-percobaan-salah | FE+BE |
| TC-AUTH-MFA-131 | TC-AUTH-MFA-E2E-028-batas-5-percobaan-salah | FE+BE |
| TC-AUTH-MFA-132 | TC-AUTH-MFA-E2E-028-batas-5-percobaan-salah | FE+BE |
| TC-AUTH-MFA-133 | TC-AUTH-MFA-E2E-028-batas-5-percobaan-salah | FE+BE |
| TC-AUTH-MFA-134 | TC-AUTH-MFA-E2E-028-batas-5-percobaan-salah | FE+BE |
| TC-AUTH-MFA-135 | TC-AUTH-MFA-E2E-028-batas-5-percobaan-salah | FE+BE |
| TC-AUTH-MFA-136 | TC-AUTH-MFA-E2E-044-konkurensi-multi-tab | FE+BE |
| TC-AUTH-MFA-137 | TC-AUTH-MFA-E2E-018-akses-halaman-mfa-dan-navigasi-browser | FE+BE |
| TC-AUTH-MFA-138 | TC-AUTH-MFA-E2E-030-user-dinonaktifkan-atau-dihapus-saat-mfa | FE+BE |
| TC-AUTH-MFA-139 | TC-AUTH-MFA-E2E-030-user-dinonaktifkan-atau-dihapus-saat-mfa | FE+BE |
| TC-AUTH-MFA-140 | TC-AUTH-MFA-E2E-030-user-dinonaktifkan-atau-dihapus-saat-mfa | FE+BE |
| TC-AUTH-MFA-141 | TC-AUTH-MFA-E2E-030-user-dinonaktifkan-atau-dihapus-saat-mfa | FE+BE |
| TC-AUTH-MFA-142 | TC-AUTH-MFA-E2E-030-user-dinonaktifkan-atau-dihapus-saat-mfa | FE+BE |
| TC-AUTH-MFA-143 | TC-AUTH-MFA-E2E-031-trust-device-dan-pasca-login | FE+BE |
| TC-AUTH-MFA-144 | TC-AUTH-MFA-E2E-031-trust-device-dan-pasca-login | FE+BE |
| TC-AUTH-MFA-145 | TC-AUTH-MFA-E2E-031-trust-device-dan-pasca-login | FE+BE |
| TC-AUTH-MFA-146 | TC-AUTH-MFA-E2E-052-platform-mobile-trust-idle-reinstall | FE+BE |
| TC-AUTH-MFA-147 | TC-AUTH-MFA-E2E-031-trust-device-dan-pasca-login | FE+BE |
| TC-AUTH-MFA-148 | TC-AUTH-MFA-E2E-019-evaluasi-single-step-tanpa-mfa | FE+BE |
| TC-AUTH-MFA-149 | TC-AUTH-MFA-E2E-020-pemicu-mfa-login-pertama | FE+BE |
| TC-AUTH-MFA-150 | TC-AUTH-MFA-E2E-031-trust-device-dan-pasca-login | FE+BE |
| TC-AUTH-MFA-151 | TC-AUTH-MFA-E2E-031-trust-device-dan-pasca-login | FE+BE |
| TC-AUTH-MFA-152 | TC-AUTH-MFA-E2E-032-email-alert-dan-template-email-mfa | FE+BE |
| TC-AUTH-MFA-153 | TC-AUTH-MFA-E2E-032-email-alert-dan-template-email-mfa | FE+BE |
| TC-AUTH-MFA-154 | TC-AUTH-MFA-E2E-032-email-alert-dan-template-email-mfa | FE+BE |
| TC-AUTH-MFA-155 | TC-AUTH-MFA-E2E-032-email-alert-dan-template-email-mfa | FE+BE |
| TC-AUTH-MFA-156 | TC-AUTH-MFA-E2E-048-resilience-enrollment-dan-email-alert | FE+BE |
| TC-AUTH-MFA-157 | TC-AUTH-MFA-E2E-048-resilience-enrollment-dan-email-alert | FE+BE |
| TC-AUTH-MFA-158 | TC-AUTH-MFA-E2E-033-pencatatan-failed-faktor-kedua | FE+BE |
| TC-AUTH-MFA-159 | TC-AUTH-MFA-E2E-033-pencatatan-failed-faktor-kedua | FE+BE |
| TC-AUTH-MFA-160 | TC-AUTH-MFA-E2E-008-kedaluwarsa-kode-otp-5-menit | FE+BE |
| TC-AUTH-MFA-161 | TC-AUTH-MFA-E2E-055-ganti-email-saat-otp-mfa | FE+BE |
| TC-AUTH-MFA-162 | TC-AUTH-MFA-E2E-033-pencatatan-failed-faktor-kedua | FE+BE |
| TC-AUTH-MFA-163 | TC-AUTH-MFA-E2E-033-pencatatan-failed-faktor-kedua | FE+BE |
| TC-AUTH-MFA-164 | TC-AUTH-MFA-E2E-033-pencatatan-failed-faktor-kedua | FE+BE |
| TC-AUTH-MFA-165 | TC-AUTH-MFA-E2E-034-pencatatan-success-login-final | FE+BE |
| TC-AUTH-MFA-166 | TC-AUTH-MFA-E2E-034-pencatatan-success-login-final | FE+BE |
| TC-AUTH-MFA-167 | TC-AUTH-MFA-E2E-051-mobile-biometric-relogin | FE+BE |
| TC-AUTH-MFA-168 | TC-AUTH-MFA-E2E-035-absence-pencatatan-log | FE+BE |
| TC-AUTH-MFA-169 | TC-AUTH-MFA-E2E-035-absence-pencatatan-log | FE+BE |
| TC-AUTH-MFA-170 | TC-AUTH-MFA-E2E-035-absence-pencatatan-log | FE+BE |
| TC-AUTH-MFA-171 | TC-AUTH-MFA-E2E-035-absence-pencatatan-log | FE+BE |
| TC-AUTH-MFA-172 | TC-AUTH-MFA-E2E-034-pencatatan-success-login-final | FE+BE |
| TC-AUTH-MFA-173 | TC-AUTH-MFA-E2E-034-pencatatan-success-login-final | FE+BE |
| TC-AUTH-MFA-174 | TC-AUTH-MFA-E2E-036-ip-address-x-forwarded-for | FE+BE |
| TC-AUTH-MFA-175 | TC-AUTH-MFA-E2E-037-integrasi-lintas-modul | FE+BE |
| TC-AUTH-MFA-176 | TC-AUTH-MFA-E2E-037-integrasi-lintas-modul | FE+BE |
| TC-AUTH-MFA-177 | TC-AUTH-MFA-E2E-044-konkurensi-multi-tab | FE+BE |
| TC-AUTH-MFA-178 | TC-AUTH-MFA-E2E-037-integrasi-lintas-modul | FE+BE |
| TC-AUTH-MFA-179 | TC-AUTH-MFA-E2E-038-client-suspended-dan-expired | FE+BE |
| TC-AUTH-MFA-180 | TC-AUTH-MFA-E2E-038-client-suspended-dan-expired | FE+BE |
| TC-AUTH-MFA-181 | TC-AUTH-MFA-E2E-039-paritas-plan-subscription | FE+BE |
| TC-AUTH-MFA-182 | TC-AUTH-MFA-E2E-039-paritas-plan-subscription | FE+BE |
| TC-AUTH-MFA-183 | TC-AUTH-MFA-E2E-039-paritas-plan-subscription | FE+BE |
| TC-AUTH-MFA-184 | TC-AUTH-MFA-E2E-039-paritas-plan-subscription | FE+BE |
| TC-AUTH-MFA-185 | TC-AUTH-MFA-E2E-040-paritas-entitas | FE+BE |
| TC-AUTH-MFA-186 | TC-AUTH-MFA-E2E-040-paritas-entitas | FE+BE |
| TC-AUTH-MFA-187 | TC-AUTH-MFA-E2E-040-paritas-entitas | FE+BE |
| TC-AUTH-MFA-188 | TC-AUTH-MFA-E2E-041-defense-token-dan-direct-api | FE+BE |
| TC-AUTH-MFA-189 | TC-AUTH-MFA-E2E-041-defense-token-dan-direct-api | FE+BE |
| TC-AUTH-MFA-190 | TC-AUTH-MFA-E2E-041-defense-token-dan-direct-api | FE+BE |
| TC-AUTH-MFA-191 | TC-AUTH-MFA-E2E-043-defense-purpose-otp-dan-email-tujuan | FE+BE |
| TC-AUTH-MFA-192 | TC-AUTH-MFA-E2E-043-defense-purpose-otp-dan-email-tujuan | FE+BE |
| TC-AUTH-MFA-193 | TC-AUTH-MFA-E2E-041-defense-token-dan-direct-api | FE+BE |
| TC-AUTH-MFA-194 | TC-AUTH-MFA-E2E-046-guard-double-submit | FE+BE |
| TC-AUTH-MFA-195 | TC-AUTH-MFA-E2E-046-guard-double-submit | FE+BE |
| TC-AUTH-MFA-196 | TC-AUTH-MFA-E2E-046-guard-double-submit | FE+BE |
| TC-AUTH-MFA-197 | TC-AUTH-MFA-E2E-044-konkurensi-multi-tab | FE+BE |
| TC-AUTH-MFA-198 | TC-AUTH-MFA-E2E-047-resilience-otp-dan-toast-sticky | FE+BE |
| TC-AUTH-MFA-199 | TC-AUTH-MFA-E2E-047-resilience-otp-dan-toast-sticky | FE+BE |
| TC-AUTH-MFA-200 | TC-AUTH-MFA-E2E-047-resilience-otp-dan-toast-sticky | FE+BE |
| TC-AUTH-MFA-201 | TC-AUTH-MFA-E2E-047-resilience-otp-dan-toast-sticky | FE+BE |
| TC-AUTH-MFA-202 | TC-AUTH-MFA-E2E-044-konkurensi-multi-tab | FE+BE |
| TC-AUTH-MFA-203 | TC-AUTH-MFA-E2E-044-konkurensi-multi-tab | FE+BE |
| TC-AUTH-MFA-204 | TC-AUTH-MFA-E2E-049-rate-limit-ip-429 | FE+BE |
| TC-AUTH-MFA-205 | TC-AUTH-MFA-E2E-049-rate-limit-ip-429 | FE+BE |
| TC-AUTH-MFA-206 | TC-AUTH-MFA-E2E-043-defense-purpose-otp-dan-email-tujuan | FE+BE |
| TC-AUTH-MFA-207 | TC-AUTH-MFA-E2E-035-absence-pencatatan-log | FE+BE |
| TC-AUTH-MFA-208 | TC-AUTH-MFA-E2E-023-deteksi-lokasi-lebih-100-km | FE+BE |
| TC-AUTH-MFA-209 | TC-AUTH-MFA-E2E-026-fail-open-geo-ip | FE+BE |
| TC-AUTH-MFA-210 | TC-AUTH-MFA-E2E-043-defense-purpose-otp-dan-email-tujuan | FE+BE |
| TC-AUTH-MFA-211 | TC-AUTH-MFA-E2E-008-kedaluwarsa-kode-otp-5-menit | FE+BE |
| TC-AUTH-MFA-212 | TC-AUTH-MFA-E2E-029-ttl-sesi-pre-auth-10-menit | FE+BE |
| TC-AUTH-MFA-213 | TC-AUTH-MFA-E2E-029-ttl-sesi-pre-auth-10-menit | FE+BE |
| TC-AUTH-MFA-214 | TC-AUTH-MFA-E2E-042-defense-cooldown-resend-dan-non-numerik | FE+BE |
| TC-AUTH-MFA-215 | TC-AUTH-MFA-E2E-054-window-90-hari-pasangan-negara | FE+BE |
| TC-AUTH-MFA-216 | TC-AUTH-MFA-E2E-025-decay-dan-refresh-trust-pasangan-negara | FE+BE |
| TC-AUTH-MFA-217 | TC-AUTH-MFA-E2E-030-user-dinonaktifkan-atau-dihapus-saat-mfa | FE+BE |

---

## Temuan sumber (untuk QA)

Temuan ambigu, kontradiktif, atau kurang precondition (S-15) tercatat per spec di `## Notes` butir "Temuan untuk QA".
