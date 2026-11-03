---
id: TC-GS-HHR-E2E-071-format-general-settings-dan-zona-waktu
title: "Format Tanggal, Jam, dan Zona Waktu General Settings Tercermin pada Semua Surface Tanggal Handheld Reader"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-392
  - TC-GS-HHR-393
  - TC-GS-HHR-394
  - TC-GS-HHR-395
  - TC-GS-HHR-396
coverage:
  web: automated
---

# Format Tanggal, Jam, dan Zona Waktu General Settings Tercermin pada Semua Surface Tanggal Handheld Reader

## Prerequisites

- Mode: FE+BE. Kelas harness: state global (format tanggal, format jam, dan zona waktu General Settings Client A). Suite `parallel: false`; spec ini mengubah state global dan memulihkannya (lihat Pemulihan).
- Flag Guided Tooltip halaman Handheld Reader: diatur hook suite untuk akun aktor spec ini (lihat `suite.md`, Hook suite).
- Akun aktor: Total Control Sari Dewi (Client A) `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; hook `after` mengembalikan sesi ke akun default suite (akun yang sama).
- Data (Client A, plan Growth, Seed Reader A dari fixture BE, format awal `dd/MM/yy` 24-hour, zona waktu `(UTC+07:00) Bangkok, Hanoi, Jakarta`): DD-01 (`Last Scanned` 21/06/26 10:15, `Activated At` 21/06/26 08:00); baris seed dibaca lewat Filter `Date` pada tanggal seed, bukan lewat posisi teratas: Seed Changelog Client A CL-01 (23/06/26 08:50), Seed Event Log Client A EL-01 (21/06/26 08:00), Seed Usage Event DD-01 UE-01 (21/06/26 10:15). Audit trail permanen dan entri non-seed bertanggal waktu aksi dapat ada di luar tanggal itu.
- Kemampuan teknis (disediakan tim FE/BE): mengubah General Settings Client A (format tanggal `MM/dd/yyyy`, format jam 12-hour, dan Time Zone `(UTC+00:00) UTC, Reykjavik, Accra`) lewat sesi API aktor hingga tersimpan; endpoint tidak didefinisikan di TC, PRD, atau LLD dan tidak ditulis di spec ini. Jam server dan jam browser disinkron (S-12); asersi tanggal membandingkan dengan nilai Seed.
- Input date picker (TC-GS-HHR-393, 394, 395): tanggal 23 Juni 2026 (Modal Changelog) dan 21 Juni 2026 (Tab Usage dan Event Log) dipilih lewat date picker, bukan diketik mentah; teks field tampil dalam format `MM/dd/yyyy` (`06/23/2026`, `06/21/2026`). Filter `Date` diproses server-side dan inklusif kedua ujung (disediakan tim FE/BE, lihat Temuan untuk QA).
- Pemulihan: langkah pemulihan eksplisit di akhir spec mengembalikan format `dd/MM/yy` 24-hour dan Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta`; kolom `Activated At` disembunyikan kembali; hook `after` memulihkan General Settings Client A sebagai cadangan.
- State global yang diubah: General Settings Client A (format tanggal, format jam, Time Zone) dan visibilitas kolom `Activated At`.

## Test Steps

### Format MM/dd/yyyy 12-hour: TC-GS-HHR-392, TC-GS-HHR-393, TC-GS-HHR-394, TC-GS-HHR-395

1. Ubah General Settings Client A: format tanggal `MM/dd/yyyy`, format jam 12-hour lewat sesi API hingga tersimpan
2. Tunggu aksi selesai
3. Muat ulang halaman Handheld Reader
4. Aktifkan kolom `Activated At` lewat panel Column Visibility
5. Amati kolom `Last Scanned` dan `Activated At` baris DD-01
6. Verifikasi `Last Scanned` DD-01 menampilkan bulan `06`, hari `21`, tahun `2026`, jam `10:15 AM` dalam urutan `MM/dd/yyyy`
7. Verifikasi `Activated At` DD-01 menampilkan bulan `06`, hari `21`, tahun `2026`, jam `08:00 AM` dalam urutan `MM/dd/yyyy`
8. Klik ikon Filter, pilih rentang tanggal pada `Last Scanned`
9. Verifikasi teks field date picker `Last Scanned` memakai format `MM/dd/yyyy`
10. Tutup Filter Panel tanpa menerapkan filter
11. Klik ikon Changelog
12. Klik ikon Filter pada Modal Changelog
13. Pilih tanggal 23 Juni 2026 sebagai awal dan akhir rentang pada `Date` lewat date picker
14. Verifikasi teks field date picker `Date` Modal Changelog memakai format `MM/dd/yyyy`
15. Klik `[Apply]`
16. Verifikasi kolom `Date` baris seed CL-01 hasil Filter `Date` menampilkan bulan `06`, hari `23`, tahun `2026`, jam `08:50 AM` dalam urutan `MM/dd/yyyy`
17. Tutup Modal Changelog
18. Klik `Device Name` baris DD-01 untuk membuka Popup Detail
19. Amati info grid `Last Scanned` dan `Activated At`
20. Verifikasi `Last Scanned` DD-01 di info grid menampilkan bulan `06`, hari `21`, tahun `2026`, jam `10:15 AM` dalam urutan `MM/dd/yyyy`
21. Klik ikon Filter pada Tab Usage
22. Pilih tanggal 21 Juni 2026 sebagai awal dan akhir rentang pada `Date` lewat date picker
23. Klik `[Apply]`
24. Verifikasi kolom `Date` baris seed UE-01 hasil Filter `Date` Tab Usage menampilkan bulan `06`, hari `21`, tahun `2026`, jam `10:15 AM`
25. Tutup Popup Detail
26. Klik ikon Event Log
27. Klik ikon Filter
28. Pilih tanggal 21 Juni 2026 sebagai awal dan akhir rentang pada `Date` lewat date picker
29. Verifikasi teks field date picker `Date` Event Log memakai format `MM/dd/yyyy`
30. Klik `[Apply]`
31. Verifikasi kolom `Date` baris seed EL-01 hasil Filter `Date` Event Log menampilkan bulan `06`, hari `21`, tahun `2026`
32. Tutup Popup Event Log

