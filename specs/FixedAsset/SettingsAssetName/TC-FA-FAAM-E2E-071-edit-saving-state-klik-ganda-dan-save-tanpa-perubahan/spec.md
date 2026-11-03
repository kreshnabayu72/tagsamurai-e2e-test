---
id: TC-FA-FAAM-E2E-071-edit-saving-state-klik-ganda-dan-save-tanpa-perubahan
title: "Edit: Saving State Tombol Save, Klik Ganda Save, dan Save Tanpa Perubahan No-Op"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-173
  - TC-FA-FAAM-223
  - TC-FA-FAAM-233
coverage:
  web: automated
---

# Edit: Saving State Tombol Save, Klik Ganda Save, dan Save Tanpa Perubahan No-Op

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #13d: Asset Name `Edit Target Item` (Code `ETI`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell` model `5420`, UoM `Unit`, Total Asset 0), dirujuk lewat fixture baru `Fixture.faAssetName.editTargetItem`; pada spec ini hanya dibuka dan ditolak validasi atau dibatalkan, tidak disimpan sehingga Last Updated tidak berubah (S-06).
- Data Dinamis (salinan seed fixture #13d, Dinamis #18 dan #34): `Edit Target Item 173 {runId}-071` (Code `ETI173`) dan `Edit Target Item 233 {runId}-071` (Code `ETI233`).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Changelog, System Log aktor (Detail User aktor > tab System Log), dan Activity Log FAMS sebelum aksi sebagai baseline; asersi memakai selisih terhadap baseline (S-12).
- Kemampuan teknis: `Spectra.intercept()` menunda respons Edit 3 detik di atas backend nyata (TC-173); dilepas segera setelah asersi state sementara (S-09).
- Kemampuan teknis (disediakan tim FE/BE): seed API per TC untuk salinan fixture bernama bersuffix `{runId}-071` (Code salinan mengikuti pola TC dan tetap di bawah batas 15 karakter) dan sesi API aktor; salinan dihapus lewat id hasil seed di hook `after`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-223: Save tanpa perubahan adalah no-op sukses

1. Ketik Search `Edit Target Item`, tekan Enter
2. Catat Last Updated baris `Edit Target Item` serta jumlah entri Changelog, System Log aktor, dan Activity Log FAMS sebagai baseline
3. Klik `⋯` baris `Edit Target Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
4. Klik `[Save]` tanpa mengubah apa pun
5. Verifikasi form tertutup normal
6. Verifikasi toast netral `No changes to save.`
7. Verifikasi Last Updated baris `Edit Target Item` tidak berubah
8. Buka Changelog (icon Changelog)
9. Verifikasi jumlah entri Changelog sama dengan baseline
10. Tutup Modal Changelog
11. Buka System Log (Detail User aktor > tab System Log)
12. Verifikasi jumlah entri System Log sama dengan baseline
13. Buka Activity Log FAMS
14. Verifikasi jumlah entri Activity Log sama dengan baseline

### TC-FA-FAAM-173: Tombol Save masuk Saving state selama request berlangsung

15. Buka Fixed Asset > Settings > Asset Master > Asset Name lalu Ketik Search `Edit Target Item 173 {runId}-071`, tekan Enter
16. Klik `⋯` baris `Edit Target Item 173 {runId}-071` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
17. Ubah Code dari `ETI173` menjadi `ETI173-2`
18. Tunda respons Edit 3 detik lewat intercept jaringan
19. Klik `[Save]`
20. Verifikasi `[Save]` menampilkan loading dan disabled
21. Verifikasi kontrol lain disabled selama request
22. Lepas intercept dan tunggu aksi selesai (modal Edit tertutup)

### TC-FA-FAAM-233: Klik ganda cepat Save hanya menyimpan sekali

23. Ganti isi kotak search dengan `Edit Target Item 233 {runId}-071`, tekan Enter
24. Klik `⋯` baris `Edit Target Item 233 {runId}-071` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
25. Ubah Code menjadi `ETI233-8`
26. Klik `[Save]` dua kali cepat
27. Tunggu aksi selesai (modal Edit tertutup)
28. Buka Changelog (icon Changelog) dan ketik Search `Edit Target Item 233 {runId}-071`, tekan Enter
29. Verifikasi Changelog memuat satu entri Edit Code
30. Tutup Modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1, 15, dan 23 untuk menemukan baris target (R-16); penutupan Modal Changelog pada langkah 10 dan 30; langkah 22 melepas intercept TC-FA-FAAM-173 segera setelah asersi state sementara dan menunggu penyelesaian (S-09, bagian 8b butir 5); tunggu aksi selesai pada langkah 27 (bagian 8b butir 8).
- Urutan TC: TC-FA-FAAM-223 (tanpa perubahan) lebih dulu, lalu TC-FA-FAAM-173 dan 233 yang menyimpan pada salinan masing-masing. Pada TC-FA-FAAM-223 tidak ada langkah baseline di TC; spec menambahkannya karena asersi tanpa entri baru memakai selisih terhadap baseline (S-12), dan jumlah dibaca lewat kemampuan teknis di Prerequisites.
- Ketiadaan entri log pada TC-FA-FAAM-223 diasersi sebagai selisih jumlah terhadap baseline sesudah toast netral `No changes to save.` yang menjadi anchor (bagian 8b butir 2); aksi no-op adalah alur fungsional TC itu, sehingga bukan asersi absence kelas g.
- Entri Changelog TC-FA-FAAM-233 dibaca lewat Search nama bersuffix yang unik (baseline nol, S-12).
- Keunikan nilai Code yang diketik (batas 15 karakter tidak menyisakan ruang untuk suffix `{runId}-<NNN>`): nilai Code mengikuti TC, nomor TC membuatnya berbeda antar spec, seed salinan idempotent, cleanup hanya menghapus yang dibuat spec ini, dan suite berjalan serial (S-12).
- Temuan untuk QA:
  - TC-FA-FAAM-223 tidak menyebut cara membuka System Log dan Activity Log; spec memakai jalur dari TC-FA-FAAM-224 (Detail User aktor > tab System Log dan Activity Log FAMS).
