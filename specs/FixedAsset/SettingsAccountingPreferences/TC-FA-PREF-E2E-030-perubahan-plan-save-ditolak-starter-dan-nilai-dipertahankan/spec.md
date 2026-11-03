---
id: TC-FA-PREF-E2E-030-perubahan-plan-save-ditolak-starter-dan-nilai-dipertahankan
title: "Perubahan Plan: Request Langsung Save pada Starter Ditolak dan Nilai Preferences Dipertahankan setelah Downgrade lalu Upgrade"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-571
  - TC-FA-PREF-572
coverage:
  web: automated
---

# Perubahan Plan: Request Langsung Save pada Starter Ditolak dan Nilai Preferences Dipertahankan setelah Downgrade lalu Upgrade

## Prerequisites

- Mode: FE+BE.
- Kelas harness: h (state tenant, perubahan plan tier).
- Akun aktor: Total Control company PC-11 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini. Pengecualian layar awal: pada awal spec company berplan Starter sehingga Preferences tidak terjangkau; hook `beforeEach` suite hanya menutup dialog dan langkah buka Preferences ada di langkah 4.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company PC-11 pada plan Starter yang sebelumnya Growth, Default Capitalization Threshold tersimpan 5.000.000 (Precondition TC-FA-PREF-571). Untuk TC-FA-PREF-572 company pada plan Growth dengan Default Capitalization Threshold tersimpan 10.000.000 dan In-service Date Source Manual by Accounting, dibentuk lewat seed pada langkah 6.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): request langsung Save Preferences memakai sesi API Total Control (Rina Anggraini) dengan payload Default Capitalization Threshold = 10000000 (butir "Sesi API aktor" di `suite.md`); perubahan plan company (upgrade ke Growth dan downgrade ke Starter) lewat fixture BE; pembacaan jumlah baris Changelog Preferences lewat kemampuan baca BE sebelum aksi (8b.10).
- State yang diubah spec: plan company dan Preferences. Hook `after` mengembalikan plan company ke Starter (kondisi awal) dan Preferences ke nilai awal; hook tetap jalan bila spec gagal di tengah.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-571: Request langsung Save Preferences pada plan Starter ditolak server

1. Kirim request langsung Save Preferences menggunakan sesi API Total Control Rina Anggraini, mengubah Default Capitalization Threshold menjadi 10000000
2. Verifikasi server menolak permintaan
3. Upgrade company ke Growth lewat fixture BE hingga tersimpan
4. Buka Settings > Accounting > Preferences
5. Verifikasi Default Capitalization Threshold tetap 5.000.000

### TC-FA-PREF-572: Nilai Preferences dipertahankan setelah downgrade ke Starter lalu upgrade kembali

6. Ubah Preferences lewat sesi API sesuai Precondition TC-FA-PREF-572 (Default Capitalization Threshold 10.000.000, In-service Date Source Manual by Accounting) hingga tersimpan
7. Klik ikon View history
8. Catat jumlah baris Changelog Preferences sebagai N_awal lewat kemampuan baca BE
9. Tutup modal Changelog
10. Turunkan plan company dari Growth ke Starter lewat fixture BE hingga tersimpan
11. Naikkan plan company kembali ke Growth lewat fixture BE hingga tersimpan
12. Buka Settings > Accounting > Preferences
13. Verifikasi Default Capitalization Threshold tampil Rp 10.000.000,00
14. Verifikasi In-service Date Source tampil Manual by Accounting
15. Klik ikon View history
16. Verifikasi modal Changelog: Preferences menampilkan jumlah baris yang sama dengan N_awal
17. Verifikasi modal Changelog: Preferences tidak memuat baris Create baru
18. Tutup modal Changelog

## Notes

- Kelas h (bagian 3 prinsip 13h): perubahan plan tier dipisah dari verifikasi baca murni; plan dipulihkan di hook `after`.
- Request langsung (langkah 1) tidak melewati browser; asersinya hanya respons server (langkah 2) dan state data (langkah 5), tanpa asersi tampilan FE (8b.1). Langkah 3 dan 4 adalah langkah penghubung tanpa `Verifikasi` (S-03); langkah 3 menjadi pemicu pelaku kedua lewat fixture BE (R-20).
- Langkah 6, 7, 9, 12, 15, dan 18 adalah langkah penghubung atau pembentuk Precondition (S-03). Langkah 8 mencatat baseline jumlah baris Changelog sebelum downgrade (S-12); jumlah absolut baris tidak diasersi.
- Langkah 17 diasersi dengan anchor langkah 16 (jumlah baris sama dengan N_awal sehingga tidak ada baris tambahan, termasuk Create baru).
- Temuan untuk QA:
  - Expected b TC-FA-PREF-572 menulis "Modal Changelog tetap memuat 2 baris Edit tanpa baris Create baru" sebagai jumlah absolut; Changelog adalah audit trail permanen sehingga spec mengasersi selisih jumlah baris terhadap baseline (S-12). Mohon TC ditulis ulang relatif.
  - Precondition TC-FA-PREF-571 meminta penguji mencatat jumlah baris awal Changelog, System Log, dan Activity Log, tetapi Expected tidak memuat asersi log; baseline itu tidak dipakai langkah dan Post Condition ("Nilai tersimpan tidak berubah") hanya diamati lewat Expected b (langkah 5).
  - Pelaku upgrade ("Upgrade company kembali ke Growth") tidak disebut TC; ditulis sebagai fixture BE yang disediakan tim FE/BE (S-13).
  - Post Condition TC-FA-PREF-572 ("Nilai Preferences yang sudah tersimpan tidak dihapus oleh downgrade") tidak punya langkah observasi sendiri; ekuivalennya sudah ada di Expected a.
