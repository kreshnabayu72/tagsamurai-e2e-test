# Coverage E2E — Auth > Session Management

Sumber: `auth/session-management/TestCases/tc-session-management.md` (349 TC aktif, `TC-AUTH-SES-1`–`349`, hash SHA-256 `5cf488596291c1f8…`). Suite: `specs/Auth/SessionManagement/`. Status seluruh spec: `draft`, belum ada script TestSpectra.

**Verifikasi lint:** `npx spectra lint --strict specs/Auth/SessionManagement` → `✓ 84 specs and 1 suites verified. All spec schemas are valid. 0 lint errors found.` (2026-11-23)

**Seleksi:** sesuai `docs/e2e-conventions.md` bagian 2, 347 dari 349 TC masuk spec; tidak ada TC hanya-BE. TC-AUTH-SES-260 dan 261 (iOS) Ditahan karena PRD §12 #4 menyatakan iOS di luar scope rilis pertama (bagian "Ditahan" di bawah). TC yang menembak endpoint langsung tanpa UI (antara lain TC-233, 234, 235, 322, 231, 232, 250, 320, 256) tetap masuk sebagai spec kelas a. Hambatan teknis dan label `Manual Only` (jam server, perangkat Android/iOS, biometrik, SSE, failure injection, status Client dan subscription, seat dan kuota) bukan alasan mengeluarkan TC; semua kebutuhan ditulis di `## Prerequisites` tiap spec.

**Mode:** semua spec `FE+BE`. Kegagalan 5xx dan timeout dipaksa lewat `Spectra.intercept()` di atas backend nyata atau dipicu di sisi server, sehingga tidak ada spec `Mode: mock`. Spec mobile memakai `coverage.mobile: automated`; spec yang memakai web dan mobile memakai keduanya.

**Nomor spec:** prefix `TC-AUTH-SES-E2E-` dari `AUTH` + `SES` pada `foundation/tc-prefix-registry.md`; `001`–`084` adalah nomor urut spec dalam suite.

**Asersi absence log (kelas g, prinsip 13):** spec fungsional tidak menulis asersi "tidak ada pencatatan" dan merujuknya ke spec absence (S-05). Spec absence: 060 (TC sendiri: 190, 195, 196, 202, 203, 211, 267), 059 (TC-212), serta lima spec absence per domain 066 (duplicate login dan session expired), 067 (sesi-produk dan concurrent), 068 (subscription tidak aktif), 069 (penolakan, force-logout, dan aksi admin), dan 070 (biometric, termasuk Expected d TC-335 dan 336 dari spec 080). TC yang klausa absence-nya dipindah ke 066–070 tercatat di `sourceTc` kedua spec (spec utama di tabel Lapisan per TC) dan di `## Notes` kedua spec (prinsip 10).

---

## TC granular → spec e2e

