---
id: TC-GS-FILEMGR-E2E-057-log-auto-transition-dan-auto-purge-aktor-system
title: "Pencatatan Log Auto-Transition dan Auto-Purge: Aktor System dan Aktor Pengguna Pelaku"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-228
  - TC-GS-FILEMGR-229
  - TC-GS-FILEMGR-230
coverage:
  web: automated
---

# Pencatatan Log Auto-Transition dan Auto-Purge: Aktor System dan Aktor Pengguna Pelaku

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Sinta Maharani (`Sinta M`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script.
- Suite serial (`parallel: false`). Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Data milik spec (suffix `{runId}-057`, seeding lewat fixture BE di hook `before`; mekanisme seeding tidak didefinisikan di TC, disediakan tim FE/BE):
  - User milik spec `Budi Santoso {runId}-057` dengan foto profil aktif `budi-avatar-{runId}-057.jpg` (salinan F01), dipakai TC-228. File pengganti `budi-new.png` (file gambar disediakan tim FE).
  - User milik spec `Rudi Hartono {runId}-057` dengan foto profil aktif `rudi-hartono-{runId}-057.png` (salinan F05), dipakai TC-229.
  - `due-photo-{runId}-057.png` (salinan R04) di Recycle Bin dengan Deleted Date lebih tua dari retensi 30 hari (sekarang - 31 hari), dipakai TC-230.
- Kemampuan teknis (disediakan tim FE/BE): pemicu job auto-purge harian lewat fixture BE; langkah ganti dan hapus foto profil di modul User (selektor modul User disediakan tim FE). Batas tunggu job: muat ulang Changelog maksimum 12 kali dengan jeda 5 detik (usulan, dapat disesuaikan tim FE; TC hanya menyebut refresh berulang tanpa batas angka). Job auto-purge harian di environment e2e dijeda kecuali dipicu spec ini, supaya `due-photo-{runId}-057.png` tidak terhapus sebelum langkah 18 (Q-3).
- Baseline log: nama file bersuffix unik, sehingga jumlah entri awal untuk nama itu nol. Baseline jumlah baris System Log `Budi Santoso {runId}-057` dicatat pada langkah 1 sebelum aksi.
- Dependensi TC (TC-106 ganti foto, TC-107 hapus foto, TC-111 auto-purge) dijalankan sebagai langkah aksi di spec ini.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus permanen lewat API file bersuffix `{runId}-057` yang masih ada dan hapus user milik spec.
- Tidak ada state global yang diubah.

## Test Steps

### Persiapan baseline

1. Buka Global Settings > User > Detail User `Budi Santoso {runId}-057` > tab System Log, catat jumlah baris sebagai baseline TC-228, lalu buka Global Settings > File Manager

### TC-GS-FILEMGR-228: Auto-transition ganti foto menulis entri aktor System

2. Di Global Settings > User ganti foto profil `Budi Santoso {runId}-057` dengan `budi-new.png`, lalu klik [Save]
3. Tunggu aksi selesai
4. Buka Global Settings > File Manager, klik ikon Changelog di toolbar, ketik Search `budi-avatar-{runId}-057`, tekan Enter
5. Verifikasi Changelog File Manager: tepat satu baris Action `Delete`, File Name `budi-avatar-{runId}-057.jpg`, Modified By `System`
6. Tutup modal Changelog lewat `✕`, buka Global Settings > User > Detail User `Budi Santoso {runId}-057` > tab System Log, ketik Search `budi-avatar-{runId}-057`, tekan Enter
7. Verifikasi System Log Detail User `Budi Santoso {runId}-057` tidak memuat baris Object `File Manager` untuk `budi-avatar-{runId}-057.jpg` (empty state "No results found")
8. Klik `(←)` pada kotak Search
9. Verifikasi jumlah baris System Log `Budi Santoso {runId}-057` sama dengan baseline langkah 1

### TC-GS-FILEMGR-229: Auto-transition hapus foto menulis entri aktor pengguna pelaku di tiga surface

10. Di Global Settings > User hapus foto profil `Rudi Hartono {runId}-057`, lalu klik [Save]
11. Tunggu aksi selesai
12. Buka Global Settings > File Manager, klik ikon Changelog di toolbar, ketik Search `rudi-hartono-{runId}-057`, tekan Enter
13. Verifikasi Changelog File Manager: tepat satu baris Action `Delete`, File Name `rudi-hartono-{runId}-057.png`, Field `File Name`, Old Value `rudi-hartono-{runId}-057.png`, New Value `—`, Modified By `Sinta M`
14. Tutup modal Changelog lewat `✕`, buka Global Settings > User > Detail User Sinta Maharani > tab System Log, ketik Search `rudi-hartono-{runId}-057`, tekan Enter
15. Verifikasi System Log Detail User Sinta Maharani: tepat satu baris Action `Delete`, Object `File Manager`, Name `rudi-hartono-{runId}-057.png`
16. Buka Global Settings > Activity Log, ketik Search `rudi-hartono-{runId}-057`, tekan Enter
17. Verifikasi Activity Log: tepat satu baris Action `Delete`, Object `File Manager`, Name `rudi-hartono-{runId}-057.png`, Modified By `Sinta M`

### TC-GS-FILEMGR-230: Auto-purge menulis entri Permanently Delete aktor System

18. Picu job auto-purge harian lewat fixture BE
19. Buka Global Settings > File Manager, klik ikon Changelog di toolbar, ketik Search `due-photo-{runId}-057`, tekan Enter; ulangi muat ulang Changelog dan Search hingga baris tampil (batas di Prerequisites)
20. Verifikasi Changelog File Manager: tepat satu baris Action `Permanently Delete`, File Name `due-photo-{runId}-057.png`, Field `File Name`, Old Value `due-photo-{runId}-057.png`, New Value `—`, Modified By `System`

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Kelas pencatatan; pemicu job auto-purge (TC-230) adalah pemicu state, bukan objek uji job itu sendiri (P-2: proses sistem yang hanya memicu kondisi yang diuji). Pengujian job (batas retensi, retry) ada di spec `TC-GS-FILEMGR-E2E-030-auto-purge-job-batas-retensi-floor-dan-retry`.
- Urutan TC sama dengan sumber (228, 229, 230). Tidak ada aksi Delete user atau file oleh pelaku UI yang menghabiskan data sebelum kasus lain.
- Nama Pre-setup literal pada TC (`budi-avatar.jpg`, `rudi-hartono.png`, `due-photo.png`, user `Budi Santoso`, `Rudi Hartono`) diganti salinan bersuffix milik spec karena aksi atas Pre-setup bersama dilarang (S-06) dan "tepat satu baris" butuh nama unik (S-12).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (baseline), langkah 3 dan 11 (Tunggu aksi selesai sebelum pindah surface), langkah 6, 14 (menutup modal dan pindah halaman), langkah 8 (mengosongkan Search sebelum membandingkan jumlah baris), langkah 19 (muat ulang berulang menunggu job).
- Asersi tidak ada baris `File Manager` pada System Log Budi (langkah 7) memakai empty state "No results found" sebagai anchor dan baseline jumlah baris (langkah 1 dan 9); asersi jumlah/state, bukan kelas g (keputusan D-1 opsi B).
- Temuan untuk QA:
  - Langkah ganti/hapus foto di modul User tidak didefinisikan di TC ini (Q-9); selektor modul lain disediakan tim FE.
  - `due-photo.png` yang batas retensinya terlampaui bisa terhapus job harian sebelum langkah pemicu (Q-3); job perlu dijeda di environment e2e atau jam dibekukan.
  - TC-228 tidak menyebut Activity Log untuk entri aktor System; spec mengikuti TC dan tidak mengasersinya.
