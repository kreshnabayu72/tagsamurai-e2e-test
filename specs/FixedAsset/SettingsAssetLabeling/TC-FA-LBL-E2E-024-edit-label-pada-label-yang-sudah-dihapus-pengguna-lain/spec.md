---
id: TC-FA-LBL-E2E-024-edit-label-pada-label-yang-sudah-dihapus-pengguna-lain
title: "Edit Label: label sudah dihapus pengguna lain saat Edit disimpan"
priority: Critical
caseType: Negative
status: draft
sourceRules:
  - F-FALB-03.k3
  - E-FALB-20
coverage:
  web: automated
---

# Edit Label: label sudah dihapus pengguna lain saat Edit disimpan

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (`DU-01`), env `FA_TC_EMAIL` dan `FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-18` (label seed milik spec, bersuffix `{runId}-024`, dibuat lewat API di hook `before`); `DU-24` (nama baru `Renamed-{runId}-024` yang diketik pelaku utama sebelum Save dan tidak pernah tersimpan); `DU-25` (baseline jumlah entri Changelog, System Log, dan Activity Log sebelum Save yang ditolak, dicatat pada langkah 6). Hook `after` menghapus sisa label seed bila masih ada.
- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding dan penghapusan label oleh pelaku kedua, serta kemampuan baca BE untuk jumlah entri Changelog, System Log, dan Activity Log serta isi entri Changelog per label (audit trail permanen, tidak diturunkan dari seeding), semuanya disediakan tim FE/BE. Pelaku kedua memakai sesi API, bukan sesi UI.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### F-FALB-03.k3: Edit pada label yang sudah dihapus pengguna lain

1. Ketik Search `DU-18`, tekan Enter
2. Verifikasi baris label `DU-18` tampil pada Labels List
3. Klik `[⋯]` pada baris label `DU-18`, pilih `Edit`
4. Pelaku kedua menghapus label `DU-18` lewat sesi API hingga penghapusan tersimpan
5. Verifikasi lewat kemampuan baca BE entri Delete untuk label `DU-18` tercatat di Changelog
6. Catat baseline `DU-25`: jumlah entri Changelog, System Log, dan Activity Log lewat kemampuan baca BE
7. Ganti isi field Label Name dengan `DU-24`
8. Klik `[Save]`
9. Verifikasi toast `This label is no longer available.` tampil
10. Verifikasi Modal Edit Label tertutup
11. Verifikasi baris label `DU-18` tidak tampil pada Labels List yang di-refresh

### E-FALB-20: Edit Label pada label yang sudah dihapus pengguna lain

12. Klik icon `Changelog` pada Table Tools
13. Ketik Search `DU-18` pada Modal Changelog: Labels, tekan Enter
14. Verifikasi hasil Search memuat entri Create dan entri Delete untuk label `DU-18`
15. Verifikasi tidak ada entri dengan Action `Edit` untuk label `DU-18` pada hasil Search
16. Klik `[✕]` pada Modal Changelog: Labels
17. Verifikasi lewat kemampuan baca BE selisih jumlah entri Changelog, System Log, dan Activity Log terhadap baseline `DU-25` sama dengan 0

## Notes

- Langkah penghubung: Search `DU-18` (langkah 1) menemukan baris target; klik `[⋯]` membuka form Edit; langkah 4 memicu penghapusan oleh pelaku kedua sebelum Save; langkah 6 mencatat baseline sesudah entri Delete pelaku kedua tertulis, supaya entri itu tidak terhitung; langkah 12 sampai 16 membuka, mencari di, dan menutup Modal Changelog: Labels.
- Anchor absence: entri Delete pelaku kedua terbaca lewat BE (langkah 5) mendahului baseline dan selisih log nol (langkah 17); toast hasil server (langkah 9) mendahului asersi baris tidak tampil (langkah 11); entri Create dan Delete untuk label `DU-18` (langkah 14) mendahului asersi tidak ada entri `Edit` (langkah 15). Entri Changelog dibaca dengan Search nama label seed bersuffix unik per spec.
- `F-FALB-03.k3` menunjuk perilaku yang sama dengan `E-FALB-20`: toast, Modal tertutup, dan tabel di-refresh diasersi sekali pada langkah 9 sampai 11 di bawah `F-FALB-03.k3` dan memenuhi klausa yang sama di `E-FALB-20`; klausa "tidak ada entri log" milik `E-FALB-20` diasersi pada langkah 15 dan 17 di bawah `E-FALB-20`.
- Asersi tidak ada entri `Edit` (langkah 15 dan 17) berada di spec ini karena itu klausa `E-FALB-20` yang dikutip spec ini sendiri, dengan aksi Save nyata dan baseline sendiri.
- Temuan PRD: PRD §8.2 dan §8.3 (L796 sampai L812) menyebut System Log dan Activity Log tanpa jalur baca per label, sehingga entri keduanya dibaca lewat kemampuan baca BE yang dinyatakan di Prerequisites (pola spec 009).
