# Coverage E2E — Auth > Reset Password

Sumber: `auth/reset-password/TestCases/tc-reset-password.md` (156 TC aktif, `TC-AUTH-RST-01`–`156`). Suite: `specs/Auth/ResetPassword/`. Status semua spec: `draft`, belum ada script.

**Verifikasi lint:** `node_modules/.bin/spectra lint --strict specs/Auth/ResetPassword` → `✓ 46 specs and 1 suites verified. 0 lint errors found.`

**Aturan seleksi:** sesuai `docs/e2e-conventions.md` bagian 2, semua TC masuk spec kecuali hanya-BE. Semua 156 TC granular masuk spec dan tepat satu spec per TC (0 TC hanya-BE; kontrak endpoint dicakup `tc-reset-password-backend.md` dengan namespace `TC-AUTH-RST-BE-*`). Tidak ada spec `Mode: mock` murni: kegagalan 5xx dan timeout yang dipaksa lewat `Spectra.intercept` di atas backend nyata ditandai FE+BE (bagian 6), dan failure injection sisi server atau penyedia tetap FE+BE.

**Nomor folder:** Prefix `TC-AUTH-RST-E2E-` berasal dari `AUTH` + `RST` di `foundation/tc-prefix-registry.md`. Nomor adalah urutan spec (`001`–`046`), bukan nomor TC sumber.

**Akun uji:** tiap spec membuat user sendiri lewat API di hook `before` dengan email bersuffix `+{runId}-NNN`; akun Pre-setup TC (Budi Santoso dan seterusnya) hanya templat nama dan status. Password lewat env var `RST_PASSWORD`, `RST_PASSWORD_NEW`, `RST_PASSWORD_ALT`, `RST_PASSWORD_ALT2`, `RST_PASSWORD_REPLAY`, `RST_PASSWORD_LOWER`, `RST_PASSWORD_WRONG`; akun admin lewat `GS_TC_PASSWORD`.

**Pembagian TC lintas spec:** asersi "tidak ada entri log" dari TC di spec lain diuji lewat aksi nyata yang dipicu di spec `TC-AUTH-RST-E2E-043-absence-not-logged` (kelas g). Isi email reset hanya diasersi di spec 007 (`TC-AUTH-RST-145`).

## TC granular → spec e2e

