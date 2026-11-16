---
id: TC-GS-FILEMGR-E2E-072-rename-user-user-name-mengikuti-nama-terkini
title: "Rename User: User Name Mengikuti Nama Terkini di Tabel Utama dan Recycle Bin, Uploaded By Tetap, dan Search Memakai Nama Terkini"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-FILEMGR-290
  - TC-GS-FILEMGR-291
coverage:
  web: automated
---

# Rename User: User Name Mengikuti Nama Terkini di Tabel Utama dan Recycle Bin, Uploaded By Tetap, dan Search Memakai Nama Terkini

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Sinta Maharani (`Sinta M`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Akun ini hanya mengubah nama akun klon milik spec di bawah, bukan dirinya sendiri. Halaman awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script.
- Suite serial (`parallel: false`). Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Data milik spec (suffix `{runId}-072`, seeding lewat fixture BE di hook `before`; mekanisme seeding tidak didefinisikan di TC, disediakan tim FE/BE). TC-290 mengubah nama pemilik file Pre-setup (Budi Santoso); karena Pre-setup bersama tidak boleh diubah (S-06), spec memakai akun klon (disediakan tim FE, email tidak tertulis di Pre-setup TC, lihat Temuan untuk QA):
  - Akun klon `Budi Santoso {runId}-072` (tampil `Budi S`) sebagai pemilik tiga file: `budi-avatar-{runId}-072.jpg` (JPG, foto profil aktif, Uploaded By akun klon itu, salinan F01), `old-avatar-{runId}-072.png` dan `expired-avatar-{runId}-072.jpg` (di Recycle Bin, Deleted Date belum melewati retensi, salinan R01 dan R03).
- Dependensi TC (TC-04 tampilan User Name dan tooltip, TC-290 untuk TC-291) dijalankan sebagai langkah aksi di spec ini.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus akun klon bersuffix `{runId}-072` yang masih ada (termasuk setelah rename) dan hapus permanen file bersuffix `{runId}-072`.
- Tidak ada state global yang diubah.

## Test Steps

### TC-GS-FILEMGR-290: Rename user mengubah User Name pada tabel utama dan Recycle Bin tanpa mengubah Uploaded By

1. Klik ikon Changelog di toolbar, ketik Search `{runId}-072`, tekan Enter
2. Catat jumlah entri Changelog untuk file bersuffix `{runId}-072` sebagai baseline
3. Tutup modal Changelog lewat `✕`
4. Di Global Settings > User ubah nama `Budi Santoso {runId}-072` menjadi `Budi Prasetyo {runId}-072`, lalu klik [Save]
5. Tunggu aksi selesai
6. Buka Global Settings > File Manager, klik ikon Search, ketik `{runId}-072`, tekan Enter
7. Verifikasi User Name `budi-avatar-{runId}-072.jpg` tampil `Budi P`
8. Arahkan kursor ke User Name `budi-avatar-{runId}-072.jpg`
9. Verifikasi tooltip menampilkan `Budi Prasetyo {runId}-072`
10. Verifikasi Uploaded By `budi-avatar-{runId}-072.jpg` tetap `Budi S`
11. Klik tombol Recycle Bin di toolbar, ketik Search `{runId}-072`, tekan Enter
12. Verifikasi User Name `old-avatar-{runId}-072.png` tampil `Budi P`
13. Verifikasi User Name `expired-avatar-{runId}-072.jpg` tampil `Budi P`
14. Tutup modal Recycle Bin lewat `✕`
15. Klik ikon Changelog di toolbar, ketik Search `{runId}-072`, tekan Enter
16. Verifikasi jumlah entri Changelog untuk file bersuffix `{runId}-072` sama dengan baseline (rename tidak menambah entri)
17. Tutup modal Changelog lewat `✕`

### TC-GS-FILEMGR-291: Search User Name memakai nama terkini setelah rename user

18. Muat ulang halaman Global Settings > File Manager, klik ikon Search, ketik `Prasetyo {runId}-072`, tekan Enter
19. Verifikasi baris `budi-avatar-{runId}-072.jpg` tampil dengan User Name `Budi P`
20. Hapus teks Search, ketik `Santoso {runId}-072`, tekan Enter
21. Verifikasi baris `budi-avatar-{runId}-072.jpg` tidak tampil
22. Klik tombol Recycle Bin di toolbar, klik ikon Search, ketik `Prasetyo {runId}-072`, tekan Enter
23. Verifikasi baris `old-avatar-{runId}-072.png` dan `expired-avatar-{runId}-072.jpg` tampil
24. Tutup modal Recycle Bin lewat `✕`

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Kelas sinkronisasi nama owner (Derived view pada User Name; Snapshot pada Uploaded By); P-3 tidak dipakai, spec memakai satu akun klon sendiri.
- Urutan TC sama dengan sumber (290, 291): TC-291 memakai hasil rename TC-290 sehingga tidak perlu rename kedua.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 sampai 3 (baseline Changelog untuk klausa "tidak menambah entri"), langkah 5 (Tunggu aksi selesai), langkah 6, 11, 14, 15, 17, 18, 22, 24 (membuka dan menutup surface serta Search entri target; TC sumber menyebut "baca User Name ... baris `budi-avatar.jpg`" lewat kode Pre-setup).
- TC-290 dan TC-291 menyebut `budi-avatar.jpg`, `old-avatar.png`, dan `expired-avatar.jpg` Pre-setup; spec menggantinya dengan salinan bersuffix milik akun klon. Search memakai suffix atau nama bersuffix agar tidak mengenai baris Pre-setup lain.
- Temuan untuk QA:
  - Akun klon `Budi Santoso` tidak ada di Tabel A1; email dan pembuatannya disediakan tim FE.
  - TC-290 Expected e menyebut "tidak menambah entri" tanpa angka; spec memakai baseline jumlah entri.
  - TC-291 Expected b tidak menyebut apakah Uploaded By ikut dicari; PRD §4.4 menetapkan Search hanya pada nama file dan nama user, sehingga spec mengasersi baris tidak tampil.
