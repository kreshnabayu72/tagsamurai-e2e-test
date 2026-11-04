---
id: TC-FA-LBL-E2E-020-bulk-delete-label-campuran-bersih-dan-dipakai
title: "Bulk Delete Label: campuran label bersih dan dipakai"
priority: High
caseType: Positive
status: draft
sourceRules:
  - E-FALB-27
  - F-FALB-05.k2
  - F-FALB-10.k3
  - FALB:must-not/menghapus-label-yang-sedang-dipakai-aset-fisik-atau-dija
coverage:
  web: automated
---

# Bulk Delete Label: campuran label bersih dan dipakai

## Prerequisites

- Mode: FE+BE
- Akun Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` spec ini membersihkan sisa data milik spec.
- Data uji: `DU-45` (tiga label seed bersuffix `{runId}-020` dengan awalan nama yang sama sehingga satu Search menampilkan ketiganya: label bersih pertama, label bersih kedua, dan satu label yang dipakai satu aset). Dua label bersih dihapus Bulk Delete; label yang dipakai dilewati.
- Kemampuan teknis: fixture BE untuk seeding label dan aset serta membaca label dan relasi aset dengan label (disediakan tim FE/BE); sesi API aktor dipakai hook `before` untuk seeding.
- State global: spec membuat tiga label dan satu aset; hook `after` menghapus sisa aset dan label yang masih ada lewat fixture BE.

## Test Steps

### F-FALB-05.k2: Bulk Delete campuran label bersih dan dipakai

1. Ketik Search awalan nama label `DU-45`, tekan Enter.
2. Centang checkbox pada baris label bersih pertama `DU-45`.
3. Centang checkbox pada baris label bersih kedua `DU-45`.
4. Centang checkbox pada baris label yang dipakai `DU-45`.
5. Klik `Bulk Action`.
6. Pilih `Delete`.
7. Verifikasi dialog dengan judul `Delete Labels` tampil.

### E-FALB-27: Bulk Delete memisahkan label yang dihapus dan yang dilewati

8. Verifikasi dialog `Delete Labels` memuat teks `The following will be deleted:` dengan nama label bersih pertama dan kedua `DU-45`, teks `The following are in use and will be skipped:` dengan nama label yang dipakai `DU-45`, teks `Are you sure you want to continue? This action cannot be undone.`, serta tombol `[Cancel]` dan `[Continue]`.
9. Klik `[Continue]`.
10. Verifikasi toast `Success, label has been deleted. Some items were skipped.` tampil.
11. Verifikasi baris label bersih pertama dan kedua `DU-45` tidak tampil lagi di tabel Labels List.
12. Verifikasi baris label yang dipakai `DU-45` masih tampil di tabel Labels List.
13. Klik icon Changelog.
14. Ketik Search awalan nama label `DU-45` pada modal Changelog: Labels, tekan Enter.
15. Verifikasi modal Changelog: Labels memuat tepat dua baris Action `Delete` pada Field `Label Name`, satu baris untuk tiap label bersih yang terhapus.

### F-FALB-10.k3: Bulk Delete menulis satu entri Delete per label yang berhasil dihapus

16. Verifikasi modal Changelog: Labels tidak memuat baris Action `Delete` untuk label yang dipakai `DU-45` (label yang dilewati tidak menulis entri).
17. Klik `[✕]` pada modal Changelog: Labels.

### FALB:must-not/menghapus-label-yang-sedang-dipakai-aset-fisik-atau-dija: Label yang dipakai tidak terhapus pada Bulk Delete

18. Verifikasi lewat fixture BE label yang dipakai `DU-45` masih tersimpan dan relasinya dengan aset tetap satu.

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16), 5 dan 6 (membuka dialog lewat Bulk Action Bar), 13, 14, dan 17 (membuka, mencari, dan menutup modal Changelog: Labels).
- Anchor positif (S-03): langkah 10 (toast sukses) menjadi anchor `Verifikasi` baris hilang pada langkah 11; langkah 15 (dua baris `Delete` tampil) menjadi anchor `Verifikasi` absence entri `Delete` pada langkah 16.
- Entri Delete dibaca dengan Search awalan nama bersuffix unik (baseline nol untuk entri Delete); entri Create hasil seeding label ada di hasil yang sama dan tidak diasersi.
- Pembagian klausa lintas spec: `FALB:must-not/menghapus-label-yang-sedang-dipakai-aset-fisik-atau-dija` dikutip spec 017 dan spec ini; spec 017 mengasersi jalur single (blokir `Cannot Delete Label`, label tetap ada), spec ini mengasersi jalur bulk (label yang dipakai dilewati dan tetap ada, langkah 12 dan 18). Seluruh klausa `E-FALB-27`, `F-FALB-05.k2`, dan `F-FALB-10.k3` diasersi di spec ini.
- Klausa log `F-FALB-05.k2` (satu entri Delete per label terhapus) dipenuhi pada langkah 15 (tepat dua baris Delete untuk dua label bersih) dan langkah 16 (tidak ada baris Delete untuk label yang dilewati); keduanya berada di bawah `E-FALB-27` dan `F-FALB-10.k3`.