| Spec | Isi | TC sumber | Platform |
|---|---|---|---|
| TC-AUTH-RST-E2E-001-screening-request-page | Screening Halaman Reset Password (Request), State Awal, dan Urutan Tab | 01, 02, 03 | web |
| TC-AUTH-RST-E2E-002-navigation-login-email-carry | Navigasi Login with Password dan Reset Password serta Pembawaan Email | 04, 05, 116 | web |
| TC-AUTH-RST-E2E-003-email-validation-blocked | Validasi Field Email pada Halaman Request Diblokir | 15, 16, 17, 18 | web |
| TC-AUTH-RST-E2E-004-recaptcha-gate-web | Gate reCAPTCHA pada Halaman Request di Web | 19, 20, 22 | web |
| TC-AUTH-RST-E2E-005-email-normalization-success | Normalisasi Email pada Request: Trim, Huruf Besar, dan Plus-Addressing | 13, 14, 146 | web |
| TC-AUTH-RST-E2E-006-request-success-loading | Request Reset Sukses dan Loading pada Button Reset Password | 12, 28 | web |
| TC-AUTH-RST-E2E-007-reset-email-content-and-link | Isi Email Reset dan Tautan yang Membuka Setup New Password | 118, 145 | web |
| TC-AUTH-RST-E2E-008-unregistered-deleted-pending-email | Request dengan Email Tidak Terdaftar, Akun Dihapus, dan Email Pending | 23, 24, 155 | web |
| TC-AUTH-RST-E2E-009-inactive-pending-activation-status | Request untuk Akun Inactive, Pending Activation, dan Perubahan Status oleh Admin | 25, 115, 151, 153 | web |
| TC-AUTH-RST-E2E-010-request-special-client-conditions | Request Sukses pada Client Suspended, Plan Starter, dan Pending Email Confirmation | 26, 27, 154 | web |
| TC-AUTH-RST-E2E-011-request-cooldown-60s | Cooldown 60 Detik pada Request Ulang untuk Email yang Sama | 29, 139, 147 | web |
| TC-AUTH-RST-E2E-012-email-quota-5-per-24h | Kuota 5 Percobaan per 24 Jam per Email pada Request | 30, 31, 32, 34, 117, 148 | web |
| TC-AUTH-RST-E2E-013-email-window-time-shift | Budget Request dan Resend Bersama serta Jendela Bergulir 24 Jam per Email | 33, 38 | web |
| TC-AUTH-RST-E2E-014-ip-rate-limit-429 | Rate Limit per IP: Penolakan 429 pada Halaman Request | 35, 36, 142 | web |
| TC-AUTH-RST-E2E-015-ip-counter-types-and-window | Counter per IP: Jenis Request yang Dihitung dan Jendela Bergulir 1 Jam | 37, 138 | web |
| TC-AUTH-RST-E2E-016-screening-email-sent-countdown | Screening Halaman Email Sent!, Countdown Resend, dan Navigasi Kembali | 39, 40, 41, 45, 46 | web |
| TC-AUTH-RST-E2E-017-resend-success-old-link | Resend Sukses Menerbitkan Token Baru dan Membatalkan Tautan Lama | 42, 43, 44, 51 | web |
| TC-AUTH-RST-E2E-018-resend-rejections | Resend untuk Akun Inactive, Dihapus, dan Kuota Per Email Habis | 47, 48, 49 | web |
| TC-AUTH-RST-E2E-019-valid-link-idempotent-superseded | Tautan Valid Idempotent dan Penggantian Token oleh Request Baru | 54, 57 | web |
| TC-AUTH-RST-E2E-020-404-expired-page-and-bad-token | Halaman 404 Varian Expired, Request New Link, dan Token Tidak Dikenal atau Kosong | 52, 53, 58, 59 | web |
| TC-AUTH-RST-E2E-021-token-24h-lifetime | Masa Berlaku Token Reset 24 Jam: 23:59, 24:00, 24:01, dan Form Terbuka | 55, 56, 131, 134, 149 | web |
| TC-AUTH-RST-E2E-022-account-status-vs-link-and-form | Akun Inactive atau Dihapus saat Tautan Dibuka dan saat Form Setup Terbuka | 60, 61, 132 | web |
| TC-AUTH-RST-E2E-023-email-change-invalidates-token | Perubahan Email User Meng-invalidate Token Reset Aktif | 114, 133, 141 | web |
| TC-AUTH-RST-E2E-024-screening-setup-new-password | Screening Halaman Setup New Password, State Awal, ARIA, Tab, dan Toggle Intip | 63, 64, 65, 66, 70 | web |
| TC-AUTH-RST-E2E-025-password-policy-checklist | Checklist Password Policy Reaktif, Batas Karakter 8–72, dan Karakter Spesial | 67, 68, 69, 80 | web |
| TC-AUTH-RST-E2E-026-setup-form-validation | Validasi Form Setup New Password: Field Wajib dan Konfirmasi Cocok | 71, 72, 73, 74 | web |
| TC-AUTH-RST-E2E-027-server-rejection-then-success | Penolakan Server atas Password Tidak Valid lalu Submit Sukses pada Token yang Sama | 75, 76, 77, 78, 79 | web |
| TC-AUTH-RST-E2E-028-submit-success-and-already-used | Submit New Password Sukses, Halaman Hasil, Tautan Already Used, dan Request Tanpa Cooldown | 81, 82, 83, 84, 85, 86, 143 | web |
| TC-AUTH-RST-E2E-029-login-with-new-password | Login dengan Password Baru, Password Lama Ditolak, dan Sifat Case-Sensitive | 111, 112 | web |
| TC-AUTH-RST-E2E-030-lock-recovery-15m-1h-requires-reset | Pemulihan Lock 15 Menit, 1 Jam, dan Requires Reset lewat Reset Password | 106, 107, 108 | web |
| TC-AUTH-RST-E2E-031-lock-recovery-permanent-counters | Pemulihan Lock Permanen serta Counter Kegagalan dan Eskalasi Dibersihkan | 109, 110 | web |
| TC-AUTH-RST-E2E-032-sessions-ended-all-devices | Submit Sukses Mengakhiri Semua Sesi Aktif di Semua Device | 113 | web+mobile |
| TC-AUTH-RST-E2E-033-biometric-refresh-token-revoked | Reset Sukses Mencabut Refresh Token Biometric | 140 | web+mobile |
| TC-AUTH-RST-E2E-034-double-submit | Klik Ganda Button Reset Password pada Request dan Setup New Password | 89, 93 | web |
| TC-AUTH-RST-E2E-035-multi-tab | Multi-Tab: Submit Ganda pada Token yang Sama dan Resend di Tab Lain | 129, 130 | web |
| TC-AUTH-RST-E2E-036-resilience-intercept | Ketahanan Request, Resend, Validate Link, dan Submit terhadap 5xx dan Timeout (Intercept) | 50, 62, 87, 88, 90, 91 | web |
| TC-AUTH-RST-E2E-037-resilience-backend-provider-failure | Ketahanan terhadap Kegagalan Sisi Server dan Penyedia: reCAPTCHA, Log, Email, dan Rollback Submit | 21, 92, 103, 144 | web |
| TC-AUTH-RST-E2E-038-defense-request-endpoint | Defense-in-Depth Request: Payload Tidak Valid, Tanpa reCAPTCHA, Token Palsu, dan Injeksi | 119, 120, 121, 128 | web |
| TC-AUTH-RST-E2E-039-defense-confirm-resend-endpoint | Defense-in-Depth Confirm dan Resend: Request Langsung ke Endpoint | 122, 123, 124, 125, 126, 127, 152, 156 | web |
| TC-AUTH-RST-E2E-040-log-request-resend | Pencatatan Request dan Resend pada Activity Log Session dan User Log | 94, 95, 96, 97 | web |
| TC-AUTH-RST-E2E-041-log-submit | Pencatatan Submit: Policy Gagal, Sama dengan Password Lama, dan Sukses | 98, 99, 101 | web |
| TC-AUTH-RST-E2E-042-log-token-states | Pencatatan Status Token: Akun Nonaktif atau Dihapus, Invalidated, dan Consumed | 100, 135, 136 | web |
| TC-AUTH-RST-E2E-043-absence-not-logged | Absence: Aksi Reset Password yang Tidak Boleh Dicatat pada Activity Log Session dan User Log | 104, 105, 137 | web |
| TC-AUTH-RST-E2E-044-active-session-opens-reset | User dengan Sesi Aktif Membuka Halaman Reset Password dan Tautan Reset | 10, 11 | web |
| TC-AUTH-RST-E2E-045-android-reset-screen | Layar Reset Password Android: Tanpa reCAPTCHA, Button Terjangkau, Request, dan Atribut Log | 06, 07, 102, 150 | mobile+web |
| TC-AUTH-RST-E2E-046-android-app-link | App Link Android: Tautan Reset Dibuka dengan dan Tanpa Aplikasi Terpasang | 08, 09 | mobile |

