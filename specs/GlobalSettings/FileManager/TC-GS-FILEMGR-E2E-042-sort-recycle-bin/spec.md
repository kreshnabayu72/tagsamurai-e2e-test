---
id: TC-GS-FILEMGR-E2E-042-sort-recycle-bin
title: "Sort Modal Recycle Bin: File Name, File Format, Nama Lengkap, Size, Deleted Date, dan Auto-Purge In"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-213
  - TC-GS-FILEMGR-214
  - TC-GS-FILEMGR-215
  - TC-GS-FILEMGR-216
  - TC-GS-FILEMGR-217
coverage:
  web: automated
---

# Sort Modal Recycle Bin: File Name, File Format, Nama Lengkap, Size, Deleted Date, dan Auto-Purge In

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sinta Maharani (Tabel A1 TC) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Tabel A3 (16 baris Recycle Bin, retensi default Lifecycle Settings 30 hari, Deleted Date relatif terhadap waktu uji). Dataset disiapkan lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme dan endpoint seeding tidak didefinisikan di TC, lihat Temuan untuk QA). Nama file literal sesuai Tabel A3 karena asersi sort bergantung pada nama, ukuran, Deleted By, dan Auto-Purge In (pengecualian setara S-12: seeding idempotent, suite serial). Setiap kolom yang di-sort memiliki sedikitnya dua nilai distinct pada Tabel A3 (S-11). Spec hanya membaca data; tidak ada aksi tulis dan tidak ada data dinamis.
- Suite serial (`parallel: false`): urutan hanya valid bila tidak ada spec lain yang menambah atau menghapus file Recycle Bin bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > File Manager.
- State global yang dipulihkan: tidak ada.
- Kemampuan teknis: membaca urutan baris dan indikator sort pada header kolom.

## Test Steps

1. Klik tombol Recycle Bin di toolbar

### TC-GS-FILEMGR-213: Siklus sort File Name dan File Format

2. Klik header File Name sekali
3. Verifikasi lima baris pertama berurutan: `due-photo.png`, `expired-avatar.jpg`, `legacy-photo.jpeg`, `old-avatar.png`, `recycled-photo-01.jpg`
4. Klik header File Name lagi
5. Verifikasi baris pertama `recycled-photo-12.jpg`
6. Klik header File Name sekali lagi
7. Verifikasi indikator sort pada File Name hilang
8. Verifikasi urutan kembali default Deleted Date terbaru (`old-avatar.png` pertama)
9. Klik header File Format sekali
10. Verifikasi baris pertama `legacy-photo.jpeg` (JPEG)

### TC-GS-FILEMGR-214: Siklus sort User Name dan Deleted By berdasarkan nama lengkap

11. Klik header User Name sekali
12. Verifikasi `old-avatar.png` (`Budi Santoso`) berada di atas `legacy-photo.jpeg` (`Siti Rahmawati`)
13. Klik header User Name lagi
14. Verifikasi `legacy-photo.jpeg` berada di atas `old-avatar.png`
15. Klik header Deleted By sekali
16. Verifikasi baris pertama `recycled-photo-05.jpg` (`Agus Wibowo`, ID terkecil di antara baris Agus; tie-break ID searah sort Ascending)
17. Klik header Deleted By lagi
18. Verifikasi baris pertama `recycled-photo-09.jpg` (`System`, ID terbesar di antara baris System; tie-break ID searah sort Descending)

### TC-GS-FILEMGR-215: Siklus sort Size berdasarkan nilai byte

19. Klik header Size sekali
20. Verifikasi baris pertama `recycled-photo-01.jpg` (`100.0 KB`)
21. Klik header Size lagi
22. Verifikasi empat baris pertama berurutan: `old-avatar.png` (`2.0 MB`), `legacy-photo.jpeg` (`1.8 MB`), `expired-avatar.jpg` (`1.0 MB`), `due-photo.png` (`700.0 KB`)

### TC-GS-FILEMGR-216: Siklus sort Deleted Date

23. Klik header Deleted Date sekali
24. Verifikasi baris pertama `due-photo.png` (Oldest First)
25. Klik header Deleted Date lagi
26. Verifikasi baris pertama `old-avatar.png` (Newest First)
27. Klik header Deleted Date sekali lagi
28. Verifikasi indikator sort pada Deleted Date hilang
29. Verifikasi urutan kembali default Newest First (`old-avatar.png` pertama)

### TC-GS-FILEMGR-217: Siklus sort Auto-Purge In berdasarkan sisa waktu

30. Klik header Auto-Purge In sekali
31. Verifikasi tiga baris pertama berurutan: `due-photo.png` (`0 days`), `expired-avatar.jpg` (`1 day`), `legacy-photo.jpeg` (`12 days`)
32. Klik header Auto-Purge In lagi
33. Verifikasi dua baris pertama berurutan: `old-avatar.png` (`29 days`), `recycled-photo-01.jpg` (`28 days`)

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber dipertahankan (213 sampai 217). Mengklik header kolom lain menggantikan sort kolom sebelumnya, sehingga tidak ada langkah pembersih di antara blok kecuali siklus ketiga klik yang mengembalikan default pada TC-GS-FILEMGR-213 (langkah 6) dan TC-GS-FILEMGR-216 (langkah 27). Sort terakhir TC-GS-FILEMGR-214 sampai TC-GS-FILEMGR-215 dan TC-GS-FILEMGR-217 tidak dikembalikan ke default karena tidak ada TC berikutnya yang bergantung pada urutan default; hook `beforeEach` suite membuka ulang File Manager di spec lain.
- Seluruh blok mengasersi urutan baris pertama atau beberapa baris pertama; tidak ada asersi universal sehingga tidak perlu baris pembanding terpisah (tabel Recycle Bin yang berisi baris dibuktikan oleh asersi baris itu sendiri).
- Temuan untuk QA:
  - TC-GS-FILEMGR-214 butir c dan d: tie-break "ID" tidak konsisten dengan data Tabel A3 bila ID diurut menurut kode R01 sampai R16. Baris Agus Wibowo mencakup `expired-avatar.jpg` (R03) yang lebih awal daripada `recycled-photo-05.jpg`, dan baris System mencakup `recycled-photo-12.jpg` yang lebih akhir daripada `recycled-photo-09.jpg`. Hasil yang diharapkan hanya konsisten bila ID dialokasikan oleh fixture BE dengan urutan tertentu yang tidak disebut TC. Spec mengikuti TC (langkah 16 dan 18); perlu definisi ID pada Tabel A3 atau koreksi expected.
  - Mekanisme dan endpoint seeding Tabel A3 tidak didefinisikan di TC (Q-4); hitungan dan urutan mengasumsikan dataset di-seed ulang per spec dan suite serial (Q-7).
  - `due-photo.png` (sekarang − 31 hari, `0 days`) tampil sampai job auto-purge berikutnya; bila job berjalan antara seeding dan asersi, langkah 3, 22, 24, 31 menjadi tidak stabil (Q-3).
  - Nilai Auto-Purge In `0 days`, `1 day`, `12 days`, `29 days`, `28 days` diturunkan dari Deleted Date dan retensi 30 hari (Q-14); aritmetika konsisten dengan Tabel A3.
