---
id: TC-GS-FILEMGR-E2E-067-storage-perubahan-laporan-dan-topup-kuota
title: "Kartu Storage Usage: Perubahan Angka Menunggu Laporan App Berikutnya dan Top-Up Kuota"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-276
  - TC-GS-FILEMGR-285
coverage:
  web: automated
---

# Kartu Storage Usage: Perubahan Angka Menunggu Laporan App Berikutnya dan Top-Up Kuota

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Sinta Maharani (`Sinta M`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script.
- Suite serial (`parallel: false`) karena spec mengubah laporan Storage dan kuota Client uji. Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE; mekanisme tidak didefinisikan di TC, lihat Temuan untuk QA):
  - Seeding laporan Storage per app dan kuota Client skenario S1 (Tabel A5: kuota 50 GB; Fixed Asset 3.2 GB, Admin Console 1.4 GB, Global Settings 204.8 MB, semuanya 14/09/26 02:00; Total Used 4.8 GB) dan laporan baru Global Settings 104.857.600 byte (`100.0 MB`) pada waktu uji (D10).
  - Top-up Storage 10 GB di License Allocation (Admin Console) sampai alokasi Active (D11, kuota 50 GB menjadi 60 GB); akun dan akses Admin Console untuk langkah ini disediakan tim FE (tidak ada di Tabel A1).
- State global yang diubah: laporan Storage dan kuota Client uji (top-up). Hook `after` (tetap jalan walau spec gagal di tengah) memulihkan laporan Storage awal dan mengembalikan kuota Client uji ke 50 GB lewat kemampuan yang disediakan tim FE.
- Data milik spec (suffix `{runId}-067`, seeding lewat fixture BE di hook `before`): `siti-profile-{runId}-067.png` (salinan F02), file aktif, dan `old-avatar-{runId}-067.png` (salinan R01) di Recycle Bin, dipakai TC-276.
- Dependensi TC (TC-268 kartu Storage Usage) dijalankan sebagai langkah aksi di spec ini.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus permanen lewat API file bersuffix `{runId}-067` yang masih ada; pulihkan laporan dan kuota seperti di atas.

## Test Steps

### TC-GS-FILEMGR-285: Perubahan kuota Storage tercermin pada pembacaan berikutnya

1. Siapkan laporan Storage skenario S1 lewat fixture BE, lalu muat ulang Global Settings > File Manager
2. Verifikasi `Storage Quota` `50.0 GB` sebelum top-up
3. Verifikasi ProgressBar berlabel `9%` sebelum top-up
4. Top-up Storage client sebesar 10 GB lewat License Allocation sampai alokasi Active (D11)
5. Muat ulang halaman File Manager
6. Verifikasi `Storage Quota` `60.0 GB` sesudah top-up
7. Verifikasi ProgressBar berlabel `8%` sesudah top-up
8. Verifikasi `Total Used` tetap `4.8 GB`

### TC-GS-FILEMGR-276: Aksi File Manager tidak mengubah kartu seketika

9. Siapkan ulang laporan Storage skenario S1 (kuota 50 GB) lewat fixture BE, lalu muat ulang Global Settings > File Manager
10. Ketik Search `siti-profile-{runId}-067`, tekan Enter, klik ikon (⋯) baris `siti-profile-{runId}-067.png`, klik `Delete`, lalu klik [Delete]
11. Klik tombol Recycle Bin di toolbar, ketik Search `old-avatar-{runId}-067`, tekan Enter, klik ikon (⋯) baris `old-avatar-{runId}-067.png`, klik `Permanently Delete`, klik [Permanently Delete], lalu tutup modal Recycle Bin lewat `✕`
12. Verifikasi kartu tetap `Global Settings 204.8 MB`
13. Verifikasi `Total Used` tetap `4.8 GB`
14. Muat ulang halaman File Manager
15. Verifikasi kartu tetap `Global Settings 204.8 MB` setelah muat ulang
16. Verifikasi `Total Used` tetap `4.8 GB` setelah muat ulang
17. Picu laporan baru Global Settings lewat fixture BE (D10), lalu muat ulang halaman File Manager
18. Verifikasi daftar app memuat `Global Settings 100.0 MB`
19. Verifikasi `Total Used` `4.7 GB`
20. Verifikasi `Last updated 14/09/26 02:00` (laporan paling lama di antara tiga app: Fixed Asset dan Admin Console)
21. Verifikasi laporan baru menggantikan laporan Global Settings sebelumnya (tepat satu baris `Global Settings` pada daftar app)

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Sinkronisasi lintas modul (Admin Console License Allocation untuk TC-285).
- Urutan TC di spec berbeda dari sumber (285, lalu 276): TC-276 menghapus dan menghapus permanen file sehingga ditaruh paling akhir (prinsip 5). Karena TC-285 mengubah kuota menjadi 60 GB dan TC-276 mensyaratkan S1 (kuota 50 GB), langkah 9 menyiapkan ulang S1.
- Nilai turunan (Q-14): 4.8/50 = 9.6% menjadi `9%`; 4.8/60 = 8%; 3.2 + 1.4 + 0.1 = 4.7 GB (`Total Used` memakai byte penuh: 3.435.973.837 + 1.503.238.554 + 104.857.600 = 5.044.069.991 byte, `4.7 GB`).
- Nama Pre-setup literal pada TC-276 (`siti-profile.png`, `old-avatar.png`) diganti salinan bersuffix milik spec (S-06, S-12).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 dan 9 (menyiapkan skenario S1), langkah 5 (muat ulang pembacaan berikutnya, TC-285 langkah 3), langkah 10 dan 11 (Search nama bersuffix sebelum aksi).
- Temuan untuk QA:
  - Mekanisme seeding laporan Storage dan akun/akses License Allocation tidak didefinisikan di TC (Q-4); ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa mengarang endpoint. Pemulihan kuota setelah top-up juga tidak didefinisikan.
  - TC-276 butir c menulis "(laporan paling lama di antara tiga app: Fixed Asset dan Admin Console)"; spec mengasersi `Last updated 14/09/26 02:00` sesuai angka TC.
