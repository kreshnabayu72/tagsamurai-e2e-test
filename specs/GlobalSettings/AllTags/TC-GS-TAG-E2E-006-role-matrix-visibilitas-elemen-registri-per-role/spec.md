---
id: TC-GS-TAG-E2E-006-role-matrix-visibilitas-elemen-registri-per-role
title: "Role Matrix: Visibilitas Elemen Registri per Role (Total Control, Manage TAG Update, Read Only, Manage TAG Read)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-25
  - TC-GS-TAG-26
  - TC-GS-TAG-27
  - TC-GS-TAG-28
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Registri per Role (Total Control, Manage TAG Update, Read Only, Manage TAG Read)

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Total Control) di hook `before`; ganti akun ke role berikutnya ditulis sebagai langkah. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.

Role yang diuji (Tabel Data Uji Pre-setup; Client A):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-25 | Total Control | Sari Dewi | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-26 | Manage TAG (Update) | Agus Wijaya | `manageTagUpdate_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TAG_UPDATE_PASSWORD` |
| TC-27 | Read Only | Maya Putri | `readOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_RO_PASSWORD` |
| TC-28 | Manage TAG (Read) | Tono Hartono | `manageTagRead_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TAG_READ_PASSWORD` |

- `GS_TAG_UPDATE_PASSWORD` dan `GS_TAG_READ_PASSWORD` belum terdaftar di `.env.example` dan `spectra.config.ts` (dicatat di `suite.md` bagian Kredensial); didaftarkan pemilik repositori.
- Langkah tiap role berbeda (daftar elemen berbeda per role), sehingga ditulis per blok role, bukan perulangan.
- Data Pre-setup (hanya dibaca): Seed Registri A (DD-01 s.d. DD-30); baris yang dipakai DD-01 (Paired) dan DD-02 (Available). Seed di-seed ulang idempotent oleh hook `before` (Q-4; mekanisme disediakan tim FE/BE). Spec tidak membuat, mengubah, atau menghapus data.
- Layar awal: Global Settings > TAG Tab All dibuka di hook `beforeEach` untuk akun hook; setelah ganti akun, halaman dibuka lewat langkah.
- Guided Tooltip: flag `guided_tooltip_seen_gs-tag-registry` disetel true untuk keempat akun oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- State global: tidak ada yang diubah. Capability tiap akun adalah data Pre-setup. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-TAG-25: Total Control: seluruh elemen aksi tulis dan baca tampil di Tab All dan Tab Not Paired

1. Amati toolbar Tab All
2. Verifikasi toolbar menampilkan `Search by Scan`, `Filter`, `Download`, `Event Log`, `Audit TAG`, `Delete by Scan`, `+ Activate TAG`
3. Buka menu baris `E2801160600002054D8A0002`
4. Verifikasi menu baris DD-02 berisi `TAG Log` dan `Delete`
5. Tutup menu baris
6. Buka menu baris DD-01 (Paired)
7. Verifikasi menu baris DD-01 hanya berisi `TAG Log`
8. Verifikasi entri `Delete` Hidden pada menu baris DD-01
9. Tutup menu baris
10. Klik Tab Not Paired
11. Verifikasi kolom checkbox tampil

### TC-GS-TAG-26: Manage TAG (Update): elemen identik dengan Total Control

12. Logout, lalu login sebagai Manage TAG (Update) (Agus Wijaya)
13. Buka Global Settings > TAG
14. Amati toolbar Tab All
15. Verifikasi toolbar menampilkan `Audit TAG`, `Delete by Scan`, `+ Activate TAG`, `Event Log`
16. Buka menu baris DD-02
17. Verifikasi menu baris DD-02 berisi `TAG Log` dan `Delete`
18. Tutup menu baris
19. Klik Tab Not Paired
20. Verifikasi kolom checkbox tampil

### TC-GS-TAG-27: Read Only: kontrol tulis Hidden, kontrol baca tampil

