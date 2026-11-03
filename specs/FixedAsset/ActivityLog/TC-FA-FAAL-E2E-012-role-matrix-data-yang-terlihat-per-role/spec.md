---
id: TC-FA-FAAL-E2E-012-role-matrix-data-yang-terlihat-per-role
title: "Role Matrix: Seluruh Baris Kedua Tab untuk Total Control dan Read Only"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-48
  - TC-FA-FAAL-49
  - TC-FA-FAAL-50
  - TC-FA-FAAL-51
coverage:
  web: automated
---

# Role Matrix: Seluruh Baris Kedua Tab untuk Total Control dan Read Only

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

  | TC | Role | Pre-setup | Email | Env var password |
  |---|---|---|---|---|
  | TC-FA-FAAL-48, TC-FA-FAAL-49 | Total Control | #1 | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
  | TC-FA-FAAL-50, TC-FA-FAAL-51 | Read Only | #2 | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |
- Login akun aktor pertama (Total Control, Pre-setup #1) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Setiap ganti akun di tengah spec memakai satu langkah logout dan login eksplisit.
- Env var `FA_TC_PASSWORD` dan `FA_RO_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (R-07). Password tidak ditulis di spec atau fixture.
- Data: Tab Session SS-01 sampai SS-11 (Pre-setup #11, total 11 baris) dan Tab User Action UA-01 sampai UA-15 (Pre-setup #12, total 15 baris), dipulihkan ke keadaan Pre-setup sebelum spec (disediakan tim FE/BE). TC-FA-FAAL-48 sampai 51 memakai baseline Z0 dengan batas bawah. Baris Tab Session berasal dari user pada group berbeda (Gedung A, Gedung B, tanpa group) dan baris Tab User Action dari aksi pada group berbeda. Urutan default Date terbaru di atas dengan 10 baris per halaman: halaman 1 Tab Session berisi SS-11 sampai SS-02.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk kedua akun aktor.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nilai data ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-48: Total Control melihat seluruh baris Tab Session client tanpa filter

1. Klik tab Session
2. Catat total Z0 pada teks pagination tab Session
3. Verifikasi Total Control: teks pagination menampilkan `Showing 1–10 of Z0 entries` dengan Z0 ≥ 11 (SS-01 sampai SS-11 termasuk dalam Z0)
4. Verifikasi Total Control: baris dari semua group tampil
5. Verifikasi Total Control: tidak ada baris yang tersaring oleh group pengguna

### TC-FA-FAAL-49: Total Control melihat seluruh baris Tab User Action client tanpa filter

6. Klik tab User Action
7. Catat total Z0 pada teks pagination tab User Action
8. Verifikasi Total Control: teks pagination menampilkan `Showing 1–10 of Z0 entries` dengan Z0 ≥ 15 (UA-01 sampai UA-15 termasuk dalam Z0)
9. Verifikasi Total Control: baris dari semua modul dan group tampil
10. Verifikasi Total Control: tidak ada baris yang tersaring

### TC-FA-FAAL-50: Read Only melihat seluruh baris Tab Session client tanpa filter

11. Ganti akun: Logout dari akun Total Control, lalu Login sebagai Read Only (`readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_RO_PASSWORD`) dan buka Fixed Asset > Reports & Logs > Activity Log
12. Klik tab Session
13. Catat total Z0 pada teks pagination tab Session
14. Verifikasi Read Only: teks pagination menampilkan `Showing 1–10 of Z0 entries` dengan Z0 ≥ 11 (SS-01 sampai SS-11 termasuk dalam Z0)
15. Verifikasi Read Only: baris dari semua group tampil
16. Verifikasi Read Only: tidak ada baris yang tersaring oleh group pengguna

### TC-FA-FAAL-51: Read Only melihat seluruh baris Tab User Action client tanpa filter

17. Klik tab User Action
18. Catat total Z0 pada teks pagination tab User Action
19. Verifikasi Read Only: teks pagination menampilkan `Showing 1–10 of Z0 entries` dengan Z0 ≥ 15 (UA-01 sampai UA-15 termasuk dalam Z0)
20. Verifikasi Read Only: baris dari semua modul dan group tampil
21. Verifikasi Read Only: tidak ada baris yang tersaring

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec Role Matrix (bagian 3a): data yang terlihat per role. Ditulis per blok role karena ganti akun menuntut langkah eksplisit (akun pertama login di hook `before`, S-07); tiap blok berdiri sendiri.
- Langkah penghubung (S-03): langkah 1, 6, 12, dan 17 (klik tab untuk membuka tab yang diamati TC dengan "Buka tab"), langkah 11 (ganti akun, lalu membuka Activity Log), langkah 2, 7, 13, dan 18 (mencatat baseline Z0 dari teks pagination, TC-FA-FAAL-48 sampai 51 langkah 2).
- Langkah 3, 8, 14, dan 19 membandingkan total dengan Z0 yang dicatat sebelumnya dan batas bawah (Z0 ≥ 11 dan Z0 ≥ 15) seperti Expected TC-FA-FAAL-48 sampai 51.
- Temuan untuk QA:
  - TC-FA-FAAL-48 sampai 51 menyebut baris berasal dari group berbeda (Gedung A, Gedung B, tanpa group) tanpa memetakan baris SS/UA ke group; spec memverifikasi lewat total pagination dan tidak menyebut group per baris.
  - TC-FA-FAAL-48 sampai 51 tidak menyebut env var password; nama env var diusulkan dari butir "Env var" di `suite.md`.
