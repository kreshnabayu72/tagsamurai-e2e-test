---
id: TC-AC-ACHA-E2E-050-format-tanggal-waktu-general-settings
title: "Format Tanggal dan Waktu Mengikuti General Settings: Last Updated List, Waktu 12 Jam, Time Zone, Allocation Log, Activity Log, System Log, dan Filter Panel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-392
  - TC-AC-ACHA-393
  - TC-AC-ACHA-394
  - TC-AC-ACHA-395
  - TC-AC-ACHA-396
  - TC-AC-ACHA-398
coverage:
  web: automated
---

# Format Tanggal dan Waktu Mengikuti General Settings: Last Updated List, Waktu 12 Jam, Time Zone, Allocation Log, Activity Log, System Log, dan Filter Panel

## Prerequisites

- Mode: FE+BE.
- Akun (Pre-setup, email lengkap `<alias>_automated_qaTeam1@qwertysystem.net`; password lewat env var, bukan di spec atau fixture):

| Alias | Pre-setup | Nama pengguna | Dipakai di | Env var password |
|---|---|---|---|---|
| `totalControlPrincipal` | #21 | Admin Pratama (aktor hook `before`) | TC-AC-ACHA-392, 393, 394, 398 | `Spectra.env.AC_TC_PASSWORD` |
| `memberOnDistributor` | #32 | Budi Santoso (MB_ON) | TC-AC-ACHA-395 dan aksi Edit TC-AC-ACHA-396 | `Spectra.env.AC_DA_MB_ON_PASSWORD` |
| `totalControlDistributor` | #27 | Hendra Wibowo | Pembaca Activity Log dan System Log TC-AC-ACHA-396 | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |

- Login akun pertama (Admin Pratama) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite dan memulihkan General Settings ke default Pre-setup #1.
- Hook suite (dinyatakan di `suite.md`): flag Guided Tooltip `guided_tooltip_seen_<page_key>` true untuk akun aktor, sesi API aktor, fixture API disediakan tim FE/BE, pemulihan preferensi Setup Column.
- State global yang diubah spec: General Settings (Date Format, Time Format, Time Zone) milik seluruh tenant. Nilai awal Pre-setup #1: Date Format `dd/MM/yy`, Time Format 24 jam (`HH:mm`), Time Zone Asia/Jakarta (UTC+07:00). Pemulihan: langkah penghubung sesudah tiap blok dan hook `after` (tetap jalan walau spec gagal di tengah). Efek pada Pre-setup bersama (S-06): Last Updated General Settings dan audit trail perubahan setelan ikut berubah dan bertambah permanen; nilai dipulihkan lewat fixture yang disediakan tim FE/BE. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: penyetel General Settings (Date Format, Time Format, Time Zone) lewat fixture API (disediakan tim FE/BE; diperlukan karena Pre-setup #20 tidak mencantumkannya). Seluruh perubahan di spec ini memakai fixture itu sebagai satu-satunya mekanisme dan sebagai langkah penyiapan state.
- "Muat ulang List" berarti muat ulang halaman (F5); Search List dipertahankan setelah F5 (TC-AC-ACHA-366), sehingga isi kotak Search diganti dengan "ganti isi kotak search dengan `X`, tekan Enter"; pada pemuatan pertama kotak masih kosong dan langkahnya sama dengan mengetik.
- Data Pre-setup: #48 Seed 30 alokasi (Last Updated baris `HALC-20260909-00003` = `09/09/26 19:00` dan `HALC-20260909-00001` = `09/09/26 05:00` pada setelan awal; dibaca saja, tidak diubah), #49 transaksi Waiting for Approval milik MB_ON, #16 kantong PT Global Distribusi saldo $20,000.00.
- Data seeding milik spec (fixture API disediakan tim FE/BE): satu salinan transaksi Waiting for Approval milik MB_ON (RFID Object TAG, Quantity 100, Client PT Sejahtera Logistik, Notes `Batch uji`, Reserve $250.00) untuk TC-AC-ACHA-395 dan satu untuk TC-AC-ACHA-396. Allocation ID tiap salinan ditangkap dari respons fixture seeding (Dynamic Reference) dan dipakai sebagai penanda Search, asersi, dan cleanup hook `after`.
- Tabel parameter TC-AC-ACHA-392 (Time Format `HH:mm`; baris `HALC-20260909-00003`):

| Date Format | Last Updated yang tampil |
|---|---|
| `dd/MM/yy` | `09/09/26 19:00` |
| `M/d/yy` | `9/9/26 19:00` |
| `dd MMM yy` | `09 Sep 26 19:00` |
| `DDD, MMM dd, yy` | `Wed, Sep 09, 26 19:00` |
| `DDD, MMM dd, yyyy` | `Wed, Sep 09, 2026 19:00` |

