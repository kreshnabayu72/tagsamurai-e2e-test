---
id: TC-FA-PREF-E2E-025-role-matrix-positif-save-cancel-view-history
title: "Role Matrix Positif: Read + Update Menjalankan Save dan Cancel, Read dan Read Only Membuka View History, Read Only Melihat Nilai Tanpa Masking"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-118
  - TC-FA-PREF-119
  - TC-FA-PREF-120
  - TC-FA-PREF-121
  - TC-FA-PREF-548
sourceRules: ["F-FAPREF-01.k22a", "F-FAPREF-01.k22b", "T-01", "F-FAPREF-01.k13", "ST-01", "F-FAPREF-02.k3a", "F-FAPREF-02.k3b", "F-FAPREF-02.k3d", "§5#b1", "L-02a", "SET-02", "FAPREF-LOGIC-03a", "SET-05", "§4.1.1#p4", "SET-08", "SET-09", "§9.11#b1"]
smoke: []
dependsOn: []
trace:
  "F-FAPREF-01.k22a": 3
  "F-FAPREF-01.k22b": 4
  "T-01": 4
  "F-FAPREF-01.k13": 5
  "ST-01": [6, 12]
  "F-FAPREF-02.k3a": 10
  "F-FAPREF-02.k3b": 11
  "F-FAPREF-02.k3d": 11
  "§5#b1": [17, 24]
  "L-02a": [18, 25]
  "SET-02": 28
  "FAPREF-LOGIC-03a": 28
  "SET-05": 29
  "§4.1.1#p4": [29, 30, 31]
  "SET-08": 30
  "SET-09": 31
  "§9.11#b1": 32
coverage:
  web: automated
---

