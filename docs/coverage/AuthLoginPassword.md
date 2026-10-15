# Coverage E2E — Auth > Login with Password

Sumber: `auth/login-password/TestCases/tc-login-password.md` (163 TC, `TC-AUTH-LP-01`–`163`, hash SHA-256 `6a8da5772ff049b8…`). Suite: `specs/Auth/LoginPassword/`. Status semua spec: `draft`, belum ada script.

**Verifikasi lint:** `spectra lint --strict specs/Auth/LoginPassword` → `✓ 53 specs and 1 suites verified. 0 lint errors found.`

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 163 TC masuk spec, 0 TC hanya-BE (`tc-login-password-backend.md` tidak merujuk id TC granular). Setiap TC terpetakan ke satu spec; dua TC punya bagian di dua spec karena asersi absence pencatatan dipindah ke spec absence (S-05): TC-161 (spec 002 dan 042) dan TC-157 (spec 028 dan 043); asersi jumlah/state TC-114 dan TC-116 berada di spec 038 dan TC-153 di spec 041 (konvensi §3 baris 90). Prefix `TC-AUTH-LP-E2E-` berasal dari `AUTH` + `LP` di `foundation/tc-prefix-registry.md`; nomor adalah urutan spec, bukan nomor TC sumber.

Spec lama generasi sebelumnya ada di `specs_dummy/Auth/LoginPassword/` dan tidak dipakai.

## TC granular → spec e2e