- Kolom Date Activity Log dan System Log (TC-AC-ACHA-396) diasersi pada format, bukan nilai absolut; jam server dan jam browser sinkron dan tidak diubah spec ini.

## Test Steps

### TC-AC-ACHA-392: Last Updated pada List mengikuti Date Format General Settings

1. Untuk setiap baris tabel parameter TC-AC-ACHA-392 (langkah 1 sampai 4): setel Date Format sesuai baris dan Time Format `HH:mm` lewat fixture General Settings
2. Muat ulang halaman (F5), lalu ganti isi kotak search dengan `HALC-20260909`, tekan Enter
3. Baca Last Updated baris `HALC-20260909-00003`
4. Verifikasi Last Updated baris `HALC-20260909-00003` tampil sesuai kolom "Last Updated yang tampil" pada baris tabel parameter yang sedang diuji

### TC-AC-ACHA-393: Waktu 12 jam dengan penanda AM atau PM

5. Pulihkan Date Format `dd/MM/yy` dan setel Time Format `hh:mm a` lewat fixture General Settings
6. Muat ulang halaman (F5), lalu ganti isi kotak search dengan `HALC-20260909`, tekan Enter
7. Verifikasi baris `HALC-20260909-00003` tampil dengan waktu `07:00 PM`
8. Verifikasi baris `HALC-20260909-00001` tampil dengan waktu `05:00 AM`

### TC-AC-ACHA-394: Last Updated mengikuti Time Zone General Settings

9. Pulihkan Time Format `HH:mm` dan setel Time Zone `(UTC+00:00) UTC, Reykjavik, Accra` lewat fixture General Settings
10. Muat ulang halaman (F5), lalu ganti isi kotak search dengan `HALC-20260909`, tekan Enter
11. Verifikasi baris `HALC-20260909-00003` tampil dengan tanggal `09/09/26`
12. Verifikasi baris `HALC-20260909-00003` tampil dengan waktu `12:00` (tujuh jam lebih awal dari tampilan Asia/Jakarta `19:00`)

### TC-AC-ACHA-398: Input tanggal Filter Panel mengikuti General Settings

13. Pulihkan Time Zone `Asia/Jakarta (UTC+07:00)` dan setel Date Format `dd MMM yy` lewat fixture General Settings
14. Muat ulang halaman (F5), buka Filter Panel, dan buka date range picker Last Updated
15. Pilih rentang `03 Sep 26` sampai `04 Sep 26`, lalu baca teks pada field Last Updated
16. Verifikasi teks tanggal terpilih pada field Last Updated memakai Date Format `dd MMM yy`
17. Verifikasi tanggal awal pada field Last Updated tampil `03 Sep 26`
18. Verifikasi teks tanggal terpilih tidak memakai format default `dd/MM/yy`
19. Tutup Filter Panel tanpa menerapkan filter
20. Pulihkan Date Format `dd/MM/yy` lewat fixture General Settings

### Ganti akun ke Budi Santoso (MB_ON)

