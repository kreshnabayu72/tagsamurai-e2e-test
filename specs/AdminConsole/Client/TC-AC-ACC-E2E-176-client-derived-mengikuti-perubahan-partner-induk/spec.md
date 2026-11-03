---
id: TC-AC-ACC-E2E-176-client-derived-mengikuti-perubahan-partner-induk
title: "Client Derived Mengikuti Perubahan Partner Induk: Address, Company Name, dan PIC Name"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-237
  - TC-AC-ACC-801
coverage:
  web: automated
---

# Client Derived Mengikuti Perubahan Partner Induk: Address, Company Name, dan PIC Name

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data milik spec (kelas Dipulihkan pada TC, ditiru bersuffix): Partner "CV Mitra Uji {runId}-176" (Distributor induk PT Distribusi Nusantara, PIC Name "Sinta Maharani", Address awal tersimpan di seed) dengan Add Own Subscription FAMS Active sehingga tercipta Client Derived "CV Mitra Uji {runId}-176". Di-seed hook `before` lewat Fixture BE (disediakan tim FE/BE, atribut P-DTL-1/C-DTL-4 Tabel A3); hook `after` menghapus Partner dan Client Derived milik spec ini lewat API.
- Alasan data bersuffix: spec mengubah Partner (aksi tulis); TC memakai Partner Pre-setup "CV Mitra Sejati" dan "CV Mitra Uji" yang dipakai TC lain, sehingga spec memakai Partner sendiri (S-06, S-12). Kedua TC dijalankan pada satu Partner Derived karena sama-sama mengamati pencerminan perubahan entitas induk.
- Kemampuan teknis: halaman Admin Console > Partner (modul Partner) tersedia untuk akun Total Control. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACC-801: Company Name dan PIC Name Client Derived mengikuti perubahan entitas induk

1. Klik ikon Search, ketik `CV Mitra Uji {runId}-176`, tekan Enter
2. Klik Company Name "CV Mitra Uji {runId}-176" untuk membuka Detail
3. Verifikasi header Detail menampilkan Company Name "CV Mitra Uji {runId}-176"
4. Verifikasi header Detail menampilkan PIC Name "Sinta Maharani"
5. Verifikasi header Detail menampilkan badge `Derived from CV Mitra Uji {runId}-176`
6. Klik `[Edit]` di header Detail
7. Verifikasi field Company Name pada popup "Edit Client" read-only (tidak dapat diubah)
8. Verifikasi field PIC Name pada popup "Edit Client" read-only (tidak dapat diubah)
9. Tutup popup "Edit Client" lewat ikon close `[✕]`

### TC-AC-ACC-237: Perubahan data entitas induk tercermin di Client Derived (Reflected)

10. Catat nilai Address pada Detail Client Derived "CV Mitra Uji {runId}-176" (nilai semula)
11. Buka Admin Console > Partner > Edit "CV Mitra Uji {runId}-176"
12. Ubah Address Partner menjadi `Jl. Asia Afrika No. 8, Bandung`
13. Klik `[Save]`
14. Tunggu aksi selesai (perubahan Partner tersimpan)
15. Muat ulang Detail Client Derived "CV Mitra Uji {runId}-176"
16. Verifikasi Address Detail Client Derived menampilkan "Jl. Asia Afrika No. 8, Bandung" (mengikuti entitas induk)

### TC-AC-ACC-801 (lanjutan): perubahan Company Name dan PIC Name Partner induk

17. Buka Admin Console > Partner > Edit "CV Mitra Uji {runId}-176"
18. Ubah Company Name menjadi `CV Mitra Uji Baru {runId}-176` dan PIC Name menjadi `Tika Maharani`
19. Klik `[Save]`
20. Tunggu aksi selesai (perubahan Partner tersimpan)
21. Buka Admin Console > Client, klik ikon Search, ketik `CV Mitra Uji Baru {runId}-176`, tekan Enter
22. Klik Company Name "CV Mitra Uji Baru {runId}-176" untuk membuka Detail
23. Verifikasi Detail Client Derived menampilkan Company Name "CV Mitra Uji Baru {runId}-176" tanpa aksi di modul Client
24. Verifikasi Detail Client Derived menampilkan PIC Name "Tika Maharani" tanpa aksi di modul Client

## Notes

- Pembagian TC lintas spec: TC-801 terbagi dua bagian di spec ini (bagian Edit read-only di awal, bagian perubahan Partner di akhir) karena langkah 1 sampai 4 TC-801 membaca Client Derived sebelum Partner diubah; kedua bagian ada di spec ini.
- Urutan: TC-801 bagian awal dijalankan sebelum TC-237 agar Company Name dan PIC Name awal diasersi sebelum Partner diubah; TC-237 mengubah Address, lalu bagian akhir TC-801 mengubah Company Name dan PIC Name (aksi tulis ke Partner di akhir spec).
- Langkah "Catat nilai Address", "Muat ulang Detail", dan Search adalah langkah penghubung (S-03), begitu pula "Tunggu aksi selesai" sesudah `[Save]` Partner (langkah 14 dan 20; butir 8 bagian 8b). Nilai Address semula (langkah 10) tidak diasersi karena TC-237 hanya meminta pembacaan (Post Condition meminta pemulihan; dipenuhi hook `after` yang menghapus Partner milik spec).
- Temuan untuk QA (S-15): TC-237 tidak menyebut nilai Address awal Partner "CV Mitra Sejati" dan memakai Client "PT Maju Bersama" (C-06); Tabel A3 mencatat Partner P-DTL-1 "CV Mitra Uji" sebagai dasar C-DTL-4 saja. Spec memakai satu Partner Derived milik sendiri untuk kedua TC. TC-801 menyebut `[Save]` pada halaman Partner tanpa mengatakan apakah ada dialog konfirmasi tambahan.
