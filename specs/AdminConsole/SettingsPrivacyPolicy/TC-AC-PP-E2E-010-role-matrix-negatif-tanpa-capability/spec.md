---
id: TC-AC-PP-E2E-010-role-matrix-negatif-tanpa-capability
title: "Role Matrix Negatif: Principal Tanpa Capability Tidak Melihat Menu dan Akses Langsung Ditolak"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PP-12
  - TC-AC-PP-14
coverage:
  web: automated
---

# Role Matrix Negatif: Principal Tanpa Capability Tidak Melihat Menu dan Akses Langsung Ditolak

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-AC-PP-12, TC-AC-PP-14 | Tanpa Capability (user Principal, role tanpa "Manage privacy policy") | Hana Wibowo | `noCapabilityAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_NOCAP_PASSWORD` |

- Login akun Tanpa Capability dilakukan di hook `before` spec ini (kredensial dari env var di atas); hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Password tidak ditulis di spec atau fixture; nama env `AC_NOCAP_PASSWORD` dan `AC_TC_PASSWORD` perlu didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`; `AC_NOCAP_PASSWORD` belum terdaftar.
- Dataset Riwayat A (Version 3 Active, 3 baris) di-seed di hook `before` lewat Fixture BE (kemampuan teknis: membuat ulang dataset Riwayat; riwayat versi append-only sehingga tidak bisa dihapus lewat UI) dan dikembalikan ke Riwayat A di hook `after`. Spec tidak membuat atau mengubah versi.
- Suite berjalan serial (`parallel: false`) karena dokumen Privacy Policy bersifat tunggal platform-wide.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah).
- Fixture `fixtures/privacyPolicy.json` (belum ada, disiapkan tim FE):

| Kunci | Isi | Dipakai di |
|---|---|---|
| `urlHalamanPrivacyPolicy` | URL langsung halaman Settings > Privacy Policy | TC-AC-PP-14 (Data Uji) |
| `submenuSettingsDiizinkanTanpaCapability` | Daftar submenu Settings selain Privacy Policy yang diizinkan bagi role akun Tanpa Capability (nilai belum ditentukan TC; disiapkan tim FE dari konfigurasi role akun uji) | TC-AC-PP-12 (Expected b) |

## Test Steps

### TC-AC-PP-12: Item sidebar Privacy Policy Hidden untuk user Principal tanpa capability Manage privacy policy

1. Berada di halaman utama setelah login sebagai Tanpa Capability
2. Buka grup Settings pada sidebar
3. Amati daftar submenu
4. Verifikasi item "Privacy Policy" tidak tampil di grup Settings (Hidden, bukan disabled)
5. Verifikasi minimal satu submenu Settings lain yang diizinkan role tersebut (daftar `submenuSettingsDiizinkanTanpaCapability`) tetap tampil

### TC-AC-PP-14: Akses langsung ke URL halaman oleh user tanpa capability menampilkan toast penolakan standar tanpa redirect

6. Ketik URL halaman Settings > Privacy Policy (`urlHalamanPrivacyPolicy`) langsung di address bar lalu tekan Enter
7. Verifikasi toast error: "You don't have permission to do this."
8. Verifikasi tidak ada redirect ke halaman unauthorized terpisah
9. Verifikasi tidak ada baris Version History yang tampil

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix negatif (bagian 3a konvensi) untuk satu role. Role negatif lain (Distributor, Partner, Client) diuji di spec `TC-AC-PP-E2E-011-role-matrix-negatif-entity-gate`; Read Only di spec Role Matrix visibilitas elemen.
- Tidak ada langkah penghubung.
- Temuan untuk QA: TC-AC-PP-12 Expected b ("Submenu Settings lain yang diizinkan role tersebut tetap tampil") tidak menyebut submenu mana yang diizinkan untuk role Tanpa Capability; langkah 5 mengasersi bahwa minimal satu submenu Settings lain dari daftar fixture `submenuSettingsDiizinkanTanpaCapability` tampil; daftar pastinya disiapkan tim FE dari konfigurasi role akun uji (kebutuhan tercatat di Prerequisites). Post Condition kedua TC ("Tidak ada perubahan data") tidak punya langkah observasi sehingga tidak diasersi.
