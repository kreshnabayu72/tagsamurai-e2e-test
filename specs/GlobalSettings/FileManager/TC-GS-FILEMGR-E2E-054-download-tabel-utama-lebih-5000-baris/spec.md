---
id: TC-GS-FILEMGR-E2E-054-download-tabel-utama-lebih-5000-baris
title: "Download Tabel Utama dengan 5.001 Baris"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-FILEMGR-197
coverage:
  web: automated
---

# Download Tabel Utama dengan 5.001 Baris

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sinta Maharani (Tabel A1 TC) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data (kelas volume, prinsip 13e): tabel utama berisi 5.001 file aktif, disiapkan lewat seed fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme dan endpoint seeding tidak didefinisikan di TC, lihat Temuan untuk QA). Berkas file fisik tidak dibutuhkan. Data seed tambahan ini dihapus di hook `after` (hanya yang dibuat spec ini; pembersihan tidak berasumsi seeding berhasil penuh).
- Suite serial (`parallel: false`): 5.001 file aktif memengaruhi hitungan semua spec tabel utama; spec ini berjalan sendiri dan mengembalikan dataset di `after`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > File Manager.
- State global yang dipulihkan di hook `after`: dataset tabel utama dikembalikan (seed 5.001 file dihapus) dan berkas unduhan dihapus.
- Kemampuan teknis: menangkap berkas unduhan browser (event download) ke direktori bersih; mengamati layar loading selama pembuatan berkas (state sementara); membaca jumlah notifikasi di Notification Center (komponen aplikasi di luar modul File Manager; selektornya disediakan tim FE).

## Test Steps

1. Catat jumlah notifikasi di Notification Center sebagai baseline
2. Klik ikon Download di toolbar tabel utama, lalu klik `Download as CSV`
3. Verifikasi layar loading tampil selama pembuatan berkas
4. Verifikasi tidak ada toast sukses
5. Verifikasi berkas CSV langsung terunduh setelah pembuatan selesai
6. Verifikasi jumlah notifikasi di Notification Center sama dengan baseline (tidak ada notifikasi baru)

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`.
- Layar loading (langkah 3) diasersi tepat setelah pemicu karena state sementara (butir 5 bagian 8b); absence toast (langkah 4) segera setelah pemicu dan sebelum asersi berkas, dengan berkas terunduh (langkah 5) sebagai anchor positif yang menyusul (butir 11 bagian 8b). Absence notifikasi memakai baseline jumlah (langkah 1) sebagai pembanding.
- Spec berdiri sendiri karena volume 5.001 baris (kelas e) tidak lazim dihasilkan seed rutin dan mengubah hitungan seluruh spec tabel utama.
- Tidak ada langkah penghubung.
- Temuan untuk QA:
  - TC-GS-FILEMGR-197 menyebut tabel utama "berisi 5.001 file aktif" tanpa menyatakan apakah total termasuk 33 file Tabel A2 atau 5.001 file tambahan. Spec menulis total 5.001 baris aktif; selisih terhadap Tabel A2 disediakan tim BE.
  - Mekanisme dan endpoint seeding 5.001 file tidak didefinisikan di TC (Q-4).
  - Jumlah baris berkas CSV (5.001) tidak diasersi karena Expected TC tidak memuatnya.