| Spec | Judul | TC sumber | Platform | Mode |
|---|---|---|---|---|
| TC-AUTH-LP-E2E-001-screening-login-page-web | Screening Halaman Login with Password (Web) | 01, 02, 03, 04 | web | mock |
| TC-AUTH-LP-E2E-002-email-validation-blocked | Validasi Field Email: Submit Diblokir dan Batas Format serta Panjang | 10, 11, 12, 13, 14, 15, 16, 17, 161 | web | FE+BE |
| TC-AUTH-LP-E2E-003-email-accepted-login-success | Email Diterima dan Login Berhasil: Spasi, Plus-Addressing, dan Kapitalisasi Campuran | 18, 27, 156 | web | FE+BE |
| TC-AUTH-LP-E2E-004-password-validation | Validasi Field Password: Kosong, Beda Huruf Besar-Kecil, Karakter Khusus, dan Spasi | 19, 20, 21, 22, 23 | web | FE+BE |
| TC-AUTH-LP-E2E-005-recaptcha-gate-web | Gate Google reCAPTCHA v2 pada Login Web | 24, 25, 26 | web | FE+BE |
| TC-AUTH-LP-E2E-006-account-status-and-unregistered-email | Penolakan Email Belum Terdaftar dan Pembedaan Pesan Kredensial Salah | 28, 37, 103 | web | FE+BE |
| TC-AUTH-LP-E2E-007-login-success-no-gate | Login Berhasil Tanpa Gate Agreement dan MFA Menuju Portal | 09, 69, 81 | web | FE+BE |
| TC-AUTH-LP-E2E-008-login-plan-parity | Login Identik pada Entitas dengan Plan Starter, Growth, Professional, Enterprise, dan Custom | 76 | web | FE+BE |
| TC-AUTH-LP-E2E-009-lock-15m-progression | Progresi Lock 15 Menit pada Kegagalan Password | 29, 30, 38, 39, 40, 41 | web | FE+BE |
| TC-AUTH-LP-E2E-010-lock-15m-evaluation-order | Urutan Evaluasi Lock 15 Menit terhadap Password Kosong dan reCAPTCHA | 42, 43 | web | FE+BE |
| TC-AUTH-LP-E2E-011-lock-15m-expiry-and-1h-stage | Lock 15 Menit Berakhir dan Masuk Tahap Lock 1 Jam | 44, 45, 46, 47, 151 | web | FE+BE |
| TC-AUTH-LP-E2E-012-lock-1h-expiry-requires-reset | Lock 1 Jam Berakhir dan Status Requires Reset | 48, 49, 50, 51, 52 | web | FE+BE |
| TC-AUTH-LP-E2E-013-lock-day-rollover | Pergantian Hari pada Hitungan Gagal dan Lock | 53, 54, 55, 56, 57 | web | FE+BE |
| TC-AUTH-LP-E2E-014-lock-permanent-escalation | Eskalasi Lock Permanent setelah 7 Hari Berturut-turut | 58, 59, 60 | web | FE+BE |
| TC-AUTH-LP-E2E-015-lock-recovery-reset-password | Pemulihan Lock lewat Reset Password | 61, 62, 63 | web | FE+BE |
| TC-AUTH-LP-E2E-016-failed-counter-rules | Aturan Hitungan Gagal: Percobaan yang Tidak Dihitung | 66, 67 | web | FE+BE |
| TC-AUTH-LP-E2E-017-lock-platform-independence | Lock Login di Web Tidak Mengunci Login di Aplikasi Mobile | 64 | mobile | FE+BE |
| TC-AUTH-LP-E2E-018-mobile-login-screening-and-success | Screening Layar Login Mobile Tanpa reCAPTCHA dan Login Berhasil | 06, 70 | mobile | FE+BE |
| TC-AUTH-LP-E2E-019-mobile-play-integrity-invalid | Login Mobile dengan Token Play Integrity Kosong atau Invalid Ditolak | 75 | mobile | FE+BE |
| TC-AUTH-LP-E2E-020-agreement-screening | Screening Layar Confirm to Continue dan Checkbox Agreement | 07, 08, 77, 91 | web | FE+BE |
| TC-AUTH-LP-E2E-021-agreement-trigger-conditions | Kondisi Pemicu Layar Confirm to Continue | 78, 79, 80 | web | FE+BE |
| TC-AUTH-LP-E2E-022-agreement-confirm-flow | Interaksi dan Konfirmasi pada Layar Confirm to Continue | 82, 83, 102 | web | FE+BE |
| TC-AUTH-LP-E2E-023-mfa-handoff-device-and-idle | Handoff ke MFA karena Device Baru dan Idle Lebih dari 30 Hari | 71, 72, 154 | web | FE+BE |
| TC-AUTH-LP-E2E-024-mfa-handoff-location-country | Handoff ke MFA karena Lokasi Berjarak Lebih dari 100 km atau Negara Berbeda | 73, 74, 158 | web | FE+BE |
| TC-AUTH-LP-E2E-025-agreement-token-ttl | Masa Berlaku Token Pra-Autentikasi pada Layar Confirm to Continue | 88, 89 | web | FE+BE |
| TC-AUTH-LP-E2E-026-agreement-policy-version-change | Versi Privacy Policy Berubah Saat Layar Confirm to Continue Terbuka | 87 | web | FE+BE |
| TC-AUTH-LP-E2E-027-resilience-submit-intercept | Ketahanan Submit Login dan Konfirmasi Agreement: Loading, Error Server, dan Timeout | 92, 97, 98, 99 | web | FE+BE |
| TC-AUTH-LP-E2E-028-resilience-provider-failure-injection | Ketahanan Login terhadap Kegagalan Penyedia: reCAPTCHA, Geo-IP, dan Versi Privacy Policy | 100, 155, 157 | web | FE+BE |
| TC-AUTH-LP-E2E-029-defense-in-depth-login-request | Defense-in-Depth Request Login: Token reCAPTCHA Dihapus, Bypass Lock, SQL Injection, dan XSS | 139, 140, 144, 145 | web | FE+BE |
| TC-AUTH-LP-E2E-030-defense-in-depth-preauth-session | Defense-in-Depth Sesi dan Token Pra-Autentikasi: Akses Portal Langsung, Token Dimodifikasi, dan Token Dipakai Ulang | 141, 142, 143, 149 | web | FE+BE |
| TC-AUTH-LP-E2E-031-navigation-links-and-email-carry | Navigasi ke Login with OTP dan Reset Password serta Pembawaan Email | 05, 93, 94, 95, 96 | web | FE+BE |
| TC-AUTH-LP-E2E-032-double-submit | Klik Ganda pada Continue dan Log in Hanya Diproses Satu Kali | 148, 150 | web | FE+BE |
| TC-AUTH-LP-E2E-033-concurrency-multitab | Konsistensi Hitungan Gagal Lintas Tab dan Submit Password Salah Bersamaan | 146, 147 | web | FE+BE |
| TC-AUTH-LP-E2E-034-rate-limit-ip | Penolakan IP Rate Limit 20 Request per Menit pada Login | 101, 104 | web | FE+BE |
| TC-AUTH-LP-E2E-035-log-failed-attempts-basic | Pencatatan Log Login Gagal: Password Kosong, reCAPTCHA, Status Akun, dan Password Salah | 105, 106, 107, 108, 109 | web | FE+BE |
| TC-AUTH-LP-E2E-036-log-lock-stages | Pencatatan Log Tahap Lock 15 Menit, 1 Jam, dan Requires Reset | 110, 111, 112 | web | FE+BE |
| TC-AUTH-LP-E2E-037-log-lock-permanent | Pencatatan Log Lock Permanent pada Kegagalan Pertama di Hari ke-8 | 113 | web | FE+BE |
| TC-AUTH-LP-E2E-038-log-success-and-consent | Pencatatan Log Consent Tidak Diberikan dan Login Berhasil | 114, 115, 116 | web | FE+BE |
| TC-AUTH-LP-E2E-039-log-entry-columns | Kolom Entri Login pada Activity Log Session dan User Log | 125, 126, 127, 128, 129, 162 | web | FE+BE |
| TC-AUTH-LP-E2E-040-log-format-general-settings | Format Tanggal, Jam, dan Zona Waktu Mengikuti General Settings | 135, 136, 137, 138 | web | FE+BE |
| TC-AUTH-LP-E2E-041-resilience-log-write-failure | Ketahanan Login terhadap Kegagalan Layanan Penulisan Log | 130, 153 | web | FE+BE |
| TC-AUTH-LP-E2E-042-absence-input-rejections | Tidak Ada Pencatatan Log untuk Penolakan Input pada Login with Password | 117, 118, 119, 121, 161 | web | FE+BE |
| TC-AUTH-LP-E2E-043-absence-state-based | Tidak Ada Pencatatan Log pada Kondisi Lock, MFA Tertunda, Agreement Ditinggalkan, dan Policy Tak Ter-resolve | 90, 120, 124, 157 | web | FE+BE |
| TC-AUTH-LP-E2E-044-absence-policy-version-change | Tidak Ada Pencatatan Log saat Konfirmasi Agreement Ditolak karena Versi Privacy Policy Berubah | 122 | web | FE+BE |
| TC-AUTH-LP-E2E-045-absence-ip-rate-limit | Tidak Ada Pencatatan Log untuk Penolakan IP Rate Limit | 123 | web | FE+BE |
| TC-AUTH-LP-E2E-046-cross-module-user-status-sync | Sinkron Status User dari Global Settings ke Login with Password | 131, 132, 133, 134 | web | FE+BE |
| TC-AUTH-LP-E2E-047-consent-shared-with-login-otp | Persetujuan Privacy Policy dari Login with Password Berlaku pada Login with OTP | 159 | web | FE+BE |
| TC-AUTH-LP-E2E-048-consent-shared-with-biometric-relogin | Persetujuan Privacy Policy dari Login with Password Berlaku pada Biometric Re-login | 160 | mobile | FE+BE |
| TC-AUTH-LP-E2E-049-account-status-pending-inactive | Penolakan Login Akun Pending Activation dan Akun Inactive | 31, 32, 33, 34, 35, 36 | web | FE+BE |
| TC-AUTH-LP-E2E-050-failed-counter-reset-on-correct-password | Aturan Hitungan Gagal: Diatur Ulang saat Password Benar | 68, 152 | web | FE+BE |
| TC-AUTH-LP-E2E-051-agreement-confirm-and-mfa-handoff | Konfirmasi Agreement ke Portal, Login Berikutnya, dan Handoff ke MFA | 84, 85, 86 | web | FE+BE |
| TC-AUTH-LP-E2E-052-lock-daily-reset-keeps-consecutive-days | Password Benar Mengatur Ulang Data Lock Harian Tanpa Mengubah Hitungan Hari Berturut-turut | 163 | web | FE+BE |
| TC-AUTH-LP-E2E-055-lock-platform-independence-web | Lock Login di Aplikasi Mobile Tidak Mengunci Login di Web | 65 | web | FE+BE |

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-AUTH-LP-01 | TC-AUTH-LP-E2E-001 | mock |
| TC-AUTH-LP-02 | TC-AUTH-LP-E2E-001 | mock |
| TC-AUTH-LP-03 | TC-AUTH-LP-E2E-001 | mock |
| TC-AUTH-LP-04 | TC-AUTH-LP-E2E-001 | mock |
| TC-AUTH-LP-05 | TC-AUTH-LP-E2E-031 | FE+BE |
| TC-AUTH-LP-06 | TC-AUTH-LP-E2E-018 | FE+BE |
| TC-AUTH-LP-07 | TC-AUTH-LP-E2E-020 | FE+BE |
| TC-AUTH-LP-08 | TC-AUTH-LP-E2E-020 | FE+BE |
| TC-AUTH-LP-09 | TC-AUTH-LP-E2E-007 | FE+BE |
| TC-AUTH-LP-10 | TC-AUTH-LP-E2E-002 | FE+BE |
| TC-AUTH-LP-11 | TC-AUTH-LP-E2E-002 | FE+BE |
| TC-AUTH-LP-12 | TC-AUTH-LP-E2E-002 | FE+BE |
| TC-AUTH-LP-13 | TC-AUTH-LP-E2E-002 | FE+BE |
| TC-AUTH-LP-14 | TC-AUTH-LP-E2E-002 | FE+BE |
| TC-AUTH-LP-15 | TC-AUTH-LP-E2E-002 | FE+BE |
| TC-AUTH-LP-16 | TC-AUTH-LP-E2E-002 | FE+BE |
| TC-AUTH-LP-17 | TC-AUTH-LP-E2E-002 | FE+BE |
| TC-AUTH-LP-18 | TC-AUTH-LP-E2E-003 | FE+BE |
| TC-AUTH-LP-19 | TC-AUTH-LP-E2E-004 | FE+BE |
| TC-AUTH-LP-20 | TC-AUTH-LP-E2E-004 | FE+BE |
| TC-AUTH-LP-21 | TC-AUTH-LP-E2E-004 | FE+BE |
| TC-AUTH-LP-22 | TC-AUTH-LP-E2E-004 | FE+BE |
| TC-AUTH-LP-23 | TC-AUTH-LP-E2E-004 | FE+BE |
| TC-AUTH-LP-24 | TC-AUTH-LP-E2E-005 | FE+BE |
| TC-AUTH-LP-25 | TC-AUTH-LP-E2E-005 | FE+BE |
| TC-AUTH-LP-26 | TC-AUTH-LP-E2E-005 | FE+BE |
| TC-AUTH-LP-27 | TC-AUTH-LP-E2E-003 | FE+BE |
| TC-AUTH-LP-28 | TC-AUTH-LP-E2E-006 | FE+BE |
| TC-AUTH-LP-29 | TC-AUTH-LP-E2E-009 | FE+BE |
| TC-AUTH-LP-30 | TC-AUTH-LP-E2E-009 | FE+BE |
| TC-AUTH-LP-31 | TC-AUTH-LP-E2E-049 | FE+BE |
| TC-AUTH-LP-32 | TC-AUTH-LP-E2E-049 | FE+BE |
| TC-AUTH-LP-33 | TC-AUTH-LP-E2E-049 | FE+BE |
| TC-AUTH-LP-34 | TC-AUTH-LP-E2E-049 | FE+BE |
| TC-AUTH-LP-35 | TC-AUTH-LP-E2E-049 | FE+BE |
| TC-AUTH-LP-36 | TC-AUTH-LP-E2E-049 | FE+BE |
| TC-AUTH-LP-37 | TC-AUTH-LP-E2E-006 | FE+BE |
| TC-AUTH-LP-38 | TC-AUTH-LP-E2E-009 | FE+BE |
| TC-AUTH-LP-39 | TC-AUTH-LP-E2E-009 | FE+BE |
| TC-AUTH-LP-40 | TC-AUTH-LP-E2E-009 | FE+BE |
| TC-AUTH-LP-41 | TC-AUTH-LP-E2E-009 | FE+BE |
| TC-AUTH-LP-42 | TC-AUTH-LP-E2E-010 | FE+BE |
| TC-AUTH-LP-43 | TC-AUTH-LP-E2E-010 | FE+BE |
| TC-AUTH-LP-44 | TC-AUTH-LP-E2E-011 | FE+BE |
| TC-AUTH-LP-45 | TC-AUTH-LP-E2E-011 | FE+BE |
| TC-AUTH-LP-46 | TC-AUTH-LP-E2E-011 | FE+BE |
| TC-AUTH-LP-47 | TC-AUTH-LP-E2E-011 | FE+BE |
| TC-AUTH-LP-48 | TC-AUTH-LP-E2E-012 | FE+BE |
| TC-AUTH-LP-49 | TC-AUTH-LP-E2E-012 | FE+BE |
| TC-AUTH-LP-50 | TC-AUTH-LP-E2E-012 | FE+BE |
| TC-AUTH-LP-51 | TC-AUTH-LP-E2E-012 | FE+BE |
| TC-AUTH-LP-52 | TC-AUTH-LP-E2E-012 | FE+BE |
| TC-AUTH-LP-53 | TC-AUTH-LP-E2E-013 | FE+BE |
| TC-AUTH-LP-54 | TC-AUTH-LP-E2E-013 | FE+BE |
| TC-AUTH-LP-55 | TC-AUTH-LP-E2E-013 | FE+BE |
| TC-AUTH-LP-56 | TC-AUTH-LP-E2E-013 | FE+BE |
| TC-AUTH-LP-57 | TC-AUTH-LP-E2E-013 | FE+BE |
| TC-AUTH-LP-58 | TC-AUTH-LP-E2E-014 | FE+BE |
| TC-AUTH-LP-59 | TC-AUTH-LP-E2E-014 | FE+BE |
| TC-AUTH-LP-60 | TC-AUTH-LP-E2E-014 | FE+BE |
| TC-AUTH-LP-61 | TC-AUTH-LP-E2E-015 | FE+BE |
| TC-AUTH-LP-62 | TC-AUTH-LP-E2E-015 | FE+BE |
| TC-AUTH-LP-63 | TC-AUTH-LP-E2E-015 | FE+BE |
| TC-AUTH-LP-64 | TC-AUTH-LP-E2E-017 | FE+BE |
| TC-AUTH-LP-65 | TC-AUTH-LP-E2E-055 | FE+BE |
| TC-AUTH-LP-66 | TC-AUTH-LP-E2E-016 | FE+BE |
| TC-AUTH-LP-67 | TC-AUTH-LP-E2E-016 | FE+BE |
| TC-AUTH-LP-68 | TC-AUTH-LP-E2E-050 | FE+BE |
| TC-AUTH-LP-69 | TC-AUTH-LP-E2E-007 | FE+BE |
| TC-AUTH-LP-70 | TC-AUTH-LP-E2E-018 | FE+BE |
| TC-AUTH-LP-71 | TC-AUTH-LP-E2E-023 | FE+BE |
| TC-AUTH-LP-72 | TC-AUTH-LP-E2E-023 | FE+BE |
| TC-AUTH-LP-73 | TC-AUTH-LP-E2E-024 | FE+BE |
| TC-AUTH-LP-74 | TC-AUTH-LP-E2E-024 | FE+BE |
| TC-AUTH-LP-75 | TC-AUTH-LP-E2E-019 | FE+BE |
| TC-AUTH-LP-76 | TC-AUTH-LP-E2E-008 | FE+BE |
| TC-AUTH-LP-77 | TC-AUTH-LP-E2E-020 | FE+BE |
| TC-AUTH-LP-78 | TC-AUTH-LP-E2E-021 | FE+BE |
| TC-AUTH-LP-79 | TC-AUTH-LP-E2E-021 | FE+BE |
| TC-AUTH-LP-80 | TC-AUTH-LP-E2E-021 | FE+BE |
| TC-AUTH-LP-81 | TC-AUTH-LP-E2E-007 | FE+BE |
| TC-AUTH-LP-82 | TC-AUTH-LP-E2E-022 | FE+BE |
| TC-AUTH-LP-83 | TC-AUTH-LP-E2E-022 | FE+BE |
| TC-AUTH-LP-84 | TC-AUTH-LP-E2E-051 | FE+BE |
| TC-AUTH-LP-85 | TC-AUTH-LP-E2E-051 | FE+BE |
| TC-AUTH-LP-86 | TC-AUTH-LP-E2E-051 | FE+BE |
| TC-AUTH-LP-87 | TC-AUTH-LP-E2E-026 | FE+BE |
| TC-AUTH-LP-88 | TC-AUTH-LP-E2E-025 | FE+BE |
| TC-AUTH-LP-89 | TC-AUTH-LP-E2E-025 | FE+BE |
| TC-AUTH-LP-90 | TC-AUTH-LP-E2E-043 | FE+BE |
| TC-AUTH-LP-91 | TC-AUTH-LP-E2E-020 | FE+BE |
| TC-AUTH-LP-92 | TC-AUTH-LP-E2E-027 | FE+BE |
| TC-AUTH-LP-93 | TC-AUTH-LP-E2E-031 | FE+BE |
| TC-AUTH-LP-94 | TC-AUTH-LP-E2E-031 | FE+BE |
| TC-AUTH-LP-95 | TC-AUTH-LP-E2E-031 | FE+BE |
| TC-AUTH-LP-96 | TC-AUTH-LP-E2E-031 | FE+BE |
| TC-AUTH-LP-97 | TC-AUTH-LP-E2E-027 | FE+BE |
| TC-AUTH-LP-98 | TC-AUTH-LP-E2E-027 | FE+BE |
| TC-AUTH-LP-99 | TC-AUTH-LP-E2E-027 | FE+BE |
| TC-AUTH-LP-100 | TC-AUTH-LP-E2E-028 | FE+BE |
| TC-AUTH-LP-101 | TC-AUTH-LP-E2E-034 | FE+BE |
| TC-AUTH-LP-102 | TC-AUTH-LP-E2E-022 | FE+BE |
| TC-AUTH-LP-103 | TC-AUTH-LP-E2E-006 | FE+BE |
| TC-AUTH-LP-104 | TC-AUTH-LP-E2E-034 | FE+BE |
| TC-AUTH-LP-105 | TC-AUTH-LP-E2E-035 | FE+BE |
| TC-AUTH-LP-106 | TC-AUTH-LP-E2E-035 | FE+BE |
| TC-AUTH-LP-107 | TC-AUTH-LP-E2E-035 | FE+BE |
| TC-AUTH-LP-108 | TC-AUTH-LP-E2E-035 | FE+BE |
| TC-AUTH-LP-109 | TC-AUTH-LP-E2E-035 | FE+BE |
| TC-AUTH-LP-110 | TC-AUTH-LP-E2E-036 | FE+BE |
| TC-AUTH-LP-111 | TC-AUTH-LP-E2E-036 | FE+BE |
| TC-AUTH-LP-112 | TC-AUTH-LP-E2E-036 | FE+BE |
| TC-AUTH-LP-113 | TC-AUTH-LP-E2E-037 | FE+BE |
| TC-AUTH-LP-114 | TC-AUTH-LP-E2E-038 | FE+BE |
| TC-AUTH-LP-115 | TC-AUTH-LP-E2E-038 | FE+BE |
| TC-AUTH-LP-116 | TC-AUTH-LP-E2E-038 | FE+BE |
| TC-AUTH-LP-117 | TC-AUTH-LP-E2E-042 | FE+BE |
| TC-AUTH-LP-118 | TC-AUTH-LP-E2E-042 | FE+BE |
| TC-AUTH-LP-119 | TC-AUTH-LP-E2E-042 | FE+BE |
| TC-AUTH-LP-120 | TC-AUTH-LP-E2E-043 | FE+BE |
| TC-AUTH-LP-121 | TC-AUTH-LP-E2E-042 | FE+BE |
| TC-AUTH-LP-122 | TC-AUTH-LP-E2E-044 | FE+BE |
| TC-AUTH-LP-123 | TC-AUTH-LP-E2E-045 | FE+BE |
| TC-AUTH-LP-124 | TC-AUTH-LP-E2E-043 | FE+BE |
| TC-AUTH-LP-125 | TC-AUTH-LP-E2E-039 | FE+BE |
| TC-AUTH-LP-126 | TC-AUTH-LP-E2E-039 | FE+BE |
| TC-AUTH-LP-127 | TC-AUTH-LP-E2E-039 | FE+BE |
| TC-AUTH-LP-128 | TC-AUTH-LP-E2E-039 | FE+BE |
| TC-AUTH-LP-129 | TC-AUTH-LP-E2E-039 | FE+BE |
| TC-AUTH-LP-130 | TC-AUTH-LP-E2E-041 | FE+BE |
| TC-AUTH-LP-131 | TC-AUTH-LP-E2E-046 | FE+BE |
| TC-AUTH-LP-132 | TC-AUTH-LP-E2E-046 | FE+BE |
| TC-AUTH-LP-133 | TC-AUTH-LP-E2E-046 | FE+BE |
| TC-AUTH-LP-134 | TC-AUTH-LP-E2E-046 | FE+BE |
| TC-AUTH-LP-135 | TC-AUTH-LP-E2E-040 | FE+BE |
| TC-AUTH-LP-136 | TC-AUTH-LP-E2E-040 | FE+BE |
| TC-AUTH-LP-137 | TC-AUTH-LP-E2E-040 | FE+BE |
| TC-AUTH-LP-138 | TC-AUTH-LP-E2E-040 | FE+BE |
| TC-AUTH-LP-139 | TC-AUTH-LP-E2E-029 | FE+BE |
| TC-AUTH-LP-140 | TC-AUTH-LP-E2E-029 | FE+BE |
| TC-AUTH-LP-141 | TC-AUTH-LP-E2E-030 | FE+BE |
| TC-AUTH-LP-142 | TC-AUTH-LP-E2E-030 | FE+BE |
| TC-AUTH-LP-143 | TC-AUTH-LP-E2E-030 | FE+BE |
| TC-AUTH-LP-144 | TC-AUTH-LP-E2E-029 | FE+BE |
| TC-AUTH-LP-145 | TC-AUTH-LP-E2E-029 | FE+BE |
| TC-AUTH-LP-146 | TC-AUTH-LP-E2E-033 | FE+BE |
| TC-AUTH-LP-147 | TC-AUTH-LP-E2E-033 | FE+BE |
| TC-AUTH-LP-148 | TC-AUTH-LP-E2E-032 | FE+BE |
| TC-AUTH-LP-149 | TC-AUTH-LP-E2E-030 | FE+BE |
| TC-AUTH-LP-150 | TC-AUTH-LP-E2E-032 | FE+BE |
| TC-AUTH-LP-151 | TC-AUTH-LP-E2E-011 | FE+BE |
| TC-AUTH-LP-152 | TC-AUTH-LP-E2E-050 | FE+BE |
| TC-AUTH-LP-153 | TC-AUTH-LP-E2E-041 | FE+BE |
| TC-AUTH-LP-154 | TC-AUTH-LP-E2E-023 | FE+BE |
| TC-AUTH-LP-155 | TC-AUTH-LP-E2E-028 | FE+BE |
| TC-AUTH-LP-156 | TC-AUTH-LP-E2E-003 | FE+BE |
| TC-AUTH-LP-157 | TC-AUTH-LP-E2E-028 | FE+BE |
| TC-AUTH-LP-157 | TC-AUTH-LP-E2E-043 | FE+BE |
| TC-AUTH-LP-158 | TC-AUTH-LP-E2E-024 | FE+BE |
| TC-AUTH-LP-159 | TC-AUTH-LP-E2E-047 | FE+BE |
| TC-AUTH-LP-160 | TC-AUTH-LP-E2E-048 | FE+BE |
| TC-AUTH-LP-161 | TC-AUTH-LP-E2E-002 | FE+BE |
| TC-AUTH-LP-161 | TC-AUTH-LP-E2E-042 | FE+BE |
| TC-AUTH-LP-162 | TC-AUTH-LP-E2E-039 | FE+BE |
| TC-AUTH-LP-163 | TC-AUTH-LP-E2E-052 | FE+BE |

## TC hanya-BE

Tidak ada.
