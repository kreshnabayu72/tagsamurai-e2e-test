---
id: TC-GS-FILEMGR-E2E-038-screening-recycle-bin-urutan-default-dan-tutup
title: "Screening Modal Recycle Bin: Layout, Urutan Default, Tutup Modal, dan Tooltip"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-16
  - TC-GS-FILEMGR-18
  - TC-GS-FILEMGR-26
  - TC-GS-FILEMGR-27
coverage:
  web: automated
---

# Screening Modal Recycle Bin: Layout, Urutan Default, Tutup Modal, dan Tooltip

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sinta Maharani (Tabel A1 TC) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Tabel A2 (33 file aktif tabel utama) dan Tabel A3 (16 baris Recycle Bin, retensi 30 hari, Deleted Date relatif terhadap waktu uji). Dataset disiapkan lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme dan endpoint seeding tidak didefinisikan di TC, lihat Temuan untuk QA). Nama file literal sesuai Tabel A2/A3 karena asersi urutan dan jumlah bergantung pada nama (pengecualian setara S-12: seeding idempotent, suite serial). Spec hanya membaca data; tidak ada aksi tulis dan tidak ada data dinamis.
- Suite serial (`parallel: false`): hitungan "33 file aktif" dan "16 baris Recycle Bin" hanya valid bila tidak ada spec lain yang menambah atau menghapus file bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > File Manager.
- State global yang dipulihkan: tidak ada.
- Kemampuan teknis: mengarahkan kursor ke ikon toolbar dan header kolom untuk membaca tooltip; membaca jumlah baris dan indikator sort.

## Test Steps

1. Klik tombol Recycle Bin di toolbar

### TC-GS-FILEMGR-16: Screening modal Recycle Bin oleh Total Control

2. Verifikasi judul modal "Recycle Bin"
3. Verifikasi teks info "Files are permanently deleted after 30 days."
4. Verifikasi Table Tools `Search | Filter | Download`
5. Verifikasi kolom Body berurutan `Checkbox | File Name (sortable) | File Format (sortable) | User Name (sortable) | Size (sortable) | Deleted Date (sortable) | Deleted By (sortable) | Auto-Purge In (sortable) | Column Visibility (⋯)`, dengan `Column Visibility (⋯)` unsortable (klik header membuka overlay Column Visibility, body per baris adalah row action menu)
6. Verifikasi baris data halaman pertama memuat nilai Tabel A3: `old-avatar.png` (PNG, User Name `Budi S`, `2.0 MB`, Deleted Date sekarang − 1 hari, Deleted By `Sinta M`, `29 days`) dan `recycled-photo-01.jpg` (JPG, User Name `Ayu L`, `100.0 KB`, Deleted Date sekarang − 2 hari, Deleted By `Sinta M`, `28 days`)
7. Verifikasi Footer pagination default 10 baris per halaman
8. Verifikasi tidak ada tombol Recover maupun Empty All

### TC-GS-FILEMGR-18: Urutan default Recycle Bin Deleted Date terbaru di atas dengan 10 baris per halaman

9. Verifikasi baris pertama `old-avatar.png` (Deleted Date sekarang − 1 hari)
10. Verifikasi tidak ada panah sort aktif pada kolom mana pun
11. Verifikasi halaman pertama memuat 10 baris dari total 16
12. Pindah ke halaman 2
13. Verifikasi baris paling akhir adalah `due-photo.png` (Deleted Date paling lama, sekarang − 31 hari)
14. Verifikasi baris halaman 2 memuat nilai Tabel A3 sisanya (lanjutan TC-GS-FILEMGR-16 butir b.ii): `legacy-photo.jpeg` (JPEG, User Name `Siti R`, `1.8 MB`, sekarang − 18 hari, Deleted By `System`, `12 days`), `expired-avatar.jpg` (JPG, User Name `Budi S`, `1.0 MB`, sekarang − 29 hari, Deleted By `Agus W`, `1 day`), dan `due-photo.png` (PNG, User Name `Dewi K`, `700.0 KB`, sekarang − 31 hari, Deleted By `Sinta M`, `0 days`)

### TC-GS-FILEMGR-27: Tooltip ikon toolbar dan header kolom Actions pada modal Recycle Bin

15. Arahkan kursor ke ikon Search di toolbar modal
16. Verifikasi tooltip `Search`
17. Arahkan kursor ke ikon Filter
18. Verifikasi tooltip `Filter`
19. Arahkan kursor ke ikon Download
20. Verifikasi tooltip `Download`
21. Arahkan kursor ke ikon (⋯) di header kolom Actions
22. Verifikasi tooltip `Column Visibility`

### TC-GS-FILEMGR-26: Menutup modal Recycle Bin lewat ikon close dan Esc, klik backdrop tidak menutup

23. Klik area gelap di luar modal
24. Verifikasi modal Recycle Bin tetap terbuka
25. Verifikasi tidak ada toast
26. Klik ikon close (X) di header modal
27. Verifikasi modal Recycle Bin tertutup
28. Verifikasi tabel utama tampil tanpa perubahan data (total 33 file aktif)
29. Verifikasi tidak ada toast
30. Klik tombol Recycle Bin di toolbar lagi
31. Verifikasi Recycle Bin masih memuat 16 baris (tidak ada mutasi data)
32. Tekan Esc
33. Verifikasi modal Recycle Bin tertutup
34. Verifikasi tidak ada toast

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec: 16, 18, 27, 26. Tooltip (TC-GS-FILEMGR-27, state sementara) diasersi tepat setelah hover; kasus menutup modal (TC-GS-FILEMGR-26) di akhir (prinsip 6).
- Langkah 14 melengkapi TC-GS-FILEMGR-16 butir b.ii ("Baris data memuat nilai Tabel A3") untuk baris yang berada di halaman 2; langkah 6 untuk baris di halaman 1. Langkah 13 dan 14 memakai halaman 2 yang dibuka pada langkah 12 (S-14).
- Absence toast (langkah 25, 29, 34) diletakkan segera setelah pemicu; anchor positifnya modal terbuka/tertutup dan tabel utama yang tampil (butir 11 dan butir 2 bagian 8b).
- Tidak ada langkah penghubung selain pembukaan ulang modal (langkah 30) yang diwajibkan TC-GS-FILEMGR-26 langkah 4.
- Temuan untuk QA:
  - TC-GS-FILEMGR-16 butir b.ii dan Tabel A3 menulis nama lengkap (mis. Budi Santoso, Sinta Maharani, Agus Wibowo), sedangkan UI menampilkan bentuk `[First Name] [Last Initial]` (mis. `Budi S`, `Sinta M`, `Agus W`); spec memakai nilai tampil. TC owner perlu menyelaraskan.
  - Mekanisme dan endpoint seeding Tabel A2/A3 serta kondisi waktu relatif (Deleted Date) tidak didefinisikan di TC; ditulis sebagai kemampuan "disediakan tim FE/BE", tidak ada endpoint karangan (Q-4).
  - `due-photo.png` (Deleted Date sekarang − 31 hari, retensi 30 hari) dinyatakan tetap tampil sampai job auto-purge berikutnya; bila job harian berjalan antara seeding dan asersi, baris ini hilang dan langkah 13 serta 14 menjadi tidak stabil. Dibutuhkan keputusan: job dijeda di environment e2e atau jam dibekukan (Q-3).
  - Hitungan 33 file aktif dan 16 baris Recycle Bin mengasumsikan dataset di-seed ulang per spec dan suite serial (Q-7).
