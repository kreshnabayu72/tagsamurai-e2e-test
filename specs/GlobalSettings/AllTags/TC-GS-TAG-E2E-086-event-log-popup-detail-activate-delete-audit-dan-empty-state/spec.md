---
id: TC-GS-TAG-E2E-086-event-log-popup-detail-activate-delete-audit-dan-empty-state
title: "Popup Detail Event Log: Activate TAG Detail, Delete Detail, Audit Detail, Sesi Tanpa Tag Berhasil, Section Kosong, dan Empty State S-07"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-259
  - TC-GS-TAG-260
  - TC-GS-TAG-261
  - TC-GS-TAG-262
  - TC-GS-TAG-340
  - TC-GS-TAG-341
  - TC-GS-TAG-342
coverage:
  web: automated
---

# Popup Detail Event Log: Activate TAG Detail, Delete Detail, Audit Detail, Sesi Tanpa Tag Berhasil, Section Kosong, dan Empty State S-07

## Prerequisites

- Mode: FE+BE.
- Akun aktor utama: Total Control Client A Sari Dewi `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup TC); kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before` (akun default suite), sehingga hook `after` mengembalikan sesi ke akun ini.
- Akun kedua (langkah 40 sampai 42, TC-341 dan TC-342): Total Control Client Log Wulan Sari `totalControl_automated_qaLog@qwertysystem.net`; kredensial `Spectra.env.GS_TC_LOG_PASSWORD` (belum terdaftar di `.env.example` dan `spectra.config.ts`; perlu didaftarkan pemilik repositori, tanpa nilai).
- Flag Guided Tooltip `gs-tag-registry` dan `gs-tag-activate` untuk kedua akun mengikuti hook suite `before` dan `after` (lihat `suite.md`, bagian Hook Guided Tooltip).
- Suite serial (`parallel: false`). Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- Data Pre-setup (dibaca saja, tanpa aksi tulis; seeding lewat fixture BE, mekanisme disediakan tim FE/BE, lihat Temuan untuk QA):
  - Client A: Seed Event Log `E-01`, `E-02`, `E-05`, `E-14` (Tab Activate TAG) dan `A-01`, `A-02` (Tab Audit TAG), Tabel Data Uji Dinamis TC. Isi detail sesi: `E-01` memuat tag Activated dan Waiting for Approval (22 Activated, 2 Waiting for Approval, 1 Failed; Device Name katalog diubah setelah aktivasi sehingga nilai snapshot berbeda dari katalog terbaru); `E-02` hanya Activated (10 baris, Waiting for Approval 0); `E-05` memuat tag Deleted (4) dan satu tag Failed (race Paired); `E-14` (Delete, Success 0, Failed 1) memuat satu tag Failed; `A-01` memuat 47 tag Found dan 3 tag Not Found yang ditandai Damaged/Missing; `A-02` memuat 30 tag Found dan 0 Not Found.
  - Client Log: Fixture Event Log `E-L1` (17/09/26 09:00, GPS, Activate, Success 0, Waiting for Approval 0, Failed 2, PIC `Budi S`) dan `A-L1` (17/09/26 10:00, RFID, Found 0, Not Found 0, PIC `Budi S`; seluruh baris dilewati karena tidak lagi eligible).
- Event Log Client A menumpuk antar spec (spec lain menambah baris), sehingga tabel dibatasi Filter Date `07/08/26` sampai `16/09/26` (Tab Activate TAG) dan `08/08/26` sampai `16/09/26` (Tab Audit TAG) agar baris seed tampil di halaman 1. Format tanggal General Settings default `dd/MM/yy`. Tanggal sistem lingkungan run lebih besar dari 16/09/26; rentang Filter Date seed `07/08/26` sampai `16/09/26` (Tab Activate TAG) dan `08/08/26` sampai `16/09/26` (Tab Audit TAG) berlaku.
- Kemampuan teknis: memilih rentang tanggal pada date range picker Filter Panel Event Log; mengganti akun (Logout lalu login) di tengah spec; mengatur nilai snapshot Device Name dan SKU di fixture `E-01` berbeda dari katalog Admin Console terbaru (disediakan tim FE/BE).
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-TAG-259: Detail sesi Activate, section Activated dan Waiting for Approval berurutan Code A-Z, snapshot Device Name

1. Klik tombol `Event Log` di toolbar
2. Klik Filter, pilih Date `07/08/26` sampai `16/09/26`, klik `[Apply]`, lalu tutup Filter Panel dengan klik Filter
3. Klik `Detail` pada baris `E-01` (16/09/26 14:30)
4. Verifikasi judul popup `Activate TAG Detail`
5. Verifikasi section `Activated` tampil sebelum section `Waiting for Approval`
6. Verifikasi baris `Failed` tidak tampil pada popup (section `Failed` tidak ada)
7. Verifikasi kolom berurutan `TAG Type | Device Name | SKU | Code`
8. Verifikasi sedikitnya satu baris tampil pada popup
9. Verifikasi kolom Device Name terisi pada setiap baris
10. Verifikasi urutan Code A-Z dalam section `Activated`
11. Verifikasi urutan Code A-Z dalam section `Waiting for Approval`
12. Verifikasi popup tanpa sort pada header kolom dan tanpa pagination
13. Verifikasi Device Name dan SKU baris pertama section `Activated` menampilkan nilai saat aktivasi (snapshot dari fixture `E-01`), bukan nilai katalog terbaru
14. Tutup popup lewat `✕`

### TC-GS-TAG-340: Popup Detail section tanpa baris tidak ditampilkan (Activate)

15. Klik `Detail` pada baris `E-02` (15/09/26 09:10)
16. Verifikasi section `Activated` tampil
17. Verifikasi judul section `Waiting for Approval` tidak tampil
18. Tutup popup lewat `✕`

