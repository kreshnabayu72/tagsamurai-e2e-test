---
id: TC-FA-LBL-E2E-018-delete-label-diblokir-volume-500-aset
title: "Delete Label: diblokir label dipakai 500 aset"
priority: Critical
caseType: Negative
status: draft
sourceRules:
  - E-FALB-02
  - F-FALB-04.k1
  - F-FALB-10.k2
coverage:
  web: automated
---

# Delete Label: diblokir label dipakai 500 aset

## Prerequisites

- Mode: FE+BE
- Akun Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` spec ini membersihkan data milik spec.
- Data uji: `DU-42` (satu label seed dengan 500 aset berlabel, bersuffix `{runId}-018`). Jumlah 500 diturunkan dari seeding (bukan dibaca dari tabel yang hanya menampilkan satu halaman).
- Kemampuan teknis: fixture BE untuk seeding volume 500 aset berlabel dan untuk membaca label serta jumlah relasi aset dengan label, dan kemampuan baca BE untuk jumlah entri Changelog, System Log, dan Activity Log (semuanya disediakan tim FE/BE).
- State global: spec membuat label `DU-42` dan 500 aset; hook `after` melepas relasi, menghapus aset, lalu menghapus label lewat fixture BE.

## Test Steps

### E-FALB-02: Delete label yang dipakai 500 aset fisik diblokir

1. Ketik Search `DU-42`, tekan Enter.
2. Catat baseline jumlah entri Changelog, System Log, dan Activity Log lewat kemampuan baca BE.
3. Klik `[⋯]` pada baris Label `DU-42`, pilih `Delete`.
4. Verifikasi dialog dengan judul `Cannot Delete Label`, nama label `DU-42`, teks `This label is assigned to 500 assets.`, teks `Remove it from those assets and Default Label lists before deleting it.`, dan tombol `[OK]` tampil.
5. Klik `[OK]`.
6. Verifikasi lewat fixture BE label `DU-42` masih tersimpan dan jumlah relasi aset dengan label `DU-42` tetap 500 (tidak ada mutasi dan penempelan tidak berubah).
7. Verifikasi lewat kemampuan baca BE tidak ada entri log baru: selisih jumlah entri Changelog, System Log, dan Activity Log terhadap baseline langkah 2 sama dengan 0.

### F-FALB-04.k1: Label yang dipakai aset diblokir

8. Verifikasi dialog `Cannot Delete Label` tertutup dan baris Label `DU-42` masih tampil di tabel Labels List.

### F-FALB-10.k2: Penolakan guard menulis nol entri log

9. Verifikasi lewat kemampuan baca BE selisih jumlah entri Changelog sama dengan 0, selisih jumlah entri System Log sama dengan 0, dan selisih jumlah entri Activity Log sama dengan 0 terhadap baseline langkah 2.

## Notes

- Pengecualian P-1 (state berat): klausa absence log milik `F-FALB-10.k2` (langkah 7 dan 9) diasersi di spec ini karena konteksnya bergantung pada seeding 500 aset yang baru dibangun. `F-FALB-10.k2` juga dikutip spec 014 dan 025 (state tenant), 015 dan 027 (batas katalog), dan 017 (guard Default Label dan guard saat konfirmasi).
- Pembagian klausa lintas spec: `F-FALB-04.k1` dikutip spec ini dan spec 017; spec ini mengasersi kasus label yang dipakai 500 aset (`E-FALB-02`), spec 017 kasus label yang dijadikan Default Label (`E-FALB-03`).
- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16), 2 (baseline log, S-12), dan 5 (menutup dialog blokir).
