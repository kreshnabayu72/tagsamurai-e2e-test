---
id: TC-FA-LBL-E2E-173-absence-log-aksi-gagal-5xx-pada-edit-create-dan-delete
title: "Absence Log: Aksi Gagal 5xx pada Edit, Create, dan Delete"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-402
  - TC-FA-LBL-520
  - TC-FA-LBL-521
coverage:
  web: automated
---

# Absence Log: Aksi Gagal 5xx pada Edit, Create, dan Delete

## Prerequisites

- Mode: FE+BE. Backend nyata dengan `Spectra.intercept()` untuk memaksa respons 5xx pada Save (TC-FA-LBL-402), Create (TC-FA-LBL-520), dan Delete (TC-FA-LBL-521).
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, `Fixture.assetLabeling.akun.totalControl`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (nama bersuffix `{runId}-173`; label seed milik spec dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label):
  - `Log Edit 402 {runId}-173` (TC-FA-LBL-402); nama yang dicoba `Fail Log 402 {runId}-173` (tidak tersimpan)
  - `Fail Log 520 {runId}-173` (TC-FA-LBL-520; tidak tersimpan)
  - `Log Delete 521 {runId}-173` (TC-FA-LBL-521)
- Fixture `fixtures/asset-labeling.json` (disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |

- Kemampuan teknis: fixture BE untuk seeding dan membersihkan label serta membaca jumlah dan isi entri Changelog Labels, System Log aktor, dan Activity Log sebagai baseline (disediakan tim FE/BE; endpoint tidak ditulis di TC; S-12). Asersi "tidak ada entri" memakai selisih jumlah entri terhadap baseline per surface (bagian 8b butir 2, surface agregat) karena audit trail permanen tidak boleh diasersi sebagai angka absolut (S-12). `Spectra.intercept()` untuk memaksa respons 5xx (endpoint ditentukan tim FE; intercept dilepas segera sesudah pemicu selesai, S-09; hook `after` melepasnya bila spec gagal di tengah).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed dan label yang dibuat spec (nama bersuffix `{runId}-173`, termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh. Entri log bersifat permanen dan tidak dihapus.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-402: Edit yang gagal 5xx tidak menulis entri di Changelog

1. Catat baseline jumlah entri Changelog Labels lewat fixture BE
2. Ketik Search `Log Edit 402 {runId}-173`, tekan Enter
3. Klik `⋯` pada baris `Log Edit 402 {runId}-173`, lalu klik `Edit`
4. Ganti isi Label Name dengan `Fail Log 402 {runId}-173`
5. Paksa respons Save 5xx (`Spectra.intercept()`)
6. Klik `[Save]`
7. Verifikasi toast `Error, failed to update label.`
8. Lepas intercept
9. Klik `✕` pada header modal Edit Label
10. Verifikasi dialog `Unsaved Changes` tampil
11. Klik `[Leave]`
12. Verifikasi baris `Log Edit 402 {runId}-173` tampil dengan nama tidak berubah
13. Verifikasi jumlah entri Changelog Labels sama dengan baseline langkah 1 (fixture BE)

### TC-FA-LBL-520: Create yang gagal 5xx tidak menulis entri di ketiga surface log

14. Catat baseline jumlah entri Changelog Labels, System Log aktor, dan Activity Log lewat fixture BE
15. Klik `[+ Label]`
16. Isi Label Name `Fail Log 520 {runId}-173`
17. Paksa respons Create 5xx (`Spectra.intercept()`)
18. Klik `[Submit]`
19. Verifikasi toast `Error, failed to create label.`
20. Verifikasi modal Create Label tetap terbuka
21. Verifikasi Label Name `Fail Log 520 {runId}-173` dipertahankan
22. Verifikasi label `Fail Log 520 {runId}-173` tidak dibuat (fixture BE)
23. Lepas intercept
24. Klik `✕` pada header modal Create Label
25. Verifikasi dialog `Unsaved Changes` tampil
26. Klik `[Leave]`
27. Verifikasi jumlah entri Changelog Labels, System Log aktor, dan Activity Log sama dengan baseline langkah 14 (fixture BE)

### TC-FA-LBL-521: Delete yang gagal 5xx tidak menulis entri di ketiga surface log

28. Catat baseline jumlah entri Changelog Labels, System Log aktor, dan Activity Log lewat fixture BE
29. Ketik Search `Log Delete 521 {runId}-173`, tekan Enter
30. Klik `⋯` pada baris `Log Delete 521 {runId}-173`, lalu klik `Delete`
31. Paksa respons Delete 5xx (`Spectra.intercept()`)
32. Klik `[Delete]` pada dialog D-01
33. Verifikasi toast `Error, failed to delete label.`
34. Verifikasi dialog D-01 tetap terbuka
35. Verifikasi label `Log Delete 521 {runId}-173` tetap ada (fixture BE)
36. Lepas intercept
37. Klik `[Cancel]` pada dialog D-01
38. Verifikasi jumlah entri Changelog Labels, System Log aktor, dan Activity Log sama dengan baseline langkah 28 (fixture BE)

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 5 (Pencatatan Audit Log & Multi-Surface Sync) dan section yang memiliki TC pemicu. Subjudul `###` memetakan langkah ke TC granular.
- P-5 (butir a): spec ini adalah spec absence (kelas g). Pemicu yang bukan objek uji (respons 5xx) hanya membentuk kondisi yang diasersi tidak tercatat; tiap TC punya label dan baseline sendiri.
- Langkah penghubung (S-03): langkah menutup form dirty lewat `✕`, dialog `Unsaved Changes`, dan `[Leave]` (S-08), serta `[Cancel]` pada dialog D-01 supaya label tidak terhapus; Search untuk menemukan baris target (R-16).
- Baseline jumlah entri dibaca lewat fixture BE (TC-FA-LBL-520 dan 521 menyebut pembukaan ketiga surface log); selisih jumlah dipakai sebagai asersi "tidak ada entri". Toast error dan state modal atau dialog yang tetap terbuka menjadi anchor positif pemicu (bagian 8b butir 2).
- Spec ini di atas smell (38 langkah) karena langkah pencatatan baseline dan pembandingan jumlah entri log (pola baca-log berulang) dikecualikan menurut bagian 3 prinsip 13; selebihnya 32 langkah. Semua blok satu kelas (absence log atas aksi tulis yang gagal 5xx) dan berdiri sendiri.
- Temuan untuk QA:
  - TC-FA-LBL-402, 520, dan 521: Post Condition tidak ada. TC-FA-LBL-402 Expected a ("nama label tidak berubah") dan TC-FA-LBL-521 Expected a ("label tetap ada") tidak menyebut tempat pengamatan; spec memakai baris tabel dan fixture BE.
