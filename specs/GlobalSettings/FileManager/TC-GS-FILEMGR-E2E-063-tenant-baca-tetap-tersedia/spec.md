---
id: TC-GS-FILEMGR-E2E-063-tenant-baca-tetap-tersedia
title: "State Tenant: Aksi Baca File Manager dan Kartu Storage Tetap Tersedia saat Suspended atau Expired"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-FILEMGR-247
  - TC-GS-FILEMGR-283
coverage:
  web: automated
---

# State Tenant: Aksi Baca File Manager dan Kartu Storage Tetap Tersedia saat Suspended atau Expired

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Sinta Maharani (`Sinta M`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1). Login di hook `before` spec ini (saat Client Active); kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script.
- Suite serial (`parallel: false`) karena spec mengubah status Client uji dan laporan Storage. Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE; akun pengubah status Client tidak disebut di TC, PRD, atau LLD, lihat Temuan untuk QA): mengubah status Client uji menjadi Suspended dan Expired; seeding laporan Storage skenario S1 (Tabel A5: kuota 50 GB; Fixed Asset 3.2 GB, Admin Console 1.4 GB, Global Settings 204.8 MB; Total Used 4.8 GB); membaca file terunduh (nama dan keberadaan).
- State global yang diubah: status Client uji dan laporan Storage. Hook `after` (tetap jalan walau spec gagal di tengah) mengembalikan status Client ke Active dan memulihkan laporan Storage awal.
- Data: Data Pre-setup Tabel A2 (33 file aktif, termasuk `budi-avatar.jpg` F01) di-seed idempotent di hook `before` dan hanya dibaca (tidak diubah, S-06; lihat Temuan untuk QA tentang hitungan 33).
- Tabel "Status Client yang diuji" (langkah 1 sampai 14 diulang per baris):

  | Status Client |
  |---|
  | Suspended |
  | Expired |

- Dependensi TC (TC-01 tabel utama, TC-268 kartu Storage Usage) dijalankan sebagai langkah aksi di spec ini.
- Cleanup (hook `after`): pulihkan status Client dan laporan Storage seperti di atas; file hasil download dihapus dari folder unduhan uji.

## Test Steps

### TC-GS-FILEMGR-247 dan TC-GS-FILEMGR-283: Aksi baca dan kartu Storage saat Suspended lalu Expired

Untuk setiap baris pada tabel "Status Client yang diuji", lakukan langkah 1 sampai 14:

1. Ubah status Client uji ke status pada baris tabel, lalu buka Global Settings > File Manager
2. Verifikasi tabel utama terbuka dan memuat 33 baris
3. Verifikasi tidak ada toast error pada pembukaan tabel utama
4. Klik teks `budi-avatar.jpg` di kolom File Name
5. Verifikasi tab browser baru terbuka dan menampilkan gambar
6. Tutup tab baru dan kembali ke tab asal
7. Klik ikon (⋯) baris `budi-avatar.jpg`, lalu klik `Download`
8. Verifikasi tidak ada toast pada Download file
9. Verifikasi Download file berhasil (file terunduh)
10. Klik ikon Download di toolbar, lalu klik `Download as CSV`
11. Verifikasi tidak ada toast pada export CSV
12. Verifikasi export CSV berhasil (file CSV terunduh)
13. Verifikasi kartu Storage Usage memuat data S1: `Total Used` `4.8 GB`, `Storage Quota` `50.0 GB`, dan daftar `Fixed Asset 3.2 GB`, `Admin Console 1.4 GB`, `Global Settings 204.8 MB`, tanpa diblokir
14. Verifikasi tidak ada toast error untuk pembacaan kartu Storage Usage

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Kelas state tenant (prinsip 13h): verifikasi baca dipisah dari write-lockdown, yang ada di spec `TC-GS-FILEMGR-E2E-062-tenant-write-lockdown-suspended-expired`.
- Langkah 1 sampai 14 diulang untuk dua baris tabel (28 langkah setelah ekspansi; idiom ulang per baris tabel, bagian 8b butir 7). TC-247 dan TC-283 sama-sama berpremis Suspended lalu Expired dan berbagi halaman, sehingga dijalankan dalam satu iterasi: langkah 2 sampai 12 untuk TC-247 dan langkah 13 sampai 14 untuk TC-283.
- Urutan Expected TC-247: butir a (langkah 2 dan 3), b (langkah 5), c (langkah 8 sampai 12), d (iterasi kedua Expired). Asersi "tanpa toast" diletakkan segera setelah pemicu (bagian 8b butir 11) sebelum asersi artefak.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (prasyarat status Client dijadikan langkah eksplisit) dan langkah 6 (menutup tab baru dan kembali ke tab asal; web membuka file di tab baru, tanpa modal, TC-GS-FILEMGR-48).
- Temuan untuk QA:
  - TC-GS-FILEMGR-247 Langkah 2 dan Expected b ("tutup modal preview", "File Preview terbuka") sama dengan TC-44/45/46 dan bertentangan dengan TC-GS-FILEMGR-48 serta PRD File Preview (web membuka file di tab browser baru, tanpa modal); spec memakai perilaku tab baru (langkah 4 sampai 6, juga pada iterasi Expired). TC owner perlu memperbaiki.
  - Akun dan mekanisme pengubah status Client tidak disebut TC, PRD, atau LLD (S-13); ditulis sebagai kemampuan yang disediakan tim FE. Status Client diubah saat sesi Total Control sudah aktif (login di hook sebelum status berubah); validitas sesi sesudahnya adalah asumsi TC.
  - Hitungan 33 baris (TC-247) bergantung pada dataset Pre-setup yang tidak diubah spec lain (Q-7); dataset di-seed idempotent oleh hook spec ini.
  - TC-247 butir c hanya menyebut Download file dan export CSV "berhasil tanpa toast"; isi file tidak diasersi (kelas f ada di spec lain).
