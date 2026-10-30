---
id: TC-GS-FILEMGR-E2E-044-screening-changelog-format-sel-dan-tutup
title: "Screening Modal Changelog: Layout, Format Sel Modified By dan Action, Tooltip, dan Tutup Modal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-28
  - TC-GS-FILEMGR-29
  - TC-GS-FILEMGR-33
  - TC-GS-FILEMGR-174
coverage:
  web: automated
---

# Screening Modal Changelog: Layout, Format Sel Modified By dan Action, Tooltip, dan Tutup Modal

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sinta Maharani (Tabel A1 TC) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Tabel A4 (14 entri Changelog File Manager; format tanggal General Settings default `dd/MM/yy HH:mm`). Dataset disiapkan lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme dan endpoint seeding tidak didefinisikan di TC, lihat Temuan untuk QA). Entri literal sesuai Tabel A4 karena asersi urutan, format sel, dan jumlah bergantung pada nilainya (pengecualian setara S-12: seeding idempotent, suite serial). Spec hanya membaca data; tidak ada aksi tulis dan tidak ada data dinamis.
- Suite serial (`parallel: false`): hitungan "14 entri" hanya valid bila tidak ada spec lain yang menghasilkan entri Changelog bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > File Manager.
- State global yang dipulihkan: tidak ada.
- Kemampuan teknis: mengarahkan kursor ke nilai sel Modified By dan ikon toolbar untuk membaca tooltip; membedakan teks polos dari badge pada sel Action.

## Test Steps

1. Klik ikon Changelog di toolbar

### TC-GS-FILEMGR-28: Screening modal Changelog File Manager

2. Verifikasi judul modal "Changelog: File Manager"
3. Verifikasi Table Tools `Search | Filter | Download`
4. Verifikasi kolom Body berurutan `Date (sortable) | Action (sortable) | File Name (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Column Visibility (⋯)`, dengan `Column Visibility (⋯)` unsortable (klik header membuka overlay Column Visibility)
5. Verifikasi tidak ada kolom Checkbox, tidak ada bulk action, dan tidak ada row action
6. Verifikasi urutan default Date Newest First: entri 14/09/26 02:00 di baris pertama
7. Verifikasi Footer pagination default 10 baris per halaman (14 entri menjadi 2 halaman)

### TC-GS-FILEMGR-29: Format sel Changelog Modified By, Action, dan nilai kosong

8. Verifikasi Modified By baris C01 (14/09/26 02:00) tampil `System` apa adanya
9. Verifikasi Modified By baris C02 (12/09/26 10:10) tampil `Sinta M`
10. Verifikasi Modified By baris C03 (10/09/26 15:00) tampil `Agus W`
11. Verifikasi kolom Action baris C01 tampil sebagai teks polos `Permanently Delete` (bukan badge)
12. Verifikasi Old Value baris C01 `former-avatar.png`
13. Verifikasi New Value baris C01 `—`
14. Arahkan kursor ke nilai Modified By baris C02
15. Verifikasi tooltip `Sinta Maharani`

### TC-GS-FILEMGR-33: Tooltip ikon toolbar dan header kolom Actions pada modal Changelog

16. Arahkan kursor ke ikon Search di toolbar modal
17. Verifikasi tooltip `Search`
18. Arahkan kursor ke ikon Filter
19. Verifikasi tooltip `Filter`
20. Arahkan kursor ke ikon Download
21. Verifikasi tooltip `Download`
22. Arahkan kursor ke ikon (⋯) di header kolom Actions
23. Verifikasi tooltip `Column Visibility`

### TC-GS-FILEMGR-174: Menutup modal Changelog lewat ikon close dan Esc, klik backdrop tidak menutup

24. Klik area gelap di luar modal
25. Verifikasi modal Changelog tetap terbuka
26. Klik ikon close (X) di header modal
27. Verifikasi modal Changelog tertutup
28. Klik ikon Changelog di toolbar lagi
29. Tekan Esc
30. Verifikasi modal Changelog tertutup

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec: 28, 29, 33, 174. Screening dan format sel di awal, tooltip (state sementara) diasersi tepat setelah hover (langkah 15, 17, 19, 21, 23), kasus menutup modal di akhir (prinsip 6).
- Baris C01, C02, dan C03 dibaca pada halaman 1 (entri 14/09/26 02:00 sampai 10/09/26 15:00 berada di tiga baris pertama menurut urutan default Date Newest First); tidak ada perpindahan halaman.
- Langkah 4 mencakup daftar kolom beserta sifat sort sebagai satu daftar utuh; langkah 5 (daftar elemen yang sama-sama tidak ada) memakai anchor kolom pada langkah 4.
- Tidak ada langkah penghubung selain pembukaan ulang modal pada langkah 28 yang diwajibkan TC-GS-FILEMGR-174 langkah 4.
- Temuan untuk QA:
  - Mekanisme dan endpoint seeding Tabel A4 tidak didefinisikan di TC (Q-4); hitungan 14 entri mengasumsikan dataset di-seed ulang per spec dan suite serial (Q-7).
  - Kolom Modified By baris C02 diasersi `Sinta M` berdasarkan Expected b TC-GS-FILEMGR-29 (format `[First Name] [Last Initial]`), sedangkan nilai `System` tampil apa adanya.