# Role Matrix Positif: Read + Update Menjalankan Save dan Cancel, Read dan Read Only Membuka View History, Read Only Melihat Nilai Tanpa Masking

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

  | Role | Email Pre-setup | Env var password | TC |
  |---|---|---|---|
  | Manage accounting - Read + Update | `manageAccountingReadUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MARU_PASSWORD` | TC-FA-PREF-118, TC-FA-PREF-119 |
  | Manage accounting - Read | `manageAccountingRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAR_PASSWORD` | TC-FA-PREF-120 |
  | Read Only | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` | TC-FA-PREF-121, TC-FA-PREF-548 |

- Akun aktor pertama: Manage accounting - Read + Update. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun ke role berikutnya memakai langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Env var `FA_MARU_PASSWORD`, `FA_MAR_PASSWORD`, dan `FA_RO_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` (plan Growth) dengan Preferences nilai awal PA-2 (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, tidak terkunci, semua setting wajib terisi). Changelog Preferences terisi data contoh PA-17.
- Data untuk TC-FA-PREF-548 (Precondition TC: Default Capitalization Threshold 5.000.000, Default Gain on Disposal `4-9100 – Laba Pelepasan Aset`, Default Capitalization Offset `1-2900 – Biaya Dikapitalisasi`, Found Asset Credit Account `4-1500 – Pendapatan Lain-lain`; PC-1, PC-5) dibentuk lewat seed pada langkah 27. Nilai awal PA-2 dan PC-1 setara selain keempat nilai tersebut.
- State yang diubah spec: Preferences (In-service Date Source dan keempat nilai TC-FA-PREF-548). Dipulihkan ke PA-2 di hook `after` dan dengan langkah seed di antara TC. Changelog Preferences bertambah satu entri Edit dari TC-FA-PREF-118 (tidak dipulihkan; audit trail permanen).
- Kemampuan teknis: seed dan pemulihan Preferences lewat sesi API aktor (butir "Seed dan pemulihan lewat API" dan "Sesi API aktor" di `suite.md`), disediakan tim FE/BE.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-118: Manage accounting - Read + Update menyelesaikan Save changes

1. Ubah In-service Date Source menjadi "Manual by Accounting"
2. Klik `[Save changes]`
3. Verifikasi tidak ada dialog "Save Changes" (Save langsung berlanjut)
4. Verifikasi toast sukses "Success, accounting preferences have been saved."
5. Verifikasi form tetap terbuka dengan In-service Date Source bernilai tersimpan "Manual by Accounting"
6. Verifikasi `[Save changes]` dan `[Cancel]` Disabled

### TC-FA-PREF-119: Manage accounting - Read + Update menjalankan Cancel

7. Pulihkan Preferences ke nilai awal PA-2 lewat sesi API hingga tersimpan, lalu muat ulang halaman Preferences
8. Ubah In-service Date Source menjadi "Manual by Accounting"
9. Klik `[Cancel]`
10. Verifikasi In-service Date Source kembali "Activation date"
11. Verifikasi tidak ada dialog dan tidak ada toast
12. Verifikasi `[Save changes]` dan `[Cancel]` kembali Disabled

### TC-FA-PREF-120: Manage accounting - Read membuka View history

13. Logout dari akun Manage accounting - Read + Update
14. Login sebagai Manage accounting - Read (`manageAccountingRead_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_MAR_PASSWORD`)
15. Buka Fixed Asset > Settings > Accounting > Preferences
16. Klik ikon View history
17. Verifikasi modal Changelog dengan judul "Changelog: Preferences" terbuka
18. Verifikasi modal menampilkan sedikitnya satu entri Changelog
19. Tutup modal Changelog

### TC-FA-PREF-121: Read Only membuka View history

20. Logout dari akun Manage accounting - Read
21. Login sebagai Read Only (`readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_RO_PASSWORD`)
22. Buka Fixed Asset > Settings > Accounting > Preferences
23. Klik ikon View history
24. Verifikasi modal Changelog dengan judul "Changelog: Preferences" terbuka
25. Verifikasi modal menampilkan sedikitnya satu entri Changelog
26. Tutup modal Changelog

### TC-FA-PREF-548: Read Only melihat seluruh nilai Preferences tanpa masking

27. Ubah Preferences lewat sesi API sesuai Precondition TC-FA-PREF-548 (Default Capitalization Threshold 5.000.000, Default Gain on Disposal `4-9100 – Laba Pelepasan Aset`, Default Capitalization Offset `1-2900 – Biaya Dikapitalisasi`, Found Asset Credit Account `4-1500 – Pendapatan Lain-lain`) hingga tersimpan, lalu muat ulang halaman Preferences
28. Verifikasi Default Capitalization Threshold tampil Rp 5.000.000,00
29. Verifikasi Default Gain on Disposal tampil 4-9100 – Laba Pelepasan Aset
30. Verifikasi Default Capitalization Offset tampil 1-2900 – Biaya Dikapitalisasi
31. Verifikasi Found Asset Credit Account tampil 4-1500 – Pendapatan Lain-lain
32. Verifikasi tidak ada nilai yang disamarkan

## Notes

- Role Matrix positif (bagian 3a): spec polaritas seragam (aksi berhasil) dan memuat beberapa aksi (Save, Cancel, View history, pembacaan nilai); satu spec per aksi tidak dipakai karena tiap aksi hanya 1 sampai 2 TC. Ditulis per blok role karena ganti akun menuntut langkah eksplisit (akun pertama login di hook `before`); langkah tiap role tidak identik (Save, Cancel dan View history, pembacaan nilai).
- Langkah TC "Buka Tab Preferences" pada TC-FA-PREF-118, 119, 120, 121, dan 548 dipenuhi hook `beforeEach` suite (layar awal) atau langkah buka Preferences setelah ganti akun (S-03).
- Langkah penghubung (S-03): langkah 7 (pemulihan Preferences lewat seed), 13 sampai 15, 19, 20 sampai 22, 26 (ganti akun dan tutup modal), 27 (seed precondition TC-FA-PREF-548).
- Seri fixture: TC-FA-PREF-118 sampai 121 memakai PA, TC-FA-PREF-548 memakai PC; nilai awal PA-2 dan PC-1 setara, sehingga satu company dipakai (langkah 27 membentuk perbedaan nilai TC-FA-PREF-548).
- Temuan untuk QA:
  - Post Condition TC-FA-PREF-118 (In-service Date Source tersimpan; entri Changelog baru untuk In-service Date Source) dan Post Condition TC-FA-PREF-119 (tidak ada perubahan data tersimpan; tidak ada entri log baru) tidak punya langkah observasi di TC, sehingga tidak diasersi (S-01). Entri Changelog baru Data Dinamis DA-3 untuk TC-FA-PREF-118 dicatat tetapi tidak diverifikasi.
  - Expected TC-FA-PREF-120 dan 121 ("menampilkan entri Changelog") tanpa jumlah; Precondition menyebut data contoh PA-17, tetapi audit trail permanen tidak boleh diasersi sebagai angka absolut (S-12), sehingga diasersi "sedikitnya satu entri".
  - Email akun tidak ditulis utuh di TC (`{namaCompany}`); nama company tiap akun perlu dikonfirmasi tim FE.
