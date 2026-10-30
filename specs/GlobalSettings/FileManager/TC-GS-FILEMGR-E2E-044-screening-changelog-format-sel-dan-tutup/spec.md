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
- Suite serial (`parallel: false`). Changelog adalah audit trail permanen yang tidak dapat di-seed ulang atau dibersihkan dan spec lain menambah entri (S-12), sehingga hitungan entri tidak diasersi sebagai total absolut: hitungan dibatasi dengan Filter Date rentang Date Tabel A4 (`23/08/26` sampai `14/09/26`, inklusif; entri terlama 23/08/26 08:00 dan terbaru 14/09/26 02:00) yang hanya memuat populasi Tabel A4. Urutan default dan hitungan halaman diasersi pada tabel yang sudah dibatasi Filter Date tersebut (langkah 6).
- Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > File Manager.
- State global yang dipulihkan: tidak ada.
- Kemampuan teknis: memilih rentang Date `23/08/26` sampai `14/09/26` pada date range picker Filter Panel Changelog (Date entri Tabel A4 tetap, bukan relatif); mengarahkan kursor ke nilai sel Modified By dan ikon toolbar untuk membaca tooltip; membedakan teks polos dari badge pada sel Action.

## Test Steps

1. Klik ikon Changelog di toolbar

### TC-GS-FILEMGR-28: Screening modal Changelog File Manager

2. Verifikasi judul modal "Changelog: File Manager"
3. Verifikasi Table Tools `Search | Filter | Download`
4. Verifikasi kolom Body berurutan `Date (sortable) | Action (sortable) | File Name (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Column Visibility (⋯)`, dengan `Column Visibility (⋯)` unsortable (klik header membuka overlay Column Visibility)
5. Verifikasi tidak ada kolom Checkbox, tidak ada bulk action, dan tidak ada row action
6. Klik ikon Filter di toolbar modal, pilih Date `23/08/26` sampai `14/09/26`, klik `[Apply]`, lalu tutup Filter Panel dengan klik ikon Filter
7. Verifikasi urutan default Date Newest First pada rentang Date Tabel A4: entri 14/09/26 02:00 di baris pertama
8. Verifikasi Footer pagination default 10 baris per halaman (14 entri dalam rentang Date Tabel A4 menjadi 2 halaman)

### TC-GS-FILEMGR-29: Format sel Changelog Modified By, Action, dan nilai kosong

9. Verifikasi Modified By baris C01 (14/09/26 02:00) tampil `System` apa adanya
10. Verifikasi Modified By baris C02 (12/09/26 10:10) tampil `Sinta M`
11. Verifikasi Modified By baris C03 (10/09/26 15:00) tampil `Agus W`
12. Verifikasi kolom Action baris C01 tampil sebagai teks polos `Permanently Delete` (bukan badge)
13. Verifikasi Old Value baris C01 `former-avatar.png`
14. Verifikasi New Value baris C01 `—`
15. Arahkan kursor ke nilai Modified By baris C02
16. Verifikasi tooltip `Sinta Maharani`

### TC-GS-FILEMGR-33: Tooltip ikon toolbar dan header kolom Actions pada modal Changelog

17. Arahkan kursor ke ikon Search di toolbar modal
18. Verifikasi tooltip `Search`
19. Arahkan kursor ke ikon Filter
20. Verifikasi tooltip `Filter`
21. Arahkan kursor ke ikon Download
22. Verifikasi tooltip `Download`
23. Arahkan kursor ke ikon (⋯) di header kolom Actions
24. Verifikasi tooltip `Column Visibility`

### TC-GS-FILEMGR-174: Menutup modal Changelog lewat ikon close dan Esc, klik backdrop tidak menutup

25. Klik area gelap di luar modal
26. Verifikasi modal Changelog tetap terbuka
27. Klik ikon close (X) di header modal
28. Verifikasi modal Changelog tertutup
29. Klik ikon Changelog di toolbar lagi
30. Tekan Esc
31. Verifikasi modal Changelog tertutup

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec: 28, 29, 33, 174. Screening dan format sel di awal, tooltip (state sementara) diasersi tepat setelah hover (langkah 16, 18, 20, 22, 24), kasus menutup modal di akhir (prinsip 6).
- Baris C01, C02, dan C03 dibaca pada halaman 1 (entri 14/09/26 02:00 sampai 10/09/26 15:00 berada di tiga baris pertama menurut urutan default Date Newest First); tidak ada perpindahan halaman.
- Langkah 4 mencakup daftar kolom beserta sifat sort sebagai satu daftar utuh; langkah 5 (daftar elemen yang sama-sama tidak ada) memakai anchor kolom pada langkah 4.
- Langkah penghubung tambahan: langkah 6 (Filter Date rentang Tabel A4 agar urutan default dan hitungan 14 entri hanya dari populasi Tabel A4; tidak ada di TC, dicatat per S-03). Tidak ada langkah penghubung lain selain pembukaan ulang modal pada langkah 29 yang diwajibkan TC-GS-FILEMGR-174 langkah 4.
- Temuan untuk QA:
  - Mekanisme dan endpoint seeding Tabel A4 tidak didefinisikan di TC (Q-4).
  - TC sumber (mis. TC-GS-FILEMGR-172 dan TC Changelog sejenis) menyatakan hitungan entri absolut ("14 entri", "5 baris") yang bertentangan dengan S-12 (Changelog tidak dapat di-seed ulang atau dibersihkan). Spec membatasi dengan Filter Date rentang Tabel A4 sebagai langkah penghubung; pemilik TC perlu menulis ulang Data Uji sebagai Filter Date rentang Tabel A4 atau hitungan relatif. Urutan default (entri teratas) juga tidak stabil tanpa Filter Date karena entri spec lain lebih baru dari 14/09/26 02:00.
  - Kolom Modified By baris C02 diasersi `Sinta M` berdasarkan Expected b TC-GS-FILEMGR-29 (format `[First Name] [Last Initial]`), sedangkan nilai `System` tampil apa adanya.
