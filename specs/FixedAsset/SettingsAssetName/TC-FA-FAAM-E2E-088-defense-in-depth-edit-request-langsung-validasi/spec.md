---
id: TC-FA-FAAM-E2E-088-defense-in-depth-edit-request-langsung-validasi
title: "Defense-in-Depth Edit: Request Langsung Emoji, Addon, Melepas Model In-Use"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-189
  - TC-FA-FAAM-209
  - TC-FA-FAAM-210
  - TC-FA-FAAM-260
  - TC-FA-FAAM-684
coverage:
  web: automated
---

# Defense-in-Depth Edit: Request Langsung Emoji, Addon, Melepas Model In-Use

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #13d: Asset Name `Edit Target Item` (Code `ETI`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell` model `5420`, UoM `Unit`, Total Asset 0), dirujuk lewat fixture baru `Fixture.faAssetName.editTargetItem`; pada spec ini hanya dibuka dan ditolak validasi atau dibatalkan, tidak disimpan sehingga Last Updated tidak berubah (S-06).
- Data Pre-setup #10: Asset Name `Dell Latitude` (Code `DLAT`, Category `IT Equipment`, TAG Type `RFID`+`QR`, Brand `Dell` model `3310`, `5420`, `7420`, Default Addon `Audit`+`Maintenance`, Default Label `Finance`+`High Priority`, UoM `Unit`, Total Asset 42), dirujuk lewat fixture baru `Fixture.faAssetName.dellLatitude`; pada spec ini hanya dibuka dan ditolak atau dibatalkan, tidak ada yang tersimpan sehingga Last Updated tidak berubah (S-06).
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP sesi API aktor (token tidak dihitung sebagai sesi web) untuk request Edit langsung ke server; asersinya hanya respons server dan state data pada List (bagian 8b butir 1).
- Pre-setup #10b: lisensi addon `Maps` tidak teralokasi aktif pada client Automation (TC-210).
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-189: Emoji yang lolos filter FE ditolak saat Edit

1. Ketik Search `Edit Target Item`, tekan Enter
2. Klik `⋯` baris `Edit Target Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Injeksi value berisi emoji langsung ke DOM field Asset Name (bypass keystroke filter FE)
4. Verifikasi error inline `Asset name contains invalid characters` real-time

### TC-FA-FAAM-684: Emoji pada nama model yang lolos filter FE ditolak server saat Edit dengan error inline

5. Ganti isi field Asset Name dengan nilai tersimpan `Edit Target Item`
6. Injeksi model `Item 😊` langsung ke input model pada baris Brand `Dell` (bypass filter FE)
7. Klik `[Save]`
8. Verifikasi error inline `Model name contains invalid characters` pada input model
9. Verifikasi tidak ada toast
10. Verifikasi modal Edit tetap terbuka
11. Kosongkan input model
12. Klik `[✕]` pada modal Edit
13. Verifikasi baris `Edit Target Item` tampil di tabel dengan Code `ETI` (record tidak berubah)

### TC-FA-FAAM-209: Edit langsung mengisi Default Addon saat Non-TAG ditolak

14. Catat TAG Type dan Default Addon baris `Edit Target Item` (TAG Type `QR`, Default Addon kosong)
15. Kirim request Edit langsung pada `Edit Target Item` dengan TAG Type `Non-TAG` dan Default Addon `Audit`
16. Verifikasi server menolak request (respons error karena Default Addon mensyaratkan TAG)
17. Muat ulang List dan Ganti isi kotak search dengan `Edit Target Item`, tekan Enter
18. Verifikasi baris `Edit Target Item` tetap ber-TAG Type `QR`
19. Verifikasi baris `Edit Target Item` tetap tanpa Default Addon

### TC-FA-FAAM-210: Edit langsung menambah addon tanpa lisensi aktif ditolak

20. Catat Default Addon baris `Edit Target Item` (kosong)
21. Kirim request Edit langsung pada `Edit Target Item` menambah Default Addon `Maps` saat lisensi Maps tidak aktif
22. Verifikasi server menolak request (lisensi addon tidak aktif)
23. Muat ulang List dan Ganti isi kotak search dengan `Edit Target Item`, tekan Enter
24. Verifikasi Default Addon baris `Edit Target Item` tetap kosong tanpa `Maps`

### TC-FA-FAAM-260: Request Edit langsung melepas model atau Brand in-use ditolak seluruhnya tanpa mutasi

25. Ganti isi kotak search dengan `Dell Latitude`, tekan Enter
26. Catat Code dan model Brand `Dell` baris `Dell Latitude` (Code `DLAT`, model `3310`, `5420`, `7420`)
27. Kirim request Edit langsung yang melepas model `5420` dan mengubah Code menjadi `API-X`
28. Verifikasi server menolak seluruh Edit
29. Muat ulang List dan Ganti isi kotak search dengan `Dell Latitude`, tekan Enter
30. Verifikasi Code baris `Dell Latitude` tetap `DLAT`
31. Klik `⋯` baris `Dell Latitude` lalu `Detail`, buka tab Models per Brand
32. Verifikasi model `5420` masih ada pada Brand `Dell`
33. Tutup Popup Detail

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC-FA-FAAM-189, 209, 210, 260, dan 684 adalah TC defense-in-depth (kelas a) dengan Expected respons API; tetap masuk spec FE+BE karena TC granular tetap sumber dan tiap TC tepat satu spec (BE mencatatnya di tingkat endpoint).
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1, 25, 17, 23, dan 29 untuk menemukan baris target (R-16); pengembalian Asset Name ke nilai tersimpan pada langkah 5, pengosongan input model pada langkah 11, dan penutupan modal pada langkah 12; penutupan Popup Detail pada langkah 33.
- Request langsung ke server (TC-FA-FAAM-209, 210, 260) hanya mengasersi respons server dan state data pada List dan Popup Detail (bagian 8b butir 1); perilaku FE tidak diasersi. TC-FA-FAAM-189 dan 684 memakai injeksi DOM di browser sehingga error inline diasersi.
- Seluruh blok tidak menyimpan perubahan sehingga fixture `Edit Target Item` dan `Dell Latitude` tidak berubah.
- Temuan untuk QA:
  - TC-FA-FAAM-209, 210, dan 260 mengharapkan "Changelog tidak memuat entri baru" atas request langsung yang ditolak. Asersi ketiadaan log atas penolakan request langsung dikelola spec absence (kelas g, S-05, keputusan 2026-10-30); karena TC ini tidak ada di spec absence mana pun, klausa itu belum teruji. Pemilik suite perlu menempatkannya di spec absence.
  - TC-FA-FAAM-209 dan 210 Expected "Server menolak" tidak menyebut kode status; spec mengasersi respons error (bukan 2xx).
  - TC-FA-FAAM-684 tidak menyebut apakah input model yang belum menjadi badge membuat form dirty; spec mengosongkan input lalu menutup dengan ✕ tanpa verifikasi dialog.
