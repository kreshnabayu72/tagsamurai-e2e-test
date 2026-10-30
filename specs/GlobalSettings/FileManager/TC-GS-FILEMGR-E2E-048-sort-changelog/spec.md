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
- Suite serial (`parallel: false`). Changelog adalah audit trail permanen yang tidak dapat di-seed ulang atau dibersihkan dan spec lain menambah entri (S-12), sehingga urutan default, posisi "baris pertama", dan hitungan entri tidak diasersi pada seluruh Changelog: tabel dibatasi dengan Filter Date rentang Date Tabel A4 (`23/08/26` sampai `14/09/26`, inklusif; entri terlama 23/08/26 08:00 dan terbaru 14/09/26 02:00) yang hanya memuat populasi Tabel A4 (langkah 2).
- Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > File Manager.
- State global yang dipulihkan: tidak ada.
- Kemampuan teknis: memilih rentang Date `23/08/26` sampai `14/09/26` pada date range picker Filter Panel Changelog (Date entri Tabel A4 tetap, bukan relatif); membaca urutan baris dan indikator sort pada header kolom; berpindah halaman pagination.

## Test Steps

1. Klik ikon Changelog di toolbar
2. Klik ikon Filter di toolbar modal, pilih Date `23/08/26` sampai `14/09/26`, klik `[Apply]`, lalu tutup Filter Panel dengan klik ikon Filter

### TC-GS-FILEMGR-168: Siklus sort kolom Date dengan default Newest First

3. Verifikasi baris pertama C01 (`former-avatar.png`)
4. Klik header Date sekali
5. Verifikasi baris pertama `archive-photo-09.jpg` (Oldest First)
6. Klik header Date lagi
7. Verifikasi baris pertama C01 (Newest First)
8. Klik header Date sekali lagi
9. Verifikasi indikator sort pada Date hilang
10. Verifikasi urutan kembali default Newest First (C01 pertama)

### TC-GS-FILEMGR-169: Siklus sort kolom Action, File Name, dan Old Value

11. Klik header Action sekali
12. Verifikasi dua baris pertama memiliki Action `Delete` (C04 dan C05)
13. Klik header Action lagi
14. Verifikasi baris pertama memiliki Action `Permanently Delete` dan adalah C01
15. Klik header File Name sekali
16. Verifikasi baris pertama `archive-photo-01.jpg`
17. Klik header File Name lagi
18. Verifikasi baris pertama `stale-avatar.png`
19. Klik header Old Value sekali
20. Verifikasi baris pertama `archive-photo-01.jpg`

### TC-GS-FILEMGR-170: Siklus sort kolom Modified By berdasarkan nama lengkap

21. Klik header Modified By sekali
22. Verifikasi baris pertama C03 (`Agus Wibowo`, entri terbaru di antara baris Agus)
23. Klik header Modified By lagi
24. Verifikasi baris pertama C01 (`System`, entri terbaru di antara baris System)

### TC-GS-FILEMGR-171: Sort kolom Field dan New Value saat seluruh entri bernilai sama

25. Klik header Field sekali
26. Verifikasi seluruh entri bernilai `File Name` dan urutan mengikuti default Date Newest First (C01 pertama)
27. Klik header Field sekali lagi
28. Verifikasi seluruh entri bernilai `File Name` dan urutan mengikuti default Date Newest First (C01 pertama)
29. Klik header New Value sekali
30. Verifikasi seluruh entri bernilai `—` dan urutan mengikuti default Date Newest First
31. Catat File Name seluruh entri halaman 1, pindah ke halaman 2, lalu catat File Name seluruh entri halaman 2
32. Verifikasi seluruh entri dalam rentang Date Tabel A4 (10 dari halaman 1 dan 4 dari halaman 2) memuat keempat belas File Name Tabel A4 masing-masing tepat sekali, yaitu 14 nilai distinct

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber dipertahankan (168 sampai 171). Mengklik header kolom lain menggantikan sort kolom sebelumnya, sehingga tidak ada langkah pembersih di antara blok.
- Langkah 31 dan 32 adalah langkah observasi tambahan (S-03) untuk Expected c TC-GS-FILEMGR-171 ("tidak ada baris ganda atau terlewat antar halaman"), yang tidak memiliki langkah pindah halaman di TC. Langkah 31 mencatat File Name semua entri halaman 1 dan 2 pada tabel yang dibatasi Filter Date; langkah 32 memverifikasi keempat belas File Name Tabel A4 muncul tepat sekali (14 nilai distinct), seperti TC-GS-FILEMGR-148 pada spec 035 langkah 55 dan 56.
- Langkah 26 dan 28 serta 30 (asersi "seluruh entri") didahului baris pembanding pada langkah 3 dan 22 (tabel Changelog termuat dengan entri).
- Langkah penghubung tambahan: langkah 2 (Filter Date rentang Tabel A4 agar urutan default, asersi "baris pertama C01" dan seterusnya, serta pencocokan 14 File Name hanya dari populasi Tabel A4; tidak ada di TC, dicatat per S-03). Tidak ada langkah penghubung lain. Filter Date tetap aktif selama klik header sort (sort tidak mereset Filter).
- Temuan untuk QA:
  - TC-GS-FILEMGR-171 Expected c tidak menyebut cara mengamati "baris ganda atau terlewat antar halaman" dan Langkah TC tidak memuat pindah halaman; spec menambahkan langkah 31 dan 32 sebagai observasi (pencatatan dan pencocokan File Name antar halaman).
  - Mekanisme dan endpoint seeding Tabel A4 tidak didefinisikan di TC (Q-4); Changelog tidak dapat di-seed ulang atau dibersihkan dan spec lain menambah entri lebih baru dari 14/09/26 02:00 (S-12), sehingga spec membatasi tabel dengan Filter Date rentang Tabel A4 (Q-7).
  - Langkah 2 mengasumsikan Filter Panel Changelog dapat ditutup lewat klik ikon Filter setelah `[Apply]` dan Filter Date tetap aktif saat sort diganti; asumsi ini tidak ada di TC maupun PRD.
  - TC-GS-FILEMGR-168 sampai 171 menyatakan urutan default dan baris pertama (C01) tanpa Filter Date; pemilik TC perlu menambahkan Filter Date rentang Tabel A4 pada Data Uji.