| Spec | Isi | TC sumber | Platform |
|---|---|---|---|
| TC-AUTH-SES-E2E-001-screening-dialog-duplicate-login-dan-logged-out | Screening Dialog Duplicate Login Attempt dan Dialog Logged Out | 1, 2, 37, 38 | web |
| TC-AUTH-SES-E2E-002-screening-dialog-lifecycle-akun-dan-akses | Screening Dialog Password Changed, Account Deactivated, Account no longer Active, Log Out, dan Access Restricted | 5, 6, 7, 8, 9 | web + mobile |
| TC-AUTH-SES-E2E-003-screening-popup-concurrent-dan-subscription | Screening Popup Concurrent Session Limit Reached dan Subscription Not Active | 10, 11 | web |
| TC-AUTH-SES-E2E-004-screening-session-expired-dan-idle-warning-web | Screening Dialog Session Expired dan Toast Idle Warning di Web | 3, 12 | web |
| TC-AUTH-SES-E2E-005-screening-session-expired-dan-idle-warning-mobile | Screening Dialog Session Expired dan Toast Idle Warning di Aplikasi Mobile | 4, 13 | mobile |
| TC-AUTH-SES-E2E-006-screening-biometric-mobile | Screening Layar Biometric di Aplikasi Mobile | 14, 15, 16 | mobile |
| TC-AUTH-SES-E2E-007-dialog-lifecycle-lintas-role-dan-entitas | Dialog Lifecycle Sesi Tampil Sama untuk Role Read Only, Entitas Distributor, dan Entitas Partner | 17, 18, 19 | web |
| TC-AUTH-SES-E2E-008-dialog-lifecycle-di-dalam-produk-lain | Dialog Lifecycle Sesi Tampil di Dalam Admin Console, Supply Asset, dan Fixed Asset | 290, 291, 292 | web |
| TC-AUTH-SES-E2E-009-limit-login-web-dan-duplicate-login | Limit Login Web: Login Pertama dan Dialog Duplicate Login Attempt via Password, OTP, dan MFA | 20, 21, 24, 25 | web |
| TC-AUTH-SES-E2E-010-limit-login-mobile-dan-duplicate-login | Limit Login Mobile: Dialog Duplicate Login Attempt Lintas Perangkat Android dan Login Mobile saat Sesi Web Aktif | 22, 23, 293, 294 | web + mobile |
| TC-AUTH-SES-E2E-011-confirm-cancel-duplicate-login-web | Cancel, Escape, Backdrop, Klik Ganda Confirm, dan Confirm pada Dialog Duplicate Login Attempt di Web | 29, 30, 31, 32, 26, 27 | web |
| TC-AUTH-SES-E2E-012-dialog-lifecycle-multi-tab | Dialog Lifecycle Multi-Tab: OK Hanya Berlaku untuk Tab yang Diklik dan Dua Dialog Duplicate Login Bersamaan | 28, 79, 94, 262, 135, 321 | web |
| TC-AUTH-SES-E2E-013-token-pra-auth-dan-sesi-lama-expired-saat-confirm | Token Pra-autentikasi dan Sesi Lama Kedaluwarsa saat Confirm Duplicate Login | 34, 35, 36, 256, 282 | web |
| TC-AUTH-SES-E2E-014-resilience-kegagalan-server-sesi-web | Resilience Kegagalan Server pada Sesi Web: Confirm, Refresh, Heartbeat, Buka Produk, Force-Logout, dan Logout | 33, 51, 52, 61, 110, 139, 143 | web |
| TC-AUTH-SES-E2E-015-heartbeat-dan-sinyal-aktivitas-web | Heartbeat dan Sinyal Aktivitas Web | 39, 40, 41, 42, 43, 244 | web |
| TC-AUTH-SES-E2E-016-idle-timeout-dan-toast-warning-web | Idle Timeout dan Toast Idle Warning Web | 44, 45, 46, 47, 48, 284 | web |
| TC-AUTH-SES-E2E-017-batas-idle-konfigurasi | Batas Idle Konfigurasi General Settings | 59, 60, 283, 217, 218 | web |
| TC-AUTH-SES-E2E-018-refresh-pada-dialog-session-expired | Refresh pada Dialog Session Expired dan Browser Dibuka Ulang | 50, 56, 57, 268, 58, 62 | web |
| TC-AUTH-SES-E2E-019-session-expired-multi-tab | Session Expired Multi Tab Web | 53, 54, 55, 49 | web |
| TC-AUTH-SES-E2E-020-accessibility-focus-trap-dialog-lifecycle | Accessibility Focus Trap dan Role Alertdialog Dialog Lifecycle | 251, 252, 305, 309, 310, 311, 312 | web + mobile |
| TC-AUTH-SES-E2E-021-idle-dan-lifecycle-sesi-mobile | Idle Timeout dan Lifecycle Sesi Mobile: Foreground, Background, dan Biometric | 63, 64, 65, 66, 71, 253 | web + mobile |
| TC-AUTH-SES-E2E-022-app-dihapus-dari-background-dan-push | App Dihapus dari Background dan Notifikasi Push Setelah Sesi Berakhir | 67, 68, 69, 317, 70 | mobile |
| TC-AUTH-SES-E2E-023-sesi-yatim-app-kill-dan-id-device | Sesi Yatim Bekas App-Kill: ID Device dan Batas Heartbeat 60 Detik | 254, 297, 298, 323 | web + mobile |
| TC-AUTH-SES-E2E-024-app-access-revoke-dan-delete-client | App Access Revoke dan Delete Client: Pemutusan Sesi-Produk | 72, 73, 74, 75, 76, 304 | web |
| TC-AUTH-SES-E2E-025-client-suspended-dialog-access-restricted | Client Suspended: Dialog Access Restricted, OK, dan Unsuspend | 77, 78, 85 | web |
| TC-AUTH-SES-E2E-026-client-suspended-kasus-tepi | Client Suspended: Push Terlewat, Tampil Ulang, Write Guard, dan Bulk Suspend | 80, 81, 82, 83, 84, 86, 87, 269 | web |
| TC-AUTH-SES-E2E-027-user-dinonaktifkan-di-produk-fixed-asset | User Dinonaktifkan di Produk Fixed Asset: Pemutusan Sesi-Produk | 326, 327 | web |
| TC-AUTH-SES-E2E-028-delete-dan-deactivate-akun-web | Deactivate dan Delete Akun User yang Sedang Login di Web | 90, 92, 88, 89, 91 | web |
| TC-AUTH-SES-E2E-029-invalidasi-semua-sesi-saat-akun-dihapus-atau-dinonaktifkan | Invalidasi Semua Sesi Web, Mobile, dan Sesi-produk saat Akun Dinonaktifkan atau Dihapus | 93, 316 | web + mobile |
| TC-AUTH-SES-E2E-030-popup-concurrent-limit-saat-seat-penuh | Popup Concurrent Session Limit Reached saat Seat Penuh | 96, 97, 98, 99, 100 | web |
| TC-AUTH-SES-E2E-031-buka-produk-seat-tersedia-dan-reuse-sesi-produk | Buka Produk saat Seat Tersedia dan Reuse Sesi-produk | 95, 101, 102, 103, 105 | web |
| TC-AUTH-SES-E2E-032-admin-console-dan-global-settings-tanpa-concurrent | Admin Console dan Global Settings Tanpa Evaluasi Concurrent dan Tanpa Seat | 106, 107, 108, 109, 221 | web + mobile |
| TC-AUTH-SES-E2E-033-cascade-sesi-produk-dan-pelepasan-seat | Cascade Sesi Platform ke Sesi-produk dan Pelepasan Seat | 245, 246, 255, 263, 301 | web + mobile |
| TC-AUTH-SES-E2E-034-sesi-produk-bersama-web-dan-mobile | Sesi-produk Bersama Web dan Mobile | 104, 137, 144, 271, 272, 273, 300 | web + mobile |
| TC-AUTH-SES-E2E-035-popup-concurrent-dan-subscription-di-mobile | Popup Concurrent Session Limit Reached dan Subscription Not Active di Aplikasi Mobile | 302, 303 | mobile |
| TC-AUTH-SES-E2E-036-subscription-tidak-aktif-memblok-buka-produk | Subscription Tidak Aktif (Archive) Memblok Pembukaan Produk Baru | 113, 116, 117, 118 | web |
| TC-AUTH-SES-E2E-037-subscription-status-lanjutan-memblok-buka-produk | Subscription Status Lanjutan (Purge, Deleted, dan Status Non-Aktif Lain) Memblok Pembukaan Produk Baru | 114, 115, 274, 275, 276, 277, 278 | web |
| TC-AUTH-SES-E2E-038-subscription-renewed-dan-kembali-active | Subscription Kembali Active dan Renewed Mengizinkan Pembukaan Produk Baru | 279, 281 | web |
| TC-AUTH-SES-E2E-039-subscription-memengaruhi-sesi-produk-existing | Perubahan Status Subscription terhadap Sesi-Produk yang Sudah Berjalan | 119, 120, 121, 122, 123, 280 | web |
| TC-AUTH-SES-E2E-040-kuota-concurrent-dan-batas-seat | Kuota Concurrent dan Batas Seat per Produk | 124, 125, 126, 127, 128, 129 | web |
| TC-AUTH-SES-E2E-041-sesi-produk-keluar-eksplisit-dan-daftar-concurrent-user | Sesi-Produk: Keluar Eksplisit, Daftar License Concurrent User, dan Pelepasan Seat | 132, 270 | web |
| TC-AUTH-SES-E2E-042-admin-force-logout-license-concurrent-user | Admin Force-Logout di License > Concurrent User | 133, 134, 136, 138, 322 | web |
| TC-AUTH-SES-E2E-043-manual-logout | Manual Logout di Web: Akhiri Sesi, Sesi-Produk Anak, dan Logout Saat Sesi Expired | 140, 141, 142 | web |
| TC-AUTH-SES-E2E-044-prompt-enable-biometric-dan-enroll | Prompt Enable Biometric: Not now, Tutup Prompt, Cancel OS Prompt, dan Enroll | 145, 146, 324, 259, 313, 315, 314 | mobile |
| TC-AUTH-SES-E2E-045-ketersediaan-biometric-perangkat-dan-ios | Ketersediaan Biometric Perangkat Android (Prompt dan Toggle) serta Enroll Ulang | 147, 148, 149, 337 | mobile |
| TC-AUTH-SES-E2E-046-relogin-biometric-sukses-dan-gagal | Re-login Biometric Android: Screen Sign In, Kegagalan, Fallback Password, dan Sukses | 152, 153, 154, 155, 156, 157, 158, 159, 160 | web + mobile |
| TC-AUTH-SES-E2E-047-biometric-agreement-dan-mfa | Re-login Biometric dengan Agreement dan MFA | 161, 162, 163, 164, 247 | web + mobile |
| TC-AUTH-SES-E2E-048-biometric-token-agreement-dan-privacy-policy | Re-login Biometric: Navigasi Back pada Confirm to Continue, Kegagalan Server Confirm Agreement, dan Privacy Policy Tidak Ter-resolve | 166, 167, 325 | mobile |
| TC-AUTH-SES-E2E-049-biometric-keamanan-penolakan-server | Re-login Biometric: Penolakan Server dan ID Device Tidak Cocok | 170, 171, 176, 257, 258 | web + mobile |
| TC-AUTH-SES-E2E-050-biometric-siklus-token-90-hari-dan-rotasi | Siklus Token Biometric 90 Hari, Perubahan Enrollment OS, dan Rotasi Token | 172, 173, 285, 181, 236, 237 | mobile |
| TC-AUTH-SES-E2E-051-biometric-kredensial-dicabut-dan-disable | Kredensial Biometric Dicabut oleh Disable, Reset Password, Change Email, dan Change Password | 177, 178, 179, 180 | web + mobile |
| TC-AUTH-SES-E2E-052-resilience-biometric-enroll-login-disable | Resilience Biometric: Kegagalan Server saat Enroll, Re-login, dan Disable | 150, 174, 248 | mobile |
| TC-AUTH-SES-E2E-053-duplicate-login-dari-biometric-re-login | Duplicate Login Attempt dari Biometric Re-login: Dialog, Cancel, Confirm, dan Urutan Layar | 168, 169, 296, 328, 295 | web + mobile |
| TC-AUTH-SES-E2E-054-web-tidak-menawarkan-biometric | Aplikasi Web Tidak Menawarkan Biometric | 151 | web |
| TC-AUTH-SES-E2E-055-change-dan-reset-password-meng-invalidate-sesi | Change Password dan Reset Password Meng-invalidate Sesi Aktif Lintas Web dan Mobile | 182, 183, 184, 185, 186, 187, 188, 264 | web + mobile |
| TC-AUTH-SES-E2E-056-pencatatan-session-lifecycle-duplicate-idle-logout | Pencatatan Session Lifecycle: Duplicate Login, Idle Expired Web dan Mobile, Sesi Mobile Digantikan, dan Manual Logout | 189, 191, 192, 193, 197 | web + mobile |
| TC-AUTH-SES-E2E-057-pencatatan-akun-akses-force-logout-dan-password | Pencatatan Sesi karena App Access Dicabut, Admin Force-Logout, Change Password, Deactivate, dan Delete Account | 194, 205, 206, 207, 208, 266 | web + mobile |
| TC-AUTH-SES-E2E-058-pencatatan-produk-concurrent-dan-cascade | Pencatatan Sesi Produk: Buka Produk, Concurrent Limit Reached, dan Sesi Berakhir karena Cascade | 198, 199, 200, 201, 204, 318, 319 | web |
| TC-AUTH-SES-E2E-059-pencatatan-biometric | Pencatatan Biometric Re-login Sukses, Biometric via MFA, dan Continue tanpa Centang Agreement | 209, 210, 267 | web + mobile |
| TC-AUTH-SES-E2E-060-absence-pencatatan-sesi | Absence Pencatatan Sesi: Kondisi yang Tidak Menulis Session Log Entry | 190, 195, 196, 202, 203, 211 | web + mobile |
| TC-AUTH-SES-E2E-061-struktur-dan-format-surface-log | Struktur, Kolom, dan Format Surface Log Sesi | 213, 214, 215, 249, 287, 288, 289 | web |
| TC-AUTH-SES-E2E-062-sinkron-lintas-modul-dan-plan-gating | Sinkron Lintas Modul dan Plan Gating: Status User, Kuota Concurrent, Plan, dan Change Password | 219, 220, 222, 299 | web |
| TC-AUTH-SES-E2E-063-dialog-non-dismissable-escape-dan-backdrop | Dialog Lifecycle Non-dismissable: Escape, Klik Backdrop, dan Tombol Silang | 224, 225, 226, 227, 228, 229, 230 | web |
| TC-AUTH-SES-E2E-064-defense-in-depth-server-side | Defense-in-depth Server-side: Create Session, Force-logout, dan Manipulasi Sesi | 231, 232, 233, 234, 235, 320, 250 | web |
| TC-AUTH-SES-E2E-065-konkurensi-dan-urutan-event | Konkurensi dan Urutan Event: Aksi Paralel, Push Terlewat, dan Reconnect SSE | 238, 239, 240, 241, 242, 243, 265 | web |
| TC-AUTH-SES-E2E-066-absence-duplicate-login-dan-session-expired | Absence Pencatatan Duplicate Login dan Session Expired: Kondisi yang Tidak Menulis Log | 29, 30, 31, 34, 35, 49, 256, 294 | web + mobile |
| TC-AUTH-SES-E2E-067-absence-sesi-produk-dan-concurrent | Absence Pencatatan Sesi-produk dan Concurrent: Reuse, Limit Reached, dan End Product Berulang | 101, 102, 104, 204, 263 | web + mobile |
| TC-AUTH-SES-E2E-068-absence-subscription-tidak-aktif | Absence Pencatatan: Pembukaan Produk Diblok karena Subscription Tidak Aktif Tidak Menulis Log | 113, 114, 115, 274, 275, 276, 277, 278 | web |
| TC-AUTH-SES-E2E-069-absence-penolakan-force-logout-dan-aksi-admin | Absence Pencatatan: Penolakan Server, Force-logout Idempotent, dan Aksi Admin | 136, 142, 233, 234, 239, 250, 320, 322, 327 | web |
| TC-AUTH-SES-E2E-070-absence-biometric | Absence Pencatatan Biometric: Kondisi Re-login, Enroll, dan Disable yang Tidak Menulis Session Log Entry | 154, 160, 162, 170, 173, 175, 176, 177, 212, 257, 258, 325, 328, 335, 336 | web + mobile |
| TC-AUTH-SES-E2E-071-admin-triggered-dialog-focus-trap | Accessibility Focus Trap dan Role Alertdialog Dialog Lifecycle yang Dipicu Aksi Admin | 306, 307, 308 | web |
| TC-AUTH-SES-E2E-072-resilience-log-write-failure | Resilience: Kegagalan Penulisan Log Tidak Membatalkan Log Out | 216 | web |
| TC-AUTH-SES-E2E-073-mobile-biometric-multi-device-change-password | Mobile Biometric Multi-Device: Change Password Mencabut Sesi Lain dan Kredensial Biometric | 223 | web + mobile |
| TC-AUTH-SES-E2E-074-biometric-relogin-ip-rate-limit-429 | Re-login Biometric: Melampaui IP Rate Limit Ditolak dengan Toast Too Many Requests | 175 | mobile |
| TC-AUTH-SES-E2E-075-biometric-agreement-token-ttl-boundary | Re-login Biometric: Umur Token Pra-autentikasi Agreement 10 Menit (Kedaluwarsa dan Batas Eksak) | 165, 286 | mobile |
| TC-AUTH-SES-E2E-076-product-session-sweep-and-time-travel | Sesi-Produk: Tab Ditutup, Kedaluwarsa Sesi Platform, dan Sweep Dinonaktifkan (Time-Travel) | 130, 131 | web |
| TC-AUTH-SES-E2E-077-expired-grace-buka-produk-tanpa-popup | Subscription Expired dan Grace: Pembukaan Produk Baru Membuat Sesi-Produk Tanpa Popup Subscription Not Active | 111, 112 | web |
| TC-AUTH-SES-E2E-078-end-product-admin-console-dan-global-settings | End Product Admin Console dan Global Settings lewat App Switcher Tanpa Seat | 329, 330 | web |
| TC-AUTH-SES-E2E-079-logout-manual-mobile-dan-ganti-akun | Logout Manual di Mobile dengan dan tanpa Biometric serta Ganti Akun di Perangkat yang Sama | 331, 332, 333 | web + mobile |
| TC-AUTH-SES-E2E-080-keamanan-token-biometric-revoke-dan-integrity-token | Keamanan Token Biometric: Pencabutan Kredensial User Lama dan integrityToken Kosong atau Invalid | 334, 335, 336 | mobile |
| TC-AUTH-SES-E2E-081-toggle-biometric-sign-in-resilience | Toggle Biometric Sign-in: Disabled Selama Request, Kegagalan Server, dan Cancel Prompt | 338, 339, 340 | mobile |
| TC-AUTH-SES-E2E-082-kembali-ke-foreground-setelah-sesi-diakhiri-server | Kembali ke Foreground Setelah Sesi Diakhiri Server Saat App di Background | 341, 342, 343 | web + mobile |
| TC-AUTH-SES-E2E-083-cek-sesi-foreground-background-dan-sse-mobile | Cek Sesi Mobile di Foreground dan Background: Hitungan Mundur Lokal, SSE, dan Pembaruan Kedaluwarsa | 344, 347, 348 | web + mobile |
| TC-AUTH-SES-E2E-084-os-kill-app-mobile-dan-sesi-tanpa-cookie | OS Kill App Mobile di Background Diperlakukan sebagai App-kill dan Sesi Mobile Tanpa Cookie | 345, 346, 349 | mobile |