21. Logout, lalu login sebagai Read Only (Maya Putri)
22. Buka Global Settings > TAG
23. Amati toolbar Tab All
24. Verifikasi toolbar menampilkan `Search by Scan`, `Search`, `Filter`, `Download`, `Event Log`
25. Verifikasi `Audit TAG`, `Delete by Scan`, `+ Activate TAG` Hidden (bukan Disabled)
26. Verifikasi kartu counter tampil
27. Verifikasi Tab `All`, `Paired`, `Not Paired` tampil
28. Buka menu baris DD-02
29. Verifikasi menu baris DD-02 hanya berisi `TAG Log`
30. Verifikasi `Delete` Hidden pada menu baris DD-02
31. Tutup menu baris
32. Klik Tab Not Paired
33. Verifikasi kolom checkbox Hidden

### TC-GS-TAG-28: Manage TAG (Read): kontrol tulis Hidden, kontrol baca tampil

34. Logout, lalu login sebagai Manage TAG (Read) (Tono Hartono)
35. Buka Global Settings > TAG
36. Amati toolbar Tab All
37. Verifikasi toolbar menampilkan `Search by Scan`, `Search`, `Filter`, `Download`, `Event Log`
38. Verifikasi `Audit TAG`, `Delete by Scan`, `+ Activate TAG` Hidden
39. Buka menu baris DD-02
40. Verifikasi menu baris DD-02 hanya berisi `TAG Log`
41. Tutup menu baris
42. Klik Tab Not Paired
43. Verifikasi kolom checkbox Hidden

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md` (Section 2). Subjudul `###` memetakan langkah ke id TC granular. Role Matrix mengikuti bagian 3a konvensi: matriks visibilitas boleh memuat polaritas tampil dan Hidden dalam satu spec.
- Langkah penghubung (tanpa `Verifikasi`, S-03): menutup menu baris (langkah 5, 9, 18, 31, 41), membuka halaman dan mengamati; ganti akun (langkah 12, 21, 34; Step ganti akun eksplisit, S-07). Anchor positif absence elemen Hidden (8b butir 2): Table Tools dan Tab yang sudah termuat menjadi anchor permukaan (langkah 24, 27, 37).
- Penyimpangan urutan: TC-25 langkah 3 menyebut "Amati menu baris DD-01 (Paired)" setelah berpindah ke Tab Not Paired; DD-01 berstatus Paired sehingga tidak tampil di Tab Not Paired. Spec mengamati DD-01 di Tab All (langkah 6) sebelum pindah ke Tab Not Paired.
- Kombinasi role x elemen tanpa TC sumber, dilaporkan sebagai usulan TC baru untuk QA: menu baris baris Paired untuk Read Only, Manage TAG (Read), dan Manage TAG (Update); toolbar Tab Paired per role.
- Temuan untuk QA:
  - TC-25 langkah 3 (lihat penyimpangan urutan di atas): DD-01 (Paired) tidak ada di Tab Not Paired.
  - TC-26 tidak menyebut `Search by Scan`, `Search`, `Filter`, `Download` pada Expected toolbar (berbeda dengan TC-25 yang menyebut sebagian); spec mengasersi daftar sebagaimana TC.
  - TC-28 butir b tidak menyebut `Delete` Hidden eksplisit (hanya "hanya berisi `TAG Log`"); spec tidak menambah asersi `Delete` Hidden pada blok ini (hanya TC-27 yang menyebutnya).
  - Post Condition semua TC bernilai `-`.
- Alasan spec melewati sekitar 35 langkah (43): empat blok role dalam satu kelas (Role Matrix visibilitas) atas satu dataset; langkah berbeda per role sehingga tidak dapat dipadatkan menjadi perulangan; tiap blok berdiri sendiri dengan ganti akun eksplisit, kegagalan satu blok tidak membuat blok lain kehilangan makna.
