---
id: TC-FA-LBL-E2E-138-resilience-delete-dan-bulk-delete-5xx-dan-timeout-di-tengah-proses-bagian-2-2
title: "Resilience Delete dan Bulk Delete: 5xx dan Timeout di Tengah Proses (Bagian 2/2)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LBL-201
  - TC-FA-LBL-202
coverage:
  web: automated
---

# Resilience Delete dan Bulk Delete: 5xx dan Timeout di Tengah Proses (Bagian 2/2)

## Prerequisites

- Mode: FE+BE. Backend nyata dengan `Spectra.intercept()` untuk memaksa timeout dan respons 5xx per item pada Bulk Delete; asersi atas state tabel yang di-refresh dari backend.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, `Fixture.assetLabeling.akun.totalControl`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label bersih milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-138`):
  - `Mid A 201 {runId}-138`, `Mid B 201 {runId}-138`, `Mid C 201 {runId}-138` (TC-FA-LBL-201; urutan seleksi A, B, C)
  - `Bulk Clean A 202 {runId}-138` dan `Bulk Clean B 202 {runId}-138` (TC-FA-LBL-202)
- Fixture `fixtures/asset-labeling.json` (disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |

- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 5xx atau timeout (endpoint ditentukan tim FE dan tidak ditulis di TC); intercept dilepas segera sesudah pemicu selesai (S-09) dan hook `after` melepasnya bila spec gagal di tengah. Intercept per item untuk Bulk Delete: respons item yang dituju dipaksa gagal sedangkan item lain tidak dipengaruhi. Fixture BE untuk seeding dan membersihkan label.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed dan label yang dibuat spec (nama bersuffix `{runId}-138`, termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh. Entri log bersifat permanen dan tidak dihapus.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-201: Bulk Delete timeout di tengah proses memakai toast koneksi, dialog tertutup, bar dan seleksi dipertahankan

1. Ketik Search `201 {runId}-138`, tekan Enter
2. Centang baris `Mid A 201 {runId}-138`
3. Centang baris `Mid B 201 {runId}-138`
4. Centang baris `Mid C 201 {runId}-138`
5. Klik `Bulk Action` lalu klik `Delete`
6. Paksa timeout untuk item kedua (`Spectra.intercept()`)
7. Klik `[Delete]` pada dialog D-03
8. Verifikasi toast error `Connection problem. Please try again.`
9. Verifikasi Bulk Action Bar tetap tampil
10. Verifikasi seleksi dipertahankan (tidak di-reset ke 0)
11. Verifikasi tabel di-refresh sehingga menampilkan keadaan nyata (hasil per item tidak diasersi)
12. Verifikasi dialog D-03 tertutup
13. Lepas intercept
14. Klik `Unselect All` untuk menghapus seleksi

### TC-FA-LBL-202: Bulk Delete gagal 5xx pada item pertama: dialog tertutup, bar dan seleksi dipertahankan, tabel di-refresh

15. Tutup toast error sebelumnya
16. Ganti isi kotak search dengan `202 {runId}-138`, tekan Enter
17. Centang baris `Bulk Clean A 202 {runId}-138`
18. Centang baris `Bulk Clean B 202 {runId}-138`
19. Klik `Bulk Action` lalu klik `Delete`
20. Paksa respons 5xx untuk item pertama (`Spectra.intercept()`)
21. Klik `[Delete]` pada dialog D-03
22. Verifikasi toast error `Error, failed to delete label.`
23. Verifikasi Bulk Action Bar tetap tampil
24. Verifikasi seleksi dipertahankan (tidak di-reset ke 0)
25. Verifikasi tabel di-refresh sehingga menampilkan keadaan nyata (hasil per item tidak diasersi)
26. Verifikasi dialog D-03 tertutup
27. Lepas intercept
28. Klik `Unselect All` untuk menghapus seleksi

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 3d (Bulk Delete Label). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): Search untuk menemukan baris label target (Search `201 {runId}-138` dan `202 {runId}-138` menampilkan label yang berbagi potongan nama); menutup toast error sebelumnya (R-12); melepas intercept (S-09); `Unselect All` supaya seleksi tidak bocor ke TC berikutnya (S-09).
- Pembagian TC lintas spec: TC-FA-LBL-170, 171, dan 200 ada di spec 137.
- Temuan untuk QA:
  - TC-FA-LBL-201 dan 202: Post Condition tidak ada. TC-FA-LBL-201 tidak menyebut berapa lama timeout; spec memakai `Spectra.intercept()` untuk simulasi timeout (disediakan tim FE).
  - Expected c TC-FA-LBL-201 dan 202 ("tabel di-refresh") tidak memberi tanda yang teramati; spec mengasersinya sebagai tabel memuat ulang data dari server (list di-fetch ulang) dan mekanisme pengamatannya disediakan tim FE.
