---
id: TC-AC-DS-E2E-192-changelog-setup-column-ceklis-dan-unceklis-kolom
title: "Setup Column Changelog: Ceklis dan Unceklis Tujuh Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-414
coverage:
  web: automated
---

# Setup Column Changelog: Ceklis dan Unceklis Tujuh Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): SKU inti dan seed (#29, #30), riwayat Changelog Principal (#33), General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Kolom yang diuji (parameter langkah 8 sampai 11): `Date`, `Action`, `SKU`, `Field`, `Old Value`, `New Value`, `Modified By`.
- Data Dinamis: tidak ada. Spec menyimpan konfigurasi kolom (ketujuh kolom tercentang, sama dengan bawaan) pada langkah 12.
- Kemampuan teknis (disediakan tim FE): menghapus preferensi kolom Setup Column modal Changelog di browser (hook `before` dan hook `after`), bukan lewat [Reset to Default].
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-414: Ceklis dan unceklis kolom Setup Column modal Changelog

1. Klik ikon Changelog
2. Verifikasi modal "Changelog: Device SKU" tampil
3. Klik header kolom Actions (⋯) pada modal
4. Verifikasi Overlay Column Visibility tampil
5. Klik `Setup Column...`
6. Verifikasi Popup Setup Column tampil
7. Untuk setiap baris tabel "Kolom yang diuji" lakukan langkah 8 sampai 11
8. Hilangkan centang kolom
9. Verifikasi kolom tersebut hilang dari preview
10. Centang kembali kolom
11. Verifikasi kolom tersebut tampil kembali di preview
12. Klik `[Save]`
13. Verifikasi Popup Setup Column tertutup
14. Tutup modal Changelog, lalu klik ikon Changelog
15. Verifikasi modal "Changelog: Device SKU" tampil
16. Verifikasi tabel memuat ketujuh kolom `Date`, `Action`, `SKU`, `Field`, `Old Value`, `New Value`, `Modified By` (konfigurasi tersimpan dan tetap berlaku setelah modal dibuka kembali)

### Pemulihan state akhir

17. Tutup modal Changelog

## Notes

- Langkah 8 sampai 11 diulang per kolom pada tabel "Kolom yang diuji" (7 iterasi, ekspansi 28 langkah; total ekspansi spec sekitar 39 langkah). Alasan melewati sekitar 35 langkah: seluruh langkah satu kelas (Setup Column modal Changelog) dan tiap iterasi kolom berdiri sendiri; kegagalan satu kolom tidak membuat kolom lain kehilangan makna. `Verifikasi` tetap satu per klausa di dalam iterasi.
- Langkah penghubung tanpa `Verifikasi`: langkah 14 (menutup dan membuka kembali modal sesuai langkah 7 TC) dan langkah 17 (S-03).
- Temuan untuk QA:
  - S-15: Expected butir a sampai g menyebut kolom hilang "pada preview dan tabel", tetapi langkah TC hanya memiliki satu `[Save]` di akhir sehingga hilangnya kolom pada tabel modal tidak teramati per kolom. Spec mengasersi preview per kolom (langkah 9 dan 11) dan tabel setelah Save (langkah 16). Perlu keputusan QA bila tabel harus diasersi per kolom.
  - Karena ketujuh kolom dicentang kembali sebelum `[Save]`, konfigurasi yang tersimpan sama dengan bawaan; butir h ("tersimpan dan tetap berlaku") hanya teramati sebagai ketujuh kolom tampil.
  - Fixture rancangan Pre-setup #33 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
