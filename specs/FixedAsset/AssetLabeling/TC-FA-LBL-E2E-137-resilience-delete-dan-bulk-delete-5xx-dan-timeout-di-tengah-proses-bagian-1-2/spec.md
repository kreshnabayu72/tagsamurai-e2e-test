---
id: TC-FA-LBL-E2E-137-resilience-delete-dan-bulk-delete-5xx-dan-timeout-di-tengah-proses-bagian-1-2
title: "Resilience Delete dan Bulk Delete: 5xx dan Timeout di Tengah Proses (Bagian 1/2)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-170
  - TC-FA-LBL-171
  - TC-FA-LBL-200
coverage:
  web: automated
---

# Resilience Delete dan Bulk Delete: 5xx dan Timeout di Tengah Proses (Bagian 1/2)

## Prerequisites

- Mode: FE+BE. Backend nyata dengan `Spectra.intercept()` untuk memaksa respons Delete 5xx dan timeout (per item pada Bulk Delete); asersi atas state backend (baris tetap ada, baris hilang sesudah intercept dilepas).
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, `Fixture.assetLabeling.akun.totalControl`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label bersih milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-137`):
  - `Delete Target 170 {runId}-137` (TC-FA-LBL-170)
  - `Delete Target 171 {runId}-137` (TC-FA-LBL-171)
  - `Mid A 200 {runId}-137`, `Mid B 200 {runId}-137`, `Mid C 200 {runId}-137` (TC-FA-LBL-200; urutan seleksi A, B, C)
- Fixture `fixtures/asset-labeling.json` (disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |

- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 5xx atau timeout (endpoint ditentukan tim FE dan tidak ditulis di TC); intercept dilepas segera sesudah pemicu selesai (S-09) dan hook `after` melepasnya bila spec gagal di tengah. Intercept per item untuk Bulk Delete: respons item kedua dipaksa gagal sedangkan item lain tidak dipengaruhi. Fixture BE untuk seeding dan membersihkan label.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed dan label yang dibuat spec (nama bersuffix `{runId}-137`, termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh. Entri log bersifat permanen dan tidak dihapus.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-170: Delete gagal 5xx: dialog D-01 tetap terbuka dan label tidak terhapus

1. Ketik Search `Delete Target 170 {runId}-137`, tekan Enter
2. Klik `⋯` pada baris `Delete Target 170 {runId}-137`, lalu klik `Delete`
3. Paksa respons Delete 5xx (`Spectra.intercept()`)
4. Klik `[Delete]` pada dialog D-01
5. Verifikasi toast error `Error, failed to delete label.`
6. Verifikasi dialog D-01 tetap terbuka
7. Verifikasi baris `Delete Target 170 {runId}-137` tetap ada
8. Lepas intercept
9. Tutup toast error secara manual
10. Klik `[Delete]` pada dialog D-01
11. Verifikasi toast `Success, label has been deleted.`
12. Verifikasi baris `Delete Target 170 {runId}-137` hilang dari tabel

### TC-FA-LBL-171: Delete timeout: toast koneksi dan dialog D-01 tetap terbuka

13. Ganti isi kotak search dengan `Delete Target 171 {runId}-137`, tekan Enter
14. Klik `⋯` pada baris `Delete Target 171 {runId}-137`, lalu klik `Delete`
15. Paksa request Delete timeout (`Spectra.intercept()`)
16. Klik `[Delete]` pada dialog D-01
17. Verifikasi toast error `Connection problem. Please try again.`
18. Verifikasi dialog D-01 tetap terbuka
19. Verifikasi baris `Delete Target 171 {runId}-137` tetap ada
20. Lepas intercept
21. Klik `[Cancel]` pada dialog D-01

### TC-FA-LBL-200: Bulk Delete gagal 5xx di tengah proses: dialog tertutup, toast error, Bulk Action Bar dan seleksi dipertahankan, tabel di-refresh

22. Ganti isi kotak search dengan `200 {runId}-137`, tekan Enter
23. Centang baris `Mid A 200 {runId}-137`
24. Centang baris `Mid B 200 {runId}-137`
25. Centang baris `Mid C 200 {runId}-137`
26. Klik `Bulk Action` lalu klik `Delete`
27. Paksa respons 5xx untuk item kedua (`Spectra.intercept()`)
28. Klik `[Delete]` pada dialog D-03
29. Verifikasi toast error `Error, failed to delete label.`
30. Verifikasi Bulk Action Bar tetap tampil
31. Verifikasi seleksi dipertahankan (tidak di-reset ke 0)
32. Verifikasi tabel di-refresh sehingga menampilkan keadaan nyata (hasil per item tidak diasersi)
33. Verifikasi dialog D-03 tertutup
34. Lepas intercept
35. Klik `Unselect All` untuk menghapus seleksi

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 3c (Delete Label Single) dan 3d (Bulk Delete Label). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): Search untuk menemukan baris label target (Search `200 {runId}-137` menampilkan ketiga label Mid yang berbagi potongan nama); menutup toast error secara manual agar toast berteks sama pada TC-FA-LBL-200 dapat diasersi lagi (R-12); melepas intercept (S-09); `[Cancel]` pada D-01 supaya label tidak terhapus; `Unselect All` supaya seleksi tidak bocor ke TC berikutnya (S-09).
- Pembagian TC lintas spec: TC-FA-LBL-201 dan 202 ada di spec 138; tidak ada asersi "tidak ada entri log" di spec ini: Post Condition TC-FA-LBL-170 ("tidak ada entri log dari percobaan gagal") tidak punya langkah observasi di TC dan dicatat di Temuan untuk QA (S-05); asersi serupa untuk Delete 5xx ada di TC-FA-LBL-521 pada spec 173.
- Temuan untuk QA:
  - TC-FA-LBL-170 Post Condition ("Tidak ada entri log dari percobaan gagal") dan TC-FA-LBL-200 Post Condition ("Entri Delete hanya untuk label yang benar-benar terhapus") tidak punya langkah observasi di TC dan tidak diasersi di spec ini; pencatatan Delete setelah kegagalan 5xx di tengah Bulk Delete diasersi di TC-FA-LBL-397 (spec 132).
  - TC-FA-LBL-200 Expected c ("tabel di-refresh") tidak memberi tanda yang teramati; spec mengasersinya sebagai tabel memuat ulang data dari server (list di-fetch ulang) dan mekanisme pengamatannya disediakan tim FE.
  - TC-FA-LBL-171 tidak menyebut berapa lama timeout; spec memakai `Spectra.intercept()` untuk simulasi timeout (disediakan tim FE).
