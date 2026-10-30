---
id: TC-GS-FILEMGR-E2E-048-sort-changelog
title: "Sort Modal Changelog: Date, Action, File Name, Old Value, Modified By, dan Kolom Bernilai Sama"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-168
  - TC-GS-FILEMGR-169
  - TC-GS-FILEMGR-170
  - TC-GS-FILEMGR-171
coverage:
  web: automated
---

# Sort Modal Changelog: Date, Action, File Name, Old Value, Modified By, dan Kolom Bernilai Sama

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sinta Maharani (Tabel A1 TC) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Tabel A4 (14 entri Changelog File Manager; format tanggal General Settings default `dd/MM/yy HH:mm`). Dataset disiapkan lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme dan endpoint seeding tidak didefinisikan di TC, lihat Temuan untuk QA). Entri literal sesuai Tabel A4 karena asersi sort bergantung pada nilai Action, File Name, Old Value, dan Modified By (pengecualian setara S-12: seeding idempotent, suite serial). Kolom yang di-sort memiliki sedikitnya dua nilai distinct pada Tabel A4 (S-11), kecuali Field dan New Value yang sengaja bernilai sama (TC-GS-FILEMGR-171). Spec hanya membaca data; tidak ada aksi tulis dan tidak ada data dinamis.
- Suite serial (`parallel: false`): urutan hanya valid bila tidak ada spec lain yang menghasilkan entri Changelog bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > File Manager.
- State global yang dipulihkan: tidak ada.
- Kemampuan teknis: membaca urutan baris dan indikator sort pada header kolom; berpindah halaman pagination.

## Test Steps

1. Klik ikon Changelog di toolbar

### TC-GS-FILEMGR-168: Siklus sort kolom Date dengan default Newest First

2. Verifikasi baris pertama C01 (`former-avatar.png`)
3. Klik header Date sekali
4. Verifikasi baris pertama `archive-photo-09.jpg` (Oldest First)
5. Klik header Date lagi
6. Verifikasi baris pertama C01 (Newest First)
7. Klik header Date sekali lagi
8. Verifikasi indikator sort pada Date hilang
9. Verifikasi urutan kembali default Newest First (C01 pertama)

### TC-GS-FILEMGR-169: Siklus sort kolom Action, File Name, dan Old Value

10. Klik header Action sekali
11. Verifikasi dua baris pertama memiliki Action `Delete` (C04 dan C05)
12. Klik header Action lagi
13. Verifikasi baris pertama memiliki Action `Permanently Delete` dan adalah C01
14. Klik header File Name sekali
15. Verifikasi baris pertama `archive-photo-01.jpg`
16. Klik header File Name lagi
17. Verifikasi baris pertama `stale-avatar.png`
18. Klik header Old Value sekali
19. Verifikasi baris pertama `archive-photo-01.jpg`

### TC-GS-FILEMGR-170: Siklus sort kolom Modified By berdasarkan nama lengkap

20. Klik header Modified By sekali
21. Verifikasi baris pertama C03 (`Agus Wibowo`, entri terbaru di antara baris Agus)
22. Klik header Modified By lagi
23. Verifikasi baris pertama C01 (`System`, entri terbaru di antara baris System)

### TC-GS-FILEMGR-171: Sort kolom Field dan New Value saat seluruh entri bernilai sama

24. Klik header Field sekali
25. Verifikasi seluruh entri bernilai `File Name` dan urutan mengikuti default Date Newest First (C01 pertama)
26. Klik header Field sekali lagi
27. Verifikasi seluruh entri bernilai `File Name` dan urutan mengikuti default Date Newest First (C01 pertama)
28. Klik header New Value sekali
29. Verifikasi seluruh entri bernilai `—` dan urutan mengikuti default Date Newest First
30. Catat File Name seluruh entri halaman 1, pindah ke halaman 2, lalu catat File Name seluruh entri halaman 2
31. Verifikasi keempat belas File Name (10 dari halaman 1 dan 4 dari halaman 2) muncul tepat sekali, yaitu 14 nilai distinct sama dengan Tabel A4

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber dipertahankan (168 sampai 171). Mengklik header kolom lain menggantikan sort kolom sebelumnya, sehingga tidak ada langkah pembersih di antara blok.
- Langkah 30 dan 31 adalah langkah observasi tambahan (S-03) untuk Expected c TC-GS-FILEMGR-171 ("tidak ada baris ganda atau terlewat antar halaman"), yang tidak memiliki langkah pindah halaman di TC. Langkah 30 mencatat File Name semua entri halaman 1 dan 2; langkah 31 memverifikasi keempat belas File Name muncul tepat sekali (14 nilai distinct sama dengan Tabel A4), seperti TC-GS-FILEMGR-148 pada spec 035 langkah 55 dan 56.
- Langkah 25 dan 27 serta 29 (asersi "seluruh entri") didahului baris pembanding pada langkah 2 dan 21 (tabel Changelog termuat dengan entri).
- Tidak ada langkah penghubung.
- Temuan untuk QA:
  - TC-GS-FILEMGR-171 Expected c tidak menyebut cara mengamati "baris ganda atau terlewat antar halaman" dan Langkah TC tidak memuat pindah halaman; spec menambahkan langkah 30 dan 31 sebagai observasi (pencatatan dan pencocokan File Name antar halaman).
  - Mekanisme dan endpoint seeding Tabel A4 tidak didefinisikan di TC (Q-4); hitungan entri mengasumsikan dataset di-seed ulang per spec dan suite serial (Q-7).
