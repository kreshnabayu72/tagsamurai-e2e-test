---
id: TC-GS-GSET-E2E-025-multi-konteks-kebijakan-satu-sesi-web
title: "Multi-Konteks: Session Idle Timeout Tidak Mengubah Kebijakan Satu Sesi Web per Akun"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-GSET-59
coverage:
  web: automated
---

# Multi-Konteks: Session Idle Timeout Tidak Mengubah Kebijakan Satu Sesi Web per Akun

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1); kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini sebagai sesi web 1 (browser 1). Browser 2 adalah konteks browser kedua yang dibuka di langkah 2 dan memakai akun yang sama untuk sesi web 2. Halaman awal browser 1: Global Settings > General Settings (dibuka hook `beforeEach` suite).
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_gs-general-settings`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Kemampuan teknis (TC-GS-GSET-59 berstatus Manual Only di TC; disediakan tim FE):
  - Dua konteks browser terpisah yang tidak berbagi cookie, masing-masing login akun yang sama (kelas multi-konteks).
  - Klien HTTP dengan token sesi browser 1 (token sesi aktor, Tabel Data Uji Pre-setup baris 9; tidak membuka sesi web baru sehingga kebijakan satu sesi web tidak terpengaruh) untuk PUT `/v2/enterprise-management/general-settings` dengan payload `currencyCode` `IDR`, `timezone` `Asia/Jakarta`, `dateFormat` `dd/MM/yy`, `timeFormat` `HH:mm`, `sessionIdleTimeout` `60`.
- Record General Settings Client A: Session Idle Timeout `1 hour` (precondition TC; disimpan lewat PUT API di langkah 1, dipakai sebagai precondition TC, tidak diasersi). Hook `after` suite memulihkan baseline Pre-setup No 10 (`IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`).
- State global: kebijakan sesi web berjalan per akun; spec ini mengakhiri sesi web 1 milik akun default suite. Suite berjalan serial (`parallel: false`, lihat `suite.md`). Hook `after` spec ini menutup konteks browser kedua, menghapus sesi login browser 2 (bila masih ada), dan login ulang akun default suite supaya spec berikutnya memulai dari sesi aktif.
- TC-GS-GSET-59: login sebagai Total Control (Budi Santoso) dan berada di Global Settings > General Settings; Session Idle Timeout tersimpan `1 hour`.

## Test Steps

### TC-GS-GSET-59: Satu sesi web aktif per akun, tidak dipengaruhi Session Idle Timeout

1. Simpan Session Idle Timeout `1 hour` lewat PUT API (dipakai sebagai precondition TC, tidak diasersi)
2. Buka browser 2 (konteks browser baru tanpa cookie browser 1)
3. Di browser 2, login sebagai Budi Santoso (`Spectra.env.GS_TC_PASSWORD`, sesi web 2) dan pilih `Confirm` pada Dialog Confirmation Duplicate Login Attempt
4. Kembali ke browser 1 dan klik menu Global Settings > General Settings
5. Verifikasi Dialog Logged Out muncul di browser 1 (sesi web 1 ter-logout, maksimal 1 sesi web aktif)
6. Di browser 2, klik menu Global Settings > General Settings
7. Verifikasi jumlah sesi web aktif tetap 1: sesi web 2 aktif dan halaman General Settings tampil di browser 2
8. Tutup konteks browser 2 dan hapus sesi login browser 2

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. Mode: FE+BE. Kelas multi-konteks (prinsip 13c): dua browser untuk satu akun.
- TC-GS-GSET-59 berstatus Manual Only di TC; tetap spec dengan kebutuhan dua browser di Prerequisites (konvensi bagian 2).
- Pemetaan Expected TC-GS-GSET-59 (satu butir, dua klausa): "sesi web 1 ter-logout dan Dialog Logged Out muncul di browser 1" ke langkah 5 (aksi pemicu di langkah 4; `Confirm` Dialog Confirmation Duplicate Login Attempt di langkah 3, `auth-foundation.md` §6); "nilai Session Idle Timeout tidak mengubah jumlah sesi yang diizinkan" ke langkah 7 (sesi web 2 menjadi satu-satunya sesi web aktif).
- Langkah penghubung: langkah 1 (precondition `1 hour`, tidak diasersi); langkah 6 (aksi di browser 2 untuk mengamati sesi web 2 pada langkah 7); langkah 8 (menutup konteks kedua dan menghapus sesi login browser 2, S-09).
- Temuan untuk QA:
  - TC-GS-GSET-59: nilai "Session Idle Timeout `1 hour`" disimpan di precondition tanpa menyebut aktor penyimpannya; spec menyimpannya lewat PUT API (langkah 1).
