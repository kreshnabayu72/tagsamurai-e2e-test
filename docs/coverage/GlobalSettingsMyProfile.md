# Coverage E2E — Global Settings > My Profile

Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md` (327 TC `TC-GS-PROFILE-1`–`327`, tanpa TC retired). Suite: `specs/GlobalSettings/MyProfile/`. Prefix: `GS` + `PROFILE` (`TC-GS-PROFILE-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`).

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 327 TC masuk 69 spec, 0 TC hanya-BE (modul tidak punya `tc-my-profile-backend.md`; TC request langsung, bypass file picker, dan akses lintas user masuk spec FE+BE lewat `K-1` atau bagian 6). Setiap TC terpetakan ke tepat satu spec di `sourceTc`.

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-GS-PROFILE-E2E-001-screening-navigasi-dan-header | Screening halaman: buka My Profile dari tiga app, Breadcrumb, dan Header | FE+BE | 31 | 1, 2, 3, 4, 5, 6, 9, 21 |
| TC-GS-PROFILE-E2E-002-screening-identity-tag-authenticator | Screening halaman: Section Identity, User TAG, Authenticator, loading, dan tanpa aksi administratif | FE+BE | 27 | 10, 11, 12, 15, 22, 23, 27, 29 |
| TC-GS-PROFILE-E2E-003-screening-variasi-data-akun | Screening halaman: variasi tampilan per akun (tanpa Employee ID, foto, TAG, plan Starter, Authenticator, Temporary User) | FE+BE | 26 | 7, 8, 13, 14, 16, 26 |
| TC-GS-PROFILE-E2E-004-tampilan-custom-field | Section Custom Field: urutan, format Phone, collapse, nilai kosong, dan alert Required | FE+BE | 21 | 17, 18, 19, 20 |
| TC-GS-PROFILE-E2E-005-guided-tooltip-otomatis-isi-dan-navigasi | Guided Tooltip: otomatis kunjungan pertama, isi Step 1-3, Next/Back/Done | FE+BE | 22 | 30, 31, 32, 33, 34 |
| TC-GS-PROFILE-E2E-006-guided-tooltip-skip-flag-dan-replay | Guided Tooltip: Skip, klik overlay, flag seen, kunjungan berikutnya, dan tombol replay | FE+BE | 23 | 35, 36, 37, 38 |
| TC-GS-PROFILE-E2E-007-guided-tooltip-interupsi-dan-keyboard | Guided Tooltip: resize viewport, navigasi keluar, dan operasi keyboard | FE+BE | 27 | 39, 40, 41 |
| TC-GS-PROFILE-E2E-008-aksesibilitas-keyboard-dan-aria | Aksesibilitas: keyboard halaman, fokus modal Change Password, ARIA, dan show/hide via keyboard | FE+BE | 38 | 42, 43, 313, 318 |
| TC-GS-PROFILE-E2E-009-tampilan-mobile-android | Mobile Android: card satu kolom, bottom sheet Avatar, bottom sheet Change Password, dan Guided Tooltip mobile | FE+BE | 26 | 45, 46, 47, 48, 49 |
| TC-GS-PROFILE-E2E-010-role-matrix-akses-my-profile-lewat-account-menu | Role Matrix: akses My Profile lewat account menu navbar per role | FE+BE | 19 | 50, 55, 60, 65, 70 |
| TC-GS-PROFILE-E2E-011-role-matrix-product-selector | Role Matrix: Product Selector berpindah konteks produk per role | FE+BE | 18 | 51, 56, 61, 66 |
| TC-GS-PROFILE-E2E-012-role-matrix-change-password-berhasil | Role Matrix: Change Password berhasil per role | FE+BE | 10 | 52, 57, 62, 67 |
| TC-GS-PROFILE-E2E-013-role-matrix-edit-photo-berhasil | Role Matrix: Edit Photo berhasil per role | FE+BE | 8 | 53, 58, 63, 68 |
| TC-GS-PROFILE-E2E-014-role-matrix-delete-photo-berhasil | Role Matrix: Delete Photo berhasil per role | FE+BE | 9 | 54, 59, 64, 69 |
| TC-GS-PROFILE-E2E-015-gate-akses-sesi-dan-pemilik-record | Gate akses My Profile: tanpa sesi, sesi habis, dan hanya record sendiri | FE+BE | 18 | 71, 72, 306, 114 |
| TC-GS-PROFILE-E2E-016-change-password-layar-modal-dan-show-hide | Change Password: layar modal, masked input, dan kontrol show/hide password | FE+BE | 48 | 73, 74, 316, 317 |
| TC-GS-PROFILE-E2E-017-change-password-checklist-password-policy | Change Password: checklist Password Policy real-time dan batas 72 karakter | FE+BE | 23 | 75, 76, 77, 78, 79, 80, 81, 82, 83 |
| TC-GS-PROFILE-E2E-018-change-password-validasi-kosong-dan-confirm-beda | Change Password: field kosong dan Confirm tidak sama diblokir | FE+BE | 55 | 84, 85, 86, 87, 90, 91, 92 |
| TC-GS-PROFILE-E2E-019-change-password-current-salah-dan-hitungan | Change Password: Current Password salah, hitungan percobaan, dan urutan evaluasi | FE+BE | 38 | 88, 89, 102, 103 |
| TC-GS-PROFILE-E2E-020-change-password-penolakan-server-aturan-policy | Change Password: penolakan server per aturan Password Policy (enam aturan) | FE+BE | 13 | 93, 94, 95, 96, 97, 98 |
| TC-GS-PROFILE-E2E-021-change-password-penolakan-server-lanjutan | Change Password: batas 72 karakter, multi-aturan, non-ASCII, sama dengan password aktif, dan anti-reuse | FE+BE | 45 | 99, 100, 101, 104, 315 |
| TC-GS-PROFILE-E2E-022-change-password-berhasil-dan-saving-state | Change Password berhasil: toast, saving state, klik ganda, auto-hide 4 detik, tanpa guard | FE+BE | 47 | 105, 106, 109, 110, 156 |
| TC-GS-PROFILE-E2E-023-change-password-berhasil-login-dan-reset-counter | Change Password berhasil: login password baru, reset counter Change Password dan Login | FE+BE | 49 | 107, 108, 307 |
| TC-GS-PROFILE-E2E-024-change-password-counter-lintas-fitur | Change Password: hitungan independen dari Login dan reset oleh Reset Password | FE+BE | 60 | 137, 138, 247, 248 |
| TC-GS-PROFILE-E2E-025-change-password-menutup-modal-kosong-dan-backdrop | Change Password: Menutup Modal Kosong (X, Cancel, Esc), Klik Backdrop, dan Isian Dikosongkan Kembali | FE+BE | 26 | 141, 142, 143, 150, 152 |
| TC-GS-PROFILE-E2E-026-change-password-dialog-unsaved-changes | Change Password: Dialog Unsaved Changes saat Menutup Modal Terisi | FE+BE | 34 | 144, 145, 146, 147, 148, 149, 151 |
| TC-GS-PROFILE-E2E-027-change-password-guard-refresh-dan-pindah-menu | Change Password: Guard Refresh Browser dan Pindah Menu Navbar saat Modal Terisi | FE+BE | 27 | 153, 154, 155, 309 |
| TC-GS-PROFILE-E2E-028-change-password-lock-15-menit-toast-format-timezone | Change Password: Lock 15 Menit (Toast, Format 12 Jam, Timezone, Note User Log, Time Format Berubah) | FE+BE | 45 | 115, 117, 118, 119, 251 |
| TC-GS-PROFILE-E2E-029-change-password-lock-state-modal-dan-tooltip-save | Change Password: [Save] Disabled saat Modal Dibuka Terkunci, Tooltip, Loading Baca Lock, dan Fail-Open | FE+BE | 52 | 44, 116, 120, 121, 139, 326, 327 |
| TC-GS-PROFILE-E2E-030-change-password-lock-batas-waktu-15-menit | Change Password: Batas Waktu Boleh-Coba-Lagi (Satu Langkah Sebelum, Tepat, dan Setelah) | FE+BE | 15 | 123, 124, 125 |
| TC-GS-PROFILE-E2E-031-change-password-lock-1-jam-dan-wajib-reset | Change Password: Lock 1 Jam, Tier Wajib-Reset, dan Tidak Lepas oleh Waktu | FE+BE | 33 | 126, 127, 128, 130 |
| TC-GS-PROFILE-E2E-032-change-password-reset-harian-dan-eskalasi-7-hari | Change Password: Reset Hitungan Harian per Timezone, Lock Melewati Tengah Malam, dan Eskalasi 7 Hari | FE+BE | 41 | 131, 132, 133, 134, 135 |
| TC-GS-PROFILE-E2E-033-resilience-halaman-dan-access-status | Resilience (Mock): Fetch Awal 500, Kegagalan Access & Status, Timeout, Try Again, dan Banner Email Change Gagal Dibaca | mock | 33 | 28, 188, 189, 305, 310 |
| TC-GS-PROFILE-E2E-034-resilience-change-password-dan-foto | Resilience (Mock): Change Password, Edit Photo, dan Delete Photo Gagal 500, 403, dan Timeout | mock | 60 | 111, 112, 113, 168, 169, 175, 176 |
| TC-GS-PROFILE-E2E-035-resilience-kegagalan-transaksi-server | Resilience: Kegagalan di Tengah Transaksi Server pada Change Password, Edit Photo, dan Delete Photo | FE+BE | 35 | 298, 299, 300 |
| TC-GS-PROFILE-E2E-036-edit-photo-overlay-dan-file-picker | Edit Photo: Hover Overlay, Edit Langsung dari Overlay, Filter File Picker, dan Batal | FE+BE | 17 | 157, 158, 159, 160, 165 |
| TC-GS-PROFILE-E2E-037-edit-photo-berhasil-per-format | Edit Photo: Berhasil dengan PNG, JPG, dan JPEG | FE+BE | 23 | 161, 162, 163 |
| TC-GS-PROFILE-E2E-038-edit-photo-ganti-resize-dan-toast | Edit Photo: Ganti Foto, Resize Lebih dari 1 MB, Tepat 1 MB, dan Toast Baru Menggantikan Toast Lama | FE+BE | 30 | 164, 166, 167, 314 |
| TC-GS-PROFILE-E2E-039-delete-photo-dialog-remove-photo-dan-berhasil | Delete Photo: Dialog Remove Photo (Cancel, Esc, Backdrop), Berhasil, dan Klik Ganda Remove | FE+BE | 28 | 170, 171, 172, 173, 174, 177 |
| TC-GS-PROFILE-E2E-040-product-selector-daftar-opsi | Product Selector: Daftar Opsi per App Access dan Produk yang Dicabut | FE+BE | 22 | 178, 179, 180, 181 |
| TC-GS-PROFILE-E2E-041-product-selector-default-sesuai-app-asal | Product Selector: Default Mengikuti App Asal Navigasi | FE+BE | 16 | 182, 183, 184, 185 |
| TC-GS-PROFILE-E2E-042-product-selector-berganti-produk-in-page | Product Selector: Berganti Produk In-Page, Loading, Refresh, dan Buka Ulang Kembali ke Default | FE+BE | 20 | 186, 187, 199, 200 |
| TC-GS-PROFILE-E2E-043-access-status-per-role-global-settings | Role Matrix: Section Access & Status Konteks Global Settings per Role | FE+BE | 34 | 190, 191, 192, 193 |
| TC-GS-PROFILE-E2E-044-access-status-konteks-produk | Section Access & Status: Konteks Fixed Asset, Admin Console, Status Inactive, dan Produk Belum Ter-provision | FE+BE | 25 | 194, 195, 196, 197, 198 |
| TC-GS-PROFILE-E2E-045-product-selector-perubahan-app-access-dan-role-saat-halaman-terbuka | Product Selector: App Access Dicabut, Role Di-assign atau Dicabut, dan Role Produk Berubah saat Halaman Terbuka | FE+BE | 46 | 201, 202, 203, 264, 265, 266 |
| TC-GS-PROFILE-E2E-046-banner-pending-email-change-tampilan | Pending Email Change: Badge Header, Banner, Teks Bantu Email, Refresh, dan Email Tidak Berubah | FE+BE | 15 | 24, 205, 206, 207, 211, 216 |
| TC-GS-PROFILE-E2E-047-banner-pending-email-change-tanpa-permintaan-dan-admin | Pending Email Change: Tanpa Permintaan Live dan Admin Mengubah Email | FE+BE | 13 | 25, 208, 246 |
| TC-GS-PROFILE-E2E-048-banner-pending-email-change-tautan-kedaluwarsa | Pending Email Change: Tautan Konfirmasi Kurang dari 24 Jam, Lebih dari 24 Jam, dan Halaman 404 Confirmation Link Expired | FE+BE | 21 | 212, 213, 214, 215 |
| TC-GS-PROFILE-E2E-049-pencatatan-edit-dan-delete-photo | Pencatatan Edit Photo dan Delete Photo di Changelog, System Log, dan Activity Log | FE+BE | 39 | 218, 219, 220, 221, 222, 223 |
| TC-GS-PROFILE-E2E-050-pencatatan-change-password-dan-password-tidak-bocor | Pencatatan Change Password: Note Sukses dan Salah, Tanpa Nilai Password | FE+BE | 29 | 228, 230, 231, 282 |
| TC-GS-PROFILE-E2E-051-pencatatan-lock-change-password | Pencatatan Change Password: Note Locked 15 Menit, 1 Jam, Wajib Reset, dan Eskalasi 7 Hari | FE+BE | 28 | 232, 233, 234, 235 |
| TC-GS-PROFILE-E2E-052-absence-log-aksi-foto-ditolak | Absence Log: Delete Photo No-op, Ekstensi Ditolak, dan Storage Penuh Tidak Menulis Log | FE+BE | 37 | 224, 225, 226 |
| TC-GS-PROFILE-E2E-053-absence-log-lain | Absence Log: Banner Email Change, Penolakan Change Password, dan Ganti Produk Tidak Menulis Log | FE+BE | 54 | 227, 236, 237 |
| TC-GS-PROFILE-E2E-054-sinkron-foto-navbar-dan-user | Sinkron Foto: Avatar Navbar, User List, dan Detail User Setelah Edit atau Delete Photo | FE+BE | 27 | 238, 239, 240, 241 |
| TC-GS-PROFILE-E2E-055-sinkron-foto-lintas-modul | Sinkron Foto: Fixed Asset, Admin Console, Recycle Bin, dan Changelog File Manager | FE+BE | 39 | 242, 243, 244, 245, 312 |
| TC-GS-PROFILE-E2E-056-sinkron-identitas-tag-dan-authenticator | Sinkron Data Admin: Rename Position dan Division, Pair dan Unpair TAG, Reset Authenticator | FE+BE | 32 | 217, 260, 261, 262, 263 |
| TC-GS-PROFILE-E2E-057-sinkron-custom-field-siklus-hidup | Sinkron Custom Field: Buat, Nonaktifkan, Aktifkan, Wajib, dan Hapus | FE+BE | 29 | 254, 255, 256, 257, 259 |
| TC-GS-PROFILE-E2E-058-sinkron-custom-field-tipe-nama-dan-dropdown | Sinkron Custom Field: Ganti Data Type, Rename Field, Rename dan Hapus Value Dropdown | FE+BE | 22 | 258, 319, 320, 321 |
| TC-GS-PROFILE-E2E-059-storage-penuh-edit-photo-diblokir | Storage Penuh atau Melebihi Kuota: Edit Photo Diblokir, Delete Photo Tetap Berhasil | FE+BE | 32 | 283, 284, 285, 288, 289, 290 |
| TC-GS-PROFILE-E2E-060-storage-batas-kuota-ledger-dan-perubahan-kuota | Storage di Bawah Kuota, Tanpa Kuota, Cek Ledger, dan Perubahan Kuota di License Allocation | FE+BE | 28 | 286, 287, 291, 252, 253 |
| TC-GS-PROFILE-E2E-061-multi-sesi-change-password-mengakhiri-sesi-lain | Multi-Sesi: Change Password Mengakhiri Sesi Lain, Dialog Password Changed, dan Lock Lintas Sesi | FE+BE | 34 | 136, 140, 249, 292, 293, 294 |
| TC-GS-PROFILE-E2E-062-multi-sesi-race-change-password-dan-user-log | Multi-Sesi: Sesi yang Kalah, Dua Request Bersamaan, dan User Log Logout | FE+BE | 34 | 229, 295, 296, 297 |
| TC-GS-PROFILE-E2E-063-multi-tab-edit-dan-delete-photo-bersamaan | Multi-Tab: Edit Photo dan Delete Photo Bersamaan di Dua Tab | FE+BE | 31 | 301, 302, 311 |
| TC-GS-PROFILE-E2E-064-realtime-banner-pending-email-change | Realtime: Banner Hilang Saat Admin Membatalkan atau Tautan Konfirmasi Diklik | FE+BE | 15 | 209, 210 |
| TC-GS-PROFILE-E2E-065-biometric-dicabut-setelah-change-password | Change Password Mencabut Kredensial Biometric Lintas Device | FE+BE | 7 | 250 |
| TC-GS-PROFILE-E2E-066-defense-akses-lintas-user | Defense-in-Depth: Akses Lintas User Ditolak 403 untuk Lihat Profil, Change Password, Edit Photo, Delete Photo, dan Access & Status | FE+BE | 24 | 204, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276 |
| TC-GS-PROFILE-E2E-067-defense-payload-langsung-photo-dan-change-password | Defense-in-Depth: Payload Edit Photo Tidak Sah (422) dan Request Change Password Langsung (Field-Level, 429) | FE+BE | 42 | 122, 129, 277, 278, 279, 280, 281, 308 |
| TC-GS-PROFILE-E2E-068-state-tenant-plan-starter-dan-enterprise | State Tenant: Plan Starter dan Enterprise Tanpa Gating pada Change Password dan Edit Photo | FE+BE | 15 | 303, 304 |
| TC-GS-PROFILE-E2E-069-state-tenant-client-suspended-dan-expired | State Tenant: Client Suspended dan Expired Menolak Aksi Tulis, My Profile Tetap Dapat Dibaca | FE+BE | 32 | 322, 323, 324, 325 |

## TC hanya-BE (tidak masuk spec)

Tidak ada. Kandidat yang ditimbang (TC-122, 129, 204, 267–281, 296–300, 308) tetap masuk spec FE+BE dengan kebutuhan teknisnya di `## Prerequisites`.

