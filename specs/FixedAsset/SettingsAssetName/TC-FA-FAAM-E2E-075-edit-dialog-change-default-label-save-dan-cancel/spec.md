---
id: TC-FA-FAAM-E2E-075-edit-dialog-change-default-label-save-dan-cancel
title: "Edit Ber-Aset: Save Default Label Cascade dan Cancel Dialog Tunggal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-244
  - TC-FA-FAAM-744
coverage:
  web: automated
---

# Edit Ber-Aset: Save Default Label Cascade dan Cancel Dialog Tunggal

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #10: Asset Name `Dell Latitude` (Code `DLAT`, Category `IT Equipment`, TAG Type `RFID`+`QR`, Brand `Dell` model `3310`, `5420`, `7420`, Default Addon `Audit`+`Maintenance`, Default Label `Finance`+`High Priority`, UoM `Unit`, Total Asset 42), dirujuk lewat fixture baru `Fixture.faAssetName.dellLatitude`. Fixture ini tidak dapat digandakan dan diubah spec ini. Pemulihan ke keadaan varian Pre-setup yang dipakai blok berikutnya dijamin fixture seed reset (disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar-blok. Efek yang tersisa: Last Updated dan entri audit trail Changelog, System Log, dan Activity Log bertambah. Suite berjalan serial (S-06, pengecualian 2026-10-30).
- Data Pre-setup #14h: `Single Asset Item` (Total Asset 1, Default Label `Interior`), hanya dibuka dan dibatalkan (TC-744). Label `Finance`, `High Priority`, `Interior`, dan `Urgent` (Pre-setup #25). Untuk TC-244, satu aset Dell Latitude memiliki label `Urgent` yang ditempel manual sebelum Save (precondition tidak tertulis di TC; lihat Temuan untuk QA) dan modul asset dibuka dalam mode baca.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Changelog, System Log aktor (Detail User aktor > tab System Log), dan Activity Log FAMS sebelum aksi sebagai baseline dengan filter Search yang sama dengan pembandingan sesudah aksi (`Single Asset Item`), agar jumlah dibandingkan pada cakupan yang sama; asersi memakai selisih terhadap baseline (S-12).
- Tidak ada state global yang diubah selain data fixture yang dipulihkan seed reset.

## Test Steps

### TC-FA-FAAM-744: Cancel pada dialog Change Default Label sebagai dialog tunggal membatalkan penyimpanan

1. Ketik Search `Single Asset Item`, tekan Enter
2. Buka Changelog, System Log aktor, dan Activity Log FAMS satu per satu, ketik Search `Single Asset Item` pada masing-masing, catat jumlah entri hasil filter sebagai baseline, lalu tutup
3. Klik `⋯` baris `Single Asset Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
4. Lepas Default Label `Interior` dan tambahkan `Urgent`
5. Klik `[Save]`
6. Klik `[Cancel]` pada dialog `Change Default Label`
7. Verifikasi dialog tertutup
8. Verifikasi modal Edit tetap terbuka dengan input dipertahankan
9. Klik `[✕]` pada modal Edit
10. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
11. Klik `[Leave]`
12. Buka Changelog (icon Changelog) dan cari entri `Single Asset Item`
13. Verifikasi jumlah entri Changelog sama dengan baseline
14. Tutup Modal Changelog
15. Buka System Log (Detail User aktor > tab System Log) dan cari entri `Single Asset Item`
16. Verifikasi jumlah entri System Log sama dengan baseline
17. Buka Activity Log FAMS dan cari entri `Single Asset Item`
18. Verifikasi jumlah entri Activity Log sama dengan baseline
19. Buka Fixed Asset > Settings > Asset Master > Asset Name lalu Ketik Search `Single Asset Item`, tekan Enter
20. Verifikasi kolom Default Label baris `Single Asset Item` tetap `Interior`

### TC-FA-FAAM-244: Save Default Label mencascade ke aset: label default terkunci dan promosi manual

21. Ganti isi kotak search dengan `Dell Latitude`, tekan Enter
22. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
23. Lepas `High Priority`, tambahkan `Urgent`, klik `[Save]`
24. Klik `[Save]` pada dialog
25. Tunggu aksi selesai (modal Edit tertutup)
26. Buka Asset Detail salah satu aset Dell Latitude di modul asset
27. Verifikasi aset memiliki label `Urgent` sebagai label default terkunci tanpa `[✕]`
28. Verifikasi label `High Priority` terlepas dari aset
29. Verifikasi label `Urgent` yang sebelumnya ditempel manual berubah menjadi default dan terkunci
30. Pulihkan `Dell Latitude` ke keadaan Pre-setup #10 lewat seed reset

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1, 19, dan 21 untuk menemukan baris target (R-16); penutupan form dirty pada langkah 9 (✕, dialog Unsaved Changes, `[Leave]`, S-08); penutupan Modal Changelog pada langkah 14; tunggu aksi selesai pada langkah 25 (bagian 8b butir 8); pemulihan fixture pada langkah 30.
- Urutan TC: TC-FA-FAAM-744 (dibatalkan) lebih dulu, lalu TC-FA-FAAM-244 yang menyimpan (S-10). Ketiadaan entri log pada TC-FA-FAAM-744 diasersi sebagai selisih nol terhadap baseline atas aksi yang dibatalkan, bukan asersi absence kelas g.
- Temuan untuk QA:
  - TC-FA-FAAM-244 Expected b mengasumsikan label `Urgent` sudah ditempel manual pada aset, tetapi Precondition TC tidak menyebutnya; spec menuliskannya sebagai kebutuhan di Prerequisites.
  - TC-FA-FAAM-244 "aset Dell Latitude" tidak menyebut aset mana dari 42; spec memakai salah satu aset yang disediakan fixture.
  - TC-FA-FAAM-244 memakai fixture Pre-setup #10 langsung dan menyimpannya; fixture tidak dapat digandakan sehingga dipulihkan seed reset (S-06, pengecualian 2026-10-30). Pernyataan ini belum tercantum di `suite.md`.
