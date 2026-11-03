---
id: TC-AC-DS-E2E-125-changelog-setup-column-pin-dan-batas-pin-keempat
title: "Setup Column Changelog: Pin dan Unpin Kolom serta Pin Keempat Diblok"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-416
  - TC-AC-DS-568
coverage:
  web: automated
---

# Setup Column Changelog: Pin dan Unpin Kolom serta Pin Keempat Diblok

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): SKU inti dan seed (#29, #30), riwayat Changelog Principal (#33), General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Kolom yang diuji (parameter langkah 4 sampai 10): `Date`, `Action`, `SKU`, `Field`, `Old Value`, `New Value`, `Modified By`.
- Data Dinamis: tidak ada. Spec menyimpan status pin sementara (langkah 4 dan 9); pada akhir tiap iterasi semua kolom kembali tidak di-pin.
- Kemampuan teknis (disediakan tim FE): menghapus preferensi kolom Setup Column modal Changelog di browser (hook `before` agar kolom berada pada konfigurasi bawaan, dan hook `after`), bukan lewat [Reset to Default]. Tabel modal Changelog dapat digulir horizontal pada viewport uji (lihat Temuan untuk QA).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-416: Pin dan unpin kolom Setup Column modal Changelog

1. Klik ikon Changelog
2. Verifikasi modal "Changelog: Device SKU" tampil
3. Untuk setiap baris tabel "Kolom yang diuji" lakukan langkah 4 sampai 10
4. Klik header kolom Actions (⋯), klik `Setup Column...`, klik ikon Pin pada kolom, klik `[Save]`
5. Gulir tabel modal secara horizontal
6. Verifikasi kolom tersebut membeku di kiri ketika tabel digulir
7. Klik header kolom Actions (⋯), klik `Setup Column...`
8. Verifikasi ikon Pin kolom tersebut berstatus di-pin (status pin tersimpan)
9. Klik ikon Pin pada kolom tersebut (unpin), klik `[Save]`, gulir tabel modal secara horizontal
10. Verifikasi kolom tersebut kembali bergerak setelah unpin

### TC-AC-DS-568: Pin keempat diblok pada Setup Column modal Changelog dengan ikon Pin disabled dan tooltip

11. Klik header kolom Actions (⋯), klik `Setup Column...`
12. Verifikasi Popup Setup Column tampil
13. Klik ikon Pin pada kolom `Date`, lalu `Action`, lalu `SKU`
14. Verifikasi tiga kolom `Date`, `Action`, dan `SKU` di-pin
15. Hover ikon Pin pada kolom `Field`
16. Verifikasi ikon Pin kolom `Field` disabled dan tidak dapat diklik
17. Verifikasi tooltip "Maximum 3 columns can be pinned at once. Unpin another column first." tampil

### Pemulihan state akhir

18. Klik ikon close `[✕]` pada Popup Setup Column (perubahan pin tidak disimpan); tutup modal Changelog

## Notes

- Langkah 4 sampai 10 diulang per kolom pada tabel "Kolom yang diuji" (7 iterasi, ekspansi 49 langkah; total ekspansi spec sekitar 60 langkah). Alasan melewati sekitar 35 langkah: seluruh langkah satu kelas (Setup Column modal Changelog) dan tiap iterasi kolom berdiri sendiri; kegagalan satu kolom tidak membuat kolom lain kehilangan makna. Blok TC-AC-DS-568 independen dari blok iterasi.
- Langkah penghubung tanpa `Verifikasi`: langkah 18 (S-03). Langkah 9 membatalkan pin (unpin) sebagai bagian aksi TC.
- Expected 416 butir a sampai g dipecah per klausa di langkah 6 (membeku) dan langkah 10 (kembali bergerak) dalam tiap iterasi; butir h di langkah 8. TC-AC-DS-568 butir a dan b di langkah 16 dan 17.
- Pembagian TC lintas spec: screening Popup Setup Column modal Changelog ada di spec 123, ceklis dan unceklis di spec 192, geser urutan dan Reset to Default di spec 124, tutup tanpa Save dan kolom terakhir di spec 126.
- Temuan untuk QA:
  - S-14: Expected 416 mensyaratkan tabel yang dapat digulir horizontal; tujuh kolom modal Changelog bisa muat tanpa gulir pada viewport lebar. TC tidak menyebut ukuran viewport; spec mengikuti TC dan mensyaratkan kemampuan tersebut di Prerequisites.
  - Fixture rancangan Pre-setup #33 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