**Total:** 347 dari 349 TC granular tercakup oleh 84 spec; 2 TC Ditahan (TC-AUTH-SES-260 dan 261). TC yang klausa absence-nya ada di spec 066–070 muncul di dua spec; selebihnya satu spec per TC.

---

## Lapisan per TC

| TC | Spec utama | Mode |
|---|---|---|
| TC-AUTH-SES-1 | TC-AUTH-SES-E2E-001-screening-dialog-duplicate-login-dan-logged-out | FE+BE |
| TC-AUTH-SES-2 | TC-AUTH-SES-E2E-001-screening-dialog-duplicate-login-dan-logged-out | FE+BE |
| TC-AUTH-SES-3 | TC-AUTH-SES-E2E-004-screening-session-expired-dan-idle-warning-web | FE+BE |
| TC-AUTH-SES-4 | TC-AUTH-SES-E2E-005-screening-session-expired-dan-idle-warning-mobile | FE+BE |
| TC-AUTH-SES-5 | TC-AUTH-SES-E2E-002-screening-dialog-lifecycle-akun-dan-akses | FE+BE |
| TC-AUTH-SES-6 | TC-AUTH-SES-E2E-002-screening-dialog-lifecycle-akun-dan-akses | FE+BE |
| TC-AUTH-SES-7 | TC-AUTH-SES-E2E-002-screening-dialog-lifecycle-akun-dan-akses | FE+BE |
| TC-AUTH-SES-8 | TC-AUTH-SES-E2E-002-screening-dialog-lifecycle-akun-dan-akses | FE+BE |
| TC-AUTH-SES-9 | TC-AUTH-SES-E2E-002-screening-dialog-lifecycle-akun-dan-akses | FE+BE |
| TC-AUTH-SES-10 | TC-AUTH-SES-E2E-003-screening-popup-concurrent-dan-subscription | FE+BE |
| TC-AUTH-SES-11 | TC-AUTH-SES-E2E-003-screening-popup-concurrent-dan-subscription | FE+BE |
| TC-AUTH-SES-12 | TC-AUTH-SES-E2E-004-screening-session-expired-dan-idle-warning-web | FE+BE |
| TC-AUTH-SES-13 | TC-AUTH-SES-E2E-005-screening-session-expired-dan-idle-warning-mobile | FE+BE |
| TC-AUTH-SES-14 | TC-AUTH-SES-E2E-006-screening-biometric-mobile | FE+BE |
| TC-AUTH-SES-15 | TC-AUTH-SES-E2E-006-screening-biometric-mobile | FE+BE |
| TC-AUTH-SES-16 | TC-AUTH-SES-E2E-006-screening-biometric-mobile | FE+BE |
| TC-AUTH-SES-17 | TC-AUTH-SES-E2E-007-dialog-lifecycle-lintas-role-dan-entitas | FE+BE |
| TC-AUTH-SES-18 | TC-AUTH-SES-E2E-007-dialog-lifecycle-lintas-role-dan-entitas | FE+BE |
| TC-AUTH-SES-19 | TC-AUTH-SES-E2E-007-dialog-lifecycle-lintas-role-dan-entitas | FE+BE |
| TC-AUTH-SES-20 | TC-AUTH-SES-E2E-009-limit-login-web-dan-duplicate-login | FE+BE |
| TC-AUTH-SES-21 | TC-AUTH-SES-E2E-009-limit-login-web-dan-duplicate-login | FE+BE |
| TC-AUTH-SES-22 | TC-AUTH-SES-E2E-010-limit-login-mobile-dan-duplicate-login | FE+BE |
| TC-AUTH-SES-23 | TC-AUTH-SES-E2E-010-limit-login-mobile-dan-duplicate-login | FE+BE |
| TC-AUTH-SES-24 | TC-AUTH-SES-E2E-009-limit-login-web-dan-duplicate-login | FE+BE |
| TC-AUTH-SES-25 | TC-AUTH-SES-E2E-009-limit-login-web-dan-duplicate-login | FE+BE |
| TC-AUTH-SES-26 | TC-AUTH-SES-E2E-011-confirm-cancel-duplicate-login-web | FE+BE |
| TC-AUTH-SES-27 | TC-AUTH-SES-E2E-011-confirm-cancel-duplicate-login-web | FE+BE |
| TC-AUTH-SES-28 | TC-AUTH-SES-E2E-012-dialog-lifecycle-multi-tab | FE+BE |
| TC-AUTH-SES-29 | TC-AUTH-SES-E2E-011-confirm-cancel-duplicate-login-web | FE+BE |
| TC-AUTH-SES-30 | TC-AUTH-SES-E2E-011-confirm-cancel-duplicate-login-web | FE+BE |
| TC-AUTH-SES-31 | TC-AUTH-SES-E2E-011-confirm-cancel-duplicate-login-web | FE+BE |
| TC-AUTH-SES-32 | TC-AUTH-SES-E2E-011-confirm-cancel-duplicate-login-web | FE+BE |
| TC-AUTH-SES-33 | TC-AUTH-SES-E2E-014-resilience-kegagalan-server-sesi-web | FE+BE |
| TC-AUTH-SES-34 | TC-AUTH-SES-E2E-013-token-pra-auth-dan-sesi-lama-expired-saat-confirm | FE+BE |
| TC-AUTH-SES-35 | TC-AUTH-SES-E2E-013-token-pra-auth-dan-sesi-lama-expired-saat-confirm | FE+BE |
| TC-AUTH-SES-36 | TC-AUTH-SES-E2E-013-token-pra-auth-dan-sesi-lama-expired-saat-confirm | FE+BE |
| TC-AUTH-SES-37 | TC-AUTH-SES-E2E-001-screening-dialog-duplicate-login-dan-logged-out | FE+BE |
| TC-AUTH-SES-38 | TC-AUTH-SES-E2E-001-screening-dialog-duplicate-login-dan-logged-out | FE+BE |
| TC-AUTH-SES-39 | TC-AUTH-SES-E2E-015-heartbeat-dan-sinyal-aktivitas-web | FE+BE |
| TC-AUTH-SES-40 | TC-AUTH-SES-E2E-015-heartbeat-dan-sinyal-aktivitas-web | FE+BE |
| TC-AUTH-SES-41 | TC-AUTH-SES-E2E-015-heartbeat-dan-sinyal-aktivitas-web | FE+BE |
| TC-AUTH-SES-42 | TC-AUTH-SES-E2E-015-heartbeat-dan-sinyal-aktivitas-web | FE+BE |
| TC-AUTH-SES-43 | TC-AUTH-SES-E2E-015-heartbeat-dan-sinyal-aktivitas-web | FE+BE |
| TC-AUTH-SES-44 | TC-AUTH-SES-E2E-016-idle-timeout-dan-toast-warning-web | FE+BE |
| TC-AUTH-SES-45 | TC-AUTH-SES-E2E-016-idle-timeout-dan-toast-warning-web | FE+BE |
| TC-AUTH-SES-46 | TC-AUTH-SES-E2E-016-idle-timeout-dan-toast-warning-web | FE+BE |
| TC-AUTH-SES-47 | TC-AUTH-SES-E2E-016-idle-timeout-dan-toast-warning-web | FE+BE |
| TC-AUTH-SES-48 | TC-AUTH-SES-E2E-016-idle-timeout-dan-toast-warning-web | FE+BE |
| TC-AUTH-SES-49 | TC-AUTH-SES-E2E-019-session-expired-multi-tab | FE+BE |
| TC-AUTH-SES-50 | TC-AUTH-SES-E2E-018-refresh-pada-dialog-session-expired | FE+BE |
| TC-AUTH-SES-51 | TC-AUTH-SES-E2E-014-resilience-kegagalan-server-sesi-web | FE+BE |
| TC-AUTH-SES-52 | TC-AUTH-SES-E2E-014-resilience-kegagalan-server-sesi-web | FE+BE |
| TC-AUTH-SES-53 | TC-AUTH-SES-E2E-019-session-expired-multi-tab | FE+BE |
| TC-AUTH-SES-54 | TC-AUTH-SES-E2E-019-session-expired-multi-tab | FE+BE |
| TC-AUTH-SES-55 | TC-AUTH-SES-E2E-019-session-expired-multi-tab | FE+BE |
| TC-AUTH-SES-56 | TC-AUTH-SES-E2E-018-refresh-pada-dialog-session-expired | FE+BE |
| TC-AUTH-SES-57 | TC-AUTH-SES-E2E-018-refresh-pada-dialog-session-expired | FE+BE |
| TC-AUTH-SES-58 | TC-AUTH-SES-E2E-018-refresh-pada-dialog-session-expired | FE+BE |
| TC-AUTH-SES-59 | TC-AUTH-SES-E2E-017-batas-idle-konfigurasi | FE+BE |
| TC-AUTH-SES-60 | TC-AUTH-SES-E2E-017-batas-idle-konfigurasi | FE+BE |
| TC-AUTH-SES-61 | TC-AUTH-SES-E2E-014-resilience-kegagalan-server-sesi-web | FE+BE |
| TC-AUTH-SES-62 | TC-AUTH-SES-E2E-018-refresh-pada-dialog-session-expired | FE+BE |
| TC-AUTH-SES-63 | TC-AUTH-SES-E2E-021-idle-dan-lifecycle-sesi-mobile | FE+BE |
| TC-AUTH-SES-64 | TC-AUTH-SES-E2E-021-idle-dan-lifecycle-sesi-mobile | FE+BE |
| TC-AUTH-SES-65 | TC-AUTH-SES-E2E-021-idle-dan-lifecycle-sesi-mobile | FE+BE |
| TC-AUTH-SES-66 | TC-AUTH-SES-E2E-021-idle-dan-lifecycle-sesi-mobile | FE+BE |
| TC-AUTH-SES-67 | TC-AUTH-SES-E2E-022-app-dihapus-dari-background-dan-push | FE+BE |
| TC-AUTH-SES-68 | TC-AUTH-SES-E2E-022-app-dihapus-dari-background-dan-push | FE+BE |
| TC-AUTH-SES-69 | TC-AUTH-SES-E2E-022-app-dihapus-dari-background-dan-push | FE+BE |
| TC-AUTH-SES-70 | TC-AUTH-SES-E2E-022-app-dihapus-dari-background-dan-push | FE+BE |
| TC-AUTH-SES-71 | TC-AUTH-SES-E2E-021-idle-dan-lifecycle-sesi-mobile | FE+BE |
| TC-AUTH-SES-72 | TC-AUTH-SES-E2E-024-app-access-revoke-dan-delete-client | FE+BE |
| TC-AUTH-SES-73 | TC-AUTH-SES-E2E-024-app-access-revoke-dan-delete-client | FE+BE |
| TC-AUTH-SES-74 | TC-AUTH-SES-E2E-024-app-access-revoke-dan-delete-client | FE+BE |
| TC-AUTH-SES-75 | TC-AUTH-SES-E2E-024-app-access-revoke-dan-delete-client | FE+BE |
| TC-AUTH-SES-76 | TC-AUTH-SES-E2E-024-app-access-revoke-dan-delete-client | FE+BE |
| TC-AUTH-SES-77 | TC-AUTH-SES-E2E-025-client-suspended-dialog-access-restricted | FE+BE |
| TC-AUTH-SES-78 | TC-AUTH-SES-E2E-025-client-suspended-dialog-access-restricted | FE+BE |
| TC-AUTH-SES-79 | TC-AUTH-SES-E2E-012-dialog-lifecycle-multi-tab | FE+BE |
| TC-AUTH-SES-80 | TC-AUTH-SES-E2E-026-client-suspended-kasus-tepi | FE+BE |
| TC-AUTH-SES-81 | TC-AUTH-SES-E2E-026-client-suspended-kasus-tepi | FE+BE |
| TC-AUTH-SES-82 | TC-AUTH-SES-E2E-026-client-suspended-kasus-tepi | FE+BE |
| TC-AUTH-SES-83 | TC-AUTH-SES-E2E-026-client-suspended-kasus-tepi | FE+BE |
| TC-AUTH-SES-84 | TC-AUTH-SES-E2E-026-client-suspended-kasus-tepi | FE+BE |
| TC-AUTH-SES-85 | TC-AUTH-SES-E2E-025-client-suspended-dialog-access-restricted | FE+BE |
| TC-AUTH-SES-86 | TC-AUTH-SES-E2E-026-client-suspended-kasus-tepi | FE+BE |
| TC-AUTH-SES-87 | TC-AUTH-SES-E2E-026-client-suspended-kasus-tepi | FE+BE |
| TC-AUTH-SES-88 | TC-AUTH-SES-E2E-028-delete-dan-deactivate-akun-web | FE+BE |
| TC-AUTH-SES-89 | TC-AUTH-SES-E2E-028-delete-dan-deactivate-akun-web | FE+BE |
| TC-AUTH-SES-90 | TC-AUTH-SES-E2E-028-delete-dan-deactivate-akun-web | FE+BE |
| TC-AUTH-SES-91 | TC-AUTH-SES-E2E-028-delete-dan-deactivate-akun-web | FE+BE |
| TC-AUTH-SES-92 | TC-AUTH-SES-E2E-028-delete-dan-deactivate-akun-web | FE+BE |
| TC-AUTH-SES-93 | TC-AUTH-SES-E2E-029-invalidasi-semua-sesi-saat-akun-dihapus-atau-dinonaktifkan | FE+BE |
| TC-AUTH-SES-94 | TC-AUTH-SES-E2E-012-dialog-lifecycle-multi-tab | FE+BE |
| TC-AUTH-SES-95 | TC-AUTH-SES-E2E-031-buka-produk-seat-tersedia-dan-reuse-sesi-produk | FE+BE |
| TC-AUTH-SES-96 | TC-AUTH-SES-E2E-030-popup-concurrent-limit-saat-seat-penuh | FE+BE |
| TC-AUTH-SES-97 | TC-AUTH-SES-E2E-030-popup-concurrent-limit-saat-seat-penuh | FE+BE |
| TC-AUTH-SES-98 | TC-AUTH-SES-E2E-030-popup-concurrent-limit-saat-seat-penuh | FE+BE |
| TC-AUTH-SES-99 | TC-AUTH-SES-E2E-030-popup-concurrent-limit-saat-seat-penuh | FE+BE |
| TC-AUTH-SES-100 | TC-AUTH-SES-E2E-030-popup-concurrent-limit-saat-seat-penuh | FE+BE |
| TC-AUTH-SES-101 | TC-AUTH-SES-E2E-031-buka-produk-seat-tersedia-dan-reuse-sesi-produk | FE+BE |
| TC-AUTH-SES-102 | TC-AUTH-SES-E2E-031-buka-produk-seat-tersedia-dan-reuse-sesi-produk | FE+BE |
| TC-AUTH-SES-103 | TC-AUTH-SES-E2E-031-buka-produk-seat-tersedia-dan-reuse-sesi-produk | FE+BE |
| TC-AUTH-SES-104 | TC-AUTH-SES-E2E-034-sesi-produk-bersama-web-dan-mobile | FE+BE |
| TC-AUTH-SES-105 | TC-AUTH-SES-E2E-031-buka-produk-seat-tersedia-dan-reuse-sesi-produk | FE+BE |
| TC-AUTH-SES-106 | TC-AUTH-SES-E2E-032-admin-console-dan-global-settings-tanpa-concurrent | FE+BE |
| TC-AUTH-SES-107 | TC-AUTH-SES-E2E-032-admin-console-dan-global-settings-tanpa-concurrent | FE+BE |
| TC-AUTH-SES-108 | TC-AUTH-SES-E2E-032-admin-console-dan-global-settings-tanpa-concurrent | FE+BE |
| TC-AUTH-SES-109 | TC-AUTH-SES-E2E-032-admin-console-dan-global-settings-tanpa-concurrent | FE+BE |
| TC-AUTH-SES-110 | TC-AUTH-SES-E2E-014-resilience-kegagalan-server-sesi-web | FE+BE |
| TC-AUTH-SES-111 | TC-AUTH-SES-E2E-077-expired-grace-buka-produk-tanpa-popup | FE+BE |
| TC-AUTH-SES-112 | TC-AUTH-SES-E2E-077-expired-grace-buka-produk-tanpa-popup | FE+BE |
| TC-AUTH-SES-113 | TC-AUTH-SES-E2E-036-subscription-tidak-aktif-memblok-buka-produk | FE+BE |
| TC-AUTH-SES-114 | TC-AUTH-SES-E2E-037-subscription-status-lanjutan-memblok-buka-produk | FE+BE |
| TC-AUTH-SES-115 | TC-AUTH-SES-E2E-037-subscription-status-lanjutan-memblok-buka-produk | FE+BE |
| TC-AUTH-SES-116 | TC-AUTH-SES-E2E-036-subscription-tidak-aktif-memblok-buka-produk | FE+BE |
| TC-AUTH-SES-117 | TC-AUTH-SES-E2E-036-subscription-tidak-aktif-memblok-buka-produk | FE+BE |
| TC-AUTH-SES-118 | TC-AUTH-SES-E2E-036-subscription-tidak-aktif-memblok-buka-produk | FE+BE |
| TC-AUTH-SES-119 | TC-AUTH-SES-E2E-039-subscription-memengaruhi-sesi-produk-existing | FE+BE |
| TC-AUTH-SES-120 | TC-AUTH-SES-E2E-039-subscription-memengaruhi-sesi-produk-existing | FE+BE |
| TC-AUTH-SES-121 | TC-AUTH-SES-E2E-039-subscription-memengaruhi-sesi-produk-existing | FE+BE |
| TC-AUTH-SES-122 | TC-AUTH-SES-E2E-039-subscription-memengaruhi-sesi-produk-existing | FE+BE |
| TC-AUTH-SES-123 | TC-AUTH-SES-E2E-039-subscription-memengaruhi-sesi-produk-existing | FE+BE |
| TC-AUTH-SES-124 | TC-AUTH-SES-E2E-040-kuota-concurrent-dan-batas-seat | FE+BE |
| TC-AUTH-SES-125 | TC-AUTH-SES-E2E-040-kuota-concurrent-dan-batas-seat | FE+BE |
| TC-AUTH-SES-126 | TC-AUTH-SES-E2E-040-kuota-concurrent-dan-batas-seat | FE+BE |
| TC-AUTH-SES-127 | TC-AUTH-SES-E2E-040-kuota-concurrent-dan-batas-seat | FE+BE |
| TC-AUTH-SES-128 | TC-AUTH-SES-E2E-040-kuota-concurrent-dan-batas-seat | FE+BE |
| TC-AUTH-SES-129 | TC-AUTH-SES-E2E-040-kuota-concurrent-dan-batas-seat | FE+BE |
| TC-AUTH-SES-130 | TC-AUTH-SES-E2E-076-product-session-sweep-and-time-travel | FE+BE |
| TC-AUTH-SES-131 | TC-AUTH-SES-E2E-076-product-session-sweep-and-time-travel | FE+BE |
| TC-AUTH-SES-132 | TC-AUTH-SES-E2E-041-sesi-produk-keluar-eksplisit-dan-daftar-concurrent-user | FE+BE |
| TC-AUTH-SES-133 | TC-AUTH-SES-E2E-042-admin-force-logout-license-concurrent-user | FE+BE |
| TC-AUTH-SES-134 | TC-AUTH-SES-E2E-042-admin-force-logout-license-concurrent-user | FE+BE |
| TC-AUTH-SES-135 | TC-AUTH-SES-E2E-012-dialog-lifecycle-multi-tab | FE+BE |
| TC-AUTH-SES-136 | TC-AUTH-SES-E2E-042-admin-force-logout-license-concurrent-user | FE+BE |
| TC-AUTH-SES-137 | TC-AUTH-SES-E2E-034-sesi-produk-bersama-web-dan-mobile | FE+BE |
| TC-AUTH-SES-138 | TC-AUTH-SES-E2E-042-admin-force-logout-license-concurrent-user | FE+BE |
| TC-AUTH-SES-139 | TC-AUTH-SES-E2E-014-resilience-kegagalan-server-sesi-web | FE+BE |
| TC-AUTH-SES-140 | TC-AUTH-SES-E2E-043-manual-logout | FE+BE |
| TC-AUTH-SES-141 | TC-AUTH-SES-E2E-043-manual-logout | FE+BE |
| TC-AUTH-SES-142 | TC-AUTH-SES-E2E-043-manual-logout | FE+BE |
| TC-AUTH-SES-143 | TC-AUTH-SES-E2E-014-resilience-kegagalan-server-sesi-web | FE+BE |
| TC-AUTH-SES-144 | TC-AUTH-SES-E2E-034-sesi-produk-bersama-web-dan-mobile | FE+BE |
| TC-AUTH-SES-145 | TC-AUTH-SES-E2E-044-prompt-enable-biometric-dan-enroll | FE+BE |
| TC-AUTH-SES-146 | TC-AUTH-SES-E2E-044-prompt-enable-biometric-dan-enroll | FE+BE |
| TC-AUTH-SES-147 | TC-AUTH-SES-E2E-045-ketersediaan-biometric-perangkat-dan-ios | FE+BE |
| TC-AUTH-SES-148 | TC-AUTH-SES-E2E-045-ketersediaan-biometric-perangkat-dan-ios | FE+BE |
| TC-AUTH-SES-149 | TC-AUTH-SES-E2E-045-ketersediaan-biometric-perangkat-dan-ios | FE+BE |
| TC-AUTH-SES-150 | TC-AUTH-SES-E2E-052-resilience-biometric-enroll-login-disable | FE+BE |
| TC-AUTH-SES-151 | TC-AUTH-SES-E2E-054-web-tidak-menawarkan-biometric | FE+BE |
| TC-AUTH-SES-152 | TC-AUTH-SES-E2E-046-relogin-biometric-sukses-dan-gagal | FE+BE |
| TC-AUTH-SES-153 | TC-AUTH-SES-E2E-046-relogin-biometric-sukses-dan-gagal | FE+BE |
| TC-AUTH-SES-154 | TC-AUTH-SES-E2E-046-relogin-biometric-sukses-dan-gagal | FE+BE |
| TC-AUTH-SES-155 | TC-AUTH-SES-E2E-046-relogin-biometric-sukses-dan-gagal | FE+BE |
| TC-AUTH-SES-156 | TC-AUTH-SES-E2E-046-relogin-biometric-sukses-dan-gagal | FE+BE |
| TC-AUTH-SES-157 | TC-AUTH-SES-E2E-046-relogin-biometric-sukses-dan-gagal | FE+BE |
| TC-AUTH-SES-158 | TC-AUTH-SES-E2E-046-relogin-biometric-sukses-dan-gagal | FE+BE |
| TC-AUTH-SES-159 | TC-AUTH-SES-E2E-046-relogin-biometric-sukses-dan-gagal | FE+BE |
| TC-AUTH-SES-160 | TC-AUTH-SES-E2E-046-relogin-biometric-sukses-dan-gagal | FE+BE |
| TC-AUTH-SES-161 | TC-AUTH-SES-E2E-047-biometric-agreement-dan-mfa | FE+BE |
| TC-AUTH-SES-162 | TC-AUTH-SES-E2E-047-biometric-agreement-dan-mfa | FE+BE |
| TC-AUTH-SES-163 | TC-AUTH-SES-E2E-047-biometric-agreement-dan-mfa | FE+BE |
| TC-AUTH-SES-164 | TC-AUTH-SES-E2E-047-biometric-agreement-dan-mfa | FE+BE |
| TC-AUTH-SES-165 | TC-AUTH-SES-E2E-075-biometric-agreement-token-ttl-boundary | FE+BE |
| TC-AUTH-SES-166 | TC-AUTH-SES-E2E-048-biometric-token-agreement-dan-privacy-policy | FE+BE |
| TC-AUTH-SES-167 | TC-AUTH-SES-E2E-048-biometric-token-agreement-dan-privacy-policy | FE+BE |
| TC-AUTH-SES-168 | TC-AUTH-SES-E2E-053-duplicate-login-dari-biometric-re-login | FE+BE |
| TC-AUTH-SES-169 | TC-AUTH-SES-E2E-053-duplicate-login-dari-biometric-re-login | FE+BE |
| TC-AUTH-SES-170 | TC-AUTH-SES-E2E-049-biometric-keamanan-penolakan-server | FE+BE |
| TC-AUTH-SES-171 | TC-AUTH-SES-E2E-049-biometric-keamanan-penolakan-server | FE+BE |
| TC-AUTH-SES-172 | TC-AUTH-SES-E2E-050-biometric-siklus-token-90-hari-dan-rotasi | FE+BE |
| TC-AUTH-SES-173 | TC-AUTH-SES-E2E-050-biometric-siklus-token-90-hari-dan-rotasi | FE+BE |
| TC-AUTH-SES-174 | TC-AUTH-SES-E2E-052-resilience-biometric-enroll-login-disable | FE+BE |
| TC-AUTH-SES-175 | TC-AUTH-SES-E2E-074-biometric-relogin-ip-rate-limit-429 | FE+BE |
| TC-AUTH-SES-176 | TC-AUTH-SES-E2E-049-biometric-keamanan-penolakan-server | FE+BE |
| TC-AUTH-SES-177 | TC-AUTH-SES-E2E-051-biometric-kredensial-dicabut-dan-disable | FE+BE |
| TC-AUTH-SES-178 | TC-AUTH-SES-E2E-051-biometric-kredensial-dicabut-dan-disable | FE+BE |
| TC-AUTH-SES-179 | TC-AUTH-SES-E2E-051-biometric-kredensial-dicabut-dan-disable | FE+BE |
| TC-AUTH-SES-180 | TC-AUTH-SES-E2E-051-biometric-kredensial-dicabut-dan-disable | FE+BE |
| TC-AUTH-SES-181 | TC-AUTH-SES-E2E-050-biometric-siklus-token-90-hari-dan-rotasi | FE+BE |
| TC-AUTH-SES-182 | TC-AUTH-SES-E2E-055-change-dan-reset-password-meng-invalidate-sesi | FE+BE |
| TC-AUTH-SES-183 | TC-AUTH-SES-E2E-055-change-dan-reset-password-meng-invalidate-sesi | FE+BE |
| TC-AUTH-SES-184 | TC-AUTH-SES-E2E-055-change-dan-reset-password-meng-invalidate-sesi | FE+BE |
| TC-AUTH-SES-185 | TC-AUTH-SES-E2E-055-change-dan-reset-password-meng-invalidate-sesi | FE+BE |
| TC-AUTH-SES-186 | TC-AUTH-SES-E2E-055-change-dan-reset-password-meng-invalidate-sesi | FE+BE |
| TC-AUTH-SES-187 | TC-AUTH-SES-E2E-055-change-dan-reset-password-meng-invalidate-sesi | FE+BE |
| TC-AUTH-SES-188 | TC-AUTH-SES-E2E-055-change-dan-reset-password-meng-invalidate-sesi | FE+BE |
| TC-AUTH-SES-189 | TC-AUTH-SES-E2E-056-pencatatan-session-lifecycle-duplicate-idle-logout | FE+BE |
| TC-AUTH-SES-190 | TC-AUTH-SES-E2E-060-absence-pencatatan-sesi | FE+BE |
| TC-AUTH-SES-191 | TC-AUTH-SES-E2E-056-pencatatan-session-lifecycle-duplicate-idle-logout | FE+BE |
| TC-AUTH-SES-192 | TC-AUTH-SES-E2E-056-pencatatan-session-lifecycle-duplicate-idle-logout | FE+BE |
| TC-AUTH-SES-193 | TC-AUTH-SES-E2E-056-pencatatan-session-lifecycle-duplicate-idle-logout | FE+BE |
| TC-AUTH-SES-194 | TC-AUTH-SES-E2E-057-pencatatan-akun-akses-force-logout-dan-password | FE+BE |
| TC-AUTH-SES-195 | TC-AUTH-SES-E2E-060-absence-pencatatan-sesi | FE+BE |
| TC-AUTH-SES-196 | TC-AUTH-SES-E2E-060-absence-pencatatan-sesi | FE+BE |
| TC-AUTH-SES-197 | TC-AUTH-SES-E2E-056-pencatatan-session-lifecycle-duplicate-idle-logout | FE+BE |
| TC-AUTH-SES-198 | TC-AUTH-SES-E2E-058-pencatatan-produk-concurrent-dan-cascade | FE+BE |
| TC-AUTH-SES-199 | TC-AUTH-SES-E2E-058-pencatatan-produk-concurrent-dan-cascade | FE+BE |
| TC-AUTH-SES-200 | TC-AUTH-SES-E2E-058-pencatatan-produk-concurrent-dan-cascade | FE+BE |
| TC-AUTH-SES-201 | TC-AUTH-SES-E2E-058-pencatatan-produk-concurrent-dan-cascade | FE+BE |
| TC-AUTH-SES-202 | TC-AUTH-SES-E2E-060-absence-pencatatan-sesi | FE+BE |
| TC-AUTH-SES-203 | TC-AUTH-SES-E2E-060-absence-pencatatan-sesi | FE+BE |
| TC-AUTH-SES-204 | TC-AUTH-SES-E2E-058-pencatatan-produk-concurrent-dan-cascade | FE+BE |
| TC-AUTH-SES-205 | TC-AUTH-SES-E2E-057-pencatatan-akun-akses-force-logout-dan-password | FE+BE |
| TC-AUTH-SES-206 | TC-AUTH-SES-E2E-057-pencatatan-akun-akses-force-logout-dan-password | FE+BE |
| TC-AUTH-SES-207 | TC-AUTH-SES-E2E-057-pencatatan-akun-akses-force-logout-dan-password | FE+BE |
| TC-AUTH-SES-208 | TC-AUTH-SES-E2E-057-pencatatan-akun-akses-force-logout-dan-password | FE+BE |
| TC-AUTH-SES-209 | TC-AUTH-SES-E2E-059-pencatatan-biometric | FE+BE |
| TC-AUTH-SES-210 | TC-AUTH-SES-E2E-059-pencatatan-biometric | FE+BE |
| TC-AUTH-SES-211 | TC-AUTH-SES-E2E-060-absence-pencatatan-sesi | FE+BE |
| TC-AUTH-SES-212 | TC-AUTH-SES-E2E-070-absence-biometric | FE+BE |
| TC-AUTH-SES-213 | TC-AUTH-SES-E2E-061-struktur-dan-format-surface-log | FE+BE |
| TC-AUTH-SES-214 | TC-AUTH-SES-E2E-061-struktur-dan-format-surface-log | FE+BE |
| TC-AUTH-SES-215 | TC-AUTH-SES-E2E-061-struktur-dan-format-surface-log | FE+BE |
| TC-AUTH-SES-216 | TC-AUTH-SES-E2E-072-resilience-log-write-failure | FE+BE |
| TC-AUTH-SES-217 | TC-AUTH-SES-E2E-017-batas-idle-konfigurasi | FE+BE |
| TC-AUTH-SES-218 | TC-AUTH-SES-E2E-017-batas-idle-konfigurasi | FE+BE |
| TC-AUTH-SES-219 | TC-AUTH-SES-E2E-062-sinkron-lintas-modul-dan-plan-gating | FE+BE |
| TC-AUTH-SES-220 | TC-AUTH-SES-E2E-062-sinkron-lintas-modul-dan-plan-gating | FE+BE |
| TC-AUTH-SES-221 | TC-AUTH-SES-E2E-032-admin-console-dan-global-settings-tanpa-concurrent | FE+BE |
| TC-AUTH-SES-222 | TC-AUTH-SES-E2E-062-sinkron-lintas-modul-dan-plan-gating | FE+BE |
| TC-AUTH-SES-223 | TC-AUTH-SES-E2E-073-mobile-biometric-multi-device-change-password | FE+BE |
| TC-AUTH-SES-224 | TC-AUTH-SES-E2E-063-dialog-non-dismissable-escape-dan-backdrop | FE+BE |
| TC-AUTH-SES-225 | TC-AUTH-SES-E2E-063-dialog-non-dismissable-escape-dan-backdrop | FE+BE |
| TC-AUTH-SES-226 | TC-AUTH-SES-E2E-063-dialog-non-dismissable-escape-dan-backdrop | FE+BE |
| TC-AUTH-SES-227 | TC-AUTH-SES-E2E-063-dialog-non-dismissable-escape-dan-backdrop | FE+BE |
| TC-AUTH-SES-228 | TC-AUTH-SES-E2E-063-dialog-non-dismissable-escape-dan-backdrop | FE+BE |
| TC-AUTH-SES-229 | TC-AUTH-SES-E2E-063-dialog-non-dismissable-escape-dan-backdrop | FE+BE |
| TC-AUTH-SES-230 | TC-AUTH-SES-E2E-063-dialog-non-dismissable-escape-dan-backdrop | FE+BE |
| TC-AUTH-SES-231 | TC-AUTH-SES-E2E-064-defense-in-depth-server-side | FE+BE |
| TC-AUTH-SES-232 | TC-AUTH-SES-E2E-064-defense-in-depth-server-side | FE+BE |
| TC-AUTH-SES-233 | TC-AUTH-SES-E2E-064-defense-in-depth-server-side | FE+BE |
| TC-AUTH-SES-234 | TC-AUTH-SES-E2E-064-defense-in-depth-server-side | FE+BE |
| TC-AUTH-SES-235 | TC-AUTH-SES-E2E-064-defense-in-depth-server-side | FE+BE |
| TC-AUTH-SES-236 | TC-AUTH-SES-E2E-050-biometric-siklus-token-90-hari-dan-rotasi | FE+BE |
| TC-AUTH-SES-237 | TC-AUTH-SES-E2E-050-biometric-siklus-token-90-hari-dan-rotasi | FE+BE |
| TC-AUTH-SES-238 | TC-AUTH-SES-E2E-065-konkurensi-dan-urutan-event | FE+BE |
| TC-AUTH-SES-239 | TC-AUTH-SES-E2E-065-konkurensi-dan-urutan-event | FE+BE |
| TC-AUTH-SES-240 | TC-AUTH-SES-E2E-065-konkurensi-dan-urutan-event | FE+BE |
| TC-AUTH-SES-241 | TC-AUTH-SES-E2E-065-konkurensi-dan-urutan-event | FE+BE |
| TC-AUTH-SES-242 | TC-AUTH-SES-E2E-065-konkurensi-dan-urutan-event | FE+BE |
| TC-AUTH-SES-243 | TC-AUTH-SES-E2E-065-konkurensi-dan-urutan-event | FE+BE |
| TC-AUTH-SES-244 | TC-AUTH-SES-E2E-015-heartbeat-dan-sinyal-aktivitas-web | FE+BE |
| TC-AUTH-SES-245 | TC-AUTH-SES-E2E-033-cascade-sesi-produk-dan-pelepasan-seat | FE+BE |
| TC-AUTH-SES-246 | TC-AUTH-SES-E2E-033-cascade-sesi-produk-dan-pelepasan-seat | FE+BE |
| TC-AUTH-SES-247 | TC-AUTH-SES-E2E-047-biometric-agreement-dan-mfa | FE+BE |
| TC-AUTH-SES-248 | TC-AUTH-SES-E2E-052-resilience-biometric-enroll-login-disable | FE+BE |
| TC-AUTH-SES-249 | TC-AUTH-SES-E2E-061-struktur-dan-format-surface-log | FE+BE |
| TC-AUTH-SES-250 | TC-AUTH-SES-E2E-064-defense-in-depth-server-side | FE+BE |
| TC-AUTH-SES-251 | TC-AUTH-SES-E2E-020-accessibility-focus-trap-dialog-lifecycle | FE+BE |
| TC-AUTH-SES-252 | TC-AUTH-SES-E2E-020-accessibility-focus-trap-dialog-lifecycle | FE+BE |
| TC-AUTH-SES-253 | TC-AUTH-SES-E2E-021-idle-dan-lifecycle-sesi-mobile | FE+BE |
| TC-AUTH-SES-254 | TC-AUTH-SES-E2E-023-sesi-yatim-app-kill-dan-id-device | FE+BE |
| TC-AUTH-SES-255 | TC-AUTH-SES-E2E-033-cascade-sesi-produk-dan-pelepasan-seat | FE+BE |
| TC-AUTH-SES-256 | TC-AUTH-SES-E2E-013-token-pra-auth-dan-sesi-lama-expired-saat-confirm | FE+BE |
| TC-AUTH-SES-257 | TC-AUTH-SES-E2E-049-biometric-keamanan-penolakan-server | FE+BE |
| TC-AUTH-SES-258 | TC-AUTH-SES-E2E-049-biometric-keamanan-penolakan-server | FE+BE |
| TC-AUTH-SES-259 | TC-AUTH-SES-E2E-044-prompt-enable-biometric-dan-enroll | FE+BE |
| TC-AUTH-SES-262 | TC-AUTH-SES-E2E-012-dialog-lifecycle-multi-tab | FE+BE |
| TC-AUTH-SES-263 | TC-AUTH-SES-E2E-033-cascade-sesi-produk-dan-pelepasan-seat | FE+BE |
| TC-AUTH-SES-264 | TC-AUTH-SES-E2E-055-change-dan-reset-password-meng-invalidate-sesi | FE+BE |
| TC-AUTH-SES-265 | TC-AUTH-SES-E2E-065-konkurensi-dan-urutan-event | FE+BE |
| TC-AUTH-SES-266 | TC-AUTH-SES-E2E-057-pencatatan-akun-akses-force-logout-dan-password | FE+BE |
| TC-AUTH-SES-267 | TC-AUTH-SES-E2E-059-pencatatan-biometric | FE+BE |
| TC-AUTH-SES-268 | TC-AUTH-SES-E2E-018-refresh-pada-dialog-session-expired | FE+BE |
| TC-AUTH-SES-269 | TC-AUTH-SES-E2E-026-client-suspended-kasus-tepi | FE+BE |
| TC-AUTH-SES-270 | TC-AUTH-SES-E2E-041-sesi-produk-keluar-eksplisit-dan-daftar-concurrent-user | FE+BE |
| TC-AUTH-SES-271 | TC-AUTH-SES-E2E-034-sesi-produk-bersama-web-dan-mobile | FE+BE |
| TC-AUTH-SES-272 | TC-AUTH-SES-E2E-034-sesi-produk-bersama-web-dan-mobile | FE+BE |
| TC-AUTH-SES-273 | TC-AUTH-SES-E2E-034-sesi-produk-bersama-web-dan-mobile | FE+BE |
| TC-AUTH-SES-274 | TC-AUTH-SES-E2E-037-subscription-status-lanjutan-memblok-buka-produk | FE+BE |
| TC-AUTH-SES-275 | TC-AUTH-SES-E2E-037-subscription-status-lanjutan-memblok-buka-produk | FE+BE |
| TC-AUTH-SES-276 | TC-AUTH-SES-E2E-037-subscription-status-lanjutan-memblok-buka-produk | FE+BE |
| TC-AUTH-SES-277 | TC-AUTH-SES-E2E-037-subscription-status-lanjutan-memblok-buka-produk | FE+BE |
| TC-AUTH-SES-278 | TC-AUTH-SES-E2E-037-subscription-status-lanjutan-memblok-buka-produk | FE+BE |
| TC-AUTH-SES-279 | TC-AUTH-SES-E2E-038-subscription-renewed-dan-kembali-active | FE+BE |
| TC-AUTH-SES-280 | TC-AUTH-SES-E2E-039-subscription-memengaruhi-sesi-produk-existing | FE+BE |
| TC-AUTH-SES-281 | TC-AUTH-SES-E2E-038-subscription-renewed-dan-kembali-active | FE+BE |
| TC-AUTH-SES-282 | TC-AUTH-SES-E2E-013-token-pra-auth-dan-sesi-lama-expired-saat-confirm | FE+BE |
| TC-AUTH-SES-283 | TC-AUTH-SES-E2E-017-batas-idle-konfigurasi | FE+BE |
| TC-AUTH-SES-284 | TC-AUTH-SES-E2E-016-idle-timeout-dan-toast-warning-web | FE+BE |
| TC-AUTH-SES-285 | TC-AUTH-SES-E2E-050-biometric-siklus-token-90-hari-dan-rotasi | FE+BE |
| TC-AUTH-SES-286 | TC-AUTH-SES-E2E-075-biometric-agreement-token-ttl-boundary | FE+BE |
| TC-AUTH-SES-287 | TC-AUTH-SES-E2E-061-struktur-dan-format-surface-log | FE+BE |
| TC-AUTH-SES-288 | TC-AUTH-SES-E2E-061-struktur-dan-format-surface-log | FE+BE |
| TC-AUTH-SES-289 | TC-AUTH-SES-E2E-061-struktur-dan-format-surface-log | FE+BE |
| TC-AUTH-SES-290 | TC-AUTH-SES-E2E-008-dialog-lifecycle-di-dalam-produk-lain | FE+BE |
| TC-AUTH-SES-291 | TC-AUTH-SES-E2E-008-dialog-lifecycle-di-dalam-produk-lain | FE+BE |
| TC-AUTH-SES-292 | TC-AUTH-SES-E2E-008-dialog-lifecycle-di-dalam-produk-lain | FE+BE |
| TC-AUTH-SES-293 | TC-AUTH-SES-E2E-010-limit-login-mobile-dan-duplicate-login | FE+BE |
| TC-AUTH-SES-294 | TC-AUTH-SES-E2E-010-limit-login-mobile-dan-duplicate-login | FE+BE |
| TC-AUTH-SES-295 | TC-AUTH-SES-E2E-053-duplicate-login-dari-biometric-re-login | FE+BE |
| TC-AUTH-SES-296 | TC-AUTH-SES-E2E-053-duplicate-login-dari-biometric-re-login | FE+BE |
| TC-AUTH-SES-297 | TC-AUTH-SES-E2E-023-sesi-yatim-app-kill-dan-id-device | FE+BE |
| TC-AUTH-SES-298 | TC-AUTH-SES-E2E-023-sesi-yatim-app-kill-dan-id-device | FE+BE |
| TC-AUTH-SES-299 | TC-AUTH-SES-E2E-062-sinkron-lintas-modul-dan-plan-gating | FE+BE |
| TC-AUTH-SES-300 | TC-AUTH-SES-E2E-034-sesi-produk-bersama-web-dan-mobile | FE+BE |
| TC-AUTH-SES-301 | TC-AUTH-SES-E2E-033-cascade-sesi-produk-dan-pelepasan-seat | FE+BE |
| TC-AUTH-SES-302 | TC-AUTH-SES-E2E-035-popup-concurrent-dan-subscription-di-mobile | FE+BE |
| TC-AUTH-SES-303 | TC-AUTH-SES-E2E-035-popup-concurrent-dan-subscription-di-mobile | FE+BE |
| TC-AUTH-SES-304 | TC-AUTH-SES-E2E-024-app-access-revoke-dan-delete-client | FE+BE |
| TC-AUTH-SES-305 | TC-AUTH-SES-E2E-020-accessibility-focus-trap-dialog-lifecycle | FE+BE |
| TC-AUTH-SES-306 | TC-AUTH-SES-E2E-071-admin-triggered-dialog-focus-trap | FE+BE |
| TC-AUTH-SES-307 | TC-AUTH-SES-E2E-071-admin-triggered-dialog-focus-trap | FE+BE |
| TC-AUTH-SES-308 | TC-AUTH-SES-E2E-071-admin-triggered-dialog-focus-trap | FE+BE |
| TC-AUTH-SES-309 | TC-AUTH-SES-E2E-020-accessibility-focus-trap-dialog-lifecycle | FE+BE |
| TC-AUTH-SES-310 | TC-AUTH-SES-E2E-020-accessibility-focus-trap-dialog-lifecycle | FE+BE |
| TC-AUTH-SES-311 | TC-AUTH-SES-E2E-020-accessibility-focus-trap-dialog-lifecycle | FE+BE |
| TC-AUTH-SES-312 | TC-AUTH-SES-E2E-020-accessibility-focus-trap-dialog-lifecycle | FE+BE |
| TC-AUTH-SES-313 | TC-AUTH-SES-E2E-044-prompt-enable-biometric-dan-enroll | FE+BE |
| TC-AUTH-SES-314 | TC-AUTH-SES-E2E-044-prompt-enable-biometric-dan-enroll | FE+BE |
| TC-AUTH-SES-315 | TC-AUTH-SES-E2E-044-prompt-enable-biometric-dan-enroll | FE+BE |
| TC-AUTH-SES-316 | TC-AUTH-SES-E2E-029-invalidasi-semua-sesi-saat-akun-dihapus-atau-dinonaktifkan | FE+BE |
| TC-AUTH-SES-317 | TC-AUTH-SES-E2E-022-app-dihapus-dari-background-dan-push | FE+BE |
| TC-AUTH-SES-318 | TC-AUTH-SES-E2E-058-pencatatan-produk-concurrent-dan-cascade | FE+BE |
| TC-AUTH-SES-319 | TC-AUTH-SES-E2E-058-pencatatan-produk-concurrent-dan-cascade | FE+BE |
| TC-AUTH-SES-320 | TC-AUTH-SES-E2E-064-defense-in-depth-server-side | FE+BE |
| TC-AUTH-SES-321 | TC-AUTH-SES-E2E-012-dialog-lifecycle-multi-tab | FE+BE |
| TC-AUTH-SES-322 | TC-AUTH-SES-E2E-042-admin-force-logout-license-concurrent-user | FE+BE |
| TC-AUTH-SES-323 | TC-AUTH-SES-E2E-023-sesi-yatim-app-kill-dan-id-device | FE+BE |
| TC-AUTH-SES-324 | TC-AUTH-SES-E2E-044-prompt-enable-biometric-dan-enroll | FE+BE |
| TC-AUTH-SES-325 | TC-AUTH-SES-E2E-048-biometric-token-agreement-dan-privacy-policy | FE+BE |
| TC-AUTH-SES-326 | TC-AUTH-SES-E2E-027-user-dinonaktifkan-di-produk-fixed-asset | FE+BE |
| TC-AUTH-SES-327 | TC-AUTH-SES-E2E-027-user-dinonaktifkan-di-produk-fixed-asset | FE+BE |
| TC-AUTH-SES-328 | TC-AUTH-SES-E2E-053-duplicate-login-dari-biometric-re-login | FE+BE |
| TC-AUTH-SES-329 | TC-AUTH-SES-E2E-078-end-product-admin-console-dan-global-settings | FE+BE |
| TC-AUTH-SES-330 | TC-AUTH-SES-E2E-078-end-product-admin-console-dan-global-settings | FE+BE |
| TC-AUTH-SES-331 | TC-AUTH-SES-E2E-079-logout-manual-mobile-dan-ganti-akun | FE+BE |
| TC-AUTH-SES-332 | TC-AUTH-SES-E2E-079-logout-manual-mobile-dan-ganti-akun | FE+BE |
| TC-AUTH-SES-333 | TC-AUTH-SES-E2E-079-logout-manual-mobile-dan-ganti-akun | FE+BE |
| TC-AUTH-SES-334 | TC-AUTH-SES-E2E-080-keamanan-token-biometric-revoke-dan-integrity-token | FE+BE |
| TC-AUTH-SES-335 | TC-AUTH-SES-E2E-080-keamanan-token-biometric-revoke-dan-integrity-token | FE+BE |
| TC-AUTH-SES-336 | TC-AUTH-SES-E2E-080-keamanan-token-biometric-revoke-dan-integrity-token | FE+BE |
| TC-AUTH-SES-337 | TC-AUTH-SES-E2E-045-ketersediaan-biometric-perangkat-dan-ios | FE+BE |
| TC-AUTH-SES-338 | TC-AUTH-SES-E2E-081-toggle-biometric-sign-in-resilience | FE+BE |
| TC-AUTH-SES-339 | TC-AUTH-SES-E2E-081-toggle-biometric-sign-in-resilience | FE+BE |
| TC-AUTH-SES-340 | TC-AUTH-SES-E2E-081-toggle-biometric-sign-in-resilience | FE+BE |
| TC-AUTH-SES-341 | TC-AUTH-SES-E2E-082-kembali-ke-foreground-setelah-sesi-diakhiri-server | FE+BE |
| TC-AUTH-SES-342 | TC-AUTH-SES-E2E-082-kembali-ke-foreground-setelah-sesi-diakhiri-server | FE+BE |
| TC-AUTH-SES-343 | TC-AUTH-SES-E2E-082-kembali-ke-foreground-setelah-sesi-diakhiri-server | FE+BE |
| TC-AUTH-SES-344 | TC-AUTH-SES-E2E-083-cek-sesi-foreground-background-dan-sse-mobile | FE+BE |
| TC-AUTH-SES-345 | TC-AUTH-SES-E2E-084-os-kill-app-mobile-dan-sesi-tanpa-cookie | FE+BE |
| TC-AUTH-SES-346 | TC-AUTH-SES-E2E-084-os-kill-app-mobile-dan-sesi-tanpa-cookie | FE+BE |
| TC-AUTH-SES-347 | TC-AUTH-SES-E2E-083-cek-sesi-foreground-background-dan-sse-mobile | FE+BE |
| TC-AUTH-SES-348 | TC-AUTH-SES-E2E-083-cek-sesi-foreground-background-dan-sse-mobile | FE+BE |
| TC-AUTH-SES-349 | TC-AUTH-SES-E2E-084-os-kill-app-mobile-dan-sesi-tanpa-cookie | FE+BE |

---

## Ditahan

| TC | Temuan | Catatan |
|---|---|---|
| TC-AUTH-SES-260 | baru: PRD §12 #4 menyatakan iOS di luar scope rilis pertama | Enroll dan re-login biometric iOS; dikeluarkan dari spec 045, kembali ke spec sesudah iOS masuk scope |
| TC-AUTH-SES-261 | baru: PRD §12 #4 menyatakan iOS di luar scope rilis pertama | Biometric iOS; dikeluarkan dari spec 045, kembali ke spec sesudah iOS masuk scope |

---

## Temuan sumber (untuk QA)

Temuan ambigu, kontradiktif, atau kurang precondition (S-15) tercatat per spec di `## Notes` butir "Temuan untuk QA".
