---
id: TC-FA-LBL-E2E-009-absence-log-edit-label-zero-delta
title: "Absence: Edit Label tanpa perubahan tidak menulis entri log di tiga surface"
priority: Critical
caseType: Negative
status: draft
sourceRules:
  - FALB-LOGIC-07b
  - FALB:FI-07
  - E-FALB-07
  - F-FALB-03.k1
  - FALB-LOGIC-07a
  - F-FALB-10.k1
  - FALB:must-not/menulis-entri-log-baru-ketika-formulir-edit-label-di-sub
coverage:
  web: automated
---

# Absence: Edit Label tanpa perubahan tidak menulis entri log di tiga surface

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (`DU-01`), env `FA_TC_EMAIL` dan `FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: label seed milik spec dengan nama awal `DU-49` (`Urgent-{runId}-009`) berwarna `#A1B2C3` (bentuk kapital `DU-10`), dibuat lewat API di hook `before` dan dihapus di hook `after`; `DU-10` (kode hex huruf kecil `#a1b2c3` yang diketik pada langkah 12); `DU-25` (baseline jumlah entri Changelog, System Log, dan Activity Log untuk label seed sebelum aksi, dicatat pada langkah 1).
- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding label; kemampuan baca BE untuk jumlah entri Changelog, System Log, dan Activity Log per label (audit trail permanen, tidak diturunkan dari seeding). Keduanya disediakan tim FE/BE.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Catat baseline `DU-25`: jumlah entri Changelog, System Log, dan Activity Log untuk label seed lewat kemampuan baca BE
2. Ketik Search label seed (nama awal `DU-49`), tekan Enter
3. Catat nilai Last Updated pada baris label seed
4. Klik `[⋯]` pada baris label seed, pilih `Edit`
5. Klik `[Save]` tanpa mengubah nama maupun warna

### FALB-LOGIC-07b: Form Edit tertutup normal dan toast zero-delta tampil

6. Verifikasi toast `No changes to save.` tampil
7. Verifikasi Modal Edit Label tertutup

### FALB:FI-07: Submit tanpa perubahan data dianggap sukses tanpa mutasi basis data

8. Verifikasi Last Updated baris label seed sama dengan nilai yang dicatat pada langkah 3

### E-FALB-07: Submit Edit tanpa mengubah nama maupun warna sukses tanpa mutasi

9. Verifikasi baris label seed tampil dengan nama awal `DU-49` dan Color Hex `#A1B2C3`

### F-FALB-03.k1: Submit zero-delta atas perubahan kapitalisasi warna saja

10. Klik `[⋯]` pada baris label seed, pilih `Edit`
11. Klik swatch warna pada field Color
12. Ganti isi kolom Hex dengan `DU-10`
13. Tekan Escape untuk menutup Color Picker Overlay
14. Klik `[Save]`
15. Verifikasi toast `No changes to save.` tampil

### FALB-LOGIC-07a: Zero-delta tanpa mutasi dan tanpa entri baru di tiga surface log

16. Verifikasi Last Updated baris label seed sama dengan nilai yang dicatat pada langkah 3
17. Verifikasi lewat kemampuan baca BE bahwa jumlah entri Changelog, System Log, dan Activity Log untuk label seed sama dengan baseline `DU-25`

### F-FALB-10.k1: Edit zero-delta menulis nol entri

18. Klik icon `Changelog` pada Table Tools
19. Ketik Search label seed (nama awal `DU-49`) pada Modal Changelog: Labels, tekan Enter
20. Verifikasi hasil Search memuat entri Create untuk label seed
21. Verifikasi jumlah baris hasil Search sama dengan baseline Changelog pada `DU-25`
22. Klik `[✕]` pada Modal Changelog: Labels

### FALB:must-not/menulis-entri-log-baru-ketika-formulir-edit-label-di-sub: Tidak menulis entri log baru pada Edit zero-delta

23. Verifikasi lewat kemampuan baca BE bahwa jumlah entri System Log dan Activity Log untuk label seed sama dengan baseline `DU-25`

## Notes

- Langkah penghubung: Search label seed (langkah 2, 19) menemukan baris target dan entri Changelog; klik `[⋯]` membuka menu baris; langkah 3 mencatat Last Updated sebagai pembanding; langkah 13 menutup Color Picker Overlay tanpa menutup modal; langkah 18 sampai 22 membuka, mencari di, dan menutup Modal Changelog: Labels.
- Anchor absence: baseline `DU-25` dicatat sebelum aksi (langkah 1); entri Create label seed pada Modal Changelog (langkah 20) mendahului asersi jumlah entri tidak bertambah (langkah 21).
- Pembagian klausa lintas spec: `E-FALB-07` dan `F-FALB-03.k1` dikutip spec 023 dan spec ini; `F-FALB-10.k1` hanya dikutip spec ini. `FALB-LOGIC-07a` dikutip spec 009 dan spec 023: spec ini mengasersi sisi zero-delta (tanpa mutasi dan tanpa entri di tiga surface log, langkah 16 dan 17), spec 023 mengasersi batasnya (perubahan kapitalisasi nama saja bukan zero-delta, Edit disimpan dan Changelog bertambah satu). Spec ini mengasersi klausa zero-delta lain (sukses tanpa mutasi, toast `No changes to save.`).
- Klausa nol entri log `F-FALB-03.k1` dipenuhi pada langkah 17 (jumlah entri Changelog, System Log, dan Activity Log sama dengan baseline), langkah 21 (jumlah baris Changelog), dan langkah 23 (System Log dan Activity Log), yang berada di bawah subjudul aturan lain.
- Dasar asersi tanpa mutasi: kolom Last Updated adalah waktu pembaruan label (`FLD-05`), sehingga nilai yang sama sebelum dan sesudah submit zero-delta diasersi sebagai tidak ada mutasi.
- Temuan PRD: PRD §8.2 dan §8.3 menyebut System Log (Detail User > Tab System Log) dan Activity Log (FAMS level) tetapi tidak memberi jalur navigasi atau Search per label untuk membaca entri per label; jumlah entri kedua surface itu dibaca lewat kemampuan baca BE (langkah 17 dan 23).
