---
id: TC-FA-CF-E2E-080-menutup-form-edit-reload-clear-field-dan-cancel-popup
title: "Form Edit: Reload, Clear Field, dan Cancel Dialog Popup Edit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-295
  - TC-FA-CF-296
  - TC-FA-CF-621
coverage:
  web: automated
---

# Form Edit: Reload, Clear Field, dan Cancel Dialog Popup Edit

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai (pengguna Sarah Johnson, Modified By `Sarah J`; Pre-setup #1 dan #18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); pola `totalControl_automated_{namaCompany}@qwertysystem.net`, disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Pre-setup Company Nilai (#18, dasar Company Alpha #11 dan baseline #12; 21 field tab General): dipakai `Storage Capacity` (Numeric 0 Decimal Places, Placeholder `Capacity in GB`, Scope {Generator, Pump}) dan `Legacy Tag` (Text, Scope kosong). Nama hasil edit Dinamis bersuffix `Dirty Reload {runId}-080`. Nilai data mengacu `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE).
- Kemampuan teknis: menangani dialog bawaan browser `beforeunload` saat muat ulang halaman (membatalkan konfirmasi; dialog dibaca dan dibatalkan oleh runner sehingga muncul atau tidaknya dapat diasersi).
- Baseline: hook `before` memulihkan baseline Company Nilai lewat seed reset Company; hook `after` memulihkan field baseline yang diubah spec (`Storage Capacity` kembali ke nama baseline) dan membersihkan data Dinamis milik spec. Mekanisme seed disediakan tim FE/BE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel oleh hook `before` dan `after` suite; lihat `suite.md`.
- State global: tidak ada yang diubah selain data Company Nilai yang dipulihkan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Atur ukuran halaman Pagination menjadi 100

### TC-FA-CF-296: Klik Clear Field pada Edit mengosongkan seluruh field tanpa me-revert dan tanpa dialog

2. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
3. Klik `[Clear Field]`
4. Verifikasi Field Name dikosongkan murni (bukan dikembalikan ke nilai tersimpan)
5. Verifikasi Placeholder dikosongkan murni (bukan dikembalikan ke nilai tersimpan)
6. Verifikasi tidak ada dialog konfirmasi
7. Verifikasi modal tetap terbuka
8. Verifikasi fokus pada input pertama
9. Verifikasi pesan error inline tidak tampil
10. Klik icon close `[✕]`
11. Verifikasi dialog `Unsaved Changes` tampil
12. Klik `[Leave]`

### TC-FA-CF-621: Cancel pada dialog Unsaved Changes Popup Edit mempertahankan modal dan input

13. Klik row action `⋯` > `Edit` pada baris `Legacy Tag`
14. Ubah Field Name menjadi `Dirty Cancel`
15. Klik icon close `[✕]`
16. Verifikasi dialog `Unsaved Changes` dengan `You have unsaved changes. Are you sure you want to leave?` tampil
17. Klik `[Cancel]` pada dialog
18. Verifikasi dialog tertutup
19. Verifikasi modal Edit tetap terbuka
20. Verifikasi Field Name masih `Dirty Cancel`
21. Klik icon close `[✕]`
22. Verifikasi dialog `Unsaved Changes` tampil
23. Klik `[Leave]`
24. Verifikasi baris `Legacy Tag` tetap bernama `Legacy Tag` pada tabel (tidak ada data berubah)

### TC-FA-CF-295: Reload saat form Edit dirty memicu konfirmasi bawaan browser

25. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
26. Ubah Field Name menjadi `Dirty Reload {runId}-080`
27. Muat ulang halaman (F5)
28. Verifikasi konfirmasi bawaan browser muncul saat form dirty
29. Batalkan konfirmasi browser
30. Klik `[Save]` hingga sukses
31. Tunggu modal tertutup
32. Muat ulang halaman (F5)
33. Verifikasi Breadcrumb halaman Custom Fields tampil
34. Verifikasi konfirmasi bawaan browser tidak muncul setelah Save sukses

## Notes

- Urutan TC di spec: 296, 621, 295. Kasus yang tidak menyimpan (296, 621) berjalan lebih dulu; TC-FA-CF-295 menyimpan perubahan nama `Storage Capacity` dan berada di akhir (bagian 3 prinsip 6). Muat ulang pada TC-FA-CF-295 adalah objek uji, sehingga sah memakai F5 (S-08) dengan kemampuan menangani dialog `beforeunload` tertulis di Prerequisites.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ukuran halaman 100 supaya seluruh baris Company Nilai tampil dan baris target ditemukan tanpa Search), langkah 10 sampai 12 dan 21 sampai 23 (menutup form dirty; `Verifikasi` dialog `Unsaved Changes` mengikuti S-08), langkah 29 (membatalkan konfirmasi browser sebagai aksi TC), langkah 31 (menunggu modal tertutup sebelum muat ulang berikutnya).
- Langkah 33 adalah anchor positif untuk asersi ketiadaan konfirmasi pada langkah 34 (halaman termuat).
- Temuan untuk QA:
  - TC-FA-CF-296 Expected c "pesan error inline dibersihkan" tidak didahului keadaan yang menampilkan pesan error; spec mengasersi bahwa tidak ada pesan error inline sesudah `[Clear Field]`.
  - TC-FA-CF-295 tidak menyebut apakah Save berhasil menutup modal atau memunculkan toast; spec menunggu modal tertutup sebagai langkah penghubung.
  - Email Total Control Company Nilai dan env var passwordnya tidak tertulis di Pre-setup TC; spec memakai `FA_TC_NILAI_PASSWORD` yang disediakan tim FE.
