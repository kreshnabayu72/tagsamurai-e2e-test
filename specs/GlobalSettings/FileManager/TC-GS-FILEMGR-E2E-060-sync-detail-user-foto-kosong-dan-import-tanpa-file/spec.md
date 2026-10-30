---
id: TC-GS-FILEMGR-E2E-060-sync-detail-user-foto-kosong-dan-import-tanpa-file
title: "Sinkronisasi: Detail User Foto Kosong setelah Delete dan Import Tidak Menyimpan File ke File Manager"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-238
  - TC-GS-FILEMGR-242
coverage:
  web: automated
---

# Sinkronisasi: Detail User Foto Kosong setelah Delete dan Import Tidak Menyimpan File ke File Manager

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Sinta Maharani (`Sinta M`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script.
- Suite serial (`parallel: false`). Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Data (seeding lewat fixture BE di hook `before`; mekanisme seeding tidak didefinisikan di TC, disediakan tim FE/BE):
  - Data Pre-setup Tabel A2 (33 file aktif) di-seed idempotent dan hanya dibaca oleh TC-242 (tidak diubah). Jumlah baris tabel utama N dan jumlah baris Recycle Bin M dicatat pada langkah 1 sebelum Import; N diturunkan dari seeding (33 pada Pre-setup suite serial, lihat Temuan untuk QA), bukan dari satu halaman tabel.
  - User milik spec `Siti Rahmawati {runId}-060` dengan foto profil aktif `siti-profile-{runId}-060.png` (salinan F02), dipakai TC-238.
  - File CSV Import user yang berisi satu baris valid (user bersuffix `{runId}-060`) dan satu baris error, disediakan tim FE.
- Dependensi TC (TC-64 Delete single) dijalankan sebagai langkah aksi di spec ini.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus user milik spec dan user hasil Import bersuffix `{runId}-060`, hapus permanen file bersuffix `{runId}-060`.
- Tidak ada state global yang diubah.

## Test Steps

### TC-GS-FILEMGR-242: Import tidak menyimpan file sumber atau laporan error ke File Manager

1. Catat jumlah baris tabel utama (N) dari seeding, klik tombol Recycle Bin di toolbar, catat jumlah baris Recycle Bin (M), lalu tutup modal Recycle Bin lewat `✕`
2. Buka Global Settings > Import dan jalankan Import user dengan satu file CSV valid dan satu baris error
3. Tunggu aksi selesai
4. Buka Global Settings > File Manager
5. Verifikasi tabel utama memuat N baris
6. Ketik Search `.csv`, tekan Enter
7. Verifikasi tabel utama tidak memuat file CSV Import maupun laporan error (empty state "No results found")
8. Klik `(←)` pada kotak Search, lalu klik tombol Recycle Bin di toolbar
9. Verifikasi Recycle Bin memuat M baris tanpa file baru
10. Tutup modal Recycle Bin lewat `✕`

### TC-GS-FILEMGR-238: Detail User pemilik menampilkan foto kosong setelah Delete file foto aktif

11. Ketik Search `siti-profile-{runId}-060`, tekan Enter
12. Klik ikon (⋯) baris `siti-profile-{runId}-060.png`, klik `Delete`, lalu klik [Delete]
13. Tunggu aksi selesai
14. Buka Global Settings > User > Detail User `Siti Rahmawati {runId}-060`
15. Verifikasi header Detail User menampilkan avatar kosong tanpa foto
16. Verifikasi tidak ada tautan ke file `siti-profile-{runId}-060.png` di Detail User

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Sinkronisasi lintas modul (User, Import).
- Urutan TC di spec berbeda dari sumber (242, 238): TC-238 menghapus file sehingga ditaruh paling akhir, dan hitungan N pada TC-242 tidak boleh terpengaruh Delete (prinsip 5).
- TC-242 mensyaratkan 33 baris (Tabel A2); spec memakai N dari baseline seeding (butir 10 bagian 8b) dan membandingkan jumlah sebelum dan sesudah Import agar asersi tidak bergantung pada spec lain.
- Nama Pre-setup literal pada TC-238 (`siti-profile.png`, user `Siti Rahmawati`) diganti salinan bersuffix milik spec (S-06, S-12).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (baseline N dan M), langkah 3 dan 13 (Tunggu aksi selesai sebelum pindah surface), langkah 4, 10 (menutup modal dan kembali ke File Manager), langkah 6 dan 8 (Search `.csv` sebagai pembanding Expected "tanpa file CSV atau laporan error", lalu mengosongkan Search), langkah 11 (Search nama bersuffix).
- Temuan untuk QA:
  - Langkah Import user di TC-242 ("satu file CSV valid dan satu baris error") tidak menyebut layar dan tombol rinci modul Import; selektor modul lain disediakan tim FE (Q-9).
  - Hitungan 33 baris pada TC-242 bergantung pada dataset Pre-setup yang tidak diubah spec lain (Q-7); spec memakai baseline jumlah sebelum Import.