### TC-GS-TAG-262: Detail tersedia untuk sesi tanpa tag berhasil

19. Klik `Detail` pada baris `E-14` (11/09/26 09:00; Delete, Success 0, Failed 1)
20. Verifikasi popup `Delete Detail` terbuka dengan section `Failed` memuat satu baris terkait
21. Tutup popup lewat `✕`

### TC-GS-TAG-260: Detail sesi Delete, section Deleted dan Failed dengan Status Sebelum Dihapus

22. Klik `Detail` pada baris `E-05` (13/09/26 10:00)
23. Verifikasi judul popup `Delete Detail`
24. Verifikasi section `Deleted` tampil sebelum section `Failed`
25. Verifikasi kolom berurutan `TAG Type | Code | Status Sebelum Dihapus`
26. Verifikasi baris section `Failed` menampilkan status saat gagal (mis. `Paired`) pada kolom Status Sebelum Dihapus
27. Tutup popup lewat `✕`

### TC-GS-TAG-261: Detail sesi Audit, section TAGs Found dan TAGs Not Found dengan Status After

28. Klik tab `Audit TAG`, klik Filter, pilih Date `08/08/26` sampai `16/09/26`, klik `[Apply]`, lalu tutup Filter Panel dengan klik Filter
29. Klik `Detail` pada baris `A-01` (16/09/26 10:00)
30. Verifikasi judul popup `Audit Detail`
31. Verifikasi section `TAGs Found` tampil sebelum section `TAGs Not Found`
32. Verifikasi kolom berurutan `TAG Type | Device Name | SKU | Code | Status After`, dengan Status After plain text
33. Verifikasi Status After baris section `TAGs Not Found` `Damaged/Missing` (mengikuti hasil Submit)
34. Verifikasi jumlah baris section `TAGs Found` 47 dan section `TAGs Not Found` 3, sama dengan kolom `Found` dan `Not Found` di baris sesi
35. Tutup popup lewat `✕`

### TC-GS-TAG-340: Popup Detail section tanpa baris tidak ditampilkan (Audit)

36. Klik `Detail` pada baris `A-02` (13/09/26 13:20)
37. Verifikasi section `TAGs Found` tampil
38. Verifikasi judul section `TAGs Not Found` tidak tampil
39. Tutup popup dan modal Event Log lewat `✕`

### TC-GS-TAG-341 dan TC-GS-TAG-342: Empty state S-07 pada Client Log

40. Klik avatar akun, pilih `Logout`
41. Login sebagai Total Control Client Log Wulan Sari (`Spectra.env.GS_TC_LOG_PASSWORD`)
42. Buka Global Settings > TAG, Tab All, lalu klik tombol `Event Log` di toolbar
43. Klik `Detail` pada baris `E-L1` (17/09/26 09:00)
44. Verifikasi popup `Activate TAG Detail` menampilkan empty state `No TAGs to show` dengan deskripsi `There are no TAGs recorded for this session.`
45. Verifikasi tidak ada section pada popup `Activate TAG Detail`
46. Tutup popup lewat `✕`, lalu klik tab `Audit TAG`
47. Klik `Detail` pada baris `A-L1` (17/09/26 10:00)
48. Verifikasi popup `Audit Detail` menampilkan empty state `No TAGs to show` dengan deskripsi `There are no TAGs recorded for this session.`
49. Verifikasi tidak ada section pada popup `Audit Detail`
50. Tutup popup dan modal Event Log lewat `✕`

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec hanya membaca data.
- Urutan TC dalam spec: 259, 340 (Activate), 262, 260, 261, 340 (Audit), 341, 342. Blok dikelompokkan menurut popup (Activate, Delete, Audit) dan akun; TC-340 terbelah antara Tab Activate TAG (`E-02`) dan Tab Audit TAG (`A-02`) sehingga muncul di dua blok, id TC tetap di `sourceTc` spec ini satu kali. TC-341 dan TC-342 di akhir karena butuh ganti akun eksplisit (langkah 40 sampai 42) dan tetap bermakna bila bagian sebelumnya gagal.
- Alasan spec di atas sekitar 35 langkah (50 langkah): seluruh blok berkelas sama (baca popup Detail dari modal Event Log, read-only), memakai Seed Event Log yang sama, dan berurutan dari modal yang sama; kegagalan membuka modal membuat semua blok kehilangan makna. Tidak ada langkah berulang dengan ekspansi.
- Langkah penghubung (tanpa `Verifikasi`, tidak ada di TC): langkah 2 dan 28 (Filter Date membatasi tabel pada populasi seed karena Event Log menumpuk, S-12), langkah 14, 18, 21, 27, 35, 39, 46, 50 (menutup popup atau modal), langkah 40 sampai 42 (ganti akun).
- Langkah 8 adalah pembanding positif (sedikitnya satu baris tampil) bagi asersi universal "setiap baris" pada langkah 9.
- Langkah 6, 17, dan 38 (absence section) memakai section atau judul lain pada popup yang sama (langkah 5, 16, 37) sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - Mekanisme seeding Seed Event Log, isi payload Detail per sesi (jumlah baris tiap section, Code, Device Name snapshot), dan cara mengubah Device Name katalog setelah aktivasi tidak didefinisikan di TC; langkah 13 mengasersi nilai snapshot dari fixture `E-01` karena TC tidak menyebut nilai literalnya (Q-4).
  - TC-259 Expected c menyebut "Device Name selalu terisi" tanpa menyebut sumber nilai kosong; TC-261 Expected c mencontohkan Status After `Damaged/Missing` hanya untuk Not Found yang ditandai (`A-01`).
  - TC-262 Expected tidak menyebut judul popup; spec memakai `Delete Detail` karena `E-14` adalah sesi Delete.
