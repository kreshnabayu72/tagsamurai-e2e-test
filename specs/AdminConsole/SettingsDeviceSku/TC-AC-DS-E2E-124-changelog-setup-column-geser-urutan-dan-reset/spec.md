---
id: TC-AC-DS-E2E-124-changelog-setup-column-geser-urutan-dan-reset
title: "Setup Column Changelog: Geser Urutan Kolom dan Reset to Default"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-415
  - TC-AC-DS-417
coverage:
  web: automated
---

# Setup Column Changelog: Geser Urutan Kolom dan Reset to Default

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): SKU inti dan seed (#29, #30), riwayat Changelog Principal (#33), General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Urutan bawaan kolom: `Date | Action | SKU | Field | Old Value | New Value | Modified By`.
- Pemindahan kolom (parameter langkah 17 dan 18; kumulatif, dimulai dari urutan bawaan; posisi tujuan dipilih spec karena TC hanya menyebut "posisi lain"):

  | # | Kolom | Posisi tujuan | Urutan preview sesudahnya |
  |---|---|---|---|
  | 1 | `Date` | 7 | `Action, SKU, Field, Old Value, New Value, Modified By, Date` |
  | 2 | `Action` | 6 | `SKU, Field, Old Value, New Value, Modified By, Action, Date` |
  | 3 | `SKU` | 5 | `Field, Old Value, New Value, Modified By, SKU, Action, Date` |
  | 4 | `Field` | 4 | `Old Value, New Value, Modified By, Field, SKU, Action, Date` |
  | 5 | `Old Value` | 3 | `New Value, Modified By, Old Value, Field, SKU, Action, Date` |
  | 6 | `New Value` | 2 | `Modified By, New Value, Old Value, Field, SKU, Action, Date` |
  | 7 | `Modified By` | 4 | `New Value, Old Value, Field, Modified By, SKU, Action, Date` |

- Data Dinamis: tidak ada. Spec menyimpan konfigurasi kolom (TC-AC-DS-417 menyimpan konfigurasi bawaan, TC-AC-DS-415 menyimpan urutan pada tabel di atas).
- Kemampuan teknis (disediakan tim FE): menghapus preferensi kolom Setup Column modal Changelog di browser (hook `before` agar kolom berada pada konfigurasi bawaan, dan hook `after`), bukan lewat [Reset to Default]. Drag and drop kolom pada Popup Setup Column.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-417: Reset to Default modal Changelog mengembalikan konfigurasi kolom ke bawaan

1. Klik ikon Changelog
2. Verifikasi modal "Changelog: Device SKU" tampil
3. Klik header kolom Actions (⋯) pada modal
4. Verifikasi Overlay Column Visibility tampil
5. Klik `Setup Column...`
6. Verifikasi Popup Setup Column tampil
7. Hilangkan centang `Old Value`
8. Geser `Date` ke posisi akhir
9. Klik `[Reset to Default]`
10. Verifikasi preview kembali ke default: tujuh kolom tampil dengan urutan awal
11. Klik `[Save]`
12. Verifikasi tabel modal tetap pada konfigurasi default

### TC-AC-DS-415: Geser urutan kolom Setup Column modal Changelog

13. Klik header kolom Actions (⋯) pada modal
14. Klik `Setup Column...`
15. Verifikasi Popup Setup Column tampil
16. Untuk setiap baris tabel "Pemindahan kolom" lakukan langkah 17 dan 18
17. Seret kolom ke posisi tujuan
18. Verifikasi urutan preview berubah menjadi "Urutan preview sesudahnya"
19. Verifikasi tidak ada kolom yang posisinya terkunci: ketujuh kolom berhasil dipindahkan
20. Klik `[Save]`
21. Verifikasi urutan kolom pada tabel modal mengikuti hasil drag: `New Value | Old Value | Field | Modified By | SKU | Action | Date`
22. Tutup modal Changelog, lalu klik ikon Changelog
23. Verifikasi modal "Changelog: Device SKU" tampil
24. Verifikasi urutan kolom pada tabel modal tetap `New Value | Old Value | Field | Modified By | SKU | Action | Date` (urutan tersimpan)

### Pemulihan state akhir

25. Tutup modal Changelog

## Notes

- Langkah 17 dan 18 diulang per baris tabel "Pemindahan kolom" (7 iterasi, ekspansi 14 langkah; total ekspansi spec sekitar 35 langkah). Semua langkah satu kelas (Setup Column modal Changelog) dan tiap pemindahan berdiri sendiri.
- Urutan TC dalam spec: TC-AC-DS-417 lebih dulu karena butuh konfigurasi bawaan dan tidak meninggalkan perubahan; TC-AC-DS-415 menyimpan urutan baru sehingga ditaruh di akhir (S-10, S-09). Hook `after` menghapus preferensi kolom di browser.
- Langkah penghubung tanpa `Verifikasi`: langkah 7 dan 8 (menyiapkan perubahan sebelum Reset sesuai TC), langkah 22 (menutup dan membuka kembali modal sesuai TC), dan langkah 25 (S-03).
- Temuan untuk QA:
  - S-15: TC 415 hanya menyebut "posisi lain" tanpa posisi tujuan; spec memilih posisi tujuan deterministik (tabel di Prerequisites). TC 415 Expected a sampai g menyebut urutan "pada preview dan tabel", sedangkan hanya ada satu `[Save]` di akhir; tabel diasersi setelah Save (langkah 21 dan 24), preview per kolom (langkah 18).
  - TC 417 langkah 8 ("geser Date ke posisi akhir") tidak menyebut Expected pada langkah itu; hanya hasil setelah Reset yang diasersi.
  - Fixture rancangan Pre-setup #33 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
