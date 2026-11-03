---
id: TC-FA-FAAM-E2E-068-edit-brand-baru-no-model-dan-badge-model
title: "Edit: Brand Baru, No Model Disisipkan, Hapus Badge Model, dan No Model Menjadi Model Nyata"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-214
  - TC-FA-FAAM-218
  - TC-FA-FAAM-219
  - TC-FA-FAAM-746
coverage:
  web: automated
---

# Edit: Brand Baru, No Model Disisipkan, Hapus Badge Model, dan No Model Menjadi Model Nyata

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Dinamis (salinan seed fixture #13d, Dinamis #25, #26, #27): `Edit Target Item 214 {runId}-068` (Code `ETI214`), `Edit Target Item 218 {runId}-068` (Code `ETI218`), dan `Edit Target Item 219 {runId}-068` (Code `ETI219`). Dinamis #97 (salinan fixture #14k): `No Model Item 746 {runId}-068` (Brand `Dell` model `No Model`, Total Asset 0). Brand `Lenovo` (Pre-setup #23).
- Kemampuan teknis (disediakan tim FE/BE): seed API per TC untuk salinan fixture bernama bersuffix `{runId}-068` (Code salinan mengikuti pola TC dan tetap di bawah batas 15 karakter) dan sesi API aktor; salinan dihapus lewat id hasil seed di hook `after`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-219: Badge model yang belum dipakai aset dapat dihapus saat Edit

1. Ketik Search `Edit Target Item 219 {runId}-068`, tekan Enter
2. Klik `⋯` baris `Edit Target Item 219 {runId}-068` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Tambahkan model `Temp 1` pada baris Dell
4. Klik `×` pada badge `Temp 1`
5. Verifikasi badge `Temp 1` hilang
6. Klik `[Save]`
7. Verifikasi toast `Success, asset name has been updated.` tampil

### TC-FA-FAAM-214: Menambah Brand baru pada Edit memunculkan baris model baru

8. Ganti isi kotak search dengan `Edit Target Item 214 {runId}-068`, tekan Enter
9. Klik `⋯` baris `Edit Target Item 214 {runId}-068` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
10. Pilih Brand `Lenovo`
11. Tambahkan model `X1` pada baris Lenovo
12. Verifikasi tabel Model/Type menampilkan baris `Dell` dan `Lenovo` urut A→Z
13. Klik `[Save]`
14. Tunggu aksi selesai (modal Edit tertutup)
15. Klik `⋯` baris `Edit Target Item 214 {runId}-068` lalu `Detail`, buka tab Models per Brand
16. Verifikasi Popup Detail menampilkan Brand `Dell` dan `Lenovo`
17. Tutup Popup Detail

### TC-FA-FAAM-218: Brand baru tanpa model pada Edit disisipi No Model saat Save

18. Ganti isi kotak search dengan `Edit Target Item 218 {runId}-068`, tekan Enter
19. Klik `⋯` baris `Edit Target Item 218 {runId}-068` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
20. Pilih Brand `Lenovo` tanpa mengetik model
21. Klik `[Save]`
22. Tunggu aksi selesai (modal Edit tertutup)
23. Klik `⋯` baris `Edit Target Item 218 {runId}-068` lalu `Detail`, buka tab Models per Brand
24. Verifikasi baris `Lenovo` menampilkan badge `No Model`
25. Tutup Popup Detail

### TC-FA-FAAM-746: Badge No Model menjadi badge biasa saat model nyata ditambahkan dan dapat dilepas bila tidak in-use

26. Ganti isi kotak search dengan `No Model Item 746 {runId}-068`, tekan Enter
27. Klik `⋯` baris `No Model Item 746 {runId}-068` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
28. Ketik model `Alpha` pada baris Dell lalu tekan Enter
29. Klik `[Save]`
30. Tunggu aksi selesai (modal Edit tertutup)
31. Klik `⋯` baris `No Model Item 746 {runId}-068` lalu `Detail`, buka tab Models per Brand
32. Verifikasi baris `Dell` menampilkan badge `Alpha` dan `No Model` urut A→Z
33. Tutup Popup Detail
34. Klik `⋯` baris `No Model Item 746 {runId}-068` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
35. Klik `×` pada badge `No Model`
36. Klik `[Save]`
37. Verifikasi toast `Success, asset name has been updated.` tampil
38. Klik `⋯` baris `No Model Item 746 {runId}-068` lalu `Detail`, buka tab Models per Brand
39. Verifikasi baris `Dell` hanya menampilkan badge `Alpha`
40. Tutup Popup Detail

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1, 8, 18, dan 26 untuk menemukan baris target (R-16); tunggu aksi selesai pada langkah 14, 22, dan 30 (Save tanpa toast di Expected TC, langkah berikutnya berpindah ke Popup Detail, bagian 8b butir 8); penutupan Popup Detail pada langkah 17, 25, 33, dan 40.
- Urutan TC: TC-FA-FAAM-219 (UI dan simpan sederhana) lebih dulu, lalu TC-FA-FAAM-214, 218, dan 746; masing-masing memakai salinan sendiri.
- Keunikan nilai Code yang diketik (batas 15 karakter tidak menyisakan ruang untuk suffix `{runId}-<NNN>`): nilai Code mengikuti TC, nomor TC membuatnya berbeda antar spec, seed salinan idempotent, cleanup hanya menghapus yang dibuat spec ini, dan suite berjalan serial (S-12).
- Temuan untuk QA:
  - TC-FA-FAAM-214 dan 218 Expected hanya menyebut Detail tanpa toast Save; spec tidak mengasersi toast dan memakai langkah tunggu aksi selesai.
  - TC-FA-FAAM-746 Expected a menyebut badge `Alpha` dan `No Model` tampil bersama sesudah Save pertama (urut A→Z); spec mengikuti TC walau badge `No Model` biasanya digantikan model nyata.
- Alasan melewati sekitar 35 langkah: empat blok berdiri sendiri pada salinan terpisah; kegagalan satu blok tidak membuat blok lain kehilangan makna. Pengamatan Popup Detail (buka, tab, tutup) diulang per blok dan menyumbang sekitar sepertiga langkah.
