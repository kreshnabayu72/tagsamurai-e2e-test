---
id: TC-GS-ROLE-E2E-016-role-matrix-negatif-direct-url-tanpa-role-manage-user-and-role
title: "Role Matrix Negatif: Akses Langsung URL Role & Permission Tanpa Role Manage user and role"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-35
coverage:
  web: automated
---

# Role Matrix Negatif: Akses Langsung URL Role & Permission Tanpa Role Manage user and role

## Prerequisites

- Mode: FE+BE.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk akun Yusuf Hidayat.

Role yang diuji (Tabel Data Uji Pre-setup #8):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-ROLE-35 | Manage TAG Read saja (tanpa Manage user and role) | Yusuf Hidayat | `manageTagRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_ROLE_MANAGETAG_READ_PASSWORD` (env baru) |

- Login Yusuf Hidayat dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture; env baru `GS_ROLE_MANAGETAG_READ_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data: memakai data Pre-setup (Pre-setup #8); spec tidak membuat, mengubah, atau menghapus data.
- Kemampuan teknis: mengetik URL di address bar browser (navigasi browser, bukan request HTTP langsung); URL halaman Role & Permission > Tab Total Control dan URL Detail "Manage TAG" disediakan tim FE.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-ROLE-35: Akses langsung URL tanpa role Manage user and role

1. Ketik URL halaman Role & Permission > Tab Total Control di address bar
2. Verifikasi toast error "You don't have permission to do this."
3. Verifikasi data tabel Role & Permission tidak ditampilkan
4. Verifikasi tidak ada redirect ke halaman unauthorized terpisah
5. Tutup toast error
6. Ketik URL Detail "Manage TAG" di address bar
7. Verifikasi toast error "You don't have permission to do this."
8. Verifikasi data tabel Role & Permission tidak ditampilkan
9. Verifikasi tidak ada redirect ke halaman unauthorized terpisah

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Spec Role Matrix negatif (bagian 3a konvensi) dengan satu role; tabel "Role yang diuji" dipertahankan agar akun dan env password tercatat.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 5 (tutup toast error sebelum toast berikutnya diasersi).
- Langkah 2 dan 7 (toast error) menjadi anchor positif bahwa respons penolakan sudah diterima sebelum asersi absence data tabel pada langkah 3 dan 8.
- Navigasi lewat address bar adalah jalur browser, sehingga perilaku FE (toast, tabel tidak tampil, tanpa redirect) diasersi sesuai Expected TC. Request langsung ke server (403) tanpa FE bukan objek spec ini.
- Layar awal spec (Global Settings, sebelum URL diketik) dibuka di hook `beforeEach`.
- Temuan untuk QA:
  - TC-GS-ROLE-35 tidak memberi URL literal dan tidak menyatakan layar tujuan akhir setelah penolakan (halaman yang tampil di balik toast); spec hanya mengasersi toast, tabel tidak tampil, dan tidak ada redirect ke halaman unauthorized terpisah.
