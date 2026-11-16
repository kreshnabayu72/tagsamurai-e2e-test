---
id: TC-FA-PREF-E2E-042-save-ditolak-akun-inactive-setelah-d-01-terbuka-dan-akun-tersimpan-inactive
title: "Save ditolak akun Inactive setelah dialog D-01 terbuka; akun tersimpan Inactive tidak memblokir Save setting lain"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-218
  - TC-FA-PREF-556
sourceRules: ["D-01", "PV-01", "PV-02", "F-FAPREF-01.k4c", "V-04", "FAPREF-LOGIC-06h", "E-FAPREF-04", "F-FAPREF-04.k2a", "F-FAPREF-01.k22b", "T-01"]
smoke: []
dependsOn: []
trace:
  "D-01": 4
  "PV-01": 4
  "PV-02": 4
  "F-FAPREF-01.k4c": [7, 11, 12]
  "V-04": [8, 9]
  "FAPREF-LOGIC-06h": 11
  "E-FAPREF-04": 13
  "F-FAPREF-04.k2a": [19, 21]
  "F-FAPREF-01.k22b": 20
  "T-01": 20
coverage:
  web: automated
---

# Save ditolak akun Inactive setelah dialog D-01 terbuka; akun tersimpan Inactive tidak memblokir Save setting lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: seri PC (TC-FA-PREF-362-621), company `PT Contoh Konstruksi` plan Growth (PC-1): Preferences nilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, akun default kosong), periode Mar 2026 sampai Dec 2026 Open, belum ada posting penyusutan. Untuk TC-FA-PREF-556: Default Gain on Disposal tersimpan kosong; Asset Class IT Equipment dan Vehicles mengosongkan akun Gain; ada 3 pelepasan belum diposting (PC-1, PC-5, PC-6, PC-7).
- Data: seri PB (TC-FA-PREF-176-361) untuk TC-FA-PREF-218: Preferences nilai awal (PB-1) dengan Default Gain on Disposal tersimpan `4-9100 – Laba Pelepasan Aset` yang berstatus Inactive (PB-2); Asset Class IT Equipment, Vehicles, Furniture (PB-3).
- Seri fixture PA, PB, dan PC bernilai awal setara (PA-2, PB-1, PC-1); spec yang memuat TC dari lebih dari satu seri men-seed ulang lewat API di antara TC sesuai Precondition TC.
- Kemampuan teknis: sesi API Total Control (butir "Sesi API aktor" di `suite.md`): pelaku kedua yang hanya memicu perubahan state; token tidak dihitung sebagai sesi web. Dipakai untuk menonaktifkan akun `4-9100 – Laba Pelepasan Aset` pada TC-FA-PREF-556 sebagai pelaku kedua; hanya pemicu state.
- Kemampuan teknis: Baca state Preferences, periode akuntansi, dan akun Chart of Accounts di server (kemampuan baca state BE) disediakan tim FE/BE tanpa endpoint karangan; dipakai untuk Expected "tidak ada yang tersimpan".
- Seed dan pemulihan lewat API (Preferences ke nilai awal, plan, penguncian, versi Tax Depreciation Class, transaksi bertanggal, akun Chart of Accounts) disediakan tim FE/BE: butir "Seed dan pemulihan lewat API" di `suite.md`. Hook `after` spec ini memulihkan state server yang diubah spec ke nilai awal.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-556: Akun default menjadi Inactive setelah dialog Save Changes terbuka ditolak saat Save

1. Pilih "4-9100 – Laba Pelepasan Aset" pada Select Default Gain on Disposal
2. Ubah Default Capitalization Threshold menjadi "3000000"
3. Klik `[Save changes]`
4. Verifikasi dialog "Save Changes" (severity warning) tampil dengan daftar bullet: "2 asset classes use the default threshold."; "2 asset classes use the default account. 3 unposted disposals will use the new account.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` dan `[Save]`
5. Lewat sesi API Total Control, ubah status akun 4-9100 menjadi Inactive hingga tersimpan
6. Klik `[Save]` pada dialog "Save Changes"
7. Verifikasi dialog "Save Changes" tertutup
8. Verifikasi caption "This default gain on disposal no longer exists. Please select another." tampil pada field Default Gain on Disposal
9. Verifikasi field Default Gain on Disposal dikosongkan otomatis
10. Buka daftar opsi Select Default Gain on Disposal
11. Verifikasi opsi akun dimuat ulang tanpa 4-9100
12. Verifikasi Default Capitalization Threshold di form tetap Rp 3.000.000,00 sebagai perubahan yang belum disimpan
13. Verifikasi tidak ada yang tersimpan: Preferences tersimpan tidak berubah
14. Klik `[Cancel]`

### TC-FA-PREF-218: Akun tersimpan yang menjadi Inactive dan tetap sama tidak memblokir Save setting lain

15. Siapkan Preferences nilai awal PB-1 dengan Default Gain on Disposal tersimpan "4-9100 – Laba Pelepasan Aset" dan akun 4-9100 berstatus Inactive lewat seed API hingga tersimpan
16. Buka ulang Fixed Asset > Settings > Accounting > Preferences
17. Ubah Select In-service Date Source menjadi "Manual by Accounting"
18. Klik `[Save changes]`
19. Verifikasi tidak ada caption V-04 pada Select Default Gain on Disposal
20. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
21. Verifikasi Select Default Gain on Disposal tetap menampilkan "4-9100 – Laba Pelepasan Aset"

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): mengembalikan form dirty ke nilai tersimpan dengan `[Cancel]` (S-09): langkah 14; memulihkan state server lewat seed/API sebelum TC berikutnya: langkah 15; membuka ulang halaman Preferences agar form memuat nilai tersimpan: langkah 16.
- Urutan: TC-FA-PREF-556 (Save ditolak) lebih dulu, lalu TC-FA-PREF-218 (Save sukses) sesuai S-10. Seed TC-FA-PREF-218 memakai seri PB; nilai awal setara dengan PC-1 (SERI di Prerequisites).
- Temuan untuk QA:
  - TC-FA-PREF-556 meminta sesi B membuka Chart of Accounts lewat UI; spec memakai sesi API Total Control sebagai pemicu state sesuai keputusan pelaku kedua hanya sebagai pemicu. Email akun sesi B (PC-8) tidak tertulis di Pre-setup.
  - Data Pre-setup PB-2 mencatat `4-9100 – Laba Pelepasan Aset` sebagai Active, sedangkan Precondition d TC-FA-PREF-218 menyatakan akun itu tersimpan sebagai Default Gain dan berstatus Inactive; spec mengikuti Precondition TC dan men-seed keadaan itu.
  - TC-FA-PREF-218 tidak menyatakan apakah perubahan In-service Date Source memunculkan dialog Save Changes; spec mengikuti langkah TC (tanpa dialog).
  - Expected d TC-FA-PREF-556 ("opsi akun dimuat ulang tanpa 4-9100") dan Expected e ("tidak ada yang tersimpan"): spec membaca nilai tersimpan lewat kemampuan baca state BE.
  - Post Condition TC yang tidak punya langkah observasi di TC (nilai tersimpan, periode dibangun ulang, entri log) tidak diasersi; Post Condition "tidak ada entri log baru" dicatat sebagai rujukan ke spec absence (S-05) dan tidak diklaim teruji di spec ini.
