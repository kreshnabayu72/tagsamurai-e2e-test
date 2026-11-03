---
id: TC-FA-FAAM-E2E-078-edit-dialog-default-addon-cascade-save
title: "Edit Ber-Aset: Save Default Addon (Enroll, Pending Quota dan Tag, Excluded, Draft, Pending Removal)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-247
  - TC-FA-FAAM-248
  - TC-FA-FAAM-249
  - TC-FA-FAAM-250
coverage:
  web: automated
---

# Edit Ber-Aset: Save Default Addon (Enroll, Pending Quota dan Tag, Excluded, Draft, Pending Removal)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #10: Asset Name `Dell Latitude` (Code `DLAT`, Category `IT Equipment`, TAG Type `RFID`+`QR`, Brand `Dell` model `3310`, `5420`, `7420`, Default Addon `Audit`+`Maintenance`, Default Label `Finance`+`High Priority`, UoM `Unit`, Total Asset 42), dirujuk lewat fixture baru `Fixture.faAssetName.dellLatitude`. Fixture ini tidak dapat digandakan dan diubah spec ini. Pemulihan ke keadaan varian Pre-setup yang dipakai blok berikutnya dijamin fixture seed reset (disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar-blok. Efek yang tersisa: Last Updated dan entri audit trail Changelog, System Log, dan Activity Log bertambah. Suite berjalan serial (S-06, pengecualian 2026-10-30).
- Varian Pre-setup #10 per blok: #10d (42 aset Active, 36 ter-pairing, 6 belum TAG pairing; lisensi Tracking tersedia 30; TC-247), #10f (3 aset `excluded_via_override` pada Tracking; TC-248), #10g (2 aset Draft dan 1 Waiting for Approval; TC-249), dan #10e (Maintenance `enrolled_via_default` pada 10 aset Active dengan 2 transaksi aktif; TC-250). Seed reset memulihkan varian yang dipakai blok berikutnya sebelum blok itu.
- Kemampuan teknis (disediakan tim FE/BE): membaca roster addon Tracking dan Maintenance (mode baca) untuk status `enrolled_via_default`, `pending_quota`, `pending_tag`, `excluded_via_override`, dan `pending_removal`.
- Tidak ada state global yang diubah selain data fixture yang dipulihkan seed reset.

## Test Steps

### TC-FA-FAAM-247: Save tambah Default Addon: enroll sampai lisensi habis, sisanya pending_quota dan pending_tag

1. Ketik Search `Dell Latitude`, tekan Enter
2. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Tambahkan Default Addon `Tracking`
4. Klik `[Save]`
5. Klik `[Save]` pada dialog `Change Default Addon`
6. Tunggu aksi selesai (modal Edit tertutup)
7. Buka roster addon Tracking
8. Verifikasi 30 aset berstatus `enrolled_via_default`
9. Verifikasi 6 aset berstatus `pending_quota`
10. Verifikasi 6 aset tanpa TAG pairing berstatus `pending_tag`
11. Verifikasi 6 aset `pending_tag` tidak memakai lisensi
12. Verifikasi urutan lisensi mulai dari tanggal registrasi terlama (Asset ID sebagai tiebreak)
13. Pulihkan `Dell Latitude` ke keadaan Pre-setup #10f lewat seed reset, buka kembali Fixed Asset > Settings > Asset Master > Asset Name, lalu Ketik Search `Dell Latitude`, tekan Enter

### TC-FA-FAAM-248: Aset excluded_via_override tidak berubah oleh penambahan addon ke default

14. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
15. Tambahkan Default Addon `Tracking`
16. Klik `[Save]`
17. Verifikasi dialog `Change Default Addon` tidak menghitung 3 aset `excluded_via_override`
18. Klik `[Save]` pada dialog `Change Default Addon`
19. Tunggu aksi selesai (modal Edit tertutup)
20. Buka roster addon Tracking
21. Verifikasi 3 aset tetap berstatus `excluded_via_override`
22. Pulihkan `Dell Latitude` ke keadaan Pre-setup #10g lewat seed reset, buka kembali Fixed Asset > Settings > Asset Master > Asset Name, lalu Ketik Search `Dell Latitude`, tekan Enter

