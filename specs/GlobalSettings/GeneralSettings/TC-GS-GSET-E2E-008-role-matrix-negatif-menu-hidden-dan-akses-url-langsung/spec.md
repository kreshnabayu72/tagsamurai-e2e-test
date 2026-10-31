---
id: TC-GS-GSET-E2E-008-role-matrix-negatif-menu-hidden-dan-akses-url-langsung
title: "Role Matrix negatif"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-24
  - TC-GS-GSET-25
  - TC-GS-GSET-26
  - TC-GS-GSET-27
coverage:
  web: automated
---

# Role Matrix negatif

## Prerequisites

- Mode: FE+BE.
- Hook suite (`suite.md`): login akun aktor pertama dan pemulihan record Client A ke baseline. Spec ini mengecualikan pembukaan halaman General Settings di `beforeEach`: user berada di Global Settings (precondition TC) karena kedua role tidak berhak membuka General Settings. Flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` disetel seen untuk kedua akun oleh hook suite dan dipulihkan di `after`.
- Role yang diuji (Tabel Data Uji Pre-setup; langkah identik per role, dipenuhi dua blok yang masing-masing diawali login role itu):

| Blok | TC | Role | Pre-setup | Email | Env var password |
|---|---|---|---|---|---|
| 1 | TC-GS-GSET-24, TC-GS-GSET-26 | System Role (tanpa Total Control/Read Only) | No 5 | `noCapabilityGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_GSET_SR_PASSWORD` |
| 2 | TC-GS-GSET-25, TC-GS-GSET-27 | Capability Individual (tanpa Total Control/Read Only) | No 4 | `manageUserRoleRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_GSET_CI_PASSWORD` |

- Login System Role di hook `before`; ganti akun ke Capability Individual lewat langkah eksplisit (langkah 7 sampai 9); hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Nama env `GS_GSET_SR_PASSWORD` dan `GS_GSET_CI_PASSWORD` baru dan belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftaran di tahap script. Email kedua akun ditulis menurut Pre-setup TC; `GS_NOCAP_PASSWORD` yang sudah ada di `.env.example` merujuk akun `noCapability_automated_qaTeam1@qwertysystem.net` (suite lain), bukan akun SR Pre-setup No 5, sehingga tidak dipakai (lihat Temuan untuk QA).
- URL halaman General Settings (Data Uji Langkah TC-GS-GSET-26 dan 27) dibaca dari `Fixture.generalSettings.pageUrl` (berkas `fixtures/generalSettings.json` belum ada, ditandai untuk tahap script).
- Kemampuan teknis: navigasi langsung ke URL lewat address bar.
- Tidak membuat data dan tidak mengubah state global.

## Test Steps

### Blok 1: System Role

#### TC-GS-GSET-24: Menu General Settings Hidden

1. Verifikasi sedikitnya satu item menu lain pada sidebar Global Settings tampil
2. Verifikasi menu General Settings Hidden (tidak muncul di sidebar)

#### TC-GS-GSET-26: Membuka URL langsung

3. Ketik URL halaman General Settings langsung di address bar, tekan Enter
4. Verifikasi toast error "You don't have permission to do this."
5. Verifikasi elemen halaman General Settings tidak ditampilkan
6. Verifikasi tidak ada redirect ke halaman unauthorized terpisah

### Ganti akun ke Capability Individual

7. Klik menu profil lalu Logout dari akun System Role
8. Tunggu aksi selesai (halaman Login tampil)
9. Login sebagai Capability Individual (`Spectra.env.GS_GSET_CI_PASSWORD`)
10. Buka Global Settings

### Blok 2: Capability Individual

#### TC-GS-GSET-25: Menu General Settings Hidden

11. Verifikasi sedikitnya satu item menu lain pada sidebar Global Settings tampil
12. Verifikasi menu General Settings Hidden (tidak muncul di sidebar)

#### TC-GS-GSET-27: Membuka URL langsung

13. Ketik URL halaman General Settings langsung di address bar, tekan Enter
14. Verifikasi toast error "You don't have permission to do this."
15. Verifikasi elemen halaman General Settings tidak ditampilkan
16. Verifikasi tidak ada redirect ke halaman unauthorized terpisah

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. Spec Role Matrix negatif (bagian 3a): langkah dua role identik tetapi ditulis per blok (bukan perulangan) karena role pertama sudah login di hook `before` dan role kedua butuh Step ganti akun eksplisit; 16 langkah.
- Urutan TC di dalam blok: TC-GS-GSET-24 sebelum TC-GS-GSET-26 dan TC-GS-GSET-25 sebelum TC-GS-GSET-27 (sidebar diamati sebelum navigasi URL langsung yang memunculkan toast 403).
- Langkah penghubung (tanpa `Verifikasi`): langkah 7, 8, dan 9 (ganti akun; langkah 8 mengikuti butir 8 bagian 8b) dan langkah 10 (membuka Global Settings sebagai halaman awal blok 2, precondition TC-GS-GSET-25 dan 27).
- Asersi absence langkah 2, 5, 12, dan 15 didahului asersi positif pada permukaan yang sama: item menu lain tampil (langkah 1 dan 11) dan toast penolakan tampil (langkah 4 dan 14).
- "Tidak ada redirect" (langkah 6 dan 16) diasersi lewat URL tetap pada halaman General Settings yang diketik dan tidak berada di halaman unauthorized.
- Temuan untuk QA:
  - TC-GS-GSET-26 dan 27 Expected menyatakan "elemen halaman tidak ditampilkan" tanpa menyebut apa yang tampil sebagai gantinya selain toast 403; spec mengasersi toast, ketiadaan elemen form, dan ketiadaan redirect sesuai TC.
  - Penamaan env var `GS_GSET_SR_PASSWORD` dan `GS_GSET_CI_PASSWORD` baru; `GS_NOCAP_PASSWORD` di `.env.example` merujuk akun `noCapability_automated_qaTeam1` yang berbeda dari email SR Pre-setup No 5 (`noCapabilityGlobalSettings_automated_{namaCompany}`), sehingga tidak dipakai.