### Zona waktu: TC-GS-HHR-396

33. Pulihkan General Settings Client A ke format tanggal `dd/MM/yy` dan format jam 24-hour, lalu ubah Time Zone Client A menjadi `(UTC+00:00) UTC, Reykjavik, Accra` dari `(UTC+07:00) Bangkok, Hanoi, Jakarta` lewat sesi API hingga tersimpan
34. Tunggu aksi selesai
35. Muat ulang halaman Handheld Reader
36. Amati `Last Scanned` baris DD-01
37. Verifikasi `Last Scanned` DD-01 menjadi `21/06/26 03:15` (bergeser -7 jam dari `21/06/26 10:15`)

### Pemulihan

38. Pulihkan Time Zone Client A menjadi `(UTC+07:00) Bangkok, Hanoi, Jakarta` lewat sesi API hingga tersimpan
39. Sembunyikan kembali kolom `Activated At` lewat panel Column Visibility

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (Section 7d). Semua TC berlabel Automatable.
- Urutan: seluruh TC format (392 sampai 395) memakai General Settings yang sama dan dijalankan berurutan dalam satu pengubahan state; TC-GS-HHR-396 terakhir karena memakai format default dan zona waktu berbeda (prinsip 3 butir 4).
- Langkah penghubung tanpa `Verifikasi` (S-03): mengubah General Settings lewat sesi API, muat ulang, mengaktifkan dan menyembunyikan kolom, membuka dan menutup Filter Panel, Modal Changelog, Popup Detail, dan Popup Event Log, memulihkan General Settings. Langkah "Tunggu aksi selesai" dipakai karena langkah berikut berpindah ke muat ulang halaman setelah aksi API. Filter Panel Daftar Reader (langkah 8) tidak diterapkan. Pemilihan tanggal pada Filter `Date` (langkah 13, 22, 28) dan `[Apply]` (langkah 15, 23, 30) adalah aksi TC-GS-HHR-393, 394, dan 395; baris hasil dibaca pada hasil Filter `Date` seed (CL-01, UE-01, EL-01), bukan pada baris teratas tabel.
- Spec memuat 39 langkah (di atas sekitar 35 langkah). Alasan: seluruhnya satu kelas harness (state global General Settings Client A) dan satu dataset (DD-01 dan baris seed CL-01, UE-01, EL-01); lima TC memakai pengubahan state yang sama (langkah 1 sampai 3) sehingga memecah spec berarti mengulang pengubahan dan pemulihan state global tanpa menambah makna; 10 langkah adalah `Verifikasi` yang dipecah per klausa Expected (S-01); TC-GS-HHR-396 berdiri sendiri pada akhir spec dan kegagalan satu surface tidak membuat surface lain kehilangan makna.
- Pembukaan tiap surface adalah langkah observasi singkat (buka, amati format, tutup) sehingga kegagalan satu surface tidak membuat surface lain kehilangan makna.
- Temuan untuk QA:
  - TC-GS-HHR-392 langkah 2 ("Aktifkan kolom `Activated At`") tidak menyebut mekanismenya; spec memakai panel Column Visibility.
  - TC-GS-HHR-392 sampai TC-GS-HHR-396 menyatakan perubahan General Settings sebagai precondition oleh Total Control tanpa langkah UI; spec mengubahnya lewat sesi API yang disediakan tim FE tanpa mengarang endpoint.
  - TC-GS-HHR-394 langkah 2 mengamati `Activated At` pada info grid, tetapi Expected hanya menyebut `Last Scanned` dan `Date` Tab Usage; spec tidak mengasersi `Activated At` di Popup Detail.
  - TC-GS-HHR-396 tidak menyebut format jam yang berlaku pada Expected `21/06/26 03:15`; spec mengikuti format default `dd/MM/yy` 24-hour dari precondition c.
  - Label Time Zone `(UTC+00:00) UTC, Reykjavik, Accra` dan `(UTC+07:00) Bangkok, Hanoi, Jakarta` disalin dari TC-GS-HHR-396 dan belum dicocokkan dengan opsi pada UI General Settings.
  - TC-GS-HHR-393, 394, dan 395 bergantung pada Filter `Date` yang diproses server-side dan inklusif kedua ujung, pada fixture yang dapat menulis entri audit trail bertanggal Juni 2026 (CL-01, UE-01, EL-01), dan pada date picker yang menerima pilihan tanggal 23 dan 21 Juni 2026 dengan teks field `MM/dd/yyyy`; ketiganya belum diverifikasi pada UI.