21. Logout lalu login sebagai Group Member Distributor `memberOnDistributor` (Pre-setup #32), lalu buka Allocation > Device Allocation

### TC-AC-ACHA-395: Date & Time Allocation Log mengikuti General Settings

22. Setel Date Format `DDD, MMM dd, yyyy` dan Time Format `hh:mm a` lewat fixture General Settings
23. Muat ulang halaman (F5), ketik Search Allocation ID transaksi Waiting for Approval milik MB_ON (salinan untuk blok ini), tekan Enter, buka menu row action `⋯` pada transaksi itu, dan klik `Allocation Log`
24. Verifikasi Date & Time di bawah judul `Allocation created by Budi S` memakai nama hari singkat sesuai Date Format `DDD, MMM dd, yyyy`
25. Verifikasi Date & Time di bawah judul `Allocation created by Budi S` memakai tahun 4 digit sesuai Date Format `DDD, MMM dd, yyyy`
26. Verifikasi Date & Time di bawah judul `Allocation created by Budi S` memakai waktu 12 jam dengan AM atau PM sesuai Time Format `hh:mm a`
27. Tutup modal Allocation Log dengan `[×]`

### TC-AC-ACHA-396: Tanggal Activity Log dan System Log mengikuti General Settings

28. Setel Date Format `M/d/yy` dan Time Format `hh:mm a` lewat fixture General Settings
29. Muat ulang halaman (F5), ganti isi kotak search dengan Allocation ID transaksi Waiting for Approval milik MB_ON (salinan untuk blok ini), tekan Enter, klik `Edit` pada transaksi itu, ubah Quantity menjadi `120`, klik `[Save]`, tunggu aksi selesai (form tertutup), dan catat Allocation ID transaksi itu
30. Logout lalu login sebagai Total Control Distributor `totalControlDistributor` (Pre-setup #27)
31. Buka Activity Log di Admin Console, cari Allocation ID transaksi itu, dan baca kolom Date baris Edit
32. Verifikasi kolom Date Activity Log memakai Date Format `M/d/yy` yang sama dengan General Settings
33. Verifikasi kolom Date Activity Log memakai Time Format `hh:mm a` yang sama dengan General Settings
34. Buka System Log pada Detail User `Budi Santoso`, cari Allocation ID transaksi itu, dan baca kolom Date baris Edit
35. Verifikasi kolom Date System Log memakai Date Format `M/d/yy` yang sama dengan General Settings
36. Verifikasi kolom Date System Log memakai Time Format `hh:mm a` yang sama dengan General Settings
37. Pulihkan General Settings ke Pre-setup #1 (Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta) lewat fixture General Settings

## Notes

- Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (Section 7a). TC-AC-ACHA-397 (Export mengikuti General Settings) ada di spec 044 (`download-isi-berkas-csv-xlsx`), bukan di spec ini. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini mengubah General Settings (state global) sehingga suite berjalan serial dan pemulihan ditulis di Prerequisites (R-08). Perubahan General Settings bukan kelas h (state tenant): perubahannya hanya format tampilan dan dipakai sebagai kondisi data, bukan write-lockdown.
- Langkah 1 sampai 4 diulang untuk setiap baris tabel parameter TC-AC-ACHA-392 (parameter tiap iterasi ada di Prerequisites); `Verifikasi` tetap satu per iterasi. Ekspansi: 5 iterasi dikali 4 langkah.
- Ukuran spec: 36 langkah (melewati sekitar 35 langkah), sekitar 52 langkah setelah ekspansi langkah 1 sampai 4 (5 iterasi dikali 4 langkah). Alasan: seluruh blok satu topik (format tanggal dan waktu mengikuti General Settings) dengan satu dataset, tiap blok memulihkan setelan sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; ekspansi loop tabel parameter, ganti akun (S-07), dan pemulihan setelan menambah langkah tanpa verifikasi.
- Urutan (S-10): TC-AC-ACHA-398 ditaruh sebelum TC-AC-ACHA-395 dan 396 (bukan menurut nomor TC) karena TC-AC-ACHA-392, 393, 394, dan 398 dijalankan oleh Admin Pratama (aktor hook `before`), sedangkan TC-AC-ACHA-395 dan 396 membutuhkan ganti akun ke Budi Santoso lalu Hendra Wibowo; urutan menurut nomor akan menambah ganti akun.
- Langkah penghubung (S-03): langkah menyetel General Settings lewat fixture (penyiapan state, bukan objek asersi), langkah memulihkan setelan sebelum blok berikutnya (S-09), langkah mencari baris lewat Search `HALC-20260909` (R-16: pencarian untuk menemukan baris target), tutup Filter Panel tanpa menerapkan, ganti akun (S-07), tutup modal Allocation Log. Asersi tambahan: tidak ada.
- Baris target (R-16): baris seed `HALC-20260909-00003` dan `HALC-20260909-00001` ditemukan lewat Search `HALC-20260909`; transaksi salinan TC-AC-ACHA-395 dan 396 ditemukan lewat Search Allocation ID yang ditangkap saat seeding.
- Baseline log: asersi TC-AC-ACHA-396 hanya mengasersi format kolom Date, bukan jumlah atau urutan baris; entri dicari dengan Allocation ID unik hasil transaksi milik spec (S-12, S-14).
- Pengecualian S-12 nama literal (Lampiran A butir A-6): Allocation ID seed `HALC-20260909-00001` dan `HALC-20260909-00003` (Pre-setup #48) adalah nilai literal yang diasersi persis; baris hanya dibaca. Notes `Batch uji` pada salinan seed mengikuti Pre-setup #49 dan tidak diasersi.
- Temuan untuk QA:
  - TC-AC-ACHA-392 sampai 396 dan 398 menyebut "ubah Date Format ... di General Settings, simpan" tanpa menyebut akun yang mengubah dan menu persisnya; precondition juga tidak menyebut hak akun (mis. Group Member MB_ON pada TC-AC-ACHA-395 dan 396) untuk membuka General Settings. Spec menyetel lewat fixture sebagai penyiapan state.
  - TC-AC-ACHA-392 menyebut "baris teratas" pada langkah tetapi Expected menyebut baris `HALC-20260909-00003`; spec menemukan baris lewat Search ID (S-14) karena urutan teratas bergantung pada data lain.
  - TC-AC-ACHA-395 dan 396 tidak menyebut nilai tanggal persis (hanya format); spec mengasersi format.
  - Post Condition TC-AC-ACHA-392 sampai 396 dan 398 ("-") tidak ada.
