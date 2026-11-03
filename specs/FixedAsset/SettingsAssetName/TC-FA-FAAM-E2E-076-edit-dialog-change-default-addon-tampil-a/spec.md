---
id: TC-FA-FAAM-E2E-076-edit-dialog-change-default-addon-tampil-a
title: "Edit Ber-Aset: Dialog Change Default Addon (Tambah, Hapus, Pengurangan Tanpa In Transaction, Tunggal)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-245
  - TC-FA-FAAM-246
  - TC-FA-FAAM-678
  - TC-FA-FAAM-679
coverage:
  web: automated
---

# Edit Ber-Aset: Dialog Change Default Addon (Tambah, Hapus, Pengurangan Tanpa In Transaction, Tunggal)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #10: Asset Name `Dell Latitude` (Code `DLAT`, Category `IT Equipment`, TAG Type `RFID`+`QR`, Brand `Dell` model `3310`, `5420`, `7420`, Default Addon `Audit`+`Maintenance`, Default Label `Finance`+`High Priority`, UoM `Unit`, Total Asset 42), dirujuk lewat fixture baru `Fixture.faAssetName.dellLatitude`; pada spec ini hanya dibuka dan dibatalkan, tidak disimpan sehingga Last Updated tidak berubah (S-06).
- Varian Pre-setup #10 yang dipakai: #10d (42 aset Active, 36 ter-pairing, 6 belum TAG pairing; lisensi Tracking tersedia 30; TC-245), #10e (Maintenance `enrolled_via_default` pada 10 aset Active dengan 2 transaksi aktif; TC-246), dan #10q (Audit `enrolled_via_default` pada 7 aset Active tanpa transaksi aktif; TC-678); ketiganya berada pada satu keadaan fixture yang sama (#10r) sehingga tidak perlu pemulihan antar-TC.
- Data Pre-setup #14p: `Solo Addon Item` (Total Asset 1: aset Active ter-pairing TAG `QR`, tanpa Default Addon; lisensi Tracking tersedia 5), hanya dibuka dan dibatalkan (TC-679).
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-245: Tambah Default Addon pada Asset Name ber-aset memunculkan dialog Change Default Addon

1. Ketik Search `Dell Latitude`, tekan Enter
2. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Tambahkan Default Addon `Tracking`
4. Klik `[Save]`
5. Verifikasi dialog `Change Default Addon` dengan teks `Adding Tracking: 30 assets will be enrolled (30 available licenses). 6 assets will be set to pending quota. 6 assets are waiting for TAG pairing.` lalu `Are you sure you want to save this change?`
6. Klik `[Cancel]` pada dialog
7. Lepas chip Default Addon `Tracking` (kembali ke nilai tersimpan)

### TC-FA-FAAM-246: Hapus Default Addon memunculkan dialog dengan jumlah aset bertransaksi aktif

8. Lepas Default Addon `Maintenance`
9. Klik `[Save]`
10. Verifikasi dialog `Change Default Addon` memuat `Removing Maintenance:` dengan klausa `8 assets will be unenrolled.` dan klausa `2 assets have an active transaction — they will stay enrolled and be unenrolled once that transaction completes.` lalu `Are you sure you want to save this change?`
11. Klik `[Cancel]` pada dialog
12. Tambahkan kembali Default Addon `Maintenance` (kembali ke nilai tersimpan)

### TC-FA-FAAM-678: Dialog Change Default Addon pengurangan tanpa aset bertransaksi aktif menghilangkan klausa In Transaction

13. Lepas Default Addon `Audit`
14. Klik `[Save]`
15. Verifikasi dialog `Change Default Addon` dengan tombol `[Cancel]` dan `[Save]` memuat `Removing Audit:` dengan klausa `7 assets will be unenrolled.` lalu `Are you sure you want to save this change?`
16. Verifikasi tidak ada klausa yang memuat `active transaction`
17. Klik `[Cancel]` pada dialog
18. Tambahkan kembali Default Addon `Audit` (kembali ke nilai tersimpan)
19. Klik `[✕]` pada modal Edit (form sama dengan nilai tersimpan, tanpa dialog)

### TC-FA-FAAM-679: Dialog Change Default Addon penambahan memakai bentuk tunggal dan menghilangkan klausa bernilai 0

20. Ganti isi kotak search dengan `Solo Addon Item`, tekan Enter
21. Klik `⋯` baris `Solo Addon Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
22. Tambahkan Default Addon `Tracking`
23. Klik `[Save]`
24. Verifikasi dialog `Change Default Addon` dengan tombol `[Cancel]` dan `[Save]` memuat `Adding Tracking:` dengan klausa `1 asset will be enrolled (5 available licenses).` lalu `Are you sure you want to save this change?`
25. Verifikasi tidak ada klausa `pending quota` dan tidak ada klausa `waiting for TAG pairing`
26. Klik `[Cancel]` pada dialog
27. Lepas chip Default Addon `Tracking` (kembali ke nilai tersimpan)
28. Klik `[✕]` pada modal Edit (form sama dengan nilai tersimpan, tanpa dialog)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1 dan 20 untuk menemukan baris target (R-16); `[Cancel]` dialog pada langkah 6, 11, 17, dan 26; pengembalian addon ke nilai tersimpan pada langkah 7, 12, 18, dan 27 agar blok berikutnya mulai dari form bersih (S-09); penutupan modal bersih pada langkah 19 dan 28 (tanpa dialog karena form sama dengan nilai tersimpan).
- Urutan TC: TC-FA-FAAM-245, 246, dan 678 berurutan pada satu pembukaan form `Dell Latitude`, lalu TC-FA-FAAM-679 pada `Solo Addon Item`. Seluruh dialog dibatalkan sehingga fixture tidak berubah dan tidak perlu seed reset.
- Verifikasi isi dialog pada TC-FA-FAAM-678 dan 679 menjadi anchor bagi asersi ketiadaan klausa (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-FAAM-245, 246, dan 678 menyebut varian #10d, #10e, dan #10q dari fixture yang sama; spec mengasumsikan ketiganya berlaku bersamaan (#10r) dan menuliskannya di Prerequisites. Bila tidak berlaku bersamaan, blok yang terdampak memerlukan seed reset varian.