## Pembagian TC lintas spec dan pengecualian

- Butir "Pembagian TC lintas spec" ada di `## Notes` spec `062`, `067`.
- `P-1` dipakai spec `063`, `069`; alasannya di `## Notes` tiap spec.
- `P-2` dipakai spec `045`, `047`, `056`, `057`, `058`, `060`; alasannya di `## Notes` tiap spec.
- `P-5` dipakai spec `029`, `052`, `053`, `059`; alasannya di `## Notes` tiap spec.
- `K-1` dipakai spec `066`, `067`; alasannya di `## Notes` tiap spec.
- Spec `068` (plan starter dan enterprise, TC-303, 304) dan `069` (Client Suspended dan Expired, TC-322–325) adalah satu topik state tenant yang dipisah karena gabungannya sekitar 50 langkah tanpa alasan yang bisa dipertahankan.

## Kebutuhan lingkungan (tim FE)

- Env var yang sudah terdaftar dan dipakai: `LP_PASSWORD_WRONG`.
- Env var baru yang perlu didaftarkan di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`: `GS_PROFILE_ADMIN_PASSWORD`, `GS_PROFILE_BASIC_PASSWORD`, `GS_PROFILE_ENTERPRISE_PASSWORD`, `GS_PROFILE_EXPIRED_PASSWORD`, `GS_PROFILE_FRESHGUIDE_PASSWORD`, `GS_PROFILE_MULTI_PASSWORD`, `GS_PROFILE_NOPHOTO_PASSWORD`, `GS_PROFILE_NOQUOTA_PASSWORD`, `GS_PROFILE_NOTENROLLED_PASSWORD`, `GS_PROFILE_PENDING_PASSWORD`, `GS_PROFILE_PHOTO_PASSWORD`, `GS_PROFILE_PWD12H_PASSWORD`, `GS_PROFILE_PWD_PASSWORD`, `GS_PROFILE_RO_PASSWORD`, `GS_PROFILE_SAMSSIEM_PASSWORD`, `GS_PROFILE_STARTER_PASSWORD`, `GS_PROFILE_STORAGEFULL_PASSWORD`, `GS_PROFILE_STORAGENEAR_PASSWORD`, `GS_PROFILE_SUSPENDED_PASSWORD`, `GS_PROFILE_SYSROLE_PASSWORD`, `GS_PROFILE_TC_PASSWORD`, `GS_PROFILE_TEMP_PASSWORD`, `GS_PROFILE_UNPROV_PASSWORD`, `PROFILE_PASSWORD_72`, `PROFILE_PASSWORD_NEW`. Pola `GS_PROFILE_<ROLE>_PASSWORD`, satu nama untuk satu akun Pre-setup (daftar akun di `suite.md`).
- Hook suite (`suite.md`, Hook suite 1 sampai 7): login aktor default, pembukaan My Profile di web, flag Guided Tooltip `guided_tooltip_seen_gs-my-profile`, sesi API pelaku kedua (admin Pre-setup #6), jaring pengaman `beforeunload`/`Unsaved Changes`, reset counter Change Password dan Login (#7, #18), serta pemulihan jam, password, foto, Storage, dan status Client di hook `after`. Suite serial (`parallel: false`).
- Kemampuan teknis yang disediakan tim FE/BE (mekanisme tidak disebut TC, PRD, atau LLD): mengatur jam server dan jam browser bersama; membaca dan mereset counter Change Password/Login; membaca jumlah sesi aktif; fixture foto aktif, kuota dan ledger Storage, status Client dan plan tier; permintaan Email change live dan umurnya; intercept jaringan (5xx, timeout) untuk spec `033`–`035`; dua sesi browser atau perangkat untuk spec `061`–`064`; request langsung ke server dan bypass file picker untuk spec `066`–`067`; emulator atau perangkat Android untuk spec mobile; hardware biometrik untuk spec `065`.
- Spec `Mode: mock` (`033`, `034`): `openapi.yaml` dan `low-level-design.md` modul tidak ada, sehingga endpoint ditulis "disediakan tim FE". Hook suite 1, 3, 4, 6, 7 mengasumsikan backend nyata; tim FE menyesuaikan mekanismenya untuk spec mock.
- Akun tanpa App Access Global Settings (Pre-setup #4, #22): spec `040` dan `043` membuka My Profile dari Fixed Asset atau Supply Asset secara eksplisit, karena hook suite 2 membuka dari Global Settings. Spec mobile `009` menulis langkah buka My Profile di aplikasi Android.
- Fixture baru: berkas `fixtures/myProfile.json` dengan kunci `Fixture.myProfile.*` yang dirujuk spec.

## Tindak lanjut di luar stage ini

Dicatat sebagai kebutuhan atau usulan; tidak membuka stage ini.

- **Perbaikan TC sumber (QA):** temuan per spec ada di butir "Temuan untuk QA" pada `## Notes`. Pola yang berulang: Post Condition tanpa langkah observasi (counter, password, sesi) tidak diasersi; mekanisme fixture (jam, counter, status Client, Storage, permintaan Email) tidak disebut; Precondition "Total Control" tidak cocok dengan akun Pre-setup #7, #9, #10, #11; TC-54/59/64/69/273 membutuhkan foto aktif padahal Pre-setup #1 tanpa foto; TC mengubah Custom Field Pre-setup #16 yang dibaca TC lain (spec memakai field milik spec bersuffix, S-06).
- **Spec panjang:** 18 spec melewati sekitar 35 langkah (nominal atau sesudah ekspansi blok ulang) dan menulis alasannya di `## Notes`; ditinjau di `e2e-audit`.
- **Tim FE:** mendaftarkan env var baru dan membuat `fixtures/myProfile.json`.

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-GS-PROFILE-1 | TC-GS-PROFILE-E2E-001-screening-navigasi-dan-header | FE+BE |
| TC-GS-PROFILE-2 | TC-GS-PROFILE-E2E-001-screening-navigasi-dan-header | FE+BE |
| TC-GS-PROFILE-3 | TC-GS-PROFILE-E2E-001-screening-navigasi-dan-header | FE+BE |
| TC-GS-PROFILE-4 | TC-GS-PROFILE-E2E-001-screening-navigasi-dan-header | FE+BE |
| TC-GS-PROFILE-5 | TC-GS-PROFILE-E2E-001-screening-navigasi-dan-header | FE+BE |
| TC-GS-PROFILE-6 | TC-GS-PROFILE-E2E-001-screening-navigasi-dan-header | FE+BE |
| TC-GS-PROFILE-7 | TC-GS-PROFILE-E2E-003-screening-variasi-data-akun | FE+BE |
| TC-GS-PROFILE-8 | TC-GS-PROFILE-E2E-003-screening-variasi-data-akun | FE+BE |
| TC-GS-PROFILE-9 | TC-GS-PROFILE-E2E-001-screening-navigasi-dan-header | FE+BE |
| TC-GS-PROFILE-10 | TC-GS-PROFILE-E2E-002-screening-identity-tag-authenticator | FE+BE |
| TC-GS-PROFILE-11 | TC-GS-PROFILE-E2E-002-screening-identity-tag-authenticator | FE+BE |
| TC-GS-PROFILE-12 | TC-GS-PROFILE-E2E-002-screening-identity-tag-authenticator | FE+BE |
| TC-GS-PROFILE-13 | TC-GS-PROFILE-E2E-003-screening-variasi-data-akun | FE+BE |
| TC-GS-PROFILE-14 | TC-GS-PROFILE-E2E-003-screening-variasi-data-akun | FE+BE |
| TC-GS-PROFILE-15 | TC-GS-PROFILE-E2E-002-screening-identity-tag-authenticator | FE+BE |
| TC-GS-PROFILE-16 | TC-GS-PROFILE-E2E-003-screening-variasi-data-akun | FE+BE |
| TC-GS-PROFILE-17 | TC-GS-PROFILE-E2E-004-tampilan-custom-field | FE+BE |
| TC-GS-PROFILE-18 | TC-GS-PROFILE-E2E-004-tampilan-custom-field | FE+BE |
| TC-GS-PROFILE-19 | TC-GS-PROFILE-E2E-004-tampilan-custom-field | FE+BE |
| TC-GS-PROFILE-20 | TC-GS-PROFILE-E2E-004-tampilan-custom-field | FE+BE |
| TC-GS-PROFILE-21 | TC-GS-PROFILE-E2E-001-screening-navigasi-dan-header | FE+BE |
| TC-GS-PROFILE-22 | TC-GS-PROFILE-E2E-002-screening-identity-tag-authenticator | FE+BE |
| TC-GS-PROFILE-23 | TC-GS-PROFILE-E2E-002-screening-identity-tag-authenticator | FE+BE |
| TC-GS-PROFILE-24 | TC-GS-PROFILE-E2E-046-banner-pending-email-change-tampilan | FE+BE |
| TC-GS-PROFILE-25 | TC-GS-PROFILE-E2E-047-banner-pending-email-change-tanpa-permintaan-dan-admin | FE+BE |
| TC-GS-PROFILE-26 | TC-GS-PROFILE-E2E-003-screening-variasi-data-akun | FE+BE |
| TC-GS-PROFILE-27 | TC-GS-PROFILE-E2E-002-screening-identity-tag-authenticator | FE+BE |
| TC-GS-PROFILE-28 | TC-GS-PROFILE-E2E-033-resilience-halaman-dan-access-status | mock |
| TC-GS-PROFILE-29 | TC-GS-PROFILE-E2E-002-screening-identity-tag-authenticator | FE+BE |
| TC-GS-PROFILE-30 | TC-GS-PROFILE-E2E-005-guided-tooltip-otomatis-isi-dan-navigasi | FE+BE |
| TC-GS-PROFILE-31 | TC-GS-PROFILE-E2E-005-guided-tooltip-otomatis-isi-dan-navigasi | FE+BE |
| TC-GS-PROFILE-32 | TC-GS-PROFILE-E2E-005-guided-tooltip-otomatis-isi-dan-navigasi | FE+BE |
| TC-GS-PROFILE-33 | TC-GS-PROFILE-E2E-005-guided-tooltip-otomatis-isi-dan-navigasi | FE+BE |
| TC-GS-PROFILE-34 | TC-GS-PROFILE-E2E-005-guided-tooltip-otomatis-isi-dan-navigasi | FE+BE |
| TC-GS-PROFILE-35 | TC-GS-PROFILE-E2E-006-guided-tooltip-skip-flag-dan-replay | FE+BE |
| TC-GS-PROFILE-36 | TC-GS-PROFILE-E2E-006-guided-tooltip-skip-flag-dan-replay | FE+BE |
| TC-GS-PROFILE-37 | TC-GS-PROFILE-E2E-006-guided-tooltip-skip-flag-dan-replay | FE+BE |
| TC-GS-PROFILE-38 | TC-GS-PROFILE-E2E-006-guided-tooltip-skip-flag-dan-replay | FE+BE |
| TC-GS-PROFILE-39 | TC-GS-PROFILE-E2E-007-guided-tooltip-interupsi-dan-keyboard | FE+BE |
| TC-GS-PROFILE-40 | TC-GS-PROFILE-E2E-007-guided-tooltip-interupsi-dan-keyboard | FE+BE |
| TC-GS-PROFILE-41 | TC-GS-PROFILE-E2E-007-guided-tooltip-interupsi-dan-keyboard | FE+BE |
| TC-GS-PROFILE-42 | TC-GS-PROFILE-E2E-008-aksesibilitas-keyboard-dan-aria | FE+BE |
| TC-GS-PROFILE-43 | TC-GS-PROFILE-E2E-008-aksesibilitas-keyboard-dan-aria | FE+BE |
| TC-GS-PROFILE-44 | TC-GS-PROFILE-E2E-029-change-password-lock-state-modal-dan-tooltip-save | FE+BE |
| TC-GS-PROFILE-45 | TC-GS-PROFILE-E2E-009-tampilan-mobile-android | FE+BE |
| TC-GS-PROFILE-46 | TC-GS-PROFILE-E2E-009-tampilan-mobile-android | FE+BE |
| TC-GS-PROFILE-47 | TC-GS-PROFILE-E2E-009-tampilan-mobile-android | FE+BE |
| TC-GS-PROFILE-48 | TC-GS-PROFILE-E2E-009-tampilan-mobile-android | FE+BE |
| TC-GS-PROFILE-49 | TC-GS-PROFILE-E2E-009-tampilan-mobile-android | FE+BE |
| TC-GS-PROFILE-50 | TC-GS-PROFILE-E2E-010-role-matrix-akses-my-profile-lewat-account-menu | FE+BE |
| TC-GS-PROFILE-51 | TC-GS-PROFILE-E2E-011-role-matrix-product-selector | FE+BE |
| TC-GS-PROFILE-52 | TC-GS-PROFILE-E2E-012-role-matrix-change-password-berhasil | FE+BE |
| TC-GS-PROFILE-53 | TC-GS-PROFILE-E2E-013-role-matrix-edit-photo-berhasil | FE+BE |
| TC-GS-PROFILE-54 | TC-GS-PROFILE-E2E-014-role-matrix-delete-photo-berhasil | FE+BE |
| TC-GS-PROFILE-55 | TC-GS-PROFILE-E2E-010-role-matrix-akses-my-profile-lewat-account-menu | FE+BE |
| TC-GS-PROFILE-56 | TC-GS-PROFILE-E2E-011-role-matrix-product-selector | FE+BE |
| TC-GS-PROFILE-57 | TC-GS-PROFILE-E2E-012-role-matrix-change-password-berhasil | FE+BE |
| TC-GS-PROFILE-58 | TC-GS-PROFILE-E2E-013-role-matrix-edit-photo-berhasil | FE+BE |
| TC-GS-PROFILE-59 | TC-GS-PROFILE-E2E-014-role-matrix-delete-photo-berhasil | FE+BE |
| TC-GS-PROFILE-60 | TC-GS-PROFILE-E2E-010-role-matrix-akses-my-profile-lewat-account-menu | FE+BE |
| TC-GS-PROFILE-61 | TC-GS-PROFILE-E2E-011-role-matrix-product-selector | FE+BE |
| TC-GS-PROFILE-62 | TC-GS-PROFILE-E2E-012-role-matrix-change-password-berhasil | FE+BE |
| TC-GS-PROFILE-63 | TC-GS-PROFILE-E2E-013-role-matrix-edit-photo-berhasil | FE+BE |
| TC-GS-PROFILE-64 | TC-GS-PROFILE-E2E-014-role-matrix-delete-photo-berhasil | FE+BE |
| TC-GS-PROFILE-65 | TC-GS-PROFILE-E2E-010-role-matrix-akses-my-profile-lewat-account-menu | FE+BE |
| TC-GS-PROFILE-66 | TC-GS-PROFILE-E2E-011-role-matrix-product-selector | FE+BE |
| TC-GS-PROFILE-67 | TC-GS-PROFILE-E2E-012-role-matrix-change-password-berhasil | FE+BE |
| TC-GS-PROFILE-68 | TC-GS-PROFILE-E2E-013-role-matrix-edit-photo-berhasil | FE+BE |
| TC-GS-PROFILE-69 | TC-GS-PROFILE-E2E-014-role-matrix-delete-photo-berhasil | FE+BE |
| TC-GS-PROFILE-70 | TC-GS-PROFILE-E2E-010-role-matrix-akses-my-profile-lewat-account-menu | FE+BE |
| TC-GS-PROFILE-71 | TC-GS-PROFILE-E2E-015-gate-akses-sesi-dan-pemilik-record | FE+BE |
| TC-GS-PROFILE-72 | TC-GS-PROFILE-E2E-015-gate-akses-sesi-dan-pemilik-record | FE+BE |
| TC-GS-PROFILE-73 | TC-GS-PROFILE-E2E-016-change-password-layar-modal-dan-show-hide | FE+BE |
| TC-GS-PROFILE-74 | TC-GS-PROFILE-E2E-016-change-password-layar-modal-dan-show-hide | FE+BE |
| TC-GS-PROFILE-75 | TC-GS-PROFILE-E2E-017-change-password-checklist-password-policy | FE+BE |
| TC-GS-PROFILE-76 | TC-GS-PROFILE-E2E-017-change-password-checklist-password-policy | FE+BE |
| TC-GS-PROFILE-77 | TC-GS-PROFILE-E2E-017-change-password-checklist-password-policy | FE+BE |
| TC-GS-PROFILE-78 | TC-GS-PROFILE-E2E-017-change-password-checklist-password-policy | FE+BE |
| TC-GS-PROFILE-79 | TC-GS-PROFILE-E2E-017-change-password-checklist-password-policy | FE+BE |
| TC-GS-PROFILE-80 | TC-GS-PROFILE-E2E-017-change-password-checklist-password-policy | FE+BE |
| TC-GS-PROFILE-81 | TC-GS-PROFILE-E2E-017-change-password-checklist-password-policy | FE+BE |
| TC-GS-PROFILE-82 | TC-GS-PROFILE-E2E-017-change-password-checklist-password-policy | FE+BE |
| TC-GS-PROFILE-83 | TC-GS-PROFILE-E2E-017-change-password-checklist-password-policy | FE+BE |
| TC-GS-PROFILE-84 | TC-GS-PROFILE-E2E-018-change-password-validasi-kosong-dan-confirm-beda | FE+BE |
| TC-GS-PROFILE-85 | TC-GS-PROFILE-E2E-018-change-password-validasi-kosong-dan-confirm-beda | FE+BE |
| TC-GS-PROFILE-86 | TC-GS-PROFILE-E2E-018-change-password-validasi-kosong-dan-confirm-beda | FE+BE |
| TC-GS-PROFILE-87 | TC-GS-PROFILE-E2E-018-change-password-validasi-kosong-dan-confirm-beda | FE+BE |
| TC-GS-PROFILE-88 | TC-GS-PROFILE-E2E-019-change-password-current-salah-dan-hitungan | FE+BE |
| TC-GS-PROFILE-89 | TC-GS-PROFILE-E2E-019-change-password-current-salah-dan-hitungan | FE+BE |
| TC-GS-PROFILE-90 | TC-GS-PROFILE-E2E-018-change-password-validasi-kosong-dan-confirm-beda | FE+BE |
| TC-GS-PROFILE-91 | TC-GS-PROFILE-E2E-018-change-password-validasi-kosong-dan-confirm-beda | FE+BE |
| TC-GS-PROFILE-92 | TC-GS-PROFILE-E2E-018-change-password-validasi-kosong-dan-confirm-beda | FE+BE |
| TC-GS-PROFILE-93 | TC-GS-PROFILE-E2E-020-change-password-penolakan-server-aturan-policy | FE+BE |
| TC-GS-PROFILE-94 | TC-GS-PROFILE-E2E-020-change-password-penolakan-server-aturan-policy | FE+BE |
| TC-GS-PROFILE-95 | TC-GS-PROFILE-E2E-020-change-password-penolakan-server-aturan-policy | FE+BE |
| TC-GS-PROFILE-96 | TC-GS-PROFILE-E2E-020-change-password-penolakan-server-aturan-policy | FE+BE |
| TC-GS-PROFILE-97 | TC-GS-PROFILE-E2E-020-change-password-penolakan-server-aturan-policy | FE+BE |
| TC-GS-PROFILE-98 | TC-GS-PROFILE-E2E-020-change-password-penolakan-server-aturan-policy | FE+BE |
| TC-GS-PROFILE-99 | TC-GS-PROFILE-E2E-021-change-password-penolakan-server-lanjutan | FE+BE |
| TC-GS-PROFILE-100 | TC-GS-PROFILE-E2E-021-change-password-penolakan-server-lanjutan | FE+BE |
| TC-GS-PROFILE-101 | TC-GS-PROFILE-E2E-021-change-password-penolakan-server-lanjutan | FE+BE |
| TC-GS-PROFILE-102 | TC-GS-PROFILE-E2E-019-change-password-current-salah-dan-hitungan | FE+BE |
| TC-GS-PROFILE-103 | TC-GS-PROFILE-E2E-019-change-password-current-salah-dan-hitungan | FE+BE |
| TC-GS-PROFILE-104 | TC-GS-PROFILE-E2E-021-change-password-penolakan-server-lanjutan | FE+BE |
| TC-GS-PROFILE-105 | TC-GS-PROFILE-E2E-022-change-password-berhasil-dan-saving-state | FE+BE |
| TC-GS-PROFILE-106 | TC-GS-PROFILE-E2E-022-change-password-berhasil-dan-saving-state | FE+BE |
| TC-GS-PROFILE-107 | TC-GS-PROFILE-E2E-023-change-password-berhasil-login-dan-reset-counter | FE+BE |
| TC-GS-PROFILE-108 | TC-GS-PROFILE-E2E-023-change-password-berhasil-login-dan-reset-counter | FE+BE |
| TC-GS-PROFILE-109 | TC-GS-PROFILE-E2E-022-change-password-berhasil-dan-saving-state | FE+BE |
| TC-GS-PROFILE-110 | TC-GS-PROFILE-E2E-022-change-password-berhasil-dan-saving-state | FE+BE |
| TC-GS-PROFILE-111 | TC-GS-PROFILE-E2E-034-resilience-change-password-dan-foto | mock |
| TC-GS-PROFILE-112 | TC-GS-PROFILE-E2E-034-resilience-change-password-dan-foto | mock |
| TC-GS-PROFILE-113 | TC-GS-PROFILE-E2E-034-resilience-change-password-dan-foto | mock |
| TC-GS-PROFILE-114 | TC-GS-PROFILE-E2E-015-gate-akses-sesi-dan-pemilik-record | FE+BE |
| TC-GS-PROFILE-115 | TC-GS-PROFILE-E2E-028-change-password-lock-15-menit-toast-format-timezone | FE+BE |
| TC-GS-PROFILE-116 | TC-GS-PROFILE-E2E-029-change-password-lock-state-modal-dan-tooltip-save | FE+BE |
| TC-GS-PROFILE-117 | TC-GS-PROFILE-E2E-028-change-password-lock-15-menit-toast-format-timezone | FE+BE |
| TC-GS-PROFILE-118 | TC-GS-PROFILE-E2E-028-change-password-lock-15-menit-toast-format-timezone | FE+BE |
| TC-GS-PROFILE-119 | TC-GS-PROFILE-E2E-028-change-password-lock-15-menit-toast-format-timezone | FE+BE |
| TC-GS-PROFILE-120 | TC-GS-PROFILE-E2E-029-change-password-lock-state-modal-dan-tooltip-save | FE+BE |
| TC-GS-PROFILE-121 | TC-GS-PROFILE-E2E-029-change-password-lock-state-modal-dan-tooltip-save | FE+BE |
| TC-GS-PROFILE-122 | TC-GS-PROFILE-E2E-067-defense-payload-langsung-photo-dan-change-password | FE+BE |
| TC-GS-PROFILE-123 | TC-GS-PROFILE-E2E-030-change-password-lock-batas-waktu-15-menit | FE+BE |
| TC-GS-PROFILE-124 | TC-GS-PROFILE-E2E-030-change-password-lock-batas-waktu-15-menit | FE+BE |
| TC-GS-PROFILE-125 | TC-GS-PROFILE-E2E-030-change-password-lock-batas-waktu-15-menit | FE+BE |
| TC-GS-PROFILE-126 | TC-GS-PROFILE-E2E-031-change-password-lock-1-jam-dan-wajib-reset | FE+BE |
| TC-GS-PROFILE-127 | TC-GS-PROFILE-E2E-031-change-password-lock-1-jam-dan-wajib-reset | FE+BE |
| TC-GS-PROFILE-128 | TC-GS-PROFILE-E2E-031-change-password-lock-1-jam-dan-wajib-reset | FE+BE |
| TC-GS-PROFILE-129 | TC-GS-PROFILE-E2E-067-defense-payload-langsung-photo-dan-change-password | FE+BE |
| TC-GS-PROFILE-130 | TC-GS-PROFILE-E2E-031-change-password-lock-1-jam-dan-wajib-reset | FE+BE |
| TC-GS-PROFILE-131 | TC-GS-PROFILE-E2E-032-change-password-reset-harian-dan-eskalasi-7-hari | FE+BE |
| TC-GS-PROFILE-132 | TC-GS-PROFILE-E2E-032-change-password-reset-harian-dan-eskalasi-7-hari | FE+BE |
| TC-GS-PROFILE-133 | TC-GS-PROFILE-E2E-032-change-password-reset-harian-dan-eskalasi-7-hari | FE+BE |
| TC-GS-PROFILE-134 | TC-GS-PROFILE-E2E-032-change-password-reset-harian-dan-eskalasi-7-hari | FE+BE |
| TC-GS-PROFILE-135 | TC-GS-PROFILE-E2E-032-change-password-reset-harian-dan-eskalasi-7-hari | FE+BE |
| TC-GS-PROFILE-136 | TC-GS-PROFILE-E2E-061-multi-sesi-change-password-mengakhiri-sesi-lain | FE+BE |
| TC-GS-PROFILE-137 | TC-GS-PROFILE-E2E-024-change-password-counter-lintas-fitur | FE+BE |
| TC-GS-PROFILE-138 | TC-GS-PROFILE-E2E-024-change-password-counter-lintas-fitur | FE+BE |
| TC-GS-PROFILE-139 | TC-GS-PROFILE-E2E-029-change-password-lock-state-modal-dan-tooltip-save | FE+BE |
| TC-GS-PROFILE-140 | TC-GS-PROFILE-E2E-061-multi-sesi-change-password-mengakhiri-sesi-lain | FE+BE |
| TC-GS-PROFILE-141 | TC-GS-PROFILE-E2E-025-change-password-menutup-modal-kosong-dan-backdrop | FE+BE |
| TC-GS-PROFILE-142 | TC-GS-PROFILE-E2E-025-change-password-menutup-modal-kosong-dan-backdrop | FE+BE |
| TC-GS-PROFILE-143 | TC-GS-PROFILE-E2E-025-change-password-menutup-modal-kosong-dan-backdrop | FE+BE |
| TC-GS-PROFILE-144 | TC-GS-PROFILE-E2E-026-change-password-dialog-unsaved-changes | FE+BE |
| TC-GS-PROFILE-145 | TC-GS-PROFILE-E2E-026-change-password-dialog-unsaved-changes | FE+BE |
| TC-GS-PROFILE-146 | TC-GS-PROFILE-E2E-026-change-password-dialog-unsaved-changes | FE+BE |
| TC-GS-PROFILE-147 | TC-GS-PROFILE-E2E-026-change-password-dialog-unsaved-changes | FE+BE |
| TC-GS-PROFILE-148 | TC-GS-PROFILE-E2E-026-change-password-dialog-unsaved-changes | FE+BE |
| TC-GS-PROFILE-149 | TC-GS-PROFILE-E2E-026-change-password-dialog-unsaved-changes | FE+BE |
| TC-GS-PROFILE-150 | TC-GS-PROFILE-E2E-025-change-password-menutup-modal-kosong-dan-backdrop | FE+BE |
| TC-GS-PROFILE-151 | TC-GS-PROFILE-E2E-026-change-password-dialog-unsaved-changes | FE+BE |
| TC-GS-PROFILE-152 | TC-GS-PROFILE-E2E-025-change-password-menutup-modal-kosong-dan-backdrop | FE+BE |
| TC-GS-PROFILE-153 | TC-GS-PROFILE-E2E-027-change-password-guard-refresh-dan-pindah-menu | FE+BE |
| TC-GS-PROFILE-154 | TC-GS-PROFILE-E2E-027-change-password-guard-refresh-dan-pindah-menu | FE+BE |
| TC-GS-PROFILE-155 | TC-GS-PROFILE-E2E-027-change-password-guard-refresh-dan-pindah-menu | FE+BE |
| TC-GS-PROFILE-156 | TC-GS-PROFILE-E2E-022-change-password-berhasil-dan-saving-state | FE+BE |
| TC-GS-PROFILE-157 | TC-GS-PROFILE-E2E-036-edit-photo-overlay-dan-file-picker | FE+BE |
| TC-GS-PROFILE-158 | TC-GS-PROFILE-E2E-036-edit-photo-overlay-dan-file-picker | FE+BE |
| TC-GS-PROFILE-159 | TC-GS-PROFILE-E2E-036-edit-photo-overlay-dan-file-picker | FE+BE |
| TC-GS-PROFILE-160 | TC-GS-PROFILE-E2E-036-edit-photo-overlay-dan-file-picker | FE+BE |
| TC-GS-PROFILE-161 | TC-GS-PROFILE-E2E-037-edit-photo-berhasil-per-format | FE+BE |
| TC-GS-PROFILE-162 | TC-GS-PROFILE-E2E-037-edit-photo-berhasil-per-format | FE+BE |
| TC-GS-PROFILE-163 | TC-GS-PROFILE-E2E-037-edit-photo-berhasil-per-format | FE+BE |
| TC-GS-PROFILE-164 | TC-GS-PROFILE-E2E-038-edit-photo-ganti-resize-dan-toast | FE+BE |
| TC-GS-PROFILE-165 | TC-GS-PROFILE-E2E-036-edit-photo-overlay-dan-file-picker | FE+BE |
| TC-GS-PROFILE-166 | TC-GS-PROFILE-E2E-038-edit-photo-ganti-resize-dan-toast | FE+BE |
| TC-GS-PROFILE-167 | TC-GS-PROFILE-E2E-038-edit-photo-ganti-resize-dan-toast | FE+BE |
| TC-GS-PROFILE-168 | TC-GS-PROFILE-E2E-034-resilience-change-password-dan-foto | mock |
| TC-GS-PROFILE-169 | TC-GS-PROFILE-E2E-034-resilience-change-password-dan-foto | mock |
| TC-GS-PROFILE-170 | TC-GS-PROFILE-E2E-039-delete-photo-dialog-remove-photo-dan-berhasil | FE+BE |
| TC-GS-PROFILE-171 | TC-GS-PROFILE-E2E-039-delete-photo-dialog-remove-photo-dan-berhasil | FE+BE |
| TC-GS-PROFILE-172 | TC-GS-PROFILE-E2E-039-delete-photo-dialog-remove-photo-dan-berhasil | FE+BE |
| TC-GS-PROFILE-173 | TC-GS-PROFILE-E2E-039-delete-photo-dialog-remove-photo-dan-berhasil | FE+BE |
| TC-GS-PROFILE-174 | TC-GS-PROFILE-E2E-039-delete-photo-dialog-remove-photo-dan-berhasil | FE+BE |
| TC-GS-PROFILE-175 | TC-GS-PROFILE-E2E-034-resilience-change-password-dan-foto | mock |
| TC-GS-PROFILE-176 | TC-GS-PROFILE-E2E-034-resilience-change-password-dan-foto | mock |
| TC-GS-PROFILE-177 | TC-GS-PROFILE-E2E-039-delete-photo-dialog-remove-photo-dan-berhasil | FE+BE |
| TC-GS-PROFILE-178 | TC-GS-PROFILE-E2E-040-product-selector-daftar-opsi | FE+BE |
| TC-GS-PROFILE-179 | TC-GS-PROFILE-E2E-040-product-selector-daftar-opsi | FE+BE |
| TC-GS-PROFILE-180 | TC-GS-PROFILE-E2E-040-product-selector-daftar-opsi | FE+BE |
| TC-GS-PROFILE-181 | TC-GS-PROFILE-E2E-040-product-selector-daftar-opsi | FE+BE |
| TC-GS-PROFILE-182 | TC-GS-PROFILE-E2E-041-product-selector-default-sesuai-app-asal | FE+BE |
| TC-GS-PROFILE-183 | TC-GS-PROFILE-E2E-041-product-selector-default-sesuai-app-asal | FE+BE |
| TC-GS-PROFILE-184 | TC-GS-PROFILE-E2E-041-product-selector-default-sesuai-app-asal | FE+BE |
| TC-GS-PROFILE-185 | TC-GS-PROFILE-E2E-041-product-selector-default-sesuai-app-asal | FE+BE |
| TC-GS-PROFILE-186 | TC-GS-PROFILE-E2E-042-product-selector-berganti-produk-in-page | FE+BE |
| TC-GS-PROFILE-187 | TC-GS-PROFILE-E2E-042-product-selector-berganti-produk-in-page | FE+BE |
| TC-GS-PROFILE-188 | TC-GS-PROFILE-E2E-033-resilience-halaman-dan-access-status | mock |
| TC-GS-PROFILE-189 | TC-GS-PROFILE-E2E-033-resilience-halaman-dan-access-status | mock |
| TC-GS-PROFILE-190 | TC-GS-PROFILE-E2E-043-access-status-per-role-global-settings | FE+BE |
| TC-GS-PROFILE-191 | TC-GS-PROFILE-E2E-043-access-status-per-role-global-settings | FE+BE |
| TC-GS-PROFILE-192 | TC-GS-PROFILE-E2E-043-access-status-per-role-global-settings | FE+BE |
| TC-GS-PROFILE-193 | TC-GS-PROFILE-E2E-043-access-status-per-role-global-settings | FE+BE |
| TC-GS-PROFILE-194 | TC-GS-PROFILE-E2E-044-access-status-konteks-produk | FE+BE |
| TC-GS-PROFILE-195 | TC-GS-PROFILE-E2E-044-access-status-konteks-produk | FE+BE |
| TC-GS-PROFILE-196 | TC-GS-PROFILE-E2E-044-access-status-konteks-produk | FE+BE |
| TC-GS-PROFILE-197 | TC-GS-PROFILE-E2E-044-access-status-konteks-produk | FE+BE |
| TC-GS-PROFILE-198 | TC-GS-PROFILE-E2E-044-access-status-konteks-produk | FE+BE |
| TC-GS-PROFILE-199 | TC-GS-PROFILE-E2E-042-product-selector-berganti-produk-in-page | FE+BE |
| TC-GS-PROFILE-200 | TC-GS-PROFILE-E2E-042-product-selector-berganti-produk-in-page | FE+BE |
| TC-GS-PROFILE-201 | TC-GS-PROFILE-E2E-045-product-selector-perubahan-app-access-dan-role-saat-halaman-terbuka | FE+BE |
| TC-GS-PROFILE-202 | TC-GS-PROFILE-E2E-045-product-selector-perubahan-app-access-dan-role-saat-halaman-terbuka | FE+BE |
| TC-GS-PROFILE-203 | TC-GS-PROFILE-E2E-045-product-selector-perubahan-app-access-dan-role-saat-halaman-terbuka | FE+BE |
| TC-GS-PROFILE-204 | TC-GS-PROFILE-E2E-066-defense-akses-lintas-user | FE+BE |
| TC-GS-PROFILE-205 | TC-GS-PROFILE-E2E-046-banner-pending-email-change-tampilan | FE+BE |
| TC-GS-PROFILE-206 | TC-GS-PROFILE-E2E-046-banner-pending-email-change-tampilan | FE+BE |
| TC-GS-PROFILE-207 | TC-GS-PROFILE-E2E-046-banner-pending-email-change-tampilan | FE+BE |
| TC-GS-PROFILE-208 | TC-GS-PROFILE-E2E-047-banner-pending-email-change-tanpa-permintaan-dan-admin | FE+BE |
| TC-GS-PROFILE-209 | TC-GS-PROFILE-E2E-064-realtime-banner-pending-email-change | FE+BE |
| TC-GS-PROFILE-210 | TC-GS-PROFILE-E2E-064-realtime-banner-pending-email-change | FE+BE |
| TC-GS-PROFILE-211 | TC-GS-PROFILE-E2E-046-banner-pending-email-change-tampilan | FE+BE |
| TC-GS-PROFILE-212 | TC-GS-PROFILE-E2E-048-banner-pending-email-change-tautan-kedaluwarsa | FE+BE |
| TC-GS-PROFILE-213 | TC-GS-PROFILE-E2E-048-banner-pending-email-change-tautan-kedaluwarsa | FE+BE |
| TC-GS-PROFILE-214 | TC-GS-PROFILE-E2E-048-banner-pending-email-change-tautan-kedaluwarsa | FE+BE |
| TC-GS-PROFILE-215 | TC-GS-PROFILE-E2E-048-banner-pending-email-change-tautan-kedaluwarsa | FE+BE |
| TC-GS-PROFILE-216 | TC-GS-PROFILE-E2E-046-banner-pending-email-change-tampilan | FE+BE |
| TC-GS-PROFILE-217 | TC-GS-PROFILE-E2E-056-sinkron-identitas-tag-dan-authenticator | FE+BE |
| TC-GS-PROFILE-218 | TC-GS-PROFILE-E2E-049-pencatatan-edit-dan-delete-photo | FE+BE |
| TC-GS-PROFILE-219 | TC-GS-PROFILE-E2E-049-pencatatan-edit-dan-delete-photo | FE+BE |
| TC-GS-PROFILE-220 | TC-GS-PROFILE-E2E-049-pencatatan-edit-dan-delete-photo | FE+BE |
| TC-GS-PROFILE-221 | TC-GS-PROFILE-E2E-049-pencatatan-edit-dan-delete-photo | FE+BE |
| TC-GS-PROFILE-222 | TC-GS-PROFILE-E2E-049-pencatatan-edit-dan-delete-photo | FE+BE |
| TC-GS-PROFILE-223 | TC-GS-PROFILE-E2E-049-pencatatan-edit-dan-delete-photo | FE+BE |
| TC-GS-PROFILE-224 | TC-GS-PROFILE-E2E-052-absence-log-aksi-foto-ditolak | FE+BE |
| TC-GS-PROFILE-225 | TC-GS-PROFILE-E2E-052-absence-log-aksi-foto-ditolak | FE+BE |
| TC-GS-PROFILE-226 | TC-GS-PROFILE-E2E-052-absence-log-aksi-foto-ditolak | FE+BE |
| TC-GS-PROFILE-227 | TC-GS-PROFILE-E2E-053-absence-log-lain | FE+BE |
| TC-GS-PROFILE-228 | TC-GS-PROFILE-E2E-050-pencatatan-change-password-dan-password-tidak-bocor | FE+BE |
| TC-GS-PROFILE-229 | TC-GS-PROFILE-E2E-062-multi-sesi-race-change-password-dan-user-log | FE+BE |
| TC-GS-PROFILE-230 | TC-GS-PROFILE-E2E-050-pencatatan-change-password-dan-password-tidak-bocor | FE+BE |
| TC-GS-PROFILE-231 | TC-GS-PROFILE-E2E-050-pencatatan-change-password-dan-password-tidak-bocor | FE+BE |
| TC-GS-PROFILE-232 | TC-GS-PROFILE-E2E-051-pencatatan-lock-change-password | FE+BE |
| TC-GS-PROFILE-233 | TC-GS-PROFILE-E2E-051-pencatatan-lock-change-password | FE+BE |
| TC-GS-PROFILE-234 | TC-GS-PROFILE-E2E-051-pencatatan-lock-change-password | FE+BE |
| TC-GS-PROFILE-235 | TC-GS-PROFILE-E2E-051-pencatatan-lock-change-password | FE+BE |
| TC-GS-PROFILE-236 | TC-GS-PROFILE-E2E-053-absence-log-lain | FE+BE |
| TC-GS-PROFILE-237 | TC-GS-PROFILE-E2E-053-absence-log-lain | FE+BE |
| TC-GS-PROFILE-238 | TC-GS-PROFILE-E2E-054-sinkron-foto-navbar-dan-user | FE+BE |
| TC-GS-PROFILE-239 | TC-GS-PROFILE-E2E-054-sinkron-foto-navbar-dan-user | FE+BE |
| TC-GS-PROFILE-240 | TC-GS-PROFILE-E2E-054-sinkron-foto-navbar-dan-user | FE+BE |
| TC-GS-PROFILE-241 | TC-GS-PROFILE-E2E-054-sinkron-foto-navbar-dan-user | FE+BE |
| TC-GS-PROFILE-242 | TC-GS-PROFILE-E2E-055-sinkron-foto-lintas-modul | FE+BE |
| TC-GS-PROFILE-243 | TC-GS-PROFILE-E2E-055-sinkron-foto-lintas-modul | FE+BE |
| TC-GS-PROFILE-244 | TC-GS-PROFILE-E2E-055-sinkron-foto-lintas-modul | FE+BE |
| TC-GS-PROFILE-245 | TC-GS-PROFILE-E2E-055-sinkron-foto-lintas-modul | FE+BE |
| TC-GS-PROFILE-246 | TC-GS-PROFILE-E2E-047-banner-pending-email-change-tanpa-permintaan-dan-admin | FE+BE |
| TC-GS-PROFILE-247 | TC-GS-PROFILE-E2E-024-change-password-counter-lintas-fitur | FE+BE |
| TC-GS-PROFILE-248 | TC-GS-PROFILE-E2E-024-change-password-counter-lintas-fitur | FE+BE |
| TC-GS-PROFILE-249 | TC-GS-PROFILE-E2E-061-multi-sesi-change-password-mengakhiri-sesi-lain | FE+BE |
| TC-GS-PROFILE-250 | TC-GS-PROFILE-E2E-065-biometric-dicabut-setelah-change-password | FE+BE |
| TC-GS-PROFILE-251 | TC-GS-PROFILE-E2E-028-change-password-lock-15-menit-toast-format-timezone | FE+BE |
| TC-GS-PROFILE-252 | TC-GS-PROFILE-E2E-060-storage-batas-kuota-ledger-dan-perubahan-kuota | FE+BE |
| TC-GS-PROFILE-253 | TC-GS-PROFILE-E2E-060-storage-batas-kuota-ledger-dan-perubahan-kuota | FE+BE |
| TC-GS-PROFILE-254 | TC-GS-PROFILE-E2E-057-sinkron-custom-field-siklus-hidup | FE+BE |
| TC-GS-PROFILE-255 | TC-GS-PROFILE-E2E-057-sinkron-custom-field-siklus-hidup | FE+BE |
| TC-GS-PROFILE-256 | TC-GS-PROFILE-E2E-057-sinkron-custom-field-siklus-hidup | FE+BE |
| TC-GS-PROFILE-257 | TC-GS-PROFILE-E2E-057-sinkron-custom-field-siklus-hidup | FE+BE |
| TC-GS-PROFILE-258 | TC-GS-PROFILE-E2E-058-sinkron-custom-field-tipe-nama-dan-dropdown | FE+BE |
| TC-GS-PROFILE-259 | TC-GS-PROFILE-E2E-057-sinkron-custom-field-siklus-hidup | FE+BE |
| TC-GS-PROFILE-260 | TC-GS-PROFILE-E2E-056-sinkron-identitas-tag-dan-authenticator | FE+BE |
| TC-GS-PROFILE-261 | TC-GS-PROFILE-E2E-056-sinkron-identitas-tag-dan-authenticator | FE+BE |
| TC-GS-PROFILE-262 | TC-GS-PROFILE-E2E-056-sinkron-identitas-tag-dan-authenticator | FE+BE |
| TC-GS-PROFILE-263 | TC-GS-PROFILE-E2E-056-sinkron-identitas-tag-dan-authenticator | FE+BE |
| TC-GS-PROFILE-264 | TC-GS-PROFILE-E2E-045-product-selector-perubahan-app-access-dan-role-saat-halaman-terbuka | FE+BE |
| TC-GS-PROFILE-265 | TC-GS-PROFILE-E2E-045-product-selector-perubahan-app-access-dan-role-saat-halaman-terbuka | FE+BE |
| TC-GS-PROFILE-266 | TC-GS-PROFILE-E2E-045-product-selector-perubahan-app-access-dan-role-saat-halaman-terbuka | FE+BE |
| TC-GS-PROFILE-267 | TC-GS-PROFILE-E2E-066-defense-akses-lintas-user | FE+BE |
| TC-GS-PROFILE-268 | TC-GS-PROFILE-E2E-066-defense-akses-lintas-user | FE+BE |
| TC-GS-PROFILE-269 | TC-GS-PROFILE-E2E-066-defense-akses-lintas-user | FE+BE |
| TC-GS-PROFILE-270 | TC-GS-PROFILE-E2E-066-defense-akses-lintas-user | FE+BE |
| TC-GS-PROFILE-271 | TC-GS-PROFILE-E2E-066-defense-akses-lintas-user | FE+BE |
| TC-GS-PROFILE-272 | TC-GS-PROFILE-E2E-066-defense-akses-lintas-user | FE+BE |
| TC-GS-PROFILE-273 | TC-GS-PROFILE-E2E-066-defense-akses-lintas-user | FE+BE |
| TC-GS-PROFILE-274 | TC-GS-PROFILE-E2E-066-defense-akses-lintas-user | FE+BE |
| TC-GS-PROFILE-275 | TC-GS-PROFILE-E2E-066-defense-akses-lintas-user | FE+BE |
| TC-GS-PROFILE-276 | TC-GS-PROFILE-E2E-066-defense-akses-lintas-user | FE+BE |
| TC-GS-PROFILE-277 | TC-GS-PROFILE-E2E-067-defense-payload-langsung-photo-dan-change-password | FE+BE |
| TC-GS-PROFILE-278 | TC-GS-PROFILE-E2E-067-defense-payload-langsung-photo-dan-change-password | FE+BE |
| TC-GS-PROFILE-279 | TC-GS-PROFILE-E2E-067-defense-payload-langsung-photo-dan-change-password | FE+BE |
| TC-GS-PROFILE-280 | TC-GS-PROFILE-E2E-067-defense-payload-langsung-photo-dan-change-password | FE+BE |
| TC-GS-PROFILE-281 | TC-GS-PROFILE-E2E-067-defense-payload-langsung-photo-dan-change-password | FE+BE |
| TC-GS-PROFILE-282 | TC-GS-PROFILE-E2E-050-pencatatan-change-password-dan-password-tidak-bocor | FE+BE |
| TC-GS-PROFILE-283 | TC-GS-PROFILE-E2E-059-storage-penuh-edit-photo-diblokir | FE+BE |
| TC-GS-PROFILE-284 | TC-GS-PROFILE-E2E-059-storage-penuh-edit-photo-diblokir | FE+BE |
| TC-GS-PROFILE-285 | TC-GS-PROFILE-E2E-059-storage-penuh-edit-photo-diblokir | FE+BE |
| TC-GS-PROFILE-286 | TC-GS-PROFILE-E2E-060-storage-batas-kuota-ledger-dan-perubahan-kuota | FE+BE |
| TC-GS-PROFILE-287 | TC-GS-PROFILE-E2E-060-storage-batas-kuota-ledger-dan-perubahan-kuota | FE+BE |
| TC-GS-PROFILE-288 | TC-GS-PROFILE-E2E-059-storage-penuh-edit-photo-diblokir | FE+BE |
| TC-GS-PROFILE-289 | TC-GS-PROFILE-E2E-059-storage-penuh-edit-photo-diblokir | FE+BE |
| TC-GS-PROFILE-290 | TC-GS-PROFILE-E2E-059-storage-penuh-edit-photo-diblokir | FE+BE |
| TC-GS-PROFILE-291 | TC-GS-PROFILE-E2E-060-storage-batas-kuota-ledger-dan-perubahan-kuota | FE+BE |
| TC-GS-PROFILE-292 | TC-GS-PROFILE-E2E-061-multi-sesi-change-password-mengakhiri-sesi-lain | FE+BE |
| TC-GS-PROFILE-293 | TC-GS-PROFILE-E2E-061-multi-sesi-change-password-mengakhiri-sesi-lain | FE+BE |
| TC-GS-PROFILE-294 | TC-GS-PROFILE-E2E-061-multi-sesi-change-password-mengakhiri-sesi-lain | FE+BE |
| TC-GS-PROFILE-295 | TC-GS-PROFILE-E2E-062-multi-sesi-race-change-password-dan-user-log | FE+BE |
| TC-GS-PROFILE-296 | TC-GS-PROFILE-E2E-062-multi-sesi-race-change-password-dan-user-log | FE+BE |
| TC-GS-PROFILE-297 | TC-GS-PROFILE-E2E-062-multi-sesi-race-change-password-dan-user-log | FE+BE |
| TC-GS-PROFILE-298 | TC-GS-PROFILE-E2E-035-resilience-kegagalan-transaksi-server | FE+BE |
| TC-GS-PROFILE-299 | TC-GS-PROFILE-E2E-035-resilience-kegagalan-transaksi-server | FE+BE |
| TC-GS-PROFILE-300 | TC-GS-PROFILE-E2E-035-resilience-kegagalan-transaksi-server | FE+BE |
| TC-GS-PROFILE-301 | TC-GS-PROFILE-E2E-063-multi-tab-edit-dan-delete-photo-bersamaan | FE+BE |
| TC-GS-PROFILE-302 | TC-GS-PROFILE-E2E-063-multi-tab-edit-dan-delete-photo-bersamaan | FE+BE |
| TC-GS-PROFILE-303 | TC-GS-PROFILE-E2E-068-state-tenant-plan-starter-dan-enterprise | FE+BE |
| TC-GS-PROFILE-304 | TC-GS-PROFILE-E2E-068-state-tenant-plan-starter-dan-enterprise | FE+BE |
| TC-GS-PROFILE-305 | TC-GS-PROFILE-E2E-033-resilience-halaman-dan-access-status | mock |
| TC-GS-PROFILE-306 | TC-GS-PROFILE-E2E-015-gate-akses-sesi-dan-pemilik-record | FE+BE |
| TC-GS-PROFILE-307 | TC-GS-PROFILE-E2E-023-change-password-berhasil-login-dan-reset-counter | FE+BE |
| TC-GS-PROFILE-308 | TC-GS-PROFILE-E2E-067-defense-payload-langsung-photo-dan-change-password | FE+BE |
| TC-GS-PROFILE-309 | TC-GS-PROFILE-E2E-027-change-password-guard-refresh-dan-pindah-menu | FE+BE |
| TC-GS-PROFILE-310 | TC-GS-PROFILE-E2E-033-resilience-halaman-dan-access-status | mock |
| TC-GS-PROFILE-311 | TC-GS-PROFILE-E2E-063-multi-tab-edit-dan-delete-photo-bersamaan | FE+BE |
| TC-GS-PROFILE-312 | TC-GS-PROFILE-E2E-055-sinkron-foto-lintas-modul | FE+BE |
| TC-GS-PROFILE-313 | TC-GS-PROFILE-E2E-008-aksesibilitas-keyboard-dan-aria | FE+BE |
| TC-GS-PROFILE-314 | TC-GS-PROFILE-E2E-038-edit-photo-ganti-resize-dan-toast | FE+BE |
| TC-GS-PROFILE-315 | TC-GS-PROFILE-E2E-021-change-password-penolakan-server-lanjutan | FE+BE |
| TC-GS-PROFILE-316 | TC-GS-PROFILE-E2E-016-change-password-layar-modal-dan-show-hide | FE+BE |
| TC-GS-PROFILE-317 | TC-GS-PROFILE-E2E-016-change-password-layar-modal-dan-show-hide | FE+BE |
| TC-GS-PROFILE-318 | TC-GS-PROFILE-E2E-008-aksesibilitas-keyboard-dan-aria | FE+BE |
| TC-GS-PROFILE-319 | TC-GS-PROFILE-E2E-058-sinkron-custom-field-tipe-nama-dan-dropdown | FE+BE |
| TC-GS-PROFILE-320 | TC-GS-PROFILE-E2E-058-sinkron-custom-field-tipe-nama-dan-dropdown | FE+BE |
| TC-GS-PROFILE-321 | TC-GS-PROFILE-E2E-058-sinkron-custom-field-tipe-nama-dan-dropdown | FE+BE |
| TC-GS-PROFILE-322 | TC-GS-PROFILE-E2E-069-state-tenant-client-suspended-dan-expired | FE+BE |
| TC-GS-PROFILE-323 | TC-GS-PROFILE-E2E-069-state-tenant-client-suspended-dan-expired | FE+BE |
| TC-GS-PROFILE-324 | TC-GS-PROFILE-E2E-069-state-tenant-client-suspended-dan-expired | FE+BE |
| TC-GS-PROFILE-325 | TC-GS-PROFILE-E2E-069-state-tenant-client-suspended-dan-expired | FE+BE |
| TC-GS-PROFILE-326 | TC-GS-PROFILE-E2E-029-change-password-lock-state-modal-dan-tooltip-save | FE+BE |
| TC-GS-PROFILE-327 | TC-GS-PROFILE-E2E-029-change-password-lock-state-modal-dan-tooltip-save | FE+BE |