### TC-FA-FAAM-249: Aset Draft dan Waiting for Approval tidak ikut cascade Default Addon

23. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
24. Tambahkan Default Addon `Tracking`
25. Klik `[Save]`
26. Verifikasi dialog `Change Default Addon` tidak menghitung 2 aset Draft dan 1 aset Waiting for Approval
27. Klik `[Save]` pada dialog `Change Default Addon`
28. Tunggu aksi selesai (modal Edit tertutup)
29. Buka roster addon Tracking
30. Verifikasi roster Tracking memuat aset Active milik `Dell Latitude`
31. Verifikasi 2 aset Draft dan 1 aset Waiting for Approval tidak terdaftar di roster Tracking
32. Pulihkan `Dell Latitude` ke keadaan Pre-setup #10e lewat seed reset, buka kembali Fixed Asset > Settings > Asset Master > Asset Name, lalu Ketik Search `Dell Latitude`, tekan Enter

### TC-FA-FAAM-250: Addon ditambahkan kembali sebelum transaksi selesai: pending_removal kembali enrolled

33. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
34. Lepas Default Addon `Maintenance`
35. Klik `[Save]`
36. Klik `[Save]` pada dialog `Change Default Addon`
37. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
38. Tambahkan Default Addon `Maintenance` lagi
39. Klik `[Save]` sebelum transaksi aset selesai
40. Klik `[Save]` pada dialog `Change Default Addon`
41. Tunggu aksi selesai (modal Edit tertutup)
42. Buka roster addon Maintenance
43. Verifikasi aset `pending_removal` kembali berstatus `enrolled_via_default`
44. Verifikasi aset itu tidak di-unenroll

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1 untuk menemukan baris target (R-16); tunggu aksi selesai pada langkah 6, 19, 28, dan 41 (bagian 8b butir 8); pemulihan varian fixture dan kembali ke halaman Asset Name pada langkah 13, 22, dan 32 (antar-blok, S-09).
- Dialog `Change Default Addon` yang dikonfirmasi pada langkah Save TC-FA-FAAM-247, 248, 249, dan 250 muncul karena klausanya bernilai bukan nol; TC-FA-FAAM-248, 249, dan 250 tidak menyebut konfirmasi dialog tetapi diperlukan agar Save selesai (lihat Temuan untuk QA).
- Verifikasi roster memuat aset Active milik `Dell Latitude` pada TC-FA-FAAM-249 adalah anchor untuk asersi ketiadaan aset Draft dan Waiting for Approval (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-FAAM-248 Expected "tidak dihitung pada dialog" tidak menyebut angka dialog; spec mengasersi dialog tidak menghitung 3 aset `excluded_via_override` tanpa menyebut angka. TC-FA-FAAM-249 sama untuk 2 aset Draft dan 1 aset Waiting for Approval.
  - TC-FA-FAAM-250 tidak menyebut dialog `Change Default Addon` saat Maintenance dilepas dan ditambahkan kembali serta tidak menyebut roster tempat status diamati; spec mengonfirmasi dialog dan mengamati roster addon Maintenance.
  - TC-FA-FAAM-247 sampai 250 menyimpan perubahan pada fixture Pre-setup #10 langsung dan tidak punya salinan di Tabel Data Dinamis; fixture dipulihkan seed reset (S-06, pengecualian 2026-10-30).
- Alasan melewati sekitar 35 langkah: empat blok satu topik (cascade Default Addon pada `Dell Latitude`) dengan varian fixture masing-masing yang dipulihkan seed reset antar-blok; kegagalan satu blok tidak membuat blok lain kehilangan makna. Pembukaan roster, tunggu, dan pemulihan antar-blok menyumbang sekitar sepertiga langkah.
