---
id: TC-FA-LBL-E2E-040-duplikat-nama-label-edit-debounce-500-ms-cek-gagal-dan-save-ditolak-server
title: "Duplikat Nama Label Edit: Debounce 500 ms, Cek Gagal, dan Save Ditolak Server"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-140
  - TC-FA-LBL-487
  - TC-FA-LBL-488
coverage:
  web: automated
---

# Duplikat Nama Label Edit: Debounce 500 ms, Cek Gagal, dan Save Ditolak Server

## Prerequisites

- Mode: FE+BE. Backend nyata. `Spectra.intercept()` dipakai hanya pada TC-FA-LBL-488 untuk menggagalkan request pengecekan keunikan nama (intercept dilepas sebelum `[Save]`).
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label seed milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-040`):
  - `Edit Target 487 {runId}-040` (TC-FA-LBL-487)
  - `Edit Target 488 {runId}-040` (TC-FA-LBL-488)
  - `Edit Target 140 {runId}-040` (TC-FA-LBL-140)
- Data Pre-setup: label `High Priority` (Pre-setup #12) ada di katalog Company Alpha; dipakai sebagai nama bentrok dan tidak diubah.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.labelHighPriority` | `High Priority` (Pre-setup #12) |
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |

- Kemampuan teknis: menunggu 300 ms dan lebih dari 500 ms sesudah ketikan terakhir, mengetik lalu menekan `[Save]` sebelum 500 ms berlalu, dan `Spectra.intercept()` untuk request pengecekan keunikan nama (endpoint disediakan tim FE; tidak ditulis di TC).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed milik spec (termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-487: Edit: pengecekan keunikan memakai debounce 500 ms, bukan blur

1. Ketik Search `Edit Target 487 {runId}-040`, tekan Enter
2. Klik `⋯` pada baris `Edit Target 487 {runId}-040`, lalu klik `Edit`
3. Ganti isi Label Name dengan `Fixture.assetLabeling.labelHighPriority`
4. Tunggu 300 ms sejak ketikan terakhir
5. Verifikasi belum ada inline error `Label name already exists`
6. Tunggu hingga lebih dari 500 ms sejak ketikan terakhir tanpa memindahkan fokus
7. Verifikasi inline error `Label name already exists` tampil tanpa blur
8. Ganti isi Label Name dengan `Edit Target 487 {runId}-040` (kembalikan ke nilai tersimpan)
9. Klik icon `[✕]`

### TC-FA-LBL-488: Edit: pengecekan keunikan gagal tidak menampilkan error dan Save tetap aktif

10. Ganti isi kotak search dengan `Edit Target 488 {runId}-040`, tekan Enter
11. Klik `⋯` pada baris `Edit Target 488 {runId}-040`, lalu klik `Edit`
12. Paksa request pengecekan keunikan nama gagal (intercept jaringan)
13. Ganti isi Label Name dengan `Fixture.assetLabeling.labelHighPriority`, tunggu lebih dari 500 ms
14. Verifikasi tidak ada pesan error pada Label Name
15. Verifikasi `[Save]` berstatus enabled
16. Lepas intercept pengecekan keunikan nama
17. Klik `[Save]`
18. Verifikasi server menolak dengan inline error `Label name already exists`
19. Verifikasi modal Edit Label tetap terbuka
20. Ganti isi Label Name dengan `Edit Target 488 {runId}-040` (kembalikan ke nilai tersimpan)
21. Klik icon `[✕]`
22. Verifikasi baris `Edit Target 488 {runId}-040` tampil dengan nama tidak berubah

### TC-FA-LBL-140: Save dengan nama bentrok yang lolos pengecekan klien ditolak server

23. Ganti isi kotak search dengan `Edit Target 140 {runId}-040`, tekan Enter
24. Klik `⋯` pada baris `Edit Target 140 {runId}-040`, lalu klik `Edit`
25. Ganti isi Label Name dengan `Fixture.assetLabeling.labelHighPriority`, lalu segera klik `[Save]` sebelum 500 ms berlalu
26. Verifikasi inline error `Label name already exists` tampil
27. Verifikasi modal Edit Label tetap terbuka
28. Verifikasi input `High Priority` dipertahankan
29. Verifikasi tidak ada toast
30. Ganti isi Label Name dengan `Edit Target 140 {runId}-040` (kembalikan ke nilai tersimpan)
31. Klik icon `[✕]`
32. Verifikasi baris `Edit Target 140 {runId}-040` tampil dengan nama tidak berubah

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 3b (Edit Label). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 10, 23 adalah Search untuk menemukan baris label target pada Labels List; bukan bagian Expected TC.
- P-5 (b): TC-FA-LBL-488 adalah satu objek-uji ringan kelas b (satu kegagalan request pengecekan keunikan) di spec fungsional dengan permukaan yang sama (duplikat nama Edit); intercept dilepas pada langkah 16 sebelum `[Save]` sehingga penolakan datang dari server nyata (S-09).
- Langkah penghubung (S-03, S-08, S-09): langkah 4, 6, 8, 9, 20, 21, 30, 31 adalah penantian jendela debounce (300 ms dan lebih dari 500 ms) dan pengembalian nama ke nilai tersimpan sebelum menutup modal bersih dengan `[✕]`.
- Seeding minimal (S-11): label seed `Edit Target <nomor TC>` dipakai terpisah per TC karena tiap TC membuka modal sendiri; tidak ada yang berhasil disimpan sehingga ketiganya tidak berubah.
- Temuan untuk QA:
  - TC-FA-LBL-487 menyebut pengamatan "tepat 300 ms"; spec menunggu 300 ms sejak ketikan terakhir lalu memverifikasi, dan ketepatan jendela waktu bergantung pada kemampuan harness FE.
  - TC-FA-LBL-488 tidak menyebut endpoint request pengecekan keunikan nama; spec memakainya sebagai kemampuan "disediakan tim FE" tanpa karangan.