Total: **156 dari 156 TC aktif tercakup, masing-masing tepat di satu spec** (46 spec: 42 web, 4 melibatkan mobile Android).

## TC sumber yang tidak masuk spec

Tidak ada (0 TC hanya-BE).

## Verifikasi silang

- Tidak ada `sourceTc` yang muncul di dua spec; seluruh 156 ID unik terpetakan 1-ke-1 (diverifikasi dengan skrip terhadap frontmatter).
- Spec melewati smell 35 langkah (jumlah langkah setelah Verifikasi dipecah per klausa): 009 (51), 011 (53), 012 (46), 016 (49), 018 (36), 024 (42), 025 (45), 027 (48), 028 (45), 030 (41), 036 (59), 039 (60), 042 (41), 043 (157). Langkah Verifikasi dan langkah pemulihan jam menjadi penyumbang utama; alasan tiap spec ada di `## Notes`.

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-AUTH-RST-01 | TC-AUTH-RST-E2E-001 | FE+BE |
| TC-AUTH-RST-02 | TC-AUTH-RST-E2E-001 | FE+BE |
| TC-AUTH-RST-03 | TC-AUTH-RST-E2E-001 | FE+BE |
| TC-AUTH-RST-04 | TC-AUTH-RST-E2E-002 | FE+BE |
| TC-AUTH-RST-05 | TC-AUTH-RST-E2E-002 | FE+BE |
| TC-AUTH-RST-06 | TC-AUTH-RST-E2E-045 | FE+BE |
| TC-AUTH-RST-07 | TC-AUTH-RST-E2E-045 | FE+BE |
| TC-AUTH-RST-08 | TC-AUTH-RST-E2E-046 | FE+BE |
| TC-AUTH-RST-09 | TC-AUTH-RST-E2E-046 | FE+BE |
| TC-AUTH-RST-10 | TC-AUTH-RST-E2E-044 | FE+BE |
| TC-AUTH-RST-11 | TC-AUTH-RST-E2E-044 | FE+BE |
| TC-AUTH-RST-12 | TC-AUTH-RST-E2E-006 | FE+BE |
| TC-AUTH-RST-13 | TC-AUTH-RST-E2E-005 | FE+BE |
| TC-AUTH-RST-14 | TC-AUTH-RST-E2E-005 | FE+BE |
| TC-AUTH-RST-15 | TC-AUTH-RST-E2E-003 | FE+BE |
| TC-AUTH-RST-16 | TC-AUTH-RST-E2E-003 | FE+BE |
| TC-AUTH-RST-17 | TC-AUTH-RST-E2E-003 | FE+BE |
| TC-AUTH-RST-18 | TC-AUTH-RST-E2E-003 | FE+BE |
| TC-AUTH-RST-19 | TC-AUTH-RST-E2E-004 | FE+BE |
| TC-AUTH-RST-20 | TC-AUTH-RST-E2E-004 | FE+BE |
| TC-AUTH-RST-21 | TC-AUTH-RST-E2E-037 | FE+BE |
| TC-AUTH-RST-22 | TC-AUTH-RST-E2E-004 | FE+BE |
| TC-AUTH-RST-23 | TC-AUTH-RST-E2E-008 | FE+BE |
| TC-AUTH-RST-24 | TC-AUTH-RST-E2E-008 | FE+BE |
| TC-AUTH-RST-25 | TC-AUTH-RST-E2E-009 | FE+BE |
| TC-AUTH-RST-26 | TC-AUTH-RST-E2E-010 | FE+BE |
| TC-AUTH-RST-27 | TC-AUTH-RST-E2E-010 | FE+BE |
| TC-AUTH-RST-28 | TC-AUTH-RST-E2E-006 | FE+BE |
| TC-AUTH-RST-29 | TC-AUTH-RST-E2E-011 | FE+BE |
| TC-AUTH-RST-30 | TC-AUTH-RST-E2E-012 | FE+BE |
| TC-AUTH-RST-31 | TC-AUTH-RST-E2E-012 | FE+BE |
| TC-AUTH-RST-32 | TC-AUTH-RST-E2E-012 | FE+BE |
| TC-AUTH-RST-33 | TC-AUTH-RST-E2E-013 | FE+BE |
| TC-AUTH-RST-34 | TC-AUTH-RST-E2E-012 | FE+BE |
| TC-AUTH-RST-35 | TC-AUTH-RST-E2E-014 | FE+BE |
| TC-AUTH-RST-36 | TC-AUTH-RST-E2E-014 | FE+BE |
| TC-AUTH-RST-37 | TC-AUTH-RST-E2E-015 | FE+BE |
| TC-AUTH-RST-38 | TC-AUTH-RST-E2E-013 | FE+BE |
| TC-AUTH-RST-39 | TC-AUTH-RST-E2E-016 | FE+BE |
| TC-AUTH-RST-40 | TC-AUTH-RST-E2E-016 | FE+BE |
| TC-AUTH-RST-41 | TC-AUTH-RST-E2E-016 | FE+BE |
| TC-AUTH-RST-42 | TC-AUTH-RST-E2E-017 | FE+BE |
| TC-AUTH-RST-43 | TC-AUTH-RST-E2E-017 | FE+BE |
| TC-AUTH-RST-44 | TC-AUTH-RST-E2E-017 | FE+BE |
| TC-AUTH-RST-45 | TC-AUTH-RST-E2E-016 | FE+BE |
| TC-AUTH-RST-46 | TC-AUTH-RST-E2E-016 | FE+BE |
| TC-AUTH-RST-47 | TC-AUTH-RST-E2E-018 | FE+BE |
| TC-AUTH-RST-48 | TC-AUTH-RST-E2E-018 | FE+BE |
| TC-AUTH-RST-49 | TC-AUTH-RST-E2E-018 | FE+BE |
| TC-AUTH-RST-50 | TC-AUTH-RST-E2E-036 | FE+BE |
| TC-AUTH-RST-51 | TC-AUTH-RST-E2E-017 | FE+BE |
| TC-AUTH-RST-52 | TC-AUTH-RST-E2E-020 | FE+BE |
| TC-AUTH-RST-53 | TC-AUTH-RST-E2E-020 | FE+BE |
| TC-AUTH-RST-54 | TC-AUTH-RST-E2E-019 | FE+BE |
| TC-AUTH-RST-55 | TC-AUTH-RST-E2E-021 | FE+BE |
| TC-AUTH-RST-56 | TC-AUTH-RST-E2E-021 | FE+BE |
| TC-AUTH-RST-57 | TC-AUTH-RST-E2E-019 | FE+BE |
| TC-AUTH-RST-58 | TC-AUTH-RST-E2E-020 | FE+BE |
| TC-AUTH-RST-59 | TC-AUTH-RST-E2E-020 | FE+BE |
| TC-AUTH-RST-60 | TC-AUTH-RST-E2E-022 | FE+BE |
| TC-AUTH-RST-61 | TC-AUTH-RST-E2E-022 | FE+BE |
| TC-AUTH-RST-62 | TC-AUTH-RST-E2E-036 | FE+BE |
| TC-AUTH-RST-63 | TC-AUTH-RST-E2E-024 | FE+BE |
| TC-AUTH-RST-64 | TC-AUTH-RST-E2E-024 | FE+BE |
| TC-AUTH-RST-65 | TC-AUTH-RST-E2E-024 | FE+BE |
| TC-AUTH-RST-66 | TC-AUTH-RST-E2E-024 | FE+BE |
| TC-AUTH-RST-67 | TC-AUTH-RST-E2E-025 | FE+BE |
| TC-AUTH-RST-68 | TC-AUTH-RST-E2E-025 | FE+BE |
| TC-AUTH-RST-69 | TC-AUTH-RST-E2E-025 | FE+BE |
| TC-AUTH-RST-70 | TC-AUTH-RST-E2E-024 | FE+BE |
| TC-AUTH-RST-71 | TC-AUTH-RST-E2E-026 | FE+BE |
| TC-AUTH-RST-72 | TC-AUTH-RST-E2E-026 | FE+BE |
| TC-AUTH-RST-73 | TC-AUTH-RST-E2E-026 | FE+BE |
| TC-AUTH-RST-74 | TC-AUTH-RST-E2E-026 | FE+BE |
| TC-AUTH-RST-75 | TC-AUTH-RST-E2E-027 | FE+BE |
| TC-AUTH-RST-76 | TC-AUTH-RST-E2E-027 | FE+BE |
| TC-AUTH-RST-77 | TC-AUTH-RST-E2E-027 | FE+BE |
| TC-AUTH-RST-78 | TC-AUTH-RST-E2E-027 | FE+BE |
| TC-AUTH-RST-79 | TC-AUTH-RST-E2E-027 | FE+BE |
| TC-AUTH-RST-80 | TC-AUTH-RST-E2E-025 | FE+BE |
| TC-AUTH-RST-81 | TC-AUTH-RST-E2E-028 | FE+BE |
| TC-AUTH-RST-82 | TC-AUTH-RST-E2E-028 | FE+BE |
| TC-AUTH-RST-83 | TC-AUTH-RST-E2E-028 | FE+BE |
| TC-AUTH-RST-84 | TC-AUTH-RST-E2E-028 | FE+BE |
| TC-AUTH-RST-85 | TC-AUTH-RST-E2E-028 | FE+BE |
| TC-AUTH-RST-86 | TC-AUTH-RST-E2E-028 | FE+BE |
| TC-AUTH-RST-87 | TC-AUTH-RST-E2E-036 | FE+BE |
| TC-AUTH-RST-88 | TC-AUTH-RST-E2E-036 | FE+BE |
| TC-AUTH-RST-89 | TC-AUTH-RST-E2E-034 | FE+BE |
| TC-AUTH-RST-90 | TC-AUTH-RST-E2E-036 | FE+BE |
| TC-AUTH-RST-91 | TC-AUTH-RST-E2E-036 | FE+BE |
| TC-AUTH-RST-92 | TC-AUTH-RST-E2E-037 | FE+BE |
| TC-AUTH-RST-93 | TC-AUTH-RST-E2E-034 | FE+BE |
| TC-AUTH-RST-94 | TC-AUTH-RST-E2E-040 | FE+BE |
| TC-AUTH-RST-95 | TC-AUTH-RST-E2E-040 | FE+BE |
| TC-AUTH-RST-96 | TC-AUTH-RST-E2E-040 | FE+BE |
| TC-AUTH-RST-97 | TC-AUTH-RST-E2E-040 | FE+BE |
| TC-AUTH-RST-98 | TC-AUTH-RST-E2E-041 | FE+BE |
| TC-AUTH-RST-99 | TC-AUTH-RST-E2E-041 | FE+BE |
| TC-AUTH-RST-100 | TC-AUTH-RST-E2E-042 | FE+BE |
| TC-AUTH-RST-101 | TC-AUTH-RST-E2E-041 | FE+BE |
| TC-AUTH-RST-102 | TC-AUTH-RST-E2E-045 | FE+BE |
| TC-AUTH-RST-103 | TC-AUTH-RST-E2E-037 | FE+BE |
| TC-AUTH-RST-104 | TC-AUTH-RST-E2E-043 | FE+BE |
| TC-AUTH-RST-105 | TC-AUTH-RST-E2E-043 | FE+BE |
| TC-AUTH-RST-106 | TC-AUTH-RST-E2E-030 | FE+BE |
| TC-AUTH-RST-107 | TC-AUTH-RST-E2E-030 | FE+BE |
| TC-AUTH-RST-108 | TC-AUTH-RST-E2E-030 | FE+BE |
| TC-AUTH-RST-109 | TC-AUTH-RST-E2E-031 | FE+BE |
| TC-AUTH-RST-110 | TC-AUTH-RST-E2E-031 | FE+BE |
| TC-AUTH-RST-111 | TC-AUTH-RST-E2E-029 | FE+BE |
| TC-AUTH-RST-112 | TC-AUTH-RST-E2E-029 | FE+BE |
| TC-AUTH-RST-113 | TC-AUTH-RST-E2E-032 | FE+BE |
| TC-AUTH-RST-114 | TC-AUTH-RST-E2E-023 | FE+BE |
| TC-AUTH-RST-115 | TC-AUTH-RST-E2E-009 | FE+BE |
| TC-AUTH-RST-116 | TC-AUTH-RST-E2E-002 | FE+BE |
| TC-AUTH-RST-117 | TC-AUTH-RST-E2E-012 | FE+BE |
| TC-AUTH-RST-118 | TC-AUTH-RST-E2E-007 | FE+BE |
| TC-AUTH-RST-119 | TC-AUTH-RST-E2E-038 | FE+BE |
| TC-AUTH-RST-120 | TC-AUTH-RST-E2E-038 | FE+BE |
| TC-AUTH-RST-121 | TC-AUTH-RST-E2E-038 | FE+BE |
| TC-AUTH-RST-122 | TC-AUTH-RST-E2E-039 | FE+BE |
| TC-AUTH-RST-123 | TC-AUTH-RST-E2E-039 | FE+BE |
| TC-AUTH-RST-124 | TC-AUTH-RST-E2E-039 | FE+BE |
| TC-AUTH-RST-125 | TC-AUTH-RST-E2E-039 | FE+BE |
| TC-AUTH-RST-126 | TC-AUTH-RST-E2E-039 | FE+BE |
| TC-AUTH-RST-127 | TC-AUTH-RST-E2E-039 | FE+BE |
| TC-AUTH-RST-128 | TC-AUTH-RST-E2E-038 | FE+BE |
| TC-AUTH-RST-129 | TC-AUTH-RST-E2E-035 | FE+BE |
| TC-AUTH-RST-130 | TC-AUTH-RST-E2E-035 | FE+BE |
| TC-AUTH-RST-131 | TC-AUTH-RST-E2E-021 | FE+BE |
| TC-AUTH-RST-132 | TC-AUTH-RST-E2E-022 | FE+BE |
| TC-AUTH-RST-133 | TC-AUTH-RST-E2E-023 | FE+BE |
| TC-AUTH-RST-134 | TC-AUTH-RST-E2E-021 | FE+BE |
| TC-AUTH-RST-135 | TC-AUTH-RST-E2E-042 | FE+BE |
| TC-AUTH-RST-136 | TC-AUTH-RST-E2E-042 | FE+BE |
| TC-AUTH-RST-137 | TC-AUTH-RST-E2E-043 | FE+BE |
| TC-AUTH-RST-138 | TC-AUTH-RST-E2E-015 | FE+BE |
| TC-AUTH-RST-139 | TC-AUTH-RST-E2E-011 | FE+BE |
| TC-AUTH-RST-140 | TC-AUTH-RST-E2E-033 | FE+BE |
| TC-AUTH-RST-141 | TC-AUTH-RST-E2E-023 | FE+BE |
| TC-AUTH-RST-142 | TC-AUTH-RST-E2E-014 | FE+BE |
| TC-AUTH-RST-143 | TC-AUTH-RST-E2E-028 | FE+BE |
| TC-AUTH-RST-144 | TC-AUTH-RST-E2E-037 | FE+BE |
| TC-AUTH-RST-145 | TC-AUTH-RST-E2E-007 | FE+BE |
| TC-AUTH-RST-146 | TC-AUTH-RST-E2E-005 | FE+BE |
| TC-AUTH-RST-147 | TC-AUTH-RST-E2E-011 | FE+BE |
| TC-AUTH-RST-148 | TC-AUTH-RST-E2E-012 | FE+BE |
| TC-AUTH-RST-149 | TC-AUTH-RST-E2E-021 | FE+BE |
| TC-AUTH-RST-150 | TC-AUTH-RST-E2E-045 | FE+BE |
| TC-AUTH-RST-151 | TC-AUTH-RST-E2E-009 | FE+BE |
| TC-AUTH-RST-152 | TC-AUTH-RST-E2E-039 | FE+BE |
| TC-AUTH-RST-153 | TC-AUTH-RST-E2E-009 | FE+BE |
| TC-AUTH-RST-154 | TC-AUTH-RST-E2E-010 | FE+BE |
| TC-AUTH-RST-155 | TC-AUTH-RST-E2E-008 | FE+BE |
| TC-AUTH-RST-156 | TC-AUTH-RST-E2E-039 | FE+BE |
