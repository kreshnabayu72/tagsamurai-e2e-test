---
id: TC-FA-PREF-E2E-052-shortcut-create-account-gain-loss-dan-akun-sama-pada-gain-dan-loss
title: "Select akun Default Gain dan Loss: akun sama dapat dipilih pada Gain dan Loss, serta shortcut + Create account membuat akun baru yang langsung terpilih"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-168
  - TC-FA-PREF-169
  - TC-FA-PREF-175
coverage:
  web: automated
---

# Select akun Default Gain dan Loss: akun sama dapat dipilih pada Gain dan Loss, serta shortcut + Create account membuat akun baru yang langsung terpilih

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: seri PA (TC-FA-PREF-1-175), company `PT Contoh Konstruksi` plan Growth (PA-1): Preferences nilai awal PA-2 (tidak terkunci, semua setting wajib terisi; Default Gain, Loss, Capitalization Offset, Found Asset Credit Account kosong); Chart of Accounts PA-3 (Active: 1-1001 Kas Utama, 1-2900 Biaya Dikapitalisasi, 4-1500 Pendapatan Lain-lain, 4-7002 Gain and Loss on Disposal, 4-9100 Laba Pelepasan Aset, 5-9100 Rugi Pelepasan Aset; Inactive: 4-9200, 5-9200, 1-2950, 4-1600).
- Data Dinamis TC-FA-PREF-168 dan 169 (DA-1): akun baru Account Code `4-9400` dan Account Name `Laba Selisih Pelepasan {runId}-052` (nama bersuffix per run, S-12). Kode `4-9400` literal dibersihkan di hook `before` (R-13) dan akun yang dibuat spec dihapus di hook `after`, keduanya lewat fixture BE yang disediakan tim FE/BE.
- State yang diubah spec: akun `4-9400` di Chart of Accounts (dibuat dan dihapus di dalam spec); Preferences tidak disimpan (form dikembalikan dengan `[Cancel]`). Hook `after` memulihkan Preferences ke PA-2.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, plan, penguncian, versi Tax Depreciation Class, transaksi bertanggal, akun Chart of Accounts) disediakan tim FE/BE: butir "Seed dan pemulihan lewat API" di `suite.md`.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-175: Akun yang sama dapat dipilih sebagai Default Gain dan Default Loss on Disposal

1. Pilih "4-7002 – Gain and Loss on Disposal" pada Select Default Gain on Disposal
2. Pilih "4-7002 – Gain and Loss on Disposal" pada Select Default Loss on Disposal
3. Verifikasi Select Default Gain on Disposal menampilkan "4-7002 – Gain and Loss on Disposal"
4. Verifikasi Select Default Loss on Disposal menampilkan "4-7002 – Gain and Loss on Disposal"
5. Verifikasi tidak ada caption pada Select Default Gain on Disposal
6. Verifikasi tidak ada caption pada Select Default Loss on Disposal
7. Verifikasi `[Save changes]` Enabled
8. Klik `[Cancel]`

### TC-FA-PREF-168: Shortcut + Create account pada Select Default Gain on Disposal membuka modal Add Account dan akun baru langsung terpilih

9. Klik `+ Create account` pada Select Default Gain on Disposal
10. Verifikasi modal Add Account di Chart of Accounts terbuka
11. Verifikasi field Function pada modal Add Account sudah terisi "Gain on Disposal"
12. Lengkapi modal Add Account dengan Account Code "4-9400" dan Account Name "Laba Selisih Pelepasan {runId}-052" lalu simpan
13. Verifikasi modal Add Account tertutup
14. Verifikasi Select Default Gain on Disposal langsung terpilih "4-9400 – Laba Selisih Pelepasan {runId}-052"
15. Buka daftar opsi Select Default Gain on Disposal
16. Verifikasi daftar opsi Select Default Gain on Disposal memuat "4-9400 – Laba Selisih Pelepasan {runId}-052"
17. Tutup daftar opsi Select Default Gain on Disposal
18. Klik `[Cancel]`

### TC-FA-PREF-169: Shortcut + Create account pada Select Default Loss on Disposal membuka modal Add Account dan akun baru langsung terpilih

19. Hapus akun "4-9400 – Laba Selisih Pelepasan {runId}-052" lewat fixture BE hingga terhapus
20. Buka ulang Fixed Asset > Settings > Accounting > Preferences
21. Klik `+ Create account` pada Select Default Loss on Disposal
22. Verifikasi modal Add Account di Chart of Accounts terbuka
23. Verifikasi field Function pada modal Add Account sudah terisi "Loss on Disposal"
24. Lengkapi modal Add Account dengan Account Code "4-9400" dan Account Name "Laba Selisih Pelepasan {runId}-052" lalu simpan
25. Verifikasi modal Add Account tertutup
26. Verifikasi Select Default Loss on Disposal langsung terpilih "4-9400 – Laba Selisih Pelepasan {runId}-052"
27. Buka daftar opsi Select Default Loss on Disposal
28. Verifikasi daftar opsi Select Default Loss on Disposal memuat "4-9400 – Laba Selisih Pelepasan {runId}-052"
29. Tutup daftar opsi Select Default Loss on Disposal
30. Klik `[Cancel]`

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Urutan blok: TC-FA-PREF-175 (tidak menyimpan, tidak membuat data) lebih dulu, lalu TC-FA-PREF-168 dan 169 yang membuat akun (S-10). Langkah 1 TC ("Buka Tab Preferences") dijalankan hook `beforeEach` suite.
- Langkah penghubung (S-03): mengembalikan form dirty ke nilai tersimpan dengan `[Cancel]` (S-09): langkah 8, 18, 30; menutup daftar opsi: langkah 17, 29; menghapus akun yang dibuat blok sebelumnya lewat fixture BE dan membuka ulang halaman agar kode `4-9400` bebas: langkah 19, 20.
- Penamaan akun: TC memakai Account Name "Laba Selisih Pelepasan" tanpa suffix; spec menambah suffix `{runId}-052` (S-12) dan membersihkan kode `4-9400` di hook `before` (R-13).
- Post Condition TC-FA-PREF-168 dan 169 ("Akun 4-9400 tersimpan di Chart of Accounts") tidak punya langkah observasi di TC dan terlihat tidak langsung lewat langkah 14, 16, 26, 28 (akun muncul di opsi Select); tidak ada asersi tambahan atas Chart of Accounts.
- Temuan untuk QA:
  - TC-FA-PREF-168 dan 169 memakai Account Code dan Account Name yang sama ("4-9400", "Laba Selisih Pelepasan") sehingga TC kedua hanya dapat berjalan bila akun TC pertama dihapus atau diganti; TC tidak memuat langkah pembersihan. Spec menghapus akun lewat fixture BE di antara blok.
  - Expected TC-FA-PREF-168 dan 169 butir b tidak menyebut apakah form Preferences menjadi dirty setelah akun dipilih otomatis; spec mengembalikan form dengan `[Cancel]` tanpa mengasersi status tombol.
  - TC-FA-PREF-175 butir c "[Save changes] Enabled" tidak menyebut apakah `[Cancel]` ikut Enabled; tidak diasersi.
  - Post Condition TC yang tidak punya langkah observasi di TC (nilai tersimpan, entri log) tidak diasersi.
